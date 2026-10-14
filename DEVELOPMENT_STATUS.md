# Development status — 2026-10-14

## Ocean Diving v2.8 — current, 2026-10-14

MDP **v3.3**, retaining all 31 major sections. **Ocean Diving** beside Keeper Level opens Reef (Level 5 / 1,000 AC) or Deep Sea (Level 10 / 10,000 AC). Fiji, Caribbean, Hawaii and Japan have original regional scenery and a compact playable map. W/A/S/D, arrows and on-screen buttons move one tile; every successful step costs exactly 5% oxygen from 100%. Blocked movement and collection clicks cost none. Eight temporary slots become owned only on a successful boat return with oxygen remaining. Exhaustion/confirmed abandonment forfeits discoveries without a fee refund.

Aquariums continue at 1× during planning, diving and results, using the existing 20-real-minute game day. Explicit safe receivers, supported coral mounts, species-conditioned survival, finite transport holding, persistent provenance and Reputation 5 Black Market-only resale are integrated. Confirmed paid Black Market purchases earn bounded reputation; canceled/failed/duplicate transactions do not. Direct normal-store livestock is restricted to Tiers 1–3; eight daily Fish slots and independent Mystery Egg odds remain unchanged. Nominal tank/equipment capacities now ceil to whole US gallons; physical liters and precise water-change calculations remain exact.

**No new biological species.** The approved 38-entry v2.7 batch and all protected freshwater content remain the roster baseline. Six sourced encounter profiles reference existing IDs; Hawaii wildlife is observation-only, and unsupported regional/depth combinations offer inert fictional salvage rather than invented animals. All captures are fictional restricted game recovery, not real collection authorization. New art is unapproved pending user review. Saves and expedition receipts remain on each player's PC in browser storage. See [DIVING_UPDATE_REPORT.md](DIVING_UPDATE_REPORT.md) and [the region ledger](assets/diving/registry.json). DIST is rebuilt through `python build.py`. Earlier milestones below are historical where superseded.

Implemented offline exploration, exact unlocks/fees/oxygen, four regions, compact collision maps, eight-slot temporary inventory, finite transport, safety-checked survival, owned rock placement, Black Market reputation/resale, high-tier normal-store rejection, active-trip persistence, local completion receipts, protected dismissal and whole-gallon nominal labels. Nine original image assets are integrated (eight backgrounds and an eight-object equipment sheet); all remain unapproved. The v2.7 species/art limits are unchanged. PDF continuity source is updated; binary PDF export remains pending unavailable PDF toolchain.

## Livestock expansion v2.7 — roster baseline milestone, 2026-10-14

MDP **v3.2** retains exactly 31 major sections. Added **38 unique marine entries: 28 fish, five named stony corals and five non-fish invertebrates**. All 38 passed the pre-registration scientific-name/synonym duplicate audit; none were skipped. The runtime now has **80 fish (69 marine, 11 protected freshwater), ten marine coral entries and five non-fish invertebrates**. The six existing freshwater plants are unchanged. Existing art-only and planned entries are excluded from these totals.

All six Mystery Egg rarity pools are now populated; the earlier empty-pool content hold is superseded. Keep independent 50/25/15/7.5/2/0.5 percent odds, 600 AC, three daily eggs, existing level/incubation gates and safe-destination checks. Daily Fish shopping remains exactly eight visible slots: 3 Common, 3 Uncommon, 1 Rare, 1 Mystery Egg. Higher tiers do not add normal Fish cards. Fixed retail, persistent selected aquarium, continuous offline simulation, rarity/genetics and existing specialist clownfish holds remain.

New livestock has inspectors, rarity, care information, value, host-filtered health compatibility and additive save support. Corals use player-selected supported rock/rack placement. Invertebrates are separate bottom residents with feeding, crawling/filtering, condition, death and transfer records. Their egg/planktonic larval reproduction and art are unsupported. New fish natural breeding is enabled only for the five explicitly supported profiles; Mystery Egg development is a simplified game presentation, not evidence of complete captive culture.

