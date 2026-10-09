---
id: idea-002
title: Wisdom is desire-driven; with enough information and resources anything decomposes into small decisions
status: untested   # untested | testing | supported | not-supported | parked
created: 2026-10-09
updated: 2026-10-09
tags: [philosophy, agents, decision-making]
related: [~/claude-memory/DESIGN.md]
---

## Hypothesis
Original wording (2026-10-09): "智慧这件事，由desire驱动，只要有足够的信息和资源，任何东西都可以被break down成很小的决策步骤".
Two linked claims: (a) wisdom is driven by desire (goals set what is attended to and kept); (b) given enough information and resources, any task can be broken into small decision steps.
Basis: a thought from one conversation about agent memory, no data. Terms "wisdom", "desire", "enough" are not yet defined (unknown, to be defined before testing).

## How to test
Everything below is a PROPOSAL for the owner to confirm or change.
- Data / tools needed: a small set of bounded tasks from different domains (e.g. a planning task, a diagnosis task, an open-ended judgment task); a way to give an agent or a person "enough information and resources"; some outcome measure per task. All unknown, to be chosen.
- Steps (proposal):
  1. Define operationally: what counts as "wisdom" (e.g. outcome quality judged by a pre-set rubric or an expert), what counts as "enough" information/resources (e.g. a fixed budget), and what counts as a "small decision step" (e.g. a step with a checkable yes/no or choice).
  2. Pick 3-5 tasks across domains, including at least one where the right goal is unclear.
  3. For each, try to decompose into small decision steps and attempt it; record where the decomposition stalled and why (missing information, unclear goal, steps that conflict).
  4. Compare with a version where the goal/desire is changed mid-task and see whether the steps and the memory kept change accordingly (tests claim (a)).
- Success criterion (proposal, decide BEFORE looking at results): decomposition completes with an acceptable outcome on all chosen tasks, and a changed goal measurably changes which steps/information are kept.
- Failure criterion (proposal): at least one task stalls even with the agreed information and resources, and the stall cannot be traced to a missing input.
- Rough cost: unknown; a first pass on 3 tasks is likely a few hours.

## Questions to settle before testing (recorded as questions, not objections)
- Can "enough information and resources" be stated in advance, or only recognised afterwards? Evidence needed: a task where the sufficiency threshold is fixed beforehand.
- Does decomposing into correct-looking small steps still guarantee that the goal itself is right? Evidence needed: a task where each step is reasonable but the overall goal is later judged wrong.
- How is "wisdom" distinguished from plain competence in the outcome measure?

## Money path (if any)
none known. Possible link to agent design (goal-driven memory and retrieval, see DESIGN.md) is untested.

## Log
- 2026-10-09: created via /idea from a remark made while discussing agent memory and reasoning. Status untested.

## Result
Not tested yet.
