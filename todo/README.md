# To-do list rules

- Data: `TODO.md` (synced through this repo). Add/edit via `/todo` in Claude Code, or by hand in the same format.
- Priority:
  - **P1** — has a deadline within ~7 days, or a real cost (money, penalty, missed chance) if late.
  - **P2** — matters but no near deadline.
  - **P3** — nice to have; can wait or be dropped.
- Reminders (`remind.py`, cron on boya-server, sent by jarvis on Telegram):
  - Every day 09:03 SGT: overdue items, items due in the next 3 days, all P1, top 3 P2, and a count of the rest. Nothing sent if the list is empty.
  - Hourly (:07) last-call check: for items with a due time, one alert when it is time to start =
    due − est − buffer (buffer = max(1h, est/2)). No last-calls 23:00–08:00 SGT; an alert that would land
    there is moved to 22:00 the evening before. Sent once per item (re-sent if due or est changes).
    State: ~/.claude/todo-alerts.json (local).
  - Sunday: full open list plus items open for 14+ days, asking keep / drop / re-prioritise.

## Time tracking (learning how long things take me)

- Each item has `cat:` — one of: `admin` (forms, bills, bookings), `writing` (reports, docs, essays), `coding`,
  `study` (reading, courses, research), `errand` (going somewhere, buying), `chores` (home), `comms` (emails, calls, messages), `other`.
- When I report something done, record the actual time (`actual:`), and add a row to `TIME-LOG.md`.
- `calibrate.py` turns TIME-LOG.md into `memory/user-time-estimates.md`: per category, the median of actual/est.
  Once a category has ≥3 samples, new estimates in that category are multiplied by that median.
- Sunday digest includes the current per-category numbers.