There are 38 new transparent sprite sheets / 304 static stage-state views. All are unapproved; 12 sheets carry explicit framing review flags. Existing approved artwork is preserved. Review [the new artwork gallery](expansion-review.html). [Implementation report](LIVESTOCK_EXPANSION_REPORT.md), [permanent registry](assets/expansion-v27/registry.json), [continuity source](PROJECT_CONTINUITY_SOURCE.md) and [PDF workflow](PDF_WORKFLOW.md) record the limits. **PDF regeneration remains pending: PDF authoring/rendering prerequisites are unavailable in this environment.** Earlier milestone material is historical where superseded.

### v2.7 delivery status

Implemented: all 38 exact approved species, 0 duplicates; store, journal, inspector, health/value, placement, safe destinations, upper Mystery pools and additive persistence. Chrome and Edge each passed 362 expansion checks plus 7,583 artwork regression checks (7,945 total per browser, zero failures). This includes 1,792 directional cases per browser, 145 protected-file hashes and a ten-game-day freshwater replay comparison. Test evidence is in the expansion report.

Partial/disclosed: 12 art framing flags, provisional eye metadata, static stage poses, selected sex-reference art, unsupported invertebrate egg/planktonic larval art/reproduction and unsupported natural breeding for 23 new fish. The project continuity source is updated; binary PDF export remains pending unavailable authoring/rendering tools. Firefox, native fullscreen modes and superseded milestone-specific full suites were not rerun. Previous artwork approvals and five specialist clownfish purchase holds are preserved.

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


## Main UI overhaul — 2026-10-13 (latest delivery)

Delivered for user review: six permanent sidebar/modal windows; viewport-fitting 2:1 aquarium; centered dynamic total value and routed breakdown; reorganized ownership/setup, store Buy/Sell/Orders, journal collection/knowledge/progression/history, equipment/feeding/water change and preview-only VIP/settings. Player-created starting and purchased aquariums begin empty/dry; saved existing tanks are preserved. Equipment removal/reinstallation uses owned shared inventory. Marine eggs have saved spawning sites, developmental framing, hit selection, inspectors and nonviable-clutch handling; biology/art reuse preserves existing hatching and lineage. Consolidated MDP v2.9 retains all 31 major sections.

Evidence, acceptance mapping, screenshots and limitations: [UI_OVERHAUL_REPORT.md](UI_OVERHAUL_REPORT.md). The complete game remains unfinished; earlier audit items, full substrate biology/displacement, clinical and rare-species certification, exclusive VIP art/entitlements and online ranking are not claimed complete. No unrelated feature work begins after this review delivery. Older milestones below reflect their original dates.

## Marine economy, disease and valuation — 2026-10-13

Delivered for review: offline marine disease/diagnosis/quarantine/timed treatment, eight legitimate medicines, two fictional restricted medicines, fixed retail prices, saved marine dealer prices/conditions/quality, current livestock values, selected-tank total/base/breakdown/history and additive save compatibility. The consolidated specification is v2.8 with all 31 major sections preserved. No new livestock or online service was added. Existing approved art and freshwater definitions/art/biology are protected.

Chrome and Edge each pass 69 new acceptance checks, 68 existing system checks and 90 current store/UI checks. Clownfish art/direction/eye regression contains 7,583 passing checks and 1,792 directional cases per browser. New checks exercise actual quantity input, exam/start-course buttons, four responsive widths, legacy migration, corrupt hidden records, exact saved listing/batch quality, contraindications, recovery/failure/harm and protected freshwater biology. Evidence and remaining limits are in [ECONOMY_DISEASE_UPDATE_REPORT.md](ECONOMY_DISEASE_UPDATE_REPORT.md).

