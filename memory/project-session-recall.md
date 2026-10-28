---
name: project-session-recall
description: "Cross-session recall (Muse-style memory, new session per topic): auto session digests, SessionStart injection of recent sessions + open items, recall.py search; where it lives, how to change it"
metadata:
  node_type: memory
  type: project
  originSessionId: 7492eea6-754a-5501-b58e-89a88afed03c
  modified: 2026-10-28T13:07:47.399Z
---

Built 2026-10-28 at the user's request after trying Meta's Muse: they like opening a new session per topic but want later sessions to know what earlier ones discussed. Not a single-thread design (user rejected copying that).

- Code: ~/claude-memory/recall/ (synced). `digest.py` summarises finished sessions (transcript idle ≥30 min; re-digested if resumed) via `claude -p --model sonnet` with no tools, no user hooks (`--setting-sources local`), `--no-session-persistence`; prompt in `digest_prompt.md`. Output: ~/claude-memory/sessions/YYYY-MM-DD_<sid8>.md + INDEX.md; pushes with sync.sh after writing. State (local): ~/.claude/session-digest-state.json; log ~/.claude/session-digest.log. Skips project folder `-tmp` and sessions under 500 chars (scripted one-shots).
- Cron (boya-server): `*/30 * * * *` digest.py, max 10 sessions per run (spreads the Pro allowance). Backfill of ~40 old sessions started 2026-10-28.
- SessionStart hook (boya-server ~/.claude/settings.json): `sync.sh pull; recent.py` → injects last 14 days (≤15 sessions) + ≤8 open items. The Mac's settings.json is NOT updated yet, and Mac transcripts are not digested.
- Search: `python3 ~/claude-memory/recall/recall.py <words>` (digests, then raw transcripts; `--raw` forces both).
- `cleanupPeriodDays: 3650` set 2026-10-28 (default 30 would have deleted transcripts from 10-06 around 11-05).
- Dry-run result 2026-10-28 (2 sessions): Haiku with the first prompt invented a user decision ("改用 condo 健身房"); Haiku also used ~7-11k thinking tokens per digest. Sonnet with the grounded prompt quoted user decisions with correct timestamps; chosen as default. Only 2 sessions were spot-checked.
- Known gaps: open items are not auto-closed when a later session resolves them (14-day window only); digests are model-written, verify details against the original before relying on them.

Related: [[reference-memory-sync]], design notes in ~/claude-memory/DESIGN.md §12.
