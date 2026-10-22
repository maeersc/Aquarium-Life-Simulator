# Aquarium Life — interface specification

## UI polish and store quantities — 2026-10-22

Playable v4.3.1 / master v4.15. The familiar aquarium layout now uses a very subtle static downward fish-scale background, opaque slate-blue panels and consistent controls. The existing guarded store supports quantities for equipment, food, consumables, ordinary medicines, rated parts and rocks. Multiple rocks enter Inventory for separate placement; sensitive livestock, unique tools and installations retain their established individual safeguards. One total charge, distinct physical IDs, capacity/stock checks, persistent receipt replay protection and local saving remain authoritative. Main schema2/tutorial2, biological simulation, economy rates, offline time and freshwater lock are unchanged. STORE_QUANTITY_RULES.md defines category behavior; UI_POLISH_QUANTITY_REPORT.md records files, actual tests and limitations. Earlier release sections below are historical where superseded.

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

## Individual equipment care — 2026-10-19

Installed-device inspectors show physical condition, maintenance, tracked service age (unknown earlier age labeled), operating efficiency, readable component names, appropriate maintenance/repair actions and warnings. Never show a fixed failure date. Open the inspector at its top; thermostat controls remain inside installed heater/chiller inspection. Tank History adds saved Equipment maintenance & failures; reads do not emit events. No standalone Temperature Control or Overnight Readiness panel is restored. Tested responsive geometry includes 1920×1080, 1600×900, 1366×768 and 390×844; detailed evidence is in the durability report.

## Equipment inventory and interface reorganization — 2026-10-19

The sidebar now has Aquariums, Aquarium Store, Field Journal, Equipment, The Dock Casino, Leaderboard Preview, VIP Store and Settings, in that order. Equipment adds searchable/filterable Inventory for stored items only. All owned installation destinations are listed, with incompatible options disabled and reasons shown. Thermostats live in installed heater/chiller inspectors. Tank Care has neither a standalone Temperature Control nor Overnight Readiness panel; current food forecasts stay in Food & Feeding and saved reports in Tank History → Reports. Breeding & Eggs and Leaderboards are removed from journal tabs; legacy routes redirect safely. Collection/inspectors/history/encyclopedia retain the corresponding breeding information. Existing dark panels, pixel thumbnails, modal controls and responsive layout are reused.


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


## Breeding observation interactions — v3.8

Breeding & Eggs has current activity/readiness, active clutches with parent/tank/date/count/progress/hatch estimates, offspring stage/survival/lineage and completed/failed history. Links open existing brood inspectors; mouthbroods are accessed from the journal or father without drawing an external pile. Coral frag clone lineage remains separate. The tab is read-only for mating: no Begin Courtship button.

The existing fish inspector shows sex/reproductive role, maturity, partner, applicable readiness/courtship/gravid/preparing/tending/male-mouthbrooding/recovery states, active brood, last spawn and cooldown. Explain gravid with its tooltip. Refresh that section once per UI heartbeat without closing the inspector, replacing rename forms or resetting the three-second outline. Courtship targets steer existing sprites; markers do not alter eyes/anatomy. Keep responsive internal scrolling and readable IDs at 1920×1080, 1600×900, 1366×768 and 390×844. All modal windows continue the same simulation clock.

## Equipment filters, inspector research and The Dock Casino - v3.7 current

Implemented the equipment-category dropdown and original fragging-tool previews, moved paid species research to living owned-fish inspectors, and added the authorized seventh sidebar entry The Dock Casino with playable Gold Fish and Predator & Prey. All wagers and returns use the existing account wallet/ledger and saved round authority; all research remains 5 AC once per canonical species. The aquarium header controls share the information-column grid and align to its actual panel edge. See STORE_CASINO_UPDATE_REPORT.md and CASINO_RULES.md for the release, verified probabilities, local persistence and limitations. Existing biological simulation, 20-minute day, rewards, freshwater lock, livestock/art approvals and local saves remain. Earlier release sections are historical where superseded.

## Main aquarium layout cleanup - 2026-10-15

The main screen now pairs a compact owned-aquarium dropdown with + New aquarium, centers the Keeper badge, removes the decorative slogan and three bottom care cards, and uses the reclaimed space for a larger proportional tank. Feeding remains in Equipment > Tank Care > Feeding, water changes in Equipment > Water Change, and livestock purchases in Aquarium Store. The dropdown preserves the selected destination through existing local saves. Canvas coordinates, three-second selection highlights, freshwater lockout and simulation rules remain unchanged. See [UI_LAYOUT_CLEANUP_REPORT.md](UI_LAYOUT_CLEANUP_REPORT.md) for changed files, desktop measurements, offline Chrome/Edge acceptance results and limitations.

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