Still incomplete/deferred: species-level coral/rare-species clinical certification, more diagnoses/agents/laboratory assays, actual invertebrate livestock and host-specific treatment profiles, full decomposition/dry setup/substrate systems, online ranking, categorical designer breeding and the remaining October 12 audit work. The full game is not declared complete. Prior phase entries below describe their dates, not the current complete status.


**Delivered: v0.1 playable offline vertical slice.** The full long-term master specification is not declared complete.

The supplied master prompt v2.1 is now consolidated in MASTER_DEVELOPMENT_PROMPT.md. Revision 2.6 retains the earlier manual-lighting and coral placement/inspection requirements in sections 8, 13 and 23 and adds the mandatory art-review gate in section 3.8; no v2.1 requirements were removed. The approved clownfish reference is present and inspected. ART_DIRECTION.md and UI_SPECIFICATION.md now record the locked requirements and current limits.

## Current phase: clownfish collection and shared store delivered for review

The active consolidated MDP is revision 2.7. Added 30 marine clownfish records while preserving existing Ocellaris ID, yielding 52 fish plus five coral categories (57 catalog/rendering entries). Five specialist clownfish care profiles are purchase-held; 25 designer varieties stay linked to biological species. Packed all 56 collection sheets, full alive/dead life stages and adult swim cycles. Earlier approved Ocellaris and freshwater art remain preserved. The gallery includes global audit and care/taxonomy/source uncertainty.

Shared modal store now has three tabs, destination header/explicit eligible alternatives, safe atomic purchases, inventory delivery and saved destination invariants. Existing products/Black Market rules are retained. Marine coral attachments use visible rock tops, stable sandbed or mounted glass racks; support edits carry colonies and block stranding. Added saved marine rock/rack inventory and visual sand type/depth. Unsupported legacy corals keep ownership with relocation flags. No new substrate chemistry or freshwater biology was developed.

See [CLOWNFISH_STORE_REPORT.md](CLOWNFISH_STORE_REPORT.md), [clownfish-review.html](clownfish-review.html), [coral-placement-review.html](coral-placement-review.html) and [CURRENT_LIVESTOCK_CATALOG.md](CURRENT_LIVESTOCK_CATALOG.md). Current browser checks and numeric evidence are in TEST_REPORT.md. **New art remains provisional; stop for user visual review.** Broader future batches remain 25 marine fish / five corals / five marine bottom feeders only when authorized.

The historical phase audits below describe earlier releases; saltwater rock/sand/rack purchasing and mounting are now implemented as described above. Quantity-by-volume substrate economics, biological substrate maturation, displacement, complete dry setup, species-level coral profiles and full decomposition remain unfinished.

## Previous phase: livestock life-stage art update delivered for review

Audited 27 implemented livestock: 22 fish (including four benthic fish) plus five coral categories. Produced 216 static authored stage/state images in 27 transparent atlases. Every implemented entry now has Egg/Baby/Juvenile/Adult, each Alive/Dead, with metadata and individual PNG exports. Five earlier marine fish remain ART ONLY; no new species, chemistry, economy or progression were added.

The offline life-stage gallery is linked from index.html. Fish stage loading follows existing growth values; dead poses are authored and never double-inverted. Approved adult Ocellaris animation is preserved. Coral early forms are future art support, with existing colony biology and health-state art retained. All earlier art sources remain available.

Chrome and Edge each pass 214 life-stage checks and 2,160 directional rendering cases, plus 68 existing system and 69 UI checks. All new art awaits user review; static coverage does not imply complete animation or scientifically validated anatomy. See [LIFE_STAGE_ART_REPORT.md](LIFE_STAGE_ART_REPORT.md) and [CURRENT_LIVESTOCK_CATALOG.md](CURRENT_LIVESTOCK_CATALOG.md).

Permanent future content rule: complete eight-image stage/state chain per new livestock entry; expansion batches target 25 fish / 5 corals / 5 bottom feeders when requested. No new batch added now. **Stop here for user review. Next planned art task after review: clownfish-only refinement; not started.**

