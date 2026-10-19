# Equipment Inventory & Interface Reorganization

Implemented 2026-10-19. Source requirements: [approved prompt](planning/inventory-interface/requirements.md). This report covers the equipment/interface update; earlier livestock-art production limitations are unchanged.

## Audit findings and repair

The simulation already computed life support from each tank’s own equipment array. It did not share heater/filter capacity across profiles or aquariums. However, equipment lacked installed-instance IDs: removal created a new storage ID and installation discarded it. Purchases installed immediately; storage was embedded in Tank Care. Ordinary removed rocks and frag racks were discarded, and decorations lacked a removal path. Journal navigation still registered Breeding & Eggs and Leaderboards; Tank Care rendered both standalone panels and a global thermostat form.

Equipment now has unique persistent IDs in both storage and installed locations. Purchase creates exactly one stored unit and uses the existing stock/AC transaction. Installation and warned removal move that exact unit, retaining condition, rating, model, switch, modifications and thermostat. Legacy source thermostat fallback is captured during removal/transfer. Fixed capacity is rechecked for every installation/transfer. Full save validation rejects duplicate identities and the draft transaction leaves failed actions unchanged. Each tank’s own installed array remains the only equipment effects authority.

## Interface behavior

- Equipment → Inventory shows only stored equipment, ordinary objects, recovered diving rocks and existing positive supply/medical quantities. Living livestock is excluded. Search/category filters combine; existing pixel previews, quantities, condition and specifications are reused. All owned destinations appear, with disabled incompatible options and full reasons below.
- Existing rock/decor purchases retain explicit placement. Removed rocks/decorations/racks return to storage; recovered rocks retain their diving inventory/sale authority. Coral/clutch attachments block support removal. Rack remounting preserves its original glass/position settings.
- Field Journal no longer registers Breeding & Eggs or Leaderboards tabs. Old breeding routes lead to Collection; old leaderboard routes lead to the relocated view. Collection retains broods/residents, inspectors retain reproductive status, and Tank History retains breeding observations, archived lineage and coral frag lineage. Autonomous reproduction is unchanged.
- Leaderboard Preview sits directly above VIP Store and below The Dock Casino. It reuses the existing single offline asset-value comparison and locked freshwater preview. All eight sidebar routes retain their existing styling and modal behavior.
- Tank Care has no standalone Temperature Control or Overnight Readiness panel, no global thermostat form and no stored-equipment section. Individual installed heater/chiller inspectors retain thermostats; heating/cooling remains gradual and capacity/condition dependent. Food & Feeding retains current food forecasts. Tank History → Reports reads existing offline audit runs, mortality and chemistry history without creating reports.

## Persistence

Base schema remains 2. The additive `itemLocationVersion: 1` migration assigns only missing legacy equipment IDs, preserves existing IDs/attributes, and initializes empty ordinary-object storage. Installed items stay installed and are never copied into Inventory. Existing account/save, wallet receipts, livestock, breeding/genetic records and local recovery/export rules remain intact. Profile inventory is read only from the active state; stale dialogs check account identity. See [schema](EQUIPMENT_INVENTORY_SAVE_SCHEMA.md).

## Files changed

Runtime: `js/equipment-inventory.js` (new ownership/compatibility authority), `js/inventory-ui.js` (new storage/installation UI), `js/core.js`, `js/save.js`, `js/thermal.js`, `js/store-rules.js`, `js/store.js`, `js/heaters.js`, `js/ui.js`, `js/app-shell.js`, `index.html`, `css/app-shell.css`.

Documentation: `MASTER_DEVELOPMENT_PROMPT.md` v4.8 (all 31 major sections retained), `GAME_DESIGN.md`, `UI_SPECIFICATION.md`, `DEVELOPMENT_STATUS.md`, `PROJECT_CONTINUITY_SOURCE.md` (one exact full master), `EQUIPMENT_INVENTORY.md`, `EQUIPMENT_INVENTORY_SAVE_SCHEMA.md`, this report, and the preserved original requirements.

Verification/build: `tests/inventory_checks.js`, `tests/inventory_qa.py`, `tests/browser_qa.py`, `tests/preparation_checks.js`, `tests/overnight_probe.js`, `tests/diving_checks.js`, `tests/breeding_qa.py`, `tests/heater_checks.js`, `tests/heater_qa.py`, `tests/package.py`, `tests/pages_qa.py`, `build.py`. Existing regression fixtures now give separate physical equipment proper IDs and explicitly install purchases before exercising biological systems; their biological assertions remain in force. Generated DIST and release ZIPs are rebuilt from these sources.

