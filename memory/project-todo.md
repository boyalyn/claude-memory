---
name: project-todo
description: "/todo command + daily Telegram reminder: where the list lives, format, cron, how to change frequency"
metadata:
  type: project
---

Set up 2026-10-17 at the user's request (they keep forgetting things).
- Data: ~/claude-memory/todo/TODO.md (synced). Rules/priority definitions: todo/README.md (P1 = deadline ≤~7 days or real cost if late; P2 = matters, no near deadline; P3 = nice to have).
- Command: ~/claude-memory/commands/todo.md, symlinked at ~/.claude/commands/todo.md on boya-server. The Mac needs the same symlink (not done as of 2026-10-17).
- Reminder: todo/remind.py, boya-server crontab `3 1 * * *` UTC = 09:03 SGT daily; pulls the repo, sends via jarvis (ssh trader@VPS notify_stdin.py); nothing sent if list empty; Sunday adds full list + items open ≥14 days. Log: ~/.claude/todo-remind.log. `--dry-run`, `--no-pull` flags for testing.
- Frequency was Claude's choice (once a day); user said "你看着办". Change it if the user asks.
- Items added on the Mac reach the reminder only after that session's SessionEnd push.
