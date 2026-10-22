"""Build the audit document from explicit review decisions and captured evidence."""
import collections,json
from pathlib import Path
from project_audit_classifications import classify
from project_audit_static import embedded

ROOT=Path(__file__).resolve().parent.parent

INTRO='''# Aquarium Life — complete project audit

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

{metrics}

Applicable checks = total checks minus NOT APPLICABLE. **NOT TESTED remains in the applicable denominator and is not successful.** PARTIAL, FAIL and MISSING are also not successful. This unweighted percentage measures checklist outcomes, not release readiness or the fraction of engineering effort remaining; the roster/category-name checks have the same numeric weight as save safety and entire biological systems.

## C. Livestock Inventory

{inventory}

“Implemented” means a runtime catalog/rendering definition, not an assertion that it is currently purchasable or scientifically complete. Marine count includes the explicitly fictional Voidfin Specter; freshwater count includes the protected fictional Glassfang Eel. Benthic fish are counted once inside the 52 fish records. Designer phenotypes never add a biological species.

**Artwork completeness has three separate meanings.** All 57 implemented base entries map eight required alive/dead stage views; 25 designers add another 200 presentations with shared base eggs/larvae. This gives 82 complete presentation chains / 656 stage-state presentations. Five historical art-only fish remain incomplete in stage coverage. There are **zero fully user-approved complete new stage chains**; approval of the existing adult Ocellaris image does not approve all new life-stage/anatomy assets. All 31 clownfish catalog entries and 25 designer entries have adult swim cycles; the other 21 implemented fish currently use static stage poses.

The collection comprises 31 named clownfish catalog entries (including explicitly uncertain hybrid-origin entries) and 25 commercial phenotype records. Five specialist care profiles are purchase-held: Whitebonnet, McCulloch's, Wide-band, Thielle's and Polynesian. Their catalog presence passes presence checks; their care/purchase readiness remains incomplete. The complete current inventory with per-entry paths/status/stages is in [CURRENT_LIVESTOCK_CATALOG.md](CURRENT_LIVESTOCK_CATALOG.md).

Coral groups: Garden zoanthids (`zoa`), Mushroom coral (`mushroom`), Branching SPS (`sps`), Hammer LPS (`lps`) and Soft leather coral (`soft`). Precise species identity is unverified. Bottom dwellers: Bronze corydoras (`cory`) and Bristlenose pleco (`pleco`) freshwater; Yellow watchman goby (`watchman`) and Tailspot blenny (`blenny`) marine.

The five **ART ONLY** subjects are Niger triggerfish (*Odonus niger*), Emperor angelfish (*Pomacanthus imperator*), Red lionfish (*Pterois volitans*), Dogface puffer (*Arothron nigropunctatus*) and Blue tang (*Paracanthurus hepatus*). Each has adult four-frame art, not a complete early/dead chain or a gameplay species definition. Three fictional proposals remain **PLANNED** with no completed art: Emberjaw Leviathan, Abyssal Crownfish and Prismheart Ray. DATA ONLY count is zero.

Local integrity checks verify 96 embedded atlas records: 13 earlier fish/coral/rock banks, 27 earlier stage atlases and 56 clownfish sheets. Every recorded atlas has the expected dimensions, binary alpha, transparency and byte-identical embedded PNG; 134 literal local runtime resource references exist. No missing literal runtime asset or HTTP(S) game request was found. Preserved historical Ocellaris sheets account for overlap between bank records and unique catalog entries.

### Clownfish species / designer inventory

{clown_inventory}

{designer_inventory}

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
| Static resource/archive/source integrity | {integrity_summary} | Same files | [Static integrity](tests/audit-evidence/static-integrity.json). |

Commands executed through isolated headless profiles with network disabled: `python tests/browser_qa.py chrome`, `python tests/browser_qa.py edge`, each browser with `--clownfish`, `--audit` and `--art-review`; additionally Chrome `--life-stages` (stale assertion failure), Edge `--sprite-audit`, and `python tests/project_audit_static.py`. A mistaken `--browser edge` invocation failed argument parsing before launching a browser and was rerun using the documented positional syntax. This command mistake has no project-feature classification.

{performance}

These are short, synthetic headless render-call/tick timings, not displayed FPS or real livestock-care recommendations. Render workload: 250 fish, 120 draws. Tick workload: 12 tanks / 3,000 fish, 20 five-minute steps. No long wall-clock memory/GC soak, low-end device study, Firefox run, extended touch/screen-reader review, or actual private-save audit was performed. The short heap snapshots do not establish memory stability.

### Evidence index

{evidence_index}

### MDP comparison: all 31 major sections

This trace compares requirement groups against actual implementation. It supplements the original 668-row checklist; it is not counted a second time in completion metrics. Full preservation of every earlier pasted version was not established, and the consolidated MDP was not rewritten.

{mdp_trace}

### Complete original checklist: 668 classified checks

The machine-readable decisions are in [checklist-classifications.json](tests/audit-evidence/checklist-classifications.json). Original wording is preserved below; IDs `section.item` identify the exact item in the user's section order. FAIL denotes implemented contradictory behavior; MISSING denotes no corresponding implementation. NOT APPLICABLE is reserved for genuinely conditional/out-of-scope checks, not a substitute for missing mandatory features.

{checklist}

## H. Next Development Milestone

Recommend one bounded milestone: **store quantity handling and coral preview/commit/transfer correctness** (I01, I02 and I21).

1. Remove the obsolete quantity event-path conflict and exercise real bubbled input events.
2. Give marine placement and save validation a consistent coordinate contract; preserve existing freshwater plant constraints and verify valid shallow sandbases/upper racks through purchase, save and reload.
3. Give the coral transfer flow an explicit valid target surface/position, with cancel preserving identity, health, funds and ownership.

Acceptance: repeat the existing system/store/clownfish regressions in Chrome and Edge; turn R05/R06/R11/R32 into meaningful passing regression checks; retain rejected-purchase rollback, no duplicate charge, selected-aquarium persistence and all protected freshwater hashes. Unsafe transfer admission (I08) is the next closely related correctness milestone and must be clearly scoped before implementation. This first group is smaller and easier to review than simultaneously adding substrate biology, more livestock and complete decomposition.

**Audit complete. STOP: no gameplay fixes or new features have been implemented. Await user review and explicit authorization before development.**
'''

