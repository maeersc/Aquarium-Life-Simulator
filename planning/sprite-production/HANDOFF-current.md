# Active production checkpoint — 2026-10-19

## MOST RECENT CHECKPOINT — supersedes historical progress below

All available acceptable artwork is complete:382 registered native sheets/6112 cells,110 fullyComplete species, batches1–11 finished. All89 fish, all15corals and6invertebrates are covered. Chrome and Edge each5398passed/0failed, including real250fish+35coral+40invert timing and9000actual owned resident draws. The16 backdrop silhouettes are recorded separately in the mixed benchmark, not miscounted as owned livestock. Preservation1314passed/0failed.

GENUINE EXTERNAL BLOCKER: built-in image_gen returnedHTTP429 usage_limit_reached on all3 generation streams. Reset reported2026-10-20T13:37:31Z /09:37AM America/New_York. No API credential is configured and no API fallback authorized. Exactly18physical sheets remain acrossLysmata debelius,Alpheus randalli,Hymenocera picta. Four Fire Shrimp baby/juvenile idle/walk source candidates were visually rejected for severe red/yellow alpha bleed and broad webbed appendages;14sources were never generated. NONE of these4 rejected sources entered the central registry/game. Original approved art remains active for all3 species. See blockers.json and reviews/batch12-rejected-sources.json. Do not claim done or end Done With Edits while these18are missing. Do not synthesize poses or accept invalid art to bypass the quota.

All batch11 last20 final contacts were actually inspected, corrected where required, registered in reviews/batch11-last20.json and passed both browsers. Hermit posterior leg masks now preserve full antennae/major claws after fine-tip disconnections were rejected. Thor antennae are fully canonical, with only original attached legs moving. Porcelain masks preserve true carapace/eyes while allowing complete original articulated appendage/root areas, resolving a severed leg-tip mask. All corrections were re-inspected across16nativecells. Current report and five home documentation sections accurately state382/110 and the3blocked species; full31-section master remains exactly once in continuity.

Release refresh verified at382: DIST1977files/843998535bytes; AquariumLife-GitHub-Pages.zip753158520bytes, rootindex and ZIPCRCverified. Chrome and Edge each5162Pages/DIST/local-save/export/import checks passed/0failed. Standard release verifier4657passed/0failed, fullyComplete110/113 and382/400physical sheets, builtAt2026-10-19T19:14:22.101303Z. Actual mixed250fish/35coral/40invert p95Chrome23.2ms/Edge19.9ms; all9000owned resident draws accepted (1920static backdrop draws counted separately), every15coral/6accepted invert species covered. Source382tests5398passed/0failed each; preservation1314/0. After this handoff update, rebuild tests/package.py sourceZIP then verifier --source-archive --check-only; do not modify archived files afterward. The all400 --require-complete gate remains intentionally unsatisfied. This is an honest portable checkpoint, not final all-livestock completion.

No image-generation cells remain running;19/20/21all failed with real429 and were drained. All exact completed requests are on disk. Source manifests/invertebrate-all-prompts.json and prepare-invertebrate-prompts.py let a future turn resume actual missing/rejected slots. Fire Shrimp replacements must be revision2 and retain the rejected originals. Native proof/matcher fallback helpers currently assume v1 when no packed metadata exists, so explicitly teach them to read the incoming ledger source or point at v2 before inspecting replacements; do not accidentally inspect rejectedv1 again. The four rejected requests must be replaced with valid newly generated sources, not treated as completed by the manifest existence check.

The notes below preserve earlier implementation context and are historical where counts/tool IDs differ.

Continue actual FULL16-FRAME LIVESTOCK SPRITE PRODUCTION to all113 usable marine entries /400 physical sheets. User repeatedly asks to finish; do not stop after a batch or claim completion early. Latest user: “can you get this done please.” No subagents authorized. Original HANDOFF.md still documents base pipeline/final release requirements but has stale counts.

## Actual completed status

