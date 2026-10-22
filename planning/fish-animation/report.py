"""Generate honest per-species coverage from actual browser evidence."""
from pathlib import Path
import json
r=Path(__file__).resolve().parents[2]
before=json.loads((r/'tests/fish-animation-evidence/before.json').read_text(encoding='utf8'))
chrome=json.loads((r/'tests/fish-animation-evidence/chrome-results.json').read_text(encoding='utf8'))
edge=json.loads((r/'tests/fish-animation-evidence/edge-results.json').read_text(encoding='utf8'))
registry=json.loads((r/'assets/animation/fish-registry.json').read_text(encoding='utf8'))
assert chrome['failed']==edge['failed']==0
text='''# Fish animation audit and runtime upgrade — v4.0.3

Audited **94 registered marine fish** against CURRENT_LIVESTOCK_CATALOG.md, runtime AL.Data.species and the actual renderer/loaded sprite manifests. This includes five acquisition-held clownfish and one existing fictional species; it does not unlock them or count designer varieties as species. The runtime contains 89 marine fish without those five explicit acquisition holds. Existing freshwater remains locked.

## Coverage classification

| Classification | Before | After |
|---|---:|---:|
| A — fully authored/working across the requested lifecycle/action scope | 0 | 0 |
| B — partial, with known art/action/anatomy limitations | 31 | 94 |
| C — static living poses moved positionally | 63 | 0 |
| D — missing/broken playable source artwork | 0 | 0 |
| E — reference-only subjects outside the runtime roster (separate count) | 5 | 5 |

**94 fish improved.** Thirty-one already had four-frame adult swim cycles, including the approved natural Ocellaris benchmark; those cycles are preserved without procedural warping. Sixty-three had one authored living pose per stage and no dedicated adult swim-cycle keyframes. All 94 now have runtime-supported idle/travel/faster beats, single-eye side-profile turns, existing feeding/rest/health/reproductive-state responses, and frozen persistent death presentation. Three life stages are tested. No fish is falsely labeled completely authored or anatomically approved.

**Manual artwork remains for all 94 if completing the full requested authored action/turn/anatomy standard:** 63 need dedicated adult cycle keyframes; all need some combination of independent opposite-side/yaw poses, concealed pectoral clean plates, species-specific feeding/spawning/mouth details and verified early-stage anatomy. Existing adult clownfish cycles cover tail/pectoral poses but do not establish all these missing states. Procedural outer-fin motion is visible and preserves the source; it cannot reconstruct pixels never painted. AI image generation alone would not verify anatomy or identical individual markings across those new views; no generic placeholder/recolored fish was substituted. This delivery completes the feasible runtime/art-registration work and explicitly inventories remaining authored-art work.

## Confirmed findings and changes

- Actual precedence previously selected static AL.ExpansionArt/LifeStages poses for 63 marine fish. Metadata contained stage/death cells, not animation cycles. Their world positions changed, while living tail/fin artwork did not.
- Added explicit species-to-motion profiles in assets/animation/fish-registry.json Profiles distinguish clownfish, substrate/hover gobies, blennies, rock-associated basslets, cruisers, wrasses, cardinalfish, water-column schoolers, extended-fin hoverers, dartfish, angels, butterflies, filefish, boxfish and the existing fictional fish. These are artistic calibrations; they do not certify all species' biomechanics or change AI/diets.
- Preserved all existing PNGs, source dimensions, silhouettes, inherited patterns and adult clownfish cycles. The shared rig bends sampled tail columns by a few integer pixels about fixed roots and flexes authored outer fin pixels around a fixed body core. Head/eye pixels remain unchanged between procedural phases. Four-pixel transparent padding and nearest-neighbor sampling avoid new clipping/blur.
- Registered **75 previously absent living eye anchors** (25 v2.9 fish × three stages). Corrected the Blue Assessor baby eye anchor: the raw source faces left correctly, but its old eye coordinate pointed at the tail after normalization. Original source imagery and native-facing normalization are preserved. Both directions are tested from actual sampled eye pixels; no second eye is synthesized.
- A juvenile Orange-Spotted Filefish source contained an unattached 159-pixel duplicate fin island below the fish. A narrow, recorded runtime exclusion removes that island; the original PNG is retained unchanged. It is not a new painted fin.
- Banggai's historical yolk-sac early pose is not used for its released early-stage display. The renderer selects its existing developed-juvenile source, respecting the existing paternal mouthbrooding lifecycle. It does not create an external egg or change release/growth rules.
- Feeding motion requires actual Eat state and respects the existing diet. Nest/guard/courtship/spawn/mouthbrood labels come from existing simulation states; tests of those presentation labels on other species are synthetic interface tests, not a claim that held reproductive strategies are implemented. Weak/injured motion differs from respiratory activity; symptoms do not become a diagnosis. Dead fish keep authored death poses, stop all live articulation and retain existing sinking/mortality records.


### Actual in-tank scale and early fin-layer gaps

All 282 fish/stage combinations are also checked at the renderer's actual size, including the individual's size gene. The core guard now scales down to one scene pixel instead of covering all tiny fin-fold pixels. Separate outer-fin motion remains unsupported by four retained early-stage sources at the relevant size: Hi-fin Red-banded Goby (caudal-fold-only source), Whitebonnet Clownfish, Lubbock's Fairy Wrasse and Redspotted Blenny (outer fin pixels unresolved below 32 scene pixels). The renderer retains caudal fin/fold motion and protects body/yolk pixels; it does not manufacture paired fins. These are explicit art gaps, not passed independent-fin animation requirements. Larger applicable outer-fin poses and every stage's tail/caudal fold are tested. All four species remain class B pending dedicated early-fin artwork.

## Per-species coverage

All rows have a dedicated stage/state sheet, authored baby/juvenile/adult source imagery (Banggai early uses developed juvenile), dead-state art and a shared procedural rig where appropriate. Egg/reference cells are not counted as proof of externally laid eggs. Existing anatomy/art-review holds remain. Every row is tested for idle/faster timing, source tail and applicable outer-fin changes (the four early source gaps above use caudal-fold motion only), head/core and sampled eye stability in both directions, fixed death, transparent bounds, renderer-owned clocks and cached reuse. Actual 94-species rendering and individual hit detection are also tested. Side profiles are mirrored; independent asymmetric opposite-side anatomy remains unverified. No new multilayer pectoral clean plate is claimed.

| Common name / scientific name | Stable runtime ID / source sheet | Before → after / adult cycle | Profile / work completed | Remaining artwork / test status |
|---|---|---|---|---|
'''
for row in before:
 id=row['id'];meta=row.get('art') or {};atlas=meta.get('atlas')
 if not atlas or not atlas.startswith('assets/'):
  folder='expansion-v29' if id in [p['id'] for p in json.loads((r/'assets/expansion-v29/registry.json').read_text(encoding='utf8'))['records']] else 'expansion-v27'
  candidate=f'assets/{folder}/{id}/atlas-v1.png'
  atlas=candidate if (r/candidate).exists() else f'assets/livestock/life-stages/fish/{id}/atlas-v1.png'
 assert (r/atlas).exists(),atlas
 checks=[x for x in chrome['checks'] if x['name'].startswith(id+':') or x['name'].startswith(id+' ')]
 assert checks and all(x['pass'] for x in checks)
 family=registry['species'][id]['family'];native=row['adultFrames']>1
 source=f'[`{id}`]({atlas})';science=row.get('scientificName') or 'Existing fictional species; no biological taxon'
 if id=='clown':source+='; [actual natural-adult benchmark](assets/livestock/fish/clownfish/clownfish-benchmark-v1-128.png)'
 hold='; acquisition held' if row.get('purchaseVerified') is False else ''
 cycle='4 authored adult frames; early rig' if native else '1 living pose/stage + rig; no authored adult cycle'
 notes='Independent turns/actions, pectoral plate, early anatomy review'
 if id=='blue-assessor':notes+='; early eye repaired'
 if id=='orange-spotted-filefish':notes+='; stray juvenile fin masked'
 if id in ['hi-fin-red-banded-goby','amphiprion-leucokranos','lubbocks-fairy-wrasse','redspotted-blenny']:notes+='; tiny early outer-fin layer unresolved, caudal fold only'
 if id=='banggai':notes+='; early released-juvenile source corrected'
 text+=f'| {row["name"]}<br>*{science}*{hold} | {source} | {"B" if native else "C"} → **B**<br>{cycle} | {registry["families"][family]["name"]}; three-stage articulation/state timing | {notes}. **{len(checks)} species checks passed** in each browser. |\n'
