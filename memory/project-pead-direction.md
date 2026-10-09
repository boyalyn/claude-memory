---
name: project-pead-direction
description: "2026-10-04 pivot to post-earnings drift (EAR ≥ 8%) research; pre-registered exits, sizing rules, $25k capital"
metadata:
  node_type: memory
  type: project
  originSessionId: decacfdb-5fed-4018-9867-0fdccec3bd99
  modified: 2026-10-04T05:55:36.780Z
---

On 2026-10-04 the user and I pivoted from sentiment to post-earnings-announcement drift.

- In-sample (scripts/pead_study.py, Nasdaq-100, 2012-2026): EAR vs AR20 Spearman r=+0.063 (p<1e-4); effect sits in the top EAR decile (≥ ~8% vs QQQ): AR20 +2.36%. Strong survivorship worry (TSLA/PLTR/AMD...).
- Out-of-sample rule frozen in scripts/pead_oos.py (S&P 500 ex-NDX, EAR vs SPY ≥ 8%, buy next open, hold 20, 0.10% cost, PASS = per-quarter mean > 0 and t ≥ 2).
- Exit candidates agreed BEFORE seeing results: A fixed 20d; B hold until ~55 sessions (before next earnings); C = B + exit if close < pre-earnings close; D = B + -12% stop. No take-profit. Select on one universe, confirm on the other.
- Sizing v1 agreed: N=10 equal slots, first-come-first-served (same-day ties by EAR), no replacing, 1 per ticker, max 3 per GICS sector, min $2,500/slot, no leverage/short, halt new entries at -15% portfolio drawdown. Compare FCFS vs random selection (100 runs).
- User's comfortable capital: **$25k** → N=10, ~$2.5k/slot.
- Monthly QQQ 10-month-SMA reminder (signals/trend.py, remote/trend_alert.py, /trend): deployed 2026-10-04, merged in PR #1.

**Outcome (same day):** portfolio sims (scripts/pead_portfolio.py) — best variant C + core index + 10-month trend: ~+2%/yr over index in backtest, alpha t≈1.7-2.0; my realistic estimate +0-2%/yr (~$0-500/yr on $25k). User decided it's NOT worth doing; dropped.

**Why:** "buy any event" had zero edge; this is the first signal with evidence. **How to apply:** don't change the frozen rules after seeing OOS; don't deploy/commit without being asked. Related: [[project-status]].
