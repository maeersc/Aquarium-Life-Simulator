# Test report - playable v3.6 / MDP v3.9

## Protected production distribution - 2026-10-22

Current master v4.17; gameplay remains v4.3.1 with a new protected distribution pipeline. Production now minifies JS/CSS, shortens internal identifiers, uses content-derived code filenames and excludes review pages, source maps, project documentation and tooling. Human-readable game code and original assets remain untouched. Assets retain their original pixels and offline file transports; no encryption, passwords, licensing dependency, profile rewrite or save-key change is introduced. Runtime safety and the mandatory performance pass take priority over obfuscation. DISTRIBUTION_PROTECTION_REPORT.md records exact mechanisms, commands, executed tests, benchmarks and limits. All7838 executed protected browser/performance/regression assertions passed; exact results, methods and limits are in the protection report and tests/distribution-protection-evidence. Earlier build descriptions are historical where superseded.

## UI polish and store quantities — 2026-10-22

Playable v4.3.1 / master v4.15. The familiar aquarium layout now uses a very subtle static downward fish-scale background, opaque slate-blue panels and consistent controls. The existing guarded store supports quantities for equipment, food, consumables, ordinary medicines, rated parts and rocks. Multiple rocks enter Inventory for separate placement; sensitive livestock, unique tools and installations retain their established individual safeguards. One total charge, distinct physical IDs, capacity/stock checks, persistent receipt replay protection and local saving remain authoritative. Main schema2/tutorial2, biological simulation, economy rates, offline time and freshwater lock are unchanged. STORE_QUANTITY_RULES.md defines category behavior; UI_POLISH_QUANTITY_REPORT.md records files, actual tests and limitations. All6463 executed browser/regression assertions passed; see the current report and tests/ui-quantity-evidence for exact suites and limitations. Earlier release sections below are historical where superseded.

## Current release — v4.3.0, 2026-10-22

Performance optimization is implemented with60FPS default, optional30FPS, independent biological time, on-demand native sheets, bounded caches, cached scenery, covered/hidden suspension and five graphics controls. The current DIST has2370source files (844,323,224bytes); its manifest records exact source hashes. GitHub Pages/local-save integration, both browsers'382-sheet checks, tutorial, equipment/offline, breeding and economy tests pass. The performance and five-minute-soak suites bring the final browser assertions to17,025with zero final failures. All2368original protected assets remain unchanged. The current Pages and portable source ZIPs are rebuilt and CRC/hash checked. See AQUARIUM_LIFE_PERFORMANCE_OPTIMIZATION_REPORT.md and tests/performance-evidence/release-validation.json for exact evidence and environmental limits. Physical GPU utilization and Netflix/audio synchronization were not measured. Native production remains382sheets/6112cells across110/113usable entries; the separate18-sheet shrimp artwork gap remains.

Earlier release sections below are historical and do not describe current counts or runtime.

### Executed v4.0.4 validation

22114 browser assertions passed across current Chrome/Edge livestock and Pages suites; zero final failures. Production16-frame sheets completed: **0**. Full artwork expansion remains unfinished; performance and source/DIST checks are detailed in LIVESTOCK_ANIMATION_16_FRAME_REPORT.md. DIST/Pages and source archives are rebuilt after this evidence update.


## Livestock16-frame expansion — playable v4.0.4 / MDPv4.7

**Partial implementation: authored artwork remains unfinished.** Audited119 marine entries in12 batches (94fish,15coral records,10invertebrates), with25 designer varieties kept separate. Added a shared validated16-frame asset path to AL.FishAnimation, an offline full-catalog review gallery and calmer existing fish timing. **Zero new production16-frame sheets are complete; all119 entries still need dedicated artwork.** One generated Ocellaris candidate failed alignment/identity checks and is retained outside deployment. Existing art, biology, local saves and freshwater lock remain. See [LIVESTOCK_ANIMATION_16_FRAME_REPORT.md](LIVESTOCK_ANIMATION_16_FRAME_REPORT.md) for each entry and actual evidence. Earlier animation reports describe the previous milestone and do not establish16-frame completion.


## Global marine fish animation audit — playable v4.0.3, 2026-10-16

Audited all 94 registered marine fish, including five acquisition-held clownfish and one fictional fish. Thirty-one have authored adult cycles; 63 previously translated static living poses. Added render-only species profiles, pixel-preserving tail/outer-fin motion, state-aware timing, banked side-profile turns and head/eye protection across three stages. No new biological species, AI/feeding/breeding rules, inheritance or saves are introduced. All 94 remain conservatively classed B (partial) because bespoke action/turn/pectoral artwork and anatomy approvals remain incomplete; this is not a claim of fully authored animation. See [FISH_ANIMATION_AUDIT.md](FISH_ANIMATION_AUDIT.md), [FISH_ANIMATION_SYSTEM.md](FISH_ANIMATION_SYSTEM.md) and [offline motion review](fish-animation-review.html).

## Ocean diving destination artwork — playable v4.0.2, 2026-10-16

