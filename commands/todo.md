---
description: Manage my to-do list (~/claude-memory/todo/TODO.md) — add, list, done, edit, review priorities (usage: /todo <thing to do> | /todo | /todo done N)
argument-hint: <new item> | done N | drop N | review | (empty = list)
---

My to-do list lives at ~/claude-memory/todo/TODO.md. Rules and priority definitions are in ~/claude-memory/todo/README.md — read it first. Keep the exact line format described in the comment at the top of TODO.md, because remind.py parses it.

Input: $ARGUMENTS

Run `~/claude-memory/sync.sh pull` first. Then decide what I want:

- **Empty** → show open items grouped by priority (P1, P2, P3), with due dates and days left/overdue. Use today's date in Singapore time (UTC+8).
- **`done N` / `完成 N`** → move item #N to "## Done" as `- [x] ...` with `done:<today>`. Reply with one line.
- **`drop N` / `删 N`** → remove item #N from Open (move to Done with ` (dropped)` after the text), one line reply.
- **`est N 4h` / `due N ...`** → change that item's estimate or due date.
- **`review` / `评估`** → re-assess every open item's priority and estimate against README rules and today's date; propose changes as a short table (id, old → new, reason) and apply only after I agree.
- **Anything else** → a new item (one message may contain several; split them). For each:
  1. Next id = highest id in the file + 1 (across Open and Done).
  2. Rewrite it as a short, concrete action in my language. Extract a due date if I gave one (convert "明天/下周五" to YYYY-MM-DD in SGT). Do not invent deadlines.
  3. Estimate the effort as `est:` (e.g. 30m, 2h, 1d) — realistic for me doing it alone, including setup. If I gave a deadline with a time of day, use `due:YYYY-MM-DDTHH:MM`; date only means end of that day. The reminder sends a last-call when due − est − buffer is reached, so a good estimate matters; if the task is unfamiliar, err on the high side and say so.
  4. Assign P1/P2/P3 by the README rules, with a one-line `why:`. If the priority depends on something I didn't say (e.g. a deadline), pick the most likely one and ask that single question in the reply.
  5. Check for a near-duplicate open item; if found, say so instead of adding twice.
  6. Append under "## Open".
  Reply: the added line(s) with est and, if due is set, the suggested latest start time, then the current top 3 open items. Keep it short — I'm often on my phone.

After any change, run `~/claude-memory/sync.sh push`. Never delete lines outright.
