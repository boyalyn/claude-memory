---
name: feedback-english-formulas
description: Formulas should look like textbook math (standard notation), English terms; not pseudo-code, not raw LaTeX source
metadata:
  type: feedback
---

Said 2026-10-12 over several turns: Chinese-translated formula terms felt odd (work language is English); raw LaTeX-looking text with underscores/braces was unreadable; pseudo-code with full-word variables was also rejected. Intent stated last: "present a mathematical formula the way it naturally looks".

**Why:** the user wants conventional math notation they can read at a glance, not code.
**How to apply:** terminal/markdown cannot render LaTeX, so write formulas with Unicode math (½, √, ≤, ², subscript digits like M₉, function notation C(t−26), max{…}) in a code block for alignment; define symbols once; keep prose in Chinese; add one small numeric example. Ask which line is wrong if a symbol does not display. Do not use LaTeX source or underscore-subscripts. Related: [[user-profile]], [[feedback-autonomy-and-docs]].
