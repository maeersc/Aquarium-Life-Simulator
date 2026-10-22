# Complete interactive tutorial audit and loop repair

October 21, 2026 - playable v4.2.1 - consolidated master v4.13

## Confirmed root causes and reproduction

A disposable new marine profile was exercised with trusted browser pointer input, following the highlighted controls. This differs materially from the earlier synthetic-click tests, which also jumped straight to known screens and did not prove the highlighted route.

1. **Covered initial canvas and navigation bounce.** `view` highlighted `#aquarium`, while `#empty-tank` covered the entire canvas and intercepted real pointer input. Its visible `#onboard-action` was not a recognized viewing interaction. The original first click could run the normal Prepare action; later clicks opened Aquariums, where the guide requested Close and returned to the still-covered canvas. The trace records repeated `view` routes (`scene-null` / `close-primary`) with no new viewing evidence. Baseline evidence: `before-covered-target.json/.png`, `before-navigation-loop.json/.png` in `tests/tutorial-audit-evidence`.
2. **Native event ordering.** The capture listener used a microtask to inspect UI outcomes. Trusted browser events can checkpoint microtasks between capture and later target/bubble handlers, so navigation/details could be read before they had opened. This explained the missed first welcome navigation and could reject an actual opened fish listing, sending the player back to open it again. Synthetic `.click()` inside one evaluated JavaScript stack masked this ordering problem.
3. **Retained closed-dialog HTML.** Queries for destination forms, product markers and thermostats were not consistently gated by an open details dialog. After equipment installation a retained `#inventory-destination` could divert `hardscape` to a hidden installation form. Closing purchase details could similarly leave the guide aimed at an invisible product/form. The repair covers shared active-details discovery, not a single species or one early step.
4. **Tooltip over the price report.** Visual review showed that avoiding only the target button could still cover destination, quantity or price information. Placement now protects the full active purchase/installation/thermostat form, with direct non-overlap and real hit tests at all four widths.

## Repairs and transition safety

The initial guide now highlights the visible empty-tank setup button. During `view`, its normal handler opens Tank Setup for review instead of performing Prepare. A verified real navigation interaction completes the viewing requirement; sand, Add water and Prepare water remain separate player actions. No task is silently skipped, no state is made biologically safe, and no reward is granted.

Capture immutable event metadata, then inspect the UI in a later timer task after native handlers finish. Fence pending jobs by the original account and task, retaining one-use interaction tickets and the bind-once listener guard. Add an observer reentrancy guard. Physical-state recognition remains idempotent, and reviewing the same product no longer erases valid destination review. A genuinely different listing invalidates only listing-specific review.

All product/destination/thermostat discovery now requires an open details dialog. Recovery chooses a visible control. Store search and equipment filters receive specific clearing instructions. Prices, lack of AC and depleted stock remain legitimate blockers, with actual reports and existing Progress > Objectives or normal restock guidance. If room temperature is already suitable and no controller is required, the temperature objective can wait for genuine ambient adjustment rather than demand an unnecessary heater.

`AL.Tutorial.diagnostics.enabled` is an explicit development-only opt-in, false by default. A bounded in-memory trace detects repeated unresolved routes without changed milestones, logs previous/current step, event, result and prerequisite checks once per unchanged progress state, and never advances, resets or rewards progress. Rendering alone and ordinary cycling/meal waiting do not create loop events.

## Complete corrected flow

The guide has22 stable IDs in12 phases. The graph is a chain with explicit prior-task prerequisites and one terminal completion. The current objective is the first missing required evidence. Real pre-existing physical states can satisfy later prerequisites early; this is recorded state recognition, not automatic installation or invented progress.

