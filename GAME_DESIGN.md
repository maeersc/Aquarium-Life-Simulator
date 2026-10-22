# Aquarium Life — design and implementation

## Performance optimization — 2026-10-22

Playable v4.3.0 / master v4.14. One capped60/30FPS scheduler, independent fixed biological steps, on-demand lossless native sources, bounded caches, cached scenery, covered/hidden render suspension, changed-value HUD updates and five graphics preferences. Main schema2/tutorial2, all player assets, protected art, local saves, freshwater lock and biological/economic formulas remain intact. PERFORMANCE_SYSTEM.md and PERFORMANCE_SETTINGS_SAVE_SCHEMA.md describe runtime/persistence; AQUARIUM_LIFE_PERFORMANCE_OPTIMIZATION_REPORT.md records actual measurements and executed regressions. The31-section authority is MASTER_DEVELOPMENT_PROMPT.md, with an exact handoff copy in PROJECT_CONTINUITY_SOURCE.md. Earlier art/PDF limitations remain separate.

## Interactive saltwater tutorial loop repair - playable v4.2.1, 2026-10-21

The interactive12-phase/22-task guide retains its real gameplay requirements. The full route audit corrects the covered empty-canvas target, trusted-event observation order and retained closed-dialog targets. The visible empty-tank setup button opens Tank Setup during the viewing task; it does not auto-fill or prepare the tank. Stable task prerequisites, idempotent observation and opt-in development loop diagnostics support future changes. Resource/filter instructions use actual controls and leave prices, stocks and biological restrictions intact. Existing guide state and verified milestones remain version2; no player save reset is required. See TUTORIAL_FULL_AUDIT_AND_REPAIR_REPORT.md for the flow, modified files, actual browser walkthroughs, interruption/recovery tests and limitations. Earlier tutorial test evidence below is historical where superseded.


## Interface simplification - playable v4.1.1, 2026-10-20

The authorized first cleanup uses six main destinations: Aquariums, Aquarium Store, Field Journal, Tank Care, The Dock Casino and Settings. VIP/premium and leaderboard placeholders leave normal navigation; local asset comparison moves into My Aquariums and art review into collapsed Settings developer tools. Progress groups Keeper Level, Objectives and Achievements. Tank Care contains Installed Equipment, Feeding, Water Changes, Lighting, Coral Fragging and Inventory. Detailed condition/history stays in Inspect; exact service and removal safeguards remain. Water changes use one preview/confirmation; warnings retain all reasons with expandable notes. Food forecasts also show real hours at 1x.

No biological, clock, reward, casino payout, ownership or save-schema changes. Existing saved accounts, local storage and freshwater lock remain. Historical interface descriptions below are superseded by master sections26.3-26.4. See SIMPLIFICATION_REPORT.md for actual tests and files.


## Coordinated economy/progression update — 2026-10-20

Implemented the authorized sanctuary25,000-AC price (no retrocharge), profile-specific first species/size/destination rewards,13 unpaid optional objectives, distinct Maintenance/catalog-priced Replace Part, itemized confirmed whole-aquarium sales including safe zero-tank ownership, Gold Fish 2×pair gross return, Casino Profile controls/actual visits and persistent 5%compatible-pair offers across all 29 currently supported fish. New marine profiles retain5,000-AC opening plus a separately receipted 250-AC starter-size award. Existing saves backfill known history without payments. Other tank/retail prices, autonomous biology, long-term durability,20-minute day, local saves, protected art and freshwater lock remain.

Gold Fish now has 152.2%theoretical return with other payouts preserved; this positive player expectation is explicitly documented, not secretly offset. Ordinary eligible livestock resale uses the requested 60%Deep reference for all origins. Shell buyback is50%; cumulative animal dealer/biological restrictions can block a whole bundle. Parts use only the seven documented serviceable catalog families; sealed devices are not given invented replaceable internals. Detailed mechanics/schema/catalogs and actual source/deployment tests are in ECONOMY_UPDATE_REPORT.md and its linked home documents. Master/full exact continuity are v4.10. Earlier milestone narratives below remain historical wherever inconsistent with these new explicit authorizations.

## Long-term marine equipment reliability — 2026-10-19

**Aquarium equipment must have long-term, equipment-specific durability and reliability. Well-maintained equipment should generally last several in-game years, with gradual wear and reasonable maintenance requirements. Failure must not be driven by excessively fast or duplicated durability deductions.**

Condition, maintenance and malfunction are independent. New equipment targets 4.5–10 game years by existing type; saved private hazards allow earlier/later faults without calendar expiration. Cleaning preserves chassis age and filter bacteria; component repair preserves identity; replacement remains a physical owned-item operation. Actual operating efficiency drives tank support. The 20-minute day, full offline progression, local saves, prices/rewards and freshwater lock remain. Mechanics and real-time balance are centralized in EQUIPMENT_DURABILITY_BALANCE_REPORT.md; care/schema in EQUIPMENT_MAINTENANCE.md and EQUIPMENT_RELIABILITY_SAVE_SCHEMA.md. Earlier universal hourly wear/full-condition Service descriptions are superseded for marine equipment.

## Equipment inventory and interface reorganization — 2026-10-19

Physical storage and per-aquarium equipment use the permanent rules in [EQUIPMENT_INVENTORY.md](EQUIPMENT_INVENTORY.md). New equipment purchases enter storage; explicit installation and warned removal retain each unit’s unique identity, fixed rating, condition and modifications. Biological effects derive only from the destination tank’s installed array. Existing handheld tools/supplies retain their approved use rules. See the additive [save extension](EQUIPMENT_INVENTORY_SAVE_SCHEMA.md); schema 2, freshwater lock, autonomous breeding, AC rules and the 20-minute day are preserved.


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