## Previous phase: Art Development Update v1.1 delivered for review

Completed shared head-local eye registration and canonical detail sampling, final-size raster caches, corrected odd-size mirroring, transform isolation, slow-motion facing and frozen death poses. All 22 existing fish and five new art-only subjects use the corrected rendering boundary. The approved clownfish source remains preserved.

Added five priority fish atlases, including the user-confirmed Emperor angelfish and Red lionfish. Added five coral state atlases and three rock collections with four variants each. Existing coral and marine hardscape/cave rendering use the new artwork; absent gameplay fish were not added to stores or care definitions. No unrelated simulation/economy/quest/breeding systems were expanded.

The offline gallery now separates Fish, Corals and Rocks, includes eye anchors and directional/frame comparisons, and persists rock preview arrangements separately from the game. See ART_UPDATE_REPORT.md, CURRENT_FISH_CATALOG.md, ART_DIRECTION.md and ART_GENERATION_RECORD.md. Automated checks: 68 system + 69 main UI + 221 art/sprite checks per browser, including 6,480 directional render cases in Chrome and Edge. Eye contact sheets and category screenshots were inspected. Schema 2 remains compatible.

New artwork is Ready for Review, not automatically Approved. Generated pose consistency, precise species anatomy, dedicated front-facing turns and additional animation states still require artist/user review. **Stop here for the user's visual approval before proceeding beyond this requested art update.**

## Previous phase: Ocellaris artwork assignment completed

The latest instruction supersedes habitat work as the next action. Stages 1?4 are implemented: a 22-species code audit, approved-reference analysis, one transparent clownfish benchmark, and an offline art-review gallery linked from the game footer. Current/proposed sprites compare at equal visible width, with native-size studies at 96/128/192/256 pixels, actual game-scale preview, a four-frame swim study, pause/step controls, turning endpoints and a static death-pose concept. The user subsequently requested the artwork for Ocellaris; it is now assigned to gameplay ID clown.

See CURRENT_FISH_CATALOG.md and ART_DIRECTION.md. All existing Ocellaris residents now use the generated four-frame atlas in the tank, store and inspector. Other species retain their previous sprites. No economy, biology, store, breeding, quest or save-schema changes were made. Gallery review preferences use a separate key and never install artwork into gameplay. Original generated source, packed candidates and the exact prompt are retained.

The proposal still needs frame consistency and anatomy/outline refinement; no true turn transition or dedicated death/decomposition artwork is complete. Other priority fish and corals have not been drawn. **This user request authorizes assignment to Ocellaris. Wait for further direction before expanding to other species or gameplay phases.** This is required by the user's Art Direction Review & Approval brief, sections 13 and 15.

The consolidated master is now revision 2.6, with the current gate integrated into section 3.8. Art-gallery verification is recorded in ART_REVIEW_REPORT.md and browser-specific art-result JSON files.

## Previous completed phase: coral interaction and interface alignment

Implemented direct coral purchase placement, preview/cancel, free repositioning, camera-aware pointer input, keyboard editing, selection in the aquarium, individual Overview/Care tabs, and shared simulation condition reports. Per-tank lighting controls and visible illumination are preserved. The interface now uses the exact locked near-black/slate-blue palette. Existing saves remain schema 2; older colonies default to the tank bed when their optional vertical coordinate is absent.

## Consolidated specification audit and dependencies

