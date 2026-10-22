# Rarity, genetics and continuous ecosystem release report

Completed and verified: 2026-10-14. Implements the authorized v2.5/v2.6 briefs in MDP v3.1, retaining all 31 major sections. The current roster remains 52 fish records, five coral groups, six existing freshwater plants and 25 base-linked designer entries; no new species were introduced.

## Completed features

- One six-tier rarity registry with six original colored 64px transparent pixel silhouettes and accessible labels. Fish, corals, bottom dwellers, broods, store/dealer cards, collection, encyclopedia and lineage share it. Approved clownfish rarity tables are unchanged. Explicit game-scarcity assignments for other existing entries are in CURRENT_LIVESTOCK_CATALOG.md and RARITY_GENETICS_RESEARCH.md.
- Exactly eight saved daily Saltwater Fish listings: three Common, three Uncommon, one Rare and one Mystery Egg. Normal species/variety prices stay fixed; listing IDs, stock, calendar and independent RNG persist. Sold-out listings stay present. Browsing advances the countdown and refreshes the grid on midnight. Purchase details pause for review. Destination selection and atomic purchase tokens remain intact.
- Exact independent Mystery odds: 50/25/15/7.5/2/0.5 percent. Rejection sampling avoids modulo bias. Purchase outcomes reveal on successful purchase, then retain species, rarity, identity and embryo genetics through normal incubation and larval hatching. **Production sales are transparently held** because the three highest tier pools are empty. There is no charge, roll, substitution or unauthorized species/rarity promotion while held.
- Persistent marine pattern identity and per-embryo inheritance. Natural Ocellaris uses independent 85/10/4/1 gameplay outcomes; exceptional natural patterns do not create designer varieties or promote rarity. New standard/Snowflake/Premium Snowflake stock supports a clearly labeled reference-line model based on the cited 2026 study. Other unverified designer crosses remain on visible holds. Legacy fish preserve existing visible art and unknown genotype. Natural bar processing protects approved eyes and facing. Pattern quality adds at most ±5% to centralized marine value.
- Continuous hidden/closed-browser progression at 20 real minutes per game day, replacing relaxed/capped modes. Existing ecosystem steps process all elapsed time asynchronously with progress and durable checkpoints. Actual water, food, equipment, disease, growth, egg and mortality models determine outcomes; closing the browser adds no mortality penalty. Healthy-day rewards use the same 50-AC per-player policy offline. Real return summaries report growth, hatches, medical events, deaths, equipment warnings, tank health and values.
- Additive validated ecosystem save migration, independent RNG streams, distinct simulation checkpoint, stable daily inventory, embryo profiles and bounded death/lineage history. A local timeline ledger rejects older same-world and repeated unchanged legacy import replays. Negative/invalid clocks fail safely. Interrupted catch-up resumes from its saved completed step.

## Actual verification

| Browser | Ecosystem + core/coral/disease/economy checks | Clownfish art/placement checks | Failed |
|---|---:|---:|---:|
| Chrome | 227 | 7583 | 0 |
| Edge | 227 | 7583 | 0 |

Each browser passed 7,810 checks across those two runs. Art coverage includes 1,792 directional cases per browser. Networking was disabled in isolated test profiles; no gameplay HTTP/HTTPS requests or JavaScript exceptions were observed in the ecosystem runs. The final ecosystem runs include the final embryo viability/value adjustment.

Evidence: tests/ecosystem-evidence/chrome-results.json and edge-results.json; tests/chrome-clownfish-results.json and edge-clownfish-results.json. The ecosystem suite reuses 68 established core/coral checks and 53 disease/value/economy checks, then adds integration, statistical and browser UI cases. The existing clock-setting fixtures synchronize their daily calendar, and the superseded capped-offline assertion now tests continuous progression. No protected baseline was rewritten.

Probability checks used 200,000 seeded draws for Mystery tiers and 200,000 for natural patterns, with absolute statistical tolerance rather than exact sample percentages. Snowflake reference crosses used 30,000 embryos each. Synthetic six-tier data exists only during a try/finally test fixture to exercise the held purchase/save/hatch path; all catalog metadata is restored immediately. No synthetic tier assignment enters the playable catalog.

