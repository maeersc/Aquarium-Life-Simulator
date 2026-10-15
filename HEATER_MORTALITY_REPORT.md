# Heater and permanent mortality update - v3.6 / MDP v3.9

2026-10-15. Implements the heater investigation, permanent livestock mortality specification, and the player's follow-up request for different heater levels through 15,000 gallons. Saltwater only.

## Confirmed findings and limits of the diagnosis

The supplied post-loss readings cannot identify the previous heater state or every individual cause. No player save, historical death record, or deployed-build version was supplied. The player confirmed they do not know the prior heater rating/condition/state. No actual player save was opened, altered or restored.

Confirmed source behavior: a thermostat value of 25 C is only a target. The previous model used a 22 C room and an equilibrium capped by enabled, positive-durability heater capacity relative to water volume. A missing, disabled or failed heater has zero output and the tank approaches 22 C. A moved/undersized or worn heater can also fail to reach its target. Purchasing legacy equipment auto-sized it for the original destination; transfers correctly preserved the old capacity. The UI did not make actual heater state/rating/condition clear enough to the player.

No offline-only heater shutdown or duplicate ordinary temperature/starvation update was reproduced. The archived original thermal code maintains approximately 25 C with properly sized working heat and matches its continuous reference in all 21 comparisons. It also reproduces 22 C with disabled/failed/missing heat. This is a confirmed reproduction of possible mechanisms, not proof of which occurred in the player's old aquarium.

Confirmed UI defect: In balance only used general ammonia/nitrite/nitrate/oxygen thresholds and cycling. It omitted resident temperature suitability and surviving-stock status, so an entirely deceased aquarium with normal current chemistry could still appear balanced. The new status separates general chemistry from suitable resident conditions and explicit empty/no-living-stock states.

Confirmed diagnostic gaps: v3.5 retained only a 200-event gameplay ring and sampled chemistry; it lacked a permanent separate account journal, complete fatal health/heat metadata, live/offline wall-time context, detailed hourly history, run/error audits, filtering and standalone log exports. Those gaps are repaired without inventing old evidence.

## Heater products and calculations

| Equipment level | Advertised tank range (US gallons) | Fixed rating | Price (AC) |
|---|---:|---:|---:|
| 1 | 5-20 | 20 gal | 110 |
| 2 | 20-75 | 75 gal | 209 |
| 3 | 75-250 | 250 gal | 694 |
| 4 | 250-1,000 | 1,000 gal | 2,776 |
| 5 | 1,000-3,000 | 3,000 gal | 8,328 |
| 6 | 3,000-7,500 | 7,500 gal | 20,820 |
| 7 | 7,500-15,000 | 15,000 gal | 41,640 |

These are heater product levels, not new keeper-level gates. Ratings are exact liters = upper US gallons x3.785411784. New prices reuse the existing heater price scale. All models share the existing heater stock and one-installed-heater constraint. The store recommends the smallest fitting level and blocks undersized new purchases; the destination selector offers other eligible aquariums. Larger heaters still obey thermostats. Transferring/removing/reinstalling gear preserves fixed capacity/model. Legacy saves and legacy APIs keep existing ratings and prices; no automatic upgrade, new charge or refund.

Main tank vitals now show heater on/off/failed/missing, level/rating and condition. Equipment > Tank Care and inspection show actual water separately from target, model/range or legacy rating, condition-adjusted capacity, available/delivered watts and inability to maintain target. A worn or disabled heater never supplies fictional power.

For marine game-hour step h: ambient A=22+0.4 x actual light, heat loss k=0.09 sqrt(75/volume), passive temperature P=A+(T-A) exp(-kh), gain G=(1-exp(-kh))/k. Each operational controller has maximum rate R=8k x effective capacity/volume. Demand is (setpoint-P)/G for heat or (P-setpoint)/G for cooling, clamped to [0,R]. New T=P+G(delivered heat-delivered cooling). Nominal watts follow the existing equipment definition, with condition and thermostat duty applied. This replaces Euler movement toward a pre-capped equilibrium with explicit bounded delivery and exponential exchange. It does not force 25 C, add a separate electrical grid, ignore wear, or change freshwater thermal biology. Rates/watts are game calibration, not a real-world sizing prescription.