text+='''
## Reference-only exclusions — category E

Blue Tang (`blue-tang`), Dogface Puffer (`dogface-puffer`), Emperor Angelfish (`emperor-angelfish`), Niger Triggerfish (`niger-triggerfish`) and Red Lionfish (`red-lionfish`) have old reference/review artwork but are absent from playable AL.Data.species. They are not added, animated as gameplay residents, or counted among the 94. Ocellaris designer varieties retain their separate variety IDs and all existing inheritance/acquisition holds; they do not inflate species totals.

## Actual verification

'''
for name,result in [('Chrome',chrome),('Edge',edge)]:
 text+=f'**{name}: {result["passed"]:,} checks passed; {result["failed"]} failed.** All 94 fish × three stages × both directions have source/fin/eye/death coverage. Original 10 specifically requested species are included, including Chalk Bass.\n\n'
 text+='| Fish count | Warm mean draw time on this QA PC |\n|---|---:|\n'
 for perf in result['performance']:text+=f'| {perf["fish"]} | {perf["meanMilliseconds"]:.2f} ms |\n'
 text+='\n'
text+='''Additional completed checks: all 94 render without mutating saves; all 94 retain correct individual hit IDs during playback; all designer varieties retain their selected source identity; actual canvas selection expires after three real seconds while its inspector stays open; a real browser reload preserves genetics/IDs; 94-fish save/parse works; different rendering rates followed by the same simulated interval yield equal entire game states (receipt wall time controlled in the fixture); offscreen fish skip sprite work; freshwater output/hitboxes match the pre-upgrade renderer pixel-for-pixel; no HTTP/HTTPS requests or uncaught browser errors; review page exercises all fish/stages without changing local saves. The 768-entry pose cache stays bounded. Timings measure warm canvas draw calls on this Windows PC, not end-to-end FPS across all hardware. Full physiological validity of every early-stage illustration, independent side views, and authored action clean plates are **not verified/completed**.

Initial checks exposed missing/incorrect eye registration and the existing detached source fin, which were corrected. A deterministic simulation comparison initially differed only in finance receipt `realTime`; controlling the test clock proved biological/RNG/account values remain identical. The Edge click test initially ran without a guaranteed visible viewport; the final test fixes its viewport, closes other panels and clicks the actual canvas. These fixes do not alter game saves or bypass game selection logic. Final failed count above comes from the completed suites.

Evidence: `tests/fish-animation-evidence/{chrome,edge}-results.json`, ten stage/direction contact sheets per browser, source-eye registration sheets, source-art defect inspection and actual inspector/review screenshots. The full built Pages regression additionally runs the per-species animation model checks alongside the previous gameplay/save/diving suites; definitive release totals and byte/ZIP verification are in `tests/fish-animation-evidence/release-validation.json` after final packaging.

## Files changed and release

- New runtime: `js/fish-animation.js`, generated `js/fish-animation-data.js`, `assets/animation/fish-registry.json`.
- Integrated presentation: `js/render.js`, `js/expansion-art.js`, `index.html`.
- Isolated review: `fish-animation-review.html`, `js/fish-animation-review.js`.
- Build/tests: `build.py`, `tests/browser_qa.py`, `tests/pages_qa.py`, `tests/package.py`, `tests/fish_animation_qa.py`, `tests/fish_animation_checks.js`, `tests/verify_fish_animation_release.py`.
- Documentation: this audit, `FISH_ANIMATION_SYSTEM.md`, `MASTER_DEVELOPMENT_PROMPT.md` §3.14, `PROJECT_CONTINUITY_SOURCE.md`, `ART_DIRECTION.md`, `DEVELOPMENT_STATUS.md`, `CURRENT_LIVESTOCK_CATALOG.md`, `UI_SPECIFICATION.md`, `README.md`, `GAME_DESIGN.md`, `TEST_REPORT.md`, `GITHUB_PAGES_BUILD_REPORT.md`.
- Planning/baselines/evidence: `planning/fish-animation/`, `tests/fish-animation-evidence/`.
- Current generated deployment/source packages: `DIST/`, `AquariumLife-GitHub-Pages.zip`, `AquariumLife-v0.1.zip`.

The simulation, feeding, disease, autonomous reproduction, genetics/inheritance, water, mortality, economy, save schema, 20-minute day and all original native art bytes remain unchanged. Animation is local/offline and has no persisted animation fields. Freshwater acquisition remains locked. Full printable continuity embeds the current 31-section master; binary PDF regeneration remains pending. No 3D renderer or new species is introduced. **The runtime improvements and audit are delivered; the detailed authored-art gaps above remain partial, not falsely complete.**
'''
(r/'FISH_ANIMATION_AUDIT.md').write_text(text,encoding='utf8')
print('Per-species audit written: 94 improved, 0 fully authored, 94 partial, 0 static, 0 broken, 5 reference-only')
