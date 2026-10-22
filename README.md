# Aquarium Life

## Protected production distribution - 2026-10-22

Current master v4.17; gameplay remains v4.3.1 with a new protected distribution pipeline. Production now minifies JS/CSS, shortens internal identifiers, uses content-derived code filenames and excludes review pages, source maps, project documentation and tooling. Human-readable game code and original assets remain untouched. Assets retain their original pixels and offline file transports; no encryption, passwords, licensing dependency, profile rewrite or save-key change is introduced. Runtime safety and the mandatory performance pass take priority over obfuscation. DISTRIBUTION_PROTECTION_REPORT.md records exact mechanisms, commands, executed tests, benchmarks and limits. Earlier build descriptions are historical where superseded.

## UI polish and store quantities — 2026-10-22

Playable v4.3.1 / master v4.15. The familiar aquarium layout now uses a very subtle static downward fish-scale background, opaque slate-blue panels and consistent controls. The existing guarded store supports quantities for equipment, food, consumables, ordinary medicines, rated parts and rocks. Multiple rocks enter Inventory for separate placement; sensitive livestock, unique tools and installations retain their established individual safeguards. One total charge, distinct physical IDs, capacity/stock checks, persistent receipt replay protection and local saving remain authoritative. Main schema2/tutorial2, biological simulation, economy rates, offline time and freshwater lock are unchanged. STORE_QUANTITY_RULES.md defines category behavior; UI_POLISH_QUANTITY_REPORT.md records files, actual tests and limitations. Earlier release sections below are historical where superseded.

## Performance optimization — 2026-10-22

Playable v4.3.0 / master v4.14. One capped60/30FPS scheduler, independent fixed biological steps, on-demand lossless native sources, bounded caches, cached scenery, covered/hidden render suspension, changed-value HUD updates and five graphics preferences. Main schema2/tutorial2, all player assets, protected art, local saves, freshwater lock and biological/economic formulas remain intact. PERFORMANCE_SYSTEM.md and PERFORMANCE_SETTINGS_SAVE_SCHEMA.md describe runtime/persistence; AQUARIUM_LIFE_PERFORMANCE_OPTIMIZATION_REPORT.md records actual measurements and executed regressions. The31-section authority is MASTER_DEVELOPMENT_PROMPT.md, with an exact handoff copy in PROJECT_CONTINUITY_SOURCE.md. Earlier art/PDF limitations remain separate.

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

## Mystery fish diving — v3.9 current, 2026-10-15

Implemented the authorized Mystery Fish update (request v3.5) on top of playable v3.8. New valid Reef/Deep trips guarantee a reachable regional fish, concealed until boat return, with saved assignments, original question-mark art/reveal, explicit safe receiving and permanent transport-loss evidence. Empty/closed collectible pools block launch. Existing oxygen, fees, resale, local accounts, biology, genetics, breeding, care rewards and freshwater lock remain. See [MYSTERY_DIVING_RULES.md](MYSTERY_DIVING_RULES.md) and [MYSTERY_DIVING_UPDATE_REPORT.md](MYSTERY_DIVING_UPDATE_REPORT.md). Current master is v4.2; earlier release entries are historical where superseded.

## Automatic marine breeding — v3.8 current, 2026-10-15

Replaced manual marine courtship with autonomous, species-aware breeding, visible swimming/nest behavior, individual reproductive status and a read-only Breeding & Eggs observation dashboard. New clutches use real parent/tank IDs, saved reproductive roles and RNG, species-specific care/losses and bounded offspring reservations. All prior local accounts, art/genetic identities, coral lineage, rewards, heaters, mortality logs, store/casino functionality and the 20-minute day remain. Freshwater stays locked. See [BREEDING_RULES.md](BREEDING_RULES.md), [BREEDING_SAVE_SCHEMA.md](BREEDING_SAVE_SCHEMA.md) and [BREEDING_UPDATE_REPORT.md](BREEDING_UPDATE_REPORT.md). Earlier release entries are historical wherever superseded.


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

