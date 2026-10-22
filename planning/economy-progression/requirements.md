# AQUARIUM LIFE — ECONOMY, PROGRESSION, EQUIPMENT & CASINO UPDATE
## Master Implementation Prompt — Codex GPT-6 Astra
### October 20, 2026 | Saltwater Development

## 1. PRIMARY OBJECTIVE

Implement the following seven changes:

1. Increase the 15,000-gallon aquarium purchase price from 5,000 AC to 25,000 AC.
2. Expand achievements and objectives with first-time livestock, aquarium-size and diving-location rewards.
3. Give players separate Maintenance and Replace Part options when servicing equipment.
4. Allow players to sell an entire aquarium and everything physically contained or installed in it.
5. Correct Gold Fish casino pair payouts to exactly 2× the original wager.
6. Move Optional Spending Limit and Recent Casino Visits into a new Profile tab inside The Dock Casino.
7. Introduce a 5% opportunity to purchase a compatible breeding pair when selecting a fish in the Aquarium Store.

Before making changes, inspect the actual codebase, existing data registries, UI, save structure, reward system, equipment definitions and casino implementation.

Implement these changes within existing systems rather than creating duplicates.

Do not alter unrelated mechanics.

Freshwater remains locked and noninteractive.

The game must remain completely offline.

---

## 2. AQUARIUM PRICE CORRECTION

### 2.1 Required Price

Change the 15,000 US-gallon aquarium purchase price:

OLD: 5,000 AC

NEW: 25,000 AC

This must be the authoritative price everywhere.

Update:
- Aquarium purchase screen.
- Tank catalog.
- New aquarium purchase confirmation.
- AC affordability checks.
- Purchase ledger.
- Tank shell asset valuation where purchase price is used.
- Related UI tooltips and help text.
- Tests and documentation.

Do not leave conflicting prices in separate files.

### 2.2 Existing Accounts

Do not charge players who already purchased this aquarium at the previous price.

Do not retroactively subtract an additional 20,000 AC.

Existing aquarium ownership remains unchanged.

Do not unintentionally change other tank prices.

---

## 3. NEW ACHIEVEMENTS AND OBJECTIVES

Expand the existing achievements and objectives system.

These rewards must be profile-specific, persistent and protected against duplicate claims.

### 3.1 First-Time Livestock Discovery

Reward:

**+50 Keeper XP**
**+50 AC**

Trigger when a player successfully obtains a biological livestock species they have never owned before.

Examples:
- First Ocellaris Clownfish.
- First Royal Gramma.
- First Chalk Bass.
- First Yellow Tang.
- First implemented coral species.
- First implemented bottom-dwelling animal species.

A player receives the reward once for each newly discovered biological species.

Example:

The player obtains their first Chalk Bass.

Award:
+50 XP
+50 AC

The player later obtains a second Chalk Bass.

Award:
0 XP
0 AC

The player obtains their first Royal Gramma.

Award:
+50 XP
+50 AC

### Species identity rules

Use the existing authoritative biological species identity.

Designer patterns, color morphs, sex differences and life stages of the same species must not automatically count as new biological species.

Preserve any separate approved collection achievements for designer varieties.

If the player obtains a new species through:
- Aquarium Store purchase and successful ownership transfer.
- Diving and successful receiving.
- Mystery Egg hatching.
- Natural breeding where the resulting offspring represents a genuinely new species in the player's ownership history.
- Other legitimate ownership methods.

Then award the first-time discovery once.

Do not award this achievement for temporary expedition inventory, unsuccessful receiving, a specimen that was only observed, or an unhatched mystery egg whose species is still unknown.

Persist the discovered-species set.

### 3.2 First-Time Aquarium Size Achievement

Reward:

**+100 Keeper XP**
**+250 AC**

Trigger when the player first acquires an aquarium capacity category that they have never previously owned.

Examples:

First 20-gallon aquarium:
+100 XP
+250 AC

First 80-gallon aquarium:
+100 XP
+250 AC

Another 80-gallon aquarium:
No additional first-size reward.

First 15,000-gallon aquarium:
+100 XP
+250 AC

Use the actual implemented aquarium catalog.

Do not invent new tank capacities.

Use stable tank-size catalog IDs rather than unreliable rounded display volumes.

This rule applies per distinct aquarium-size category, not per individual tank.

### 3.3 Diving Location Achievements

Reward:

**+50 Keeper XP**
**+50 AC**

Award once for the first successfully completed expedition at each unique diving destination or explicitly defined subdestination.

