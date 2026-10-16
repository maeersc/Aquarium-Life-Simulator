# Mystery fish diving update — playable v3.9 / MDP v4.2

Implemented the attached Mystery Fish request (titled v3.5) on the current v3.8 game without reverting automatic breeding or earlier features. Primary authority: Master Development Prompt §5.5. Full encounter/selection/save/survival rules and primary biological sources: [MYSTERY_DIVING_RULES.md](MYSTERY_DIVING_RULES.md).

## Changes and cause

Earlier dives used optional livestock presence rolls and could contain only rocks. Fish also used actual species artwork/names before collection. New valid trips always assign one eligible regional fish at a proven reachable cell, conceal every fish until successful boat return, then require explicit compatible receiving or quarantine. Fish cannot be granted by mere capture, failed trips, unsafe delivery or replay.

Fiji previously had a coral encounter but no collectible fish pool. Two already implemented, sourced Fiji fish now have encounter profiles; no biological roster expansion or rarity change was needed. Hawaii retains its existing observation-only policy and is visibly blocked, as required when there is no valid collectible fish pool. Six valid region/mode combinations remain playable.

Selection uses saved diving RNG uniformly among verified fish matching region/mode/survey depth, separately from Mystery Egg odds. Guaranteed route costs at most 30% oxygen, or 20% capturing from adjacent range. Original shared pixel silhouette has a large question mark and gentle swimming animation; a short pixel wipe reveals existing species art. All eight temporary slots, range checks, oxygen/movement, fees, rentals, receiving, health, resale/provenance and local save rules remain.

Assignments, positions, capture, temporary inventory, oxygen and random stream persist. Revealed reports additionally save pending/released/received/failed state, precommitted survival/condition draws, holding deadline and receiver/death-record identity. Local trip/recovery receipts prevent normal duplicate grants. Old pre-update trips resume unchanged. Pending fish are unowned and valued at zero until a successful safe receiving action; final value uses existing central valuation. Transport holding still expires under live and offline progression, with original survival calculations preserved. Permanent journal records retain known trigger and expedition evidence, leaving unmeasured physiology/chemistry unknown. They appear in offline reports and full/selected local exports without changing owned-death reward rules.

## Files changed

- Runtime: `js/diving-mystery.js` (new authority); `js/diving.js`, `js/diving-data.js`, `assets/diving/registry.json` (launch/pools/assessment/receipts); `js/diving-ui.js`, `js/diving-art.js`, `css/diving.css` (concealment, capture, reveal, receiving, current values); `js/core.js`, `js/simulation.js`, `index.html`, `js/ui.js` (actions/shared clock/script/current version).
- Mortality: `js/mortality-journal.js`, `js/mortality-ui.js`, `js/overnight-ui.js`, `MORTALITY_LOG_SCHEMA.md` (additive transport evidence through the existing logger, UI/export/offline reporting).
- Documentation: this report, `MYSTERY_DIVING_RULES.md`, `MASTER_DEVELOPMENT_PROMPT.md`, full `PROJECT_CONTINUITY_SOURCE.md`, `README.md`, `GAME_DESIGN.md`, `DEVELOPMENT_STATUS.md`, `UI_SPECIFICATION.md`, `RESEARCH_SOURCES.md`, `DIVING_UPDATE_REPORT.md`, `TEST_REPORT.md`, `GITHUB_PAGES_BUILD_REPORT.md`.
- QA/build: `tests/mystery_diving_checks.js`, `tests/mystery_diving_qa.py`, `tests/verify_mystery_diving_release.py`, `tests/browser_qa.py`, existing `tests/diving_checks.js`, `tests/diving_resale_checks.js`, `tests/diving_qa.py`, `build.py`, `tests/package.py`; requirements, backups and one-time integration scripts in `planning/mystery-diving/`. Evidence in `tests/mystery-diving-evidence/`; generated DIST and both release ZIPs are rebuilt after final validation.

## Verification

All final selected checks passed. Commands use isolated QA browser profiles, never player profiles/saves. Full evidence JSON/screenshots remain in the corresponding tests folders.

