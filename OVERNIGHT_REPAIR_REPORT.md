# Overnight mortality repair report - playable v3.5 / MDP v3.8

2026-10-15. Saltwater repair on the existing local offline browser game. No individual player save was supplied or opened; the investigation reproduces source-code faults using isolated deterministic fixtures. This establishes reproducible causes, not a retrospective diagnosis of unavailable player data.

## Root causes and original-code reproduction

The primary reproducible fault is food access combined with rapid direct starvation damage, even while ammonia, oxygen and temperature stay normal. Eight hours correctly advances 24 game days. The original code matched continuous play in all 60 comparisons, so an extra offline multiplier was not the cause in these fixtures.

1. Adult fish gained 30 hunger/day (immature fish 57.6/day, with extra anthias hunger). Direct starvation damage was max(0,H-85) x 0.16 HP/hour: up to 57.6 HP/day even with substantial nutrition reserves. Invertebrates used a 0.13 slope, up to 46.8 HP/day. Nonphotosynthetic corals used max(0,H-65) x 0.08, up to 67.2 HP/day before generic healing. Later malnutrition-condition damage could compound calorie deprivation.
2. The one daily feeder dispensed only the chosen food, regardless of every resident diet. A tank with 1,000 appropriate rations of each type still starved residents that could not eat its selected pellets. There was no actual natural grazing/scavenging resource pathway.
3. Coral-only tanks did not satisfy the feeder activation condition, leaving nonphotosynthetic colonies unfed.
4. Juveniles outgrew fry eligibility while an unchanged fry selection continued dispensing unsuitable food.
5. Every reef coral consumed the same skeletal mineral concentration budget, including soft corals, without tank-volume scaling. This was a separate chronic-care defect, not assumed to explain all losses.
6. Concurrent sync catch-up lacked the async ownership guard, and repeatedly added epoch checkpoints accumulated rounding error. Ordinary baseline catch-up did not double time, but re-entry and interrupted checkpoint handling needed hardening. A health-condition loop could reach zero and then apply treatment recovery in the same tick.

Original-code 8-hour loss observations (in-game days elapsed from fixture creation; water sampled at the death step):

| Scenario | Species | Day | Cause | Ammonia | Oxygen | Temperature | Nutrition |
|---|---|---:|---|---:|---:|---:|---:|
| mixed-feeder | watchman | 4.486 | Starvation | 0.0000 | 7.346 | 25.000 | 56.09 |
| mixed-feeder | lysmata-amboinensis | 4.951 | Starvation | 0.0000 | 7.354 | 25.000 | 48.19 |
| mixed-feeder | tiger-sand-conch | 6.465 | Starvation | 0.0000 | 7.357 | 25.000 | 42.29 |
| no-feeder | clown | 4.486 | Starvation | 0.0000 | 7.373 | 25.000 | 56.09 |
| coral-feeding | tubastraea-micranthus | 4.177 | Cause of death undetermined. | 0.0000 | 7.380 | 25.000 | 81.09 |
| juvenile | clown | 22.660 | Starvation | 0.0000 | 7.376 | 25.000 | 57.63 |

Original-code diagnostic gaps are real: the old coral loss has an undetermined cause. Its recorded hunger/normal water and the bypassed feeder reproduce the starvation pathway; the report does not invent an old explicit cause label. Full original continuous/offline results and chemistry min/max are in tests/overnight-evidence/chrome-before.json.

## Exact formula and behavior changes

Rates use GAME hours, never real hours. See MDP 14.1/14.2 for the authoritative shared rule and [all 213 current marine species/stage rates](planning/overnight-repair/species-rates.csv): 94 fish adult/immature pairs, 15 corals, 10 benthic entries. These are explicit game calibrations using existing species diets, activity, size and specialist overrides; they are not clinically verified starvation durations.

Let clamp01(x)=min(1,max(0,x)). Adult fish m=clamp((0.7+0.3*activity)*sizeFactor,0.65,1.6), sizeFactor=1.15 below 6 cm /0.8 above 20 cm /1 otherwise. Purple Queen/Bartlett anthias m=2.3; Blotched anthias m=1.8. Hunger/day=24m adult, 40.8m immature. Shrimp=19.2/day; other benthic residents=12/day. NPS coral=19.2/day, photosynthetic coral=0 calorie hunger. Stage fragility q=1.7 immature fish,1.3 young invertebrates,1 otherwise.