Include existing and new destinations where implemented:

Reef Diving:
- Fiji.
- Caribbean.
- Hawaii.
- Japan.
- Coral Triangle — Indonesia.
- Coral Triangle — Philippines.
- Sri Lanka.
- Marshall Islands.
- Maldives.
- Australia.
- Florida.

Deep Sea Diving:
- Existing implemented deep-sea destinations.
- Mariana Trench.

Use actual destination IDs from the diving registry.

Do not count a failed expedition as successful completion.

Do not repeatedly award rewards for visiting the same location.

If Indonesia and the Philippines exist as distinct dive destinations, award each separately.

### 3.4 Additional Objectives

Expand the available objective variety beyond these three achievement groups.

Reuse the established categories:
- Aquarium setup and cycling.
- Livestock care.
- Tank maintenance.
- Coral care and fragging.
- Fish breeding and egg hatching.
- Ocean Diving.
- Deep Sea research.
- Equipment installation and servicing.
- Tank ownership progression.
- Species collection.
- Aquarium health and survival.

Provide meaningful, achievable objectives with progress indicators.

Do not invent new AC rewards for unspecified objectives without checking existing economy balance and documenting proposed amounts.

Do not require harmful livestock treatment to complete objectives.

### 3.5 Reward Ledger and Save Safety

For each one-time achievement, use a stable reward ID.

Track:
- Profile ID.
- Achievement ID.
- Species, tank-size or location ID.
- Unlock timestamp.
- Claimed or awarded status.
- XP awarded.
- AC awarded.
- Financial transaction ID where appropriate.

Grant the reward exactly once.

Prevent repeated rewards through:
- Save/load.
- Multiple acquisition routes.
- Rebuying the same species.
- Selling and repurchasing livestock.
- Rebuying a previously owned tank size.
- Repeating a diving destination.
- Rapid repeated clicks.

For existing saves, backfill known first-time discovery records from authoritative ownership and history data where reliable, without fabricating historic transactions or repeatedly crediting old rewards.

---

## 4. EQUIPMENT MAINTENANCE AND PART REPLACEMENT

When inspecting equipment that requires service, provide two distinct options:

**Maintenance**

**Replace Part**

Do not treat these as the same action.

### 4.1 Maintenance

Maintenance represents normal cleaning and servicing.

Examples:
- Cleaning pump impellers.
- Cleaning filter components.
- Removing debris.
- Cleaning protein skimmer collection cups.
- Inspecting moving parts.
- Calibrating suitable equipment.

Maintenance can:
- Restore operating efficiency.
- Reduce contamination.
- Reduce avoidable malfunction risk.
- Improve maintenance condition.

Maintenance must not magically make worn equipment brand new.

Preserve the recently approved long-term durability rules.

### 4.2 Replace Part

Allow players to replace a damaged or worn component when the equipment supports repairable parts.

Examples:
- Pump impeller.
- Filter motor.
- Heater controller or replaceable component where appropriate.
- Skimmer pump component.
- Chiller serviceable component.
- Automatic feeder drive component.

Use equipment-specific supported repair parts.

Do not invent replaceable components for equipment that is realistically sealed or nonserviceable.

### 4.3 Replacement Cost

The player pays the same AC price as buying the corresponding new replacement part from the existing item catalog.

Example:

Replacement Pump Impeller Store Price: 150 AC

Replace Part Cost: 150 AC

Do not use the price of an entirely new pump when replacing only its impeller.

Do not arbitrarily apply a discount or markup to the replacement part.

If a component has no defined part price, audit the existing product catalog and introduce an appropriate documented part entry instead of silently guessing.

### 4.4 Replacement Behavior

When a part is replaced:
- Verify required AC or owned replacement-part inventory.
- Apply the replacement once.
- Record the AC transaction when purchased.
- Restore the relevant component condition.
- Recalculate equipment reliability and efficiency.
- Preserve the main equipment's unique identity.
- Preserve its actual service age.
- Preserve unrelated worn components.
- Record the maintenance event in Tank History.

Do not reset the entire piece of equipment to new condition unless all relevant components have genuinely been renewed.

Preserve each tank's independent equipment operation.

### 4.5 Durability Protection

Do not reintroduce rapid durability depletion.

The existing equipment-longevity update must remain intact.

Maintenance and part replacement should support multi-year in-game service life.

---

## 5. SELL AN ENTIRE AQUARIUM

Add an option in:

Aquarium Store → Sell

Named:

**Sell Entire Aquarium**