Eight original pixel-art PNG environments replace the simplified expansion scenery for Indonesia, Philippines, Sri Lanka, Marshall Islands, Maldives, Australia, Florida and Mariana Trench. A central per-mode art mapping drives selection previews, proportional in-dive backgrounds and expedition-result accents. Older regional PNGs, native encounter pools, all diving gameplay, local saves and freshwater lock are preserved. See [DIVING_LOCATION_ART_REPORT.md](DIVING_LOCATION_ART_REPORT.md). Art is implemented for review; no prior livestock/art approval is changed.

## Global aquarium preparation repair — v4.0.1, 2026-10-16

Corrected the saved `prepared=true` / stale `emptyDry=true` contradiction across setup, rendering, biological readiness and all receiving hosts. Existing saves repair only from preparation completion evidence; normal chemistry alone never certifies preparation. See [AQUARIUM_PREPARATION_REPAIR_REPORT.md](AQUARIUM_PREPARATION_REPAIR_REPORT.md). Master v4.4 preserves all 31 major sections, local saves, freshwater lock and the 20-minute day. Earlier release reports remain historical where superseded.


## Global diving expansion and liquidation — playable v4.0, 2026-10-16

Implemented the authorized Emergency Diving Sales & Rock Resale and Global Ocean Diving Expansion request (specification v3.6). Seven new reef selections and Mariana remote exploration use the central registry. Catch development, medical assessment, concealed attached eggs and regular-store liquidation extend the existing receiving authority. See [DIVING_EXPANSION_REPORT.md](DIVING_EXPANSION_REPORT.md) and [DIVING_EXPANSION_SAVE_SCHEMA.md](DIVING_EXPANSION_SAVE_SCHEMA.md). Earlier milestone reports remain historical where superseded. All saves stay local; freshwater remains locked; one game day remains 20 real minutes.


## Universal ocean diving receiving — 2026-10-16

All registered diving fish, corals and invertebrates now share species-aware diagnostics and explicit saved post-boat receiving. Every owned aquarium is shown; supported coral mounts and host-compatible quarantine retain all safeguards. The repair also corrects invalid noninfectious carrier flags, rock surface discovery and missing/ambiguous host mappings. Tests enumerate the real eligible registry, plus old-save, condition, expiry, replay and future-registration checks. See [GLOBAL_DIVING_RECEIVING_REPORT.md](GLOBAL_DIVING_RECEIVING_REPORT.md). Earlier host-limited flow descriptions are historical where superseded. Game v3.9 / master v4.2; local saves and freshwater lock remain.

## Diving receiving diagnostics repair — 2026-10-16

All owned aquariums now remain visible in receiving, with disabled incompatible options, exact actual/required checks, preparation/quarantine guidance, live eligibility refresh and the unchanged finite holding countdown. Properly prepared 80-gal marine tanks at exactly 27°C can receive Chalk Bass subject to existing transport survival; legitimate safeguards remain enforced. See [DIVING_RECEIVING_REPAIR_REPORT.md](DIVING_RECEIVING_REPAIR_REPORT.md) for the confirmed UI cause, data audit, files, tests and the limits of identifying an unsupplied player save. Current gameplay stays v3.9 / master v4.2, with local saves and freshwater lock preserved.

## v3.9 final verified release — 2026-10-15

**1288 selected browser/model/deployment checks passed, zero failed.** Both browsers passed the mystery feature and built Pages/local-save flows; existing diving/resale, automatic breeding, heater/mortality and store/casino/header regressions passed. Viewports: 1920×1080, 1600×900, 1366×768 and 390×844. See [MYSTERY_DIVING_UPDATE_REPORT.md](MYSTERY_DIVING_UPDATE_REPORT.md) for exact suites, all 19 acceptance categories, changed files and limits. DIST and both ZIPs are current; source/DIST/ZIP hashes and CRC checks are independently verified. Browser saves, receipts and mortality history remain local. No public deployment was performed.

## Mystery fish diving — v3.9 current, 2026-10-15

Implemented the authorized Mystery Fish update (request v3.5) on top of playable v3.8. New valid Reef/Deep trips guarantee a reachable regional fish, concealed until boat return, with saved assignments, original question-mark art/reveal, explicit safe receiving and permanent transport-loss evidence. Empty/closed collectible pools block launch. Existing oxygen, fees, resale, local accounts, biology, genetics, breeding, care rewards and freshwater lock remain. See [MYSTERY_DIVING_RULES.md](MYSTERY_DIVING_RULES.md) and [MYSTERY_DIVING_UPDATE_REPORT.md](MYSTERY_DIVING_UPDATE_REPORT.md). Current master is v4.2; earlier release entries are historical where superseded.

## Current v3.8 delivery — 2026-10-15

Current autonomous breeding acceptance and regression evidence is recorded in BREEDING_UPDATE_REPORT.md and tests/breeding-evidence. Older milestone totals below describe their historical source state. The retired v2.6 ecosystem UI runner assumes unlocked freshwater and missing mystery tiers; it is not a current-release acceptance gate. Do not count its aborted run as a pass.

## v3.7 final verification - 2026-10-15

