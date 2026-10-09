---
name: polymarket-access
description: Polymarket public data APIs reachable from both Singapore laptop and the Hetzner DE server; trading geoblocked in DE; user wants data only
metadata:
  type: reference
---

Tested 2026-10-04: gamma-api.polymarket.com, clob.polymarket.com, data-api.polymarket.com all return 200 without auth from the local machine (Singapore) and from the Hetzner server (178.105.158.87, DE). polymarket.com itself doesn't resolve/answer locally (SG blocks the site), and polymarket.com/api/geoblock from the server says {"blocked": true, "country": "DE"} — i.e. trading is blocked from Germany anyway.

User's intent: use Polymarket data only, no betting. Don't build order placement or suggest geoblock workarounds. Related: [[project-status]].

**Study result (2026-10-04, scripts/polymarket_moves.py + polymarket_leadlag.py):** Polymarket big moves co-move with Nasdaq/crude futures in the same hours but do NOT lead (post-move drift ~0; weekend moves don't predict reopen). Common-sense labels validated overall (t=3.1); validated themes = Iran escalation/de-escalation and oil (oil channel); Fed themes unreliable (sign flips); trade/Ukraine/shutdown unconfirmed. Codified in src/nasdaq_event_agent/signals/polymarket_themes.py as context-only logic (not a trade signal).

Deployed 2026-10-04: remote/polymarket_alert.py runs in the bot and checks every 15 min. It pushes only VALIDATED themes; the rest go to /actions. /pm shows its status. POLYMARKET_ALERTS=false turns it off.
