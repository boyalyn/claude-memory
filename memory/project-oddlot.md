---
name: project-oddlot
description: Odd-lot US issuer tender arbitrage researched and dropped 2026-10-04 (small spreads + 30% gross withholding for the user)
metadata:
  type: project
---

scripts/oddlot_study.py (branch feature/oddlot-tender-monitor, uncommitted at time of writing): SEC full-text search for SC TO-I with "odd lot", 2015+. Fixed-price offers: median spread ~2% (~$40 per 99-share trade); Dutch auctions aren't an arb. Parser only extracted 79 of 478 filings; termination detection had false positives (boilerplate "extended or terminated").

moomoo SG: no corporate-action fee, but the user confirmed issuer-tender proceeds DO get 30% US withholding on gross for them (Singapore has no US income-tax treaty; refund only via 1040-NR). **User dropped this direction.** Don't re-propose US tender/odd-lot arbitrage. Related: [[project-momentum-study]].
