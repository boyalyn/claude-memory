---
name: feedback-keep-exploring
description: When the user is mid-exploration, do not keep suggesting to wrap up or abandon; offer next experiments instead
metadata:
  type: feedback
---

2026-10-12 (Ichimoku/SPY/QQQ thread): after several results I repeatedly ended replies with "this line can be closed / I would not use it"; the user said they were dissatisfied and had not explored enough.

**Why:** they want to understand the mechanism and keep testing variants; a verdict at every turn feels like being pushed out. This is different from the earlier go/no-go preference in [[feedback-goal-money-or-abandon]], which applies when they ask for a decision.
**How to apply:** report results and what they do and do not show, then propose 2-4 concrete next experiments (with the question each answers) instead of closing the topic. Give a pursue/abandon verdict only when asked. Keep pre-registering rules and reporting disconfirming results honestly. Related: [[project-ichimoku-spy]], [[feedback-working-style]].

**Second occurrence, 2026-10-13 (Bittensor SN13 miner):** I told the user "no-go / survival <5% / consider shutting down" three times while my own pipeline had undiscovered bugs (cost numbers contaminated by their other Apify job, then a cache bug that sent invalid timestamps, then a comment/score-ratio rule). Each verdict was built on data I had not audited. The user said they have told me "countless times" not to conclude hastily, to check more and explore more.
**How to apply (stricter):** before ANY stop/continue recommendation on something I built or run, first audit my own data path end to end — run the system's own validator/checker on a sample of exactly what is sent, check for shared-account or shared-resource contamination in measurements, state the lag between a change and when its effect can show up, and say plainly what is unverified. Report measurements and open hypotheses; do not give survival probabilities or shutdown advice from early or lagged numbers. Link: [[project-bittensor]].