New acceptance: Chrome 138/138, Edge 138/138. Built DIST / Pages / local saves: Chrome 259/259, Edge 259/259. Regression suites: finance/rewards/fragging 98/98 each; Chrome gameplay 412/412 and overnight 97/97 (60 equivalent live/offline pairs); Edge heater/mortality 108/108 and health/economy/freshwater 362/362. Total 1,969 passed, zero failed, with overlap between suites. Header right-edge delta is zero at 1920 x 1080, 1600 x 900 and 1366 x 768 in both browsers. See STORE_CASINO_UPDATE_REPORT.md for scope, files, repaired failures and limitations. The owned-fish research fixtures and authorized seven-item sidebar expectation reflect the new requirements; remaining biological assertions are unchanged.

## UI layout cleanup verification - 2026-10-15

Current cleanup suite: Chrome 48/48 and Edge 48/48. Rebuilt DIST / GitHub Pages / local-save integration: Chrome 258/258 and Edge 258/258. Total for this update: 612 passed, zero failed. Six viewport sizes include 1366 x 768 desktop and 390 x 844 mobile; fish/coral pointer selection, three-second highlight expiry, placement space, actual aquarium purchase, selector persistence and actual reload passed. No game HTTP requests in offline layout tests or uncaught exceptions. No biology changes; previous biological evidence below remains historical evidence, not newly rerun tests. See UI_LAYOUT_CLEANUP_REPORT.md and tests/layout-cleanup-evidence for scope and limitations.

## Current heater and permanent mortality release v3.6 - 2026-10-15

**1,443 passing checks in Chrome and 1,443 in Edge, zero failures: 2,886 executed release checks.** These include overlapping regressions, not that many distinct requirements. The archived original thermal-code comparison adds 21 matched pairs per browser (42 overall) outside this release total. Simulated absences are accelerated fixed-step tests, not days of wall-clock observation.

| Suite | Chrome pass / fail | Edge pass / fail |
|---|---:|---:|
| Heater levels / permanent journal / real UI and exports | 108 / 0 | 108 / 0 |
| Overnight matrix / model / live UI | 97 / 0 | 97 / 0 |
| Reward / finance / full recovery / live windows | 98 / 0 | 98 / 0 |
| Gameplay / migrations / store destinations | 412 / 0 | 412 / 0 |
| Livestock / health / economy / protected freshwater replay | 362 / 0 | 362 / 0 |
| Diving / trading / continued simulation | 108 / 0 | 108 / 0 |
| Exact rebuilt DIST / local saves / original and mortality JSON exports | 258 / 0 | 258 / 0 |

The 108-check suite contains 86 model checks and 22 real UI/local export/reload checks. It includes 21 repaired thermal live/offline comparisons at 8/12/24h, seven heater levels through the actual 15,000-gallon aquarium, fixed pricing/capacity, undersized purchase rejection, transfer/legacy protection, and below-ambient cooling requirements. Properly equipped/fed thermal cases remain at25 C; failed/disabled/missing/weak cases can die cold. Food exhaustion remains independently lethal at25 C in longer tests. All60 existing overnight pairs also match continuous biology and retain their provisioned-case survival outcomes.

Mortality checks exercise fish/coral/invertebrate/nursery identity and fatal health, no duplicate records/financial penalty, exact water versus thermostat target, named/unknown causes, nutrient-only photosynthetic coral evidence, 48-hour history, account separation, canonical replay IDs, all pending records beyond200, quota retry, protected original/legacy state, rejected draft writes, monotonic completed audits, independent retry errors, invalid diagnostic import, actual JSON downloads and real browser reload. Source simulation and UI send no internet requests. Hosted tests use a local repository subpath and verify separate device storage, autosave, backup/import, full journal export and current source hashes.

All1,419 prior runtime assets and js/data.js are SHA-256 unchanged; both protected ten-day freshwater replays pass. The full31-section MDPv3.9 is embedded in continuity with both permanent38/35-entry ledgers retained. No new art/biological species or approvals. Binary PDF generation, other browser engines/fullscreen and unchanged artwork galleries were not rerun; printable continuity source is current. No actual player save was inspected or restored and no public deployment occurred.

Evidence: tests/heater-evidence/release-verification.json, per-browser results/logic/original-thermal files, tests/overnight-evidence and the existing regression evidence folders. Source/formulas/limits: HEATER_MORTALITY_REPORT.md and MORTALITY_LOG_SCHEMA.md. Earlier release material below is historical where superseded.

## Current overnight mortality repair v3.5 - 2026-10-15

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

## Current v3.4 reward validation - 2026-10-15

The selected final suites executed **1,231 passing checks per browser, zero failures (2,462 executed assertions overall)**. Counts include overlapping regression assertions, not that many distinct requirements. The full prior artwork gallery suite was not rerun for this reward-only change.

| Current suite | Chrome passed / failed | Edge passed / failed |
|---|---:|---:|
| Survival v3.4 / finance baseline / live UI | 98 / 0 | 98 / 0 |
| Preserved gameplay / migration | 412 / 0 | 412 / 0 |
| Shared livestock / health / economy / freshwater replay | 362 / 0 | 362 / 0 |
| Diving / continuing simulation | 108 / 0 | 108 / 0 |
| Rebuilt DIST / local saves / export / import | 251 / 0 | 251 / 0 |

