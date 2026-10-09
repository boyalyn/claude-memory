---
name: project-bittensor
description: Bittensor/SN13 research 2026-10-09 — what was checked, on-chain numbers, scripts location, what is untested
metadata:
  type: project
---

User wants money from Bittensor; has no GPU. Checked 2026-10-09:
- Freelancer/GitHub bounty demand for Bittensor dev work: none found (0 hits). GPU-rental route (Vast/io.net) needs owning a GPU: no-go.
- SN13 (Data Universe, CPU-only, scrapes Reddit/X) on-chain snapshot via ~/lab/bittensor/sn13.py (venv .venv, bittensor 11.3.0, read-only): register burn ~0.0077 TAO (~$2, non-refundable), 256 UIDs full, 246 miners, miner pool ~$1,046/day, established miners ~$5.4/day each (flat, top 10% = 13% of pay), but ~58 new miners/day and only ~21 miners older than 14 days (high churn). Prices: TAO $272.6, SN13 alpha $1.21.
- Not yet tested: whether scraping works (Reddit blocks unauthenticated, needs own account or paid Apify), real costs, survival odds. Snapshot only, no time series.

**Why:** step 2 of a staged plan; step 1 is a no-cost scraping test on boya-server before paying any registration fee.
**How to apply:** do not register or stake without user confirmation; re-run sn13.py for fresh numbers. See [[feedback-goal-money-or-abandon]].
