# AQUARIUM LIFE — CRITICAL OVERNIGHT LIVESTOCK DEATH REPAIR
## Codex GPT-6 Astra | Priority Bug Fix
### Saltwater Only — Preserve Existing Game Systems

## 1. Problem

Players are reporting that when they close Aquarium Life, go to bed, and return the next morning, all or nearly all their livestock are dead.

This is a serious gameplay and simulation-balancing problem.

Investigate the actual source code, reproduce the behavior, and correct the underlying cause.

Do not assume starvation is the only explanation.

Possible causes include:
- Excessive offline time acceleration.
- Incorrect feeding or hunger rates.
- Broken automatic feeding.
- Excessive ammonia accumulation.
- Incorrect biological filtration.
- Oxygen depletion.
- Equipment not operating during offline catch-up.
- Incorrect water chemistry update order.
- Disease progressing too rapidly.
- Coral starvation or bleaching incorrectly becoming death.
- Integer overflow or simulation timestep errors.
- Time being processed more than once after login.
- Incorrect last-saved timestamps.
- Death events being duplicated during catch-up.

Do not simply make livestock immortal.

Do not disable the existing offline ecosystem simulation.

## 2. Preserve the Existing Game Clock

The approved time conversion remains:

20 real minutes = one in-game day.

Consequently:

- 8 real hours = 24 in-game days.
- 12 real hours = 36 in-game days.
- 24 real hours = 72 in-game days.

Do not silently change this conversion.

The game clock, equipment, livestock, chemistry, and rewards must all use one authoritative simulation timeline.

## 3. Audit Offline Catch-Up

Examine how the game calculates elapsed time between sessions.

Ensure:

- Elapsed time is calculated once.
- No duplicate catch-up runs occur.
- Simulation advances in correctly ordered time steps.
- Filtration continues working.
- Oxygen exchange continues working.
- Heaters, pumps, and other equipment operate according to their actual state.
- Feeding and digestion are correctly processed.
- Waste production and nutrient removal remain balanced.
- Disease progresses appropriately.
- Livestock health changes reflect actual conditions.

Never apply twenty-four days of biological waste production instantaneously while processing filtration only once.

The same aquarium state should produce reasonably equivalent results whether the game runs continuously or catches up after being closed.

## 4. Correct Feeding and Starvation

Investigate current feeding requirements for all marine livestock.

Fish, corals, and bottom dwellers must have species-appropriate nutritional needs.

Do not apply an identical daily food requirement to every organism.

Ensure:
- Fish hunger progresses at balanced rates.
- Coral receives appropriate photosynthetic energy and nutritional inputs.
- Algae grazers can consume naturally available algae.
- Scavengers use suitable available organic food.
- Predatory fish have appropriate dietary requirements.
- Actual food availability determines nutrition.

Healthy adult fish should not suddenly die because they missed one feeding.

Starvation should develop progressively, according to species, size, age, metabolism, and condition.

More vulnerable species and early life stages may decline faster where biologically appropriate.

Do not artificially keep an organism healthy if it has genuinely exhausted its food supply.

## 5. Automatic Feeding and Overnight Care

Audit whether the game already supports automatic feeders.

If supported, ensure they operate during offline simulation.

Their operation must depend on:
- Equipment installation.
- Power and operational status.
- Feeding schedule.
- Available food stock.
- Compatible food.
- Actual livestock requirements.

Automatic feeders must consume their stored food supply.

They must not generate unlimited free food.

If no suitable automatic feeder exists, report the missing functionality and recommend the smallest compatible addition.

Do not fabricate offline feeding events without an approved food source.

Coral feeding and bottom-dweller feeding must remain species appropriate.

## 6. Water Chemistry and Equipment

Audit:
- Ammonia.
- Nitrite.
- Nitrate.
- Dissolved oxygen.
- Temperature.
- Salinity.
- pH.
- Filtration.
- Biological cycling.
- Waste decomposition.
- Equipment failures.

Check that equipment works identically during active gameplay and offline progression.

Ensure biological filtration processes ammonia and nitrite continuously, subject to actual established bacterial capacity.

Avoid accumulating waste for many simulated days before applying any filtration.

Ensure equipment failures are caused by genuine modeled conditions and not random unavoidable overnight mass-death events.

Never reset established bacterial colonies accidentally on login.

## 7. Health, Disease and Mortality

Investigate how health declines during offline catch-up.

Ensure:
- Health changes happen in chronological order.
- Causes of damage are recorded.
- An organism cannot die multiple times.
- Dead livestock cannot generate further living-organism feeding or disease events.
- Disease transmission respects valid species and conditions.
- Temporary coral stress does not automatically mean coral death.
- Mortality thresholds are evaluated consistently.

