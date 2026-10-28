#!/usr/bin/env python3
"""Write a short digest of each finished Claude Code session into ~/claude-memory/sessions/.

A session counts as finished when its transcript has not changed for IDLE_MIN minutes.
A session that is resumed later is digested again (same file, overwritten).
Each digest is one model call (MODEL) through `claude -p` (the logged-in subscription, no API key).

  digest.py                         digest finished sessions that are new or changed (cron)
  digest.py --dry-run --limit 5     write to /tmp/session-digest-dry, leave state and repo alone
  digest.py --session 903311cb      one session by id prefix (skips the idle check)
Flags: --limit N (default 10 per run, 0 = no limit), --model haiku|sonnet (default MODEL),
       --no-push (skip sync.sh push after writing digests).
"""
import datetime as dt
import fcntl
import json
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
SESSIONS = REPO / "sessions"
PROMPT_FILE = HERE / "digest_prompt.md"
PROJECTS = Path.home() / ".claude" / "projects"
STATE = Path.home() / ".claude" / "session-digest-state.json"  # local, not synced: what was digested
LOCK = Path.home() / ".claude" / "session-digest.lock"
WORKDIR = Path.home() / ".cache" / "session-digest"  # neutral cwd for claude -p
DRY_DIR = Path("/tmp/session-digest-dry")
CLAUDE = Path.home() / ".local" / "bin" / "claude"
SGT = dt.timezone(dt.timedelta(hours=8))
MODEL = "sonnet"   # 2026-10-28 dry-run: Haiku over-read user decisions and spent ~10k thinking tokens per digest

IDLE_MIN = 30
SKIP_PROJECTS = {"-tmp"}           # scratch workspaces
MAX_USER_CHARS = 3000              # per message, head kept
MAX_ASSISTANT_CHARS = 1500
MAX_TOTAL_CHARS = 80000            # whole conversation: head + tail kept
HEAD_CHARS = 15000
MIN_USER_MSGS = 1
MIN_CHARS = 500                    # below this it is a scripted one-shot (e.g. flight-watch cron), not a conversation

# User-message wrappers that are not the user's words.
NOISE_PREFIXES = ("<task-notification>", "<local-command-caveat>", "<local-command-stdout>",
                  "<local-command-stderr>", "Caveat:")
SYSTEM_REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
COMMAND = re.compile(r"<command-name>(.*?)</command-name>.*?(?:<command-args>(.*?)</command-args>)?", re.S)

SECRET_PATTERNS = [
    re.compile(r"sk-ant-[A-Za-z0-9_\-]{10,}"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}"),
    re.compile(r"\b\d{8,10}:[A-Za-z0-9_\-]{30,}"),        # Telegram bot token
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"(?i)\b(token|secret|password|passwd|api[_-]?key)\b(\s*[:=]\s*)\S+"),
]
LONG_BLOB = re.compile(r"[A-Za-z0-9_\-+=]{32,}")


# ---------- transcripts ----------

def find_transcripts():
    for d in sorted(PROJECTS.iterdir()):
        if d.is_dir() and d.name not in SKIP_PROJECTS:
            yield from sorted(d.glob("*.jsonl"))


def project_label(path):
    """'-home-boya-lab-news-etf' -> 'lab/news-etf'."""
    name = path.parent.name
    home = "-" + str(Path.home()).strip("/").replace("/", "-") + "-"
    return name[len(home):].replace("lab-", "lab/", 1) if name.startswith(home) else name


def to_sgt(ts):
    return dt.datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(SGT)


def clean_user_text(text):
    text = SYSTEM_REMINDER.sub("", text).strip()
    if text.startswith(NOISE_PREFIXES):
        return ""
    m = COMMAND.search(text)
    if m and text.startswith("<command-"):
        return f"{m.group(1)} {m.group(2) or ''}".strip()
    return text


def cut(text, limit):
    return text if len(text) <= limit else text[:limit] + " …[cut]"


