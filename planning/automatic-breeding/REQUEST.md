# AQUARIUM LIFE — AUTOMATIC FISH BREEDING & NATURAL COURTSHIP
## Codex GPT-6 Astra — Saltwater Breeding System Update

### 1. Primary Objective

Replace the current manually triggered fish-breeding system with an autonomous, biologically appropriate breeding system.

Currently, the Field Journal → Breeding & Eggs interface contains a "Begin Courtship" button.

Remove the requirement for players to manually begin courtship.

Fish must breed naturally in their aquarium when the appropriate conditions are satisfied.

Preserve the existing genetic inheritance, lifecycle, health, disease, and save systems.

Freshwater remains locked and must not be expanded.

---

### 2. Automatic Breeding Conditions

Fish should periodically evaluate their eligibility to reproduce based on:

- Biological species.
- Sexual maturity.
- Compatible reproductive partners.
- Sex and reproductive role where applicable.
- Individual health.
- Nutrition.
- Stress levels.
- Water chemistry.
- Temperature.
- Tank capacity.
- Suitable nesting or spawning habitat.
- Territorial conditions.
- Appropriate species-specific breeding triggers.

Do not allow every mature pair to reproduce automatically every day.

Use realistic cooldowns, fertility limits, and appropriately balanced probabilities.

Prevent overcrowding and unlimited offspring generation.

Species that cannot reliably reproduce in captivity must not use unrealistic generic breeding rules.

Do not automatically assign male/female reproduction to species with different natural reproductive systems.

---

### 3. Visible Courtship Behavior

When a compatible breeding pair enters courtship, make the behavior visible inside the aquarium.

Examples of suitable behaviors include:

- Swimming close together.
- Following a potential mate.
- Short synchronized swimming movements.
- Circling.
- Courtship displays.
- Moving toward a preferred spawning location.
- Preparing or defending a nesting area.

Courtship animations must use the existing approved hybrid pixel-art style.

Keep fish anatomy and eye positions correct throughout the animation.

Do not teleport fish together.

Courtship must fit naturally into normal aquarium movement rather than freezing the whole tank.

Different species should exhibit appropriate behaviors rather than one universal mating animation.

---

### 4. Female Reproductive Status

When a player clicks a female fish, the existing livestock inspector should display her reproductive status.

Possible statuses:

- Immature.
- Not Ready to Breed.
- Ready to Breed.
- Courtship.
- Gravid — Carrying Eggs.
- Preparing to Spawn.
- Recovering After Spawning.

Only show states biologically applicable to that species and individual.

For egg-laying marine fish, use the scientifically appropriate term:

**Gravid — Carrying Eggs**

Do not incorrectly describe every egg-laying fish as pregnant.

If useful for beginners, include a tooltip:

"Gravid means the female is carrying developing eggs before spawning."

For species with male mouthbrooding or different reproductive roles, display the correct individual-specific status.

For example, Banggai Cardinalfish males may carry developing offspring in their mouths.

Do not show a female as pregnant simply because a breeding pair exists.

---

### 5. Visible Spawning and Egg Placement

When spawning occurs, create visible eggs or a biologically appropriate clutch in the aquarium containing the parents.

Critical requirements:

- Eggs appear in the same aquarium as the spawning parents.
- Eggs are associated with their actual parents.
- Eggs persist after saving and reloading.
- Eggs cannot duplicate on reload.
- Eggs must not appear in unrelated aquariums.
- Eggs must be rendered using appropriate pixel artwork.
- Egg development advances with the existing game clock.

The egg placement must depend on species.

Examples:

**Ocellaris Clownfish**
- Parents select suitable hard substrate, often near their host or defended nesting area.
- The female deposits a clutch on that surface.
- The male performs appropriate fertilization and parental care behavior.
- Eggs remain attached to the spawning surface.
- Parents may guard or tend the clutch.

