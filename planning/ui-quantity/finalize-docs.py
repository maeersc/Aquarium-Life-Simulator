from pathlib import Path
import json
R=Path(__file__).resolve().parents[2]
p=R/'MASTER_DEVELOPMENT_PROMPT.md';old=p.read_text(encoding='utf8');s=old
start=s.index('## 24.17 Store Quantity Persistence');end=s.index('## 24.16 Graphics Preference Persistence',start);block=s[start:end];s=s[:start]+s[end:];s=s.replace('# 25. GRAPHICS ENGINE, ANIMATION & PERFORMANCE',block+'# 25. GRAPHICS ENGINE, ANIMATION & PERFORMANCE',1)
p.write_text(s,encoding='utf8');p=R/'PROJECT_CONTINUITY_SOURCE.md';c=p.read_text(encoding='utf8');assert c.count(old)==1;p.write_text(c.replace(old,s,1),encoding='utf8')
p=R/'GITHUB_PAGES.md';c=p.read_text(encoding='utf8');i=c.index('\n')+1;p.write_text(c[:i]+'''
## Current delivery — playable v4.3.1, 2026-10-22

The current UI polish and store quantity release is rebuilt with `python build.py`. Deploy all contents of DIST, including `.nojekyll`, or extract AquariumLife-GitHub-Pages.zip at the Pages site root. Original local art and on-demand native source transports remain included. All player saves, inventories, receipts and profiles remain device-local; JSON export/import moves a collection between browser/site origins. See UI_POLISH_QUANTITY_REPORT.md and STORE_QUANTITY_RULES.md. Earlier release sections are historical where superseded.

'''+c[i:].lstrip('\n'),encoding='utf8')
p=R/'UI_POLISH_QUANTITY_REPORT.md';c=p.read_text(encoding='utf8').replace('Implementation is complete; packaged-release verification is in progress. This report is finalized with actual results before delivery.','Implemented and verified in the source and rebuilt DIST. All6463 executed browser/regression assertions passed. The final release verifier checks source/DIST/ZIP byte identity, original assets and exact documentation continuity.').replace('A small64×32 local SVG','A445-byte64×32 local SVG').replace('GITHUB_PAGES_BUILD_REPORT.md and this report.','GITHUB_PAGES_BUILD_REPORT.md, GITHUB_PAGES.md and this report.').replace('tests/ui_quantity_qa.py, tests/verify_ui_quantity_release.py','tests/ui_quantity_qa.py, tests/pages_qa.py, tests/verify_ui_quantity_release.py')
a=c.index('Pending final packaged runs.');b=c.index('\n## Limits',a)
c=c[:a]+'''| Executed command / target | Passed | Failed |
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
''' +c[b:]
p.write_text(c,encoding='utf8')
for f in ['DEVELOPMENT_STATUS.md','TEST_REPORT.md','GITHUB_PAGES_BUILD_REPORT.md']:
 p=R/f;s=p.read_text(encoding='utf8');needle='Earlier release sections below are historical where superseded.';s=s.replace(needle,'All6463 executed browser/regression assertions passed; see the current report and tests/ui-quantity-evidence for exact suites and limitations. '+needle,1);p.write_text(s,encoding='utf8')
