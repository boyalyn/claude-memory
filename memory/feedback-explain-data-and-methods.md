---
name: feedback-explain-data-and-methods
description: Before any result, explain the data (source, contents, gaps), the method step by step, and limits; show prompt/strategy text before testing; name versions by date; never call simulated or reconstructed data "real"
metadata:
  type: feedback
---

On 2026-10-18 (SN101 run-3 prep) the user was confused, then said they were very unhappy and that it was serious: "你没有说清楚快照是什么，怎么拼凑的矿工". They asked me to save this so it never happens again.

What went wrong:
1. I used a new data source (tag101.ai homepage "SCORING SNAPSHOT": cluster labels, tag counts, 2-3 published tags per cluster, no post text, no per-miner answers) and called it "真实数据". I never said what it was, where it came from, or what it lacks.
2. I rebuilt 247 fake miners from it (each picks 3 distinct clusters, weighted by the remaining tag quota, plus a random published tag) and reported scores without explaining that method.
3. I wrote 4 new prompt variants and tested them without showing their text first. Then I reported only code names (new_long, new_medium).
4. I said "旧版/新版分流 prompt". Both versions were written in the last two days, and neither had run live. The user could not tell which was which.
5. The user could not tell this was a new round of testing, separate from the previous one.

**Why:** the user decides on real money from my reports. Unexplained data, methods or labels make a conclusion impossible to judge, and overstating ("real data") is misleading.

**How to apply:**
- Before presenting any result that uses new data or a new method, say: (a) what the data is, where it comes from, what it contains and what it does not; (b) how it is used, step by step, with one concrete example; (c) its limits (sample size, approximations, what is invented).
- Label data honestly: real, simulated, reconstructed from aggregates, or paraphrased. Never call simulated or reconstructed data "real".
- Show the actual text of any prompt or strategy before testing or deploying it. Let the user review it.
- Name versions by what they are plus their date (e.g. "routed prompt v1, entity-first, 10-17"), never "old/new". Say whether a version has run live.
- When there are several test rounds, say which round a result comes from and how it differs from the earlier one.
- Related: [[feedback-working-style]], [[feedback-no-judgments-in-memory]], [[project-sn101-prep]].