EVIDENCE=[
 ('E01','Runtime + code','Offline boot/new game','[index.html](index.html), [main.js:3](js/main.js#L3), [Chrome audit startup](tests/audit-evidence/chrome-project-audit.json), [Edge](tests/audit-evidence/edge-project-audit.json). Protocol file:, three stylesheets, zero startup exceptions and zero game HTTP(S) requests. Network was disabled. [New installation view](tests/audit-evidence/chrome-new-installation.png).'),
 ('E02','Runtime + code','Core/system rules','[68-check source](tests/suite.js), [Chrome system results](tests/chrome-results.json), [Edge](tests/edge-results.json); [core.js](js/core.js) constructor/compatibility/actions/act, [simulation.js](js/simulation.js), [save.js](js/save.js). Named checks in result files cover each exercised behavior; no claim of absent-feature completion.'),
 ('E03','Runtime','Current shared store','[store_qa.py](tests/store_qa.py), [Chrome 88 results](tests/chrome-store-results.json), [Edge](tests/edge-store-results.json). Exact tabs/category labels, native modal, fixed header/internal scroll, repeated opening, Escape/X, 1440/1024/760/390 widths, saved selection, destination/stock/funds, stale compatibility and duplicates are exercised. [store.js](js/store.js) products/render/details/chooseDestination/submit/open/close.'),
 ('E04','Runtime + metadata','Current collection and stage maps','[clownfish checks](tests/clownfish_checks.js), [Chrome 7583 results](tests/chrome-clownfish-results.json), [Edge](tests/edge-clownfish-results.json); audit R01/R02/R03/R20/R21/R24/R25. Current R02 checks 616 fish/designer stage/state presentations; coral coverage is additionally in E06. [clownfish-art.js](js/clownfish-art.js), [clownfish-art-bank.js](js/clownfish-art-bank.js), [life-stages.js](js/life-stages.js).'),
 ('E05','Runtime + code','Eyes, flipping, immutable rendering','[sprite-kit.js](js/sprite-kit.js) raster/draw, [sprite_checks.js](tests/sprite_checks.js), [clownfish checks](tests/clownfish_checks.js), [art results](tests/chrome-art11-results.json), [Edge eye diagnostic](tests/edge-eye-after.json). Applicable eyes are sampled with the complete sprite at final raster size; bounded raster cache, left/right pixel coordinates and save/restore are checked.'),
 ('E06','Runtime + static','Earlier coral/rock/stage banks','[asset-bank.js](js/asset-bank.js) frame/coral/drawCoral and manifest, [life_stage_checks.js](tests/life_stage_checks.js), audit `lifeAssetChecks` 113/2160 in each [audit JSON](tests/audit-evidence/chrome-project-audit.json); [221 art results](tests/chrome-art11-results.json), [Edge](tests/edge-art11-results.json), [static integrity](tests/audit-evidence/static-integrity.json). Five coral × five visual states, rigid vs soft motion and 12 rock variants inspected/tested.'),
 ('E07','Manual visual inspection','Livestock and approved reference','Inspected [approved reference](assets/reference/approved_clownfish_hybrid.png); all eight [current fish contact pages](tests/audit-evidence/chrome-fish-contact-1.png) (1–8 in the same folder); all four designer contacts and three old life-stage contacts in assets/previews; five art-only adult atlases; coral/rock gallery screenshots and the mounting study. The [offline galleries](clownfish-review.html) expose all mappings and provisional review status. These observations are not automatic user approval.'),
 ('E08','Code inspection + runtime fixtures','Simulation feature scope','[simulation.js](js/simulation.js) water/food/fishHealth/floraConditions/ecosystems/breedingReady/makeBrood/eggs/daily/step/motion/offline; [core.js](js/core.js) fields/actions. The entire module was inspected. Existing positive behavior is exercised by E02; missing-state claims come from absence of fields/branches plus relevant R12/R15–R19/R23/R28/R29 observations.'),
 ('E09','Runtime + code','Coral placement, attachment and inspector','[habitat.js](js/habitat.js) definitions/solid/candidates/placement/validAttachment/migrate/sync; [core.js:69](js/core.js#L69) support/depth actions and buyFlora/moveFlora/reposition; [ui.js](js/ui.js) inspectFlora/beginCoral/placement handlers; [save.js](js/save.js) flora constraints. E02/E03/E04 positive mounting cases and R05–R11/R22/R23/R30 negative/boundary observations. [Coral Care view](tests/edge-coral-info.png).'),
 ('E10','Code inspection + validated state','Substrate and dry setup scope','[habitat.js:11](js/habitat.js#L11) sandProducts/initialize/bed, [core.js:9](js/core.js#L9) tank and buySand, [simulation.js](js/simulation.js) step/water/ecosystems, [store.js:33](js/store.js#L33) sand product and depth form. R12/R28/R29/R30 capture initial scenery, static substrate, missing mass/effectiveVolume and rejected removal of an occupied support.'),
 ('E11','Runtime + code','Fish identity, health and breeding','[core.js:31](js/core.js#L31) fish/value/kill/moveFish, [simulation.js:52](js/simulation.js#L52) fishHealth/breedingReady/makeBrood/eggs/motion, [data.js](js/data.js) species; E02 named health, hunger, aging, predation, cooldown, lineage/brood/viability and no-duplicate-ID results. Audit R19/R20/R21/R36/R37 records current limits.'),
 ('E12','Runtime + code','Food and inventory','[data.js](js/data.js) foods/supplies (seven foods), [core.js:116](js/core.js#L116) feed, [simulation.js](js/simulation.js) food and automatic feeder branch, [ui.js](js/ui.js) foodPage. E02 wrong diet, uneaten-waste, consumption, starvation and once-per-day inventory assertions.'),
 ('E13','Runtime + code','Economy/progression/capacity','[core.js:58](js/core.js#L58) value/assets/progress/pay/earn/sell/claim, [data.js](js/data.js) sizes/quests, [simulation.js:129](js/simulation.js#L129) daily/achievements, [BALANCE_REPORT](BALANCE_REPORT.md) and current system result `balances`. Existing 19 quests, nine size products, budgets/demand, daily sale limits and finite scenario tests are evidence; expanded scenario coverage is explicitly incomplete.'),
 ('E14','Runtime + code','Lighting/time/temperature','[simulation.js](js/simulation.js) light/lightPower/water, [render.js](js/render.js) scene illumination, [core.js](js/core.js) setLighting/controls, [main.js](js/main.js) fixed ticks and speed, E02/E03 manual night-on/day-off/auto/durability/temperature checks and [light on](tests/chrome-light-on.png)/[off](tests/chrome-light-off.png). Biology and visuals share installed lamp output.'),
 ('E15','Runtime + code','Equipment','[data.js](js/data.js) equipment, [core.js:8](js/core.js#L8) equipment constructor plus buyEquipment/service/toggleEquipment/moveEquipment, [simulation.js:16](js/simulation.js#L16) wear/failure/effects, [ui.js](js/ui.js) equipmentPage. E02 heater failure/service/auto feeder/dosing/containment and E03 equipment destination/cost/state checks.'),
 ('E16','Runtime + code + visuals','UI, VIP and events','[theme.css](css/theme.css), [main.css](css/main.css), [store.css](css/store.css), [ui.js](js/ui.js) pages/bind/inspectors/settingsPage/vipPage, [store.js](js/store.js). E03 responsive/dialog/UI execution and R32–R35 real input/thumb/focus/backdrop observations; [current catalog](tests/audit-evidence/chrome-current-catalog.png), [VIP screenshot](tests/audit-evidence/chrome-vip-preview.png), [store narrow view](assets/previews/chrome-store-mobile.png). VIP inspection finds no payment/card/checkout path; Save.validate rejects enabled entitlements. E02 validates offline season change and owned lantern persistence.'),
 ('E17','Runtime + code','Persistence','[save.js](js/save.js) validate/migrate/parse/load/save/exportSave/recover, [main.js](js/main.js) autosave/hidden/unload save, [ui.js](js/ui.js) import/export/recovery handlers; E02/E03 and R21/R22/R24/R26/R27. Export/import controls are present, current game-state round trips validated; storage-error catch/recovery was also inspected. No private player saves were used.'),
 ('E18','Static inspection + source verification','Catalog, protected scope and resources','[static audit](tests/project_audit_static.py), [integrity results](tests/audit-evidence/static-integrity.json), [audit baseline](tests/audit-code-baseline.json), [protected baseline](tests/freshwater-protection-baseline.json), [collection metadata](assets/livestock/fish/clownfish/collection.json), [CURRENT_LIVESTOCK_CATALOG](CURRENT_LIVESTOCK_CATALOG.md). 145 protected entries match directly, and simulation matches after restoring only the previously authorized marine pairing block. 42 audited source files unchanged. WoRMS/ORA checks are described in C with their limits.'),
 ('E19','Measured runtime + code','Performance','Two audit JSON `performance` and `performanceMetrics` records; [main.js:9](js/main.js#L9), [render.js](js/render.js) selected-tank draw/cache/particle limits, [sprite-kit.js](js/sprite-kit.js) bounded raster cache, [life-stages.js](js/life-stages.js)/[asset-bank.js](js/asset-bank.js) 256-entry caches. No displayed-FPS or long soak result is inferred from render costs.'),
 ('E20','Document inspection','Continuity and MDP rules','[GAME_DESIGN](GAME_DESIGN.md), [ART_DIRECTION](ART_DIRECTION.md), [UI_SPECIFICATION](UI_SPECIFICATION.md), [catalog](CURRENT_LIVESTOCK_CATALOG.md), [DEVELOPMENT_STATUS](DEVELOPMENT_STATUS.md), [BALANCE_REPORT](BALANCE_REPORT.md), [README](README.md), [31-section MDP](MASTER_DEVELOPMENT_PROMPT.md). Actual major headings and latest scope/reference/life-stage/eyes/store destination/coral mounting/25-5-5 rules checked. Historical wording conflicts and unverified full-version preservation are recorded, not silently repaired.')]