The existing AC display is a native keyboard-accessible button. Financial Overview is a centered dialog with X/Escape/backdrop dismissal, internal scroll, period summaries, actual chart, filters and twenty-receipt pages. Equipment gains Coral Fragging; eligible coral inspectors open a method/mount confirmation with parent and child value/size/risk previews. Saltwater Store gains Research; Deep Market gains Wanted Livestock. Neither adds a seventh sidebar window. Report text and source limitations are shared with Journal Encyclopedia. Aquarium time continues in these dialogs.

## Earlier milestone record - historical where superseded

**Authorized 2026-10-14:** The user approved the complete 25/5/5 roster and rarities, confirmed saltwater-only, and explicitly requested "Implement v2.9". Roster approval and artwork approval are separate; new artwork remains unapproved. [Authorization](planning/v2.9/approval.json).

## v2.9 — current implementation

Implemented the twelve-step saved/skippable saltwater tutorial with medical guidance, three-second selection outlines, disabled freshwater UI, separate +50 healthy / +100 survival rewards with persistent death/recovery tracking, Deep Market display rename, local asset-value leaderboard preview, exact 15,000-US-gallon / 5,000-AC aquarium, proportional water-change salt consumption, independent mystery products and the approved 35-species marine batch. Saves remain local to each player's browser on their PC. The bottom mystery product is content-held because its Legendary host specialist is not eligible. See [V29_UPDATE_REPORT.md](V29_UPDATE_REPORT.md) for actual checks, care/art limits and release details. Earlier milestone sections below are historical wherever superseded.

Keep six main windows. Settings contains Resume/Restart Tutorial. The guide can Skip/Back/Next/Show me and highlights actual available controls over native dialogs. Expiring three-second outlines do not close inspectors. Freshwater controls are disabled with the coming-update message. Field Journal contains local Leaderboards and survival progress in Tank History. Store coral purchase asks for a valid supported mount before completing.

## Earlier milestone record




## Ocean Diving v2.8 — historical, 2026-10-14

MDP **v3.3**, retaining all 31 major sections. **Ocean Diving** beside Keeper Level opens Reef (Level 5 / 1,000 AC) or Deep Sea (Level 10 / 10,000 AC). Fiji, Caribbean, Hawaii and Japan have original regional scenery and a compact playable map. W/A/S/D, arrows and on-screen buttons move one tile; every successful step costs exactly 5% oxygen from 100%. Blocked movement and collection clicks cost none. Eight temporary slots become owned only on a successful boat return with oxygen remaining. Exhaustion/confirmed abandonment forfeits discoveries without a fee refund.

Aquariums continue at 1× during planning, diving and results, using the existing 20-real-minute game day. Explicit safe receivers, supported coral mounts, species-conditioned survival, finite transport holding, persistent provenance and Reputation 5 Black Market-only resale are integrated. Confirmed paid Black Market purchases earn bounded reputation; canceled/failed/duplicate transactions do not. Direct normal-store livestock is restricted to Tiers 1–3; eight daily Fish slots and independent Mystery Egg odds remain unchanged. Nominal tank/equipment capacities now ceil to whole US gallons; physical liters and precise water-change calculations remain exact.

**No new biological species.** The approved 38-entry v2.7 batch and all protected freshwater content remain the roster baseline. Six sourced encounter profiles reference existing IDs; Hawaii wildlife is observation-only, and unsupported regional/depth combinations offer inert fictional salvage rather than invented animals. All captures are fictional restricted game recovery, not real collection authorization. New art is unapproved pending user review. Saves and expedition receipts remain on each player's PC in browser storage. See [DIVING_UPDATE_REPORT.md](DIVING_UPDATE_REPORT.md) and [the region ledger](assets/diving/registry.json). DIST is rebuilt through `python build.py`. Earlier milestones below are historical where superseded.

The always-visible Ocean Diving button is immediately after the saved Keeper Level badge; the six sidebar windows are unchanged. Planning uses the shared detail dialog, two mode tabs, region selector, exact rental breakdown, explicit launch confirmation, encounter cards and inventory. X, Escape and backdrop close ordinary windows. All three request confirmation during an active trip; interior clicks do not dismiss it. Purchase confirmation is still explicit and validates again before commitment. A sticky oxygen/region/inventory/boat-route HUD stays visible while scrolling the active dive. Keyboard auto-repeat is ignored; a controlled held-key timer submits actual steps. Touch-friendly direction buttons use the same action path.