**Demersal Egg-Layers**
- Deposit eggs on appropriate rock, shelter, or other suitable surfaces.

**Pelagic Spawners**
- Release eggs into the water column.
- Eggs must not automatically become stationary rock-attached clutches.
- Model appropriate dispersal, viability, and larval-rearing requirements.

**Mouthbrooders**
- Preserve appropriate parental brooding rather than generating an external egg pile.

Do not force all saltwater fish to lay the same kind of eggs.

---

### 6. Egg Artwork and Growth

Create or reuse approved species-appropriate artwork for:

- Spawning.
- Eggs or clutch.
- Developing embryos.
- Hatching.
- Larval or baby stages.
- Juvenile stages.

Keep the eggs visually small and believable.

Do not make individual fish eggs expand unrealistically from five pixels to twenty-five pixels as their literal biological size.

Use suitable zoom, cluster rendering, and development-stage visuals instead.

Eggs must remain visible and inspectable where the reproductive strategy supports visible eggs.

---

### 7. Eggs and Offspring Survival

Eggs are not guaranteed to survive or hatch.

Success depends on appropriate factors such as:

- Fertilization.
- Water quality.
- Temperature.
- Oxygenation.
- Parental care.
- Fungus or disease where relevant.
- Predation.
- Species-specific incubation requirements.

Newly hatched larvae must have appropriate nutritional requirements.

Do not turn newly hatched larvae instantly into miniature adults.

Hatching must produce correctly identified individuals with persistent unique IDs.

Avoid excessive automatic population growth.

---

### 8. Genetic Inheritance

Preserve the existing clownfish genetic inheritance system.

For normal Ocellaris pairings, retain the approved:

- 85% standard pattern.
- 10% minor variation.
- 4% misbar.
- 1% exceptional pattern.

This distribution applies only to the previously approved normal Ocellaris pairing conditions.

Designer Ocellaris pairings must follow their separately documented inheritance rules.

Preserve:
- Parent identity.
- Stable genetic seeds.
- Lineage.
- Individual pattern variation.
- Life-stage development.
- Unique markings after save/load.
- Correct left/right rendering.

Do not give unrelated fish clownfish-specific genetics.

---

### 9. Field Journal — Breeding & Eggs Redesign

Keep the Breeding & Eggs tab in the Field Journal.

Remove the "Begin Courtship" button and any other mandatory manual mating trigger.

Instead, turn this interface into a breeding observation and tracking dashboard.

Display:

**Breeding Activity**
- Current courtship pairs.
- Ready-to-breed individuals.
- Recent spawning events.

**Active Clutches**
- Parent species.
- Parent IDs.
- Aquarium.
- Spawning date.
- Egg count where known.
- Development progress.
- Estimated hatch period where supported.

**Offspring**
- Hatched fry or larvae.
- Current life stage.
- Survival status.
- Genetic lineage.

**Breeding History**
- Completed spawning events.
- Failed spawning events.
- Successful hatching.
- Parentage records.

**Player-Fragged Coral Lineage**
- Keep the existing separate coral fragmentation history.

The Field Journal observes and records reproduction. It does not manually start it.

---

### 10. Fish Inspector Integration

When clicking a fish in the tank, display:

- Sex or reproductive role, where known.
- Current reproductive status.
- Maturity.
- Current mate or paired partner where applicable.
- Courtship state.
- Egg or offspring status.
- Last spawning event where applicable.
- Reproductive cooldown.

The inspector must refresh when the reproductive state changes.

Preserve the existing three-second visual selection-highlight rule.

The fish selection outline disappears after three seconds, but the inspector stays open.

---

### 11. Aquarium Simulation Timing

Breeding must use the existing authoritative game clock.

One in-game day remains twenty real-world minutes.

Courtship, spawning, egg incubation, hatching, and larval growth continue during:

- Normal gameplay.
- Store browsing.
- Diving.
- Casino gameplay.
- Offline progression.

