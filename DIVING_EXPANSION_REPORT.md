# Global ocean diving expansion and emergency resale — playable v4.0

2026-10-16. Implements both authorized attachments: Emergency Diving Sales & Rock Resale and Global Ocean Diving Expansion specification v3.6. Master prompt v4.3 retains all 31 major sections. No new biological species, freshwater development, server saves or pressure aquarium was added.

## Changes

- Emergency Sale works directly on unreceived living fish, corals and invertebrates. It needs no receiving aquarium. The exact confirmed offer is `max(0, floor(AL.Valuation.livestock(actual assessed specimen).value × .25))`. Dead-on-arrival, expired and explicitly sale-protected specimens cannot be liquidated. A zero-floor offer is allowed and gets one explicit zero-AC ledger receipt. Receiving and selling use the same saved health and survival draws. Receiving, release and sale are mutually exclusive terminal outcomes.
- Existing owned diving resale is unchanged: regular store pays floor(Deep reference × .60). Deep Market still needs Reputation 5, an active matching Wanted request and its other existing access/condition limits. Emergency Sale adds no reputation and fills no Wanted order.
- Returned rock inventory retains a stable item ID, region, expedition, group, variant/size, quantity and saved condition. Estimate = floor((existing rock product price + variant × 25) × quantity × condition); buyback = floor(estimate × .40). Results and regular Saltwater Sell show the exact offer and confirm sale. Placing/removing preserves the same recovered rock identity. Attached corals and eggs still block support removal; an installed rock cannot be sold. Bought rocks cannot be passed off as recovered inventory.
- Seven new reef selections preserve Fiji, Caribbean, Hawaii and Japan: Indonesia/Bunaken, Philippines/Puerto Galera, Sri Lanka/Kayankerni, Marshall Islands/Majuro, Maldives/Madivaru Beyru, Australia/Lady Musgrave Island on the Great Barrier Reef, and Florida/Tortugas–Keys. Mariana is Deep Sea only with a fictional remote research drone and explicitly labeled battery budget. No living hadal pool or ordinary reef receiving is invented.
- Fish capture saves the actual individual before ownership: unique ID, stage, age, growth/body size, sex/temperament, genes/pattern and provenance. Approved base weights are 20/35/45 baby/juvenile/adult, restricted and normalized to each supported habitat. Settled Ocellaris supports all three in the Coral Triangle; other current profiles conservatively support juveniles/adults. Receiving preserves development. Pre-upgrade captured active/pending fish migrate to deterministic adult snapshots without reroll; future profiles without stage metadata safely retain adult fallback. Existing young-fish fine-food metabolism is used; baby receiving requires refuge and food.
- Saved medical draws produce healthy/stressed/malnourished/injured/suspected infection/severely compromised outcomes; transport failure remains possible. Species sensitivity, transport exposure, pre-existing risk, age and quarantine affect survival. Existing host-eligible diseases are used, with more than one possible fish infection. Signs are not falsely labeled confirmed diagnoses. Results show health, symptoms, quarantine advice, compatible-care restrictions and the existing Disease & Treatment Guide.
- Mystery eggs use a separate configurable 3% opportunity per eligible expedition. Current eligible identity is existing Ocellaris, attached to a removable support chip near anemone habitat in the two Coral Triangle zones. Hidden identity, unique clutch ID, genes/pattern, approximate viability and provenance are assigned once. No mouthbrooded/liveborn animals or open-water demersal eggs are fabricated. A prepared dedicated incubation tank is checked through shared biological safeguards plus fine food, protected support and gentle flow. Inventory never incubates eggs. Hatching creates a real early larva, transfers genetics and origin, reveals identity/rarity, and updates the Field Journal. Failed/abandoned eggs remain unidentified.

## Regional evidence and limits

The registry is the authoritative destination/profile source; UI and simulation do not maintain separate region lists. The following existing species are used at new zones. Survey locality supports occurrence; chosen grid depths, discovery weights and developmental ages remain game calibrations, not survey abundance claims.

