# AQUARIUM LIFE — PERMANENT LIVESTOCK MORTALITY LOGGING SYSTEM
## Codex GPT-6 Astra | Critical Diagnostic Feature
### Saltwater-Only Development

## 1. Primary Objective

Implement a permanent livestock death logging and diagnostic system in Aquarium Life.

This feature is intended to investigate and troubleshoot unexpected livestock deaths, particularly overnight mass mortality during offline simulation.

Every confirmed livestock death must generate an individual, persistent diagnostic record.

The system must cover:
- Saltwater fish.
- Coral.
- Bottom-dwelling fish and invertebrates.
- Every applicable life stage.

Preserve existing aquarium, health, disease, equipment, economy, and save systems.

Freshwater development remains locked.

---

## 2. Centralized Mortality Event System

Create one authoritative mortality logging system.

Whenever livestock transitions from alive to dead, generate exactly one death record.

Do not create separate conflicting death loggers for fish, corals, and invertebrates.

Each record must contain:

### Livestock Identity
- Unique livestock instance ID.
- Species ID.
- Common name.
- Scientific name.
- Livestock category.
- Rarity.
- Life stage.
- Age.
- Current and maximum health before death.
- Aquarium ID.
- Aquarium name.

### Time and Simulation
- Unique mortality event ID.
- In-game day.
- In-game time.
- Real-world timestamp.
- Whether the event occurred during live or offline simulation.
- Simulation step ID or interval.
- Last known healthy timestamp.
- Elapsed time since last feeding where applicable.

### Suspected Cause
- Primary suspected cause.
- Additional contributing causes.
- Supporting diagnostic evidence.
- Cause confidence or certainty level.

Possible categories:
- Starvation.
- Temperature stress.
- Oxygen deprivation.
- Ammonia toxicity.
- Nitrite toxicity.
- Salinity stress.
- Disease.
- Aggression or injury.
- Age-related mortality.
- Equipment failure.
- Environmental collapse.
- Unknown cause.

Do not invent a cause if sufficient evidence is unavailable.

Use "Unknown" when the cause cannot be established.

---

## 3. Water Chemistry Snapshot

At the moment of death, record:

- Actual temperature.
- Heater target temperature.
- Salinity.
- pH.
- Ammonia.
- Nitrite.
- Nitrate.
- Dissolved oxygen.
- Relevant alkalinity and reef chemistry.
- Actual water volume.
- Biological filter state.
- Bioload.
- Water quality warnings.

Capture the values before any post-death decomposition or cleanup calculations alter them.

Do not substitute water readings from the next login.

---

## 4. Equipment Snapshot

Record the status of equipment that may affect survival.

Include:

- Heater installed.
- Heater enabled.
- Heater target temperature.
- Actual heater output where modeled.
- Heater capacity.
- Circulation pump condition.
- Filter operation.
- Aeration and oxygenation.
- Lighting state.
- Automatic feeder condition.
- Food remaining.
- Relevant equipment failures.

If the game does not currently model a particular equipment property, mark it unavailable rather than inventing values.

---

## 5. Livestock Health and Nutrition Snapshot

At the time of death, record:

- Health before the fatal update.
- Health after damage calculation.
- Hunger or nutrition.
- Stress.
- Disease conditions.
- Active medication.
- Recent feeding.
- Injury.
- Relevant behavior or aggression events.
- Death-triggering damage amount.
- Damage source.

Corals additionally require:
- Living tissue condition.
- Bleaching.
- Polyp condition.
- Light exposure.
- Relevant nutrient availability.

Bottom dwellers require relevant diet and substrate information where modeled.

---

## 6. Historical Conditions

A single death snapshot may not explain what caused mortality.

Maintain a bounded diagnostic history for each aquarium.

Record meaningful state samples over simulated time.

The history should support reviewing at least the preceding 48 in-game hours, with sufficient resolution to identify dangerous changes.

Track:
- Temperature trends.
- Oxygen trends.
- Ammonia and nitrite spikes.
- Hunger decline.
- Health decline.
- Equipment failures.
- Major water changes.
- Feeding events.
- Disease progression.

Use compact samples and event-based diagnostics to avoid excessive local storage.

When livestock dies, attach or reference the recent diagnostic window.

Preserve enough evidence to investigate deaths even if water conditions later return to normal.

---

## 7. Overnight Simulation Debugging

The logging system must work during offline catch-up.

When the player returns after eight real hours away, all simulated death events must retain their correct in-game timestamps.

Do not assign every overnight death the login timestamp.

Record:
- Offline catch-up start and end.
- Total elapsed simulated time.
- Number of simulation steps processed.
- Relevant equipment operation.
- Health decline.
- Each death event.
- Whether a simulation error occurred.

Ensure that repeated login or save/load operations cannot duplicate death events.

This system must help diagnose:
- Repeated temperature damage.
- Excessive starvation.
- Duplicate health updates.
- Heater inactivity.
- Incorrect time advancement.
- Sudden oxygen depletion.
- Unexplained mortality.

Do not automatically blame the heater or starvation.

---

## 8. Dedicated Local Log Storage

Store mortality records separately from ordinary aquarium gameplay objects.

Suggested logical file:

`LIVESTOCK_MORTALITY_LOG.json`

Because the game runs in a browser through `file://`, do not assume JavaScript can silently write an arbitrary file to the player's computer.

