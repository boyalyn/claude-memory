#!/usr/bin/env python3
"""Print recent sessions and their open items. Run by the SessionStart hook; stdout goes into Claude's context.

  recent.py                 last DAYS days from ~/claude-memory/sessions
  recent.py --dir /tmp/x    another digest folder (testing)
Keep the output small: it is paid for on every call of every session.
"""
import datetime as dt
import re
import sys
from pathlib import Path

SESSIONS = Path(__file__).resolve().parent.parent / "sessions"
SGT = dt.timezone(dt.timedelta(hours=8))
DAYS = 14
MAX_SESSIONS = 15
MAX_OPEN = 8


def main(argv):
    folder = Path(argv[argv.index("--dir") + 1]) if "--dir" in argv else SESSIONS
    if not folder.is_dir():
        return
    cutoff = (dt.datetime.now(SGT) - dt.timedelta(days=DAYS)).strftime("%Y-%m-%d")
    files = sorted((f for f in folder.glob("20*.md") if f.name[:10] >= cutoff), reverse=True)
    if not files:
        return
    lines, open_items = [], []
    for f in files[:MAX_SESSIONS]:
        t = f.read_text(encoding="utf-8")
        title = re.search(r"^# (.+)$", t, re.M)
        one = re.search(r"^ONE_LINE:\s*(.+)$", t, re.M)
        title = title.group(1) if title else f.stem
        lines.append(f"- {f.name[5:10]} {title} — {one.group(1) if one else ''}")
        for item in re.findall(r"^- \[ \] (.+)$", t, re.M):
            open_items.append(f"- [ ] {item} （{f.name[5:10]} {title}）")
    print(f"## 最近 {DAYS} 天的会话（自动摘要，sessions/INDEX.md；摘要由 model 生成，细节以原文为准）")
    print("\n".join(lines))
    if open_items:
        print("\n## 当时没收尾的事（后来的会话可能已处理；相关时向用户确认，别每次都提）")
        print("\n".join(open_items[:MAX_OPEN]))
    print("\n用户提到以前的事时，先查：python3 ~/claude-memory/recall/recall.py <关键词>")


if __name__ == "__main__":
    main(sys.argv[1:])
