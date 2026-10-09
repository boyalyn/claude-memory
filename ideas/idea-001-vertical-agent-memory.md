---
id: idea-001
title: Vertical (domain-specific) agent memory as a product
status: untested   # untested | testing | supported | not-supported | parked
created: 2026-10-09
updated: 2026-10-09
tags: [agent-memory, product, money]
related: []
---

## Hypothesis
General-purpose agent memory layers (Mem0, Zep, Letta, free open-source tools such as claude-mem and Basic Memory) are numerous, but a memory system built for ONE specific domain/workflow (e.g. research logs for a field, with domain-specific cues, consolidation and staleness rules) might still have paying users.
Basis: only a single conversation plus a web scan of vendor blogs on 2026-10-09. It is a guess, not a finding.

## How to test
- Data / tools needed: primary sources for what the incumbents actually earn and who pays (company announcements, filings, pricing pages); a short list of 5-10 candidate verticals; a handful of conversations with people in those verticals.
- Steps:
  1. Check the funding/revenue/partnership claims from primary sources (Mem0 US$24M, AWS Agent SDK, Letta, Zep); note which claims came only from vendor blogs.
  2. Check whether free tools (claude-mem, Basic Memory) already cover a candidate vertical.
  3. For 2-3 verticals, find people who currently keep this kind of memory by hand and ask what they pay for / would pay for.
  4. Cheapest build: adapt the existing markdown + hooks setup for one vertical and let 3 users try it.
- Success criterion (decided before testing): at least 3 people from one vertical agree to pay a stated price (any amount > 0) for a working version, or one pilot user keeps using it unprompted for 4 weeks.
- Failure criterion: after step 3, nobody in 2-3 verticals names a recurring pain they would pay to solve; record per vertical what was asked and answered.
- Rough cost: step 1-2 about half a day; step 3 a few days of conversations; step 4 about a week.

## Money path (if any)
Who pays: users in the chosen vertical (subscription or per-seat). How much and capacity: unknown, to be found in step 3. What can be lost: time only if stopped after step 3.

## Log
- 2026-10-09: created from a chat about agent memory. Earlier chat remark that the area is crowded is NOT evidence about this idea (see Hypothesis basis).

## Result
Not tested yet.
