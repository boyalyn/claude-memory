---
name: project-stock-watch
description: Air purifier restock watcher on the VPS (haze Oct 2026) — cron, files, watch list, known gaps
metadata:
  type: project
---

Set up 2026-10-16 18:46 SGT during the Singapore haze (purifiers sold out). Code: ~/lab/stock-watch (local) and
~/stock-watch on VPS (trader). Cron `*/15 * * * *` runs stock_watch.py; pushes via Jarvis (tech-digest notify_stdin.py,
see [[reference-notification-channel]]) when a watched item turns buyable; one alert per out→in transition.
Watch list in watchlist.json: Courts LG AeroHit AS35, Blueair Mini Max, Tefal PT2220, Daikin MC30YVM7 (only if ≤S$300),
plus Courts searches for Levoit Core/Vital and Xiaomi purifiers. Courts stock read from JSON-LD schema.org availability.
Gaps: Gain City returns 403 to the VPS; PRISM+ Shopify "available" includes backorders (Dec delivery) so it was dropped;
Shopee search blocked by captcha. User's room is small. Crontab backup ~/crontab.bak.<timestamp>.
**How to apply:** remove the cron line when the user has bought one or the haze ends.
2026-10-17: Courts returned HTTP 404 for all product pages 2026-10-16 21:15 → 2026-10-17 03:00 SGT (watcher sent one "all failed" alert, then self-recovered; nothing on the VPS had changed). Added a one-time "已恢复" Jarvis message after an all-fail streak. Courts search with multi-word queries returned 0 items, so searches changed to "levoit"/"xiaomi" (the path pattern still filters); as of 10-17 Courts lists no Levoit/Xiaomi purifiers.
