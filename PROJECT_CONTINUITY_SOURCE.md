# Aquarium Life — printable continuity source

## Protected production distribution - 2026-10-22

Current master v4.17; gameplay remains v4.3.1 with a new protected distribution pipeline. Production now minifies JS/CSS, shortens internal identifiers, uses content-derived code filenames and excludes review pages, source maps, project documentation and tooling. Human-readable game code and original assets remain untouched. Assets retain their original pixels and offline file transports; no encryption, passwords, licensing dependency, profile rewrite or save-key change is introduced. Runtime safety and the mandatory performance pass take priority over obfuscation. DISTRIBUTION_PROTECTION_REPORT.md records exact mechanisms, commands, executed tests, benchmarks and limits. The exact complete31-section master is embedded below. Earlier build descriptions are historical where superseded.

## Permanent post-update optimization workflow — 2026-10-22

Current authority: master v4.16; playable game remains v4.3.1. Every subsequent development prompt automatically requires Implement → Profile → Re-optimize → Validate → Report before completion. The canonical rule is master section25.5; section31.3 requires a Performance & Optimization section and gates the exact completion message on genuinely completed feature work, optimization and validation. Preserve capped 60 FPS default, optional 30 FPS, independent biology, original pixel quality, offline operation and existing saves; report unavailable measurements honestly. The root AGENTS.md directs future sessions to these requirements. This documentation update changes no runtime, assets, saves or gameplay. The exact complete31-section master is embedded below; earlier release notes are historical where superseded.

## UI polish and store quantities — 2026-10-22

Playable v4.3.1 / master v4.15. The familiar aquarium layout now uses a very subtle static downward fish-scale background, opaque slate-blue panels and consistent controls. The existing guarded store supports quantities for equipment, food, consumables, ordinary medicines, rated parts and rocks. Multiple rocks enter Inventory for separate placement; sensitive livestock, unique tools and installations retain their established individual safeguards. One total charge, distinct physical IDs, capacity/stock checks, persistent receipt replay protection and local saving remain authoritative. Main schema2/tutorial2, biological simulation, economy rates, offline time and freshwater lock are unchanged. STORE_QUANTITY_RULES.md defines category behavior; UI_POLISH_QUANTITY_REPORT.md records files, actual tests and limitations. The exact complete31-section master is embedded below. Earlier release sections are historical where superseded.

## Performance optimization — 2026-10-22

Playable v4.3.0 / master v4.14. One capped60/30FPS scheduler, independent fixed biological steps, on-demand lossless native sources, bounded caches, cached scenery, covered/hidden render suspension, changed-value HUD updates and five graphics preferences. Main schema2/tutorial2, all player assets, protected art, local saves, freshwater lock and biological/economic formulas remain intact. PERFORMANCE_SYSTEM.md and PERFORMANCE_SETTINGS_SAVE_SCHEMA.md describe runtime/persistence; AQUARIUM_LIFE_PERFORMANCE_OPTIMIZATION_REPORT.md records actual measurements and executed regressions. Exact complete31-section master remains embedded below. Earlier art/PDF limitations remain separate.

## Interactive tutorial loop repair - 2026-10-21

Playable v4.2.1 / master v4.13. The full route audit found a canvas hidden behind the empty-tank panel, pre-dispatch reads of trusted events, and stale form targets in closed dialogs. The initial setup button now supports actual navigation, event observations wait for completed handlers, and details queries require an open dialog. Schema2/tutorial2, physical ownership, biology, economy, local saves and freshwater lock remain unchanged. TUTORIAL_FULL_AUDIT_AND_REPAIR_REPORT.md is the current handoff and executed-test record; earlier tutorial evidence is historical. The exact complete31-section master is embedded below. Earlier art/PDF limitations remain separate.


## Interface simplification - 2026-10-20

User requested starting the reviewed cleanup. Master v4.11 / playable v4.1.1 now uses six useful destinations, grouped Progress and unified Tank Care. Previews leave the player interface; diagnostics and simulation remain intact. See SIMPLIFICATION_REPORT.md. Exact complete master remains embedded below.

## Coordinated economy update — 2026-10-20

Implemented the seven authorized changes in master 4.6,6.6,11.8,17.9,18.12–18.13,20.4 and24.14. Complete exact master v4.10 below retains all 31 major sections. Read ECONOMY_UPDATE_REPORT.md for files, current test evidence, approved payouts/rewards/parts and sale restrictions. Freshwater remains locked, saves local, existing IDs/conditions/genetics/history protected. Full binary PDF export and unrelated missing artwork remain separate earlier limitations.

## Equipment durability and reliability — 2026-10-19

Implemented master 11.7 with preserved physical Inventory ownership, additive tracking, separate maintenance/condition/faults, multi-year hazards, actual operating output and chronological offline parity. See EQUIPMENT_DURABILITY_BALANCE_REPORT.md for exact formulas, 2,048-seed distributions per type, measured real-time lifespan, executed tests and limits; EQUIPMENT_MAINTENANCE.md and EQUIPMENT_RELIABILITY_SAVE_SCHEMA.md define care and persistence. The complete exact master v4.9 below retains all 31 major sections. All saves remain local; freshwater locked. Earlier binary PDF and unrelated artwork limits remain separate and are not claimed complete.

## Equipment inventory and interface update — 2026-10-19

Implemented the physical storage/location rules in master sections 11.6, 18.11 and 24.12, plus the navigation cleanup in 26.3–26.8. See EQUIPMENT_INVENTORY_UPDATE_REPORT.md for changed files, migration, actual browser evidence and release verification. The complete master v4.8 below retains all 31 major sections. Earlier sprite-production limitations remain accurately recorded and are unrelated to this equipment update.

## Full livestock sprite production — current work

The verified production checkpoint contains382 native sixteen-frame sheets (6112 actual authored cells), covering110 of113 usable marine entries: all89 fish, all15 corals and6 of9 invertebrates. Batches1–11 are complete. The remaining18 sheets belong to Fire Shrimp (Lysmata debelius), Randall's pistol shrimp (Alpheus randalli) and Harlequin Shrimp (Hymenocera picta). Built-in image generation returned HTTP429 daily usage_limit_reached; four Fire Shrimp source candidates were rejected for alpha noise and webbed appendages, and14 sources were not generated. No rejected candidate enters gameplay. The reported reset is2026-10-20 at09:37AM America/New_York. Original approved art remains active for these three species. All119 biological records, six acquisition holds, freshwater lock, local saves, biology and economy are preserved. Full production is NOT complete. Exact per-entry paths, missing work and current Chrome/Edge evidence are in [LIVESTOCK_16_FRAME_SPRITE_PRODUCTION_REPORT.md](LIVESTOCK_16_FRAME_SPRITE_PRODUCTION_REPORT.md). Player visual approval is separate.

## Global marine fish animation audit — playable v4.0.3, 2026-10-16

Audited all 94 registered marine fish, including five acquisition-held clownfish and one fictional fish. Thirty-one have authored adult cycles; 63 previously translated static living poses. Added render-only species profiles, pixel-preserving tail/outer-fin motion, state-aware timing, banked side-profile turns and head/eye protection across three stages. No new biological species, AI/feeding/breeding rules, inheritance or saves are introduced. All 94 remain conservatively classed B (partial) because bespoke action/turn/pectoral artwork and anatomy approvals remain incomplete; this is not a claim of fully authored animation. See [FISH_ANIMATION_AUDIT.md](FISH_ANIMATION_AUDIT.md), [FISH_ANIMATION_SYSTEM.md](FISH_ANIMATION_SYSTEM.md) and [offline motion review](fish-animation-review.html).

## Ocean diving destination artwork — playable v4.0.2, 2026-10-16

Eight original pixel-art PNG environments replace the simplified expansion scenery for Indonesia, Philippines, Sri Lanka, Marshall Islands, Maldives, Australia, Florida and Mariana Trench. A central per-mode art mapping drives selection previews, proportional in-dive backgrounds and expedition-result accents. Older regional PNGs, native encounter pools, all diving gameplay, local saves and freshwater lock are preserved. See [DIVING_LOCATION_ART_REPORT.md](DIVING_LOCATION_ART_REPORT.md). Art is implemented for review; no prior livestock/art approval is changed.

## Global diving expansion and liquidation — playable v4.0, 2026-10-16

Implemented the authorized Emergency Diving Sales & Rock Resale and Global Ocean Diving Expansion request (specification v3.6). Seven new reef selections and Mariana remote exploration use the central registry. Catch development, medical assessment, concealed attached eggs and regular-store liquidation extend the existing receiving authority. See [DIVING_EXPANSION_REPORT.md](DIVING_EXPANSION_REPORT.md) and [DIVING_EXPANSION_SAVE_SCHEMA.md](DIVING_EXPANSION_SAVE_SCHEMA.md). Earlier milestone reports remain historical where superseded. All saves stay local; freshwater remains locked; one game day remains 20 real minutes.

Playable v4.0.4 / MDP v4.7, 2026-10-16. Binary PDF regeneration pending.

## Mystery fish diving — v3.9 current, 2026-10-15

Implemented the authorized Mystery Fish update (request v3.5) on top of playable v3.8. New valid Reef/Deep trips guarantee a reachable regional fish, concealed until boat return, with saved assignments, original question-mark art/reveal, explicit safe receiving and permanent transport-loss evidence. Empty/closed collectible pools block launch. Existing oxygen, fees, resale, local accounts, biology, genetics, breeding, care rewards and freshwater lock remain. See [MYSTERY_DIVING_RULES.md](MYSTERY_DIVING_RULES.md) and [MYSTERY_DIVING_UPDATE_REPORT.md](MYSTERY_DIVING_UPDATE_REPORT.md). Current master is v4.2; earlier release entries are historical where superseded.

## Automatic marine breeding — v3.8 current, 2026-10-15

Replaced manual marine courtship with autonomous, species-aware breeding, visible swimming/nest behavior, individual reproductive status and a read-only Breeding & Eggs observation dashboard. New clutches use real parent/tank IDs, saved reproductive roles and RNG, species-specific care/losses and bounded offspring reservations. All prior local accounts, art/genetic identities, coral lineage, rewards, heaters, mortality logs, store/casino functionality and the 20-minute day remain. Freshwater stays locked. See [BREEDING_RULES.md](BREEDING_RULES.md), [BREEDING_SAVE_SCHEMA.md](BREEDING_SAVE_SCHEMA.md) and [BREEDING_UPDATE_REPORT.md](BREEDING_UPDATE_REPORT.md). Earlier release entries are historical wherever superseded.

## Equipment filters, inspector research and The Dock Casino - v3.7 current

Implemented the equipment-category dropdown and original fragging-tool previews, moved paid species research to living owned-fish inspectors, and added the authorized seventh sidebar entry The Dock Casino with playable Gold Fish and Predator & Prey. All wagers and returns use the existing account wallet/ledger and saved round authority; all research remains 5 AC once per canonical species. The aquarium header controls share the information-column grid and align to its actual panel edge. See STORE_CASINO_UPDATE_REPORT.md and CASINO_RULES.md for the release, verified probabilities, local persistence and limitations. Existing biological simulation, 20-minute day, rewards, freshwater lock, livestock/art approvals and local saves remain. Earlier release sections are historical where superseded.

## v3.3 current release - 2026-10-14

Implemented the authorized v3.1 coral fragging/trading, v3.2 financial dashboard and v3.3 Marine Research Center. Equipment has three reusable coral tools and two mounting consumables; eligible parents produce independently simulated, mounted clones with tissue loss, recovery and lineage. Diving livestock can use regular or Deep Market dealers; regular pays floor(0.60 x the same Deep reference), and Deep requires Reputation 5 plus an active wanted request. Wanted Livestock remains separate from exactly four rotating dealer stock slots.

The AC button opens a reconciled, persisted financial history. Existing wallets migrate unchanged; new profiles start at the requested 5,000 AC. Saltwater Research and the existing Encyclopedia share permanent 5-AC canonical-species unlocks. All 94 marine fish are indexed; 93 real species are researchable, one fictional entry is preview-only. Fully verified dossiers: 0; incomplete: 93; five have reviewed biological annotations. Partial content is disclosed before purchase. See [V33_UPDATE_REPORT.md](V33_UPDATE_REPORT.md), [FINANCIAL_TRANSACTIONS.md](FINANCIAL_TRANSACTIONS.md) and [RESEARCH_SOURCES.md](RESEARCH_SOURCES.md).

Saltwater-only scope, safe persistent store destinations, local PC/browser saves, existing rewards/odds, all old livestock and artwork approvals/holds remain. No new biological species or art assets were added. Full printable continuity source is updated; binary PDF regeneration remains pending. Current playable version v3.3 / consolidated MDP v3.6.

## Earlier milestone record - historical where superseded

**Authorized 2026-10-14:** The user approved the complete 25/5/5 roster and rarities, confirmed saltwater-only, and explicitly requested "Implement v2.9". Roster approval and artwork approval are separate; new artwork remains unapproved. [Authorization](planning/v2.9/approval.json).

Implemented the twelve-step saved/skippable saltwater tutorial with medical guidance, three-second selection outlines, disabled freshwater UI, separate +50 healthy / +100 survival rewards with persistent death/recovery tracking, Deep Market display rename, local asset-value leaderboard preview, exact 15,000-US-gallon / 5,000-AC aquarium, proportional water-change salt consumption, independent mystery products and the approved 35-species marine batch. Saves remain local to each player's browser on their PC. The bottom mystery product is content-held because its Legendary host specialist is not eligible. See [V29_UPDATE_REPORT.md](V29_UPDATE_REPORT.md) for actual checks, care/art limits and release details. Earlier milestone sections below are historical wherever superseded.

## Permanent v2.7 roster baseline — all 38 entries

| Name / scientific name / ID | Category / rarity / care | Status / batch / date | Art / alive-dead support / notes |
|---|---|---|---|
| Chalk Bass / *Serranus tortugarum* / `chalk-bass` | fish / Common / Moderate | IMPLEMENTED; PARTIAL art / v2.7 / 2026-10-14 | PARTIAL: source framing needs review; not user approved; Eight static stage/state views, including living and deceased; Simplified researched captive spawning. [Atlas](assets/expansion-v27/chalk-bass/atlas-v1.png) |
| Lantern Bass / *Serranus baldwini* / `lantern-bass` | fish / Uncommon / Moderate | IMPLEMENTED; art pending visual approval / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; Mystery Egg developmental presentation uses calibrated game incubation. [Atlas](assets/expansion-v27/lantern-bass/atlas-v1.png) |
| Yellow Assessor / *Assessor flavissimus* / `yellow-assessor` | fish / Uncommon / Moderate | IMPLEMENTED; PARTIAL art / v2.7 / 2026-10-14 | PARTIAL: source framing needs review; not user approved; Eight static stage/state views, including living and deceased; Simplified researched captive spawning. [Atlas](assets/expansion-v27/yellow-assessor/atlas-v1.png) |
| Blue Assessor / *Assessor macneilli* / `blue-assessor` | fish / Rare / Moderate | IMPLEMENTED; art pending visual approval / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; Eight static stage/state views, including living and deceased; Simplified researched captive spawning. [Atlas](assets/expansion-v27/blue-assessor/atlas-v1.png) |
| Candy Basslet / *Liopropoma carmabi* / `candy-basslet` | fish / Ultra Rare / Difficult | IMPLEMENTED; art pending visual approval / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; Mystery Egg developmental presentation uses calibrated game incubation. [Atlas](assets/expansion-v27/candy-basslet/atlas-v1.png) |
| Pink-Streaked Wrasse / *Pseudocheilinops ataenia* / `pink-streaked-wrasse` | fish / Rare / Moderate | IMPLEMENTED; art pending visual approval / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; Mystery Egg developmental presentation uses calibrated game incubation. [Atlas](assets/expansion-v27/pink-streaked-wrasse/atlas-v1.png) |
| White-Banded Possum Wrasse / *Wetmorella albofasciata* / `white-banded-possum-wrasse` | fish / Rare / Difficult | IMPLEMENTED; art pending visual approval / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; Mystery Egg developmental presentation uses calibrated game incubation. [Atlas](assets/expansion-v27/white-banded-possum-wrasse/atlas-v1.png) |
| Tanaka's Pygmy Wrasse / *Wetmorella tanakai* / `tanakas-pygmy-wrasse` | fish / Very Rare / Difficult | IMPLEMENTED; art pending visual approval / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; Mystery Egg developmental presentation uses calibrated game incubation. [Atlas](assets/expansion-v27/tanakas-pygmy-wrasse/atlas-v1.png) |
| Carpenter's Flasher Wrasse / *Paracheilinus carpenteri* / `carpenters-flasher-wrasse` | fish / Uncommon / Moderate | IMPLEMENTED; art pending visual approval / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; Mystery Egg developmental presentation uses calibrated game incubation. [Atlas](assets/expansion-v27/carpenters-flasher-wrasse/atlas-v1.png) |
| McCosker's Flasher Wrasse / *Paracheilinus mccoskeri* / `mccoskers-flasher-wrasse` | fish / Rare / Moderate | IMPLEMENTED; art pending visual approval / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; Mystery Egg developmental presentation uses calibrated game incubation. [Atlas](assets/expansion-v27/mccoskers-flasher-wrasse/atlas-v1.png) |
| Exquisite Fairy Wrasse / *Cirrhilabrus exquisitus* / `exquisite-fairy-wrasse` | fish / Uncommon / Moderate | IMPLEMENTED; PARTIAL art / v2.7 / 2026-10-14 | PARTIAL: source framing needs review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; Mystery Egg developmental presentation uses calibrated game incubation. [Atlas](assets/expansion-v27/exquisite-fairy-wrasse/atlas-v1.png) |
| Lubbock's Fairy Wrasse / *Cirrhilabrus lubbocki* / `lubbocks-fairy-wrasse` | fish / Uncommon / Moderate | IMPLEMENTED; PARTIAL art / v2.7 / 2026-10-14 | PARTIAL: source framing needs review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; Mystery Egg developmental presentation uses calibrated game incubation. [Atlas](assets/expansion-v27/lubbocks-fairy-wrasse/atlas-v1.png) |
| Ruby Longfin Fairy Wrasse / *Cirrhilabrus rubriventralis* / `ruby-longfin-fairy-wrasse` | fish / Rare / Moderate | IMPLEMENTED; art pending visual approval / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; Mystery Egg developmental presentation uses calibrated game incubation. [Atlas](assets/expansion-v27/ruby-longfin-fairy-wrasse/atlas-v1.png) |
| Greenbanded Goby / *Tigrigobius multifasciatus* / `greenbanded-goby` | fish / Uncommon / Moderate | IMPLEMENTED; PARTIAL art / v2.7 / 2026-10-14 | PARTIAL: source framing needs review; not user approved; Eight static stage/state views, including living and deceased; Simplified researched captive spawning. [Atlas](assets/expansion-v27/greenbanded-goby/atlas-v1.png) |
| Sharknose Goby / *Elacatinus evelynae* / `sharknose-goby` | fish / Uncommon / Moderate | IMPLEMENTED; art pending visual approval / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; Eight static stage/state views, including living and deceased; Simplified researched captive spawning. [Atlas](assets/expansion-v27/sharknose-goby/atlas-v1.png) |
| Orange-Spotted Prawn Goby / *Amblyeleotris guttata* / `orange-spotted-prawn-goby` | fish / Uncommon / Moderate | IMPLEMENTED; art pending visual approval / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; Mystery Egg developmental presentation uses calibrated game incubation. [Atlas](assets/expansion-v27/orange-spotted-prawn-goby/atlas-v1.png) |
| Randall's Prawn Goby / *Amblyeleotris randalli* / `randalls-prawn-goby` | fish / Rare / Moderate | IMPLEMENTED; PARTIAL art / v2.7 / 2026-10-14 | PARTIAL: source framing needs review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; Mystery Egg developmental presentation uses calibrated game incubation. [Atlas](assets/expansion-v27/randalls-prawn-goby/atlas-v1.png) |
| Hi-Fin Red-Banded Goby / *Stonogobiops nematodes* / `hi-fin-red-banded-goby` | fish / Rare / Moderate | IMPLEMENTED; PARTIAL art / v2.7 / 2026-10-14 | PARTIAL: source framing needs review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; Mystery Egg developmental presentation uses calibrated game incubation. [Atlas](assets/expansion-v27/hi-fin-red-banded-goby/atlas-v1.png) |
| Blue-Striped Trimma Goby / *Trimma striatum* / `blue-striped-trimma-goby` | fish / Rare / Difficult | IMPLEMENTED; art pending visual approval / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; Mystery Egg developmental presentation uses calibrated game incubation. [Atlas](assets/expansion-v27/blue-striped-trimma-goby/atlas-v1.png) |
| Redspotted Blenny / *Blenniella chrysospilos* / `redspotted-blenny` | fish / Uncommon / Moderate | IMPLEMENTED; PARTIAL art / v2.7 / 2026-10-14 | PARTIAL: source framing needs review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; Mystery Egg developmental presentation uses calibrated game incubation. [Atlas](assets/expansion-v27/redspotted-blenny/atlas-v1.png) |
| Starry Blenny / *Salarias ramosus* / `starry-blenny` | fish / Uncommon / Moderate | IMPLEMENTED; art pending visual approval / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; Mystery Egg developmental presentation uses calibrated game incubation. [Atlas](assets/expansion-v27/starry-blenny/atlas-v1.png) |
| Two-Spot Blenny / *Ecsenius bimaculatus* / `two-spot-blenny` | fish / Uncommon / Moderate | IMPLEMENTED; art pending visual approval / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; Mystery Egg developmental presentation uses calibrated game incubation. [Atlas](assets/expansion-v27/two-spot-blenny/atlas-v1.png) |
| Yellow Candy Hogfish / *Bodianus bimaculatus* / `yellow-candy-hogfish` | fish / Rare / Difficult | IMPLEMENTED; PARTIAL art / v2.7 / 2026-10-14 | PARTIAL: source framing needs review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; Mystery Egg developmental presentation uses calibrated game incubation. [Atlas](assets/expansion-v27/yellow-candy-hogfish/atlas-v1.png) |
| Blotched Anthias / *Odontanthias borbonius* / `blotched-anthias` | fish / Very Rare / Difficult | IMPLEMENTED; art pending visual approval / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; Mystery Egg developmental presentation uses calibrated game incubation. [Atlas](assets/expansion-v27/blotched-anthias/atlas-v1.png) |
| Purple Queen Anthias / *Pseudanthias tuka* / `purple-queen-anthias` | fish / Very Rare / Expert | IMPLEMENTED; art pending visual approval / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; Mystery Egg developmental presentation uses calibrated game incubation. [Atlas](assets/expansion-v27/purple-queen-anthias/atlas-v1.png) |
| Copperband Butterflyfish / *Chelmon rostratus* / `copperband-butterflyfish` | fish / Legendary / Expert | IMPLEMENTED; art pending visual approval / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; specialist species. Mystery Egg uses a calibrated pelagic-egg developmental presentation.. [Atlas](assets/expansion-v27/copperband-butterflyfish/atlas-v1.png) |
| Orange-Spotted Filefish / *Oxymonacanthus longirostris* / `orange-spotted-filefish` | fish / Very Rare / Expert | IMPLEMENTED; PARTIAL art / v2.7 / 2026-10-14 | PARTIAL: source framing needs review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; Mystery Egg developmental presentation uses calibrated game incubation. [Atlas](assets/expansion-v27/orange-spotted-filefish/atlas-v1.png) |
| Spotted Boxfish / *Ostracion meleagris* / `spotted-boxfish` | fish / Ultra Rare / Expert | IMPLEMENTED; art pending visual approval / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; Eight static stage/state views, including living and deceased; Natural breeding unavailable; Mystery Egg developmental presentation uses calibrated game incubation. [Atlas](assets/expansion-v27/spotted-boxfish/atlas-v1.png) |
| Pineapple Coral / *Blastomussa wellsi* / `blastomussa-wellsi` | coral / Uncommon / Moderate | IMPLEMENTED; art pending visual approval / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; Eight static stage/state views, including living and deceased; Existing fragmentation system; sexual reproduction not modeled. [Atlas](assets/expansion-v27/blastomussa-wellsi/atlas-v1.png) |
| Acan Lord Coral / *Micromussa lordhowensis* / `micromussa-lordhowensis` | coral / Rare / Moderate | IMPLEMENTED; art pending visual approval / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; Eight static stage/state views, including living and deceased; Existing fragmentation system; sexual reproduction not modeled. [Atlas](assets/expansion-v27/micromussa-lordhowensis/atlas-v1.png) |
| Cyphastrea Coral / *Cyphastrea serailia* / `cyphastrea-serailia` | coral / Rare / Moderate | IMPLEMENTED; art pending visual approval / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; Eight static stage/state views, including living and deceased; Existing fragmentation system; sexual reproduction not modeled. [Atlas](assets/expansion-v27/cyphastrea-serailia/atlas-v1.png) |
| Purple Leptastrea / *Leptastrea purpurea* / `leptastrea-purpurea` | coral / Rare / Moderate | IMPLEMENTED; PARTIAL art / v2.7 / 2026-10-14 | PARTIAL: source framing needs review; not user approved; Eight static stage/state views, including living and deceased; Existing fragmentation system; sexual reproduction not modeled. [Atlas](assets/expansion-v27/leptastrea-purpurea/atlas-v1.png) |
| Cactus Coral / *Pavona cactus* / `pavona-cactus` | coral / Rare / Difficult | IMPLEMENTED; art pending visual approval / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; Eight static stage/state views, including living and deceased; Existing fragmentation system; sexual reproduction not modeled. [Atlas](assets/expansion-v27/pavona-cactus/atlas-v1.png) |
| Sexy Anemone Shrimp / *Thor amboinensis* / `sexy-anemone-shrimp` | bottom_dweller / Uncommon / Moderate | IMPLEMENTED; PARTIAL art / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; egg/planktonic larval art unsupported; Eight static stage/state views; early settled juvenile through adult; Specialist larval rearing is not modeled; no automatic aquarium reproduction. [Atlas](assets/expansion-v27/sexy-anemone-shrimp/atlas-v1.png) |
| Porcelain Anemone Crab / *Neopetrolisthes maculatus* / `porcelain-anemone-crab` | bottom_dweller / Rare / Moderate | IMPLEMENTED; PARTIAL art / v2.7 / 2026-10-14 | PARTIAL: source framing needs review; not user approved; egg/planktonic larval art unsupported; Eight static stage/state views; early settled juvenile through adult; Specialist larval rearing is not modeled; no automatic aquarium reproduction. [Atlas](assets/expansion-v27/porcelain-anemone-crab/atlas-v1.png) |
| Bumblebee Snail / *Engina mendicaria* / `bumblebee-snail` | bottom_dweller / Uncommon / Moderate | IMPLEMENTED; PARTIAL art / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; egg/planktonic larval art unsupported; Eight static stage/state views; early settled juvenile through adult; Specialist larval rearing is not modeled; no automatic aquarium reproduction. [Atlas](assets/expansion-v27/bumblebee-snail/atlas-v1.png) |
| Tiger Sand Conch / *Conomurex luhuanus* / `tiger-sand-conch` | bottom_dweller / Rare / Moderate | IMPLEMENTED; PARTIAL art / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; egg/planktonic larval art unsupported; Eight static stage/state views; early settled juvenile through adult; Specialist larval rearing is not modeled; no automatic aquarium reproduction. [Atlas](assets/expansion-v27/tiger-sand-conch/atlas-v1.png) |
| Halloween Hermit Crab / *Ciliopagurus strigatus* / `halloween-hermit-crab` | bottom_dweller / Rare / Moderate | IMPLEMENTED; PARTIAL art / v2.7 / 2026-10-14 | Ready for user visual review; not user approved; egg/planktonic larval art unsupported; Eight static stage/state views; early settled juvenile through adult; Specialist larval rearing is not modeled; no automatic aquarium reproduction. [Atlas](assets/expansion-v27/halloween-hermit-crab/atlas-v1.png) |



## Permanent v2.9 additive ledger