TRACE=[
 (1,'PARTIAL','Playable offline simulator concept exists; full biological/management scope remains unfinished.','1, 14–23'),
 (2,'PARTIAL','Offline/classic-script foundation and saltwater scope work; compressed modules/duplicate UI remain.','1, 8, 36'),
 (3,'PARTIAL','Local reference and complete mapped stage art; provisional anatomy/density and incomplete corpse/VIP art.','2–7, 9, 17, 30'),
 (4,'PARTIAL','Nine sizes/multiple ownership; no dry tanks, dimensions or displacement.','14, 21'),
 (5,'FAIL','New tanks include scenery/equipment/water rather than the required dry construction loop.','14'),
 (6,'PARTIAL','XP, discovery, quests/showcase exist; dedicated prestige/business reputation incomplete.','27, 29'),
 (7,'PARTIAL','Rock/sand visual ownership and editing work; no mass, substrate biology or maintenance.','11–13'),
 (8,'PARTIAL','Coral inspector, growth/stress/supports work; bleach/decomposition/taxon and transfer gaps.','9, 10, 17, 32'),
 (9,'PARTIAL','Persistent fish/health/aging/death exist; nutrition, respiratory profiles and staged decay incomplete.','16, 17'),
 (10,'PARTIAL','School/seek/rest/hide/encounter states work; no rock collision, dimensions or complete territories/courtship.','6, 18'),
 (11,'PARTIAL','Core equipment effects/durability/service work; sensors/test history and probability/service interval profiles incomplete.','23'),
 (12,'PARTIAL','Central simplified water/nitrogen/mixing work; dead coral/substrate/live-rock nutrient processes absent.','15, 17'),
 (13,'PARTIAL','Saved Auto/On/Off visually brighten tank; no algae/heat/spectrum model or full dawn/dusk behavior.','22'),
 (14,'PARTIAL','Seven foods, visible consumption and auto-feed; no live/coral foods or complete persistent nutrition/freshness.','19'),
 (15,'PARTIAL','Broods, viability/lineage/continuous inheritance work; designer pattern genetics/courtship incomplete.','20'),
 (16,'PARTIAL','Bounded condition/gene/demand value and load; no required rarity/variety or full habitat asset valuation.','21, 28'),
 (17,'PARTIAL','Bounded budgets/resale/electricity/rewards; no full current 30/90/365-day balance matrix/cooldowns.','28'),
 (18,'PARTIAL','Destination invariants and atomic shared modal work; quantity handler/details/ledger completeness incomplete.','24–26'),
 (19,'PARTIAL','Level/night/containment/stock/inspection fictional foundation; no dealer reputation/full rotating roster.','27'),
 (20,'PARTIAL','19 quests/three achievements; relocation quest bug and missing full construction/prestige coverage.','29'),
 (21,'PARTIAL','Five preview-tier names and disabled payments; required illustrated tier panels absent.','30'),
 (22,'PARTIAL','Six local season values and persistent lantern; dedicated event chains/art are incomplete.','31'),
 (23,'PARTIAL','Rock/sand/coral edits saved; support/mount/growth/transfer/boundary validation defects.','10–12, 32'),
 (24,'PARTIAL','Versioned save/recovery/migration/offline cap work; coral schema/geometry disagreement and absent biological fields.','33'),
 (25,'PARTIAL','Fixed ticks, atlases/caches/selected rendering; no presets/background cache/spatial grouping/long soak.','34'),
 (26,'PARTIAL','Locked palette, dialog/responsive UI and inspectors; missing full inventory/setup/scaling/accessibility review.','24, 32'),
 (27,'PARTIAL','Current regressions pass but boundary audit finds gaps; historical life-stage harness is stale.','G executed tests'),
 (28,'PARTIAL','Integrated roadmap exists; its later phases and foundational dry setup are unfinished.','14, 30, 31, 34, 36'),
 (29,'PARTIAL','Offline namespaced modules/data/assets/tests organized; duplicate compressed modules impede maintenance.','1, 36'),
 (30,'PARTIAL','All required docs/31 headings/latest named rules present; conflicting historical wording persists.','36'),
 (31,'PARTIAL','Playable vertical slice delivered; full target completion cannot be declared. Audit stop overrides development instructions.','A–H')]

