---
id: idea-005
title: Medical-aesthetics (医美) client management system — follow-ups and client records are manual today
status: untested
created: 2026-10-24
updated: 2026-10-24
tags: [startup, saas, crm, medical-aesthetics, beauty, follow-up, automation]
related: [idea-004 (logged in the same message), memory project-todo (reminder/follow-up pattern), memory project-tech-digest (Telegram bot that sends scheduled messages)]
---

## Hypothesis
Medical-aesthetics studios (医美工作室) handle client follow-ups (回访, e.g. post-treatment check-ins, rebooking
reminders) and client records (资料留存, e.g. treatment history, photos, notes) mostly by hand. A product that makes
this easier would solve a real pain. The user said they want to build it as a to-C product.
User's words (2026-10-24): "想做一个医美的管理系统，它的痛点主要是现在的就是一些医美工作室对于客户的回访，或者是客户的资料的留存是比较手动的，然后就是想做一个 to C 的产品。"
Basis: the user's own idea, one conversation, no data (source of the pain observation unknown — personal experience, a friend's studio, or general impression).

Not specified yet (unknown, to be found in test):
- Who uses it and who pays: the studio and its staff, or the studio's clients (the end consumers). The pain as described sits with the studio; the user said to-C. See open question 1.
- Region / market (Singapore, China, elsewhere) — affects tools in use (WhatsApp vs WeChat), data-protection law, competitors.
- Studio size (solo practitioner, small studio, chain) and what they use today (paper, Excel, WeChat/WhatsApp chats, an existing booking system).
- Which follow-ups matter most (post-treatment care check, next-session reminder, birthday / promotion, review requests).
- What "client records" must include (photos, consent forms, treatment/product batch details) and any rules on storing them.

## How to test
- Data / tools needed: access to 5-10 studios (owners or front-desk staff) and 5-10 of their clients; desk research on existing studio software and consumer apps; a simple concierge setup (spreadsheet + scheduled WhatsApp/WeChat/Telegram messages, drafts written by Claude).
- Steps (proposal, for the user to confirm):
  1. Decide the target user for the first test (studio vs consumer), per open question 1.
  2. Desk research: existing tools and prices. Candidates to check (from memory, unverified): general salon/spa booking + CRM (Fresha, Vagaro, Zenoti, Mangomint), aesthetics-specific clinic systems (Aesthetic Record, Pabau), and in China 美业 SaaS and consumer platforms such as 新氧. Note what they do for follow-ups and records, and what reviews complain about.
  3. Interviews: 5-10 studios — walk through their real follow-up and record-keeping process, time spent per week, what gets missed, what they already pay for software. If consumer side: 5-10 clients — do they want to keep their own treatment history / reminders, and would they use an app for it.
  4. Concierge MVP with 1-2 studios for 4 weeks: user (with Claude drafting messages) runs their follow-ups from a spreadsheet; measure follow-ups sent on time, client replies, rebookings, staff time saved.
- Success criterion (PROPOSAL, user to confirm before step 3):
  - Studio side: at least 3 of 10 studios describe follow-ups/records as a top-3 problem AND say they would pay at least an agreed monthly price (amount to set after desk research on competitor prices); at least 1 studio keeps using the concierge MVP for the full 4 weeks.
  - Consumer side (if chosen): at least 3 of 10 clients say they would install an app for their own records/reminders, and at least 2 actually use a prototype (even a shared spreadsheet/bot) for 2 weeks.
- Failure criterion (PROPOSAL): fewer than 2 of 10 studios (or clients) rank this as a real problem, or studios already use a tool that covers it and are satisfied, or no studio continues the concierge MVP past 2 weeks.
- Rough cost: desk research ~2-3h; interviews ~1-2 weeks of calendar time (mostly finding studios); concierge MVP ~1-2h per week per studio for 4 weeks; money ~S$0.

## Money path (if any)
Unknown, to be found in test. Possible paths to check (not yet verified):
- Studio pays: monthly SaaS subscription per studio or per seat; setup fee; add-ons (automated messaging, marketing).
- Consumer pays: app subscription — or free for consumers, paid by studios to be listed / to receive bookings.
- Commission on rebookings driven by follow-ups.
Who pays: unknown (depends on open question 1). What can be lost: build time; sensitive client data (photos, medical details) if leaked — data-protection obligations (e.g. Singapore PDPA, China PIPL) to be checked.

## Open questions (to test, not judgments)
1. Who is the user and who pays — studio (to-B) or the studio's clients (to-C)? Evidence needed: the user's intent, then interviews on both sides (step 3) to see where the pain and willingness to pay are.
2. Where did the pain observation come from, and how common is it? Test: interviews — count how many studios run follow-ups by hand and how much time it takes.
3. Do existing systems (step 2 list) already solve follow-ups/records, and why do these studios not use them (price, language, too complex, WhatsApp/WeChat integration)? Evidence needed: pricing pages, reviews, interview answers.
4. What rules apply to storing client photos and treatment records in the target region (medical vs non-medical aesthetics may differ)? Evidence needed: regulator guidance / PDPA or PIPL text.
5. Which channel do clients actually respond on (WhatsApp, WeChat, SMS, phone call)? Test: reply rates per channel in the concierge MVP.

## Log
- 2026-10-24: created from the user's description (one message, logged together with idea-004). No desk research yet.

## Result