| Common / scientific name / stable ID | Category / approved rarity / care | Batch / status | Art |
|---|---|---|---|
| Flame angelfish / *Centropyge loriculus* / `centropyge-loriculus` | fish / Rare / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/centropyge-loriculus/atlas-v1.png); NOT APPROVED |
| Coral beauty angelfish / *Centropyge bispinosa* / `centropyge-bispinosa` | fish / Uncommon / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/centropyge-bispinosa/atlas-v1.png); NOT APPROVED |
| Cherub angelfish / *Centropyge argi* / `centropyge-argi` | fish / Uncommon / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/centropyge-argi/atlas-v1.png); NOT APPROVED |
| African flameback angelfish / *Centropyge acanthops* / `centropyge-acanthops` | fish / Rare / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/centropyge-acanthops/atlas-v1.png); NOT APPROVED |
| Potter's angelfish / *Centropyge potteri* / `centropyge-potteri` | fish / Ultra Rare / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/centropyge-potteri/atlas-v1.png); NOT APPROVED |
| Joculator angelfish / *Centropyge joculator* / `centropyge-joculator` | fish / Legendary / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/centropyge-joculator/atlas-v1.png); NOT APPROVED |
| Regal angelfish / *Pygoplites diacanthus* / `pygoplites-diacanthus` | fish / Ultra Rare / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/pygoplites-diacanthus/atlas-v1.png); NOT APPROVED |
| Orchid dottyback / *Pseudochromis fridmani* / `pseudochromis-fridmani` | fish / Common / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/pseudochromis-fridmani/atlas-v1.png); NOT APPROVED |
| Yellow longnose butterflyfish / *Forcipiger flavissimus* / `forcipiger-flavissimus` | fish / Rare / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/forcipiger-flavissimus/atlas-v1.png); NOT APPROVED |
| Pyramid butterflyfish / *Hemitaurichthys polylepis* / `hemitaurichthys-polylepis` | fish / Uncommon / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/hemitaurichthys-polylepis/atlas-v1.png); NOT APPROVED |
| Kole tang / *Ctenochaetus strigosus* / `ctenochaetus-strigosus` | fish / Rare / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/ctenochaetus-strigosus/atlas-v1.png); NOT APPROVED |
| Tomini tang / *Ctenochaetus tominiensis* / `ctenochaetus-tominiensis` | fish / Uncommon / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/ctenochaetus-tominiensis/atlas-v1.png); NOT APPROVED |
| Purple tang / *Zebrasoma xanthurum* / `zebrasoma-xanthurum` | fish / Very Rare / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/zebrasoma-xanthurum/atlas-v1.png); NOT APPROVED |
| Gem tang / *Zebrasoma gemmatum* / `zebrasoma-gemmatum` | fish / Legendary / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/zebrasoma-gemmatum/atlas-v1.png); NOT APPROVED |
| Achilles tang / *Acanthurus achilles* / `acanthurus-achilles` | fish / Ultra Rare / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/acanthurus-achilles/atlas-v1.png); NOT APPROVED |
| Foxface rabbitfish / *Siganus vulpinus* / `siganus-vulpinus` | fish / Uncommon / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/siganus-vulpinus/atlas-v1.png); NOT APPROVED |
| One-spot foxface / *Siganus unimaculatus* / `siganus-unimaculatus` | fish / Rare / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/siganus-unimaculatus/atlas-v1.png); NOT APPROVED |
| Midas blenny / *Ecsenius midas* / `ecsenius-midas` | fish / Uncommon / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/ecsenius-midas/atlas-v1.png); NOT APPROVED |
| Lawnmower blenny / *Salarias fasciatus* / `salarias-fasciatus` | fish / Common / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/salarias-fasciatus/atlas-v1.png); NOT APPROVED |
| Bicolor blenny / *Ecsenius bicolor* / `ecsenius-bicolor` | fish / Common / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/ecsenius-bicolor/atlas-v1.png); NOT APPROVED |
| Angular flasher wrasse / *Paracheilinus angulatus* / `paracheilinus-angulatus` | fish / Rare / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/paracheilinus-angulatus/atlas-v1.png); NOT APPROVED |
| Melanurus wrasse / *Halichoeres melanurus* / `halichoeres-melanurus` | fish / Uncommon / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/halichoeres-melanurus/atlas-v1.png); NOT APPROVED |
| Yellow wrasse / *Halichoeres chrysus* / `halichoeres-chrysus` | fish / Common / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/halichoeres-chrysus/atlas-v1.png); NOT APPROVED |
| Leopard wrasse / *Macropharyngodon meleagris* / `macropharyngodon-meleagris` | fish / Very Rare / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/macropharyngodon-meleagris/atlas-v1.png); NOT APPROVED |
| Bartlett's anthias / *Nemanthias bartlettorum* / `nemanthias-bartlettorum` | fish / Rare / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/nemanthias-bartlettorum/atlas-v1.png); NOT APPROVED |
| Duncan coral / *Duncanopsammia axifuga* / `duncanopsammia-axifuga` | coral / Common / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/duncanopsammia-axifuga/atlas-v1.png); NOT APPROVED |
| Candy cane coral / *Caulastraea furcata* / `caulastraea-furcata` | coral / Uncommon / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/caulastraea-furcata/atlas-v1.png); NOT APPROVED |
| Yellow scroll coral / *Turbinaria reniformis* / `turbinaria-reniformis` | coral / Very Rare / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/turbinaria-reniformis/atlas-v1.png); NOT APPROVED |
| Black sun coral / *Tubastraea micranthus* / `tubastraea-micranthus` | coral / Ultra Rare / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/tubastraea-micranthus/atlas-v1.png); NOT APPROVED |
| Rhizo coral / *Rhizotrochus typus* / `rhizotrochus-typus` | coral / Legendary / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/rhizotrochus-typus/atlas-v1.png); NOT APPROVED |
| Skunk cleaner shrimp / *Lysmata amboinensis* / `lysmata-amboinensis` | bottom_dweller / Common / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/lysmata-amboinensis/atlas-v1.png); NOT APPROVED |
| Fire shrimp / *Lysmata debelius* / `lysmata-debelius` | bottom_dweller / Very Rare / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/lysmata-debelius/atlas-v1.png); NOT APPROVED |
| Randall's pistol shrimp / *Alpheus randalli* / `alpheus-randalli` | bottom_dweller / Uncommon / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/alpheus-randalli/atlas-v1.png); NOT APPROVED |
| Harlequin shrimp / *Hymenocera picta* / `hymenocera-picta` | bottom_dweller / Ultra Rare / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/hymenocera-picta/atlas-v1.png); NOT APPROVED |
| Coleman's shrimp / *Periclimenes colemani* / `periclimenes-colemani` | bottom_dweller / Legendary / Difficult | v2.9 / 2026-10-14 / REGISTERED; ACQUISITION HELD pending required fire-urchin host support | [8 stage/state views](assets/expansion-v29/periclimenes-colemani/atlas-v1.png); NOT APPROVED |

# AQUARIUM LIFE

## COMPLETE MASTER DEVELOPMENT PROMPT — VERSION 4.17
### Offline Browser Edition — playable v4.3.1, 2026-10-22

## Full livestock sprite production — current work

The verified production checkpoint contains382 native sixteen-frame sheets (6112 actual authored cells), covering110 of113 usable marine entries: all89 fish, all15 corals and6 of9 invertebrates. Batches1–11 are complete. The remaining18 sheets belong to Fire Shrimp (Lysmata debelius), Randall's pistol shrimp (Alpheus randalli) and Harlequin Shrimp (Hymenocera picta). Built-in image generation returned HTTP429 daily usage_limit_reached; four Fire Shrimp source candidates were rejected for alpha noise and webbed appendages, and14 sources were not generated. No rejected candidate enters gameplay. The reported reset is2026-10-20 at09:37AM America/New_York. Original approved art remains active for these three species. All119 biological records, six acquisition holds, freshwater lock, local saves, biology and economy are preserved. Full production is NOT complete. Exact per-entry paths, missing work and current Chrome/Edge evidence are in [LIVESTOCK_16_FRAME_SPRITE_PRODUCTION_REPORT.md](LIVESTOCK_16_FRAME_SPRITE_PRODUCTION_REPORT.md). Player visual approval is separate.

## Global marine fish animation audit — playable v4.0.3, 2026-10-16

Audited all 94 registered marine fish, including five acquisition-held clownfish and one fictional fish. Thirty-one have authored adult cycles; 63 previously translated static living poses. Added render-only species profiles, pixel-preserving tail/outer-fin motion, state-aware timing, banked side-profile turns and head/eye protection across three stages. No new biological species, AI/feeding/breeding rules, inheritance or saves are introduced. All 94 remain conservatively classed B (partial) because bespoke action/turn/pectoral artwork and anatomy approvals remain incomplete; this is not a claim of fully authored animation. See [FISH_ANIMATION_AUDIT.md](FISH_ANIMATION_AUDIT.md), [FISH_ANIMATION_SYSTEM.md](FISH_ANIMATION_SYSTEM.md) and [offline motion review](fish-animation-review.html).

## Ocean diving destination artwork — playable v4.0.2, 2026-10-16

Eight original pixel-art PNG environments replace the simplified expansion scenery for Indonesia, Philippines, Sri Lanka, Marshall Islands, Maldives, Australia, Florida and Mariana Trench. A central per-mode art mapping drives selection previews, proportional in-dive backgrounds and expedition-result accents. Older regional PNGs, native encounter pools, all diving gameplay, local saves and freshwater lock are preserved. See [DIVING_LOCATION_ART_REPORT.md](DIVING_LOCATION_ART_REPORT.md). Art is implemented for review; no prior livestock/art approval is changed.

## Global aquarium preparation repair — v4.0.1, 2026-10-16

Corrected the saved `prepared=true` / stale `emptyDry=true` contradiction across setup, rendering, biological readiness and all receiving hosts. Existing saves repair only from preparation completion evidence; normal chemistry alone never certifies preparation. See [AQUARIUM_PREPARATION_REPAIR_REPORT.md](AQUARIUM_PREPARATION_REPAIR_REPORT.md). Master v4.4 preserves all 31 major sections, local saves, freshwater lock and the 20-minute day. Earlier release reports remain historical where superseded.

## Global diving expansion and liquidation — playable v4.0, 2026-10-16

Implemented the authorized Emergency Diving Sales & Rock Resale and Global Ocean Diving Expansion request (specification v3.6). Seven new reef selections and Mariana remote exploration use the central registry. Catch development, medical assessment, concealed attached eggs and regular-store liquidation extend the existing receiving authority. See [DIVING_EXPANSION_REPORT.md](DIVING_EXPANSION_REPORT.md) and [DIVING_EXPANSION_SAVE_SCHEMA.md](DIVING_EXPANSION_SAVE_SCHEMA.md). Earlier milestone reports remain historical where superseded. All saves stay local; freshwater remains locked; one game day remains 20 real minutes.

## Mystery fish diving — v3.9 historical, 2026-10-15

Implemented the authorized Mystery Fish update (request v3.5) on top of playable v3.8. New valid Reef/Deep trips guarantee a reachable regional fish, concealed until boat return, with saved assignments, original question-mark art/reveal, explicit safe receiving and permanent transport-loss evidence. Empty/closed collectible pools block launch. Existing oxygen, fees, resale, local accounts, biology, genetics, breeding, care rewards and freshwater lock remain. See [MYSTERY_DIVING_RULES.md](MYSTERY_DIVING_RULES.md) and [MYSTERY_DIVING_UPDATE_REPORT.md](MYSTERY_DIVING_UPDATE_REPORT.md). Current master is v4.2; earlier release entries are historical where superseded.

## Automatic marine breeding — v3.8 historical, 2026-10-15

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

The former standalone Overnight Readiness panel is removed. Food & Feeding retains current food forecasts; Field Journal > Tank History > Reports retains historical offline and mortality evidence. Welcome Back and Tank History retain actual death-step causes, identities, food, equipment and chemistry separately from current recovered water. Local loads retain an untouched pre-repair snapshot when storage permits, exportable in Settings. Saves and downloads remain on each player's PC/browser. Review [OVERNIGHT_REPAIR_REPORT.md](OVERNIGHT_REPAIR_REPORT.md) for formulas, the complete absence matrix, reproducible evidence and limitations. Current playable release is v3.5 / consolidated MDP v3.8. Earlier release sections below are historical where superseded.

## v3.3 current release - 2026-10-14

Implemented the authorized v3.1 coral fragging/trading, v3.2 financial dashboard and v3.3 Marine Research Center. Equipment has three reusable coral tools and two mounting consumables; eligible parents produce independently simulated, mounted clones with tissue loss, recovery and lineage. Diving livestock can use regular or Deep Market dealers; regular pays floor(0.60 x the same Deep reference), and Deep requires Reputation 5 plus an active wanted request. Wanted Livestock remains separate from exactly four rotating dealer stock slots.

The AC button opens a reconciled, persisted financial history. Existing wallets migrate unchanged; new profiles start at the requested 5,000 AC. Saltwater Research and the existing Encyclopedia share permanent 5-AC canonical-species unlocks. All 94 marine fish are indexed; 93 real species are researchable, one fictional entry is preview-only. Fully verified dossiers: 0; incomplete: 93; five have reviewed biological annotations. Partial content is disclosed before purchase. See [V33_UPDATE_REPORT.md](V33_UPDATE_REPORT.md), [FINANCIAL_TRANSACTIONS.md](FINANCIAL_TRANSACTIONS.md) and [RESEARCH_SOURCES.md](RESEARCH_SOURCES.md).

Saltwater-only scope, safe persistent store destinations, local PC/browser saves, existing rewards/odds, all old livestock and artwork approvals/holds remain. No new biological species or art assets were added. Full printable continuity source is updated; binary PDF regeneration remains pending. Current playable version v3.4 / consolidated MDP v3.7.

## Earlier milestone record - historical where superseded

## Daily livestock survival reward v3.4 - current rule, 2026-10-15

Players earn **100 AC** for every completed qualifying in-game day without a livestock death. The player must own eligible living marine livestock throughout the full simulated day. This is one account-wide payment, not one per aquarium. The separate healthy-aquarium award remains **50 AC**; both independently qualified awards total **150 AC**.

A confirmed fish, coral or bottom-invertebrate death cancels the current qualifying day and starts 1,440 game minutes of recovery. Another confirmed death restarts recovery. Recovery time cannot count toward a qualifying reward day. Illness or living coral bleaching is not a death. The authoritative game calendar remains 20 real minutes per day; legitimate offline catch-up processes the same conditions. Game windows do not stop simulation. Casino requirements apply only if that game is implemented.

Existing balances and actual historical ledger receipts remain unchanged. Every future survival payment is 100 AC through the existing financial service, with canonical account/transaction IDs, actual payment time and completed qualifying day/status. Local save, financial sequence and offline timeline guards prevent re-awarding a settled day. See [V34_UPDATE_REPORT.md](V34_UPDATE_REPORT.md) and [FINANCIAL_TRANSACTIONS.md](FINANCIAL_TRANSACTIONS.md).

**Authorized 2026-10-14:** The user approved the complete 25/5/5 roster and rarities, confirmed saltwater-only, and explicitly requested "Implement v2.9". Roster approval and artwork approval are separate; new artwork remains unapproved. [Authorization](planning/v2.9/approval.json).

Implemented the twelve-step saved/skippable saltwater tutorial with medical guidance, three-second selection outlines, disabled freshwater UI, separate +50 healthy / +100 survival rewards with persistent death/recovery tracking, Deep Market display rename, local asset-value leaderboard preview, then5,000-AC 15,000-US-gallon aquarium (current25,000-AC price: section 4.6), proportional water-change salt consumption, independent mystery products and the approved 35-species marine batch. Saves remain local to each player's browser on their PC. The bottom mystery product is content-held because its Legendary host specialist is not eligible. See [V29_UPDATE_REPORT.md](V29_UPDATE_REPORT.md) for actual checks, care/art limits and release details. Earlier milestone sections below are historical wherever superseded.

---

# 1. ROLE, RESPONSIBILITIES & DEVELOPMENT MISSION

You are an elite multidisciplinary game development team consisting of:

- Senior JavaScript Game Engineer
- HTML5 Canvas Rendering Specialist
- Game Systems Architect
- Aquarium Biology and Marine Ecology Specialist
- Pixel-Art Technical Artist
- Animation Director
- UI/UX Designer
- Economy and Balance Designer
- Artificial Intelligence Behavior Programmer
- Quality Assurance Engineer
- Performance Optimization Specialist

Your mission is to develop **Aquarium Life**, a premium-quality, realistic, 2D pixel-art aquarium management and life simulation game.

The player creates, maintains, expands, and manages freshwater and saltwater aquariums, with the current development expansion focusing on saltwater.

The game must offer:

- Individual living fish with persistent attributes.
- Realistic aquarium water chemistry.
- Fish compatibility, aggression, predation, and death.
- Aquarium construction and customization.
- Substrate, rock, and coral ecosystems.
- Breeding, eggs, hatching, and genetics.
- A strategic economy with meaningful purchasing and selling limitations.
- Aquarium stores and a fictional Deep Market.
- Player quests and unlockable progression.
- Detailed graphics and animated environments.
- VIP content previews without real purchases.
- Fully offline browser operation.

This is a real game, not a static interface prototype.

**The central development philosophy is that every living creature and every environmental condition must have meaningful consequences.**

Do not declare features completed until they are functional and verified.

---

# 2. CORE GAME PHILOSOPHY & TECHNICAL REQUIREMENTS

## 2.1 Offline-First Development

The initial game must run entirely offline.

The player opens:

`index.html`

The game must start without requiring:

- Internet access.
- A backend server.
- Node.js during gameplay.
- Accounts.
- Cloud services.
- Third-party APIs.
- Remote assets.
- External CDNs.
- Subscriptions.
- Network connections.

Use HTML5, CSS3, and JavaScript.

Use locally bundled images, sprites, fonts, and other assets.

Ensure JavaScript loading works directly under `file://`, avoiding module-loading arrangements blocked by local-file security restrictions.

The game should support modern desktop Chrome, Edge, and Firefox as far as practical.

Never depend on a local development server for normal gameplay.

## 2.2 Technical Architecture

Separate gameplay simulation, graphics, UI, persistent state, game data, and player transactions.

Do not place all systems inside one massive JavaScript file.

Use reusable services and data-driven configuration.

Implement clear interfaces between systems.

## 2.3 Core Rules

1. All major game buttons must perform real actions.
2. Save data must remain valid and recoverable.
3. Individual fish must have persistent identities.
4. Aquarium chemistry must follow internally consistent simulation rules.
5. Players must experience consequences from their management decisions.
6. Game difficulty should arise from understandable mechanics, not arbitrary hidden punishments.
7. The economy must resist exploits.
8. Graphics must be visually consistent.
9. The game must remain usable on low-end computers.
10. Do not sacrifice core simulation stability to add more content.

## 2.4 Realism and Fun

Use real aquarium biology and husbandry as the foundation for gameplay.

When real-world accuracy conflicts with accessibility, make carefully documented simplifications.

Do not present fictional aquarium mechanics as established scientific facts.

Special fictional black-market creatures may use fictional biology, but their gameplay rules must remain consistent.

## 2.5 Permanent Saltwater Development Scope

Current and upcoming livestock development is saltwater only: marine fish, corals, benthic fish, invertebrates, eggs, specialty livestock and fictional marine specimens. Preserve existing freshwater livestock definitions, artwork, health, care, growth, diet, behavior and reproduction. Shared store, navigation, inventory, save and compatibility infrastructure may change when required, with freshwater regressions checked. Existing freshwater purchases and the pre-existing fictional Glassfang eel remain available; do not add freshwater species or silently revise their biology. Freshwater remains a long-term design category, not an authorized current expansion.

---

## 2.6 v2.9 Authorization and Freshwater Lock

**Authorized 2026-10-14:** The user approved the complete 25/5/5 roster and rarities, confirmed saltwater-only, and explicitly requested "Implement v2.9". Roster approval and artwork approval are separate; new artwork remains unapproved. [Authorization](planning/v2.9/approval.json). Freshwater creation, selection, purchases and shared interaction controls display `Freshwater — Coming in a Future Update.` Existing definitions, artwork, saved residents and biological simulation remain retained. Future development milestones must ask whether freshwater is next; the current answer authorizes saltwater-only v2.9.

# 3. OFFICIAL ART DIRECTION — LOCKED

## 3.1 Primary Visual Reference

The approved image must be located at:

`assets/reference/approved_clownfish_hybrid.png`

Inspect this image before creating or replacing visual assets.

If the image is missing, identify that limitation and follow the written requirements without claiming exact visual matching.

This image is the primary visual reference for Aquarium Life.

## 3.2 Locked Hybrid Art Style

Combine the following four artistic approaches.

### Classic 16-bit

- Crisp sprite boundaries.
- Recognizable silhouettes.
- Pixel-perfect scaling.
- Readable movement.
- Controlled visual complexity.

### Vibrant Arcade

- Vivid tropical fish colors.
- Saturated coral colors.
- Strong contrast.
- Exciting collectible presentation.

### Realistic Detailed Pixel

- Anatomically recognizable fish.
- Detailed fins.
- Species-specific coloration.
- Proper eye and mouth placement.
- Distinct scale patterns.
- Detailed coral structures.
- Natural-looking rocks and sand.

### Premium Indie

- Atmospheric underwater lighting.
- Layered aquarium depth.
- Sunlight shafts.
- Subtle reflections.
- Animated particles.
- Beautiful aquarium scenery.

## 3.3 Species-Specific Artwork

Fish must be recognizable as their actual species.

Do not use one generic fish sprite with different colors for every species.

Each species should have distinctive:

- Body shape.
- Head shape.
- Fin configuration.
- Tail structure.
- Patterns.
- Coloration.
- Proportions.
- Movement animation.

Priority fish for visual development:

- Niger Triggerfish.
- Clownfish.
- Angelfish.
- Lionfish.
- Dogface Pufferfish.
- Blue Tang.

Use scientifically appropriate marine species definitions. Ambiguous common names must be resolved into explicit species before assigning precise care requirements.

## 3.4 Coral Artwork

Apply the same hybrid pixel-art standard to:

- Zoanthids.
- Mushroom corals.
- SPS corals.
- LPS corals.
- Soft corals.

Corals must show detailed structures and species-appropriate movement.

Coral growth, stress, bleaching, and death must have visibly different states.

## 3.5 Habitat Artwork

The following must match the same style:

- Rocks.
- Sand.
- Aquarium backgrounds.
- Decorations.
- Plants.
- Equipment visible in the tank.
- Bubbles.
- Water effects.
- Store previews.
- VIP previews.

## 3.6 Fish and Coral Death Artwork

Provide dedicated artwork or animation states for:

**Fish**
- Healthy.
- Stressed.
- Sick.
- Recently deceased.
- Sideways/upside-down.
- Drifting or sinking.
- Settled on the tank bottom.
- Decomposition stages.
- Remaining organic or skeletal matter where appropriate.

**Corals**
- Healthy.
- Stressed.
- Bleached but alive.
- Tissue recession.
- Dead tissue.
- Exposed stony skeleton.
- Algae-covered remains.
- Gradual structural degradation.

Maintain an appropriate general-audience appearance.

Do not use excessive gore.

## 3.7 Pixel Rendering Requirements

Use appropriate native sprite resolutions, allowing different species and object sizes.

Maintain consistent pixel density across visual assets.

Use nearest-neighbor scaling for base sprites and separate optional atmospheric effects.

Prevent blurry fish graphics.

Use sprite atlases and cached artwork where beneficial.

Avoid emoji or generic geometric shapes as final livestock artwork.

---

## 3.8 Current Livestock Art Review Gate

This historical art-review phase was artwork only. The later expressly authorized store/collection milestone and current marine economy/disease/valuation milestone supersede that earlier scope gate for their named features. Unrelated gameplay expansion and automatic art approval remain prohibited. Current medical rules are in 9.3.1, valuation in 16.4, medicines in 18.5 and restricted treatments in 19.3.

Follow this sequence: audit actual implemented species into CURRENT_FISH_CATALOG.md; inspect the approved reference; produce a transparent clownfish benchmark; present an offline gallery with current/proposed equal-scale comparisons, multiple native-resolution studies, actual game-scale previews and basic animation; then STOP for explicit user feedback. Only after the user approves the clownfish standard may art development expand to other priority fish and corals. Do not advance to another gameplay phase before that approval.

The user has requested the generated clownfish artwork for Ocellaris clownfish. This specifically authorizes assigning that atlas to the existing clown species ID in aquarium rendering, store previews and inspectors. Preserve existing saves and prior art. This assignment does not require adding other species or resuming unrelated gameplay phases.

Record reference interpretation, proposed sprite/animation rules, honest quality limitations and biological ambiguities in ART_DIRECTION.md. Gallery review statuses are Not Started, Needs Improvement, Ready for Review and Approved; only the user can approve. Preserve existing art and saves. Planned priority fish are not evidence of implemented gameplay species. Marine angelfish and lionfish exact species must be resolved before definitive art. Never present generated or procedural prototypes as finished hand-crafted assets.

---

## 3.9 Art Development Update v1.1 - Preserved Prior Delivery

The user now authorizes art expansion across all six priority fish, five saltwater coral categories and Fiji/Caribbean/Hawaiian rock collections. This supersedes the earlier stop-after-first-clownfish gate for the expressly requested art update. It does not authorize unrelated economy, breeding, quests, Deep Market or chemistry expansion.

Permanent rules: anatomically appropriate visible eyes remain attached to the head in every applicable frame; correct left/right facing follows meaningful movement with jitter resistance; fish-local transformations preserve all body components and do not affect UI or other animals. Side views show the near-side eye, not two forced eyes. Use registered baked eyes or stable local components, shared safe transforms, validated source rectangles and bounded caches. Support authored side-specific sprites when asymmetry requires them.

The selected marine angelfish is adult Emperor angelfish (Pomacanthus imperator); the selected lionfish is Red lionfish (Pterois volitans), explicitly confirmed by the user. Create their art without inventing new care/store mechanics for absent gameplay species. Audit all older fish for eye/direction defects and distinguish implemented gameplay fish from art-only subjects.

Coral art must distinguish healthy, stressed, bleached living tissue, tissue loss and dead remains with appropriate rigid/soft movement. Stony skeleton and collapsed soft tissue differ. Rock art needs small/medium/large/arch variants, transparent openings, appropriate material definitions, consistent scaling and safe layering; geographic names alone do not imply chemistry.

The offline gallery includes Fish, Corals and Rocks with directions, frames, eye overlays, native/enlarged/gameplay-scale views, coral states, rock variants and lighting. Preserve prior art and saves. Verify all affected frames/directions, transforms, sizes, loading, UI and offline operation. Pixel-presence checks do not prove perfect anatomy; provide reproducible visual contact sheets and identify artistic limitations. After delivering and testing this art update, STOP for user visual approval before unrelated development.

---

## 3.10 Permanent Livestock Life-Stage Art Standard

The full life-stage standard survives the later dedicated clownfish and shared-store milestone in section 3.11. Earlier approved art and historical sources remain preserved. Do not infer authorization for unrelated gameplay expansion from an art update.

Audit actual code and assets before adding or replacing art. Classify every entry IMPLEMENTED, ART ONLY, DATA ONLY or PLANNED. Maintain CURRENT_LIVESTOCK_CATALOG.md with names, known scientific names, IDs, category, status, stages/missing stages, alive/dead art, paths, animation, quality and notes. Do not guess scientific names, inflate totals or count a benthic fish twice.

Permanent rule: **every livestock species must map Egg, Baby, Juvenile and Adult to both alive and dead artwork**. This includes fish, corals, bottom feeders, future invertebrates and specialty livestock. Biological equivalents may be embryo, larva, fry, settled polyp, frag or juvenile colony. Simulation gaps never excuse silently missing art; build the artwork or disclose its scaffold status. Babies/juveniles need meaningful anatomy, pattern or colony changes, not a scaled adult. Dead poses must preserve recognizable identity and applicable eye placement without gore.

The approved hybrid pixel style and permanent eye/facing/transform rules remain locked. Use local transparent PNGs or mapped atlases, preserved previous sources, explicit metadata and offline loading. Store/catalog and gallery artwork must follow the same style. Stony and soft coral remains differ; pale living bleaching is not death.

Future expansion batches target **25 new fish + 5 new corals + 5 new bottom feeders**, each with the full art chain. The later explicit v2.7 authorization adds exactly 28 fish + 5 corals + 5 non-fish bottom dwellers as a one-batch exception; the default future batch target remains 25/5/5. The earlier audit contained 22 fish and five coral categories. The current dedicated collection audit is recorded in section 3.11 and CURRENT_LIVESTOCK_CATALOG.md. Five additional marine adult-art studies remain ART ONLY.

Required order: audit, catalog, standardized pipeline, existing fish, existing corals, existing bottom feeders, all required dead states, review gallery, testing, stop. Code changes are limited to art loading, rendering, animation, stage display and previews. Existing simulation and save schema remain authoritative.

The review gallery must be reachable from index.html offline, with Fish/Corals/Bottom Feeders, implementation status, every stage and dead state, nearest-neighbor enlargement, actual display-scale references and disclosed missing content. Approval is the user's decision; never mark new art approved automatically.

Deliver catalog, updated art direction, stage art and alive/dead support, working gallery, development status, missing-content notes and a clear implemented/scaffolded distinction. **Stop after each authorized art milestone for user visual review.** The subsequent dedicated clownfish instruction authorizes section 3.11; no broader expansion follows automatically.

## 3.11 Dedicated Clownfish Collection and Art Review

The dedicated exception contains the following 31 catalogued scientific names. Verify accepted names and synonyms with FishBase and primary taxonomic sources. A listed name does not resolve every hybrid-origin dispute; disclose the uncertainty for A. leucokranos and A. thiellei. Preserve gameplay ID `clown` for A. ocellaris and do not duplicate Premnas biaculeatus as a separate species.

Amphiprion ocellaris, Amphiprion percula, Amphiprion biaculeatus, Amphiprion clarkii, Amphiprion frenatus, Amphiprion melanopus, Amphiprion ephippium, Amphiprion perideraion, Amphiprion sandaracinos, Amphiprion akallopisos, Amphiprion polymnus, Amphiprion sebae, Amphiprion akindynos, Amphiprion allardi, Amphiprion bicinctus, Amphiprion chrysopterus, Amphiprion nigripes, Amphiprion omanensis, Amphiprion chagosensis, Amphiprion chrysogaster, Amphiprion fuscocaudatus, Amphiprion latifasciatus, Amphiprion leucokranos, Amphiprion mccullochi, Amphiprion latezonatus, Amphiprion rubrocinctus, Amphiprion tricinctus, Amphiprion barberi, Amphiprion pacificus, Amphiprion thiellei, Amphiprion maohiensis.

Designer varieties are linked phenotypes, not extra biological species:

Black Ocellaris (Amphiprion ocellaris), Snowflake Ocellaris (Amphiprion ocellaris), Premium Snowflake (Amphiprion ocellaris), Black Snowflake (Amphiprion ocellaris), Black Ice Snowflake (Amphiprion ocellaris), Wyoming White (Amphiprion ocellaris), Snow Storm (Amphiprion ocellaris), Black Storm (Amphiprion ocellaris), Mocha Storm (Amphiprion ocellaris), Mocha Ocellaris (Amphiprion ocellaris), Gladiator (Amphiprion ocellaris), Mocha Gladiator (Amphiprion ocellaris), DaVinci (Amphiprion ocellaris), Frostbite (Amphiprion ocellaris), Black Frostbite (Amphiprion ocellaris), Midnight (Amphiprion ocellaris), Domino (Amphiprion ocellaris), Naked Ocellaris (Amphiprion ocellaris), Misbar Ocellaris (Amphiprion ocellaris), Longfin Ocellaris (Amphiprion ocellaris), Picasso Percula (Amphiprion percula), Premium Picasso Percula (Amphiprion percula), Platinum Percula (Amphiprion percula), Onyx Percula (Amphiprion percula), Lightning Maroon (Amphiprion biaculeatus).

Each collection entry requires Egg, Baby, Juvenile and Adult alive/dead support. Genuinely indistinguishable designer eggs and larvae may share their base-species art through explicit metadata. Juvenile pigmentation and fin development must differ meaningfully from adults. Build a four-pose adult swimming cycle with stable head-local eye pixels, complete fins, nearest-neighbor scaling, restored canvas transforms and documented mirrored side views. Preserve original files and the approved assigned adult Ocellaris benchmark until the user approves a replacement. Never automatically mark new art approved.

Species profiles include identity, adult length and SL/TL measurement, difficulty, tank volume/footprint, temperature, pH, salinity, diet, territorial behavior, pair structure, reef interaction, reproduction, lifespan confidence, host requirements and verification sources. Use Easy, Moderate, Challenging, Difficult, Expert or Extreme for husbandry; designer rarity and price are separate. Separate sourced facts, genus-level guidance and conservative game calibration. Missing specialist care information means a visible purchase hold, not an invented verified profile. Designer genetics must remain linked to the base species; do not fabricate exact inheritance.

Audit every existing livestock entry without hiding absent art or adding planned examples to playable totals. The offline collection gallery needs species/designer views, search, base-species filter, all stages and deaths, direction, play/pause/frame step, zoom/backgrounds, actual gameplay scale, original/revised/reference comparison, taxonomy/care/art status and separately saved review notes. Include a global livestock audit and a coral placement test scene. The historical dedicated-collection audit had 52 fish records (including four benthic fish) and five coral categories; the current v2.7 roster is in section 6.4; five specialist clownfish profiles remain purchase-held. Five earlier fish studies remain ART ONLY and three named proposals PLANNED. **Stop at the completed review gallery for user review.**

---

## 3.12 v2.9 Artwork

35 original transparent sprite sheets provide 280 static stage/state views: appropriate early equivalents, baby/larva, juvenile/growing, adult/mature and their authored deceased states. Fish/shrimp art faces right and mirrors as a complete sprite when moving left. Original generated files and prompts are retained. Technical alpha cropping and nearest-neighbor packing do not repaint specimens. One source-boundary review flag and provisional eye metadata remain; no automatic approval or claim of complete swim/feeding animation. Review v29-review.html and assets/expansion-v29/art-generation-record.json.