Equipment > Tank Care and Field Journal > Tank History show **Overnight Readiness**. Welcome Back and Tank History retain actual death-step causes, identities, food, equipment and chemistry separately from current recovered water. Local loads retain an untouched pre-repair snapshot when storage permits, exportable in Settings. Saves and downloads remain on each player's PC/browser. Review [OVERNIGHT_REPAIR_REPORT.md](OVERNIGHT_REPAIR_REPORT.md) for formulas, the complete absence matrix, reproducible evidence and limitations. Current playable release is v3.5 / consolidated MDP v3.8. Earlier release sections below are historical where superseded.

## Daily livestock survival reward v3.4 - current rule, 2026-10-15

Players earn **100 AC** for every completed qualifying in-game day without a livestock death. The player must own eligible living marine livestock throughout the full simulated day. This is one account-wide payment, not one per aquarium. The separate healthy-aquarium award remains **50 AC**; both independently qualified awards total **150 AC**.

A confirmed fish, coral or bottom-invertebrate death cancels the current qualifying day and starts 1,440 game minutes of recovery. Another confirmed death restarts recovery. Recovery time cannot count toward a qualifying reward day. Illness or living coral bleaching is not a death. The authoritative game calendar remains 20 real minutes per day; legitimate offline catch-up processes the same conditions. Game windows do not stop simulation. Casino requirements apply only if that game is implemented.

Existing balances and actual historical ledger receipts remain unchanged. Every future survival payment is 100 AC through the existing financial service, with canonical account/transaction IDs, actual payment time and completed qualifying day/status. Local save, financial sequence and offline timeline guards prevent re-awarding a settled day. See [V34_UPDATE_REPORT.md](V34_UPDATE_REPORT.md) and [FINANCIAL_TRANSACTIONS.md](FINANCIAL_TRANSACTIONS.md).

## Earlier milestone material - superseded where inconsistent

## v3.3 current release - 2026-10-14

Implemented the authorized v3.1 coral fragging/trading, v3.2 financial dashboard and v3.3 Marine Research Center. Equipment has three reusable coral tools and two mounting consumables; eligible parents produce independently simulated, mounted clones with tissue loss, recovery and lineage. Diving livestock can use regular or Deep Market dealers; regular pays floor(0.60 x the same Deep reference), and Deep requires Reputation 5 plus an active wanted request. Wanted Livestock remains separate from exactly four rotating dealer stock slots.

The AC button opens a reconciled, persisted financial history. Existing wallets migrate unchanged; new profiles start at the requested 5,000 AC. Saltwater Research and the existing Encyclopedia share permanent 5-AC canonical-species unlocks. All 94 marine fish are indexed; 93 real species are researchable, one fictional entry is preview-only. Fully verified dossiers: 0; incomplete: 93; five have reviewed biological annotations. Partial content is disclosed before purchase. See [V33_UPDATE_REPORT.md](V33_UPDATE_REPORT.md), [FINANCIAL_TRANSACTIONS.md](FINANCIAL_TRANSACTIONS.md) and [RESEARCH_SOURCES.md](RESEARCH_SOURCES.md).

Saltwater-only scope, safe persistent store destinations, local PC/browser saves, existing rewards/odds, all old livestock and artwork approvals/holds remain. No new biological species or art assets were added. Full printable continuity source is updated; binary PDF regeneration remains pending. Current playable version v3.3 / consolidated MDP v3.6.

Upload the contents of [DIST](DIST/) or extract AquariumLife-GitHub-Pages.zip into the GitHub Pages publishing root. Rebuild after every source edit with python build.py. Saves, backups, research and financial receipts stay in each player's browser on their PC; JSON exports are local downloads. Browsers/origins have separate storage. No test profile or player save is shipped.

## Earlier milestone record - historical where superseded

## v2.9 — current implementation

Implemented the twelve-step saved/skippable saltwater tutorial with medical guidance, three-second selection outlines, disabled freshwater UI, separate +50 healthy / +100 survival rewards with persistent death/recovery tracking, Deep Market display rename, local asset-value leaderboard preview, exact 15,000-US-gallon / 5,000-AC aquarium, proportional water-change salt consumption, independent mystery products and the approved 35-species marine batch. Saves remain local to each player's browser on their PC. The bottom mystery product is content-held because its Legendary host specialist is not eligible. See [V29_UPDATE_REPORT.md](V29_UPDATE_REPORT.md) for actual checks, care/art limits and release details. Earlier milestone sections below are historical wherever superseded.

