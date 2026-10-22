# AQUARIUM LIFE — EQUIPMENT INVENTORY & INTERFACE REORGANIZATION
## Master Implementation Prompt — Codex GPT-6 Astra
### Saltwater Development | Consolidated Update

## 1. PRIMARY OBJECTIVE

Implement five approved changes to Aquarium Life:

1. Add an Inventory tab inside Equipment that displays ONLY player-owned items currently in storage, not installed or placed inside any aquarium.
2. Remove the obsolete Breeding & Eggs tab from the Field Journal.
3. Move Leaderboard Preview into the main sidebar, directly above VIP Store.
4. Remove the standalone Temperature Control section from Equipment → Tank Care.
5. Remove the Overnight Readiness section from Equipment → Tank Care.

**CRITICAL: Every aquarium must operate independently with its own installed equipment.**

Do not create an account-wide equipment system that allows one heater, filter, pump, or other physical item to operate across multiple aquariums.

The player's Inventory represents physical storage, not shared aquarium equipment.

This prompt supersedes all previous inventory-related prompts and corrections.

Before modifying code, audit the existing equipment, inventory, purchasing, placement, saving, navigation, and UI systems.

Preserve all established game mechanics, save data, and approved visual design.

Freshwater remains locked and noninteractive.

---

## 2. INVENTORY TAB — EQUIPMENT

Add a new tab inside the existing Equipment interface named:

**Inventory**

### 2.1 Inventory purpose

Inventory must display ONLY items that:

- Belong to the current player profile.
- Are not installed in any aquarium.
- Are not physically placed inside any aquarium.
- Have not been sold, discarded, consumed, or destroyed.
- Are eligible for storage under the existing game rules.

The Inventory is a storage location for items currently not in use.

### 2.2 Inventory contents

Include supported stored items such as:

- Heaters.
- Chillers.
- Filters.
- Pumps.
- Aeration equipment.
- Aquarium lighting.
- Protein skimmers.
- Automatic feeders.
- Testing equipment.
- Coral fragging tools and supplies.
- Unplaced rocks.
- Unplaced decorations.
- Other compatible physical aquarium items.

Only show items actually owned by the player.

Do not invent new product types simply to populate the Inventory.

Living fish and coral remain managed by the appropriate livestock and receiving systems unless an existing approved holding or quarantine system specifically applies.

Do not treat living specimens as ordinary stored equipment.

### 2.3 Inventory exclusions

Do not display:

- Equipment installed in a tank.
- Rocks already placed inside a tank.
- Decorations already placed inside a tank.
- Supplies already consumed.
- Items already sold.
- Items belonging to another player profile.
- Items currently assigned to another valid physical location.

Do not create an "Installed by Aquarium" section inside the Inventory.

Installed equipment remains visible through the appropriate individual aquarium equipment interface.

---

## 3. AQUARIUM-SPECIFIC EQUIPMENT OWNERSHIP

Every aquarium maintains its own installed equipment collection.

### Example

Aquarium A — 20 Gallons:
- Heater A.
- Filter A.
- Circulation Pump A.

Aquarium B — 80 Gallons:
- Heater B.
- Filter B.
- Circulation Pump B.

These are separate physical pieces of equipment.

Heater A cannot heat Aquarium B.

Filter A cannot filter Aquarium B.

One equipment item cannot operate in two aquariums simultaneously.

### Permanent rules

1. Every installed equipment instance has a unique persistent ID.
2. An installed item is assigned to exactly one aquarium.
3. Its effects apply only to that aquarium.
4. Installed items do not appear in Inventory.
5. Removing an item returns that exact instance to Inventory.
6. Item condition and durability are preserved during removal.
7. Equipment may be installed into another compatible aquarium after removal.
8. Equipment is never duplicated by installation, removal, switching tanks, or save/load.
9. Each aquarium requires its own adequate life-support equipment.
10. Equipment compatibility checks examine only equipment actually installed in that aquarium.

Do not interpret account ownership as shared equipment operation.

---

