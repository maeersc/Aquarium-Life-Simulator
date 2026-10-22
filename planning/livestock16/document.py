"""Write honest coverage and consolidate the new requirement into master3.14."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[2]
path=root/'assets/animation/livestock-registry.json'
ledger=json.loads(path.read_text(encoding='utf8'))
candidate={
 'id':'ocellaris-adult-16-candidate-1','species':'clown','stage':'adult','status':'rejected; not a production sprite sheet','tool':'built-in image_gen',
 'path':'planning/livestock16/ocellaris-adult-candidate-rejected.png',
 'reference':'assets/livestock/fish/clownfish/clownfish-benchmark-v1-128.png',
 'requestedFrames':16,'productionFrames':0,'size':[1536,1024],
 'reasons':['Equal4x4 cell partition cuts through living fish at row boundaries','Head/eye location and body proportions drift between poses','Not suitable to replace the approved benchmark or apply inherited markings'],
 'prompt':'Create a production pixel art sprite sheet for Aquarium Life. Edit/reference target is the provided approved natural Ocellaris clownfish sheet. Preserve EXACT same orange-white-black fish identity, three white bars, body proportion, vivid classic16-bit pixelart, single visible eye at right and fin number. Need exactly16 distinct subtle swim keyframes arranged in a4column by4row grid, equal cells, uniform head/eye/anchor coordinate within every cell, consistent right-facing full fish side-profile, transparent background throughout no borders letters labels shadows. Frame1neutral,2tail beginning bend,3pectoral slightly forward,4tail small sweep,5pectoral adjustment,6tail nearpeak,7subtle body flex while head fixed,8tail recovers,9neutral,10opposite small tail sweep,11pectoral recovery,12continued opposite sweep,13opposite peak,14fin recovery,15tail approachesneutral,16nearneutral ending continuous loop. Keep calm short tail amplitudes. All fish same size and eye location, clean attachedfins, no added fins/eyes, no headwobble, no morphingbars. Do not put four copies of the old strip; paint16 meaningful new individually controlled poses. All sixteen fish fit fully in individual equalcells with generous transparency and no cropping. This is an unapproved candidate to be QA checked before integration, do not invent a different fish.'}
ledger['candidates']=[{k:v for k,v in candidate.items() if k!='prompt'}]
path.write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
(root/'planning/livestock16/generation-record.json').write_text(json.dumps(candidate,indent=2,ensure_ascii=False)+'\n',encoding='utf8')

intro='''## Livestock16-frame expansion — playable v4.0.4 / MDPv4.7

**Partial implementation: authored artwork remains unfinished.** Audited119 marine entries in12 batches (94fish,15coral records,10invertebrates), with25 designer varieties kept separate. Added a shared validated16-frame asset path to AL.FishAnimation, an offline full-catalog review gallery and calmer existing fish timing. **Zero new production16-frame sheets are complete; all119 entries still need dedicated artwork.** One generated Ocellaris candidate failed alignment/identity checks and is retained outside deployment. Existing art, biology, local saves and freshwater lock remain. See [LIVESTOCK_ANIMATION_16_FRAME_REPORT.md](LIVESTOCK_ANIMATION_16_FRAME_REPORT.md) for each entry and actual evidence. Earlier animation reports describe the previous milestone and do not establish16-frame completion.

'''
report=['# Livestock16-frame animation expansion — v4.0.4\n',intro,
'''## Actual delivery and limits

The full requested art expansion is **not finished**. All119 entries have been audited and recorded, not falsely marked production-complete. This includes six acquisition-held records (five clownfish and Coleman shrimp), one existing fictional fish and five generic legacy coral groups. It excludes11 protected freshwater fish, six freshwater plants and five reference-only fish absent from the runtime. Runtime dictionary keys are authoritative; legacy coral definitions do not all contain an internal `id`, so the audit uses their dictionary keys. No game species IDs or acquisition rules were changed.

The existing94 marine fish now have calmer presentation rates: normal requested16-slot pacing is approximately6–10slots/second depending on family/stage, representing roughly0.4–0.6cycles/second. These slots are **not sixteen authored frames**. The31 adult clownfish retain their existing four poses; the other63 fish retain procedural articulation of their existing one-pose sources. Idle/perching/resting reduces rate and strength; fast movement increases rate, outer fins use one cycle instead of two per tail cycle, maximum normal displacement is one scene pixel and the added swim bob is removed. Turning does not reset phase. Earlier actual-size fin-layer gaps remain explicit in FISH_ANIMATION_SYSTEM.md.

No invertebrate is given a fish rig. Their retained source art lacks separated walking limbs/antennae/feet. No coral skeleton is bent to fabricate an animation. The loader hooks are integrated at the real coral and invertebrate draw points; without a validated sheet they retain their existing stage/health/death artwork and presentation. Existing coral placement/fragging and all biological systems remain untouched.

## Totals

| Item | Actual count |
|---|---:|
| Marine entries audited |119|
| Audit batches, last containing9 |12|
| Fish timing improved, original appearance retained |94|
| Designer varieties preserved, not additional species |25|
| New production16-frame sheets |**0**|
| Completed fish16-frame upgrades |**0**|
| Completed coral/invertebrate16-frame upgrades |**0 /0**|
| Entries awaiting authored artwork |**119**|
| Generated candidates / rejected / integrated |1 /1 /0|
| New player art approvals |0|

## Every implemented marine entry

All rows are **artwork-required; not complete; final appearance not player-approved**. A dash means no new production path exists, not a missing deployed dependency. Original source links point to real existing artwork. Stages/states identify required slots, not finished animation coverage. Tests validate retained sources and safe fallback, not absent artwork quality.

| Batch | Name / stable ID | Category | Existing source | New16-frame path / completed frames | Required stages / states | Missing artwork / validation |
|---:|---|---|---|---|---|---|
''']
for e in ledger['entries']:
    category=e['category']+(' (bottom fish)' if e['profile'] in ['goby','blenny'] else '')
    report.append(f"|{e['batch']}|{e['name']} / `{e['id']}`|{category}|[source]({e['existingPath']})|— / **0**|{', '.join(e['stages'])} / {', '.join(e['requiredStates'])}|{e['missingArtwork']} Retained live/dead sources and category fallback checked; new16-frame visual validation **not possible until artwork exists**.|\n")
report.append('\n## Batch ledger\n\nEach batch completed the source audit, species mapping, appropriate fallback integration and retained-source playback checks. The artwork-creation/production-approval step is unfinished in every batch; the next batch was still processed as required.\n\n| Batch | Entries | Production sheets | Status |\n|---:|---|---:|---|\n')
for b in ledger['batches']:
    report.append(f"|{b['number']}|{', '.join('`'+i+'`' for i in b['ids'])}|0|Audited; authored artwork required|\n")
report.append('''
## Designer pattern coverage

All25 varieties remain attached to their existing biological species. A future production slot must match the specific variety; missing variety or life-stage sheets fall back to that specimen's retained source. No base-species sheet silently replaces a designer pattern.

| Biological ID | Variety | Existing source |16-frame status / user approval |
|---|---|---|---|
''')
for e in ledger['entries']:
    for v in e['varieties']:
        report.append(f"|`{e['id']}`|{v['name']} / `{v['id']}`|[source]({v['existingPath']})|Artwork required / no new approval|\n")
report.append('''
## Candidate generation and the production gate

Built-in image_gen was used with the approved Ocellaris benchmark as the edit/reference target, requesting16 subtly different right-facing poses, equal4×4 cells, fixed head/eye registration and identical markings. The exact prompt, tool, reference and rejection reasons are preserved in `planning/livestock16/generation-record.json`; the original output is retained at `planning/livestock16/ocellaris-adult-candidate-rejected.png`. This is not a finished sprite sheet. Its1536×1024 output has transparency, but equal384×256 cells cut the fish across the first/second rows. Visible body/eye offsets and proportions vary. It is not loaded by the game or included in DIST. No raster surgery or repeated-frame padding was used to disguise the failure.

The remaining sources are flattened stage/state art, not separately painted limb/polyp/pectoral layers or sixteen poses. They cannot establish new hidden anatomy or stable markings by duplication. Each entry records its specific missing source layers. Completing the requested expansion needs aligned authored keyframes or layered pixel-art source for those slots and a visual review of each; code support and automated timing tests do not substitute for that artwork. This is a disclosed artwork limitation, not a claim that image generation guarantees or certifies anatomy. No new real-world biological claims/research were introduced.

## Changed and created files

- `assets/animation/livestock-registry.json`, generated `js/livestock-animation-data.js`:119 entries,12 batches, original paths, life stages, states, missing-art reasons, acquisition/approval state and zero production clips.
- `assets/animation/fish-registry.json`, generated `js/fish-animation-data.js`: calmer family/stage artistic rates and amplitudes.
- `js/fish-animation.js`: central validated sheet library, lazy local loading,16-cell indexing, anchors, retained source fallback, bounded frame cache, no additional rig bending on authored cells and calm existing motion.
- `js/render.js`, `js/expansion-ui.js`, `index.html`: shared fish/coral/invertebrate hooks and local data script; freshwater branch retained.
- `livestock-animation-review.html`, `css/livestock-animation-review.css`, `js/livestock-animation-review.js`: all119 entries, categories, old artwork, missing-sheet status, stage/state/facing/morph selectors,0.1×–2× playback, pause/step and individual authored-frame inspection when a real sheet exists. Isolated from Save/main/startup; no player storage access. No added player-facing debugging controls.
- `fish-animation-review.html`: loads the new central data alongside the retained94-fish review.
- `livestock_animation_build.py`, `build.py`: validate central sheet definitions and embed local PNGs for file:// and hosted offline playback; versionv4.0.4. Missing/prototype/repeated cells cannot be counted as production; source SHA and exact geometry are required.
- `tests/livestock16_checks.js`, `tests/livestock16_qa.py`, `tests/browser_qa.py`, `tests/verify_livestock16_release.py`: catalog, calm timing, retained art, loader fixtures, actual selection, local saves, no-network/gallery, performance and release checks. Synthetic loader fixtures are not livestock assets or art approvals.
- The consolidated31-section master, ART_DIRECTION, CURRENT_LIVESTOCK_CATALOG, DEVELOPMENT_STATUS, FISH_ANIMATION_SYSTEM, PROJECT_CONTINUITY_SOURCE, README, TEST_REPORT and build report record the partial delivery and remaining art accurately.

## Current validation evidence

Pending final runs. See `tests/livestock16-evidence` for actual current results; no absent-art quality checks are claimed as passed.
''')
(root/'LIVESTOCK_ANIMATION_16_FRAME_REPORT.md').write_text(''.join(report),encoding='utf8')
master=root/'MASTER_DEVELOPMENT_PROMPT.md';old=master.read_text(encoding='utf8')
start=old.index('## 3.14 ');end=old.index('# 4. ',start)
section='''## 3.14 Marine livestock animation — authoritative16-frame requirement (v4.0.4)

Audit every runtime marine fish, coral and non-fish invertebrate against CURRENT_LIVESTOCK_CATALOG and original source art. Use runtime dictionary keys, preserve stable IDs/holds, exclude protected freshwater and unimplemented reference art, avoid duplicate species and track designer morphs under their biological species. Process the entire eligible roster in batches of10; record missing artwork and continue to the next entry. Keep artwork-required and rejected candidates separate from completed production assets. LIVESTOCK_ANIMATION_16_FRAME_REPORT.md is the per-entry evidence/status ledger; never claim visual approval until the player actually reviews it.

The sole presentation authority remains AL.FishAnimation, with family/stage motion in assets/animation/fish-registry.json and all-livestock authored-sheet slots in assets/animation/livestock-registry.json. Preserve2D Canvas, approved original sprites, natural Ocellaris benchmark, body/head/eyes, genetic markings, designer identities, stages and death art. A fish needs a genuinely authored16-frame normal swim cycle at each applicable free-swimming stage: neutral, initial tail/pectoral adjustments, one controlled sweep, neutral transition, opposite sweep and seamless recovery. These are species-appropriate phases, not an identical rig imposed on unrelated anatomy. Exactly16 distinct aligned transparent cells, fixed anchor/head/eye, stable proportions/lighting/pixel resolution, attached fins and persistent markings are required. Duplicated stills, recolored placeholders, static concept grids or unreviewed generated approximations cannot satisfy that count. Early anatomy must use its own appropriate source; retain Banggai's developed juvenile release and never invent external eggs or mature larval fins. Keep unresolved caudal-fold-only/early outer-fin layers explicit.

Separate frame count from speed. Begin normal fish playback around6–10frames/second for a16-frame cycle, then tune calm species/stage movement. Reduce resting/perched movement, increase actual fast propulsion naturally, avoid excessive fin flapping, repeated whole-body wobble and double-frequency fin exaggeration. Distinguish clowns' short hover, tang cruising, goby/blenny perch/dart, wrasse propulsion, basslet/cardinal hovering and other implemented anatomical families. No puffer/lion/trigger profile may create a species absent from the roster. Until authored poses exist, only restrained existing-pixel articulation is allowed and must remain labelled partial. Retire procedural deformation wherever a validated authored sheet supplies that motion; do not stack both.

Invertebrate sequences must depict appropriate leg/claw/antenna/foot/fan and shell-carrying movement, including very slow crawling. Never use a fish swimming rig for them. Coral motion is limited to appropriate existing polyps/tentacles/retraction/feeding/flow response; rigid stony skeletons and attachment points stay stable. Minimal-motion species must not be exaggerated to fill a sheet. Preserve placement, fragging, growth, health, bleaching, recovery and mortality. Lack of separate polyp/limb layers is missing artwork, not permission to distort the whole organism.

Register species ID, local PNG path, cell width/height/count, ordered16indices, playback timing, anchor, facing, stage, state and variety identity centrally. Reject missing, blank, repeated or unvalidated production sheets. Keep prototypes out of gameplay. Local lazy decoding/cached sheets and bounded extracted-frame caches serve both file:// and hosted offline play. Retain original art until a compatible sheet is ready; never substitute another stage or designer variety. Apply genetic markings to the selected authored source, then draw it without an extra fin warp. Mirror existing side profiles correctly, retain the single visible eye and preserve phase across direction changes; independent opposite-side/yaw art is not implied. Anchors, layering, hitboxes, offscreen culling, selection IDs, three-second outlines and independent inspector lifetime remain consistent.

Use renderer-owned real-time clocks only. Existing Eat/Rest/Hide and autonomous breeding/visible-health states may inform motion; rendering never initiates feeding, mating, disease, eggs or biological RNG. Respiratory activity and weak/injured motion remain distinct; dead specimens freeze live motion and retain authored mortality art and simulation sinking. Do not change20real minutes/day, offline ecology, water, breeding, health, genetics, economy, acquisition restrictions or save schema.

Provide a development-only offline all-livestock gallery with names/categories, original artwork, real new sheets or explicit missing status, individual-cell inspection, animated playback, slow-speed control, stage/state/facing/morph selectors and completion/approval status. No unfinished controls enter the ordinary player UI and the gallery must not access player saves. Validate every actual sheet's16cells, loads, transparency/bounds, subtle meaningful differences, stable eyes/body/patterns, fin attachment/loop and actual visual quality; do not claim missing-sheet checks passed. Also verify actual gameplay clicks, calm/idle/turn/death, save/load, offscreen/performance at normal and high stock, renderer-rate independence, all original freshwater output and freshwater lock. Future marine additions must automatically fail coverage if unmapped. Retain the consolidated31-section master and exact continuity copy. Current architecture/limits are in FISH_ANIMATION_SYSTEM.md; current authored-art coverage is in LIVESTOCK_ANIMATION_16_FRAME_REPORT.md.

'''
new=old[:start]+section+old[end:];new=new.replace('VERSION 4.6','VERSION 4.7')
new=new.replace('## Global marine fish animation audit',intro+'## Global marine fish animation audit',1)
continuity=root/'PROJECT_CONTINUITY_SOURCE.md';text=continuity.read_text(encoding='utf8');assert text.count(old)==1
text=text.replace(old,new);text=text.replace('## Global marine fish animation audit',intro+'## Global marine fish animation audit',1).replace('Playable v4.0.3 / MDP v4.6','Playable v4.0.4 / MDP v4.7')
master.write_text(new,encoding='utf8');continuity.write_text(text,encoding='utf8')
for name in ['ART_DIRECTION.md','CURRENT_LIVESTOCK_CATALOG.md','DEVELOPMENT_STATUS.md','README.md','TEST_REPORT.md','GITHUB_PAGES_BUILD_REPORT.md']:
    p=root/name;s=p.read_text(encoding='utf8');first=s.index('\n');p.write_text(s[:first+1]+'\n'+intro+s[first+1:],encoding='utf8')
p=root/'FISH_ANIMATION_SYSTEM.md';s=p.read_text(encoding='utf8');p.write_text(s+'\n\n'+intro+'''### Validated sheet contract and caches

`AL.FishAnimation.sheets` is part of the same service, not a second competing animator. Its library keys by biologicalID/stage/state/variety. A production record declares `path`, `sha256`, `frameWidth`, `frameHeight`, `columns`, `frameCount:16`, `order:[0..15]`, `framesPerSecond`, `anchor`, `facing`, optional existing-eye metadata and explicit validation evidence. The build checks original path, PNG header/cell dimensions, fileSHA, sixteen distinct recorded frame hashes, art-review evidence, state/stage/timing and completion accounting. It embeds local dataURLs for offline/file loading. The browser decodes lazily once per library record, then rejects actual blank/repeated decoded cells. Only256 extracted frames are retained; original sheet decoding is lazy, so absent/unseen sheets consume no texture memory. This release has zero production sheet records; fixture tests exercise the code without pretending they are animal art.

`source` selects only an exact-stage/exact-variety swim sheet, otherwise the existing source. `draw` honors its centered anchor and bypasses the procedural rig. Pattern output retains authored metadata and separate frame identity, preventing an old fallback-frame pattern cache from replacing a new sheet cell. The existing pattern authority and inherited data are unchanged. `drawResident` handles coral/invertebrate sheets with fixed or mirrored anchors, never fish bending; dead calls always return to original mortality presentation. With no validated sheet, existing sprites/behavior remain. Some legacy coral groups remain unverified biological identities, and settled invertebrate baby images are not newly verified planktonic larvae.

Normal existing family cycles are now0.42–0.56Hz before actual-state/stage modifiers; normal requested16-slot rate is tested around6–10Hz, not a claim of16authored poses. Fin oscillation uses one cycle, normal displacement stays at most one scene pixel and added bob is zero. Rest/perch reduces rate; faster movement raises it; banked direction changes retain phase. These are artistic calibrations, not measured biological research. Old animation audit rate descriptions are historical.

Future artwork belongs under `assets/livestock/animations/<species>/` or an equally explicit existing structure. Prototype sheets belong outside the production clip list. Add real visual evidence and exact hashes before changing `framesCompleted`; no missing sheet should be listed with an invented path. Full status, remaining layers and candidate rejection are in LIVESTOCK_ANIMATION_16_FRAME_REPORT.md.
''',encoding='utf8')
print('Updated honest119-entry coverage,12-batch ledger, master4.7 and continuity')