The 98-check reward suite contains 34 new reward model checks, 16 real UI checks and 48 existing finance/fragging/research model checks. Its new tests cover all twenty requested acceptance items, including real fixed-step/offline qualification, each livestock class, 100-only/50-only/150-combined conditions, full recovery without partial-overlap payment, migration and actual historical payments, local replay guards, live notifications, window simulation, ledger details and actual reload.

All 1,419 asset files and six protected existing data/core/biology/healthy-care/wallet modules remain byte-identical (planning/v3.4/preservation-results.json). The complete updated 31-section master is embedded in the continuity source. Current actual payment is 100; old amounts in earlier reports/receipts below are historical facts, not active rules.

The final DIST passed 251 checks each in Chrome and Edge at an HTTP repository subpath: current policy, whole runtime hashes, local saves, autosave/backup, real JSON export/import, separate browser profiles, network-disabled saves and direct file launch. No player saves/profiles enter release artifacts. New evidence and screenshots: tests/update34-evidence. Details/limits: V34_UPDATE_REPORT.md.

Untested: Firefox, public GitHub deployment, manual screen-reader use and long-duration human play. Casino/login checks are not applicable because those features do not exist. Completely offline forward clock authenticity is unavailable; elapsed conditions are simulated once and settled day/timeline/financial keys prevent duplicate payment. Existing research content remains incomplete; binary PDF export is still pending.

## Earlier test records - historical and superseded where inconsistent

Historical record: earlier survival-reward amounts and results below are superseded by v3.4. Current payments are 100 AC plus a separate independently qualified 50-AC healthy award. Actual historical receipts/test evidence are preserved, not rewritten. See V34_UPDATE_REPORT.md.

## Current v3.3 validation - 2026-10-14

This section supersedes historical totals below. Actual final runs: **8,800 passed, zero failed per browser; 17,600 executed checks overall.** These are executed assertions across suites, not a claim of that many unique requirements.

| Suite | Chrome passed / failed | Edge passed / failed |
|---|---:|---:|
| New v3.1-v3.3 model and UI | 85 / 0 | 85 / 0 |
| Preserved v2.9 gameplay and 35-entry batch | 412 / 0 | 412 / 0 |
| Diving, current resale rules and modal clock | 108 / 0 | 108 / 0 |
| Livestock/core/health/economy and protected freshwater | 362 / 0 | 362 / 0 |
| Clownfish art/collection and direction regression | 7583 / 0 | 7583 / 0 |
| Final deployed DIST and device-local save/export/import | 250 / 0 | 250 / 0 |

The 85 new checks comprise 48 model assertions and 37 real UI checks. Model and UI logs/screenshots remain in tests/update33-evidence. Current DIST tests serve the final build at a real local repository subpath and perform actual JSON downloads, imports, autosave, reload, profile isolation, network-disabled saves and direct-file launch. No cloud saves or external runtime requests.

Testing fixed the Cancel form submission and Frag Rack category routing. An earlier Edge hosted-import attempt timed out; the diagnostic-enabled final rerun passed all 250 checks, as did Chrome. No reproducible game import defect was established from that earlier timeout. Old manually assigned wallet/time fixtures now set explicit finance openings, and stock/wanted fixtures follow the new trading rule. The deterministic simulation test excludes only real PC receipt timestamps.

Browser source-data/art preservation checks, byte-identical js/data.js and the existing freshwater replay remain intact. See planning/v3.1-v3.3/protection-results.json. Three regenerated QA screenshot previews differ from an older pre-v2.9 baseline; they are not modified livestock sprites.

Not tested: Firefox, manual screen-reader use, real public GitHub deployment and long human play sessions. Casino/login checks are not applicable because those systems do not exist. Research contents remain 0 fully verified / 93 incomplete (5 with reviewed annotations), explicitly disclosed in UI; test passage does not certify missing biology. PDF export/render verification remains pending. Full details: V33_UPDATE_REPORT.md.

## Earlier test records - historical where superseded

## v2.9 — current implementation

Implemented the twelve-step saved/skippable saltwater tutorial with medical guidance, three-second selection outlines, disabled freshwater UI, separate +50 healthy / +200 survival rewards with persistent death/recovery tracking, Deep Market display rename, local asset-value leaderboard preview, exact 15,000-US-gallon / 5,000-AC aquarium, proportional water-change salt consumption, independent mystery products and the approved 35-species marine batch. Saves remain local to each player's browser on their PC. The bottom mystery product is content-held because its Legendary host specialist is not eligible. See [V29_UPDATE_REPORT.md](V29_UPDATE_REPORT.md) for actual checks, care/art limits and release details. Earlier milestone sections below are historical wherever superseded.

See [the current release report](V29_UPDATE_REPORT.md), [new art gallery](v29-review.html), [DIST](DIST/) and [build manifest](DIST/build-manifest.json).

## Historical milestone record


## Ocean Diving v2.8 — historical, 2026-10-14