See [the current release report](V29_UPDATE_REPORT.md), [new art gallery](v29-review.html), [DIST](DIST/) and [build manifest](DIST/build-manifest.json).

## Historical milestone record


## Ocean Diving v2.8 — historical, 2026-10-14

MDP **v3.3**, retaining all 31 major sections. **Ocean Diving** beside Keeper Level opens Reef (Level 5 / 1,000 AC) or Deep Sea (Level 10 / 10,000 AC). Fiji, Caribbean, Hawaii and Japan have original regional scenery and a compact playable map. W/A/S/D, arrows and on-screen buttons move one tile; every successful step costs exactly 5% oxygen from 100%. Blocked movement and collection clicks cost none. Eight temporary slots become owned only on a successful boat return with oxygen remaining. Exhaustion/confirmed abandonment forfeits discoveries without a fee refund.

Aquariums continue at 1× during planning, diving and results, using the existing 20-real-minute game day. Explicit safe receivers, supported coral mounts, species-conditioned survival, finite transport holding, persistent provenance and Reputation 5 Black Market-only resale are integrated. Confirmed paid Black Market purchases earn bounded reputation; canceled/failed/duplicate transactions do not. Direct normal-store livestock is restricted to Tiers 1–3; eight daily Fish slots and independent Mystery Egg odds remain unchanged. Nominal tank/equipment capacities now ceil to whole US gallons; physical liters and precise water-change calculations remain exact.

**No new biological species.** The approved 38-entry v2.7 batch and all protected freshwater content remain the roster baseline. Six sourced encounter profiles reference existing IDs; Hawaii wildlife is observation-only, and unsupported regional/depth combinations offer inert fictional salvage rather than invented animals. All captures are fictional restricted game recovery, not real collection authorization. New art is unapproved pending user review. Saves and expedition receipts remain on each player's PC in browser storage. See [DIVING_UPDATE_REPORT.md](DIVING_UPDATE_REPORT.md) and [the region ledger](assets/diving/registry.json). DIST is rebuilt through `python build.py`. Earlier milestones below are historical where superseded.


## GitHub Pages build

Prepare the private build-only tools once with `python tools/production/bootstrap.py`.
The protected production build preserves readable development source, excludes maps/review tools and retains original pixel assets/local saves. See [distribution protection](DISTRIBUTION_PROTECTION_REPORT.md).

Run **`python build.py`** to refresh **`DIST`** from the current game sources and
rebuild **`AquariumLife-GitHub-Pages.zip`**. The ZIP contains the contents of DIST
at its root. Upload those contents to your publishing repository; keep
`index.html`, `.nojekyll`, `js`, `css` and `assets` together. See
[GitHub Pages deployment and local saves](GITHUB_PAGES.md) for publishing steps.

All active saves, recovery backups and timeline data stay in each player's local
browser storage. Export/Import JSON in Settings provides PC file backups and
transfers; there are no server saves. Moving from a local file to the hosted
address requires exporting and importing the old save. See
[build verification](GITHUB_PAGES_BUILD_REPORT.md) for the actual DIST tests.

## Livestock expansion v2.7 — roster baseline milestone, 2026-10-14

MDP **v3.2** retains exactly 31 major sections. Added **38 unique marine entries: 28 fish, five named stony corals and five non-fish invertebrates**. All 38 passed the pre-registration scientific-name/synonym duplicate audit; none were skipped. The runtime now has **80 fish (69 marine, 11 protected freshwater), ten marine coral entries and five non-fish invertebrates**. The six existing freshwater plants are unchanged. Existing art-only and planned entries are excluded from these totals.

All six Mystery Egg rarity pools are now populated; the earlier empty-pool content hold is superseded. Keep independent 50/25/15/7.5/2/0.5 percent odds, 600 AC, three daily eggs, existing level/incubation gates and safe-destination checks. Daily Fish shopping remains exactly eight visible slots: 3 Common, 3 Uncommon, 1 Rare, 1 Mystery Egg. Higher tiers do not add normal Fish cards. Fixed retail, persistent selected aquarium, continuous offline simulation, rarity/genetics and existing specialist clownfish holds remain.

