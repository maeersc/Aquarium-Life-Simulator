# Aquarium Life — art direction: clownfish collection review

## Global marine fish animation audit — playable v4.0.3, 2026-10-16

Audited all 94 registered marine fish, including five acquisition-held clownfish and one fictional fish. Thirty-one have authored adult cycles; 63 previously translated static living poses. Added render-only species profiles, pixel-preserving tail/outer-fin motion, state-aware timing, banked side-profile turns and head/eye protection across three stages. No new biological species, AI/feeding/breeding rules, inheritance or saves are introduced. All 94 remain conservatively classed B (partial) because bespoke action/turn/pectoral artwork and anatomy approvals remain incomplete; this is not a claim of fully authored animation. See [FISH_ANIMATION_AUDIT.md](FISH_ANIMATION_AUDIT.md), [FISH_ANIMATION_SYSTEM.md](FISH_ANIMATION_SYSTEM.md) and [offline motion review](fish-animation-review.html).

## Ocean diving destination artwork — playable v4.0.2, 2026-10-16

Eight original pixel-art PNG environments replace the simplified expansion scenery for Indonesia, Philippines, Sri Lanka, Marshall Islands, Maldives, Australia, Florida and Mariana Trench. A central per-mode art mapping drives selection previews, proportional in-dive backgrounds and expedition-result accents. Older regional PNGs, native encounter pools, all diving gameplay, local saves and freshwater lock are preserved. See [DIVING_LOCATION_ART_REPORT.md](DIVING_LOCATION_ART_REPORT.md). Art is implemented for review; no prior livestock/art approval is changed.

## Global diving expansion and liquidation — playable v4.0, 2026-10-16

Implemented the authorized Emergency Diving Sales & Rock Resale and Global Ocean Diving Expansion request (specification v3.6). Seven new reef selections and Mariana remote exploration use the central registry. Catch development, medical assessment, concealed attached eggs and regular-store liquidation extend the existing receiving authority. See [DIVING_EXPANSION_REPORT.md](DIVING_EXPANSION_REPORT.md) and [DIVING_EXPANSION_SAVE_SCHEMA.md](DIVING_EXPANSION_SAVE_SCHEMA.md). Earlier milestone reports remain historical where superseded. All saves stay local; freshwater remains locked; one game day remains 20 real minutes.


## Equipment filters, inspector research and The Dock Casino - v3.7 current

Implemented the equipment-category dropdown and original fragging-tool previews, moved paid species research to living owned-fish inspectors, and added the authorized seventh sidebar entry The Dock Casino with playable Gold Fish and Predator & Prey. All wagers and returns use the existing account wallet/ledger and saved round authority; all research remains 5 AC once per canonical species. The aquarium header controls share the information-column grid and align to its actual panel edge. See STORE_CASINO_UPDATE_REPORT.md and CASINO_RULES.md for the release, verified probabilities, local persistence and limitations. Existing biological simulation, 20-minute day, rewards, freshwater lock, livestock/art approvals and local saves remain. Earlier release sections are historical where superseded.

## Daily livestock survival reward v3.4 - current rule, 2026-10-15

Players earn **100 AC** for every completed qualifying in-game day without a livestock death. The player must own eligible living marine livestock throughout the full simulated day. This is one account-wide payment, not one per aquarium. The separate healthy-aquarium award remains **50 AC**; both independently qualified awards total **150 AC**.

A confirmed fish, coral or bottom-invertebrate death cancels the current qualifying day and starts 1,440 game minutes of recovery. Another confirmed death restarts recovery. Recovery time cannot count toward a qualifying reward day. Illness or living coral bleaching is not a death. The authoritative game calendar remains 20 real minutes per day; legitimate offline catch-up processes the same conditions. Game windows do not stop simulation. Casino requirements apply only if that game is implemented.

Existing balances and actual historical ledger receipts remain unchanged. Every future survival payment is 100 AC through the existing financial service, with canonical account/transaction IDs, actual payment time and completed qualifying day/status. Local save, financial sequence and offline timeline guards prevent re-awarding a settled day. See [V34_UPDATE_REPORT.md](V34_UPDATE_REPORT.md) and [FINANCIAL_TRANSACTIONS.md](FINANCIAL_TRANSACTIONS.md).

## Earlier milestone material - superseded where inconsistent