MDP **v3.3**, retaining all 31 major sections. **Ocean Diving** beside Keeper Level opens Reef (Level 5 / 1,000 AC) or Deep Sea (Level 10 / 10,000 AC). Fiji, Caribbean, Hawaii and Japan have original regional scenery and a compact playable map. W/A/S/D, arrows and on-screen buttons move one tile; every successful step costs exactly 5% oxygen from 100%. Blocked movement and collection clicks cost none. Eight temporary slots become owned only on a successful boat return with oxygen remaining. Exhaustion/confirmed abandonment forfeits discoveries without a fee refund.

Aquariums continue at 1× during planning, diving and results, using the existing 20-real-minute game day. Explicit safe receivers, supported coral mounts, species-conditioned survival, finite transport holding, persistent provenance and Reputation 5 Black Market-only resale are integrated. Confirmed paid Black Market purchases earn bounded reputation; canceled/failed/duplicate transactions do not. Direct normal-store livestock is restricted to Tiers 1–3; eight daily Fish slots and independent Mystery Egg odds remain unchanged. Nominal tank/equipment capacities now ceil to whole US gallons; physical liters and precise water-change calculations remain exact.

**No new biological species.** The approved 38-entry v2.7 batch and all protected freshwater content remain the roster baseline. Six sourced encounter profiles reference existing IDs; Hawaii wildlife is observation-only, and unsupported regional/depth combinations offer inert fictional salvage rather than invented animals. All captures are fictional restricted game recovery, not real collection authorization. New art is unapproved pending user review. Saves and expedition receipts remain on each player's PC in browser storage. See [DIVING_UPDATE_REPORT.md](DIVING_UPDATE_REPORT.md) and [the region ledger](assets/diving/registry.json). DIST is rebuilt through `python build.py`. Earlier milestones below are historical where superseded.


## Livestock expansion v2.7 — roster baseline milestone, 2026-10-14

MDP **v3.2** retains exactly 31 major sections. Added **38 unique marine entries: 28 fish, five named stony corals and five non-fish invertebrates**. All 38 passed the pre-registration scientific-name/synonym duplicate audit; none were skipped. The runtime now has **80 fish (69 marine, 11 protected freshwater), ten marine coral entries and five non-fish invertebrates**. The six existing freshwater plants are unchanged. Existing art-only and planned entries are excluded from these totals.

All six Mystery Egg rarity pools are now populated; the earlier empty-pool content hold is superseded. Keep independent 50/25/15/7.5/2/0.5 percent odds, 600 AC, three daily eggs, existing level/incubation gates and safe-destination checks. Daily Fish shopping remains exactly eight visible slots: 3 Common, 3 Uncommon, 1 Rare, 1 Mystery Egg. Higher tiers do not add normal Fish cards. Fixed retail, persistent selected aquarium, continuous offline simulation, rarity/genetics and existing specialist clownfish holds remain.

New livestock has inspectors, rarity, care information, value, host-filtered health compatibility and additive save support. Corals use player-selected supported rock/rack placement. Invertebrates are separate bottom residents with feeding, crawling/filtering, condition, death and transfer records. Their egg/planktonic larval reproduction and art are unsupported. New fish natural breeding is enabled only for the five explicitly supported profiles; Mystery Egg development is a simplified game presentation, not evidence of complete captive culture.

There are 38 new transparent sprite sheets / 304 static stage-state views. All are unapproved; 12 sheets carry explicit framing review flags. Existing approved artwork is preserved. Review [the new artwork gallery](expansion-review.html). [Implementation report](LIVESTOCK_EXPANSION_REPORT.md), [permanent registry](assets/expansion-v27/registry.json), [continuity source](PROJECT_CONTINUITY_SOURCE.md) and [PDF workflow](PDF_WORKFLOW.md) record the limits. **PDF regeneration remains pending: PDF authoring/rendering prerequisites are unavailable in this environment.** Earlier milestone material is historical where superseded.


Current results: **362 expansion + 7,583 artwork checks per browser, 0 failed**, Chrome and Edge. See [the v2.7 acceptance report](LIVESTOCK_EXPANSION_REPORT.md) for evidence and not-run coverage. Earlier numerical totals below are historical.

## Rarity, genetics and continuous ecosystem — v2.5/v2.6 (historical milestone)

At this historical milestone, MDP **v3.1** retained the same 31 major sections. Six original colored rarity icons are shared by livestock inspectors, shops, collection, encyclopedia and breeding. Daily Saltwater Fish shopping has exactly eight saved slots (3 Common, 3 Uncommon, 1 Rare, 1 Mystery Egg), fixed normal prices and a countdown. Selected aquarium and purchase safety remain persistent.

Time now continues while away: 20 real minutes = one game day, with all elapsed time processed in responsive batches. Actual ecosystem conditions determine survival and 50-AC healthy-day eligibility; the old relaxed/capped/no-offline-reward policy is superseded. Return reports show real simulation results. Imports cannot replay an older locally recorded timeline.

Marine pattern identities persist through breeding, growth, turning, transfer and reload. Natural Ocellaris inheritance uses the approved 85/10/4/1 gameplay distribution; new Snowflake reference-line stock supports the documented limited model. Existing approved art and freshwater biology are preserved.

