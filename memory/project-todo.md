---
name: project-todo
description: "/todo command + daily Telegram reminder: where the list lives, format, cron, how to change frequency"
metadata:
  type: project
---

Set up 2026-10-17 at the user's request (they keep forgetting things).
- Data: ~/claude-memory/todo/TODO.md (synced). Rules/priority definitions: todo/README.md (P1 = deadline ≤~7 days or real cost if late; P2 = matters, no near deadline; P3 = nice to have).
- Command: ~/claude-memory/commands/todo.md, symlinked at ~/.claude/commands/todo.md on boya-server. The Mac needs the same symlink (not done as of 2026-10-17).
- Reminder: todo/remind.py, boya-server crontab: `remind.py digest` at `3 1 * * *` UTC = 09:03 SGT daily, `remind.py lastcall` hourly at :07; each run pulls the repo, sends via jarvis (ssh trader@VPS notify_stdin.py); nothing sent if list empty; Sunday adds full list + items open ≥14 days. Log: ~/.claude/todo-remind.log. `--dry-run`, `--no-pull` flags for testing.
- Last-call (user request 2026-10-17: warn early enough to still finish): items carry `est:`; alert once at due − est − max(1h, est/2), none 23:00–08:00 SGT (moved to 22:00 the night before); state ~/.claude/todo-alerts.json. `--now=` flag for testing.
- Time learning (user request 2026-10-17): items carry `cat:`; on done, record `actual:` and a row in todo/TIME-LOG.md, run todo/calibrate.py → regenerates [[user-time-estimates]] (median actual/est per category; applied to new estimates once n≥3). Sunday digest shows the numbers.
- `nag:on` (repeated reminders: 20:00 from 4 days before due, then 12/15/18/21 from the day before until done) and `repeat:monthly` (next copy added on done) added 2026-10-17 for the user's monthly credit-card payments (Trust + Citi, before the 6th; items due the 5th).
- Frequency was Claude's choice (once a day); user said "你看着办". Change it if the user asks.
- Items added on the Mac reach the reminder only after that session's SessionEnd push.
