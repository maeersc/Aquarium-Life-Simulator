# AQUARIUM LIFE — DAILY LIVESTOCK SURVIVAL REWARD
## Codex GPT-6 Astra — Economy Update v3.4

### 1. Main Objective

Implement a daily livestock survival reward in Aquarium Life.

For every completed in-game day in which no player-owned livestock dies, award the player:

**+100 Aquarium Credits (AC)**

This replaces the previously specified +200 AC livestock no-death reward.

Do not award both amounts.

Preserve the existing +50 AC healthy aquarium reward as a separate system.

### 2. Reward Requirements

A player qualifies for the 100 AC survival bonus when:

- One full in-game day has passed.
- The player owns at least one living livestock organism throughout the qualifying period.
- No livestock has died in any of the player's active aquariums during that day.
- The day has been processed successfully by the existing simulation.
- The reward has not already been claimed or awarded.

Eligible livestock includes:
- Saltwater fish.
- Corals.
- Bottom-dwelling invertebrates.

Only confirmed livestock deaths count as deaths. A sick fish or living bleached coral does not automatically count as dead.

Award the bonus once per player account, not once per aquarium.

### 3. In-Game Time

Preserve the current time conversion:

**20 real-world minutes = 1 full in-game day.**

Therefore, a player can earn 100 AC every 20 real-world minutes if all survival conditions are satisfied.

Rewards must also be processed during legitimate offline simulation.

The player does not need to keep the browser open.

Do not pause the reward timer when the player opens:
- Aquarium Store.
- Deep Market.
- Field Journal.
- Equipment.
- Ocean Diving.
- The Dock Casino.
- Other game windows.

### 4. Livestock Death Penalty

If any livestock dies:

1. Record the death event and its authoritative simulation time.
2. Cancel the current qualifying survival bonus.
3. Begin a recovery period lasting one full in-game day.
4. The player must complete that recovery period without another livestock death.
5. A new death during recovery restarts the recovery timer.
6. Once recovery completes, normal daily reward qualification can resume.

Do not award the 100 AC bonus during the recovery period.

Do not allow the player to bypass the penalty by changing aquariums, transferring livestock, logging out, or reloading a save.

### 5. Reward Notifications

When the player receives the bonus, show a small notification:

**Livestock Survival Bonus: +100 AC**

When livestock dies, display:

**Livestock lost! Daily survival bonus interrupted. Complete one full in-game day without a death to restore eligibility.**

Display the recovery countdown where appropriate.

Avoid excessive pop-up notifications during long offline catch-up periods. Use a consolidated summary for multiple earned or missed rewards.

### 6. AC Financial Dashboard Integration

Connect the reward to the existing AC transaction ledger.

Record:
- Transaction type: Livestock Survival Bonus.
- Amount: +100 AC.
- In-game day.
- Real timestamp.
- Player account ID.
- Qualification status.
- Unique transaction ID.

The reward must appear when the player clicks their Aquarium Credits balance.

Example:

Day 25 — Livestock Survival Bonus — +100 AC.

Prevent duplicate rewards from:
- Save/load.
- Offline catch-up.
- Repeated simulation updates.
- Multiple aquariums.
- Importing older saves.
- Changing system time.

### 7. Preserve Healthy Aquarium Bonus

The existing healthy aquarium reward remains:

**+50 AC per qualifying in-game day.**

The livestock survival bonus is separate:

**+100 AC per qualifying in-game day.**

If both conditions are met, the player receives:

**150 AC total.**

If only the healthy aquarium conditions are met, award only the eligible 50 AC.

If only the livestock survival conditions are met, award only the eligible 100 AC.

Never automatically award both when only one condition is satisfied.

### 8. Save Data

Persist:
- Last processed in-game day.
- Survival bonus eligibility.
- Last livestock death timestamp.
- Recovery-period state.
- Reward history.
- Last awarded qualifying day.
- Transaction IDs.

Use the existing local-account save architecture.

Do not create a separate competing wallet system.

### 9. Required Tests

Verify:

1. A complete death-free in-game day awards 100 AC.
2. A partial day awards nothing.
3. Accounts without eligible livestock receive no survival reward.
4. Multiple aquariums do not multiply the reward.
5. Fish deaths interrupt qualification.
6. Coral deaths interrupt qualification.
7. Bottom-dweller deaths interrupt qualification.
8. Living but sick livestock does not count as dead.
9. Death recovery lasts one full in-game day.
10. Additional deaths restart recovery.
11. Rewards resume after recovery and a qualifying day.
12. Offline progression can award legitimately earned rewards.
13. Save/load cannot duplicate rewards.
14. The AC Financial Dashboard records payments accurately.
15. The existing 50 AC healthy aquarium reward still works.
16. The old 200 AC survival bonus is no longer awarded.
17. All credit changes use the centralized transaction ledger.
18. Existing livestock and account saves remain intact.
19. Game remains functional offline.
20. Freshwater remains locked.

Report tests as passed, failed, or untested.

### 10. Documentation

Update the consolidated Master Development Prompt and relevant project files:

- GAME_DESIGN.md.
- DEVELOPMENT_STATUS.md.
- BALANCE_REPORT.md.
- AC financial transaction documentation.
- Project locked-rules and continuity documentation.

Replace the old +200 AC no-death bonus rule with:

**Players earn 100 AC for every completed qualifying in-game day without a livestock death. After a livestock death, one full death-free in-game day must pass before reward eligibility can resume.**

Do not leave conflicting 100 AC and 200 AC survival reward rules in the project.

### 11. Completion Requirement

When all authorized edits are complete, Codex must report:
- Files changed.
- Reward system implemented.
- Death recovery behavior.
- Save/load behavior.
- AC ledger integration.
- Tests performed.
- Remaining limitations.

The final standalone line must be:

Done With Edits

Do not claim successful completion if implementation is incomplete.

## FINAL DIRECTIVE

Implement the +100 AC livestock survival reward.

Replace the old +200 AC survival bonus.

Preserve the +50 AC healthy aquarium reward.

Ensure deaths interrupt eligibility, enforce the full in-game-day recovery period, and prevent duplicate payments.

Keep freshwater development locked and preserve all existing Aquarium Life functionality.