Black Market shows reputation level, total XP, next-level XP, purchase caps and resale lock. Owned diving fish, coral and non-fish residents appear under Black Market → Sell with condition/budget checks; their inspectors route to that channel. Ordinary exchange/cutting actions reject diving provenance. Main tank selectors and store summaries show nominal whole gallons; precise replacement-water amounts retain fractional gallons.

## Livestock expansion v2.7 — roster baseline milestone, 2026-10-14

MDP **v3.2** retains exactly 31 major sections. Added **38 unique marine entries: 28 fish, five named stony corals and five non-fish invertebrates**. All 38 passed the pre-registration scientific-name/synonym duplicate audit; none were skipped. The runtime now has **80 fish (69 marine, 11 protected freshwater), ten marine coral entries and five non-fish invertebrates**. The six existing freshwater plants are unchanged. Existing art-only and planned entries are excluded from these totals.

All six Mystery Egg rarity pools are now populated; the earlier empty-pool content hold is superseded. Keep independent 50/25/15/7.5/2/0.5 percent odds, 600 AC, three daily eggs, existing level/incubation gates and safe-destination checks. Daily Fish shopping remains exactly eight visible slots: 3 Common, 3 Uncommon, 1 Rare, 1 Mystery Egg. Higher tiers do not add normal Fish cards. Fixed retail, persistent selected aquarium, continuous offline simulation, rarity/genetics and existing specialist clownfish holds remain.

New livestock has inspectors, rarity, care information, value, host-filtered health compatibility and additive save support. Corals use player-selected supported rock/rack placement. Invertebrates are separate bottom residents with feeding, crawling/filtering, condition, death and transfer records. Their egg/planktonic larval reproduction and art are unsupported. New fish natural breeding is enabled only for the five explicitly supported profiles; Mystery Egg development is a simplified game presentation, not evidence of complete captive culture.

There are 38 new transparent sprite sheets / 304 static stage-state views. All are unapproved; 12 sheets carry explicit framing review flags. Existing approved artwork is preserved. Review [the new artwork gallery](expansion-review.html). [Implementation report](LIVESTOCK_EXPANSION_REPORT.md), [permanent registry](assets/expansion-v27/registry.json), [continuity source](PROJECT_CONTINUITY_SOURCE.md) and [PDF workflow](PDF_WORKFLOW.md) record the limits. **PDF regeneration remains pending: PDF authoring/rendering prerequisites are unavailable in this environment.** Earlier milestone material is historical where superseded.

### v2.7 interface behavior

Retain the six-window sidebar and current selected aquarium across store open/close, tab changes, purchases and reload. Fish keep the existing eight-card daily layout. Five invertebrate products appear under Saltwater → Bottom Feeders; named corals appear under Saltwater → Corals with scientific names and difficulty. Unsafe destinations reject or offer an eligible destination before payment. Invertebrates have their own inspector and transfer/remove/sell actions, linked diagnosis, Current Value and rarity. Collection/encyclopedia filter marine fish, corals and invertebrates without adding freshwater entries. The collection links to a separate offline 38-entry art review with category/species/direction/backdrop controls and separately saved review notes; notes never approve art or replace game saves.

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


## Main interface overhaul — 2026-10-13 (current)

The permanent sidebar is exactly Aquariums, Aquarium Store, Field Journal, Equipment, VIP Store (Preview Only), Settings. All open titled native dialogs with top-right X/Escape/focus and internal scrolling. There is one primary window plus appropriate secondary inspectors/confirmations. A header selector switches windows cleanly; sub-tabs persist for the session. AL.Shell owns routing and presentation, reusing AL.UI views and Core transactions; AL.Store remains the sole buying/selling/listing interface. Existing modal pause behavior is preserved.

The viewport shell keeps the actual aquarium canvas 2:1, with no page scrolling across verified 1920×1080, 1440×900, 1366×768, 1280×720, 1024×600, 760×650 and 390×844 sizes. Summary panels scroll internally; narrow layouts use a horizontal summary strip. TOTAL AQUARIUM VALUE is centered above water, recalculated through AL.Valuation; click opens Aquariums / Tank Value. No scene artwork is covered.

