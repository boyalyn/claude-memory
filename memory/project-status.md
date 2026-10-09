---
name: project-status
description: Where the trading-agent project and the side projects stand as of 2026-10-06, and the big-picture conclusion
metadata:
  type: project
---

**Big picture (user's own conclusion, 2026-10-05):** with public data on US large caps, an active retail trader is very unlikely to beat just holding QQQ. Every signal tested over 2026-10-04/05 failed: sentiment and "buy any 8-K", PEAD, the momentum satellite, the QQQ earnings/news tilts, Polymarket lead-lag and odd-lot tenders. The user "放弃了" the stock-signal route. Effort now goes to tools that help them hold an index position (drawdown reminders, macro context) and to their real goal, a tech startup / super individual (see [[user-profile]]).

Trading stack (nasdaq-event-agent, main = PR #1 + #2 merged 2026-10-05): the agent still runs `--mode paper` with DRY_RUN=true and places no orders. The bot has /trend (QQQ vs 10-month SMA, auto push after each month's last close) and /pm (Polymarket alerts for validated Iran/oil themes, context only). Any move to REAL or DRY_RUN=false still needs explicit consent.

Same server also runs:
- the `xray` proxy, see [[reference-vps-proxy]]
- the `tech-digest.timer`, see [[project-tech-digest]]

Detailed findings: [[project-pead-direction]], [[project-momentum-study]], [[project-oddlot]], [[polymarket-access]]. Research scripts and conclusions are in the repo's scripts/ and CLAUDE.md.

**How to apply:** don't re-propose stock-picking / timing signals (earnings, news, sentiment, momentum tilts, event fast lanes) unless the user brings a genuinely new angle. If they do, test it out-of-sample on another universe before any forward test.

**Update 2026-10-08:** user repositioned the agent as a read-only index *adviser* (not a trader): risk gauge `/risk` (VIX, drawdown, trend, Polymarket, earnings calendar) + `/advice` (reads moomoo account, 1-2 stepwise allocation fixes). Volatility-targeting backtest failed (0/24), so VIX is a gauge only. See [[project-forward-test]] for the Form 4 paper test that still runs.