## 3.13 Equipment and casino artwork - v3.7 permanent

Equipment Artwork: Product artwork must visually represent the item being sold; fragging tools must not reuse unrelated heater or equipment sprites. Original code-native transparent pixel previews cover cutters, kit, saw, plugs and mounting supplies consistently across store, details and inventory. Casino wheel/title/symbols/backs/dealer/result effects are original pixel artwork; livestock cards reuse existing catalog art. No new livestock art approval is implied and existing holds remain.

## 3.14 Marine livestock animation — authoritative16-frame requirement (v4.0.4)

Audit every runtime marine fish, coral and non-fish invertebrate against CURRENT_LIVESTOCK_CATALOG and original source art. Use runtime dictionary keys, preserve stable IDs/holds, exclude protected freshwater and unimplemented reference art, avoid duplicate species and track designer morphs under their biological species. Process the entire eligible roster in batches of10; record missing artwork and continue to the next entry. Keep artwork-required and rejected candidates separate from completed production assets. LIVESTOCK_16_FRAME_SPRITE_PRODUCTION_REPORT.md is the current per-entry production/evidence ledger; LIVESTOCK_ANIMATION_16_FRAME_REPORT.md remains the historical infrastructure audit; never claim visual approval until the player actually reviews it.

Production sources and exact prompts are retained under planning/sprite-production. Produce actual sixteen-pose drawings with the built-in image tool, pack and inspect every native cell before central registration, and run real gameplay/gallery checks for each batch before continuing. Technical alpha extraction, nearest-neighbor packing, consistent original-eye registration and declared native-facing normalization do not create extra drawn poses. Preserve the biological-species early source shared by designer babies and Banggai's existing baby-to-developed-juvenile alias; do not double-count shared source sheets. Completion is based on actual assets and current file-hash evidence, never requested frame slots or player approval inferred from agent inspection.

The sole presentation authority remains AL.FishAnimation, with family/stage motion in assets/animation/fish-registry.json and all-livestock authored-sheet slots in assets/animation/livestock-registry.json. Preserve2D Canvas, approved original sprites, natural Ocellaris benchmark, body/head/eyes, genetic markings, designer identities, stages and death art. A fish needs a genuinely authored16-frame normal swim cycle at each applicable free-swimming stage: neutral, initial tail/pectoral adjustments, one controlled sweep, neutral transition, opposite sweep and seamless recovery. These are species-appropriate phases, not an identical rig imposed on unrelated anatomy. Exactly16 distinct aligned transparent cells, fixed anchor/head/eye, stable proportions/lighting/pixel resolution, attached fins and persistent markings are required. Duplicated stills, recolored placeholders, static concept grids or unreviewed generated approximations cannot satisfy that count. Early anatomy must use its own appropriate source; retain Banggai's developed juvenile release and never invent external eggs or mature larval fins. Keep unresolved caudal-fold-only/early outer-fin layers explicit.

Separate frame count from speed. Begin normal fish playback around6–10frames/second for a16-frame cycle, then tune calm species/stage movement. Reduce resting/perched movement, increase actual fast propulsion naturally, avoid excessive fin flapping, repeated whole-body wobble and double-frequency fin exaggeration. Distinguish clowns' short hover, tang cruising, goby/blenny perch/dart, wrasse propulsion, basslet/cardinal hovering and other implemented anatomical families. No puffer/lion/trigger profile may create a species absent from the roster. Until authored poses exist, only restrained existing-pixel articulation is allowed and must remain labelled partial. Retire procedural deformation wherever a validated authored sheet supplies that motion; do not stack both.

Invertebrate sequences must depict appropriate leg/claw/antenna/foot/fan and shell-carrying movement, including very slow crawling. Never use a fish swimming rig for them. Coral motion is limited to appropriate existing polyps/tentacles/retraction/feeding/flow response; rigid stony skeletons and attachment points stay stable. Minimal-motion species must not be exaggerated to fill a sheet. Preserve placement, fragging, growth, health, bleaching, recovery and mortality. Lack of separate polyp/limb layers is missing artwork, not permission to distort the whole organism.

Register species ID, local PNG path, cell width/height/count, ordered16indices, playback timing, anchor, facing, stage, state and variety identity centrally. Reject missing, blank, repeated or unvalidated production sheets. Keep prototypes out of gameplay. Local lazy decoding/cached sheets and bounded extracted-frame caches serve both file:// and hosted offline play. Retain original art until a compatible sheet is ready; never substitute another stage or designer variety. Apply genetic markings to the selected authored source, then draw it without an extra fin warp. Mirror existing side profiles correctly, retain the single visible eye and preserve phase across direction changes; independent opposite-side/yaw art is not implied. Anchors, layering, hitboxes, offscreen culling, selection IDs, three-second outlines and independent inspector lifetime remain consistent.

Use renderer-owned real-time clocks only. Existing Eat/Rest/Hide and autonomous breeding/visible-health states may inform motion; rendering never initiates feeding, mating, disease, eggs or biological RNG. Respiratory activity and weak/injured motion remain distinct; dead specimens freeze live motion and retain authored mortality art and simulation sinking. Do not change20real minutes/day, offline ecology, water, breeding, health, genetics, economy, acquisition restrictions or save schema.

Provide a development-only offline all-livestock gallery with names/categories, original artwork, real new sheets or explicit missing status, individual-cell inspection, animated playback, slow-speed control, stage/state/facing/morph selectors and completion/approval status. No unfinished controls enter the ordinary player UI and the gallery must not access player saves. Validate every actual sheet's16cells, loads, transparency/bounds, subtle meaningful differences, stable eyes/body/patterns, fin attachment/loop and actual visual quality; do not claim missing-sheet checks passed. Also verify actual gameplay clicks, calm/idle/turn/death, save/load, offscreen/performance at normal and high stock, renderer-rate independence, all original freshwater output and freshwater lock. Future marine additions must automatically fail coverage if unmapped. Retain the consolidated31-section master and exact continuity copy. Current architecture/limits are in FISH_ANIMATION_SYSTEM.md; current authored-art coverage is in LIVESTOCK_16_FRAME_SPRITE_PRODUCTION_REPORT.md.

# 4. WORLD STRUCTURE, AQUARIUM TYPES & SIZES

Players can own multiple aquariums.

Supported aquarium types:

- Freshwater.
- Saltwater fish-only.
- Saltwater reef.
- Breeding.
- Quarantine.
- Egg incubation.
- Specialist habitat.
- Prestige exhibition aquarium.

## 4.1 Aquarium Sizes

All player-facing aquarium capacities, fish requirements, equipment ratings, destination selectors and water-change quantities use **US gallons**. One centralized formatter uses exactly **1 US gallon = 3.785411784 liters**, normally one decimal. Preserve the authoritative internal liter values and physical capacity; never relabel liters as gallons or change an old aquarium's size. Chemical concentrations remain mg/L. Nominal product marketing, if introduced, must be distinct from actual capacity.

| Aquarium | Display (US gal) | Internal saved capacity (L) |
|---|---:|---:|
| Nano | 5.3 gal | 20 |
| Small | 10.6 gal | 40 |
| Starter | 19.8 gal | 75 |
| Community | 39.6 gal | 150 |
| Gallery | 79.3 gal | 300 |
| Showcase | 132.1 gal | 500 |
| Grand aquarium | 264.2 gal | 1,000 |
| Public exhibit | 660.4 gal | 2,500 |
| Ocean hall | 1,320.9 gal | 5,000 |

Sizes are product categories, not guarantees that all species can be kept in these tanks.

Species suitability must consider actual dimensions, mature size, swimming area, social needs, and filtration capacity.

## 4.2 Aquarium Ownership

Players may:

- Buy tanks.
- Name tanks.
- Rename tanks.
- Customize tanks.
- Install equipment.
- Place substrate and rock.
- Purchase and introduce livestock.
- Monitor tank history.
- Transfer compatible organisms.
- Maintain multiple aquariums.

Each aquarium has its own persistent environment and simulation state.

## 4.3 Empty Tank Rule

**Every newly purchased or created aquarium starts completely empty and dry.**

No fish, coral, rock, sand, or water should appear automatically.

The tank must be constructed and prepared by the player.

---



## 4.5 Nominal Whole US Gallons

Display nominal aquarium/equipment capacities with mathematical ceiling to whole US gallons (75 L → 20 gal). Preserve exact internal liters, stocking capacity and all dose/chemistry calculations. Use the separate preciseVolume presentation for replacement-water quantities. See §5.5 for diving receiver displays.

## 4.6 15,000-US-Gallon Aquarium

Ocean Sanctuary is exactly 56,781.17676 L of simulation water and costs exactly 25,000 AC total for marine purchase at Keeper Level 10, without a 1.25 markup. It starts empty/dry. Defined water envelope: 1,000 × 400 × 141.9529419 cm, substrate area 40 m². Saved water remains the usable game capacity; sand/rock displacement and structural engineering are not modeled. Freshwater is future-locked. Installed equipment scales to actual volume through existing price/capacity/energy/service formulas; filter capacity must cover volume, reef lighting and flow must meet selected livestock profiles. Shell value uses the 25,000-AC base. Existing purchases are not retroactively charged; all other tank prices remain unchanged. Stable size catalog IDs are used for profile milestones in section 6.6. Water preparation, substrate, shelter, cycling and compatible livestock are separate purchases.

# 5. GAMEPLAY LOOP & NEW TANK SETUP

The basic gameplay loop is:

Build → Prepare → Cycle → Stock → Maintain → Grow → Earn → Expand.

## 5.1 Required Setup Progression

Player-facing order:

1. Add sand.
2. Prepare and add appropriate water.
3. Install necessary equipment.
4. Arrange suitable rock and hardscape.
5. Establish the nitrogen cycle.
6. Verify water readiness.
7. Introduce appropriate livestock.

Rocks may be installed earlier when biologically appropriate.

Do not force all live rock to be added only after cycling; properly prepared live rock may help establish biological filtration, while uncured rock may introduce additional waste.

## 5.2 Setup Visualization

Every stage must have a visible effect.

Examples:

- Empty tank displays bare glass.
- Sand addition creates a visible substrate layer.
- Water addition changes water level.
- Rock placement changes habitat geometry.
- Equipment becomes visible where appropriate.
- Cycling generates realistic chemical and biological changes.
- Livestock appears only after proper introduction.

## 5.3 Cycling

Cycling is a biological process, not merely a countdown.

Implement bacterial establishment and sufficient processing capacity.

Show:

- Ammonia.
- Nitrite.
- Nitrate.
- Biological filter maturity.
- Relevant warnings.
- Water testing history.

The player should understand why the tank is or is not ready.

## 5.4 Livestock Readiness

Readiness must depend on the requirements of the specific organism.

Fish, coral, and other organisms may require different environmental maturity.

A tank being biologically cycled does not automatically mean it is suitable for sensitive corals.

---



## 5.5 Ocean Diving — Primary Mystery Fish Specification (playable v3.9)

Every valid Reef Diving and Deep Sea Diving expedition must provide at least one reachable mystery fish encounter. Its species is concealed using a question-mark silhouette until successful return to the boat. Geographic eligibility, inventory, oxygen, post-dive survival, and save persistence remain mandatory.

Ocean Diving remains saltwater-only and uses the existing fixed-step simulation, shared modal, health, value, inventory and local save authority. Its button remains beside saved Keeper Level. Reef requires Keeper 5 and exactly 1,000 AC; Deep Sea requires Keeper 10 and exactly 10,000 AC, all rentals included once in an atomic confirmed launch.

The data-driven `assets/diving/registry.json` contains nine encounter profiles referencing existing species IDs and twelve destination selections; no biological species was added. Original Fiji, Caribbean, Hawaii and Japan remain. New reef selections: Coral Triangle—Indonesia (Bunaken), Coral Triangle—Philippines (Puerto Galera), Sri Lanka (Kayankerni), Marshall Islands (Majuro), Maldives (Madivaru Beyru), Australia (Lady Musgrave Island/Great Barrier Reef), and Florida (Tortugas/Keys). Existing Yellow longnose butterflyfish is eligible at the six new Indo-Pacific zones; existing Ocellaris clownfish additionally inhabits the two Coral Triangle zones; Chalk Bass inhabits Florida. Country range evidence is supplemented by locality records bundled in the registry. Existing 38/35-entry livestock and art ledgers remain unchanged. See DIVING_EXPANSION_REPORT.md for sources and conservative content limits. Hawaii remains wildlife-closed. Missing valid living pools block ordinary collection launches; the explicitly approved Mariana remote survey is a nonliving-only exception, never an exception to livestock receiving safety.

Both compact 11×7 maps retain terrain, regional scenery, boat and twelve encounter positions. First eight rocks remain; object 9 at (4,1) is a guaranteed mystery fish. Its safe round trip costs six movements / 30% oxygen, or four movements / 20% when capturing from an adjacent cell. Optional final three objects retain existing regional selection/presence rules; all optional fish are also concealed. Each fish swims smoothly inside its saved logical cell, so animation cannot move the guarantee beyond its safe route. Use one shared original dark generic pixel silhouette and large question mark for every fish. Do not expose names, scientific names, rarity, asset value or identifying shapes/markings through planner, map, interaction panel, temporary inventory or failed report. A local offline client/save is inspectable, not cryptographically secret; single-species pools limit uncertainty.

WASD, arrows and direction buttons move cardinally. Native key repeat is ignored in favor of controlled held repeats. Start at 100% oxygen; each successful movement consumes exactly five percentage points. Blocked movement, idle time, frames and collection clicks use none. Preserve warnings at 30/15/5%, route cost and return reserve. Zero oxygen fails even on boat arrival. Left-click within one Manhattan cell attempts capture; farther clicks select only. Recheck range, eight-slot capacity and duplicate status in the authority. Captured fish display `Unknown Fish — ?`, take one temporary slot and grant no permanent ownership. Inventory cannot overflow or discard existing finds. Failure/confirmed abandonment forfeits finds without identity reveal, fee refund or livestock grant.

Successful positive-oxygen boat return saves revealed results with actual common/scientific name, rarity, existing species art, original short pixel wipe and origin. Reduced-motion uses final art immediately. Pending recovery is explicitly labeled Awaiting receiving assessment, destination Not received, owned asset value zero. Choose a safe compatible cycled aquarium or quarantine after reveal; never auto-select or auto-place. Recheck safety cumulatively on each receive action. Final results display actual condition, destination and current central asset value. Close/reopen resumes pending results; block another launch until pending fish are received, explicitly released or expired. Corals/invertebrates retain an explicit pre-capture receiving/mount plan, then all newly collected livestock use the same saved post-boat receiving transaction. Corals explicitly confirm a currently supported mount; rocks use owned placement inventory.

Preserve the existing survival formula using species sensitivity, transport quality, elapsed game time, movement, prior condition and receiving/quarantine. Commit survival/condition draws at boat return; retries or reloads do not reroll. Preserve healthy/stressed/injured/suspected illness/DOA, finite sensitivity-based holding deadlines and real mortality. Pending expiry runs on the shared live/offline simulation. Transport DOA adds an event to the existing permanent account mortality journal with identity, actual loss time, known trigger and available expedition evidence. Unmeasured water, temperature, hunger, health history and equipment remain unknown; do not invent a physiological cause. Do not count unowned transport loss as an owned-tank death or alter care reward rules. Survivors enter the existing health system with permanent origin/trip provenance. Existing regular resale is floor(0.60 × Deep reference); Deep requires Reputation 5, matching active Wanted request and all existing eligibility limits under 19.6. Do not guarantee profit.

Planning, play, confirmation and results keep the authoritative aquarium clock at 1×, 20 real minutes per game day, while preserving the prior speed preference. Keep hunger, chemistry, disease, eggs, coral, growth, equipment, calendar/store rotation and rewards advancing. Save active region/mode, guarantee ID, hidden assignment, position, collected flags, inventory, oxygen, fee/transaction and RNG; save report reveal state, precommitted assessment, deadline, recovery result/destination and death-record link. Local completion/recovery receipts prevent ordinary replay grants. Legacy active trips resume unchanged without retroactive rerolls. Keep all data on the player's PC/browser and existing export/import/timeline safeguards.

Preserve existing diver/boat/equipment/scenery and approved species art. No new art is automatically approved. X/Escape/backdrop dismiss ordinary windows but protect active trips with explicit loss confirmation; inside clicks cannot click through. Sticky oxygen/inventory HUD and responsive mouse/keyboard/touch controls remain. Full implementation/testing/limits: MYSTERY_DIVING_UPDATE_REPORT.md. Other master sections reference this primary specification instead of duplicating it.

### Receiving diagnostics repair — 2026-10-16

Every owned aquarium must appear in the fish receiving selector, showing name, US gallons, water classification, actual temperature and eligibility. Disable rejected destinations and expose exact reasons with actual values/requirements; never hide them. Expandable checks cover habitat, volume, species temperature range, salinity, pH, ammonia/nitrite/oxygen, prepared/cycled water and both bacterial colonies, working filter/circulation, stocking/reserved offspring, entity capacity, quarantine/course restrictions and all existing species safeguards. Quarantine is optional for an untreated catch, with its existing survival benefit; introducing untreated livestock into an active restricted course is unavailable. Show equipment condition/output without demanding perfect condition. Actual readings, not rounded display text or thermostat target, control compatibility. Preserve explicit selection/focus and refresh eligibility when aquarium conditions change.

Show the unchanged finite holding deadline and time remaining in game time with an approximate 1× real-time equivalent. Read-only UI/validation errors must not delete, kill, reroll or alter the specimen/deadline. Only existing expiry or actual transport assessment causes mortality. Successful receiving must use the existing validated transaction, permanent ID/health/genes/provenance, count/value recalculation and local save/receipts, clearing pending status without duplicates. Preserve old saves and freshwater lock. See DIVING_RECEIVING_REPAIR_REPORT.md for the Chalk Bass audit, precise confirmed UI cause and diagnostic limitations; 80 gallons and 27°C alone do not prove a particular saved tank's eligibility.

### Universal diving receiving — permanent, 2026-10-16

Every implemented diving-eligible fish, coral and bottom-dwelling invertebrate uses the same receiving authority, all-owned destination diagnostics and saved post-boat ownership transaction. Resolve its actual unique biological ID/category and apply that species' own requirements; never hardcode a Chalk Bass exception or map missing IDs to another host. Validate complete unique region/mode/depth/transport profiles before spawning. Every aquarium remains visible, with disabled unsafe choices and exact actual/required checks. Preserve fish-specific ranges/group/stocking/behavior, coral light/flow/minerals/support/clearance, and invertebrate range/oxygen/flow/habitat/load requirements. A fully prepared compatible coral-only quarantine is allowed, without waiving any environmental, support or medication checks.

Preserve finite saved holding, committed condition/survival draws, explicit destination/mount, identity/health/rarity/origin/genetics where modeled/value, count/value recalculation, atomic local saves and replay receipts. Invalid receiving or a changed mount must leave pending livestock intact so a valid destination/mount can be chosen. Never mark a noninfectious injury as an infectious carrier or relax health validation to accept it. Permanent transport mortality resolves the actual host category without inventing unmeasured causes. Old saved snapshots and completed reports remain compatible; no duplicate grants or resurrection. Regression coverage must enumerate the actual eligible registry across hosts, sizes, regions and both dive modes so future complete registrations automatically use and test this service. See GLOBAL_DIVING_RECEIVING_REPORT.md for current coverage, confirmed causes, files and limits.

### Regional collection, random development and medical assessment — v4.0 permanent

Every living encounter must resolve through the existing species registry, verified region/habitat/depth profile and shared receiving rules. Never substitute fish to fill empty pools. All eligible ordinary expeditions retain the reachable concealed mystery-fish opportunity, eight slots, movement controls, 5% oxygen per successful movement and mandatory boat return. Fish identity, rarity, value and developmental art stay concealed before return.

Approved configurable stage weights are baby 20%, juvenile 35%, adult 45%. Restrict and normalize to biologically eligible stages: settled Ocellaris in anemone-associated Coral Triangle habitat supports all three; remaining current profiles conservatively allow juveniles/adults. No free-swimming larva is mislabeled a settled baby. Save the actual individual at capture with ID, approximate accelerated age, growth, adult size, sex/temperament, genetics/pattern, source and expedition. Receiving never recreates it as an adult. Young fish retain existing fine-food metabolism, protection and sale development checks. Dedicated refuge and fine fry food are required for baby receiving.

Use the same saved survival/medical draws for receiving and emergency valuation, never redraw in UI or after load. Transport assessment includes species sensitivity, transport quality, elapsed exposure, movements, pre-existing risk, young-stage fragility and quarantine benefit. Healthy, stressed, malnourished, injured, suspected infection, severely compromised and dead-on-arrival outcomes are possible. Existing host-eligible conditions are used; symptoms are not diagnoses. Show HP, signs, quarantine advice, treatment host restrictions and Disease & Treatment Guide access. Actual finite holding and permanent transport mortality records remain.

### Mystery eggs — v4.0 permanent

An eligible expedition has one independent 3% discovery opportunity; store Mystery Egg rarity odds are untouched. Current external egg pool: existing Ocellaris in the two Coral Triangle zones, attached to a removable substrate chip near anemone habitat. Never float demersal eggs in open water or collect mouthbrooded/liveborn offspring as eggs. Assign permanent hidden species, clutch ID, genetics/embryo pattern, provenance, approximate development and viability at collection. Parents remain unknown. One representative egg uses an explicitly simplified recovery model with 85% initial estimated viability and a 24-game-hour finite holding deadline; no incubation occurs in inventory. Save/load cannot reroll identity.

List every owned aquarium with the shared species checks and additional empty dedicated marine incubation, fine-food and gentle-flow requirements. Development uses the existing species water/oxygen and suitable-hour model, with operating filter/circulation and protected support required. Ordinary wear tolerance is explicit. Poor conditions pause progress and reduce viability; failure is retained in the expedition report. Identity, rarity, coloration, genetic pattern and expected asset value stay concealed in map, results, aquarium scene, inspector and Journal until hatch. Hatching creates a unique actual early larva, transfers established genetics/provenance, reveals the report and updates the Field Journal. Larvae need fine food and retain accelerated game growth; this does not claim complete real-world captive culture. Store-purchased identified Mystery Eggs retain their old reveal policy.

### Emergency Sale and diving rock resale — v4.0 permanent

Unreceived living diving fish/coral/invertebrates may use regular Aquarium Store Emergency Sale without a suitable receiver: `max(0, floor(central eligible specimen value × 0.25))`. Calculate using the actual saved specimen, stage, genetics/quality, health and transport survival; dead/expired/protected specimens are ineligible. Show and confirm the exact offer. This service is unavailable after receiving, does not satisfy Wanted requests and earns no Deep Market reputation. Preserve regular owned diving resale at exactly floor(Deep reference × 0.60), and preserve Deep Market Reputation 5, active Wanted request, condition/access/budget checks.

Recovered nonliving rocks retain unique item ID, product group/variant, size/one-piece quantity, condition, region and expedition. Keep/place or explicitly sell after successful boat return, through expedition results or Aquarium Store → Saltwater → Sell. Central rock estimate is `floor((existing product price + variant × 25) × quantity × condition)`; buyback is floor(estimate × 0.40). This stays below retail. Placing/removing preserves the same identity/provenance; removal still refuses attached coral or eggs and requires inventory space. Store-bought rocks cannot masquerade as recovered salvage. Finite inventory limits remain.

Each confirmed sale produces exactly one account ledger receipt with item/species ID, expedition, dealer, actual amount, time and resulting balance; a valid zero-AC emergency offer records one explicit zero income receipt. Atomic ownership/status changes, financial keys and local settled receipts prevent double clicks and stale-save replay. No server is added. See DIVING_EXPANSION_SAVE_SCHEMA.md.

### Mariana Trench — v4.0 permanent

Deep Sea only, Keeper 10 and 10,000 AC. Represent a fictional tethered research drone at a 6,000 m southern Mariana hadal slope with battery presentation (100%, 5% per successful movement) and return to dock. Never draw an ordinary diver at hadal depth. Registry records approximately 2 °C, approximately 600 atmospheres, no decompression-safe livestock transport and no approved pressure aquarium. There is no valid living pool, egg pool or ordinary reef receiving path; only nonliving fictional sample recovery. No specialized pressure containment or fabricated hadal livestock is authorized.

### Destination identity and artwork — v4.0.2 permanent

Every selectable diving destination must have a defined regional identity, a valid geographically native species pool for each supported mode, and assigned selection/in-dive artwork. An explicitly observation-only or remote nonliving research destination may retain its intentionally empty collectible living pool; artwork never authorizes new species or collection. Preserve all existing depth, wildlife-closed and transport restrictions.

The primary destination registry is `assets/diving/registry.json`. Each supported mode has one `art` entry with a unique region-mode ID, original PNG path and description. The same registered source serves the picker, proportionally cropped map and result accent. Complete prompts and original filenames live in `assets/diving/art-prompts.json`; new source-v2 PNGs are unmodified built-in ImageGen outputs, integrated for user review. Fiji/Caribbean/Hawaii/Japan source PNGs remain unchanged. Do not silently substitute unrelated scenery. Build must reject missing, duplicate or incorrectly assigned art; runtime records failed loads explicitly. Embed local assets for file/offline play and package native files with case-correct relative paths for Pages.

Seven new reefs have distinct coral/rock/lagoon/shelf compositions. Mariana uses black-navy hadal terrain, sediment, a tethered research lander and localized lamp illumination without sunlight, reef corals or living collectibles. Existing drone controls, oxygen/battery cost, catch/reveal silhouettes, receiving, emergency sale and saving remain authoritative. Art rendering is read-only and must not consume simulation RNG or alter expedition state. Keep text on solid UI panels, preserve image aspect ratio and check desktop/mobile scaling. Do not add network asset dependencies or saved art state.

## 5.6 Interactive Saltwater Onboarding - Permanent Rule

The Aquarium Life saltwater onboarding tutorial is an interactive, guided gameplay experience. The player is directed through real interface controls using visible highlights and contextual instructions. Tutorial progression requires verified aquarium setup actions, not pressing Next. The tutorial covers creating and preparing a saltwater aquarium, installing life-support equipment, establishing the nitrogen cycle, purchasing compatible livestock, receiving livestock, and basic feeding and care.

Implement twelve phases through22 stable task IDs: welcome/owned aquarium/main view; appropriate substrate/depth, filling and preparation; installed filtration/temperature control/circulation; relevant shelter and supported placement; measured temperature/salinity; actual nitrogen cycling; real water/life-support verification; actual Saltwater Fish navigation; compatible starter care/price; destination/checks/atomic stocking and observation; compatible manual feeding, real appetite and living-resident inspection; verified completion. Adapt to existing six-menu destinations. Already satisfied real setup/ownership and documented prior individual feeding are recognized without duplicate purchases, emptying, replacing healthy livestock or recycling.

No Next/Back bypass, automatic purchase/setup, free fish, fabricated rewards, bacterial/chemistry edits or tutorial-driven time advance. Protect the existing fishless-finish shortcut while an active/paused guide is pinned; normal speed controls and offline progression remain. Store confirmation already stocks animals atomically: teach that actual workflow rather than inventing a second receiving fee or holding queue. Use the shared species-aware receiving/medical authority and existing Finance/Core transactions. Incoming group quantity is reflected consistently in group, adult-load and entity checks; ordinary diving remains one individual by default. Incoming checks keep all existing residents/treatment restrictions; readiness for an already-owned fish avoids counting that fish twice. The five-percent compatible-pair listing rule is unchanged and optional.

Recommendations use implemented care, volume, level, actual stock, price and compatibility rather than rarity. If no safe affordable starter is available, explain legitimate daily rotation/objective options; never reroll stock or invent a replacement species. Detailed state/targets/recovery: TUTORIAL_STATE_MACHINE.md. Persistence is defined in24.15; contextual UI in26.10.

The interactive saltwater tutorial must be fully traversable from start to finish without unintended loops, dead ends, contradictory instructions, obsolete navigation references, or progression softlocks. Every required UI target must be highlighted, each instruction must match the actual interface, and progression must reflect verified gameplay actions.

# 6. PLAYER PROGRESSION, COLLECTIONS & ACHIEVEMENTS

The player progresses through aquarium management, not merely through a traditional experience bar.

Progression may include:

- Player level.
- Fishkeeping experience.
- Aquarium prestige.
- Species discovery.
- Coral collection.
- Breeding success.
- Environmental care achievements.
- Tank expansion.
- Special equipment unlocks.
- Business reputation.
- Black-market discovery.

## 6.1 Progression Principles

Reward:

- Successful habitat creation.
- Healthy livestock.
- Stable water chemistry.
- Responsible breeding.
- Collection milestones.
- Aquarium improvements.
- Quest completion.

Avoid rewarding animal deaths or preventable suffering.

## 6.2 Unlock System

Advanced equipment, specialty livestock, and larger aquariums may require progression.

Essential basic care supplies must remain accessible.

Every unlock must have documented conditions.

---

## 6.3 Keeper Progress and Encyclopedia

Click the keeper-level badge to open Field Journal / Keeper Progress; never add a seventh sidebar entry. Show actual level, lifetime XP, XP to the next level, the 200-XP progress meter, recent retained quest-claim events, available objectives and existing unlock rules. Completed available quests grant 100 XP once, plus their listed credits. No invented feeding/inspection XP or automatic level bonus. Suggestions use real prerequisites and progress, with welfare-first guidance.

Species Encyclopedia has Saltwater and Freshwater habitat controls. Saltwater categories: Fish, Corals, Bottom Feeders, Other Marine Invertebrates. Freshwater: Fish, Plants, Bottom Feeders, Other Freshwater Livestock. Filter only existing definitions; honest empty categories, no freshwater expansion. Keep species art, care, diet, adult size, gallon minimum, temperament, habitat, stages, disease reference and breeding information independent of purchase access.



## 6.4 Authorized marine livestock registry v2.7

The permanent source `assets/expansion-v27/registry.json` contains exactly 38 new entries dated 2026-10-14: 28 fish, five named stony corals and five non-fish bottom dwellers. The duplicate/synonym audit found zero prior matches. Current runtime: 80 fish (69 marine, 11 protected freshwater), ten marine coral entries, five invertebrates; six freshwater plants unchanged. Do not count the 25 designer phenotypes, five ART ONLY fish or three PLANNED creatures as added biological species. `CURRENT_LIVESTOCK_CATALOG.md` records every exact name, ID, rarity, difficulty, status, date, art path and limit. New animal artwork remains unapproved; 12 sheets carry framing flags. Invertebrate eggs/planktonic larval art remain partial.

## 6.5 Approved v2.9 Marine Species

