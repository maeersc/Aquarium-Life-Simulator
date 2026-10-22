# AQUARIUM LIFE — COMPLETE INTERACTIVE TUTORIAL AUDIT & LOOP REPAIR
## Master Implementation Prompt — Codex GPT-6 Astra
### Priority: Critical Tutorial Bug Fix | Saltwater Only

## 1. PRIMARY OBJECTIVE

The Aquarium Life interactive tutorial contains a navigation or progression loop near the beginning.

This is a critical onboarding issue because new players may become confused, repeat actions unnecessarily, or become unable to progress.

Your responsibility is to audit, repair, and validate the ENTIRE interactive saltwater tutorial.

Do not merely patch the first visible loop.

Inspect every tutorial step, UI highlight, navigation transition, completion condition, and saved progression state.

The goal is a clear, logical, beginner-friendly experience that guides a new player from an empty saltwater aquarium to successfully introducing and caring for their first fish.

**Do not return to the old corner pop-up tutorial with a Next button.**

Preserve the interactive highlighted-control design.

---

## 2. REPRODUCE THE BEGINNING-OF-TUTORIAL LOOP

Start by running the game as a completely new player.

Use a disposable test profile or isolated test save. Do not overwrite real player data.

Follow the tutorial exactly as instructed.

Record:
- Tutorial step ID.
- Displayed instruction.
- Highlighted control.
- Required player action.
- Actual navigation destination.
- Completion condition.
- Next tutorial step.
- Any unexpected return to a previous step.

Identify precisely where the loop occurs.

Investigate whether the cause is:
- Repeated event listeners.
- Conflicting tutorial states.
- Incorrect completion conditions.
- Navigation resetting the tutorial.
- Steps referencing outdated UI tabs.
- Missing equipment or purchase validation.
- Incorrect save restoration.
- A completed step becoming incomplete.
- Two steps repeatedly directing the player to each other.
- A highlighted target becoming unavailable.
- State updates occurring in the wrong order.

Fix the actual root cause.

Do not hide the loop by automatically skipping affected steps.

---

## 3. AUDIT THE COMPLETE TUTORIAL FLOW

Inspect every tutorial step in the live codebase.

Create a documented flow showing:

**Current Step → Required Action → Validated Result → Next Step**

Every required action must lead toward successful aquarium setup.

Detect:
- Circular dependencies.
- Unreachable steps.
- Dead ends.
- Repeated instructions.
- Missing prerequisites.
- Invalid navigation targets.
- Contradictory instructions.
- Unexpected tutorial resets.
- Steps that cannot complete.
- Steps that complete without the required action.

Do not assume the existing tutorial-step definitions are correct.

Use the actual implementation as the source of truth when diagnosing bugs, then reconcile it against the approved tutorial requirements.

### Loop prevention

Legitimate return visits to an interface are allowed when a different task requires them.

For example, revisiting Aquarium Store to buy fish after purchasing equipment is acceptable.

However, the tutorial must not repeatedly instruct a player to perform the same completed action without a meaningful reason.

---

## 4. REVIEW TUTORIAL LANGUAGE

Review every player-facing instruction.

Instructions must be:
- Short.
- Clear.
- Grammatically correct.
- Appropriate for someone who has never played Aquarium Life.
- Specific about what the player should click.
- Consistent with the actual interface.
- Free from unnecessary technical terminology.

Use the exact visible names of real controls.

Do not tell players to open tabs that no longer exist.

### Good example

"Click Equipment on the left sidebar to prepare your aquarium."

Then highlight Equipment.

After the click:

"Open Inventory to see the equipment you own."

Then highlight Inventory.

After opening Inventory:

"Select your filter and click Install."

Then highlight the correct available filter.

### Bad example

"Go prepare the aquarium equipment."

This is too vague.

Also avoid:

"Click Next to continue."

The actual player action should determine tutorial progression.

### Instruction placement

Use a concise tooltip near the highlighted control.

Do not cover:
- The target button.
- Important aquarium information.
- Purchase confirmations.
- Equipment selection controls.
- Water chemistry values needed for the current task.

---

## 5. VERIFY ALL HIGHLIGHT TARGETS

Every tutorial instruction must highlight the correct interactive control.

Check:
- Main sidebar buttons.
- Aquarium dropdown.
- New Aquarium.
- Aquarium Store tabs.
- Product cards.
- Quantity controls where relevant.
- Equipment.
- Inventory.
- Install and Place actions.
- Water & Wellbeing.
- Heater and filter inspectors.
- Water preparation.
- Substrate placement.
- Rock placement.
- Fish purchase.
- Aquarium receiving.
- Feeding controls.

Only highlight controls that genuinely exist in the current game.

Use stable UI identifiers rather than hardcoded pixel coordinates.

### Target behavior

When a tutorial step becomes active:

