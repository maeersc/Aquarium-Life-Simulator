# Aquarium Life — Ocean Diving v2.8 implementation report

## Mystery fish diving — v3.9 current, 2026-10-15

Implemented the authorized Mystery Fish update (request v3.5) on top of playable v3.8. New valid Reef/Deep trips guarantee a reachable regional fish, concealed until boat return, with saved assignments, original question-mark art/reveal, explicit safe receiving and permanent transport-loss evidence. Empty/closed collectible pools block launch. Existing oxygen, fees, resale, local accounts, biology, genetics, breeding, care rewards and freshwater lock remain. See [MYSTERY_DIVING_RULES.md](MYSTERY_DIVING_RULES.md) and [MYSTERY_DIVING_UPDATE_REPORT.md](MYSTERY_DIVING_UPDATE_REPORT.md). Current master is v4.2; earlier release entries are historical where superseded.

Date: **2026-10-14**. MDP **v3.3**, exactly **31 major sections**.

Implemented the authorized diving update. **Zero new biological species**: the approved 38-entry v2.7 expansion remains the roster baseline. Current totals remain 80 fish (69 marine/11 freshwater), ten marine coral entries, five non-fish invertebrates and six protected freshwater plants.

## Features and regions

Ocean Diving is the authorized saltwater-only exploration feature v2.8. Use the existing fixed-step aquarium simulation, save, health, value, inventory and shared modal architecture. The button is always visible immediately beside the saved Keeper Level badge. Reef requires level 5 and costs exactly 1,000 AC; Deep Sea requires level 10 and costs exactly 10,000 AC. All rental/access components sum to that fixed total and are charged once by an atomic, confirmed launch transaction.

The data-driven registry `assets/diving/registry.json` currently enables Fiji, Caribbean, Hawaii and Japan. Its six encounter profiles reference existing v2.7 IDs, verified scientific names/ranges, appropriate habitats and conservative game depth bands. Unverified or incorrect-region organisms cannot spawn or be collected. Hawaii wildlife is observation-only; restricted fragments are explicitly fictional recovery and Black Market-only, never a claim of legal collection. Do not add future regions automatically or infer origin from common names. Preserve the approved 38-entry roster; diving catches are individuals, not new species.

Maps are compact 11×7 cell worlds with boat/descent, solid terrain, sand/reef scenery, nearby discoverable objects and traversable routes. W/A/S/D, arrows and direction buttons submit one cardinal movement action. Ignore native key auto-repeat; implement controlled held repeats. Only a completed movement costs exactly five oxygen percentage points. Start at 100%; blocked movement, frames, idle time and collection clicks cost no oxygen. Warn at 30, 15 and 5 percent and show route distance/return cost. Arrival must precede oxygen exhaustion; zero oxygen even on boat arrival fails. A nearby collection/physical return is winnable. No unapproved oxygen capacity or cost upgrades.

Left-click discovery selection and collection validate interaction distance at action time; moving fish have bounded positions. Each object occupies one of exactly eight temporary slots. Full inventory rejects new recovery without discarding existing discoveries. Nothing is permanently awarded before successful boat return. Exhaustion or explicitly confirmed abandonment records a non-graphic rescue, forfeits unreturned finds and gives no automatic fee refund.

Choose an explicit safe biological receiver before collecting livestock, and a supported mounting position for coral. Recheck safety cumulatively on return. Species sensitivity, prior condition, transport quality, elapsed game time, movement and receiving/quarantine conditions affect the saved assessment. Transport holding has a finite sensitivity-based deadline; animals cannot survive indefinitely in non-biological inventory. Persist healthy/stressed/injured/suspected illness/dead-on-arrival outcomes. Survivors enter existing fish/flora/invertebrate health systems and central valuation; unsafe or lost deliveries remain zero-value outcome records. Owned recovered rocks enter bounded inventory and are consumed through the existing placement workflow. Report region, mode, total fee, recovered objects, living/impaired/lost organisms, estimated asset value and resale eligibility. Never guarantee profit.

Planning, active play, confirmation and results run the authoritative aquarium simulation at 1× (20 real minutes = one game day), even if the underlying view was paused or accelerated. Keep hunger, chemistry, disease, growth, eggs, coral, equipment, calendar/store rotation and daily-care eligibility advancing through the same simulation; skip rendering the obscured aquarium. Preserve the prior speed preference when closing. Hidden/closed periods use existing offline catch-up. Save active position, oxygen, temporary IDs, collected flags, fee/transaction, region/mode and game state without relaunching or charging on resume. Core validation, transaction tokens, local completion receipts and existing timeline checks prevent normal duplicate/replayed settlement; editable local JSON is not cryptographic anti-cheat.