## v3.3 current release - 2026-10-14

Implemented the authorized v3.1 coral fragging/trading, v3.2 financial dashboard and v3.3 Marine Research Center. Equipment has three reusable coral tools and two mounting consumables; eligible parents produce independently simulated, mounted clones with tissue loss, recovery and lineage. Diving livestock can use regular or Deep Market dealers; regular pays floor(0.60 x the same Deep reference), and Deep requires Reputation 5 plus an active wanted request. Wanted Livestock remains separate from exactly four rotating dealer stock slots.

The AC button opens a reconciled, persisted financial history. Existing wallets migrate unchanged; new profiles start at the requested 5,000 AC. Saltwater Research and the existing Encyclopedia share permanent 5-AC canonical-species unlocks. All 94 marine fish are indexed; 93 real species are researchable, one fictional entry is preview-only. Fully verified dossiers: 0; incomplete: 93; five have reviewed biological annotations. Partial content is disclosed before purchase. See [V33_UPDATE_REPORT.md](V33_UPDATE_REPORT.md), [FINANCIAL_TRANSACTIONS.md](FINANCIAL_TRANSACTIONS.md) and [RESEARCH_SOURCES.md](RESEARCH_SOURCES.md).

Saltwater-only scope, safe persistent store destinations, local PC/browser saves, existing rewards/odds, all old livestock and artwork approvals/holds remain. No new biological species or art assets were added. Full printable continuity source is updated; binary PDF regeneration remains pending. Current playable version v3.3 / consolidated MDP v3.6.

This update creates no new raster art and approves no prior artwork. Fragments reuse their parent's existing biological artwork at individual size. Research uses existing catalog thumbnails. All old stage, framing, sex/reference and animation limits remain as recorded in the v2.7/v2.9 reports.

## Earlier milestone record - historical where superseded

**Authorized 2026-10-14:** The user approved the complete 25/5/5 roster and rarities, confirmed saltwater-only, and explicitly requested "Implement v2.9". Roster approval and artwork approval are separate; new artwork remains unapproved. [Authorization](planning/v2.9/approval.json).

## v2.9 — current implementation

Implemented the twelve-step saved/skippable saltwater tutorial with medical guidance, three-second selection outlines, disabled freshwater UI, separate +50 healthy / +100 survival rewards with persistent death/recovery tracking, Deep Market display rename, local asset-value leaderboard preview, exact 15,000-US-gallon / 5,000-AC aquarium, proportional water-change salt consumption, independent mystery products and the approved 35-species marine batch. Saves remain local to each player's browser on their PC. The bottom mystery product is content-held because its Legendary host specialist is not eligible. See [V29_UPDATE_REPORT.md](V29_UPDATE_REPORT.md) for actual checks, care/art limits and release details. Earlier milestone sections below are historical wherever superseded.

35 original generated species sheets / 280 static stage-state views are integrated, with source originals, prompts, atlases and metadata. All remain NOT USER APPROVED. Original approved Ocellaris clownfish art and older batches are preserved. Five contact pages were visually inspected. One source-boundary flag (Yellow scroll coral adult), provisional eye-coordinate metadata, static poses and stylized earliest developmental equivalents are disclosed. Do not claim validated captive breeding, sex-specific poses or full animation. Review [v29-review.html](v29-review.html).

## Earlier milestone record




## Ocean Diving v2.8 — current, 2026-10-14

MDP **v3.3**, retaining all 31 major sections. **Ocean Diving** beside Keeper Level opens Reef (Level 5 / 1,000 AC) or Deep Sea (Level 10 / 10,000 AC). Fiji, Caribbean, Hawaii and Japan have original regional scenery and a compact playable map. W/A/S/D, arrows and on-screen buttons move one tile; every successful step costs exactly 5% oxygen from 100%. Blocked movement and collection clicks cost none. Eight temporary slots become owned only on a successful boat return with oxygen remaining. Exhaustion/confirmed abandonment forfeits discoveries without a fee refund.

Aquariums continue at 1× during planning, diving and results, using the existing 20-real-minute game day. Explicit safe receivers, supported coral mounts, species-conditioned survival, finite transport holding, persistent provenance and Reputation 5 Black Market-only resale are integrated. Confirmed paid Black Market purchases earn bounded reputation; canceled/failed/duplicate transactions do not. Direct normal-store livestock is restricted to Tiers 1–3; eight daily Fish slots and independent Mystery Egg odds remain unchanged. Nominal tank/equipment capacities now ceil to whole US gallons; physical liters and precise water-change calculations remain exact.

