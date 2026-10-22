# AQUARIUM LIFE — CORAL FRAGGING & DIVING LIVESTOCK TRADING
## Codex GPT-6 Astra — Development Update v3.1
### Authorized Saltwater Implementation Prompt

## 1. Mission

Implement coral fragging and an improved livestock resale system in the existing Aquarium Life game.

This update must integrate with the current aquarium simulation, livestock catalog, asset valuation, economy, equipment, Deep Market, Ocean Diving, journal, and save systems.

**Saltwater development only. Freshwater remains locked.**

Before editing, inspect the current code, `CURRENT_LIVESTOCK_CATALOG.md`, and consolidated Master Development Prompt. Preserve existing livestock, accounts, and save data.

Do not build duplicate feeding, breeding, health, valuation, inventory, or store systems.

---

## 2. New Equipment — Coral Fragging Tools

Add a new category within the existing Equipment interface:

**Coral Fragging**

Introduce the following equipment:

| Equipment | Purpose |
|---|---|
| Coral Fragging Kit | Allows compatible soft coral and straightforward colony fragmentation actions |
| Precision Coral Cutters | Allows supported branching coral fragment removal |
| Coral Frag Saw | Allows supported stony coral fragmentation actions |
| Frag Plugs | Mounting support for new coral fragments |
| Frag Rack | Holds appropriately mounted frags in a compatible aquarium |
| Coral Mounting Supplies | Secures fragments to appropriate underwater supports |

Use fixed normal-store prices, determined through the existing equipment economy and balance checks.

Consumable frag plugs and mounting supplies must be deducted when used. Reusable tools must not disappear after one use unless their defined durability system requires replacement.

Do not assume one tool is appropriate for every species.

### Equipment availability

Players must:
1. Own the appropriate fragging tool.
2. Have an eligible mature coral.
3. Have enough mounting resources.
4. Have a suitable place for the resulting frag.

Coral fragging must not be an unlimited free duplication mechanic.

---

## 3. Frag Coral Action

When a player clicks an adult coral, add a button to its inspection modal:

**Frag Coral**

The button must show whether fragging is available or locked.

If locked, display the reason.

Possible reasons:
- Coral is immature.
- Coral is too small.
- Health is too low.
- Insufficient living tissue.
- Coral is diseased or experiencing major stress.
- Required equipment is missing.
- No valid frag mounting location is available.
- Coral is still recovering from earlier fragging.
- The species cannot safely use the selected fragmentation method.

### Fragging interface

Clicking Frag Coral opens a centered modal containing:

- Parent coral name.
- Scientific name.
- Current coral health.
- Coral maturity.
- Current size.
- Coral rarity.
- Available fragging tools.
- Number of eligible fragments.
- Required mounting resources.
- Estimated parent tissue loss.
- Estimated stress or injury risk.
- Expected fragment sizes.
- Estimated fragment values.
- Confirm Fragging button.
- Cancel button.

Keep the X in the upper-right corner, Escape support, and backdrop-click dismissal for noncommitted actions.

No cutting occurs before confirmation.

---

## 4. Biological Coral Fragging Rules

Use different rules for different coral types.

### Branching corals

Eligible mature branching corals can produce branch fragments.

Examples:
- Suitable branching SPS.
- Branching forms of certain LPS corals.

Each fragment must contain viable tissue and the necessary supporting structure.

### Mushroom corals

Support biologically appropriate tissue-based propagation.

Growth, attachment, and recovery differ from branching corals.

### Zoanthids

Use a colony-division model based on viable connected polyps and appropriate supporting substrate.

### Stony LPS corals

Differentiate branching and wall-type coral anatomy.

Do not assume that every hammer coral can be divided using the same method.

### Leather and other soft corals

Use suitable soft-coral fragmentation and attachment behavior.

### Safety and biological accuracy

The game should abstract hazardous handling actions rather than provide detailed real-world cutting instructions.

Some coral groups can contain dangerous toxins.

Coral fragmentation must be species-appropriate and medically safe within the game simulation.

---

## 5. Coral Health, Growth and Recovery

For the initial game-balancing baseline, require:

**At least 85% parent coral health** before fragging.

This is a proposed gameplay threshold, not a universal biological rule.

Allow more restrictive species-specific thresholds.

After fragging:
- Reduce the parent colony's size or living tissue.
- Apply an appropriate temporary stress effect.
- Recalculate parent coral current asset value.
- Create a separate fragment identity.
- Give the new fragment an appropriate starting health and tissue condition.
- Require mounting.
- Begin species-specific recovery and growth processes.