def main():
    rows=classify();counts=collections.Counter(r['status'] for r in rows);applicable=len(rows)-counts['NOT APPLICABLE']
    metrics='| Status | Checks |\n|---|---:|\n'+'\n'.join(f'| {s} | {counts[s]} |' for s in ['PASS','PARTIAL','FAIL','MISSING','NOT TESTED','NOT APPLICABLE'])
    metrics+=f'\n| Total feature checks | {len(rows)} |\n| Applicable checks | {applicable} |\n| Verified pass percentage | **{counts["PASS"]}/{applicable} = {counts["PASS"]*100/applicable:.2f}%** |'
    inventory='''| Inventory measure | Count |
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
| DATA ONLY / PLANNED entries | 0 / 3 |'''
    collection=embedded('js/clownfish-collection-data.js')
    species='| Clownfish common name | Scientific name | Runtime ID | Availability |\n|---|---|---|---|\n'
    species+='\n'.join(f'| {s["name"]} | *{s["scientificName"]}* | `{s["id"]}` | '+('Purchase-held; provisional specialist care' if not s['purchaseVerified'] else 'Catalog/store; admission rules apply')+' |' for s in collection['species'])
    designers='| Designer phenotype | Biological base | Stage presentation |\n|---|---|---|\n'
    names={s['id']:s['scientificName'] for s in collection['species']}
    designers+='\n'.join(f'| {v["name"]} | *{names[v["speciesId"]]}* | Eight slots; shared base egg/larva; provisional approval |' for v in collection['varieties'])
    integrity=json.loads((ROOT/'tests/audit-evidence/static-integrity.json').read_text())
    integrity_summary=f'{integrity["bankRecords"]} atlas records valid; no missing literal resources; 42 baseline files unchanged'
    perf='| Measured synthetic workload | Chrome | Edge |\n|---|---:|---:|\n'
    chrome=json.loads((ROOT/'tests/audit-evidence/chrome-project-audit.json').read_text())
    edge=json.loads((ROOT/'tests/audit-evidence/edge-project-audit.json').read_text())
    for label,key in [('Mean render-call cost','meanFrameMs'),('p95 render-call cost','p95FrameMs'),('Maximum sampled render-call cost','maxFrameMs'),('3,000 fish / 20 simulation steps','twentyStepsMs')]:
        perf+=f'| {label} | {chrome["performance"][key]:.2f} ms | {edge["performance"][key]:.2f} ms |\n'
    perf+=f'| Short-run JS heap used snapshot | {chrome["performanceMetrics"]["JSHeapUsedSize"]/1048576:.2f} MiB | {edge["performanceMetrics"]["JSHeapUsedSize"]/1048576:.2f} MiB |'
    evidence='\n\n'.join(f'<a id="{id.lower()}"></a>\n\n**{id} — {label} ({kind}).** {description}' for id,kind,label,description in EVIDENCE)
    trace='| MDP section | Assessment | Actual implementation comparison | Checklist sections |\n|---|---|---|---|\n'
    mdp=(ROOT/'MASTER_DEVELOPMENT_PROMPT.md').read_text(encoding='utf8').splitlines()
    headings={int(line[2:].split('.')[0]):line[2:] for line in mdp if line.startswith('# ') and line[2:].split('.')[0].isdigit()}
    trace+='\n'.join(f'| [{headings[n]}](MASTER_DEVELOPMENT_PROMPT.md) | {status} | {note} | {checks} |' for n,status,note,checks in TRACE)
    matrix=[]
    for section,items in __import__('itertools').groupby(rows,key=lambda r:r['section']):
        matrix.append(f'#### {section}\n\n| Check | Original requirement | Status | Finding | Evidence |\n|---|---|---|---|---|')
        for row in items:
            requirement=row['item'].replace('|','\\|').replace('�','–')
            links='; '.join(f'[{e}](#{e.lower()})' for e in row['evidence'])
            matrix.append(f'| {row["check"]} | {requirement} | **{row["status"]}** | {row["finding"]} | {links} |')
        matrix.append('')
    report=INTRO.replace('{metrics}',metrics).replace('{inventory}',inventory).replace('{clown_inventory}',species).replace('{designer_inventory}',designers).replace('{integrity_summary}',integrity_summary).replace('{performance}',perf).replace('{evidence_index}',evidence).replace('{mdp_trace}',trace).replace('{checklist}','\n'.join(matrix))
    (ROOT/'FULL_PROJECT_AUDIT.md').write_text(report,encoding='utf8')
    data={'date':'2026-10-12','counts':dict(counts),'total':len(rows),'applicable':applicable,'verifiedPassPercentage':round(counts['PASS']*100/applicable,2),'checks':rows}
    (ROOT/'tests/audit-evidence/checklist-classifications.json').write_text(json.dumps(data,indent=2),encoding='utf8')
    print(json.dumps({k:v for k,v in data.items() if k!='checks'}))

if __name__=='__main__':main()