| Current step | Actual required action/context | Completion condition | Next |
|---|---|---|---|
| `welcome` | Aquariums / My Aquariums | Real Aquariums navigation has completed. | `aquarium` |
| `aquarium` | Aquariums / selection or new purchase | An owned marine tank is pinned to this guide. | `view` |
| `view` | Main aquarium | Actual empty-tank setup-button navigation or a canvas interaction is recorded. | `substrate` |
| `substrate` | Store / Saltwater / Sand | Positive actual sand depth when the selected tank/species requires sand. | `fill` |
| `fill` | Aquariums / Tank Setup | Preparation.filled reports actual water present. | `prepare` |
| `prepare` | Aquariums / Tank Setup | Preparation.prepared reports completed saltwater preparation. | `filter` |
| `filter` | Tank Care / Inventory or equipment store | Core.has confirms operational installed filtration. | `controller` |
| `controller` | Tank Care / installed controller or Inventory | A suitable installed controller, or species-safe room conditions, is verified. | `flow` |
| `flow` | Tank Care / Inventory or equipment store | Core.has confirms operational installed circulation. | `hardscape` |
| `hardscape` | Inventory or Store / Rocks, then aquarium placement | Actual rock/cave is placed when the tank/species requires shelter. | `temperature` |
| `temperature` | Actual readings or installed thermostat | Actual prepared water lies within the selected species temperature and salinity ranges. | `cycle` |
| `cycle` | Tank Setup then actual chemistry | Preparation.state reports the real nitrogen cycle established. | `quality` |
| `quality` | Actual aquarium water readings | All shared species-aware receiving checks and nitrate threshold pass; the player reviews readings after cycle verification. | `shop` |
| `shop` | Store / Saltwater / Fish | Actual Saltwater / Fish shop interaction is recorded. | `details` |
| `details` | Actual fish listing details | A currently compatible supported starter listing has actually opened with its care and price. | `destination` |
| `destination` | Purchase destination and compatibility report | Pinned destination and that same listing compatibility report have both been reviewed. | `stocking` |
| `stocking` | Existing atomic purchase confirmation | A living permanently owned fish belongs to this tank through the existing transaction. | `observe` |
| `observe` | Main aquarium | A real canvas observation occurs while that resident is alive and owned. | `feed` |
| `feed` | Tank Care / Feeding | A compatible manual portion decrements inventory; documented prior feeding may satisfy returning players. | `appetite` |
| `appetite` | Main aquarium / real meal | The individual records a real meal after that portion; prior recorded meals remain valid for existing players. | `inspect` |
| `inspect` | Living fish inspector | The actual living resident inspector opens for the guide fish. | `complete` |
| `complete` | Completion summary | All21 prior milestones, living owned resident and current passing readiness checks are present. | Terminal |

## Targets and player language

Removed the initial requirement to click through the empty-tank panel. Closed installation destinations and canceled product details are no longer active targets. Actual stable controls are used for Aquariums, Tank Setup, Add water, Prepare water, Aquarium Store, Saltwater, Fish, Sand & Substrate, Equipment, Tank Care, Installed Equipment, Inventory, Install, destination review, Confirm purchase, Feeding and Livestock Collection. No removed Breeding & Eggs, standalone Temperature Control, Overnight Readiness or freshwater path is introduced.

Instructions now name View Details, Substrate depth (inches), Equipment category / All Equipment, Search items, Thermostat setting and Save thermostat. They explain ordinary waiting and overfeeding simply, and keep implementation and transaction details in this report. A positive sand depth, not merely opening its product, is required. A canceled rock preview remains unplaced. The guide still uses real shared Store/receiving safeguards and the existing five-percent optional pair offer.

## Saves, existing players and interruptions

Main schema2, update29.version1 and tutorial.version2 remain. No player data, finances, RNG streams, equipment/livestock identities, genomes, origin, illness, deaths or physical assets are reset. Existing prepared/cycled water, installed devices, shelter, livestock and documented individual meals are recognized. Historical completed tasks are not erased merely because of ordinary navigation. Current stocking safety is still revalidated.

Uncommitted native purchase dialogs are intentionally reopened through the guide after a reload. They are not serialized as pending payments or replayed actions. The same product retains its review evidence; the normal Store/Inventory identity and receipt guards continue to prevent duplication. Per-profile jobs and transient diagnostics do not become saved completion evidence. Switching tanks retains the pinned guide aquarium; explicit guide-tank changes and actual loss of a fish/tank keep their established recovery rules.

## Executed tests and release evidence

Final actual suite results are recorded here after execution. No unit-only result is labeled a browser walkthrough. The previous `TUTORIAL_OVERHAUL_REPORT.md` and its original evidence are historical and do not prove the original trusted-pointer route was traversable.

| Actual executed source suite | Result |
|---|---|
| Clean-profile highlighted A-F walkthrough, Edge | **60 passed, 0 failed** (before the final twelve added QA assertions) |
| Expanded B-E recovery and real modal/purchase hit tests, Edge | **56 passed, 0 failed** (reuses actual clean-walkthrough saves; does not claim a second clean walkthrough) |
| Existing tutorial, migration, save, pause/restart and target regressions, Chrome | **142 passed, 0 failed** |
| Long-term equipment and live/offline reliability, Chrome | **787 passed, 0 failed** |
| Economy, rewards, service, sale and save regressions, Edge | **85 passed, 0 failed** |