Actual heater maintenance/wear and other equipment continue in every ordered live/offline step. The 20-real-minute day remains:8/12/24 real hours =24/36/72 game days. Hunger, compatible food, finite grazing/scavenging, disease, oxygen, age/predation, mineral budgets and +50/+100 reward rules from v3.5 remain; logs distinguish these causes instead of always blaming temperature. Ammonia/nitrite/nitrate and benthic thermal/oxygen/salinity damage contributions are now separately named without applying additional damage.

## Permanent mortality authority and evidence

The existing AL.Mortality is extended as the single authority. Every individually modeled marine fish/coral/benthic/nursery death uses the same confirmed-loss hook once. A canonical account/individual event ID and existing death flags prevent repeats; ordinary catch-up still has its ownership/replay guards. Transaction drafts defer permanent writes until successful validation, so a rejected action cannot leak a false death. Logging creates no financial entry, charge, compensation or second recovery interval.

Each detailed record preserves identity/common/scientific name where known/category/rarity/stage/age units; actual simulated step/day/time and preceding interval; mapped real death time distinct from capture/login time; live/offline/run context; fatal health before/after/maximum and applied loss; hunger/nutrition/last consumed meal/last observed healthy time; disease/medication/stress/behavior; actual chemistry, heater target/output/condition/model, volume/bacterial/bioload state, food inventory and damage contributors. Coral tissue/bleaching/polyps/light and bottom diet/substrate are included. A low-viability nursery records its actual viability before death, not a false 100 HP. Unknown old fields stay unavailable and uncertain causes are Unknown.

Each tank keeps 50 hourly condition samples and 100 recent care events. After sufficient observation the samples cover at least48 game hours. The permanent event copies only its own individual window with water/heater trends and recent relevant events. Death-time chemistry is a separate exact snapshot before new decomposition/cleanup. Logging cannot reconstruct pre-installation history. High activity may evict older care events while sampled health/disease severity trends remain.

Dedicated account-local browser keys archive individual v2 events and offline-run audits; persisted records are not automatically pruned. Main game saves retain the latest200 archived events/20 runs plus every unpersisted pending item for portability/retry. Storage failure warns and preserves pending data rather than silently discarding it. Unreadable journal entries stay protected. Browser storage remains finite and clearing it can erase data; export both game and complete journal before changing profiles. Ordinary game backup alone is not an unlimited journal archive. No credentials or whole gameplay object is exported as diagnostics. Full schema: [MORTALITY_LOG_SCHEMA.md](MORTALITY_LOG_SCHEMA.md).

Offline audits contain start/target real and game times, expected/processed game minutes, step count, initial/final equipment, running/completed/error status and actual error text. Death real timestamps map into the absence interval; they are not all assigned the return timestamp. A running checkpoint without completion remains an incomplete attempt, not a fabricated success.

Field Journal > Tank History > Livestock Deaths offers aquarium/species/cause/date/game-day/live-offline filters, full reports, Export Mortality Log and Export Selected Death Report. Welcome Back gives the newly recorded count and View Death Reports scoped to its offline run. Exports download LIVESTOCK_MORTALITY_LOG.json and LIVESTOCK_DEATH_REPORT.json locally. No debugging layer remains over the aquarium.

## Measured thermal matrix

One lightly stocked, mature 1,000 L tank, normal other chemistry, actual functioning equipment and ample compatible supplies except the stated challenge. Initial temperature22 C, setpoint25 C; lights off isolates the22 C ambient. Weak heat is rated75 L. Proper is1,000 L and oversized2,000 L. Shortage has only2pellet rations. Each cell gives final temperature / living fish (initial1).

| Case | 8 h /24 game days | 12 h /36 game days | 24 h /72 game days |
|---|---|---|---|
| proper | 25.000 C / 1 | 25.000 C / 1 | 25.000 C / 1 |
| oversized | 25.000 C / 1 | 25.000 C / 1 | 25.000 C / 1 |
| weak | 22.427 C / 0 | 22.333 C / 0 | 22.053 C / 0 |
| disabled | 22.000 C / 0 | 22.000 C / 0 | 22.000 C / 0 |
| failed | 22.000 C / 0 | 22.000 C / 0 | 22.000 C / 0 |
| missing | 22.000 C / 0 | 22.000 C / 0 | 22.000 C / 0 |
| shortage | 25.000 C / 1 | 25.000 C / 0 | 25.000 C / 0 |

