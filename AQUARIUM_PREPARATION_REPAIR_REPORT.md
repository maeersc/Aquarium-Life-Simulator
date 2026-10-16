# Global aquarium preparation repair — playable v4.0.1

2026-10-16. Saltwater only. Master v4.4 retains all 31 major sections. Existing local accounts, fish, corals, bottom dwellers, rocks, equipment, chemistry, bacteria, genetics, diving economies, mortality, rewards and the 20-minute day are preserved.

## Confirmed root cause

The actual normal setup flow reproduced the player's failure before editing runtime code. Evidence: `tests/preparation-evidence/before-repair.json` (isolated QA aquarium, not player data).

1. New-game empty setup and purchased aquariums call `emptyTank`, which stores `emptyDry=true`.
2. The old `Core.prepare` set only `prepared=true`. It never cleared `emptyDry`.
3. Cycling and most store/health checks read only `prepared`. Cycling therefore ran normally and established both bacterial colonies.
4. The renderer already used `emptyDry && !prepared`, so prepared tanks visibly contained water.
5. Diving's fish/coral/invertebrate receiving tables instead required `prepared && !emptyDry`. They rejected the same prepared, wet, cycled aquarium as “Unprepared / dry.”
6. Save validation allowed the contradictory flags, serialization retained both, and restoration/offline progression did not reconcile them. No evidence showed offline simulation resetting preparation; it preserved the original setup error.

The reproduced 300-L tank had `prepared=true`, `emptyDry=true`, 36.0833 completed cycle hours and both colonies at 1.0 after normal setup, cycling and a real save round trip. Its exact volume passed (79.252 US gallons versus a 30-US-gallon Chalk Bass requirement), while its preparation row failed. This confirms the shared stale-flag defect without assuming that volume, temperature or chemistry alone proves readiness.

## Repair and save compatibility

`AL.Preparation` is now the shared authority. It keeps the existing schema-2 flags, avoiding a new persisted phase enum that could conflict again:

| Displayed stage | Meaning |
|---|---|
| Dry aquarium | Explicit dry marker, no completed preparation |
| Filled; water not prepared | Water present; preparation incomplete |
| Prepared saltwater | Preparation completed; cycling may still be needed/in progress |
| Prepared and cycled | Preparation complete; both current colonies established; no active fishless cycle |

The existing free Prepare water action includes filling and sets both flags atomically: `prepared=true`, `emptyDry=false`. The optional Add water action only fills. Neither sand, equipment, normal displayed chemistry nor filling automatically prepares/cycles an aquarium. Per-tank preparation history records actual setup actions and observation times; a migration timestamp is not presented as the original preparation date.

**Existing affected saves repair automatically when evidence is sufficient.** A saved true preparation flag directly proves completed preparation and clears its stale dry marker. A lost false flag may be restored from valid per-tank completed preparation/cycle history or legacy completed fishless-cycle progress, which the original simulation could only advance after preparation. A later recorded dry/filled state supersedes older cycle evidence. Colony percentages, normal chemistry, owned livestock, installed equipment, global preparation statistics and mere elapsed time do not independently authorize repair.

Normalization runs at restore, action, save and simulation boundaries, including actual offline catch-up. Migration is idempotent, awards no repeated preparation/cycle rewards and preserves all tank contents and biological/chemical state. Unknown completion remains unprepared and can use the normal free preparation action. Freshwater state is not migrated; its lock and biological behavior remain unchanged.

All receiving hosts use the shared completion check: regular-store fish/eggs, Reef/Deep diving fish, corals, bottom dwellers, compatible offspring/incubation and quarantine. The detailed table and all-owned-destination dropdown remain. A filled unprepared tank is no longer described as dry. Every species-specific minimum volume, water, cycling, habitat, support, stocking and treatment/quarantine safeguard still applies.

## Capacity audit

- Actual volumes remain in liters. 75 L displays nominally as 20 gal but equals 19.813 US gal; 300 L displays as 80 gal but equals 79.252 US gal. Neither was resized or given a special species exception.
- The 75-L prepared tank correctly remains too small for Chalk Bass (30 US gal minimum). The prepared 300-L tank passes its full compatibility report and accepts the returned fish once.
- Adult-load reservations now consistently exclude nonviable eggs. They still include live adult fish/invertebrate loads, viable egg counts, natural-courtship reservations and supported bottom-dweller nurseries. These are future adult-capacity reservations, distinct from current growth-weighted bioload.
- Retained dead fish occupy the existing physical/save fish-entity limit until removal, while contributing no living adult load. Previously, living-only entity counting could permit a transfer that later failed the save array limit. Core compatibility and diving diagnostics now agree. Fish, coral and invertebrate array limits remain separate.
- Rated equipment capacity and condition-adjusted output remain distinct. Ordinary wear warnings remain advisory where already advisory; no blanket full-rated-output receiving restriction was introduced. Operating filtration/circulation and species-specific flow checks remain.

