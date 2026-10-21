# Interactive saltwater tutorial overhaul

October 20, 2026 - playable v4.2 - consolidated master v4.12

The passive corner tutorial has been replaced with a guided, persistent real-action experience. Twenty-two tasks cover the twelve requested phases. Progress requires genuine state or interaction evidence; there is no Next-button completion path.

## Implementation

1. **Old interface removed.** Removed the corner panel, static lesson array and Next/Back/Show me progression. Existing selection-outline behavior, freshwater UI lock and survival notifications remain. Legacy tutorial exports delegate to the new interface without an old completion bypass.
2. **Contextual spotlight.** Actual DOM IDs/data attributes identify navigation, tabs, stock cards, product forms, destinations, equipment, readings, placement canvas and inspectors. A concise tooltip, visible outline and optional dim regions follow real element bounds and clipped scroll containers. The target stays clickable; only the tooltip accepts pointer events. Resizing, scrolling, native modals and dynamic listings are handled. Missing controls produce one recoverable diagnostic per unresolved context, working controls and no false completion.
3. **All twelve phases.** Welcome and real tank selection/view; sand/depth, filling and preparation; exclusive installed filtration/controller/circulation; relevant shelter placement; measured temperature/salinity; actual nitrogen cycle; current water verification; actual Saltwater Fish navigation; requirements/price; real destination/checks/atomic stocking and observation; compatible manual feeding/actual appetite/inspection; verified completion. The [state registry](TUTORIAL_STATE_MACHINE.md) lists every stable task ID, context, expected action, validation and recovery.
4. **Authoritative validation.** Existing Core, Preparation, installed Inventory, Thermal, Sim, StoreRules, medical, receiving and Finance services supply evidence. Page opening alone cannot install gear, prepare water, establish bacteria, own a fish or feed it. Tutorial controls never click gameplay actions, change chemistry or advance time. The existing fishless-finish shortcut is unavailable while the active/paused guide is pinned; ordinary speed controls remain.
5. **Correct receiving context.** Ordinary Store confirmation already purchases and stocks a fish atomically, so the guide teaches that transaction rather than creating a second fee or artificial holding screen. All owned aquariums remain listed with compatibility explanations. The guide reuses shared checks. Current-resident readiness avoids counting the same fish twice; incoming checks retain all existing residents and treatment courses. Shared quantity diagnostics now consistently use the actual incoming count for social group, adult load and entity capacity. Diving still defaults to one individual. No biological threshold or price is changed by that quantity support.
6. **Existing players.** Genuine prepared/cycled tanks, functioning installed units, existing shelter, owned residents and recorded individual meals are recognized. No unnecessary aquarium/fish repurchase, emptying or recycling is required. Established bare-bottom tanks do not need new sand unless the species requires it; species-specific shelter remains legitimate. Old passive completed/skipped guides keep opt-out; old Next clicks are not converted to false interactive milestones.
7. **Control and recovery.** Pause/Resume, confirmed Skip/Restart, View Current Objective and completion review work. Restart resets guidance only and retains bounded diagnostic history. Aquarium switching does not retarget the guide; Settings allows deliberate guide-tank selection without switching the player's aquarium or moving assets. Sold/missing tanks and unavailable fish recover safely, clearing inappropriate current-subject evidence while retaining actual mortality and ownership history.
8. **Persistence and logging.** Main save schema stays2; `update29.tutorial` becomes version2. Stable current task, verified milestone evidence, pinned tank/fish, relevant interaction/feeding data, status, completion time and bounded history persist locally. Arbitrary old step/status writes reject. Save/load and real Continue restore context without processing elapsed time in tutorial code. Failed local storage cannot invent a successful-save event. Settings > Local Debug Log exposes the last200 sequenced tutorial events and local JSON export; this build had no separate debug-log service to reuse. [Full schema and migration](TUTORIAL_SAVE_SCHEMA.md).
9. **Accessibility.** Text plus visible outlines avoid color-only guidance. Existing native controls, keyboard focus/Enter placement, modal dismissal and normal confirmations remain. Reduced motion uses static highlights. No rapid reactions are required. Tested geometry covers scene/sidebar and native modal targets at desktop and phone sizes.

