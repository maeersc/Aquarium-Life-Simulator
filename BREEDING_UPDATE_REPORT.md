# Aquarium Life — automatic breeding update v3.8

Implemented 2026-10-15. Consolidated MDP v4.1; save schema remains 2. Detailed mechanics and scientific uncertainty: [BREEDING_RULES.md](BREEDING_RULES.md). Persistence: [BREEDING_SAVE_SCHEMA.md](BREEDING_SAVE_SCHEMA.md).

## Changes

The former marine journal button created a brood immediately and applied generic male/female eligibility. The marine simulation now periodically evaluates species-specific partners and conditions, performs chance rolls on a saved hourly schedule, steers real courtship/nest behavior, creates a persistent same-tank clutch and applies fertilization, care, water, disease, predation and dispersal losses. There is no guaranteed minimum hatchling. The manual marine action rejects without mutating the account; the journal is an observation dashboard.

Four profiles cover 29 existing biological IDs: 26 purchase-eligible clownfish with hard-substrate eggs and male tending; Banggai paternal mouthbrooding and developed juvenile release; simultaneous-hermaphrodite Chalk Bass with alternating egg-donor roles, pelagic spawning and live-plankton larvae; Sharknose Goby with demersal cavity eggs and male care. Five specialist clownfish acquisition/art holds and all incomplete species/designer profiles remain held. Old and purchased clutches retain their original saved model. No new livestock species or art asset is added.

Clownfish juveniles are nonbreeders, mature into the male role and undergo a timed female transition only when their mature group lacks an established female. Only the dominant male and one established female breed; established females never reverse. Courtship uses normal smooth swimming targets and small observation markers. Original anatomy, eyes, facing, stage art and patterns are retained. Attached scene clusters stay 8 logical pixels, pelagic eggs 5; fixed magnified clusters show development.

The existing inspector shows applicable role/maturity/mate/readiness/courtship/gravid/preparing/parental-care/mouthbrooding/recovery fields and refreshes independently of its three-second selection outline. Breeding & Eggs tracks pairs, readiness, spawning, clutch parent/tank/date/count/progress/hatch estimates, offspring status/lineage and histories. Coral frag clone lineage remains separate.

Reproduction reserves the whole cohort's adult load and entity slots, retains 20% biological headroom and respects habitat/territory, nutrition, disease and recovery. The headroom was added after long-term economy tests exposed overbreeding pressure in small starter tanks. Natural offspring cannot be sold until juvenile growth and at least seven game days after hatch; no direct AC reward is added. Marine invertebrate admissions also honor fish clutch/pair reservations. Existing welfare, valuation, rewards, equipment maintenance, thermal simulation and the 20-minute game day remain authoritative.

`js/patterns.js` is unchanged: normal Ocellaris still use 85/10/4/1, and Snowflake reference-line segregation/explicitly inferred nonviability remain separate. Other species retain ordinary catalog identities, not clown-specific inheritance. Additive migration preserves account, tank, fish, existing egg/parent/pattern/lineage IDs and histories. Saved schedules, reproductive roles/states/sites, brood survival, unique hatchling IDs, minimum sale ages and an independent RNG survive reload. The same fixed steps process active gameplay, modals, casino, diving and offline time; saved checkpoint guards prevent duplicate elapsed-time processing.

## Files changed

- Runtime: `index.html`; `js/breeding.js`, `js/breeding-ui.js`, `css/breeding.css`; integration in `js/core.js`, `js/simulation.js`, `js/save.js`, `js/marine-care.js`, `js/invertebrates.js`, `js/valuation.js`, `js/update31.js`, `js/ui.js`, `js/app-shell.js`, `js/main.js`, `js/render.js`, `js/brood-view.js`, `js/update31-ui.js`, `js/expansion-ui.js`.
- QA/deployment: `tests/breeding_checks.js`, `tests/breeding_qa.py`, `tests/browser_qa.py`, `tests/suite.js`, `tests/verify_breeding_release.py`, `tests/package.py`, `build.py`, evidence in `tests/breeding-evidence`, rebuilt `DIST` and both release ZIPs. The legacy mouthbrood unit fixture now restores a brood directly rather than invoking the removed marine player action; its carrier-loss assertion remains.
- Design/continuity: full 31-section `MASTER_DEVELOPMENT_PROMPT.md`, `GAME_DESIGN.md`, `DEVELOPMENT_STATUS.md`, `UI_SPECIFICATION.md`, both current fish/livestock catalogs, `RARITY_GENETICS_RESEARCH.md`, `RESEARCH_SOURCES.md`, `PROJECT_CONTINUITY_SOURCE.md`, `PDF_WORKFLOW.md`, `GITHUB_PAGES.md`, `README.md`, `TEST_REPORT.md` and these three breeding documents. Original 38/35 roster ledgers are retained. Request and source snapshots are under `planning/automatic-breeding`.

## Acceptance evidence

The reproducible runner is `python tests/browser_qa.py <chrome|edge> --breeding`, using isolated QA browser profiles with networking disabled. Evidence JSON and screenshots are under `tests/breeding-evidence`; real player saves/profiles were not opened or modified.