## Mystery fish diving — v3.9 current, 2026-10-15

Implemented the authorized Mystery Fish update (request v3.5) on top of playable v3.8. New valid Reef/Deep trips guarantee a reachable regional fish, concealed until boat return, with saved assignments, original question-mark art/reveal, explicit safe receiving and permanent transport-loss evidence. Empty/closed collectible pools block launch. Existing oxygen, fees, resale, local accounts, biology, genetics, breeding, care rewards and freshwater lock remain. See [MYSTERY_DIVING_RULES.md](MYSTERY_DIVING_RULES.md) and [MYSTERY_DIVING_UPDATE_REPORT.md](MYSTERY_DIVING_UPDATE_REPORT.md). Current master is v4.2; earlier release entries are historical where superseded.

## Automatic marine breeding — v3.8 current, 2026-10-15

Replaced manual marine courtship with autonomous, species-aware breeding, visible swimming/nest behavior, individual reproductive status and a read-only Breeding & Eggs observation dashboard. New clutches use real parent/tank IDs, saved reproductive roles and RNG, species-specific care/losses and bounded offspring reservations. All prior local accounts, art/genetic identities, coral lineage, rewards, heaters, mortality logs, store/casino functionality and the 20-minute day remain. Freshwater stays locked. See [BREEDING_RULES.md](BREEDING_RULES.md), [BREEDING_SAVE_SCHEMA.md](BREEDING_SAVE_SCHEMA.md) and [BREEDING_UPDATE_REPORT.md](BREEDING_UPDATE_REPORT.md). Earlier release entries are historical wherever superseded.


## Equipment filters, inspector research and The Dock Casino - v3.7 current

Implemented the equipment-category dropdown and original fragging-tool previews, moved paid species research to living owned-fish inspectors, and added the authorized seventh sidebar entry The Dock Casino with playable Gold Fish and Predator & Prey. All wagers and returns use the existing account wallet/ledger and saved round authority; all research remains 5 AC once per canonical species. The aquarium header controls share the information-column grid and align to its actual panel edge. See STORE_CASINO_UPDATE_REPORT.md and CASINO_RULES.md for the release, verified probabilities, local persistence and limitations. Existing biological simulation, 20-minute day, rewards, freshwater lock, livestock/art approvals and local saves remain. Earlier release sections are historical where superseded.

## Heater levels and permanent mortality journal v3.6 - current, 2026-10-15

Marine equipment now offers seven fixed heater levels: 5-20, 20-75, 75-250, 250-1,000, 1,000-3,000, 3,000-7,500 and 7,500-15,000 US gallons. Store recommendations use the selected aquarium; undersized new purchases are blocked. The main tank view shows heater state, rated capacity and condition. Legacy heaters retain their actual saved ratings; transfers never resize a heater.

Marine heat uses capacity/condition-limited thermostat output and exact exponential heat exchange on the same live/offline timeline. No setpoint overrides failed or missing equipment. Status distinguishes suitable resident conditions, general chemistry, unsafe resident temperatures and empty/deceased aquariums. The 20-minute day, existing nutrition, maintenance, local saves, +50/+100 rewards and freshwater lock remain.

The existing single mortality authority now maintains a dedicated permanent account journal, detailed fatal-step evidence, hourly recent history and offline-run audits. Field Journal > Tank History > Livestock Deaths has filters, complete reports, Export Mortality Log and selected-report JSON export. Welcome Back links to the latest offline period. Original recorded evidence migrates unchanged; unknown older facts remain unknown. Storage failures retain pending records and warn rather than silently dropping them. See [HEATER_MORTALITY_REPORT.md](HEATER_MORTALITY_REPORT.md) and [MORTALITY_LOG_SCHEMA.md](MORTALITY_LOG_SCHEMA.md). Current playable version v3.6 / MDP v3.9. Earlier release statements are historical where superseded.

## Overnight mortality repair v3.5 - current rule, 2026-10-15

Repaired marine starvation, diet selection and coral-only automatic feeding on the existing 20-real-minute game day. Eight real hours still advances 24 game days. Provisioned adult, mixed, juvenile, coral and grazing/scavenging test aquariums survive 8, 12 and 24 real hours; this does not guarantee every stocking or unsupported tank. Actual food exhaustion, untreated disease and failed environmental support can still kill residents.

Automatic feeders check six times per game day, consume actual compatible inventory and adapt to maturation. Natural grazing/scavenging uses finite available resources. Hunger must coincide with depleted nutrition before calorie-deprivation damage; the separate malnutrition condition does not apply the same damage twice. No existing dead livestock is restored, no credits are compensated, and freshwater biology remains protected.

Current feeding forecasts remain in Food & Feeding; historical reports remain in Tank History → Reports. The standalone Overnight Readiness panel is removed. Welcome Back and Tank History retain actual death-step causes, identities, food, equipment and chemistry separately from current recovered water. Local loads retain an untouched pre-repair snapshot when storage permits, exportable in Settings. Saves and downloads remain on each player's PC/browser. Review [OVERNIGHT_REPAIR_REPORT.md](OVERNIGHT_REPAIR_REPORT.md) for formulas, the complete absence matrix, reproducible evidence and limitations. Current playable release is v3.5 / consolidated MDP v3.8. Earlier release sections below are historical where superseded.

## Daily livestock survival reward v3.4 - current rule, 2026-10-15

Players earn **100 AC** for every completed qualifying in-game day without a livestock death. The player must own eligible living marine livestock throughout the full simulated day. This is one account-wide payment, not one per aquarium. The separate healthy-aquarium award remains **50 AC**; both independently qualified awards total **150 AC**.