1. Locate the target.
2. Scroll it into view if needed.
3. Apply the highlight.
4. Display the correct instruction.
5. Wait for the real required interaction.
6. Validate the gameplay result.
7. Clear the old highlight.
8. Activate the next step.

Ensure the highlight does not block clicking.

If a target cannot be found, log the issue and provide recovery rather than trapping the player.

---

## 6. ESTABLISH A CORRECT SALTWATER SETUP ORDER

Confirm the tutorial teaches a sensible aquarium setup sequence.

The expected learning progression is:

### Stage 1 — Getting Started

- Introduce the aquarium screen.
- Identify or create the tutorial aquarium.
- Explain that a new tank starts dry.
- Show where tank information is located.

### Stage 2 — Preparing the Aquarium

- Obtain suitable substrate.
- Place substrate in the aquarium.
- Obtain and arrange suitable rocks where applicable.
- Prepare and add saltwater through the real game systems.

### Stage 3 — Installing Life Support

- Open Equipment.
- Open Inventory when equipment is already owned.
- Obtain missing equipment through Aquarium Store.
- Install an appropriate filter.
- Install necessary heating or cooling equipment.
- Set up appropriate circulation and other required life support.

### Stage 4 — Stabilizing Conditions

- Verify actual water temperature.
- Verify salinity.
- Explain ammonia, nitrite, and nitrate.
- Establish the nitrogen cycle.
- Confirm the receiving system recognizes the tank as prepared and cycled.

### Stage 5 — Choosing Livestock

- Open Aquarium Store.
- Navigate to Saltwater Fish.
- Inspect a suitable beginner fish.
- Review care requirements.
- Purchase one appropriate fish.

### Stage 6 — Introducing Livestock

- Choose the prepared aquarium.
- Review receiving checks.
- Complete valid receiving or acclimation.
- Observe the fish entering the aquarium.

### Stage 7 — Basic Care

- Inspect the fish.
- Choose suitable food.
- Feed appropriately.
- Check health and water conditions.
- Complete onboarding.

Adapt individual steps to existing real mechanics and supported navigation.

Do not invent controls to match this outline.

Do not bypass the nitrogen cycle or fabricate safe water values.

---

## 7. REMOVE INVALID OR OBSOLETE TUTORIAL REFERENCES

The tutorial must reflect the current Aquarium Life interface.

Specifically:

- Do not reference the removed Breeding & Eggs Field Journal tab.
- Do not direct players to the removed standalone Temperature Control panel in Tank Care.
- Do not direct players to the removed Overnight Readiness panel.
- Recognize that Inventory shows only uninstalled and unplaced items.
- Recognize that installed equipment belongs exclusively to its aquarium.
- Use the real heater or chiller controls for thermostat changes.
- Use the actual Aquarium Store purchase and installation workflows.
- Do not direct players to freshwater gameplay.

Audit the latest implemented navigation names instead of assuming older documentation still matches the game.

---

## 8. PREVENT PROGRESSION SOFTLOCKS

No tutorial step should become impossible because:
- A required item has already been installed.
- A tank has already been filled.
- The aquarium is already cycled.
- A required item is unavailable from the current rotating store.
- The player temporarily lacks AC.
- A product stock count has changed.
- A modal closes unexpectedly.
- A tank is switched.
- The game is saved and reopened.
- An expected UI control is disabled.
- The player pauses the tutorial.
- The player returns from Ocean Diving or another screen.

If the required gameplay state is already valid, recognize that state and mark the step satisfied.

If the player lacks resources, show the actual requirement and a supported way to resolve it.

Do not grant free items, AC, XP, or livestock just to force progression.

Do not repeatedly reset completed tutorial tasks.

---

## 9. TUTORIAL STATE MANAGEMENT

Review the tutorial state machine.

Each step must have:
- Stable unique ID.
- Explicit prerequisites.
- Correct UI target.
- Clear instruction.
- Completion validator.
- Defined next step.
- Persistent completion state.
- Recovery behavior.

### Transition safety

Prevent:
- Multiple step advances from one click.
- Reentrant state updates.
- Duplicate event handlers.
- Recursive navigation loops.
- Out-of-order progression.
- Stale references.
- Repeated reward grants.
- Save/load rewinding completed steps.

Transitions must be deterministic and idempotent.

Use an explicit completion event or authoritative state validation rather than fragile assumptions about which page is currently open.

### Loop detection

Add a development-only diagnostic that recognizes repeated unresolved step transitions or unexpected cycling between tutorial states.

Log:
- Previous step.
- Current step.
- Triggering event.
- Validation result.
- Relevant prerequisites.

Do not let logging itself change tutorial progress.

---

## 10. TEST THE EXPERIENCE AS A REAL PLAYER

After repairing the tutorial, perform complete end-to-end walkthroughs using the actual interactive game.

