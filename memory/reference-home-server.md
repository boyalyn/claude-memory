---
name: reference-home-server
description: User's home server boya-server (LAN, behind CGNAT) running Claude Code Remote Control as their pocket dev machine
metadata:
  type: reference
---

Host alias `boya-server-home` in ~/.ssh/config: 192.168.1.65, user `boya`. It's on the home LAN only, reachable when the user's Mac is at home. A static public IP failed before, most likely CGNAT; it isn't needed. Hardware: Intel N100 4 cores, 16 GB RAM, 98 GB disk, no GPU, Ubuntu 24.04. sudo needs the user's password (I don't have it). python3, git and tmux are installed; there is no docker, node or Tailscale.

Purpose: the user's "pocket computer". From the iPhone Claude app (Code tab), they drive Claude Code running there to design experiments, test ideas and build agents. It's deliberately separate from the Hetzner trading box, so there are no broker or trading secrets on it.

Setup (2026-10-06):
- Claude Code installed at ~/.local/bin/claude and logged in with `claude auth login` (full scope). setup-token tokens can't do Remote Control.
- Workspace ~/lab (git init'd, trusted).
- User systemd service ~/.config/systemd/user/claude-rc.service runs ~/bin/claude-rc.sh inside tmux session `lab`: `claude remote-control --name home-lab --spawn same-dir --permission-mode default`.
- linger is enabled, so it starts at boot. Restart=always; auto-restart was verified (~1.5 min). Exits are logged to ~/.claude-rc.log. A reboot hasn't been tested yet.
- Inspect with `tmux attach -t lab` or `systemctl --user status claude-rc`.

Gotchas:
- `pkill -f "claude remote-control"` over ssh kills the ssh shell too, because its own command line matches.
- Starting a second server right after killing one in the same folder fails; ExecStartPre now waits.
- Trusted Devices didn't appear editable for the user's Pro account. Meanwhile, keep permission prompts on (default mode).

Plan discussed (not built): a Telegram "butler" bot as the single entry point. The digest bot gets upgraded and dispatches to digest / trading read-only / dev agent on this box. The trading bot stays independent for the kill switch. Related: [[project-tech-digest]], [[project-status]].
