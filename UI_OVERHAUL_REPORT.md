# Aquarium Life — main UI overhaul report

Historical milestone report. Current gameplay/time/settings results are in [GAMEPLAY_UPDATE_REPORT.md](GAMEPLAY_UPDATE_REPORT.md); this is not a new full-project audit.

Date: 2026-10-13. Delivered for user review; unrelated development stops here.

The interface uses exactly six permanent sidebar windows. The selected aquarium stays central with a live total value above the water. Existing buying, selling, care, collection, progression, breeding, saves and preview-only VIP features are routed into those windows. No artwork or livestock roster was replaced.

Player-created starting and purchased tanks start empty/dry; existing saved aquariums retain their equipment, scenery and residents. Equipment removed from a tank is stored with capacity/condition for later installation. Marine clutches are selectable, attached to persistent spawning sites, and retain progress/lineage through saving and hatching. Failed external marine clutches remain inspectable/removable for up to one game day.

## Executed verification

| Suite | Chrome | Edge |
|---|---:|---:|
| UI acceptance + marine logic | 139 passed / 0 failed | 139 passed / 0 failed |
| System regression | 68 passed / 0 failed | 68 passed / 0 failed |
| Shared store / destination regression | 90 passed / 0 failed | 90 passed / 0 failed |
| Economy / disease / valuation regression | 69 passed / 0 failed | 69 passed / 0 failed |
| Clownfish art / directional regression | 7583 passed / 0 failed | 7583 passed / 0 failed |

Protected data/art/source files: **145 / 145 unchanged**. Consolidated MDP: **31 / 31 major sections retained**, version 2.9. No new species and no remote gameplay requests. The ten-day freshwater biological comparison and marine-only source-hook comparison passed.

The approved dry-tank change required test fixtures to install their equipment explicitly before biological checks. Old inline-management assertions were moved to the correct modal containers. These fixture changes preserve the behaviors being tested rather than hiding failures.

## Required 40-check acceptance mapping

| # | Requirement | Verified evidence |
|---:|---|---|
| 1 | PASS — Exactly six sidebar entries | Sidebar DOM assertion |
| 2 | PASS — Approved names and order | Exact ordered label assertion |
| 3 | PASS — Each entry opens its own modal | Six real sidebar clicks |
| 4 | PASS — Every modal has top-right X | Visible control assertions; desktop/narrow visual inspection |
| 5 | PASS — Escape closes modal | Real keyboard events for every primary window |
| 6 | PASS — Closing returns to aquarium | Visibility and state assertions after each Escape |
| 7 | PASS — No unnecessary desktop page scrolling | Seven viewport scroll-height/width assertions |
| 8 | PASS — Internal modal scrolling works | Overflow and scrollTop test on encyclopedia |
| 9 | PASS — Aquarium visible and correctly scaled | Canvas bounds and 2:1 assertions at seven sizes |
| 10 | PASS — Total value centered above aquarium | Geometry comparison of header and water canvas |
| 11 | PASS — Value uses real state | Exact AL.Valuation comparison plus economy model tests |
| 12 | PASS — Switching aquariums updates value | Actual selected-tank switch and header assertion |
| 13 | PASS — Value opens correct breakdown | Click → Aquariums / Tank Value and all row labels |
| 14 | PASS — Store has exactly three habitat tabs | Exact store tab label assertion |
| 15 | PASS — Night Market belongs to Black Market | Black tab / progression tests; six-sidebar assertion |
| 16 | PASS — Marketplace remains in store | Actual Sell click and rehome controls; Orders actual history |
| 17 | PASS — Fish Collection renamed Livestock Collection | Journal tab assertion |
| 18 | PASS — Collection in Field Journal | Real journal route and six filter controls |
| 19 | PASS — Achievements accessible | Existing store route regressions exercise moved achievements |
| 20 | PASS — Quests and history accessible | Remembered quest route, history links and modal route regressions |
| 21 | PASS — Coral / plant information in journal | All fish/flora encyclopedia entries and independent notes |
| 22 | PASS — Coral purchases accessible | Five coral products in Saltwater Store |
| 23 | PASS — Equipment has Lighting / Tank Care / Water Change | Exact three-tab assertion |
| 24 | PASS — Tank Care includes pumps / filters / heaters | Category controls assertion |
| 25 | PASS — VIP preview-only | Five tiers, prohibition banner and disabled payments assertions |
| 26 | PASS — Breeding records accessible | Parentage, incubation and juvenile-growth assertions |
| 27 | PASS — Eggs appear in correct aquarium | Visible clutch hitbox; absent in other aquarium |
| 28 | PASS — Egg stages display correctly | Early/late size, alive/dead art and nonviable inspector tests |
| 29 | PASS — Eggs anchored appropriately | No drift; rock support-removal block; persistent local coordinates |
| 30 | PASS — Egg progress saved / reloaded | Exact brood JSON, ID and anchor round trip |
| 31 | PASS — Egg-to-larva transitions work | Single hatch, larval growth, parent lineage and post-hatch reload |
| 32 | PASS — Eye / direction rules functional | 7,583 clownfish/art checks and 1,792 directional cases per browser |
| 33 | PASS — No freshwater-specific development | 145 protected data/art/source files identical; protected simulation comparison; ten-day biology equality |
| 34 | PASS — No save data lost | Full state equality after navigation; migration and active save validation regressions |
| 35 | PASS — No duplicate purchases / livestock | Store repeated-confirm tests and post-hatch reload checks |
| 36 | PASS — Offline index works | file:// execution; zero HTTP(S) requests |
| 37 | PASS — Resize preserves layout | Seven sizes including short desktop and narrow layouts |
| 38 | PASS — Modal keyboard focus works | Native focus assertions; real Tab remains trapped; close restoration |
| 39 | PASS — Buttons perform real / honest actions | Equipment remove/reinstall persistence; live lighting; real transactions; explicit dry/unimplemented states |
| 40 | PASS — Main tank rendering remains intact | Canvas/lighting regression, real art inspection and screenshots |

