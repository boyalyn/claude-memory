---
name: project-japan-trip-2026-11
description: "User's 2026-11-08..15 Japan trip (Shanghai->Tokyo->Kyoto->Osaka->SIN): Tokyo+Kyoto hotels booked, Osaka hotel and return flight open; active trackers 2,12,13"
metadata:
  node_type: memory
  type: project
  originSessionId: 3882c9d7-69bd-54ea-908e-bfea8dead8f2
  modified: 2026-10-27T04:59:58.958Z
---

Trip plan as of 2026-10-26 (user travels alone as far as known; all searches used adults=1):
- 11-08 Shanghai -> Tokyo: **booked** (user did not say which flight). JL80/JL82 watch cron removed ([[project-flight-watch]]).
- Tokyo 11-08 -> 11-10: **booked** Richmond Hotel Premier Asakusa International.
- Kyoto 11-10 -> 11-13 (3 nights): **booked 2026-10-29** THE GATE HOTEL Kyoto Takasegawa by HULIC (user booked it themselves via the official site link; Google Hotels showed S$379/night that day; plan/price actually paid not told). Before booking: User likes Gion Crystal Hotel (祇園クリスタルホテル, S$210/night on 10-26; 16-17 m2 rooms; breakfast only on 朝食付き plans). Budget about S$200/night. Rejected: Arashiyama (too quiet), Celestine (over budget). 5-stars were over budget at S$338+/night, but on 10-26 the user asked to watch two of them for price drops (trackers #10/#11).
- Osaka 11-13 -> 11-15 (2 nights, Namba): not booked. Shortlist: Toyoko Inn Osaka Namba S$151, Super Hotel Premier Namba S$204, Sotetsu Fresa Inn Osaka-Namba S$219.
- Return Osaka -> SIN 11-15: not booked (to-do #14; tracker #2, about S$685 vs target S$500).
- User decided not to rent a car.

Travel MCP trackers (max 5; active after 2026-10-29: #2, #12, #13; #6 and #7 stopped 2026-10-29 at user request), as of 2026-10-26 10:00 SGT: #2 flight; #6 Sotetsu Fresa (location "Namba Osaka", target 218, works: S$219 on 10-26); #7 Super Hotel Premier Namba (target 203; got null on 10-26 because the hotel is not in the unfiltered results for "Namba Osaka", "Shinsaibashi Osaka", "Super Hotel Namba Osaka" or "Super Hotel Premier Osaka"; the user has not decided what to do with it yet); #10 (stopped 2026-10-29 after Kyoto booked) THE HOTEL HIGASHIYAMA KYOTO TOKYU (location "Higashiyama Kyoto", target 349; S$350 on 10-26); #11 (stopped 2026-10-29 after Kyoto booked) THE GATE HOTEL Kyoto Takasegawa (location "Takasegawa Kyoto", target 379; S$380 on 10-26). #8/#9 (location "Kyoto") got null and were replaced by #10/#11. #4 Gion Crystal and #5 Toyoko Inn were stopped 10-26 at the user's request. Targets are set S$1 under the latest price. Daily check 09:00 SGT, alerts go to @boya_assist_bot. Stop the hotel trackers once booked or after the stay dates; stop #2 after the return is booked.

2026-10-27 check (Kyoto 11-10..13, adults=1): trackers #10 and #11 both returned null at the 09:03 SGT run, but manual search_hotels with the same locations found them: Tokyu S$330/night (below target 349, no alert because of the null), Gate S$379. Gion Crystal did not appear in searches "Gion Crystal Hotel Kyoto" or "Gion Kyoto" (max_price 260). Cause of tracker nulls not investigated yet.

2026-10-29 check (Google Hotels via Travel MCP, adults=1, SGD/night): Gion Crystal found only via Japanese name "祇園クリスタルホテル 京都" (also appears under "Higashiyama Kyoto" stars [4,5]): S$210, same as 10-26. Tokyu (Pan Pacific) S$340. The Gate (search "Takasegawa Kyoto") S$379, total S$1137, 4.5 (1163 reviews). Osaka 11-13..15 (Fri+Sat nights): tracker #6 Sotetsu Fresa read S$179 on 10-28 then null on 10-29, and manual searches (English and Japanese names) did not return it; Toyoko Inn Namba not returned either; "Super Hotel Premier Namba Shinsaibashi Natural Hot Spring" S$337 (10-26 note had S$204; same property not confirmed). Other Osaka prices seen: Comfort Hotel Osaka Shinsaibashi S$170, APA Namba-ekihigashi S$202-208, APA Hotel&Resort Namba Ekimae Tower S$215, Meander Osaka S$255, KOKO Hotel Shinsaibashi S$241, Vessel Inn Namba S$287. Flight tracker #2 S$617 on 10-29.

2026-10-29 Osaka trackers added at user request ("还有两周多", keep watching Osaka): #12 Comfort Hotel Osaka Shinsaibashi (location "Shinsaibashi Osaka hotel", target 169, S$170 that day) and #13 "APA HOTEL＆RESORT OSAKA NAMBA EKIMAE TOWER" (full-width ＆; location "Namba Osaka", target 214, S$215). Both created with adults=1 and hotel_name copied exactly from Google's result name, after an unfiltered search_hotels with that location returned the hotel. Server code was not read (from boya-server, trader cannot read /srv/mcp and root SSH is refused).
2026-10-30 09:03 SGT first run: #12 and #13 both null even with exact Google names. Manual unfiltered search_hotels right after (same location, adults=1) did not list either hotel at all: the unfiltered result list changes day to day (hostels/vacation rentals fill it), so the null means the hotel was not in that day's list. With filters (min_rating 4, max_price 260, sort reviews) "Namba Osaka" still listed APA Ekimae Tower at S$215; "Shinsaibashi Osaka hotel" with min_rating 4, max_price 250 did not list Comfort (reason unknown: price above 250, sold out, or ranking). #2 flight S$618 on 10-30.

Related: [[project-todo]], [[project-mcp-servers]], [[reference-notification-channel]].
