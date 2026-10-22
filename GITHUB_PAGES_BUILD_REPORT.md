# Aquarium Life — DIST and local-save verification

## Protected production distribution - 2026-10-22

Current master v4.17; gameplay remains v4.3.1 with a new protected distribution pipeline. Production now minifies JS/CSS, shortens internal identifiers, uses content-derived code filenames and excludes review pages, source maps, project documentation and tooling. Human-readable game code and original assets remain untouched. Assets retain their original pixels and offline file transports; no encryption, passwords, licensing dependency, profile rewrite or save-key change is introduced. Runtime safety and the mandatory performance pass take priority over obfuscation. DISTRIBUTION_PROTECTION_REPORT.md records exact mechanisms, commands, executed tests, benchmarks and limits. All7838 executed protected browser/performance/regression assertions passed; exact results, methods and limits are in the protection report and tests/distribution-protection-evidence. Earlier build descriptions are historical where superseded.

## UI polish and store quantities — 2026-10-22

Playable v4.3.1 / master v4.15. The familiar aquarium layout now uses a very subtle static downward fish-scale background, opaque slate-blue panels and consistent controls. The existing guarded store supports quantities for equipment, food, consumables, ordinary medicines, rated parts and rocks. Multiple rocks enter Inventory for separate placement; sensitive livestock, unique tools and installations retain their established individual safeguards. One total charge, distinct physical IDs, capacity/stock checks, persistent receipt replay protection and local saving remain authoritative. Main schema2/tutorial2, biological simulation, economy rates, offline time and freshwater lock are unchanged. STORE_QUANTITY_RULES.md defines category behavior; UI_POLISH_QUANTITY_REPORT.md records files, actual tests and limitations. All6463 executed browser/regression assertions passed; see the current report and tests/ui-quantity-evidence for exact suites and limitations. Earlier release sections below are historical where superseded.

## Current release — v4.3.0, 2026-10-22

Performance optimization is implemented with60FPS default, optional30FPS, independent biological time, on-demand native sheets, bounded caches, cached scenery, covered/hidden suspension and five graphics controls. The current DIST has2370source files (844,323,224bytes); its manifest records exact source hashes. GitHub Pages/local-save integration, both browsers'382-sheet checks, tutorial, equipment/offline, breeding and economy tests pass. The performance and five-minute-soak suites bring the final browser assertions to17,025with zero final failures. All2368original protected assets remain unchanged. The current Pages and portable source ZIPs are rebuilt and CRC/hash checked. See AQUARIUM_LIFE_PERFORMANCE_OPTIMIZATION_REPORT.md and tests/performance-evidence/release-validation.json for exact evidence and environmental limits. Physical GPU utilization and Netflix/audio synchronization were not measured. Native production remains382sheets/6112cells across110/113usable entries; the separate18-sheet shrimp artwork gap remains.

Earlier release sections below are historical and do not describe current counts or runtime.

### Executed v4.0.4 validation

22114 browser assertions passed across current Chrome/Edge livestock and Pages suites; zero final failures. Production16-frame sheets completed: **0**. Full artwork expansion remains unfinished; performance and source/DIST checks are detailed in LIVESTOCK_ANIMATION_16_FRAME_REPORT.md. DIST/Pages and source archives are rebuilt after this evidence update.


## Livestock16-frame expansion — playable v4.0.4 / MDPv4.7

**Partial implementation: authored artwork remains unfinished.** Audited119 marine entries in12 batches (94fish,15coral records,10invertebrates), with25 designer varieties kept separate. Added a shared validated16-frame asset path to AL.FishAnimation, an offline full-catalog review gallery and calmer existing fish timing. **Zero new production16-frame sheets are complete; all119 entries still need dedicated artwork.** One generated Ocellaris candidate failed alignment/identity checks and is retained outside deployment. Existing art, biology, local saves and freshwater lock remain. See [LIVESTOCK_ANIMATION_16_FRAME_REPORT.md](LIVESTOCK_ANIMATION_16_FRAME_REPORT.md) for each entry and actual evidence. Earlier animation reports describe the previous milestone and do not establish16-frame completion.


## Global marine fish animation audit — playable v4.0.3, 2026-10-16

Audited all 94 registered marine fish, including five acquisition-held clownfish and one fictional fish. Thirty-one have authored adult cycles; 63 previously translated static living poses. Added render-only species profiles, pixel-preserving tail/outer-fin motion, state-aware timing, banked side-profile turns and head/eye protection across three stages. No new biological species, AI/feeding/breeding rules, inheritance or saves are introduced. All 94 remain conservatively classed B (partial) because bespoke action/turn/pectoral artwork and anatomy approvals remain incomplete; this is not a claim of fully authored animation. See [FISH_ANIMATION_AUDIT.md](FISH_ANIMATION_AUDIT.md), [FISH_ANIMATION_SYSTEM.md](FISH_ANIMATION_SYSTEM.md) and [offline motion review](fish-animation-review.html).