Offline reproduction must be deterministic under saved state and persistent random seeds.

Avoid generating unlimited offspring during extended offline absences.

Do not invent extra completed clutches merely because a large amount of time elapsed.

---

### 12. Population Management

Automatic breeding must not overwhelm the aquarium.

Implement biologically justified limits based on:

- Habitat and nesting capacity.
- Species fertility.
- Parental condition.
- Available food.
- Larval survival needs.
- Tank stocking capacity.
- Predation.
- Stress and competition.

Do not arbitrarily guarantee that every clutch survives.

Breeding should add ecological depth without creating endless free AC through immediate offspring sales.

---

### 13. Save/Load Integrity

Persist:

- Reproductive maturity.
- Reproductive role.
- Paired partner identity.
- Courtship state.
- Spawning-site identity.
- Clutch ID.
- Parent IDs.
- Egg count and viability.
- Egg positions.
- Incubation progress.
- Hatch status.
- Offspring IDs.
- Genetic data.
- Last spawning timestamp.
- Breeding cooldowns.

Use save-schema migration where necessary.

Preserve existing breeding history.

Never duplicate eggs or offspring after loading a saved game.

---

### 14. Required Testing

Verify:

1. Fish can breed without clicking Begin Courtship.
2. The manual courtship button is removed.
3. Only eligible mature fish participate.
4. Incompatible fish do not reproduce.
5. Appropriate partner and reproductive-role checks work.
6. Courtship behavior is visible.
7. Fish movement remains functional during courtship.
8. Female gravid states display correctly.
9. Male mouthbrooding states display correctly where applicable.
10. Spawning occurs in the parents' aquarium.
11. Clownfish eggs attach to valid spawning substrate.
12. Pelagic spawners do not use generic attached clutches.
13. Eggs remain visible after saving.
14. Reloading does not duplicate clutches.
15. Incubation progresses correctly.
16. Hatchlings receive unique IDs.
17. Genetics persist correctly.
18. Normal Ocellaris inheritance rules remain intact.
19. Offspring use appropriate lifecycle artwork.
20. Breeding cooldowns work.
21. Overcrowding does not cause infinite reproduction.
22. The Field Journal displays active and historical breeding events.
23. Coral fragging history remains functional.
24. Offline breeding behaves consistently with live simulation.
25. Existing accounts and aquariums remain compatible.
26. Freshwater stays locked.
27. The game remains completely offline.

Report genuine test results.

---

### 15. Documentation

Update the appropriate sections of the consolidated Master Development Prompt.

Also update:
- GAME_DESIGN.md.
- DEVELOPMENT_STATUS.md.
- UI_SPECIFICATION.md.
- CURRENT_LIVESTOCK_CATALOG.md where reproductive metadata changes.
- Breeding and genetics documentation.
- Save-schema documentation.
- Project continuity notes and PDF where supported.

Add this permanent rule:

**Fish breeding in Aquarium Life happens autonomously when biologically appropriate conditions are satisfied. The player does not manually initiate courtship through the Field Journal. Reproductive condition is visible through individual livestock inspection, and eggs or offspring appear in the same aquarium as their parents according to species-specific reproductive biology.**

Do not duplicate breeding mechanics across unrelated design sections.

---

### 16. Codex Completion Requirement

When all authorized edits are genuinely complete, provide:

- Files edited.
- Breeding behaviors implemented.
- Species reproductive strategies supported.
- UI changes.
- Save/load changes.
- Tests passed.
- Tests failed or not run.
- Remaining limitations.

The final standalone line must be exactly:

Done With Edits

Do not use this phrase if work is unfinished or blocked.

# FINAL DIRECTIVE

Convert fish breeding from manual initiation to natural, autonomous aquarium behavior.

Show courtship animations, individual reproductive status, species-appropriate spawning, visible eggs and developing offspring.

Preserve existing genetic inheritance and all other Aquarium Life systems.

Do not unlock freshwater development.
