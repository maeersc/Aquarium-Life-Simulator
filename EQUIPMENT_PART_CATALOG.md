# Serviceable equipment part catalog

The former catalog had no replacement-part prices. This authorized update adds these explicit new-part entries to AL.Data.parts and Aquarium Store → Equipment → Replacement Parts, using existing part families rather than pretending a whole unit is an impeller.

| SKU | Supported equipment/component | Base new-part AC |
|---|---|---:|
|flow-impeller|Circulation pump / impeller|45|
|filter-impeller|Filter / impeller|50|
|skimmer-intake|Skimmer / intake assembly|55|
|skimmer-pump|Skimmer / service pump|95|
|air-diaphragm|Air pump / diaphragm|20|
|feeder-dispenser|Feeder / dispensing cartridge|60|
|dosing-tubing|Dosing / tubing set|35|

These are documented game catalog prices introduced under the requested missing-part audit, not claims about manufacturer prices. Rated variants use exactly ceil(base price×max(1,rated liters/equipment base liters)), matching the existing rating convention. The Store and inspector call the same product function and charge the same integer price. No substitution of full-unit price, markup or discount occurs. SKU and exact rating must match an owned part before consumption. All initial per-SKU store stock is 30 and follows the authoritative game-day restock; no part is granted to old accounts.

Generic sealed heaters/LED fixtures/chillers, electronics and unlisted motors/housings do not receive invented replaceable internals. A matching fault in a supported part can be resolved; unrelated faults and chassis wear remain. Zero-condition and beyond-repair devices need whole-unit replacement. Maintenance removes dirt and preserves bacteria/physical wear; a purchased or owned part renews only itself to100%. The original multi-year exposure/hazard model, time scaling and fixed heater ratings remain intact. Maintenance fee coefficient is unchanged. See EQUIPMENT_MAINTENANCE.md and the schema.
