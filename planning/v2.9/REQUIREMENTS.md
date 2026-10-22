# AQUARIUM LIFE — FUTURE DEVELOPMENT UPDATE v2.9
## Tutorial, Livestock Welfare, Deep Market, Tank Expansion & Collection Systems
### Codex GPT-6 Astra — PLANNED / NOT YET AUTHORIZED FOR IMPLEMENTATION

# 1. DEVELOPMENT STATUS AND SCOPE

This document defines a future development milestone for Aquarium Life.

Preserve all existing approved rules and the current project codebase.

**Do not implement this update until the player approves the next livestock roster and explicitly authorizes implementation.**

Current development remains SALTWATER ONLY.

Do not introduce or unlock freshwater livestock features.

This update covers:
- Saltwater beginner tutorial.
- Livestock selection highlight correction.
- Medical inspection guidance.
- Freshwater lockout.
- Daily no-death reward.
- Deep Market renaming.
- Preview-only leaderboards.
- New 15,000-gallon aquarium.
- Water-change cost balancing.
- Next 25/5/5 livestock expansion.
- Mystery Coral and bottom-dweller Mystery Egg.

Follow the existing consolidated 31-section Master Development Prompt.

Do not delete or replace earlier functionality.

---

# 2. BEGINNER SALTWATER TUTORIAL

Create a simple, interactive step-by-step tutorial for first-time Aquarium Life players.

The tutorial should appear after the player chooses Start New Game.

It must teach players how to establish their first aquarium safely and progress toward their first achievement.

## Required tutorial steps

### Step 1 — Welcome to Aquarium Life

Explain:
- What the game is about.
- How to earn Aquarium Credits.
- How to navigate the six main menu tabs.
- How to use the active aquarium.

Provide a Next button.

### Step 2 — Obtain Your First Aquarium

Guide the player to Aquariums.

Explain:
- Tank sizes in US gallons.
- Aquarium purchase price.
- Tank base value.
- Dynamic total tank asset value.

Do not automatically populate the tank.

### Step 3 — Add Substrate

Guide the player to select suitable saltwater sand.

Explain:
- Fiji.
- Caribbean.
- Hawaiian.
- Sand depth.
- How depth affects the aquarium.

### Step 4 — Prepare Saltwater

Explain:
- Appropriate saltwater preparation.
- Salinity.
- Temperature.
- Water volume.

Do not allow an unprepared tank to bypass established setup safeguards.

### Step 5 — Install Equipment

Guide the player through:

Equipment → Tank Care

Demonstrate:
- Filter.
- Heater where necessary.
- Circulation pump.
- Appropriate lighting.

### Step 6 — Add Rockwork

Demonstrate:
- Purchasing rock.
- Placing rock.
- Moving rock forward/backward with the mouse wheel.
- Creating shelter.
- Why the rock must rest on a valid support.

### Step 7 — Establish the Nitrogen Cycle

Explain:
- Ammonia.
- Nitrite.
- Nitrate.
- Biological filtration.

Guide the player to the aquarium's water-condition interface.

Do not instantly declare a tank cycled without satisfying its underlying simulation requirements.

### Step 8 — Purchase Your First Fish

Open Aquarium Store → Saltwater → Fish.

Explain:
- Common rarity.
- Care difficulty.
- Retail prices.
- Compatibility.
- Destination aquarium.

Choose an eligible beginner fish.

Do not override the existing eight-slot daily fish rotation.

### Step 9 — Feed and Inspect Livestock

Teach:
- How to feed.
- How to click a fish.
- How to see health, hunger, life stage and rarity.
- How to see its current AC value.

### Step 10 — Medical Inspection

Explain how to identify unhealthy fish.

Demonstrate:
- Opening the fish inspector.
- Checking symptoms.
- Accessing Field Journal → Disease & Treatment Guide.
- Using available diagnostic tools.
- Understanding quarantine.
- Finding legitimate medicine in Aquarium Store → Saltwater → Medicine & Treatment.

Do not give the player a dangerous treatment without proper warnings.

Do not require a fish to become genuinely sick just to complete the tutorial.

Use a safe demonstration or example screen.

### Step 11 — Maintain a Healthy Aquarium

Teach:
- Water testing.
- Feeding.
- Water changes.
- Equipment maintenance.
- Livestock survival bonuses.

### Step 12 — Collect Your First Achievement

Guide the player to:

Field Journal → Achievements.

Show:
- Achievement requirements.
- Progress.
- Claiming or receiving rewards.
- Next available objectives.

The first achievement must be achievable using implemented gameplay.

## Tutorial requirements