## Ocean diving destination artwork — playable v4.0.2, 2026-10-16

Eight original pixel-art PNG environments replace the simplified expansion scenery for Indonesia, Philippines, Sri Lanka, Marshall Islands, Maldives, Australia, Florida and Mariana Trench. A central per-mode art mapping drives selection previews, proportional in-dive backgrounds and expedition-result accents. Older regional PNGs, native encounter pools, all diving gameplay, local saves and freshwater lock are preserved. See [DIVING_LOCATION_ART_REPORT.md](DIVING_LOCATION_ART_REPORT.md). Art is implemented for review; no prior livestock/art approval is changed.

## Global aquarium preparation repair — v4.0.1, 2026-10-16

Corrected the saved `prepared=true` / stale `emptyDry=true` contradiction across setup, rendering, biological readiness and all receiving hosts. Existing saves repair only from preparation completion evidence; normal chemistry alone never certifies preparation. See [AQUARIUM_PREPARATION_REPAIR_REPORT.md](AQUARIUM_PREPARATION_REPAIR_REPORT.md). Master v4.4 preserves all 31 major sections, local saves, freshwater lock and the 20-minute day. Earlier release reports remain historical where superseded.


## Global diving expansion and liquidation — playable v4.0, 2026-10-16

Implemented the authorized Emergency Diving Sales & Rock Resale and Global Ocean Diving Expansion request (specification v3.6). Seven new reef selections and Mariana remote exploration use the central registry. Catch development, medical assessment, concealed attached eggs and regular-store liquidation extend the existing receiving authority. See [DIVING_EXPANSION_REPORT.md](DIVING_EXPANSION_REPORT.md) and [DIVING_EXPANSION_SAVE_SCHEMA.md](DIVING_EXPANSION_SAVE_SCHEMA.md). Earlier milestone reports remain historical where superseded. All saves stay local; freshwater remains locked; one game day remains 20 real minutes.


## Universal ocean diving receiving — 2026-10-16

All registered diving fish, corals and invertebrates now share species-aware diagnostics and explicit saved post-boat receiving. Every owned aquarium is shown; supported coral mounts and host-compatible quarantine retain all safeguards. The repair also corrects invalid noninfectious carrier flags, rock surface discovery and missing/ambiguous host mappings. Tests enumerate the real eligible registry, plus old-save, condition, expiry, replay and future-registration checks. See [GLOBAL_DIVING_RECEIVING_REPORT.md](GLOBAL_DIVING_RECEIVING_REPORT.md). Earlier host-limited flow descriptions are historical where superseded. Game v3.9 / master v4.2; local saves and freshwater lock remain.

## Diving receiving diagnostics repair — 2026-10-16

All owned aquariums now remain visible in receiving, with disabled incompatible options, exact actual/required checks, preparation/quarantine guidance, live eligibility refresh and the unchanged finite holding countdown. Properly prepared 80-gal marine tanks at exactly 27°C can receive Chalk Bass subject to existing transport survival; legitimate safeguards remain enforced. See [DIVING_RECEIVING_REPAIR_REPORT.md](DIVING_RECEIVING_REPAIR_REPORT.md) for the confirmed UI cause, data audit, files, tests and the limits of identifying an unsupplied player save. Current gameplay stays v3.9 / master v4.2, with local saves and freshwater lock preserved.

## v3.9 final verified release — 2026-10-15

**1288 selected browser/model/deployment checks passed, zero failed.** Both browsers passed the mystery feature and built Pages/local-save flows; existing diving/resale, automatic breeding, heater/mortality and store/casino/header regressions passed. Viewports: 1920×1080, 1600×900, 1366×768 and 390×844. See [MYSTERY_DIVING_UPDATE_REPORT.md](MYSTERY_DIVING_UPDATE_REPORT.md) for exact suites, all 19 acceptance categories, changed files and limits. DIST and both ZIPs are current; source/DIST/ZIP hashes and CRC checks are independently verified. Browser saves, receipts and mortality history remain local. No public deployment was performed.

## Mystery fish diving — v3.9 current, 2026-10-15

