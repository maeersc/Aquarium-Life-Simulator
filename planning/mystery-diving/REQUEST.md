# AQUARIUM LIFE — MYSTERY FISH OCEAN DIVING UPDATE v3.5
## Codex GPT-6 Astra — Saltwater Only

### 1. Main Objective

Update the existing Ocean Diving and Deep Sea Diving minigames so that players can always encounter and attempt to catch at least one mystery fish during every valid diving expedition.

The fish must be displayed as a dark silhouette with a large question mark.

Players must not know the fish's identity before completing the expedition.

Preserve all existing diving costs, controls, equipment, oxygen, regional habitats, inventory and aquarium systems.

### 2. Guaranteed Fish Encounter

Every properly initialized diving expedition must generate at least one reachable, collectible mystery fish encounter.

This applies to:
- Reef Diving, unlocked at Aquarium Keeper Level 5.
- Deep Sea Diving, unlocked at Aquarium Keeper Level 10.

The encounter must:
- Spawn within a reachable portion of the map.
- Have a valid movement route from the starting location.
- Be collectible without exceeding the oxygen budget when accounting for the return trip.
- Use an eligible fish species from the selected region and dive habitat.

Do not guarantee successful ownership if the player fails the dive, runs out of oxygen, or cannot return to the boat.

A player who completes the encounter and safely returns should receive the collected specimen, subject to the established post-dive survival assessment.

### 3. Mystery Fish Appearance

Before the reveal, display the fish using:
- A dark fish silhouette.
- A visible question mark.
- Original Aquarium Life pixel-art styling.
- Smooth underwater movement.
- Clear interaction indicators.

Do not expose:
- Species name.
- Scientific name.
- Rarity.
- Asset value.
- Species-specific appearance or markings.

Avoid silhouettes that make rare fish trivially identifiable before capture.

The mystery effect must work for both Reef Diving and Deep Sea Diving.

### 4. Fish Capture

When the diver approaches a mystery fish:

1. Check interaction distance.
2. Check remaining inventory capacity.
3. Allow a left-click to attempt capture.
4. Record the specimen in temporary expedition inventory.
5. Mark the encounter as collected.
6. Prevent duplicate collection.

Captured mystery fish occupy one of the eight available inventory slots.

The temporary inventory displays:

"Unknown Fish — ?"

Do not reveal the species yet.

### 5. Region-Specific Fish Selection

The mystery fish must always be a valid species for the selected diving region.

Examples:
- Fiji.
- Caribbean.
- Hawaii.
- Japan.

Preserve the documented geographic range and habitat-depth restrictions.

Do not place a region-exclusive Hawaiian species into Fiji merely because it has a compatible rarity.

Only select species that exist in the implemented livestock database and are eligible for that expedition.

If a region lacks a valid fish pool, do not silently invent a species or substitute an incompatible fish. Clearly flag the missing content and block that destination until a proper pool exists.

### 6. Rarity

Mystery fish may belong to any eligible rarity tier supported by the selected region and diving mode.

Keep the existing six-tier rarity system.

Do not automatically guarantee Legendary fish.

Define and document diving-specific species selection probabilities based on:
- Destination.
- Habitat.
- Diving mode.
- Valid species pool.
- Approved rarity rules.

Do not silently reuse Mystery Egg probability tables for diving unless those odds have been explicitly approved for diving.

### 7. Oxygen and Inventory

Preserve the established rules:

- Starting oxygen: 100%.
- Every successful movement step consumes 5 percentage points.
- WASD and arrow-key movement.
- Eight maximum inventory slots.
- Player must return to the boat to keep discoveries.

Do not consume oxygen just because the player clicks an encounter.

Ensure the guaranteed mystery fish is reachable and that the shortest safe route back to the boat is feasible within the available movement budget.

### 8. Return-to-Boat Reveal

When the player returns successfully:

Show an expedition-results screen.

For each mystery fish reveal:
- Actual species.
- Scientific name.
- Rarity.
- Artwork.
- Survival condition.
- Current asset value.
- Origin and destination.

Use a short original pixel-art reveal animation.