## 4. PURCHASING AND STORING EQUIPMENT

When a player buys equipment from Aquarium Store:

1. Validate the purchase.
2. Deduct the correct AC amount.
3. Create or transfer ownership of the purchased item exactly once.
4. Add the item to Inventory.
5. Make it available for installation in a compatible aquarium.
6. Persist the transaction.

Do not automatically install purchased equipment unless the player explicitly chooses an existing supported direct-install workflow.

### Inventory item information

Display:
- Item name.
- Pixel-art thumbnail.
- Category.
- Quantity, where stacking is valid.
- Durability or condition.
- Equipment specifications.
- Compatibility information.
- Install or Place action where appropriate.

Allow search and category filtering.

Do not stack equipment instances with different durability, modifications, or persistent identity in a way that loses their individual attributes.

---

## 5. INSTALLING ITEMS FROM INVENTORY

Players must be able to install stored equipment into any compatible aquarium they own.

### Workflow

1. Open Equipment → Inventory.
2. Select a stored item.
3. Click Install or Place.
4. Select a destination aquarium.
5. Display aquarium compatibility.
6. Confirm installation.
7. Remove the item from Inventory.
8. Assign it exclusively to the destination aquarium.
9. Activate the appropriate equipment effects.
10. Save the change.

If installation fails, the item must remain safely in Inventory.

### Compatibility

Validate:
- Aquarium type.
- Actual aquarium volume.
- Equipment capacity.
- Installation requirements.
- Available equipment positions or slots.
- Existing equipment conflicts.
- Placement restrictions.

Incompatible tanks should be shown with clear explanations.

Do not allow the same item to be installed twice.

---

## 6. REMOVING EQUIPMENT AND OBJECTS

When a player removes equipment from an aquarium:

1. Identify the installed item.
2. Check removal requirements.
3. Warn about potential life-support risks.
4. Deactivate its effects on that aquarium.
5. Remove its aquarium assignment.
6. Return that same item to Inventory.
7. Preserve condition, durability, and modifications.
8. Update the tank simulation.
9. Save the transaction.

Removing a working heater may cause the aquarium temperature to change naturally.

Removing a working filter may affect water quality.

Do not automatically protect the aquarium from genuine consequences.

### Rocks and decorations

When removable rocks or decorations are taken out:

- Return them to Inventory.
- Preserve their identity and attributes.
- Respect attached coral and placement dependencies.
- Do not silently delete attached livestock.
- Require safe reattachment or block removal where necessary.

---

## 7. REMOVE BREEDING & EGGS FROM FIELD JOURNAL

The Breeding & Eggs tab is still visible despite previous requests to remove it.

Remove it completely from the Field Journal's top-level navigation.

Audit all navigation and UI registrations to ensure the tab does not reappear after reopening the page or reloading the game.

### Important distinction

**Remove the tab, not the breeding system.**

Preserve:
- Autonomous pair formation.
- Courtship.
- Reproductive sex and role changes.
- Gravid females.
- Spawning.
- Eggs and clutches.
- Mouthbrooding.
- Hatching.
- Offspring development.
- Genetic inheritance.
- Breeding histories.

### Where breeding information belongs

**Individual Livestock Inspector**
- Biological sex or reproductive role.
- Pair status.
- Partner.
- Courtship.
- Gravid or brooding status.
- Reproductive readiness.

**Livestock Collection**
- Current offspring.
- Eggs and clutches.
- Baby and juvenile livestock.

**Tank History**
- Pair formation.
- Courtship events.
- Spawning.
- Egg laying.
- Hatching.
- Failed breeding events.
- Growth milestones.

**Species Encyclopedia**
- Reproductive biology.
- Pairing requirements.
- Sex changes.
- Species-specific reproduction.

Do not reintroduce a manual Begin Courtship button.

Existing saved breeding information must remain intact.

Redirect any saved navigation state pointing to the removed tab to a valid Field Journal section.

---

## 8. MOVE LEADERBOARD PREVIEW TO MAIN SIDEBAR