- Next.
- Back.
- Skip Tutorial.
- Resume Tutorial.
- Highlight the relevant UI control.
- Explain the current objective.
- Preserve progress after saving/loading.

Do not block normal gameplay permanently if the player skips.

Allow players to restart the tutorial through Settings.

---

# 3. LIVESTOCK SELECTION HIGHLIGHT — THREE SECONDS

When a player clicks livestock in the aquarium, its selection rectangle or outline should appear briefly.

**The visual selection box must disappear automatically after 3 seconds.**

Requirements:
- Highlight appears on click.
- Three-second countdown begins.
- Highlight disappears after three seconds.
- Clicking another creature transfers the highlight.
- Reclicking the same creature restarts the timer.
- Changing tanks clears the old highlight.
- No stale outline remains.
- The livestock inspector must remain open until the player closes it or changes selection.

Only the temporary selection outline expires.

Do not automatically close the livestock information window after three seconds.

Do not use permanent selection outlines that obscure fish artwork.

---

# 4. FRESHWATER CONTENT — LOCKED

Freshwater development is not yet authorized.

When the game starts:

- Freshwater options must appear greyed out.
- Freshwater controls must be disabled.
- Freshwater purchasing must be unavailable.
- Freshwater tank creation must be locked.
- Freshwater-specific interactions must not open active gameplay.

Display:

"Freshwater — Coming in a Future Update."

Existing freshwater data, saves, species, and artwork must be preserved.

Do not delete freshwater code.

## Permanent authorization rule

**Before every future Aquarium Life implementation prompt, explicitly ask the player whether freshwater development is next.**

Until the player explicitly authorizes freshwater work, continue saltwater-only development.

The player must not accidentally unlock freshwater by clicking a disabled element.

Shared UI improvements may be implemented without expanding freshwater biology.

---

# 5. DAILY LIVESTOCK SURVIVAL BONUS

Keep the existing daily aquarium health reward:

**+50 AC per qualifying healthy in-game day.**

Add a separate bonus:

**+200 AC per qualifying livestock-death-free in-game day.**

The total possible daily reward is:

**250 AC.**

These two rewards are separate.

## 5.1 Survival bonus eligibility

Evaluate the player's eligible active, stocked aquariums.

A qualifying day requires:
- No livestock deaths in any eligible player-owned aquarium during the qualification period.
- Valid simulation progression.
- At least one eligible living livestock organism.
- No attempt to multiply the reward by tank count.

Fish, corals, and bottom-dwelling livestock all count.

A death includes a confirmed death event, not merely temporary illness or bleaching in a living coral.

## 5.2 Death penalty and recovery

If any owned livestock dies:

1. Cancel the current day's survival bonus.
2. Record the death's authoritative simulation timestamp.
3. Begin a full one-in-game-day death-free recovery interval.
4. Do not award another survival bonus before the interval completes.
5. Restart the recovery interval if another livestock death occurs.

A fresh bonus becomes eligible only after the full recovery interval and the applicable qualifying day conditions have been satisfied.

Use the existing game calendar and persistent state.

Do not allow reopening the game or changing the system clock to bypass the recovery period.

## 5.3 Time and offline rules

One in-game day remains:

20 minutes of real elapsed time.

The aquarium simulation continues while the player is away.

Process genuine death-free eligibility during offline catch-up.

Do not generate rewards for unqualified periods.

Preserve all prior anti-duplication safeguards.

## 5.4 User notifications

Examples:

"Daily Healthy Tank Reward: +50 AC"

"Livestock Survival Bonus: +200 AC"

"Livestock loss detected. Survival bonus requires one full death-free in-game day before eligibility can resume."

Explain the qualification status in Field Journal → Tank History.

---

# 6. RENAME BLACK MARKET TO DEEP MARKET

Change all player-facing references of:

Black Market

to:

**Deep Market**

This includes:
- Aquarium Store main tab.
- Shop headings.
- Notifications.
- Reputation menus.
- Selling screens.
- Buying screens.
- Tooltips.
- Journal references.
- Help content.

Preserve its existing functions:

- Variable livestock prices.
- Hidden specimen health risks.
- Restricted fictional medicines.
- Reputation.
- Diving-acquired livestock sales.
- Purchase restrictions.
- Rare-item availability.

Do not reset reputation or previously purchased livestock.

For compatibility, preserve existing internal IDs and save data where needed.

The Deep Market must remain inside the Aquarium Store modal.

---

# 7. LEADERBOARDS — PREVIEW ONLY

Create a new Leaderboards interface accessible without adding a seventh permanent main-sidebar tab.

