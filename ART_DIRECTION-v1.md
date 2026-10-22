# Aquarium Life ? livestock art direction

**Current phase: clownfish artwork assigned to Ocellaris at the user's request.** The concept reference and use of this specific artwork for Ocellaris are approved. Broader species work remains outside this change. This phase is exclusively visual development. Economy, biology, breeding, quests, stores, VIP and other gameplay remain unchanged.

## Authority and approval gate

The visual source of truth is [approved_clownfish_hybrid.png](assets/reference/approved_clownfish_hybrid.png). It is present, was inspected before generation, and remains unchanged. The user's Livestock Art Style Development brief v1.0 requires: audit ? reference analysis ? clownfish benchmark ? in-game-scale preview ? **stop for user review**. Other priority species and coral production wait for explicit clownfish approval. This gate takes precedence over the earlier next-phase habitat work.

The [master specification](MASTER_DEVELOPMENT_PROMPT.md), section 3, retains the long-term rules. The [current fish catalog](CURRENT_FISH_CATALOG.md) distinguishes implemented fish from planned subjects and ART ONLY proposals.

## Reference analysis

The large concept combines a readable compact silhouette with deliberately stepped contours. A navy-black outer edge separates saturated orange from the blue environment. Golden upper planes, burnt-orange lower planes and restrained cream highlights imply volume. Ivory white bands use cool lavender/blue shadow clusters. Ordered scale clusters follow the body instead of random noise; ray-like clusters describe dorsal, pectoral and tail fins. A bright eye highlight, clear mouth and gill contour concentrate attention on the face.

The reference also exaggerates eye size, body depth and fin presentation. Preserve its color richness and clustered detail while resolving species anatomy. The underwater rays, coral scenery, text and decorative particles belong to presentation, never to the transparent animal sprite. This phase creates independent artwork rather than using the full concept as a fish texture.