## Economy, biology and data preservation

No new tutorial AC/XP reward or free fish is introduced. Actual first-size/species rewards and existing quests remain independently governed and recorded. The configured five-percent compatible-pair offer is preserved and optional. All accounts, wallet/receipts, RNG streams, species/genetics, installed/stored physical identities, medical state and mortality history retain their authorities. Freshwater remains locked; no freshwater biological development is added. One game day is still20 real minutes; cycling still uses36 game hours in the existing model. Guide code never restores deceased livestock or writes safe water values.

The pre-tutorial release comparison preserves **2,481 runtime/data/artwork files byte for byte**. After removing only the new tutorial observer hooks and normalizing line endings, Core and simulation bodies match their baseline exactly. Thermal, hunger, health, mortality, equipment-aging, breeding, prices, rewards, pair-offer and art modules are among the protected files. Evidence: `tests/tutorial-evidence/protected-runtime.json`.

## Actual executed source tests

| Suite | Result |
|---|---|
| Full interactive tutorial, Edge | **142 passed, 0 failed** |
| Existing economy/service/sale/save, Chrome | **85 passed, 0 failed** |
| Long-term equipment and live/offline reliability, Chrome | **787 passed, 0 failed** |
| Simplified care/menus, Chrome | **106 passed, 0 failed** |

The tutorial browser suite starts through the real New Game flow, buys/places sand, fills/prepares actual water, purchases and installs three real units, rejects duplicate installation, cancels/commits keyboard rock placement, saves a real thermostat, waits for gradual heating, processes the full36-game-hour cycle through ordinary five-minute steps, reviews actual water, buys another real empty tank, verifies both receiving choices including its disabled unprepared destination, buys an eligible current fish listing, verifies the exact debit plus approved species reward, feeds one compatible inventory portion, waits for the individual's actual meal record and opens the actual inspector. The exercised listing was an actual supported Percula variety in the fixed initial scenario, rather than a forced Ocellaris exception. The guide can recommend any qualifying implemented current starter listing.

It also exercises supported old saves, real established ownership/meal evidence, pause/resume, confirmed skip/restart, no fake Next/ticket completion, bounded debug logging and storage failure rollback, group quantity and same-species treatment safeguards, aquarium switching/selection, sold last tank, fish loss, current completion-time preservation, actual browser reload/Continue, no remote requests and freshwater lock. Screenshots and geometric checks cover **1920x1080, 1600x900, 1366x768 and390x844**, including modal and sidebar alignment. An independently opened financial window keeps the recovery target inside its active native modal. Desktop and phone screenshots were visually inspected.

Reliability execution includes actual8/12/24-real-hour equivalence with live simulation, repeated-sync no-replay checks and provisioned livestock survival. Those results preserve current equipment/water/health behavior; they are not a guarantee for every unprovisioned tank.

The completed rebuilt-DIST tutorial/reliability, economy and Pages/local-save runs, manifest hashes and release gates are recorded after build in `tests/tutorial-evidence/release-results.json` and corresponding actual browser outputs. Final byte/CRC verification compares both ZIPs with current source and DIST. Reproduce with:

```
python tests/browser_qa.py edge --tutorial
python tests/browser_qa.py chrome --simplify
python build.py
python tests/browser_qa.py chrome --tutorial --dist --with-reliability
python tests/browser_qa.py edge --economy20 --dist
python tests/browser_qa.py edge --pages
python tests/package.py
python tests/verify_sprite_production_release.py --source-archive --check-only
```

## Required 28-case mapping