**Historical v2.6 limits (superseded by v2.7):** Mystery Egg sales were held because Very Rare, Ultra Rare and Legendary pools are empty; exact odds remain visible and no substitution is made. Other unverified designer genetics remain on a visible breeding hold. Existing provisional artwork and simplified biological models remain provisional. See [ECOSYSTEM_UPDATE_REPORT.md](ECOSYSTEM_UPDATE_REPORT.md) for actual tests, files, screenshots and remaining limitations, and [RARITY_GENETICS_RESEARCH.md](RARITY_GENETICS_RESEARCH.md) for assignment/genetics evidence. Earlier milestone sections below are historical wherever their offline/store policy conflicts with this update.


## Gameplay, time and settings v2.4 — 2026-10-13 (historical milestone)

The current consolidated specification is **MDP v3.0**, retaining exactly 31 major sections. Aquarium capacities and requirements display US gallons using 3.785411784 L/gal; saved physical liters are unchanged. Field Journal separates Saltwater/Freshwater encyclopedia categories and adds Keeper Progress through the clickable level badge. Store title, destination, balance and X now share a compact header.

Settings offers saved 12/24-hour formatting and Windowed/Fullscreen/Borderless Fullscreen preferences. Fullscreen uses the browser API after a click; Borderless is explicitly its browser equivalent, not native OS borderless. Coral, rock and decoration previews support wheel depth (up back/down front), PageUp/PageDown, valid support constraints and persistent z layering. Marine eggs retain aquarium/parent identities, care/exposure metadata and centralized value; attached eggs follow support depth, pelagic eggs drift, protected broods remain internal. Existing artwork and freshwater biology stay unchanged.

At 1×, 20 real minutes make one game day. A full observed healthy day earns exactly 50 AC per player, independent of tank count; up to 30 game minutes of minor variation is tolerated, while severe crises block the day. Empty-only collections and offline catch-up cannot earn it. Existing energy costs and showcase income remain separate. Saved care checkpoints prevent repeat claims. Welcome Back now requires Continue before simulation/catch-up/saving; Start Over requires confirmation and offers backup export. Unreadable saves remain protected.

See [GAMEPLAY_UPDATE_REPORT.md](GAMEPLAY_UPDATE_REPORT.md) for the 45-item acceptance mapping, actual browser results, screenshots, migration policy and limitations. Earlier dated sections below are historical where they conflict with this update.


## Main UI overhaul verification — 2026-10-13

Current UI evidence is in `tests/ui-overhaul-evidence`, produced by `python tests/browser_qa.py chrome --shell` and the Edge equivalent. Existing system/store, economy/medical and clownfish eye/direction regressions are run separately. New-purchase fixtures now explicitly install the equipment removed by the approved empty/dry design; store legacy-route assertions target primary modal contents, and the protected simulation comparison removes only declared marine hooks. See [UI_OVERHAUL_REPORT.md](UI_OVERHAUL_REPORT.md) for final counts and the 40 required checks. Older reported outcomes below belong to their original milestones.

## Marine economy, disease and valuation — 2026-10-13

Current marine acceptance: Chrome 69 passed / 0 failed; Edge 69 passed / 0 failed. Existing system 68/0 and current Store/UI 90/0 in each browser. Clownfish art/eye/direction 7,583/0 with 1,792 directional cases per browser. Commands: `python tests/browser_qa.py chrome --economy` (or edge), ordinary browser regression command, and `--clownfish`. [Chrome new evidence](tests/economy-evidence/chrome-results.json), [Edge](tests/economy-evidence/edge-results.json). Includes actual examination/treatment buttons and real quantity input, no runtime HTTP requests, 1440/1024/760/390px inspector checks, exact pre-update freshwater biology comparison and protected art/data hashes. More detail in the [update report](ECONOMY_DISEASE_UPDATE_REPORT.md).

The previous full-project audit is the dated October 12 snapshot, not a fresh audit of the new milestone. Some root result artifacts below have been rerun and superseded; new acceptance results have their own dated evidence folder. No multi-hour performance soak, Firefox, real private-save collection or clinical efficacy certification was performed.


| Suite | Chrome | Edge | Evidence |
|---|---:|---:|---|
| Current simulation and transaction systems | 68 passed, 0 failed | 68 passed, 0 failed | tests/chrome-results.json, edge-results.json |
| Store, destinations, mounting, management and lighting | 88 passed, 0 failed | 88 passed, 0 failed | tests/chrome-store-results.json, edge-store-results.json |
| Collection sprites, gallery and attachment study | 7,583 passed, 0 failed | 7,583 passed, 0 failed | tests/chrome-clownfish-results.json, edge-clownfish-results.json |
| Collection directional stage/size cases (included above) | 1,792 | 1,792 | Every species/variety, stage/state, four sizes |
| Collection packing | 56 sheets, no failures | Same static pipeline | tests/clownfish-packing-report.json |

