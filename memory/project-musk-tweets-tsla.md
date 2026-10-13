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

**Apify**: token for this study is in ~/lab/tsla-study/.env (mode 600, git-ignored; fetch_tweets.py / fetch_forward.py read it). The Bittensor token was deliberately removed from boya-server and lives only on the VPS; do not look for it. Account upgraded 2026-10-12; monthly cap $40 (raised), cycle runs from the 12th; the Bittensor miner shares the account's cap and was spending ~$1/h on 2026-10-13. apidojo actor 61RPP7dywgiy0JPD0 cost about $0.4 per 1,000 tweets.

**User constraints**
- Scraping X/Apify only with the user's explicit go-ahead (he stopped it twice mid-run). Forward set was pulled on 2026-10-13 with his go-ahead: data/tweets_forward.jsonl, 7,888 tweets 2025-04-14..2026-10-13, cost about $3.2.
- User wants exploration on training data 2018-2024 to be described, not turned into strategies; validation sets are single-use and the rule is frozen before looking. Do not fit rules on one year and run them on all later data.
- Real-money trading not intended.

**Results run so far (numbers from the scripts)**: training 2018-2024 keyword-day 5d market-adjusted diff +110 bp (NW t 2.22). Holdout 2025-01..04 (69 days): +263 bp, s.e. ~198 (inconclusive). Pre-2018 (2012-2017, 1505 days): +42 bp, NW t 0.75 (inconclusive). Forward set (forward_eval.py, 371 signal days 2025-04-15..2026-10-06): -66.5 bp, NW s.e. 57 bp, t -1.17, perm p(diff>0)=0.61 (verdict per PLAN_FORWARD.md: inconclusive); pooled forward + 2012-17: -11.6 bp, s.e. 40. Earlier intraday rule (long 5h after a tweet) on 2019-04..2025-03: net -30 bp per event.

**Proposition P (user's own wording, 2026-10-13)**: keyword tweet -> buy 5 min later -> hold 5 h -> sell (x=5, y=5 chosen by the user from the 2018-2022 development grid, kwgrid_dev.py: +50 bp gross, 105 events). Frozen in PLAN_KWTRADE.md (hash in data/PLAN_KWTRADE.sha256), run once by kwtrade_eval.py: minute holdout 2023-01..2025-03-07, 64 keyword events, mean net -13.0 bp, 95% CI [-54.8, +23.7], verdict inconclusive; hourly-bar forward 2025-04-15..2026-10-13, 82 events, mean net -40.1 bp, CI [-94.9, +4.4], verdict per rule 'contradicted' (p(net>=0)=0.042).

**Data-quality facts (audit 2026-10-13, dq_audit.py / dq_rerun.py)**
- data/min/TSLA_1D.csv (Kaggle) is NOT adjusted for the 2020-08-31 5:1 split (prices before it are 5x yfinance's; 2020-08-24..28 show 5-day returns of about -80%). Use yfinance auto_adjust for daily prices. All training-period day-level scripts explore_daily/content_vol/kw_groups/news_split/pretrend/newsproxy used the Kaggle file; corrected rerun (dq_rerun.py): keyword-day 5d effect +90 bp (NW t 1.87) instead of +110 (t 2.22); volatility coefficient +73 bp (t 3.06) instead of +77. Clean TSLA~SPY daily beta 2018-2024 = 1.57 (1.53 had been frozen in later plans; negligible difference).
- Kaggle all_musk_posts.csv: 'original' rows (isReply != True) include unflagged replies; in 2018-01..2019-04, 225 of 227 Kaggle originals missing from the Apify non-reply set start with '@'. Drop text starting with '@' (kwgrid_dev_clean.py, kwtrade_eval_clean.py do this). Reply flag is NaN for ~20% of 2013-2017 rows. Kaggle completeness vs Apify non-reply tweets: 100% (2018-19), 88.5% (2023), 77.6% (2024), 66.7% (2025); 2020-2022 unchecked.
- TSLA_1min.csv: stamps = ET + 5h; bars run 09:35..15:54 ET (first and last 5 minutes missing), median 380 bars/day, 25 of 1804 days under 300 bars, no bad prices; pre-2018 minute stamps use a different convention (not used). Apify tweet times match snowflake-ID times within 1 s. SPY minute file has exact duplicate rows (harmless). Robintrack stamps are UTC.
- Rerun of proposition P with '@' tweets removed: dev grid has 66 keyword events (not 105), x=5,y=5 gross +45 bp, net CI [-3, +85]; holdout unchanged (64 events, net -13.0 bp, CI [-54.8, +23.7]); forward hourly 82 events net -40.1 bp, CI [-96.4, +4.6].

- Definition D2 (keyword in own text OR quoted tweet's text; PLAN_KWQUOTE.md, hash data/PLAN_KWQUOTE.sha256, kwquote_eval.py; exploratory second look at validation data already seen under D1): quote tweets are 16% of originals in 2018-2022 vs 70% (2023-25-03) and 83% (2025-04..2026-10). Results (net of 10 bp, x=5 min, y=5 h): TRAIN 81 events +25.2 bp CI [-11.4, +64.2]; VAL1 128 events -11.6 bp CI [-42.5, +18.1]; VAL2 (hourly) 220 events -26.3 bp CI [-68.0, +6.8]. Quoted-text-only events: VAL1 -10.3, VAL2 -18.0, TRAIN -16.2.
- data_compare.py: training vs validation differences (tweets/day 2.1 vs ~20; keyword share of tweets 17.8% vs 2.4%/4.9%; TSLA beta to SPY 1.46 vs 2.3; random-time 5h drift +4.3 vs +3.7 bp; s.e. of keyword mean 22 vs 19 bp; 2019-04..2022 tweets come only from Kaggle, completeness unchecked).
- Pending: a scheduled reminder (2026-10-13 17:08Z) to spot-check Kaggle completeness 2020-2022 with ~$0.1 of Apify once the account quota is back.

**Open**: possible DOGE study (Kaggle johnsmith44/dogecoin-price-data-elon-musks-tweets-2021) was offered, not started; SUMMARY.md of the study was offered, not written.
