# Physical equipment and object locations — schema 2

This is an additive local-save extension, `itemLocationVersion: 1`. It does not bump the base schema or create an account-wide equipment effects layer.

| Authority | Physical location |
|---|---|
| `tank.equipment[]` | Installed exclusively in that aquarium |
| `ownedEquipment[]` | Stored, uninstalled equipment instances |
| `tank.hardscape[]`, `tank.decorations[]`, `tank.mounts[]` | Placed exclusively in that aquarium |
| `ownedObjects[]` | Stored ordinary rock, decoration or glass frag rack; `kind` distinguishes them |
| `diving.rocks[]` | Existing recovered-rock storage, not duplicated into `ownedObjects` |
| `inventory` / `medicalInventory` | Existing supply quantities and medical batches; unchanged consumption/quality rules |

Installed equipment gains a persistent `id` through new-tank creation or an idempotent load migration. Existing IDs are preserved. Legacy missing equipment IDs are allocated using the saved entity counter while avoiding existing identities. Installed arrays are never copied to storage. Capacity, model, durability, switch state, modifications and any other existing fields remain attached to the instance. The migration initializes `ownedObjects: []` only if absent.

Equipment may have `temperatureTarget` from an individual heater/chiller control. Values must be finite and 18–30 °C. Legacy units without it retain the existing tank-target fallback; removal or transfer captures that source setting on the unit so a destination cannot silently change it. Changing a thermostat never assigns actual water temperature. The tank target remains the established replacement-water/default target.

`Core.act` moves authoritative memberships on a draft, checks compatibility and validates the entire save before commit. Equipment/object IDs share global entity-uniqueness validation with livestock and other assets. Duplicate IDs reject rather than deleting an item. Confirmation tokens prevent replay; a missing already-installed/removed ID also rejects an un-tokened repeat. Installed state is never inferred from ownership or selected aquarium.

Purchases use the existing stock, AC ledger, idempotency, local save and JSON export/import pipeline. Standard equipment retains the purchase-sizing capacity; fixed heater models never expand on transfer. Installation/removal do not generate purchase receipts. Profile storage is read only from the active profile’s state; stale inventory dialogs verify account identity.

Storage limits: equipment 50; ordinary objects 100; recovered rocks 80 under the existing diving validator. Stored object kinds reference existing catalog definitions; physical placement and attached-support safety revalidate before commit. No livestock or old breeding/history fields are removed. Local browser storage/export/recovery policies and their visible storage-failure warnings remain unchanged.

## Additive reliability extension

Equipment now carries `reliability.version=1` and a bounded per-item history; the profile has an equipmentReliability event ledger. These fields follow the exact physical ID and location without altering the schema 2 ownership contract. Migration preserves all original fields and current condition, adding unknown-prior-age tracking only when absent. Storage/transfer never rerolls thresholds or ages a disconnected device. See EQUIPMENT_RELIABILITY_SAVE_SCHEMA.md for every field, guard and history bound.

## October20 coordinated extension

equipmentParts stores rated spare quantities, separate from physical equipment identities. Pair offer IDs are reserved and checked in global identity validation until ownership transfers; bought previews clear. Whole-aquarium receipts retain historical IDs without creating owned duplicates; tanks may become empty with selectedTank empty string. All old item-location rules persist. Full fields are in ECONOMY_UPDATE_SAVE_SCHEMA.md.
