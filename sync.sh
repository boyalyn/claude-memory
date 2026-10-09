#!/usr/bin/env bash
# Usage: sync.sh pull | push. Never fails the caller; logs to ~/.claude/memory-sync.log
# Portable across Linux and macOS (no GNU-only flags).
R="$(cd "$(dirname "$0")" && pwd)"
LOG="$HOME/.claude/memory-sync.log"
G="git -C $R -c user.name=$(whoami) -c user.email=memory-sync@localhost"
T=""; command -v timeout >/dev/null 2>&1 && T="timeout 20"; command -v gtimeout >/dev/null 2>&1 && T="gtimeout 20"
NOW="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
{
  echo "== $NOW $1"
  case "$1" in
    pull) $T $G pull --rebase --autostash origin main ;;
    push) $G add -A
          $G diff --cached --quiet || $G commit -qm "sync from $(hostname) $NOW"
          $T $G pull --rebase --autostash origin main && $T $G push -u origin main ;;
  esac
} >>"$LOG" 2>&1
exit 0
