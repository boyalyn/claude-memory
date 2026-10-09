---
name: reference-notification-channel
description: "How to message the user from this server (\"jarvis\" = the tech-digest Telegram bot) and what is still missing"
metadata:
  node_type: memory
  type: reference
  originSessionId: 8508b71b-36e8-5127-8a54-8f707594c1ce
  modified: 2026-10-06T20:46:18.829Z
---

The user calls the Telegram bot in the repo boyalyn/tech-digest "jarvis" (cloned at /home/boya/lab/tech-digest;
sending code: tech_digest/telegram.py send_plain(token, chat_id, text)). It needs DIGEST_TELEGRAM_BOT_TOKEN and
DIGEST_TELEGRAM_CHAT_IDS, which live only in the .env on the production VPS (178.105.158.87, user trader) —
not in git and not on this machine as of 2026-10-07. Do not poll getUpdates with that bot (its chat service already does).
Ask the user to place the two values in /home/boya/lab/tech-digest/.env or to approve reading just those two lines over SSH.
Fallback: the PushNotification tool (phone push only if Remote Control is connected and the user is away from the terminal;
a test on 2026-10-07 was "not sent" because the terminal was active, so delivery is unverified).
This session runs on the server inside tmux "lab" (systemd user service claude-rc.service, Linger=yes), so closing the
user's laptop does not stop it.
