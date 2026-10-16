# Diving livestock receiving repair — v3.9, 2026-10-16

## Universal ocean diving receiving — 2026-10-16

All registered diving fish, corals and invertebrates now share species-aware diagnostics and explicit saved post-boat receiving. Every owned aquarium is shown; supported coral mounts and host-compatible quarantine retain all safeguards. The repair also corrects invalid noninfectious carrier flags, rock surface discovery and missing/ambiguous host mappings. Tests enumerate the real eligible registry, plus old-save, condition, expiry, replay and future-registration checks. See [GLOBAL_DIVING_RECEIVING_REPORT.md](GLOBAL_DIVING_RECEIVING_REPORT.md). Earlier host-limited flow descriptions are historical where superseded. Game v3.9 / master v4.2; local saves and freshwater lock remain.

## Confirmed cause and scope

The previous receiving UI used `AL.game.tanks.filter(t => AL.Diving.receiving(...).ok)`. Any rejected aquarium disappeared completely; it displayed neither the failing predicate nor actual values. Thus “No compatible receiver” meant **zero tanks passed all existing checks**, not that the player owned no tank. Eligibility also refreshed only when the expedition report changed; correcting water or preparation did not reliably refresh the destination list. Both interface defects are repaired.

The player's actual save/screenshot diagnostic data was not supplied. **80 US gallons and 27°C alone cannot establish which additional predicate rejected that particular aquarium.** No claim is made that its cycling, shelter, stocking or chemistry was actually wrong. Reproductions confirm that an otherwise prepared nominal 80-gallon tank at exactly 27°C passes, while missing rock shelter, insufficient bacterial colonies, unsafe water or predatory residents independently reproduce the old empty dropdown. Actual water slightly above 27°C can round to 27°C elsewhere while legitimately failing the species range; the new diagnostics show the full numeric reading rather than hiding that difference. No temperature tolerance or other biological limit was loosened to make the example pass.

## Chalk Bass record audit

Exactly one implemented record: `chalk-bass`, Chalk Bass, *Serranus tortugarum*, marine, Common, Moderate care, minimum 30 US gal / 113.56235352 L. Runtime temperature is 24–27°C inclusive; pH 8.0–8.4; salinity 33–36 ppt. Group minimum is one; habitat requires rock shelter/cave; diet is frozen food. Its Caribbean Reef encounter profile resolves to this same stable ID and scientific name. No duplicate species, biological data change, new rarity, genetic change or acquisition override was added. A nominal 80-gal tank stores 300 physical liters (~79.252 US gal); an actual 80-US-gal tank stores 302.83294272 L. Both exceed the unchanged minimum.

## Receiving checks and interface

Every owned aquarium is listed, with name, nominal US gallons, Saltwater/Freshwater, actual temperature and Available/Unavailable. Rejected options remain visible and disabled with exact reasons. Expand each aquarium's checks to see actual values, requirements, Pass/Blocked, preparation guidance and advisory warnings. The same diagnostic report validates the final fish transfer; the UI cannot grant permission the authority would reject.

Individual checks cover habitat/freshwater lock, physical volume, actual temperature/species range, salinity, pH, ammonia ≤0.15 mg/L, nitrite ≤0.15 mg/L, oxygen ≥5.5 mg/L, prepared water, ammonia-processing colony ≥0.65, nitrite-processing colony ≥0.5, functioning filtration/circulation, adult load including reserved offspring, entity capacity, quarantine, rock shelter, species group and Keeper access. Every prior store/species safety rejection remains enforced, including predators, specialist habitat/food, boxfish toxin/species-only housing and reserved brood restrictions.

The audit found no explicit fish receiving equipment check in the old path. Fish receiving now also requires installed/enabled/functioning filter and circulation pump. Rated output, condition and effective capacity are shown; capacity below tank volume is an advisory, not a new “100% condition required” gate. Adding an untreated fish to an active restricted medication course is blocked. Quarantine itself is optional for this catch and keeps the existing survival bonus; it never waives cycling, species habitat or water requirements. Medicine/course rules elsewhere are unchanged.

Destinations refresh from live tank conditions without reopening results, retaining the dropdown node, explicit selection, keyboard focus and open diagnostic sections. Selection is scoped to the current local world, so switching accounts cannot reuse a different world's choice. No automatic destination is chosen.

The existing finite holding deadline is unchanged and now has an updating game-time countdown plus an approximate real-seconds equivalent at 1×. Blocked compatibility checks and UI refresh are pure read-only operations: they never delete the specimen, alter its assignment/draw/deadline, change health or create a death. The existing approved holding expiry and transport-survival assessment still apply. No specimen was resurrected, automatically compensated or given unlimited holding.

## Ownership, health and persistence

