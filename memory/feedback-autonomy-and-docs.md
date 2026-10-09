---
name: feedback-autonomy-and-docs
description: "User's standing permissions for running code/downloads/sudo and how they want research docs written"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 8508b71b-36e8-5127-8a54-8f707594c1ce
  modified: 2026-10-06T20:46:09.500Z
---

On the home server (/home/boya) the user said (2026-10-06): no approval needed for downloads, running
code, writing/modifying code in the working folders, or running such commands; they also granted sudo on
this machine. Overnight they asked me to keep the server busy exploring and only stop if they say stop or
usage passes ~95% (raised from 85% on 2026-10-07).

**Why:** they want long autonomous research runs and were repeatedly interrupted by prompts.
**How to apply:** just run scripts/downloads in the work folders; still do NOT commit/push, touch the
production VPS (178.105.158.87), or use credentials I wasn't handed without asking. Sudo was only for this machine.
Exception (2026-10-09): the user authorized automatic commit/push of the memory-sync repo boyalyn/claude-memory (~/claude-memory) via SessionStart/SessionEnd hooks in ~/.claude/settings.json; the no-push rule still applies to all code repos.

Docs: write in English, plain language the user can follow (they are learning the finance terms):
each doc starts with "In plain words", has a glossary, states success criteria BEFORE results, and gives
results as tables + a "what this means" paragraph. Index at docs/README.md in the nasdaq-event-agent repo.
Related: [[project-trader-research-state]]

Research method preference (2026-10-07): the user wants to TUNE parameters, so do NOT pre-freeze thresholds. Split the data in time first (train/validation/test), tune on train (+validation to pick among the best), open the test segment once at the end; keep a random-schedule null and report how many configurations were tried. Interrupted me once for freezing thresholds before splitting.
