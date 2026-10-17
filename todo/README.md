# To-do list rules

- Data: `TODO.md` (synced through this repo). Add/edit via `/todo` in Claude Code, or by hand in the same format.
- Priority:
  - **P1** — has a deadline within ~7 days, or a real cost (money, penalty, missed chance) if late.
  - **P2** — matters but no near deadline.
  - **P3** — nice to have; can wait or be dropped.
- Reminders (`remind.py`, cron on boya-server, sent by jarvis on Telegram):
  - Every day 09:03 SGT: overdue items, items due in the next 3 days, all P1, top 3 P2, and a count of the rest. Nothing sent if the list is empty.
  - Sunday: full open list plus items open for 14+ days, asking keep / drop / re-prioritise.
