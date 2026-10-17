---
id: idea-003
title: Phone room scan -> AI agent plans a tidy, sustainable room, buys the items, and follows up
status: untested
created: 2026-10-17
updated: 2026-10-17
tags: [consumer-app, agent, vision, shopping, home]
related: [~/lab/shopping_mcp (existing Shopee/Amazon ordering MCP with user-approval links), ~/claude-memory/todo (reminder/follow-up pattern)]
---

## Hypothesis
Many people want a tidier home but don't know how to arrange it or keep it that way. An app where you scan your room
with the phone, a model like Claude analyses layout and clutter, proposes a concrete arrangement plus a routine that is
sustainable to maintain, buys the needed items (storage, organisers) for you, and keeps pushing the improvement over
time would be something many people need and would pay for.
Basis: the user's own intuition, one conversation, no data yet.

## How to test
- Data / tools needed: phone photos/video or a LiDAR scan of a few real rooms; a vision-capable model; the existing
  shopping_mcp for ordering; market data on existing apps (room-planning, decluttering, home-organisation apps) and their pricing/reviews.
- Steps (proposal, for the user to confirm):
  1. Desk research: who already does this (scan-to-layout apps, AI interior design apps, decluttering coaches/apps), what they charge, what reviews complain about.
  2. Manual prototype: scan 2-3 real rooms (user's own first), have Claude produce plan + shopping list + weekly routine; check whether the plan is actually usable and the items fit.
  3. Demand check: show the output to ~10 people in the target group; count how many would pay and how much.
- Success criterion (proposal, decide before testing): in step 2 the plan is followed and the room is still tidy after 2 weeks for at least 2 of 3 rooms; in step 3 at least 3 of 10 people say they would pay ≥ S$10 (or a commission on purchases is viable).
- Failure criterion (proposal): plans not usable without heavy manual correction, or fewer than 2 of 10 would pay.
- Rough cost: desk research ~2h; prototype ~1 day; demand check ~1 week of asking people.

## Money path (if any)
Possible: subscription for coaching/follow-up; affiliate commission on items bought through the agent; one-off plan fee.
Who pays: households / renters / students wanting a tidier space. What can be lost: build time; wrong purchases if the agent orders without approval (shopping_mcp already requires user approval links).
Unknown, to be found in test: willingness to pay, commission rates, competitors' pricing.

## Open questions (to test, not judgments)
- Does a phone scan give enough information (dimensions, what is inside drawers/cupboards) for a good plan?
- Does follow-up actually change behaviour, and what keeps people using it after the first tidy-up?
- Which existing apps already cover parts of this, and what do they not do?

## Log
- 2026-10-17: created from the user's description. Background desk research requested ("有空的话在后台评估").