This option allows players to sell an aquarium along with all physical contents and installed equipment.

### 5.1 Aquarium Selection

Show a list of owned aquariums.

For each aquarium display:
- Aquarium name.
- Tank size.
- Number of fish.
- Number of corals.
- Number of bottom dwellers.
- Installed equipment count.
- Rocks and decorations.
- Estimated total sale value.

Allow the player to select which aquarium to sell.

### 5.2 Whole-Aquarium Sale

A successful whole-aquarium sale transfers ownership of:

- Aquarium shell.
- Installed equipment.
- Resident livestock.
- Corals.
- Bottom dwellers.
- Placed rocks.
- Decorations.
- Other physically attached or assigned sale-eligible assets.

Items in the player's uninstalled Inventory must NOT be sold.

Equipment installed in other aquariums must NOT be sold.

Livestock in other aquariums must NOT be sold.

### 5.3 Valuation

Calculate a detailed itemized offer using the existing authoritative valuation system.

Show:
- Tank shell buyback value.
- Installed equipment resale values.
- Fish resale values.
- Coral resale values.
- Bottom-dweller resale values.
- Rocks and decoration resale values.
- Applicable condition adjustments.
- Any existing legal or biological sale restrictions.
- Total AC payout.

Preserve the established livestock resale rule:

Ordinary Aquarium Store livestock resale equals 60% of the Deep Market reference buying quote when eligible.

Do not confuse current tank asset value with guaranteed dealer resale value.

Use applicable resale/buyback rules for equipment, rocks and tank shells.

Do not sell an ineligible living specimen as though it were eligible.

If the entire transaction cannot proceed due to a sale restriction, display the blocker before confirmation. Do not silently discard the restricted item.

### 5.4 Confirmation

This is a destructive transaction.

Before confirming, display:

"You are about to sell this aquarium and all eligible contents. This action cannot be undone."

Show the exact total payout and itemized contents.

Require an explicit confirmation separate from selecting the aquarium.

### 5.5 Transaction Integrity

The transaction must be atomic:

Either:
- The entire valid sale succeeds, the aquarium and included items are removed from ownership, and the full AC payout is granted once.

Or:
- The sale fails with no partial inventory deletion and no AC payout.

Do not permit partial sale corruption.

Remove:
- The sold tank's ownership entry.
- Installed equipment ownership assigned to it.
- Sold livestock and placed objects.

Preserve historical records in Tank History and the financial ledger.

Do not erase historical discoveries or achievements.

If the sold aquarium was the currently selected tank, safely select another owned tank or show the existing no-aquarium state.

Do not require the player to keep one aquarium unless an existing approved rule explicitly requires it.

Prevent save/reload duplication and double-sale exploits.

---

## 6. THE DOCK CASINO — GOLD FISH PAYOUT CORRECTION

Correct the Gold Fish game.

### Pair payout

A winning pair must pay:

**2× the original wager.**

Example:

Original wager: 100 AC

Pair payout: 200 AC total

This includes the original stake.

Therefore:
- Wager deducted: 100 AC.
- Winning payout credited: 200 AC.
- Net profit: +100 AC.

Do not credit 200 AC profit plus return another 100 AC stake.

### Additional examples

Wager: 50 AC
Pair payout: 100 AC total
Net profit: +50 AC

Wager: 250 AC
Pair payout: 500 AC total
Net profit: +250 AC

Wager: 1,000 AC
Pair payout: 2,000 AC total
Net profit: +1,000 AC

### Required checks

Audit:
- Pair identification.
- Symbol matching.
- Wager deduction.
- Prize calculation.
- Total payout.
- Net profit display.
- Casino ledger.
- Win/loss history.
- Duplicate settlement protection.

Preserve existing approved payouts for other winning combinations unless those rules are demonstrably broken.

Show the pair payout as:

"PAIR — 2×"

Do not mislabel gross payout as net profit.

Casino activity uses fictional in-game AC only.

No real-money payments or cash prizes.

---

## 7. THE DOCK CASINO — NEW PROFILE TAB

Create a tab inside The Dock Casino named:

**Profile**

Place it near the top of the Casino interface alongside the existing casino navigation.

Move these existing controls into Profile:

1. Optional Spending Limit.
2. Recent Casino Visits.

Remove their previous placements after migration.

Do not create duplicate versions.

### Profile tab

Show:

**Optional Spending Limit**
- Existing spending-limit value.
- Existing editing controls.
- Remaining allowance where supported.
- Existing limit enforcement.

