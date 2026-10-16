# Ocean diving destination artwork — v4.0.2

Implemented 2026-10-16. Master Development Prompt v4.5. Saltwater only; saves remain local.

## Changes

The eight expansion destinations previously used small code-authored SVG scenes with repeated geometric reef motifs. They now have eight distinct original 1536 × 1024 PNG environments. All original generated files were copied byte-for-byte into the project; no existing artwork was overwritten. The old expansion SVG sources are retained for history but no longer selected at runtime.

| Destination | New source in `assets/diving/` | Identity |
|---|---|---|
| Coral Triangle — Indonesia | `indonesia-reef-v2.png` | Dense colorful coral buttresses and a sheltered sand channel |
| Coral Triangle — Philippines | `philippines-reef-v2.png` | Purple foliose coral slopes and branching gardens |
| Sri Lanka | `sri-lanka-reef-v2.png` | Golden rocky shelves, boulders and sparse coral patches |
| Marshall Islands | `marshall-reef-v2.png` | Open pale-sand atoll lagoon and scattered bommies |
| Maldives | `maldives-reef-v2.png` | Bright coral shelf dropping into open sapphire water |
| Australia | `australia-reef-v2.png` | Great Barrier Reef branching/table-coral terraces |
| Florida | `florida-reef-v2.png` | Atlantic limestone, sea fans, sponges and brain corals |
| Mariana Trench | `mariana-deep-v2.png` | Dark hadal escarpment, sediment, tethered research lander and lamps |

The built-in imagegen tool generated each asset from a separate regional prompt. Full final prompts, exact saved paths and original generated filenames are preserved in [assets/diving/art-prompts.json](assets/diving/art-prompts.json). These are presentation backgrounds, not a change to collectible species availability or an automatic approval of livestock artwork. Implementation is complete for user art review.

The central destination registry now assigns an `art` entry for every supported region/mode, including all eight unchanged Fiji/Caribbean/Hawaii/Japan PNG backgrounds. The picker, map and results accent all resolve the same assigned source. The map crops proportionally to its 880 × 560 canvas; previews and result banners use `object-fit: cover`. Text stays on solid panels. Images preload once and animation reuses decoded assets. No new loading screen or network dependency was added.

Runtime reports failed/missing art explicitly in diagnostics; the build refuses missing, duplicate or misassigned destination artwork and regenerates the embedded local art data. There is no unrelated-region fallback. All 17 runtime art records (16 environments plus equipment) are packaged offline.

## Files modified

- Runtime: `js/diving-art.js`, `js/diving-ui.js`, `js/diving-data.js`, `js/diving-art-data.js`, `css/diving.css`, `index.html`.
- Registries/assets: `assets/diving/registry.json`, `assets/diving/art-prompts.json`, eight new PNGs listed above.
- Build/QA: `build.py`, `tests/pack_diving_art.py`, `tests/browser_qa.py`, `tests/diving_qa.py`, `tests/location_art_qa.py`, `tests/pages_qa.py`, `tests/package.py`, `tests/verify_location_art_release.py`.
- Documentation: `MASTER_DEVELOPMENT_PROMPT.md`, `PROJECT_CONTINUITY_SOURCE.md`, `ART_DIRECTION.md`, `ART_GENERATION_RECORD.md`, `DEVELOPMENT_STATUS.md`, `UI_SPECIFICATION.md`, `README.md`, `GAME_DESIGN.md`, `TEST_REPORT.md`, `GITHUB_PAGES_BUILD_REPORT.md`, this report.
- Evidence and one-time installation records: `tests/location-art-evidence/`, `planning/location-art/`.
- Release artifacts: `DIST/`, `AquariumLife-GitHub-Pages.zip`, `AquariumLife-v0.1.zip`.

## Verification

Actual offline browser checks: **Chrome 147 passed / 0 failed; Edge 147 passed / 0 failed**. Every one of the 16 region/mode previews loaded. All 14 launchable combinations were launched using actual UI controls, displayed their assigned backgrounds and returned to their matching result accents. Hawaii's two observation-only launch restrictions stayed enforced; its preserved backgrounds were decoded and drawn directly without bypassing the restriction. New destinations fit 1920 × 1080, 1600 × 900, 1366 × 768 and 390 × 844 layouts. Expedition save/parse and a real browser reload succeeded. No missing image elements, uncaught exceptions or HTTP/HTTPS requests occurred during the offline suite. Evidence: `tests/location-art-evidence/{chrome,edge}-results.json` and screenshots.

Full built-game regression and release integrity results are recorded in `tests/location-art-evidence/release-validation.json` after final packaging. These include the repository-subpath native PNG requests, original mystery/reveal/oxygen/catch rules, universal receiving, emergency sales, preparation, local accounts and save flows. Source hashes separately verify that gameplay authorities, species pools, old art, genetics and the freshwater lock have not changed.

| Final suite | Passed | Failed |
|---|---:|---:|
| Chrome offline artwork / actual destination UI | 147 | 0 |
| Edge offline artwork / actual destination UI | 147 | 0 |
| Chrome built Pages / gameplay / local saves | 702 | 0 |
| Edge built Pages / gameplay / local saves | 702 | 0 |
| Total browser assertions | **1,698** | **0** |

Initial Chrome attempts intermittently timed out on navigation from the synthetic HTTP test site into a local file after network-emulation changes. Direct local-folder launch had already passed in the offline artwork suite; one sequential Pages replay also completed that navigation. The harness now checks standalone extracted-folder use in a fresh offline tab, with its own navigation result and resource monitoring, preserving the independently tested hosted profile. The completed Chrome replay passed all 702 checks without increasing the timeout or changing game code. One interim documentation hash mismatch was corrected by rebuilding. Initial failure evidence is retained as `chrome-first-pages-attempt.json`; final totals above use the completed successful suites. Load timing depends on the PC; no FPS or low-memory-device benchmark is claimed.

Visually inspected the eight original PNGs and representative actual Chrome/Edge map, picker, mobile and result screenshots. Mariana is dark with localized research lighting, no shallow tropical reef art. Original generic salvage/terrain icons, movement grid and static diver/drone sprites are retained; no new animation or terrain collision redesign is claimed. Binary PDF regeneration remains pending; full printable continuity source is updated. No gameplay/save restrictions were removed and no remaining implementation blocker is known.