Browsers ran real file:// pages with network disabled and isolated test profiles. No runtime exceptions or HTTP/HTTPS requests appeared in current store/review suites. Current freshwater definition file and 144 protected art/source files match their baseline SHA-256 values. Simulation differs only in its marked marine clownfish sex block; existing freshwater biological behavior code is byte-preserved.

Store checks cover three main tabs and every subcategory; saved selection on open/close/reopen/reload; fixed destination header; eligible alternative choice; unsafe and stale-water rejection; once-only charging; actual equipment/inventory/rock/sand destinations; single-egg social safeguards and reserved offspring territory; physical coral support and rollback; support edits/removal and save migration; modal focus/Escape and responsive widths. Existing management screens, coral Overview/Care inspector, Ocellaris inspector and tank-light pixel brightness remain checked.

Collection checks cover 31 catalog names, 25 base-linked varieties, all 56 loaded sheets, five specialist holds, eight stage/state views, shared egg/larva pixels, visible pupil pixels at 25/52/73/117-pixel widths, exact whole-sprite mirroring with odd-size pixel centers, restored canvas transforms, four distinct swimming poses, identical eye pixels across poses, no automatic approval, female invariants, designer save/genes round trips and offline review controls. The isolated coral study validates supported and unsupported placement, mounted rack movement, occupied removal blocking and JSON round trips without player storage writes.

Nine diagnostic collection contact sheets and desktop/mobile store/gallery/study screenshots were inspected. These checks verify rendering/interaction, not universal species anatomy or independently verified care for every specialist. All new art remains provisional. Firefox was unavailable and remains unverified. Source atlases and original artwork are preserved.

Two final Edge invocations were initially started concurrently against the same isolated profile/port; the harness connection failed. They were rerun sequentially and passed. This was a test orchestration issue; no game change was needed.

Run python tests/browser_qa.py chrome (or edge) for current system/store checks; add --clownfish for collection checks. Older art/life-stage suites and original full-page-store UI assertions are historical fixtures. Their recorded prior milestone results below are not current store validation.

## Historical validation records


Date: **2026-10-11**. Tests ran on Windows through actual local-file URLs with network emulation set to offline.

The current life-stage gallery has **214 passing checks in each of Chrome and Edge**, including **2,160 directional render cases** per browser across 216 authored stage/state images. See [LIFE_STAGE_ART_REPORT.md](LIFE_STAGE_ART_REPORT.md), [Chrome results](tests/chrome-life-stage-results.json) and [Edge results](tests/edge-life-stage-results.json). The gameplay checks below were repeated after stage integration. All 27 entries were visually inspected using contact sheets; that inspection does not replace user art approval or scientific anatomy review.

The earlier art 1.1 suite recorded 221 checks and 6,480 render cases per browser for the preserved prior animation assets; those historical results remain in [ART_UPDATE_REPORT.md](ART_UPDATE_REPORT.md).

## Final results

| Browser | System checks | Browser/UI checks | JavaScript exceptions | Gameplay HTTP(S) requests |
|---|---:|---:|---:|---:|
| Headless Chrome 154.0.0.0 | 68 passed, 0 failed | 69 passed, 0 failed | 0 | 0 |
| Headless Edge 154.0.0.0 | 68 passed, 0 failed | 69 passed, 0 failed | 0 | 0 |

These are the same 137 checks repeated in two browsers, not 274 different test cases. Machine-readable evidence:

- [Chrome results](tests/chrome-results.json)
- [Edge results](tests/edge-results.json)
- [Chrome aquarium screenshot](tests/chrome-aquarium-preview.png)
- [Edge aquarium screenshot](tests/edge-aquarium-preview.png)
- [Light on](tests/chrome-light-on.png) and [light off](tests/chrome-light-off.png) screenshots.
- [Coral placement](tests/chrome-coral-placement.png) and [coral Care tab](tests/edge-coral-info.png) screenshots.

The screenshot depicts an aquarium populated by the isolated automated test. Real new games start with **no fish**.

## System coverage

- Coral placement purchase atomicity, coordinate validation/rollback, free repositioning preserving identity and health, old saves without vertical positions, shared inspection/simulation conditions, two-dimensional LPS spacing, and rooted freshwater plants.

- Lighting overrides at night/day, intensity and reef-light output, failed hardware, saved mode validation, older-save compatibility, off-state lamp wear and plant growth, and independent per-tank settings.

- Freshwater and marine state initialization and complete species data.
- Uncycled-tank restrictions, gradual bacterial establishment, incompatible water, minimum adult swimming volume and social group minimums.
- Atomic money/stock/identity updates, idempotent purchase tokens, rollback, finite shop stock and bounded adult load.
- Food inventory consumption, suitable-food selection, decomposition of unsuitable food, fry food and actual-consumption quest progress.
- Replacement-water fraction calculations, matching marine salinity and supply use.
- Gradual toxicity damage, starvation, oxygen loss, corpse pollution/removal and individual maximum lifespan.
- Thirty-day cared-for fish survival, 120-day unattended state stability and deterministic repeated simulation.
- Motion bounds, resting, hiding, predator reports, actual predation and territorial attack cooldowns.
- Heater failure/recovery, equipment servicing and once-daily automatic feeding.
- Readiness restrictions, spawning cooldowns, livebearing gestation, inherited genes, lineage, condition-sensitive incubation and male mouthbrood dependency.
- Healthy reef care across all five coral categories, coral damage from unsuitable salinity, freshwater nitrate uptake and inadequate-light consequences.
- Bounded sale prices, loss-making purchase/resale loops, daily sale limits, buyer budget resets and demand recovery.
- Single-claim quest rewards, independent new tanks, night-market level/time/containment restrictions, and blocked legal contraband resale.
- Disabled VIP payments, JSON round trips, malformed input, duplicate identities, missing fields, nonfinite/negative values, stale identity counters, schema migration and future-schema rejection.
- Relaxed absence, survival catch-up caps, reserved brood capacity, invalid environmental controls, entire-school transfers and persistence of seasonal acquisitions.
- Beginner, breeder, hoarder and fictional rare-collector economy scenarios.