Exactly 25 fish, five corals and five non-fish bottom dwellers were approved with their rarities before implementation. Additive stable IDs, accepted-name/alias checks, original art, game care profiles, diets, habitat checks, health, value and saves are registered in assets/expansion-v29/registry.json. All three categories contain T5 and T6. Coleman’s shrimp is registered but acquisition-held: its obligatory fire-urchin host is unsupported. No 36th host species was invented. Earlier 38-entry registry, clownfish/designer identities and prior art-only subjects remain preserved. Current totals: 105 fish (94 marine/11 retained freshwater), 15 marine corals, 10 non-fish marine invertebrates, six retained freshwater plants. Rarity is not care difficulty or conservation status.

| Common / scientific name / stable ID | Category / approved rarity / care | Batch / status | Art |
|---|---|---|---|
| Flame angelfish / *Centropyge loriculus* / `centropyge-loriculus` | fish / Rare / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/centropyge-loriculus/atlas-v1.png); NOT APPROVED |
| Coral beauty angelfish / *Centropyge bispinosa* / `centropyge-bispinosa` | fish / Uncommon / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/centropyge-bispinosa/atlas-v1.png); NOT APPROVED |
| Cherub angelfish / *Centropyge argi* / `centropyge-argi` | fish / Uncommon / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/centropyge-argi/atlas-v1.png); NOT APPROVED |
| African flameback angelfish / *Centropyge acanthops* / `centropyge-acanthops` | fish / Rare / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/centropyge-acanthops/atlas-v1.png); NOT APPROVED |
| Potter's angelfish / *Centropyge potteri* / `centropyge-potteri` | fish / Ultra Rare / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/centropyge-potteri/atlas-v1.png); NOT APPROVED |
| Joculator angelfish / *Centropyge joculator* / `centropyge-joculator` | fish / Legendary / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/centropyge-joculator/atlas-v1.png); NOT APPROVED |
| Regal angelfish / *Pygoplites diacanthus* / `pygoplites-diacanthus` | fish / Ultra Rare / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/pygoplites-diacanthus/atlas-v1.png); NOT APPROVED |
| Orchid dottyback / *Pseudochromis fridmani* / `pseudochromis-fridmani` | fish / Common / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/pseudochromis-fridmani/atlas-v1.png); NOT APPROVED |
| Yellow longnose butterflyfish / *Forcipiger flavissimus* / `forcipiger-flavissimus` | fish / Rare / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/forcipiger-flavissimus/atlas-v1.png); NOT APPROVED |
| Pyramid butterflyfish / *Hemitaurichthys polylepis* / `hemitaurichthys-polylepis` | fish / Uncommon / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/hemitaurichthys-polylepis/atlas-v1.png); NOT APPROVED |
| Kole tang / *Ctenochaetus strigosus* / `ctenochaetus-strigosus` | fish / Rare / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/ctenochaetus-strigosus/atlas-v1.png); NOT APPROVED |
| Tomini tang / *Ctenochaetus tominiensis* / `ctenochaetus-tominiensis` | fish / Uncommon / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/ctenochaetus-tominiensis/atlas-v1.png); NOT APPROVED |
| Purple tang / *Zebrasoma xanthurum* / `zebrasoma-xanthurum` | fish / Very Rare / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/zebrasoma-xanthurum/atlas-v1.png); NOT APPROVED |
| Gem tang / *Zebrasoma gemmatum* / `zebrasoma-gemmatum` | fish / Legendary / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/zebrasoma-gemmatum/atlas-v1.png); NOT APPROVED |
| Achilles tang / *Acanthurus achilles* / `acanthurus-achilles` | fish / Ultra Rare / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/acanthurus-achilles/atlas-v1.png); NOT APPROVED |
| Foxface rabbitfish / *Siganus vulpinus* / `siganus-vulpinus` | fish / Uncommon / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/siganus-vulpinus/atlas-v1.png); NOT APPROVED |
| One-spot foxface / *Siganus unimaculatus* / `siganus-unimaculatus` | fish / Rare / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/siganus-unimaculatus/atlas-v1.png); NOT APPROVED |
| Midas blenny / *Ecsenius midas* / `ecsenius-midas` | fish / Uncommon / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/ecsenius-midas/atlas-v1.png); NOT APPROVED |
| Lawnmower blenny / *Salarias fasciatus* / `salarias-fasciatus` | fish / Common / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/salarias-fasciatus/atlas-v1.png); NOT APPROVED |
| Bicolor blenny / *Ecsenius bicolor* / `ecsenius-bicolor` | fish / Common / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/ecsenius-bicolor/atlas-v1.png); NOT APPROVED |
| Angular flasher wrasse / *Paracheilinus angulatus* / `paracheilinus-angulatus` | fish / Rare / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/paracheilinus-angulatus/atlas-v1.png); NOT APPROVED |
| Melanurus wrasse / *Halichoeres melanurus* / `halichoeres-melanurus` | fish / Uncommon / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/halichoeres-melanurus/atlas-v1.png); NOT APPROVED |
| Yellow wrasse / *Halichoeres chrysus* / `halichoeres-chrysus` | fish / Common / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/halichoeres-chrysus/atlas-v1.png); NOT APPROVED |
| Leopard wrasse / *Macropharyngodon meleagris* / `macropharyngodon-meleagris` | fish / Very Rare / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/macropharyngodon-meleagris/atlas-v1.png); NOT APPROVED |
| Bartlett's anthias / *Nemanthias bartlettorum* / `nemanthias-bartlettorum` | fish / Rare / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/nemanthias-bartlettorum/atlas-v1.png); NOT APPROVED |
| Duncan coral / *Duncanopsammia axifuga* / `duncanopsammia-axifuga` | coral / Common / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/duncanopsammia-axifuga/atlas-v1.png); NOT APPROVED |
| Candy cane coral / *Caulastraea furcata* / `caulastraea-furcata` | coral / Uncommon / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/caulastraea-furcata/atlas-v1.png); NOT APPROVED |
| Yellow scroll coral / *Turbinaria reniformis* / `turbinaria-reniformis` | coral / Very Rare / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/turbinaria-reniformis/atlas-v1.png); NOT APPROVED |
| Black sun coral / *Tubastraea micranthus* / `tubastraea-micranthus` | coral / Ultra Rare / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/tubastraea-micranthus/atlas-v1.png); NOT APPROVED |
| Rhizo coral / *Rhizotrochus typus* / `rhizotrochus-typus` | coral / Legendary / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/rhizotrochus-typus/atlas-v1.png); NOT APPROVED |
| Skunk cleaner shrimp / *Lysmata amboinensis* / `lysmata-amboinensis` | bottom_dweller / Common / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/lysmata-amboinensis/atlas-v1.png); NOT APPROVED |
| Fire shrimp / *Lysmata debelius* / `lysmata-debelius` | bottom_dweller / Very Rare / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/lysmata-debelius/atlas-v1.png); NOT APPROVED |
| Randall's pistol shrimp / *Alpheus randalli* / `alpheus-randalli` | bottom_dweller / Uncommon / Moderate | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/alpheus-randalli/atlas-v1.png); NOT APPROVED |
| Harlequin shrimp / *Hymenocera picta* / `hymenocera-picta` | bottom_dweller / Ultra Rare / Difficult | v2.9 / 2026-10-14 / IMPLEMENTED; game care calibration; art not user approved | [8 stage/state views](assets/expansion-v29/hymenocera-picta/atlas-v1.png); NOT APPROVED |
| Coleman's shrimp / *Periclimenes colemani* / `periclimenes-colemani` | bottom_dweller / Legendary / Difficult | v2.9 / 2026-10-14 / REGISTERED; ACQUISITION HELD pending required fire-urchin host support | [8 stage/state views](assets/expansion-v29/periclimenes-colemani/atlas-v1.png); NOT APPROVED |

## 6.6 First-time profile achievements — permanent

First-Time Species Achievement: A newly owned biological livestock species grants 50 XP and 50 AC once per player profile. First-Time Aquarium Size Achievement: First ownership of a new aquarium-size category grants 100 XP and 250 AC once per profile. Dive Destination Achievement: First successful expedition at each unique implemented mode/region destination grants 50 XP and 50 AC. Use canonical existing biological IDs, exact size catalog IDs and actual diving registry IDs, not designer morphs/stages, display rounding or observed/unreceived inventory. Successful hatching/receiving and other legitimate permanent ownership share one authority. New starter ownership counts; old reliable histories backfill without fabricated dates, payments or retroactive rewards. Stable award IDs, actual Finance keys, status and timestamps survive sell/rebuy, every route and reload. Pending capped awards wait safely. Detailed registry/objective scope: ACHIEVEMENT_OBJECTIVES.md; schema 24.14.

# 7. SALTWATER ROCKS, SAND & SUBSTRATE BIOLOGY

**This section is the primary home for substrate mechanics.**

The current expansion includes saltwater rock and sand only.

Do not use this update to introduce a new freshwater substrate catalog.

## 7.1 Sand Categories

Provide:

- Fiji Sand.
- Caribbean Sand.
- Hawaiian Sand.

Each must have:

- Unique item ID.
- Name.
- Pixel-art preview.
- Color and texture.
- Grain-size characteristics.
- Material composition.
- Bulk density.
- Price.
- Quantity.
- Tank placement compatibility.
- Inventory state.

Geographic names may define a product's origin and art appearance, but chemistry must follow the actual material properties.

## 7.2 Rock Categories

Provide:

- Fiji Rocks.
- Caribbean Rocks.
- Hawaiian Rocks.

Give each distinct:

- Sprite silhouettes.
- Texture.
- Color.
- Sizes.
- Habitat geometry.
- Caves and hiding opportunities.
- Placement options.
- Cost.

Support dry rock, prepared/cured live rock, and uncured rock as biologically distinct states when appropriate.

Live rock is biologically active aquarium material, not an animal requiring fish-like HP.

## 7.3 Rock Editing

Players must be able to:

- Purchase rocks.
- Place rocks.
- Move rocks.
- Rotate rocks where supported.
- Remove rocks.
- Rearrange habitat.
- Create hiding places.

Prevent invalid placements or objects passing through aquarium boundaries.

Warn when rock movement would create unsafe conditions for livestock.

## 7.4 Sand Depth

Allow player-selected substrate depth from:

**0 to 5 inches (12.7 cm maximum).**

Support 0.25-inch increments.

Show inches and centimeters.

Depth categories:

| Depth | Category |
|---|---|
| 0 in | Bare bottom |
| 0.25–1 in | Very shallow |
| 1–2 in | Shallow |
| 2–3 in | Moderate |
| 3–4 in | Deep |
| 4–5 in | Deep sand bed |

These are game classifications, not universal scientific thresholds.

## 7.5 Substrate Quantity

Determine required sand quantity from tank floor area, desired depth, and sand bulk density.

Calculate the sand's physical displacement.

Deeper substrate reduces effective water volume.

Purchasing and adding sand must consume the correct inventory quantity.

The player must not generate infinite substrate by editing depth.

## 7.6 Substrate Biology

Model relevant biological factors:

- Surface biofilms.
- Microbial colonization.
- Oxygen penetration.
- Organic accumulation.
- Nutrient processing.
- Possible denitrification.
- Anaerobic zones.
- Grain size.
- Maintenance and disturbance.

Deep sand beds are not automatically dangerous.

Risk depends on actual conditions.

## 7.7 Visible Sand Maturation

Substrate must visually change over time.

Possible growth:

- Brown/golden diatoms.
- Green algae.
- Cyanobacterial mats.
- Normal microbial biofilm.
- Organic deposits.

Cyanobacteria are not true algae.

Growth should depend on:

- Light intensity.
- Lighting duration.
- Nutrients.
- Silicate where relevant.
- Organic waste.
- Flow.
- Grazing organisms.
- Maintenance.
- Tank maturity.

Do not force every aquarium through the same bloom timeline.

## 7.8 Sand Maintenance

Players can:

- Inspect substrate.
- Remove accessible surface waste.
- Clean appropriate surface areas.
- Manage excessive growth.
- Adjust lighting.
- Adjust feeding and nutrients.
- Maintain suitable water movement.

Deep sand disturbance may create risk under unfavorable conditions.

Do not make every cleaning action catastrophic.

## 7.9 Substrate Inspector

Create a panel showing:

- Type.
- Depth.
- Approximate quantity.
- Effective water displacement.
- Surface algae coverage.
- Organic waste.
- General biological condition.
- Maintenance warnings.

Substrate must affect real gameplay and must not be purely decorative.

---

# 8. CORAL ECOSYSTEM, HEALTH & DEATH

**This section is the primary home for coral biology and coral death.**

## 8.1 Coral Categories

Saltwater coral groups:

1. Zoanthids and Mushrooms.
2. Small Polyp Stony Corals (SPS).
3. Large Polyp Stony Corals (LPS).
4. Soft Corals.

Define specific species or husbandry profiles within these broad categories.

## 8.2 Coral Attributes

Each coral should have:

- Unique identity.
- Species.
- Coral group.
- Age.
- Health.
- Growth stage.
- Size.
- Lighting requirement.
- Water flow requirement.
- Temperature tolerance.
- Salinity tolerance.
- Nutrient requirements.
- Relevant chemistry.
- Compatibility.
- Space requirements.
- Value.
- Propagation potential.

## 8.2.1 Individual Coral Inspector

Players can select a placed coral in the aquarium or its collection entry and inspect it like an individual fish.

Provide Overview and Care tabs showing its identity, group/profile, age, health, growth, coloration, value, propagation readiness, environmental requirements, current conditions, and actionable warnings.

Use the same environmental calculations in inspection and simulation. Provide repositioning, compatible transfer, propagation, and removal actions with appropriate validation.

## 8.3 Coral Interaction

Corals may:

- Grow.
- Extend and retract polyps.
- Respond to lighting.
- Respond to water movement.
- Compete for space.
- Damage neighboring corals through species-appropriate mechanisms.
- Recover from stress.
- Lose tissue.
- Die.

## 8.4 Coral Health States

Implement:

**Healthy:** Normal coloration, tissue, and polyp activity.

**Stressed:** Reduced extension, reduced growth, or other species-specific symptoms.

**Bleached:** Pale or white appearance due to loss or reduction of symbiotic algae/pigments in applicable corals.

**Tissue Loss:** Progressive loss of living tissue.

**Dead:** No viable coral tissue remains.

Bleached coral is not automatically dead.

Recovery must be possible under suitable conditions.

### Marine Coral Health Extension

Corals retain individual identity, age, health and mounting and additionally track living tissue, pigment/bleaching, polyp extension, nutrition, examined conditions and treatment history. Distinguish environmental stress, noninfectious bleaching, tissue loss, applicable suspected infectious syndromes and pest damage. Do not assign fish parasites to corals. Broad coral groups do not imply a verified taxon-specific diagnosis. Standard unexamined frags have fixed prices; introduced risk is assigned once at acquisition and saved. Living bleaching can recover; dead tissue has no living asset value. Select the existing appropriate health-state art without replacing artwork.

## 8.5 Death Artwork

Stony coral tissue death exposes a typically pale calcium carbonate skeleton.

The skeleton can:

- Remain physically present.
- Accumulate algae.
- Undergo bioerosion.
- Become structurally weakened.
- Break down over time.

Soft corals may collapse and decompose rather than leave equivalent stony skeletons.

## 8.6 Coral Decomposition

Dead organic tissue contributes to waste and bacterial oxygen demand.

Stony skeletons must not automatically generate large calcium spikes simply because coral tissue dies.

Calcium carbonate dissolution depends on relevant water chemistry and erosion conditions.

When dissolution occurs, it may influence calcium and alkalinity.

Use the central water chemistry engine for these effects.

---



## 8.7 Named coral expansion

Add Blastomussa wellsi, Micromussa lordhowensis, Cyphastrea serailia, Leptastrea purpurea and Pavona cactus as separate stable species IDs, preserving the five older broad coral groups. Apply stony-coral host restrictions, light/flow, footprint, clearance and player-selected supported rock/rack placement; no unsupported midwater purchase or silent placement. Store scientific identity, rarity, living tissue, bleaching versus death and central value. Existing fragmentation is reused; no sexual reproduction claim.

## 8.8 Coral fragging - implemented v3.1

Mature, healthy eligible marine corals may produce one independent mounted fragment per recovery cycle using owned species-appropriate equipment. Canonical definitions are AL.Update31.profiles; do not duplicate numeric profiles across unrelated systems. Kit, cutters and saw are reusable existing-inventory supplies; plugs and mounting supplies are consumable. Existing 100-AC Frag Rack is reused.

The actual individual inspector shows eligibility and reasons. Confirmation previews identity, rarity, maturity, health, anatomy/method, tools, eligible count, consumables, tissue/size loss, injury risk, recovery/establishment and parent/fragment asset value. The player chooses a valid existing supported mount. X/Escape/backdrop/Cancel creates no fragment. All handling is abstracted; no real cutting protocol is provided.

Minimum health is at least 85%, with stricter species thresholds. Immaturity, small size, disease/treatment, unsuitable water/light/flow, missing tools/consumables, no free mount/capacity or recovery block the operation. Legacy hammer wall/branch ambiguity and unverified nonphotosynthetic methods remain held. Successful fragments retain species, rarity and cloned genes, receive unique IDs, parent/root-clone identity, provenance, independent health/growth/death and establishment timers. Parents lose size/health/tissue and receive temporary stress/recovery. Refragging needs both regrowth and elapsed recovery. Valuation is shared with section 16; immediate parent-plus-child asset value cannot increase. Sales use the actual owned individual and section 19.6. No immediate adult fragment or flat cutting payout is allowed.

---

# 9. INDIVIDUAL FISH SIMULATION, AGING & DEATH

**This section is the primary home for fish biology, mortality, and corpse decomposition.**

Every fish is a persistent individual.

## 9.1 Fish Attributes

Required attributes:

| Attribute | Purpose |
|---|---|
| Unique ID | Identity |
| Species | Biological definition |
| Name | Player customization |
| Sex | Reproductive biology |
| Age | Biological age |
| Life stage | Fry, juvenile, adult, elderly |
| Expected lifespan | Typical longevity |
| Maximum lifespan | Individual biological limit |
| HP | Current health |
| Maximum HP | Health capacity |
| Hunger | Feeding requirement |
| Nutrition | Diet quality |
| Stress | Environmental/behavioral stress |
| Happiness | General welfare |
| Energy | Activity |
| Fertility | Reproduction |
| Genetics | Inherited traits |
| Growth | Development |
| Adult size | Mature physical dimensions |
| Temperament | Behavioral tendencies |
| Aggression | Conflict propensity |
| Disease state | Illness |
| Immunity | Resistance |
| Market value | Individual worth |
| Bioload | Environmental contribution |
| Oxygen demand | Respiratory requirement |
| Diet | Accepted foods |
| Habitat | Environmental needs |

## 9.2 Aging

Fish age with simulation time.

Life stages:

- Egg where applicable.
- Larva/fry.
- Juvenile.
- Adult.
- Elderly.
- Deceased.

Species have different lifespan distributions.

Aging affects fertility, growth, vulnerability, and behavior.

Mortality should follow species-specific age and health conditions rather than identical fixed birthdays.

## 9.3 Fish Health

Fish may suffer damage from:

- Ammonia.
- Nitrite.
- Oxygen deficiency.
- Temperature extremes.
- Incorrect salinity.
- Disease.
- Stress.
- Aggression.
- Predation.
- Starvation.
- Old age.
- Other biologically relevant environmental conditions.

Damage should depend on intensity, duration, species tolerance, and condition.

## 9.3.1 Current Marine Disease, Examination and Treatment

Implement a centralized data-driven system for marine ich, marine velvet, Brooklynellosis, flukes, selected bacterial syndromes, malnutrition and environmental injury. Define eligible hosts, cause/uncertainty, route, onset, symptoms, severity, contagiousness, damage, diagnosis confidence, treatment, contraindications and recovery. Some conditions are noncontagious. Fish disease must not be assigned to future shrimp, crabs, snails, starfish or urchins; those organisms need separately verified host profiles when authorized. No new invertebrate roster is authorized by this update.

Examination consumes diagnostic supplies and reveals confidence-qualified findings. Visual symptoms alone are not a definitive diagnosis; hidden carriage stays undisclosed until examination. Selected bacterial treatment requires a delayed follow-up and adequate confidence. Negative examinations do not guarantee freedom from disease. Quarantine uses independent prepared/cycled marine water, suitable capacity and coral mounts where applicable. Transfers preserve individual identity and history and revalidate water, social/territory and active-course restrictions.

Treatment consumes owned units exactly once and progresses over time. Effect depends on host, diagnosis, severity, duration, environment and saved product quality. Wrong treatment can fail or harm; there is no universal instant cure. Copper-inspired products require monitored bare fish-only adult quarantine and cannot be administered to reef coral/invertebrates. Use documented veterinary/husbandry references. Clinical concentrations and real-world recipes are not game controls; numeric rates and durations are explicitly accelerated game parameters. Severe disease uses existing fish mortality and coral death states, not a parallel death engine. Preserve the existing freshwater disease/treatment behavior unchanged.

## 9.4 Fish Death Animation

When a fish dies:

1. Swimming behavior ceases.
2. Fin and tail movements stop.
3. The body loses normal posture.
4. The fish rolls sideways or upside down.
5. Its movement responds to buoyancy and current.
6. Sinking bodies descend toward the substrate.
7. The body settles on a physical surface.

**The intended visual signature is an upside-down dead fish descending to the aquarium floor.**

However, some bodies may float or change buoyancy as decomposition progresses.

Model this rather than forcing physically impossible identical behavior.

## 9.5 Persistent Dead Fish

Dead fish remain in the tank unless removed, consumed, or sufficiently decomposed.

Store:

- Original fish identity.
- Species.
- Death time.
- Cause of death.
- Body mass.
- Position.
- Decomposition stage.
- Remaining organic mass.
- Buoyancy.

The player can select a corpse and remove it.

## 9.6 Decomposition States

**Recently Deceased**
- Recognizable coloration.
- Motionless.
- Little visible decomposition.

**Early Decomposition**
- Discoloration.
- Bacterial activity.
- Organic breakdown.

**Advanced Decomposition**
- Stronger visual deterioration.
- Potential bloating.
- Increased release of decomposing matter.

**Remains**
- Limited soft tissue.
- Possible skeletal remnants.
- Gradually declining organic effects.

## 9.7 Water Chemistry Effects

Corpse decomposition may:

- Increase organic waste.
- Increase ammonia.
- Increase bacterial oxygen demand.
- Affect downstream nitrite/nitrate production.
- Increase risks to surviving livestock.

Scale the effect with mass, temperature, filtration, oxygen, tank volume, and decay progress.

## 9.8 Death Notifications

Provide:

- Fish death alert.
- Cause where known.
- Corpse location.
- Removal action.
- Water contamination warning.

Maintain a permanent death history.

---



## 9.9 Separate non-fish residents

Thor amboinensis, Neopetrolisthes maculatus, Engina mendicaria, Conomurex luhuanus and Ciliopagurus strigatus live in a separate invertebrates array, never as generic fish. Persist identity, rarity, nutrition, condition, settled growth, age, death, treatment, position and transfer. Their crawling, tail sway, fan feeding and sand foraging use actual particles; leftovers/death pollute. Existing malnutrition/injury care is host-filtered through invertSupport; fish parasite/copper treatment is incompatible. This is a simplified game health model, not veterinary dosing. No planktonic larval rearing, egg art or reproduction is claimed.

## 9.10 Three-Second Livestock Outline

Selecting fish, corals, invertebrates or nurseries sets a performance-clock deadline exactly three real seconds after the latest selection. Reclicking resets it; another selection transfers it; switching aquariums clears it. Rendering reads the deadline, so game speed or pause cannot prolong it. The inspector remains open and usable after the outline expires.

## 9.11 Confirmed marine mortality and loss evidence - v3.5

Health at zero is terminal; temporary bleaching/stress at positive health is living. Stop living feeding, disease and treatment processing at death, and record a single confirmed loss through the existing mortality/recovery hook. No treatment may revive zero-health livestock in the same step. Record damaging contributions and the actual terminal cause where modeled, otherwise disclose cause undetermined. Never infer old causes from current normal water. Preserve full post-death recovery and the independent +50/+100 rewards; absence itself has no direct damage multiplier. See section 24.8 for bounded diagnostics and backup behavior.


## 9.12 Individual Reproductive Observations — v3.8

The existing livestock inspector displays reproductive role, maturity, partner, state, clutch, last spawn and recovery from section 15. Readiness/state refresh without resetting selection outlines, names or input focus. Apply only biologically relevant labels.

# 10. FISH AI, TEMPERAMENT & COMPATIBILITY

Fish behavior must be species-specific.

Personality traits may include:

- Peaceful.
- Shy.
- Curious.
- Active.
- Territorial.
- Aggressive.
- Predatory.
- Social.
- Nocturnal.
- Solitary.

Traits may overlap.

## 10.1 AI States

Implement:

- Explore.
- School.
- Feed.
- Rest.
- Hide.
- Defend territory.
- Chase.
- Flee.
- Hunt.
- Court mate.
- Protect offspring where applicable.

Use a state machine, utility AI, or efficient hybrid.

## 10.2 Compatibility

Evaluate:

- Adult size.
- Tank dimensions.
- Temperament.
- Territorial requirements.
- Predation.
- Diet.
- Schooling needs.
- Temperature.
- Salinity.
- pH.
- Habitat.
- Reef compatibility.

Provide four compatibility classifications:

- Compatible.
- Conditional.
- High Risk.
- Incompatible.

Explain the reasons.

## 10.3 Aggression

Aggressive fish can:

- Chase others.
- Cause stress.
- Damage fins.
- Injure tankmates.
- Kill other fish.

Aggression should be context-dependent.

Do not make aggressive fish attack continuously without meaningful triggers.

## 10.4 Predation

Predators may consume suitable smaller prey organisms based on species behavior, relative size, feeding state, and opportunity.

Predation should have meaningful nutritional and water chemistry consequences.

Fish must respect physical tank geometry and should not swim through solid rocks.

---

## 10.4 Natural Courtship Steering — v3.8

Use section 15 profile-specific nest preparation, circling and water-column spawning targets through the existing smooth velocity/movement system. No teleportation, tank-wide freeze or sprite/anatomy rewrite. Food seeking and severe stress take priority. Other fish continue swimming; small observation markers identify courting or mouthbrooding individuals.

# 11. EQUIPMENT, FILTRATION & MAINTENANCE

Equipment categories:

- Mechanical filters.
- Biological filtration.
- Heaters.
- Chillers.
- Air pumps.
- Circulation pumps.
- Protein skimmers.
- Aquarium lights.
- Automatic feeders.
- Monitoring sensors.
- Water treatment equipment.
- Reef dosing equipment.

## 11.1 Equipment Attributes

Each item includes:

- Name.
- Capacity.
- Efficiency.
- Purchase price.
- Maintenance cost.
- Electricity usage.
- Durability.
- Failure probability.
- Service interval.
- Compatibility.

## 11.2 Equipment Simulation

Equipment must influence aquarium conditions.

Examples:

- Heaters affect temperature.
- Pumps affect flow.
- Filters affect waste processing.
- Skimmers remove suitable waste components.
- Lighting influences photosynthetic organisms.
- Aeration influences gas exchange.

## 11.3 Failure and Maintenance

Equipment may become less efficient or fail.

Provide warnings and repair/replacement actions.

Failures should have understandable consequences rather than arbitrary instant livestock deaths.

---

## 11.4 Fixed marine heater levels and thermostat output - v3.6

Seven equipment levels span 5-20 / 20-75 / 75-250 / 250-1,000 / 1,000-3,000 / 3,000-7,500 / 7,500-15,000 US gallons. These are product levels, not new keeper-level gates. Each new heater has a stable model ID and fixed capacity equal to its range maximum in liters. Price follows the existing heater scale: ceil(110 x max(1,rated liters/150)); models share the existing heater stock and physical equipment type. Only one heater remains installed per tank. Recommend the smallest model that covers actual tank volume; allow purchase into storage, then reject installation into an undersized destination and explain eligible alternatives. Larger units still obey their thermostat. Existing equipment, stored gear and legacy auto-sized APIs retain old capacities and costs; do not retroactively assign or upgrade models. Transfers and inventory preserve fixed model/rating. Freshwater is not unlocked or redesigned.

Marine thermal calculations use ambient A=22+0.4*actual light output, heat-loss k=0.09*sqrt(75/volume) per game hour, passive temperature A+(T-A)*exp(-k*h), and gain=(1-exp(-k*h))/k. Maximum heater/chiller temperature rate is 8*k*operating-efficiency-adjusted capacity/volume (marine efficiency follows section 11.7). Request only the difference to setpoint divided by gain, clamped to available output; apply gain times delivered heating minus cooling. A thermostat cannot provide heat without installed, enabled, nonfailed capacity. Rated watts derive from the existing equipment calibration and duty; a separate electrical-grid/power supply is not modeled. Game wattage is not a clinical sizing guide. Equipment wear precedes output calculation as before. Freshwater retains the original thermal formula.

Main vitals show current water and installed-heater status. Individual installed-equipment inspection retains thermostat, fixed rating, condition and available/delivered output; Tank Care does not render a standalone Temperature Control panel. Normal post-loss chemistry never implies the heater operated previously. See the release report for original-code reproductions and thermal comparisons.


## 11.6 Aquarium-specific physical equipment — permanent

Every installed heater, chiller, filter, light, pump and other equipment instance has one persistent unique ID and operates only in the aquarium whose equipment array contains it. Profile ownership never grants shared life support. Installation, removal and transfer retain the exact ID, capacity, condition, model, modifications, enabled state and any individual thermostat. Removal requires a life-support warning and returns that same unit to physical storage; genuine consequences remain. Installation validates owned marine destination, fixed capacity, habitat and one slot per equipment type. Tank Care contains installed equipment and active maintenance; thermostat controls are on the individual installed heater/chiller. Current feeding forecasts remain under Food & Feeding; historical offline reports remain under Tank History → Reports. Standalone Temperature Control and Overnight Readiness panels are absent from Tank Care.

## 11.5 Equipment category metadata - permanent

Equipment Filtering: Every equipment product must have a stable category assignment, and the Equipment Store must support category filtering alongside text search. AL.EquipmentCatalog extends the central existing equipment/supply records, including all seven fixed heater levels and fragging tools/mounts. Offer only categories with actual products; do not invent monitoring equipment. Search and category form an intersection and clearing search retains category. Capacity, price, stock and safe destination validation are unchanged; show existing game ratings and disclose absent minimum/manufacturer ratings.

## 11.7 Long-term marine equipment reliability — permanent

**Aquarium equipment must have long-term, equipment-specific durability and reliability. Well-maintained equipment should generally last several in-game years, with gradual wear and reasonable maintenance requirements. Failure must not be driven by excessively fast or duplicated durability deductions.**

Keep physical condition, maintenance cleanliness and malfunction state independent. Use equipment-specific probabilistic multi-year exposure hazards, saved private randomness and actual powered game hours, never a fixed failure date or a per-render deduction. One game day remains 20 real minutes; active/offline use the same chronological simulation with overlap protection. Scheduled lights age only while on; stored or disabled equipment supplies no effects and accrues no powered wear. Legacy IDs, condition, modifications, records, thermostats, locations and unknown prior age remain intact. Never blanket-restore old gear.