Use the existing persistent local storage system for the active log.

Provide an Export function that downloads a standalone JSON file.

Requirements:
- Versioned logging schema.
- Unique event IDs.
- Account-specific records.
- Validated save/load.
- Efficient storage.
- No accidental duplication.
- No silent deletion of existing records.

Never include passwords or account credentials in diagnostic exports.

If storage capacity is exceeded, warn the player and preserve records safely where possible.

---

## 9. Mortality History Interface

Add a new section inside:

**Field Journal → Tank History → Livestock Deaths**

Display a chronological list of all recorded livestock deaths.

Each entry should show:
- Livestock name.
- Aquarium.
- Date and time.
- Suspected cause.
- Live or offline simulation.
- Whether diagnostic evidence is available.

Clicking an entry opens its complete diagnostic report.

Include filters for:
- Aquarium.
- Species.
- Cause.
- Date.
- Offline deaths.
- Live deaths.

Add:

**Export Mortality Log**

Also offer an export of the selected death report.

Do not permanently display technical debugging information over the aquarium.

---

## 10. Welcome Back Integration

When offline simulation causes livestock deaths, show a summary when the player logs in.

Example:

"During your absence, 4 livestock deaths were recorded."

Provide:

**View Death Reports**

This button opens the Mortality History interface, filtered to the latest offline simulation period.

Do not display invented explanations.

If the cause is unknown, state that clearly.

---

## 11. Example Diagnostic Report

The following is an illustrative format, not a diagnosis of the player's actual aquarium.

Livestock: Ocellaris Clownfish
Species ID: clown
Aquarium: 20 Gallon Tank
Death: Day 28, 04:15
Simulation: Offline
Suspected Cause: Temperature Stress
Confidence: Moderate

Temperature at death: 22.0°C
Heater target: 25.0°C
Heater operating: No
Ammonia: 0.00 mg/L
Nitrite: 0.00 mg/L
Dissolved oxygen: 7.8 mg/L
Health before fatal update: 6%
Final damage: 8%
Hunger: 74%

Recent history:
- Temperature dropped below the species' configured safe range.
- Heater output was unavailable.
- Livestock health declined over several simulated intervals.

Clearly distinguish recorded facts from inferred causes.

---

## 12. Financial and Reward Integration

Every death event must connect correctly to the existing +100 AC livestock survival reward rules.

When a death occurs:
- Cancel the appropriate survival bonus.
- Start or restart the required one-day recovery interval.
- Do not apply the penalty multiple times for the same death event.

Death logging must not create additional AC transactions itself.

The mortality records may be referenced by the Tank History and Financial Overview systems.

---

## 13. Existing Save Protection

Do not reset:
- Aquarium Credits.
- Accounts.
- Livestock.
- Tank progress.
- Achievements.
- Equipment.
- Deep Market reputation.
- Aquarium conditions.

Migrate existing saves safely.

For deaths that occurred before this logging system existed, do not manufacture diagnostic reports.

Older deaths may be shown as historical events only if valid records already exist.

---

## 14. Required Tests

Verify:

1. A fish death produces one record.
2. A coral death produces one record.
3. A bottom-dweller death produces one record.
4. A single death cannot produce duplicate records.
5. Every record retains the correct livestock identity.
6. Water parameters are recorded at the actual death time.
7. Heater target and actual temperature are recorded separately.
8. Hunger and health values are captured.
9. Disease and injury causes are captured where applicable.
10. Unknown causes are identified honestly.
11. Offline simulation generates correctly timestamped records.
12. Deaths remain recorded after login.
13. Save/load preserves death history.
14. Historical aquarium condition samples remain available.
15. Multiple aquariums maintain correct separate records.
16. Multiple accounts do not share death logs.
17. Mortality Log JSON export works offline.
18. Exported JSON contains valid structured data.
19. Reopening the game does not duplicate deaths.
20. Welcome Back shows accurate mortality summaries.
21. Livestock survival rewards respect the death records.
22. No extra AC is deducted or awarded by logging.
23. Existing gameplay performance remains acceptable.
24. Freshwater remains locked.
25. Existing aquarium data remains intact.

Report actual test results.

---

## 15. Documentation

Update:
- Consolidated 31-section Master Development Prompt.
- GAME_DESIGN.md.
- DEVELOPMENT_STATUS.md.
- UI_SPECIFICATION.md.
- Save-schema documentation.
- Mortality diagnostic documentation.
- Project PDF continuity section where supported.

Add the permanent rule:

**Every livestock death must create one persistent, account-specific mortality record containing the livestock identity, actual simulation time, relevant health and environmental conditions, equipment status, and available evidence for the cause of death.**

Do not duplicate this mechanic across unrelated design sections.

---

## 16. Codex Completion Requirement

When authorized edits are genuinely finished, Codex must provide:

- Files changed.
- Mortality logging implementation summary.
- Export functionality.
- Diagnostic data recorded.
- Testing results.
- Known limitations.
- Documentation changes.

The final standalone line must be exactly:

Done With Edits

Do not claim successful completion if the work is unfinished.

# FINAL DIRECTIVE

Implement permanent livestock mortality logging, diagnostic snapshots, historical condition tracking, and offline JSON export.

The system must make it possible to investigate why livestock die during long offline periods, even when the aquarium appears healthy after reopening.

Preserve all existing game systems and continue saltwater-only development.
