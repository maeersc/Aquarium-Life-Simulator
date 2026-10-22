# Aquarium Life v2.9 implementation report

Historical record: earlier survival-reward amounts and results below are superseded by v3.4. Current payments are 100 AC plus a separate independently qualified 50-AC healthy award. Actual historical receipts/test evidence are preserved, not rewritten. See V34_UPDATE_REPORT.md.

Implemented on 2026-10-14 after the user approved the complete roster/rarities, confirmed saltwater-only and explicitly requested **Implement v2.9**. [Authorization](planning/v2.9/approval.json), [original requirements](planning/v2.9/REQUIREMENTS.md).

## Result

The game now includes the saved twelve-step saltwater tutorial, medical example, three-second livestock selection outlines, freshwater UI/transaction lock, separate healthy/survival rewards, Deep Market display name, local asset-value leaderboard preview, exact 15,000-gallon aquarium and proportional marine replacement salt. New livestock, original stage artwork and mystery products are integrated additively.

**DIST and both ZIPs are rebuilt. Saves remain on each player's PC**, in that browser's localStorage with local recovery backups and user-controlled JSON download/import. No accounts, cloud saves, analytics or save server were added. Hosted storage belongs to its browser/profile/site origin; use JSON export/import to move progress between the local folder and a Pages URL.

## Livestock and art

Added exactly **25 fish, five corals and five non-fish bottom dwellers**, with the approved IDs/rarities. All categories contain Ultra Rare and Legendary records. The complete names, scientific identities, aliases, care, diets, minimum capacities, holds, sources, implementation status and art paths are in [the permanent v2.9 registry](assets/expansion-v29/registry.json) and [current catalog](CURRENT_LIVESTOCK_CATALOG.md).

Current registered totals: **105 fish (94 marine / 11 retained freshwater), 15 marine coral records, 10 marine invertebrates and six retained freshwater plants**. The earlier 38-entry batch and clownfish/designer collection remain separate and intact. No old species was replaced; aliases and previously recorded art-only subjects were screened. Generic legacy coral groups remain legacy identities, not newly verified species.

Coleman's shrimp is **registered but acquisition-held** because its obligatory fire-urchin host is not implemented. The approved roster did not authorize inventing another host species. Consequently the production Mystery Bottom-Dweller Egg visibly holds purchases for its empty eligible Legendary tier. No charge, replacement tier or probability reweight occurs. A controlled complete-pool test fixture verifies the nursery machinery without releasing the held animal.

Thirty-five separate original image-generation calls plus six refinements produced transparent species sheets. The built-in `image_gen.imagegen` tool was used; no CLI fallback. All original generated files were preserved; project copies, exact prompts and refinement records are in [art-generation-record.json](assets/expansion-v29/art-generation-record.json). Each folder retains source images, prompt versions, atlas and metadata. Technical processing only alpha-crops and fits complete subjects using nearest-neighbor scaling, including per-subject row boundaries.

There are **280 authored static stage/state views**, covering earliest equivalents, baby/larva, juvenile/growing and adult/mature, alive/deceased. Five stage contact pages and the adult contact were visually inspected. Complete sprites mirror for left/right motion. **All new art remains unapproved**: roster approval is separate. One Yellow scroll coral adult source-boundary flag, provisional eye coordinates, stylized early biology and static poses are disclosed. Full swim/turn/feed animation, sex-specific variants and researched natural reproduction are not claimed. [Offline review gallery](v29-review.html).

## Implemented behavior

