# Art update 1.1 — assets and exact prompts

## Ocean diving destination artwork — playable v4.0.2, 2026-10-16

Eight original pixel-art PNG environments replace the simplified expansion scenery for Indonesia, Philippines, Sri Lanka, Marshall Islands, Maldives, Australia, Florida and Mariana Trench. A central per-mode art mapping drives selection previews, proportional in-dive backgrounds and expedition-result accents. Older regional PNGs, native encounter pools, all diving gameplay, local saves and freshwater lock are preserved. See [DIVING_LOCATION_ART_REPORT.md](DIVING_LOCATION_ART_REPORT.md). Art is implemented for review; no prior livestock/art approval is changed.

## Daily livestock survival reward v3.4 - current rule, 2026-10-15

Players earn **100 AC** for every completed qualifying in-game day without a livestock death. The player must own eligible living marine livestock throughout the full simulated day. This is one account-wide payment, not one per aquarium. The separate healthy-aquarium award remains **50 AC**; both independently qualified awards total **150 AC**.

A confirmed fish, coral or bottom-invertebrate death cancels the current qualifying day and starts 1,440 game minutes of recovery. Another confirmed death restarts recovery. Recovery time cannot count toward a qualifying reward day. Illness or living coral bleaching is not a death. The authoritative game calendar remains 20 real minutes per day; legitimate offline catch-up processes the same conditions. Game windows do not stop simulation. Casino requirements apply only if that game is implemented.

Existing balances and actual historical ledger receipts remain unchanged. Every future survival payment is 100 AC through the existing financial service, with canonical account/transaction IDs, actual payment time and completed qualifying day/status. Local save, financial sequence and offline timeline guards prevent re-awarding a settled day. See [V34_UPDATE_REPORT.md](V34_UPDATE_REPORT.md) and [FINANCIAL_TRANSACTIONS.md](FINANCIAL_TRANSACTIONS.md).

## Earlier milestone material - superseded where inconsistent

## v2.9 — current implementation

Implemented the twelve-step saved/skippable saltwater tutorial with medical guidance, three-second selection outlines, disabled freshwater UI, separate +50 healthy / +100 survival rewards with persistent death/recovery tracking, Deep Market display rename, local asset-value leaderboard preview, exact 15,000-US-gallon / 5,000-AC aquarium, proportional water-change salt consumption, independent mystery products and the approved 35-species marine batch. Saves remain local to each player's browser on their PC. The bottom mystery product is content-held because its Legendary host specialist is not eligible. See [V29_UPDATE_REPORT.md](V29_UPDATE_REPORT.md) for actual checks, care/art limits and release details. Earlier milestone sections below are historical wherever superseded.

See [the current release report](V29_UPDATE_REPORT.md), [new art gallery](v29-review.html), [DIST](DIST/) and [build manifest](DIST/build-manifest.json).

## Historical milestone record


## October 12 collection generation — 2026-10-12

Built-in image generation produced 56 preserved source-v1 sheets under assets/livestock/fish/clownfish/species and designer, plus source-v2 revisions for Longfin Ocellaris and Lightning Maroon. GENERATION_PROMPT.md files, collection metadata and tests/clownfish-generation-jobs.json preserve briefs. Packing exports native192x160 poses, individual stage/swim PNGs, atlases and metadata; no API keys or runtime image services. Transparent-alpha extraction, nearest-neighbor packing and existing artist-eye sampling are engineering operations. Nine diagnostic contact sheets are in assets/previews. All new artwork is provisional, and original approved Ocellaris art remains assigned.


Current life-stage assets and exact prompts are indexed in [assets/livestock/life-stages/README.md](assets/livestock/life-stages/README.md). The record below preserves the earlier art 1.1 sources.

Method: **built-in imagegen**, using `assets/reference/approved_clownfish_hybrid.png` as the style reference and requesting transparent outputs. Source outputs and edit revisions are preserved. Python/Pillow scripts only pack/sample the generated images; JavaScript performs registered sprite-component rendering. No external generator or network asset is required during play.

## Fish atlases (192 x 128 per frame, four frames)