**No new biological species.** The approved 38-entry v2.7 batch and all protected freshwater content remain the roster baseline. Six sourced encounter profiles reference existing IDs; Hawaii wildlife is observation-only, and unsupported regional/depth combinations offer inert fictional salvage rather than invented animals. All captures are fictional restricted game recovery, not real collection authorization. New art is unapproved pending user review. Saves and expedition receipts remain on each player's PC in browser storage. See [DIVING_UPDATE_REPORT.md](DIVING_UPDATE_REPORT.md) and [the region ledger](assets/diving/registry.json). DIST is rebuilt through `python build.py`. Earlier milestones below are historical where superseded.

Built-in ImageGen created original source-v1 PNGs under `assets/diving/`: Fiji/Caribbean/Hawaii/Japan reef and deep backdrops plus one transparent 4×2 equipment atlas (diver, boat, oxygen cylinder, rock, sparkle, mask, transport crate, buoy). `js/diving-art-data.js` embeds those files for offline use. Regional scenery avoids generic culture symbols and generic final livestock silhouettes; live encounters reuse the existing species-specific expansion art. The approved clownfish reference was inspected and preserved. The supplied sprite is a static authored pose moved by the minigame; no separately authored swimming cycle is claimed. Sources are not overwritten. Art remains unapproved. Full prompts and original generated filenames are preserved in `assets/diving/art-prompts.json`; packing preserves original sources and uses detected alpha gutters, nearest-neighbor atlas packing and base64 embedding, with a technical contact sheet for QA.

## Livestock expansion v2.7 — roster baseline milestone, 2026-10-14

MDP **v3.2** retains exactly 31 major sections. Added **38 unique marine entries: 28 fish, five named stony corals and five non-fish invertebrates**. All 38 passed the pre-registration scientific-name/synonym duplicate audit; none were skipped. The runtime now has **80 fish (69 marine, 11 protected freshwater), ten marine coral entries and five non-fish invertebrates**. The six existing freshwater plants are unchanged. Existing art-only and planned entries are excluded from these totals.

All six Mystery Egg rarity pools are now populated; the earlier empty-pool content hold is superseded. Keep independent 50/25/15/7.5/2/0.5 percent odds, 600 AC, three daily eggs, existing level/incubation gates and safe-destination checks. Daily Fish shopping remains exactly eight visible slots: 3 Common, 3 Uncommon, 1 Rare, 1 Mystery Egg. Higher tiers do not add normal Fish cards. Fixed retail, persistent selected aquarium, continuous offline simulation, rarity/genetics and existing specialist clownfish holds remain.

New livestock has inspectors, rarity, care information, value, host-filtered health compatibility and additive save support. Corals use player-selected supported rock/rack placement. Invertebrates are separate bottom residents with feeding, crawling/filtering, condition, death and transfer records. Their egg/planktonic larval reproduction and art are unsupported. New fish natural breeding is enabled only for the five explicitly supported profiles; Mystery Egg development is a simplified game presentation, not evidence of complete captive culture.

There are 38 new transparent sprite sheets / 304 static stage-state views. All are unapproved; 12 sheets carry explicit framing review flags. Existing approved artwork is preserved. Review [the new artwork gallery](expansion-review.html). [Implementation report](LIVESTOCK_EXPANSION_REPORT.md), [permanent registry](assets/expansion-v27/registry.json), [continuity source](PROJECT_CONTINUITY_SOURCE.md) and [PDF workflow](PDF_WORKFLOW.md) record the limits. **PDF regeneration remains pending: PDF authoring/rendering prerequisites are unavailable in this environment.** Earlier milestone material is historical where superseded.

### v2.7 art integration and honest coverage

One original transparent sheet per species, with source masters preserved under `assets/expansion-v27/<id>/`. Fish map egg, larva, juvenile and adult alive/dead. Corals map living/dead frag, young colony, stressed colony, mature colony, living bleaching, tissue loss and bare skeleton. Invertebrates map early settled juvenile, small juvenile, larger juvenile and adult alive/dead; these are not mislabeled as eggs or planktonic larvae. Source correction v2 removes inappropriate fin filaments on Pink-streaked, White-banded Possum and Tanaka's Pygmy Wrasse; v1 files remain archived.