Verified behaviors include real Continue after saved absence, actual restore-backup rejection, automatic hidden-tab return, open-store midnight refresh, interrupted asynchronous replay, 20/60-minute absence conversion, uncapped 10-hour absence, sync/async deterministic agreement, healthy survival and rewards, toxic-water deaths without rewards, actual feeder stock use, equipment wear, incubation, stable listing/embryo identity, transaction idempotency, coral/egg/bottom/fish inspectors, and layouts at 390/768/1366/1920px.

All 145 protected freshwater definition/art/source hashes match their prior baseline. A ten-day freshwater biological replay matches the earlier protected code exactly. Existing approved raster art was not overwritten. integrity.json records the final runtime hashes and MDP section count.

## Visual review

The daily-store and six-icon key screenshots were opened and visually inspected. Shapes, locked stepped colors, readable labels, destination/balance header and the explicit content-hold explanation are present. Evidence screenshots for each browser:

- tests/ecosystem-evidence/{browser}-daily-store.png
- tests/ecosystem-evidence/{browser}-rarity-key.png
- tests/ecosystem-evidence/{browser}-fish-inspector.png
- tests/ecosystem-evidence/{browser}-welcome-back.png

## Files edited and assets created

New runtime modules: js/rarity.js, js/patterns.js, js/daily-store.js, js/offline.js and css/rarity.css. New assets: assets/rarity/1.svg through 6.svg and mystery.svg (original transparent code-native pixel art).

Updated runtime integration: js/core.js, js/simulation.js, js/save.js, js/main.js, js/store.js, js/store-rules.js, js/ui.js, js/app-shell.js, js/gameplay.js, js/gameplay-ui.js, js/livestock-health.js, js/valuation.js, js/brood-view.js, js/render.js.

Updated module-loading pages: art-review-v1.html, art-review-v11.html, art-review.html, clownfish-review.html, coral-placement-review.html, index.html, life-stage-review.html, tests/eye-review.html, tests/index.html, tests/life-stage-contact.html, tests/sprite-audit.html. Tests/package.py includes the new evidence folder; tests/browser_qa.py adds --ecosystem, with ecosystem_checks.js, ecosystem_qa.py and this reproducible report builder. The obsolete relaxed/capped assertion in tests/suite.js is replaced by the authorized continuous policy.

Updated documentation: MASTER_DEVELOPMENT_PROMPT.md, GAME_DESIGN.md, ART_DIRECTION.md, UI_SPECIFICATION.md, DEVELOPMENT_STATUS.md, CURRENT_LIVESTOCK_CATALOG.md, BALANCE_REPORT.md, README.md, TEST_REPORT.md, plus RARITY_GENETICS_RESEARCH.md and this report. Earlier milestone sections are historical where superseded.

## Remaining limitations / tests not run

- Production Mystery Egg purchases cannot be tested with the approved catalog because Very Rare, Ultra Rare and Legendary pools are empty. The content hold and conditional synthetic-catalog pipeline both pass. Sales require a later authorized eligible-content decision; published odds are never redistributed.
- Only the documented Snowflake reference-line inheritance is modeled. Homozygous early nonviability is explicitly an inference from reported segregation, not a measured genotype or universal commercial-strain guarantee. Other unsupported designer crosses are held; cross-species hybrid breeding remains unauthorized.
- Existing provisional species art, taxonomy/care holds and simplified incubation, nutrition, disease and ecosystem models remain. Automated pixel/direction checks do not confer user art approval or validate clinical husbandry accuracy.
- Long absences are computationally replayed in batches, not tested by waiting real weeks. Extremely large saves remain subject to existing entity, numeric and 5-MB import bounds. A pre-2000 checkpoint requires recovery rather than silently discarding an implausible interval.
- Local storage and the timeline ledger are not secure anti-cheat; JSON editing, storage clearing or another device can bypass local bookkeeping. No backend, leaderboard or server authority was added. Lineage retains the latest 100 archived losses; existing event/medical/value logs remain bounded.
- No payment, deployment, unrelated gameplay expansion or freshwater biological/art development was performed. User review is the next milestone.

Portable release: AquariumLife-v0.1.zip, rebuilt by tests/package.py with archive CRC verification. Open index.html locally; no server is required.