The final expanded A-F suite has72 assertions. It is repeated against rebuilt DIST, followed by reliability/economy/Pages checks. Actual released-build results, entries, times and hashes are recorded in `tests/tutorial-audit-evidence/release-results.json` and the corresponding browser JSON. The final release gate compares current source, DIST, Pages ZIP and portable source ZIP; no source-only result is represented as a DIST browser run.

Protected-file comparison confirms **2,507 runtime/data/art/CSS files unchanged**, including Core, simulation, preparation, Finance and shared receiving. Evidence: `tests/tutorial-audit-evidence/protected-runtime.json`.

The new A-F suite starts through real New Game with the unchanged starting wallet including the existing first-size reward (5,250 AC), follows highlighted targets with trusted pointer/key events, pays the actual prices and installs real Inventory units. It uses the existing20x speed button and wall-clock browser simulation for the full36-game-hour cycle, with no test call to Sim.step/advance, bacteria edits or chemistry edits in the clean walkthrough. Food is consumed through the actual feeding/meal system. Baseline and step-by-step before/after traces are retained.

B covers an established aquarium by deliberately restarting guidance through its Settings confirmation, then following actual highlights without repurchases. C restores actual saved states captured during A and performs real save/reload/Continue during preparation, equipment installation, active cycling, fish purchasing and receiving. D uses disposable negative copies for money, equipment, tank volume, stock, missing controls and interrupted dialogs. E checks layout and actual purchase hit testing at1920x1080,1600x900,1366x768 and390x844. F evaluates every prerequisite/next edge, reachability, the terminal state, idempotence, retained ownership and opt-in loop diagnostics.

Development checks found two fixture assumptions: the legacy Config value did not include the approved starter-size reward, and Continue may display an ordinary welcome-back modal before a speed control is accessible. An insufficient-AC fixture also initially edited the wallet before save validation; it now uses a recorded Finance debit, preserving ledger reconciliation. These fixtures were corrected without changing the starting balance, simulation, modal safeguards or rewards. Adding the new report to the build initially omitted a Path prefix for the old tutorial report; this packaging-only error was corrected before producing the release. The original probe was a diagnostic trace, not a passing A-F test; final suites require genuine completion and return failure on unresolved repetition.

## Files modified

Runtime: `js/tutorial.js`, `js/tutorial-ui.js`, `js/ui.js`; release version in `index.html`. The simulation, Core transaction implementation, preparation authority, Finance, all species/art and shared receiving module remain unchanged in this repair.

QA/release: `tests/tutorial_audit_qa.py`, `tests/tutorial_audit_extra.py`, `tests/tutorial_audit_checks.js`, `tests/browser_qa.py`, current-version expectation in `tests/pages_qa.py`, `tests/package.py`, `build.py`, `tests/tutorial-audit-evidence` and `planning/tutorial-loop-repair`.

Documentation: this report, `GAME_DESIGN.md`, `UI_SPECIFICATION.md`, `DEVELOPMENT_STATUS.md`, `TUTORIAL_STATE_MACHINE.md`, `TUTORIAL_SAVE_SCHEMA.md`, authoritative tutorial/persistence/UI/QA homes in `MASTER_DEVELOPMENT_PROMPT.md`, and its exact complete31-section copy in `PROJECT_CONTINUITY_SOURCE.md`. The new permanent traversability requirement is written once in the master tutorial home, not duplicated across unrelated systems.

## Remaining limits

Legitimate insufficient AC, unavailable stock until normal rotation/restock, inappropriate species/tank size, equipment faults, unsafe water and medical restrictions remain enforceable requirements. Guidance explains recovery and preserves Pause/Resume/confirmed Skip. It does not create money, items or safe water to bypass a blocker. The guided single-fish recommendation still uses supported group-one beginner species; it does not invent missing captive-care data.

Chrome/Edge are the browser targets exercised for this repair. Safari, Firefox and assistive screen-reader software are not claimed tested. Previous unrelated missing sprite-production/PDF work is outside this tutorial repair and is not claimed completed. Any new test failure or unverified critical route must be resolved or explicitly reported before completion.
