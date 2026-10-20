# Equipment reliability — additive schema 2 extension, version 1

Physical location continues to use EQUIPMENT_INVENTORY_SAVE_SCHEMA.md: each unique equipment ID belongs to exactly one installed tank or ownedEquipment storage. Reliability is attached to the same instance. Installation/removal/transfer never clones or resets it. Freshwater tank equipment retains its former biological/simulation behavior; freshwater remains locked.

## Per-instance reliability

`reliability.version=1`; `legacy` identifies unknown prior age; `baselineCondition` preserves condition when tracking began; `quality` is the existing optional item quality clamped to [0.5,1.5], default 1. `seed` (unsigned 32-bit), integer `draw`, positive `lifeThreshold` and `componentThreshold` persist private hazard sampling. Reload never rerolls valid metadata.

Nonnegative game-hour fields: `trackedHours` (installed), `operatingHours` (actual on-time), `effectiveHours` (normalized risk exposure), `maintenanceHours`, `componentStart` (exposure cursor after clearing/replacing a fault). `maintenance` is 0–100. `lastEnd` is null or the last processed authoritative game-minute timestamp, preventing overlap. `cycles` counts observed operating starts; `wasOperating` is a boolean. `warning`/`critical` prevent repeated dirt warnings until service.

`state` is working, temporary-malfunction, repair-required or beyond-repair; UI derives Off, Maintenance recommended and Reduced efficiency without adding incompatible state strings. `failurePart` is null or a valid component key for that equipment profile. `parts` contains exactly that profile's named component conditions (0–100). `failures` and `repairs` are nonnegative integer counters. `history` retains the latest 40 events for this physical device, even when moved/stored.

## Profile event ledger

`equipmentReliability={version:1,nextEvent:1,events:[]}`. The latest 600 events persist per profile. Each row includes a monotonically allocated `equipment-event-N` identity, equipmentId, type, tankId, tankName, authoritative game-minute time, kind (maintenance/repair/failure/maintenance-warning), factual message, condition, maintenance, state and operatingHours. Retention bounds do not reset nextEvent. Per-item history copies the actual event, not a new ownership record. A Tank History read never creates an event. Faults also feed the existing mortality equipment-event diagnostics; death snapshots include actual ID, reliability state, maintenance and operating status.

Save validation checks finite field ranges, known version/state/component keys, integer counters, lastEnd/event timestamps no later than saved game time, component cursor <= effective age, bounded histories and distinct ledger IDs below nextEvent. Invalid extensions reject rather than deleting, silently repairing or resampling equipment. The existing global physical-ID validator still prevents location duplication. Core actions operate on a draft, charge through the established AC ledger, validate and persist using the same local pipeline.

## Existing saves

Idempotent Inventory migration first allocates only missing physical IDs. Reliability migration then adds metadata only when absent. Current durability, existing IDs, capacity/model, condition, modifications, purchase records, enabled state, location, tank and thermostat remain untouched. New fields start future tracking at zero with neutral maintenance 100%; no past maintenance is invented. A legacy device at zero condition starts repair-required and stays zero unless the player explicitly pays for repair. That explicit legacy repair restores 25% chassis condition; normal repair restores only the identified component to 80%. No automatic refunds or livestock restoration occur.

Full local JSON round trips preserve thresholds, private draw cursor, histories and age exactly. Rendering and inspect/history queries are read-only. `lastEnd` and existing offline account checkpoints protect repeated catch-up; uninstalled gear is excluded from simulation. No server save, network dependency or player data is included in DIST or ZIPs.