The fish is only added to the player's permanent collection through the existing valid receiving or quarantine process.

Do not bypass tank compatibility.

### 9. Fish Survival

Preserve the existing post-diving survival system.

The fish may return:
- Healthy.
- Stressed.
- Injured.
- Sick.
- Dead on arrival.

Survival must depend on the applicable existing biological and expedition systems.

A guaranteed encounter does not mean guaranteed survival.

If a specimen dies during recovery, record the mortality event with the available diagnostic evidence.

### 10. Selling Diving Livestock

Preserve the existing resale rules:

- Diving-acquired livestock may be sold to the ordinary Aquarium Store when eligible.
- The ordinary store offers 60% of the Deep Market reference buying quote.
- Deep Market sales require Reputation Level 5 or higher.
- Deep Market sales require a matching active Wanted Livestock request.
- A species not currently wanted cannot be sold to the Deep Market.

Keep the selected specimen's expedition provenance.

### 11. Save and Load

Persist:
- Dive region.
- Diving mode.
- Mystery encounter identity.
- Encounter position.
- Captured status.
- Hidden species assignment.
- Temporary inventory.
- Oxygen.
- Expedition state.
- Reveal state.
- Recovery result.

Determine and save each mystery fish's identity at encounter creation or another authoritative pre-reveal stage.

Do not allow repeated save loading to reroll the fish.

### 12. Required Tests

Verify:
1. Reef Diving creates at least one collectible mystery fish.
2. Deep Sea Diving creates at least one collectible mystery fish.
3. Encounter is reachable with sufficient oxygen for return.
4. Fish remains unidentified before reveal.
5. Question-mark silhouette renders correctly.
6. Capture requires valid range and inventory capacity.
7. Inventory does not exceed eight slots.
8. Failed dives do not grant permanent livestock.
9. Successful return triggers species reveal.
10. Region-specific eligibility works.
11. Habitat-depth restrictions work.
12. Species assignment persists across save/load.
13. The same encounter cannot be collected twice.
14. Post-dive survival rules still work.
15. Aquarium compatibility checks still work.
16. Resale rules remain unchanged.
17. Aquarium simulation time continues during diving.
18. Freshwater remains locked.
19. Game remains fully offline.

Do not claim a test passed unless it was actually performed.

### 13. Future Feature — Expanded Ocean Exploration

Record a future development concept inspired by the sense of discovery found in underwater exploration games such as Endless Ocean.

Possible future features:
- Larger underwater maps.
- Different ocean depths.
- Expanded marine ecosystems.
- Discoverable marine habitats.
- Underwater photography.
- Marine species observation.
- Research discoveries.
- Hidden underwater locations.
- Rare encounters and environmental events.

Use original designs, mechanics, UI, and artwork.

Do not copy another game's protected assets, maps, interface, characters, or distinctive creative content.

**This is a future feature only. Do not implement the expanded exploration system in this update.**

### 14. Documentation

Update the existing diving system's primary section in the consolidated Master Development Prompt.

Update DEVELOPMENT_STATUS.md and relevant gameplay documentation.

Add this permanent rule:

"Every valid Reef Diving and Deep Sea Diving expedition must provide at least one reachable mystery fish encounter. Its species is concealed using a question-mark silhouette until successful return to the boat. Geographic eligibility, inventory, oxygen, post-dive survival, and save persistence remain mandatory."

Do not duplicate the diving system elsewhere in the MDP.

### 15. Completion Requirement

When authorized edits are genuinely completed, report:
- Files changed.
- Mystery fish encounter implementation.
- Species selection logic.
- Silhouette artwork.
- Save persistence.
- Tests passed and failed.
- Known limitations.

End the final response with the exact standalone line:

Done With Edits

Do not claim completion when work is incomplete.

## FINAL DIRECTIVE

Implement guaranteed mystery fish encounters in Reef Diving and Deep Sea Diving.

Conceal their identity until the player successfully returns to the boat.

Preserve all existing mechanics, regional restrictions, mortality tracking, livestock valuation, Deep Market rules, and offline simulation.

Keep freshwater locked.
