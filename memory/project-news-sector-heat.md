---
name: project-news-sector-heat
description: 2026-10-10/11 news-heat -> sector ETF study (~/lab/news-etf): setup, data traps, tested results on 2009-2019 train period; test period 2020+ untouched
metadata:
  type: project
---

Idea: buy sector ETFs when news heat for the sector rises, exit when it fades (user request 2026-10-10). Code/data in ~/lab/news-etf (scripts: clean.py, weekly_sample.py, make_tiers.py, label.py, run_labels.py, classify_all.py, diag*.py, analysis2.py, diag_full.py).

Setup: FNSPID (Hugging Face Zihan1004/FNSPID, nasdaq_exteral_data.csv, streamed; covers 1999-2024-01, headlines are company-heavy, 2021-22 thin, ~half have no publisher). Split fixed in advance: train 2009-2019, test 2020-2023 locked and never loaded (no test prices downloaded, no test headlines labelled). Labels: Haiku via `claude -p --model haiku --setting-sources local` (uses Claude Code quota, hits the 5h session limit after roughly 7.5k-13k headlines per window; script waits through limits). 45,045 labels exist (2009-10 at 200/week, 2011-2018-09 at 60/week "tier A"; tier B backfill to 200/week never run).

Tested results (train period only, fixed thresholds):
- Haiku-label heat, 60 headlines/week: no excess return vs SPY after heat>1.5 at 4/8/12w (|t|<1.2); same after heat fades, with VADER tone, and with common-level demeaning.
- Split-half reliability of that weekly heat was only 0.09 (200/week would be 0.17): the measurement was too noisy to test anything. Do not buy more Haiku labels for this.
- Local TF-IDF+LR classifier trained on the Haiku labels (train 2009-15, validate 2016-18): per-ETF F1 0.53-0.72, weekly fidelity to Haiku 0.60 on the same headlines. Applied to all ~8M headlines: reliability 0.91; buckets still no significant excess return (z>2: +0.21%/4w t=0.67; z<=-1: -0.29%/4w t=-1.56); corr(heat, same-window return)=0.035.
- Price-only views (no return tests): at weekly heat, price position vs 52w high/26w avg and next-12w peak (median week 9, +5.9%) same as baseline; daily price path ±20 days around weekly signal: no difference (day+10 hot-base -0.55%, se 0.32).
- Daily heat (5d smoothing, z vs 252d, demeaned; weekend news->Monday; split-half reliability 0.82, ~3000 headlines/day): 260 hot events, hot-base price diff day+1 +0.11% (se 0.07), +2 +0.12, +5 +0.09, +10 +0.14, +20 +0.01; daily heat vs next-days price change corr 0.00-0.015 (band ±0.029). Script daily_heat.py; zero Claude quota.
- Heat is not seasonally adjusted (earnings-season composition not removed); XLC/XLRE have prices only from 2018/2015 (news about Google/Meta/Netflix was in XLK/XLY before 2018).

Traps hit: sample ids collided between pilot and weekly caches; pkill/pgrep -f matches own shell; GDELT DOC API rate-limits this machine's IP; FNSPID All_external.csv ends 2020-06.
Related: [[project-momentum-study]], [[feedback-goal-money-or-abandon]], [[feedback-no-judgments-in-memory]].
