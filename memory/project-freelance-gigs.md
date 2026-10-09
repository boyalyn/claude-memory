---
name: project-freelance-gigs
description: "Freelancer.com outsourcing side income (started 2026-10-09): gig-scout scanner, /propose command, daily playbook refresh, delivery packager, rules we agreed, what is unverified"
metadata:
  node_type: memory
  type: project
  originSessionId: 6f36d8cc-e1b4-5338-aa2d-12a77e639704
  modified: 2026-10-09T09:56:42.671Z
---

Started 2026-10-09 after the user asked whether outsourced dev work could be taken on automatically. Goal is income, see [[feedback-goal-money-or-abandon]]. The user registered a Freelancer.com worker account on 2026-10-09 and placed bids on two jobs (Wayback extraction, Telegram CS bot); outcomes not known yet. NTU email does not mean the user is a student (they are not); their Singapore work-permit status was not confirmed.

**What exists** (code in `/home/boya/lab/gig-scout`, committed in the lab repo; `/propose` is in the separate `tech-digest` repo):
- `gig_scout/cli.py` scans Freelancer (public API, no login) and GitHub "💎 Bounty" issues, filters, dedupes, and sends new matches to the "jarvis" Telegram bot ([[reference-notification-channel]]). Runs on the VPS via `trader` cron `7,37 * * * *` (every 30 min since 2026-10-09; was every 3 h) (`~/gig-scout/run.sh`, reads `~/tech-digest/.env`). Manual run: `ssh trader@178.105.158.87 '~/gig-scout/run.sh'`, or locally `GIG_SCOUT_STATE=/tmp/gs.json python3 -m gig_scout.cli --dry-run --limit 40`. The first real Telegram send had not been observed as of 2026-10-09.
- Filter: Freelancer posts must be at most 3 h old with at most 15 bids (new-account edge is speed; checked 2026-10-09: many earlier suggestions already had 97-340 bids, and the few-bid posts were undoable or underpriced); fixed price, English, dev keywords, a blocklist of topics judged not doable (Power Automate, Cabinet Vision, audiobook TTS, traffic bots, Quotex, data entry, copywriting); Freelancer floor lowered 50 -> 10 USD for cold start (raise back to 50 after about 5 good reviews), cap 500; GitHub cap 1500. SecureBananaLabs bounty repo is blocklisted (every issue tagged $780). Algora has no public API; its bounties are the GitHub label.
- `/propose <freelancer link>` in the jarvis bot (tech_digest/propose.py): reads the project by `seo_urls[]`, runs `claude -p` with no tools, returns verdict GO/MAYBE/SKIP, bid, proposal. Steered by `~/tech-digest/data/propose_profile.md` (optional) and `propose_playbook.md`.
- Daily job `gig_scout/daily.py` via cron `23 4 * * *` (`run_daily.sh`): samples closed projects, rewrites the playbook with Claude, keeps history in `data/playbook_history/`, pings Telegram. It learns from client-side data only.
- `gig_scout/deliver.py PROJECT_DIR --client --title --run`: clean zip (drops .env, .git, __pycache__), blocks on likely secrets (line marker `nosecret` exempts), warns on missing README/deps/sample output, writes a delivery message. Added 2026-10-09. Scanner alerts now show bid count, age and a ready `/propose <url>` line. As of 2026-10-09 deliver.py and these filter changes were not yet committed.
- Restarting the chat service: `trader` has no sudo, but the unit has `Restart=always`, so killing the python process restarts it. Do not `pkill -f tech_digest.chat` inside an ssh command (it matches the ssh shell).

**Data facts** (7,101 projects sampled by id, 2026-10-09, `gig-scout/analysis/pull.py`):
- Public API shows project text, budget, bid count and award status; other freelancers' bids need login. So winning proposal text has NOT been studied. A personal access token from Freelancer developer settings in the VPS `.env` might allow it; untested.
- About 1/3 of closed dev projects get awarded (27% excluding direct invites; direct invites 85%). Fixed price 36% vs hourly 21%. Budget 50-500 USD about 38% vs 20-25% above 500. Higher bid counts correlate with more awards (selection effect, not advice).
- Clients explicitly banning AI: 0.8% of dev posts, mostly creative work. About 6% explicitly want AI tools. Some posts demand a codeword or format at the start of the proposal and some reject generic or ChatGPT bids.

**Rules agreed with the user:**
- No automated bidding (platform terms risk, new account); the user pastes and sends each bid. The user first said the bot only needs to remind them, then asked for `/propose`.
- No fake/self-dealt orders or reviews. Skip traffic bots, binary-options bots and data-entry jobs.
- Deliver on-platform with milestone payments; usually a zip with README, requirements, sample output, plus a delivery message.
- Commit only when asked ([[feedback-working-style]]).

**Unverified:** Freelancer fee ("10% or minimum $5") and exact UI wording come from general knowledge, not checked in the user's account.

**Freelancer terms (read from https://www.freelancer.com/about/terms on 2026-10-09):** section 33 says users will not use any robot, spider, scraper or other automated means to access the Website, "including for the avoidance of doubt access to our API", for any purpose without Freelancer's express written permission. No clause specifically about bidding was found. So automated bidding (authenticated, tied to the user's account) and, strictly read, our unauthenticated scanner and daily job are both covered. The user asked on 2026-10-09 for automatic bidding; I advised against it and did not build it. Whether the user accepted the scanner risk was not yet decided at the time of writing.

**Decision 2026-10-09:** the user chose to keep the scanner and daily job running (accepting the section-33 risk above, which is mainly an IP block or rate limit since they do not log in) and not to automate bidding. Instead each Freelancer alert carries a `/propose` draft: `run.sh` sets GIG_DRAFT=1 and uses the tech-digest venv python; at most 3 drafts per run; the user pastes and submits manually.

**Rules added 2026-10-09 (user instructions):**
- Backoff: gig_scout/backoff.py. A 403/429 from freelancer.com pauses the scanner and the daily job for 6 h (state `~/.gig-scout/backoff.json`), sends one Telegram note, never retries or routes around. The user asked about using rotating IPs; I declined (section 33.2(e) forbids bypassing access restrictions).
- Autonomy gate: the user requires that every pushed project can be done 100% independently by Claude. Cannot be guaranteed up front; implemented as a fail-closed gate: `/propose` output now has `AUTONOMY: YES/NO` and the scanner (run.sh sets GIG_DRAFT=1) alerts only when VERDICT: GO and AUTONOMY: YES, max 6 judge calls per run, failed judgements retried next run. In a test run it rejected 6 of 6 candidates, so alerts will be rare. GitHub bounties are off unless GIG_GITHUB=1 (no gate for them).
