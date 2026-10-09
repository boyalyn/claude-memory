---
name: project-trader-research-state
description: "Where the nasdaq-event-agent research lives, fixed constraints, data traps, open to-dos and pointers to docs (facts only; no verdicts)"
metadata:
  node_type: memory
  type: project
---

Slimmed on 2026-10-09 at the user's request: results and interpretations live in the repo docs, not here ([[feedback-no-judgments-in-memory]]). The full pre-slimming text is in the claude-memory repo at archive/project-trader-research-state.2026-10-09.full.md (and in git history). Read the docs for numbers; treat any old conclusion as unverified.

**Where things are**
- Repo: /home/boya/lab/nasdaq-event-agent (boyalyn/nasdaq-event-agent, cloned over SSH). Index of docs: docs/README.md. Studies are numbered docs (form4-study, form4-regime-and-scan, form4-health-filter, qqq-dip-add-study, ipo-earnings-study, vix-stress-study, event-gbm-study "Version 1-14", literature-review-2026-10, literature-checks-2026-10, paper-preregistration, paper-results-part1/part2, paper-data-budget, paper-surprises-log).
- Scripts in scripts/, caches in .cache/ (prices, panel, panel_ext, event_gbm, submissions, literature, paper). Python env .venv (statsmodels installed).
- Benchmark used throughout: buy-and-hold QQQ. Assumed account ~US$25k for trading studies.

**Fixed constraints (user's instructions)**
- Research only: no live trading or REAL mode without explicit consent (CLAUDE.md). DRY_RUN untouched.
- Evaluation splits: train folds 2018-20, validation 2021-04..2023-06, TEST segment (events from 2023-09) is LOCKED; do not open unless the user says so. Splits must be by time blocks, not random.
- Nothing from this research is committed except what the docs say; check `git status` before assuming.
- Forward paper test code exists on branch feature/forward-paper-test (src/nasdaq_event_agent/forward/, docs/forward-paper-test.md). It is NOT deployed: this server has never connected to the production VPS; host key unverified (ED25519 SHA256:HYfquog9PC+1+77slaQ0Q3FS2/8iLTlawMevAMA4guU as seen from here). Do not bypass host-key verification; deployment needs the user to confirm the fingerprint or run deploy/sync_to_server.sh themselves.
- Personal finances of the user are intentionally NOT stored. The paper's "individual" is a persona defined from public statistics (US$10k-100k, base US$50k; docs/paper-preregistration.md section 10).
- LLM stage for earnings/news is deliberately not started; if started: mask names and dates, use placebo, only post-cutoff events are clean, use `claude -p` (no `claude` CLI existed on this machine on 2026-10-07; do not use other API keys).

**Known data traps (facts)**
- Yahoo has no delisted tickers (survivorship); ticker reuse produced wrong price series (use insider-price consistency check). Share of Form 4 buy filings whose ticker is in today's panel: ~40% in 2011-15, ~61% in 2021-23, ~79% in 2025.
- SEC bulk Form 4 data stops at 2026Q1.
- Machine: Intel N100, 4 cores, 15 GB RAM, ~75 GB free; `sudo` needs a password (not passwordless), so QEMU/KVM cannot be installed by Claude. Norgate is Windows-only; the user dropped it.

**Paper project (user's direction, 2026-10-07)**
- User asked for a paper for individuals / non-finance readers (not a thesis; no WRDS/CRSP access). Direction later changed: open-minded root-cause analysis of why individuals struggle vs index funds (Part A) plus how an individual can maximise outcomes, hedge and allocate (Part B). Not personalised advice. Refuted claims must be surfaced prominently ([[feedback-goal-money-or-abandon]]).
- Data budget rule: operating data <=1% of capital/yr, research budget ~US$1,000 once (docs/paper-data-budget.md). Nothing bought; the user decides purchases.

**Open to-dos (as of 2026-10-07)**
- Paper: P3 (retail rule zoo with Reality Check), P2 (re-implement ~10 signals on free data), then Part B.
- Cheap next checks noted: add Deflated Sharpe / MinTRL to the harness (done in scripts/evalstats.py); beta-adjusted target; portfolio-level validation (current validation is per-event equal weight, no capital accounting).
- Forward paper test deployment (see constraint above).

Related: [[feedback-autonomy-and-docs]], [[reference-notification-channel]]
