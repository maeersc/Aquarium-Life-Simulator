# Aquarium Life — complete project audit

Historical milestone report. Current gameplay/time/settings results are in [GAMEPLAY_UPDATE_REPORT.md](GAMEPLAY_UPDATE_REPORT.md); this is not a new full-project audit.

> Historical snapshot notice: this is the October 12 audit. The subsequently authorized [marine economy/disease/valuation update](ECONOMY_DISEASE_UPDATE_REPORT.md) and [main UI overhaul](UI_OVERHAUL_REPORT.md) change some findings, including navigation, scrolling, dry tank creation, egg placement, equipment inventory, quantity input, transfers, living bleaching and valuation. Original checklist classifications/counts have not been re-audited. Root regression artifacts may have newer reruns; the original boundary observations remain in tests/audit-evidence.

Audit date: **2026-10-12**. Target: the user's complete project checklist v1.0 and the consolidated **31-section MDP v2.7**, including the lighting, life-stage, eye/facing, coral mounting, saltwater scope and permanent store-destination rules. This is an audit of the current playable v0.1 implementation, not a declaration that the entire MDP has shipped.

The original checklist and its SHA-256 are preserved in [audit-checklist-source.json](tests/audit-checklist-source.json). Every one of its **668 feature checks** is classified in section G. The six introductory status definitions are not feature checks. Report headings A–H and the stop instruction are deliverable instructions, not additional completion points. Status is assessed for the wording of each check: an existing category/name or mapped image can pass while its broader feature remains incomplete.

Only audit infrastructure, evidence files, this report and the permitted livestock catalog audit notes were changed. **Game JavaScript, CSS, HTML, consolidated MDP and gameplay rules were not changed.** Forty-two source/document hashes match the pre-audit baseline. Existing user saves were not opened or modified; browser observations use isolated test profiles. The release ZIP was integrity-checked, not rebuilt.

## A. Executive Summary

**The project is a functioning offline vertical slice with substantial unfinished specification work and several reproducible defects. It is not complete against the full MDP.** Offline launch, core chemistry, feeding/health, bounded transactions, persistent individual fish, quests, equipment, manual lighting and the shared store work in the exercised scenarios. Store opening/closing/tab changes/purchases preserve the selected aquarium. Purchases reject unsafe water and incompatible habitats. Protected freshwater data/art remain unchanged.

Both Chrome and Edge reproduce the same important gaps:

- Changing fish quantity in the real store detail form throws an uncaught `TypeError` from an obsolete UI handler. The modal's own compatibility update runs first; this is a broken interaction, not a demonstrated startup crash or duplicated charge.
- Geometry can label a shallow sandbase or upper rack placement Suitable, while save validation rejects its vertical coordinate. Rejected transactions remain atomic.
- Fish/coral transfers do not use all purchase-admission rules: unsafe water and mixed clownfish territories can be accepted by Core actions. Purchases themselves correctly block these cases.
- Fish have no rock-collision integration, and legal center coordinates can clip an entire adult silhouette against the glass.
- SPS transfer UI omits a valid destination mounting position; grown coral geometry and side-glass rack movement have additional validation gaps.

Major unfinished requirements include completely dry new tanks, water filling, physical tank dimensions, substrate mass/displacement/maturation/algae/cleaning, independent living coral bleaching, finite corpse/tissue decomposition, some nutrition/genetics/value rules, illustrated VIP tiers, dedicated seasonal content and three graphics presets. Current sand depth and rock ownership are functional visual/mounting systems; their existence does not supply those missing biological systems.

No save corruption, startup crash, duplicate-charge exploit or infinite resale profit was reproduced in the executed fixtures. This does not certify every possible action sequence. Important open risks are the differences between legacy and new admission/UI paths, provisional species care/anatomy, absent expanded economy scenarios, stale historical test assertions, and untested extended memory/frame-pacing behavior. Firefox, real-player save collections, screen readers and long wall-clock soak tests were not verified.

## B. Completion Metrics

| Status | Checks |
|---|---:|
| PASS | 491 |
| PARTIAL | 112 |
| FAIL | 11 |
| MISSING | 47 |
| NOT TESTED | 3 |
| NOT APPLICABLE | 4 |
| Total feature checks | 668 |
| Applicable checks | 664 |
| Verified pass percentage | **491/664 = 73.95%** |

Applicable checks = total checks minus NOT APPLICABLE. **NOT TESTED remains in the applicable denominator and is not successful.** PARTIAL, FAIL and MISSING are also not successful. This unweighted percentage measures checklist outcomes, not release readiness or the fraction of engineering effort remaining; the roster/category-name checks have the same numeric weight as save safety and entire biological systems.

## C. Livestock Inventory

| Inventory measure | Count |
|---|---:|
| Implemented marine fish, including marine bottom dwellers | 41 |
| Implemented clownfish named catalog entries | 31 |
| Designer clownfish phenotypes (not extra species) | 25 |
| Implemented coral groups | 5 |
| Bottom dwellers, already included in fish totals | 4 (2 marine / 2 freshwater) |
| Protected existing freshwater fish | 11 |
| Combined implemented fish | 52 |
| Combined base livestock entries, fish + coral | 57 |
| Fully complete eight-slot base art presentation chains | 57 |
| Fully complete eight-slot designer presentation chains | 25 |
| Incomplete historical ART ONLY chains | 5 |
| Fully user-approved complete new stage chains | 0 |
| DATA ONLY / PLANNED entries | 0 / 3 |

“Implemented” means a runtime catalog/rendering definition, not an assertion that it is currently purchasable or scientifically complete. Marine count includes the explicitly fictional Voidfin Specter; freshwater count includes the protected fictional Glassfang Eel. Benthic fish are counted once inside the 52 fish records. Designer phenotypes never add a biological species.

**Artwork completeness has three separate meanings.** All 57 implemented base entries map eight required alive/dead stage views; 25 designers add another 200 presentations with shared base eggs/larvae. This gives 82 complete presentation chains / 656 stage-state presentations. Five historical art-only fish remain incomplete in stage coverage. There are **zero fully user-approved complete new stage chains**; approval of the existing adult Ocellaris image does not approve all new life-stage/anatomy assets. All 31 clownfish catalog entries and 25 designer entries have adult swim cycles; the other 21 implemented fish currently use static stage poses.

The collection comprises 31 named clownfish catalog entries (including explicitly uncertain hybrid-origin entries) and 25 commercial phenotype records. Five specialist care profiles are purchase-held: Whitebonnet, McCulloch's, Wide-band, Thielle's and Polynesian. Their catalog presence passes presence checks; their care/purchase readiness remains incomplete. The complete current inventory with per-entry paths/status/stages is in [CURRENT_LIVESTOCK_CATALOG.md](CURRENT_LIVESTOCK_CATALOG.md).

Coral groups: Garden zoanthids (`zoa`), Mushroom coral (`mushroom`), Branching SPS (`sps`), Hammer LPS (`lps`) and Soft leather coral (`soft`). Precise species identity is unverified. Bottom dwellers: Bronze corydoras (`cory`) and Bristlenose pleco (`pleco`) freshwater; Yellow watchman goby (`watchman`) and Tailspot blenny (`blenny`) marine.

The five **ART ONLY** subjects are Niger triggerfish (*Odonus niger*), Emperor angelfish (*Pomacanthus imperator*), Red lionfish (*Pterois volitans*), Dogface puffer (*Arothron nigropunctatus*) and Blue tang (*Paracanthurus hepatus*). Each has adult four-frame art, not a complete early/dead chain or a gameplay species definition. Three fictional proposals remain **PLANNED** with no completed art: Emberjaw Leviathan, Abyssal Crownfish and Prismheart Ray. DATA ONLY count is zero.

Local integrity checks verify 96 embedded atlas records: 13 earlier fish/coral/rock banks, 27 earlier stage atlases and 56 clownfish sheets. Every recorded atlas has the expected dimensions, binary alpha, transparency and byte-identical embedded PNG; 134 literal local runtime resource references exist. No missing literal runtime asset or HTTP(S) game request was found. Preserved historical Ocellaris sheets account for overlap between bank records and unique catalog entries.

### Clownfish species / designer inventory

| Clownfish common name | Scientific name | Runtime ID | Availability |
|---|---|---|---|
| Ocellaris clownfish | *Amphiprion ocellaris* | `clown` | Catalog/store; admission rules apply |
| True Percula clownfish | *Amphiprion percula* | `amphiprion-percula` | Catalog/store; admission rules apply |
| Maroon clownfish | *Amphiprion biaculeatus* | `amphiprion-biaculeatus` | Catalog/store; admission rules apply |
| Clark's clownfish | *Amphiprion clarkii* | `amphiprion-clarkii` | Catalog/store; admission rules apply |
| Tomato clownfish | *Amphiprion frenatus* | `amphiprion-frenatus` | Catalog/store; admission rules apply |
| Cinnamon / Fire clownfish | *Amphiprion melanopus* | `amphiprion-melanopus` | Catalog/store; admission rules apply |
| Red Saddleback clownfish | *Amphiprion ephippium* | `amphiprion-ephippium` | Catalog/store; admission rules apply |
| Pink Skunk clownfish | *Amphiprion perideraion* | `amphiprion-perideraion` | Catalog/store; admission rules apply |
| Orange Skunk clownfish | *Amphiprion sandaracinos* | `amphiprion-sandaracinos` | Catalog/store; admission rules apply |
| Skunk clownfish | *Amphiprion akallopisos* | `amphiprion-akallopisos` | Catalog/store; admission rules apply |
| Saddleback clownfish | *Amphiprion polymnus* | `amphiprion-polymnus` | Catalog/store; admission rules apply |
| Sebae clownfish | *Amphiprion sebae* | `amphiprion-sebae` | Catalog/store; admission rules apply |
| Barrier Reef clownfish | *Amphiprion akindynos* | `amphiprion-akindynos` | Catalog/store; admission rules apply |
| Allard's clownfish | *Amphiprion allardi* | `amphiprion-allardi` | Catalog/store; admission rules apply |
| Red Sea Twoband clownfish | *Amphiprion bicinctus* | `amphiprion-bicinctus` | Catalog/store; admission rules apply |
| Orangefin clownfish | *Amphiprion chrysopterus* | `amphiprion-chrysopterus` | Catalog/store; admission rules apply |
| Maldives clownfish | *Amphiprion nigripes* | `amphiprion-nigripes` | Catalog/store; admission rules apply |
| Oman clownfish | *Amphiprion omanensis* | `amphiprion-omanensis` | Catalog/store; admission rules apply |
| Chagos clownfish | *Amphiprion chagosensis* | `amphiprion-chagosensis` | Catalog/store; admission rules apply |
| Mauritius clownfish | *Amphiprion chrysogaster* | `amphiprion-chrysogaster` | Catalog/store; admission rules apply |
| Seychelles clownfish | *Amphiprion fuscocaudatus* | `amphiprion-fuscocaudatus` | Catalog/store; admission rules apply |
| Madagascar clownfish | *Amphiprion latifasciatus* | `amphiprion-latifasciatus` | Catalog/store; admission rules apply |
| Whitebonnet clownfish | *Amphiprion leucokranos* | `amphiprion-leucokranos` | Purchase-held; provisional specialist care |
| McCulloch's clownfish | *Amphiprion mccullochi* | `amphiprion-mccullochi` | Purchase-held; provisional specialist care |
| Wide-band clownfish | *Amphiprion latezonatus* | `amphiprion-latezonatus` | Purchase-held; provisional specialist care |
| Australian Red clownfish | *Amphiprion rubrocinctus* | `amphiprion-rubrocinctus` | Catalog/store; admission rules apply |
| Three-band clownfish | *Amphiprion tricinctus* | `amphiprion-tricinctus` | Catalog/store; admission rules apply |
| Barber's clownfish | *Amphiprion barberi* | `amphiprion-barberi` | Catalog/store; admission rules apply |
| Pacific clownfish | *Amphiprion pacificus* | `amphiprion-pacificus` | Catalog/store; admission rules apply |
| Thielle's clownfish | *Amphiprion thiellei* | `amphiprion-thiellei` | Purchase-held; provisional specialist care |
| Polynesian clownfish | *Amphiprion maohiensis* | `amphiprion-maohiensis` | Purchase-held; provisional specialist care |

| Designer phenotype | Biological base | Stage presentation |
|---|---|---|
| Black Ocellaris | *Amphiprion ocellaris* | Eight slots; shared base egg/larva; provisional approval |
| Snowflake Ocellaris | *Amphiprion ocellaris* | Eight slots; shared base egg/larva; provisional approval |
| Premium Snowflake | *Amphiprion ocellaris* | Eight slots; shared base egg/larva; provisional approval |
| Black Snowflake | *Amphiprion ocellaris* | Eight slots; shared base egg/larva; provisional approval |
| Black Ice Snowflake | *Amphiprion ocellaris* | Eight slots; shared base egg/larva; provisional approval |
| Wyoming White | *Amphiprion ocellaris* | Eight slots; shared base egg/larva; provisional approval |
| Snow Storm | *Amphiprion ocellaris* | Eight slots; shared base egg/larva; provisional approval |
| Black Storm | *Amphiprion ocellaris* | Eight slots; shared base egg/larva; provisional approval |
| Mocha Storm | *Amphiprion ocellaris* | Eight slots; shared base egg/larva; provisional approval |
| Mocha Ocellaris | *Amphiprion ocellaris* | Eight slots; shared base egg/larva; provisional approval |
| Gladiator | *Amphiprion ocellaris* | Eight slots; shared base egg/larva; provisional approval |
| Mocha Gladiator | *Amphiprion ocellaris* | Eight slots; shared base egg/larva; provisional approval |
| DaVinci | *Amphiprion ocellaris* | Eight slots; shared base egg/larva; provisional approval |
| Frostbite | *Amphiprion ocellaris* | Eight slots; shared base egg/larva; provisional approval |
| Black Frostbite | *Amphiprion ocellaris* | Eight slots; shared base egg/larva; provisional approval |
| Midnight | *Amphiprion ocellaris* | Eight slots; shared base egg/larva; provisional approval |
| Domino | *Amphiprion ocellaris* | Eight slots; shared base egg/larva; provisional approval |
| Naked Ocellaris | *Amphiprion ocellaris* | Eight slots; shared base egg/larva; provisional approval |
| Misbar Ocellaris | *Amphiprion ocellaris* | Eight slots; shared base egg/larva; provisional approval |
| Longfin Ocellaris | *Amphiprion ocellaris* | Eight slots; shared base egg/larva; provisional approval |
| Picasso Percula | *Amphiprion percula* | Eight slots; shared base egg/larva; provisional approval |
| Premium Picasso Percula | *Amphiprion percula* | Eight slots; shared base egg/larva; provisional approval |
| Platinum Percula | *Amphiprion percula* | Eight slots; shared base egg/larva; provisional approval |
| Onyx Percula | *Amphiprion percula* | Eight slots; shared base egg/larva; provisional approval |
| Lightning Maroon | *Amphiprion biaculeatus* | Eight slots; shared base egg/larva; provisional approval |