- Batches1–10:100 species,338 registered sheets/5408 actual authored native cells. Includes all89 fish plus11 coral species (zoa plus batch10's ten). Chrome and Edge each4769 passed/0 failed with338 sheets. This is actual current SHA coverage; report.py has marked100 fullyComplete.
- All fish finished including designer varieties and preserved biological early aliases. Batch8 remaining iris corrections and source-facing normalization are recorded in reviews/batch8-remaining.json. Batch9 notes in reviews/batch9.json. All native contacts were genuinely inspected. Batch10 masks and notes are in reviews/batch10*.json; all20 final contacts inspected and registered. No user visual approval inferred.
- DIST and AquariumLife-GitHub-Pages.zip were last rebuilt at289 sheets/80 species:1879 sourcefiles,779538149 bytes; PagesZIP700472478 bytes. Source ZIP still stale. Final rebuild both required after all400 genuine sheets/checks.
- Remaining physical assets:8 coral sheets (last4 corals, batch11) and54 invert sheets (9 species×3 stages×idle/walk). None of these registered yet.

## New non-fish technical supports (not a second animator)

- tests/preview_livestock16_resident.py makes unapproved16-cell native proof and first native pose from manually inspected body landmark anchors. Does not register/approve or synthesize poses.
- tests/inspect_livestock16_resident_sources.py BATCH makes first-source proof pages and JSON transforms; --native makes native-first pages at1:1. Each page8 entries, source proofs metadata previewOrigin/previewScale/sourceBox lets you convert manually inspected screenpoint into sourceglobal coordinates. Native proofs have origin32,80 per192×160tile;192×192legacy origin32,64, tiles256×280. Pages are under packed/batchN-source-firsts-PAGE.{png,json} / -native-firsts-.
- tests/prepare_livestock16_tissue_masks.py SPEC.json rasterizes MANUALLY specified native tissue polygons/discs/rings. Each spec needs nativeFirstInspected:true and description. Geometry fields polygons,discs, rings[x,y,rx,ry,innerRatio],protectedPolygons,protectedDiscs. Ring inner areas stay canonical, even where rings overlap. This assembles original imagegen tissue poses around canonical first body, never generates motion.
- pack_resident now supports protectedPolygons after mutable polygons; actual whole skeleton/shell/body/eyes stay identical outside reviewed mutable tissue masks. Body registration must protect actual visible pixels, at least16 protected visiblepixels,16 unique actual final cells; margins/binaryalpha checks retained. Final all16 native contact review required separately before registration.

## Current in-flight local tooling

Tool cells can vanish on a new user message. Completed request files on disk are authoritative. Do not depend on V8 load() or old cell IDs surviving. Every new missing request must persist exact prompt and returned actual generated source. Image tool output is {image_url,output_hint}; NEVER text full result/base64. Use output_hint.match(/[A-Z]:\\[^:\r\n]*?\.png/g).at(-1) for actual source path. No imagegen fallback CLI authorized.

Current image generation loops: functions cells19 adults,20 juveniles,21 babies, each finishes one image at a time and persists requests. These resume38 missing invert requests. Original earlier loops were lost on user steering after16 invert requests; no assumption that the remaining38 were generated. Read per-asset request files / collect batch11 and12 to determine actual progress. If19–21 vanish, use persisted manifest to resume only missing files.

Authoritative complete54-job prompt manifest: requests/invertebrate-all-prompts.json. Recreated by planning/sprite-production/prepare-invertebrate-prompts.py, which derives layout from existing exact sexy-anemone-shrimp-adult-idle request. Existing generated requests preserve their actual original prompts; do not replace them with rebuilt prompts. The preparation script prints only missing jobs as JSON; use it to restore tool-store jobs after interruption. Long whole-manifest PowerShell WriteAllText exceeded Windows command length; use this Python script or apply_patch instead.

All27 original invert stage refs and all30 original coral refs have actually been viewed in native or reference proof form. Every actual NEW final16-cell sheet still needs its own native contact review.

### Pending functions cells as of writing

-22: writing batch11-coral-tissue-masks.json, prepare masks, import8coral sheets, report. Import produced7success; tubastraea colony failed because mutable fringe covered its dark body-registration point. Report338/100. Cell eventually completed.
-25: writing and importing16 early invert masks/sheets; inspect returned results. No approval/registration yet.
-26: fixes tubastraea colony mask with protectedDiscs[[96,133,4]], checks RGBA at actual anchor, prepares masks, reimports just that sheet, then views the8coral contacts in2groups (first4 in cell26, remaining4 still need viewing). Await/drain output and inspect actual images. Do not mark unseen contacts.
-27: collect11 and12 without import +ledger counts. Await output.

Avoid concurrent ledger-mutating import/register processes. Some earlier pending calls may have overlapped; after all local imports finish, run one sequential collect11 --import so no production ledger slot is lost. Raw/packed physical files remain separate. Never change central registry/runtime during browser/build/hash checks.

## Last4corals —8 sheets

IDs caulastraea-furcata, turbinaria-reniformis, tubastraea-micranthus, rhizotrochus-typus. All source refs and first original source/native proofs viewed. All8 body landmark template tracks and unapproved16-native contacts generated, first proof reviewed. Landmark evidence reviews/batch11-coral-landmarks.json. Native masks manually defined in reviews/batch11-coral-tissue-masks.json. Seven packed successfully; tubastraea colony correction in cell26 above. Candidate contacts packed/ID/{frag,colony}_polyp_motion_16-contact.png.

Once EVERY final native contact viewed/corrected, create explicit reviews/batch11-corals.json flags/observations, then register8 sequentially. Can keep native ready until all6 other batch11 species done per batch workflow. Do not consider this batch complete before those36 invert sheets pass.

## Early invert work —16 sheets

IDs sexy-anemone-shrimp6 states/stages, porcelain-anemone-crab6, bumblebee-snail4 (babyidle,juvenileidle/walk,adultidle). All first source proofs actually viewed; manually selected fixed central white trunk /red carapace/gold shell band landmarks. Metadata/source coords in reviews/batch11-early-invert-landmarks.json. All16 unapproved native contacts and native firsts generated; native first proof pages1–2 actually viewed. Final native masks defined from these firsts in reviews/batch11-early-invert-tissue-masks.json. Cell25 importing16; NOT yet final-contact reviewed or registered.

Masks protect Thor raised patterned abdomen, main trunk and paired eyes while sampling original distal legs/antennae; crab protects spotted carapace/eyes/large claw plates while sampling distal legs/soft feeding fans; snail protects complete shell and head/eye stalks while sampling muscular foot edge only. Verify all16 final cells for disconnections/extra eyes/incorrect mutations, correct masks/anchors if necessary. Native source-facing allright so far.

Missing snail baby/adult walk requests were generated by resumed loops (see actual files); they still need raw import, first-source/native landmark/mask and actual final16-cell review. Conch all6 requests were being generated; some Halloween/cleaner requests now exist. Remaining3 batch12 shrimp have not yet been produced as of original restart, check manifest.

## New meaningful QA

tests/sprite_production_qa.py now explicitly awaits every selected adult source before250-fish timing, ensuring benchmark does not accidentally time fallback sprites. At318 and338 both browsers passed this stronger check.

tests/resident_sprite_checks.js now has async mixedPerformance(check). When both authored coral and invert categories exist, creates actual250fish+35corals+40inverts via actual runtime constructors/fixtures, preloads selected native sources, verifies every authored resident draw accepted, unchanged ecology/state and measured p95<33.3ms with bounded caches. Returns null while invert art absent; null is NOT completion. Final release verifier --require-complete now REQUIRES measured mixed full15coral/9invert category coverage and9000accepted resident draws. This helper has not yet run with actual invert clips and may require actual debugging/optimization; do not weaken tests or claim passed.

Current baseline caches128decoded/1024cells; all113 selected adult species fit128 sheets if one invertstate. Gallery metadata stays local classic-script8MBchunks, no fetch/CDN. At338p95still passed, exact original metrics in browser evidence.

## Final obligations

All113/400 +all12batches; preservation1314checks; source Chrome/Edge and builtPages Chrome/Edge; mixedscene; local save/export/import/offline; final docs complete status/master4.8/game4.0.5 only when genuinely done; preserve all31mastersections and exact full master once inside PROJECT_CONTINUITY_SOURCE. Historical audits remain historical; do not globally change historical claims. FISH_ANIMATION_SYSTEM and report need describe actual nonfish protected-body/tissue assembly and current coverage. No user visual approval claimed.

Final order: docs/report → build.py → finalbrowser/Pages suites → verify_sprite_production_release.py --require-complete → tests/package.py sourceZIP → verifier --require-complete --source-archive --check-only. Do not deliver stale source archive or include player saves/profiles. Final user report ends Done With Edits ONLY after all authorized work actually complete.
