---
name: project-tech-digest
description: Daily tech/startup news digest for the user's super-individual goal - repo, how it runs, how to change it
metadata:
  type: project
---

Repo: ~/Projects/tech-digest, pushed to github.com/boyalyn/tech-digest (private). Built 2026-10-05.

Sources: HN, Show HN, Product Hunt, TechCrunch, The Verge AI, OpenAI, GitHub Blog, Simon Willison, Ben's Bites, Lenny's, e27, r/SaaS, r/indiehackers, HF papers. Reddit indiehackers often returns 429; that's fine, failed sources are skipped and listed in the footer.

Pipeline: one Claude call produces a structured Chinese digest (top items, opportunities, tools, money). Any URL not among the collected items is dropped. It is sent to Telegram bot @boya_assist_bot (a separate bot from the trading bot).

Summary backend: `claude -p` (Claude Code CLI under the trader user on the VPS), authenticated with the user's **Claude Pro** subscription token (`CLAUDE_CODE_OAUTH_TOKEN` from `claude setup-token`). Model `DIGEST_CLAUDE_MODEL=sonnet` to spare the Pro allowance. Pro includes no API credits; the user chose this over paying for the API. ANTHROPIC_API_KEY is stripped from the subprocess so it can't override the token. `DIGEST_BACKEND=api` remains as an alternative.

Server: code in /home/trader/tech-digest; `.env` (600) holds the token, bot token and chat id. Scheduling (since 2026-10-06): a thread in the `tech-digest-chat` service runs the digest at data/settings.json push_time (default 08:00 SGT; the user changes it with /time). It runs once a day with a 4h catch-up, and failures are reported in Telegram. The systemd `tech-digest.timer` is DISABLED; re-enabling it would double-send. Logs: `journalctl -u tech-digest`. First real digest was delivered 2026-10-05.

Chat (added 2026-10-06): `tech-digest-chat` systemd service long-polls @boya_assist_bot and answers the user via `claude -p` (Pro token), with only WebFetch+WebSearch tools. Digest entries are numbered [n]; each sent digest is archived in data/archive/DATE.json with its message ids. Routing: a reply to an answer resumes that session (`--resume`); a reply to a digest starts a new session grounded in it; a plain message continues within 6h; /new resets. State lives in data/chat_state.json. Gotcha: Telegram's getUpdates `timeout` param clashed with our HTTP timeout kwarg; it was renamed http_timeout.

Profile (added 2026-10-06; the user wants this to grow into a personal assistant): data/profile.md on the server, learned from chat logs (data/chat_log/*.jsonl). It is consolidated once a day before the digest, and the bot reports the changes. It is injected into the chat and digest prompts. /profile, /remember, /forget, /undo; history in data/profile_history/. It never stores secrets or account/health details. DIGEST_CHAT_MODEL is available for cheaper chat replies (the user hasn't chosen one yet). Pro has one shared usage pool for claude.ai and Claude Code, so there's no separate chat allowance.

Reader controls (2026-10-06): 👍/👎 inline buttons per entry go to data/feedback.jsonl and the chat log, then into the profile. /sources shows per-source picks, votes and last fetch. /addsource validates the feed or discovers it from the page. /removesource. These live in data/settings.json; FEEDS in code are only the defaults.

User confirmed (2026-10-06) English sources are enough; don't add Chinese/domestic tech news.

**How to apply:** to change sources edit FEEDS in sources.py; to change focus edit SYSTEM in summarize.py; rsync to the server (never overwrite .env). If a morning run fails, check for an expired Pro token or the usage limit first.
