# AQUARIUM LIFE — INTERACTIVE SALTWATER TUTORIAL OVERHAUL
## Master Implementation Prompt — Codex GPT-6 Astra
### Guided Click-by-Click Onboarding | Saltwater Only

## 1. PRIMARY OBJECTIVE

Replace the existing passive tutorial, which displays corner pop-ups with a Next button, with a fully interactive guided onboarding system.

The player must learn Aquarium Life by navigating the actual interface and performing real actions.

The tutorial must guide players through the complete process of setting up a saltwater aquarium, establishing safe water conditions, installing equipment, cycling the aquarium, purchasing compatible fish and introducing those fish into the tank.

Every required UI element must be visually highlighted.

The player must click the appropriate controls and genuinely complete each task to advance.

Do not automatically complete tasks when the player presses a tutorial button.

Preserve the existing game UI, aquarium simulation, accounts, economy, purchases, livestock compatibility rules and offline architecture.

Freshwater remains locked and noninteractive.

---

## 2. INTERACTIVE TUTORIAL PHILOSOPHY

The tutorial must teach through direct interaction.

Replace the old behavior:

"Read instructions → Click Next → Read instructions → Click Next"

With:

"Read instruction → Highlight correct UI element → Player clicks → Perform real action → Validate result → Continue"

The tutorial controls should not perform the player's actions automatically.

The actual game interface is the tutorial environment.

Use a concise instruction tooltip anchored near the relevant UI element instead of a large persistent corner pop-up.

Progression is based on verified gameplay state, not merely opening the correct page.

---

## 3. HIGHLIGHTING SYSTEM

Implement a reusable, context-aware tutorial spotlight system.

### Visual requirements

When the player must interact with a particular control:

- Highlight the correct control.
- Add a clearly visible border or glow.
- Slightly dim unrelated interface areas where appropriate.
- Keep the highlighted control fully readable.
- Use a small directional arrow when helpful.
- Position an instruction tooltip near the target.
- Ensure the target remains clickable.
- Preserve the game's approved dark and slate-blue UI design.

The highlight must move to the next target after the player completes the current action.

### Example

Step: Open Equipment.

Highlight:
Left Sidebar → Equipment.

The player clicks Equipment.

Next highlight:
Equipment → Inventory or another relevant equipment section.

The player clicks the required control.

Next highlight:
The appropriate equipment item or Install action.

### Technical requirements

Do not use fixed screen coordinates.

Target actual DOM elements through stable identifiers or a centralized tutorial target registry.

Support:
- Browser resizing.
- Different screen resolutions.
- Sidebar layout changes.
- Scrolling within panels.
- Modals.
- Dropdown menus.
- Dynamic product lists.
- Tank switching.
- Keyboard navigation where supported.

Do not create an overlay that blocks the very control the player needs to click.

Do not let spotlight positioning become misaligned after opening a modal.

If a tutorial target is missing, show a recoverable error and log the missing target rather than trapping the player.

---

## 4. REQUIRED TUTORIAL SEQUENCE

Create a guided saltwater aquarium onboarding sequence.

Inspect the actual game architecture and adapt exact navigation to the currently implemented tabs and screens.

Do not invent nonexistent navigation or force users through obsolete UI elements.

### Phase 1 — Welcome and Aquarium Selection

Explain the objective:

"Let's build your first healthy saltwater aquarium."

Highlight:
- Aquariums.
- New Aquarium if the player does not already own a suitable tutorial tank.
- Tank selection.
- The main aquarium viewing area.

If the player already has a valid tank, use a supported tutorial path without forcing an unnecessary new purchase.

### Phase 2 — Aquarium Preparation

Guide the player through the actual preparation process.

Include:
- Understanding that the aquarium starts dry.
- Locating substrate.
- Selecting suitable sand.
- Purchasing or using owned substrate where required.
- Placing the substrate.
- Understanding and adjusting substrate depth.
- Filling the aquarium with saltwater through the real water-preparation system.

Do not assume a filled tank is biologically ready for livestock.

The existing water-preparation state must update correctly.

Do not reintroduce the previously repaired "Unprepared / dry" state bug.

### Phase 3 — Equipment Installation

Guide the player into the actual Equipment interface.

Highlight and explain:
- Equipment tab.
- Equipment Inventory.
- Installing owned equipment.
- Purchasing missing equipment through Aquarium Store.
- Choosing the correct destination aquarium.
- Filtration.
- Heater where appropriate.
- Circulation.
- Other genuinely required life-support equipment.

Each installed piece of equipment must belong exclusively to the selected aquarium.

Installed equipment must disappear from uninstalled Inventory.

Do not duplicate physical items.

### Phase 4 — Aquarium Hardscape

Guide the player through:
- Aquarium Store.
- Compatible rocks.
- Purchasing or selecting owned rocks.
- Placing rocks inside the aquarium.
- Creating appropriate shelter.
- Understanding safe positioning.