Place it under an appropriate existing interface, such as:

Field Journal → Leaderboards.

The leaderboard must contain two options:

1. Saltwater Leaderboard.
2. Freshwater Leaderboard.

Freshwater leaderboard is preview-only and may display a locked future-content state.

## 7.1 Ranking metric

Rank aquariums according to:

**Current Total Aquarium Asset Value in AC.**

This includes:
- Tank shell's eligible current value.
- Equipment.
- Fish.
- Coral.
- Bottom dwellers.
- Rocks/substrate.
- Eligible decorations.

Do not rank players by wallet balance or spendable AC.

Do not double-count inventory or mounted assets.

## 7.2 Preview behavior

The leaderboard is not online yet.

Do not implement:
- Servers.
- User accounts.
- Networking.
- Public competitive ranking submissions.
- Fake real-player rankings.

Display a polished preview illustrating the planned leaderboard.

Any sample ranks or scores must be clearly marked as demonstrations.

Use existing local owned aquariums for an optional local comparison only if accurately identified.

The long-term leaderboard will require verified, server-authoritative asset valuation.

---

# 8. NEW 15,000-GALLON AQUARIUM

Add a new tank capacity:

**15,000 US gallons**

Approved base purchase price:

**5,000 AC**

The tank type must support future use as:
- Saltwater.
- Freshwater.

However, freshwater purchase and setup must remain locked until authorized.

## 8.1 Tank properties

Define:
- Actual internal water capacity.
- Physical dimensions.
- Substrate area.
- Equipment requirements.
- Water-change volume.
- Lighting demands.
- Filtration demands.
- Livestock habitat requirements.
- Tank base value.
- Running and maintenance costs.

Preserve existing capacity and gallon-display rules.

## 8.2 Purchase cost

Buying the tank costs exactly 5,000 AC.

Do not confuse the tank purchase price with a water-change cost.

## 8.3 Maintenance cost scaling

Audit the existing water-change pricing system.

Find the smallest existing aquarium and its baseline water-change cost.

Use that baseline to calculate proportional costs for larger tanks.

For a 10% water change:

Water Removed = Actual Tank Water Volume × 0.10

Calculate replacement water, salt mix, treatment, and other eligible consumable costs from actual changed volume.

Do not arbitrarily charge the same maintenance cost to a 20-gallon and a 15,000-gallon aquarium.

Preserve the existing cost model when it already correctly accounts for equipment, volume and consumables.

## 8.4 Rounding

Tank labels must round up to the nearest whole US gallon.

Do not round underlying volumes used by chemistry or cost calculations.

## 8.5 Economy balancing

A 15,000-gallon aquarium is an enormous system.

Its maintenance costs should reflect the amount of water, required equipment, and consumables involved.

Test affordability relative to:
- The 5,000 AC purchase price.
- Daily income.
- Livestock value.
- Equipment expenses.
- Water-change frequency.

Document balance problems instead of secretly changing the approved purchase price.

---

# 9. NEXT SALTWATER LIVESTOCK EXPANSION

The next normal livestock expansion contains:

- 25 new saltwater fish species.
- 5 new coral species.
- 5 new bottom-dwelling species.

Total:

**35 new species-level entries.**

Do not reuse entries from the previously approved 38-livestock batch.

## 9.1 Required premium rarity additions

Each of the three livestock categories must include:

- At least one new Tier 5 — Ultra Rare.
- At least one new Tier 6 — Legendary.

This means at least:

- Fish: one Ultra Rare and one Legendary.
- Corals: one Ultra Rare and one Legendary.
- Bottom dwellers: one Ultra Rare and one Legendary.

These rarities are game collection classifications, not statements about conservation status.

Do not artificially label an ordinary species Legendary without presenting a reasonable game-design explanation.

## 9.2 Mandatory approval gate

Before implementing the new species:

1. Inspect CURRENT_LIVESTOCK_CATALOG.md.
2. Inspect the permanent livestock registry.
3. Inspect the previous 38-entry expansion and its actual implementation status.
4. Check scientific identities and synonyms.
5. Propose exactly 25 eligible new fish.
6. Propose exactly five eligible new corals.
7. Propose exactly five eligible new bottom dwellers.
8. Give each a proposed rarity.
9. Give each a proposed care difficulty.
10. Present the complete list to the user.
11. Wait for explicit approval.

**Do not implement the 35-species roster before approval.**

## 9.3 Existing content remains protected

Do not duplicate:
- Existing 31 clownfish catalog records.
- Existing designer varieties.
- Earlier implemented fish.
- Earlier coral records.
- Existing bottom-dwelling species.
- Previously approved 38 expansion species where implemented.