Implemented the authorized Mystery Fish update (request v3.5) on top of playable v3.8. New valid Reef/Deep trips guarantee a reachable regional fish, concealed until boat return, with saved assignments, original question-mark art/reveal, explicit safe receiving and permanent transport-loss evidence. Empty/closed collectible pools block launch. Existing oxygen, fees, resale, local accounts, biology, genetics, breeding, care rewards and freshwater lock remain. See [MYSTERY_DIVING_RULES.md](MYSTERY_DIVING_RULES.md) and [MYSTERY_DIVING_UPDATE_REPORT.md](MYSTERY_DIVING_UPDATE_REPORT.md). Current master is v4.2; earlier release entries are historical where superseded.

## v3.7 equipment, inspector research and Dock Casino - 2026-10-15

Current playable release is v3.7 / consolidated MDP v4.0. DIST includes equipment-category search filters, original fragging-tool previews, owned-fish inspector research at 5 AC once per species, playable Gold Fish and Predator & Prey, and aligned aquarium header controls. All player data, including casino rounds and research, remains device-local. Use the rebuilt DIST contents or AquariumLife-GitHub-Pages.zip at the site root. See STORE_CASINO_UPDATE_REPORT.md and CASINO_RULES.md for changes, odds, persistence and limitations. Earlier build/release sections below are historical.

## UI layout cleanup rebuild - 2026-10-15

DIST now contains the compact aquarium selector, removed bottom cards/slogan, centered Keeper badge and enlarged proportional tank. The build contains the new css/ui-cleanup.css and UI_LAYOUT_CLEANUP_REPORT.md. All current deployment files are rebuilt from source; build-manifest.json is authoritative for timestamp, file count and hashes. The GitHub Pages ZIP contains DIST files at archive root. Chrome and Edge each passed all 258 built Pages/local-save checks after this UI update. Source and deployment archives are refreshed; local saves and freshwater lockout remain. See UI_LAYOUT_CLEANUP_REPORT.md for current acceptance evidence; earlier build timestamps below are historical.

## Current heater/mortality release v3.6 - 2026-10-15

DIST contains **1,520 current source files / 456,024,826 source bytes**, built at 2026-10-15T13:52:07.406621+00:00. Pages ZIP is **425,615,424 bytes**. Every source/DIST/Pages entry matches manifest SHA-256; archive CRC passes. The root index and .nojekyll are present; the four new heater/thermal/journal/UI modules and current heater report/schema documentation are included.

Chrome and Edge each passed **258 checks against this exact built game**, including repository-subpath resources, current seven-level catalog/journal, actual local save/autosave/reload, account/profile isolation, wallet/destination retention, original pre-repair snapshot download, account-specific permanent mortality storage and real standalone mortality JSON export. All selected suites total **1,443 per browser / 2,886 release checks, zero failures**. There are another42 original-thermal diagnostic comparisons outside that total. See TEST_REPORT.md and tests/heater-evidence/release-verification.json.

Upload the contents of DIST or extract AquariumLife-GitHub-Pages.zip at the publishing root. No public deployment was performed. Saves, account/financial/timeline data and the permanent journal remain local to the player browser/PC; normal JSON backup carries a bounded working set, so also export the full mortality journal to move all old records. No player profile/download is shipped. The source archive retains compatibility filename AquariumLife-v0.1.zip and is refreshed with current source/docs/requirements/evidence through python tests/package.py, which validates CRC. No existing death was resurrected or wallet compensated.

Earlier build records below are historical where superseded.

## Current overnight repair build v3.5 - 2026-10-15

DIST contains **1,514 source files / 455,965,949 source bytes**, built at 2026-10-15T12:25:32.557229+00:00. Pages ZIP is **425,590,768 bytes**. Every current source/DIST/Pages entry matches the manifest SHA-256, including build-manifest.json; ZIP CRC passes. Three added runtime modules implement marine care, mortality evidence and Overnight Readiness.

Chrome and Edge each passed **255 final built-DIST checks**, including a repository URL subpath, real local save/reload/autosave, destination and wallet retention, independent browser storage, local export/import and an actual byte-identical pre-repair Settings download. Total selected repaired-release checks: **1,332 per browser / 2,664 overall, zero failures**. No public GitHub deployment was attempted.

Upload the contents of DIST or extract AquariumLife-GitHub-Pages.zip at the publishing root. Both have index.html and .nojekyll at root. Browser profiles/player data are excluded. All saves, timeline/financial records and backup downloads remain local to each player PC/browser. The source ZIP uses compatibility filename AquariumLife-v0.1.zip, refreshed by python tests/package.py with current source/docs/requirements/evidence and CRC validation. See OVERNIGHT_REPAIR_REPORT.md and tests/overnight-evidence/release-verification.json.

Earlier build records below are historical where superseded.

## Current v3.4 build - 2026-10-15