The ocellaris art subject is **Amphiprion ocellaris**. Orange coloration, three white bands and fine black band margins are supported by the [Florida Museum species profile](https://www.floridamuseum.ufl.edu/discover-fish/species-profiles/clown-anemonefish/). This identification is now also stored on the runtime Ocellaris definition; the other real species still lack scientific-name fields. No husbandry parameters were altered.

## Benchmark deliverables

- [Offline gallery](art-review.html), also linked from the game's footer.
- [Original generated atlas](assets/livestock/fish/clownfish/clownfish-benchmark-v1-source.png): 1254?1254 RGBA, a 2?2 four-pose source sheet; retained unchanged.
- Packed 1?4 PNG atlases at 96, 128, 192 and 256 pixels per frame. [128-pixel proposal](assets/livestock/fish/clownfish/clownfish-benchmark-v1-128.png).
- [Metadata](assets/livestock/fish/clownfish/benchmark-v1.json) and a classic-script copy for direct file loading.
- [Exact prompt and method](assets/livestock/fish/clownfish/GENERATION_PROMPT.md). Generated with the built-in imagegen tool; not presented as hand-crafted production art.
- [Comparison screenshot](assets/previews/chrome-art-review.png) and [game-scale screenshot](assets/previews/chrome-art-scale.png). The gallery itself is the short interactive animation preview.

`tests/prepare_art.py` only packs and samples generated artwork: per-cell alpha bounds, uniform scale, consistent transparent padding, nearest-neighbor resizing and binary alpha at threshold 128. It does not invent animal geometry or paint detail. Original alpha and artwork remain preserved in the source file. Packed candidates have clean binary transparent edges; no background removal service is needed during gameplay.

## Proposed production standard ? pending approval

1. Draw a species-specific lateral silhouette facing right, with a stable body pivot, generous fin clearance and an explicit visible-subject bounding box. Do not stretch one template into different species.
2. Use 128?128 as the provisional clownfish frame canvas. Its visible fish spans about 112?71 pixels. Compare 96/128/192/256 at the same displayed fish width before committing. These current candidates are sampling studies of one source, not independently painted resolutions.
3. Let large fins or elongated bodies determine future canvas aspect ratios. Shared pixel density and display scale matter more than identical canvas dimensions. High-detail large subjects may need 192/256; no such standard is approved yet.
4. Keep a restrained palette of warm body ramps, cool white-band shadows, dark navy edging and selected bright highlights. Use ordered clusters, clean negative space and purposeful fin-ray detail. Avoid isolated noise, blurred contours and smooth painted gradients.
5. Build anatomy into the silhouette: recognizable mouth, eye, gill cover, dorsal/anal/pectoral structures, tail attachment and pattern placement. Preserve the ocellaris three-band layout and refine overly heavy band borders.
6. Keep light direction fixed at upper left. Separate environmental overlays from sprite colors. Add no baked-in aquarium scenery or drop shadow.
7. Ship local transparent PNG atlases with versioned names and metadata for frame geometry, pivot, animation cadence, orientation, source, review status and known limitations. Preserve old artwork and the source reference.
8. Use nearest-neighbor rendering and cached atlases. The current 480?240 gameplay scene is an important constraint: native asset detail above its screen footprint mainly benefits enlargement. No claim is made that the full concept's detail survives a roughly 42-pixel-wide animal.

## Animation concepts and current completeness

| State | Proposed treatment | This review |
|---|---|---|
| Idle | Small pectoral pulses and restrained tail beats, stable body | Four swim poses slowed to 3 fps; separate idle drawings unfinished |
| Normal swim | Coordinated tail/fin cycle with stable eye, gill and bands | Four generated poses at 6 fps; minor body/band drift needs cleanup |
| Turning | Intermediate head-on/three-quarter views, tail follows body | Mirrored left/right endpoints only; no authored turn transition |
| Fast swim | Stronger tail excursion, faster coordinated beat | Concept only, no dedicated frames |
| Feeding | Small jaw/gill movement and controlled approach pose | Concept only |
| Resting | Reduced extension and species-appropriate posture | Concept only |
| Stress/illness | Reduced fin extension, restrained color/posture changes | Concept only; no biology changes |
| Death | Fin motion stops; controlled roll into an inverted/side pose | Frozen inverted frame-zero pose demonstration only |
| Decomposition | Readable, general-audience staged remains | Concept only; no decay simulation changes |

The generated cycle changes fins and tail rather than merely sliding a whole static sprite. It still changes body details slightly. Match landmarks and refine frame registration before any production approval. Death does not continue to flap in the gallery. The game now uses this atlas for Ocellaris, with four cached 128 x 80 frames, preserved proportions, genetic brightness and the existing display footprint. Deceased fish freeze their sprite frame. True turns and dedicated death/decomposition art remain unfinished.

## Fair gallery comparison

Current and proposed artwork use identical visible widths, centered subject bounds and preserved aspect ratios. Both receive the same selected dark/bright/checker backdrop. Native views and equal-width resolution studies are labeled explicitly. The tank preview uses an isolated instance of the real renderer, neutral adult gene/growth values and the current sprite scale formula; both fish receive the same camera factor and dimming.

The gallery reads the 22 runtime species definitions. Only clownfish has proposed art. Other replacement panels say Not Started. All four resolution atlases are loaded once and reused; the gallery caps animation drawing at 30 Hz and respects reduced-motion preference. The 128 atlas decodes to 256 KiB; all four candidate atlases total 2000 KiB of RGBA pixels, excluding canvases/reference. These are memory calculations, not a measured frame-rate guarantee.

The gallery never loads `main.js` or `save.js` and never writes the gameplay save key. Explicit user review uses a separate local key. The assigned clownfish defaults to Approved; other existing art defaults to Needs Improvement. The user explicitly requested assignment of this artwork to Ocellaris. Gallery review controls record further feedback; they do not install other art or authorize automatic expansion.

## Visual review findings

The proposal is recognizably clownfish-like and considerably closer to the reference's color and texture than the legacy procedural sprite. Transparent separation, stronger fin detail, three bands, a defined face and nearest-neighbor enlargement are working.

It is **not production-complete**. The body is rounder and fin silhouettes more exaggerated than the desired natural profile. Black margins and white-blue rim highlights are strong. Some microtexture aliases when reduced. Four-frame body/band consistency needs manual review and refinement. True turning, dedicated idle and death sequences are unfinished. Assignment to Ocellaris is authorized; remaining quality refinements and other species require further direction.

## Coral standard ? specification only in this pass

Keep zoanthids as individual polyps on a colony mat, mushrooms as fleshy discs, SPS as structured small-polyp branching/plating forms, LPS as larger fleshy polyps over an appropriate skeleton, and soft corals as flexible lobes/branches. Resolve specific husbandry/art subjects before definitive anatomy. Use clustered texture, readable silhouettes, restrained flow motion and the same lighting logic as fish.

Future visual sheets should distinguish healthy extension, stressed/retracted tissue, pale-but-living bleaching, partial tissue loss and dead remains. Stony skeleton and collapsed soft tissue need different artwork. These are art-state requirements, not newly implemented coral biology. No new coral assets were created before clownfish approval.

## Remaining priority subjects

Niger triggerfish, marine angelfish, lionfish, dogface pufferfish and blue tang have no gameplay definitions or replacement sprites. Marine angelfish and lionfish exact species remain unresolved and must be selected before definitive art. The existing freshwater angelfish and yellow tang are not substitutes. Artwork for these subjects waits for approval; they will not be silently added to gameplay.