A valid receive action rechecks pending/unsettled state, expiry and current destination compatibility, then runs the existing precommitted transport/condition assessment. A survivor is created through the existing fish constructor with permanent ID, real health/genetic/pattern state, rarity and diving provenance in the chosen tank. Core transaction handling updates counts, invalidates/recalculates value, validates the draft and saves through the existing local UI action. Pending receiving inventory is cleared by the settled recovery status; its historical transport snapshot remains as an audit receipt, not a second animal. Failed delivery remains subject to the existing permanent mortality journal. Duplicate actions and replayed saved pending states remain blocked by the saved recovery state and local receipts. Save schema and old aquarium/livestock records remain compatible.

## Files modified

- New `js/diving-receiving.js`: one structured receiving report, all-owned destination discovery and finite countdown presentation.
- `js/diving.js`: fish receiving delegates to that report; coral/invertebrate receiving is preserved.
- `js/diving-ui.js`, `css/diving.css`, `index.html`: disabled visible options, per-tank checks/help, live refresh/focus/selection, countdown, script inclusion.
- `build.py`, `tests/package.py`, `tests/browser_qa.py`, `tests/pages_qa.py`: deployment inclusion and isolated regression/build coverage.
- New `tests/receiving_checks.js`, `tests/receiving_qa.py`, `tests/verify_receiving_release.py`, `tests/receiving-evidence/`, and request/backups/integration scripts under `planning/receiving-repair/`.
- This report, `MASTER_DEVELOPMENT_PROMPT.md` §5.5, the full `PROJECT_CONTINUITY_SOURCE.md`, `MYSTERY_DIVING_RULES.md`, `DEVELOPMENT_STATUS.md`, `TEST_REPORT.md`, `GITHUB_PAGES_BUILD_REPORT.md`, plus rebuilt DIST and release ZIPs.

## Verification

The final source suites completed successfully in isolated browser profiles:

| Executed suite | Passed | Failed |
|---|---:|---:|
| Receiving model, UI and real reload — Chrome | 44 | 0 |
| Receiving model, UI and real reload — Edge | 44 | 0 |
| Existing mystery capture/reveal/holding/resale/save protections — Edge | 61 | 0 |
| Total source checks | 149 | 0 |

Each receiving suite contains 31 model checks and 13 browser/layout/save checks. Tests cover all ten requested categories: every owned destination including legacy freshwater, disabled rejection reasons with actual/required values, valid nominal/physical 80-gal Chalk Bass at 27°C, unsafe water/equipment/cycling/shelter/stock/predator rejection, optional quarantine and active-course restrictions, real owned ID/count/value, health/genes/condition persistence, cleared pending inventory, repeated-action and save replay protections, and existing additive save compatibility. Additional checks verify exact 27.000001°C visibility, unchanged finite deadlines, countdown/live clock, corrected eligibility without reopening, and actual browser reload. Existing mystery regressions cover precommitted survival, expiry mortality, replay receipts and all prior transport outcomes. Tests deliberately choose a successful precommitted draw for the receiving example; gameplay survival is still probabilistic.

UI/layout checks ran at 1920×1080, 1600×900, 1366×768 and 390×844. Screenshots were visually inspected; long check tables scroll inside their own container and failed values remain readable. No uncaught JavaScript exceptions or HTTP/HTTPS gameplay requests occurred. Earlier development fixture errors were corrected; there are no remaining source-suite failures.

The final built-DIST tests run in Chrome and Edge at an HTTP repository subpath, re-executing the 31 receiving model cases alongside the existing diving/mystery/expansion and actual local save/account/export checks. Per-check results and exact final counts are recorded in `tests/pages-evidence/chrome-results.json` and `edge-results.json`. The release verifier requires the new receiving-runtime check and zero failures in both; it also verifies all source/DIST SHA-256 values, ZIP CRCs/root entries, unchanged prior assets, the full 31-section continuity and current source archive. Machine-readable final combined counts are in `tests/receiving-evidence/release-validation.json`.

DIST and AquariumLife-GitHub-Pages.zip are rebuilt after source/docs/layout finalization. AquariumLife-v0.1.zip contains current source/docs/tests without profiles/caches. The final build-manifest.json is authoritative for build time, file count and hashes. No public deployment or player-save edit was performed.


## Remaining restrictions

The original tank's exact rejecting predicate remains unknown without its saved readings/state; the repaired game now exposes that evidence directly. If the aquarium is legitimately uncycled, lacks equipment/shelter, is overstocked, has unsafe tankmates/water or an active restricted course, receiving remains blocked until corrected. Full-precision temperature is checked against the actual species range rather than the heater target. No existing deceased animal is restored. Original survival losses and finite deadlines remain possible even with a compatible receiver. All game, account, journal and receipt data stays local to the player's PC/browser; no public deployment or server save was added. Freshwater remains locked and its data/biology is unchanged.