| Target phase | Existing foundation | Remaining before the phase can be called complete |
|---|---|---|
| 1: Foundation | Offline startup, fixed steps, validated saves | Broader legacy migration corpus and storage-failure QA |
| 2: UI | Functional navigation, inspectors, locked palette | Comprehensive inventory, UI scaling, accessibility audit, habitat screens |
| 3: Tank setup | Prepared water, equipment, accelerated cycling | Completely empty/dry tanks, player-installed equipment, explicit water filling, setup visual states, readiness history |
| 4: Saltwater habitat | Coral placement and decorative cover | Fiji/Caribbean/Hawaiian sand and rock catalogs, quantity inventory, dimensions, 0–5 in depth, displaced water volume, rock editing, substrate biology and inspector |
| 5: Fish | 20 real species plus fictional species, identity, health, AI | Marine-priority species expansion including missing priority species, biological/art audit, rock collision, finite mass decay and permanent death history |
| 6: Coral | Five categories, growth, health, conditions, placement, inspector | Specific husbandry profiles, independent bleaching/recovery, tissue loss, differentiated dead remains, waste and conditional skeleton dissolution |
| 7: Economy | Validated transactions, stock/budgets/demand, fictional market | Habitat inventory pricing, sale cooldowns, specialty buyers, broader black-market catalog/reputation |
| 8: Breeding | Eligibility, genetics, clutches, incubation, fry | More species-specific reproductive/habitat rules and genetics/lineage presentation |
| 9: Progression | 19 connected quests and three achievements | Habitat/coral-state objectives, expanded unlocks and prestige |
| 10: VIP/events | No payments, free light previews, seasonal foundation | Locally illustrated VIP tier panels, event quests and lasting cosmetic rewards |
| 11: Polish | Cached pixels, frame fallback, offline QA | Full reference-quality artwork, graphics presets, audio hooks, maximum-load and Firefox QA |

After the art-review gate is explicitly released, the next gameplay implementation dependency is tank dimensions and versioned dry-tank setup, followed by owned substrate/rock inventories and effective water volume. Preserve existing tanks as established habitats during migration. That shared habitat/water foundation is needed before adding substrate chemistry, rock-aware AI and more detailed decomposition.

## Integrated phases

| Phase | Working implementation |
|---|---|
| Foundation | Local `index.html`, classic scripts, explicit state factories, fixed simulation steps, pause/speeds, responsive HTML/CSS interface |
| Aquarium simulation | Nine sizes, multiple freshwater/marine tanks, preparation, accelerated fishless cycling, nitrogen conversion, oxygen, temperature, replacement-water mixing, equipment wear/service |
| Fish | 20 real species plus two fictional species; individual state, animated procedural sprites, compatibility, physical-space restrictions, schooling, deterministic motion, stress, health, age and deaths |
| Ecosystems | Accepted diets, fine fry food, food decomposition, six plants, five reef coral categories, nutrient/light/flow/mineral interactions, territorial attacks and predation |
| Economy | Atomic validated purchases, finite stock, one wallet, load reservations for broods, budget/demand/sale caps, cutting sales, recurring showcase, energy expenses |
| Breeding | Player-triggered readiness, complementary-sex pairs, eggs, gestation, male mouthbrooding, suitable-condition incubation, bounded inherited genes, offspring identity and lineage |
| Progression | 19 functional journal entries with prerequisites and single-claim rewards, level locks, collection discovery, three checked achievements |
| Presentation | Aquarium-centered interface, zoom/pan/inspection, layered pixel scenery, fish/plant animation, notifications, complete navigation, route selection and guided setup |
| VIP | Explicitly unavailable tier concepts; three freely previewable lighting treatments; zero currency and no payment functions |
| Persistence | Autosave, manual save, validated JSON export/import, prior-save recovery, corruption protection, narrow schema migration, relaxed/survival return modes |
| Seasonal foundation | Offline event selector, persistent themed lantern purchase, associated objective |

## Tested

See TEST_REPORT.md and machine-readable browser reports for final counts and versions. The tests include actual offline `file://` operation, new-game choices, all navigation/store categories, transactions, welfare, chemistry, breeding, long simulations, deterministic state, market bounds, save/reload, real export/import, corrupt-primary recovery and responsive widths.

Both Chrome and Edge have been run. Firefox is not installed here and remains unverified. Screen-reader behavior and sustained maximum-size collections have not received comprehensive testing.

## Known limits and intentionally unfinished expansion