Do not treat a unit test of the tutorial state machine as sufficient proof that the highlighted UI works.

Where browser automation is available, use it to perform the real clicks, purchases, installations, and interactions.

### Test A — Brand-New Player

Use a clean test profile with the standard starting balance.

Complete onboarding from beginning to end.

Verify:
- Every instruction is understandable.
- Every highlight points to the correct control.
- No loops occur.
- No step is skipped incorrectly.
- The player understands why each task matters.
- The tutorial can actually be completed.

### Test B — Existing Player

Use a disposable save with:
- An existing aquarium.
- Installed equipment.
- Prepared saltwater.
- An established nitrogen cycle.
- Existing livestock.

Verify completed prerequisites are recognized.

Do not force unnecessary repurchases or resets.

### Test C — Interrupted Tutorial

Save and reload during:
- Aquarium preparation.
- Equipment installation.
- Cycling.
- Fish purchasing.
- Fish receiving.

Verify progress and highlights restore correctly.

### Test D — Error Recovery

Test:
- Insufficient AC.
- Incompatible equipment.
- Fish unsuitable for tank volume.
- Missing required equipment.
- Store stock changes.
- Missing tutorial highlight target.
- Switching aquariums.
- Closing and reopening menus.

Verify the tutorial explains how to recover and never becomes trapped in a loop.

### Test E — UI Layout

Test at multiple supported desktop browser sizes.

Check:
- Highlight alignment.
- Tooltip visibility.
- Modal placement.
- Scroll handling.
- Sidebar interaction.
- Keyboard focus.
- No blocked buttons.

### Test F — Deterministic Flow Audit

Create an automated test that evaluates the tutorial state graph.

Verify:
- Every required step is reachable.
- Every nonterminal step has a valid completion path.
- No unintended cycles exist.
- Every referenced navigation target is valid.
- The final completion state is reachable.

Do not report an end-to-end test as passed unless the real interactive sequence was actually executed.

---

## 11. OFFLINE AND BIOLOGICAL SIMULATION

Preserve the real aquarium simulation throughout the tutorial.

Do not:
- Fake nitrogen cycling.
- Automatically set ideal water chemistry.
- Grant permanent equipment.
- Introduce fish into unsafe tanks.
- Change the in-game clock to skip required biology.
- Pause ordinary aquarium simulation unnecessarily.
- Disable fish health or mortality systems.

Ensure the tutorial provides practical guidance when waiting for real biological processes.

Players may safely explore permitted interfaces while cycling continues, without losing their place in onboarding.

---

## 12. DEVELOPMENT REPORT

Create or update:

TUTORIAL_FULL_AUDIT_AND_REPAIR_REPORT.md

Include:

1. The exact root cause of the beginning-of-tutorial loop.
2. Steps involved in the loop.
3. Files modified.
4. The corrected tutorial flow.
5. All tutorial steps and their completion conditions.
6. Invalid targets discovered.
7. Instructions rewritten for clarity.
8. Softlocks corrected.
9. Save/load corrections.
10. Tests executed.
11. Tests passed.
12. Tests failed or not executed.
13. Any remaining limitations.

Provide a readable step-by-step tutorial map for future development.

Do not claim a browser walkthrough occurred unless the browser interface was actually exercised.

---

## 13. MASTER DOCUMENTATION

Update the tutorial's authoritative home section in the consolidated Aquarium Life Master Development Prompt.

Update:
- GAME_DESIGN.md.
- UI_SPECIFICATION.md.
- DEVELOPMENT_STATUS.md.
- Tutorial state machine documentation.
- Project continuity/handoff notes.

Preserve the established no-duplicate-documentation rule.

Add this permanent requirement:

**The interactive saltwater tutorial must be fully traversable from start to finish without unintended loops, dead ends, contradictory instructions, obsolete navigation references, or progression softlocks. Every required UI target must be highlighted, each instruction must match the actual interface, and progression must reflect verified gameplay actions.**

---

## 14. COMPLETION REQUIREMENT

After all authorized work is completed, report:

- What caused the tutorial loop.
- Exactly how it was fixed.
- Whether the entire tutorial was completed in a clean-profile browser walkthrough.
- Whether existing-player and save/load tests passed.
- Any steps that remain blocked or unverified.
- Files changed.

Only after genuinely completing all authorized work, end with the exact standalone line:

Done With Edits

Do not use this completion line if essential tutorial repair work is still incomplete.

# FINAL DIRECTIVE

Conduct a complete tutorial quality-assurance and repair pass.

Find and eliminate the early progression loop, then verify the entire saltwater onboarding experience as a real new player would encounter it.

Keep instructions simple, highlights accurate, progression logical, and every step achievable.

Do not replace the interactive tutorial with passive Next-button pop-ups.

Preserve all aquarium systems, player saves, economic rules and biological realism.

Freshwater remains locked.