New livestock has inspectors, rarity, care information, value, host-filtered health compatibility and additive save support. Corals use player-selected supported rock/rack placement. Invertebrates are separate bottom residents with feeding, crawling/filtering, condition, death and transfer records. Their egg/planktonic larval reproduction and art are unsupported. New fish natural breeding is enabled only for the five explicitly supported profiles; Mystery Egg development is a simplified game presentation, not evidence of complete captive culture.

There are 38 new transparent sprite sheets / 304 static stage-state views. All are unapproved; 12 sheets carry explicit framing review flags. Existing approved artwork is preserved. Review [the new artwork gallery](expansion-review.html). [Implementation report](LIVESTOCK_EXPANSION_REPORT.md), [permanent registry](assets/expansion-v27/registry.json), [continuity source](PROJECT_CONTINUITY_SOURCE.md) and [PDF workflow](PDF_WORKFLOW.md) record the limits. **PDF regeneration remains pending: PDF authoring/rendering prerequisites are unavailable in this environment.** Earlier milestone material is historical where superseded.


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


## Latest interface update

Open `index.html` offline. The sidebar now has six management windows; the live tank value above the water opens its breakdown. Equipment, feeding, water changes, collection, breeding and local sales are reorganized without removing saved progress. New player-created tanks start empty/dry; buy equipment, prepare water and cycle before stocking. Marine clutches can be selected directly in the aquarium. See [UI_OVERHAUL_REPORT.md](UI_OVERHAUL_REPORT.md) for screenshots and verified results. No paid VIP services or network connection.

## Marine economy, disease and valuation — 2026-10-13

The current offline build includes marine disease diagnosis and timed care, Saltwater → Medicine & Treatment, Black Market → Restricted Treatments, saved dealer risk/price rolls and separate retail/current asset/dealer values. Click a fish/coral for Current Value and health actions; click Tank Value for shell/content totals.

For fish quarantine: purchase a marine Quarantine aquarium, open its Equipment screen and choose Prepare bare quarantine habitat while it is unoccupied. Prepare and cycle its own water normally. Buy diagnostics in the Saltwater medicines tab, inspect/examine the animal, then choose Move to quarantine. Switch to that tank to start an eligible owned course. Maintain appropriate water/food and close the inspector/resume time so treatment advances. Selected antibacterial care requires a follow-up examination at least 24 game hours later. Corals need a separate cycled marine quarantine with appropriate light/flow and a permitted rock/sand/rack mounting; copper cannot treat them. No medicine is a universal cure. Prices/clinical rates are game parameters, not real dosing instructions.

Ordinary medicine purchases enter medical inventory. Restricted fictional batches can fail or harm and retain hidden quality on reload; assay consumes diagnostics. Export a JSON backup from Settings when moving folders/browsers. Existing saves migrate without erasing owned livestock, wallet or selected aquarium. No new livestock or online leaderboard was added. The future verified leaderboard is documentation only.

[Implementation, tests and limits](ECONOMY_DISEASE_UPDATE_REPORT.md). Previous milestone MDP: v2.8. Older phase sections below describe their historical deliveries.


A playable, entirely offline aquarium simulation with local pixel-art livestock and procedural scenery. First playable build, **v0.1**.

## Play

Open **`index.html`** in Chrome, Edge, or Firefox. If you received a ZIP, extract the entire folder first. Keep `index.html`, `css/`, and `js/` together.

No install, server, Node.js, account, internet connection, or payment is needed. The game uses classic local scripts and makes no gameplay network requests. Browser JavaScript must be enabled.

Chrome and Edge were tested through actual `file://` URLs with network access disabled. Firefox is an intended target but was not installed in the test environment; it has not been browser-verified.

## Current collection and store update

Open [Clownfish collection review](clownfish-review.html) for 31 catalogued scientific names and 25 linked designer varieties, every living/dead life-stage view, swimming frames, original/reference comparisons and the global art audit. Open [Coral attachment study](coral-placement-review.html) to test supported mounting without modifying your aquarium save. New art remains provisional; five specialist care profiles are visible but not purchasable yet.

The Store opens over your aquarium with Saltwater/Freshwater/Black Market tabs. Its header remembers your selected aquarium. Incompatible purchases require you to choose an eligible destination explicitly; equipment and habitat items install there, supplies enter inventory. A purchase or tab change never switches aquariums automatically. Place coral on a permitted rock top, stable sandbed base or mounted rack; unsupported open water is blocked. Click a rock/rack to edit it; relocate attached corals before removing their support. Saved older unsupported colonies stay owned with a relocation notice.