A confirmed fish, coral or bottom-invertebrate death cancels the current qualifying day and starts 1,440 game minutes of recovery. Another confirmed death restarts recovery. Recovery time cannot count toward a qualifying reward day. Illness or living coral bleaching is not a death. The authoritative game calendar remains 20 real minutes per day; legitimate offline catch-up processes the same conditions. Game windows do not stop simulation. Casino requirements apply only if that game is implemented.

Existing balances and actual historical ledger receipts remain unchanged. Every future survival payment is 100 AC through the existing financial service, with canonical account/transaction IDs, actual payment time and completed qualifying day/status. Local save, financial sequence and offline timeline guards prevent re-awarding a settled day. See [V34_UPDATE_REPORT.md](V34_UPDATE_REPORT.md) and [FINANCIAL_TRANSACTIONS.md](FINANCIAL_TRANSACTIONS.md).

## Earlier milestone material - superseded where inconsistent

## v3.3 current release - 2026-10-14

Implemented the authorized v3.1 coral fragging/trading, v3.2 financial dashboard and v3.3 Marine Research Center. Equipment has three reusable coral tools and two mounting consumables; eligible parents produce independently simulated, mounted clones with tissue loss, recovery and lineage. Diving livestock can use regular or Deep Market dealers; regular pays floor(0.60 x the same Deep reference), and Deep requires Reputation 5 plus an active wanted request. Wanted Livestock remains separate from exactly four rotating dealer stock slots.

The AC button opens a reconciled, persisted financial history. Existing wallets migrate unchanged; new profiles start at the requested 5,000 AC. Saltwater Research and the existing Encyclopedia share permanent 5-AC canonical-species unlocks. All 94 marine fish are indexed; 93 real species are researchable, one fictional entry is preview-only. Fully verified dossiers: 0; incomplete: 93; five have reviewed biological annotations. Partial content is disclosed before purchase. See [V33_UPDATE_REPORT.md](V33_UPDATE_REPORT.md), [FINANCIAL_TRANSACTIONS.md](FINANCIAL_TRANSACTIONS.md) and [RESEARCH_SOURCES.md](RESEARCH_SOURCES.md).

Saltwater-only scope, safe persistent store destinations, local PC/browser saves, existing rewards/odds, all old livestock and artwork approvals/holds remain. No new biological species or art assets were added. Full printable continuity source is updated; binary PDF regeneration remains pending. Current playable version v3.3 / consolidated MDP v3.6.

Research is a local account action, accessible even with a retained freshwater tank selected. It grants information only; disease treatment, ownership and acquisition eligibility remain separate. Current gameplay uses the shared models in js/finance.js, js/update31.js and js/research.js. See MDP sections 8, 17, 18, 19 and 24.

## Earlier milestone record - historical where superseded

**Authorized 2026-10-14:** The user approved the complete 25/5/5 roster and rarities, confirmed saltwater-only, and explicitly requested "Implement v2.9". Roster approval and artwork approval are separate; new artwork remains unapproved. [Authorization](planning/v2.9/approval.json).

## v2.9 — current implementation

Implemented the twelve-step saved/skippable saltwater tutorial with medical guidance, three-second selection outlines, disabled freshwater UI, separate +50 healthy / +100 survival rewards with persistent death/recovery tracking, Deep Market display rename, local asset-value leaderboard preview, exact 15,000-US-gallon / 5,000-AC aquarium, proportional water-change salt consumption, independent mystery products and the approved 35-species marine batch. Saves remain local to each player's browser on their PC. The bottom mystery product is content-held because its Legendary host specialist is not eligible. See [V29_UPDATE_REPORT.md](V29_UPDATE_REPORT.md) for actual checks, care/art limits and release details. Earlier milestone sections below are historical wherever superseded.

Tutorial, care/survival rewards, preview ranking and new mystery purchases use the actual simulation and transaction rules. Saltwater-only applies to this milestone. Retained freshwater biology is regression tested through an isolated test adapter; the production UI and transactions stay locked.

## Earlier milestone record




## Ocean Diving v2.8 — historical, 2026-10-14

MDP **v3.3**, retaining all 31 major sections. **Ocean Diving** beside Keeper Level opens Reef (Level 5 / 1,000 AC) or Deep Sea (Level 10 / 10,000 AC). Fiji, Caribbean, Hawaii and Japan have original regional scenery and a compact playable map. W/A/S/D, arrows and on-screen buttons move one tile; every successful step costs exactly 5% oxygen from 100%. Blocked movement and collection clicks cost none. Eight temporary slots become owned only on a successful boat return with oxygen remaining. Exhaustion/confirmed abandonment forfeits discoveries without a fee refund.

Aquariums continue at 1× during planning, diving and results, using the existing 20-real-minute game day. Explicit safe receivers, supported coral mounts, species-conditioned survival, finite transport holding, persistent provenance and Reputation 5 Black Market-only resale are integrated. Confirmed paid Black Market purchases earn bounded reputation; canceled/failed/duplicate transactions do not. Direct normal-store livestock is restricted to Tiers 1–3; eight daily Fish slots and independent Mystery Egg odds remain unchanged. Nominal tank/equipment capacities now ceil to whole US gallons; physical liters and precise water-change calculations remain exact.