Working equipment can recommend maintenance or gradually lose output; temporary faults need service, identified repairable faults need component repair, beyond-repair gear needs physical replacement and remains owned. Cleaning preserves long-term wear and established filter bacteria. Inspector actions and Tank History show factual saved events. Heater/chiller output remains capacity/setpoint/ambient driven; faulty gear cannot supply life support. Freshwater stays locked and its existing wear/biology is protected. Current parameters, distributions, maintenance intervals, exact calculations and real-time equivalents live in EQUIPMENT_DURABILITY_BALANCE_REPORT.md; maintenance instructions in EQUIPMENT_MAINTENANCE.md. Those profiles are game calibrations, not manufacturer guarantees. No new product, tariff, award or automatic compensation is authorized by this repair.

## 11.8 Equipment Maintenance and Replace Part — permanent

Equipment Service: Maintenance and Replace Part are distinct operations. Replacement parts cost their normal new-part catalog price. Cleaning preserves permanent wear, age and filter biology. Use only catalogued supported external parts, with exact rated inventory fit or one new-part payment, renew only that component to100%, preserve unrelated conditions/identity/age and record the actual event. Sealed/unlisted assemblies and zero-condition/beyond-repair chassis need whole-unit replacement; never invent serviceable sealed internals. The existing longevity model in 11.7 remains. EQUIPMENT_PART_CATALOG.md is the sole part/price home and EQUIPMENT_MAINTENANCE.md explains the UI. Supersedes the earlier generic discounted component repair and zero-chassis restoration.

# 12. WATER CHEMISTRY & ECOSYSTEM MODEL

**This section is the primary home for water chemistry.**

All other systems must call the same water chemistry engine rather than maintaining independent chemical calculations.

## 12.1 Primary Parameters

Simulate:

- Temperature.
- Salinity.
- pH.
- Total ammonia/ammonium and relevant toxic ammonia fraction.
- Nitrite.
- Nitrate.
- Dissolved oxygen.
- Alkalinity.
- Organic waste.
- Water clarity.

Saltwater reef parameters:

- Calcium.
- Magnesium.
- Phosphate.
- Relevant carbonate chemistry.

Use appropriate units and consistent calculation conventions.

## 12.2 Nitrogen Cycle

Waste generation and decay introduce ammonia.

Biological filtration converts ammonia through nitrite into nitrate.

Microbial populations must develop over time.

Processing capacity depends on environmental conditions and established biofilter biomass.

Track the effect of:
- Fish waste.
- Uneaten food.
- Dead organisms.
- Organic debris.
- Live rock.
- Biological filters.
- Water changes.
- Relevant biological nutrient processing.

## 12.3 Water Changes

Allow partial water changes.

Replacement water must have defined chemistry.

Water changes must calculate the actual effects of removing and replacing water.

Incorrect salinity or temperature can stress livestock.

## 12.4 Chemical Consequences

Fish corpses, dead coral tissue, algae growth, substrate conditions, equipment, and feeding must all influence the shared water model.

Never create arbitrary unrelated chemical spikes.

## 12.5 Tank Readiness

Readiness is calculated using:

- Water parameters.
- Biological processing capacity.
- Equipment.
- Environmental stability.
- Relevant species care requirements.

Report why stocking is safe or unsafe.

---

### Authoritative preparation lifecycle — v4.0.1 permanent

Use `AL.Preparation` for setup and preparation checks across stores, fish/coral/invertebrate receiving, eggs/offspring, quarantine, health, rendering and simulation. The existing `prepared` boolean records completed water preparation; `emptyDry` records physical absence of water. Prepared water implies filled water. Do not add a second persisted phase enum that can diverge from these flags. Derive four displayed stages: dry, filled but unprepared, prepared saltwater, prepared and cycled. Current cycled status additionally requires both established bacterial colonies and no active fishless cycle; preparation alone never certifies chemical safety or species compatibility.

The existing free Prepare water action includes filling and atomically sets `prepared=true`, `emptyDry=false`, recording preparation once. An optional Add water action only fills; it never prepares, cycles or grants livestock. Substrate, rocks and installed equipment are independent setup steps and cannot certify water preparation. Persist per-tank preparation observations, filled/prepared actions and completed cycles in a bounded `preparationHistory`; timestamps are actual game observations, never invented original setup dates.

Migration repairs a stale dry marker when saved `prepared=true` confirms prior completion. A lost false preparation flag can be restored from valid per-tank completed preparation/cycle history, or legacy completed fishless-cycle progress (the original simulation only advanced cycling after preparation). Honor later dry/filled history rather than reusing an earlier completed cycle. Default/normal water values, biomass, equipment, colony percentages, elapsed time and collection-wide preparation statistics alone are insufficient evidence. Never reset chemistry, bacteria, equipment, rocks, living/dead livestock, money or history to repair these flags; never award preparation or cycling a second time. Apply the same normalization at restore, action, save and simulation boundaries, including offline catch-up.

Keep the all-owned-aquarium compatibility table and report actual preparation state. A filled unprepared tank is not labeled dry. Species-specific minimum liters, temperature, salinity, pH, oxygen, toxins, habitat, light/flow, cycling, stocking and treatment/quarantine restrictions remain independent gates. A nominal 20-gal/75-L aquarium still fails a 30-US-gallon species minimum; a correctly prepared compatible 80-gal/300-L home may receive it. Actual physical liters and installed/effective equipment capacities do not change because of rounded nominal gallon labels.

Capacity audit: marine adult-load reservations count viable eggs/offspring once; nonviable eggs reserve no future adult load. Retained dead fish occupy existing physical/save entity slots until removed, while contributing no living adult load. Regular fish compatibility and diving tables use the same counts. Keep independent fish, coral and invertebrate array limits and existing equipment wear advisories; no blanket full-output equipment restriction is introduced. Freshwater biology and its lock remain unchanged.

## 12.6 Proportional Water-Change Cost Audit

Changed liters = actual saved volume × fraction. Preserve marine water ceil(changed L × 0.13 AC), freshwater water ceil(changed L × 0.04 AC) and existing freshwater conditioner biology. Marine salt is one dose per two changed liters, rounded up, minimum one. Smallest actual catalog tank is 20 L (ceil label 6 gal): 10% changes 2 L, costs 1 AC and one salt dose. Ocean Sanctuary 10% changes exactly 5,678.117676 L: 739 AC water + 2,840 salt doses. Salt packs are 35 AC/10 doses, so 284 packs cost 9,940 AC; combined replacement cost 10,679 AC before energy, food, medicine or repairs. No blanket treatment charge is invented. Preparation, clinical courses and maintenance retain their own rules. This exceeds the approved shell price; see BALANCE_REPORT.md. Never secretly change the 5,000-AC price.

# 13. DAY/NIGHT, TEMPERATURE & LIGHTING

Create an in-game clock.

Authoritative default pacing: **20 real minutes = one 24-hour game day**; 1 real second = 1.2 game minutes and 1 real minute = 72 game minutes at 1×. All existing biological, market, treatment, breeding, lighting and calendar systems use this same clock. Speeds 0/1/5/20, hidden-tab pause and modal/placement pause remain. Fractional steps split at midnight so checkpoints do not lose calendar minutes.

Allow configurable simulation speed.

Clock presentation is a saved 12 Hour / 24 Hour preference. Main clock, journal timestamps, feeder and lighting schedules and market-opening references use the centralized formatter. Durations remain elapsed game hours, never AM/PM clock times. Formatting cannot change biology or time progression.

## 13.1 Day/Night

Periods:

- Dawn.
- Day.
- Dusk.
- Night.

Different organisms respond differently to light cycles.

## 13.2 Lighting

Lighting characteristics:

- Intensity.
- Spectrum.
- Coverage.
- Schedule.
- Power usage.
- Heat contribution.

Lighting affects:
- Coral.
- Algae.
- Photosynthetic organisms.
- Fish activity.
- Temperature.

## 13.2.1 Player Light Controls and Visible Illumination

Provide a per-aquarium On / Off control and an Auto schedule option. An installed, working light visibly brightens the player's aquarium view, including fish, corals, plants, and hardscape. Switching it off visibly dims the tank. Manual On must work at night; Auto restores the programmed schedule.

Use shared lighting output for rendering and biological effects. Respect intensity, equipment condition, and saved per-tank settings.

## 13.3 Temperature

Tank temperature changes according to:

- Room conditions.
- Water volume.
- Heater/chiller capacity.
- Equipment heat.
- Environmental exchange.

Avoid instant unjustified changes.

## 13.4 Time and Lifespans

Use deliberate time scaling for:

- Incubation.
- Growth.
- Lifespan.
- Disease.
- Coral development.
- Equipment wear.

Do not blindly equate all biological timescales with one game clock if that makes progression impractical.

Document the chosen scaling.

---

# 14. FOOD, DIET & FEEDING

Food types:

- Flakes.
- Pellets.
- Sinking pellets.
- Algae wafers.
- Frozen food.
- Live food.
- Herbivore foods.
- Specialized predator food.
- Fry food.
- Coral foods.

Food attributes:

- Price.
- Quantity.
- Nutrition.
- Particle size.
- Protein.
- Fat.
- Plant content.
- Freshness.
- Decay characteristics.

Fish diets are species-specific.

Overfeeding increases organic waste.

Underfeeding reduces condition, health, and fertility.

Automatic feeders are implemented equipment; marine operation follows the current rules below. Freshwater feeding remains unchanged.

Food particles should be visible in the aquarium, with efficient graphics.

---

## 14.1 Authoritative marine feeding and calorie deprivation - v3.5

One MarineCare service supplies all marine hunger, stage, compatible diet, natural forage and calorie-deprivation formulas. Rate units are game hours. Adult fish metabolism m = clamp((0.7 + 0.3 x catalog activity) x size factor, 0.65, 1.6), size factor 1.15 below 6 cm, 0.8 above 20 cm, otherwise 1. Fast-feeding Purple Queen/Bartlett anthias use m=2.3; Blotched anthias 1.8. Hunger/hour is m for adults or 1.7m for immature fish. Shrimp use 0.8/hour; other benthic residents 0.5/hour. Nonphotosynthetic corals use 0.8/hour; photosynthetic corals do not use fish-like calorie hunger. These are gameplay calibrations, not clinical starvation tolerances.

With hunger H, nutrition N and stage fragility q (immature fish 1.7, young invertebrates 1.3, otherwise 1), calorie damage/hour = 0.5 x q x clamp(m,0.7,1.6) x clamp((H-85)/15,0,1) x clamp((45-N)/45,0,1). Nutrition change/hour for food-dependent residents is m x (-0.20 if H>70; +0.20 if H<45; -0.015 otherwise), plus actual consumed food benefits. Malnutrition remains a diagnosable condition without a second calorie damage path. Disease, chemistry, stress, age and predation remain separate genuine risks.

An installed, enabled, nonfailed feeder checks at 01:00, 05:00, 09:00, 13:00, 17:00 and 21:00, with a persisted slot guard. It selects the preferred ration only when compatible, otherwise actual stocked catalog-compatible food for each resident's current stage. Immature fish require fry; adult diets, specialist predators, benthic diets and nonphotosynthetic coral foods use existing catalog definitions. Sort hunger first and target particles so other diets cannot steal the intended meal. Consume one real inventory ration per bounded batch (40 particles, up to five per individual, 120 total tank particles). No stock or operating equipment means no invented meal. The schedule also works in coral-only tanks. Manual feeding remains available.

## 14.2 Finite natural foods and coral energy - v3.5

Grazeable algae begins at zero and grows only in mature lit habitat with actual grazers and dissolved nitrate/phosphate. Growth is bounded by available nutrients, water volume and grazer demand, and removes corresponding nutrients. Grazing consumes this biomass; compatible scavengers consume actual organic detritus above the retained minimum. Neither creates free unlimited food or substitutes for specialist tissue/plankton diets.

Photosynthetic corals require their existing light/nutrient/flow care and decline progressively if energy reserves are depleted. Feeding-dependent corals require consumed compatible food; hunger blocks generic healing. Only calcifying corals consume skeletal minerals, and concentration loss scales by 75 L / actual tank volume. Original biological care ranges, living bleaching states and frag recovery remain. The repair report includes exact formulas and a generated rate entry for every current marine species/stage.


# 15. BREEDING, GENETICS & EGGS

Breeding is a core long-term system.

## 15.1 Autonomous Reproductive Eligibility — permanent v3.8

**Fish breeding in Aquarium Life happens autonomously when biologically appropriate conditions are satisfied. The player does not manually initiate courtship through the Field Journal. Reproductive condition is visible through individual livestock inspection, and eggs or offspring appear in the same aquarium as their parents according to species-specific reproductive biology.**

No marine player action starts courtship. Once per saved game hour, mature same-species partners in the same tank evaluate health ≥85 HP, nutrition ≥75%, hunger ≤40, stress <25, energy ≥20, correct reproductive roles, no active disease/treatment, no other pairing/dependent brood and expired recovery. Designer/genetic holds remain. Prepared cycled water must meet species temperature/pH/salinity ranges, ammonia/nitrite ≤0.05 mg/L, nitrate ≤30 and oxygen ≥6; minimum tank volume applies. Require appropriate hard nest/cavity/cover, separated unoccupied territories, no nearby aggressive disturbance, real adult food and the correct stocked larval ration.

Reserve each potential offspring's adult load plus existing residents, invertebrates, nurseries, eggs and other courting cohorts. Breeding reservations fit within 80% of tank biological capacity, retaining 20% headroom. Preserve 250 fish/entity slots and at most 20 incubating/courting cohorts per tank. Store admissions honor the reservations. Courtship transfers its reservation to eggs once. Unsuitable conditions cancel courtship with 24 game hours of recovery, rather than silently producing eggs.

| Current profile | Courtship / spawning / incubation | Window and probability | Recovery / larval food |
|---|---|---|---|
| 26 eligible catalog clownfish | Protandrous pair, close swimming and hard-nest preparation for 6 game hours; attached clutch and male tending; 168 suitable incubation hours | 07:00–18:00; hourly 0.085 × minimum parental fertility | 336 game hours; fine fry food |
| Banggai cardinalfish | Compatible female/male circling for 8 hours; paternal internal mouthbrooding; 504 suitable hours; small juveniles at release | 06:00–18:00; hourly 0.070 × fertility | 720 hours; fine fry food |
| Chalk bass | Simultaneous hermaphrodites, no F/M requirement; 3-hour water-column display; pelagic drifting eggs; 24 suitable hours | 17:00–20:00; hourly 0.140 × fertility | 240 hours; cultured live plankton |
| Sharknose goby | Compatible female/male cavity preparation for 5 hours; demersal eggs and male tending; 144 suitable hours | 08:00–12:00; hourly 0.110 × fertility | 336 hours; fine fry food |

Every cohort represents two potential offspring, not real egg production. Probabilities, windows, durations and headroom are game calibrations. Egg-donor roles in the chalk-bass model alternate on later spawning events; legacy sex fields are not its sexual system. Clownfish larvae are immature nonbreeders, mature into the male role, and the largest mature male in a group without an established female undergoes a saved 14-day transition. Established females never reverse; only the dominant mature male and one established female breed. Readiness is not a daily guarantee. Complete biological sources, numerical loss rates and limitations are in BREEDING_RULES.md.

## 15.2 Egg Purchasing

Players may buy viable eggs from legitimate specialist stores or fictional black-market sources.

Each egg or clutch tracks:

- Species.
- Fertilization status.
- Age.
- Incubation progress.
- Viability.
- Parent genetics where known.
- Environmental requirements.
- Market value.

## 15.3 Natural Incubation and Survival

New natural clutches retain actual parent IDs, spawning tank/time/site, independent embryo genes/patterns and per-embryo survival. Fertilization chance is clamp(0.72 + 0.25 × minimum parental fertility, 0.72, 0.96). Preserve known Snowflake reference-model nonviability separately from unfertilized eggs. Never guarantee a survivor.

Suitable development adds dtHours × clamp(1.06 ** (temperature − 25), 0.75, 1.2). Unsafe water pauses development and raises egg-loss risk. Independently calibrated water, care, parental disease, hungry-neighbor predation and pelagic dispersal hazards use 1 − exp(−rate × dtHours); record the category that actually caused each simulated loss. Internal broods do not receive external predation. Missing/dead male carriers lose internal broods; lost nest support loses attached broods. A spawn does not receive the preceding simulation interval twice.

Hatching rechecks capacity and creates unique individual IDs in the parents' aquarium, copies the assigned embryo identities once and records outcomes/lineage. Zero survivors and failed spawning are valid recorded outcomes. Legacy and purchased broods keep their original simplified incubation/genetics rather than being reinterpreted as newly observed natural spawning. See BREEDING_RULES.md for the exact authoritative formulas.

## 15.4 Genetics

Possible traits:

- Color.
- Pattern.
- Size.
- Fin shape.
- Fertility.
- Growth tendency.
- Longevity predisposition.
- Disease resistance.
- Temperament modifiers.

Genetics must remain bounded and economically balanced.

## 15.5 Offspring, Nutrition and Responsible Sale

New natural larvae start at age 1 / baby-stage growth and use existing life-stage art; Banggai release small juveniles at 30% of species maturity, a developmental-age game calibration. None are instant adults. Persist unique IDs, parents, generation, appearance seeds, origin clutch and hatch time. Standard Ocellaris inheritance remains independent of survival. Other species receive ordinary catalog-pattern identities, not clownfish bar outcomes or Snowflake alleles.

Pelagic chalk-bass larvae accept cultured live plankton, represented by the marine-only plankton ration; ordinary fry food does not satisfy that saved requirement. Other supported larvae accept fine fry food. Feeders use actual compatible stock and switch to existing adult diets after juvenile growth and initial establishment; newly released Banggai juveniles retain fine fry food for seven game days. Hunger, nutrition, disease, predation and mortality remain active. Naturally bred offspring must reach juvenile growth and at least seven game days after hatch before sale; existing dealer welfare, budget and value checks remain. No automatic AC payout is added. Population growth remains limited by reservations, habitat, fertility, recovery, real nutrition and survival.

## 15.6 Persistent Marine Eggs and Observations

Clownfish and supported demersal clutches remain attached to a saved physical nest site, with local coordinates that follow a moved supporting rock. Pelagic eggs drift in the water column using saved age; they never become stationary rock clutches. Mouthbroods remain internal with a male carrier and no external egg pile. Existing egg/baby/juvenile artwork is reused; anatomy, eyes and orientation remain unchanged. Attached scene clusters remain 8 logical pixels and pelagic eggs 5; fixed magnified clusters and embryo detail show development instead of literal fivefold egg growth. Click visible eggs or use the journal/parent inspector to inspect internal broods.

Failed external clutches stay inspectable for one game day or until removed, add pollution once and never hatch. Supporting-rock removal remains blocked while an attached clutch exists. Values use the central valuation authority. New natural broods disclose their actual loss categories; legacy/purchased broods disclose their original simplified model.

The Field Journal Breeding & Eggs tab observes current pairs/readiness, actual spawning events, active clutches (species, parents, tank, date, count, progress and estimated suitable hours), offspring stages/survival/lineage, and completed/failed history. It has no manual marine mating trigger. Keep player-fragged coral clone lineage separate. Individual fish inspectors show role, maturity, current partner, Courtship, Gravid — Carrying Eggs only for the modeled egg donor, Preparing to Spawn, male mouthbrooding/tending, last spawn and recovery where applicable. Explain gravid with the beginner tooltip. Update observations live while keeping the inspector open after its selection outline expires at three seconds.

## 15.7 Persistent Pattern Inheritance — v2.6

Marine fish retain a versioned pattern identity: deterministic seed, phenotype, unknown or supported genotype, color traits, bounded pattern quality, variety and parent IDs. Assign each embryo independently at fertilization, then copy its identity at hatch. Rendering, turning, growth, illness, transfer and reload must never reroll these traits. Legacy fish retain their exact existing visible catalog patterns; no guessed genotype is assigned during migration.

Normal Ocellaris × Normal Ocellaris with no designer traits uses independent 85% standard three-bar / 10% minor natural / 4% misbar / 1% exceptional natural gameplay probabilities. These are not scientific mutation rates. Exceptional natural patterns never become named designer varieties or receive a rarity promotion. Only mid-body bar pixels are varied; approved eyes, silhouettes, orientation, framing and stage artwork remain intact.

New standard Ocellaris, Snowflake Ocellaris and Premium Snowflake retail stock can carry a clearly labeled **reference-line gameplay model**, separate from an individually measured genotype (which remains unknown). The supported gja5b model follows documented Snowflake evidence: Normal × Snowflake segregates 1:1; Snowflake × Snowflake segregates 1:2:1 at fertilization, with double-mutant embryos modeled as early nonviable. That lethality is an explicit inference from observed segregation, not demonstrated certainty for every commercial strain. Premium is a retail grade, not a separately inherited gene; viable designer offspring resolve to the approved ordinary Snowflake entry. Mixed supported grades may breed. Legacy unknown designer genotypes and other designer strains remain on a visible breeding hold rather than receiving invented probabilities. No cross-species hybrids are authorized. Evidence, scope and limits: RARITY_GENETICS_RESEARCH.md.

Use section 16 for rarity and centralized value, section 18 for purchased eggs and daily availability, and section 24 for persistence/offline progression.



## 15.8 Current Species Boundaries — v3.8

29 existing biological fish IDs have autonomous profiles: 26 purchase-eligible clownfish, Banggai, Chalk Bass and Sharknose Goby. The five existing specialist clownfish acquisition/art holds remain breeding holds. The older generic marine button/rules are superseded. Yellow/Blue Assessor, Greenbanded Goby and other incomplete profiles are held until reproductive role, habitat and larval-rearing details are reviewed; no assertion of biological impossibility is made. Historical v2.7 registry flags remain the earlier batch record; current runtime breedingSupported/breedingStatus/autonomousBreeding metadata is authoritative. Species/art/catalog counts and all unsupported designer holds remain unchanged.

Already saved and legitimately purchased species-identified Mystery Eggs retain their original calibrated model; they do not establish complete natural captive-culture feasibility. No new invertebrate egg/planktonic larval reproduction or freshwater biology is authorized. Coral fragmentation remains governed by section 8.8.

# 16. FISH RARITY, MARKET VALUE & AQUARIUM ASSET VALUE

Separate three concepts.

## 16.1 Fish Market Value

An individual creature's economic worth.

Factors:

- Species.
- Rarity.
- Age.
- Health.
- Genetics.
- Coloration.
- Fertility.
- Size.
- Market demand.
- Scarcity.
- Legal eligibility.

Example structure:

Fish Value = Base Species Value × Condition Modifier × Genetics Modifier × Demand Modifier × Rarity Modifier

Cap modifiers and validate all results.

## 16.2 Tank Biological Capacity

A normalized measure of biological load.

It depends on species characteristics and environmental conditions.

Physical space constraints are evaluated separately.

A fish with an acceptable waste load may still be unsuitable for the aquarium.

## 16.3 Aquarium Asset Value

Include the condition-adjusted value of:

- Tank.
- Equipment.
- Sand.
- Rock.
- Decorations.
- Coral.
- Fish.
- Other owned components.

Do not treat asset value as spendable cash.

---

## 16.4 Authoritative Current Livestock and Tank Valuation

Keep fixed retail purchase price, current individual asset value and actual dealer resale offer separate. Every owned fish/coral/bottom dweller has a persistent ID and a bounded current AC value. Consider biological/product baseline, stage, age/size, health, disease severity, genotype/designer traits, nutrition/condition, fertility and market eligibility. Age cannot increase value without limit; desirable juveniles or viable eggs can outrank ordinary adults. Coral frags grow into colonies; tissue, polyps and living bleaching affect value. Dead organisms have zero living value; any material value is a separate physical asset, never a living sale.

One valuation service owns formulas and all tank totals. Display Base Tank Value and Current Total Tank Value = shell current value + equipment + owned rock/substrate/racks + living livestock/eligible broods + decorations. Count benthic fish once and attached corals separately from their supports. Asset totals are not spendable credits. Recompute on authoritative ticks/actions and periodic UI updates, not each visual frame. Moving livestock transfers its current value; existing acclimation stress can legitimately change that value. Keep bounded meaningful value history and correct save/reload totals.

## 16.5 Future Verified Aquarium Leaderboard — Documentation Only

The long-term end-stage goal is an online ranking by verified aquarium asset value. Preserve stable IDs and transparent formulas, but future competition requires server-authoritative ownership, transactions and valuation. Never trust browser-local save values as verified online scores. No networking, cloud account, server, online score submission or functioning leaderboard is authorized now.

## 16.6 Central Six-Tier Livestock Rarity — Permanent

One AL.Rarity registry owns numeric ID, stable key, display name, icon, colors, order and description. Exactly six tiers:

| ID | Key | Name | Symbol | Colors |
|---|---|---|---|---|
| 1 | common | Common | Goldfish | White #FFFFFF |
| 2 | uncommon | Uncommon | Clownfish | Orange #F28B30 |
| 3 | rare | Rare | Lionfish | Red #ED4545 |
| 4 | very_rare | Very Rare | Arowana | Gold #D9A83F / silver #E2E8EE |
| 5 | ultra_rare | Ultra Rare | Great White Shark | Blue #368CE8 / white #FFFFFF |
| 6 | legendary | Legendary | Niger Triggerfish | Purple #9D52E8 / green #49C878 |

Use original 64×64 transparent pixel silhouette assets with stepped colors and accessible text. They represent collection rarity, never the actual animal's species. Goldfish/Arowana are symbols only. Every existing fish, coral, plant and applicable brood/embryo resolves valid rarity; missing/invalid classifications are data errors. Approved clownfish species and variety rarities remain unchanged. Other current assignments and trade references are documented in CURRENT_LIVESTOCK_CATALOG.md and RARITY_GENETICS_RESEARCH.md; scarcity is a game design choice, not conservation status.

Persist individual rarity across buying, transfer, growth, disease, recovery, breeding and death. Archive removed/deceased rarity and parentage in the bounded 100-entry lineage history. All store, inspector, collection, encyclopedia and breeding presentations use the same icon registry. Inspectors distinguish rarity, care difficulty, stage, age, health/disease, pattern/variety, quality, value and lineage; coral inspectors include size, light, flow and mounting requirements. Known eggs show their actual tier(s).

Pattern quality adds at most ±5% to the existing marine valuation factors. Health/disease continue affecting current value independently; rarity grants no immunity or retail repricing. Freshwater biology and valuation remain unchanged.



## 16.7 New livestock rarity and value

Use each central registry rarity exactly. New fish/corals/invertebrates reuse condition/stage/health-based asset value and bounded dealer offers. Non-fish bottom resident totals contribute once to tank value. Dead individuals have zero current value and retain immutable rarity in lineage history. New stock and specialist food prices are fixed game parameters. Rarity is a user-approved design assignment, not a conservation/trade status.

## 16.8 Local Leaderboard Preview

Leaderboard Preview is a compact main-sidebar entry directly above VIP Store and below The Dock Casino. It opens the existing single offline local marine comparison, ranked by current aquarium asset value excluding wallet and stored inventory. The previously authorized freshwater presentation remains a locked preview. No server, public submissions, invented players or online leaderboard is introduced.

# 17. ECONOMY, INCOME & MARKET BALANCING

Primary currency:

**Aquarium Credits (AC).**

Suggested starting balance:

5,000 AC for new local profiles. Existing wallets are never reset or topped up.

Balance against the chosen starting aquarium and its setup requirements.

## 17.1 Income

Possible sources:

- Fish sales.
- Eligible egg sales.
- Coral propagation.
- Quests.
- Breeding contracts.
- Limited buyer orders.
- Exhibitions.
- Collection milestones.
- Prestige-related rewards.

## 17.2 Expenses

Include:

- Fish.
- Tanks.
- Sand.
- Rock.
- Corals.
- Equipment.
- Food.
- Electricity.
- Water.
- Salt mix.
- Maintenance.
- Treatments.

## 17.3 Selling Restrictions

**Players must not buy and sell unlimited quantities continuously.**

Implement:

- Limited store buying budgets.
- Buyer demand.
- Market saturation.
- Stock rotation.
- Transaction cooldowns.
- Specialty buyers.
- Species eligibility.
- Price changes based on supply and demand.

Prevent purchasing an item and instantly reselling it repeatedly for guaranteed profit.

## 17.4 Fair Progression

Early-game players should have meaningful ways to recover economically.

Maintenance should matter but should not create unavoidable bankruptcy loops.

Rare specimens should be exciting but not automatically generate infinite profit.

## 17.5 Simulation Tests

Test 30-, 90-, and 365-day economic scenarios.

Evaluate:

- Starting progression.
- Expansion affordability.
- Food and equipment costs.
- Breeding profitability.
- Late-game wealth.
- Supply saturation.
- Black-market risk/reward.
- Exploit resistance.

Record findings in `BALANCE_REPORT.md`.

---

## 17.6 Daily Aquarium Care Reward

Grant **50 AC once per player per eligible game day**, separate from existing showcase income. Log exactly `Daily Aquarium Care Reward: +50 AC`. It is not per tank and does not grant XP. Require a full 1,440 observed game minutes and at least one living stocked aquarium/viable brood. Ignore empty tanks; all stocked aquariums must qualify. Check prepared/cycled water, running filtration, ammonia/nitrite at most 0.15 mg/L, oxygen at least 6 mg/L, species temperature/pH/salinity and existing coral care requirements. Deceased residents and severe unmanaged welfare crises block the day; ammonia/nitrite above 0.5 mg/L or oxygen below 4 are severe. Up to 30 game minutes of minor unsafe variation is tolerated; sustained unsafe time blocks the reward. Observe transactions as well as simulation steps so last-second cleanup cannot erase severe history. Explain nonqualification in the journal.

Persist observed time, unsafe time/reasons, severe flags, calendar day, last completed/claimed day and lifetime reward credits. Never pay an unobserved/migrated partial day, skipped day or already settled day. Accelerated speed uses the same calendar and requirements. Continuous catch-up evaluates the same tracked health history and pays 50 AC for each eligible day; there is no separate offline earning cap or absence penalty. See section 24. Continue performs catch-up once, then records the current save timestamp. Changing wall-clock time must not manufacture this reward. Local JSON backups are not tamper-proof or an online score authority.

## 17.7 Separate Livestock Survival Bonus - v3.4 permanent rule

Players earn 100 AC for every completed qualifying in-game day without a livestock death. After a livestock death, one full death-free in-game day must pass before reward eligibility can resume.

Qualification is account-wide: at least one eligible marine fish, living coral or bottom invertebrate throughout all 1,440 simulated minutes, no confirmed death in any active aquarium, successfully processed day and no previous payment. Recovery minutes are excluded from the qualification counter. Sick living organisms and living bleached corals are not confirmed deaths. Every new death resets recovery to its authoritative simulation time plus 1,440 minutes; duplicate corpse processing does not restart it. A full qualifying calendar day after recovery is required.