- New Game starts the twelve lessons with Next, Back, Show me, Skip, saved Resume and Settings Restart. Medical guidance uses an example and real inspection/diagnostic/quarantine/medicine destinations; it does not create illness or bypass cycling. The first achievement uses the actual once-only preparation quest reward, 120 AC and 100 XP.
- Selection expires three real seconds after the latest click, independently of game speed. Reclick/transfer/tank switch are handled; inspectors stay open. Fish, corals, invertebrates and nurseries use the same deadline.
- Freshwater creation, selection, purchases and interaction controls are disabled and explain the future-content lock. Existing species, art, saves and biological simulation remain retained. Future development milestones must ask whether freshwater is next; this milestone's answer is already recorded.
- Healthy-day **+50 AC** and survival **+200 AC** are separate player-wide awards. A genuine fully tracked stocked game day is required; empty tanks and additional tanks do not multiply payment. A confirmed fish/coral/invertebrate/nursery loss cancels the day and starts/restarts a complete 1,440-minute recovery. Living illness/bleaching is not death. Saved day/payment/loss checkpoints prevent reload replay; offline simulation uses the same rules. Backward wall-clock changes do not rewind the checkpoint. Fully offline device clocks cannot be cryptographically authenticated.
- Player-facing Deep Market labels preserve internal `black` identities, reputation, dealer quotes/hidden condition, restricted medicines, inventory and diving resale. The market remains inside Aquarium Store. Ordinary direct livestock stays T1–T3; eligible upper-tier coral/invertebrate dealer listings retain their saved price and risk.
- Field Journal Leaderboards compares only owned marine aquariums locally using central current installed asset value, excluding wallet and uninstalled inventory. Freshwater is a locked preview. No public rankings, fake players, accounts or seventh sidebar window.
- Mystery Coral costs 450 AC; the bottom nursery product is calibrated at 500 AC. Separate persistent random streams use exact independent **50 / 25 / 15 / 7.5 / 2 / 0.5%** tiers, with all pools and safe receivers validated before charge/roll. Three daily stock each do not change the eight Fish slots. Coral requires the player's supported mount before purchase. The bottom development abstraction takes 48 suitable hours, persists viability/outcome/value, reserves capacity and settles once into the **same-ID small juvenile**, never an instant adult. Confirmed losses feed the survival rules.
- Additive schema-2 migration introduces a version-1 v2.9 extension and new inventories/listings without resetting old progress or rerolling existing dealer/fish selections. Validation rejects malformed extensions, duplicate IDs and invalid new mystery roll/rarity pairs. Store destination selection and placements persist through shopping and reload.

## Large tank and balance audit

Ocean Sanctuary is **15,000 US gal = 56,781.17676 L**, purchased for exactly **5,000 AC total**, at Keeper Level 10. No marine markup is applied. It starts empty/dry. Its defined water envelope is 1,000 × 400 × 141.9529419 cm, substrate area 40 m²; structural engineering and displacement are outside the game. Actual saved volume drives equipment capacity, existing price/energy/service formulas, water and substrate costs. Habitat/readiness checks still apply; the cheap shell does not include life support or livestock. Freshwater capability is future-locked.

Replacement water retains `ceil(changed liters × 0.13)` for marine water. Marine salt now consumes one dose per two actual changed liters, rounded up; freshwater conditioner/biology stays unchanged. The smallest actual catalog tank is **20 L**, shown as 6 gal, rather than 20 US gallons.

| Change | Actual replacement water | Water charge | Salt doses |
|---|---:|---:|---:|
| 20-L tank, 10% | 2 L | 1 AC | 1 |
| 15,000-gal tank, 10% | 5,678.117676 L | 739 AC | 2,840 |

Salt packs are 35 AC per ten doses: 284 packs cost 9,940 AC. Thus a 10% large-tank change costs **10,679 AC** including water, before power, food, medicine or repairs. That equals 42.716 ideal 250-AC bonus days; one weekly change averages 1,525.57 AC/game day. The older 5,000-L Ocean Hall costs 33,750 AC marine, exposing the approved new shell's substantial price inversion. These affordability limits are documented, not hidden through a changed purchase price. No long-duration 15,000-gallon affordability playtest is claimed; the report gives exact arithmetic and real purchase/maintenance transaction tests. [Balance report](BALANCE_REPORT.md).

## Executed tests and corrections

Final browser results are stored as JSON and screenshots under the linked evidence folders. Counts include individual checks, not separate test runs; 373 v2.9 model checks are included in each 412 total.

| Suite | Chrome | Edge | Evidence |
|---|---:|---:|---|
| v2.9 model, real controls, reload, placement, compact layouts and new gallery | 412 passed / 0 failed | 412 passed / 0 failed | [v2.9](tests/update29-evidence/) |
| Existing livestock/core/health/economy and retained biology | 362 passed / 0 failed | 362 passed / 0 failed | [regressions](tests/expansion-evidence/) |
| Diving, Deep Market reputation and resale | 108 passed / 0 failed | 108 passed / 0 failed | [diving](tests/diving-evidence/) |
| Protected clownfish artwork/directional collection | 7,583 passed / 0 failed | 7,583 passed / 0 failed | [artwork](tests/chrome-clownfish-results.json) |
| Rebuilt DIST at HTTP repository subpath, real local JSON export/import/autosave/profile isolation | 247 passed / 0 failed | 247 passed / 0 failed | [Pages](tests/pages-evidence/) |
| **Total per browser** | **8,712 passed / 0 failed** | **8,712 passed / 0 failed** | **17,424 combined** |

Also verified: all **1,426** pre-existing asset hashes, unchanged original `js/data.js`, the 145-file freshwater protection set used by the regressions, ten-day freshwater replay against protected earlier code, 31 numbered master sections, full master text in the printable continuity source, every old/new batch ID in that source, all new IDs in the catalog, nonapproval of new art, source/DIST hashes and ZIP CRCs.

