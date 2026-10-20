# First-time profile progression and optional objectives

AL.Progression extends the existing Achievements and Quests & Objectives screens; it does not replace legacy quest rewards, designer collection achievements or survival/healthy-care rewards.

| First-time milestone | Keeper XP | AC | Stable identity |
|---|---:|---:|---|
| Newly owned biological species |50|50|first-species:<host>:<canonical catalog ID>|
| First ownership of a catalog size category |100|250|first-size:<size catalog ID>|
| First successful diving destination |50|50|first-destination:<mode>:<region ID>|

Awards are automatic after valid permanent ownership or successful expedition completion. The first starter aquarium counts for a genuinely new marine profile: opening balance5000 AC plus a separate 250-AC achievement receipt and100 XP. Eggs do not count before hatch; temporary expedition inventory, observations, failed receiving and dead transport results do not count. Nursery animals enter this award at the modeled larval/hatch stage, not an unhatched embryo. The same observation runs after actions and chronological simulation, so store, received diving livestock, hatching, breeding and other legitimate ownership paths converge.

Fish use canonical biological identity; designer patterns, sex and stages do not create new biological species. Named implemented corals/invertebrates use their existing scientific/catalog identity. Unverified legacy groups such as Zoanthus spp. are not invented as unique biological species. All acquisition holds remain. Captive breeding currently produces existing species; it does not invent hybrids for a reward.

Size categories are catalog IDs, independent of display rounding and water classification. Reliable old freshwater size ownership backfills shared history without enabling freshwater interaction or changing biology. Reef and Deep modes are explicit subdestinations: the 12 implemented regions yield16 mode/region destinations (four original regions support both; seven added regions reef-only; Mariana deep-only). Repeating either exact destination earns nothing. Successful empty expeditions count when the existing expedition authority records success; failure/abandonment does not.

Old saves backfill known ownership from current residents, authoritative discovered fish/invertebrates, reliable identified purchase/sale receipts, coral lineage, owned catalog sizes/prior tank purchase receipts and successful expedition history. Backfilled records are known-before-update, with no invented unlock time, historical AC receipt or retroactive XP/cash. Missing older history cannot be reconstructed. Future earned records save profile ID, achievement ID, subject, unlock time, status, XP, AC, award time and actual Finance transaction ID. Financial idempotency keys and the retained subject set survive sales/rebuying, reload and repeated routes. If the existing wallet/XP cap blocks payment, the unlock waits as pending and is paid once when capacity exists; it never breaks biological simulation or invents a historical payment.

Thirteen additional objectives show persistent best progress and completion timestamps, with **no extra AC or XP**: three cycled filters; fifty meals; ten prepared water changes; one safe supported coral frag; one natural spawning event; five hatchlings; three distinct reef destinations; one deep expedition; three equipment service/part events; five installed devices; three size categories over time; ten biological species; seven game days of safe water. Existing rewarded quests retain their amounts. No objective asks players to injure livestock. Runtime registry: js/progression.js; schema: ECONOMY_UPDATE_SAVE_SCHEMA.md.