See [current delivery report](CLOWNFISH_STORE_REPORT.md) and [catalog](CURRENT_LIVESTOCK_CATALOG.md). This milestone preserves freshwater livestock definitions, art and biology.

## Earlier life-stage art update

Open **[Life-stage art review](life-stage-review.html)** from the game's footer. All 27 then-implemented livestock entries have Egg, Baby, Juvenile and Adult artwork, each alive and dead: 216 static stage/state images. Compare stages, switch direction/background, inspect eye anchors and save review notes separately from your game. The approved adult Ocellaris animation remains intact; coral early stages are preview-only art support.

That earlier stage-only update added no species; the later collection/store milestone is described above. [Delivery and test report](LIFE_STAGE_ART_REPORT.md) · [Complete livestock catalog](CURRENT_LIVESTOCK_CATALOG.md) · [Assets and prompts](assets/livestock/life-stages/README.md).

## Earlier art update 1.1

Open [Livestock Art Review](art-review.html) from the game's footer. Fish includes all 22 current species plus five new art-only priority subjects; Corals shows five visual states; Rocks includes Fiji/Caribbean/Hawaiian size and arch variants. Use the eye-anchor checkbox, animation controls, background and camera options to inspect the artwork. Rock preview arrangements save separately from your collection.

Eye detail is now registered to the head and sampled at the final sprite size; left/right presentation follows displayed movement with stable transforms. The new coral and marine scenery art is integrated into the existing game. The five new fish remain art-only subjects. See [ART_UPDATE_REPORT.md](ART_UPDATE_REPORT.md) for tests, limitations and the pending visual approval.

## Your first aquarium

The original clownfish benchmark gallery is preserved at [art-review-v1.html](art-review-v1.html); the subsequent fish/coral/rock gallery remains at [art-review.html](art-review.html). Current stage artwork and its review status are documented in the life-stage report above.

1. Choose freshwater or marine. Both routes start with 3,000 AC and an empty 75 L aquarium with basic equipment and supplies.
2. **Prepare water**, then **Start fishless cycle**. Use **Finish fishless setup** to simulate the 36-hour setup while all aquariums are unoccupied. This is an accelerated game mechanic, not real aquarium cycling guidance.
3. Open **Field journal** and claim your preparation and cycling rewards.
4. In **Aquarium store**, inspect a species and read its compatibility report. Guppies or a school of six neon tetras are affordable freshwater options; an ocellaris clownfish fits the marine starter.
5. Add plants or suitable reef corals. Use **Food & feeding** to select food your residents accept. Wait for food to be eaten before feeding again.
6. Watch ammonia, nitrite, oxygen, hunger and equipment durability. **Water change** opens the laboratory, where prepared 10%, 25%, and 50% changes affect actual chemistry.
7. Complete journal entries, earn credits, and unlock larger aquariums. Daily showcases and bounded livestock sales provide recurring income.

## Controls and management

- **Pause / 1× / 5× / 20×:** below the aquarium. At 1×, a real minute advances one game hour.
- **Inspect fish:** select a visible fish or open its collection entry. Rename, inspect lineage, treat an infection, transfer, or view a local sale offer.
- **Camera:** zoom and pan with the lower-right aquarium controls.
- **Aquarium light:** use the control above the tank to choose **On**, **Off**, or **Auto**. On lights the tank even at night; Off dims the view; Auto follows the equipment screen's daily schedule. The intensity slider also changes visible brightness. Each tank's choice is saved.
- **Aquarium tabs:** switch between owned tanks. All owned tanks simulate; only the selected tank renders.
- **Equipment:** toggle, service, install, or transfer devices; set target temperature and lighting schedule.
- **Place coral:** in a prepared, cycled reef, open **Plants & corals → Place coral**, move the preview, then click the desired spot. Arrow keys move the preview; Enter places it. Escape or Cancel exits without spending credits.
- **Inspect coral:** click a colony or its **Inspect** button for **Overview** and **Care** tabs. View health, age, growth, value, light/flow requirements and water warnings. **Reposition** moves an existing colony; positions survive saving and reloading. Left/Right arrow keys switch information tabs.
- **Plants & corals:** transfer compatible organisms or sell healthy cuttings after sufficient growth. Freshwater plants use a position slider and remain rooted at the bottom.
- **Breeding:** view readiness conditions and start courtship. Broods need suitable water; fry need fine food.
- **Social fish transfers:** move the entire resident school together, explicitly indicated before transfer.
- **Notifications:** the header event-history button opens the retained log.
- **Night market:** level 4+, 20:00–04:00 game time. Its creatures and confiscation rules are fictional.
- **VIP preview:** free lighting previews only. No payments, purchasable tiers or subscriptions exist.