Remove Leaderboard Preview from the Field Journal navigation.

Add it to the main left sidebar.

### Required sidebar order

1. Aquariums.
2. Aquarium Store.
3. Field Journal.
4. Equipment.
5. The Dock Casino.
6. Leaderboard Preview.
7. VIP Store.
8. Settings.

Leaderboard Preview must appear directly above VIP Store.

Use the existing sidebar styling, icon dimensions, and spacing.

Do not create an oversized new navigation button.

### Preserve leaderboard functionality

Leaderboard Preview must continue to support:

- Saltwater aquarium rankings.
- Freshwater preview presentation where previously authorized.
- Rankings based on aquarium asset value, not the player's AC wallet.
- Clearly labeled demonstration rankings.
- Offline operation.

Do not introduce a server or real online leaderboard.

Freshwater must remain locked and noninteractive.

The relocated sidebar entry should open the existing leaderboard interface.

Avoid duplicate leaderboard implementations.

---

## 9. REMOVE TEMPERATURE CONTROL FROM TANK CARE

Remove the standalone Temperature Control panel from:

Equipment → Tank Care

The panel must no longer be rendered or occupy layout space.

### Preserve temperature management

Do not remove:
- Water temperature simulation.
- Heater thermostats.
- Chiller thermostats.
- Temperature monitoring.
- Temperature warnings.
- Livestock temperature compatibility.
- Equipment capacity limits.
- Heating and cooling behavior.
- Temperature history.

### Heater and chiller controls

Temperature targets should be configured through the individual installed heater or chiller's equipment controls.

For example:

Equipment → Installed Heater → Thermostat Setting

The actual aquarium water temperature remains visible in the Water & Wellbeing panel.

Do not allow thermostat changes to instantly set the water temperature.

Heating and cooling must continue following the existing simulation.

If the removed Temperature Control panel contains the only way to configure a thermostat, relocate that control before deleting the panel.

---

## 10. REMOVE OVERNIGHT READINESS FROM TANK CARE

Remove the standalone Overnight Readiness panel from:

Equipment → Tank Care

The panel must no longer be rendered or occupy layout space.

### Preserve the underlying systems

Do not delete:
- Offline progression.
- Food forecasts.
- Equipment condition tracking.
- Temperature simulation.
- Water chemistry simulation.
- Mortality tracking.
- Historical reports.
- Relevant aquarium warnings.

### Historical information

Any historical reports that previously appeared in Overnight Readiness should remain accessible through:

Field Journal → Tank History → Reports

Retain current actionable warnings in their appropriate existing interfaces.

Do not automatically create a new report every time the player opens Tank History.

Tank Care should concentrate on active maintenance and equipment operation.

---

## 11. UI AND VISUAL DESIGN

Preserve Aquarium Life's current premium dark interface.

Use:
- Black and dark backgrounds.
- Slate-blue panels.
- Compact navigation.
- Consistent spacing.
- Readable text.
- Approved pixel-art inventory icons.
- Existing modal styling.

Do not redesign unrelated screens.

After removing Temperature Control and Overnight Readiness, allow the remaining Tank Care content to reflow naturally.

Do not leave large empty gaps.

Ensure Inventory works correctly with different browser window sizes.

---

## 12. SAVE/LOAD AND DATA MIGRATION

Inspect the existing equipment and storage architecture.

Create safe migrations where necessary.

### Required safeguards

- Existing installed equipment stays installed in its correct tank.
- Existing stored equipment appears in Inventory exactly once.
- Item IDs remain stable.
- Item durability remains stable.
- Equipment upgrades remain attached to the correct instance.
- Rocks and decorations retain their correct location.
- Account profiles remain isolated.
- No equipment is deleted.
- No equipment is duplicated.
- AC purchase records remain consistent.

Do not copy all installed equipment into Inventory during migration.

Each item must have one authoritative physical location.

Use safe transactional ownership changes for purchase, installation, removal, and transfer.

---

## 13. REQUIRED TESTING

Test all of the following:

### Inventory