## Executed tests

| Suite | Result |
|---|---|
| Chrome source inventory/model/UI | 70 passed, 0 failed (final source execution) |
| Edge rebuilt DIST inventory/model/UI | 70 passed, 0 failed |
| Chrome autonomous breeding, eggs, inheritance, history, offline equivalence | 86 passed, 0 failed |
| Chrome aquarium preparation and shared diving receiving | 207 passed, 0 failed |
| Edge heater/mortality model and UI, 8/12/24-hour live/offline matrix | 108 passed, 0 failed |
| Edge GitHub Pages repository subpath, local saves/export/import and direct-folder launch | 5,162 passed, 0 failed |
| Protected biology, breeding, economy/offline code and artwork registries versus previous release | 19 unchanged, 0 differences |
| Release source/DIST hashes and both ZIPs | Verified through the build/package commands and final integrity verifier below |

Inventory and sidebar layouts were checked at 1920×1080, 1600×900, 1366×768, 764×900 and 390×844, including pixel thumbnails and internal scrolling. Desktop and mobile screenshots are under `tests/inventory-evidence`. Network-disabled isolated profiles were used; no player save was opened or modified.

### Required acceptance coverage

| Requested checks | Evidence |
|---|---|
| 1–5: Inventory tab, stored-only items, no installed/placed items | Inventory browser and model checks |
| 6–10: purchase to storage, compatible destination, exclusive installation, same-ID removal, condition preservation | All 11 existing equipment types purchased in model; actual store/install/remove UI; cross-tank roundtrip with modified condition and attributes |
| 11–14: safe failures, double-clicks, save/reload, isolated profiles | Occupied/weak/missing/freshwater destinations reject transactionally; token and stale-ID replay tests; actual local reload and separate-profile fixtures |
| 15–19: independent tank capacity/effects, heater/filter removal, switching | Per-tank Core capacity and Thermal status checks; no stored capacity; unique membership through switches/transfers |
| 20–24: removed tabs, automatic breeding, eggs/offspring/history | Removed navigation and legacy-route checks plus existing 86-check breeding suite |
| 25–27: sidebar order and retained functions | Exact eight-entry order, existing modal routes, casino observation in breeding suite |
| 28–33: Tank Care cleanup, individual thermostats, thermal simulation, historical reports, reflow | Inventory UI and heater suites; report count unchanged on history open; desktop/mobile overflow checks and screenshots |
| 34–37: old saves, livestock identity, offline operation, freshwater lock | Idempotent missing-ID migration, existing storage preservation, duplicate-save rejection, livestock/breeding reload checks, preparation/receiving and offline regression suites |

Initial failures identified outdated fixtures without equipment IDs, old immediate-install/seven-sidebar expectations, a wrapped navigation control and an asynchronous reload timing assumption. The hosted save flows passed, while the first final direct-file context timed out; the QA runner now releases the previously tested hosted renderer before cold file launch, retaining the same strict initialization checks and 60-second limit. The final Edge deployment suite passed all 5,162 checks. Fixtures/assertions were updated for the authorized storage workflow, the navigation layout was corrected, and reload waits for actual app readiness. The final executions listed above passed. Unperformed testing is not counted as passed.

## Limits

Storage limits are explicit: 50 equipment, 100 ordinary objects and the existing 80 recovered rocks. No new monitoring/testing products, tool-durability model or physical food-container system was invented. Existing supply quantities and reusable fragging-tool rules remain. Local browser storage availability is still subject to the existing visible save/export failure handling. Ordinary object placement explicitly selects the chosen aquarium for its preview; equipment installation and store purchases preserve the current selection. Freshwater stays locked; its biological definitions and simulation are unchanged. The 20-real-minute day, offline progression, realistic mortality, AC rewards and original artwork remain.

## Final release verification

DIST and AquariumLife-GitHub-Pages.zip are produced by `python build.py`, which verifies every copied source hash, local URL/case and archive CRC. The source archive is produced by `python tests/package.py`. Exact final build time, source count and hashes are recorded in `DIST/build-manifest.json`. Final built Inventory results are in `tests/inventory-evidence/edge-results.json`; repository-subpath/local-save checks are in `tests/pages-evidence/edge-results.json`; the release integrity verifier is `python tests/verify_sprite_production_release.py --source-archive --check-only`. These are rebuild and deployment checks, not a claim that the separate unfinished 18 sprite sheets have been produced.
