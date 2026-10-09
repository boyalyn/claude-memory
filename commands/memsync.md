---
description: Manually sync Claude memory (pull then push) and report the result
---

Manually sync the memory repo at ~/claude-memory now. Do these steps in order and do not skip any:

1. Run `~/claude-memory/sync.sh pull`, then `~/claude-memory/sync.sh push` (the script never fails the caller, so you must check the outcome yourself).
2. Show the last lines of `~/.claude/memory-sync.log` for this run.
3. Run `git -C ~/claude-memory status -sb` and `git -C ~/claude-memory log --oneline -3`.
4. Report plainly:
   - OK: branch is level with origin/main and the working tree is clean.
   - Problem: a rebase in progress, conflict markers, or ahead/behind origin. In that case list the conflicted files and what each side changed, propose a resolution, and wait for my confirmation before resolving. Never discard either side's changes without asking.
5. If MEMORY.md was merged, check that every file linked in the index exists and every file in memory/ has an index line; list mismatches.
