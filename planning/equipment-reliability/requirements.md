# AQUARIUM LIFE — REALISTIC EQUIPMENT DURABILITY & LONG-TERM RELIABILITY
## Codex GPT-6 Astra — Saltwater Only
### Priority: Equipment Longevity, Maintenance and Fair Offline Progression

## 1. PRIMARY OBJECTIVE

Equipment in Aquarium Life is losing durability much too quickly.

Rebalance the entire equipment durability and reliability system so equipment can last multiple in-game years when properly maintained.

The player's real-world experience is that aquarium equipment can run for years, with only occasional component failures.

Aquarium Life should reflect this long-term reliability rather than requiring players to constantly replace equipment.

Preserve the established game clock:

**One in-game day = 20 real-world minutes.**

Do not change the game clock to solve equipment wear.

Audit the actual equipment simulation and its existing durability calculations before making changes.

Freshwater remains locked.

---

## 2. AUDIT THE EXISTING DURABILITY SYSTEM

Inspect:
- Equipment durability calculations.
- Wear rates.
- Maintenance intervals.
- Equipment failure probabilities.
- Offline catch-up calculations.
- Durability deductions on each simulation step.
- Repair behavior.
- Equipment quality or tier modifiers.
- Save/load serialization.
- Equipment installation and removal.
- Temperature and water-quality effects.

Identify why equipment loses durability so quickly.

Specifically investigate whether:
- Wear is applied too frequently.
- Real-time seconds are incorrectly treated as game days.
- Wear scales incorrectly with accelerated time.
- Durability is deducted multiple times during offline simulation.
- The same wear is applied through multiple overlapping systems.
- Every piece of equipment receives identical wear rates.
- Maintenance penalties are too severe.
- Equipment durability is recalculated or reset incorrectly after loading.

Report the actual root cause.

Do not simply multiply all equipment durability by an arbitrary number without inspecting the simulation.

---

## 3. LONG-TERM SERVICE LIFE

Equipment should have realistic long-term service-life expectations.

Suggested initial gameplay targets:

| Equipment | Expected In-Game Service Life |
|---|---|
| Heater | 3–7 years |
| Circulation Pump | 4–8 years |
| Filter | 5–10 years |
| Protein Skimmer | 5–10 years |
| Aquarium Lighting | 5–10 years |
| Chiller | 5–10 years |
| Automatic Feeder | 3–6 years |
| Air Pump | 3–6 years |

These ranges are proposed balance targets, not exact real-world guarantees.

Use equipment-specific parameters where available.

An expensive high-quality pump should generally be more reliable than a low-quality pump, but no item should be guaranteed to last forever.

Treat expected life as a probabilistic service-life model rather than a fixed expiration date.

Do not invent permanent failure dates.

---

## 4. IMPORTANT TIME-SCALING REQUIREMENT

One real-world hour equals three in-game days.

One real-world day equals 72 in-game days.

Therefore, even equipment designed to last several in-game years will age noticeably during extended real-world play.

Calculate durability and service life against the authoritative in-game elapsed time.

**Do not scale equipment wear twice.**

Do not apply one entire day's wear on every short simulation tick.

Use mathematically consistent time-step calculations.

Live simulation and offline catch-up must produce equivalent wear outcomes under equivalent operating conditions.

Document how this scaling affects actual player experience.

Do not make equipment failure impossibly frequent simply because the simulation clock is accelerated.

---

## 5. SEPARATE WEAR, MAINTENANCE AND FAILURE

Implement or refine separate concepts:

### Equipment Condition

Represents the general physical state of the equipment.

Declines gradually through long-term operation.

### Maintenance Condition

Represents service needs such as:
- Cleaning.
- Removing debris.
- Replacing consumable filter media.
- Inspecting pumps.
- Calibrating sensors.
- Cleaning impellers.

Maintenance should restore performance where appropriate without magically turning old equipment into a new item.

### Failure Risk

Represents the probability of equipment malfunction.

Failure probability may increase with:
- Extreme age.
- Poor maintenance.
- Existing damage.
- Poor operating conditions.
- Low equipment quality.
- Relevant component wear.

A well-maintained device must not fail automatically when its calendar age reaches a target number.

---

## 6. EQUIPMENT-SPECIFIC WEAR

Different equipment should age differently.

### Pumps

Consider:
- Impeller condition.
- Debris accumulation.
- Motor wear.
- Maintenance intervals.

### Heaters

Consider:
- Thermostat reliability.
- Heating-element wear.
- Operating cycles.

### Filters

Distinguish:
- Durable filter housing.
- Mechanical parts.
- Replaceable consumable media.
- Biological filtration bacteria.

Cleaning a filter should not reset the aquarium's established nitrogen cycle without a biologically justified event.

### Lighting

Distinguish:
- Long-lived LED fixtures.
- Replaceable lamps.
- Gradual light-output degradation.

Do not represent normal gradual light degradation as instant total failure.

### Protein Skimmers

Consider:
- Pump condition.
- Intake contamination.
- Collection-cup maintenance.
- Long-term component wear.

Use similar appropriate models for chillers, aeration pumps and automatic feeders.

---

## 7. MAINTENANCE SYSTEM

Players should perform realistic maintenance without being overwhelmed.

Maintenance should:
- Extend useful service life.
- Reduce avoidable malfunction risk.
- Restore reduced operating efficiency.
- Preserve appropriate long-term wear.
- Produce appropriate maintenance history events.

Do not require the player to clean equipment every few real-world minutes.