**Recent Casino Visits**
- Visit dates or game timestamps.
- Recent sessions.
- Existing visit history information.
- Relevant wagering summaries where already supported.

Preserve player-profile isolation.

Do not reset existing limits or visit history.

### Spending-limit enforcement

Moving the controls must not weaken their enforcement.

Apply the spending limit to actual valid wagering transactions as the existing rules require.

The UI must not become a bypass for the limit.

---

## 8. AQUARIUM STORE — BREEDING PAIR PURCHASE CHANCE

Introduce a rare opportunity to purchase a breeding pair instead of a single fish.

### 8.1 Availability Chance

When a player opens a fish's purchase details, there should be a:

**5% chance**

that the current valid store offer includes the option:

"Buy Breeding Pair"

This must be a real, persistent offer generated through the existing store listing or offer state.

Do not generate a fresh 5% roll on every click.

Do not allow players to repeatedly close and reopen details to reroll the offer.

Store the result until the relevant listing or store refresh legitimately changes.

### 8.2 Biological Eligibility

The user wants the breeding-pair offer to be possible for any fish offered in the store.

Implement it for every species that has a biologically supported captive breeding-pair configuration.

Do not fabricate a conventional male-female pair for species with incompatible reproductive systems or unknown captive breeding requirements.

For species that breed through sex changes, use the appropriate biologically compatible pairing and reproductive roles.

For species whose reproductive behavior is not pair-based, either use a separately accurate reproductive-unit offer when authorized or omit the pair option with an accurate explanation.

Do not pretend every fish species forms permanent bonded pairs.

### 8.3 Purchase Contents

A successful breeding-pair purchase provides two distinct individual fish.

Each must have:
- Unique livestock ID.
- Correct species.
- Appropriate sex or reproductive role.
- Individual age and maturity.
- Individual health.
- Individual genetics.
- Individual value.
- Appropriate pairing compatibility.

Do not create two identical references to the same livestock entity.

### 8.4 Pairing Status

The purchase offer must clearly distinguish:

"Compatible Breeding Pair"

from:

"Established Bonded Pair"

If the store explicitly sells an established breeding pair, that status must be backed by a legitimate simulated pairing record and compatible mature individuals.

Do not guarantee immediate spawning.

Breeding must still depend on:
- Health.
- Aquarium conditions.
- Stress.
- Nutrition.
- Suitable spawning habitat.
- Reproductive maturity.
- Species-specific reproductive behavior.

Preserve autonomous breeding.

### 8.5 Price

Price the breeding pair using two legitimate specimen valuations and any existing approved pair-pricing rules.

Show the exact total purchase price before confirmation.

Do not invent an unapproved universal breeding-pair discount.

Deduct AC once.

### 8.6 Receiving

Both specimens must pass the existing aquarium receiving and compatibility system.

Check:
- Available aquarium volume.
- Combined bioload.
- Species compatibility.
- Quarantine requirements.
- Water parameters.
- Suitable habitat.

Do not bypass compatibility because the items are sold as a pair.

If the game cannot safely receive both fish, explain why and block or use an existing authorized receiving workflow.

### 8.7 Save Protection

Persist:
- Offer availability.
- Offer ID.
- Listing refresh ID.
- Two specimen identities.
- Pair relationship where applicable.
- Purchase transaction.
- Receiving status.

Prevent purchase duplication and click-reroll exploits.

---

## 9. INTEGRATION AND SAVE COMPATIBILITY

Audit how these systems interact:

- Aquarium purchases.
- Account progression.
- First-time discovery history.
- XP rewards.
- AC transactions.
- Equipment repairs.
- Equipment inventory.
- Whole-tank selling.
- Casino wagering.
- Breeding-pair purchasing.
- Aquarium receiving.
- Save/load.

Preserve all currently owned items, aquariums and livestock.

Do not overwrite existing profiles.

Do not reset achievements.

Do not remove established livestock genetics or breeding history.

Use stable IDs and transactional updates for purchases, rewards and sales.

---

## 10. REQUIRED TESTS

### Tank Pricing

1. The 15,000-gallon aquarium costs exactly 25,000 AC.
2. Existing owners are not charged retroactively.
3. Other aquarium prices remain unchanged.

### Achievements

4. First new livestock species grants 50 XP and 50 AC.
5. Repeated ownership of the same species grants no duplicate reward.
6. A new aquarium-size category grants 100 XP and 250 AC.
7. Buying another tank of the same size grants no duplicate reward.
8. Completing a new dive destination grants 50 XP and 50 AC.
9. Repeating that destination grants no duplicate reward.
10. Rewards survive saving and reloading.

