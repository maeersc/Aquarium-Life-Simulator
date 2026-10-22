# Life-stage asset index

Built-in imagegen created 27 species/category sheets for the audited implemented livestock. Sources, unsuccessful variants and revisions are preserved. User approval is pending.

The machine-readable [catalog](catalog.json) lists every ID and folder. Each folder contains:

- `source-v1.png`, with `source-v2.png` where revised. Guppy source-v1 is rejected because it depicted a clownfish; guppy source-v2 is used. Neon source-v2 removes a coral base from its eggs.
- `GENERATION_PROMPT.md` (initial brief), `FINAL_GENERATION_PROMPT.md` where the final subject-first prompt differs, and `REVISION_PROMPT.md` where applicable. The original cardinal prompt uses the inspected clownfish image as a style reference. The original neon prompt also used it; its revision uses the neon source as an edit target. Other final sources use a textual style brief based on the inspected reference.
- `egg_alive.png`, `egg_dead.png`, `baby_alive.png`, `baby_dead.png`, `juvenile_alive.png`, `juvenile_dead.png`, `adult_alive.png`, `adult_dead.png`.
- `atlas-v1.png`: eight 192 × 160 frames ordered alive Egg/Baby/Juvenile/Adult, then dead Egg/Baby/Juvenile/Adult.
- `metadata-v1.json`: explicit frame map, source crop rectangles, alpha bounds, head-local eye landmarks, category, implementation status, animation limits and pending approval.

Runtime loader: `js/life-stages.js`. Embedded PNG resource: `js/life-stage-data.js`. Rebuild from project root with `python tests/prepare_life_stages.py --pack`. The packer copies/samples generated pixels only; no procedural replacement animal art is painted. Source files are never overwritten by packing.

## Future content contract

Every new fish, coral, benthic animal, invertebrate or specialty livestock must provide Egg, Baby, Juvenile and Adult, each alive and dead. Biological equivalents such as internal embryo, larva, settled polyp and juvenile colony must be identified honestly. Juveniles require distinct anatomy/pattern development, not a resized adult. Eyes must remain attached in applicable stages and both swimming directions. Death is authored, static and non-gory.

Future expansion batch target: **25 fish + 5 corals + 5 bottom feeders**. Do not add a new batch without a requested livestock expansion. Do not double-count benthic fish in both category totals. Existing ART ONLY subjects and PLANNED proposals do not become implemented when artwork is produced.

Source data and finished static art completeness are separate from simulation support, animation completeness and user approval. All are recorded independently. The catalog and gallery must expose missing stages; no placeholder may be labeled finished. Preserve previous sources and review feedback when refining assets.
