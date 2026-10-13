---
name: project-opportunity-scan-2026-10
description: 2026-10-13 scan of other Bittensor subnets and Virtuals ACP as income options — measured facts, candidates, what is still unverified
metadata:
  type: project
---

Data lives in ~/lab/bittensor/data/{subnets.json,panel.jsonl,identities.json} and ~/lab/virtuals/agents.jsonl (public ACP registry pull, 44,062 agents, read-only API https://acpx.virtuals.io/api/agents?pagination[page]=N&pagination[pageSize]=100).

**Virtuals ACP (measured 2026-10-13):** only 2,275 of 44,062 agents ever had a successful job; 1,438 have revenue>0; lifetime revenue total $3.92M, top 10 = 57%, top 100 = 97%, #100 earns $2,580, #500 earns $4.52; 321 agents active in last 30 days; 123 graduated (graduation = 10 successful sandbox jobs). 39,940 agents were created Feb-Mar 2026 (incentive spike); agents created since May 2026: 2,095 with ZERO successful jobs. Last-activity per month collapsed after April (May 101, Jun 65, Jul 33, Aug 27, Sep 24, Oct 17). Offer prices of agents with >=10 jobs: median $0.02, p90 $4.2. Data/scraping/research-keyword agents: 1,882, only 34 with revenue>=$100. Provider side needs ETH gas + USDC on Base, no VIRTUAL needed. Fee: 60% of job to provider (older source).

**Bittensor subnet scan (128 subnets, TAO $275):** SN13 median miner pay $4.69/day, p10 $1.90, burn $3.24, 246 miners, 139 coldkeys, ~61 new registrations/day. Other low-burn subnets with flat plateau pay: SN33 ReadyAI (CPU-only possible, needs LLM API e.g. GPT-4o; median $12.06, p10 $8.30, burn $14, 19 coldkeys), SN101 Tag101 (tags X posts via OpenAI; median $14.91, p10 $2.23, burn $8.8, 17 coldkeys), SN32 ItsAI (median $9.12, burn $14.6), SN83 CliqueAI (algorithmic max-clique; median $20.5, p10 $3.9, p90 $52, burn $27, 17 coldkeys), SN22 Desearch (crawl pages; median $3.19, burn $2.6), SN105 Beam (bandwidth; median $8, burn $5.4, 147 coldkeys). Many subnets are dominated by a few coldkeys running ~14 miners each. Not yet verified: per-task LLM/API cost, real hardware needs, whether a fresh miner reaches the plateau. SN13 itself: paid Apify scraping cost ($1.5-9/day) is >= plateau pay ($4.7/day).