| Requested cases | Executed evidence |
|---|---|
|1-6 New launch, actual targets/tabs, no Next, resizing, modals|New marine start; real sidebar/tab clicks; forged completion/ticket rejection; modal/sidebar geometry at four widths; installation dialogs|
|7-12 Aquarium, sand, preparation, equipment, exclusive Inventory, rock|Actual second-tank purchase; exact sand price/depth; fill separate from preparation; three purchases/installations; repeat-install rejection; canceled placement no charge and actual Enter placement|
|13-15 Temperature, real readings, no cycle bypass|Real thermostat form with ordinary thermal drift tolerance; positive warm-up steps; authoritative receiving/nitrate values; guarded legacy finish dispatch; full36-hour cycle through fixed steps|
|16-20 Compatible fish, money, receiving, stocking, feeding|Actual affordable current listing; exact paid receipt/approved50AC species reward; both owned choices with disabled rejection; permanent identity; no Feeding-page-only completion; compatible portion and actual meal|
|21-26 Persistence, existing players, pause/resume, safe skip, missing targets, switching|Actual reload/Continue plus validated JSON; legacy opt-out/state recognition; paused ecosystem still advances; separate confirmation; one diagnostic/recovery; pinned aquarium and real selector|
|27-28 Offline and freshwater lock|Network-disabled execution/no external requests; local save restoration; disabled freshwater start and retained-water rejection model tests|

## Failures resolved and limits

Development checks caught an exact-temperature assertion that needed tolerance for normal intervening simulation ticks; a raw second-tank fixture that bypassed ordinary mortality-history initialization; a sale fixture assuming only one aquarium after a second real purchase was added; and an initial social-count diagnostic still adding one instead of the actual batch. These were corrected without weakening water/quarantine safeguards. The full Pages suite also caught an invertebrate capacity display that referenced the new fish-only quantity; the non-fish helper body was restored to its exact baseline and a dedicated regression was added. Restart initially cleared useful debug events; bounded profile history is now retained. Skip verification excludes only the existing automatic initial asset-value history entry, while still checking money, XP, time, RNG, physical contents and absence of false setup. Final listed source runs have no remaining failures.

The guided starter recommendation uses supported group-one beginner profiles; it does not invent captive-care data for unverified species. Legitimate insufficient funds, unavailable daily stock, equipment faults, incompatible water, actual treatment restrictions or missing shelter can block progress. The guide explains recovery and offers deliberate pause/skip; it does not grant exceptions. The ordinary twenty-minute day and full offline obligations remain. Windows Chrome/Edge were tested; Safari/Firefox and screen-reader software were not executed. The system supplies labeled native semantics, but does not claim a separate screen-reader audit. Existing unrelated incomplete livestock art and binary-PDF work remain separate earlier limits. No additional permission is required to use this completed tutorial.

## Files modified

New runtime: `js/tutorial.js`, `js/tutorial-ui.js`, `css/tutorial.css`.

Runtime integration: `index.html`, `js/core.js`, `js/save.js`, `js/simulation.js`, `js/update29.js`, `js/update29-ui.js`, `js/ui.js`, `js/store.js`, `js/inventory-ui.js`, `js/diving-receiving.js`, `css/update29.css`.

Documentation: this report, `TUTORIAL_STATE_MACHINE.md`, `TUTORIAL_SAVE_SCHEMA.md`, current additions in `GAME_DESIGN.md`, `UI_SPECIFICATION.md`, `DEVELOPMENT_STATUS.md`, tutorial/persistence/UI/QA home sections of `MASTER_DEVELOPMENT_PROMPT.md` and its exact full copy in `PROJECT_CONTINUITY_SOURCE.md`. All31 major sections remain.

QA/release: new `tests/tutorial_checks.js`, `tests/tutorial_qa.py`, `tests/browser_qa.py`, updated confirmed-skip regression in `tests/economy_update_qa.py`, superseded passive expectations in `tests/update29_checks.js` / `tests/update29_qa.py`, current version expectation in `tests/pages_qa.py`, `build.py`, `tests/package.py`, `tests/tutorial-evidence`, rebuilt DIST and both release ZIPs. Original requested specification and pre-edit tutorial/master sources are retained under `planning/interactive-tutorial`.