## Files changed

Runtime: new `js/aquarium-preparation.js`; `js/core.js`, `js/save.js`, `js/simulation.js`, `js/diving-receiving.js`, `js/store-rules.js`, `js/invertebrates.js`, `js/breeding.js`, `js/gameplay.js`, `js/habitat.js`, `js/livestock-health.js`, `js/marine-care.js`, `js/thermal.js`, `js/update29.js`, `js/expansion.js`, `js/render.js`, `js/ui.js`, `js/app-shell.js`, `index.html`. Existing standalone review/test HTML entry points that load Core also load its shared preparation dependency; artwork itself was not regenerated or edited.

QA/build: `tests/preparation_checks.js`, `tests/preparation_qa.py`, `tests/browser_qa.py`, `tests/pages_qa.py`, `tests/package.py`, release verification, `build.py`, and isolated evidence under `tests/preparation-evidence`. Guarded integration scripts and pre-repair snapshots are retained under `planning/preparation-repair`.

Documentation: this report, `MASTER_DEVELOPMENT_PROMPT.md`, full `PROJECT_CONTINUITY_SOURCE.md`, `README.md`, `GAME_DESIGN.md`, `DEVELOPMENT_STATUS.md`, `UI_SPECIFICATION.md`, `TEST_REPORT.md`, `GITHUB_PAGES_BUILD_REPORT.md`. Binary PDF regeneration is not claimed; the complete printable continuity source is updated.

## Test results

Source tests exercise all four stages, both reported sizes through actual setup/cycling actions, independent second-tank setup, saved stale flags, sufficient/insufficient migration evidence, idempotence, filled-state labels, aquarium data preservation, successful and rejected boat transfers, repeat receiving prevention, actual UI fill/prepare controls, real browser reload, all current diving species/hosts, quarantine/incubation safeguards, volume/equipment/load/entity consistency, 8-/24-real-hour calls to the actual offline service, matched active/catch-up stepping and a seven-game-day freshwater replay against the pre-repair engine.

Responsive checks cover 1920×1080, 1600×900, 1366×768 and 390×844. QA uses dedicated profiles; no actual player save was inspected or modified. Built acceptance runs DIST at a local GitHub Pages-style repository URL, with local-account, valuation, market, medical, growth, genetics, offline and receiving regressions.

<!-- FINAL-RESULTS -->
| Current browser suite | Passed | Failed |
|---|---:|---:|
| preparation-evidence/chrome-results.json | 207 | 0 |
| preparation-evidence/edge-results.json | 207 | 0 |
| pages-evidence/chrome-results.json | 669 | 0 |
| pages-evidence/edge-results.json | 669 | 0 |

**1752 executed browser assertions passed; zero failed.** The source suite includes all current shared receiving profiles. Both source browsers also passed the actual UI, actual reload and protected seven-day freshwater differential replay. Built suites include the prior complete diving/mystery/receiving/expansion, economy, medical, local-account and save checks, plus the preparation regressions. Independent executions in Chrome and Edge are intentionally counted separately.

Commands: `python tests/browser_qa.py chrome --preparation`, `python tests/browser_qa.py edge --preparation`, and `python tests/browser_qa.py chrome --pages` / `edge --pages`. Build: `python build.py`. Final integrity: `python tests/verify_preparation_release.py --source-archive --check-only`. Packaging: `python tests/package.py`. The final source, DIST and both ZIP archives are matched by hashes/byte comparisons and ZIP CRC; release evidence is in `tests/preparation-evidence/release-validation.json`. No real GitHub deployment or unrun browser is claimed.
<!-- END-FINAL-RESULTS -->

## Remaining restrictions

The player's actual local save was not supplied, so its exact flag values cannot be independently inspected here. The verified migration repairs the reproduced defect and supported completion-evidence cases automatically when those saves are loaded. Tanks with no proof of completed preparation remain unprepared. The 20-gallon Chalk Bass volume rejection, unsafe chemistry, incomplete cycling, habitat/treatment restrictions and freshwater lock remain intentional. No unconditional receiving override, stock reset, revived livestock or server saving was introduced.
