#!/usr/bin/env python3
"""Daily to-do reminder: parse TODO.md and send a digest via jarvis (notify over ssh to the VPS)."""
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LINE = re.compile(r"^- \[ \] #(\d+) (P[123])(.*?) — (.+?)(?: — why: (.*))?$")
SGT = dt.timezone(dt.timedelta(hours=8))


def parse(text):
    items, in_open = [], False
    for line in text.splitlines():
        if line.startswith("## "):
            in_open = line.strip() == "## Open"
            continue
        m = LINE.match(line.strip()) if in_open else None
        if not m:
            continue
        tags = dict(re.findall(r"(\w+):(\d{4}-\d{2}-\d{2})", m.group(3)))
        items.append({
            "id": int(m.group(1)), "p": m.group(2), "text": m.group(4).strip(),
            "due": dt.date.fromisoformat(tags["due"]) if "due" in tags else None,
            "added": dt.date.fromisoformat(tags["added"]) if "added" in tags else None,
        })
    return items


def fmt(it, today):
    s = f"#{it['id']} [{it['p']}] {it['text']}"
    if it["due"]:
        d = (it["due"] - today).days
        s += f" (逾期 {-d} 天)" if d < 0 else " (今天到期)" if d == 0 else f" ({d} 天后到期 {it['due']:%m-%d})"
    return s


def build(items, today):
    if not items:
        return None
    key = lambda i: (i["p"], i["due"] or dt.date.max, i["id"])
    items = sorted(items, key=key)
    urgent = [i for i in items if i["due"] and (i["due"] - today).days <= 3]
    shown = {i["id"] for i in urgent}
    p1 = [i for i in items if i["p"] == "P1" and i["id"] not in shown]
    shown |= {i["id"] for i in p1}
    p2 = [i for i in items if i["p"] == "P2" and i["id"] not in shown][:3]
    shown |= {i["id"] for i in p2}
    out = [f"📝 To-do {today:%m-%d %a}  共 {len(items)} 项"]
    if urgent:
        out += ["", "⏰ 到期 / 快到期:"] + [fmt(i, today) for i in urgent]
    if p1:
        out += ["", "🔴 P1:"] + [fmt(i, today) for i in p1]
    if p2:
        out += ["", "🟡 P2 前几项:"] + [fmt(i, today) for i in p2]
    rest = [i for i in items if i["id"] not in shown]
    if today.weekday() == 6:  # Sunday: full review
        if rest:
            out += ["", "其余:"] + [fmt(i, today) for i in rest]
        stale = [i for i in items if i["added"] and (today - i["added"]).days >= 14]
        if stale:
            out += ["", "🧹 已放 14 天以上，保留 / 删掉 / 改优先级？"] + [fmt(i, today) for i in stale]
    elif rest:
        out += ["", f"另有 {len(rest)} 项低优先级（周日完整列出）"]
    out += ["", "在 Claude Code 里: /todo done N · /todo 列表"]
    return "\n".join(out)


def main():
    dry = "--dry-run" in sys.argv
    if "--no-pull" not in sys.argv:
        subprocess.run([str(HERE.parent / "sync.sh"), "pull"], check=False)
    today = dt.datetime.now(SGT).date()
    msg = build(parse((HERE / "TODO.md").read_text(encoding="utf-8")), today)
    if msg is None:
        print("no open items, nothing sent")
        return
    if dry:
        print(msg)
        return
    subprocess.run(
        ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=15", "trader@178.105.158.87",
         "cd ~/tech-digest && .venv/bin/python notify_stdin.py"],
        input=msg.encode(), check=True, timeout=60)
    print("sent")


if __name__ == "__main__":
    main()