Do not count designer morphs as additional biological species.

---

# 10. NEW MYSTERY CORAL

Add a mystery product to:

Aquarium Store → Saltwater → Corals.

Name:

**Mystery Coral**

The product must use the existing six-tier rarity system.

Exact independent odds per purchase:

- Common — 50%.
- Uncommon — 25%.
- Rare — 15%.
- Very Rare — 7.5%.
- Ultra Rare — 2%.
- Legendary — 0.5%.

Each purchase has an independent outcome.

Do not increase or decrease individual probability because another mystery product was purchased.

## 10.1 Biological rules

The Mystery Coral should produce an eligible coral frag, juvenile colony, or appropriate early coral form.

Do not pretend every coral reproduces through fish-style eggs.

Use species-appropriate visual art.

Once resolved, each individual coral receives:
- Species.
- Rarity.
- Unique identity.
- Health.
- Stage.
- Current value.
- Correct mounting requirements.

## 10.2 Rarity pool eligibility

Only include implemented, correctly classified coral species.

Do not silently substitute lower-tier corals when a higher-tier pool is empty.

If an eligible rarity pool is unavailable, visibly hold purchasing until the catalog satisfies the advertised odds.

---

# 11. NEW BOTTOM-DWELLER MYSTERY EGG

Add a mystery product to:

Aquarium Store → Saltwater → Bottom Feeders.

Display name:

**Mystery Bottom-Dweller Egg**

Use exactly the same independent rarity probabilities:

- Common — 50%.
- Uncommon — 25%.
- Rare — 15%.
- Very Rare — 7.5%.
- Ultra Rare — 2%.
- Legendary — 0.5%.

## 11.1 Species-appropriate life stages

Bottom-dwelling invertebrates do not all develop in identical ways.

Use appropriate:
- Eggs.
- Egg masses.
- Brooded embryos.
- Larval stages.
- Juvenile stages.

Where the Mystery Egg mechanic represents a species whose natural early stage is unsuitable as a literal transferable egg, use a clearly identified game abstraction or appropriate early-stage specimen.

Do not invent inaccurate biological details.

## 11.2 Persistent outcomes

Assign and persist the outcome properly.

Do not reroll after save/load.

Maintain:
- Unique identity.
- Eligible species pool.
- Rarity.
- Viability.
- Growth.
- Health.
- Value.
- Art stages.

Do not produce adult organisms instantly from eggs unless a distinct mechanic explicitly supports that outcome.

---

# 12. STORE RARITY AND MYSTERY RULES

Preserve the standard Saltwater Fish store:

- Three Common fish listings.
- Three Uncommon fish listings.
- One Rare fish listing.
- One Mystery Egg listing.

Total:
Eight slots.

Refresh every in-game day.

Normal direct-sale livestock must remain Tier 1–3 only.

Tier 4–6 direct livestock purchases are not available through the ordinary store.

Eligible higher-tier discoveries remain possible through authorized mystery items, the Deep Market, and diving where applicable.

The Mystery Coral and Bottom-Dweller Mystery Egg do not change the fish-store's eight-slot limit.

---

# 13. ARTWORK REQUIREMENTS

All new livestock artwork must follow the approved Aquarium Life hybrid pixel-art style.

Every new species must receive biologically applicable:

- Earliest reproductive/developmental stage.
- Baby or larval stage.
- Juvenile stage.
- Adult stage.
- Living artwork.
- Dead artwork.

All swimming animals must face their correct movement direction.

Fish eyes must remain properly rendered.

Corals must attach to valid surfaces.

Use the correct colored six-tier rarity silhouettes.

No generic placeholders should be represented as approved finished art.

---

# 14. SAVE/LOAD, OFFLINE SIMULATION AND COMPATIBILITY

Preserve:
- 20-minute real-time game days.
- Continuous offline ecosystem simulation.
- Healthy-day +50 AC reward.
- New death-free +200 AC reward.
- Aquarium values.
- Livestock unique IDs.
- Health and disease states.
- Black Market to Deep Market migration.
- Reputation.
- Livestock rarity.
- Mystery outcomes.
- Aquarium Keeper progress.
- Tank selections.
- Diving progress where implemented.

Use versioned migrations.

Do not reset or erase existing player progress.

Do not modify protected freshwater livestock.

---

# 15. REQUIRED QUALITY ASSURANCE

Verify:

1. Beginner tutorial starts correctly.
2. Tutorial can be skipped and resumed.
3. Medical inspection is explained accurately.
4. Livestock highlight disappears after three seconds.
5. Livestock inspector remains usable.
6. Freshwater UI is disabled.
7. Freshwater livestock cannot be purchased.
8. Existing freshwater data remains intact.
9. Healthy aquarium reward remains 50 AC.
10. Death-free survival bonus can award 200 AC.
11. Bonuses are separate.
12. A livestock death cancels the appropriate survival bonus.
13. Full recovery interval is enforced.
14. Save/load cannot duplicate rewards.
15. Black Market is renamed Deep Market throughout player-facing UI.
16. Reputation and inventory remain intact.
17. Leaderboards are preview-only.
18. Saltwater and Freshwater leaderboard views exist.
19. Ranking metric uses current tank asset value.
20. Wallet balance is not treated as tank value.
21. The 15,000-gallon tank is registered.
22. Tank purchase price is 5,000 AC.
23. Freshwater version remains locked.
24. Water-change costs reflect changed water volume.
25. Smaller tank maintenance baselines remain coherent.
26. Next livestock batch contains no duplicates.
27. Each livestock category contains proposed Tier 5 and Tier 6 candidates.
28. New species have user approval before implementation.
29. Mystery Coral odds total 100%.
30. Bottom-Dweller Mystery Egg odds total 100%.
31. Mystery outcomes are independently rolled.
32. Outcomes persist after reload.
33. Unsupported rarity pools cannot silently substitute.
34. All artwork follows the approved style.
35. Existing game remains fully offline.

Report which tests were actually executed.

Do not label unverified items as complete.

---

# 16. DOCUMENTATION AND REGISTRY RULES

Maintain the single consolidated 31-section MDP.

Update the appropriate primary sections for:

- Tutorial.
- UI.
- Livestock.
- Economy.
- Tank valuation.
- Deep Market.
- Leaderboard preview.
- Water-change costs.
- Mystery products.
- Save persistence.

Maintain:
- CURRENT_LIVESTOCK_CATALOG.md.
- Permanent species ledger.
- GAME_DESIGN.md.
- UI_SPECIFICATION.md.
- ART_DIRECTION.md.
- DEVELOPMENT_STATUS.md.
- BALANCE_REPORT.md.

Preserve the established locked-rules section and internal continuity/handoff information near the back of the project PDF.

Every new livestock species must be logged accurately with:
- Scientific name.
- Category.
- Rarity.
- Care difficulty.
- Unique ID.
- Batch number.
- Art status.
- Implementation status.
- Approval status.

Do not record a proposed species as implemented.

---

# 17. NEW PERMANENT RULES

1. First-time players receive a guided saltwater tutorial.
2. Fish medical inspection must be explained during the tutorial.
3. Livestock selection outlines expire after three seconds.
4. Freshwater remains locked until explicitly authorized.
5. Future development prompts must ask whether freshwater is next.
6. Livestock survival earns an additional 200 AC per qualifying day.
7. Livestock death requires one complete death-free day before bonus eligibility can resume.
8. Black Market is renamed Deep Market.
9. Leaderboards remain preview-only.
10. Leaderboards rank current aquarium asset value, not wallet balance.
11. A 15,000-gallon aquarium costs 5,000 AC.
12. Water-change costs scale with actual changed water volume.
13. Future livestock batches require user-approved lists and duplicate checks.
14. The next batch needs at least one Ultra Rare and one Legendary in each livestock category.
15. Mystery Coral uses the approved six-tier independent odds.
16. Bottom-Dweller Mystery Egg uses the approved six-tier independent odds.
17. Current freshwater species and their systems remain protected.
18. All added species must be recorded in the permanent livestock registry.
19. The consolidated MDP and PDF continuity rules must remain intact.
20. Codex must notify the user when authorized edits are complete.

---

# 18. CODEX COMPLETION REQUIREMENT

For future authorized implementation work:

Report:
- Files edited.
- Features implemented.
- Species added.
- Existing species preserved.
- Tests passed.
- Tests failed.
- Outstanding limitations.
- Documentation updated.

When authorized edits have genuinely been completed, the final standalone line must read:

Done With Edits

Do not use that completion phrase if work is unfinished or blocked.

---

# 19. CURRENT EXECUTION INSTRUCTION

This document is a **future development specification**.

For now:

1. Record these new requirements.
2. Preserve earlier locked rules.
3. Prepare the next duplicate-checked livestock candidate list.
4. Wait for rarity review and user approval.
5. Do not implement new species or unrelated systems yet.

When the user later authorizes implementation, follow all approved requirements and complete testing.

Do not advance to freshwater without explicit permission.