Aquariums tabs: My Aquariums, New Aquarium, Tank Setup, Tank Value, Water & Wellbeing. Journal tabs: Livestock Collection, Species Encyclopedia, Breeding & Eggs, Achievements, Quests & Objectives, Tank History, Disease & Treatment Guide. Collection includes individual livestock and broods with six filters. Historical fish discoveries are preserved; historical plant/coral discovery is not fabricated. Equipment tabs: Lighting, Tank Care, Water Change; equipment removal stores the original condition/capacity for reinstallation. Food/feeder care sits in Tank Care. Store Buy/Sell/Orders retains the three habitats and 8/7/7 subcategories, fixed retail, risky saved listings and explicit destination. Coral/plant cutting sales are in Sell. VIP five tiers and existing-art previews remain non-purchasable; unimplemented premium artwork has honest empty states.

Player-created starting aquariums and subsequent purchases are empty and dry. Existing saves are not cleared. Marine external eggs use persistent spawning sites, visible stage framing and selectable hitboxes; inspector shows parents, stage, viability, progress, calibrated care and real brood value. Failed external marine clutches remain briefly inspectable/removable; internal brood behavior is unchanged. Settings retains saves/preferences/recovery. [Verified acceptance and limitations](UI_OVERHAUL_REPORT.md). Older dated descriptions below are historical and are superseded where navigation or dry construction differs.

## Marine economy, disease and valuation — 2026-10-13

Main aquarium footer displays clickable Tank Value for the selected aquarium. Its modal separates Base Tank Value, Current Total Tank Value, physical shell, equipment, fish/viable broods, corals/plants, bottom dwellers, rock/substrate/racks and decorations plus bounded history. It is distinct from spending credits.

Fish/benthic and coral inspectors display Current Value and eligible dealer offer, optional valuation modifiers, nutrition/stress and confidence-qualified medical findings. Hidden conditions are not automatically named. Coral Overview/Care tabs remain; the overview adds living tissue/pigment/polyp measures, medical actions and history. Examination uses diagnostics. Diagnosis & treatment lists owned batches with host/water/quarantine restrictions and duration. Start consumes one unit, Stop refunds none. A course progresses only while simulation time runs; modal inspection pauses existing biology. Quarantine transfer filters eligible marine destinations and offers explicit valid coral mounts, preserving identity and history. Equipment offers Prepare bare quarantine habitat only for an unoccupied marine quarantine tank; normal prepare/cycle/readiness still apply.

Exactly three primary store tabs remain. Category counts are now Saltwater 8 (including Medicine & Treatment), Freshwater 7 unchanged, Black Market 7 (including Restricted Treatments). Ordinary products/medicines have fixed prices; dealer listings show persisted prices and uncertainty warnings. Medicine purchases go to shared medical inventory and preserve the selected aquarium. Medical inventory shows units/batches; restricted quality stays undisclosed until an assay. Freshwater-specific medicine/disease controls were not added. Existing X/Escape/focus/scroll/backdrop/responsive behavior remains.

The obsolete bubbled quantity handler is now limited to its original buyFish form, avoiding the modal conflict. Quarantine/treatment transfer checks reject unsafe water and active-course reef bypasses. New medicine previews use locally drawn bottles/diagnostic kit forms in the existing store illustration system; no animal art was replaced. The older UI phase descriptions below are historical; complete dry construction, substrate biology, comprehensive inventory and illustrated VIP tiers remain unfinished.


## Current shared store and collection UI — 2026-10-12

Centered 1080px/84vh modal, internal scroll, visible aquarium backdrop, fixed close/header/tab controls, native focus trapping and higher-dialog-first Escape. Exactly Saltwater/Freshwater/Black Market with 7/7/6 category tabs; explicit saved destination selector and compatibility commit controls. No tab/purchase implicit aquarium selection. Empty freshwater category text: “Freshwater content is coming soon.” Local product art includes actual fish/coral/rock assets and recognizable canvas equipment/consumable/decoration forms. The collection gallery supports biological/designer/global views, all stage/death states, linked-base filters, frame controls and review notes separate from the player save. Coral mounting previews combine text with red/yellow/green outlines; mounted rack/rock inspectors support persisted edits. Palette remains locked.


The [consolidated development specification](MASTER_DEVELOPMENT_PROMPT.md), sections 23 and 26, defines the target. `css/theme.css` implements its locked colors; `css/main.css` owns the existing responsive layout and components.

## Implemented layout

