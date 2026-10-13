---
name: project-forecast-journal
description: Weekly forecast journal set up 2026-10-12 in ~/lab/forecast-journal so the user can test whether their market judgment beats a baseline
metadata:
  type: project
---

Context: after the Ichimoku/bear-detection discussion the user said bear markets come from structural causes (subprime, housing bubbles) and that reading news and understanding markets may beat data-driven methods; they agreed to a once-a-week routine and said the exercise is essentially training themselves.

Built ~/lab/forecast-journal: journal.csv (id, date_made, question, resolve_date, resolution_source, prob_yes, baseline_prob, reason, action_taken, outcome), score.py (Brier score vs baseline, calibration buckets, flags overdue rows, warns below 30 resolved questions), README.md (rules: write before the event, never edit old rows, yes/no questions with checkable source, short horizons because bear markets are too rare to score). Journal is empty as of 2026-10-12; weekly reminder channel is the Jarvis bot, Saturday 09:00 SGT. Nothing committed to git.
**How to apply:** when the user brings a market view, offer to log it as a row with a probability; when asked, run score.py and report the Brier score vs baseline with the sample size. Related: [[project-ichimoku-spy]], [[feedback-keep-exploring]].

2026-10-12 user request (pending, not implemented): weekly reminder through the Jarvis Telegram bot, submissions through Jarvis, each reminder also chooses a topic and an analysis direction. Full spec in ~/lab/forecast-journal/SPEC_jarvis.md. The user will close the session first; implement in a later session (say "implement the Jarvis reminder"). Reminder time chosen: every Saturday 09:00 Singapore time (UTC+8, Saturday 01:00 UTC). Sessions cannot continue by themselves after closing, so this needs the user to start one.