Early runs exposed and corrected a nursery-row syntax error, floating-point gallon label edge, missing new-tank nursery initialization, nonuniform atlas cropping, incorrect rock mounting candidates, provenance validation, small-screen width feedback and test-only fixture assumptions. Earlier failures are superseded by the final evidence, not treated as passing runs. Browser graphics failed inside the sandbox, so the approved isolated headless runners were used outside it.

Legacy suite fixtures were updated for the approved additive totals, Deep Market name, proportional salt and separate survival income. Retained freshwater mechanics are tested in an explicitly isolated adapter that temporarily removes the two **new access gates**, then restores them; production freshwater gating is separately tested in v2.9. Manually edited fixture calendars are resynchronized; real simulation/reload checkpoints are not bypassed. The standalone clownfish gallery deliberately retains its own 80-record historical baseline; the game runtime has 105.

Not run/claimed: Firefox, native OS fullscreen/desktop wrapping, user artwork approval, clinical or real-world husbandry validation, natural breeding for the new species, full sprite animation, production bottom-mystery purchase while held, a large-tank long-duration affordability playtest, or binary PDF export/render verification. Local save integrity is not a competitive anti-cheat service.

## Original 35-item acceptance mapping

Items 1–8: tutorial start/skip/resume/medical, outline expiry/inspector, freshwater UI/purchases and retained data are covered by real browser input/reload, model rejection, hashes and the protected biology replay. Items 9–14: actual fixed-step/offline +50/+200 payments, death cancellation, repeated loss/recovery, later resumption and save replay are model tested. Items 15–16: Deep Market UI, old reputation/listing migration and real resale are covered by v2.9/diving checks; presentation of legacy log text is converted without changing saved IDs.

Items 17–20: both preview views, local asset valuation, no wallet metric or network/accounts are tested. Items 21–25: exact tank registration, actual 5,000-AC UI purchase, future freshwater lock, 20-L baseline, exact changed liters/charge/doses and atomic insufficient-salt rejection are tested. Items 26–28: 35 unique approved records, separate old 38-entry registry, scientific identity/alias screening and category T5/T6 coverage are checked against approval and ledgers.

Items 29–33: exact summed odds, all twelve coral CDF boundary transactions, independent streams, persisted outcomes/identity/health/mount, conditional nursery settlement/reload and empty-tier content hold/no-substitution are exercised. **Item 34 is partial:** original style/stage/directional artwork was produced and visually inspected, but remains unapproved with the disclosed boundary/static-pose limits. Item 35: browsers run without external traffic and deployed saves/export/import remain device-local. This mapping does not promote subjective art approval into a passed automated assertion.

## Files and release

New runtime: `js/update29-data.js`, `update29-catalog.js`, `update29-art-data.js`, `update29.js`, `update29-ui.js`, `update29-review.js`, `css/update29.css`, `v29-review.html`, and `assets/expansion-v29/` sources/prompts/atlases/metadata/registry/contact sheets. The registry records each of the 35 species and every original project asset path.

Shared integration edits: `index.html`; `js/core.js`, `save.js`, `simulation.js`, `gameplay.js`, `offline.js`, `ui.js`, `app-shell.js`, `main.js`, `store.js`, `store-rules.js`, `livestock-market.js`, `livestock-health.js`, `valuation.js`, `invertebrates.js`, `expansion.js`, `expansion-ui.js`, `expansion-art.js`, `diving.js`, `diving-ui.js`, `health-ui.js`; build/package scripts and relevant browser/model regression fixtures. Original biological definitions and old image files were preserved.

Documentation updated: current livestock catalog and permanent v2.9 registry; GAME_DESIGN, UI_SPECIFICATION, ART_DIRECTION, DEVELOPMENT_STATUS, BALANCE_REPORT; the single 31-section **MDP v3.5**; PROJECT_CONTINUITY_SOURCE and PDF_WORKFLOW; README, TEST_REPORT, ART_GENERATION_RECORD, GITHUB_PAGES_BUILD_REPORT; archived proposal with its later authorization notice; this report and machine evidence. The printable continuity source includes all old/new batch IDs, full master and permanent back-of-source rules. **Binary PDF regeneration remains pending** under the existing unsupported-export allowance; no new verified PDF is claimed.

`python build.py` rebuilt **DIST: 1,505 source files / 455,864,429 source bytes**, plus `.nojekyll` and build manifest. All selected source hashes match. `AquariumLife-GitHub-Pages.zip` contains `index.html` at its root and has a verified CRC; upload the **extracted DIST contents** for Pages. `python tests/package.py` refreshes the full historical-name `AquariumLife-v0.1.zip` source/evidence package without test browser profiles, downloads or actual player saves. The manifest, Pages archive size/hash and packaging command are recorded in [release verification](tests/update29-evidence/release-verification.json).
