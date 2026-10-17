#!/usr/bin/env python3
"""To-do reminders via jarvis (notify over ssh to the VPS).

  remind.py digest      daily summary (cron 09:03 SGT)
  remind.py lastcall    hourly: alert once when time left before due <= est + buffer
Flags: --dry-run (print, don't send), --no-pull (skip git pull), --now=YYYY-MM-DDTHH:MM (SGT, testing).
"""
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE = Path.home() / ".claude" / "todo-alerts.json"  # local, not synced: which last-calls were sent
LINE = re.compile(r"^- \[ \] #(\d+) (P[123])(.*?) — (.+?)(?: — why: (.*))?$")
SGT = dt.timezone(dt.timedelta(hours=8))
QUIET_START, QUIET_END = 23, 8  # no last-call messages 23:00-08:00 SGT
DEFAULT_EST = dt.timedelta(hours=1)
# nag:on items, extra reminders on top of the 09:03 digest, by days left until due (SGT hours):
NAG_FROM_DAYS = 4                    # start this many days before the due date
NAG_EARLY_HOURS = {20}               # 2-4 days left
NAG_LATE_HOURS = {12, 15, 18, 21}    # 1 day left, due day, and every day while overdue


def parse_est(s):
    m = re.fullmatch(r"(\d+(?:\.\d+)?)(m|h|d)", s)
    if not m:
        return None
    n, u = float(m.group(1)), m.group(2)
    return dt.timedelta(minutes=n) if u == "m" else dt.timedelta(hours=n) if u == "h" else dt.timedelta(hours=8 * n)


def parse(text):
    items, in_open = [], False
    for line in text.splitlines():
        if line.startswith("## "):
            in_open = line.strip() == "## Open"
            continue
        m = LINE.match(line.strip()) if in_open else None
        if not m:
            continue
        tags = dict(re.findall(r"(\w+):(\S+)", m.group(3)))
        due = None
        if "due" in tags:  # due:YYYY-MM-DD (= 23:59 SGT) or due:YYYY-MM-DDTHH:MM
            v = tags["due"]
            due = dt.datetime.fromisoformat(v if "T" in v else v + "T23:59").replace(tzinfo=SGT)
        items.append({
            "id": int(m.group(1)), "p": m.group(2), "text": m.group(4).strip(), "due": due,
            "est": parse_est(tags.get("est", "")) or DEFAULT_EST, "has_est": "est" in tags,
            "added": dt.date.fromisoformat(tags["added"]) if "added" in tags else None,
            "nag": tags.get("nag") == "on", "repeat": tags.get("repeat"),
        })
    return items


def buffer(est):
    """Slack on top of the estimate: things take longer than planned."""
    return max(dt.timedelta(hours=1), est / 2)


def alert_time(it):
    """Last moment to start (due - est - buffer), pulled earlier out of quiet hours to 22:00."""
    t = it["due"] - it["est"] - buffer(it["est"])
    if t.hour >= QUIET_START or t.hour < QUIET_END:
        day = t.date() if t.hour >= QUIET_START else t.date() - dt.timedelta(days=1)
        t = dt.datetime.combine(day, dt.time(QUIET_START - 1), SGT)
    return t


def human(td):
    if td < dt.timedelta(hours=1):
        return f"{max(1, round(td.total_seconds() / 60))} 分钟"
    return f"{round(td.total_seconds() / 1800) / 2:g} 小时"  # nearest half hour


def fmt(it, now):
    s = f"#{it['id']} [{it['p']}] {it['text']}"
    if it["has_est"]:
        s += f" ~{human(it['est'])}"
    if it["due"]:
        d = (it["due"].date() - now.date()).days
        when = it["due"].strftime("%m-%d" if it["due"].time() == dt.time(23, 59) else "%m-%d %H:%M")
        s += (f" (逾期 {-d} 天)" if d < 0 else " (已过截止)") if it["due"] < now else " (今天到期)" if d == 0 else f" ({d} 天后 {when})"
    return s


