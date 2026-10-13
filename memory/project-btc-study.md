---
name: project-btc-study
description: 2026-10-11 BTC spot single-asset study (~/lab/btc-study): pre-registered plan, dev tuning, locked test opened ONCE, results; no live trading set up
metadata:
  type: project
---

Replaced a TSLA single-stock plan (lab/tsla-study/PLAN.md; never run, news only 2019-2023 and no Polymarket history). BTC plan: ~/lab/btc-study/PLAN.md. Data (Binance spot 1h from 2017-08, funding from 2019-09, Fear&Greed from 2018-02, blockchain.com on-chain, DefiLlama USDT supply) split at 2023-01-01: data/dev vs data/locked. Config frozen in frozen_config.json (sha256 in frozen_config.sha256), test_once.py refuses a second run (test_opened.lock). THE LOCKED TEST HAS BEEN SPENT (opened 2026-10-11); further rule changes cannot be validated on 2023-2026.

Dev (2018-03..2022-12, 54 tuning trials): H1 long/flat on SMA(n) best around n=100-150 (Sharpe 1.0-1.3 net of 0.1%/side), buy&hold Sharpe 0.47, maxDD -77%; walk-forward picks were unstable (2022 pick lost -50% vs B&H -64%).
Locked test (2023-01..2026-10-09, BTC 16.6k -> 82.6k):
- SMA125 (frozen): CAGR +45.9% vs B&H +53.1%; Sharpe 1.23 vs 1.15; maxDD -27% vs -53%; 64% in market; 9.8 trades/yr; 19 trades, 6 winners. Excess vs B&H -9%/yr, 95% CI [-29%, +19%]. Dropping the top 3 trades gives CAGR -2.3%.
- H3 F&G>=80 and H5 USDT-supply top tercile: dev positive, test negative sign, CIs include 0. H2 funding: nothing significant. H4 unique-addresses: sign flipped vs dev.
- H4 n-transactions bottom tercile: +3.1% (14d) / +6.7% (28d) vs all days, CI excludes 0 (28 episodes), dev sign same but not significant; tx counts were distorted by Ordinals/inscriptions from 2023, not a validated tradable rule.
Per the pre-registered criteria nothing passed; no automated trading was built and no Binance API key was requested. User's Binance holds idle USDT; asked about auto-trading H1 — answered: needs explicit consent, would add BTC risk to USDT cash, paper (signal-only) first.
Related: [[project-news-sector-heat]], [[feedback-goal-money-or-abandon]], [[feedback-working-style]].