Parent coral and new frag must both remain subject to:
- Lighting.
- Flow.
- Water chemistry.
- Feeding.
- Disease.
- Tissue loss.
- Growth.
- Death.

Do not automatically kill a frag because it is small.

Do not guarantee survival after fragmentation.

Repeated fragging must require regrowth and recovery.

---

## 6. Coral Frag Genetics and Individual Identity

A newly created coral fragment is a new owned livestock individual.

It must have:
- Unique instance ID.
- Parent coral ID.
- Biological species ID.
- Genetic or clone lineage.
- Original rarity.
- Current health.
- Current size.
- Growth state.
- Current asset value.
- Disease status.
- Mounting location.
- Creation timestamp.
- Origin: Player Fragged.

Because fragment propagation is asexual, preserve the parent's genetic identity unless a previously approved mechanic explicitly supports variation.

Do not independently reroll the new fragment's rarity.

Do not invent a new species when a fragment is created.

Record fragment lineage in the Field Journal.

---

## 7. Coral Frag Asset Value

Every coral frag must have its own current AC value.

Its value should depend on:
- Species.
- Rarity.
- Fragment size.
- Number of viable polyps, where relevant.
- Living tissue.
- Health.
- Color and recognized strain/variety.
- Maturity.
- Growth quality.
- Disease.
- Genetic or lineage characteristics where appropriate.
- Current market demand.

A tiny fresh fragment should generally have a lower value than a healthy established colony of the same quality.

However, an unusually valuable species or verified phenotype may command a premium.

### Anti-exploit requirements

Fragmentation must not manufacture unlimited AC.

When a colony is divided:
- Recalculate the parent value.
- Assign realistic fragment values.
- Include cutting risks, recovery, resources, and dealer margins.
- Prevent splitting one coral into many fragments whose immediate combined resale value creates guaranteed profit.

All updates must be atomic and persistent.

---

## 8. Selling Coral Fragments

Players must be able to sell eligible coral frags through:

**Aquarium Store → Saltwater → Sell**

and, when eligible:

**Aquarium Store → Deep Market → Sell**

A fresh fragment may require a suitable establishment period before being accepted as healthy livestock.

Dealer offers must consider:
- Species.
- Rarity.
- Frag size.
- Health.
- Maturity.
- Polyp and tissue condition.
- Color/quality.
- Provenance.
- Demand.
- Dealer budget.

Use the centralized individual asset valuation system.

The current asset value displayed in the coral inspector must remain separate from the actual dealer's purchase offer.

Selling the fragment removes that exact owned individual from its tank or holding system and updates the tank's total value.

Never remove its parent by mistake.

---

## 9. Diving Livestock — Revised Sale Rules

Replace the previous restriction that diving-acquired livestock can only be sold through the Deep Market.

**New permanent rule:**

Livestock acquired through Ocean Diving can be sold through either:

1. Regular Aquarium Store.
2. Deep Market, if wanted and reputation-eligible.

All other diving requirements remain unchanged.

Preserve:
- Regional collection rules.
- Dive survival outcomes.
- Temporary inventory.
- Return-to-boat requirements.
- Health and quarantine.
- Individual animal provenance.
- Existing rarity.

### Regular-store buying policy

The normal store must provide a resale channel for eligible player-owned diving livestock.

This does not mean the normal store begins directly selling Tier 4–6 livestock in its public product listings.

Maintain the approved restriction:

**No direct Tier 4–6 livestock sales in the regular store.**

The regular store's buying and selling rules are separate.

---

## 10. Exact Dealer Price Difference

For diving-acquired livestock, the regular store must always offer:

**40% less than the Deep Market reference buy offer.**

Formula:

Regular Store Offer = Deep Market Reference Offer × 0.60

Examples:

| Deep Market reference offer | Regular store offer |
|---|---|
| 100 AC | 60 AC |
| 500 AC | 300 AC |
| 1,000 AC | 600 AC |
| 5,000 AC | 3,000 AC |
| 10,000 AC | 6,000 AC |

Use one centralized reference quote for both dealers.

The quote can reflect specimen health, species, size, rarity, and other authorized valuation modifiers.

Do not independently randomize two prices and then attempt to apply the discount.

Round monetary offers consistently to whole AC according to the existing economy policy.

### Critical distinction

The Deep Market reference offer is a price calculation, not a guaranteed active purchase offer.

Even when the Deep Market does not currently want the species, compute its reference value internally.