def digest(items, now):
    if not items:
        return None
    today = now.date()
    items = sorted(items, key=lambda i: (i["p"], i["due"] or dt.datetime.max.replace(tzinfo=SGT), i["id"]))
    urgent = [i for i in items if i["due"] and (i["due"].date() - today).days <= 3]
    shown = {i["id"] for i in urgent}
    p1 = [i for i in items if i["p"] == "P1" and i["id"] not in shown]
    shown |= {i["id"] for i in p1}
    p2 = [i for i in items if i["p"] == "P2" and i["id"] not in shown][:3]
    shown |= {i["id"] for i in p2}
    out = [f"📝 To-do {today:%m-%d %a}  共 {len(items)} 项"]
    if urgent:
        lines = []
        for i in urgent:
            line = fmt(i, now)
            if i["due"] > now:
                line += f"\n   建议最晚 {alert_time(i):%m-%d %H:%M} 开始"
            lines.append(line)
        out += ["", "⏰ 到期 / 快到期:"] + lines
    if p1:
        out += ["", "🔴 P1:"] + [fmt(i, now) for i in p1]
    if p2:
        out += ["", "🟡 P2 前几项:"] + [fmt(i, now) for i in p2]
    rest = [i for i in items if i["id"] not in shown]
    if today.weekday() == 6:  # Sunday: full review
        if rest:
            out += ["", "其余:"] + [fmt(i, now) for i in rest]
        stale = [i for i in items if i["added"] and (today - i["added"]).days >= 14]
        try:
            import calibrate
            cal = [line for _, line in calibrate.summary()[0]]
        except Exception as e:  # never let calibration break the digest
            cal = [f"(calibration error: {e})"]
        if cal:
            out += ["", "⏱ 你的实际用时 / 预估（按类别）:"] + [c.split(" → ")[0] for c in cal]
        if stale:
            out += ["", "🧹 已放 14 天以上，保留 / 删掉 / 改优先级？"] + [fmt(i, now) for i in stale]
    elif rest:
        out += ["", f"另有 {len(rest)} 项低优先级（周日完整列出）"]
    out += ["", "在 Claude Code 里: /todo done N · /todo 列表"]
    return "\n".join(out)


def lastcall(items, now, sent):
    """Messages for items whose alert time has passed and that weren't alerted for this due+est yet."""
    if (now.hour >= QUIET_START or now.hour < QUIET_END):
        return [], sent
    msgs, keep = [], {}
    for it in items:
        if not it["due"]:
            continue
        key = f"{it['id']}|{it['due'].isoformat()}|{it['est']}"
        if key in sent:
            keep[key] = sent[key]
            continue
        if alert_time(it) <= now < it["due"]:
            left = it["due"] - now
            if left >= it["est"]:
                tail = f"还剩 {human(left)}，预计要 {human(it['est'])}，现在开始还来得及。"
            else:
                tail = f"只剩 {human(left)}，预计要 {human(it['est'])}，已经很紧了——先做最关键的部分，或者想办法延期。"
            msgs.append(f"⚠️ 最后提醒 #{it['id']} [{it['p']}] {it['text']}\n截止 {it['due']:%m-%d %H:%M}，{tail}\n做完回 /todo done {it['id']}")
            keep[key] = now.isoformat()
    nags = []
    for it in items:
        if not (it["nag"] and it["due"]):
            continue
        d = (it["due"].date() - now.date()).days
        hours = NAG_LATE_HOURS if d <= 1 else NAG_EARLY_HOURS if d <= NAG_FROM_DAYS else set()
        key = f"nag|{it['id']}|{now:%Y-%m-%dT%H}"
        if key in sent:
            keep[key] = sent[key]
        elif now.hour in hours:
            when = "已逾期！" if it["due"] < now else "今天截止" if d == 0 else f"还有 {d} 天（{it['due']:%m-%d} 截止）"
            nags.append(f"#{it['id']} {it['text']} — {when}")
            keep[key] = now.isoformat()
    if nags:
        msgs.append("🔔 还没标记完成:\n" + "\n".join(nags) + "\n做完回 /todo done N（不标记会一直提醒）")
    return msgs, keep


def send(msg):
    subprocess.run(
        ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=15", "trader@178.105.158.87",
         "cd ~/tech-digest && .venv/bin/python notify_stdin.py"],
        input=msg.encode(), check=True, timeout=60)


def main():
    args = sys.argv[1:]
    mode = next((a for a in args if not a.startswith("--")), "digest")
    dry = "--dry-run" in args
    now_arg = next((a.split("=", 1)[1] for a in args if a.startswith("--now=")), None)
    now = dt.datetime.fromisoformat(now_arg).replace(tzinfo=SGT) if now_arg else dt.datetime.now(SGT)
    if "--no-pull" not in args:
        subprocess.run([str(HERE.parent / "sync.sh"), "pull"], check=False)
    items = parse((HERE / "TODO.md").read_text(encoding="utf-8"))

    if mode == "digest":
        msgs = [m for m in [digest(items, now)] if m]
    else:
        sent = json.loads(STATE.read_text()) if STATE.exists() else {}
        msgs, new_state = lastcall(items, now, sent)
    for m in msgs:
        print(m) if dry else send(m)
    if mode == "lastcall" and not dry:
        STATE.write_text(json.dumps(new_state, indent=1))
    print(f"{now:%m-%d %H:%M} {mode}: {len(msgs)} message(s){' (dry run)' if dry else ' sent'}")


if __name__ == "__main__":
    main()