`metadata-v1.json` records native direction, frame bounds, provisional eye registration, source hash, framing flags and approval=false. The technical packer detects transparent gutters and uses nearest-neighbor sizing; it does not repaint generated imagery. Twelve automatic boundary flags require visual review and are listed in the expansion report. Fish use static authored stages with existing runtime movement/mirroring; no new fin-cycle animation is claimed. Flasher/fairy adult references depict males, Boxfish depicts a female reference; alternate sex artwork is not supplied. All new art remains subject to user approval. Generation prompts and correction notes are in `tests/expansion-evidence/art-prompts.json`.

## Rarity, genetics and continuous ecosystem — v2.5/v2.6 (historical milestone)

At this historical milestone, MDP **v3.1** retained the same 31 major sections. Six original colored rarity icons are shared by livestock inspectors, shops, collection, encyclopedia and breeding. Daily Saltwater Fish shopping has exactly eight saved slots (3 Common, 3 Uncommon, 1 Rare, 1 Mystery Egg), fixed normal prices and a countdown. Selected aquarium and purchase safety remain persistent.

Time now continues while away: 20 real minutes = one game day, with all elapsed time processed in responsive batches. Actual ecosystem conditions determine survival and 50-AC healthy-day eligibility; the old relaxed/capped/no-offline-reward policy is superseded. Return reports show real simulation results. Imports cannot replay an older locally recorded timeline.

Marine pattern identities persist through breeding, growth, turning, transfer and reload. Natural Ocellaris inheritance uses the approved 85/10/4/1 gameplay distribution; new Snowflake reference-line stock supports the documented limited model. Existing approved art and freshwater biology are preserved.

**Historical v2.6 limits (superseded by v2.7):** Mystery Egg sales were held because Very Rare, Ultra Rare and Legendary pools are empty; exact odds remain visible and no substitution is made. Other unverified designer genetics remain on a visible breeding hold. Existing provisional artwork and simplified biological models remain provisional. See [ECOSYSTEM_UPDATE_REPORT.md](ECOSYSTEM_UPDATE_REPORT.md) for actual tests, files, screenshots and remaining limitations, and [RARITY_GENETICS_RESEARCH.md](RARITY_GENETICS_RESEARCH.md) for assignment/genetics evidence. Earlier milestone sections below are historical wherever their offline/store policy conflicts with this update.


## Gameplay, time and settings v2.4 — 2026-10-13 (historical milestone)

The current consolidated specification is **MDP v3.0**, retaining exactly 31 major sections. Aquarium capacities and requirements display US gallons using 3.785411784 L/gal; saved physical liters are unchanged. Field Journal separates Saltwater/Freshwater encyclopedia categories and adds Keeper Progress through the clickable level badge. Store title, destination, balance and X now share a compact header.

Settings offers saved 12/24-hour formatting and Windowed/Fullscreen/Borderless Fullscreen preferences. Fullscreen uses the browser API after a click; Borderless is explicitly its browser equivalent, not native OS borderless. Coral, rock and decoration previews support wheel depth (up back/down front), PageUp/PageDown, valid support constraints and persistent z layering. Marine eggs retain aquarium/parent identities, care/exposure metadata and centralized value; attached eggs follow support depth, pelagic eggs drift, protected broods remain internal. Existing artwork and freshwater biology stay unchanged.

At 1×, 20 real minutes make one game day. A full observed healthy day earns exactly 50 AC per player, independent of tank count; up to 30 game minutes of minor variation is tolerated, while severe crises block the day. Empty-only collections and offline catch-up cannot earn it. Existing energy costs and showcase income remain separate. Saved care checkpoints prevent repeat claims. Welcome Back now requires Continue before simulation/catch-up/saving; Start Over requires confirmation and offers backup export. Unreadable saves remain protected.

See [GAMEPLAY_UPDATE_REPORT.md](GAMEPLAY_UPDATE_REPORT.md) for the 45-item acceptance mapping, actual browser results, screenshots, migration policy and limitations. Earlier dated sections below are historical where they conflict with this update.


## Main UI / egg presentation — 2026-10-13

