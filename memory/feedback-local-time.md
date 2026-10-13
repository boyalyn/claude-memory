---
name: feedback-local-time
description: Report times in the user's local time (Singapore, UTC+8), not UTC
metadata:
  type: feedback
---

2026-10-13: the user said "don't tell me UTC, tell me local time" after many Bittensor status reports quoted UTC.

**Why:** UTC forces them to convert in their head while they follow a time-sensitive experiment, often from the phone.
**How to apply:** in every user-facing message give times as local clock time (assumed Singapore, UTC+8 — NTU email, home server public IP in Singapore; correct if they say otherwise), with the date only when it is not today. Convert before writing (e.g. 11:34 UTC = 19:34). Server logs and chain data stay in UTC internally. Link: [[user-profile]], [[project-bittensor]].
