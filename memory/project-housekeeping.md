---
name: project-housekeeping
description: "Weekly read-only housekeeping report of both servers (cron, services, repos, logs) — option A; how to act on it; what was cleaned 2026-10-17"
metadata:
  type: project
---

User asked 2026-10-17 for regular cleanup of all scheduled jobs on boya-server + VPS (errors, conflicts, useless jobs, push all code).
- Chosen option A: `~/lab/deploy/housekeeping/weekly_report.py` (boya-server cron `53 1 * * 0` UTC = Sun 09:53 SGT) runs `inventory.sh` (read-only), saves `reports/<date>.md` (gitignored), sends flags to jarvis. When the user says "处理周检", read the latest report, fix/propose, commit and push. An unattended `claude -p` with commit/push rights was blocked by the auto-mode classifier ("Create Unsafe Agents"); option B (user grants that permission) not chosen.
- Never auto-touch trading (agent/bot/opend/forward-daily), network/access (xray, tailscale, funnel, claude-rc), wallets.
- Done 2026-10-17 with user OK: stopped+disabled user unit sn101-judge (unit file kept; `systemctl --user enable --now sn101-judge` to restore); removed VPS cron chain_snapshot.py (backup ~/crontab.bak.202610171217 on VPS); pushed nasdaq-event-agent (feature/forward-paper-test) and tech-digest (main).
- ~/lab repo has NO remote yet (as of 2026-10-17); code committed locally only (.gitignore excludes data, .env, venvs, nested repos). User will create a GitHub repo and tell the name (to-do #12). insider-signals-mcp has no commits/remote either.
- Third-party clones ignored by the report: subnets/tag101, subnets/bittensor-conversation-genome-project, VPS ~/data-universe.
- git identity for commits: boya <li0003ya@e.ntu.edu.sg> (set per repo; tech-digest lacked it).