`calorieDamage/hour = 0.5 * q * clamp(m,0.7,1.6) * clamp01((H-85)/15) * clamp01((45-N)/45)`

Hunger alone no longer immediately removes health while reserves are adequate. Adult Ocellaris reaches at most 12 HP/day from this channel versus 57.6 before; stage/species variation remains. Existing physical total-damage dead bands remain (>0.15/hour fish, >0.1/hour invertebrates); the rate export gives maximum calorie contributions, not an unconditional daily deduction. Positive-health recovery still requires existing conditions. Nutrition change/hour is m*(-0.20 for H>70;+0.20 for H<45;-0.015 otherwise), plus actual consumed food benefits. Only this calorie pathway handles starvation; the malnutrition diagnosis retains symptoms/progression without second HP damage. Real disease/toxicity/stress/age/predation remain lethal.

Feeders check six persisted slots per game day at 01/05/09/13/17/21. They require installed, enabled, nonfailed hardware and real compatible stock. Select preferred compatible food or another stocked catalog diet. Fry becomes adult food on maturation. Coral-only tanks are eligible. Target hungry residents first; each real ration produces bounded targeted particles (40 per batch, up to 5 per individual,120 tank cap). Additional batches consume further rations. Manual feeding and existing pollution remain.

Finite algal growth/hour is min(0.5*volume/75*light, nitrate*(volume/75)*20, phosphate*(volume/75)*1000, remaining biomass capacity), only in mature lit hardscape with grazers. Capacity=min(30*volume/75,24*sum(grazer hourly hunger)). Growth removes matching N/P; grazing consumes biomass at up to 1.2*hourly hunger. Scavenging consumes actual organic material above 0.02 at up to 0.6*hourly hunger, with 50 biomass units per(volume/75) organic concentration unit. No free inventory or infinite food.

Photosynthetic coral keeps existing light/nutrient/flow dependence: nourished nutrition gain 0.15/hour scaled by bleaching; deficit loss 0.08/hour, progressive extra damage 0.3*clamp01((25-N)/25) HP/hour below 25 nutrition. NPS uses actual compatible meals and the shared reserve-gated calorie damage. Hungry/depleted NPS cannot use generic healing. Only stony/SPS/LPS colonies consume skeletal Ca/Mg/alkalinity, retaining the former per-colony coefficients scaled by75/actual liters. No fabricated chemistry reset.

## Mortality, time, preparation and preservation

Both catch-up entry points reject overlapping ownership. Every simulated interval still runs chronological <=5-game-minute steps for feeding, chemistry, equipment, health, disease, growth and rewards. Intermediate epoch checkpoints are anchored to the target minus remaining duration; resume rounds to a micro game minute to avoid floating timestamp replay. A repeated processed timestamp does nothing. Baseline and repaired loops both match their continuous counterpart exactly; interrupted durable resume is separately checked within 1e-6 for biology. No server/login account exists to process a second interval. Startup Continue, hidden return and restored state use the shared service.

Death is confirmed at zero health; living bleaching/stress is not death. Stop living feeding and disease/treatment events at zero. One loss event retains identity, species/tank, simulated terminal step and preceding interval, named modeled cause, hunger/nutrition/conditions, actual water/bacteria, operating equipment/durability, actual compatible food, damage contributors and recent warnings. Retain 200 events/account and 160 chemistry samples/tank (12-game-hour spacing); death water is independent of sampled/history/current water. Cause/conditions of older unobserved deaths remain unknown. UI explains this and never substitutes post-login water.

Equipment > Tank Care and Journal > Tank History show Overnight Readiness: real stock/approximate coverage, feeder, gear condition/forecast, cycle/water, vulnerable residents and actual natural foods. Estimates disclose batching, stage/competition and future-care uncertainty. They are not a Safe/guaranteed survival label. Welcome Back shows new losses and previously deceased residents.

Schema 2 stays intact with additive marineCareVersion1, forage/autoFeedSlot, mortality v1 and chemistry history. Normal local load attempts an exact once-per-account raw snapshot BEFORE migration; Settings can export it unchanged. If an extra copy cannot be retained, Welcome Back requests JSON export before Continue. No tank, wallet, identity, selection, corpse or old history reset; no automatic resurrection, refund or compensation. Timeline/financial import protections still restrict old restores. Browser quota/clearing/private mode and different site/profile origins remain limitations; JSON backup is the portable local option. No active player data was touched during this development.

## Absence matrix