| Suite | Passed | Failed |
|---|---:|---:|
| Mystery model + real controls/reload/export — Chrome | 61 | 0 |
| Mystery model + real controls/reload/export — Edge | 61 | 0 |
| Existing diving/oxygen/receiving/resale — Edge | 108 | 0 |
| Automatic breeding + live/offline parity — Chrome | 86 | 0 |
| Heater + permanent mortality journal — Edge | 108 | 0 |
| Store destinations/equipment/research/casino/header — Edge | 138 | 0 |
| Built DIST / Pages subpath / local saves + mystery model — Chrome | 363 | 0 |
| Built DIST / Pages subpath / local saves + mystery model — Edge | 363 | 0 |
| **Total** | **1288** | **0** |

The mystery model covers 100 seeded expeditions in each of six valid region/mode combinations, plus an 800-seed Fiji Reef selection check (392 Exquisite wrasse / 408 butterflyfish). It tests range/capacity/eight slots, duplicate clicks, abandoned/exhausted forfeiture, geographic/depth/closed/empty-pool guards, save/reveal/recovery/receipt persistence, all five transport outcomes, alternate safe receivers, unsafe/missing receiver rejection, actual offline expiry/live parity/repeated login, account journal isolation and legacy trip compatibility. The actual browser suite exercises left/right clicks, question-mark art, pre-return concealment, real reloads, explicit receiving, live clock/equipment, responsive results at 1920×1080 / 1600×900 / 1366×768 / 390×844, and a real local mortality JSON download. Screenshots were visually inspected. No uncaught JavaScript exceptions or external gameplay requests were found.

All 19 requested acceptance categories are covered: (1–3) both modes + reachability/return; (4–5) hidden identity + original silhouette; (6–7) range/capacity/eight slots; (8) failed-dive forfeiture; (9) boat reveal; (10–11) region/depth eligibility; (12–13) persisted identity/no duplicate; (14–15) all survival states/safe receiving; (16) existing resale regressions; (17) real shared clock and breeding/live-offline regressions; (18) production freshwater lock; (19) offline resources/local saves. Built-DIST checks repeat the diving/mystery model and actual origin/profile/save/export protections under a repository URL subpath.

During development one new receiver fixture initially reused a rock ID; that test fixture was corrected to allocate unique identities. An initial UI assertion returned a DOM element rather than a Boolean; it was corrected. Final suites have zero failures. Older broad legacy runners that expect unlocked freshwater were not used as current production acceptance; no production lock was removed. No unrun historical suite is counted in this release total.

DIST, AquariumLife-GitHub-Pages.zip and the compatibility-named AquariumLife-v0.1.zip source archive are rebuilt from current source. Final SHA-256/source/DIST/archive checks, CRCs, manifest counts and protected-art/continuity verification are recorded in tests/mystery-diving-evidence/release-validation.json. The build-manifest.json is authoritative for the final timestamp and byte count. Only report text/evidence is finalized after runtime QA; no game calculation changes follow those tests.


## Known limits

- Regional pools remain deliberately small: five combinations have one eligible guaranteed species; Fiji Reef has two. Names/rarity are concealed in the UI, but players may infer identities from these known pools or inspect editable local data. No Legendary was invented or guaranteed.
- The guarantee applies to newly initialized valid trips. Existing saved trips are not rerolled; Hawaii remains blocked. Compact maps are retained. Larger exploration, photography and ecosystem discovery are documented only for a future milestone.
- Survival/condition and transport timing remain game calibrations. Physiological causes and transport water/temperature/hunger histories are not measured; mortality records explicitly preserve that uncertainty. No existing dead livestock is restored.
- Before an explicit receiver is chosen, results honestly show Awaiting receiving assessment / Not received / zero owned value. Closing the window does not stop the holding deadline or aquarium clock. Final condition/value/destination appear after receiving.
- Saves/journals/receipts are browser-origin local. Changing browser/site address requires exporting/importing backups; clearing storage can remove receipts. Editable offline saves cannot provide cryptographic anti-cheat. Export the complete mortality journal to preserve entries beyond the bounded game snapshot.
- Existing artwork approval status is preserved. The new silhouette/reveal is original code-native pixel art; it does not imply approval of previously unapproved species art. Full 31-section printable continuity source is updated; no new binary PDF is claimed. No public GitHub deployment is performed.

The future exploration concept is documented in master §28.1 and MYSTERY_DIVING_RULES.md; no expanded exploration runtime was added.