- [Niger triggerfish atlas](assets/livestock/fish/niger-triggerfish/atlas-v11.png), [prompt](assets/livestock/fish/niger-triggerfish/GENERATION_PROMPT.md).
- [Emperor angelfish atlas](assets/livestock/fish/emperor-angelfish/atlas-v11.png), [prompt](assets/livestock/fish/emperor-angelfish/GENERATION_PROMPT.md).
- [Red lionfish atlas](assets/livestock/fish/red-lionfish/atlas-v11.png), [prompt](assets/livestock/fish/red-lionfish/GENERATION_PROMPT.md), [cutout revision](assets/livestock/fish/red-lionfish/CUTOUT_PROMPT.md).
- [Dogface puffer atlas](assets/livestock/fish/dogface-puffer/atlas-v11.png), [prompt](assets/livestock/fish/dogface-puffer/GENERATION_PROMPT.md), [cutout revision](assets/livestock/fish/dogface-puffer/CUTOUT_PROMPT.md).
- [Blue tang atlas](assets/livestock/fish/blue-tang/atlas-v11.png), [prompt](assets/livestock/fish/blue-tang/GENERATION_PROMPT.md), [cutout revision](assets/livestock/fish/blue-tang/CUTOUT_PROMPT.md).
- [Preserved clownfish atlas](assets/livestock/fish/clownfish/clownfish-benchmark-v1-128.png), [original prompt](assets/livestock/fish/clownfish/GENERATION_PROMPT.md).

## Coral atlases (192 x 192 per frame, five states / two poses)

- [Zoanthids](assets/livestock/corals/zoa/atlas-v11.png), [prompt](assets/livestock/corals/zoa/GENERATION_PROMPT.md), [tissue-state revision](assets/livestock/corals/zoa/REVISION_PROMPT.md).
- [Mushrooms](assets/livestock/corals/mushroom/atlas-v11.png), [prompt](assets/livestock/corals/mushroom/GENERATION_PROMPT.md), [tissue-state revision](assets/livestock/corals/mushroom/REVISION_PROMPT.md).
- [SPS](assets/livestock/corals/sps/atlas-v11.png), [prompt](assets/livestock/corals/sps/GENERATION_PROMPT.md).
- [LPS](assets/livestock/corals/lps/atlas-v11.png), [prompt](assets/livestock/corals/lps/GENERATION_PROMPT.md).
- [Soft leather](assets/livestock/corals/soft/atlas-v11.png), [prompt](assets/livestock/corals/soft/GENERATION_PROMPT.md).

## Rock atlases (192 x 192 per variant, four variants)

- [Fiji](assets/livestock/rocks/fiji/atlas-v11.png), [prompt](assets/livestock/rocks/fiji/GENERATION_PROMPT.md).
- [Caribbean](assets/livestock/rocks/caribbean/atlas-v11.png), [prompt](assets/livestock/rocks/caribbean/GENERATION_PROMPT.md), [cutout revision](assets/livestock/rocks/caribbean/CUTOUT_PROMPT.md).
- [Hawaiian volcanic-inspired](assets/livestock/rocks/hawaiian/atlas-v11.png), [prompt](assets/livestock/rocks/hawaiian/GENERATION_PROMPT.md).

Each directory contains `metadata-v11.json`, `source-v1.png` and any selected `source-v2.png` revision. [prepare_art_update.py](tests/prepare_art_update.py) reproducibly packs the atlases and creates the classic local `js/art-assets-data.js` resource with embedded PNGs for origin-clean file-URL canvas operations.




## Livestock expansion v2.7 — generation record

2026-10-14: Built-in ImageGen produced 38 transparent species sheets plus three corrective wrasse edits. Source masters and prior versions are preserved in assets/expansion-v27/<id>/. The technical packer detects alpha gutters, nearest-neighbor scales and packs eight authored views without semantic repainting. All 304 views load offline. Prompts/correction notes: [art-prompts.json](tests/expansion-evidence/art-prompts.json). All new art is unapproved; twelve framing flags, provisional eyes and unsupported invertebrate egg/planktonic larval artwork are explicitly recorded in [the report](LIVESTOCK_EXPANSION_REPORT.md). Review [the gallery](expansion-review.html).


## Ocean Diving v2.8

Nine original built-in ImageGen assets and full prompts are preserved under assets/diving/. They include eight region/mode backgrounds and a transparent equipment/diver/boat sprite sheet. All remain unapproved. Existing approved benchmark and livestock assets are preserved. Packing preserves the original sources, detects equipment alpha gutters, and uses nearest-neighbor technical atlas packing/base64 embedding; see DIVING_UPDATE_REPORT.md and assets/diving/art-prompts.json.


Equipment framing correction: the generated boat crossed a nominal source cell boundary. The preserved source was technically packed into `assets/diving/equipment-atlas-v1.png` using alpha gutters; `equipment-atlas-metadata-v1.json` records all eight source bounds. Icons retain their source aspect ratios. No semantic repainting or source overwrite occurred.
