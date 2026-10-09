---
description: Log an unverified idea into ~/claude-memory/ideas/ (usage: /idea <rough description>)
argument-hint: <rough description of the idea>
---

Log this idea into the ideas library at ~/claude-memory/ideas/ (README.md there has the rules; follow them):

$ARGUMENTS

Steps:
1. Read ~/claude-memory/ideas/INDEX.md to find the next free number and to check for a similar existing idea. If one looks similar, show it and ask whether to update it or add a new one.
2. Create ~/claude-memory/ideas/idea-NNN-short-slug.md from _template.md. Fill every section from what I wrote. Where I gave no information, write "unknown, to be found in test" rather than inventing. Mark status `untested`, state the basis of the hypothesis (e.g. "one conversation, no data"), and propose success and failure criteria BEFORE any testing, but flag them as proposals for me to confirm.
3. Add a row to INDEX.md (id, title, status, updated).
4. Do not judge or argue against the idea. If you have a concern, record it only as a question or a test to run, with the evidence it would need.
5. Reply with the file path, a three-line summary, and the one question that most affects how to test it. If the description is too vague to fill the template, ask that single question first.