Only require a hardscape step when relevant to the tutorial's selected aquarium and species.

### Phase 5 — Water Temperature and Salinity

Highlight:
- Water & Wellbeing.
- Current temperature.
- Current salinity.
- Installed heater or chiller controls where applicable.
- Appropriate saltwater preparation controls.

Teach the difference between:
- Target equipment temperature.
- Actual aquarium temperature.

The player must observe actual water conditions approaching appropriate values.

Do not instantly force the aquarium to the desired temperature.

Do not recreate the removed standalone Temperature Control panel under Equipment → Tank Care.

### Phase 6 — Nitrogen Cycle

Explain:
- Ammonia.
- Nitrite.
- Nitrate.
- Beneficial bacterial colonies.
- Why cycling matters before introducing livestock.

Highlight the actual water chemistry display.

The tutorial must not falsely mark an aquarium cycled because the player viewed a tutorial message.

Wait for the existing authoritative nitrogen-cycle simulation to establish suitable biological filtration.

Provide legitimate in-game guidance and safe progression while the player waits.

Do not artificially skip days, zero ammonia, set bacterial colonies to maximum, or bypass required cycling rules.

### Phase 7 — Water Quality Verification

Guide the player through checking:
- Temperature.
- Salinity.
- pH.
- Ammonia.
- Nitrite.
- Nitrate.
- Dissolved oxygen.
- Filtration condition.
- Circulation.
- Prepared and cycled status.

Only require the parameters supported by the active aquarium simulation and relevant starter species.

Show whether the aquarium is actually suitable for introducing livestock.

If it is not ready, explain why.

### Phase 8 — Aquarium Store Navigation

Highlight:
- Aquarium Store.
- Saltwater.
- Fish category.
- Available fish listings.
- A suitable beginner-friendly fish.

Do not select a species solely based on rarity.

The recommended starter fish must be compatible with the player's actual aquarium volume, water chemistry and equipment.

Explain basic species care requirements.

Do not unlock freshwater.

### Phase 9 — Purchasing the First Fish

Guide the player through:
- Selecting a fish.
- Opening its information.
- Reviewing minimum tank requirements.
- Reviewing water-parameter compatibility.
- Understanding the price.
- Confirming purchase.

Use the actual store and AC ledger.

Do not give a free fish unless an established tutorial reward authorizes it.

Preserve the existing 5% breeding-pair store offer rule, but do not require a breeding pair for tutorial completion.

### Phase 10 — Receiving and Placing the Fish

Highlight the actual receiving or stocking interface.

Guide the player to:
- Select a compatible aquarium.
- Review receiving checks.
- Address any legitimate blocking conditions.
- Complete the receiving action.
- Observe the fish enter the aquarium.

Do not bypass quarantine requirements where applicable.

Do not hide incompatible tanks.

Preserve the shared receiving system used by store purchases and diving catches.

### Phase 11 — Feeding and Daily Care

Teach:
- Selecting appropriate food.
- Feeding the fish.
- Monitoring appetite.
- Avoiding overfeeding.
- Monitoring water chemistry.
- Understanding equipment condition.
- Recognizing livestock stress or illness.

Highlight the actual controls and livestock inspector.

Do not complete feeding objectives unless the real feeding event occurs.

### Phase 12 — Tutorial Completion

Once the first fish is successfully introduced and the player has demonstrated appropriate care, show a concise completion message.

Example:

"Your First Saltwater Aquarium Is Ready!"

Show:
- Completed tutorial milestones.
- Aquarium status.
- First livestock.
- Relevant achievement or quest progress.
- Existing approved tutorial rewards, if any.

Do not invent new AC or XP rewards without checking the current progression definitions.

---

## 5. TUTORIAL STATE MACHINE

Implement the tutorial as a persistent state machine.

Each step must define:
- Unique step ID.
- Required current UI context.
- Highlight target.
- Instruction text.
- Expected user action.
- Gameplay validation condition.
- Completion event.
- Next step.
- Recovery behavior if interrupted.

Do not advance solely because a player clicked the highlighted button when the underlying task remains incomplete.

Example:

Installing a filter:

Opening Equipment is not sufficient.

Opening Inventory is not sufficient.

Selecting a filter is not sufficient.

The step completes only when compatible filtration equipment is genuinely installed in the appropriate aquarium and the save state reflects the installation.

---

## 6. EXISTING PLAYERS AND ALREADY-COMPLETED TASKS

The tutorial must recognize real, previously completed aquarium setup actions.

Do not force experienced players to:
- Repurchase a tank.
- Remove established equipment.
- Empty an aquarium.
- Restart nitrogen cycling.
- Purchase duplicate items.
- Sell or replace healthy livestock.

If the current aquarium already satisfies a requirement, mark that requirement as satisfied using authoritative game state.

Provide a reviewable explanation of the completed requirement and proceed to the next incomplete step.

Never create false completion records.

---

