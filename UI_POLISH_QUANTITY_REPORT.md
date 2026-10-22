# UI polish and store quantity update — v4.3.1

Implemented and verified in the source and rebuilt DIST. All6463 executed browser/regression assertions passed. The final release verifier checks source/DIST/ZIP byte identity, original assets and exact documentation continuity.

The familiar left sidebar, top utility bar, centered aquarium, header aquarium controls and right wellbeing column remain in place. A445-byte64×32 local SVG repeats behind the general interface on black. Its staggered quadratic scallops bow downward; dark-grey strokes at45% opacity stay quiet. This static CSS background adds no drawing loop, timer, filter or Canvas overlay. Navigation text, buttons and slate-blue panels retain solid surfaces. Panel/field/action spacing, header control and store button heights, selected/hover/focus states and purchase totals are consistent.

## Purchase behavior

The original Core.act cloned transaction, StoreRules, Finance and immediate local save remain the single pipeline. Shared policy/quote enforces integer1–99, current stock, wallet, inventory capacity and existing destination/access rules before mutation. Equipment creates separate physical identities/reliability records; foods and supplies add their existing portions/doses; medical packs merge within1000-unit batches/80-batch capacity; rated parts use existing stacks. Multiple ordinary rocks create separate stored IDs for individual placement. One rock keeps direct placement. Each order makes one full debit and receipt, with quantity, unit price, total and physical item IDs where appropriate. UI submit lock plus persistent financial receipt keys prevent duplicate/replayed orders even after eviction from the recent100-token ring.

Supported bulk categories: equipment (including fixed heaters/Deep Market containment), food, consumable/mounting supplies, ordinary medicines/diagnostics, rated service parts and ordinary rocks. Individual purchases: substrate installation, decorations, mounted racks, reusable fragging tools, restricted dealer medicine batches. Fish retain the existing resident-count flow; corals, invertebrates, eggs, mysteries and breeding pairs retain individual biology, assessment, mounting and saved-offer/roll rules. No livestock may enter ordinary storage. See STORE_QUANTITY_RULES.md for exact limits.

Details show Unit Price / Quantity / Total Cost and instantly update without rebuilding the store. Minus/numeric/plus inputs support keyboard interaction. Invalid, unaffordable, unavailable or oversized orders disable confirmation and explain the check. Core repeats every guard for direct/stale submissions. Selected aquarium, inventories, livestock and historical receipts survive save/load; no save-schema reset, biological rate, reward or offline change is introduced. Freshwater stays locked.

## Files

- Runtime: js/store.js, js/store-rules.js, js/core.js, js/equipment-inventory.js, js/livestock-market.js, js/equipment-parts.js, js/finance.js; js/ui.js and index.html version labels.
- Visuals: css/ui-cleanup.css, assets/ui/downward-scales.svg. Original art is untouched.
- Documentation: MASTER_DEVELOPMENT_PROMPT.md v4.15 (31 homes), exact PROJECT_CONTINUITY_SOURCE.md, UI_SPECIFICATION.md, DEVELOPMENT_STATUS.md, STORE_QUANTITY_RULES.md, FINANCIAL_TRANSACTIONS.md, EQUIPMENT_INVENTORY.md, README.md, TEST_REPORT.md, GITHUB_PAGES_BUILD_REPORT.md, GITHUB_PAGES.md and this report.
- Build/QA: build.py, tests/package.py, tests/browser_qa.py, tests/ui_quantity_checks.js, tests/ui_quantity_qa.py, tests/pages_qa.py, tests/verify_ui_quantity_release.py and tests/ui-quantity-evidence. Planning scripts/baseline are historical implementation evidence, not runtime dependencies.

## Actual validation

| Executed command / target | Passed | Failed |
| --- | ---: | ---: |
| Chrome `--ui-quantity` / source |164|0|
| Edge `--ui-quantity --dist` |164|0|
| Chrome `--tutorial-audit` / source |72|0|
| Chrome `--economy20` / source |85|0|
| Chrome `--equipment-reliability` / source |787|0|
| Edge `--pages` / DIST at HTTP repository subpath and file URLs |5162|0|
| Chrome `--performance --checks-only --dist` |29|0|
| **Total** |**6463**|**0**|

The quantity suite includes117 model checks covering every marine-compatible equipment type and every ordinary medical product, full order failures, one debit/receipt, exact stock, separate identities, dose/part stacks, medicine batch overflow, rock storage and safe placement, final-validation rollback, sensitive-item restrictions, replay beyond the recent token window and JSON round trips. Trusted pointer/text input exercises actual minus/plus/numeric controls, instant totals, invalid/fractional/empty quantities, purchases, immediate duplicate submit, selected aquarium retention, Deep Market equipment, sidebar state and actual browser save/reload. Network is disabled in both quantity suites. The Pages suite separately checks repository-relative deployment, local origins, export/import and existing receiving/diving/art systems. Reliability checks include8/12/24-hour live/offline parity, survival and repeated-login guards. Tutorial completes the real90-second accelerated fishless cycle and all22 tasks. Economy preserves pair-offer pricing and existing single-unit flows.

Images were captured at1920×1080,1600×900,1366×768 and390×844 in both browsers. Representative desktop/mobile images were visually inspected: scales hang downward, solid panels and labels remain readable, the aquarium is uncovered, header/right-panel alignment and responsive stacking are retained. The texture was softened after initial inspection. Selected/hover surfaces stay solid. The445-byte SVG uses a static repeat; production adds no timer or rendering loop.

Same-scene three-second samples, with a short warm-up:

| Browser | Pattern off FPS | Pattern on FPS | Off / on mean Canvas draw |
| --- | ---: | ---: | --- |
| Chrome |60.31|60.26|0.58 /0.51ms|
| Edge (DIST) |59.98|59.90|0.57 /0.50ms|

These short headless software-rendered samples show no noticeable regression in this fixture; they are not physical GPU or all-hardware benchmarks. Current scheduler/cache/settings regressions passed separately. Original protected art/data is hash-checked; unchanged biological/economic modules include simulation, offline, thermal, breeding, progression, preparation, diving/receiving, casino and update29 authorities.

Test harness corrections during verification: native number inputs explicitly select existing text before trusted insertion; selected-state assertions wait for the existing120ms transition. The old Pages check still expected the obsolete sidebar labelv4.2.1; it now requires the version from the actual build manifest while retaining every mystery-service assertion. Final suites were rerun and passed; no production safeguard was removed to pass a test.

Build with `python build.py`; source package with `python tests/package.py`. The former regenerates file transports and manifest, verifies source hashes/case-sensitive URLs and CRC-checks the root-level Pages ZIP. The latter CRC-checks the portable source ZIP. `python tests/verify_ui_quantity_release.py --source-archive --check-only` independently checks every source/DIST/Pages byte, every archived source file, all2368 protected original assets, current quantity-suite runtime hashes and the exact31-section master embedded in continuity. Evidence and actual assertion counts are in tests/ui-quantity-evidence; all saves remain local.

## Limits

Bulk quantities cap at99 and remain bounded by each catalog/storage limit. Placement-based single installations and sensitive livestock do not get a generic bulk multiplier. Local saves belong to the browser/site origin; existing export/import moves them between origins. Original incomplete shrimp artwork and the prior ungenerated binary PDF remain separate historical limitations; this update neither changes nor claims them complete.
