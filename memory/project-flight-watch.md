---
name: project-flight-watch
description: ENDED 2026-10-26 — outbound SHA->TYO 11-08 ticket bought, JL80/JL82 watch cron removed; script + history kept in ~/lab/flight-watch
metadata:
  node_type: memory
  type: project
  originSessionId: ed4dc638-f19a-5ae6-9f65-366fd6ff071a
  modified: 2026-10-24T14:16:26.362Z
---

Set up 2026-10-24 because the user wants to watch two named flights, JL80 (PVG 10:00->HND 13:50) and JL82 (SHA 13:05->HND 16:50), on 2026-11-08. This is the outbound flight for to-do #3. The travel MCP trackers can't do this: they only follow the cheapest fare on a route.

- Code: ~/lab/flight-watch/watch.py; prices are logged to history.csv. Cron runs daily at 01:10 UTC (09:10 SGT); log at ~/.claude/flight-watch.log.
- How it works: `claude -p --model haiku` with hooks disabled calls mcp__claude_ai_Travel__search_flights (SHA->HND nonstop, sort=departure; it retries with sort=price if a flight is missing). The script parses the raw tool_result, not the model's text. Each run costs about US$0.04 and 1 SerpApi search (cached for 6h).
- Jarvis alert rule: price lower than the last check, a flight missing from the results, or an error.
- Prices: 2026-10-24 JL80 S$534, JL82 S$898. On 2026-10-17 JL82 was about S$534 (from the to-do note).
- Tracker #3 (cheapest nonstop on the route) was created and then stopped the same day. Tracker #2 (Osaka->SIN 11-15) is unrelated and still active.
- **Remove the cron line after 2026-11-08** (the script already does nothing after that date).

Related: [[project-mcp-servers]], [[project-todo]], [[reference-notification-channel]].

**2026-10-26 update:** The user bought the outbound ticket (they did not say which flight; options shown were FM 895 S$400, IJ 6 S$213, JL80 S$534, JL82 S$898). I removed the cron line from boya-server's crontab and marked to-do #3 done. watch.py and history.csv are still in ~/lab/flight-watch.