The approved aquarium artwork, fish sprites, eye registration and facing rules are preserved. New shell and dialogs use the locked near-black/slate/aqua palette. The canvas retains its exact 2:1 shape; no crop/stretch is used to fit the viewport. TOTAL AQUARIUM VALUE belongs above the water, clear of livestock/scenery. New empty/dry tank framing uses simple local Canvas forms only.

Marine egg placement reuses existing alive/dead stage art. Developing hard-surface clutch framing runs approximately 5–12 logical scene pixels; magnified egg-inspector framing runs 5–25, with local nearest-neighbor scaling. These are cluster/readability measures, not a claim that individual eggs enlarge fivefold. Pelagic egg glyphs remain small; internal broods are not drawn on sand. Larvae continue through the existing art pipeline. No atlas/reference/source artwork was replaced and no freshwater art was developed. Premium sections show actual existing artwork as clearly labeled references or honest unimplemented empty states, without inventing approved exclusive assets.

Active milestone: the dedicated 31-name / 25-phenotype marine collection, full stage/death mapping and four adult swim poses per entry. Existing approved adult Ocellaris, historical sources and protected freshwater assets remain intact. New art is provisional. See CLOWNFISH_STORE_REPORT.md and clownfish-review.html.

## Permanent life-stage and content-batch rules

Every new livestock entry, including fish, corals, bottom feeders, future invertebrates and specialty animals, must supply Egg, Baby, Juvenile and Adult artwork in both alive and dead states. Internal biological terms may differ (embryo, fry, larva, polyp, frag), but all eight stage/state slots must be mapped. Lack of simulation support never excuses silently omitting art. Record missing work explicitly.

Eggs must distinguish viable and failed forms. Livebearer Egg equivalents are internal embryos. Babies require immature anatomy; juveniles require developing fins/patterns or colony structure, not simple adult scaling. Stony coral death can reveal skeleton; soft-bodied coral death collapses tissue. Bleached living tissue is not dead remains. Preserve correct eye detail and species identity without gore.

Future livestock expansion target: 25 new fish + 5 corals + 5 bottom feeders per content update. The dedicated 31-name / 25-phenotype clownfish collection is an explicit user-authorized exception; broader batches remain gated. Counts must distinguish IMPLEMENTED, ART ONLY, DATA ONLY and PLANNED and must not double-count benthic fish.

Current delivery: 27 eight-frame life-stage atlases, 192 × 160 pixels per frame, plus individual PNGs. Static poses use explicit source rectangles and per-stage/state eye anchors. Corpses already have authored poses and must not be inverted again. Fish art selects existing growth thresholds; coral early stages remain review-only. Approved adult Ocellaris animation and existing adult coral health-state art remain active. Other fish now use the new stage poses, with prior procedural art preserved as fallback.

The new [life-stage gallery](life-stage-review.html) is linked from index.html and includes enlarged and gameplay-scale comparisons for Fish, Corals and Bottom Feeders. New metadata starts `approved: false`; explicit user review alone sets a gallery approval choice. See [the report](LIFE_STAGE_ART_REPORT.md) and [complete livestock audit](CURRENT_LIVESTOCK_CATALOG.md).

After this submission, stop for user review. The authorized clownfish collection is now implemented; further anatomy/style refinement follows the user's review.

The following sections retain the earlier art 1.1 production rules. Where source geometry or runtime assignment differs, the life-stage rules above take precedence. Earlier animation sheets and galleries remain available.

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

### Current rarity assets and pattern treatment

assets/rarity/1.svg–6.svg are original 64×64 transparent code-native pixel silhouettes; mystery.svg is the original product egg. No existing raster artwork was overwritten. Deliberate stepped colors preserve the locked tier palette, with 30–40px UI icons and adjacent readable labels. Natural offspring bar changes are cached per immutable seed/frame/stage and applied before mirroring; the head, eyes, fins and alpha outline remain untouched. Legacy catalog art is passed through exactly. The approved reference remains assets/reference/approved_clownfish_hybrid.png.


Equipment framing correction: the generated boat crossed a nominal source cell boundary. The preserved source was technically packed into `assets/diving/equipment-atlas-v1.png` using alpha gutters; `equipment-atlas-metadata-v1.json` records all eight source bounds. Icons retain their source aspect ratios. No semantic repainting or source overwrite occurred.
