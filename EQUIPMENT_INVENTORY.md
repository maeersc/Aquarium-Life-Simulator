# Equipment Inventory

## UI polish and store quantities — 2026-10-22

Playable v4.3.1 / master v4.15. The familiar aquarium layout now uses a very subtle static downward fish-scale background, opaque slate-blue panels and consistent controls. The existing guarded store supports quantities for equipment, food, consumables, ordinary medicines, rated parts and rocks. Multiple rocks enter Inventory for separate placement; sensitive livestock, unique tools and installations retain their established individual safeguards. One total charge, distinct physical IDs, capacity/stock checks, persistent receipt replay protection and local saving remain authoritative. Main schema2/tutorial2, biological simulation, economy rates, offline time and freshwater lock are unchanged. STORE_QUANTITY_RULES.md defines category behavior; UI_POLISH_QUANTITY_REPORT.md records files, actual tests and limitations. Earlier release sections below are historical where superseded.

Equipment → Inventory is physical storage for the current local player profile. Only actually owned, uninstalled and unplaced items appear. Living fish, corals, eggs and other residents use Collection, receiving or approved quarantine instead. Installed equipment and placed rocks/decorations/racks are managed on their own aquarium; there is no Installed by Aquarium section in Inventory.

Search and category filtering combine. Existing product pixel previews, category, quantity, condition and fixed specifications are shown. Equipment remains one row per persistent instance. Existing care/fragging supplies stack only in their established quantity model; reusable fragging tools remain reusable. Remaining medical batches link to the existing medical inventory. Recovered diving rocks retain their existing inventory and sale authority. No products are invented.

Purchase equipment in Aquarium Store. The chosen aquarium sizes standard auto-sized equipment, while fixed heater models retain their listed rating. The purchase goes into Inventory and preserves the current aquarium selection. A purchase is not an installation or a source of aquarium life support.

Choose Install, review every owned destination and its compatibility, then confirm. Installation checks marine habitat, product habitat, actual volume versus fixed capacity, occupied type and equipment positions. Incompatible destinations remain listed, disabled, with reasons. A failed operation leaves storage unchanged. A removed unit can be installed elsewhere after the same checks.

Each aquarium uses only its installed equipment array. Removal/transfer warns about loss of life support; it does not neutralize the resulting temperature/chemistry risks. The same ID, condition, fixed capacity, model, enabled state, thermostat and modifications move with the unit. A disabled unit stays disabled until turned on. Storage never contributes capacity or consumes installed-equipment wear.

Removed rocks, decorations and frag racks return to storage with their original identity and attributes. Recovered rocks return through the diving-rock inventory. Coral/clutch attachments block removal until safely relocated or hatched. Ordinary stored rocks and decorations use the existing placement preview; a stored glass frag rack remounts with its original glass/position settings after destination confirmation. Existing purchases of rocks/decorations/racks retain their explicit direct-placement workflow.

Thermostats are configured in individual installed heater/chiller inspectors. Water temperature changes through the existing thermal simulation. Tank Care retains installed operation, service and removal; Food & Feeding retains current food forecasts. Tank History → Reports retains offline audit runs and mortality/chemistry evidence. Opening history does not create a report.

Storage bounds remain explicit: 50 equipment instances, 100 ordinary objects and the existing 80 recovered rocks. Existing quantities, handheld-tool durability limitations and product catalog remain unchanged. See [save schema](EQUIPMENT_INVENTORY_SAVE_SCHEMA.md) and [acceptance report](EQUIPMENT_INVENTORY_UPDATE_REPORT.md).

## Reliability state follows physical ownership

The same equipment instance retains condition, maintenance, component wear, tracked age, private failure thresholds and actual service history when removed, installed or transferred. Storage supplies no aquarium effects and accrues no powered wear. A beyond-repair unit remains owned and removable but cannot be installed as functioning life support. Legacy condition is never reset by migration. Installed-device care/history is documented in EQUIPMENT_MAINTENANCE.md; persistent fields in EQUIPMENT_RELIABILITY_SAVE_SCHEMA.md.

## October20 parts and whole-sale boundary

Matching rated new service-part quantities appear in Inventory and are consumed only by Replace Part. Stored gear/parts/supplies/objects and other aquariums are excluded from a whole-aquarium sale. Installed gear belonging to the sold tank transfers with it and remains historical rather than copied into storage. Zero owned aquariums is a valid profile; storage remains accessible. See EQUIPMENT_PART_CATALOG.md and WHOLE_AQUARIUM_SALES.md.

## Quantity delivery — v4.3.1

Each purchased equipment unit receives a different permanent ID and independent new reliability state, fixed/rated capacity and thermostat. A bulk order must fit all50 stored slots. Rocks bought in multiples enter the existing100-object ordinary storage; each piece is placed through existing compatibility/placement validation. Single rocks keep the established direct placement flow. No stored item supplies life support. Supply packs add their existing portions/doses; ordinary medical packs merge to1000 units per batch before creating further batches within the80-batch cap. Rated service parts remain stacks keyed by SKU and capacity, capped10000. All orders validate full stock, capacity and funds before commit.
