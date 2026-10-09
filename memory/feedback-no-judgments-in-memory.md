---
name: feedback-no-judgments-in-memory
description: "Do not store verdicts/judgments (go/no-go, X is better) in memory; store only facts, instructions and tested results"
metadata:
  type: feedback
---

The user said (2026-10-09): do not write judgment-type conclusions into memory, because a precise verdict reached in a few conversation turns is very unlikely to be reliable.

**Why:** a stored verdict gets treated as fact by later sessions and anchors them; a shallow early judgment would then block better analysis.
The user also described themselves (2026-10-09) as very open-minded and dislikes ideas being rejected. Do not close doors: prefer "not supported by test X yet / needs Y" over "rejected / no-go", say what evidence would change the view, and keep ideas alive unless the user parks them.

Rule on negation (2026-10-09): when I argue against an idea, support it with concrete, arguable evidence (a measurement, a cited source I actually read, a calculation the user can check), and state the evidence's limits (source bias, sample size, what was not tested). Opinions, vibes, or "the market is crowded" are not enough to negate; without such evidence say "unverified" and propose the test.

**How to apply:** memory holds only (a) facts, (b) the user's instructions/preferences, (c) results actually measured, with how they were measured. Judgments in chat are fine to give (see [[feedback-goal-money-or-abandon]]) but are not persisted. In ~/claude-memory/ideas, change status to supported/not-supported only after a real test, never from conversation alone; untested hypotheses must be labelled as such with their basis. [[reference-ideas-log]]
