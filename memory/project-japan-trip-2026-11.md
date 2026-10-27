---
name: project-japan-trip-2026-11
description: "User's 2026-11-08..15 Japan trip (Shanghai->Tokyo->Kyoto->Osaka->SIN): what is booked, shortlisted hotels, active price trackers 2,6,7,10,11 to stop after the trip"
metadata:
  node_type: memory
  type: project
  originSessionId: 3882c9d7-69bd-54ea-908e-bfea8dead8f2
  modified: 2026-10-27T04:59:58.958Z
---

Trip plan as of 2026-10-26 (user travels alone as far as known; all searches used adults=1):
- 11-08 Shanghai -> Tokyo: **booked** (user did not say which flight). JL80/JL82 watch cron removed ([[project-flight-watch]]).
- Tokyo 11-08 -> 11-10: **booked** Richmond Hotel Premier Asakusa International.
- Kyoto 11-10 -> 11-13 (3 nights): not booked. User likes Gion Crystal Hotel (祇園クリスタルホテル, S$210/night on 10-26; 16-17 m2 rooms; breakfast only on 朝食付き plans). Budget about S$200/night. Rejected: Arashiyama (too quiet), Celestine (over budget). 5-stars were over budget at S$338+/night, but on 10-26 the user asked to watch two of them for price drops (trackers #10/#11).
- Osaka 11-13 -> 11-15 (2 nights, Namba): not booked. Shortlist: Toyoko Inn Osaka Namba S$151, Super Hotel Premier Namba S$204, Sotetsu Fresa Inn Osaka-Namba S$219.
- Return Osaka -> SIN 11-15: not booked (to-do #14; tracker #2, about S$685 vs target S$500).
- User decided not to rent a car.

Travel MCP trackers (max 5, all slots used), as of 2026-10-26 10:00 SGT: #2 flight; #6 Sotetsu Fresa (location "Namba Osaka", target 218, works: S$219 on 10-26); #7 Super Hotel Premier Namba (target 203; got null on 10-26 because the hotel is not in the unfiltered results for "Namba Osaka", "Shinsaibashi Osaka", "Super Hotel Namba Osaka" or "Super Hotel Premier Osaka"; the user has not decided what to do with it yet); #10 THE HOTEL HIGASHIYAMA KYOTO TOKYU (location "Higashiyama Kyoto", target 349; S$350 on 10-26); #11 THE GATE HOTEL Kyoto Takasegawa (location "Takasegawa Kyoto", target 379; S$380 on 10-26). #8/#9 (location "Kyoto") got null and were replaced by #10/#11. #4 Gion Crystal and #5 Toyoko Inn were stopped 10-26 at the user's request. Targets are set S$1 under the latest price. Daily check 09:00 SGT, alerts go to @boya_assist_bot. Stop the hotel trackers once booked or after the stay dates; stop #2 after the return is booked.

2026-10-27 check (Kyoto 11-10..13, adults=1): trackers #10 and #11 both returned null at the 09:03 SGT run, but manual search_hotels with the same locations found them: Tokyu S$330/night (below target 349, no alert because of the null), Gate S$379. Gion Crystal did not appear in searches "Gion Crystal Hotel Kyoto" or "Gion Kyoto" (max_price 260). Cause of tracker nulls not investigated yet.

Related: [[project-todo]], [[project-mcp-servers]], [[reference-notification-channel]].
