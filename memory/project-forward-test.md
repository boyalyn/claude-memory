---
name: project-forward-test
description: Form 4 + financial-health forward paper test (QQQ core) deployed 2026-10-08; rule frozen, bookkeeping only, bot /forward
metadata:
  type: project
---

Deployed to the VPS 2026-10-08: `forward-daily.timer` (07:30 UTC) runs `nasdaq-agent forward-daily`. Rule: single Form 4 open-market buy >= $250k, stock down >= 40% over 120d, cap $50M-$10B, non-financial, healthy balance sheet; buy next open, hold 60 trading days, 10 slots (parallel 20-slot book), idle cash in QQQ. Never places orders; DRY_RUN/TRADING_ENV unchanged. Bot command `/forward` shows rule + progress.

**Why:** backtest +4-6%/yr over QQQ but monthly t~1.5 and the edge sits only in QQQ drawdowns (>=15% below high); user wants an honest forward test, not real money. "Health data" = company financial health, not personal health.

**How to apply:** don't tune the rule mid-test. Don't call it a win/loss before 12 months, 30 closed trades and 2 QQQ drawdowns. Rule text: repo `docs/forward-paper-test.md`. Related: [[project-status]].