Use the approved hybrid pixel style and preserved original reference. Original diver/boat/oxygen/rock/effect/mask/crate/buoy art and eight regional backgrounds are local/embedded; existing species-specific living/dead artwork represents actual creatures. No new art is approved automatically. X, Escape and backdrop dismiss ordinary shared windows but require explicit loss confirmation for an active dive; inside clicks never dismiss or click through to aquarium objects. The oxygen/inventory/region/return HUD remains visible while scrolling. Other sections reference this primary specification rather than duplicating its rules.

## Verified regional profiles

Four regions, six deliberately conservative existing-species profiles. Hawaii is wildlife observation-only. Fiji/Hawaii deep dives currently have no verified eligible implemented livestock and offer inert fictional salvage. This is an honest limited encounter catalog, not an exhaustive regional ecosystem. No unverified species was silently assigned a location.

| Existing species / ID | Region / mode / game depth band | Collection / conservation | Evidence |
|---|---|---|---|
| Chalk Bass / *Serranus tortugarum* / `chalk-bass` | caribbean / reef / 12–90 m | fictional-restricted; Not treated as protected by this game; legal access is not asserted | [source](https://repository.library.noaa.gov/view/noaa/18269/noaa_18269_DS1.pdf) · [range](https://stri-sites.si.edu/docs/publications/pdfs/carvalho_filho_et_al_2023_serranus_fuscula.pdf) |
| Candy Basslet / *Liopropoma carmabi* / `candy-basslet` | caribbean / deep / 10–70 m | fictional-restricted; Game restricted specimen; no legal collection claim | [source](https://pmc.ncbi.nlm.nih.gov/articles/PMC4042691/) |
| Cactus Coral / *Pavona cactus* / `pavona-cactus` | fiji / reef / 3–20 m | fictional-restricted-fragment; CITES Appendix II stony coral; controlled trade, never an ordinary legal collectible. Fictional restricted fragment only. | [source](https://library.sprep.org/sites/default/files/518.pdf) · [range](https://www.coraltraits.org/species/1149/traits/218) |
| Porcelain Anemone Crab / *Neopetrolisthes maculatus* / `porcelain-anemone-crab` | japan / reef / 8–8 m | fictional-restricted; No real collection authorization; habitat/host sensitivity retained | [source](https://www.godac.jamstec.go.jp/bismal/e/view/9004880) |
| Blotched Anthias / *Odontanthias borbonius* / `blotched-anthias` | japan / deep / 70–300 m | fictional-restricted; IUCN Least Concern in cited museum profile; rarity is independent | [source](https://fishesofaustralia.net.au/Home/species/5363) · [range](https://www.jstage.jst.go.jp/article/jji/70/1/70_22-013/_pdf/-char/en) |
| Spotted Boxfish / *Ostracion meleagris* / `spotted-boxfish` | hawaii, japan / reef / 0–30 m | fictional-restricted; Least Concern in cited profile; Hawaii is observation-only regardless of rarity | [source](https://fishbase.se/Fieldguide/FieldGuideSummary.php?c_code=608&genusname=Ostracion&speciesname=meleagris) |


The cited NOAA chalk-bass profile documents Caribbean rubble/sand habitat and a wider 12–396 m range; the game's 12–90 m gate is a conservative subset. JAMSTEC documents the Japanese crab at 8 m. The Japanese anthias source documents deep reefs 70–300 m and the research paper records Japanese specimens at 95–100/180 m. Other depth gates are conservative game survey bands, not claimed complete distribution maps. The Fiji coral checklist supports native occurrence and controlled-trade context. Hawaii's observation-only game policy is conservative; this software does not grant real collection permission or teach extraction techniques.

## Actual tests

| Browser | Suite | Passed | Failed | Evidence |
|---|---|---:|---:|---|
| Chrome | Diving v2.8 | 108 | 0 | [tests/diving-evidence/chrome-results.json](tests/diving-evidence/chrome-results.json) |
| Chrome | Livestock/core/health/freshwater | 362 | 0 | [tests/expansion-evidence/chrome-results.json](tests/expansion-evidence/chrome-results.json) |
| Chrome | Artwork regression | 7,583 | 0 | [tests/chrome-clownfish-results.json](tests/chrome-clownfish-results.json) |
| Chrome | Deployed DIST / local PC saves | 247 | 0 | [tests/pages-evidence/chrome-results.json](tests/pages-evidence/chrome-results.json) |
| Edge | Diving v2.8 | 108 | 0 | [tests/diving-evidence/edge-results.json](tests/diving-evidence/edge-results.json) |
| Edge | Livestock/core/health/freshwater | 362 | 0 | [tests/expansion-evidence/edge-results.json](tests/expansion-evidence/edge-results.json) |
| Edge | Artwork regression | 7,583 | 0 | [tests/edge-clownfish-results.json](tests/edge-clownfish-results.json) |
| Edge | Deployed DIST / local PC saves | 247 | 0 | [tests/pages-evidence/edge-results.json](tests/pages-evidence/edge-results.json) |

Evidence includes real keyboard/mouse/modal actions, reload and local JSON-save tests. A test helper had to be reinstated after the intentional browser reload; early harness issues and high-tier fixtures reflecting old acquisition rules were corrected, then the suites rerun. Historical v2.6 empty-pool/old-roster expectations were not treated as current passes. The 145 protected hashes are in [integrity.json](tests/diving-evidence/integrity.json). Actual browser results, rather than this narrative, govern pass/fail status.

| Request test | Verified behavior |
|---:|---|
| 1 | PASS — Button beside Keeper Level: actual DOM order and locked visibility. |
| 2 | PASS — Reef unlock at saved level 5; level 4 rejects. |
| 3 | PASS — Deep unlock at saved level 10; level 9 rejects. |
| 4 | PASS — Reef flat fee exactly 1,000 AC through real UI and Core action. |
| 5 | PASS — Deep flat fee exactly 10,000 AC through real UI and Core action. |
| 6 | PASS — Breakdowns sum to flat totals, with one charge and idempotent launch token. |
| 7 | PASS — Exactly Fiji, Caribbean, Hawaii and Japan available; future Red Sea rejects. |
| 8 | PASS — Seeded region/mode encounter sweeps use the documented whitelist. |
| 9 | PASS — Incorrect-region map objects and owned provenance fail save validation. |
| 10 | PASS — Actual W/A/S/D browser key events complete a four-step circuit. |
| 11 | PASS — All four Arrow browser key events complete the same circuit. |
| 12 | PASS — Successful movement debits exactly five percentage points; held steps are bounded. |
| 13 | PASS — Blocked movement leaves position/oxygen unchanged. |
| 14 | PASS — Actual map/collection clicks and idle time consume no oxygen. |
| 15 | PASS — Actual left-click selection plus collect button recovers a nearby rock; out-of-range calls reject. |
| 16 | PASS — Eight real near-boat collections fill exactly eight temporary slots. |
| 17 | PASS — A ninth in-range collection rejects specifically for full inventory. |
| 18 | PASS — A real out-and-back path returns successfully with oxygen remaining. |
| 19 | PASS — Twentieth movement exhausts oxygen; zero even on boat arrival fails. |
| 20 | PASS — Failures/confirmed abandonment forfeit temporary items with no automatic fee refund. |
| 21 | PASS — Five species recovery outcomes round-trip through saved reports; actual living fish/coral/invertebrate fixtures verify provenance. |
| 22 | PASS — Unsafe receivers reject before capture and record loss if unsafe on return; coral attachments validate; holding expires. |
| 23 | PASS — Core and real Black Market Sell UI reject reputation 4 and unlock at reputation 5. |
| 24 | PASS — Confirmed saved dealer purchase awards bounded reputation; shared market action integration covers treatments/containment. |
| 25 | PASS — Opening/canceled/failed actions award zero; duplicate transaction returns the same state without XP. |
| 26 | PASS — Normal direct Tier 4–6 calls reject; real dealer listings support approved upper fish. |
| 27 | PASS — Exact 50/25/15/7.5/2/0.5 independent Mystery odds and all six fish pools retained. |
| 28 | PASS — Exactly 3 Common / 3 Uncommon / 1 Rare / 1 Mystery daily slots. |
| 29 | PASS — Actual planning, active and results windows advance the paused underlying aquarium at 1×. |
| 30 | PASS — Actual hunger/age/chemistry/equipment change; six simulated game hours advance eggs and day/store rotation. |
| 31 | PASS — 75 L displays 20 gal; 2,500 L displays 661 gal; preciseVolume retains fractions and internal liters. |
| 32 | PASS — Actual backdrop closes ordinary planning; interior click does not dismiss. |
| 33 | PASS — Actual regular X and Escape close planning; both protect an active trip. |
| 34 | PASS — All active-dismissal paths show loss confirmation and require explicit abandonment. |
| 35 | PASS — Actual browser reload restores active position/oxygen/haul and one fee; return rewards once; local completion receipt prevents old-snapshot settlement. |
| 36 | PASS — Actual file:// gameplay/art has no HTTP/HTTPS gameplay requests; DIST also tested on an HTTP repository subpath. |
| 37 | PASS — Eleven freshwater fish/six plants retained; 145 file hashes unchanged; expansion suite checks exact ten-day biology replay. |
| 38 | PASS — Additive legacy migration and existing expansion/health/art/deployment suites provide compatibility evidence. |

Not run: Firefox (not installed), actual remote GitHub Pages deployment, binary PDF rendering, and obsolete full milestone suites with superseded roster/empty-pool/gallon fixtures. Six-hour progression uses the actual simulation for 360 game minutes; actual real-time planning/active/results tests cover fixed-step advancement, not a five-real-minute wall-clock wait. No external account was changed and no site was published.

## Artwork

Built-in ImageGen created **nine original PNG assets**: eight distinct regional reef/deep backgrounds and a transparent eight-object equipment sprite sheet. All are saved at [assets/diving/](assets/diving/) and embedded by `tests/pack_diving_art.py` into `js/diving-art-data.js`. [Exact prompt set and generated filenames](assets/diving/art-prompts.json). [Visual contact sheet](tests/diving-evidence/background-contact.png). Sources are preserved; existing approved fish/reference files were not overwritten. New art is **unapproved, pending user review**. The diver uses a static authored pose; movement and collection sparkle are runtime effects, not a newly authored multi-pose swimming cycle. Existing v2.7 framing/breeding/earliest-stage limits remain.

## Files edited

- Added `js/diving-data.js`, `diving.js`, `diving-art.js`, `diving-art-data.js`, `diving-ui.js`; `css/diving.css`; nine source PNGs, prompt record and permanent `assets/diving/registry.json`.
- Updated `index.html`, `js/core.js`, `save.js`, `main.js`, `livestock-market.js`, `health-save.js`, `store.js`, `store-rules.js`, `ui.js`, `expansion-ui.js`, `invertebrates.js`, `valuation.js`, `simulation.js`, `gameplay.js`, `app-shell.js`. Shared hooks preserve existing atomic validation, health/value factors, geometry, saved selection and fixed-step chemistry. Freshwater species/biology and original art remain protected.
- Added diving logic/resale/input/browser tests and art packer; updated browser runner, authorized high-tier expansion test fixtures, build and package scripts. Evidence lives in `tests/diving-evidence/`. Temporary integration scripts are removed before packaging.
- Updated all six required project docs, catalog, README, TEST_REPORT, consolidated master, generation record, region ledger and printable/PDF continuity source. Rebuilt `DIST` and the GitHub Pages upload ZIP from current sources.

## Limits and persistence

All saves, recovery data, timeline and diving completion receipts stay in the player's browser on their PC. Export/import JSON remains local. Receipt/timeline guards prevent normal repeat/reload settlement; editable local data is not cryptographically tamper-proof or a verified leaderboard. Clearing browser site data also clears those local guards. Active trips resume with saved oxygen; prolonged absence advances aquarium time and can expire transported livestock before return. No oxygen upgrades, future regions, newly invented species or practical collection instructions were added.

Survival, sensitivity, holding deadlines, medical conditions, reputation and collector demand are bounded game parameters, not measured field/veterinary outcomes. Explicit unsafe receiving conditions cause a recorded loss, never silent unsafe placement. Restricted coral is fictional fragment recovery with permanent source risk and Black Market-only resale, separate from actual legal permissions.

**PDF source is updated; binary PDF regeneration remains pending** the unavailable PDF toolchain. New artwork awaits user approval; existing roster/art limits are preserved. [GitHub Pages instructions](GITHUB_PAGES.md) and [build manifest](DIST/build-manifest.json) document the portable delivery. Run `python build.py` after future edits to refresh DIST and its upload ZIP.


Equipment framing correction: the generated boat crossed a nominal source cell boundary. The preserved source was technically packed into `assets/diving/equipment-atlas-v1.png` using alpha gutters; `equipment-atlas-metadata-v1.json` records all eight source bounds. Icons retain their source aspect ratios. No semantic repainting or source overwrite occurred.
