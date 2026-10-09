---
name: reference-access-and-credentials
description: How server/GitHub/Telegram/moomoo access works and where each secret lives (no secret values stored here)
metadata:
  type: reference
---

No secret is stored in memory or git. Each lives where it is used; a new session only needs the user's machine.

- **Server SSH** (178.105.158.87, Hetzner): key-based using `~/.ssh/id_ed25519` on their Mac. Aliases added to ~/.ssh/config on 2026-10-06: `ssh de-server` (trader) and `ssh de-root` (root); a backup is at ~/.ssh/config.bak-20261006. `ssh trader@...` day to day, `ssh root@...` for admin. Works from any session on this Mac; nothing to re-enter.
- **Server secrets**: `/home/trader/nasdaq-event-agent/.env` (Finnhub key, Telegram token + allowed user id, optional REMOTE_REAL_PIN; mode 600) and `/home/trader/opend/opend.env` (moomoo account id only). The moomoo password is NOT stored anywhere: OpenD keeps a remembered login in `~/.com.moomoo.OpenD/` on the server. If it ever expires, the user must SSH in and log in by hand (SMS code can be relayed via the bot's /code).
- **Local `.env`** (gitignored) has the Finnhub key and SEC user agent; `deploy/sync_to_server.sh` never overwrites the server's `.env`.
- **GitHub**: repo boyalyn/nasdaq-event-agent (private), SSH remote. `gh` is authenticated but needs `GH_CONFIG_DIR="$HOME/.config-gh"` because `~/.config` is root-owned.
- **Trader sudo**: only `/usr/local/sbin/nasdaq-killswitch kill|restore-opend|start-agent`.
- Project facts and operating notes are in the repo's CLAUDE.md and deploy/DEPLOY.md.