A near-black application surrounds slate-blue panels. The main aquarium remains visible above management screens. The header shows level, credits, clock, notifications, settings, and save state. Aquarium tabs select independently simulated tanks. Navigation opens functional fish, store, equipment, food, plants/corals, breeding, journal, market, achievements, VIP, and settings screens. Water details open from the aquarium sidebar.

## Lighting and coral interaction

The aquarium toolbar offers Auto, On, and Off. Disabled or broken lighting reports its condition. A saved setting belongs to the selected tank. The renderer visibly reflects output and intensity.

In a suitable reef, **Plants & corals → Place coral** starts a preview. Moving the pointer positions its anchor; clicking commits one purchase. Arrow keys adjust the anchor, Enter confirms, and Escape or Cancel discards the preview. Simulation pauses while placing. Previewing does not consume funds or stock. Navigation, tank changes, and opening a dialog cancel pending placement.

Selecting a coral in the tank or pressing Inspect opens its Overview and Care tabs. Overview shows individual health, age, growth, color, value, and cutting readiness. Care shows light and flow targets/current values, water ranges, and shared simulation warnings. Reposition returns the existing colony to preview mode; Transfer and Sell cutting use validated actions. Dead organisms offer removal.

The tab list supports Left/Right, Home, and End, maintains focus, and labels its panel. Native dialogs and forms provide keyboard interaction. A visible focus outline identifies the aquarium canvas. Placement handles camera zoom and pan; positions persist in JSON and browser saves.

## Verification and remaining screens

Automated checks cover desktop and narrow layouts, keyboard coral editing, real pointer placement, dialogs, and offline transactions. Comprehensive screen-reader and extended touch testing remain open.

Dry-tank construction, sand/rock stores, a substrate inspector, separate water-filling controls, and physical rock editing are not implemented. Inventory is currently represented through supply/food management rather than a dedicated comprehensive inventory screen. UI scaling, graphics preset selection, and illustrated VIP tiers also remain open. Existing screens must not label these future systems complete.

## Art-review gallery 1.1

The existing footer opens the offline Fish/Corals/Rocks gallery. Fish selection includes the 22 runtime species and five clearly labeled art-only subjects. Enlarged right/left previews share frame and display scale; a checkbox shows head-local eye component bounds. Motion selects normal, idle, mirrored turning and frozen death concepts. Frame stepping, pause, native views and aquarium-scale camera/lighting controls support inspection.

Corals expose all five visual states with a comparison grid. Rocks expose all three art collections and four variants, separate selection outlines and clamped click-to-position preview arrangements. Preview layouts and explicit user review status/notes persist under a gallery-only key. They never overwrite gameplay saves. New assets default to Ready for Review.


## Life-stage review gallery

The index footer links life-stage-review.html. Categories contain 18 fish, five corals and four benthic fish (27 distinct implemented entries). Four stage columns each show alive/dead plates and fixed 2x scene-pixel scale references. Direction, background, enlarged preview, eye anchors and optional motion inspection are available. Eight static poses do not imply eight animations. Review notes and explicit approval choices persist under aquarium-life-stage-reviews-v1, separate from game saves. Mobile layout uses two columns. Earlier art-only fish and rocks remain in the previous linked gallery.

### v2.5/v2.6 interaction details

Store browsing continues game time and updates only the countdown each second; the grid rebuilds on calendar rollover. Purchase details pause for review. Searching does not remove the eight daily slots; the search input remains relevant in other categories. Catalog entries remain in Field Journal. Each colored rarity silhouette has a text tier label. Mystery Egg details show its original artwork, exact six-tier odds, independent-roll statement, purchase-reveal policy and explicit missing-content reason. No other aquarium can override the content hold.

Continue shows catch-up progress followed by a factual Welcome Back report. Hidden-tab return uses the same path and refreshes an open store to the current day. Settings explain continuous away time instead of offering obsolete relaxed/capped controls. The six-sidebar layout, gallon display, lighting, depth controls and selected aquarium remain intact.

## Survival UI v3.4

Tank History updates the eligibility and recovery countdown while open. A live payment shows exactly Livestock Survival Bonus: +100 AC. A confirmed death shows exactly Livestock lost! Daily survival bonus interrupted. Complete one full in-game day without a death to restore eligibility. Offline catch-up suppresses individual reward/death toast bursts and gives actual earned survival AC and completed days without a payment in one return summary. Financial receipt details expose the qualifying day and qualification status separately from the actual payment timestamp.
