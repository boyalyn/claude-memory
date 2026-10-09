---
name: reference-ideas-log
description: "Where the user's unverified ideas live (~/claude-memory/ideas/) and how to log, update and reference them"
metadata:
  type: reference
---

The user keeps unverified ideas in ~/claude-memory/ideas/ (one file per idea, `idea-NNN-slug.md`, template `_template.md`, index `INDEX.md`, rules in `README.md`).
When the user says "log an idea: ...", create the next-numbered file from the template (fill hypothesis, how to test, success/failure criterion, money path) and add a row to INDEX.md. When they cite "idea-007", read that file. At session start in /home/boya/lab, read INDEX.md if the user mentions ideas, backlog, or "what should I test next".
Keep status, updated date, Log and the INDEX row in sync; never delete ideas; if a test does not support one, record what was tested and what evidence would change the view.

**Why:** the user wants a durable place for ideas they have no time to test now, referable in later chats.
**How to apply:** only monetizable directions matter, so always fill the Money path section ([[feedback-goal-money-or-abandon]]); success criteria are written before testing.