The final rebuild contains **1,511 source files / 455,939,227 source bytes**. Game content v3.4; built at 2026-10-15T11:27:42.923876+00:00. Every source, DIST file and root-ready Pages ZIP entry is checked against its manifest SHA-256. Pages ZIP: **425,579,852 bytes**, CRC verified, index.html and .nojekyll at the archive root.

Chrome and Edge each passed **251 final built-DIST/local-save checks, zero failures**. Other selected final suites bring totals to 1,231 per browser / 2,462 executed assertions, zero final failures; see TEST_REPORT.md and V34_UPDATE_REPORT.md. The v3.4 runtime pays 100 survival AC, preserves the independent 50 healthy AC, and saves all account/financial/recovery data locally.

Upload the contents inside DIST, or extract AquariumLife-GitHub-Pages.zip at the publishing root. No profile/player save, server wallet or cloud save is shipped. The development archive retains compatibility filename AquariumLife-v0.1.zip while containing current v3.4 source/docs/requirements/evidence; python tests/package.py refreshes it. This is local repository-subpath validation, not a claim of public GitHub deployment.

## Earlier release records - historical and superseded where inconsistent

Historical record: earlier survival-reward amounts and results below are superseded by v3.4. Current payments are 100 AC plus a separate independently qualified 50-AC healthy award. Actual historical receipts/test evidence are preserved, not rewritten. See V34_UPDATE_REPORT.md.

## Current playable v3.3 release - 2026-10-14

DIST is rebuilt from the final financial/fragging/research runtime. All 1,511 source files / 455,932,366 source bytes match the manifest SHA-256 and current source. Build timestamp: 2026-10-15T01:38:01.666682+00:00.

AquariumLife-GitHub-Pages.zip: 425,577,604 bytes; ZIP CRC verified, index.html and .nojekyll at the archive root. Upload **the contents of DIST**, or extract that ZIP directly into the publishing root. No outer DIST prefix, browser profile, player save, backend, cloud wallet, dependency download or external runtime service is required.

The final archive audit refreshed a later status-document edit; runtime code is unchanged from the tested build, and every final source/DIST/Pages ZIP file hash matches. Final Chrome and Edge each passed **250 deployed-DIST/local-save checks with zero failures**. These include v3.3 services, new 5,000-AC financial baseline, atomic 5-AC research, all runtime hashes, repository-subpath resources, local saves/autosave/backup, real JSON export/import, isolated browser profiles, network-disabled save and extracted file launch. The first Edge import attempt timed out; the final diagnostic-enabled rerun passed all 250 checks. No untested public GitHub deployment is claimed.

All other final suites bring totals to **8,800 passed per browser, zero failures (17,600 executed assertions overall)**; see TEST_REPORT.md. Research biological content remains incomplete as disclosed in V33_UPDATE_REPORT.md and RESEARCH_SOURCES.md. PDF regeneration remains pending.

The development archive keeps its compatibility filename AquariumLife-v0.1.zip while containing the current v3.3 source, documentation, archived requirements and QA evidence; it is rebuilt separately by python tests/package.py. The Pages ZIP contains only the runtime closure. Both exclude test profiles/player saves.

## Earlier build records - historical where superseded

## v2.9 — current implementation

Implemented the twelve-step saved/skippable saltwater tutorial with medical guidance, three-second selection outlines, disabled freshwater UI, separate +50 healthy / +200 survival rewards with persistent death/recovery tracking, Deep Market display rename, local asset-value leaderboard preview, exact 15,000-US-gallon / 5,000-AC aquarium, proportional water-change salt consumption, independent mystery products and the approved 35-species marine batch. Saves remain local to each player's browser on their PC. The bottom mystery product is content-held because its Legendary host specialist is not eligible. See [V29_UPDATE_REPORT.md](V29_UPDATE_REPORT.md) for actual checks, care/art limits and release details. Earlier milestone sections below are historical wherever superseded.

See [the current release report](V29_UPDATE_REPORT.md), [new art gallery](v29-review.html), [DIST](DIST/) and [build manifest](DIST/build-manifest.json).

## Historical milestone record


## Current v2.8 refresh — 2026-10-14

The current release includes Ocean Diving. `python build.py` regenerates the
offline regional data script, refreshes DIST from current sources, verifies source
hashes and produces the root-ready GitHub Pages ZIP. The live file/byte totals and
build date are recorded in `DIST/build-manifest.json`.

Chrome and Edge each passed **108 diving, 362 livestock/core/health, 7,583 artwork,
and 247 deployed-DIST/local-save checks**, with zero final failures. The deployed
checks use an actual HTTP repository subpath and real local JSON export/import;
active dive reload/return is covered by the diving suite. All player progress,
recovery backups, offline timeline and expedition completion receipts remain
device-local browser storage. No player save or test profile is copied into DIST.

