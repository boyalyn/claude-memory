---
name: feedback-sn101-jarvis-report
description: SN101 emission + ranking must reach the user via Jarvis automatically every epoch (VPS cron jarvis_report.py --auto), plus after every check
metadata:
  type: feedback
---

After each SN101 verification (scheduled or ad-hoc check), send a Jarvis report: `ssh trader@178.105.158.87 'cd ~/sn101 && .venv/bin/python jarvis_report.py "<one-line Chinese conclusion>"'` (script reports emission, relative emission, rank among all miners and same-time registrants, avg-score gap, eviction line, immunity left, last-2h task health; `--dry` prints without sending).

**Why:** user asked on 2026-10-15 01:45 SGT: "sn101每次验证后通过Jarvis汇报emission，排名" — they follow results on the phone.
**How to apply:** do it at the end of every SN101 check, in addition to the chat reply; channel details in [[reference-notification-channel]]; project state in [[project-sn101-prep]].

**2026-10-15 09:40 SGT update:** user: "我需要实时收到，不是我问你的时候收到" — on-demand reports are not enough. VPS cron `*/10 * * * * jarvis_report.py --auto` now pushes once per new epoch (~72 min) with the change vs the previous push (state ~/sn101/jarvis_state.json, log ~/sn101/jarvis_report.log; notify uses check=True so failures show in the log). Keep this cron running whenever an SN101 miner is live; if a new hotkey/UID is used, the script follows hotkey miner2 (HK constant).
