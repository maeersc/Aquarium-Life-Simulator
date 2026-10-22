"""Consolidate the authorized October 12 milestone into existing project documents."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
def read(name):return (ROOT/name).read_text(encoding='utf-8')
def write(name,text):(ROOT/name).write_text(text,encoding='utf-8')
if 'VERSION 2.7' in read('MASTER_DEVELOPMENT_PROMPT.md'):
    print('The one-time milestone consolidation is already applied.')
    raise SystemExit(0)
c=json.loads(read('assets/livestock/fish/clownfish/collection.json'))
species=c['species'];varieties=c['varieties']

p=read('MASTER_DEVELOPMENT_PROMPT.md').replace('VERSION 2.6','VERSION 2.7')
p=re.sub(r'### Revision:.*', '### Revision: 2.7 consolidates the dedicated clownfish collection, saltwater scope lock, physical coral mounting, shared store redesign and permanent destination-aquarium rule.',p,count=1)
pos=p.index('\n---\n\n# 3.')
p=p[:pos]+'''
## 2.5 Permanent Saltwater Development Scope

Current and upcoming livestock development is saltwater only: marine fish, corals, benthic fish, invertebrates, eggs, specialty livestock and fictional marine specimens. Preserve existing freshwater livestock definitions, artwork, health, care, growth, diet, behavior and reproduction. Shared store, navigation, inventory, save and compatibility infrastructure may change when required, with freshwater regressions checked. Existing freshwater purchases and the pre-existing fictional Glassfang eel remain available; do not add freshwater species or silently revise their biology. Freshwater remains a long-term design category, not an authorized current expansion.
'''+p[pos:]
p=p.replace('## 3.9 Art Development Update v1.1 - Active Scope','## 3.9 Art Development Update v1.1 - Preserved Prior Delivery').replace('## 3.10 Livestock Life-Stage Art Update v1.0 - Current Priority','## 3.10 Permanent Livestock Life-Stage Art Standard')
p=p.replace('This update supersedes the completed art 1.1 delivery scope for current work. Development remains art only. Do not advance economy, quests, black market, water chemistry, VIP or progression until the user is satisfied with livestock art.','The full life-stage standard survives the later dedicated clownfish and shared-store milestone in section 3.11. Earlier approved art and historical sources remain preserved. Do not infer authorization for unrelated gameplay expansion from an art update.')
p=p.replace('Current audited scope is 22 playable fish (including four benthic fish) and five implemented coral categories. Five additional fish with adult art remain ART ONLY.','The earlier audit contained 22 fish and five coral categories. The current dedicated collection audit is recorded in section 3.11 and CURRENT_LIVESTOCK_CATALOG.md. Five additional marine adult-art studies remain ART ONLY.')
p=p.replace('**Stop after delivery for user visual review.** After this update is completed and reviewed, the next intended task is **clownfish-only refinement** (visual polish, life-stage refinement, animation polish, final benchmark quality). Do not begin that follow-up yet.','**Stop after each authorized art milestone for user visual review.** The subsequent dedicated clownfish instruction authorizes section 3.11; no broader expansion follows automatically.')
pos=p.index('\n---\n\n# 4.')
p=p[:pos]+'''
## 3.11 Dedicated Clownfish Collection and Art Review

The dedicated exception contains the following 31 catalogued scientific names. Verify accepted names and synonyms with FishBase and primary taxonomic sources. A listed name does not resolve every hybrid-origin dispute; disclose the uncertainty for A. leucokranos and A. thiellei. Preserve gameplay ID `clown` for A. ocellaris and do not duplicate Premnas biaculeatus as a separate species.

'''+', '.join(e['scientificName'] for e in species)+'''.

Designer varieties are linked phenotypes, not extra biological species:

'''+', '.join(e['name']+' ('+e['scientificName']+')' for e in varieties)+'''.

Each collection entry requires Egg, Baby, Juvenile and Adult alive/dead support. Genuinely indistinguishable designer eggs and larvae may share their base-species art through explicit metadata. Juvenile pigmentation and fin development must differ meaningfully from adults. Build a four-pose adult swimming cycle with stable head-local eye pixels, complete fins, nearest-neighbor scaling, restored canvas transforms and documented mirrored side views. Preserve original files and the approved assigned adult Ocellaris benchmark until the user approves a replacement. Never automatically mark new art approved.

Species profiles include identity, adult length and SL/TL measurement, difficulty, tank volume/footprint, temperature, pH, salinity, diet, territorial behavior, pair structure, reef interaction, reproduction, lifespan confidence, host requirements and verification sources. Use Easy, Moderate, Challenging, Difficult, Expert or Extreme for husbandry; designer rarity and price are separate. Separate sourced facts, genus-level guidance and conservative game calibration. Missing specialist care information means a visible purchase hold, not an invented verified profile. Designer genetics must remain linked to the base species; do not fabricate exact inheritance.

Audit every existing livestock entry without hiding absent art or adding planned examples to playable totals. The offline collection gallery needs species/designer views, search, base-species filter, all stages and deaths, direction, play/pause/frame step, zoom/backgrounds, actual gameplay scale, original/revised/reference comparison, taxonomy/care/art status and separately saved review notes. Include a global livestock audit and a coral placement test scene. The current audit has 52 fish records (including four benthic fish) and five coral categories; five specialist clownfish profiles remain purchase-held. Five earlier fish studies remain ART ONLY and three named proposals PLANNED. **Stop at the completed review gallery for user review.**
'''+p[pos:]
p=p.replace('Use image-based cards and detailed inspectors.\n\nShow compatibility warnings before purchase.','''Use the shared centered store modal: desktop width 900–1100 pixels and height 75–85vh, visible aquarium backdrop, fixed header/navigation/X and internal product scrolling. Fit smaller screens without off-screen controls or page scrolling. Trap focus in the active dialog; Escape closes higher-priority details first, otherwise the store. Restore focus to the Store opener. Prevent duplicate modals and background interactions.

Exactly three main tabs: Saltwater, Freshwater and Black Market. Start with Saltwater unless the current shopping session already chose a tab. Saltwater has Fish, Bottom Feeders, Corals, Rocks & Environment, Sand & Substrate, Equipment, Food & Supplies. Freshwater has the same seven categories with Plants instead of Corals. Black Market has Fish, Bottom Feeders, Corals, Rocks & Environment, Eggs & Specimens, Special Equipment. An empty freshwater category says exactly “Freshwater content is coming soon.” Preserve the locked near-black/slate palette and original UI.

Use actual existing product definitions, prices, stock and local artwork. Show habitat, care difficulty, designer/base identity and compatibility before purchase. Rocks/sand include Fiji, Caribbean and Hawaiian collections and 0–5 inch depth. Do not introduce fake products to fill empty categories. Recalculate equipment cost for the chosen destination. The existing level-4/discovery/20:00–04:00/containment/stock restrictions apply to Black Market purchases.

## 18.4 Permanent Store Destination Aquarium

1. Opening or closing the store never changes the selected aquarium.
2. Switching Saltwater, Freshwater or Black Market never changes it.
3. Display the current selected aquarium in the store header.
4. Check livestock compatibility against that aquarium at purchase time.
5. If incompatible, warn and require the player to explicitly choose an eligible owned aquarium before committing; never automatically select another.
6. Block unsafe animal placement, including harmful water conditions, predatory combinations, insufficient space and missing containment.
7. Deliver equipment, rock, sand and decorations to the explicit destination; consumable supplies go into their declared inventory.
8. Preserve selected aquarium after every completed purchase, including a new-tank purchase.
9. Closing and reopening the store retains the selection.
10. Save explicit destination choices and all placements correctly.

This rule covers all three tabs. Validate fresh state at commit, reserve stock, charge once, save once and roll back rejected transactions. Product browsing and aquarium selection are separate actions. Preserve the freshwater scope lock from section 2.5.''')
old='Provide valid-placement indicators.\n\nSave all placements.'
new='''Coral mounting must correspond to visible physical support: permitted rock tops, stable sandbed bases/plugs, or a rack securely mounted to aquarium glass. Supported forms are category-specific. Reject unsupported open water, solid-rock interiors, overlapping bases and aquarium boundaries. Show Suitable, Conditional or Invalid using text plus green/yellow/red previews, with light, flow and stinging-clearance explanations. Full silhouette and mounting footprint need clearance; pale bleaching remains distinct from death.

Store surface type, support ID, local mount coordinates, orientation and footprint. Moving rock or rack carries its attached colonies; block support removal until colonies are relocated. Sand-depth edits must preserve or reject existing supports. Migration attaches only an unambiguous valid old position; otherwise retain the owned colony with an explicit relocation-required state, never delete it or continue rendering floating coral. Repositioning and transfer require valid destination surfaces, with health and identity preserved. The offline test scene must exercise rock tops, stable sandbed, back/side-glass racks, open water, rock interiors, overlap, boundaries, support edits, camera and save/load.

Save all placements and destination selections. Implement habitat chemistry only when separately authorized; this milestone's sand visuals do not claim new substrate chemistry.'''
p=p.replace(old,new)
p=p.replace('- Coral states.','- Coral states, physical attachment support IDs/local coordinates and relocation-required ownership.\n- Selected aquarium and explicit store destination choices.\n- Designer variety linked to its biological species.',1)
p=p.replace('## 15.4 Genetics','Marine clownfish are protandrous: maintain one established female and a subordinate male. Established females never revert to male, including during pairing, replacement and save/load. Different clownfish species must not be automatically mixed into one territory.\n\n## 15.4 Genetics',1)
p=p.replace('11. Current livestock content expansion focuses on saltwater.','11. Current and upcoming livestock development is saltwater only; protect existing freshwater content per section 2.5.')
p=p.replace('12. Freshwater remains in the long-term design.','12. Freshwater remains in the long-term design; shared infrastructure changes require freshwater regression checks.')
p=p.replace('31. All updates must preserve the single consolidated MDP and avoid repeated rules.','31. All updates must preserve this consolidated 31-section MDP; permanent store-destination invariants are in section 18.4, mounting in 23.1 and art review in 3.11.')
p=p.replace('## 27.7 UI and VIP','Store destination invariants require regression checks across all three tabs, purchase holds, alternative eligibility, stale water conditions, repeated submissions, explicit product destinations, JSON round trips, focus/Escape/backdrop behavior and responsive sizes. Validate every clownfish entry, shared early-stage mapping, eye anchoring, left/right transforms, animation frames and protected freshwater baselines.\n\n## 27.7 UI and VIP')
write('MASTER_DEVELOPMENT_PROMPT.md',p)

old=read('CURRENT_LIVESTOCK_CATALOG.md');start=old.index('## Implemented entries');oldrows=old[start:];oldrows='\n'.join(line for line in oldrows.splitlines() if not line.startswith('| Ocellaris clownfish |'))
rows=[]
for e in species:
 rows.append(f"| {e['name']} | {e['scientificName']} | `{e['id']}` | fish | IMPLEMENTED{'; purchase hold' if not e['purchaseVerified'] else ''} | Egg/Baby/Juvenile/Adult, alive + dead | None in mapped static stages | 8 stages + 4 adult swim poses | [{e['id']} atlas]({e['folder']}/atlas-v1.png) | Provisional; head-registered eyes; mirrored sides | {e['taxonomyStatus']}; {e['careVerification']} |")
oldrows=oldrows.replace('\n## Other audit findings','\n'+'\n'.join(rows)+'\n\n## Other audit findings') if '\n## Other audit findings' in oldrows else oldrows+'\n\n'+'\n'.join(rows)
oldrows=oldrows.replace('The next planned task, only after this update is reviewed, is clownfish-only refinement.','The dedicated clownfish collection is now delivered for review; broader expansion remains gated.')
header='''# Current livestock catalog — 2026-10-12

Audit sources: actual species definitions, collection metadata, render banks and existing asset metadata. Six freshwater plants are flora, excluded from animal-livestock totals.

- Fish category: 48 implemented records; bottom/benthic category: 4 (cory, pleco, watchman, blenny). Combined fish: 52, including 11 protected freshwater and 41 marine records.
- Corals: 5 implemented category-level entries; precise taxon remains unverified.
- Total implemented catalog/rendering entries: 57. Five specialist clownfish profiles are purchase-held; available catalog records are not a claim that all 57 are currently purchasable.
- Dedicated clownfish: 31 catalogued scientific names, including disputed hybrid-origin entries leucokranos and thiellei; 25 linked designer varieties add no biological species count. Existing `clown` ID is preserved.
- All 57 implemented entries map the eight required life-stage/state views. New collection adds 56 sheets, 572 uniquely packed poses (31 × 12 + 25 × 8); 448 stage/state presentations include shared designer egg/larva poses.
- Five previous marine fish remain ART ONLY with adult swim art but missing early/dead sets. DATA ONLY: 0. Three fictional proposals remain PLANNED. The global gallery shows these limits explicitly.
- All new art remains Provisional pending user review. Existing freshwater art/source files are byte-identical.

'''
write('CURRENT_LIVESTOCK_CATALOG.md',header+oldrows+'\n\n## Designer varieties (separate from species counts)\n\n| Variety | Base scientific species | Art and metadata | Status |\n|---|---|---|---|\n'+'\n'.join(f"| {e['name']} | {e['scientificName']} (`{e['speciesId']}`) | [{e['id']}]({e['folder']}/metadata-v1.json) | {e['verificationStatus']}; early art shared |" for e in varieties)+'\n')

report='''# Clownfish collection and shared store delivery — 2026-10-12

Implemented the dedicated clownfish collection and the authorized shared store/mounting milestone. The full long-term master design is still incomplete. Open [clownfish-review.html](clownfish-review.html), [coral-placement-review.html](coral-placement-review.html), or the playable [index.html](index.html) directly from disk.

## Store behavior

The centered store keeps the aquarium visible behind a modal with fixed controls and scrolling cards. Exactly three main tabs and 7/7/6 subcategories use actual inventory. The selected aquarium appears in the header; opening, closing, changing product tabs and purchasing never automatically switch it. Explicit destination changes are saved. Incompatible animal purchases warn, disable commit and let the player explicitly choose an eligible owned aquarium. Fresh conditions are rechecked at commit; failed purchases and repeated submissions cannot spend twice. Supplies use shared inventory; equipment, rock, sand and decoration use the chosen aquarium. Equipment pricing follows destination volume. Existing Black Market access and containment restrictions remain.

## Coral mounting

Five existing coral categories now attach to permitted real rock tops, stable sandbed bases or mounted glass racks. Alpha collision geometry comes from the actual twelve rock images. Reject open water, solid interiors, boundary clearance and overlapping bases; care and LPS clearance produce explanatory conditional warnings. Save support IDs/local coordinates, carry colonies when supports move, block occupied support removal and revalidate sand-depth edits. Unsupported old placements retain ownership with a relocation notice. The isolated test scene exercises these actions without touching player storage. Click a rock or rack in gameplay to inspect/edit it. Coral inspectors retain Overview/Care tabs.

The three sand looks and 0–5 inch depth are saved visual habitat choices. New chemistry, displaced water-volume calculations, substrate fauna and maturation have not been added. Starter scenery still exists; completely dry construction remains future work.

## Clownfish and art

31 catalogued scientific names and 25 designer phenotypes, linked to base species. Existing Ocellaris ID `clown`, approved adult animation and historical sources are preserved. New original sources include 56 sheets plus two revised sheets. They pack 572 unique native 192 × 160 poses: 372 species poses and 200 designer poses. Designer eggs/larvae share base art explicitly; all 56 entries show eight living/dead stage views and four adult swim poses. All 57 implemented livestock catalog entries retain mapped full-stage support. Five earlier marine art studies remain art-only and disclose missing stages.

Engineering packing preserves transparency, complete fins and source files. Two fin-heavy sheets need connected-alpha component extraction because fin projections share column ranges while the animals remain physically separate. Dark-face eye coordinates and one closed juvenile eye are registered manually from source pixels. Other pupils use tighter component detection; adult cycles share canonical eye pixels sampled from the artist's sprite. Presentation restores transforms and mirrors the whole animal. No dedicated front-facing turns or complete carcass-decay animation is claimed. Dead poses are authored static states; existing mortality/pollution remains in the simulation.

The review gallery separates biological names/designer phenotypes, supports search/base filters, all stages/states, directions, frame controls, enlarged and actual-scale views, original/reference comparisons, care/sources, global audit and separately stored review notes. All new art is Provisional; only the user can approve it. Nine diagnostic contact sheets were inspected for packing, pose consistency and eye registration; precise anatomy and asymmetric pattern fidelity remain review subjects.

## Verification and boundaries

Taxonomy list/length measurements: [FishBase genus list](https://www.fishbase.org/identification/SpeciesList.php?genus=Amphiprion). Accepted names/synonyms: [WoRMS genus records](https://www.marinespecies.org/aphia.php?p=taxlist&tName=Amphiprion). Group husbandry and protandrous pair structure: [OATA clownfish care](https://ornamentalfish.org/wp-content/uploads/Clownfish-Sept-2022.pdf). Historical host/identity context: [Fautin and Allen field guide](https://www.meerwasserforum.info/file-download/95760/). Named breeder phenotypes: [ORA clownfish catalog](https://www.orafarm.com/products/fish/clownfish/); entry-specific links are retained in collection.json.

A listed name is not proof that hybrid origin is resolved: leucokranos and thiellei remain explicitly uncertain. Those two plus mccullochi, latezonatus and maohiensis are purchase-held until specialist care is verified. Species-specific lifespan is not verified; existing life scaling and minimum footprint recommendations are labeled game calibration/policy. Host lists are not invented. Mocha Storm, Mocha Ocellaris and Onyx appearances remain provisionally attributed. Designer genotype/inheritance is not modeled; base-species care and genetics stay authoritative. Established clownfish females no longer revert to male.

Freshwater definitions and 144 protected asset/source files are byte-identical. The simulation differs only in the marked marine clownfish pairing block; freshwater diet, care, growth, behavior and reproduction code is preserved. Shared safer purchasing changes are authorized and tested.

## Validation

Chrome and Edge each pass 68 current system checks, shared-store regressions and the complete collection/gallery/attachment checks. Machine-readable counts and results are in tests/*-store-results.json and tests/*-clownfish-results.json. Tests use isolated browser profiles, real file:// URLs and disabled network; no gameplay HTTP/HTTPS requests. Collection matrices cover 1,792 stage/size directional cases per browser, eyes at 25/52/73/117 pixels, transform restoration, exact mirroring, shared early pixels, four distinct swim frames, female invariants and duplicate-charge protection. Store tests cover all three tabs, chosen destinations, unsafe/stale purchases, modal focus/Escape, save reload, habitat actions and widths 1440/1024/760/390.

The original UI automation reflects an earlier full-page store and is retained as a historical fixture. Current default automation runs the current simulation and modal-store tests; --clownfish runs the new collection checks. Firefox remains unverified in this environment.

## Delivery gate

The consolidated MDP is revision 2.7 with its original 31 major sections, integrated scope/store/mounting/collection rules. This milestone stops for the user's visual review. No broader fish/coral/bottom-feeder expansion is begun. Portable ZIP retains local game, galleries, sources, metadata, prompts, documentation and current test reports.
'''
write('CLOWNFISH_STORE_REPORT.md',report)

status=read('DEVELOPMENT_STATUS.md');status=status.replace('# Development status — 2026-10-11','# Development status — 2026-10-12',1)
status=status.replace('## Current phase: livestock life-stage art update delivered for review','## Previous phase: livestock life-stage art update delivered for review',1)
pos=status.index('## Previous phase: livestock life-stage')
status=status[:pos]+'''## Current phase: clownfish collection and shared store delivered for review

The active consolidated MDP is revision 2.7. Added 30 marine clownfish records while preserving existing Ocellaris ID, yielding 52 fish plus five coral categories (57 catalog/rendering entries). Five specialist clownfish care profiles are purchase-held; 25 designer varieties stay linked to biological species. Packed all 56 collection sheets, full alive/dead life stages and adult swim cycles. Earlier approved Ocellaris and freshwater art remain preserved. The gallery includes global audit and care/taxonomy/source uncertainty.

Shared modal store now has three tabs, destination header/explicit eligible alternatives, safe atomic purchases, inventory delivery and saved destination invariants. Existing products/Black Market rules are retained. Marine coral attachments use visible rock tops, stable sandbed or mounted glass racks; support edits carry colonies and block stranding. Added saved marine rock/rack inventory and visual sand type/depth. Unsupported legacy corals keep ownership with relocation flags. No new substrate chemistry or freshwater biology was developed.

See [CLOWNFISH_STORE_REPORT.md](CLOWNFISH_STORE_REPORT.md), [clownfish-review.html](clownfish-review.html), [coral-placement-review.html](coral-placement-review.html) and [CURRENT_LIVESTOCK_CATALOG.md](CURRENT_LIVESTOCK_CATALOG.md). Current browser checks and numeric evidence are in TEST_REPORT.md. **New art remains provisional; stop for user visual review.** Broader future batches remain 25 marine fish / five corals / five marine bottom feeders only when authorized.

The historical phase audits below describe earlier releases; saltwater rock/sand/rack purchasing and mounting are now implemented as described above. Quantity-by-volume substrate economics, biological substrate maturation, displacement, complete dry setup, species-level coral profiles and full decomposition remain unfinished.

'''+status[pos:];write('DEVELOPMENT_STATUS.md',status)

art=read('ART_DIRECTION.md');pos=art.index('## Permanent life-stage');art='# Aquarium Life — art direction: clownfish collection review\n\nActive milestone: the dedicated 31-name / 25-phenotype marine collection, full stage/death mapping and four adult swim poses per entry. Existing approved adult Ocellaris, historical sources and protected freshwater assets remain intact. New art is provisional. See CLOWNFISH_STORE_REPORT.md and clownfish-review.html.\n\n'+art[pos:];art=art.replace('This phase adds no expansion batch.','The dedicated 31-name / 25-phenotype clownfish collection is an explicit user-authorized exception; broader batches remain gated.').replace('After this submission, stop for user review. The next intended art follow-up is **clownfish-only refinement**, covering visual polish, stage refinement, animation and final benchmark quality. Do not begin it before this update is reviewed.','After this submission, stop for user review. The authorized clownfish collection is now implemented; further anatomy/style refinement follows the user\'s review.');write('ART_DIRECTION.md',art)

readme=read('README.md');pos=readme.index('## Life-stage art update');readme=readme[:pos]+'''## Current collection and store update

Open [Clownfish collection review](clownfish-review.html) for 31 catalogued scientific names and 25 linked designer varieties, every living/dead life-stage view, swimming frames, original/reference comparisons and the global art audit. Open [Coral attachment study](coral-placement-review.html) to test supported mounting without modifying your aquarium save. New art remains provisional; five specialist care profiles are visible but not purchasable yet.

The Store opens over your aquarium with Saltwater/Freshwater/Black Market tabs. Its header remembers your selected aquarium. Incompatible purchases require you to choose an eligible destination explicitly; equipment and habitat items install there, supplies enter inventory. A purchase or tab change never switches aquariums automatically. Place coral on a permitted rock top, stable sandbed base or mounted rack; unsupported open water is blocked. Click a rock/rack to edit it; relocate attached corals before removing their support. Saved older unsupported colonies stay owned with a relocation notice.

See [current delivery report](CLOWNFISH_STORE_REPORT.md) and [catalog](CURRENT_LIVESTOCK_CATALOG.md). This milestone preserves freshwater livestock definitions, art and biology.

'''+readme[pos:];readme=readme.replace('## Life-stage art update','## Earlier life-stage art update',1).replace('All 27 implemented livestock entries','All 27 then-implemented livestock entries',1).replace('New art awaits your approval. No new species or unrelated mechanics were added.','That earlier stage-only update added no species; the later collection/store milestone is described above.');readme=readme.replace('20 real-world species with provisional game husbandry data; two fictional creatures;','52 fish catalog/rendering records (including two fictional creatures and five care-verification purchase holds); 25 designer phenotypes linked to base species;');readme=readme.replace('as revision 2.6','as revision 2.7').replace('purchasable sand/rock, depth and substrate biology,','substrate biology and displacement,');readme=readme.replace('python tests/browser_qa.py chrome\n','python tests/browser_qa.py chrome\npython tests/browser_qa.py chrome --clownfish\n');write('README.md',readme)

for name,title,text in [
 ('UI_SPECIFICATION.md','Current shared store and collection UI', 'Centered 1080px/84vh modal, internal scroll, visible aquarium backdrop, fixed close/header/tab controls, native focus trapping and higher-dialog-first Escape. Exactly Saltwater/Freshwater/Black Market with 7/7/6 category tabs; explicit saved destination selector and compatibility commit controls. No tab/purchase implicit aquarium selection. Empty freshwater category text: “Freshwater content is coming soon.” Local product art includes actual fish/coral/rock assets and recognizable canvas equipment/consumable/decoration forms. The collection gallery supports biological/designer/global views, all stage/death states, linked-base filters, frame controls and review notes separate from the player save. Coral mounting previews combine text with red/yellow/green outlines; mounted rack/rock inspectors support persisted edits. Palette remains locked.'),
 ('GAME_DESIGN.md','Current marine collection, mounting and destination behavior', 'Current catalog has 52 fish records plus five coral categories. 31 clownfish names include explicit hybrid uncertainty; 25 designer varieties reuse base biological species. Five specialist profiles are purchase-held. Difficulty and designer rarity are separate. Clownfish pairing never demotes an established female. Permanent shared Store destination behavior follows MDP 18.4; physical coral attachments follow 23.1. Marine rock/rack ownership and 0–5 inch visual sand depth now persist; new substrate chemistry is not implemented. Existing freshwater biological data and systems remain protected.'),
 ('ART_GENERATION_RECORD.md','October 12 collection generation', 'Built-in image generation produced 56 preserved source-v1 sheets under assets/livestock/fish/clownfish/species and designer, plus source-v2 revisions for Longfin Ocellaris and Lightning Maroon. Prompt-v1 files, collection metadata and tests/clownfish-generation-jobs.json preserve briefs. Packing exports native192x160 poses, individual stage/swim PNGs, atlases and metadata; no API keys or runtime image services. Transparent-alpha extraction, nearest-neighbor packing and existing artist-eye sampling are engineering operations. Nine diagnostic contact sheets are in assets/previews. All new artwork is provisional, and original approved Ocellaris art remains assigned.')]:
 old=read(name);first=old.find('\n');write(name,old[:first+1]+'\n## '+title+' — 2026-10-12\n\n'+text+'\n\n'+old[first+1:])

write('assets/livestock/fish/clownfish/README.md','''# Dedicated clownfish collection

31 catalogued scientific names and 25 designer phenotypes linked to base species. Sources and uncertainty are recorded in collection.json. All generated source PNGs and prompts are preserved. Sources are not silently approved. See the offline clownfish-review.html gallery and CLOWNFISH_STORE_REPORT.md.

Species atlases have twelve 192×160 frames: eight Egg/Baby/Juvenile/Adult alive/dead poses and four adult swim frames. Designer atlases have eight frames: juvenile/adult alive/dead plus four swim frames; egg/baby alive/dead explicitly resolve to the base species. JSON metadata records frame mapping, native direction, eyes, anchor, bounds and approval status. Native source facing is normalized only during frame loading. Existing approved Ocellaris adult art remains assigned to its original runtime ID.

Engineering-only packer: tests/pack_clownfish_art.py. Catalog/brief builder: tests/prepare_clownfish_collection.py. Browser review checks: tests/clownfish_qa.py and clownfish_checks.js. Diagnostic contact composition: clownfish_contacts.py. Re-running catalog scaffolding must never remove preserved source files or regenerate art without authorization.
''')
print('Updated consolidated MDP 2.7 and current milestone documents.')
