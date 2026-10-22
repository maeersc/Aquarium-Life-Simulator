# Aquarium Life - art direction 1.1

Active scope: fish eye persistence, correct direction, six priority fish, coral visual states and three rock collections. New assets await the user's visual review. The original approved clownfish source remains assigned and preserved. No unrelated gameplay phase is authorized by this art update.

## Locked visual source

[The approved concept](assets/reference/approved_clownfish_hybrid.png) was inspected before generation. Preserve its crisp outlines, saturated tropical palette, intentional highlight/shadow clusters, defined fins and readable faces. The environment and text are presentation, never baked into transparent animal sprites. Avoid noise, blur, smooth painting and generic recolored body templates when detailed assets exist.

The user selected adult Emperor angelfish (*Pomacanthus imperator*) and Red lionfish (*Pterois volitans*). Adult Emperor mask/stripe direction is informed by [Australian Museum](https://australian.museum/learn/animals/fishes/emperor-angelfish-pomacanthus-imperator/); lionfish identity and fin form by [Florida Museum](https://www.floridamuseum.ufl.edu/discover-fish/species-profiles/red-lionfish/). These are visual subjects, not new husbandry definitions.

## Permanent eye and directional standard

An applicable side-view frame has one near-side eye attached to its head. Baked eyes are registered using per-frame source coordinates and a canonical artist eye component. Separate components use head-local anchors; never use screen offsets. The registered sprite is sampled once at its final scene size, with a minimum readable eye footprint, then mirrored/scaled/inverted as one object. Clear transparent component regions before copying them so old body fragments cannot remain underneath.

Use the shared `AL.SpriteKit` draw boundary with save/restore, integer placement, correct odd-size flip extents and bounded raster caches. Track facing from displayed target displacement, preserving it under sub-threshold jitter. Normal and idle use consistent cadences modulated by existing species activity. Freeze the pose after death. Optional authored left-side artwork bypasses generic mirroring for asymmetric species.

The tests cover every existing fish and new art subject. Native pixel continuity and transform tests are evidence of technical correctness, not a claim of perfect anatomical accuracy. Inspect contact sheets and enlarged views for placement and style.

## Production geometry and metadata

New priority fish atlases use four 192 x 128 RGBA frames, with stable head-local eye registration, transparent padding and preserved proportions. The assigned clownfish keeps its original 128-pixel candidate atlas and a 128 x 80 runtime canvas. Older fish remain 64 x 40 procedural sources, now with explicit eye/anchor/frame metadata. The scene remains 480 x 240 with smoothing disabled; camera scale is separate from native sprite size.

Metadata includes art/species ID, frame width/height/count/cadence, bounds, anchor, eye component, facing behavior, animation states and rendering layer. New fish have null runtime species IDs and explicit ART ONLY usage. All thirteen new asset families start Ready for Review with `approved: false`.

`tests/prepare_art_update.py` packs generated sources with uniform nearest-neighbor sampling, binary alpha and consistent padding. Its pupil-location aid is reviewed visually and does not validate biology by itself. Source PNGs, edit attempts, revisions and exact prompts remain available in [ART_GENERATION_RECORD.md](ART_GENERATION_RECORD.md). Embedded local PNG resources keep file-URL canvases readable for thumbnails and tests; no remote asset service runs during play.

## Coral states and motion

Five categories have healthy, stressed, bleached, tissue-loss and dead artwork. Bleached tissue is pale but intact; dead remains differ. Zoanthids and mushrooms leave collapsed tissue on their base, not stony skeleton cups. SPS/LPS can expose pale skeletons; soft leather collapses. Existing health state selects current living/dead appearances; the gallery separately previews bleaching without expanding biology.

SPS geometry stays rigid while selected existing polyp/tip highlights pulse. Soft tissues use two restrained flow poses. More frames and individual polyp layers would improve smoothness; they require further artist review. Preserve pixel detail in zoomed views and clear silhouettes at the small gameplay footprint.

## Rock collections

Fiji and Caribbean art products are reef-limestone interpretations, with porous cavities and limited coralline accents. The Hawaiian product is explicitly volcanic-inspired, with darker angular forms. Geographic names do not assign universal geology or chemical effects.

Each collection includes small, medium, large and arch variants with bottom anchors. Use consistent source pixel density, preserve clear openings, clamp art-preview placement inside the display, and draw selection outlines independently of the sprite. The existing marine scenery/cave rendering uses these images; no new inventory or placement biology is implied.

## Review and outstanding craft work

The offline gallery separates Fish, Corals and Rocks. Fish show right/left poses, normal/idle motion, turning, frozen death, eye anchors, native detail and aquarium scale. Corals show all five states. Rocks show all sizes and saved preview arrangements under tank lighting. User review labels are stored separately from gameplay.

Generated artwork remains an art-review submission. Some body/fin/pattern changes between poses need cleanup. Turning uses mirrored side profiles, not authored head-on frames; idle shares swim poses. Dedicated feeding/illness/decomposition frames and scientifically reviewed anatomy for all older species remain unfinished. Stop after this submission for user visual approval before unrelated development.