All21 repaired physical continuous/offline comparisons match exactly; all21 original thermal comparisons also match. Proper/oversized fed cases survive every duration at25 C. Weak/absent/failed cases still permit actual cold-water deaths with normal chemistry and modest hunger. The shortage case survives8h but dies from prolonged severe malnutrition in longer absences despite25 C, so the logger does not automatically blame the heater. This matrix does not promise every stocking scenario will survive.

| 8-hour challenge loss | Actual recorded cause | Death temperature | Hunger | Ammonia | Oxygen |
|---|---|---:|---:|---:|---:|
| weak | Extreme temperature | 22.549 | 35.78 | 0.0000 | 7.716 |
| disabled | Extreme temperature | 22.000 | 32.30 | 0.0000 | 7.793 |
| failed | Extreme temperature | 22.000 | 32.30 | 0.0000 | 7.793 |
| missing | Extreme temperature | 22.000 | 32.30 | 0.0000 | 7.793 |

Each of the seven products additionally survives eight hours in the largest existing catalog aquarium within its rating, including the actual15,000-gallon aquarium. The existing60-pair absence matrix also exercises 20min/2h/8h/12h/24h mixed fish, photosynthetic/NPS coral, grazing/scavenging, juveniles and multiple aquariums. New diagnostic metadata naturally differs between live and offline; comparisons exclude only wall/capture timestamp, context and run ID while preserving actual biological/chemical/food/reward/death-step comparisons.

## Tests, preservation and delivery

Reproduce with python tests/browser_qa.py chrome --heater or edge --heater. Tests cover direct fish/coral/invertebrate/nursery losses; identity; one record; fatal health, disease and actual heat versus setpoint; >48-hour history; old/current migration and corpses; permanent overflow beyond200, storage quota retry, rejected draft writes, account isolation, repeated return, actual browser reload and real offline JSON downloads; offline completion/error audit; finite starvation; all products, prices, model validation, weak-purchase rejection and fixed transfer; responsive real UI and filters. The original thermal module is archived under planning/heater-mortality and replayed separately for comparison.

The measured representative mixed 24-game-day run took 357.9 ms in the recorded Chrome fixture; this is a local single-run measurement, not a hardware-wide performance guarantee. All 1419 original runtime assets and js/data.js remain SHA-256 unchanged. No livestock species or art was added, and previous approvals/holds remain. The ten-day protected freshwater replay is part of the shared regression suite.

New runtime files: js/heaters.js, js/thermal.js, js/mortality-journal.js and js/mortality-ui.js. Integrated core/actions, simulation, health, invertebrates, expansion, marine care, nursery handling, offline progression, save validation/persistence, store/destinations and existing main/UI shells. Source evidence: planning/heater-mortality/preservation.json. Tests/build/package are updated.

Updated the complete31-section MDPv3.9, GAME_DESIGN, DEVELOPMENT_STATUS, UI_SPECIFICATION, BALANCE_REPORT, README, GITHUB_PAGES, PDF_WORKFLOW, save-schema/mortality documentation and full continuity source with both permanent38/35-entry rosters. Binary PDF regeneration remains the previously disclosed unsupported toolchain step; no old PDF is labeled current. Final measured suite and build/archive counts are recorded in TEST_REPORT.md, GITHUB_PAGES_BUILD_REPORT.md and tests/heater-evidence/release-verification.json.

## Remaining limitations

The player-specific historic cause is undetermined without old evidence; normal readings after loss do not rule out earlier stress, starvation or failure. The supplied deployment/build version was not available for inspection. No dead livestock was resurrected, no compensation granted, and no account/equipment/credit reset occurred. The repair applies to future/pending progression. New logs cannot recreate older missing deaths or unobserved history. Browser quota/profile clearing can remove local data; no backend/login/cloud recovery exists. Unhatched multi-egg brood viability remains an aggregate incubation model, not invented individual death identities; all individually modeled stages use the shared authority. Game heat/metabolism remain simplified calibrations. Firefox/fullscreen and unchanged artwork galleries were not rerun. Public GitHub deployment was not performed; upload the rebuilt DIST contents to update the hosted game.