| New reef selection | Existing fish pool | Locality/range evidence |
|---|---|---|
| Indonesia — Bunaken/Lekuan | Yellow longnose butterflyfish; Ocellaris clownfish | [REEF Bunaken/Lekuan survey](https://www.reef.org/db/reports/geo?region_code=CIP&zones=43130021) |
| Philippines — Puerto Galera | Yellow longnose butterflyfish; Ocellaris clownfish | [REEF Puerto Galera surveys](https://www.reef.org/db/reports/geo?region_code=CIP&zones=7102) |
| Sri Lanka — Kayankerni | Yellow longnose butterflyfish | [Kayankerni primary reef survey](https://kayankerni.org/wp-content/uploads/2022/11/01.-A-preliminary-report-on-the-status-of-Kayankerni-coral-reef-Sri-Lanka_2019.pdf) |
| Marshall Islands — Majuro | Yellow longnose butterflyfish | [NOAA archived Majuro survey](https://repository.library.noaa.gov/view/noaa/45869/noaa_45869_DS1.pdf) |
| Maldives — Madivaru Beyru | Yellow longnose butterflyfish | [REEF Madivaru Beyru survey](https://www.reef.org/db/reports/geo?region_code=IORS&zones=23010046) |
| Australia — Lady Musgrave Island/GBR | Yellow longnose butterflyfish | [Fishes of Australia museum record](https://fishesofaustralia.net.au/home/species/2410) |
| Florida — Tortugas/Keys | Chalk Bass | [Florida State Museum checklist](https://www.floridamuseum.ufl.edu/wp-content/uploads/sites/35/2017/03/Vol-2-No-8.pdf) |

Ocellaris substrate-attached eggs, larval period and settled juvenile habitat use the [University of Michigan biological account](https://animaldiversity.org/accounts/Amphiprion_ocellaris/). The 85% initial estimated viability, representative single egg, accelerated incubation, transport assessment and support-chip recovery are explicit game models, not measured wild survival rates or a claim of complete captive-culture feasibility. Region-specific art is original code-native pixel-style SVG scenery; existing species-specific baby/juvenile/adult atlases are reused. No generic fish is presented as finished species art.

Mariana uses a fictional tethered drone at 6,000 m, approximately 2 °C and 600 atmospheres. The game has no approved pressure-maintained transport or aquarium, so only nonliving sample recovery is available. This follows the distinction in [NOAA's robotic exploration description](https://oceantoday.noaa.gov/oceanasalab_rovs/) and [NOAA's Mariana context](https://www.ncei.noaa.gov/news/planet-postcard-mariana-trench). No real collection authorization is asserted for any destination. Hawaii remains wildlife-closed.

## Files

Runtime: `js/diving-expansion.js` (new), `js/diving.js`, `js/diving-mystery.js`, `js/diving-ui.js`, `js/diving-art.js`, generated `js/diving-data.js`, `assets/diving/registry.json`, eight new regional SVGs, `js/core.js`, `js/finance.js`, `js/valuation.js`, `js/simulation.js`, `js/marine-care.js`, `js/brood-view.js`, `js/app-shell.js`, `js/update31.js`, `js/update31-ui.js`, `index.html`.

Build/QA: `build.py`, `tests/browser_qa.py`, `tests/diving_expansion_checks.js`, `tests/diving_expansion_qa.py`, `tests/diving_checks.js`, `tests/mystery_diving_checks.js`, `tests/global_receiving_checks.js`, `tests/pages_qa.py`, `tests/package.py`, release-verification tooling and evidence. Guarded one-time integration scripts are development records, not runtime dependencies.

Documentation: this report, `DIVING_EXPANSION_SAVE_SCHEMA.md`, `MASTER_DEVELOPMENT_PROMPT.md`, `PROJECT_CONTINUITY_SOURCE.md`, `README.md`, `GAME_DESIGN.md`, `DEVELOPMENT_STATUS.md`, `BALANCE_REPORT.md`, `UI_SPECIFICATION.md`, `CURRENT_LIVESTOCK_CATALOG.md`, `ART_DIRECTION.md`, `MYSTERY_DIVING_RULES.md`, `GITHUB_PAGES_BUILD_REPORT.md`, `TEST_REPORT.md`.

## Verification

The release validation table is generated from the final browser evidence below. Browser runs use isolated QA profiles and offline source or a local HTTP repository subpath; they do not inspect player saves. Coverage includes new destinations, all current shared fish/coral/invertebrate profiles, stages, saved health, exact 25%/60% pricing, Deep gates, zero-AC receipts, sale replay, rock/coral support, hidden egg identity, actual incubation/hatching/failure, save/load, active/catch-up equivalence, movement limits, responsive 1920×1080 / 1600×900 / 1366×768 / 390×844, continued aquarium time, and offline/local storage.

<!-- FINAL-RESULTS -->
| Final browser suite | Passed | Failed |
|---|---:|---:|
| diving-expansion-evidence/chrome-results.json | 342 | 0 |
| diving-expansion-evidence/edge-results.json | 342 | 0 |
| pages-evidence/chrome-results.json | 636 | 0 |
| pages-evidence/edge-results.json | 636 | 0 |

**1956 executed browser assertions passed; zero failed.** Source suites include shared receiving and mystery regressions; built suites also include the broader existing core/expansion, medical, valuation, resale and local-account checks. These totals intentionally count independent browser executions. No unrun Firefox or real GitHub deployment is claimed.

Both source browsers completed the full, unmodified 168-game-hour incubation and one real hatch, retained hidden identity after an actual reload, exercised actual Emergency Sale confirmation, verified active aquarium time during results, and checked all requested desktop viewports plus a 390 px narrow layout. The separate release verifier checks source/DIST/ZIP hashes and current source archive contents.
<!-- END-FINAL-RESULTS -->

Remaining content limits: small verified fish pools are intentional. No new coral/invertebrate locality pools, hadal livestock, pressure tanks, actual scientific diagnosis engine, complete wild/captive culture model or binary PDF regeneration is claimed. The printable PDF continuity source is current. Existing 38/35 roster ledgers, species-specific art/genetics, original aquarium saves, freshwater lock, reward rules and the 20-minute day are preserved.
