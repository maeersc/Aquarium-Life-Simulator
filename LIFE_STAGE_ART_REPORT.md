# Livestock life-stage art update 1.0

Delivered for visual review, 2026-10-11. This is an art update; the full game roadmap remains unfinished.

## Open the review

Open [index.html](index.html), then **Life-stage art review** in the footer, or open [the gallery directly](life-stage-review.html). Everything runs through local files with network access disabled. The older [animation, coral health and rock gallery](art-review.html) remains available.

The new gallery groups Fish, Corals and Bottom Feeders. Every implemented entry has four stage columns, each with alive and dead artwork, an enlarged preview, a gameplay-scale reference, right/left presentation, transparency/light/dark backgrounds, eye-anchor overlay and an optional movement preview. Review notes and explicit user approval choices use a separate local storage key; they do not edit the game save.

## Audited scope and delivery

- **27 implemented entries:** 18 fish in the Fish category, four benthic fish in Bottom Feeders, and five coral categories. The four benthic fish are included in the game's 22 fish definitions, not additional species.
- **216 authored stage/state images:** Egg, Baby, Juvenile and Adult, each Alive and Dead, in 27 transparent eight-frame atlases. Individual PNG exports accompany the atlases.
- **Five existing ART ONLY fish:** Niger triggerfish, Emperor angelfish, Red lionfish, Dogface pufferfish and Blue tang retain their earlier adult artwork. Their missing life stages are disclosed in the catalog; they have no gameplay definitions and are not counted as complete.
- **No new livestock added.** No snails, shrimp, hermit crabs, starfish, sea cucumbers or urchins were found in working content. Three named fictional proposals remain PLANNED. Six freshwater plants are outside this animal-livestock update.

See [CURRENT_LIVESTOCK_CATALOG.md](CURRENT_LIVESTOCK_CATALOG.md) for every ID, classification, stage status, source path and limits. Scientific names absent from game data have not been invented. The implemented corals are broad categories rather than exact species.

## What changed in the aquarium

Fish use their existing `growth` value: below 0.3 selects Baby, 0.3 through less than 1 selects Juvenile, and 1 selects Adult. Each dead fish selects its own stage's authored death pose, without applying a second upside-down transform. Movement, facing hysteresis, state, breeding and mortality continue to come from the existing simulation. Store/catalog thumbnails use the new adult art where available.

The approved adult Ocellaris animation and thumbnails remain assigned. Its earlier stages and dead states use this update. Its new adult stage plate is an unapproved study visible in the gallery, not a replacement of the approved adult animation. The legacy renderer and all earlier asset sources remain available as fallbacks and history.

External broods use species-specific egg icons. Internal livebearer gestation and protected mouthbroods no longer draw loose eggs on the substrate. This changes only their presentation. Guppy/platy Egg labels map to internal embryo equivalents. Coral early forms are gallery/future art support: this update adds no coral reproduction simulation. Existing coral health-state rendering, including bleaching and tissue loss previews, is preserved.

## Production and registration

Artwork was created with the built-in imagegen tool. Each species/category has its own brief and source sheet. The approved hybrid clownfish reference was inspected for style. Initial reference-conditioned outputs for the guppy and tetra sheets were reviewed; the guppy subject mismatch was rejected and a new guppy source created. A neon revision removed an inappropriate coral substrate from its freshwater eggs. Both originals remain preserved.

Packing performs transparent-gutter extraction, nearest-neighbor resampling, binary alpha and metadata registration. It does not draw replacement animals. The pleco's snout bristles required manually inspected pupil coordinates because automated dark-component detection chose the wrong detail. Eye patches remain sprite-local and transform with the animal through the shared SpriteKit boundary.

Each packed frame is 192 × 160 pixels. The eight-frame atlas is 1536 × 160. Metadata explicitly maps stages/states to frames, records bounds and eye landmarks, and declares static animation and pending approval. Embedded local PNG data keeps the canvas origin-clean under `file://` for previews and thumbnails.

Assets, original sources and exact prompts: [life-stage asset index](assets/livestock/life-stages/README.md). Developer packer: [prepare_life_stages.py](tests/prepare_life_stages.py).

## Verification

Chrome and Edge each passed:

- **214 life-stage/gallery checks**, including **2,160 directional rendering cases** across all 216 images, both directions and five raster sizes.
- **68 existing system checks and 69 existing UI/browser checks** after integration.
- All eight images per entry are distinct and nonempty, with transparent margins and binary alpha; no duplicated image is counted as a separate authored stage.
- Head-local eye samples remain visible at tested sizes; mirror pixels and canvas transform restoration agree.
- All 132 fish stage/state combinations reach the real tank renderer; 131 use new stage art and the one adult living Ocellaris retains its approved animation. All 66 dead combinations avoid double inversion.
- Gallery reviews survive reload as plain text. Gameplay save bytes remain unchanged by gallery use. The renderer does not mutate its input simulation state.
- Layouts fit 1440, 1024, 760 and 390 pixel viewports. No JavaScript exceptions or HTTP/HTTPS requests occurred.

Results: [Chrome](tests/chrome-life-stage-results.json), [Edge](tests/edge-life-stage-results.json). Screenshots: [fish](assets/previews/chrome-life-fish.png), [corals](assets/previews/chrome-life-corals.png), [bottom feeders](assets/previews/chrome-life-bottom_feeders.png), [mobile](assets/previews/chrome-life-mobile.png). All 27 entries were visually inspected in three contact sheets: [1](assets/previews/chrome-life-contact-1.png), [2](assets/previews/chrome-life-contact-2.png), [3](assets/previews/chrome-life-contact-3.png).

## Review limits and next step

Complete coverage means eight **static authored poses**, not finished animation sets or scientific validation of every larval feature. Swimming/turning previews translate and mirror those poses; dedicated fin cycles, turn frames and decomposition remain future work. Tiny brood icons cannot expose every detail visible in the enlarged egg artwork. Coral early forms are illustrative equivalents for the category-level definitions. Technical tests do not determine whether the style, anatomy or stage distinctions meet the user's artistic standard. No new artwork is automatically approved.

Permanent future rule: every new livestock entry needs all eight stage/state images. Future content expansion targets 25 new fish, five corals and five bottom feeders per update; no such expansion was added here.

**Stop for user art review. The next intended task, only after this update is reviewed, is clownfish-only refinement: visual polish, life stages, animation and final benchmark quality. That refinement has not begun.**