Keep +50 healthy-care qualification independent: 100 alone, 50 alone, or 150 when both qualify. Use the existing centralized finance service and permanent survival-day key. Receipts retain account/transaction IDs, actual game and PC payment times, qualifying day, period bounds and qualification status. Preserve all prior wallets and actual historical receipts without a top-up, clawback or retroactive payment. The additive policyVersion 2 migration excludes recovery time from older partial counters. Last-completed/paid day, death, recovery and earned totals persist.

20 real minutes remain one game day. Store, Deep Market, Journal, Equipment, Diving and other game windows keep simulation running; offline processing uses the same model and a consolidated earned/missed-day summary. Opening a window does not unlock freshwater. The implemented Dock Casino follows section 17.9 without changing reward qualification. Backward clock changes and saves cannot lower the processed offline timestamp; imports older than saved finance/timeline checkpoints remain refused. A completely offline client cannot authenticate intentional forward clock changes, but it simulates elapsed conditions and never pays the same qualifying day twice.

## 17.8 Authoritative AC ledger and Financial Overview - implemented v3.2

Every change to spendable Aquarium Credits must be captured by one authoritative, persisted, auditable financial transaction system. AL.Finance is that runtime service. Migration preserves each existing wallet as its opening balance without inventing historical receipts. New profiles start at 5,000 AC. Keep assets separate from spendable AC.

All actual purchases, maintenance/energy, water changes, expedition fees, livestock sales, quest rewards, healthy/survival rewards and research use the ledger. Atomic draft transactions prevent partial charges/ownership changes; durable keys prevent repeat receipts. Implemented casino wagers and returns use category Casino; never invent achievement or other cash entries for systems without actual payouts.

The existing header AC button opens Financial Overview: native keyboard activation, centered internal-scrolling modal, X/Escape/backdrop dismissal, actual balance, opening/income/expenses/net/closing reconciliation, day/7/30/all-time periods, newest-first category/direction/search filters, detailed receipts and twenty-entry pages. Actual daily charts and explicit older aggregates are supported. Account IDs, sequence, timing, category, source/destination, available species/individual/tank/dealer and resulting balance persist. See FINANCIAL_TRANSACTIONS.md for schema, archival and recovery limits. No account login/server is implied.

---

## 17.9 The Dock Casino — permanent rules version 2

Gold Fish Pair Payout: A pair pays exactly twice the original wager, including the returned stake. Label PAIR — 2×;100 AC wager deducts100, credits200 total, net+100. Preserve25×Gold triple,3×other triples,0loss and all Predator rules. js/casino-rules.js is the sole runtime authority and CASINO_RULES.md records exact enumeration: unchanged symbol odds plus corrected pair return give 152.2%theoretical return. Do not silently rebalance another combination to offset this authorized correction.

Casino Profile: Optional Spending Limit and Recent Casino Visits are located in The Dock Casino → Profile. Preserve old preferences/history and central enforcement across both games; no duplicate inline limit/history controls. Actual new session timestamps/summaries may be recorded, never invented for old visits. AL.Casino remains the sole account wager/settlement authority through atomic Core/Finance, with committed outcomes, once-only wager/payout keys, save-first UI commits, correct gross/net labels, pending-safe dismissal and local anti-replay heads. Existing settled version 1 records keep their actual old return; unresolved old draws upgrade explicitly to corrected rules without a second stake or reroll. Scope/biology, ongoing clock, healthy/survival rewards, no deposits/cash prizes/withdrawals and local-only saves remain. Casino is an account activity, including no-aquarium profiles; it never enables freshwater interaction.

# 18. STORES, INVENTORY & TRANSACTIONS

Store categories:

- Fish.
- Eggs.
- Corals.
- Sand.
- Rocks.
- Equipment.
- Food.
- Decorations.
- Medical supplies.
- Specialist materials.

Every item must have:

- ID.
- Name.
- Category.
- Description.
- Price.
- Stock quantity.
- Visual preview.
- Requirements.
- Availability conditions.

## 18.1 Purchase Validation

Purchasing must:

1. Check balance.
2. Check stock.
3. Check restrictions.
4. Check valid delivery or storage.
5. Deduct funds exactly once.
6. Transfer ownership.
7. Update stock.
8. Record transaction.
9. Save relevant state.

Prevent double-click duplication.

Store Quantity Rule: The Aquarium Store supports multi-quantity purchasing where appropriate, with clear unit price, quantity, and total cost display. Bulk purchasing must not bypass inventory, ownership, receiving, compatibility, or transaction integrity rules.

The shared StoreRules policy/quote validates integer quantities1–99, actual stock, wallet and inventory capacity inside the existing cloned Core.act transaction. Equipment, food packs, consumable supply packs, ordinary medical packs, rated service parts and ordinary rocks support bulk. One total debit/receipt; separate physical equipment/rock identities; original supply dose semantics. Multiple rocks enter ordinary Inventory for separate safe placement; one rock retains direct placement. Sand, decorations and mounted racks remain one installation/placement; reusable tools one owned tool; restricted medicine one quality-bearing batch. Livestock keep the existing resident-count compatibility system or individual assessment/placement, mystery roll and pair-offer authorities. No generic livestock bulk override. Details explain restrictions and show unit price, quantity and total. Deep Market equipment uses this same policy; access/hours remain enforced. Replay keys survive the recent100 transaction window through the existing financial receipt index. Optional receipt quantity/unitPrice/totalCost/itemIds preserve schema2 compatibility. See STORE_QUANTITY_RULES.md and UI_POLISH_QUANTITY_REPORT.md.


## 18.11 Equipment Inventory — physical storage only

Equipment → Inventory lists only the current profile’s actually owned, uninstalled and unplaced physical items. Installed equipment, placed hardscape/decorations/racks, consumed/sold items and living livestock are excluded. Existing reusable tools, care/mounting supplies, remaining medical batches and recovered diving rocks use their established storage authorities. Search and category filters combine; existing product pixel previews, quantities, fixed specifications and equipment condition are shown. Do not invent products or merge distinct equipment identities. Purchases debit/record once and create equipment in storage; the selected sizing aquarium remains selected and does not receive an automatic installation. Choose Install/Place, inspect all owned destinations and their exact rejection reasons, then confirm. Failed or duplicate actions cannot lose/duplicate items. Removed ordinary rocks, decorations and frag racks return with their original identity; recovered rocks return through the existing diving-rock inventory. Attached living corals and clutches block support removal. See EQUIPMENT_INVENTORY.md.

## 18.2 Living Inventory

Living fish and corals must occupy suitable tanks or modeled holding facilities.

Do not allow fish to survive indefinitely in ordinary item inventory.

## 18.3 Store UI

Use the shared centered store modal: desktop width 900–1100 pixels and height 75–85vh, visible aquarium backdrop, a compact fixed header with store title, selected aquarium name/dropdown, balance and top-right X in one region, and internal product scrolling. Keep Buy/Sell/Orders, habitat/category tabs and search compact with usable focus targets; maximize visible product area. Fit smaller screens without off-screen controls or page scrolling. Trap focus in the active dialog; Escape closes higher-priority details first, otherwise the store. Restore focus to the Store opener. Prevent duplicate modals and background interactions.

Exactly three main tabs: Saltwater, Freshwater and Deep Market. Start with Saltwater unless the current shopping session already chose a tab. Saltwater has Fish, Bottom Feeders, Corals, Rocks & Environment, Sand & Substrate, Equipment, Food & Supplies. Saltwater additionally has Medicine & Treatment. Freshwater retains its original seven categories with Plants instead of Corals; no new freshwater medicines or disease content are authorized. Deep Market has Fish, Bottom Feeders, Corals, Rocks & Environment, Eggs & Specimens, Special Equipment, Restricted Treatments. An empty freshwater category says exactly “Freshwater content is coming soon.” Preserve the locked near-black/slate palette and original UI.

Use actual existing product definitions, prices, stock and local artwork. Show habitat, care difficulty, designer/base identity and compatibility before purchase. Rocks/sand include Fiji, Caribbean and Hawaiian collections and 0–5 inch depth. Do not introduce fake products to fill empty categories. Recalculate equipment cost for the chosen destination. The existing level-4/discovery/20:00–04:00/containment/stock restrictions apply to Deep Market purchases.

## 18.4 Permanent Store Destination Aquarium

1. Opening or closing the store never changes the selected aquarium.
2. Switching Saltwater, Freshwater or Deep Market never changes it.
3. Display the current selected aquarium in the store header.
4. Check livestock compatibility against that aquarium at purchase time.
5. If incompatible, warn and require the player to explicitly choose an eligible owned aquarium before committing; never automatically select another.
6. Block unsafe animal placement, including harmful water conditions, predatory combinations, insufficient space and missing containment.
7. Deliver equipment, rock, sand and decorations to the explicit destination; consumable supplies go into their declared inventory.
8. Preserve selected aquarium after every completed purchase, including a new-tank purchase.
9. Closing and reopening the store retains the selection.
10. Save explicit destination choices and all placements correctly.

This rule covers all three tabs. Validate fresh state at commit, reserve stock, charge once, save once and roll back rejected transactions. Product browsing and aquarium selection are separate actions. Preserve the freshwater scope lock from section 2.5.

---

## 18.5 Fixed Retail Products and Legitimate Marine Medicines

Normal livestock prices are predetermined by species/variety, offered life stage and documented grade; reopening/reloading never randomizes them. Stock may change. Current normal fish products are standard adults, existing egg products are clutches, and corals are standard unexamined frags. Medicine & Treatment is a Saltwater subcategory while all three primary tabs and permanent destination rules remain. Fixed-price products include diagnostics, appropriate quarantine parasite/ciliate/fluke care, selected antibacterial care, nutritional support, isolated coral pest care and coral environmental recovery. Each has local artwork, eligible hosts, administration, duration, stock and restrictions. Copper and other unsafe treatments must not be falsely marked reef-safe. Consumable batches occupy medical inventory, not a livestock tank. Do not expand freshwater-specific medicine/disease systems.

## 18.6 Daily Saltwater Fish Store — Permanent

Exactly eight normal Saltwater → Fish listings: Common ×3, Uncommon ×3, Rare ×1, Mystery Egg ×1. Select verified implemented species or approved base-linked designer varieties of the assigned tier; never create species or fake cards. Avoid duplicate biological species when alternatives exist. If a future tier pool is too small, allow documented same-tier repeats. The full catalog is in Field Journal. Bottom-feeder and other existing categories retain their purpose.

Persist calendar day, selection, independent rotation RNG, unique listing IDs and remaining stock. Refresh once per completed game day, including every offline day; opening, closing and reloading never refresh. Sold-out listings remain visible. Fixed adult species/variety retail prices never change with rotation. Fish listing stock is max(4, social-group size), also bounded by existing shop stock. Purchases retain atomic validation, tokens and selected aquarium. Stale listing IDs reject before charging. Store browsing advances the clock; purchase details pause for review. Show “New Livestock Arrives In: MM:SS”, accounting for selected speed and displaying pause status. No per-second card rebuild.

## 18.7 Mystery Egg — Exact Independent Odds and Safe Purchase

Every independent roll uses Common 50%, Uncommon 25%, Rare 15%, Very Rare 7.5%, Ultra Rare 2%, Legendary 0.5%; no pity, guarantees or redistribution. Use a separate persisted 32-bit stream and rejection-sampled 10,000 buckets. Validate funds, stock, incubation capacity and a safe selected home with an eligible outcome in every tier before rolling. Assign the species, rarity, ID and embryos once, save them, and use existing species incubation and larval hatch development.

The intended reveal event is **successful purchase**; show this policy before confirmation. There is no concealed owned-result period in this build. Never expose a result before its purchase roll. Nominal product price is fixed at 600 AC, three daily eggs when available. The explicit v2.7 authorization populates all six marine rarity pools, removing the prior empty-pool hold. Retain the level-10 gate, three daily eggs, incubation capacity and compatibility with a safe selected destination for an eligible outcome in every tier before payment or RNG draw. Stock/roll/embryo identity persist exactly once. High-rarity additions enter Mystery pools without increasing the eight normal daily Fish slots, promoting existing clownfish or redistributing odds. Specialized food, coral-prey and isolated Boxfish checks apply. A new species authorization never waives those safety gates.



## 18.8 Permanent Normal-Store Upper-Rarity Restriction

Ordinary direct livestock sales are limited to Common, Uncommon and Rare across fish, coral and bottom dwellers. Tiers 4–6 require a supported Mystery Egg, Deep Market or eligible diving source. Never hatch coral/invertebrates from fish eggs. Reject bypass calls atomically. Keep the eight daily slots and exact independent Mystery odds in §§18.6–18.7. Regional acquisition/provenance is governed by §5.5.

## 18.9 Mystery Coral and Bottom-Dweller Egg

Saltwater Corals lists Mystery Coral (450 AC); Bottom Feeders lists Mystery Bottom-Dweller Egg (500 AC). Each has a separate persistent PRNG and independent exact T1–T6 odds 50/25/15/7.5/2/0.5%. All six implemented eligible tier pools and safe destinations are checked before charge or RNG use; missing tiers visibly hold purchase, never substitute or reweight. Three daily units each do not enlarge the eight Fish slots. Coral requires player-chosen supported mounting before purchase and resolves to a living frag. Bottom outcomes use a clearly labeled brooded/larval nursery abstraction for 48 suitable hours, then settle once as the same-ID small juvenile; viability/death/value/capacity reservations persist. Natural reproduction is not claimed. Production bottom purchase is content-held because the Legendary Coleman host specialist is not eligible. Conditional complete-pool QA verifies development without releasing that species. Outcomes, rarity rolls, identity, health, stage, provenance and mounts save without reroll.

## 18.10 Marine Research Center - implemented v3.3

All implemented saltwater fish species may be researched for exactly 5 AC per biological species per account. Research unlocks are permanent and provide verified biological, husbandry, behavioral, and medical information where evidence supports it; unavailable claims must be labeled unverified or incomplete. Research never grants livestock or overrides content holds.

Fish Research: Fish species research costs 5 AC per species per player account and is initiated from an owned living fish's existing inspector. Completed research remains available in the Species Encyclopedia after sale/death and costs nothing to view. Designer morphs share their parent's canonical biological species. Enforce living ownership at purchase, show confirmation before the atomic unlock/ledger deduction, block insufficient funds, and preserve all previous unlocks. Fictional creatures cannot be charged for biological research; coral and bottom-invertebrate paid research are not authorized.

The Saltwater Store Research subcategory and hidden navigation routes are removed. Encyclopedia cards distinguish research unlocked/not unlocked and incomplete data; unresearched entries say: "Select an owned fish in your aquarium to unlock its research for 5 AC." The existing report and central source-backed local data remain shared. Keep identification/classification, habitat/range, separately labeled game care, diet, temperament/compatibility, growth, breeding, medical guidance/risks, verified facts and separate rarity/difficulty game information. Unknown science stays labeled unavailable; no invented facts or medical predispositions. Preserve three-second selection highlight expiry without closing the inspector/report.

Current coverage: 94 marine records, 93 real researchable biological species, one fictional preview; zero fully verified dossiers, 93 incomplete, five with reviewed source annotations. This incomplete-content status is explicit before any optional paid unlock. Future content verification must update coverage rather than silently changing that claim. Progress uses the live denominator and local-account unlock timestamps. Optional Research Your First Fish guidance/achievement adds no AC reward. No research prerequisite is imposed on ordinary fish purchase.

---

## 18.12 Whole-Aquarium Sale — permanent

Whole-Aquarium Sale: Players may sell an entire aquarium and all sale-eligible physical contents through the Aquarium Store, using a single confirmed transaction. List owned aquariums/counts, exact itemized offers and blockers before a separate irreversible confirmation. Use AL.AquariumSale and authoritative valuation/quotes, never the total asset value as a guaranteed offer. Shell buyback uses50%current shell value; equipment/objects retain their physical condition-adjusted conventions, recovered rocks their existing quote, all ordinary resident sales the 60%Deep reference rule in19.6. Preserve animal eligibility, cumulative dealer budget/count limits, finite viable brood/nursery restrictions and receiving assignments. Uninstalled Inventory/parts and other tanks are excluded. Atomic removal/payout, durable tank-sale receipts, preserved discoveries/health/equipment/breeding/financial history, safe selection fallback and a fully saved empty ownership state prevent partial or duplicate sale. Exact rules/limitations: WHOLE_AQUARIUM_SALES.md.

## 18.13 Breeding Pair Store Opportunity — permanent

Breeding Pair Store Opportunity: Each eligible fish listing has a 5%chance to offer a biologically compatible breeding pair, fixed for the listing's legitimate refresh period. Use the existing supported breeding profiles across every eligible catalog fish; retain honest unsupported/hold explanations and designer inheritance holds. Save the listing draw and two mature, individually identified/conditioned/genetic fish before display; clicking or reloading cannot reroll. Quote the two legitimate retail/dealer specimen prices with no universal discount. Distinguish Compatible Breeding Pair from Established Bonded Pair; do not invent an established bond, spawning event or new reproductive protocol. Shared two-fish compatibility plus sequential receiving/medical checks must include combined adult load, actual water/habitat/quarantine and stock. An atomic confirmed purchase transfers those exact IDs, pays once, decrements actual stock, clears preview ownership and records a durable receipt. Autonomous biology and current store destination remain unchanged. Detailed rules: BREEDING_PAIR_OFFERS.md.

# 19. DEEP MARKET & DANGEROUS FICTIONAL CREATURES

Create a distinctive fictional underground trading system.

Content may include:

- Restricted fictional fish.
- Dangerous predators.
- Mutated specimens.
- Rare eggs.
- Experimental aquatic creatures.
- Extraordinary cosmetic strains.

## 19.1 Deep-Market Systems

Include:

- Dealer schedules.
- Rotating limited inventory.
- Reputation.
- Higher prices.
- Risk.
- Unreliable sellers.
- Special containment requirements.
- Fictional inspections or confiscation consequences.

## 19.2 Exceptional Creatures

Potential original species:

- Emberjaw Leviathan.
- Voidfin Specter.
- Glassfang Eel.
- Abyssal Crownfish.
- Prismheart Ray.

Each must have distinctive gameplay behavior and environmental requirements.

Do not make rare specimens valuable solely because of their price.

Use fictional legal rules where applicable, and research any real-world species restrictions before representing them as factual.

---

## 19.3 Saved Dealer Listings and Restricted Treatments

Marine dealer livestock prices may vary within bounds with rarity/scarcity, dealer behavior, condition and demand. Animals may be healthy, stressed, malnourished, infected or asymptomatic carriers; warnings communicate uncertainty without exposing exact hidden condition. Assign price/condition at listing creation, persist them, rotate only under designed inventory/dawn rules and reject stale listing submissions. Reload/open/close never rerolls a listing. Preserve limited stock, level/discovery/hours/containment and safe purchase validation. The protected pre-existing freshwater fictional specimen keeps its legacy biology and price path.

Restricted Treatments is a Deep Market subcategory for fictional unregulated/experimental/counterfeit/contaminated products. Save each listing's authenticity, contamination, effectiveness, intended hidden target and host compatibility, and copy exact quality into the acquired batch and active course. Outcomes may be helpful, unresolved or harmful. Diagnosis/assay can reveal qualified findings. No real-world adulteration recipe, toxic mixture or unsafe chemical formulation is part of the game. Ownership, inventory, payment and treatment actions remain atomic/idempotent.



## 19.4 Reputation and Diving Resale

Persist Deep Market reputation XP independently of Keeper XP. Level is 1 + floor(XP/100). Confirmed paid market purchases award at least 1 XP, then one per full 100 AC spent; cap at 25 per purchase and 50 per game day. Canceled, failed and duplicate transactions earn zero. Show level/XP/next-level and unlock notice. Diving-acquired individuals retain permanent provenance. The former Deep-only resale restriction is superseded by section 19.6: regular 60%-reference sales or condition/wanted/reputation-gated Deep sales. No dead specimen is sold as healthy. See §5.5 for capture/return rules.

## 19.5 Deep Market Display Name

Every current player-facing market heading, message, reputation description and buying/selling label uses Deep Market. Existing black internal IDs, legacy save fields, hidden saved dealer condition/medicine quality, prices, opening hours, reputation, inventory and diving resale remain compatible. Deep Market stays inside Aquarium Store. Eligible upper-tier new corals/invertebrates use saved dealer listings; ordinary direct livestock remains T1–T3.

## 19.6 Dealer buying, Wanted Livestock and stock integrity - implemented v3.1

Diving livestock may be sold to either regular Aquarium Store or Deep Market. For the same actual specimen, calculate one condition-sensitive Deep reference through the existing central valuation/diving offer service. Ordinary Aquarium Store livestock resale is exactly floor(reference x0.60) for every eligible origin, including diving, retail, captive breeding and established fragments, as explicitly required by the October20 update. This supersedes the earlier diving-only discount limitation. Current asset values and stock listing prices are never substituted for the actual dealer reference.

Deep Market buys only eligible specimens matching an active biological-ID Wanted Livestock request, at Reputation Level 5 or higher, during unlocked opening hours and within existing budget/daily limits. Identity matching never relies on editable display names. The separate daily wanted board persists requested condition, remaining quantity and expiry. Offline time advances requests and parent/fragment recovery without rerolling from reopening.

Wanted Livestock does not increase exactly four persisted rotating dealer livestock stock slots. Medicines/equipment are separate. Normal direct Tier 4-6 sales-to-player restrictions, eight normal Fish slots and independent Mystery odds remain. Purchased livestock, diving recoveries, bred fish and player fragments retain their origin, biological sale eligibility and shared ordinary 60%-reference quote. Every sale removes only the chosen eligible owned individual, records actual AC once and preserves the player's selected aquarium.

---

# 20. QUESTS, OBJECTIVES & UNLOCKABLES

Quests must be tied to actual player activities.

Categories:

- Tank setup.
- Water testing.
- Nitrogen cycling.
- Fish care.
- Food and feeding.
- Compatibility.
- Breeding.
- Coral care.
- Habitat construction.
- Economy.
- Collection.
- Black-market discovery.
- Aquarium prestige.
- Seasonal events.

## 20.1 Quest Data

Each quest has:

- ID.
- Name.
- Description.
- Objectives.
- Prerequisites.
- Progress.
- Rewards.
- Completion state.
- Unlock rules.

## 20.2 Sample Quests

**First Steps:** Prepare your first aquarium.

**Biological Balance:** Successfully establish nitrogen processing.

**Healthy Habitat:** Maintain stable conditions for a specified period.

**Reef Architect:** Create a suitable reef habitat.

**First Hatch:** Hatch a viable egg.

**Master Breeder:** Raise multiple eligible offspring.

**Hidden Dealer:** Discover the Deep Market.

**Aquarium Magnate:** Reach an aquarium asset-value milestone.

## 20.3 Rewards

Rewards may unlock:

- Larger tanks.
- New fish.
- Advanced equipment.
- Coral access.
- Decorations.
- Breeding tools.
- Specialist shops.
- Prestige items.

---

## 20.4 Additional objective registry — October20

Retain existing paid quest amounts and prerequisites. Add the 13 achievable optional progress goals in ACHIEVEMENT_OBJECTIVES.md across setup/cycling, meals, water changes, safe fragging, autonomous spawning, hatchlings, reef/deep exploration, equipment service/installation, size/species collection and safe water. Persist best progress/completion and show progress bars. They grant no unspecified extra AC or XP and require no harmful treatment. One-time paid achievements live only in 6.6.

# 21. VIP STORE — PREVIEW ONLY

The VIP system must be visible and attractive, but non-purchasable.

**No payment processing is allowed.**

VIP tiers:

1. Bronze.
2. Silver.
3. Gold.
4. Platinum.
5. Diamond.

## 21.1 VIP Content

Preview:

- Exclusive fish variants.
- Holiday fish cosmetics.
- Decorative coral variants.
- Aquarium backgrounds.
- Special decorations.
- Tank cosmetic effects.
- Prestige badges.
- Lighting themes.

## 21.2 VIP Visuals

Every VIP tier should have a polished illustrated preview panel.

Use actual locally bundled pixel-art artwork.

Do not use text-only placeholder VIP cards as final content.

Display:

**VIP PREVIEW — NOT AVAILABLE FOR PURCHASE**

No checkout, subscription activation, card fields, payment SDKs, or external purchase links.

VIP should focus primarily on cosmetic rewards, not overpowering economic advantages.

---

# 22. HOLIDAYS & LIMITED-TIME CONTENT

Create an event framework supporting:

- Halloween.
- Winter holidays.
- Valentine's Day.
- Spring event.
- Summer event.
- Game anniversary.

Possible rewards:

- Seasonal fish color variants.
- Special decorations.
- Event quests.
- Cosmetics.
- Backgrounds.
- Collection achievements.

Events must work offline and allow manual testing.

Previously obtained cosmetic rewards must not disappear when an event ends.

---

# 23. AQUARIUM CUSTOMIZATION & PLACEMENT

Players should have meaningful control over the appearance of each aquarium.

Customizable elements:

- Sand type.
- Sand depth.
- Rock arrangement.
- Coral placement.
- Background.
- Decorations.
- Equipment position where supported.
- Lighting.
- Aquarium name.

## 23.1 Placement System

Support:

- Select.
- Preview.
- Place.
- Move.
- Rotate where applicable.
- Remove.
- Cancel.
- Confirm.

Corals use a player-controlled preview followed by a click/tap to choose their horizontal and vertical position. Existing colonies can be repositioned. Support keyboard placement and Escape to cancel. Canceling a new purchase must not spend currency or consume stock; committing spends currency and transfers ownership exactly once. Do not move living coral into ordinary inventory during editing.

Coral mounting must correspond to visible physical support: permitted rock tops, stable sandbed bases/plugs, or a rack securely mounted to aquarium glass. Supported forms are category-specific. Reject unsupported open water, solid-rock interiors, overlapping bases and aquarium boundaries. Show Suitable, Conditional or Invalid using text plus green/yellow/red previews, with light, flow and stinging-clearance explanations. Full silhouette and mounting footprint need clearance; pale bleaching remains distinct from death.

Store surface type, support ID, local mount coordinates, orientation and footprint. Moving rock or rack carries its attached colonies; block support removal until colonies are relocated. Sand-depth edits must preserve or reject existing supports. Migration attaches only an unambiguous valid old position; otherwise retain the owned colony with an explicit relocation-required state, never delete it or continue rendering floating coral. Repositioning and transfer require valid destination surfaces, with health and identity preserved. The offline test scene must exercise rock tops, stable sandbed, back/side-glass racks, open water, rock interiors, overlap, boundaries, support edits, camera and save/load.

Save all placements and destination selections. Implement habitat chemistry only when separately authorized; this milestone's sand visuals do not claim new substrate chemistry.

Physical habitat geometry must be available to appropriate AI and compatibility systems.

During coral, rock and decoration placement, mouse wheel over the aquarium only changes normalized `z` depth: up toward 0 (back), down toward 1 (front). PageUp/PageDown provide keyboard alternatives. Arrow keys place horizontally/vertically; Enter commits, Escape cancels. Show depth and validity text with a crisp preview; do not intercept unrelated modal scrolling. Rock/decor purchases remain uncharged until commit. Use a stable bed perspective plane for rocks/decor, real painter ordering around fish and restrained depth lighting; no blur or full 3D system. Corals require an eligible support at the selected depth; wheel movement cannot float a colony. Move attached colonies and eggs with their support. Save z and infer deterministic middle/support depth for old objects. Z depth is distinct from sand thickness in inches.

## 23.2 Visual Layering

Maintain:

- Background.
- Rear hardscape.
- Corals/plants.
- Fish.
- Particles.
- Foreground objects.
- Glass and lighting effects.

The aquarium should remain the visual centerpiece.

---

# 24. LOCAL SAVE, LOAD & OFFLINE PROGRESSION

Use versioned local save data.

Support:

- Autosave.
- Manual save.
- JSON export.
- JSON import.
- Schema validation.
- Migration.
- Error recovery.

Save every relevant component, including:

- Player.
- Currency.
- Tank ownership.
- Water parameters.
- Sand type and depth.
- Rock placement.
- Biological substrate state.
- Algae.
- Equipment.
- Fish identities and genetics.
- Dead fish entities.
- Coral states, physical attachment support IDs/local coordinates and relocation-required ownership.
- Selected aquarium and explicit store destination choices.
- Designer variety linked to its biological species.
- Market inventory.
- Quests.
- Time.
- VIP previews.
- Achievements.

### Marine Health and Market Save Extension

Preserve schema-1/schema-2 compatibility with a versioned additive marine extension: individual health/history/course state, independent medical random stream, tank exposure, legitimate stock, medicine batches, saved dealer listings/quality and value history. Migration preserves existing IDs, wallet, health, art assignments and selected aquarium. Known current extensions missing or containing invalid hidden fields are rejected and protected rather than silently regenerated. Batch/listing IDs participate in unique-identity and counter validation. Import/export/reload must not duplicate purchases, doses or hidden outcomes.

## 24.1 Storage Limitations

Browser storage under `file://` can behave differently between browsers and contexts.

Detect whether persistence is available.

Notify the player if local persistence is restricted.

Allow export/import backups.

Never silently erase saves.

## 24.2 Continuous Offline Ecosystem — Permanent v2.5

Simulation continues while the player is away: 20 real minutes = 1,440 game minutes; 60 real minutes = three game days. Replace the former relaxed/capped modes. Active pause remains a player control; away time advances at 1× regardless of the active speed. Hidden-tab return and startup Continue use the same catch-up path.

Persist a simulation checkpoint distinct from savedAt. Replay all elapsed time through the existing deterministic ≤5-game-minute biological steps, without rendering missed frames. Batch asynchronously with progress UI and periodic durable checkpoints; an interrupted catch-up resumes from the last saved completed step. Never silently drop elapsed duration. Hunger, actual feeder inventory, water chemistry, disease/treatment, growth, eggs, equipment wear, mortality, utility costs, shop days and eligible care rewards use their existing models. Absence itself has no death penalty.

Negative clock deltas never reverse time or grant rewards; explain clock rollback. Invalid/nonfinite timestamps fail safely, and implausible pre-2000 checkpoints require recovery rather than a silently capped replay. Saves use additive ecosystemVersion 1, world ID, independent RNG states, daily stock and pattern/embryo records. A local timeline ledger rejects older same-world imports and repeated unchanged legacy import replays; legitimate recovery remains available. This is local safety bookkeeping, not secure anti-cheat. Clearing browser storage, editing JSON or moving to another device can bypass the ledger; authoritative online scoring remains deferred.

After catch-up show actual elapsed real time/game days, current credits, care rewards, number of residents that grew, hatched offspring, observed medical-event count, deaths (including colonies), equipment warnings and per-tank health/value. Do not infer unrecorded events. Unknown designer biology and existing simplified ecosystem limitations remain explicit.

---

## 24.3 Startup and Gameplay Migration