- Numerical biology is provisional game data. Cycling, breeding and brood sizes are compressed. No comprehensive scientific art or husbandry review is claimed.
- Specialized betta reproduction is unavailable and explained in breeding readiness. This build permits only one betta per aquarium.
- The infection system is a generic stress-related illness, not a catalog of contagious diseases or medications.
- Quarantine, breeding and incubation tanks are independent simulated tanks; detailed quarantine protocols, fry-specific equipment and infectious transmission are not implemented.
- Fish movement includes schooling, resting, seeking food, shelter, exploration and encounter states. Territory memory, obstacle-aware path planning, pair-bond persistence and offspring guarding are future work.
- Genetics implements five bounded traits. Pattern alleles, fin-shape inheritance, dominance and pedigree visualizations are future work. Fertility does not impose a separate stochastic spawning-failure roll.
- Food has actual diet/quality/pollution effects but no freshness/spoilage inventory model, explicit fat metabolism, coral feeding or live-food culture.
- Core equipment covers filters, heater, chiller, aeration, skimmer, lighting, feeder, circulation, reef dosing and fictional containment. Standalone RO systems, finite test-kit usage and sensor products are not modeled.
- Hardness and reef minerals are simplified; no complete acid/base equilibrium, realistic marine ion balance or chlorine toxicity model exists.
- Seasonal content currently consists of selectable offline event state, lanterns and an actual objective. Full event quest chains, seasonal fish and annual scheduling are future work.
- VIP tiers are labeled concepts, not active rewards. Paid access remains disabled by design.
- No audio, visitor business, exhibition competitions, contracts, specialist rare-fish buyers, online trading or 100+ species expansion.
- Corals use click-to-place previews and direct two-dimensional repositioning; freshwater plants use a position slider. There is no drag-and-drop decoration editor. Decorative hardscape can be added but not yet rearranged/transferred; coral anchors are bounded, but physical rock attachment and collision are unfinished.
- The printed vegetation and starter hardscape are visual scenery; they do not count as owned plants or breeding cover.
- Desktop and narrow layouts were checked for horizontal overflow. Large-colony/maximum-ownership performance, extended touch play and Firefox require additional QA.

## Defects resolved during development

- Added a visible per-tank Auto/On/Off light control and save-compatible manual overrides. Lamp output now changes the brightness of fish, plants and hardscape, with surface glow and underwater rays. Intensity, failed equipment and night-time manual lighting are reflected in the view.

- Purchase confirmation tokens originally risked collision after reload; tokens now include a per-session namespace.
- Resting bottom dwellers could choose a target beyond the aquarium; targets are clamped.
- The feeding objective now requires consumption, rather than counting an unsuitable feeding attempt.
- Brood reservations now contribute to future adult capacity before further purchases.
- Schooling transfers move the full resident group, with a clear confirmation description.
- Rendering no longer consumes simulation randomness or moves authoritative fish positions; motion advances only in fixed steps.
- All transactions now validate the resulting full state, preventing invalid environmental inputs from poisoning saves.
- Per-pixel scenery polygon drawing was replaced with scanline spans, palette caching and cached plant animation; measured draw cost dropped substantially.

## Gameplay priorities deferred during art review

1. Empty/dry tank construction with safe migration and visible water/setup states.
2. Owned saltwater sand/rock, dimensional quantity/depth/displacement calculations, placement and substrate biology.
3. Persistent finite corpse mass and differentiated coral bleaching/tissue/death states through the shared water model.
4. Marine species/art review, geometry-aware AI and species-specific breeding.
5. Illustrated VIP previews, broader economy/events, graphics presets, Firefox/accessibility and maximum-capacity QA.

## Architecture and balance decisions

No runtime dependency or build step is introduced. Source remains small enough to inspect directly and is split by state/actions, simulation, persistence, art, UI and data. User actions commit validated drafts. Maximum entities, particles, history and plant caches are bounded. See GAME_DESIGN.md for formulas and BALANCE_REPORT.md for measured outcomes.
