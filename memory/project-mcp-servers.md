---
name: project-mcp-servers
description: Monorepo of the user's remote MCP servers (claude.ai custom connectors); first is travel (SerpApi flights/hotels + price tracking)
metadata:
  type: project
---

The user wants ALL MCP servers in ONE repo: ~/Projects/mcp-servers. There is one subpackage per server under mcp_servers/, with shared auth and Telegram code in mcp_servers/common. It isn't on GitHub yet; ask before pushing (the user pushes their other repos as private).

travel (built 2026-10-06): the user found Claude Cowork can't get real fares. Reason: fares are dynamic and JS-rendered, and Amadeus self-service shut down 2026-07. Fix: SerpApi Google Flights/Hotels (free 250 searches/mo), chosen by the user.
- Tools: search_flights, get_return_flights, search_hotels, track_flight_price, track_hotel_price, list_price_trackers, stop_price_tracker, search_quota.
- 6h cache. Interactive searches keep 20 in reserve for trackers. Max 5 trackers, checked daily at 09:00 SGT by mcp-travel-check.timer. Telegram alerts go via @boya_assist_bot.
- MCP Python SDK is 2.x: `MCPServer` (FastMCP renamed). Raise `ToolError` for anticipated failures, otherwise the model only sees "Error executing tool". DNS-rebinding protection needs the public host in allowed_hosts.

Deployment on Hetzner: system user `mcp`, /srv/mcp, secrets in /srv/mcp/.env (600). The bearer token was generated there; the user reads it with `ssh de-root grep MCP_TRAVEL_TOKEN /srv/mcp/.env`. Service: mcp-travel on 127.0.0.1:8765.

Public URL: https://hetzner-de.tail8bd3c4.ts.net/mcp via **Tailscale Funnel**. The user ran the funnel command themselves; my attempt was blocked by the auto-mode classifier (External Ingress Tunnel), as was opening 8443 to all (Security Weaken). The bearer token is the only gate.

History / gotchas:
- First try was Caddy + sslip.io on :8443 firewalled to Anthropic's 160.79.104.0/21. claude.ai never connected (likely the non-443 port), so it was removed along with ports 80/8443.
- Xray listening on 0.0.0.0:443 stole :443 on the Tailscale IP, so Funnel got the apple.com cert and a TLS reset. Fixed by binding Xray to the public IP (vps-proxy commit 3cee9ca).
- Funnel took ~3.5 min to become reachable.

Status 2026-10-06: **working end to end.** The connector was added in claude.ai and the tools are also visible in Claude Code sessions. Verified with real searches: SIN->HND,NRT flights and Shinjuku hotels. Real SerpApi responses are saved as test fixtures; 12 tests pass.

More gotchas:
- SerpApi rejects metro codes (TYO), so common city codes are expanded to airport lists.
- Hotel list results rarely include per-source prices, so free_cancellation is null (unknown), not false.
- Funnel intermittently stopped delivering until tailscaled restarted. A watchdog timer (funnel-watchdog, every 2 min) probes the public path and restarts tailscaled after 2 failures.
- claude.ai sent "Bearer<token>" with no space even though the user typed the space, so the server now accepts Bearer with or without the space, or the bare token. The user configured the bare token.
- The token was rotated after the user pasted the old one into chat. Logs never record token characters.
- claude.ai probes /.well-known/oauth-*; these return 404.

The repo is NOT pushed to GitHub yet; ask first. Related: [[reference-tailscale]], [[reference-vps-proxy]].
