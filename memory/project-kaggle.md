---
name: project-kaggle
description: Kaggle work on home server (2026-10-09): setup, results, tuning lessons, user's next ask (prize competitions)
metadata:
  type: project
---

Work dir ~/lab/kaggle (venv via uv, Kaggle token in .env as KAGGLE_API_TOKEN, 4 CPU cores, no GPU). Notes: ~/lab/kaggle/NOTES.md.
Notify the user with ~/lab/kaggle/notify.sh "msg": it ssh's to the VPS and runs ~/tech-digest/notify_stdin.py (added 2026-10-09 with user's permission);
the bot token never leaves the VPS (copying it to this machine was denied by the permission classifier, so don't retry that).
User goal: top 10% on chosen competitions, auto-submit, self-run experiments, ping via jarvis when stuck. On 2026-10-09 the user said stop
the current experiments, summarise tuning lessons, then look for competitions with prize money.
Results/lessons are in NOTES.md (Spaceship in top 10%; Store Sales 0.397 vs 0.390 line; s6e10 plateau; Titanic below line).
**Why:** user is "not caring about prize" earlier, then changed to prize competitions on 2026-10-09.
**How to apply:** joining a competition needs the user to click Join on the website; Store Sales allows 5 submissions/day.

2026-10-09 update: user chose to chase medals (Playground/Getting Started give none; only Featured/Research do). Abandoned NFL Big Data Bowl
(judged writeup, draft pick explains ~all variance). Working on Enveda CASMI26 (Featured, code in ~/lab/kaggle/enveda: lib.py/retr.py/val.py,
kernel_main.py; Kaggle kernel boyaliu97/enveda-retrieval-baseline runs OK in <10 min). Submitting to Featured comps returns 403
"Identity Verify your account" until the user verifies at kaggle.com/settings. Kaggriculture not joined yet. Local val of retrieval baseline:
best-of-25 Tanimoto 0.372 (LB top-10% line ~0.425; metric unconfirmed).

Enveda findings (2026-10-09): submit only via notebook (kaggle competitions submit -k user/kernel -v N -f submission.csv); 5 submissions/day.
Identity verification done by user. Scores: v1 retrieval (mass filter + spectral cosine on train library) = 0.125; sample CCOx25 = 0.000;
constant "greedy 25 central molecules" = 0.000 -> metric is NOT best-of-25 Tanimoto (would give ~0.27); it is hit/threshold based.
Top-10% line 0.425, LB top 0.484. 45% of test queries have a library candidate with cosine>0.9 (25% >0.98) at same mass, yet score only 0.125,
so the exact match rule is unclear. Local no-self validation: best-of-25 Tanimoto>=0.7 for 10.7% of molecules.

2026-10-09 end: user said to give up on Kaggriculture (could not join) and Enveda paused; no background jobs left running (watch_join stopped).
Unsubmitted: store-sales/sub6.csv. Unrun: titanic/run2.py.

Enveda round 2 (2026-10-09/10): MRR@25 on tautomer-canonical InChIKey14; test = unpublished natural molecules. Pool train+COCONUT (~729k) helps (0.125 -> 0.191).
Fingerprint net (fpnet.py, CPU, ~5 min/epoch) scored 0.183 on LB despite local MRR 0.57: local validations (random, similarity-thresholded, np-examples) did not
predict LB ranking. Datasets/kernels on Kaggle: boyaliu97/casmi-pool-lib (private dataset), kernels casmi-analog-v2, casmi-fpnet-v3. Top-10% line 0.425, my best 0.191.