**No new biological species.** The approved 38-entry v2.7 batch and all protected freshwater content remain the roster baseline. Six sourced encounter profiles reference existing IDs; Hawaii wildlife is observation-only, and unsupported regional/depth combinations offer inert fictional salvage rather than invented animals. All captures are fictional restricted game recovery, not real collection authorization. New art is unapproved pending user review. Saves and expedition receipts remain on each player's PC in browser storage. See [DIVING_UPDATE_REPORT.md](DIVING_UPDATE_REPORT.md) and [the region ledger](assets/diving/registry.json). DIST is rebuilt through `python build.py`. Earlier milestones below are historical where superseded.

Primary design reference: MDP §5.5. Maps are 11×7 cells with compact traversable routes, real collision tests and boat-distance warnings. Mobile fish shift deterministically after successful steps; distance is checked at the moment of collection. Trips have twelve discoveries, eight temporary slots, and near-boat rocks so a real out-and-back route is possible within twenty steps. Zero oxygen on a boat-arrival step is failure: arrival must happen with oxygen remaining. Failed or abandoned trips use a non-graphic safe-rescue report. There are no oxygen upgrades.

Every organism is assigned an explicit eligible receiving tank (and supported coral mount) before recovery. Safety is rechecked per individual on return, including cumulative stocking and prior received individuals. Unsafe delivery records a loss rather than inserting an animal. A 12–24-game-hour sensitivity-based transport deadline prevents indefinite survival in expedition inventory. Outcomes depend on sensitivity, transport, elapsed game time, steps, prior condition and a quarantine benefit; probabilities are game calibrations, not field-survival measurements. Alive specimens enter the existing health and valuation systems, not a new parallel animal model.

## Livestock expansion v2.7 — roster baseline milestone, 2026-10-14

MDP **v3.2** retains exactly 31 major sections. Added **38 unique marine entries: 28 fish, five named stony corals and five non-fish invertebrates**. All 38 passed the pre-registration scientific-name/synonym duplicate audit; none were skipped. The runtime now has **80 fish (69 marine, 11 protected freshwater), ten marine coral entries and five non-fish invertebrates**. The six existing freshwater plants are unchanged. Existing art-only and planned entries are excluded from these totals.

All six Mystery Egg rarity pools are now populated; the earlier empty-pool content hold is superseded. Keep independent 50/25/15/7.5/2/0.5 percent odds, 600 AC, three daily eggs, existing level/incubation gates and safe-destination checks. Daily Fish shopping remains exactly eight visible slots: 3 Common, 3 Uncommon, 1 Rare, 1 Mystery Egg. Higher tiers do not add normal Fish cards. Fixed retail, persistent selected aquarium, continuous offline simulation, rarity/genetics and existing specialist clownfish holds remain.

New livestock has inspectors, rarity, care information, value, host-filtered health compatibility and additive save support. Corals use player-selected supported rock/rack placement. Invertebrates are separate bottom residents with feeding, crawling/filtering, condition, death and transfer records. Their egg/planktonic larval reproduction and art are unsupported. New fish natural breeding is enabled only for the five explicitly supported profiles; Mystery Egg development is a simplified game presentation, not evidence of complete captive culture.

There are 38 new transparent sprite sheets / 304 static stage-state views. All are unapproved; 12 sheets carry explicit framing review flags. Existing approved artwork is preserved. Review [the new artwork gallery](expansion-review.html). [Implementation report](LIVESTOCK_EXPANSION_REPORT.md), [permanent registry](assets/expansion-v27/registry.json), [continuity source](PROJECT_CONTINUITY_SOURCE.md) and [PDF workflow](PDF_WORKFLOW.md) record the limits. **PDF regeneration remains pending: PDF authoring/rendering prerequisites are unavailable in this environment.** Earlier milestone material is historical where superseded.

### v2.7 gameplay details

New species are registered once through `ExpansionData`; freshwater species and simulation parameters are not extended. Specialist food inventory is marine-only. Predatory fish are checked against owned invertebrates. Prawn gobies/conch/hermit require sand; cave residents need rock shelter. Grazers require 72 prepared game hours. Purple Queen Anthias requires live plankton inventory, Copperband requires frozen food, and feeding-conditioned Orange-spotted Filefish requires specialist rations plus living branching SPS and can damage it when hungry. Spotted Boxfish requires a dedicated species-only aquarium; severe stress/death can release a bounded modeled toxin that filtration and water changes reduce. These are gameplay calibrations, not universal husbandry prescriptions.

The five supported new natural breeding profiles are Chalk Bass, Yellow Assessor, Blue Assessor, Greenbanded Goby and Sharknose Goby. Assessor broods stay protected in the mouthbrooding presentation. Game incubation of 48/72 hours and compressed lifespan/maturity are not biological timing claims. Remaining 23 new fish display an explicit natural-breeding hold; all five new invertebrates have no reproduction system. Corals use the existing fragmentation/placement system.

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


## Main interface and visible broods — 2026-10-13 (previous milestone)

The aquarium remains the viewport focus. Exactly six sidebar entries open management dialogs: Aquariums, Aquarium Store, Field Journal, Equipment, VIP Store (Preview Only), Settings. Ownership/setup/value/water live in Aquariums; buying, selling and delivered-order history in Store; collection/encyclopedia/breeding/progression/history/disease references in Journal; owned equipment and feeding/water changes in Equipment. Existing state, selected destination, credits and progression are retained. Primary windows replace one another, remember sub-tabs and pause simulation under the existing rules while canvas animation continues.

Player-created starting tanks and purchases start empty and dry; old aquariums retain their assets. Equipment must be chosen/installed, water prepared and fishless cycling completed before stocking. Removed equipment is owned inventory preserving capacity and wear; installing it consumes the stored item. Values use the same authoritative asset model, displayed above the tank; uninstalled equipment is excluded from installed-tank totals. Water-change estimates use the actual replacement formula, supplies and credit cost; dry water changes are blocked.