Mass death should be possible if a tank truly becomes uninhabitable, but it must not happen routinely to healthy, adequately supported aquariums.

## 8. Add Overnight Survival Diagnostics

Add a clear explanation to the existing Welcome Back report.

If livestock died while the player was away, show:

- Species and individual name/ID.
- Estimated in-game death time.
- Primary recorded cause.
- Relevant aquarium water conditions.
- Whether feeding equipment was operational.
- Whether food ran out.
- Any equipment failures.
- Important preceding warnings.

Examples:

"Clownfish died from prolonged severe malnutrition."

"Yellow Tang died following critically low dissolved oxygen."

"Mushroom coral suffered sustained tissue loss during unsuitable water conditions."

Do not invent a cause when diagnostic information is unavailable.

If the actual cause is uncertain, display:

"Cause of death undetermined."

Record enough information to reproduce and investigate the problem later.

## 9. Improve Overnight Preparation Warnings

Before leaving the game, players should be able to inspect whether their aquarium is prepared for unattended operation.

Add an **Overnight Readiness** summary through an appropriate existing interface.

Show:
- Food supply.
- Automatic feeder status.
- Filter condition.
- Pump/oxygenation status.
- Temperature stability.
- Current water quality.
- Sick or vulnerable livestock.
- Estimated risks.

Use warnings based on actual state.

Do not guarantee survival.

Avoid a misleading overall "Safe" status when critical information is unknown.

## 10. Preserve Daily AC Rewards

Preserve:
- +50 AC healthy-aquarium reward.
- +100 AC livestock survival reward.
- Full in-game-day recovery after a livestock death.

Only award credits for actual qualifying simulated periods.

Do not allow the offline repair to duplicate rewards.

Do not grant livestock survival bonuses for days in which a death occurred.

The existing AC Financial Dashboard must remain consistent with simulated events.

## 11. Existing Save Protection

Do not delete livestock or reset player progress while repairing this problem.

Before migration or repair, preserve a recoverable backup where supported.

If historical death records are already present, do not silently resurrect animals or award compensation.

Report the affected saves and available recovery options.

Preserve:
- Local accounts.
- Wallet balances.
- Livestock IDs.
- Tank conditions.
- Equipment.
- Existing death history.
- Rewards.
- Aquarium values.

## 12. Required Reproduction Tests

Create deterministic tests with representative marine tanks.

Test the same initial tank state through continuous simulation and offline catch-up.

Test absences of:

- 20 real minutes.
- 2 real hours.
- 8 real hours.
- 12 real hours.
- 24 real hours.

Test these scenarios:

A. Healthy cycled aquarium with appropriate equipment and sufficient food.

B. Healthy aquarium with a properly configured automatic feeder.

C. Aquarium without enough food for prolonged absence.

D. Aquarium with a failed circulation pump.

E. Aquarium with an immature nitrogen cycle.

F. Aquarium with existing livestock disease.

G. Reef aquarium with photosynthetic and feeding-dependent corals.

H. Aquarium with algae-grazing and scavenging invertebrates.

I. Aquarium containing vulnerable juveniles.

J. Multiple aquariums on one local account.

K. Save/load and login performed repeatedly after a long absence.

L. An aquarium remaining open continuously for the same elapsed simulated period.

Expected behavior:

Healthy, stable, adequately provisioned aquariums should not experience unexplained overnight mass mortality.

Genuinely neglected or severely unstable aquariums may experience illness or death according to documented simulation conditions.

Continuous and offline simulation should have consistent outcomes, within defined numerical tolerances.

Every death should have a traceable cause when the simulation can determine one.

## 13. Development Report

When finished, report:

1. Root cause found.
2. Relevant files changed.
3. Biology or chemistry formulas corrected.
4. Whether automatic feeding was involved.
5. Offline simulation corrections.
6. Overnight balancing tests performed.
7. Continuous versus offline comparison results.
8. Any remaining limitations.
9. Whether existing saves are affected.
10. Documentation updated.

Update the appropriate consolidated MDP sections without duplicating mechanics.

Preserve saltwater-only development. Do not unlock freshwater.

## 14. Completion Rule

Notify the player when all authorized edits are finished.

If implementation and required tests have genuinely completed, end with this exact standalone line:

Done With Edits

Do not claim completion if the underlying issue remains unresolved.

# FINAL DIRECTIVE

Find and fix the actual cause of overnight livestock mass deaths.

Maintain realistic biological conditions, preserve the twenty-minute game-day clock, correct offline simulation inconsistencies, and make properly maintained aquariums viable for ordinary overnight absences.

Do not mask a broken simulation with artificial invulnerability.

Preserve player data, aquarium economy, and all existing approved features.
