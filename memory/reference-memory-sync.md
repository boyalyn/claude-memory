---
name: reference-memory-sync
description: "How Claude Code memory is synced between the Mac and boya-server via the private git repo boyalyn/claude-memory (symlink, hooks, log, troubleshooting)"
metadata:
  type: reference
---

Memory files are shared between devices through the private repo `git@github.com:boyalyn/claude-memory.git`, cloned to `~/claude-memory` on each device (Mac: /Users/boyaliu/claude-memory; boya-server: /home/boya/claude-memory). The repo holds `memory/` (all memory files plus the index `MEMORY.md`) and `sync.sh`.

**Symlink rule:** each device's project memory dir is a symlink to the repo's `memory/`:
`~/.claude/projects/<project-folder>/memory -> ~/claude-memory/memory`.
`<project-folder>` is the project's absolute working-directory path with every `/` replaced by `-` (leading `-`), so it differs per device and per project (Mac: `-Users-boyaliu-Projects-nasdaq-event-agent`). Verify with `ls ~/.claude/projects` and `ls -ld <dir>/memory`. A new project folder needs its own symlink. Scratch-workspace sessions have throwaway project folders; don't link those.

**Script:** `~/claude-memory/sync.sh pull|push`. It always exits 0 (never blocks a session) and writes everything to the log.
- `pull`: `git pull --rebase --autostash origin main`.
- `push`: `git add -A`, commit "sync from <hostname> <UTC time>" if anything changed, pull --rebase, then `git push -u origin main`.
- Uses `timeout`/`gtimeout` (20 s) only if installed, so it works on macOS without either.

**Hooks:** `~/.claude/settings.json` on each device: SessionStart runs `$HOME/claude-memory/sync.sh pull`, SessionEnd runs `$HOME/claude-memory/sync.sh push`. The user authorised automatic commit/push for this repo only (see [[feedback-autonomy-and-docs]]); every other code repo still needs an explicit ask. On the Mac, the first manual push of the merged memories was done only after the user confirmed.

**Log:** `~/.claude/memory-sync.log` (appended, one `== <UTC time> pull|push` header per run, then git output).

**Troubleshooting:**
- Nothing syncing: `tail -30 ~/.claude/memory-sync.log`. Because the script exits 0, errors show only there.
- Check `git -C ~/claude-memory status -sb` (ahead/behind) and `git -C ~/claude-memory log --oneline -5`.
- Rebase conflict (same file edited on two devices): resolve in `~/claude-memory`, `git rebase --continue`, run `sync.sh push`. Never discard either side without showing the user.
- Auth errors: the SSH key of that device must have access to the GitHub repo (`ssh -T git@github.com`).
- Memory missing in a session: the project-folder symlink is absent or points elsewhere; also confirm hooks are in `settings.json` (valid JSON: `python3 -m json.tool`).
- Mac backups from the first merge (2026-10-09), kept in the project folder: `memory.old` (original dir) and `memory.bak-20261009` (copy). Safe to delete once the user is satisfied.
- Keep secrets out: memory files hold no tokens or passwords, only where they live. The repo is private but treat it as such.