The normal store can still buy the specimen at 60% of that reference value.

This keeps the exact 40% discount rule consistent.

Prevent the player from selling a specimen twice through both dealers.

---

## 11. Deep Market — Wanted Livestock Board

Add a new section inside:

**Aquarium Store → Deep Market**

Name:

**Wanted Livestock**

The board shows which livestock the Deep Market is currently seeking to purchase.

This is a buying-request board, separate from the Deep Market's four rotating stock offers.

Do not increase the existing four-slot sale inventory.

### Wanted list details

Each wanted entry should show:
- Species common name.
- Scientific name.
- Rarity.
- Requested specimen type.
- Minimum acceptable health.
- Required maturity or size, if applicable.
- Reference dealer offer or quote range.
- Time remaining on the request.
- Any additional permitted conditions.

The board must use actual implemented species from the catalog.

Do not offer requests for nonexistent or unsupported livestock.

### Wanted list rotation

Use the established in-game timing system.

Rotate or refresh requests according to a documented schedule that supports persistence and offline progression.

Do not reroll the Wanted Livestock board each time the player closes and reopens the store.

A request's remaining duration must be saved.

### Species matching

Only matching livestock can be sold to the Deep Market.

Validate biological species ID and any specific request conditions.

Common-name text matching is not sufficient.

A fish with the wrong species identity must be rejected, even if its name appears similar.

---

## 12. Deep Market Selling Requirements

To sell diving-acquired livestock to the Deep Market, the player must satisfy BOTH:

1. Deep Market Reputation Level 5 or higher.
2. The specimen matches an active Wanted Livestock request.

If either requirement is missing, the Deep Market must refuse the sale.

Display the reason clearly.

Examples:

"Requires Deep Market Reputation Level 5."

"This species is not currently wanted."

"This specimen does not meet the requested condition."

### Reputation

Preserve the existing rule:

Players increase Deep Market reputation through completed purchases from the Deep Market.

Do not increase reputation for failed or canceled transactions.

Do not let players bypass reputation requirements by changing tanks or reloading.

### Frag sales

Coral fragments may also be offered to the Deep Market when they match an eligible wanted request.

Apply the reputation gate and request conditions to frag sales according to the same marketplace rules.

Coral fragments and naturally collected diving organisms must retain their distinct provenance.

---

## 13. Dealer Pricing for Other Livestock

For ordinary player-bred, purchased, or player-fragged livestock, use the existing dealer pricing and asset valuation rules unless explicitly superseded.

Coral frag prices must still reflect their actual individual condition and market demand.

Do not automatically apply the diving-specific 40% rule to all livestock origins.

Use clear provenance-based pricing policies.

Avoid overlapping price formulas that create contradictions.

---

## 14. Store Interface

Maintain the Aquarium Store's existing three main tabs:

- Saltwater.
- Freshwater — locked.
- Deep Market.

Under Saltwater, provide the existing Buy/Sell functionality.

Under Deep Market, include:
- Buy.
- Sell.
- Wanted Livestock.
- Reputation information.
- Existing restricted products.

Keep the four rotating Deep Market livestock stock slots separate from the Wanted Livestock board.

Selecting Sell should show eligible owned specimens from the currently selected aquarium or supported holding location.

Each listing should display:
- Livestock name.
- Health.
- Rarity.
- Stage or frag size.
- Current asset value.
- Actual dealer offer.
- Eligibility or refusal reason.

Preserve selected aquarium state.

---

## 15. Tutorial and Field Journal Integration

Add coral fragging education to the existing Saltwater tutorial and Field Journal.

Explain:
- Why corals need to mature.
- What equipment is required.
- Why frags need mounting.
- Why the parent coral loses size.
- Why new frags need recovery.
- How fragments grow.
- How coral fragments can be sold.

Also explain:
- Regular-store resale of diving livestock.
- The 40% discount from Deep Market reference offers.
- Deep Market Wanted Livestock requests.
- Reputation Level 5.
- Why the Deep Market may refuse a specimen.

Tutorial steps should demonstrate relevant actions without forcing the player to sacrifice a valuable coral.

---

## 16. Time, Simulation and Save Integrity

All coral health, frag recovery, growth, and Wanted Livestock board timers must use the existing authoritative game clock.

One in-game day remains 20 real minutes.

All existing aquariums continue simulating during:
- Diving.
- Deep Market browsing.
- Fragging modal interactions.
- Casino gameplay.
- Offline progression.