| User acceptance cases | Evidence |
|---|---|
| 1–5 Automatic breeding, removed button, maturity, species, roles | Shared simulation starts/spawns without a manual action; manual action rejects atomically; maturity/health/nutrition/stress/illness/water/sex/species/genetic checks; simultaneous chalk-bass and timed clownfish roles |
| 6–9 Visible courtship, continuous movement, gravid and male brooding | Smooth target/position checks, unrelated fish movement, actual scene/inspector screenshots, live state refresh, three-second outline expiry, internal father/no external pile |
| 10–14 Parent tank, rock/pelagic placement and persistent single clutches | Valid support IDs, separate aquariums, drift checks, five parse/save cycles, actual local reload, no extra clutches |
| 15–19 Incubation, hatch IDs, genetics and stages | Suitable-hour advance, unique newborn IDs, copied embryo seeds/parents/generation, exact 100-bucket 85/10/4/1 mapping, 2,000 Snowflake embryos, baby/juvenile artwork selection, no Ocellaris traits on unrelated fish |
| 20–23 Recovery/capacity, observation/history and coral lineage | Recovery and occupied nests, dominant roles, full adult/entity reservations and headroom, dealer establishment holds, journal sections/hatch histories, separate unchanged coral lineage |
| 24–27 Offline parity, old saves, freshwater lock and no network | Exact 8/12/24-real-hour live/offline breeding projections; repeated checkpoint replay; additive/idempotent migration and malformed-state rejection; protected freshwater regression; no HTTP/HTTPS gameplay requests |

All four live modal contexts — Store, Field Journal, Dock Casino and Diving — are checked with actual animation-frame clock progression. Responsive breeding UI is checked at **1920×1080, 1600×900, 1366×768 and 390×844**. The existing casino/header regression also checks header alignment at all three requested desktop sizes.

Measured final suite counts and package checks are recorded below.

## Limitations and not-run coverage

This is a calibrated game model, not a complete real-world aquaculture simulation. No species-specific endocrine model, full nesting anatomy, live-culture enrichment/density or complete larval settlement protocol is claimed. Existing provisional art and specialist/uncertain profiles remain held. The latest 600 detailed reproductive records persist with older completed-cohort aggregate totals; this is not an unlimited full-detail breeding archive. Living/loss records retain their own lineage separately.

No current binary continuity PDF was produced: Node, ReportLab, pypdf/PyMuPDF and Poppler are unavailable. The complete maintained printable source and all 31 master sections are updated. Firefox, Safari, actual multi-device/profile transfers, and exhaustive year-long outcomes for every individual species were not run.

An exploratory invocation of the retired v2.6 `--ecosystem` runner stopped at its obsolete unlocked-freshwater fixture; that runner also expects pre-v2.7 missing Mystery Egg tiers. It is not counted as a passing current-release suite. Current protected freshwater comparisons, marine genetics, mystery/store, migration and offline coverage are exercised by the current acceptance/regression suites instead. No production freshwater lock was relaxed to satisfy the retired runner.

## Release verification

Current release suites: **1,808 passing assertions, zero current-suite failures** (assertions overlap between suites and browsers):

| Suite | Browser | Passed / failed |
|---|---|---|
| Autonomous breeding model, live UI, save/reload, modal clock and offline parity | Chrome | 86 / 0 |
| Autonomous breeding model, live UI, save/reload, modal clock and offline parity | Edge | 86 / 0 |
| Livestock/core/coral/disease/value/economy and protected freshwater comparison | Chrome | 362 / 0 |
| v2.9 saltwater/tutoring/save/mystery/roster compatibility | Edge | 412 / 0 |
| Equipment filters, owned research, store destinations, casino and header alignment | Edge | 138 / 0 |
| Heater, overnight mortality, death journal and equipment behavior | Edge | 108 / 0 |
| Existing survival/care rewards, finance, dialogs and local saves | Chrome | 98 / 0 |
| Built DIST at an HTTP Pages repository subpath, local save/reload/import behavior | Chrome | 259 / 0 |
| Built DIST at an HTTP Pages repository subpath, local save/reload/import behavior | Edge | 259 / 0 |

Evidence paths are listed in `tests/breeding-evidence/release-validation.json`. The retired runner caveat above is separate and is not hidden in these totals. No current-release regression failure remains.

Rebuilt **DIST** declares game content v3.8 and contains 1,536 current source/runtime/document files. `python build.py` verifies source/DIST SHA-256 correspondence, local dependency paths and Pages ZIP CRC/root structure. `AquariumLife-GitHub-Pages.zip` contains the current DIST contents at its root; `AquariumLife-v0.1.zip` contains current portable source, complete continuity and QA evidence, excluding browser profiles and development caches. All save data remains device-local; no publication or cloud account operation was performed.

Final reproducible checks: `python tests/verify_breeding_release.py`, `python tests/package.py`, then `python tests/verify_breeding_release.py --source-archive --check-only`. These compare every deployed/archive byte to current source, preserve every prior deployed asset and all prior continuity registry rows, and verify the unchanged genetics source and complete 31-section MDP. The manifest and validation JSON retain measured build time and byte counts; they are authoritative instead of a manually copied archive size.
