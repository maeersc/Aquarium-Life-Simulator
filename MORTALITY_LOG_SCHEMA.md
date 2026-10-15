# Aquarium Life - permanent mortality journal schema

Current: playable v3.6 / MDP v3.9, 2026-10-15. The permanent rule is authoritative in MDP 24.9. This document describes its serialization; it does not introduce a second logger.

## Storage and migration

The existing schema-2 game retains `mortality.version: 1`, `next` and its original event objects. Add `journalVersion: 1`, monotonic `steps` and recent `runs`. Each new detailed event has `schemaVersion: 2`. Old v1 events retain their original IDs and evidence without invented missing fields. Marine tanks add `mortalityHistory.samples` and `mortalityHistory.events`. Existing equipment may optionally have a validated fixed `heaterModel`; untagged equipment remains legacy with its exact capacity.

The dedicated local journal uses keys:

```
aquarium-life-mortality-v2:<encoded account ID>:event:<encoded event ID>
aquarium-life-mortality-v2:<encoded account ID>:run:<encoded run ID>
```

Each envelope is `{version:2, accountId, event}` or `{version:2, accountId, run}`. These records are separate from the main `aquarium-life-v2` game save. Persisted events are immutable and never automatically pruned. Runs update from running to completed/error under their same ID. The browser account ID is the existing local financial identity, not an online login or credentials.

The game carries the latest 200 durably archived events / 20 runs for portable backup, plus **every record that could not be durably archived**. A failed write never justifies dropping a pending record. Warn in the UI and retain pending data for a normal game save/export/retry. Never overwrite an unreadable journal entry. Browsers impose finite storage: quota or blocked storage may also prevent a full game save; export local JSON before closing. Clearing site data or losing a browser profile can erase local data. No cloud recovery is supplied.

Loading an old valid game archives its retained old events. A new loss has canonical ID `<account>:death:<individual ID>`, so a stale replay cannot manufacture a second event for the same individually modeled life. `deathRecordId` and the existing `survivalLossRecorded` guard also prevent repeated notifications/penalties. Original v1 sequence IDs remain unchanged. The existing local timeline and finance guards still restrict older imports; the journal is diagnostic evidence, not cryptographic anti-cheat.

## Detailed event fields

| Group | Recorded fields |
|---|---|
| Identity | account/event/individual/species IDs, common and scientific name where known, category, rarity, stage, age and units, aquarium ID/name |
| Time | actual simulation time, day/time, interval start, global step, live/offline context, run ID, mapped real timestamp and separate capture timestamp |
| Health | health immediately before fatal update when observed, health after, maximum 100, applied fatal health loss, stress, conditions and medication, behavior, last observed healthy timestamp |
| Nutrition | actual hunger/nutrition, last consumed meal and elapsed game minutes, compatible inventory stocks and exhaustion flag |
| Cause | named model trigger or terminal damage contributions, cause category, contributing channels and explicitly model-based certainty; Unknown when unavailable |
| Environment | exact death-step full chemistry, heater target, actual volume, bacterial populations, canonical bioload before/after where observed, equipment/model/condition/operation and thermal output |
| Coral/bottom | tissue, bleaching, polyps, light/flow/nutrients; compatible benthic diet, substrate and finite forage |
| History | preceding sampled individual health/hunger/nutrition/highest disease severity with water/heater state, and recent relevant feeding/health/equipment/control/water-change events |

Offline real time maps the simulated death to checkpoint + elapsed game minutes / 1.2 * 1000 ms. It is **not** the login time. Live records use actual capture wall time. Clock rollback follows existing no-negative-progression rules; timestamps depend on the player's device clock. Maximum temporal precision remains the actual simulation interval (at most five game minutes). Samples are hourly and rounded for compact resident trends; full death chemistry remains unrounded.

The per-tank sample ring holds 50 hourly snapshots, enough to cover the preceding 48 game hours after sufficient observation. New or migrated tanks cannot retroactively supply that history. Recent care events are bounded at 100; high activity can evict older individual care events while the hourly trend remains. Every death copies its own recent window into the permanent record before later conditions or cleanup can alter it.

Unhatched multi-egg brood viability is an existing aggregate incubation model, not a set of individually identified livestock deaths. Its existing brood history/viability rules remain. Individually modeled fry, coral frags and bottom nursery specimens use the shared death authority and existing recovery rules.

## Export and UI

Field Journal > Tank History > Livestock Deaths merges the active working set and account-specific dedicated records. Filters cover aquarium, species, cause, real date, game day, live/offline and a selected offline run. Welcome Back links to the latest run. Full reports expose observed facts separately from inferred/model-based causes and identify old missing evidence.

`Export Mortality Log` downloads `LIVESTOCK_MORTALITY_LOG.json` with `{schema:"AquariumLifeMortalityLog", version:2, accountId, exportedAt, records, offlineRuns}`. Selected export downloads `LIVESTOCK_DEATH_REPORT.json` with the same schema/version/account and one `record`. These contain diagnostic evidence, not passwords, credentials or the full game. No arbitrary file is silently written outside browser storage. Archive all records before moving profiles: the normal game backup includes only its portable working set plus pending data, not an unlimited historical journal.

## Validation and financial boundary

Validate event IDs/account ownership, uniqueness, finite time/water/damage, known equipment/conditions, detailed version/mode/health/thermal/history shape and bounded samples. Reject invalid current imports instead of rebuilding hidden evidence. An unreadable dedicated entry remains protected for manual recovery and produces a warning.

Transaction drafts defer dedicated writes until their existing validation commits, preventing a rejected action from leaving a false permanent loss.

The existing confirmed-death hook alone cancels qualification and starts/restarts 1,440 game minutes of recovery. Logging adds no AC receipt, charge, award or extra recovery reset. Keep +100 death-free survival and independent +50 healthy-aquarium rules, including historical receipts. Do not resurrect dead entities, reset accounts, falsify water or compensate losses automatically.
