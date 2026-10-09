#!/usr/bin/env bash
# Usage: sync.sh pull | push. Never fails the caller; logs to ~/.claude/memory-sync.log
R="$(cd "$(dirname "$0")" && pwd)"
LOG="$HOME/.claude/memory-sync.log"
G="git -C $R -c user.name=$(whoami) -c user.email=memory-sync@localhost"
{
  echo "== $(date -Is) $1"
  case "$1" in
    pull) timeout 20 $G pull --rebase --autostash origin main ;;
    push) $G add -A
          $G diff --cached --quiet || $G commit -qm "sync from $(hostname) $(date -Is)"
          timeout 20 $G pull --rebase --autostash origin main && timeout 20 $G push -u origin main ;;
  esac
} >>"$LOG" 2>&1
exit 0
