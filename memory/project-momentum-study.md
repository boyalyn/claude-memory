---
name: project-momentum-study
description: 2026-10-04 core+momentum satellite backtest (scripts/momentum_study.py); earnings fast lane failed confirmation
metadata:
  type: project
---

User's goal: just make money; wants dynamic allocation (not prediction) after missing MU's run with static VOO/QQQ.

scripts/momentum_study.py (point-in-time S&P 500 membership from fja05680/sp500; yfinance lacks delisted names: coverage 69% of members in 2012 → 99% 2026, flatters satellite vs SPY). $25k, SPY core, 12-1 momentum top-N satellite, monthly.
- N=10/W=30%: full 2013-05..2026-08 CAGR 15.7% vs SPY 14.5%, QQQ 20.0%, MTUM 15.4%; 2013-19 ≈ SPY (13.5 vs 13.5), 2020-26 17.8 vs 15.4.
- Earnings fast lane (EAR ≥ +8% → buy next open, protect 55 sessions): +2.2pp in 2013-19 but −3.9pp in 2020-26 → FAILED pre-registered rule. Fast exit (EAR ≤ −8%) adds nothing.
- Static QQQ beat every dynamic variant over the period.

**How to apply:** don't re-propose the event fast lane; any momentum claim must mention survivorship and that QQQ-vs-SPY choice dwarfed the satellite effect. Related: [[project-pead-direction]].

**Later same day:** QQQ-framework tilts (scripts/qqq_tilt_study.py) — earnings tilt hold 20 looked +1.5pp vs QQQ but failed out-of-sample on S&P ex-NDX vs SPY (scripts/spx_tilt_oos.py). Equal-weight members trail cap-weighted index ~4-5pp/yr since 2020 (megacap concentration) — headwind for any stock-picking tilt. **User dropped the earnings/news-driven tilt route entirely (2026-10-04).** Remaining ideas they liked: odd-lot tender offer monitor (SC TO-I), trend reminder for drawdowns.