1. Inventory tab appears under Equipment.
2. Inventory contains only stored items.
3. Installed equipment does not appear in Inventory.
4. Placed rocks do not appear in Inventory.
5. Placed decorations do not appear in Inventory.
6. Purchased equipment enters Inventory.
7. Equipment can be installed into any compatible tank.
8. Installation removes the item from Inventory.
9. Removal returns the same item to Inventory.
10. Item durability survives transfers.
11. Failed installations do not lose items.
12. Double-clicking cannot duplicate items.
13. Saving and reloading preserves ownership.
14. Different player profiles cannot access each other's inventory.

### Aquarium independence

15. Each aquarium uses only its own equipment.
16. Equipment cannot operate in multiple tanks simultaneously.
17. Removing a heater affects only its original aquarium.
18. Removing a filter affects only its original aquarium.
19. Tank switching does not duplicate equipment.

### Field Journal

20. Breeding & Eggs tab is completely removed.
21. Automatic breeding continues.
22. Eggs and offspring remain accessible.
23. Breeding records remain available in Tank History.
24. Leaderboard Preview no longer appears in Field Journal.

### Sidebar

25. Leaderboard Preview appears directly above VIP Store.
26. The Dock Casino remains above Leaderboard Preview.
27. Existing sidebar functions continue operating.

### Tank Care

28. Temperature Control panel is removed.
29. Overnight Readiness panel is removed.
30. Heater and chiller thermostats still work.
31. Aquarium temperature simulation continues.
32. Historical readiness reports remain accessible.
33. No unnecessary empty layout gaps remain.

### General

34. Existing saves continue loading.
35. No livestock is deleted or duplicated.
36. The game remains fully offline.
37. Freshwater remains locked and noninteractive.

Report which tests passed, failed, or were not executed.

Do not claim unperformed tests passed.

---

## 14. DOCUMENTATION

Update the relevant home sections of the consolidated 31-section Aquarium Life Master Development Prompt.

Also update:
- GAME_DESIGN.md.
- UI_SPECIFICATION.md.
- DEVELOPMENT_STATUS.md.
- Equipment inventory documentation.
- Save-schema documentation.
- Project continuity notes.

### Permanent locked rules

**Inventory:** The Inventory tab shows only player-owned physical items that are not currently installed or placed inside any aquarium.

**Equipment independence:** Each aquarium operates using only equipment physically installed in that aquarium. Equipment cannot operate in multiple tanks simultaneously.

**Item location:** Every physical item exists in exactly one location: storage, one aquarium, or another valid existing state.

**Breeding navigation:** Breeding & Eggs is not a top-level Field Journal tab. Breeding happens autonomously, and its information is accessible through the appropriate existing systems.

**Leaderboard:** Leaderboard Preview is a main-sidebar entry directly above VIP Store.

**Tank Care:** Standalone Temperature Control and Overnight Readiness panels are removed, while thermostat controls and simulation/reporting functions remain available in their appropriate locations.

Do not duplicate these definitions across unrelated design sections.

---

## 15. COMPLETION REQUIREMENT

After all authorized implementation work has genuinely completed, provide:

1. Files modified.
2. Inventory implementation details.
3. Equipment installation and removal behavior.
4. Save migrations.
5. Breeding tab removal.
6. Leaderboard relocation.
7. Tank Care cleanup.
8. Tests executed and results.
9. Remaining limitations or blockers.

The final standalone line must be exactly:

Done With Edits

Do not use this completion line if required authorized work remains unfinished.

# FINAL DIRECTIVE

Implement the finalized Inventory system as physical storage for uninstalled and unplaced items only.

Keep all installed equipment tied exclusively to its individual aquarium.

Remove Breeding & Eggs from Field Journal navigation.

Move Leaderboard Preview into the main sidebar immediately above VIP Store.

Remove standalone Temperature Control and Overnight Readiness panels from Tank Care without removing their underlying functionality.

Preserve existing gameplay, saved accounts, visual design, and fully offline operation.

Keep freshwater locked.
