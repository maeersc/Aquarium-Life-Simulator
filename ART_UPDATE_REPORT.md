# Art development update 1.1 — review submission

Historical art 1.1 submission. The current delivery is [LIFE_STAGE_ART_REPORT.md](LIFE_STAGE_ART_REPORT.md).

Date: 2026-10-11. **Rendering fixes implemented; new artwork awaits visual approval.**

Open [the offline gallery](art-review.html) from the game's **Livestock art review** footer link. Its Fish, Corals and Rocks categories provide enlarged and native views, actual aquarium-scale previews, animation controls, head-local eye overlays and local review notes. The five additional fish are labeled ART ONLY and do not appear in shops.

## Eye defect and architectural correction

The approved clownfish PNGs contain eyes. The defects arose after extraction and rendering: each animation pose was independently fitted to its silhouette bounds, so changing fin/tail outlines shifted the head. Repeated nearest-neighbor resampling could then drop small pupil pixels. Odd-width centered flips also occupied different pixel columns. The original simulation already had a heading threshold, but using its heading directly could face a fish against its still-interpolating displayed movement.

The fix registers frames to measured head/eye coordinates, copies a canonical artist eye component to that head-local position, and caches the complete sprite at its final scene size. Tiny eye components keep a minimum sampled footprint. The eye is part of the fish-local raster, not a floating screen-space decoration. Mirroring, death inversion and scaling transform it together with the head. Clearing the canonical component region before copying prevents transparent pixels from leaving another pose underneath; this caught and resolved a remaining Emperor-angelfish inconsistency during QA.

`js/sprite-kit.js` provides the shared raster/draw boundary, odd-size alignment, thresholded facing and optional authored left-side sprite support. `js/render.js` uses displayed target displacement for stable facing at slow and fast interpolation rates. Render corrections do not mutate authoritative fish positions, genes, health or saved headings. Swimming uses a common normal/idle cadence scaled by existing species activity; deceased fish freeze frame zero.

Before/after diagnostics: [before](assets/previews/chrome-eye-before.png), [after](assets/previews/chrome-eye-after.png). The original approximate pupil-region counts are diagnostic evidence, not an anatomical proof. The final suite uses explicit local component bounds and exact pixel comparisons.

## Delivered artwork

| Subject | Scientific/art definition | Integration and status |
|---|---|---|
| Ocellaris clownfish | Amphiprion ocellaris | Existing assigned artwork preserved; eye registration and shared rendering corrected |
| Niger triggerfish | Odonus niger | Four-frame transparent art-only atlas; Ready for Review |
| Emperor angelfish | Pomacanthus imperator, adult | User-confirmed species; four-frame art-only atlas; Ready for Review |
| Red lionfish | Pterois volitans | User-confirmed species; four-frame art-only atlas; Ready for Review |
| Dogface pufferfish | Arothron nigropunctatus | Four-frame art-only atlas; Ready for Review |
| Blue tang | Paracanthurus hepatus | Four-frame art-only atlas; Ready for Review |
| Zoanthids, mushrooms, SPS, LPS, soft leather coral | Five existing coral categories | Five state columns and two poses per category; integrated into existing coral rendering |
| Fiji, Caribbean, Hawaiian rocks | Reef limestone / specified volcanic-inspired art products | Small, medium, large and arch variants; marine scenery/cave rendering and isolated placement preview |

The existing 22 gameplay fish remain the same 22 species IDs. All share the corrected eye/direction pipeline. Twenty-one older sprites remain procedural and need broader artistic/anatomical refinement; they were not replaced with simplified artwork. See [CURRENT_FISH_CATALOG.md](CURRENT_FISH_CATALOG.md).

Coral bleaching is distinct from death in the visual review. Zoanthid/mushroom dead states were revised to collapsed tissue rather than inappropriate stony cups. SPS/LPS can expose pale skeletons; soft leather tissue collapses. SPS holds rigid geometry while selected existing highlights pulse. Other living coral poses show restrained flow variation. The existing health model selects healthy/stressed/tissue-loss/dead appearances; independent bleaching remains a gallery art study, not a new biology engine.

Rock selection outlines never distort the PNG. Preview arrangements are clamped inside the display and stored separately from gameplay. Marine background rocks and existing cave decorations now use the PNG art. These are visual integrations: no new rock store, inventory, chemistry or physical placement system is claimed.

## Verification

| Browser | System checks | Main-game UI checks | Art/sprite checks | Directional pixel render cases |
|---|---:|---:|---:|---:|
| Chrome | 68 passed | 69 passed | 221 passed | 6,480 |
| Edge | 68 passed | 69 passed | 221 passed | 6,480 |

All ran through `file://` with networking disabled. No JavaScript exceptions or HTTP(S) requests were observed. The same cases run in each browser; these are not separate unique cases.

The rendering matrix covers 27 fish subjects, four frames, three genetic brightness values, five scene widths (16, 22, 33, 59, 109), both horizontal directions and normal/inverted poses. It checks retained pupil detail, identical eye components across frames, eye bounds, exact mirrored pixels and transform restoration. Additional checks cover all 22 actual movement definitions, slow interpolation, jitter thresholds, independent fish, optional asymmetric left art, transparent frames, rigid SPS geometry, distinct bleached/dead states, transparent arch probes, all gallery states/variants, preview persistence and layouts at 1440/1024/760/390 pixels.

Evidence: [Chrome art results](tests/chrome-art11-results.json), [Edge art results](tests/edge-art11-results.json), [Chrome game results](tests/chrome-results.json), [Edge game results](tests/edge-results.json). [Fish](assets/previews/chrome-art11-fish.png), [corals](assets/previews/chrome-art11-corals.png), [rocks](assets/previews/chrome-art11-rocks.png). The three [eye contact sheets](assets/previews/chrome-art11-eyes-1.png), [second sheet](assets/previews/chrome-art11-eyes-2.png), [third sheet](assets/previews/chrome-art11-eyes-3.png) were inspected for broad head attachment and consistent direction.

Reproduce with `python tests/browser_qa.py chrome --art-review` and `python tests/browser_qa.py edge --art-review`. Main-game checks omit `--art-review`. Open `tests/eye-review.html` for the reproducible all-fish contact sheet.

## Art quality and limits

These are generated art assets prepared for review with built-in imagegen, not finished hand-crafted sprite production. Original sources, revisions and prompts are listed in [ART_GENERATION_RECORD.md](ART_GENERATION_RECORD.md). Native frame dimensions, bounds, anchors, cadence, eye metadata, layers and review state are bundled locally; no generation service is used at runtime. The original approved reference and all clownfish PNGs are preserved, along with the earlier gallery in `art-review-v1.html`.

Pixel continuity tests do not prove perfect anatomy. The new fish still show small fin/body/pattern differences between generated poses; the canonical eye/head registration prevents eye drift but does not replace a full artist cleanup pass. Turning uses stable mirrored side profiles rather than authored head-on transition frames; idle reuses swim poses at a slower cadence. Dedicated decomposition art and species-specific asymmetric side drawings are not finished. Firefox, extensive touch/screen-reader review and maximum-population performance remain unverified.

No economy, quest, breeding, black-market or water-chemistry systems were expanded. Save schema 2 remains compatible. **This art update stops here for the user's visual review before unrelated development resumes.**
