# Clownfish collection and shared store delivery — 2026-10-12

Implemented the dedicated clownfish collection and the authorized shared store/mounting milestone. The full long-term master design is still incomplete. Open [clownfish-review.html](clownfish-review.html), [coral-placement-review.html](coral-placement-review.html), or the playable [index.html](index.html) directly from disk.

## Store behavior

The centered store keeps the aquarium visible behind a modal with fixed controls and scrolling cards. Exactly three main tabs and 7/7/6 subcategories use actual inventory. The selected aquarium appears in the header; opening, closing, changing product tabs and purchasing never automatically switch it. Explicit destination changes are saved. Incompatible animal purchases warn, disable commit and let the player explicitly choose an eligible owned aquarium. Fresh conditions are rechecked at commit; failed purchases and repeated submissions cannot spend twice. Supplies use shared inventory; equipment, rock, sand and decoration use the chosen aquarium. Equipment pricing follows destination volume. Existing Black Market access and containment restrictions remain.

## Coral mounting

Five existing coral categories now attach to permitted real rock tops, stable sandbed bases or mounted glass racks. Alpha collision geometry comes from the actual twelve rock images. Reject open water, solid interiors, boundary clearance and overlapping bases; care and LPS clearance produce explanatory conditional warnings. Save support IDs/local coordinates, carry colonies when supports move, block occupied support removal and revalidate sand-depth edits. Unsupported old placements retain ownership with a relocation notice. The isolated test scene exercises these actions without touching player storage. Click a rock or rack in gameplay to inspect/edit it. Coral inspectors retain Overview/Care tabs.

The three sand looks and 0–5 inch depth are saved visual habitat choices. New chemistry, displaced water-volume calculations, substrate fauna and maturation have not been added. Starter scenery still exists; completely dry construction remains future work.

## Clownfish and art

31 catalogued scientific names and 25 designer phenotypes, linked to base species. Existing Ocellaris ID `clown`, approved adult animation and historical sources are preserved. New original sources include 56 sheets plus two revised sheets. They pack 572 unique native 192 × 160 poses: 372 species poses and 200 designer poses. Designer eggs/larvae share base art explicitly; all 56 entries show eight living/dead stage views and four adult swim poses. All 57 implemented livestock catalog entries retain mapped full-stage support. Five earlier marine art studies remain art-only and disclose missing stages.

Engineering packing preserves transparency, complete fins and source files. Two fin-heavy sheets need connected-alpha component extraction because fin projections share column ranges while the animals remain physically separate. Dark-face eye coordinates and one closed juvenile eye are registered manually from source pixels. Other pupils use tighter component detection; adult cycles share canonical eye pixels sampled from the artist's sprite. Presentation restores transforms and mirrors the whole animal. No dedicated front-facing turns or complete carcass-decay animation is claimed. Dead poses are authored static states; existing mortality/pollution remains in the simulation.

The review gallery separates biological names/designer phenotypes, supports search/base filters, all stages/states, directions, frame controls, enlarged and actual-scale views, original/reference comparisons, care/sources, global audit and separately stored review notes. All new art is Provisional; only the user can approve it. Nine diagnostic contact sheets were inspected for packing, pose consistency and eye registration; precise anatomy and asymmetric pattern fidelity remain review subjects.

## Verification and boundaries

Taxonomy list/length measurements: [FishBase genus list](https://www.fishbase.org/identification/SpeciesList.php?genus=Amphiprion). Accepted names/synonyms: [WoRMS genus records](https://www.marinespecies.org/aphia.php?p=taxlist&tName=Amphiprion). Group husbandry and protandrous pair structure: [OATA clownfish care](https://ornamentalfish.org/wp-content/uploads/Clownfish-Sept-2022.pdf). Historical host/identity context: [Fautin and Allen field guide](https://www.meerwasserforum.info/file-download/95760/). Named breeder phenotypes: [ORA clownfish catalog](https://www.orafarm.com/products/fish/clownfish/); entry-specific links are retained in collection.json.

A listed name is not proof that hybrid origin is resolved: leucokranos and thiellei remain explicitly uncertain. Those two plus mccullochi, latezonatus and maohiensis are purchase-held until specialist care is verified. Species-specific lifespan is not verified; existing life scaling and minimum footprint recommendations are labeled game calibration/policy. Host lists are not invented. Mocha Storm, Mocha Ocellaris and Onyx appearances remain provisionally attributed. Designer genotype/inheritance is not modeled; base-species care and genetics stay authoritative. Established clownfish females no longer revert to male.

Freshwater definitions and 144 protected asset/source files are byte-identical. The simulation differs only in the marked marine clownfish pairing block; freshwater diet, care, growth, behavior and reproduction code is preserved. Shared safer purchasing changes are authorized and tested.

## Validation

Chrome and Edge each pass 68 current system checks, 88 shared-store checks and 7,583 collection/gallery/attachment checks. Machine-readable counts and results are in tests/*-store-results.json and tests/*-clownfish-results.json. Tests use isolated browser profiles, real file:// URLs and disabled network; no gameplay HTTP/HTTPS requests. Collection matrices cover 1,792 stage/size directional cases per browser, eyes at 25/52/73/117 pixels, transform restoration, exact mirroring, shared early pixels, four distinct swim frames, female invariants and duplicate-charge protection. Store tests cover all three tabs, chosen destinations, unsafe/stale purchases, modal focus/Escape, save reload, habitat actions and widths 1440/1024/760/390.

The original UI automation reflects an earlier full-page store and is retained as a historical fixture. Current default automation runs the current simulation and modal-store tests; --clownfish runs the new collection checks. Firefox remains unverified in this environment.

## Delivery gate

The consolidated MDP is revision 2.7 with its original 31 major sections, integrated scope/store/mounting/collection rules. This milestone stops for the user's visual review. No broader fish/coral/bottom-feeder expansion is begun. Portable ZIP retains local game, galleries, sources, metadata, prompts, documentation and current test reports.