Valid save: “Welcome Back to Aquarium Life”, Continue and Start Over. Defer simulation, catch-up and autosaving until Continue. Restore actual aquariums, selected destination, identities, settings, time, currency and progression; never create a duplicate aquarium. First launch: “Welcome to Aquarium Life” and Start New Game, followed by the existing habitat choice. Start Over, including Settings reset, requires explicit Confirm Start Over / Cancel and offers export; opening or cancelling confirmation does not replace data. Corrupt saves stay locked with export/import/recovery/reset choices, never silently replaced. The startup gate requires a choice and cannot be dismissed into an unsaved placeholder game.

Keep schema 2 with additive `gameplayVersion: 1`: clock/display preferences, daily-care checkpoint, normalized object depth and brood aquarium identity. Migrate legacy data deterministically, retaining physical liters, IDs, wallet, selected aquarium, stocks, medical hidden state and asset ownership. An incomplete known gameplay extension is protected as invalid rather than silently resetting its care checkpoint. Validate ranges and brood-home consistency. No new accounts, server or online entitlement system.



## 24.4 Additive expansion migration

Expansion version 1 adds missing marine invertebrate arrays, ecosystem age, missing species stock, specialist-food inventory/stock and invertSupport stock once. Preserve existing fish/coral IDs, wallet, selected aquarium, daily listing IDs/calendar, RNG streams, disease histories and clown genetic profiles. Existing physical liters remain canonical; UI minimums use US gallons. Validate global animal IDs, host-specific health, stock, bounded toxin state and invertebrate positions/conditions. Persist invertebrateRng in offline checkpoints; include invertebrates in daily-care and offline-death/value summaries. No schema reset or freshwater species/biology expansion.



## 24.5 Expedition Persistence and Local Receipts

The v4.0 catch, sale, rock and concealed diving-egg fields are documented in DIVING_EXPANSION_SAVE_SCHEMA.md. Mystery encounter/reveal/recovery fields and transport journal schema 3 are additive under the existing save schema; see §5.5 and MYSTERY_DIVING_RULES.md. Diving extension version 1 adds optional migration of reputation, active trip, history, owned recovered rocks and divingRng. Preserve wallet, existing residents, selected aquarium, hidden dealer rolls, clock and genetics. Restored valid active trips resume with the saved oxygen and haul and no new charge. A local completion receipt marks a replayed older active snapshot failed/forfeited instead of awarding it again. Invalid transport/outcome/provenance/region/identity state fails validation. Active game, recovery, timeline and receipts remain localStorage on the player PC; JSON export/import remains local. See §5.5 and the existing offline import timeline guard.

## 24.6 v2.9 Local Persistence

Schema-2 saves receive the update29 survival and daily mystery extensions; the former passive tutorial is superseded by the interactive version2 extension in24.15, independent RNG fields and marine nursery arrays. Migration adds inventory/stock and required new market listings without rerolling existing listings, fish slots, old individuals or reputation. Validation rejects invalid extension states, duplicate identities and forged new mystery roll/rarity pairs. Selected aquarium remains authoritative through store opening/closing/tabs/purchases and save/load. Autosave/backup and user JSON export/import remain on the player’s PC in browser localStorage/downloads. Browser/site/profile storage is separate; export/import moves progress between origins. No cloud or server saves. build.py refreshes DIST and Pages ZIP; tests/package.py refreshes the source ZIP.

## 24.7 Financial, frag and research save extensions - v3.3

Persist additive finance v1, update31 v1 and research v1 objects without replacing old tank/livestock/world identities. Reusable tools/consumables use the existing inventory and stock. Persist lineage/provenance, genes, supported positions, health, size, creation/recovery/establishment times, wanted/stock state and permanent account research. Values recalculate from authoritative condition; never restore fictional rewards from asset growth.

Ledger import checks complement the existing local timeline and expedition receipts to reject older locally saved financial checkpoints. Account ledgers/unlocks do not mix. All main saves, recovery backups, receipts and exports remain on the player's PC/browser, with no backend. Browser storage is not cryptographic anti-cheat; explicitly report recovery/storage-origin limitations.

---

## 24.8 Overnight repair persistence and observations - v3.5 migration baseline

The permanent journal in 24.9 supersedes the prior 200-event-only retention policy. Existing v1 evidence remains valid; the gameplay ring is now a portable working set backed by dedicated records, not the complete permanent history.

Keep schema 2. Add marineCareVersion 1, per-marine-tank finite forage and autoFeedSlot, mortality version 1 with next sequence and at most 200 individual loss events per local account, and at most 160 water observations per tank at 12-game-hour spacing. Each death separately captures its actual step time and preceding interval, identity/species/tank, primary cause, hunger/nutrition/conditions, full water and bacterial state, equipment operating state/condition, compatible food stock, damaging contributions and recent recorded warnings. Five-game-minute steps bound death-time precision; old unobserved events remain unknown. Current recovered readings never overwrite historical evidence.

Before normal local-load migration, retain the original raw JSON once per existing account/world when storage permits. Settings exports this untouched snapshot; a storage failure offers current JSON backup before Continue. Existing deaths, account/world/individual IDs, selection, wallet, livestock assets and histories remain. No automatic recovery or compensation. Existing timeline/financial anti-replay restrictions still apply to old imports; browser storage is local and quota/origin dependent.

Synchronous and asynchronous catch-up share an in-flight ownership guard. Anchor intermediate real checkpoints to the return timestamp minus remaining duration, with micro-game-minute rounding on resume. Repeated completed timestamps apply no extra time, damage or rewards. Startup, hidden return and restored progression use the same ordered <=5-game-minute step. No elapsed-time cap, clock change, disabled ecosystem or separate offline starvation multiplier is permitted.


## 24.9 Permanent account mortality authority - v3.6

**Every livestock death must create one persistent, account-specific mortality record containing the livestock identity, actual simulation time, relevant health and environmental conditions, equipment status, and available evidence for the cause of death.** Extend AL.Mortality as the single authority shared by fish, corals, bottom residents and individually simulated immature/nursery stages. Log exactly one confirmed alive-to-dead transition through the existing survival-loss hook; logging creates no AC transaction or additional penalty. Aggregate unhatched brood viability remains its existing brood model, not invented individually identified animals.

Retain original v1 events without fabricating missing facts. New v2 events record canonical account/individual death IDs, species/common/scientific names where known, category/rarity/stage/age units, fatal-update health before/after and maximum, actual step/day/time, mapped real timestamp, capture timestamp, live/offline context/run, last observed healthy/consumed meal, hunger/nutrition/stress/conditions/medication, named modeled cause/contributors/certainty, exact water/target/volume/bacteria/bioload and equipment/model/output/food. Corals include tissue/bleaching/polyps/light/nutrients; benthic residents include diet/substrate. Record facts before decomposition/cleanup and never infer them from login water. Unknown evidence is explicitly unavailable and unknown causes display Unknown.

Keep per-tank 50 hourly samples (at least 48 preceding game hours after sufficient observation), 100 recent care events, and attach the dying individual's recent window to its permanent record. Track failures, controls, water changes, consumed food and health observations. Offline audits retain target/processed time, exact steps, initial/final operation, completion/error status and each event's run ID. Repeated return or replay must not duplicate a loss ID; all live/offline biology still uses the same fixed-step path.

Dedicated browser-local account-prefixed v2 journal keys hold individual event and offline-run records without automatic pruning. Gameplay carries the latest 200 durably archived events/20 runs plus every unpersisted pending record for portable saves and retry. Never evict an unpersisted item on quota failure; warn and offer full/selected JSON export and the existing game backup. Do not overwrite unreadable journal entries. Browser storage is finite and can be cleared externally; permanent means retained until the user/browser removes it, not unlimited cloud storage. Schema/keys/validation/import/export and legacy limits are documented in MORTALITY_LOG_SCHEMA.md. No credentials or whole-account gameplay objects belong in diagnostic exports.


## 24.10 Casino and inspector research persistence - v3.7

The additive casino extension preserves wallets, tanks and old research data. Account-bound sequences, committed draws, wager amounts, exact outcomes, receipt IDs, latest 100 rounds and cumulative totals survive save/load. Main saves commit before live UI wallet replacement. A saved pending round resumes to the same outcome. Local casino heads refuse stale snapshots, including losing settlements without a payout receipt; older raw files remain protected. Casino keys/ledger evidence are not pruned with the 100-round display history. No server, cross-device identity or tamper-proof offline guarantee is implied. Research unlocks remain permanent per canonical species/account and separate from ownership.

## 24.11 Autonomous Breeding Persistence — v3.8

Add root breeding v1 RNG/journal/archive, tank next-check/pair/reservation fields, individual role/maturity/mate/state/clutch/last-spawn/recovery/transition fields, natural clutch site/parents/embryo survival/losses, and hatchling origin/IDs/larval ration/minimum sale age. Keep schema 2 and legacy sex fields; roles are authoritative for hermaphrodites and immature clownfish. Migration is additive/idempotent and never rolls, spawns, hatches or assigns unknown genotypes. Validate all active references, species/roles/carriers/sites, unique IDs, reservations and viability; preserve historical parent IDs after sale/death. Detail schema: BREEDING_SAVE_SCHEMA.md.

Shared fixed steps and account/world checkpoints govern live, modal, diving, casino and offline progression. No elapsed interval is replayed on login. Retain up to 600 detailed reproductive records plus archived completed-cohort totals; the dashboard displays the latest 100. Preserve existing keeper, loss and coral histories. No backend, no cloud save and no player-data clearing; retain JSON export/import and the current 5 MB limit.

## 24.12 Physical inventory persistence — additive schema 2 extension

`itemLocationVersion: 1` adds missing legacy equipment IDs exactly once, preserving stored IDs and all original fields, and initializes empty `ownedObjects`. Never copy installed equipment into storage. Authoritative location is membership in one tank equipment/object array, `ownedEquipment`, `ownedObjects`, or the existing diving-rock inventory. Global identity validation spans installed equipment and every stored/placed entity. Duplicate IDs reject rather than silently deleting/reassigning items. Individual `temperatureTarget` is optional; legacy units retain the existing tank-target fallback. New purchases and transfers use the Core draft transaction, save validation, existing AC ledger and local save/export pipeline. See EQUIPMENT_INVENTORY_SAVE_SCHEMA.md.

## 24.13 Equipment reliability persistence — additive version 1

Persist per-instance reliability age/exposure, maintenance/component state, private RNG thresholds/cursors, processed interval and bounded factual history alongside the unchanged physical item and location. The profile ledger retains its event sequence through pruning. Idempotent migration adds only absent tracking; unknown legacy age is labeled unknown and old condition remains unchanged. Reject invalid extensions rather than rerolling them. See EQUIPMENT_RELIABILITY_SAVE_SCHEMA.md; physical locations remain section 24.12. Saving/export/import stays entirely local.

## 24.14 Coordinated economy persistence — additive schema 2 extensions

Persist profile progression records/objectives, exact rated part quantities/stock, whole-aquarium receipts/history and saved listing-bound pair offers/individuals/receipts. Preserve all original items, prices paid, IDs, conditions, genetics, old quests, reproduction records and wallet; no retroactive sanctuary charge or invented back-pay. Only actual supported new ownership earns future first-time rewards. Global identity validation includes reserved offered fish; paid offers clear previews. Empty tanks[]/selectedTank'' is valid after a confirmed last-tank sale; historical sold-tank breeding links require actual sale receipts. Versioned casino outcomes preserve settled old facts and explicitly upgrade unresolved draws. Fields, limits and migration: ECONOMY_UPDATE_SAVE_SCHEMA.md. Saves remain local to the player's browser/PC.

## 24.15 Interactive Tutorial Persistence - Version2

Keep main schema2 and update29.version1. Upgrade update29.tutorial to version2 with profile identity, status/current stable task/legacy numeric phase, verified milestones and sources/times, pinned aquarium and owned fish, actual listing, interaction/manual-feed signals, bounded past-tank references, completion acknowledgement and last200 sequenced diagnostic events. Old active guides enter interactive guidance and recognize real state. Old skipped/completed guides remain opted out; old Next clicks are not verified setup. Preserve legacy metadata; reject unsupported/malformed versions.

Only explicit guidance operations may mutate this state; arbitrary step/status completion writes reject. Skip/Restart require confirmation; restarting preserves real assets/rewards and bounded debug history. Switching aquariums does not retarget the guide. Explicit guide-tank selection does not change player selection. Missing/sold tanks and unavailable fish recover without creating, deleting or restoring animals/items. Validate profile, times, known steps/phase, marine species, bounded references/signals/events and complete evidence. Save diagnostics commit with the actual main local checkpoint; failed writes roll back provisional success events. Restoration observes saved state without processing elapsed time. Only the normal offline authority advances the ecosystem. See TUTORIAL_SAVE_SCHEMA.md.

Loop repair v4.2.1 retains the complete version2 extension and all physical/financial save data. Observe state idempotently with a reentrancy guard. Reopening the same fish listing preserves destination/check evidence; changing the actual listing invalidates only listing-specific review. Pending mouse/key observation jobs are fenced by profile and starting task, run after native event dispatch, and are never serialized as progress. A reload restores committed state and guides the player to reopen any uncommitted purchase; it never replays a payment or installation.

## 24.16 Graphics Preference Persistence

Additive `settings.graphics` under main schema2 stores the five presentation controls. Missing or invalid presentation choices normalize without resetting any player assets. Existing particle-off settings remain off. Keep20-second autosave and immediate transaction/tutorial/visibility checkpoints, validation, backups, anti-replay ledgers, and device-local JSON export/import. Never serialize decoded artwork. See PERFORMANCE_SETTINGS_SAVE_SCHEMA.md.

## 24.17 Store Quantity Persistence

Quantity purchasing retains main schema2 and all authoritative inventory arrays, stock maps, medicine batches, rated part stacks, local checkpoints and wallet sequence. New receipt metadata is additive; historic receipts are never rewritten. A rejected draft cannot partially charge or deliver. Successful purchases use existing immediate local saving and finance anti-rollback checks. No server/account service is introduced.

## 24.18 Production Protection and Existing Saves

Production transformation never encrypts or rewrites player profiles, local authentication, account IDs, financial replay keys or saved species/property names. Keep original local storage keys and schema2/tutorial2 migration/validation. Preserve the same DIST/index.html launch location and existing export/import behavior; moving between browser/site origins still uses explicit JSON backups. Source maps and private build records must not contain player data or ship in production. See section29.1.

# 25. GRAPHICS ENGINE, ANIMATION & PERFORMANCE

Use an efficient 2D rendering system suitable for offline browsers.

Canvas 2D is preferred unless another approach is clearly justified.

## 25.1 Rendering

Aquarium Life defaults to a maximum target of 60 FPS, with an optional 30 FPS performance mode. Rendering must be efficiently frame-paced, uncapped rendering is prohibited, and visual updates must remain independent of authoritative biological simulation. CPU, GPU and memory usage must be optimized so the game can operate alongside other desktop applications without unnecessary system-wide resource contention.

Use one authoritative gameplay scheduler, phase-preserving requestAnimationFrame deadlines and no visual catch-up bursts. Render only the selected visible aquarium; covered management views and hidden tabs stop its Canvas updates. Preserve16 authored frames, individual patterns, sharp eyes, facing, life stages and species-specific elapsed-time motion. Cache current static scenery with bounded ownership. Load native PNGs on demand; generated per-sheet scripts preserve file:// pixel reads without eager embedded banks. See PERFORMANCE_SYSTEM.md.

## 25.2 Simulation Performance

Preserve the existing5-game-minute simulation steps and20-real-minute day. Rendering cadence must not alter biology, equipment, rewards or clock speed. Bound foreground catch-up work per callback while retaining every pending minute; drain pending time before checkpoint saves. Keep pending time across transaction clones, reset on genuine profile/checkpoint restoration, and use existing offline catch-up once per hidden interval. Never count elapsed time twice or silently discard long frame gaps. Simulate other owned aquariums without drawing them.

## 25.3 Graphics & Performance Settings

Frame Rate:30FPS Performance Mode or60FPS Default. Graphics Quality:Low/Medium/High(default). Water Effects:Low/Medium/High(default). Decorative Particles:Off/Low/Full(default, respecting an older off preference). Background Resource Saving:on by default. These controls affect presentation only. No unlimited option or automatic particle-linked FPS. Add render scale only with measured benefit; preserve native pixel sharpness. Hidden tabs always stop drawing; resource saving also reduces covered-menu polling.

## 25.4 Profiling and Memory Acceptance

Profile actual game scenes before optimizing. Record repeatable before/after frame times, main-thread cost, heap and known pixel-cache budgets; state when physical GPU/Netflix/audio-sync measurements are unavailable. Verify small/mixed/dense/multiple-tank scenes, sustained navigation, local video, hidden/return accounting and virtual high-refresh cadence. Test full gameplay and every existing native sheet. Keep exact original art and biological/economic authorities. Cache ceilings must prevent unlimited accumulation while accommodating the active scene; stress-test final-size color/raster reuse to avoid eviction churn. See AQUARIUM_LIFE_PERFORMANCE_OPTIMIZATION_REPORT.md for executed results and limitations.

## 25.5 Permanent Post-Update Optimization Rule

Apply this rule automatically to every subsequent Aquarium Life development prompt and update, including features, fixes and UI changes. After implementation, complete a performance optimization and regression-testing pass before declaring the update finished. An update is not complete until its authorized feature work, post-implementation optimization pass and required validation are genuinely finished and reported.

### Phase 1 — Implement

- Complete the requested changes while preserving existing systems and save compatibility.
- Avoid unnecessary processing and duplicate code.

### Phase 2 — Profile

- Check CPU, GPU and memory usage where measurable; explicitly identify unavailable measurements.
- Inspect rendering and animation performance.
- Identify unnecessary calculations, event listeners, timers, asset loading and DOM updates.
- Check for memory leaks and duplicate simulation, rendering or animation loops.

### Phase 3 — Re-optimize

- Optimize new performance bottlenecks introduced by the update.
- Improve inefficient existing code encountered within the affected systems.
- Avoid unnecessary asset loading, redraws and repeated calculations.
- Preserve gameplay accuracy, approved pixel-art quality and visual sharpness.

### Phase 4 — Validate

- Confirm the game defaults to a capped 60 FPS target and preserves optional 30 FPS performance mode. Never introduce uncapped rendering.
- Verify authoritative biological simulation remains independent of rendering FPS. Do not change biological accuracy solely to improve FPS.
- Test newly implemented features and affected existing systems.
- Check save/load integrity, offline operation and compatibility with existing player saves.
- Confirm no significant performance regression, unnecessary background rendering, duplicate loops or avoidable memory leaks were introduced.
- Test multitasking performance where possible and report what was actually tested.

### Phase 5 — Report

Every implementation completion report must include a **Performance & Optimization** section showing:

- Performance issues discovered.
- Optimizations performed.
- Before-and-after measurements where available, with the measured scenario and method.
- Regression tests completed and their actual results.
- Remaining performance concerns and unavailable or unperformed measurements/tests.

Do not invent benchmark results or claim unperformed tests passed. Default target 60 FPS, optional 30 FPS mode, no uncapped rendering, no unnecessary background rendering, no duplicate simulation/animation loops, no avoidable memory leaks, no degradation of approved pixel art, no biological accuracy changes merely for FPS, fully offline operation and existing player saves are permanent requirements.

Only end an implementation report with the exact standalone line `Done With Edits` after the authorized feature work, optimization pass and required validation are genuinely complete. If any required work remains, report it accurately and do not use that completion line. Section 31.3 applies this gate to all future editing completion reports.

---

# 26. UI/UX TECHNICAL SPECIFICATION

## 26.1 UI Inspiration

Use the friendly, inviting atmosphere of classic aquarium-management games, especially the general experience associated with Happy Aquarium.

The interface must remain original.

## 26.2 Locked Colors

```css
:root {
  --app-bg: #080B10;
  --panel: #34465C;
  --panel-dark: #253449;
  --panel-raised: #40566E;
  --border: #536B83;
  --text: #F3F7FC;
  --text-muted: #B9C9D9;
  --accent: #45D6D0;
  --selection: #68A9F4;
  --warning: #F4B860;
  --danger: #EF7075;
  --success: #79D6A3;
}
```

UI Background Rule: Aquarium Life uses a black base UI background with a subtle low-contrast dark-grey fish-scale texture overlay. The fish-scale pattern points downward and is used only in general interface background areas, not inside the aquarium tank scene.

UI Preservation Rule: UI polish updates should refine the current Aquarium Life layout and styling rather than redesigning the game into a different interface structure.

The page and sidebar use a black#000 base with one static64×32 SVG tile: hanging quadratic scallops, dark-grey#16191d strokes at45% opacity. No animation, JavaScript drawing or aquarium Canvas overlay. Panels remain solid slate-blue, with protected navigation labels/buttons. Utility/header alignment, panel padding, field spacing, selected/hover/focus states and store button heights retain the familiar layout. See UI_SPECIFICATION.md and UI_POLISH_QUANTITY_REPORT.md.

Slate-blue UI panels.

Clean typography and consistent spacing.

## 26.3 Main Layout - Six Main Destinations

The aquarium uses six permanent sidebar entries, in this order:

1. Aquariums.
2. Aquarium Store.
3. Field Journal.
4. Tank Care.
5. The Dock Casino.
6. Settings.

Remove unfinished VIP/premium and leaderboard previews from normal navigation. Keep local aquarium asset comparison in My Aquariums. Development art-review links belong in collapsed Settings > Developer tools, with no main-scene footer links or premium-currency placeholder. Older preview routes safely return to My Aquariums; existing saves and unused legacy data are retained. This authorized simplification supersedes the earlier eight-window layout.

Every entry opens a titled native modal above the aquarium with a top-right X, Escape, focus trapping/restoration, internal scrolling and small-screen support. Only one primary window is open; details/confirmation dialogs may be secondary. A window selector allows replacing the primary modal without stacking. Remember each primary sub-tab during the session. Opening/closing does not reset simulation, aquarium selection or livestock positions. Existing modal pause rules remain; canvas animation continues.

The main page must fit the viewport without page scrolling. Pair the compact selected-aquarium dropdown with + New aquarium in the shared information-column header grid; align the button right edge to the unchanged Water & Wellbeing panel edge, accounting for native scrollbar spacing. Keep control heights/styles, readable option names, native focus, responsive stacking and no overflow. Never resize the information panel merely to align controls. Remove the decorative slogan and three bottom care cards; retain their functions in Tank Care/Store menus.  Right summaries use internal scroll areas; on narrow screens they form a horizontally scrolling strip with internal vertical regions. The aquarium stays at its original 2:1 ratio and is fitted to available height, never cropped or stretched. The live TOTAL AQUARIUM VALUE button is centered in the header above water and opens Aquariums / Tank Value. Use AL.Valuation, count eligible installed assets once and keep base shell value distinct from total assets and wallet credits. Individual inspectors retain current values.

## 26.4 Management Window Destinations

| Primary window | Sections and ownership |
|---|---|
| Aquariums | My Aquariums with local asset comparison; New Aquarium; Tank Setup; Tank Value; Water Laboratory |
| Aquarium Store | Buy, Sell, Orders; exactly Saltwater / Freshwater / Deep Market primary habitat tabs; unchanged 8 / 7 / 7 product subcategories; fish rehoming and eligible coral/plant cutting sales; existing night-market discovery, stock, listing prices and risks |
| Field Journal | Livestock Collection; Species Encyclopedia; Progress (Keeper Level / Objectives / Achievements); Tank History; Disease & Treatment Guide |
| Tank Care | Installed Equipment; Feeding; Water Changes; Lighting; Coral Fragging; Inventory. Equipment uses a category dropdown. Routine service and inspection remain visible; transfers/removal are in Inspect. |
| The Dock Casino | Gold Fish; Predator & Prey; Profile (the sole spending-limit editor and Recent Casino Visits/history); rules/confirmation/gross-net results; pending-safe dismissal |
| Settings | Display mode, 12/24-hour clock, offline/visual preferences, saving, export/import, recovery and confirmed new story |

Former sidebar features remain functional at these destinations. Fish Collection is Livestock Collection and includes owned fish, benthic fish, coral, existing plants and broods; filters cover species, life stage, collection status, care difficulty, rarity and aquarium. Historical fish discovery uses the existing discovered list; plant/coral historical discovery is not invented. Encyclopedia notes are independent of purchase permissions and expose existing names/scientific-name availability, diet, care, compatibility, behavior, calibrated growth/lifespan, stages, disease guide and art. Guides never reveal an individual's hidden infection.

All player-created initial aquariums and purchased aquariums start empty and dry. Do not clear existing saves. Setup uses installed equipment, water preparation and fishless cycling; dry aquariums cannot perform normal water changes. Equipment locations and installation follow sections 11.6 and 18.11; profile storage never supplies equipment effects. Purchases remain Store transactions. The water-change page previews the actual established formula and uses real funds/inventory; chemistry is not duplicated.

Marine egg presentation and persistence follow section 15.6. The inspector remains available from the scene and Field Journal / Livestock Collection.

### Livestock and Tank Value/Medical UI

Clicking fish/coral/bottom dwellers shows species/name, age/stage, health, nutrition/stress, examined or suspected condition, relevant genes/variety, Current Value in AC and eligible dealer offer. An optional breakdown explains bounded modifiers without automatically naming an unexamined infection. Marine controls provide examination, diagnosis/treatment, appropriate quarantine transfer, medical inventory, stopping a course and restricted-batch assay. Close inspectors/resume time to advance courses. Coral Overview/Care tabs and physical placement stay functional.

Show the clickable, centered TOTAL AQUARIUM VALUE above the water display. Its breakdown distinguishes base shell, equipment, fish/viable broods, corals, bottom dwellers, rocks/substrate/racks and decorations, with bounded meaningful history. All stores retain the selected aquarium unless the player explicitly chooses another. Medical stock is shared inventory with declared marine eligibility, never an automatic unsafe livestock destination.

### Display Mode Controls

Windowed exits the Fullscreen API when active. Fullscreen requests browser fullscreen from a user gesture. Borderless Fullscreen uses the same browser-managed equivalent, explicitly labeled; true OS borderless/exclusive display and resolution control require a future desktop wrapper. Save the preferred mode, report actual fullscreen state separately, handle denial/unavailable APIs gracefully, and never auto-enter after reload or fake unsupported success. Existing six-window navigation and top-right close controls remain; startup follows the protected gate in section 24.3.

### Simplified routine care and warnings

Tank Care uses existing transactions, receiving, feeding, equipment and water-change authorities. Keep the laboratory for detailed readings; route water changes to one preview/confirmation in Tank Care. Feed forecasts show both game days and real hours at 1x using the unchanged twenty-minute day. Progress groups existing views without new rewards or save fields; legacy achievement/objective/keeper shortcuts still work. Tutorial destinations follow the same routes.

Main warnings show three distinct notes and an expandable complete remainder; preserve every underlying reason and the actual resident-specific status. Expanded notes survive refresh. Keep deaths, equipment faults and unsafe temperatures visible. Summaries do not change chemistry, biology, eligibility or simulation. Device age/components/intervals remain available in collapsed details while Maintenance and Replace Part remain accessible. Empty ownership, physical storage and local export/import remain functional.

### Installed-equipment inspection and history

The individual inspector shows physical condition, maintenance status, tracked/unknown service age, efficiency, component wear, eligible maintenance/repair actions and warnings; never a promised failure date. Device history follows the same physical ID and historical tank assignment. Tank History holds maintenance/failure events. Keep standalone Temperature Control and Overnight Readiness panels removed; use individual installed heater/chiller controls for thermostats. Mechanics belong only in section 11.7.

## 26.5 Interface States

Support:

- Hover.
- Selected.
- Disabled.
- Warning.
- Critical.
- Loading.
- Empty.
- Success.
- Error.

Use actionable notifications.

## 26.6 Accessibility

Implement:

- Keyboard navigation.
- Focus visibility.
- Escape-to-close dialogs.
- Labeled controls.
- Readable font sizes.
- Clear contrast.
- Optional reduced motion.
- Adjustable UI scale.

Prioritize usability over unnecessary visual decoration.

---



## 26.7 Diving and Modal Interaction

Keep the six main sidebar windows. Add the Ocean Diving button beside Keeper Level; follow §5.5 for shared-modal planning/play/results and protected dismissal. Ordinary X/Escape/backdrop behavior remains, with no click-through. Provide responsive keyboard/mouse/direction-button input, sticky oxygen HUD, explicit safe receivers and visible reputation and the two dealer sale routes in section 19.6. Capacities follow §4.5.

## 26.8 Breeding Observation UI — v3.8

Breeding & Eggs is not a top-level Field Journal tab. Redirect old breeding navigation to Livestock Collection. Individual inspectors retain reproductive roles, pair/partner, courtship, gravid/brooding state and readiness. Collection retains eggs, clutches and baby/juvenile residents; Tank History retains the read-only breeding observations, archived lineage, spawning/hatching/failure records and coral frag lineage. Encyclopedia retains species reproduction. No manual Begin Courtship action is introduced; all autonomous biology, saved records and genetics remain intact. Old journal leaderboard routes redirect to the relocated main-sidebar interface.

## 26.9 Resident status, heater visibility and Livestock Deaths - v3.6

Use actual current species temperature ranges for every living resident/brood, with coral care ranges where no individual catalog temperature exists. Empty or entirely deceased aquariums must not display biological balance; label them explicitly. General marine chemistry is a separate statement and cannot override resident safety or explain old deaths. Current heater state/rating/condition is visible in vitals, with full output and thermostat details in Equipment.

Field Journal > Tank History > Livestock Deaths provides chronological account records, aquarium/species/cause/real-date/game-day/live-offline filters, latest-offline-period filtering, clickable full reports, Export Mortality Log and Export Selected Death Report. Reports disclose old missing evidence, sampled versus exact death-step water, and model-based causal confidence. Welcome Back states the actual newly recorded loss count and offers View Death Reports. Keep detailed debugging inside these interfaces, not permanently over the aquarium scene.


## 26.10 Contextual Tutorial UI

Use stable DOM IDs/data attributes and actual element bounds, clipped to scroll containers, for a reusable spotlight and concise anchored tooltip. Track native dialogs, tabs, dynamic listings, dropdowns, resizing, scrolling and pinned aquarium context. The target remains readable and clickable: dim regions/ring have no pointer interception. Hide a stale ring when its target is offscreen. A missing target shows a recoverable explanation, logs once per unresolved context and retains Pause/Skip. Required controls change only after real state/evidence verifies the action. Focus target scrolls/focuses, never clicks or performs a purchase.

Guide controls: Pause, Resume, Restart with confirmation, Skip with confirmation, View Current Objective and completion review/dismiss. Native confirmation must preserve underlying pending Store/details content. Settings contains current objective, deliberate guide-aquarium selection, verified milestones and Local Debug Log/export. Keep visible outlines and text, native keyboard interaction/focus, readable contrast, static reduced-motion presentation, no rapid reactions and existing modal-close behavior. The old corner panel and Next/Back controls are removed.