Review maintenance interval frequency relative to accelerated game time.

Provide reasonable warnings before condition becomes critical.

Maintenance must remain meaningful without becoming a constant repetitive chore.

---

## 8. EQUIPMENT FAILURE BEHAVIOR

Avoid treating every maintenance issue as complete device destruction.

Support appropriate states where the existing architecture allows:

- Working normally.
- Maintenance recommended.
- Reduced efficiency.
- Temporary malfunction.
- Repair required.
- Failed beyond repair.

A dirty pump may lose flow efficiency before stopping entirely.

A heater thermostat may malfunction without instantly destroying the equipment.

Do not make failure results arbitrary or unrealistically catastrophic.

Preserve actual effects on aquarium temperature, oxygen and water chemistry.

---

## 9. EXISTING EQUIPMENT AND SAVE DATA

Apply improved durability rules to existing accounts and aquariums.

Preserve:
- Equipment identity.
- Current location.
- Tank assignment.
- Current durability.
- Maintenance history.
- Modifications.
- Purchase records.

Do not reset every existing device to brand new.

Do not delete equipment.

Do not duplicate devices.

If existing durability values were damaged by a confirmed wear-calculation bug, provide a safe and documented migration or recovery method rather than silently altering all equipment values.

Respect the finalized Inventory system:

- Installed equipment belongs exclusively to its aquarium.
- Uninstalled equipment appears in Inventory.
- Stored equipment cannot operate a tank.
- Each aquarium needs its own physical equipment.

---

## 10. UI IMPROVEMENTS

Inside the individual equipment inspector, display:

- Current condition.
- Maintenance status.
- Approximate service age.
- Operating efficiency.
- Maintenance action where applicable.
- Repair action where supported.
- Appropriate warnings.

Do not promise a specific failure date.

Do not restore the removed standalone Temperature Control or Overnight Readiness panels in Tank Care.

Temperature settings remain accessible through installed heater and chiller controls.

Historical maintenance and failures belong in Tank History.

---

## 11. OFFLINE PROGRESSION

Audit durability behavior during extended offline periods.

Test:
- 8 real-world hours.
- 12 real-world hours.
- 24 real-world hours.
- Multiple in-game years through deterministic simulation tests.

Ensure:
- No duplicate wear application.
- No duplicate failures.
- No unrealistic cascading failures from a faulty time step.
- Maintenance history remains consistent.
- Equipment effects remain biologically meaningful.

Do not pause all equipment wear during offline progression.

Do not artificially make equipment immortal.

---

## 12. TESTING REQUIREMENTS

Verify:

1. Equipment lasts substantially longer under normal operation.
2. Maintenance reduces avoidable failure risk.
3. Different equipment types have appropriate durability behavior.
4. Wear does not depend on rendering frame rate.
5. Offline simulation applies wear correctly.
6. Equipment doesn't receive duplicate durability deductions.
7. Existing equipment remains assigned to the correct aquarium.
8. Inventory ownership is preserved.
9. Repairs preserve item identity.
10. Equipment failure affects only the aquarium where it is installed.
11. Biological filtration persists correctly through appropriate maintenance.
12. Temperature controls remain functional.
13. Tank History records maintenance and failures.
14. No duplicated or deleted equipment.
15. No unauthorized economy changes.
16. Freshwater remains locked.
17. The game remains fully offline.

Run quantitative service-life tests using fixed random seeds.

Report estimated equipment failure distributions rather than testing only one arbitrary simulation run.

Do not claim tests passed unless they were genuinely executed.

---

## 13. BALANCE REPORT

Create or update:

EQUIPMENT_DURABILITY_BALANCE_REPORT.md

Include:
- Original wear formulas.
- Original estimated service life.
- Updated wear formulas.
- New expected service life.
- Equipment-specific maintenance intervals.
- Failure risk modeling.
- Effect of offline progression.
- Test results.
- Remaining limitations.

Explicitly show equivalent expected equipment service life in both in-game years and real-world elapsed time at the game's current time scale.

Do not hide unrealistic player-facing replacement frequency.

---

## 14. DOCUMENTATION

Update the correct home sections in the consolidated 31-section Aquarium Life Master Development Prompt.

Also update:
- GAME_DESIGN.md.
- DEVELOPMENT_STATUS.md.
- BALANCE_REPORT.md.
- Equipment maintenance documentation.
- Save-schema documentation.
- Project continuity notes.

Add the permanent rule:

**Aquarium equipment must have long-term, equipment-specific durability and reliability. Well-maintained equipment should generally last several in-game years, with gradual wear and reasonable maintenance requirements. Failure must not be driven by excessively fast or duplicated durability deductions.**

Do not duplicate durability mechanics throughout unrelated design sections.

---

## 15. COMPLETION REPORT

When all authorized edits are genuinely completed, report:

1. Root cause of rapid durability loss.
2. Files modified.
3. Equipment categories rebalanced.
4. New wear and failure calculations.
5. Estimated equipment service life.
6. Maintenance interval changes.
7. Offline simulation test results.
8. Save migration changes.
9. Known limitations.

Only when authorized work is genuinely complete, end with:

Done With Edits

# FINAL DIRECTIVE

Make aquarium equipment substantially more durable while preserving realistic maintenance and occasional failures.

Players should enjoy maintaining their aquariums, not constantly replacing equipment.

Keep Aquarium Life saltwater-only, fully offline, and consistent with the established equipment inventory and per-tank installation rules.