## Interface review

- [Main aquarium, 1440 × 900](tests/ui-overhaul-evidence/chrome-main-1440-900.png).
- [Short desktop, 1024 × 600](tests/ui-overhaul-evidence/chrome-main-1024-600.png).
- [Narrow layout, 390 × 844](tests/ui-overhaul-evidence/chrome-main-390-844.png).
- [Tank Value window](tests/ui-overhaul-evidence/chrome-tank-value.png).
- [Livestock Collection](tests/ui-overhaul-evidence/chrome-journal-collection.png).
- [Equipment lighting](tests/ui-overhaul-evidence/chrome-equipment-lighting.png).
- [Coral store](tests/ui-overhaul-evidence/chrome-store-corals.png).
- [Egg inspector](tests/ui-overhaul-evidence/chrome-egg-inspector.png).

## Scope and practical limits

This update is complete for the implemented systems, not a declaration that the entire game or every historical audit item is finished. Native modals keep the existing simulation pause rule; close them to advance incubation/treatment. Canvas animation continues. Main scrolling is removed at the seven verified viewport sizes; internal summary/dialog scrolling remains intentional.

Orders are a view of completed instant-delivery transactions from the existing bounded log, not a new queued-delivery service. Tank History includes recent keeper-wide events (70 retained), observed individual medical events and selected-tank value history; no absent archival records are fabricated. Historical fish discovery is preserved, while historical coral/plant species discovery was never tracked.

VIP tiers are concepts; existing appropriate artwork is reused in reference previews, and missing exclusive decorations/collections are labeled unimplemented. There are no payments, subscriptions or network services. Existing unverified scientific names and game-calibrated biological parameters are explicitly labeled.

Marine spawning presentations distinguish hard-surface groups, water-column groups and internal broods. Nest cavities, individual embryos and rare-species microstructure remain simplified; no invertebrate roster or sexual coral-spawning simulation was invented. Coral fragmentation remains the existing mechanic. Freshwater biology/art stay protected. The low-level legacy template is retained for save/biology fixtures; player story creation explicitly requests the empty/dry template.

Reproduction reference: [UF/IFAS marine ornamental culture](https://ask.ifas.ufl.edu/publication/FA224) supports adhesive clownfish eggs, demersal groups, protected cardinalfish mouthbrooding and pelagic tang/wrasse spawning. [Florida Museum clownfish profile](https://www.floridamuseum.ufl.edu/discover-fish/species-profiles/orange-clownfish/) supports rock-associated nests. These are broader-group presentation references, not certification of every legacy species profile.

Evidence: [Chrome acceptance JSON](tests/ui-overhaul-evidence/chrome-results.json), [Edge acceptance JSON](tests/ui-overhaul-evidence/edge-results.json), [integrity checks](tests/ui-overhaul-evidence/integrity.json). Run `python tests/browser_qa.py chrome --shell` or replace chrome with edge.