Taxonomic verification is narrower than biological care certification. The 31 supplied names were checked against the current [WoRMS Amphiprion taxon list](https://www.marinespecies.org/aphia.php?p=taxlist&tName=Amphiprion). The project's FishBase source could not be rechecked in this audit because the request returned HTTP 403. Commercial source review used the primary [ORA clownfish catalog](https://www.orafarm.com/products/fish/clownfish/); Mocha Storm, Mocha Ocellaris and Onyx Percula reference confidence remains provisional. A taxon listing or commercial label does not establish definitive hybrid ancestry, breeding segregation, lifespan or husbandry. No scientific data was changed.

## D. Visual Issues

| Finding | Classification and evidence |
|---|---|
| Eye anchoring and sprite directions | Technical tests and manual contacts found no detached-eye or reversed-head defect at tested sizes/directions. Transform reset and odd-width mirroring pass. Tank-edge clipping can still crop visible anatomy (I06). This is not universal anatomy/user approval. |
| Reference consistency | Detailed coral/rock/fish art is present; older animal sheets have finer/noisier texture density than newer clownfish. Sand/equipment/decorations remain procedural. Exact species/morph anatomy and full stylistic acceptance remain provisional (I18/I24). |
| Life-stage availability | All implemented entries have eight mapped presentations. Five historical art-only fish lack full early/dead sets. Coral early stages are gallery assets rather than a complete staged colony simulation (I23/I18). |
| Movement/animation | Stable mirrored turns exist; perspective turn poses and bite animation are missing. Most non-clownfish adult fins are frozen because the renderer chooses one static stage frame (R15/I15). |
| Coral support visuals | Open-water/rock-interior/new-placement overlap rejection works. Shallow/upper positions disagree with save validation; side racks can lose glass anchoring; growth/depth edits skip full silhouette validation (R05/R06/R09/R10/I02/I04/I07). |
| Rock artwork | Three distinct collections × four sizes/arch variants have detailed transparent art and alpha geometry. No missing rock atlas was found. Geometry is not yet used by fish AI; dry/live state art is absent (I05). |
| Coral bleaching/death | Bleached art exists, but the main runtime state selector never returns it. Dead stony skeleton and collapsed soft art exist; algae-covered/degrading remains do not (I11/I12). |
| Store images | Actual collection thumbnails loaded, including all 52 field-guide fish. Existing fish/coral/rock products use local art. Equipment/consumables use illustrative procedural previews. No broken image was reproduced; VIP has text cards rather than actual tier-specific images (I17). |

Representative current visual evidence: [all fish contact page 2](tests/audit-evidence/chrome-fish-contact-2.png), [clownfish contact page 7](tests/audit-evidence/chrome-fish-contact-7.png), [designer contact page 3](assets/previews/clownfish-varieties-contact-3.png), [all earlier coral stages](assets/previews/chrome-life-contact-3.png), [rock gallery](assets/previews/chrome-art11-rocks.png), [coral gallery](assets/previews/chrome-art11-corals.png), [mounted coral study](assets/previews/chrome-coral-attachment-study.png), [store](assets/previews/chrome-store-desktop.png). Existing contact images were inspected during this audit; their creation is from the corresponding earlier milestone unless located under `tests/audit-evidence/`.

## E. Gameplay Issues

| System | Actual behavior and limitation |
|---|---|
| Store/destinations | Three-tab modal and explicit persisted destination choice work. R32 reproduces the duplicate quantity handler exception. Core's purchase path checks fresh compatibility at commit and preserves destination/stock/funds on rejection. |
| Transfers | Core accepts a fish transfer into oxygen=1 mg/L, a second clownfish species territory, and a coral transfer into oxygen=1/ammonia=10 water (R36–R38). These are Core-action reproductions of the transfer path, not successful unsafe purchases. SPS transfer defaults also fail despite a valid available rack (R11). |
| Placement/save validation | Save's y=.3–.92 restriction disagrees with Habitat's legal scene positions. R05 previews a valid 0.25-inch sandbed at y=.936458 but rejects purchase; R06 rejects an upper mounted rack y=.25. No invalid draft replaced the original state in those rejection cases. |
| Growth/supports | `buySand` checks attachment but skips full grown-colony placement bounds/overlap; `ecosystems` grows size without full geometry checks. Side rack horizontal movement does not preserve its side-glass location. |
| Relocation migration | Legacy unsupported colonies remain owned and are hidden with `relocationRequired`. They still age/grow/consume minerals and count toward healthy-reef quest progress (R23). The holding/relocation biology needs an explicit consistent rule. |
| New aquarium construction | New marine tanks already have five rocks, 2.4-inch sand, four equipment items and full water parameters/visuals. Fish and corals start absent. `prepared=false` does not implement the mandated empty dry tank (R12). |
| Chemistry/decomposition | Simplified central water chemistry, bacterial processing and water changes work. Fish corpses pollute constantly until removed; their mass/decay stage/buoyancy are not modeled. All corpses rise. Dead coral adds no organic waste. No substrate/algae/dissolution process exists (R17/R18/R28). |
| Biology/genetics | Individual fish fields, hunger/health/stress/growth/lineage and continuous inherited genes work. Full nutrition, species oxygen/physical-habitat rules and categorical designer genetics do not. Snowflake parents produce base-species offspring without a phenotype model (R19). |
| Metadata | 19 real older fish lack scientific names; all five coral definitions are broad groups. New care is explicitly conservative game calibration, five profiles are held, real-world lifespan data is unverified (R31). |
| Economy | Atomic funds/stock, bounded resale, demand, eight daily sales and 1,200 AC buyer budget work. No infinite buy/sell loop was reproduced. Rarity/variety do not affect resale as specified; asset totals omit rock/sand/racks/decorations; transaction cooldowns and expanded 30/90/365-day economy scenarios are absent. |
| Saves | Representative migration, corrupt input, duplicate IDs and round trips work. Private player saves were not inspected. Validation catches malformed state but is inconsistent with legal coral placement. Browser failure paths offer export/recovery; extended quota/long-run durability is not guaranteed. |

## F. Recommended Fix Order

This register covers every significant defect and missing feature group found. Priorities indicate a recommended order, not authorization to implement. **No P0 defect was confirmed** in the executed fixtures. If a real save-loss/crash/duplication report appears, it takes precedence.

| Order / ID | Priority | Issue and concrete scope | Evidence / acceptance target |
|---|---|---|---|
| 1 · I01 | P1 | Obsolete delegated `purchase-count` handler throws in the new modal. | R32; `ui.js::updateCompatibility` and document input handler. Actual quantity edit must update compatibility with zero exceptions, without double charges. |
| 2 · I02 | P1 | Habitat placement and save y ranges disagree. | R05/R06; `habitat.js::placement`, `save.js::validate`. Shallow sandbase and upper-rack preview/commit/save/reload must agree; invalid geometry must still roll back. |
| 3 · I21 | P1 | SPS transfer UI has no destination surface/position choice. | R11; `ui.js::moveFloraDialog`, `core.js::moveFlora`. Select a target mount before commit; retain identity/health and rollback on cancel. |
| 4 · I08 | P1 | Transfer paths bypass safe water and clownfish territory checks. | R36/R37/R38; `core.js::moveFish/moveFlora` vs `store-rules.js::report`. Use consistent destination admission for moves, with protected freshwater regressions. |
| 5 · I04 | P1 | A left/right rack can be moved horizontally away from its glass while staying marked mounted. | R10; `core.js::moveRack`. Enforce glass-local coordinates. Reproduction is Core/review-scene scope; the current store sells back-glass racks. |
| 6 · I07 | P1 | Growth and sand edits omit full colony geometry revalidation. | R09/R30; `simulation.js::ecosystems`, `core.js::buySand`. Define growth constraints; preserve/reject support edits using actual size, bounds and neighbor clearance. |
| 7 · I03 | P1 | Hidden relocation-required corals contribute active reef growth/minerals/rewards. | R22/R23; `simulation.js::ecosystems`, `core.js::progress`. Define modeled holding/relocation biology and truthful quest eligibility while preserving ownership. |
| 8 · I06 | P1 | Fixed center bounds allow full fish silhouettes to clip the glass. | R14; `simulation.js::motion`, `render.js::draw`. Include actual raster/body bounds and both facings in boundary behavior. |
| 9 · I05 | P1 | Fish ignore solid rock; physical dimensions/swim corridors/territories are absent. | R13; `motion` never calls Habitat geometry. Introduce shared physical geometry/admission/avoidance in a separately approved milestone. |
| 10 · I09 | P1 | Mandatory empty dry setup is absent. | R12; MDP 4.3/5.1/5.2 vs `core.js::tank`/Habitat.initialize. Design a saved dry/fill/equipment/setup progression and legacy migration before implementation. |
| 11 · I11 | P2 | Living bleaching is unreachable and cannot recover as its own state. | R16; `asset-bank.js::coralState`, `floraConditions/ecosystems`. Keep bleaching, tissue loss and death distinct. |
| 12 · I12 | P2 | Corpse buoyancy, sinking, finite tissue mass, staged decay, dead-coral waste, conditional skeleton erosion and permanent death history are incomplete. | R17/R18; MDP 8.6/9.4–9.8. Use central chemistry, bounded remaining mass and explicit saved stages. |
| 13 · I10 | P2 | Substrate quantities/units/displacement/maturation/algae/cleaning/deep-bed risk are missing; UI step differs from 0.25 inches. | R28/R29; MDP 7.4–7.9. Physical floor area/mass/effective volume are dependencies for later biological substrate work. No freshwater biology expansion is authorized. |
| 14 · I14 | P2 | Scientific/coral identities, lifespans and species-specific care/maturity/social/oxygen profiles are incomplete. | R31; metadata and held entries. Verify sources, separate game calibrations and keep uncertainty explicit; do not silently alter protected freshwater data. |
| 15 · I15 | P2 | Most non-clownfish fins are static; perspective turn and feeding frames are missing. | R15; `LifeStages.forFish`/renderer selection. Preserve full stage/death art while adding correctly anchored live cycles when approved. |
| 16 · I23 | P2 | Five art-only marine studies lack early/dead chains. | E06/static metadata. Supply complete stage chains before treating these subjects as completed livestock; do not add gameplay definitions automatically. |
| 17 · I13 | P2 | Designer phenotype purchase/save support does not implement breeding pattern genetics. | R19/R21; `makeBrood`/fish constructor. Decide a documented biological phenotype/genotype model rather than pretending exact breeder segregation is known. |
| 18 · I19 | P2 | No live/coral foods, persistent nutrition, food freshness/fat or complete age-related fertility/activity curves. | `data.js::foods`, `fishHealth/breedingReady`; MDP 9/14/15. Expand only under a separately approved biology milestone. |
| 19 · I16 | P2 | Value omits rarity/variety and owned habitat assets; per-sale cooldowns and full current economy scenarios are missing. | `core.js::value/assets/sell`, BALANCE_REPORT scope. Run current-roster 30/90/365-day affordability/breeding/market scenarios before calling economy complete. |
| 20 · I20 | P2 | Duplicate legacy shop/admission UI, stale historical stage test totals and inconsistent active/historical documentation. | `ui.js::storePage/updateCompatibility`, `life_stage_qa.py:71`, MDP 3.8, UI_SPECIFICATION. Update explicit historical scope and data-derived assertions after approval; keep consolidated MDP intact. |
| 21 · I22 | P2 | Graphics presets, spatial interaction optimization and long-run memory/frame-pacing evidence are absent. | E19; MDP 25.3. Add real presets retaining sprite quality; measure displayed FPS, GC and multi-hour behavior at representative capacities. |
| 22 · I17 | P2 | VIP lacks required illustrated fish/coral/season/decoration/background tier previews. | `ui.js::vipPage`, screenshot. Bundle real local art; retain preview-only, disabled entitlements and no payments. |
| 23 · I18 | P2 | Species/variety anatomy, stage biology and final visual approval remain provisional. | E07; metadata `approved:false`. User review and focused reference comparisons are needed; technical pixel tests do not approve anatomy. |
| 24 · I24 | P3 | Event-specific chains/art, prestige, comprehensive inventory, tooltips, UI scaling/reduced motion and scenery-density polish are incomplete. | `settingsPage/vipPage/quest/renderer` and MDP 20/22/26. Address after correctness/biology priorities; preserve original palette and offline operation. |

## G. Verification Evidence

Evidence labels distinguish **runtime execution**, **static/code inspection**, and **manual visual inspection**. Every PASS row in the full matrix cites one or more evidence entries below. A code-inspection PASS means the exact implementation was inspected; it is not falsely represented as a runtime or hardware certification. Scope qualifications in each row control the claim.

### Executed checks and limitations

| Run | Chrome | Edge | Scope / artifact |
|---|---:|---:|---|
| System/regression suite | 68 passed, 0 failed | 68 passed, 0 failed | [Chrome](tests/chrome-results.json), [Edge](tests/edge-results.json); chemistry, health, funds/stock, IDs, save/biology and finite economy fixtures. |
| Current store/UI suite | 88 passed, 0 failed | 88 passed, 0 failed | [Chrome](tests/chrome-store-results.json), [Edge](tests/edge-store-results.json); tabs, destinations, keyboard/dialogs, purchase rejection, placement, lights, persistence and protected freshwater checks. Default quantity was not evidence for arbitrary quantity editing. |
| Clownfish collection suite | 7,583 passed, 0 failed | 7,583 passed, 0 failed | [Chrome](tests/chrome-clownfish-results.json), [Edge](tests/edge-clownfish-results.json); 1,792 stage/size/direction cases each. |
| Preserved art/sprite gallery suite | 221 passed, 0 failed | 221 passed, 0 failed | [Chrome](tests/chrome-art11-results.json), [Edge](tests/edge-art11-results.json); 6,480 directional rendering cases each, coral state/rock banks and gallery behavior. |
| Earlier 27-atlas pixel checks, independently executed in audit runner | 113 passed, 0 failed | 113 passed, 0 failed | `lifeAssetChecks` in the two current audit JSON files; 2,160 rendering cases each. This is not a claim that the complete historical integration harness passes. |
| Full-project boundary/absence observations | 38 probes; 21 unmet predicates | Same 38 / same 21 | [Chrome audit](tests/audit-evidence/chrome-project-audit.json), [Edge audit](tests/audit-evidence/edge-project-audit.json). Unmet predicates include missing features as well as defects. Runner exit 0 means observations completed, not all features passed. R04 is a pointer; actual old-atlas verification is the independently stored 113-result matrix. |
| Assigned Ocellaris eye diagnostic | Covered by current art/collection checks | Separate diagnostic executed | [Edge eye samples](tests/edge-eye-after.json); 48 frame/size/facing samples retain dark eye pixels. |
| Full historical `--life-stages` integration harness | Aborted on stale 22-fish assertion | Not rerun as a full harness in this audit | [life_stage_qa.py:71](tests/life_stage_qa.py#L71) expects 131 stage selections/66 deaths. Current valid totals are 311/156 (R03). Existing historical JSON must not be described as a new successful full-harness run. |
| Static resource/archive/source integrity | 96 atlas records valid; no missing literal resources; 42 baseline files unchanged | Same files | [Static integrity](tests/audit-evidence/static-integrity.json). |

Commands executed through isolated headless profiles with network disabled: `python tests/browser_qa.py chrome`, `python tests/browser_qa.py edge`, each browser with `--clownfish`, `--audit` and `--art-review`; additionally Chrome `--life-stages` (stale assertion failure), Edge `--sprite-audit`, and `python tests/project_audit_static.py`. A mistaken `--browser edge` invocation failed argument parsing before launching a browser and was rerun using the documented positional syntax. This command mistake has no project-feature classification.

| Measured synthetic workload | Chrome | Edge |
|---|---:|---:|
| Mean render-call cost | 4.52 ms | 4.32 ms |
| p95 render-call cost | 4.10 ms | 4.40 ms |
| Maximum sampled render-call cost | 37.80 ms | 35.50 ms |
| 3,000 fish / 20 simulation steps | 114.30 ms | 116.90 ms |
| Short-run JS heap used snapshot | 6.04 MiB | 6.11 MiB |

These are short, synthetic headless render-call/tick timings, not displayed FPS or real livestock-care recommendations. Render workload: 250 fish, 120 draws. Tick workload: 12 tanks / 3,000 fish, 20 five-minute steps. No long wall-clock memory/GC soak, low-end device study, Firefox run, extended touch/screen-reader review, or actual private-save audit was performed. The short heap snapshots do not establish memory stability.

### Evidence index

<a id="e01"></a>

**E01 — Offline boot/new game (Runtime + code).** [index.html](index.html), [main.js:3](js/main.js#L3), [Chrome audit startup](tests/audit-evidence/chrome-project-audit.json), [Edge](tests/audit-evidence/edge-project-audit.json). Protocol file:, three stylesheets, zero startup exceptions and zero game HTTP(S) requests. Network was disabled. [New installation view](tests/audit-evidence/chrome-new-installation.png).

<a id="e02"></a>

**E02 — Core/system rules (Runtime + code).** [68-check source](tests/suite.js), [Chrome system results](tests/chrome-results.json), [Edge](tests/edge-results.json); [core.js](js/core.js) constructor/compatibility/actions/act, [simulation.js](js/simulation.js), [save.js](js/save.js). Named checks in result files cover each exercised behavior; no claim of absent-feature completion.

<a id="e03"></a>

**E03 — Current shared store (Runtime).** [store_qa.py](tests/store_qa.py), [Chrome 88 results](tests/chrome-store-results.json), [Edge](tests/edge-store-results.json). Exact tabs/category labels, native modal, fixed header/internal scroll, repeated opening, Escape/X, 1440/1024/760/390 widths, saved selection, destination/stock/funds, stale compatibility and duplicates are exercised. [store.js](js/store.js) products/render/details/chooseDestination/submit/open/close.

<a id="e04"></a>

**E04 — Current collection and stage maps (Runtime + metadata).** [clownfish checks](tests/clownfish_checks.js), [Chrome 7583 results](tests/chrome-clownfish-results.json), [Edge](tests/edge-clownfish-results.json); audit R01/R02/R03/R20/R21/R24/R25. Current R02 checks 616 fish/designer stage/state presentations; coral coverage is additionally in E06. [clownfish-art.js](js/clownfish-art.js), [clownfish-art-bank.js](js/clownfish-art-bank.js), [life-stages.js](js/life-stages.js).

<a id="e05"></a>

**E05 — Eyes, flipping, immutable rendering (Runtime + code).** [sprite-kit.js](js/sprite-kit.js) raster/draw, [sprite_checks.js](tests/sprite_checks.js), [clownfish checks](tests/clownfish_checks.js), [art results](tests/chrome-art11-results.json), [Edge eye diagnostic](tests/edge-eye-after.json). Applicable eyes are sampled with the complete sprite at final raster size; bounded raster cache, left/right pixel coordinates and save/restore are checked.

<a id="e06"></a>

**E06 — Earlier coral/rock/stage banks (Runtime + static).** [asset-bank.js](js/asset-bank.js) frame/coral/drawCoral and manifest, [life_stage_checks.js](tests/life_stage_checks.js), audit `lifeAssetChecks` 113/2160 in each [audit JSON](tests/audit-evidence/chrome-project-audit.json); [221 art results](tests/chrome-art11-results.json), [Edge](tests/edge-art11-results.json), [static integrity](tests/audit-evidence/static-integrity.json). Five coral × five visual states, rigid vs soft motion and 12 rock variants inspected/tested.

<a id="e07"></a>

**E07 — Livestock and approved reference (Manual visual inspection).** Inspected [approved reference](assets/reference/approved_clownfish_hybrid.png); all eight [current fish contact pages](tests/audit-evidence/chrome-fish-contact-1.png) (1–8 in the same folder); all four designer contacts and three old life-stage contacts in assets/previews; five art-only adult atlases; coral/rock gallery screenshots and the mounting study. The [offline galleries](clownfish-review.html) expose all mappings and provisional review status. These observations are not automatic user approval.

<a id="e08"></a>

**E08 — Simulation feature scope (Code inspection + runtime fixtures).** [simulation.js](js/simulation.js) water/food/fishHealth/floraConditions/ecosystems/breedingReady/makeBrood/eggs/daily/step/motion/offline; [core.js](js/core.js) fields/actions. The entire module was inspected. Existing positive behavior is exercised by E02; missing-state claims come from absence of fields/branches plus relevant R12/R15–R19/R23/R28/R29 observations.

<a id="e09"></a>

**E09 — Coral placement, attachment and inspector (Runtime + code).** [habitat.js](js/habitat.js) definitions/solid/candidates/placement/validAttachment/migrate/sync; [core.js:69](js/core.js#L69) support/depth actions and buyFlora/moveFlora/reposition; [ui.js](js/ui.js) inspectFlora/beginCoral/placement handlers; [save.js](js/save.js) flora constraints. E02/E03/E04 positive mounting cases and R05–R11/R22/R23/R30 negative/boundary observations. [Coral Care view](tests/edge-coral-info.png).

<a id="e10"></a>

**E10 — Substrate and dry setup scope (Code inspection + validated state).** [habitat.js:11](js/habitat.js#L11) sandProducts/initialize/bed, [core.js:9](js/core.js#L9) tank and buySand, [simulation.js](js/simulation.js) step/water/ecosystems, [store.js:33](js/store.js#L33) sand product and depth form. R12/R28/R29/R30 capture initial scenery, static substrate, missing mass/effectiveVolume and rejected removal of an occupied support.

<a id="e11"></a>

**E11 — Fish identity, health and breeding (Runtime + code).** [core.js:31](js/core.js#L31) fish/value/kill/moveFish, [simulation.js:52](js/simulation.js#L52) fishHealth/breedingReady/makeBrood/eggs/motion, [data.js](js/data.js) species; E02 named health, hunger, aging, predation, cooldown, lineage/brood/viability and no-duplicate-ID results. Audit R19/R20/R21/R36/R37 records current limits.

<a id="e12"></a>

**E12 — Food and inventory (Runtime + code).** [data.js](js/data.js) foods/supplies (seven foods), [core.js:116](js/core.js#L116) feed, [simulation.js](js/simulation.js) food and automatic feeder branch, [ui.js](js/ui.js) foodPage. E02 wrong diet, uneaten-waste, consumption, starvation and once-per-day inventory assertions.

<a id="e13"></a>

**E13 — Economy/progression/capacity (Runtime + code).** [core.js:58](js/core.js#L58) value/assets/progress/pay/earn/sell/claim, [data.js](js/data.js) sizes/quests, [simulation.js:129](js/simulation.js#L129) daily/achievements, [BALANCE_REPORT](BALANCE_REPORT.md) and current system result `balances`. Existing 19 quests, nine size products, budgets/demand, daily sale limits and finite scenario tests are evidence; expanded scenario coverage is explicitly incomplete.

<a id="e14"></a>

**E14 — Lighting/time/temperature (Runtime + code).** [simulation.js](js/simulation.js) light/lightPower/water, [render.js](js/render.js) scene illumination, [core.js](js/core.js) setLighting/controls, [main.js](js/main.js) fixed ticks and speed, E02/E03 manual night-on/day-off/auto/durability/temperature checks and [light on](tests/chrome-light-on.png)/[off](tests/chrome-light-off.png). Biology and visuals share installed lamp output.

<a id="e15"></a>

**E15 — Equipment (Runtime + code).** [data.js](js/data.js) equipment, [core.js:8](js/core.js#L8) equipment constructor plus buyEquipment/service/toggleEquipment/moveEquipment, [simulation.js:16](js/simulation.js#L16) wear/failure/effects, [ui.js](js/ui.js) equipmentPage. E02 heater failure/service/auto feeder/dosing/containment and E03 equipment destination/cost/state checks.

<a id="e16"></a>

**E16 — UI, VIP and events (Runtime + code + visuals).** [theme.css](css/theme.css), [main.css](css/main.css), [store.css](css/store.css), [ui.js](js/ui.js) pages/bind/inspectors/settingsPage/vipPage, [store.js](js/store.js). E03 responsive/dialog/UI execution and R32–R35 real input/thumb/focus/backdrop observations; [current catalog](tests/audit-evidence/chrome-current-catalog.png), [VIP screenshot](tests/audit-evidence/chrome-vip-preview.png), [store narrow view](assets/previews/chrome-store-mobile.png). VIP inspection finds no payment/card/checkout path; Save.validate rejects enabled entitlements. E02 validates offline season change and owned lantern persistence.

<a id="e17"></a>

**E17 — Persistence (Runtime + code).** [save.js](js/save.js) validate/migrate/parse/load/save/exportSave/recover, [main.js](js/main.js) autosave/hidden/unload save, [ui.js](js/ui.js) import/export/recovery handlers; E02/E03 and R21/R22/R24/R26/R27. Export/import controls are present, current game-state round trips validated; storage-error catch/recovery was also inspected. No private player saves were used.

<a id="e18"></a>

**E18 — Catalog, protected scope and resources (Static inspection + source verification).** [static audit](tests/project_audit_static.py), [integrity results](tests/audit-evidence/static-integrity.json), [audit baseline](tests/audit-code-baseline.json), [protected baseline](tests/freshwater-protection-baseline.json), [collection metadata](assets/livestock/fish/clownfish/collection.json), [CURRENT_LIVESTOCK_CATALOG](CURRENT_LIVESTOCK_CATALOG.md). 145 protected entries match directly, and simulation matches after restoring only the previously authorized marine pairing block. 42 audited source files unchanged. WoRMS/ORA checks are described in C with their limits.

<a id="e19"></a>

**E19 — Performance (Measured runtime + code).** Two audit JSON `performance` and `performanceMetrics` records; [main.js:9](js/main.js#L9), [render.js](js/render.js) selected-tank draw/cache/particle limits, [sprite-kit.js](js/sprite-kit.js) bounded raster cache, [life-stages.js](js/life-stages.js)/[asset-bank.js](js/asset-bank.js) 256-entry caches. No displayed-FPS or long soak result is inferred from render costs.

<a id="e20"></a>

**E20 — Continuity and MDP rules (Document inspection).** [GAME_DESIGN](GAME_DESIGN.md), [ART_DIRECTION](ART_DIRECTION.md), [UI_SPECIFICATION](UI_SPECIFICATION.md), [catalog](CURRENT_LIVESTOCK_CATALOG.md), [DEVELOPMENT_STATUS](DEVELOPMENT_STATUS.md), [BALANCE_REPORT](BALANCE_REPORT.md), [README](README.md), [31-section MDP](MASTER_DEVELOPMENT_PROMPT.md). Actual major headings and latest scope/reference/life-stage/eyes/store destination/coral mounting/25-5-5 rules checked. Historical wording conflicts and unverified full-version preservation are recorded, not silently repaired.

### MDP comparison: all 31 major sections

This trace compares requirement groups against actual implementation. It supplements the original 668-row checklist; it is not counted a second time in completion metrics. Full preservation of every earlier pasted version was not established, and the consolidated MDP was not rewritten.

| MDP section | Assessment | Actual implementation comparison | Checklist sections |
|---|---|---|---|
| [1. ROLE, RESPONSIBILITIES & DEVELOPMENT MISSION](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Playable offline simulator concept exists; full biological/management scope remains unfinished. | 1, 14–23 |
| [2. CORE GAME PHILOSOPHY & TECHNICAL REQUIREMENTS](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Offline/classic-script foundation and saltwater scope work; compressed modules/duplicate UI remain. | 1, 8, 36 |
| [3. OFFICIAL ART DIRECTION — LOCKED](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Local reference and complete mapped stage art; provisional anatomy/density and incomplete corpse/VIP art. | 2–7, 9, 17, 30 |
| [4. WORLD STRUCTURE, AQUARIUM TYPES & SIZES](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Nine sizes/multiple ownership; no dry tanks, dimensions or displacement. | 14, 21 |
| [5. GAMEPLAY LOOP & NEW TANK SETUP](MASTER_DEVELOPMENT_PROMPT.md) | FAIL | New tanks include scenery/equipment/water rather than the required dry construction loop. | 14 |
| [6. PLAYER PROGRESSION, COLLECTIONS & ACHIEVEMENTS](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | XP, discovery, quests/showcase exist; dedicated prestige/business reputation incomplete. | 27, 29 |
| [7. SALTWATER ROCKS, SAND & SUBSTRATE BIOLOGY](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Rock/sand visual ownership and editing work; no mass, substrate biology or maintenance. | 11–13 |
| [8. CORAL ECOSYSTEM, HEALTH & DEATH](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Coral inspector, growth/stress/supports work; bleach/decomposition/taxon and transfer gaps. | 9, 10, 17, 32 |
| [9. INDIVIDUAL FISH SIMULATION, AGING & DEATH](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Persistent fish/health/aging/death exist; nutrition, respiratory profiles and staged decay incomplete. | 16, 17 |
| [10. FISH AI, TEMPERAMENT & COMPATIBILITY](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | School/seek/rest/hide/encounter states work; no rock collision, dimensions or complete territories/courtship. | 6, 18 |
| [11. EQUIPMENT, FILTRATION & MAINTENANCE](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Core equipment effects/durability/service work; sensors/test history and probability/service interval profiles incomplete. | 23 |
| [12. WATER CHEMISTRY & ECOSYSTEM MODEL](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Central simplified water/nitrogen/mixing work; dead coral/substrate/live-rock nutrient processes absent. | 15, 17 |
| [13. DAY/NIGHT, TEMPERATURE & LIGHTING](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Saved Auto/On/Off visually brighten tank; no algae/heat/spectrum model or full dawn/dusk behavior. | 22 |
| [14. FOOD, DIET & FEEDING](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Seven foods, visible consumption and auto-feed; no live/coral foods or complete persistent nutrition/freshness. | 19 |
| [15. BREEDING, GENETICS & EGGS](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Broods, viability/lineage/continuous inheritance work; designer pattern genetics/courtship incomplete. | 20 |
| [16. FISH RARITY, MARKET VALUE & AQUARIUM ASSET VALUE](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Bounded condition/gene/demand value and load; no required rarity/variety or full habitat asset valuation. | 21, 28 |
| [17. ECONOMY, INCOME & MARKET BALANCING](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Bounded budgets/resale/electricity/rewards; no full current 30/90/365-day balance matrix/cooldowns. | 28 |
| [18. STORES, INVENTORY & TRANSACTIONS](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Destination invariants and atomic shared modal work; quantity handler/details/ledger completeness incomplete. | 24–26 |
| [19. BLACK MARKET & DANGEROUS FICTIONAL CREATURES](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Level/night/containment/stock/inspection fictional foundation; no dealer reputation/full rotating roster. | 27 |
| [20. QUESTS, OBJECTIVES & UNLOCKABLES](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | 19 quests/three achievements; relocation quest bug and missing full construction/prestige coverage. | 29 |
| [21. VIP STORE — PREVIEW ONLY](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Five preview-tier names and disabled payments; required illustrated tier panels absent. | 30 |
| [22. HOLIDAYS & LIMITED-TIME CONTENT](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Six local season values and persistent lantern; dedicated event chains/art are incomplete. | 31 |
| [23. AQUARIUM CUSTOMIZATION & PLACEMENT](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Rock/sand/coral edits saved; support/mount/growth/transfer/boundary validation defects. | 10–12, 32 |
| [24. LOCAL SAVE, LOAD & OFFLINE PROGRESSION](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Versioned save/recovery/migration/offline cap work; coral schema/geometry disagreement and absent biological fields. | 33 |
| [25. GRAPHICS ENGINE, ANIMATION & PERFORMANCE](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Fixed ticks, atlases/caches/selected rendering; no presets/background cache/spatial grouping/long soak. | 34 |
| [26. UI/UX TECHNICAL SPECIFICATION](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Locked palette, dialog/responsive UI and inspectors; missing full inventory/setup/scaling/accessibility review. | 24, 32 |
| [27. QUALITY ASSURANCE & AUTOMATED TESTING](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Current regressions pass but boundary audit finds gaps; historical life-stage harness is stale. | G executed tests |
| [28. DEVELOPMENT ROADMAP & EXECUTION ORDER](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Integrated roadmap exists; its later phases and foundational dry setup are unfinished. | 14, 30, 31, 34, 36 |
| [29. PROJECT FILE STRUCTURE](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Offline namespaced modules/data/assets/tests organized; duplicate compressed modules impede maintenance. | 1, 36 |
| [30. CONTINUITY, DOCUMENTATION & LOCKED RULES](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | All required docs/31 headings/latest named rules present; conflicting historical wording persists. | 36 |
| [31. FINAL EXECUTION INSTRUCTIONS FOR CODEX](MASTER_DEVELOPMENT_PROMPT.md) | PARTIAL | Playable vertical slice delivered; full target completion cannot be declared. Audit stop overrides development instructions. | A–H |

### Complete original checklist: 668 classified checks

The machine-readable decisions are in [checklist-classifications.json](tests/audit-evidence/checklist-classifications.json). Original wording is preserved below; IDs `section.item` identify the exact item in the user's section order. FAIL denotes implemented contradictory behavior; MISSING denotes no corresponding implementation. NOT APPLICABLE is reserved for genuinely conditional/out-of-scope checks, not a substitute for missing mandatory features.

#### 1. PROJECT FOUNDATION

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 01.01 | Game launches through `index.html`. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E01](#e01); [E02](#e02); [E03](#e03); [E18](#e18) |
| 01.02 | Game works without internet. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E01](#e01); [E02](#e02); [E03](#e03); [E18](#e18) |
| 01.03 | No external CDN dependencies. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E01](#e01); [E02](#e02); [E03](#e03); [E18](#e18) |
| 01.04 | No mandatory backend. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E01](#e01); [E02](#e02); [E03](#e03); [E18](#e18) |
| 01.05 | No account required. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E01](#e01); [E02](#e02); [E03](#e03); [E18](#e18) |
| 01.06 | No payment processor. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E01](#e01); [E02](#e02); [E03](#e03); [E18](#e18) |
| 01.07 | No runtime external asset requests. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E01](#e01); [E02](#e02); [E03](#e03); [E18](#e18) |
| 01.08 | JavaScript loads correctly under `file://`. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E01](#e01); [E02](#e02); [E03](#e03); [E18](#e18) |
| 01.09 | CSS loads correctly. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E01](#e01); [E02](#e02); [E03](#e03); [E18](#e18) |
| 01.10 | All local images load. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E01](#e01); [E02](#e02); [E03](#e03); [E18](#e18) |
| 01.11 | No missing assets. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E01](#e01); [E02](#e02); [E03](#e03); [E18](#e18) |
| 01.12 | No fatal console errors. | **PARTIAL** | Startup is clean; changing a store quantity throws an uncaught exception (R32). | [E01](#e01); [E02](#e02); [E03](#e03); [E18](#e18) |
| 01.13 | Game starts correctly from a new installation. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E01](#e01); [E02](#e02); [E03](#e03); [E18](#e18) |
| 01.14 | Existing saves load without crashing. | **PASS** | Representative schema-1/schema-2 saves and corruption paths were exercised; no private player save was opened. | [E01](#e01); [E02](#e02); [E03](#e03); [E18](#e18) |
| 01.15 | Codebase is organized and maintainable. | **PARTIAL** | Namespaced modules exist, but core/UI/simulation are heavily compressed and duplicate shop code remains (I20). | [E01](#e01); [E02](#e02); [E03](#e03); [E18](#e18) |
| 01.16 | No unnecessary duplicate systems. | **FAIL** | Legacy full-page shop and its delegated quantity handler coexist with the modal shop; the handler causes R32 (I01). | [E01](#e01); [E02](#e02); [E03](#e03); [E18](#e18) |
| 01.17 | All game data has valid identifiers. | **PASS** | Runtime species identifiers, base links, unique entity IDs and asset bank records validated. | [E01](#e01); [E02](#e02); [E03](#e03); [E18](#e18) |

#### 2. OFFICIAL ART STYLE

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 02.01 | Approved reference exists in the project. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E16](#e16) |
| 02.02 | All current saltwater fish artwork follows the reference. | **PARTIAL** | Older fish have finer, noisier shading than the newer clownfish. All new sheets are provisional, not approved (I18). | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E16](#e16) |
| 02.03 | Coral artwork follows the reference. | **PARTIAL** | Detailed coral art exists, but style acceptance and species-level anatomy remain provisional. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E16](#e16) |
| 02.04 | Bottom-feeder artwork follows the reference. | **PARTIAL** | Four benthic stage sets exist; their fine shading differs from the newer clownfish collection. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E16](#e16) |
| 02.05 | Rock artwork follows the reference. | **PARTIAL** | All three rock collections have detailed art; visual acceptance is still pending. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E16](#e16) |
| 02.06 | Sand artwork follows the reference. | **PARTIAL** | Substrate uses procedural colored grains rather than three polished bundled substrate texture sets (I10). | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E16](#e16) |
| 02.07 | Store thumbnails show appropriate artwork. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E16](#e16) |
| 02.08 | VIP preview artwork is visually consistent. | **MISSING** | VIP cards contain future-concept text; tier-specific illustrated previews are missing (I17). | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E16](#e16) |
| 02.09 | Sprites have crisp pixel boundaries. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E16](#e16) |
| 02.10 | Sprites are not blurry at gameplay scale. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E16](#e16) |
| 02.11 | Fish have recognizable species anatomy. | **PARTIAL** | Recognizable adult silhouettes were inspected; complete species/stage anatomical certification is not established. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E16](#e16) |
| 02.12 | Colors are vivid but appropriate to species. | **PARTIAL** | Vivid art is present; commercial varieties and species-specific biological accuracy are still provisional. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E16](#e16) |
| 02.13 | Artwork has consistent pixel density. | **PARTIAL** | Different generations use different effective texture density despite common frame dimensions. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E16](#e16) |
| 02.14 | Sprites use suitable transparent backgrounds. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E16](#e16) |
| 02.15 | Existing approved artwork is preserved. | **PASS** | Assigned adult Ocellaris source and earlier reference remain in place; audit source hashes are unchanged. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E16](#e16) |
| 02.16 | Artwork differences are documented. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E16](#e16) |
| 02.17 | No generic placeholder shapes are presented as finished artwork. | **PASS** | Actual animal art is shown; VIP concepts are explicitly labeled unfinished, not sold as completed artwork. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E16](#e16) |

#### 3. LIVESTOCK CATALOG

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 03.01 | Every species has a unique internal ID. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 03.02 | Every species has an appropriate common name. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 03.03 | Scientific names are recorded where applicable. | **PARTIAL** | Nineteen real older fish lack scientificName; all five coral entries are broad groups (R31/I14). | [E02](#e02); [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 03.04 | Saltwater/freshwater classification is correct. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 03.05 | Species data is valid. | **PARTIAL** | Identifiers and numeric game definitions work, but care profiles are game calibrations and five specialist profiles are held. | [E02](#e02); [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 03.06 | Designer morphs are distinguished from biological species. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 03.07 | No duplicate catalog records. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 03.08 | Every implemented species has a working sprite. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 03.09 | Every implemented species can be displayed correctly. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 03.10 | Catalog entries match store entries. | **PASS** | Five purchase-held catalog species stay visible as unavailable; art-only/planned entries are not store livestock. | [E02](#e02); [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 03.11 | Planned species are not marked implemented. | **PASS** | The global gallery explicitly labels planned subjects; no runtime species is inferred from a proposal. | [E02](#e02); [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 03.12 | Art-only species are identified. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 03.13 | Data-only species are identified. | **PASS** | DATA ONLY count is zero; metadata states this explicitly. | [E02](#e02); [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 03.14 | Implementation counts are accurate. | **PASS** | 52 fish entities/definitions plus five coral groups; benthic fish are counted once. | [E02](#e02); [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |

#### 4. LIFE-STAGE ARTWORK

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 04.01 | Egg/early-stage artwork exists. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 04.02 | Nonviable egg/early-stage artwork exists. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 04.03 | Baby/larval artwork exists. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 04.04 | Dead baby/larval artwork exists. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 04.05 | Juvenile artwork exists. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 04.06 | Dead juvenile artwork exists. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 04.07 | Adult artwork exists. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 04.08 | Dead adult artwork exists. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 04.09 | Stage artwork follows species biology. | **PARTIAL** | All eight mappings exist; stage biology and all newly generated anatomy have not received scientific/user approval (I18). | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 04.10 | Juveniles are visually distinct from adults. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 04.11 | Baby fish are not merely shrunken adult sprites. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 04.12 | Designer morph artwork changes at biologically appropriate stages. | **PARTIAL** | Shared base eggs/larvae and separate juvenile/adult phenotypes exist; exact pattern-development timing is provisional. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 04.13 | Artwork transitions correctly between stages. | **PASS** | Current renderer covers 311 stage selections and 156 authored dead selections without double inversion (R03). | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 04.14 | Unnecessary duplicated sprite assets are avoided. | **PASS** | Designer eggs/larvae reuse their base species. Historical sheets are retained deliberately for continuity. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 04.15 | Dead artwork remains recognizable as the correct species. | **PASS** | Manual contact review preserves recognizable silhouettes/colors in authored dead forms; this is visual inspection only. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 04.16 | Sprite asset paths remain valid after saving/loading. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |

#### 5. FISH EYES — CRITICAL PERMANENT RULE

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 05.01 | Eyes remain attached to the head. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 05.02 | Eyes do not disappear. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 05.03 | Eyes do not flicker. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 05.04 | Eyes do not float independently. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 05.05 | Eyes are visible in the appropriate side profile. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 05.06 | Eyes remain correctly positioned when facing left. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 05.07 | Eyes remain correctly positioned when facing right. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 05.08 | Eye positioning survives sprite scaling. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 05.09 | Eye positioning survives animation changes. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 05.10 | Eye positioning survives turning. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 05.11 | Eye layers render in the correct order. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 05.12 | Eye pixels are not accidentally cropped. | **PARTIAL** | Raster eye components survive cropping/scaling tests, but the complete fish can clip against tank edges (R14/I06). | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 05.13 | Canvas transformations reset correctly. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |
| 05.14 | Eye correctness has been reviewed across all implemented fish. | **PASS** | All 52 gameplay fish inspected in eight current contact pages, plus all 56 clownfish sheets and earlier stage contacts; approval remains separate. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07) |

#### 6. SWIMMING AND ANIMATION

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 06.01 | Fish face left when swimming left. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E08](#e08) |
| 06.02 | Fish face right when swimming right. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E08](#e08) |
| 06.03 | Fish do not continuously flicker between directions. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E08](#e08) |
| 06.04 | Turning animation works. | **PARTIAL** | Stable mirrored switching exists; intermediate perspective/turn poses are absent. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E08](#e08) |
| 06.05 | Idle swimming works. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E08](#e08) |
| 06.06 | Normal swimming works. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E08](#e08) |
| 06.07 | Fast swimming works where supported. | **PARTIAL** | Seek-food movement accelerates 1.7x; dedicated fast animation poses are absent. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E08](#e08) |
| 06.08 | Feeding animation works where supported. | **PARTIAL** | Fish pursue food and enter Eat behavior; there is no authored bite/feeding cycle (I19). | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E08](#e08) |
| 06.09 | Resting animation works. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E08](#e08) |
| 06.10 | Species have distinctive swimming behavior. | **PARTIAL** | Activity, zone, schooling and night behavior vary, but movement uses one common steering model. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E08](#e08) |
| 06.11 | Fins and tails animate appropriately. | **PARTIAL** | Clownfish adults have four-frame cycles; most non-clownfish select one static stage image (R15/I15). | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E08](#e08) |
| 06.12 | Fish do not pass through solid rocks. | **MISSING** | Motion never consults Habitat.solid; a fish placed in rock remains inside it (R13/I05). | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E08](#e08) |
| 06.13 | Fish stay within aquarium boundaries. | **FAIL** | Centers clamp to fixed normalized bounds, independent of full sprite dimensions (R14). | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E08](#e08) |
| 06.14 | Sprite flipping does not mirror UI text. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E08](#e08) |
| 06.15 | Animation does not detach body parts. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E08](#e08) |
| 06.16 | No visible sprite clipping. | **FAIL** | Full adult silhouette can extend beyond the glass at legal center positions (R14/I06). | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E08](#e08) |
| 06.17 | Fish movement remains smooth at different frame rates. | **PARTIAL** | Interpolation and facing hysteresis are present; exhaustive visual testing across varied hardware/frame pacing is incomplete. | [E04](#e04); [E05](#e05); [E06](#e06); [E07](#e07); [E08](#e08) |

#### 7. CLOWNFISH COLLECTION

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 07.01 | Ocellaris. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.02 | True Percula. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.03 | Maroon. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.04 | Clark's. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.05 | Tomato. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.06 | Cinnamon. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.07 | Red Saddleback. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.08 | Pink Skunk. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.09 | Orange Skunk. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.10 | Skunk/Nosestripe. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.11 | Saddleback. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.12 | Sebae. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.13 | Barrier Reef. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.14 | Allard's. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.15 | Red Sea Twoband. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.16 | Orangefin. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.17 | Maldives. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.18 | Oman. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.19 | Chagos. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.20 | Mauritius. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.21 | Seychelles. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.22 | Madagascar. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.23 | Whitebonnet. | **PASS** | Whitebonnet is catalogued with hybrid uncertainty and a purchase hold; presence is verified, care completeness is not. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.24 | McCulloch's. | **PASS** | McCulloch is present with a specialist care hold. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.25 | Wide-band. | **PASS** | Wide-band is present with a specialist care hold. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.26 | Australian Red. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.27 | Three-band. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.28 | Barber's. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.29 | Pacific. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.30 | Thielle's. | **PASS** | Thielle is catalogued with hybrid uncertainty and a purchase hold. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.31 | Polynesian. | **PASS** | Polynesian is present with a specialist care hold. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.32 | Black Ocellaris. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.33 | Snowflake. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.34 | Premium Snowflake. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.35 | Black Snowflake. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.36 | Black Ice. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.37 | Wyoming White. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.38 | Snow Storm. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.39 | Black Storm. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.40 | Mocha Storm. | **PARTIAL** | Mocha Storm exists and is base-linked; commercial-label/source confidence remains provisional. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.41 | Mocha. | **PARTIAL** | Mocha Ocellaris exists and is base-linked; commercial-label/source confidence remains provisional. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.42 | Gladiator. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.43 | Mocha Gladiator. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.44 | DaVinci. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.45 | Frostbite. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.46 | Black Frostbite. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.47 | Midnight. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.48 | Domino. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.49 | Naked. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.50 | Misbar. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.51 | Longfin. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.52 | Picasso. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.53 | Premium Picasso. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.54 | Platinum. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.55 | Onyx Percula. | **PARTIAL** | Onyx Percula exists and is base-linked; commercial-label/source confidence remains provisional. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.56 | Lightning Maroon. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.57 | Designer varieties reference their correct biological species. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.58 | Varieties are not misrepresented as separate species. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.59 | Pattern artwork matches its intended variety. | **PARTIAL** | All intended pattern sheets exist, but exact breeder phenotype correspondence is not fully certified (I18). | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.60 | Species-specific anatomy is preserved. | **PARTIAL** | Basic clownfish family silhouettes are recognizable; species-specific spine/fin/anatomy review remains provisional. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.61 | Life stages render correctly. | **PASS** | All 31 species and 25 varieties have eight stage/state presentations; designer early stages share the base. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.62 | Eye and swimming rules are satisfied. | **PASS** | Technical eye/direction tests pass at tested sizes. Tank-edge clipping is recorded separately in section 6. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.63 | Care requirements are correctly inherited. | **PASS** | Variety purchases reuse biological species care and compatibility. This does not certify the underlying care science. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |
| 07.64 | Species and variety counts are accurate. | **PASS** | 31 named catalog entries and 25 phenotypes; phenotypes do not increase biological species counts. | [E04](#e04); [E05](#e05); [E07](#e07); [E18](#e18) |

#### 8. SALTWATER-ONLY DEVELOPMENT RULE

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 08.01 | No new freshwater fish were added unintentionally. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E18](#e18) |
| 08.02 | No freshwater bottom feeders were added. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E18](#e18) |
| 08.03 | No freshwater plants were added. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E18](#e18) |
| 08.04 | No freshwater breeding systems were expanded. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E18](#e18) |
| 08.05 | Existing freshwater sprites were preserved. | **PASS** | 144 protected freshwater art/source files are byte-identical to the earlier baseline. | [E02](#e02); [E03](#e03); [E18](#e18) |
| 08.06 | Existing freshwater species data was preserved. | **PASS** | js/data.js is byte-identical to the protected baseline. | [E02](#e02); [E03](#e03); [E18](#e18) |
| 08.07 | Existing freshwater biology remains unchanged. | **PASS** | Replacing only the previously delivered marine clownfish block reproduces the protected simulation file exactly. | [E02](#e02); [E03](#e03); [E18](#e18) |
| 08.08 | Shared UI changes do not damage freshwater systems. | **PASS** | Shared UI freshwater destination/navigation/purchase tests pass; no new freshwater biology was introduced. | [E02](#e02); [E03](#e03); [E18](#e18) |
| 08.09 | Saltwater and freshwater catalogs remain separated. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E18](#e18) |
| 08.10 | Freshwater store navigation does not authorize freshwater content development. | **PASS** | Navigation exposes protected existing stock and honest empty categories; the current MDP explicitly protects freshwater. | [E02](#e02); [E03](#e03); [E18](#e18) |

#### 9. CORAL CATALOG AND ARTWORK

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 09.01 | Correct species/group data. | **PARTIAL** | Five category-level care groups exist, without verified coral species identities (I14). | [E06](#e06); [E07](#e07); [E09](#e09) |
| 09.02 | Species-appropriate artwork. | **PARTIAL** | Distinct group silhouettes exist; precise taxon anatomy remains unverified. | [E06](#e06); [E07](#e07); [E09](#e09) |
| 09.03 | Healthy art. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E06](#e06); [E07](#e07); [E09](#e09) |
| 09.04 | Stressed art. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E06](#e06); [E07](#e07); [E09](#e09) |
| 09.05 | Bleached art. | **PASS** | Bleached art exists in the review bank, but gameplay never selects it (R16/I11). This row checks artwork existence. | [E06](#e06); [E07](#e07); [E09](#e09) |
| 09.06 | Tissue-loss art. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E06](#e06); [E07](#e07); [E09](#e09) |
| 09.07 | Dead-state art. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E06](#e06); [E07](#e07); [E09](#e09) |
| 09.08 | Exposed skeleton for applicable stony corals. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E06](#e06); [E07](#e07); [E09](#e09) |
| 09.09 | Soft-coral death states differ appropriately. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E06](#e06); [E07](#e07); [E09](#e09) |
| 09.10 | Coral animations are subtle and natural. | **PASS** | Two-frame soft coral motion and rigid-skeleton polyp pulses exist; frames stop on death. | [E06](#e06); [E07](#e07); [E09](#e09) |
| 09.11 | Growth stages have consistent artwork. | **PARTIAL** | Eight static colony/early-stage views exist; live colony growth mainly scales adult health-state art. | [E06](#e06); [E07](#e07); [E09](#e09) |
| 09.12 | Coral sprites do not look like generic shapes. | **PARTIAL** | Distinct detailed colonies replace generic templates; exact group anatomy is still provisional. | [E06](#e06); [E07](#e07); [E09](#e09) |
| 09.13 | All coral art matches the approved reference. | **PARTIAL** | Reviewable local art exists; user acceptance of full reference fidelity is pending. | [E06](#e06); [E07](#e07); [E09](#e09) |

#### 10. CORAL PLACEMENT — CRITICAL

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 10.01 | Placement requires a valid surface or mounting structure. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E09](#e09) |
| 10.02 | Suitable rock placement works. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E09](#e09) |
| 10.03 | Species-appropriate sandbed placement works. | **FAIL** | Shallow permitted sand depth gives a suitable preview at y=.936458, but Save.validate rejects y>.92 (R05/I02). | [E02](#e02); [E04](#e04); [E09](#e09) |
| 10.04 | Glass-mounted racks or other valid supports work. | **FAIL** | Upper mounted rack y=.25 passes geometry but is rejected by the save y>=.3 constraint (R06/I02). Side rack movement also loses glass anchoring (R10/I04). | [E02](#e02); [E04](#e04); [E09](#e09) |
| 10.05 | Open-water placement is rejected. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E09](#e09) |
| 10.06 | Coral placement inside solid rock is rejected. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E09](#e09) |
| 10.07 | Coral placement outside the aquarium is rejected. | **PASS** | New placement checks full sprite/footprint bounds. Subsequent growth is a separate gap (I07). | [E02](#e02); [E04](#e04); [E09](#e09) |
| 10.08 | Coral mounting information is saved. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E09](#e09) |
| 10.09 | Coral attachment survives reload. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E09](#e09) |
| 10.10 | Moving a rock moves attached corals correctly. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E09](#e09) |
| 10.11 | Removing a rock cannot leave floating corals. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E09](#e09) |
| 10.12 | Changing sand depth revalidates relevant coral placement. | **FAIL** | Removing a sand support is blocked, but full grown-silhouette/neighbor validation is skipped during other depth edits (R09/R30/I07). | [E02](#e02); [E04](#e04); [E09](#e09) |
| 10.13 | Placement previews show valid/conditional/invalid states. | **PARTIAL** | Suitable/Conditional/Invalid text and color previews exist, but some Suitable previews cannot commit (R05/R06). | [E02](#e02); [E04](#e04); [E09](#e09) |
| 10.14 | Lighting requirements influence placement warnings. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E09](#e09) |
| 10.15 | Water-flow requirements influence placement warnings. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E09](#e09) |
| 10.16 | Neighbor aggression/spacing is checked. | **PASS** | Initial footprint overlap and LPS warnings work; ongoing growth does not continuously revalidate geometry. | [E02](#e02); [E04](#e04); [E09](#e09) |
| 10.17 | Species-specific allowed surfaces are respected. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E09](#e09) |

#### 11. ROCKS AND ENVIRONMENT

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 11.01 | Fiji Rock artwork exists. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E06](#e06); [E07](#e07); [E09](#e09) |
| 11.02 | Caribbean Rock artwork exists. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E06](#e06); [E07](#e07); [E09](#e09) |
| 11.03 | Hawaiian Rock artwork exists. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E06](#e06); [E07](#e07); [E09](#e09) |
| 11.04 | Each category has recognizable visual differences. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E06](#e06); [E07](#e07); [E09](#e09) |
| 11.05 | Small rock variants exist. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E06](#e06); [E07](#e07); [E09](#e09) |
| 11.06 | Medium rock variants exist. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E06](#e06); [E07](#e07); [E09](#e09) |
| 11.07 | Large rock variants exist. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E06](#e06); [E07](#e07); [E09](#e09) |
| 11.08 | Cave/arch variants exist where implemented. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E06](#e06); [E07](#e07); [E09](#e09) |
| 11.09 | Rocks can be purchased. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E06](#e06); [E07](#e07); [E09](#e09) |
| 11.10 | Rocks can be placed. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E06](#e06); [E07](#e07); [E09](#e09) |
| 11.11 | Rocks can be moved. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E06](#e06); [E07](#e07); [E09](#e09) |
| 11.12 | Rocks can be removed safely. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E06](#e06); [E07](#e07); [E09](#e09) |
| 11.13 | Rock positions save/load correctly. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E06](#e06); [E07](#e07); [E09](#e09) |
| 11.14 | Rocks provide appropriate habitat geometry. | **PARTIAL** | Detailed alpha-column geometry supports coral mounting; AI and physical swim-space integration are incomplete (I05). | [E02](#e02); [E06](#e06); [E07](#e07); [E09](#e09) |
| 11.15 | Fish respect rock collision. | **MISSING** | Fish motion has no rock collision integration (R13). | [E02](#e02); [E06](#e06); [E07](#e07); [E09](#e09) |
| 11.16 | Coral attachments to rocks remain valid. | **PARTIAL** | Support IDs and move/remove validation work, but growth/depth edits can leave invalid full silhouettes (I07). | [E02](#e02); [E06](#e06); [E07](#e07); [E09](#e09) |
| 11.17 | Dry and live rock states are distinguished where supported. | **NOT APPLICABLE** | No dry/live rock-state feature is implemented; this conditional check is inapplicable, not a success. Full dry setup remains required in section 14. | [E02](#e02); [E06](#e06); [E07](#e07); [E09](#e09) |
| 11.18 | Rock artwork matches the approved visual style. | **PARTIAL** | Twelve detailed collection/size/arch variants exist; art approval is pending. | [E02](#e02); [E06](#e06); [E07](#e07); [E09](#e09) |

#### 12. SAND AND SUBSTRATE

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 12.01 | Three required sand categories exist. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E09](#e09); [E10](#e10) |
| 12.02 | Each has distinct visual artwork. | **PARTIAL** | Three grain colors alter procedural sand; standalone polished category texture art is incomplete. | [E02](#e02); [E09](#e09); [E10](#e10) |
| 12.03 | Sand can be purchased. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E09](#e09); [E10](#e10) |
| 12.04 | Sand quantity is calculated. | **MISSING** | Every installation costs 40 AC regardless of mass, floor area or depth (R29/I10). | [E02](#e02); [E09](#e09); [E10](#e10) |
| 12.05 | Sand can be added to empty tanks. | **PASS** | A tank with no livestock accepts substrate installation; this does not imply a dry tank exists. | [E02](#e02); [E09](#e09); [E10](#e10) |
| 12.06 | Sand depth supports 0–5 inches. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E09](#e09); [E10](#e10) |
| 12.07 | Depth changes in 0.25-inch increments. | **FAIL** | Store/inspector fields use step=0.1 rather than 0.25; Core accepts arbitrary finite depths. | [E02](#e02); [E09](#e09); [E10](#e10) |
| 12.08 | Inches and centimeters are displayed. | **MISSING** | Inches are displayed; centimetre conversion is absent. | [E02](#e02); [E09](#e09); [E10](#e10) |
| 12.09 | Required mass scales with aquarium floor area. | **MISSING** | No physical floor dimensions or required sand mass exists. | [E02](#e02); [E09](#e09); [E10](#e10) |
| 12.10 | Sand depth changes the tank's visual profile. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E09](#e09); [E10](#e10) |
| 12.11 | Sand reduces effective water volume appropriately. | **MISSING** | Water chemistry and capacity use nominal volume; no displacement model (R29). | [E02](#e02); [E09](#e09); [E10](#e10) |
| 12.12 | Sand changes persist after reload. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E09](#e09); [E10](#e10) |
| 12.13 | Substrate depth affects appropriate habitat checks. | **PARTIAL** | Depth moves bed/support anchors and disallows removing an occupied sand base; burrowing/maturation suitability is absent. | [E02](#e02); [E09](#e09); [E10](#e10) |
| 12.14 | Deep-bed conditions are modeled appropriately. | **MISSING** | No corresponding runtime implementation found in the cited modules. | [E02](#e02); [E09](#e09); [E10](#e10) |
| 12.15 | No arbitrary bonuses are assigned solely from geographical sand names. | **PASS** | Geographical sand names change visual grains without chemistry/stat bonuses. | [E02](#e02); [E09](#e09); [E10](#e10) |

#### 13. SUBSTRATE MATURATION AND ALGAE

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 13.01 | Sand develops biological maturation over time. | **MISSING** | No corresponding runtime implementation found in the cited modules. | [E08](#e08); [E10](#e10) |
| 13.02 | Brown diatom growth is supported. | **MISSING** | No corresponding runtime implementation found in the cited modules. | [E08](#e08); [E10](#e10) |
| 13.03 | Green algae growth is supported. | **MISSING** | No corresponding runtime implementation found in the cited modules. | [E08](#e08); [E10](#e10) |
| 13.04 | Cyanobacterial growth is distinguished from true algae. | **MISSING** | No corresponding runtime implementation found in the cited modules. | [E08](#e08); [E10](#e10) |
| 13.05 | Biofilm development is supported. | **MISSING** | No corresponding runtime implementation found in the cited modules. | [E08](#e08); [E10](#e10) |
| 13.06 | Growth responds to light. | **MISSING** | No corresponding runtime implementation found in the cited modules. | [E08](#e08); [E10](#e10) |
| 13.07 | Growth responds to relevant nutrients. | **MISSING** | No corresponding runtime implementation found in the cited modules. | [E08](#e08); [E10](#e10) |
| 13.08 | Growth responds to water flow. | **MISSING** | No corresponding runtime implementation found in the cited modules. | [E08](#e08); [E10](#e10) |
| 13.09 | Growth responds to maintenance. | **MISSING** | No corresponding runtime implementation found in the cited modules. | [E08](#e08); [E10](#e10) |
| 13.10 | Growth responds to grazing organisms where implemented. | **MISSING** | No corresponding runtime implementation found in the cited modules. | [E08](#e08); [E10](#e10) |
| 13.11 | Algae does not appear solely because a fixed timer elapsed. | **PARTIAL** | No algae growth exists at all; absence of a fixed timer is not a working environmental algae model. | [E08](#e08); [E10](#e10) |
| 13.12 | Substrate remains visually clean under suitable conditions. | **PARTIAL** | Sand stays visually static, including under unsuitable conditions; cleanliness is not condition-dependent. | [E08](#e08); [E10](#e10) |
| 13.13 | Surface cleaning functions. | **MISSING** | No corresponding runtime implementation found in the cited modules. | [E08](#e08); [E10](#e10) |
| 13.14 | Organic waste accumulation is modeled. | **PASS** | Whole-tank organic waste is modeled from food/fish/corpses; spatial substrate accumulation is absent. | [E08](#e08); [E10](#e10) |
| 13.15 | Deep sand disturbance risks are condition-dependent. | **MISSING** | No anaerobic strata, conditional disturbance risk or substrate-cleaning action (I10). | [E08](#e08); [E10](#e10) |

#### 14. NEW AQUARIUM SETUP

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 14.01 | No automatic fish. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E01](#e01); [E02](#e02); [E08](#e08); [E09](#e09); [E10](#e10) |
| 14.02 | No automatic coral. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E01](#e01); [E02](#e02); [E08](#e08); [E09](#e09); [E10](#e10) |
| 14.03 | No automatic rock. | **FAIL** | New marine tank includes five owned starter rocks (R12/I09). | [E01](#e01); [E02](#e02); [E08](#e08); [E09](#e09); [E10](#e10) |
| 14.04 | No automatic sand. | **FAIL** | Marine sand defaults to 2.4 inches (R12); freshwater scenery is also pre-drawn. | [E01](#e01); [E02](#e02); [E08](#e08); [E09](#e09); [E10](#e10) |
| 14.05 | No automatic water. | **FAIL** | New tanks have full water parameters and full water visuals; prepared=false is not a dry/fill state. | [E01](#e01); [E02](#e02); [E08](#e08); [E09](#e09); [E10](#e10) |
| 14.06 | Empty glass tank is shown. | **MISSING** | Dry bare-glass rendering and water level/filling state are missing. | [E01](#e01); [E02](#e02); [E08](#e08); [E09](#e09); [E10](#e10) |
| 14.07 | Player selects substrate. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E01](#e01); [E02](#e02); [E08](#e08); [E09](#e09); [E10](#e10) |
| 14.08 | Player adds substrate. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E01](#e01); [E02](#e02); [E08](#e08); [E09](#e09); [E10](#e10) |
| 14.09 | Player prepares appropriate water. | **PARTIAL** | Prepare toggles readiness; separate water mixing/quantity/filling steps are absent. | [E01](#e01); [E02](#e02); [E08](#e08); [E09](#e09); [E10](#e10) |
| 14.10 | Player fills aquarium. | **MISSING** | No corresponding runtime implementation found in the cited modules. | [E01](#e01); [E02](#e02); [E08](#e08); [E09](#e09); [E10](#e10) |
| 14.11 | Equipment can be installed. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E01](#e01); [E02](#e02); [E08](#e08); [E09](#e09); [E10](#e10) |
| 14.12 | Rock placement is supported during appropriate setup stages. | **PARTIAL** | Marine rock editing works, but no staged dry/live-rock setup progression exists. | [E01](#e01); [E02](#e02); [E08](#e08); [E09](#e09); [E10](#e10) |
| 14.13 | Nitrogen cycling occurs. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E01](#e01); [E02](#e02); [E08](#e08); [E09](#e09); [E10](#e10) |
| 14.14 | Readiness is based on actual conditions. | **PARTIAL** | Cycling/toxins/oxygen admission checks work; physical dimensions and substrate maturity do not. | [E01](#e01); [E02](#e02); [E08](#e08); [E09](#e09); [E10](#e10) |
| 14.15 | Fish cannot be introduced when critical conditions are unsafe. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E01](#e01); [E02](#e02); [E08](#e08); [E09](#e09); [E10](#e10) |
| 14.16 | Coral-specific habitat maturity is checked. | **PARTIAL** | Cycle/reef/chemistry/light/flow checks exist; coral-specific long-term habitat age is absent. | [E01](#e01); [E02](#e02); [E08](#e08); [E09](#e09); [E10](#e10) |
| 14.17 | Setup progress remains saved. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E01](#e01); [E02](#e02); [E08](#e08); [E09](#e09); [E10](#e10) |
| 14.18 | Setup guidance explains the next action. | **PARTIAL** | Prepare/cycle/stock hints exist; complete build/fill/substrate guidance does not. | [E01](#e01); [E02](#e02); [E08](#e08); [E09](#e09); [E10](#e10) |

#### 15. WATER CHEMISTRY

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 15.01 | Temperature. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E09](#e09) |
| 15.02 | Salinity. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E09](#e09) |
| 15.03 | pH. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E09](#e09) |
| 15.04 | Ammonia. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E09](#e09) |
| 15.05 | Nitrite. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E09](#e09) |
| 15.06 | Nitrate. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E09](#e09) |
| 15.07 | Dissolved oxygen. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E09](#e09) |
| 15.08 | Alkalinity. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E09](#e09) |
| 15.09 | Calcium. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E09](#e09) |
| 15.10 | Magnesium. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E09](#e09) |
| 15.11 | Phosphate. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E09](#e09) |
| 15.12 | Organic waste. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E09](#e09) |
| 15.13 | Water clarity. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E09](#e09) |
| 15.14 | Nitrogen cycle. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E09](#e09) |
| 15.15 | Biological filtration maturity. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E09](#e09) |
| 15.16 | Water changes. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E09](#e09) |
| 15.17 | Equipment influence. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E09](#e09) |
| 15.18 | Waste from feeding. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E09](#e09) |
| 15.19 | Waste from fish. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E09](#e09) |
| 15.20 | Effects of dead organisms. | **PARTIAL** | Fish corpses and failed broods pollute; dead coral tissue is ignored (R17/I12). | [E02](#e02); [E08](#e08); [E09](#e09) |
| 15.21 | Relevant substrate nutrient processes. | **MISSING** | No substrate nutrient/maturation engine exists (R28/I10). | [E02](#e02); [E08](#e08); [E09](#e09) |
| 15.22 | Tank readiness uses actual water values. | **PASS** | Admission tests current temperature, salinity, pH, oxygen and toxins; this is a simplified game model. | [E02](#e02); [E08](#e08); [E09](#e09) |

#### 16. FISH HEALTH, AGING AND SURVIVAL

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 16.01 | Unique identity. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.02 | Age. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.03 | Life stage. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.04 | Expected lifespan. | **PARTIAL** | Expected lifespan is stored per species, but real-world lifespan verification is explicitly null for new clownfish. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.05 | Maximum lifespan. | **PARTIAL** | Maximum lifespan is bounded genetically; species-specific biological calibration remains provisional. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.06 | Health/HP. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.07 | Hunger. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.08 | Nutrition. | **PARTIAL** | Food quality affects particle nutrition/hunger, without a persistent individual nutrition/diet-quality state (I19). | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.09 | Stress. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.10 | Happiness/welfare. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.11 | Energy. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.12 | Fertility. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.13 | Genetics. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.14 | Growth. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.15 | Temperament. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.16 | Aggression. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.17 | Disease status. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.18 | Oxygen requirements. | **PARTIAL** | Oxygen affects health, but one generic low-oxygen threshold replaces species-specific respiratory demand. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.19 | Habitat requirements. | **PARTIAL** | Water/minimum litres/cover/social requirements exist; rock navigation, actual dimensions and hosting are absent. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.20 | Tank bioload. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.21 | Appropriate aging. | **PARTIAL** | Age, growth and probabilistic old-age death work; age-specific activity/fertility curves are incomplete. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.22 | Disease effects. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.23 | Environmental damage. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.24 | Natural death. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 16.25 | Death records. | **PARTIAL** | Cause and death count persist, but the 70-entry event log is not a permanent death history after removal (I12). | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |

#### 17. DEATH ART AND DECOMPOSITION

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 17.01 | Fish stops swimming at death. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E06](#e06); [E08](#e08); [E09](#e09); [E11](#e11) |
| 17.02 | Death pose appears. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E06](#e06); [E08](#e08); [E09](#e09); [E11](#e11) |
| 17.03 | Fish rolls sideways/upside down. | **PARTIAL** | Authored collapsed/sideways poses appear; no time-varying roll animation. | [E02](#e02); [E06](#e06); [E08](#e08); [E09](#e09); [E11](#e11) |
| 17.04 | Buoyancy and current affect corpse movement. | **MISSING** | Every dead fish is forced upward by the same constant motion rule (R18/I12). | [E02](#e02); [E06](#e06); [E08](#e08); [E09](#e09); [E11](#e11) |
| 17.05 | Sinking corpses reach the bottom. | **MISSING** | No sinking/bottom settlement implementation. | [E02](#e02); [E06](#e06); [E08](#e08); [E09](#e09); [E11](#e11) |
| 17.06 | Corpse remains visible. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E06](#e06); [E08](#e08); [E09](#e09); [E11](#e11) |
| 17.07 | Decomposition stages are displayed. | **MISSING** | deadHours is tracked but does not select early/advanced/remains imagery (R18). | [E02](#e02); [E06](#e06); [E08](#e08); [E09](#e09); [E11](#e11) |
| 17.08 | Decomposition affects chemistry. | **PARTIAL** | Constant corpse-driven pollution exists, without finite mass or decay-stage scaling. | [E02](#e02); [E06](#e06); [E08](#e08); [E09](#e09); [E11](#e11) |
| 17.09 | Corpse removal works. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E06](#e06); [E08](#e08); [E09](#e09); [E11](#e11) |
| 17.10 | Dead fish cannot reproduce or be sold as living fish. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E06](#e06); [E08](#e08); [E09](#e09); [E11](#e11) |
| 17.11 | Death cause is recorded. | **PASS** | Cause is stored on the dead entity and displayed in inspector/log; long-term history is incomplete. | [E02](#e02); [E06](#e06); [E08](#e08); [E09](#e09); [E11](#e11) |
| 17.12 | Bleaching is distinct from death. | **MISSING** | Bleached gallery art exists, but no independent living bleach state (R16/I11). | [E02](#e02); [E06](#e06); [E08](#e08); [E09](#e09); [E11](#e11) |
| 17.13 | Bleached living coral may recover. | **MISSING** | Generic stress recovers; there is no separate bleaching recovery mechanic. | [E02](#e02); [E06](#e06); [E08](#e08); [E09](#e09); [E11](#e11) |
| 17.14 | Dead tissue degrades. | **MISSING** | No finite fish/coral tissue mass or degradation progression. | [E02](#e02); [E06](#e06); [E08](#e08); [E09](#e09); [E11](#e11) |
| 17.15 | Stony skeleton can remain. | **PASS** | Stony dead artwork remains visible until manual removal; no dissolution or skeleton-algae process. | [E02](#e02); [E06](#e06); [E08](#e08); [E09](#e09); [E11](#e11) |
| 17.16 | Skeleton may accumulate algae. | **MISSING** | No corresponding runtime implementation found in the cited modules. | [E02](#e02); [E06](#e06); [E08](#e08); [E09](#e09); [E11](#e11) |
| 17.17 | Chemical dissolution is conditional. | **MISSING** | No corresponding runtime implementation found in the cited modules. | [E02](#e02); [E06](#e06); [E08](#e08); [E09](#e09); [E11](#e11) |
| 17.18 | Dead tissue affects organic waste. | **MISSING** | Dead coral does not add organic waste (R17); no dead-tissue mass model. | [E02](#e02); [E06](#e06); [E08](#e08); [E09](#e09); [E11](#e11) |

#### 18. COMPATIBILITY, AGGRESSION AND PREDATION

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 18.01 | Species compatibility rules. | **PARTIAL** | Purchase checks are stronger than transfer checks; transfers can admit unsafe water or mixed clownfish territories (R36-R38/I08). | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 18.02 | Adult size requirements. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 18.03 | Physical tank-space requirements. | **MISSING** | Admission uses nominal litres, not actual floor dimensions/swim corridors. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 18.04 | Territorial behavior. | **PARTIAL** | Aggressive encounters and cover matter; persistent geometric territories do not exist. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 18.05 | Schooling behavior. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 18.06 | Predator/prey relationships. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 18.07 | Chase behavior. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 18.08 | Fleeing behavior. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 18.09 | Stress from aggression. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 18.10 | Injury from attacks. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 18.11 | Death from severe predation or aggression. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 18.12 | Compatibility warnings before purchases. | **PARTIAL** | Store warnings and purchase commits work; legacy inspector/transfer rules disagree with StoreRules. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 18.13 | Reef compatibility. | **PARTIAL** | Reef compatibility metadata is displayed but does not model coral-hosting/reef predation rules. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 18.14 | Species-specific social needs. | **PARTIAL** | School counts and clownfish pair rules exist; actual social territories are incomplete. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |
| 18.15 | Predation does not behave randomly without triggers. | **PASS** | Predation requires proximity, hunger, size ratio, probability and cooldown, rather than an unconditional timer. | [E02](#e02); [E08](#e08); [E11](#e11); [E18](#e18) |

#### 19. FOOD AND FEEDING

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 19.01 | Flakes. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E12](#e12) |
| 19.02 | Pellets. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E12](#e12) |
| 19.03 | Sinking foods. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E12](#e12) |
| 19.04 | Frozen foods. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E12](#e12) |
| 19.05 | Live foods. | **MISSING** | No live-food catalog or consumption simulation. | [E02](#e02); [E08](#e08); [E12](#e12) |
| 19.06 | Herbivore foods. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E12](#e12) |
| 19.07 | Predator foods. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E12](#e12) |
| 19.08 | Fry food. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E12](#e12) |
| 19.09 | Coral food where appropriate. | **MISSING** | No dedicated coral-food product/feeding system. | [E02](#e02); [E08](#e08); [E12](#e12) |
| 19.10 | Species-specific diet rules. | **PARTIAL** | Adult accepted-food lists and fry food work; persistent nutritional adequacy is absent. | [E02](#e02); [E08](#e08); [E12](#e12) |
| 19.11 | Hunger changes correctly. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E12](#e12) |
| 19.12 | Feeding animations. | **PARTIAL** | Particles and food seeking exist; explicit bite/mouth animation is absent. | [E02](#e02); [E08](#e08); [E12](#e12) |
| 19.13 | Uneaten food produces waste. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E12](#e12) |
| 19.14 | Starvation affects health. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E12](#e12) |
| 19.15 | Overfeeding affects water. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E12](#e12) |
| 19.16 | Automatic feeding where implemented. | **PASS** | Automatic feeder consumes inventory once per day at 09:00, validated by the system suite. | [E02](#e02); [E08](#e08); [E12](#e12) |

#### 20. BREEDING AND GENETICS

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 20.01 | Species-appropriate breeding. | **PARTIAL** | Livebearer, mouthbrood and pair strategies exist, but many marine species use simplified shared brood assumptions. | [E02](#e02); [E04](#e04); [E08](#e08); [E11](#e11); [E18](#e18) |
| 20.02 | Biological maturity checks. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E08](#e08); [E11](#e11); [E18](#e18) |
| 20.03 | Fertility. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E08](#e08); [E11](#e11); [E18](#e18) |
| 20.04 | Sex/reproductive structure. | **PARTIAL** | F/M sex and carrier dependencies exist; a full species-specific reproductive anatomy/courtship model is incomplete. | [E02](#e02); [E04](#e04); [E08](#e08); [E11](#e11); [E18](#e18) |
| 20.05 | Clownfish sex-change biology. | **PARTIAL** | Established females are never demoted by pairing; transfers can still create mixed or inappropriate territories (R37). | [E02](#e02); [E04](#e04); [E08](#e08); [E11](#e11); [E18](#e18) |
| 20.06 | Eggs. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E08](#e08); [E11](#e11); [E18](#e18) |
| 20.07 | Incubation. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E08](#e08); [E11](#e11); [E18](#e18) |
| 20.08 | Species-dependent hatch duration. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E08](#e08); [E11](#e11); [E18](#e18) |
| 20.09 | Egg viability. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E08](#e08); [E11](#e11); [E18](#e18) |
| 20.10 | Baby/fry stages. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E08](#e08); [E11](#e11); [E18](#e18) |
| 20.11 | Juvenile growth. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E08](#e08); [E11](#e11); [E18](#e18) |
| 20.12 | Genetic inheritance. | **PASS** | Five bounded continuous genes are inherited; verified categorical morph segregation is outside this implemented model. | [E02](#e02); [E04](#e04); [E08](#e08); [E11](#e11); [E18](#e18) |
| 20.13 | Color/pattern genetics. | **PARTIAL** | Color brightness gene exists; pattern and fin-shape alleles are not modeled (I13). | [E02](#e02); [E04](#e04); [E08](#e08); [E11](#e11); [E18](#e18) |
| 20.14 | Designer variety integration. | **PARTIAL** | Saved purchase phenotype exists, but Snowflake parents produce offspring with no variety model (R19/I13). | [E02](#e02); [E04](#e04); [E08](#e08); [E11](#e11); [E18](#e18) |
| 20.15 | Parent lineage. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E08](#e08); [E11](#e11); [E18](#e18) |
| 20.16 | Breeding cannot duplicate fish. | **PASS** | Entity IDs and atomic actions prevent duplicate broods/purchases in tested paths. | [E02](#e02); [E04](#e04); [E08](#e08); [E11](#e11); [E18](#e18) |
| 20.17 | Offspring become valid persistent entities. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E08](#e08); [E11](#e11); [E18](#e18) |

#### 21. AQUARIUM SIZES AND CAPACITY

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 21.01 | 20 L. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E10](#e10); [E13](#e13) |
| 21.02 | 40 L. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E10](#e10); [E13](#e13) |
| 21.03 | 75 L. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E10](#e10); [E13](#e13) |
| 21.04 | 150 L. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E10](#e10); [E13](#e13) |
| 21.05 | 300 L. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E10](#e10); [E13](#e13) |
| 21.06 | 500 L. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E10](#e10); [E13](#e13) |
| 21.07 | 1,000 L. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E10](#e10); [E13](#e13) |
| 21.08 | 2,500 L. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E10](#e10); [E13](#e13) |
| 21.09 | 5,000 L. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E10](#e10); [E13](#e13) |
| 21.10 | Multiple tank ownership. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E10](#e10); [E13](#e13) |
| 21.11 | Tank naming. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E10](#e10); [E13](#e13) |
| 21.12 | Tank switching. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E10](#e10); [E13](#e13) |
| 21.13 | Tank dimensions. | **MISSING** | Volume-only aquarium products; no physical length/width/height model. | [E02](#e02); [E08](#e08); [E10](#e10); [E13](#e13) |
| 21.14 | Effective water volume. | **MISSING** | No sand/rock displacement-adjusted effective volume (R29). | [E02](#e02); [E08](#e08); [E10](#e10); [E13](#e13) |
| 21.15 | Stocking capacity. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E10](#e10); [E13](#e13) |
| 21.16 | Physical suitability. | **PARTIAL** | Minimum nominal volume and reserved adult load exist; dimension/corridor suitability does not. | [E02](#e02); [E08](#e08); [E10](#e10); [E13](#e13) |
| 21.17 | Equipment capacity. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E10](#e10); [E13](#e13) |
| 21.18 | Maintenance costs. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E10](#e10); [E13](#e13) |
| 21.19 | Tank asset value. | **PARTIAL** | Core.assets includes tank, fish, corals and equipment, but omits rock, sand, racks and decorations (I16). | [E02](#e02); [E08](#e08); [E10](#e10); [E13](#e13) |

#### 22. DAY/NIGHT, LIGHTING AND TEMPERATURE

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 22.01 | In-game clock. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E14](#e14) |
| 22.02 | Dawn. | **PARTIAL** | Time-dependent ambience is present; explicit dawn-phase behavior is incomplete. | [E02](#e02); [E08](#e08); [E14](#e14) |
| 22.03 | Day. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E14](#e14) |
| 22.04 | Dusk. | **PARTIAL** | Time-dependent ambience is present; explicit dusk-phase behavior is incomplete. | [E02](#e02); [E08](#e08); [E14](#e14) |
| 22.05 | Night. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E14](#e14) |
| 22.06 | Light intensity. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E14](#e14) |
| 22.07 | Light schedule. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E14](#e14) |
| 22.08 | Light spectrum where implemented. | **NOT APPLICABLE** | No independently configurable spectrum engine; conditional spectrum check is inapplicable. | [E02](#e02); [E08](#e08); [E14](#e14) |
| 22.09 | Coral response. | **PARTIAL** | Daily light affects coral stress/growth; distinct bleaching and pigment recovery are absent. | [E02](#e02); [E08](#e08); [E14](#e14) |
| 22.10 | Fish activity changes. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E14](#e14) |
| 22.11 | Nocturnal behavior. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E14](#e14) |
| 22.12 | Algae response. | **MISSING** | No algae engine (I10). | [E02](#e02); [E08](#e08); [E14](#e14) |
| 22.13 | Heater functionality. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E14](#e14) |
| 22.14 | Chiller functionality. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E14](#e14) |
| 22.15 | Temperature stability. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E14](#e14) |
| 22.16 | Lighting/temperature interactions. | **PARTIAL** | Day-dependent ambient temperature exists; lamp-generated heat/spectrum interactions are not modeled. | [E02](#e02); [E08](#e08); [E14](#e14) |
| 22.17 | Configurable simulation speed. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E14](#e14) |

#### 23. EQUIPMENT

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 23.01 | Filters. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E15](#e15) |
| 23.02 | Heaters. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E15](#e15) |
| 23.03 | Chillers. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E15](#e15) |
| 23.04 | Circulation pumps. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E15](#e15) |
| 23.05 | Aeration. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E15](#e15) |
| 23.06 | Protein skimmers. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E15](#e15) |
| 23.07 | Lighting. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E15](#e15) |
| 23.08 | Water testing. | **PARTIAL** | Water laboratory displays values; dedicated testing consumables/instruments/history are not implemented. | [E02](#e02); [E08](#e08); [E15](#e15) |
| 23.09 | Automatic feeders. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E15](#e15) |
| 23.10 | Relevant reef equipment. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E15](#e15) |
| 23.11 | Equipment purchase. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E15](#e15) |
| 23.12 | Equipment installation. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E15](#e15) |
| 23.13 | Equipment operation. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E15](#e15) |
| 23.14 | Equipment maintenance. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E15](#e15) |
| 23.15 | Equipment failure. | **PASS** | Durability reaching zero disables effect and logs failure; a broader random fault model is not claimed. | [E02](#e02); [E08](#e08); [E15](#e15) |
| 23.16 | Electricity costs. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E15](#e15) |
| 23.17 | Equipment state saved correctly. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E15](#e15) |

#### 24. MAIN STORE UI — CRITICAL

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 24.01 | Store opens through Store button. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.02 | Modal is centered. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.03 | Aquarium remains visible behind dark overlay. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.04 | Background clicks do not affect the tank. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.05 | X button is in the top-right corner. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.06 | X closes the store. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.07 | Escape closes the store. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.08 | Closing does not reload the game. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.09 | Modal scrolls internally. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.10 | Header remains visible. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.11 | Tabs remain usable. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.12 | Keyboard focus remains appropriate. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.13 | Opening repeatedly does not duplicate windows. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.14 | Existing inventory/economy connections work. | **PARTIAL** | Default purchase connections work; editing livestock quantity triggers the duplicate legacy handler (R32/I01). | [E03](#e03); [E16](#e16) |
| 24.15 | Saltwater. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.16 | Freshwater. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.17 | Black Market. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.18 | Fish. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.19 | Bottom Feeders. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.20 | Corals. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.21 | Rocks & Environment. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.22 | Sand & Substrate. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.23 | Equipment. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.24 | Food & Supplies. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.25 | Fish. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.26 | Bottom Feeders. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.27 | Plants. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.28 | Rocks & Environment. | **PASS** | Existing cave/driftwood/seasonal decorations only; no new freshwater habitat biology. | [E03](#e03); [E16](#e16) |
| 24.29 | Sand & Substrate. | **PASS** | Freshwater substrate category is intentionally empty with honest text. | [E03](#e03); [E16](#e16) |
| 24.30 | Equipment. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.31 | Food & Supplies. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.32 | Fish. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.33 | Bottom Feeders. | **PASS** | Black Market bottom-feeder category is present but empty. | [E03](#e03); [E16](#e16) |
| 24.34 | Corals. | **PASS** | Black Market coral category is present but empty. | [E03](#e03); [E16](#e16) |
| 24.35 | Rocks & Environment. | **PASS** | Black Market rocks/environment category is present but empty. | [E03](#e03); [E16](#e16) |
| 24.36 | Eggs & Specimens. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |
| 24.37 | Special Equipment. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E03](#e03); [E16](#e16) |

#### 25. STORE DESTINATION AQUARIUM — PERMANENT RULE

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 25.01 | Opening store preserves selected aquarium. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09) |
| 25.02 | Closing store preserves selected aquarium. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09) |
| 25.03 | Switching main tabs preserves selected aquarium. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09) |
| 25.04 | Switching sub-tabs preserves selected aquarium. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09) |
| 25.05 | Store header displays selected aquarium. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09) |
| 25.06 | Purchasing does not automatically switch tanks. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09) |
| 25.07 | Livestock purchases validate destination aquarium. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09) |
| 25.08 | Incompatible destinations are clearly identified. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09) |
| 25.09 | Player may choose another eligible destination. | **PASS** | Explicit destination selection saves the new selection; a purchase then preserves that explicit choice. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09) |
| 25.10 | An unsafe aquarium cannot receive livestock through a purchase bypass. | **PASS** | StoreRules is enforced inside Core.act for purchases; oxygen/toxin/predator/held-profile bypass tests reject atomically. Transfer gaps are separate (I08). | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09) |
| 25.11 | Equipment goes to the correct destination or inventory. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09) |
| 25.12 | Rock goes to correct destination or inventory. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09) |
| 25.13 | Sand goes to correct destination or inventory. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09) |
| 25.14 | Coral placement still requires suitable surface. | **PASS** | Coral purchase commits require an allowed support; false-positive previews and later support edits are reported in section 10. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09) |
| 25.15 | Destination-related state persists correctly after saving. | **PASS** | Selection, mounts, depth and purchased entities round-trip; shopping tab choice is session-local, not saved across app restarts. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09) |
| 25.16 | Freshwater animals cannot accidentally enter a marine tank. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09) |
| 25.17 | Saltwater animals cannot accidentally enter a freshwater tank. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09) |

#### 26. STORE PURCHASES AND INVENTORY

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 26.01 | Product preview images. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E16](#e16) |
| 26.02 | Correct names. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E16](#e16) |
| 26.03 | Correct prices. | **PASS** | Equipment confirmation recomputes cost for the explicit destination volume; retail and commit formulas match. | [E02](#e02); [E03](#e03); [E04](#e04); [E16](#e16) |
| 26.04 | Correct stock. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E16](#e16) |
| 26.05 | Care difficulty labels. | **PARTIAL** | Difficulty labels exist; most old species use level/aggression fallback and new care remains provisional. | [E02](#e02); [E03](#e03); [E04](#e04); [E16](#e16) |
| 26.06 | Product detail windows. | **PARTIAL** | Details/compatibility dialogs work; quantity changes throw a legacy UI exception (I01). | [E02](#e02); [E03](#e03); [E04](#e04); [E16](#e16) |
| 26.07 | Species compatibility information. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E16](#e16) |
| 26.08 | Insufficient funds validation. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E16](#e16) |
| 26.09 | Purchase confirmation. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E16](#e16) |
| 26.10 | Atomic transactions. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E16](#e16) |
| 26.11 | No double-click duplication. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E16](#e16) |
| 26.12 | Inventory updates. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E16](#e16) |
| 26.13 | Store stock updates. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E16](#e16) |
| 26.14 | Transaction history where implemented. | **PARTIAL** | Bounded transaction tokens and a bounded event log exist; a complete player-visible financial ledger is absent. | [E02](#e02); [E03](#e03); [E04](#e04); [E16](#e16) |
| 26.15 | Purchases remain after reload. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E16](#e16) |
| 26.16 | Living livestock is not stored indefinitely in invalid inventory. | **PASS** | Animals enter a compatible tank rather than ordinary inventory. Relocation-required corals remain owned entities, with a separate biology bug (I03). | [E02](#e02); [E03](#e03); [E04](#e04); [E16](#e16) |
| 26.17 | Empty categories have honest empty states. | **PASS** | Empty categories state that content is unavailable/coming soon rather than offering fake products. | [E02](#e02); [E03](#e03); [E04](#e04); [E16](#e16) |

#### 27. BLACK MARKET

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 27.01 | Black Market tab exists. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E08](#e08); [E16](#e16) |
| 27.02 | Unlock state is respected. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E08](#e08); [E16](#e16) |
| 27.03 | Existing black-market stock loads. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E08](#e08); [E16](#e16) |
| 27.04 | Appropriate rare/fictional items display. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E08](#e08); [E16](#e16) |
| 27.05 | Dealer stock restrictions work. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E08](#e08); [E16](#e16) |
| 27.06 | Prices work. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E08](#e08); [E16](#e16) |
| 27.07 | Reputation where implemented. | **NOT APPLICABLE** | No dealer reputation feature; conditional reputation check is inapplicable. | [E02](#e02); [E03](#e03); [E08](#e08); [E16](#e16) |
| 27.08 | Special care requirements are shown. | **PARTIAL** | Containment, habitat and night access are displayed, but fictional care uses simplified game parameters. | [E02](#e02); [E03](#e03); [E08](#e08); [E16](#e16) |
| 27.09 | Dangerous creatures have suitable warnings. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E08](#e08); [E16](#e16) |
| 27.10 | Transactions use normal validation. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E08](#e08); [E16](#e16) |
| 27.11 | No freshwater content was added during the current phase. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E08](#e08); [E16](#e16) |
| 27.12 | No infinite-profit exploit. | **PASS** | Contraband resale is prohibited, stock is bounded and ordinary purchase validation applies; this is evidence for current paths, not proof against all conceivable exploits. | [E02](#e02); [E03](#e03); [E08](#e08); [E16](#e16) |

#### 28. ECONOMY AND VALUATION

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 28.01 | Aquarium Credits currency. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13); [E18](#e18) |
| 28.02 | Starting balance. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13); [E18](#e18) |
| 28.03 | Livestock market values. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13); [E18](#e18) |
| 28.04 | Individual fish value modifiers. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13); [E18](#e18) |
| 28.05 | Rarity. | **PARTIAL** | Rarity is stored/displayed and designer retail differs, but Core.value ignores rarity and variety-specific retail. | [E02](#e02); [E08](#e08); [E13](#e13); [E18](#e18) |
| 28.06 | Health influence. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13); [E18](#e18) |
| 28.07 | Age influence. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13); [E18](#e18) |
| 28.08 | Genetics influence. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13); [E18](#e18) |
| 28.09 | Supply/demand. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13); [E18](#e18) |
| 28.10 | Aquarium asset value. | **PARTIAL** | Rock, sand, decorations and rack ownership is omitted from Core.assets (I16). | [E02](#e02); [E08](#e08); [E13](#e13); [E18](#e18) |
| 28.11 | Tank biological capacity value. | **PASS** | Adult reserved load and current growth load are separate from wallet/asset value. | [E02](#e02); [E08](#e08); [E13](#e13); [E18](#e18) |
| 28.12 | Limited store budgets. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13); [E18](#e18) |
| 28.13 | Controlled selling. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13); [E18](#e18) |
| 28.14 | Market saturation. | **PASS** | Sales reduce bounded demand, which recovers at dawn. | [E02](#e02); [E08](#e08); [E13](#e13); [E18](#e18) |
| 28.15 | Transaction cooldowns. | **MISSING** | Daily budgets/limits exist; no per-transaction resale waiting period (I16). | [E02](#e02); [E08](#e08); [E13](#e13); [E18](#e18) |
| 28.16 | Maintenance expenses. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13); [E18](#e18) |
| 28.17 | No infinite buy/sell loops. | **PASS** | Repeated immediate resale loses money and daily limits stop sales in exercised system fixtures. | [E02](#e02); [E08](#e08); [E13](#e13); [E18](#e18) |
| 28.18 | Economy balancing tests. | **PARTIAL** | 30-day care, 60-day breeding, hoarding/resale and 120-day bounded simulations ran; no complete new-roster 30/90/365-day economy matrix (I16). | [E02](#e02); [E08](#e08); [E13](#e13); [E18](#e18) |

#### 29. QUESTS AND ACHIEVEMENTS

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 29.01 | Quest list. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13) |
| 29.02 | Active quests. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13) |
| 29.03 | Completed quests. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13) |
| 29.04 | Locked quests. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13) |
| 29.05 | Objective tracking. | **PARTIAL** | Objectives use saved actions/state, but relocation-required corals incorrectly count for reef objectives (R23/I03). | [E02](#e02); [E08](#e08); [E13](#e13) |
| 29.06 | Rewards. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13) |
| 29.07 | Unlock conditions. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13) |
| 29.08 | One-time reward claims. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13) |
| 29.09 | Tank setup quests. | **PARTIAL** | Prepare/cycle/stock quests exist; full dry-construction/substrate/water-filling chain is absent. | [E02](#e02); [E08](#e08); [E13](#e13) |
| 29.10 | Cycling quests. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13) |
| 29.11 | Fish care quests. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13) |
| 29.12 | Coral quests. | **FAIL** | Invisible relocation-required colonies count as healthy reef progress (R23). | [E02](#e02); [E08](#e08); [E13](#e13) |
| 29.13 | Breeding quests. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13) |
| 29.14 | Marketplace quests. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13) |
| 29.15 | Aquarium prestige. | **PARTIAL** | Showcase and asset/discovery progression exist; a dedicated prestige score/system is incomplete. | [E02](#e02); [E08](#e08); [E13](#e13) |
| 29.16 | Achievements. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13) |
| 29.17 | Progress saving. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E08](#e08); [E13](#e13) |

#### 30. VIP PREVIEW

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 30.01 | Bronze. | **PASS** | Bronze concept card exists; illustrated-tier completeness is evaluated separately below. | [E08](#e08); [E16](#e16) |
| 30.02 | Silver. | **PASS** | Silver concept card exists; illustrated-tier completeness is evaluated separately below. | [E08](#e08); [E16](#e16) |
| 30.03 | Gold. | **PASS** | Gold concept card exists; illustrated-tier completeness is evaluated separately below. | [E08](#e08); [E16](#e16) |
| 30.04 | Platinum. | **PASS** | Platinum concept card exists; illustrated-tier completeness is evaluated separately below. | [E08](#e08); [E16](#e16) |
| 30.05 | Diamond. | **PASS** | Diamond concept card exists; illustrated-tier completeness is evaluated separately below. | [E08](#e08); [E16](#e16) |
| 30.06 | Image previews. | **MISSING** | Text cards and free tint buttons do not satisfy locally bundled illustrated VIP tiers (I17). | [E08](#e08); [E16](#e16) |
| 30.07 | Exclusive cosmetic fish previews. | **MISSING** | No corresponding runtime implementation found in the cited modules. | [E08](#e08); [E16](#e16) |
| 30.08 | Coral cosmetic previews. | **MISSING** | No corresponding runtime implementation found in the cited modules. | [E08](#e08); [E16](#e16) |
| 30.09 | Seasonal item previews. | **MISSING** | No corresponding runtime implementation found in the cited modules. | [E08](#e08); [E16](#e16) |
| 30.10 | Decoration previews. | **MISSING** | No corresponding runtime implementation found in the cited modules. | [E08](#e08); [E16](#e16) |
| 30.11 | Premium background previews. | **PARTIAL** | Free ambient tint choices exist; actual premium background image previews are absent. | [E08](#e08); [E16](#e16) |
| 30.12 | Clear VIP Preview label. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E08](#e08); [E16](#e16) |
| 30.13 | No payment processor. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E08](#e08); [E16](#e16) |
| 30.14 | No checkout. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E08](#e08); [E16](#e16) |
| 30.15 | No subscription charge. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E08](#e08); [E16](#e16) |
| 30.16 | No payment-card collection. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E08](#e08); [E16](#e16) |
| 30.17 | No unauthorized entitlement activation. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E08](#e08); [E16](#e16) |

#### 31. SEASONAL EVENTS

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 31.01 | Halloween framework. | **PARTIAL** | Offline selectable season value exists; no dedicated Halloween reward/content chain. | [E02](#e02); [E08](#e08); [E16](#e16) |
| 31.02 | Winter event framework. | **PARTIAL** | Offline selectable season value exists; no dedicated winter reward/content chain. | [E02](#e02); [E08](#e08); [E16](#e16) |
| 31.03 | Valentine's event framework. | **PARTIAL** | Offline selectable season value exists; no dedicated Valentine reward/content chain. | [E02](#e02); [E08](#e08); [E16](#e16) |
| 31.04 | Spring event framework. | **PARTIAL** | Offline selectable season value exists; no dedicated spring reward/content chain. | [E02](#e02); [E08](#e08); [E16](#e16) |
| 31.05 | Summer event framework. | **PARTIAL** | Offline selectable season value exists; no dedicated summer reward/content chain. | [E02](#e02); [E08](#e08); [E16](#e16) |
| 31.06 | Anniversary event framework. | **PARTIAL** | Offline selectable season value exists; no dedicated anniversary reward/content chain. | [E02](#e02); [E08](#e08); [E16](#e16) |
| 31.07 | Event artwork consistency. | **PARTIAL** | Generic procedural lantern exists; dedicated event art sets are absent. | [E02](#e02); [E08](#e08); [E16](#e16) |
| 31.08 | Event quests where implemented. | **PARTIAL** | One seasonal decoration objective exists; event-specific quest chains are absent. | [E02](#e02); [E08](#e08); [E16](#e16) |
| 31.09 | Offline event testing. | **PASS** | Season selection is local, save-validated and available without internet; system fixture changes season offline. | [E02](#e02); [E08](#e08); [E16](#e16) |
| 31.10 | Previously acquired event items remain owned. | **PASS** | System fixture confirms acquired lantern ID survives a season change. | [E02](#e02); [E08](#e08); [E16](#e16) |

#### 32. USER INTERFACE AND EXPERIENCE

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 32.01 | Main background is near-black. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E09](#e09); [E16](#e16) |
| 32.02 | Panels are slate blue. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E09](#e09); [E16](#e16) |
| 32.03 | Aquarium is the main visual centerpiece. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E09](#e09); [E16](#e16) |
| 32.04 | UI has original identity. | **PARTIAL** | Distinct palette/layout is present; originality is subjective and has not received user review. | [E02](#e02); [E03](#e03); [E09](#e09); [E16](#e16) |
| 32.05 | Navigation is understandable. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E09](#e09); [E16](#e16) |
| 32.06 | Text is readable. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E09](#e09); [E16](#e16) |
| 32.07 | Menus have consistent styling. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E09](#e09); [E16](#e16) |
| 32.08 | Buttons have hover states. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E09](#e09); [E16](#e16) |
| 32.09 | Buttons have focus states. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E09](#e09); [E16](#e16) |
| 32.10 | Warnings are clear. | **PARTIAL** | Compatibility reasons are clear, but Suitable coral previews can disagree with commit (I02). | [E02](#e02); [E03](#e03); [E09](#e09); [E16](#e16) |
| 32.11 | Tooltips explain unfamiliar systems. | **PARTIAL** | Some hover titles and explanations exist; unfamiliar chemistry/placement concepts are not comprehensively covered. | [E02](#e02); [E03](#e03); [E09](#e09); [E16](#e16) |
| 32.12 | Fish inspector works. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E09](#e09); [E16](#e16) |
| 32.13 | Coral inspector works. | **PARTIAL** | Overview/Care tabs and reposition work; SPS transfer UI lacks mounting coordinates (I21). | [E02](#e02); [E03](#e03); [E09](#e09); [E16](#e16) |
| 32.14 | Substrate inspector works. | **PARTIAL** | Type/depth/support controls exist; cm/mass/maturation/maintenance sections are absent (I10). | [E02](#e02); [E03](#e03); [E09](#e09); [E16](#e16) |
| 32.15 | Water conditions panel works. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E09](#e09); [E16](#e16) |
| 32.16 | Equipment inspector works. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E09](#e09); [E16](#e16) |
| 32.17 | Quest interface works. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E09](#e09); [E16](#e16) |
| 32.18 | Inventory interface works. | **PARTIAL** | Food/supply inventory is visible; no comprehensive owned-item inventory inspector. | [E02](#e02); [E03](#e03); [E09](#e09); [E16](#e16) |
| 32.19 | Aquarium selector works. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E09](#e09); [E16](#e16) |
| 32.20 | UI remains usable at smaller desktop resolutions. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E09](#e09); [E16](#e16) |
| 32.21 | No misleading buttons. | **PARTIAL** | SPS transfer can appear available yet fail on default destination coordinates; some old buy eligibility differs from commit rules. | [E02](#e02); [E03](#e03); [E09](#e09); [E16](#e16) |
| 32.22 | No invisible interactive elements. | **PARTIAL** | No hidden store duplicate was observed, but full interaction coverage outside the exercised screens is incomplete. | [E02](#e02); [E03](#e03); [E09](#e09); [E16](#e16) |

#### 33. SAVE/LOAD AND OFFLINE PROGRESSION

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 33.01 | Autosave. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |
| 33.02 | Manual save. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |
| 33.03 | Save schema version. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |
| 33.04 | Save validation. | **PARTIAL** | Schema/number/identity checks are strong, but coral legal-coordinate ranges disagree with placement and full growth geometry is not validated (I02/I07). | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |
| 33.05 | Save migration. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |
| 33.06 | Export save. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |
| 33.07 | Import save. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |
| 33.08 | Corrupt-save handling. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |
| 33.09 | Fish identities persist. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |
| 33.10 | Life stages persist. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |
| 33.11 | Fish death states persist. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |
| 33.12 | Coral states persist. | **PARTIAL** | Health/age/growth/color persist; separate living bleaching/decomposition fields do not exist. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |
| 33.13 | Coral attachments persist. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |
| 33.14 | Substrate depth persists. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |
| 33.15 | Rock placement persists. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |
| 33.16 | Currency persists. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |
| 33.17 | Inventory persists. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |
| 33.18 | Quests persist. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |
| 33.19 | Store stock persists. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |
| 33.20 | Tank selection persists. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |
| 33.21 | Offline progression is bounded. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |
| 33.22 | Long absence does not cause unintended save corruption. | **PASS** | Representative 365-day absence fixture produces bounded eight-hour catch-up and a valid state (R27); this is not a real-year soak. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |
| 33.23 | Browser storage limitations are handled. | **PASS** | Code catches unavailable/quota storage, protects unreadable saves and offers export/recovery; no durability guarantee is made for disabled storage. | [E02](#e02); [E03](#e03); [E04](#e04); [E09](#e09); [E17](#e17) |

#### 34. PERFORMANCE AND OPTIMIZATION

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 34.01 | Rendering and simulation are separated. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E08](#e08); [E14](#e14); [E19](#e19) |
| 34.02 | Simulation uses consistent timesteps. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E08](#e08); [E14](#e14); [E19](#e19) |
| 34.03 | Chemistry calculations are not performed unnecessarily every frame. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E08](#e08); [E14](#e14); [E19](#e19) |
| 34.04 | Sprite atlases or equivalent batching are used appropriately. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E08](#e08); [E14](#e14); [E19](#e19) |
| 34.05 | Static scenery is cached where useful. | **PARTIAL** | Sprite/plant/palette caches exist; background grains/hardscape are redrawn every visual frame. | [E02](#e02); [E04](#e04); [E08](#e08); [E14](#e14); [E19](#e19) |
| 34.06 | Fish interactions scale reasonably. | **PARTIAL** | Short 250-fish render and 3,000-fish tick workloads are measured, but repeated linear school/encounter searches lack spatial grouping. | [E02](#e02); [E04](#e04); [E08](#e08); [E14](#e14); [E19](#e19) |
| 34.07 | Offscreen aquariums are not fully rendered unnecessarily. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E08](#e08); [E14](#e14); [E19](#e19) |
| 34.08 | Particle effects are bounded. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E08](#e08); [E14](#e14); [E19](#e19) |
| 34.09 | Lighting is adjustable. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E08](#e08); [E14](#e14); [E19](#e19) |
| 34.10 | Performance preset works. | **MISSING** | No Performance preset selector/configuration (I22). | [E02](#e02); [E04](#e04); [E08](#e08); [E14](#e14); [E19](#e19) |
| 34.11 | Balanced preset works. | **MISSING** | No Balanced preset selector/configuration (I22). | [E02](#e02); [E04](#e04); [E08](#e08); [E14](#e14); [E19](#e19) |
| 34.12 | Ultra preset works. | **MISSING** | No Ultra preset selector/configuration (I22). | [E02](#e02); [E04](#e04); [E08](#e08); [E14](#e14); [E19](#e19) |
| 34.13 | Fish remain visually clear under lower graphics settings. | **PASS** | Disabling ambient particles retains the same sprite rasterization; there are no actual graphics presets. | [E02](#e02); [E04](#e04); [E08](#e08); [E14](#e14); [E19](#e19) |
| 34.14 | Memory usage remains stable. | **NOT TESTED** | Only short-run heap snapshots and bounded-cache inspection; no extended memory/GC soak. | [E02](#e02); [E04](#e04); [E08](#e08); [E14](#e14); [E19](#e19) |
| 34.15 | Long-running simulation does not cause progressive slowdown. | **NOT TESTED** | Long simulated time is validated, but multi-hour wall-clock slowdown/heap behavior was not tested. | [E02](#e02); [E04](#e04); [E08](#e08); [E14](#e14); [E19](#e19) |
| 34.16 | Browser resizing is handled correctly. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E02](#e02); [E04](#e04); [E08](#e08); [E14](#e14); [E19](#e19) |
| 34.17 | Frame rate is measured rather than assumed. | **PARTIAL** | Render-call costs are measured; end-to-end displayed FPS/frame pacing was not measured (I22). | [E02](#e02); [E04](#e04); [E08](#e08); [E14](#e14); [E19](#e19) |

#### 35. CONTENT EXPANSION RULE

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 35.01 | Content batch rule is documented. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E18](#e18) |
| 35.02 | Every added species has unique metadata. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E18](#e18) |
| 35.03 | Every added species follows art-stage requirements. | **PASS** | All added clownfish sheets supply eight views and adult swim poses; art-only historical fish remain explicitly incomplete. | [E04](#e04); [E05](#e05); [E18](#e18) |
| 35.04 | Every added fish follows eye/direction rules. | **PASS** | All added clownfish technical eye/direction cases pass at tested sizes; species anatomy is still provisional. | [E04](#e04); [E05](#e05); [E18](#e18) |
| 35.05 | Every added coral follows placement restrictions. | **NOT APPLICABLE** | No coral species were added during the dedicated clownfish expansion. Existing coral defects are assessed elsewhere. | [E04](#e04); [E05](#e05); [E18](#e18) |
| 35.06 | Every added species has appropriate care difficulty. | **PARTIAL** | Difficulty/care metadata exists, but five specialist profiles remain held and group calibrations need verification. | [E04](#e04); [E05](#e05); [E18](#e18) |
| 35.07 | No existing species is duplicated. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E18](#e18) |
| 35.08 | No freshwater livestock expansion occurs without authorization. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E04](#e04); [E05](#e05); [E18](#e18) |
| 35.09 | Special approved expansions, such as the clownfish collection, are clearly identified as exceptions. | **PASS** | The dedicated clownfish collection is explicitly exempted from the broader 25/5/5 batch target. | [E04](#e04); [E05](#e05); [E18](#e18) |

#### 36. DOCUMENTATION AND CONTINUITY

| Check | Original requirement | Status | Finding | Evidence |
|---|---|---|---|---|
| 36.01 | `GAME_DESIGN.md`. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E18](#e18); [E20](#e20) |
| 36.02 | `ART_DIRECTION.md`. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E18](#e18); [E20](#e20) |
| 36.03 | `UI_SPECIFICATION.md`. | **PARTIAL** | Current header is accurate, but an unqualified older paragraph still says sand/rock stores and substrate inspector are absent (I20). | [E18](#e18); [E20](#e20) |
| 36.04 | `CURRENT_LIVESTOCK_CATALOG.md`. | **PASS** | Catalog updated with audit quality distinctions without changing biological data. | [E18](#e18); [E20](#e20) |
| 36.05 | `DEVELOPMENT_STATUS.md`. | **PARTIAL** | Current/historical milestones are separated at top; unqualified earlier wording and stale test assumptions still need cleanup. | [E18](#e18); [E20](#e20) |
| 36.06 | `BALANCE_REPORT.md`. | **PARTIAL** | Original phase balance findings exist; expanded clownfish/habitat economics lack required current 30/90/365-day coverage. | [E18](#e18); [E20](#e20) |
| 36.07 | `README.md`. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E18](#e18); [E20](#e20) |
| 36.08 | Consolidated 31-section Master Development Prompt. | **PASS** | Actual consolidated file has all 31 numbered major sections. | [E18](#e18); [E20](#e20) |
| 36.09 | Contains every locked rule. | **PARTIAL** | Critical locked rules are present, but the historical art-only gate and newer active store scope are ambiguously combined. | [E18](#e18); [E20](#e20) |
| 36.10 | Preserves earlier requirements. | **NOT TESTED** | Full word-by-word preservation against every historical pasted request/version was not verified; 31 sections and latest named rules were checked. | [E18](#e18); [E20](#e20) |
| 36.11 | Avoids duplicate descriptions. | **PARTIAL** | Historical art/update instructions and duplicate active-scope language remain; no cleanup was authorized. | [E18](#e18); [E20](#e20) |
| 36.12 | Uses one primary section per major mechanic. | **PASS** | Primary numbered sections exist, with cross-references for shared store/mounting/art rules. | [E18](#e18); [E20](#e20) |
| 36.13 | Correctly cross-references interacting systems. | **PASS** | Actual cross-references 2.5, 3.10/3.11, 18.4, 23.1 and 24 are present. | [E18](#e18); [E20](#e20) |
| 36.14 | Preserves current saltwater-only development scope. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E18](#e18); [E20](#e20) |
| 36.15 | Documents future freshwater expansion. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E18](#e18); [E20](#e20) |
| 36.16 | Records the latest approved art reference. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E18](#e18); [E20](#e20) |
| 36.17 | Includes the store destination aquarium rule. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E18](#e18); [E20](#e20) |
| 36.18 | Includes the life-stage artwork rule. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E18](#e18); [E20](#e20) |
| 36.19 | Includes the coral placement rule. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E18](#e18); [E20](#e20) |
| 36.20 | Includes the eye persistence rule. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E18](#e18); [E20](#e20) |
| 36.21 | Includes the 25/5/5 content expansion rule. | **PASS** | Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G. | [E18](#e18); [E20](#e20) |


## H. Next Development Milestone

Recommend one bounded milestone: **store quantity handling and coral preview/commit/transfer correctness** (I01, I02 and I21).

1. Remove the obsolete quantity event-path conflict and exercise real bubbled input events.
2. Give marine placement and save validation a consistent coordinate contract; preserve existing freshwater plant constraints and verify valid shallow sandbases/upper racks through purchase, save and reload.
3. Give the coral transfer flow an explicit valid target surface/position, with cancel preserving identity, health, funds and ownership.

Acceptance: repeat the existing system/store/clownfish regressions in Chrome and Edge; turn R05/R06/R11/R32 into meaningful passing regression checks; retain rejected-purchase rollback, no duplicate charge, selected-aquarium persistence and all protected freshwater hashes. Unsafe transfer admission (I08) is the next closely related correctness milestone and must be clearly scoped before implementation. This first group is smaller and easier to review than simultaneously adding substrate biology, more livestock and complete decomposition.

**Audit complete. STOP: no gameplay fixes or new features have been implemented. Await user review and explicit authorization before development.**
