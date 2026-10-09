---
name: feedback-working-style
description: How the user wants me to work on this project - commits, honesty, real-money caution, verification
metadata:
  type: feedback
---

Only commit/push/change server state when asked; they say "提交 push" explicitly each time.
**Why:** it is their live trading stack. **How to apply:** finish the work, report, then offer; never auto-commit.

Report my own mistakes plainly, with the corrected conclusion (e.g. the SEC press-release bug, the daily-loss breaker bug). They valued this and asked follow-ups rather than being upset.
**Why:** decisions about real money rest on my claims. **How to apply:** verify with real data, not invented fixtures; say what is untested.

Real money: default to SIMULATE + DRY_RUN; ask before anything that could place a real order or weaken safeguards; keep secrets out of git, memory and chat echoes.
**Why:** they intend live trading via moomoo eventually. **How to apply:** see [[reference-access-and-credentials]].

Prefer evidence over reassurance: when asked "will X improve results?", run the experiment (they approved the event study) and say when a result is just noise.

Don't jump to conclusions: when a result looks bad, they said "不要这么快给我下结论" and asked for the *why*. Decompose causes, e.g. megacap concentration vs. signal decay vs. survivorship, before calling something dead.
**Why:** a hasty "it failed" hid useful structure (the equal-weight vs cap-weight headwind). **How to apply:** after a failed test, show the decomposition, then let them decide.

They won't wait months for forward tests ("周期太长了，我无法忍受"). They proposed testing on a different untouched universe (S&P ex-NDX) instead.
**How to apply:** offer a fast out-of-sample check on another universe or period first; suggest a forward test only if that passes.

When they ask for something I can't do under auto-mode rules (e.g. the proxy), stop, explain, and wait. Their explicit in-chat authorization was enough to proceed the second time.

Don't imply a user error from indirect evidence: when logs suggested a missing space in a header value, the user was sure they'd typed it and stopped my tool call. Present what the system received as a neutral fact and offer a workaround that doesn't depend on who was right.
**How to apply:** "the server received X" rather than "you typed X wrong".

An interrupted or "rejected" Bash call can still have partly executed. A multi-step command that was stopped had already applied its first local edit. **How to apply:** after an interruption, check the actual state (files, server) before redoing or assuming nothing happened. Avoid destructive steps such as `journalctl --vacuum` (it wipes ALL units' archived logs, and -u doesn't scope it) inside long chained commands.