## Browser/UI coverage

- Assigned Ocellaris PNG artwork loads under file URLs; four distinct frames and readable thumbnails work; store/individual inspectors display the new asset; saved fish retain their existing species identity after reload.

- Real pointer coral placement and selection, cancel without spending, prevention of repeated-click duplication, Overview/Care contents, keyboard tab navigation, repositioning with zoom/pan, Escape rollback, arrow-key/Enter confirmation, saved positions after reload, and placement layout at 1600/390 pixels.
- Computed styles verify the locked near-black background and slate-blue panels. Coral screenshots were visually inspected.

- Actual Auto/On/Off control, saved manual mode after reload, night-time manual lighting, return to the automatic schedule, separate tank modes, and sampled canvas luminance showing On is at least 35% brighter than Off.

- `file://` entry point loads with route-selection dialog while offline.
- Freshwater route creates the stated wallet and starting state.
- Prepare, fishless cycle, compatibility dialog, actual purchase and feeding form connect to the simulation.
- All 13 navigation screens and all eight store categories render content.
- Quest claim and browser reload preserve the wallet transaction.
- Export button downloads a real JSON file containing actual game data.
- File-input import validates and restores that downloaded state after an intentional in-memory change.
- A deliberately corrupted primary save remains preserved, recovery UI opens, and the previous valid backup restores without duplicate fish.
- Equipment installation, water-change controls, independent aquarium purchase and individual inspection work.
- Renderer/interpolation leave authoritative game state unchanged.
- No horizontal page overflow at widths 1600, 1024, 760 or 390 pixels.
- No JavaScript exceptions and no HTTP(S) page requests observed throughout the run.

## Performance evidence

The same representative aquarium (eight residents and six plants) was drawn 60 times after warming the first frame in headless browsers with GPU acceleration disabled:

| Browser | Mean render-call cost |
|---|---:|
| Chrome | 4.56 ms/frame |
| Edge | 4.72 ms/frame |

An earlier implementation measured about 67 ms/frame. Pixel scanline filling, palette caching and cached plant frames removed that bottleneck. The application targets 60 FPS and has a 30 FPS fallback; **render-call timing is not a measurement or guarantee of end-to-end displayed FPS**, maximum-capacity performance or performance on every desktop.

## Problems found and resolved

- Initial headless launch was blocked by sandbox graphics restrictions. The explicitly approved harness subsequently ran outside that sandbox with its own profiles.
- The test WebSocket parser expected a different valid HTTP 101 status phrase; it now accepts the status code.
- A test reset initially re-saved state through the application's unload handler. The test now suppresses saving only during its intentional reset.
- A toxicity test incorrectly expected fatal damage despite a working mature filter removing the exposure. The sustained-exposure test now disables filtration; the immediate-step check still verifies gradual damage.
- A test equipment selector initially chose a disabled installed item. It now targets an available purchase.
- A collector-report counter held an old transaction snapshot; the final report reads the active aquarium state.
- Pointer placement testing exposed CSS-pixel rounding in synthetic mouse coordinates. Position assertions now allow one displayed pixel; placement handoff uses immediate scrolling to keep its target stationary.
- Game fixes include session-unique purchase tokens, bounded resting targets, actual-consumption feeding progress, brood-space reservations, whole-school transfers, full transaction validation, deterministic fixed-step motion and renderer optimization.

All final automated checks pass. No unresolved runtime exception was observed in these tested flows.

## Verification limits

- Firefox is not installed and has not been run. There are no Firefox-specific dependencies, but compatibility remains unverified.
- Desktop screenshots were inspected; this is not a comprehensive accessibility, touch-input or biological-art audit.
- No audio system exists, so no audio testing was performed.
- Maximal 12-tank / 250-fish-per-tank collections and long real-wall-clock sessions were not benchmarked.
- Storage-unavailable and quota-error handling exist; the final browser suite uses functioning local storage and does not exhaust the browser quota.
- Schema 1 migration is covered with a structurally compatible fixture, not a real legacy release corpus.

## Reproduce

Open `tests/index.html` directly for the 68 system checks. For full browser automation:

```text
python tests/browser_qa.py chrome
python tests/browser_qa.py edge
```

Only the developer automation needs Python; playing and running the in-browser system suite do not.