Each cell is alive/initial, measured AFTER repair. All rows have normal initial water except explicitly failed-flow/immature-cycle challenges. Established fixture is 1,000 L, lightly stocked, 100% enabled gear at 2x capacity, mature bacteria, supported coral mounts and ample real supplies. No-feeder case removes that gear; shortage has only 2 pellet rations; failed-flow starts air/pump failed with O2=3 and includes SPS; disease starts established velvet. Photosynthetic and NPS colonies use separate dedicated tanks. Juvenile starts age 5/growth 0.08 and matures during progression. Multiple uses two separate aquariums.

| Scenario | 20 min / 1 day | 2 h / 6 days | 8 h / 24 days | 12 h / 36 days | 24 h / 72 days |
|---|---|---|---|---|---|
| healthy-feeder | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 |
| mixed-feeder | 7/7 | 7/7 | 7/7 | 7/7 | 7/7 |
| no-feeder | 1/1 | 1/1 | 1/1 | 0/1 | 0/1 |
| food-shortage | 1/1 | 1/1 | 1/1 | 0/1 | 0/1 |
| failed-flow | 2/2 | 1/2 | 1/2 | 1/2 | 1/2 |
| immature-cycle | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 |
| disease | 1/1 | 0/1 | 0/1 | 0/1 | 0/1 |
| coral-photosynthetic | 2/2 | 2/2 | 2/2 | 2/2 | 2/2 |
| coral-feeding | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 |
| grazers-scavengers | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| juvenile | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 |
| multiple | 2/2 | 2/2 | 2/2 | 2/2 | 2/2 |

Risk-case losses remain traceable:

| Scenario | Species | Game day | Actual modeled cause |
|---|---|---:|---|
| no-feeder | clown | 26.694 | Prolonged severe malnutrition |
| food-shortage | clown | 30.625 | Prolonged severe malnutrition |
| failed-flow | sps | 2.170 | Sustained coral environmental stress |
| disease | clown | 3.486 | Marine velvet |

The immature-cycle challenge self-stabilized at this light load with working filtration; the simulation correctly did not force a death to fit the scenario name. The failed-flow fish survives but the flow-dependent SPS dies. A healthy adult without a feeder survives 8 h here, then genuine deprivation kills it during the 12 h/24 h cases. These are measured fixture outcomes, not universal husbandry promises.

## Verification and reproducibility

Run `python tests/browser_qa.py chrome --overnight-before` for archived original modules and `python tests/browser_qa.py chrome --overnight` / `edge --overnight` for the repair. All 60 repaired continuous/offline comparisons per browser match exactly, including growth, disease/health, food, chemistry, equipment, rewards and captured death diagnostics. The 8-hour pairs explicitly compare24continuous game days against8realhours of catch-up. Fixtures use identical cloned states, random streams and5-minute steps. Original-code 60/60 comparisons also match, ruling out an ordinary extra catch-up multiplier as the reproduced root cause.

Additional checks cover finite food/resources, species/stages, coral-only feeders, disabled feeders, real lethal starvation, disease, no repeat death/feeding, living bleaching, zero-health terminal state, mineral volume, overlapping sync/async, interrupted replay, repeated return, dead legacy entities and exact raw backup, historical chemistry, reward ledger and actual browser reload. Responsive real UI was inspected at 390 px and 1366 px. Original-snapshot Settings download is additionally tested against the built hosted game. Final browser totals and archive verification are recorded below after packaging.

All 1419 previous runtime asset files are SHA-256 unchanged; js/data.js is unchanged. The ten-day freshwater replay matches the protected prior model in Chrome and Edge. No new art/species, no artwork approvals altered; 105 fish (94 marine/11 fresh), 15 marine corals, 10 invertebrates and 6 fresh plants retain existing registries/holds. All local-safe store and financial rules remain. See planning/overnight-repair/preservation.json.

## Files and documentation

New runtime: js/marine-care.js, js/mortality.js, js/overnight-ui.js. Integration: core, save, simulation, invertebrates, livestock-health, expansion, update29, offline, main, app-shell, gameplay-ui, store, ui and index.html; build.py identifies v3.5. Tests add original/repaired probes, model/UI checks, protected fixture-clock alignment and hosted original export; package.py includes isolated overnight evidence, never profiles/downloaded saves.

