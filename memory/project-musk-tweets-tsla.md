---
name: project-musk-tweets-tsla
description: "~/lab/tsla-study Musk-tweets vs TSLA study (started 2026-10-12): data locations, frozen plans + hashes, user constraints on Apify, pending forward test"
metadata:
  node_type: memory
  type: project
  originSessionId: 9e0bf1b1-6f31-5c95-9ab3-76ec0eef0e49
  modified: 2026-10-13T05:33:49.222Z
---

Facts only; numbers live in the scripts' output and the PLAN_*.md files in ~/lab/tsla-study ([[feedback-no-judgments-in-memory]]).

**Where things are** (~/lab/tsla-study)
- Tweets: data/tweets.jsonl (Apify, 2018-01..2019-04, non-reply), data/tweets_gap.jsonl (Apify, 2023-01..2025-03-07, non-reply), data/kag_tw/all_musk_posts.csv (Kaggle dadalyndell, 2010..2025-04-13, ~75% of non-reply tweets in 2024). Tweet times are UTC.
- Prices: data/min/TSLA_1min.csv + TSLA_1D.csv (Kaggle yug201; 1-min stamps = ET + 5h, labels can be off by up to ~5 min; daily bars start 09:35 ET), data/spy/spy_1min_2008_2021_cleaned.csv (Kaggle rockinbrock; stamps = Mountain time, ET = stamp + 2h), Robintrack holders data/rh/, TSLA 8-K list data/tsla_8k.csv.
- Scripts: fetch_tweets.py (Apify, 30-day chunks, `START END [OUT]`), minute_event.py, oos_test.py, explore_train.py, explore_daily.py, explore_content_vol.py, explore_kw_groups.py, explore_news_split.py, explore_pretrend.py, explore_newsproxy.py, holdout_2025.py, holdout_pre2018.py.
- Frozen plans (sha256 in data/*.sha256): PLAN_TWEETS.md, PLAN_OOS.md (+Amendments 1, 2), PLAN_HOLDOUT2025.md, PLAN_PRE2018.md, PLAN_FORWARD.md.

**Apify**: token in ~/data-universe/.env (APIFY_API_TOKEN); account upgraded by the user on 2026-10-12; monthly cap $19, billing cycle restarts on the 12th; apidojo actor 61RPP7dywgiy0JPD0 costs about $0.43 per 1,000 tweets. data-universe (Bittensor) shares the account.

**User constraints**
- No Apify/X scraping until the Bittensor project finishes; then backfill 2025-04-14..today for the forward test defined in PLAN_FORWARD.md (frozen 2026-10-13, not yet run). Wait for the user's go-ahead.
- User wants exploration on training data 2018-2024 to be described, not turned into strategies; validation sets are single-use and the rule is frozen before looking. Do not fit rules on one year and run them on all later data.
- Real-money trading not intended.

**Open**: forward test (PLAN_FORWARD.md); possible DOGE study (Kaggle johnsmith44/dogecoin-price-data-elon-musks-tweets-2021) was offered, not started; SUMMARY.md of the study was offered, not written.