def extract(path):
    """Return (turns, meta). turns = [(sgt_time, role, text)], user/assistant words only."""
    turns, first, last = [], None, None
    for line in path.open(encoding="utf-8", errors="replace"):
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        if e.get("isSidechain") or e.get("type") not in ("user", "assistant"):
            continue
        ts = e.get("timestamp")
        when = to_sgt(ts) if ts else None
        if when:
            first, last = first or when, when
        msg = e.get("message") or {}
        content = msg.get("content") if isinstance(msg, dict) else None
        if e["type"] == "user":
            if e.get("isCompactSummary"):
                text = "[earlier part, summarised] " + (content if isinstance(content, str) else "")
                turns.append((when, "summary", cut(text, MAX_USER_CHARS * 2)))
                continue
            if isinstance(content, str):
                text = clean_user_text(content)
            elif isinstance(content, list):
                parts = []
                for c in content:
                    if not isinstance(c, dict):
                        continue
                    if c.get("type") == "text":
                        parts.append(clean_user_text(c.get("text", "")))
                    elif c.get("type") == "image":
                        parts.append("[image]")
                text = "\n".join(p for p in parts if p)
            else:
                text = ""
            if text:
                turns.append((when, "user", cut(text, MAX_USER_CHARS)))
        else:
            parts = [c.get("text", "") for c in content or [] if isinstance(c, dict) and c.get("type") == "text"]
            text = "\n".join(p for p in parts if p.strip())
            if text:
                turns.append((when, "assistant", cut(text, MAX_ASSISTANT_CHARS)))
    meta = {"start": first, "end": last, "n_user": sum(1 for t in turns if t[1] == "user")}
    return turns, meta


def render(turns):
    lines = []
    for when, role, text in turns:
        stamp = when.strftime("%m-%d %H:%M") if when else "?"
        lines.append(f"[{stamp}] {role.upper()}: {text}")
    full = "\n\n".join(lines)
    if len(full) > MAX_TOTAL_CHARS:
        tail = MAX_TOTAL_CHARS - HEAD_CHARS
        full = full[:HEAD_CHARS] + "\n\n…[middle of conversation omitted]…\n\n" + full[-tail:]
    return full


# ---------- summarising ----------

def scrub(text):
    for p in SECRET_PATTERNS:
        text = p.sub(lambda m: (m.group(1) + m.group(2) + "[redacted]") if m.re.groups == 2 else "[redacted]", text)
    # long random-looking strings (upper + lower + digits); keeps file names, snake_case and hex hashes
    def blob(m):
        s = m.group(0)
        random_like = re.search(r"[A-Z]", s) and re.search(r"[a-z]", s) and re.search(r"\d", s)
        return "[redacted]" if random_like else s
    return LONG_BLOB.sub(blob, text)


def call_model(system_prompt, conversation, model):
    WORKDIR.mkdir(parents=True, exist_ok=True)
    cmd = [str(CLAUDE), "-p", "--model", model, "--output-format", "json",
           "--setting-sources", "local",          # no user hooks (memory sync) for this call
           "--tools", "", "--strict-mcp-config", "--disable-slash-commands",
           "--no-session-persistence",            # the call itself must not become a transcript
           "--system-prompt", system_prompt]
    r = subprocess.run(cmd, input=conversation, capture_output=True, text=True, cwd=WORKDIR, timeout=300)
    try:
        out = json.loads(r.stdout)
    except json.JSONDecodeError:
        raise RuntimeError(f"claude -p failed (exit {r.returncode}): {(r.stderr or r.stdout)[:300]}")
    if out.get("is_error"):
        raise RuntimeError(f"claude -p error: {str(out.get('result'))[:300]}")
    return out["result"].strip(), out.get("usage", {})


def digest_file_name(meta, sid):
    day = meta["start"].strftime("%Y-%m-%d") if meta["start"] else "unknown"
    return f"{day}_{sid[:8]}.md"


def build_digest(path, sid, turns, meta, system_prompt, model=MODEL):
    span = ""
    if meta["start"]:
        span = f"{meta['start']:%Y-%m-%d %H:%M}–{meta['end']:%m-%d %H:%M} SGT"
    header_for_model = (f"Project: {project_label(path)}\nSession time: {span}\n"
                        f"User messages: {meta['n_user']}\n\n--- conversation ---\n\n")
    body, usage = call_model(system_prompt, scrub(header_for_model + render(turns)), model)
    body = scrub(body)
    title_m = re.search(r"^TITLE:\s*(.+)$", body, re.M)
    title = title_m.group(1).strip() if title_m else "(no title)"
    body = re.sub(r"^TITLE:.*\n?", "", body, count=1, flags=re.M).strip()
    text = (f"# {title}\n\n"
            f"- session: `{sid}` · project: {project_label(path)} · {span} · 用户消息 {meta['n_user']} 条\n\n"
            f"{body}\n")
    return text, usage