Marine external broods retain IDs, parents, viability and incubation progress, plus deterministic saved hard-surface/water-column sites. Supported demersal presentations are shelter/hard-surface approximations; tang/wrasse-like pelagic presentations stay in water; Banggai mouthbrooding remains protected, not sand eggs. Clownfish rock adhesion and broader reproductive groups are informed by [UF/IFAS marine ornamental culture](https://ask.ifas.ufl.edu/publication/FA224) and [Florida Museum clownfish reproduction](https://www.floridamuseum.ufl.edu/discover-fish/species-profiles/orange-clownfish/). Exact rare-species nest microstructure is not claimed to be modeled. Small clutch/magnified framing changes are a visibility guideline, not biological egg enlargement. Existing egg/dead/larval assets remain. Failed external marine clutches persist for one game day or removal, contribute one failure-pollution event and cannot hatch. Freshwater species/data/biology were not expanded.

Save schema stays 2: optional emptyDry flag, bounded validated ownedEquipment and marine brood anchor/failure timestamp are additive. Old marine broods acquire deterministic sites without rerolling genes/illness, changing IDs, or advancing RNG. [UI overhaul report](UI_OVERHAUL_REPORT.md) records scope and verified checks. Earlier phase descriptions remain historical.

## Marine economy, disease and valuation — 2026-10-13

The current approved milestone adds centralized marine health (`livestock-health.js`), saved dealer inventory (`livestock-market.js`), authoritative value (`valuation.js`) and strict additive persistence (`health-save.js`). It does not add livestock or online services. Normal adult/variety/egg/frag prices remain fixed by their product definitions and grade. Marine fictional dealer fish/eggs and restricted medicines get saved bounded price/condition/quality rolls at listing creation; dawn generates new listing identities. Stale submissions reject. The pre-existing freshwater fictional listing retains its legacy price/biology.

Marine fish use ich, velvet, Brooklynellosis, flukes, selected bacterial syndrome, malnutrition and environmental injury profiles. Corals have separate bleaching/tissue/pest/stress/infectious-syndrome profiles. A standard unexamined frag can acquire a saved introduction risk (5% pest roll, an additional 2% possible infectious-syndrome roll only for stony groups); these are game calibration values, not measured prevalence. Ordinary fish start healthy. Introduced contagious pressure spreads only to eligible hosts within an aquarium. Environmental/noninfectious conditions do not become contagious. Independent marine medical/dealer random streams do not advance the protected freshwater biological random stream. All 144 protected freshwater art/source files and species definitions remain byte-identical; a ten-day biological comparison matches the prior code.

Examination consumes diagnostic units. Active parasite findings use a confidence-qualified examination; carriers remain suspected. Selected bacterial diagnosis starts at 60% and requires a follow-up at least 24 game hours later to reach the 92% in-game testing confidence required for targeted antibiotics. Confidence values and times are game abstractions. Treatment is a timed individual monitored course, not real concentration dosing. Correct choice, host, confidence, severity, environment and batch quality affect recovery. Quarantine-only courses cannot be moved into a reef while active. Fish-only copper/ciliate/fluke/antibacterial courses require prepared, cycled, bare adult-fish quarantine; coral dips require a separately mounted coral quarantine environment. Diagnosis does not instantly cure. Courses consume units once, may remain unresolved, and need appropriate feeding/water. Severe fish illness calls the existing mortality engine; coral HP/dead art and existing removal remain authoritative.

Normal medicines: diagnostic supplies, monitored copper quarantine, ciliate quarantine, fluke quarantine, targeted antibacterial, nutritional support, coral pest care and coral environmental recovery. Two fictional restricted products have persisted hidden target, authenticity, efficacy, contamination and compatibility. Each acquired batch copies listing quality; an active course copies it again. Assay consumes diagnostics and reveals quality without rerolling.

Asset value, retail and resale are distinct. Marine living value uses baseline × 0.85 × bounded stage/growth, HP, nutrition, disease, condition/tissue/pigment/polyps, age, traits and fertility modifiers; cap = 4× baseline. Designer baseline is its fixed variety price. Fish resale requires ≥60 HP, low disease burden and no active course; it is at most 75% of baseline and remains below retail. Fictional resale is prohibited. Dead living value is zero. Freshwater individual valuation retains the old formula. Tank totals include the reference shell (marine shell factor 1.25), capacity/condition-adjusted equipment, fish/viable broods, corals/plants, distinct benthic fish, owned rock/substrate/racks and decorations exactly once. Dead coral skeletons have no assigned material resale value in this milestone. Cache totals per authoritative state/tick, never per sprite frame; keep at most 30 meaningful marine value-history entries. Existing transfer stress can reduce value at arrival.

Save schema remains 2 with marine extension version 1. Legacy saves gain defaults/listings without changing existing wallet/IDs/health. Current invalid/missing hidden fields reject rather than reroll. New identity namespaces include listing/batch IDs. Existing readable and corrupt-save recovery behavior remains. The older phase descriptions below are historical where they conflict with this current section; that milestone used MDP v2.8.

Veterinary design basis: [Merck parasites](https://www.merckvetmanual.com/exotic-and-laboratory-animals/aquarium-fish/parasitic-diseases-of-fish), [UF marine ich](https://ask.ifas.ufl.edu/publication/FA164), [UF copper compatibility](https://ask.ifas.ufl.edu/publication/FA165), [UF monogeneans](https://ask.ifas.ufl.edu/publication/FA033), [Merck bacterial disease](https://www.merckvetmanual.com/exotic-and-laboratory-animals/aquarium-fish/bacterial-diseases-of-fish), [NOAA bleaching](https://oceanservice.noaa.gov/facts/coral_bleach.html), [NOAA coral syndrome uncertainty](https://floridakeys.noaa.gov/coral-disease/disease.html). Literature informs host/treatment families and contraindications; numeric game rates are not clinical recommendations. Broad coral profiles and exact isolate/rare-species responses remain provisional.

Future only: verified aquarium-value leaderboard needs server-authoritative ownership/transactions/value. Browser-local saves cannot be trusted as online scores. No accounts, networking or leaderboard was built. Invertebrate host guards are scaffolded; no shrimp/crab/snail/starfish/urchin roster or clinical profiles were added. Full corpse decomposition, complete dry setup, substrate biology, categorical morph genetics and unrelated audit gaps remain outside this approved milestone.


## Current marine collection, mounting and destination behavior — 2026-10-12

Current catalog has 52 fish records plus five coral categories. 31 clownfish names include explicit hybrid uncertainty; 25 designer varieties reuse base biological species. Five specialist profiles are purchase-held. Difficulty and designer rarity are separate. Clownfish pairing never demotes an established female. Permanent shared Store destination behavior follows MDP 18.4; physical coral attachments follow 23.1. Marine rock/rack ownership and 0–5 inch visual sand depth now persist; new substrate chemistry is not implemented. Existing freshwater biological data and systems remain protected.


## Scope and architecture

The [consolidated master specification](MASTER_DEVELOPMENT_PROMPT.md) is the long-term source of truth. Revision 2.6 preserves the supplied v2.1, integrates the previously approved lighting and coral controls into their primary sections, and adds the mandatory current art-review gate. This document describes actual implemented behavior and its known deviations; it does not override the target requirements. See DEVELOPMENT_STATUS.md for the dependency-ordered phase audit, ART_DIRECTION.md for visual rules, and UI_SPECIFICATION.md for interactions.

This is a playable vertical slice, not the entire long-term master specification. HTML, CSS and classic JavaScript run directly from `file://`. `window.AL` owns namespaced modules; simulation and economy do not depend on DOM or canvas. No service worker, fetch, module loader, remote asset, backend, account or payment processor is present.

`AL.Core.newGame()` creates fully initialized state. A seeded linear congruential generator governs simulation randomness. A fixed step advances five game minutes; all biological calculations and authoritative motion execute inside that step. Renderer interpolation and animation clocks do not mutate simulation state or consume its random seed. This permits deterministic replay of the same starting state and actions.

All user transactions run against a draft state. Preconditions, stock, funds, placement and schema validation complete before the draft replaces the active state. Idempotency tokens prevent repeated submissions of a purchase dialog, and immediate duplicate button actions are debounced. A new browser session has a distinct transaction-token namespace. Persistence failure leaves a coherent in-memory transaction and a visible export warning; browser storage cannot guarantee durability when unavailable.

## Time, safety and progression

At 1×, one real minute equals 72 game minutes (20 real minutes per day). Speeds are 0, 1, 5 and 20. A hidden tab pauses; modal dialogs pause biological simulation. Optional survival catch-up converts elapsed wall time using the same 1× ratio, caps it to at most eight game hours, and advances bounded steps. Relaxed return does not simulate absence. Fishless setup skip runs the actual simulation and is allowed only if **every** aquarium has no fish or broods.

One-time journal rewards award 100 XP. `level = 1 + floor(XP / 200)`. There are 19 entries, enough to reach level 10. Progress is derived from actual actions or living state. Rewards require prerequisites and can be claimed once. School welfare and water-stability streaks reset when their conditions cease. Discovery is persistent; three achievements are checked at the next day boundary.

## Habitats and capacity

Tank sizes are 20, 40, 75, 150, 300, 500, 1,000, 2,500 and 5,000 liters. Maximum ownership is 12 tanks, with at most 250 fish entities per tank. Reef aquariums require marine water. Breeding, quarantine and incubation tanks are separate simulated habitats; this build does not grant hidden efficiency bonuses to their names.

Adult swimming-space minima, freshwater/marine separation, schooling counts, cycling status, toxins and fictional containment requirements are checked separately from load. Adult stocking capacity is `volume × 0.7` abstract load units. Admission reserves full adult load for fish and developing broods. The displayed 0–100 indicator uses current growth-adjusted load. It is a **game abstraction**, not a universal biological stocking rule.

Mixing potential predators and prey produces a high-risk report. Conditional aggression is permitted after a visible warning. A second betta is blocked: specialist betta breeding is deliberately outside this slice. Social fish transfer as a whole school to avoid a single-fish transfer being permanently blocked by the destination group minimum.

## Chemistry and ecology

Fish, corpses and uneaten food add organic waste. Organic decomposition adds ammonia. Two independently stored bacterial populations sequentially convert ammonia to nitrite and nitrite to nitrate. Rates depend on active filter capacity, durability and oxygen. New filters start nearly uncolonized.

Fishless cycling has a deliberately accelerated 36-hour maturation mechanic and a measured ammonia source. Completion seeds the simplified mature filter. This acceleration is openly labeled and must not be mistaken for real-world advice.

Prepared water changes interpolate parameters by the replacement fraction. Freshwater consumes conditioner; marine water consumes salt mix. Temperature-matched replacement water prevents an arbitrary instant thermal shock. These prepared changes do not expose an unimplemented raw-tap-water preparation system.

Oxygen balances gas exchange, aeration, flow, bacterial use, livestock respiration and plant photosynthesis. Plants consume nitrate while illuminated. Temperature moves gradually toward room/equipment targets with volume-dependent inertia. pH drifts with waste and buffering. GH and KH are stored and participate in replacement chemistry; KH also buffers the simplified pH drift. Conductivity and detailed acid/base chemistry are not modeled.

Reef corals consume calcium, magnesium and alkalinity. Health depends on salinity, temperature, ammonia, nitrate, minerals, programmed daily lighting and circulation. LPS proximity can damage neighboring colonies, calculated using both axes with the scene's 2:1 proportions. Growth requires health, light and nutrients, caps at 2.5×, and supports bounded cutting sales. Plant/coral space is limited by tank volume. Biological types have six plant and five coral silhouettes. Empty aquariums currently contain printed backdrop vegetation and starter hardscape; only purchased live organisms affect ecology. This starter scenery and included equipment conflict with the consolidated specification's dry/empty construction rule and must be replaced in the next habitat phase.

Coral purchases use a preview and explicit player-selected two-dimensional position. Canceling does not consume money or stock. Confirmation runs the same atomic purchase validation as other transactions. Repositioning preserves identity, health and funds. The anchor is bounded to x=0.05–0.95 and y=0.30–0.92; actual rock contact, collision and sprite-boundary checks are not yet modeled. Freshwater plants stay at y=0.92. Old schema-2 colonies without a vertical position still load and render at y=0.92; no reset or schema bump is needed.

The coral inspector has Overview and Care tabs. Health, age, growth, color, value and cutting readiness come from the selected organism. `AL.Sim.floraConditions` supplies both the inspector's conditions/warnings and the simulation's stress calculation, preventing divergent care rules. Coral placement pauses the simulation and supports pointer and keyboard control. Bleaching is not yet independent from HP: color currently follows health, dead coral remains inert, and the complete tissue-loss, skeleton and decomposition model remains open.

## Fish, food and behavior

Individuals retain ID, species, name, sex, age, health, hunger, stress, happiness, energy, fertility, growth, adult size, aggression, temperament, disease, immunity, genetics, rarity, lineage, origin and behavior. Requirements such as diet and salinity resolve through the species definition instead of duplicating immutable fields on every fish. Value and current load are computed.

Behavior chooses food seeking, resting, shelter, schooling or exploration; encounter logic adds chasing, fleeing and hunting. Diurnal/nocturnal preferences and bottom/midwater zones affect movement. Predation requires a sufficiently smaller victim, hunger, an encounter and a probability reduced by cover. Territorial attacks require triggers and have cooldowns; not all aggressive fish attack continuously. Corpses persist and pollute until removed.

Health effects accumulate with exposure duration. Wrong salinity, toxins, low oxygen, thermal deviation, starvation, severe stress and a generic infection can damage fish. Healthy conditions permit recovery. Aging reduces growth-stage/fertility eligibility and market value; elders have probabilistic mortality and an individual maximum lifespan. Detailed species-specific senescence is not implemented.

Seven food types have protein, plant fraction, quality, particle size, pollution and price data. Diet compatibility controls consumption, quality controls hunger reduction, and fry require fine food. Unconsumed food becomes pollution. The feeding quest advances only on actual consumption. Food stock does not currently spoil; this limitation is explicit rather than represented by a nonfunctional freshness control.

## Breeding and genes

Marine reproduction is autonomous under the permanent rule in MDP section 15. Player actions do not initiate marine courtship. Species-specific role, maturity, condition, chemistry, nest, territory, food and reserved adult-capacity checks precede persistent hourly chance rolls. The four reviewed profiles cover 26 eligible clownfish, Banggai, Chalk Bass and Sharknose Goby; other incomplete profiles remain held. Preserve established clownfish females, immature nonbreeders and simultaneous chalk-bass roles. Appropriate same-tank attached, drifting pelagic and internal paternal broods progress on the unchanged shared clock.

The Field Journal observes reproduction and retains separate coral frag lineage. The fish inspector refreshes reproductive status without extending its three-second outline. Eggs remain small, losses are meaningful, hatchlings have unique inherited identities and development-specific feeding/art, and sale requires juvenile growth plus establishment. Normal Ocellaris 85/10/4/1 and separate documented Snowflake genetics are unchanged. See BREEDING_RULES.md for formulas, scientific sources, parameter uncertainty and bounded-history limits; BREEDING_SAVE_SCHEMA.md for migration and replay protection. Freshwater biology remains frozen and inaccessible.

## Economy

Only earnable Aquarium Credits are active. New players receive 3,000 AC. Marine starter equipment is included; additional marine tanks cost 1.25× their freshwater base price. Installed device cost scales as `base price × max(1, volume / base device capacity)`. Daily energy costs scale with installed capacity and watts. Unpaid energy shortfalls receive a visible emergency allowance, keeping basic welfare equipment on rather than creating a debt death spiral.

Legal fish sale value:

```text
floor(retail × 0.52 × health/stress condition × life-stage factor
      × bounded genetic/fertility quality × bounded species demand)
```

Demand is bounded to 0.35–1.1. Quality is bounded to 0.8–1.15. Immediate resale is always below retail. Daily local buying budget is 1,200 AC and eight fish. A sale reduces species demand by 0.12; each day restores 0.08. Low-health fish and fictional contraband cannot be sold through the legal exchange. Cutting sales require health and growth and consume the same buyer budget.

One showcase can award 90 AC per game day after three healthy fish and 24 occupied safe hours. Finite journal rewards fund early expansion. See BALANCE_REPORT.md for simulated scenarios and remaining risks.

## Fictional market, events and VIP

Voidfin specters are light-sensitive and nocturnal; Glassfang eels are high-risk predators. Both require containment, limited shop stock, appropriate tanks, progression and an overnight opening schedule. They arrive with lower health and stress. Weekly fictional inspections have a 12% confiscation risk with working containment and 65% without it. These invented rules make no claim about actual wildlife law.

Six event labels are selectable offline. A seasonal lantern persists after switching the event, and its purchase advances an actual quest. A full event quest/reward catalog is future work.

VIP state always has zero premium currency, no tier, and disabled payments. Five tiers are explicitly labeled future cosmetic concepts. Three lighting treatments can be previewed freely. There is no purchasing action or entitlement simulation.

## Art update 1.1 rendering boundary

The current art-only update adds a shared SpriteKit final-size raster/draw boundary with registered head-local eye components, canonical per-frame eye detail, odd-size mirror alignment, optional authored left-side art and thresholded facing from displayed target displacement. It does not mutate saved fish positions or headings. Normal/idle animation cadence uses existing species activity; deceased poses freeze.

AssetBank loads thirteen local embedded-PNG families for five art-only priority fish, five existing coral groups and three rock collections. Coral art maps the existing health model to living/stressed/tissue-loss/dead states; separate bleaching is a gallery art study. Rigid SPS geometry uses subtle highlight pulses. Marine scenery and existing cave decorations use rock art; no new rock inventory/chemistry/physical editor is implied. Review preferences and gallery rock layouts use a separate local key.

All existing gameplay fish IDs and schema 2 saves remain compatible. Sources and prior artwork are preserved. See ART_UPDATE_REPORT.md for the complete art-state and direction test matrix and remaining animation/anatomy limits.

## Rendering and performance

Aquarium lighting has per-tank Auto, On and Off modes. Older saves without a mode use Auto. Manual On overrides the schedule, while Off disables illumination; both modes affect fish behavior, photosynthesis, coral lighting, lamp wear and power use. Installed lights must work to illuminate the tank. The renderer uses this same output to adjust full-scene brightness, surface glow and underwater rays, including fish and live organisms. Freshwater lamps use a warmer hue; marine lamps use a cooler hue. A darkened room does not cancel a manually illuminated aquarium.

Canvas renders a 480×240 scene scaled into the display canvas with smoothing disabled. Ocellaris now uses the user-assigned four-frame PNG atlas, bundled locally in js/clownfish-art.js and cached as 128 x 80 canvases. Its existing species ID, body proportions, visible footprint, genetic brightness and save compatibility are retained. Store and inspector thumbnails use the same artwork. Other species sprites are 64×40 procedural rasters with four fin/tail frames, distinct body shapes and markings, and gene-dependent palette brightness. Scale is growth- and species-dependent. Scene layers include background silhouettes, hardscape, live plants, equipment, residents, food, foreground organisms, glass and lighting.

Pixel polygons use scanline spans; shaded colors, fish frames and eight-phase plant animations are cached with bounded plant-cache size. Bubbles and ambient particles are bounded. The application requests 60 FPS and falls to 30 when averaged drawing time exceeds 14 ms, recovering below 8 ms. Particle disabling also caps at 30 FPS. No guarantee is made for all computers or maximum-capacity collections; the test report distinguishes measured render cost from end-to-end display performance.

## Persistence

Schema 2 JSON contains the complete state, including stock, clock, timers, seeds, genetics and transactions. Validation checks numeric ranges, required fields, habitat integrity, known IDs, entity uniqueness and counters. A narrow migration handles structurally compatible schema 1 data by initializing transaction history, offline cap and disabled VIP state. Other incompatible/future schemas remain protected.

Browser-local storage retains the active save and the previous valid backup. Corruption locks writes. Raw export, backup recovery and validated import are available. JSON export/import works independently of browser storage. No offline client-side system can prevent a player from editing their own saves; exploit prevention here concerns normal gameplay interactions and accidental data corruption.

## Biological references and uncertainty

The following primary manufacturer care resources informed the general direction. They were consulted during development; no online access is needed by the game.

- [Aqueon: freshwater aquarium water quality](https://www.aqueon.com/articles/freshwater-aquarium-water-quality) — the nitrogen cycle, maintenance and buffering context.
- [Aqueon: tetra care](https://www.aqueon.com/resources/care-guides/tetras) — community compatibility, schooling context and aquarium care.
- [Aqueon: starting a new aquarium](https://www.aqueon.com/articles/starting-a-new-aquarium-60-days) — gradual establishment of a new ecosystem.
- [Fluval: saltwater care guide](https://fluvalaquatics.com/careguides/Fluval-Saltwater-Care-Guide_en.pdf) — broad marine and reef system context.
- [Coralife: ocellaris clownfish care guide](https://www.coralifeproducts.com/-/media/Project/OneWeb/Coralife/Files/Care-Guide-PDFS/CL_CareGuide_OcellarisClownfish_Feb24.pdf) — a species-specific reference for future data review.

**Every numerical species minimum, tolerance, lifespan, incubation time and brood size in this build remains a provisional game parameter unless separately reviewed.** The catalog is not a real husbandry reference. Sprites were checked for the intended broad pattern distinctions, but there has been no comprehensive scientific art validation. Fictional species are explicitly labeled throughout.


## Life-stage art boundary

AL.LifeStages maps the existing fish growth thresholds to authored Baby/Juvenile/Adult poses and chooses stage-specific death art. The renderer never mutates growth or mortality. External broods use species egg icons; internal gestation and mouthbroods do not scatter external eggs. Coral early stages are review-only future assets. Approved adult clownfish animation remains assigned; other fish stage poses are static. Existing saves remain schema 2. See LIFE_STAGE_ART_REPORT.md.