For an empty aquarium, highlight its visible setup button rather than the canvas underneath the empty-tank panel. During the initial viewing task that button opens Tank Setup for review; filling/preparation remain separate real actions. Discover purchase markers, destination forms and thermostats only inside an open details dialog, never retained hidden HTML. Read trusted click/change/key outcomes in a later task after native navigation and modal handlers finish. Keep instructions aligned with actual visible labels and explain resource/stock blockers. Opt-in developer diagnostics detect repeated unresolved routes and record previous/current task, event, validation and prerequisite results without advancing or resetting guidance.

# 27. QUALITY ASSURANCE & AUTOMATED TESTING

Test the entire game systematically.

## 27.1 Startup and Saving

- Offline startup.
- Direct `index.html` loading.
- New game creation.
- Save/load.
- Export/import.
- Corrupt-save handling.

## 27.2 Tank Setup

- New tanks start empty.
- Sand purchasing.
- Depth from 0 to 5 inches.
- Correct substrate quantities.
- Water filling.
- Equipment installation.
- Nitrogen cycling.
- Livestock readiness.

## 27.3 Water and Substrate

- Waste increases appropriate chemical components.
- Filtration processes waste.
- Water changes alter chemistry correctly.
- Diatoms/algae develop under suitable conditions.
- Substrate changes affect effective water volume.
- Deep-bed risks are condition-dependent.

## 27.4 Fish

- Species data valid.
- Health changes.
- Feeding.
- Aging.
- Aggression.
- Predation.
- Compatibility.
- Death.
- Corpse motion.
- Corpse persistence.
- Decomposition.
- Corpse removal.
- Water chemistry interactions.

## 27.5 Corals

- Growth.
- Light requirements.
- Flow requirements.
- Bleaching.
- Recovery.
- Tissue loss.
- Death.
- Skeleton persistence.
- Conditional dissolution.
- Chemical consequences.

## 27.6 Economy

- No negative balance.
- No purchase duplication.
- No sell/buy exploit.
- Limited market budgets.
- Stock persistence.
- Bounded valuations.
- Quest reward validation.

Store destination invariants require regression checks across all three tabs, purchase holds, alternative eligibility, stale water conditions, repeated submissions, explicit product destinations, JSON round trips, focus/Escape/backdrop behavior and responsive sizes. Validate every clownfish entry, shared early-stage mapping, eye anchoring, left/right transforms, animation frames and protected freshwater baselines.

### Marine Economy/Disease Update Acceptance

Verify fixed normal retail/medicine pricing; designed dealer rotation; exact saved hidden condition/quality; individual and tank values; growth, illness, recovery and death effects; no double counting; value transfers; symptoms/progression; appropriate diagnosis and timed effective/ineffective/harmful treatment; reef contraindications; quarantine identity; stock/dose/payment idempotency and save/import protection. Repeat existing UI/art/eye/direction/coral/light/offline regressions and protected freshwater comparisons. Record measured 30/90/365-day marine scenarios without extrapolating one scenario to the entire roster.

## 27.7 UI and VIP

- Every functional control performs its action.
- Proper error states.
- Keyboard use.
- VIP images display.
- VIP cannot initiate payments.
- Graphics remain visually consistent.

Run automated tests where possible and document any manual checks still required.

---

## 27.10 Six-Window Main UI Acceptance

Verify all 40 checks in [UI_OVERHAUL_REPORT.md](UI_OVERHAUL_REPORT.md), including exact sidebar order, all X/Escape/focus paths, state preservation, internal scrolling, centered live values and breakdown routing, moved store/journal/equipment features, preview-only VIP, marine egg placement/development/selection/save/hatching, protected fish eye/direction artwork and freshwater definitions/biology, offline execution and resizing. Automated fixtures must explicitly furnish newly purchased dry tanks before testing occupied-tank biology. Do not mark new interface behavior passed from obsolete inline-management selectors.

---

## 27.11 Gameplay v2.4 Acceptance

Verify all 45 user checks in GAMEPLAY_UPDATE_REPORT.md with executable evidence: units/physical capacities, habitat encyclopedia scope, supported marine egg placement/persistence/hatching, real keeper XP, store geometry/destination safety, fullscreen success/denial, clock formats/schedules, depth/support/wheel isolation, authoritative time, exactly-once care policy and startup/corrupt-save safety. Preserve freshwater data/art hashes and the exact ten-day biology comparison. Rerun system/store, six-window UI, marine health/value/economy and existing directional artwork regressions. Do not claim a new full-project audit or tests of unsupported browsers/desktop wrappers.

## 27.12 Rarity / Genetics / Offline Acceptance

Run tests/browser_qa.py chrome --ecosystem and edge --ecosystem with networking disabled and dedicated profiles. Verify sections 15–18 and 24 together with existing core, coral, economy and disease regressions. Test repeatable 200,000-roll rarity/natural-pattern samples with statistical tolerance; reference-line segregation, persistent embryos, safe purchase stock, negative clocks, complete catch-up, async/sync agreement, real Continue/import controls, unchanged protected freshwater biology, colored icon previews and narrow layouts. Record actual results and content-held paths honestly in ECOSYSTEM_UPDATE_REPORT.md. Never claim the unpopulated Mystery Egg pool was successfully sold.



## 27.13 v2.7 acceptance evidence

The dated LIVESTOCK_EXPANSION_REPORT.md maps all 24 requested acceptance items to actual results. Each browser passed 362 expansion checks and 7,583 artwork regression checks, zero failures. Evidence covers all 38 inspectors/rarities, save round trips, categories, actual six-tier Mystery purchases/hatching, safe destinations, coral support, non-fish treatment/transfer/death/offline value, eight daily slots, ten-day unchanged freshwater replay, 145 protected file hashes and no gameplay HTTP requests. Do not present older hardcoded roster/empty-pool milestone suites as current passes. Firefox and unsupported biological features were not tested as implemented.



## 27.14 Diving v2.8 Acceptance

Use tests/diving_checks.js, diving_resale_checks.js and the real browser diving_qa.py for all 38 requested checks. Run both Chrome and Edge offline, actual keyboard/left-click/modal/reload flows, safe recovery and resale, and the continued aquarium clock. Rerun expansion, art and deployed DIST/local-save regression suites. Record actual passed/failed/not-run results and evidence in DIVING_UPDATE_REPORT.md; do not infer an unrun suite passed.

## 27.15 v2.9 Acceptance Evidence

Actual executed results and the complete original 35-item checklist are mapped in V29_UPDATE_REPORT.md and tests/update29-evidence. Browser checks exercise actual New Game/tutorial controls, reload, selection deadline, store destination, safe coral placement, held bottom product, both leaderboard views, achievement claim and large-tank purchase. Model checks exercise genuine fixed-step/offline rewards, all coral CDF boundaries, nursery persistence/settlement, recovery, transaction rollback and save validation. Source art was visually inspected but is NOT user approved; artwork approval is still an explicit limit. Earlier 31 major sections, protected art/definitions and retained freshwater replay are verified. Report only actual tests; historical failures/fixture adjustments are disclosed.

## 27.16 Overnight mortality acceptance - v3.5

Archive immutable original modules before edits and compare identical initial states using original and repaired code. Run 12 scenarios at 20 real minutes, 2, 8, 12 and 24 hours, including a matched continuous five-minute-step reference for every case. Provisioned marine mixed, juvenile, coral-only, photosynthetic, grazing/scavenging and multiple-tank cases must survive this fixture matrix; risk cases retain genuine starvation/disease/environmental losses with captured causes. Test overlapping catch-up, repeated return, interrupted save/reload, legacy dead entities, pre-repair preservation/export, historical water, finite food and exact rewards. Verify the protected freshwater replay and art/data hashes, local browser saves, responsive diagnostics and final DIST repository-subpath loading. Report actual counts and remaining limitations in OVERNIGHT_REPAIR_REPORT.md, never assert the player's unavailable historical save was individually diagnosed.


## 27.17 Heater and permanent-log acceptance - v3.6

Test original versus repaired thermal code with proper/oversized/weak/disabled/failed/missing heaters and real food shortage at 8/12/24 real hours; compare every repaired state with identical continuous progression. Verify seven actual heater products through the 15,000-gallon catalog aquarium, prices, fixed ratings, undersized rejection, transfers, model validation and legacy preservation. Verify individually simulated death categories/stages, exact heat target versus actual water, health/hunger/conditions, at least 48-hour evidence windows, per-account history, more than 200 losses, storage failure/retry, exports, repeated return/reload and offline error audits. Preserve all existing overnight, financial/recovery, freshwater replay, gameplay, diving and hosted local-save acceptance. Report measured counts and limitations; do not claim the unavailable player's old save was diagnosed.


## 27.18 Autonomous Breeding Acceptance — v3.8

Verify every authorized 27-case category: automatic eligible breeding, manual-control removal, maturity/species/roles, visible smooth movement, gravid/internal brooding, correct tank/support/pelagic placement, persistent clutches, no replay, incubation, unique hatchling IDs/stages/genetics, 85/10/4/1 and separate Snowflake rules, recovery/capacity, observations/history/coral lineage, matched live/offline timelines, additive saves, freshwater lock and fully offline behavior. Test UI clock progression during Store, Journal, Casino and Diving. Exact pass/fail and not-run evidence belongs in BREEDING_UPDATE_REPORT.md; do not infer an unrun suite passed.

## 27.19 Equipment reliability acceptance

Run fixed-seed quantitative distributions across every existing marine equipment profile, actual maintained multi-year fault/repair histories, paired neglected cases and quality scaling. Verify 8/12/24-real-hour actual live/offline equivalence, repeated login no-replay, renderer independence, same-item storage/transfers, old condition preservation, biological filter preservation, operational thermal/flow/light/oxygen effects, real UI actions/history and strict local save round trips. Retain freshwater lock/biology and economy coefficients/rewards. Record actual pass/fail counts, real-time replacement/maintenance expectations and limits in EQUIPMENT_DURABILITY_BALANCE_REPORT.md and tests/equipment-reliability-evidence. Rebuild DIST and both archives from final sources; do not infer a test passed.

## 27.20 October20 economy acceptance

Run all 42 requested acceptance categories through tests/economy_update_checks.js and actual browser UI, plus existing durability/Inventory/receiving/breeding/heater/casino regressions. Cover original prices/legacy owners; canonical once-only awards across routes and save/load; literal new-part price versus maintenance; whole-sale ownership isolation, blockers, stale quotes, confirmations, zero-tank recovery and history; exact1000-outcome casino enumeration/versioned saved settlement/limits/replay; fixed 100,000-listing pair sample, actual purchase UI, repeated details and valid individuals for every supported fish. Validate1920×1080,1600×900,1366×768 and390×844. Record actual passed/failed/not-run evidence, balance implications and limits in ECONOMY_UPDATE_REPORT.md. Rebuild DIST/Pages/source archives and verify exact current sources; do not claim tests or unrelated artwork completion that did not occur.

## 27.21 Interactive Tutorial Acceptance

Exercise the actual dry marine start, navigation/targets, sand depth and charges, filling/preparation without stale dry flags, exclusive owned equipment installation, cancellation/confirmed rock placement, gradual temperature adjustment, the full36-game-hour fishless cycle through five-minute steps, actual water checks, compatible current listing, all owned receivers with rejection reasons, atomic paid stocking, real manual food/consumption and resident inspection. Cover no Next bypass, prior valid tanks/feeding, migrations, confirmed skip/restart, pause/resume, missing targets, sold tanks/fish loss, pinned selection, real reload/Continue, offline/local-only saving, profile isolation, blocked storage, unchanged pair odds and freshwater lock. Test1920x1080,1600x900,1366x768 and390x844 target alignment in scene/modal contexts and reduced motion. Report real results in TUTORIAL_OVERHAUL_REPORT.md and tests/tutorial-evidence, alongside current care/economy/offline regressions.

For the complete flow audit, use trusted pointer/keyboard input on resolved highlights, not only synthetic clicks or direct calls that jump to known screens. Exercise a standard-balance clean profile all the way to a real meal and inspection, including wall-clock cycling through the existing 20x speed control. Test existing established saves and actual browser reload/Continue during preparation, installation, cycling, purchasing and receiving. Add deterministic task-graph reachability/prerequisite checks, resource/equipment/stock/missing-target recovery, cancellation, native modal hit tests and four viewport widths. Current findings, flow map and executed evidence live in TUTORIAL_FULL_AUDIT_AND_REPAIR_REPORT.md and tests/tutorial-audit-evidence. Earlier v4.2 evidence remains historical, not proof that its original highlighted route worked.

## 27.22 UI Polish and Quantity Acceptance

Use tests/browser_qa.py --ui-quantity for actual offline native-input controls, immediate totals, integer/funds/stock/storage failures, distinct equipment IDs, supply/medical/part stacks, rock storage/placement, single-item safeguards, financial reconciliation, replay after recent-token eviction, local reload and destination retention. Capture1920×1080,1600×900,1366×768 and390×844. Verify downward scale orientation visually, opaque panels, unaffected Canvas and an identical-scene pattern-off/on render sample. Preserve full tutorial, economy, Pages/local-save, equipment/offline and performance regressions; record actual outcomes in UI_POLISH_QUANTITY_REPORT.md.

## 27.23 Protected Production Acceptance

Verify original development/art hashes, production-only allowlist, minified code/styles, stable public keys, no maps/review documents/tooling/player data, exact manifest and ZIP bytes and deterministic rebuild. Run tests/browser_qa.py --protected-build in Chrome/Edge for actual offline file-origin gameplay and all382 existing native sheets; --pages covers HTTP repository-subpath loads and existing diving/receiving/art/save systems. Run affected tutorial, economy, equipment/offline and breeding suites against --dist. Benchmark development and protected builds in fresh browser processes, record actual startup, capped60/30FPS, one-core main-thread CPU, GC heap, hidden/covered work and local-video playback. Compare exact matched biological state and run a five-minute navigation/listener/memory soak. Do not claim physical GPU, Netflix/DRM/audio-sync results or missing artwork completion without actual evidence. Section25.5 gates completion; record final outcomes in DISTRIBUTION_PROTECTION_REPORT.md.

# 28. DEVELOPMENT ROADMAP & EXECUTION ORDER

Develop in integrated phases.

## Phase 1 — Foundation
- Offline `index.html`.
- Game state.
- Simulation clock.
- Local saving.
- Rendering foundation.

## Phase 2 — UI Framework
- Black/slate-blue theme.
- Navigation.
- Aquarium viewport.
- Inspectors.
- Stores.

## Phase 3 — Tank Setup
- Empty tanks.
- Sand.
- Water.
- Equipment.
- Cycling.

## Phase 4 — Saltwater Habitat
- Fiji/Caribbean/Hawaiian substrates and rock.
- Sand-depth controls.
- Rock placement.
- Substrate maturation.

## Phase 5 — Fish Simulation
- Species data.
- Detailed art.
- AI.
- Health.
- Compatibility.
- Aging.
- Death and decomposition.

## Phase 6 — Coral Simulation
- Detailed coral sprites.
- Health.
- Growth.
- Bleaching.
- Death.
- Reef chemistry.

## Phase 7 — Economy
- Shops.
- Inventory.
- Transactions.
- Limited selling.
- Black-market foundations.

## Phase 8 — Breeding
- Genetics.
- Fertility.
- Eggs.
- Incubation.
- Fry.

## Phase 9 — Progression
- Quests.
- Achievements.
- Unlocks.
- Prestige.

## Phase 10 — VIP & Events
- Illustrated previews.
- Seasonal framework.
- No payment functionality.

## Phase 11 — Final Polish
- Animation refinement.
- Audio hooks.
- Performance.
- Balance.
- Full test suite.

Deliver functioning vertical slices rather than attempting every future feature at once.

---

## 28.1 Future Ocean Exploration — concept only

Future separately authorized exploration may include larger original maps, varied depths/ecosystems, habitat discovery, photography, observation/research, hidden locations and rare environmental encounters. Use original mechanics/UI/art; never copy another game's protected assets, maps, interface, characters or distinctive creative content. This concept is documentation only; no expanded exploration system is part of the current release. Current diving remains governed only by §5.5.

# 29. PROJECT FILE STRUCTURE

Recommended architecture:

```text
AquariumLife/
├── index.html
├── css/
│   ├── theme.css
│   ├── layout.css
│   ├── components.css
│   └── screens.css
├── js/
│   ├── main.js
│   ├── core/
│   │   ├── gameState.js
│   │   ├── clock.js
│   │   ├── commands.js
│   │   ├── events.js
│   │   └── saveManager.js
│   ├── simulation/
│   │   ├── tanks.js
│   │   ├── fish.js
│   │   ├── fishAI.js
│   │   ├── mortality.js
│   │   ├── decomposition.js
│   │   ├── water.js
│   │   ├── filtration.js
│   │   ├── substrate.js
│   │   ├── algae.js
│   │   ├── corals.js
│   │   ├── equipment.js
│   │   ├── feeding.js
│   │   ├── breeding.js
│   │   └── genetics.js
│   ├── economy/
│   │   ├── wallet.js
│   │   ├── stores.js
│   │   ├── marketplace.js
│   │   └── blackMarket.js
│   ├── progression/
│   │   ├── quests.js
│   │   ├── achievements.js
│   │   └── unlocks.js
│   ├── rendering/
│   │   ├── aquariumRenderer.js
│   │   ├── fishSprites.js
│   │   ├── coralSprites.js
│   │   ├── substrateRenderer.js
│   │   └── effects.js
│   ├── ui/
│   │   ├── navigation.js
│   │   ├── inspectors.js
│   │   ├── dialogs.js
│   │   ├── tankSetup.js
│   │   ├── placementEditor.js
│   │   ├── storesUI.js
│   │   └── vipPreview.js
│   └── data/
│       ├── species.js
│       ├── coralSpecies.js
│       ├── substrates.js
│       ├── rockTypes.js
│       ├── products.js
│       └── quests.js
├── assets/
│   ├── reference/
│   │   └── approved_clownfish_hybrid.png
│   ├── fish/
│   ├── corals/
│   ├── substrates/
│   ├── rocks/
│   ├── interface/
│   └── audio/
├── tests/
├── README.md
├── GAME_DESIGN.md
├── ART_DIRECTION.md
├── UI_SPECIFICATION.md
├── DEVELOPMENT_STATUS.md
└── BALANCE_REPORT.md
```

This structure may be improved when justified.

All runtime files must be loadable in the offline browser environment.

---

## 29.1 Protected Production Distribution

Development source, original assets, review pages, full debugging and test tooling remain human-readable and unchanged by production builds. `python tools/production/bootstrap.py` prepares pinned build-only Terser5.44.0/clean-css5.3.3 and a checksum-verified portable Node22.23.0 on Windows; `python build.py` then reproducibly regenerates DIST and the root-level Pages ZIP offline using the installed local tools. No global installation, runtime server, licensing service or player dependency is added.

Production includes only index.html, required local runtime assets/scripts/styles, a checksum manifest, .nojekyll and a short ownership/protection notice. Exclude review pages, development documentation, original named code copies, source maps, tests, build tools, archives and player data. Minify JS/CSS; use scoped local-identifier mangling and content-derived runtime filenames. Preserve public AL interfaces, registry/species/save keys, script dependency order, relative URLs, dynamic file-origin sprite transports and all16 native frames. Disable gameplay expression rewrites when they threaten performance or fidelity. Do not mangle properties or global interfaces, add runtime string decryption, control-flow flattening, anti-debugging loops, debugger traps or artificial slowdowns.

Minification reduces syntax; identifier mangling is limited obfuscation; ZIP compression reduces storage/transfer; SHA-256/CRC checks detect accidental corruption. None is encryption or tamper-proofing. PNG assets retain their exact approved pixels; HTTP native files and on-demand classic-script transports preserve existing file:// compatibility. Offline delivery cannot conceal a distributed asset-decryption key from its recipient. Do not add ineffective encryption claims, passwords or online key services. No save encryption, authentication change or save rewrite is authorized. Browser code/assets remain inspectable, copyable and locally modifiable.

Keep the source-to-protected mapping, transformation/cache records and all development evidence outside DIST. Public checksums contain output paths/hashes, not source maps. Validate all original source/art hashes, native transports and every published checksum, and reproduce manifest/ZIP bytes with a second build under the same pinned toolchain. Complete section25.5 with matched development/protected benchmarks, local-video multitasking where possible, memory/listener soak, file and HTTP repository-subpath launches, purchases/Inventory, saves, tutorial, diving, casino and biological/breeding regressions. Report physical GPU/Netflix/audio-sync measurements as unavailable when not measured. See DISTRIBUTION_PROTECTION_REPORT.md for actual commands, evidence and limitations.

# 30. CONTINUITY, DOCUMENTATION & LOCKED RULES

Maintain a single consolidated Master Development Prompt.

Do not create disconnected addenda that replace the main specification.

Whenever development requirements change:

1. Find the correct primary section.
2. Integrate the changes.
3. Preserve previously approved requirements.
4. Check for duplication.
5. Cross-reference related systems.
6. Update documentation.
7. Increment the specification version.

Gameplay v2.4 requirements are integrated into sections 4, 6, 13, 15, 17, 18, 23, 24, 26 and 27. The permanent completion rule is section 31.3; keep it for future edits.

## 30.1 Project Documents

**GAME_DESIGN.md**
- Authoritative current game design.
- Locked mechanics.
- Biological assumptions.
- Economy rules.

**ART_DIRECTION.md**
- Approved reference.
- Sprite dimensions and conventions.
- Color rules.
- Coral/rock/sand style.
- Death artwork states.

**UI_SPECIFICATION.md**
- Colors.
- Layouts.
- Components.
- Interaction patterns.
- Screens.

**DEVELOPMENT_STATUS.md**
- Completed work.
- In-progress work.
- Unfinished requirements.
- Bugs.
- Next priorities.
- Test status.

**BALANCE_REPORT.md**
- Economy assumptions.
- Simulation tests.
- Results.
- Adjustments.

Equipment reliability documentation: maintain EQUIPMENT_MAINTENANCE.md, EQUIPMENT_RELIABILITY_SAVE_SCHEMA.md and EQUIPMENT_DURABILITY_BALANCE_REPORT.md with section 11.7 as the mechanics home. Preserve the entire exact master in PROJECT_CONTINUITY_SOURCE.md, including all 31 major sections.

## 30.2 Permanent Locked Decisions

1. The project is an offline browser aquarium simulation.
2. `index.html` must work directly.
3. The approved clownfish image defines the visual style.
4. Fish must be the visual centerpiece.
5. Corals and habitat art must match fish quality.
6. UI background is near-black.
7. UI panels are slate blue.
8. UI may take broad inspiration from Happy Aquarium but must be original.
9. New tanks begin completely empty.
10. The player must establish a viable habitat before stocking it.
11. Current and upcoming livestock development is saltwater only; protect existing freshwater content per section 2.5.
12. Freshwater remains in the long-term design; shared infrastructure changes require freshwater regression checks.
13. Fiji, Caribbean, and Hawaiian rocks and sand are supported.
14. Sand depth is player-selectable from 0 to 5 inches.
15. Sand displays biological maturation and environmental growth.
16. Dead fish have distinctive visual states and persistent decomposition.
17. Unremoved dead organisms can affect water quality.
18. Coral bleaching and death are separate biological states.
19. Dead stony coral may leave skeletons and undergo gradual erosion/dissolution.
20. Fish are individual persistent creatures.
21. Species care requirements should follow defensible real-world information.
22. Fish aggression, compatibility, and predation matter.
23. Breeding and eggs have species-dependent mechanics.
24. The economy must resist unlimited buy/sell exploitation.
25. Players progress through quests and aquarium achievements.
26. The Deep Market contains high-risk and fictional prohibited content.
27. VIP is preview-only with images and no payment processing.
28. The game must remain performant.
29. UI controls must be real and functional.
30. Saving and loading must preserve all relevant state.
31. All updates must preserve this consolidated 31-section MDP; permanent store-destination invariants are in section 18.4, mounting in 23.1 and art review in 3.11.

---



## 30.3 Permanent livestock logging and completion rule

Every future added livestock species MUST be logged in the permanent registry, CURRENT_LIVESTOCK_CATALOG.md, consolidated MDP and PDF/continuity source in the same batch. Required fields: common/scientific names, stable ID, category, rarity, care difficulty, planned/approved/implemented/art-only/partial status, batch, implementation date, art status, alive/dead support and honest notes. Never auto-approve artwork, hide missing stages or infer unsupported biology. PROJECT_CONTINUITY_SOURCE.md is the printable source; PDF_WORKFLOW.md records generation requirements. If tools cannot generate and verify a PDF, update the source and explicitly report PDF regeneration pending. Completion reports list changed files, species/duplicates, passed/failed/not-run tests, documentation and remaining limits; end the completed authorized editing task with the exact standalone line Done With Edits.



## 30.4 Regional Eligibility and Registry Continuity

Every collectible region assignment must carry a verified scientific identity/source, habitat and depth suitability, conservation/collection status independent of rarity, care/art/health/value and receiving requirements. The six v2.8 profiles reference existing taxa; do not duplicate them as new species. Keep the source region ledger, generated offline script, current catalog and continuity/PDF source synchronized. Maintain exact species counts and distinguish fictional restricted recovery from legal collection. Keep DIST current through python build.py; local saves never become deployment inputs. Completion/reporting rules in §30.3 remain.

## 30.5 v2.9 Continuity and Locked Additions

Maintain one consolidated 31-section MDP, current catalog, old/new permanent registries, GAME_DESIGN, UI_SPECIFICATION, ART_DIRECTION, DEVELOPMENT_STATUS and BALANCE_REPORT. Verbatim original requirements and the original proposal remain archived under planning/v2.9; approval.json records later explicit implementation authorization. Never confuse registered/acquisition-held, implemented or art-approved status. Keep the complete 35-row new ledger and prior 38-row ledger in the continuity source with the full MDP and back-of-source rules. Binary PDF regeneration remains pending unsupported authoring/rendering tooling. Preserve future freshwater authorization checks, twenty-minute days, local saves, six windows, Deep Market identity compatibility, exact rewards/odds, large-tank price and volume maintenance, and all prior locked rules. Completed authorized edit reports identify files/features/species/tests/limits/docs, then use the exact completion line.

## 30.6 Permanent v3.1-v3.3 continuity rules

Retain the current three source specifications under planning/v3.1-v3.3. Keep one 31-section master, catalog, existing registries, UI/design/status/balance, financial schema, source-evidence/coverage and full continuity source current. Refer to sections 8.8, 17.8, 18.10, 19.6 and 24.7 rather than inventing alternate frag, wallet, research or resale formulas.

Freshwater remains locked until explicitly approved. Preserve existing art approvals and acquisition holds. Fragments and research add no biological species. Continue simulation during shopping, research, fragging, diving and financial dialogs, plus offline catch-up. Casino requirements apply only if such games are implemented. Rebuild DIST and both release archives from the final sources. Do not claim PDF generation without export/render verification or complete research evidence where fields are unknown.

---

## 30.7 Permanent overnight repair rules - v3.5

Preserve the twenty-minute day, chronological offline ecosystem, finite compatible food, species/stage differences and real mortality. Do not resurrect previously dead livestock or award compensation without a separate explicit instruction. Retain recoverable original data where local storage supports it; disclose unavailable historical causes and current-state readiness limits. Keep freshwater scope, all art approvals/holds, roster registries, safe store destinations, rewards, asset valuation and local storage boundaries intact. Rebuild DIST and both ZIPs after source edits. This repair adds no biological species or art.


## 30.8 Automatic Breeding Continuity — v3.8

Preserve the permanent autonomous-breeding rule in 15.1, current species boundaries in 15.8 and additive schema in 24.11. Keep original genetics/art approvals, specialist holds, all 38/35 roster ledger entries and the complete 31-section master in the printable continuity source. Refresh DIST/Pages ZIP and the source ZIP for delivery. If PDF authoring/rendering is unavailable, retain the updated full source and report binary PDF pending.

# 31. FINAL EXECUTION INSTRUCTIONS FOR CODEX

Inspect the existing project before making changes.

If an existing Aquarium Life implementation is present:

- Examine the codebase.
- Review documentation.
- Identify completed systems.
- Identify missing requirements.
- Preserve functioning features.
- Protect existing save data.
- Plan implementation dependencies.

If the project is empty, initialize it.

Do not stop after writing a plan.

Begin implementing real functionality.

## 31.1 First Playable Release Targets

Aim to deliver:

- Offline browser startup.
- Polished main aquarium UI.
- Empty-tank onboarding.
- Working sand and water setup.
- Basic biological cycling.
- Purchasable rock and sand.
- At least 20 data-driven fish species over the initial full gameplay milestone, prioritizing saltwater first.
- Working fish movement.
- Individual fish statistics.
- Health and environmental requirements.
- Fish death, corpse persistence, and decomposition.
- Coral health, bleaching, and death.
- Algae and substrate development.
- Adjustable sand depth.
- Core equipment.
- Feeding.
- Working store and economy.
- Limited selling.
- Initial breeding/egg mechanics.
- At least 15 connected quests.
- Black-market foundation.
- VIP image previews.
- Save/load.
- Performance presets.

These targets are not permission to deliver fake implementations.

## 31.2 Implementation Standards

Before modifying code:
- Understand dependencies.
- Check for duplicate systems.
- Identify test requirements.

During implementation:
- Write clean, maintainable code.
- Use shared simulation logic.
- Keep data-driven configuration.
- Validate transactions.
- Preserve visual consistency.
- Avoid unnecessary libraries.

After implementation:
- Complete the mandatory Implement → Profile → Re-optimize → Validate → Report workflow in section25.5 before declaring completion.
- Run available tests.
- Check runtime errors.
- Verify offline compatibility.
- Identify any tests not performed.
- Update documentation.
- Report completed and incomplete work accurately.

## 31.3 Completion Reporting

At the end of each major development phase, report:

1. Features implemented.
2. Existing systems modified.
3. Tests executed and their results.
4. Known limitations.
5. Save compatibility changes.
6. Next recommended development phase.
7. Performance & Optimization: issues discovered, optimizations performed, available before/after measurements, completed regression tests/results and remaining concerns or unmeasured items (section25.5).

Never call an untested or partially implemented system fully complete.

Do not silently remove requirements to reduce development scope.

### Permanent Editing Completion Rule

An authorized implementation is complete only after its feature work, mandatory post-implementation optimization pass and required regression validation in section25.5 are genuinely finished and reported. After an authorized editing task is actually complete, report the files/features changed, tests run and pass/fail results, remaining limitations and updated documentation. Every implementation completion report must include the Performance & Optimization section required by section25.5. The final response must end with the exact standalone line `Done With Edits`. Preserve spelling and capitalization. Do not use that phrase for planning, incomplete work or a blocked task; explain what remains instead. This rule is locked for future Aquarium Life editing tasks.

## 31.4 Final Development Mission

Build Aquarium Life into a polished, biologically grounded, visually beautiful, strategically engaging aquarium simulator.

The player should experience the satisfaction of constructing an empty tank, establishing a stable ecosystem, caring for individual creatures, developing thriving reefs, discovering rare fish, and building a valuable aquarium collection.

The approved hybrid pixel-art style must remain consistent throughout the game.

All major systems must produce meaningful visual and simulation consequences.

**Start development using this consolidated specification as the authoritative source of truth.**
