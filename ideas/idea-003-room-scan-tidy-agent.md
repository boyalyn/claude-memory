---
id: idea-003
title: Phone room scan -> AI agent plans a tidy, sustainable room, buys the items, and follows up
status: untested
created: 2026-10-17
updated: 2026-10-17
tags: [consumer-app, agent, vision, shopping, home]
related: [~/lab/shopping_mcp (existing Shopee/Amazon ordering MCP with user-approval links), ~/claude-memory/todo (reminder/follow-up pattern)]
---

## Hypothesis
Many people want a tidier home but don't know how to arrange it or keep it that way. An app where you scan your room
with the phone, a model like Claude analyses layout and clutter, proposes a concrete arrangement plus a routine that is
sustainable to maintain, buys the needed items (storage, organisers) for you, and keeps pushing the improvement over
time would be something many people need and would pay for.
Basis: the user's own intuition, one conversation, no data yet.

## How to test
- Data / tools needed: phone photos/video or a LiDAR scan of a few real rooms; a vision-capable model; the existing
  shopping_mcp for ordering; market data on existing apps (room-planning, decluttering, home-organisation apps) and their pricing/reviews.
- Steps (proposal, for the user to confirm):
  1. Desk research: who already does this (scan-to-layout apps, AI interior design apps, decluttering coaches/apps), what they charge, what reviews complain about.
  2. Manual prototype: scan 2-3 real rooms (user's own first), have Claude produce plan + shopping list + weekly routine; check whether the plan is actually usable and the items fit.
  3. Demand check: show the output to ~10 people in the target group; count how many would pay and how much.
- Success criterion (proposal, decide before testing): in step 2 the plan is followed and the room is still tidy after 2 weeks for at least 2 of 3 rooms; in step 3 at least 3 of 10 people say they would pay ≥ S$10 (or a commission on purchases is viable).
- Failure criterion (proposal): plans not usable without heavy manual correction, or fewer than 2 of 10 would pay.
- Rough cost: desk research ~2h; prototype ~1 day; demand check ~1 week of asking people.

## Money path (if any)
Possible: subscription for coaching/follow-up; affiliate commission on items bought through the agent; one-off plan fee.
Who pays: households / renters / students wanting a tidier space. What can be lost: build time; wrong purchases if the agent orders without approval (shopping_mcp already requires user approval links).
Unknown, to be found in test: willingness to pay, commission rates, competitors' pricing.

## Open questions (to test, not judgments)
- Does a phone scan give enough information (dimensions, what is inside drawers/cupboards) for a good plan?
- Does follow-up actually change behaviour, and what keeps people using it after the first tidy-up?
- Which existing apps already cover parts of this, and what do they not do?

## Log
- 2026-10-17: created from the user's description. Background desk research requested ("有空的话在后台评估").
- 2026-10-17: desk research added (background agent).

## Desk research 2026-10-17
Method: web search only (2026-10-17), no product built. Third-party numbers (revenue/users) are self-reported or from aggregators; marked where weak. "unverified" = could not confirm from a primary source.

### 1. Existing products
**A. Scan -> layout / floor plan**
- Apple RoomPlan (framework, free for devs): uses Camera + LiDAR, outputs USD/USDZ with dimensions of walls/cabinets etc. and detected furniture types. https://developer.apple.com/augmented-reality/roomplan/
- magicplan: floor plan from phone; free for 2 projects; Sketch US$12.99/mo (yearly $129.99), Report $39.99/mo, Estimate $89.99/mo -> mainly contractor market. https://www.magicplan.app/pricing
- Polycam: LiDAR/photogrammetry 3D scanner; Pro ~US$17.99/mo or $99.99/yr (sources disagree, another says $17-27/mo). https://learn.poly.cam/product-faqs/how-much-does-polycam-cost , https://www.trustradius.com/products/polycam/pricing
- 两者都只做“测量/建模”，不做整理建议、不做购物、不跟进。

**B. AI interior design / redesign**
- Interior AI (Pieter Levels): photo -> restyled render. Pro ~US$49/mo yearly or $99/mo monthly, no free tier. https://resources.rework.com/tools/ai-tools/best-ai-interior-design-tools-2026 . Revenue: ~$50K MRR in 2022, ~$600K in 2023 (aggregator, self-reported by founder). https://getlatka.com/companies/InteriorAI
- RoomGPT (open source, Hassan El Mghari): launched 2023-03-02; ~1M monthly visitors, ~$23K last monthly revenue, $168K profit in 6 months, "1.6M users" (case-study sites, unverified primary). https://www.indiehackers.com/post/case-study-interior-design-ai-saas-company-that-made-168k-in-total-profit-in-6-months-efff542b1e , https://www.starterstory.com/roomgpt-breakdown
- Planner 5D: 3D home design, claims 90M+ users (other pages say 64M/74M). https://planner5d.com/pages/about
- Homestyler: 3D/AI design platform, ~21M registered users. https://resources.homestyler.com/our-story/
- IKEA Kreativ: inside IKEA app, scan room (panorama + figure-eight; LiDAR improves accuracy), erase existing furniture, place IKEA items, add to cart. https://www.ikea.com/gb/en/customer-service/knowledge/articles/250fg37g-2498-40gg-916c-f27d354683f0.html , https://www.techradar.com/news/ikeas-new-iphone-app-can-delete-and-replace-your-old-furniture . Critique: unclear feedback about what's already in cart; less accurate without LiDAR. https://ixd.prattsi.org/2024/02/design-critique-ikea-kreativ-ios-app/
- 常见差评（AI design apps）：生成图扭曲房间几何、移动门窗、在墙上开洞、不能调整家具位置；订阅自动扣费/难取消。https://marlvel.ai/apps/ai-interior-design/reviews , https://marlvel.ai/apps/home-ai-ai-interior-design/reviews

**C. Decluttering / cleaning / inventory apps** (这一类与 idea 最接近)
- Settlewood: photo -> zones -> action plan, tidiness score updated per new photo, habit tracker (morning/afternoon/evening routines); from US$6.99 subscription; App Store launch 2026-04-28. No purchasing feature listed. https://peerpush.com/p/settlewood
- ClearNest: AI decluttering plan, 15-min daily tasks, before/after photos, reminders; US$4.99/mo or $49.99/yr; too few ratings to show. https://apps.apple.com/us/app/clearnest/id6738142826
- Declutter: AI Home Organizer (Emir Arikan): detects clutter, "suggests optimal room layout", after-preview, micro-tasks, streaks; released 2026-01-02; 4.6 stars from 7 ratings, <1,000 downloads (estimate). https://mwm.ai/apps/declutter-ai-home-organizer/6757100915
- Also: AI Tidy Nook (ADHD-friendly photo -> tidy plan) https://hunted.space/product/ai-tidy-nook ; Organz.ai https://indexator.ai/startups/organz-ai
- Tody (cleaning task scheduler): free, ~US$30/yr sync subscription (older: $6/yr Android). https://www.wilx.com/2025/11/11/what-tech-app-day-tody-app/ , https://mobilesyrup.com/2019/07/14/tody-cleaning-review/
- Sweepy (cleaning schedule): free + subscription ~US$2-3/mo. https://apps.apple.com/app/id1498897320
- Sortly: item inventory, business-focused; free 100 items, Advanced $24-49/mo. https://help.sortly.com/hc/en-us/articles/360035774271
- 通用替代品：人们已直接把房间照片丢给 ChatGPT 要整理方案；有人反馈最大的作用是“有人告诉我该做什么”的问责感（body doubling）。https://apartmenttherapy.com/ai-declutter-kitchen-drawer-37682668 , https://www.tomsguide.com/ai/i-used-chatgpt-to-help-me-with-my-spring-cleaning-and-it-made-the-job-so-much-easier , https://jennaredfield.substack.com/p/i-organized-and-decluttered-my-entire

**D. Professional organisers in Singapore**
- Hourly S$30-125; examples: The Declutter Professionals S$50/h (min 2h), Orderly S$65/h weekdays, Tidyupsg S$60/h (min 3h), Get Organised & Beyond from S$100/h; Your Tidy Half S$250 per 3h + S$80/h, **S$80 per 1h virtual session**. Typical process: client sends photos first, then site visit. https://www.womensweekly.com.sg/style/domestic-diva-awards/domestic-diva-2022-7-professional-home-organisersutm_sourcefacebookutm_mediumdc-social-sponsoredutm_campaignarticle , https://vulcanpost.com/633121/professional-organiser-declutter-50-an-hour (2022 figures; current prices unverified)
- Airtasker SG organising tasks: ~S$100-500, e.g. bedroom declutter + storage S$180, bomb shelter reorg S$150. https://www.airtasker.com/sg/services/organising/

### 2. Gaps (scan -> plan -> purchase -> follow-up)
- 没找到一个产品同时做齐四步。现有分布：scan+dimension（RoomPlan/magicplan/Polycam）；scan+设计+加购物车但只卖自家家具、不做整理和跟进（IKEA Kreativ）；photo+整理计划+习惯跟进但不量尺寸、不推荐/代购收纳品（Settlewood、ClearNest、Declutter AI）。
- 可能缺的：(a) 用真实尺寸选收纳品（“这个柜子 38cm 宽，买这款”）；(b) 在 Shopee/Amazon 上带用户批准的代购；(c) 新加坡 HDB 场景（小户型、bomb shelter、热湿防霉）的本地化。以上只是“没搜到”，不代表不存在（unverified）。
- 已存在的“跟进”只是 reminders/streaks/tidiness score；有没有长期留存数据——未找到（unknown）。

### 3. Money signals
- 同类 app 订阅价：decluttering apps US$4.99-6.99/mo（$49.99/yr）；cleaning schedulers US$2-3/mo；AI design US$49-99/mo；scan apps US$13-18/mo（见上）。
- Amazon.com Associates: Home / Furniture / Home Improvement 3.00%, Kitchen 4.50%, "All other" 4.00%; cookie 24h. https://affiliate-program.amazon.com/help/node/topic/GRXPHT8U84RAYDXZ
- Amazon.sg Associates: Home "8.50%" per a third-party list — unverified (official rate card needs login). https://uppromote.com/blog/affiliate-programs-in-singapore
- Shopee SG Affiliate: general 1.5-8% (third-party); Home & Living 4-7% (third-party, unverified); official blog: social-media orders 2% to 7%, Commission Xtra up to 40%, attribution window 7 days after click. https://shopee.sg/blog/shopee-affiliate-how-to-earn/ , https://uppromote.com/affiliate-directory/shopee/
- 粗算（假设，unverified）：一次整理买 S$60 收纳品 x 5% ≈ S$3 佣金/用户；对比人工 organiser S$50-100/h、虚拟咨询 S$80/h。
- 市场规模信号：RoomGPT/Interior AI 证明“拍照->AI 改造图”在 2023 有付费流量；decluttering 类 2026 新 app 的评分数很少（ClearNest 不显示、Declutter AI 7 条），说明这些新进入者暂时没有大量用户（基于评分数推断）。

### 4. Technical feasibility
- RoomPlan 给 dimensions + furniture types（需要 LiDAR iPhone/iPad Pro）；开发者报告 "Room size exceeded" 错误、扫描抖动不准；桌面上的小物件基本被忽略 -> 量不到抽屉/柜内/桌面杂物。https://developer.apple.com/forums/thread/775853 , https://itechcraft.com/blog/your-101-guide-to-using-apple-roomplan-api-for-your-next-app/
- VLM 能力：benchmarks 显示 GPT-4o / Claude 3.5 Sonnet 在 counting + spatial relations、occlusion、尺寸/距离估计上明显弱于人类；用参照物提示可提升估距准确率。https://arxiv.org/html/2412.12693v4 (SPHERE), https://arxiv.org/html/2504.15485v2 (CAPTURe), https://arxiv.org/pdf/2506.18385 (InternSpatial)。（较新模型的表现未测，unknown）
- 推论（未验证）：照片足以给“分区/丢什么/放哪里”这类定性建议（已有 app 和 ChatGPT 用户在用）；精确选尺寸的收纳品需要 LiDAR 或用户手量。
- 生成“整理后效果图”有扭曲门窗/几何的已知问题（见 1B 差评）。

### 5. Cheapest demand tests (cost rough, own estimates)
1. 手动服务帖：“发 3 张房间照片 -> 24h 内给整理方案 + Shopee 购物清单 + 2 周跟进”，先免费 5 人再标价 S$10-20；发 Carousell（services）、Reddit r/singapore / r/askSingapore、小红书“新加坡 收纳”。成本：S$0 + 每单 ~30-60 min 时间 + 少量 Claude tokens。
2. 用 Shopee affiliate 链接放购物清单，记录点击->下单转化（7 天窗口），直接测佣金收入。成本 S$0。
3. Landing page（Carrd/Framer，~US$0-19）+ waitlist，配 S$20-50 小红书/IG 投放，看 email 注册率。
4. 在 Airtasker SG 接/看 organising 任务，了解真实需求与定价（S$100-500 区间）。成本 S$0。
5. 跟进有效性：自己房间 + 2 位朋友，2 周后拍照对比 tidiness（对应本文件 “How to test” 第 2 步）。

### Evidence for / against / unknowns
- For: 人工 organiser 在 SG 有市场（S$50-125/h，含 S$80 virtual session）；有人已在用 ChatGPT 拍照整理并反馈有效；没搜到四步合一的产品；Shopee Home 佣金高于 Amazon.com Home 3%。
- Against: 2026 已有 ≥4 个 photo->declutter plan + habit app，定价 US$5-7/mo，门槛低；免费 ChatGPT/Claude 可替代核心功能；affiliate 每单佣金小（几 S$）；RoomPlan 限 LiDAR 设备且看不到小物件；VLM 空间推理有已知短板。
- Unknowns: 这些 decluttering app 的收入/留存；SG 用户愿付多少；跟进是否真的改变行为；Amazon.sg/Shopee Home 官方佣金；最新 Claude 模型对杂乱/尺寸判断的准确度。