Opening a dialog or placing coral pauses biological simulation. Hidden browser tabs do not accrue active simulation time. Day/night remains a lighting and behavior system, not a real-world calendar dependency.

## Saving and recovery

The game autosaves every 20 active seconds and after transactions. **Save** also saves immediately.

**Settings → Export JSON backup** downloads the full state. **Import JSON backup** validates a file and shows a replacement confirmation. Keep exported backups: browsers can isolate or restrict storage for local files, and moving the game or clearing browser data can change which save is accessible.

If storage fails, the game continues in memory and displays a warning. Export JSON to retain progress. A malformed, duplicate-identity, incompatible, or future-version save is not silently erased: autosave is locked and a recovery dialog offers raw-file download, the previous valid backup, or JSON import.

**Relaxed return** is the default: nothing deteriorates while closed. Optional **Survival** processes elapsed time in bounded five-minute simulation steps, up to the selected limit (maximum eight game hours), and reports losses and credit changes.

JSON files are portable saves, not tamper-proof accounts. This is an offline single-player game.

## What is in this build

52 fish catalog/rendering records (including two fictional creatures and five care-verification purchase holds); 25 designer phenotypes linked to base species; nine tank sizes; multiple tanks; fish identity, sex, aging, health, disease, stress, nutrition, genetics and lineage; schooling and other behavior states; water chemistry; equipment wear; seven foods; six plants; five coral groups; purchases and controlled resale; livebearing, egg incubation and mouthbrooding; 19 quests; achievements; local saving and recovery; seasonal lanterns and freely selectable offline events.

The consolidated [master specification](MASTER_DEVELOPMENT_PROMPT.md) retains the supplied v2.1 requirements and integrates the approved lighting and coral controls plus the mandatory art-review gate as revision 2.7. This playable release does **not** implement the full specification. In particular, tanks still include starter equipment and printed scenery; completely empty/dry construction, substrate biology and displacement, full corpse decay, separate coral bleaching/tissue states, and illustrated VIP tiers remain unfinished. See [DEVELOPMENT_STATUS.md](DEVELOPMENT_STATUS.md) for the phase audit. The procedural artwork has not received a comprehensive biological art review.

## Tests

Open **`tests/index.html`** for the browser-based simulation suite. It needs no extra software and does not modify the actual game save.

Optional developer browser automation uses Python 3 standard-library tools and an installed Chrome or Edge:

```text
python tests/browser_qa.py chrome
python tests/browser_qa.py chrome --clownfish
python tests/browser_qa.py edge
```

The harness uses dedicated test browser profiles. It exercises actual local-file loading, UI navigation, transactions, save/reload, export/import, corruption recovery, screenshots, responsiveness, and absence of HTTP requests. It writes results under `tests/`.

Read [TEST_REPORT.md](TEST_REPORT.md), [BALANCE_REPORT.md](BALANCE_REPORT.md), and [GAME_DESIGN.md](GAME_DESIGN.md) for evidence, assumptions and limitations.

## Source layout

```text
index.html            Local entry point
css/main.css          Responsive interface and components
css/theme.css         Locked near-black and slate-blue palette
js/data.js            Editable balance, species, items and quest definitions
js/core.js            State factories, compatibility, economy and atomic actions
js/simulation.js      Clock steps, water, equipment, health, AI, ecology and breeding
js/save.js            Validation, migration, persistence, recovery and JSON files
js/render.js          Procedural sprites, cached animation and Canvas renderer
js/ui.js              Navigation, accessible forms, management screens and dialogs
js/main.js            Fixed-step loop and application initialization
tests/                Repeatable simulation and browser tests
```