Updated the full 31-section MDP v3.8, printable continuity source with both full 38/35-entry permanent rosters, README, GAME_DESIGN, UI_SPECIFICATION, DEVELOPMENT_STATUS, BALANCE_REPORT, GITHUB_PAGES and PDF_WORKFLOW. Binary PDF generation remains a previously disclosed toolchain limitation; no old PDF is claimed current. Art documents/registries remain unchanged. Immutable original modules, requirements, rate export and preservation evidence are under planning/overnight-repair.

## Remaining limits

No unavailable historical player chemistry or death reason can be reconstructed. The repair affects future progression, including pending elapsed time after upgrade; existing corpses remain dead. Poor stocking, incompatible diets without real supply, disease, juvenile vulnerability, exhausted food, aging gear, finite minerals/nutrients and longer absence still carry risk. Representative stable tanks passed 72 game days; this is not all possible species/stock/volume combinations. Food, natural forage and metabolism remain explicit simplified game calibrations. No freshwater content/biology expansion, cloud recovery, secure online score or retrospective loss compensation is included. Other-browser engines/fullscreen modes and unchanged old artwork suites were not rerun for this repair.

## Final release checks

The final selected suites passed **1,332 checks in Chrome and 1,332 in Edge, zero failures (2,664 executed checks)**. Counts include overlapping regressions. The original-code baseline adds 60 matched continuous/offline comparisons used for diagnosis, outside that repaired-release total. These are automated accelerated fixed-step simulations, not days of wall-clock observation.

| Suite | Chrome pass / fail | Edge pass / fail |
|---|---:|---:|
| Overnight matrix / model / real UI | 97 / 0 | 97 / 0 |
| Survival reward / finance / live UI | 98 / 0 | 98 / 0 |
| Gameplay / migration / store destination | 412 / 0 | 412 / 0 |
| Livestock / disease / economy / protected freshwater replay | 362 / 0 | 362 / 0 |
| Diving / trading / continuous tank progression | 108 / 0 | 108 / 0 |
| Rebuilt DIST / hosted local saves / actual original export | 255 / 0 | 255 / 0 |

The 97-check overnight suite contains 60 continuous/offline pairs, 28 focused model checks and 9 real browser UI/local-reload checks. Twelve scenarios each cover 20 minutes, 2, 8, 12 and 24 real hours. All adequately provisioned adult/mixed/juvenile/coral/grazer/multiple-aquarium fixtures survive all durations. No-feeder and exhausted-stock adults survive 8h here, then die during the longer tests; genuine disease and failed coral flow remain lethal with captured evidence. Repeated or interrupted catch-up does not repeat health damage/rewards. Hosted tests also download and byte-compare an untouched pre-repair snapshot through Settings.

All 1,419 previous runtime assets and js/data.js are SHA-256 unchanged; protected ten-day freshwater biology is exactly equal. Every current loss in the matrix has a known modeled cause, preceding interval and retained actual death-time water. Original/repaired results, species/stage rates, formulas and limitations: [OVERNIGHT_REPAIR_REPORT.md](OVERNIGHT_REPAIR_REPORT.md), tests/overnight-evidence and planning/overnight-repair. No individual player save was examined or restored. The full 31-section MDP v3.8 and both permanent roster ledgers remain in the continuity source. Old artwork suites/other browser engines were not rerun.

Earlier release records below are historical where superseded.

DIST contains **1,514 source files / 455,965,949 source bytes**, built at 2026-10-15T12:25:32.557229+00:00. Pages ZIP is **425,590,768 bytes**. Every current source/DIST/Pages entry matches the manifest SHA-256, including build-manifest.json; ZIP CRC passes. Three added runtime modules implement marine care, mortality evidence and Overnight Readiness.

Chrome and Edge each passed **255 final built-DIST checks**, including a repository URL subpath, real local save/reload/autosave, destination and wallet retention, independent browser storage, local export/import and an actual byte-identical pre-repair Settings download. Total selected repaired-release checks: **1,332 per browser / 2,664 overall, zero failures**. No public GitHub deployment was attempted.

Upload the contents of DIST or extract AquariumLife-GitHub-Pages.zip at the publishing root. Both have index.html and .nojekyll at root. Browser profiles/player data are excluded. All saves, timeline/financial records and backup downloads remain local to each player PC/browser. The source ZIP uses compatibility filename AquariumLife-v0.1.zip, refreshed by python tests/package.py with current source/docs/requirements/evidence and CRC validation. See OVERNIGHT_REPAIR_REPORT.md and tests/overnight-evidence/release-verification.json.

Earlier build records below are historical where superseded.