# ---------- index ----------

def rebuild_index(folder):
    """INDEX.md: one line per session, newest first. Read by the SessionStart hook and by recall.py."""
    rows = []
    for f in folder.glob("20*.md"):
        t = f.read_text(encoding="utf-8")
        title = re.search(r"^# (.+)$", t, re.M)
        one = re.search(r"^ONE_LINE:\s*(.+)$", t, re.M)
        proj = re.search(r"project: ([^ ·]+)", t)
        open_items = len(re.findall(r"^- \[ \] ", t, re.M))
        rows.append((f.name, f"- {f.name[:10]} [{proj.group(1) if proj else '?'}] "
                              f"{title.group(1) if title else f.stem} — {one.group(1) if one else ''}"
                              f"{f' (未收尾 {open_items})' if open_items else ''} → sessions/{f.name}"))
    rows.sort(reverse=True)
    (folder / "INDEX.md").write_text("# 会话摘要索引（自动生成，勿手改）\n\n" + "\n".join(r for _, r in rows) + "\n",
                                     encoding="utf-8")


# ---------- main ----------

def main(argv):
    dry = "--dry-run" in argv
    limit = 10
    only = None
    model = MODEL
    for a in argv:
        if a.startswith("--limit"):
            limit = int(a.split("=", 1)[1]) if "=" in a else int(argv[argv.index(a) + 1])
        if a.startswith("--model"):
            model = a.split("=", 1)[1] if "=" in a else argv[argv.index(a) + 1]
        if a.startswith("--session"):
            only = a.split("=", 1)[1] if "=" in a else argv[argv.index(a) + 1]

    lock = LOCK.open("w")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        print("another digest run is active; exiting")
        return

    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    out_dir = DRY_DIR if dry else SESSIONS
    out_dir.mkdir(parents=True, exist_ok=True)
    system_prompt = PROMPT_FILE.read_text(encoding="utf-8")

    todo = []
    now = time.time()
    for path in find_transcripts():
        sid = path.stem
        st = path.stat()
        if only:
            if sid.startswith(only):
                todo.append((st.st_mtime, path))
            continue
        if now - st.st_mtime < IDLE_MIN * 60:
            continue                                   # still active
        prev = state.get(sid)
        if prev and prev.get("size") == st.st_size:
            continue                                   # unchanged since last digest
        todo.append((st.st_mtime, path))
    todo.sort(reverse=True)                            # newest first
    if limit:
        todo = todo[:limit]

    done = 0
    for _, path in todo:
        sid = path.stem
        size = path.stat().st_size
        turns, meta = extract(path)
        if meta["n_user"] < MIN_USER_MSGS or not meta["start"] or len(render(turns)) < MIN_CHARS:
            if not dry:
                state[sid] = {"size": size, "status": "skipped-short"}
            print(f"skip {sid[:8]} (too short)")
            continue
        try:
            text, usage = build_digest(path, sid, turns, meta, system_prompt, model)
        except Exception as ex:                        # keep going; retried next run
            print(f"FAIL {sid[:8]}: {ex}")
            continue
        name = (state.get(sid) or {}).get("file") or digest_file_name(meta, sid)
        (out_dir / name).write_text(text, encoding="utf-8")
        if not dry:
            state[sid] = {"size": size, "status": "ok", "file": name,
                          "digested_at": dt.datetime.now(SGT).isoformat(timespec="seconds")}
        done += 1
        inp = sum(usage.get(k, 0) for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens"))
        think = (usage.get("output_tokens_details") or {}).get("thinking_tokens", 0)
        print(f"ok   {sid[:8]} -> {out_dir / name}  ({model}: in {inp} / out {usage.get('output_tokens')} tokens, thinking {think})")

    if done:
        rebuild_index(out_dir)
    if not dry:
        STATE.write_text(json.dumps(state, indent=1))
        if done and "--no-push" not in argv:
            subprocess.run([str(REPO / "sync.sh"), "push"])   # so the Mac sees new digests without waiting for a SessionEnd
    print(f"{dt.datetime.now(SGT):%Y-%m-%d %H:%M} digested {done} of {len(todo)} candidates")


if __name__ == "__main__":
    main(sys.argv[1:])