Save:
- Parent/child frag lineage.
- Tool ownership.
- Frag consumables.
- Parent recovery timers.
- Frag health and growth.
- Frag mounting data.
- Individual current asset values.
- Diving provenance.
- Active Wanted Livestock requests.
- Request expiry.
- Reputation.
- Completed resale transactions.

Prevent save/reload duplication of coral fragments, equipment, or AC.

---

## 17. Required Testing

Test and report:

1. Frag Coral appears on eligible adult coral inspectors.
2. Immature corals cannot be fragged.
3. Health restrictions work.
4. Correct equipment is required.
5. Missing tools prevent fragging.
6. Required consumables are deducted.
7. New fragments receive unique IDs.
8. Fragment species matches the parent.
9. Fragment genetics/lineage are preserved.
10. Parent coral loses the correct amount of tissue/size.
11. Parent and fragment health are independently simulated.
12. Parent and fragment values recalculate.
13. Coral mounting restrictions work.
14. Repeated fragging cannot create infinite livestock.
15. Frag sale transactions remove only the correct individual.
16. Diving livestock can be sold to the normal store.
17. The regular store offers exactly 60% of the Deep Market reference value.
18. Deep Market buying is refused below Reputation Level 5.
19. Deep Market buying is refused when a species is absent from Wanted Livestock.
20. A wanted species can be sold when all conditions are met.
21. Wanted Livestock requests persist through save/load.
22. Wanted Livestock request refresh does not exploit reopening.
23. The Deep Market retains exactly four rotating livestock stock slots.
24. Normal-store direct Tier 4–6 restrictions remain intact.
25. Aquarium asset value decreases correctly after sale.
26. AC increases exactly once after a successful sale.
27. The game remains fully offline.
28. Freshwater interactions remain disabled.
29. Existing saves and livestock data remain intact.
30. Coral recovery and Wanted List timers advance correctly while offline.

Clearly distinguish tests passed, failed, and untested.

---

## 18. Documentation and Permanent Rule Updates

Update:
- Consolidated 31-section Master Development Prompt.
- GAME_DESIGN.md.
- CURRENT_LIVESTOCK_CATALOG.md.
- DEVELOPMENT_STATUS.md.
- UI_SPECIFICATION.md.
- BALANCE_REPORT.md.
- Relevant equipment and gameplay documentation.
- Permanent locked-rules/continuity section.
- Updated project PDF, where PDF regeneration is supported.

Add these permanent rules:

**Rule A — Coral Fragging:** Mature, healthy eligible corals may be fragmented using the correct owned equipment. Fragments are independent livestock individuals retaining parent species and clone lineage. Parent tissue and value are reduced appropriately.

**Rule B — Coral Frag Valuation:** Coral frag prices depend on species, size, rarity, health, color/quality, maturity, and market conditions.

**Rule C — Diving Resale:** Diving livestock can be sold to either the regular Aquarium Store or the Deep Market.

**Rule D — Exact Discount:** The regular Aquarium Store always offers 60% of the calculated Deep Market reference buy value for the same diving specimen.

**Rule E — Wanted Livestock:** The Deep Market buys only eligible specimens matching its active Wanted Livestock board.

**Rule F — Reputation:** Deep Market sales of diving livestock require Reputation Level 5 or higher.

**Rule G — Store Integrity:** The Wanted Livestock board does not increase the four-slot rotating Deep Market stock inventory.

**Rule H — Freshwater Lock:** Freshwater development remains disabled until the player explicitly approves it.

Do not duplicate these mechanics across unrelated design sections; use cross-references.

---

## 19. Codex Completion Rule

After completing all authorized editing work, tell the player that the task is finished.

Report:
- Files edited.
- Systems completed.
- Coral-fragging equipment added.
- Resale formulas implemented.
- Wanted Livestock board behavior.
- Tests passed/failed.
- Known limitations.
- Documentation and PDF status.

If all authorized edits are genuinely completed, the very last standalone line must be exactly:

Done With Edits

Never claim completion when the work is incomplete.

# FINAL DIRECTIVE

Implement coral fragging with equipment requirements, species-specific behavior, parent/fragment health and valuation, and safe mounting.

Allow diving livestock to be sold through the regular store or Deep Market.

Use the exact 40% regular-store discount relative to Deep Market reference buy offers.

Require Reputation Level 5 and an active Wanted Livestock request for Deep Market sales.

Preserve all earlier Aquarium Life rules, the four-slot Deep Market inventory, existing saves, and the saltwater-only development scope.

Run tests and report completion.