### Equipment

11. Maintenance and Replace Part are separate actions.
12. Replacement cost equals the new part's listed price.
13. Part replacement preserves equipment identity.
14. Maintenance does not reset permanent wear.
15. Existing durability balance remains intact.

### Whole-Tank Sale

16. Whole-tank selling includes the selected tank and eligible physical contents.
17. It excludes stored Inventory.
18. It excludes other aquariums.
19. The offer is itemized and confirmed.
20. AC is awarded exactly once.
21. Sold items cannot be reclaimed through save/load.
22. Failed sales do not partially delete assets.

### Casino

23. A 100 AC pair wager pays 200 AC total.
24. Net profit is correctly displayed as 100 AC.
25. Existing non-pair payout rules remain intact.
26. Profile contains Optional Spending Limit.
27. Profile contains Recent Casino Visits.
28. Spending-limit enforcement remains functional.
29. Casino transactions cannot settle twice.

### Breeding Pair Store

30. Exactly 5% offer eligibility is configured for suitable listings.
31. Opening a listing repeatedly does not reroll the offer.
32. Species reproductive compatibility is respected.
33. Two unique fish IDs are created.
34. Purchase cost is applied exactly once.
35. Both fish must pass receiving requirements.
36. Breeding remains autonomous.
37. Pair offers persist correctly across valid save/load boundaries.

### General

38. Existing aquariums remain intact.
39. Existing livestock remains intact.
40. The game stays fully offline.
41. Freshwater remains locked.
42. No unauthorized economy rules are changed.

Report actual tests executed.

Do not invent successful test results.

---

## 11. DOCUMENTATION

Merge these changes into the relevant home sections of the existing consolidated 31-section Aquarium Life Master Development Prompt.

Update:
- GAME_DESIGN.md.
- UI_SPECIFICATION.md.
- DEVELOPMENT_STATUS.md.
- BALANCE_REPORT.md.
- Aquarium pricing definitions.
- Achievement and objective registry.
- Equipment repair documentation.
- Whole-aquarium sale documentation.
- Casino payout definitions.
- Breeding-pair offer rules.
- Save-schema documentation.
- Project continuity notes and PDF source where supported.

### Permanent rules

**15,000-Gallon Aquarium:** Purchase price is 25,000 AC. Existing purchases are not retroactively charged.

**First-Time Species Achievement:** A newly owned biological livestock species grants 50 XP and 50 AC once per player profile.

**First-Time Aquarium Size Achievement:** First ownership of a new aquarium-size category grants 100 XP and 250 AC once per profile.

**Dive Destination Achievement:** First successful expedition at each unique diving destination grants 50 XP and 50 AC.

**Equipment Service:** Maintenance and Replace Part are distinct operations. Replacement parts cost their normal new-part catalog price.

**Whole-Aquarium Sale:** Players may sell an entire aquarium and all sale-eligible physical contents through the Aquarium Store, using a single confirmed transaction.

**Gold Fish Pair Payout:** A pair pays exactly twice the original wager, including the returned stake.

**Casino Profile:** Optional Spending Limit and Recent Casino Visits are located in The Dock Casino → Profile.

**Breeding Pair Store Opportunity:** Each eligible fish listing has a 5% chance to offer a biologically compatible breeding pair, fixed for the listing's legitimate refresh period.

Preserve one authoritative home for each rule.

Do not duplicate mechanics across unrelated MDP sections.

---

## 12. COMPLETION REPORT

When authorized edits have genuinely been completed, provide:

1. Files modified.
2. Aquarium price correction.
3. Achievements and objectives created.
4. Equipment service improvements.
5. Whole-aquarium selling implementation.
6. Gold Fish payout correction.
7. Casino Profile changes.
8. Breeding-pair purchase implementation.
9. Save migrations.
10. Tests passed.
11. Tests failed or not executed.
12. Remaining limitations and approval requirements.

Only when all authorized work is genuinely complete, end with the exact standalone line:

Done With Edits

Do not claim completion if an authorized requirement remains unfinished.

# FINAL DIRECTIVE

Implement all seven updates as one coordinated Aquarium Life development pass.

Maintain accurate economy calculations, realistic aquarium equipment, autonomous breeding, safe livestock transfers and persistent achievement records.

Preserve the established design, existing player saves and offline architecture.

Freshwater remains locked.