See [DIVING_UPDATE_REPORT.md](DIVING_UPDATE_REPORT.md) for the current file list,
38-item acceptance mapping, new art, region restrictions and remaining limits.
The following section records the initial deployment milestone, with its original
file sizes and scope retained as history.

## Initial publishing build v2.7 — historical

Date: 2026-10-14. Game content: v2.7. No species, genetics, freshwater biology,
save schema, prices or gameplay rules changed in this deployment task.

## Delivered build

- `DIST/index.html` is the deployable entry point. The folder contains current
  scripts/styles, referenced local assets and working art-review entry points.
- `build.py` rebuilds DIST using only Python's standard library. It copies the
  current classic-script source rather than running an unnecessary transpiler.
- The final build contains **1,371 source files / 325,213,103 source bytes**, plus
  `.nojekyll` and `build-manifest.json`. Source and output SHA-256 hashes match.
- `AquariumLife-GitHub-Pages.zip` packages **DIST's contents at ZIP root**, including
  `index.html` and `.nojekyll`, and passes the ZIP CRC check. There is no extra
  outer folder to accidentally publish instead of the game.
- A temporary stale-file probe was added to DIST and removed by the final rebuild,
  confirming that rebuilding does not leave obsolete generated files behind.
- Build inputs exclude all test profiles, downloads, local browser saves and
  development archives. The resulting files fit the normal GitHub per-file and
  Pages site-size limits. Use Git for files over the web uploader's smaller limit.

## Local saves

The existing save implementation already uses browser localStorage. It was
preserved and verified from the **built DIST**, served at an HTTP repository
subpath `/aquarium-life/` that models a Pages project URL.

Active game, recovery backup and timeline data remain local to the player's
browser profile on their PC. Autosave and Save now use this same storage. Export
downloads a real JSON file, and Import reads a user-selected local JSON file.
There are no server save routes, cloud accounts, database writes or save uploads.

Separate browser contexts at the **same served URL** start independently and
cannot read or overwrite one another's progress. Browser data belongs to the
origin/profile; moving from a local file or another domain requires JSON
export/import. Clearing site storage can erase browser saves. These practical
limits are documented in `GITHUB_PAGES.md` rather than claiming automatic file
backups or cross-device synchronization.

## Verification

Run the tests with:

```powershell
python tests/browser_qa.py chrome --pages
python tests/browser_qa.py edge --pages
```

**Chrome: 247 passed / 0 failed. Edge: 247 passed / 0 failed.**
Final browser counts and individual results are recorded in
`tests/pages-evidence/chrome-results.json` and `edge-results.json`.
Each final suite covers:

- Current source/DIST/manifest hashes, correct subpath resources and all 38
  expansion records and sprite sheets.
- The existing expansion's real purchase, placement, inspector, value, health,
  save migration, Mystery Egg and non-fish lifecycle checks, executed against
  the HTTP-served DIST payload.
- Manual save, the actual **20-second autosave**, a local recovery backup,
  reload/Welcome Back, selected aquarium and light preference retention.
- Actual JSON download to disk, its contents, local file selection, validation
  and confirmed import restoring that player's data.
- A blocked-storage warning directing the player to JSON export; saving with
  networking disabled after loading; independent browser-profile storage.
- No external service/analytics/save-upload requests or game JavaScript errors;
  the local test server receives only static file reads.
- The extracted DIST also loading directly through `file://`.

Intermediate test-harness issues were corrected: linked root Markdown documents
are valid build inputs, the procedural art module has no image-error array,
and repeated download checks need unique folders because CDP can overwrite an
existing same-named test download. Those did not require gameplay/save changes.

Firefox and an actual remote GitHub deployment were not run. No repository was
published and no account settings changed. A hosted URL needs a connection to
load its files; this task does not add a service worker or offline reload cache.
The extracted local build remains offline-capable.

## Files changed

- Added `build.py`, generated `DIST/` and `AquariumLife-GitHub-Pages.zip`.
- Added `GITHUB_PAGES.md` and this build report; updated `README.md`.
- Added `tests/pages_qa.py` and the `--pages` mode in `tests/browser_qa.py`.
- Updated `.gitignore` to exclude release ZIPs and generated QA save downloads.
- Added browser evidence under `tests/pages-evidence/`; no player profile is
  included in the deployment artifact.

Publishing instructions: [GITHUB_PAGES.md](GITHUB_PAGES.md). Rebuild after future
source changes with `python build.py`, then upload the refreshed DIST contents.