## 7. TUTORIAL NAVIGATION AND PLAYER CONTROL

During active tutorial steps:

- Highlight the intended interaction.
- Guide players back if they navigate away.
- Prevent accidental advancement.
- Keep real gameplay controls functional when relevant.

Do not permanently lock the entire game interface.

Include:
- Pause Tutorial.
- Resume Tutorial.
- Restart Tutorial.
- Skip Tutorial, with confirmation.
- View Current Objective.

The Skip option is for the player to deliberately opt out.

It must not simulate completing aquarium setup or grant unearned achievements.

There should be no repeated Next button that allows bypassing required interactions.

---

## 8. SAVE/LOAD AND MULTIPLE AQUARIUMS

Persist tutorial progress per player profile.

Track:
- Tutorial started.
- Tutorial completed.
- Current step.
- Completed verified steps.
- Tutorial aquarium ID.
- Paused or skipped status.
- Relevant objective data.

Ensure:
- Reloading restores the correct tutorial state.
- Completed valid actions remain completed.
- The spotlight returns to the correct control.
- Deleted or sold tutorial aquariums are handled safely.
- Multiple aquariums do not confuse objective targeting.
- No duplicate AC or XP rewards.
- No duplicated equipment or livestock.

---

## 9. ACCESSIBILITY AND UI RESPONSIVENESS

The highlight must remain clear without relying on color alone.

Use:
- Visible outline.
- Instruction text.
- Optional arrow.
- Clear focus styling.
- Appropriate contrast.

Support keyboard focus and interaction where possible.

Respect reduced-motion settings.

Do not require rapid reactions or precise pointer movement.

Use existing modal close behavior unless a genuine transaction requires confirmation.

The tutorial must work on supported desktop resolutions without clipping important controls.

---

## 10. DEBUGGING AND TESTING

Use the existing Local Debug Log in Settings.

Log:
- Tutorial step started.
- Target resolved.
- Required action performed.
- Validation passed.
- Validation failed.
- Step completed.
- Step skipped.
- Missing UI target.
- Save/restoration events.

Do not spam logs continuously every rendered frame.

### Required tests

Verify:

1. Tutorial launches for eligible new saltwater profiles.
2. Highlighting follows the correct UI target.
3. Player must click actual tabs and controls.
4. No Next-button bypass exists.
5. Highlight remains aligned after resizing.
6. Highlight remains aligned inside modals.
7. Aquarium creation works.
8. Substrate placement works.
9. Saltwater preparation works.
10. Equipment installation works.
11. Equipment Inventory does not duplicate items.
12. Rock placement works.
13. Temperature controls remain functional.
14. Water chemistry checks use real values.
15. Nitrogen cycling cannot be bypassed.
16. Compatible fish selection works.
17. Purchase transactions remain correct.
18. Fish receiving works.
19. Fish placement completes correctly.
20. Feeding objective requires real feeding.
21. Save/reload restores progress.
22. Existing players are not forced to restart.
23. Pausing and resuming works.
24. Skipping does not give unearned rewards.
25. Missing targets do not trap the player.
26. Aquarium switching is handled correctly.
27. Game remains offline.
28. Freshwater stays locked.

Report actual test results.

---

## 11. DOCUMENTATION

Update the appropriate tutorial and UI home sections in the consolidated 31-section Aquarium Life Master Development Prompt.

Also update:
- GAME_DESIGN.md.
- UI_SPECIFICATION.md.
- DEVELOPMENT_STATUS.md.
- Tutorial state machine documentation.
- Save-schema documentation.
- Project continuity notes.

Add this permanent rule:

"The Aquarium Life saltwater onboarding tutorial is an interactive, guided gameplay experience. The player is directed through real interface controls using visible highlights and contextual instructions. Tutorial progression requires verified aquarium setup actions, not pressing Next. The tutorial covers creating and preparing a saltwater aquarium, installing life-support equipment, establishing the nitrogen cycle, purchasing compatible livestock, receiving livestock, and basic feeding and care."

Do not duplicate this rule across unrelated systems.

---

## 12. COMPLETION REQUIREMENT

When all authorized edits are genuinely completed, report:

1. Files modified.
2. Tutorial system changes.
3. Old tutorial interface removed.
4. Spotlight/highlight implementation.
5. Tutorial steps implemented.
6. State validation system.
7. Save/load changes.
8. Existing-player handling.
9. Accessibility checks.
10. Tests passed.
11. Tests failed or untested.
12. Remaining limitations.

Only when all authorized tasks are genuinely complete, finish with:

Done With Edits

# FINAL DIRECTIVE

Replace the passive corner-pop-up tutorial with a fully interactive saltwater aquarium setup tutorial.

Guide the player through the actual game UI using clear highlighted controls and real task completion requirements.

Start with aquarium setup and finish with safely introducing and caring for the first fish.

Preserve every established biological, equipment, economy and progression rule.

Keep the game entirely offline and freshwater locked.
