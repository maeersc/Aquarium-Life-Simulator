# AQUARIUM LIFE — AC FINANCIAL DASHBOARD & TRANSACTION HISTORY
## Codex GPT-6 Astra — Development Update v3.2
### Authorized Saltwater Implementation

## 1. DEVELOPMENT OBJECTIVE

Add a comprehensive Aquarium Credits financial tracking system to Aquarium Life.

When a player clicks their Aquarium Credits (AC) balance in the top-right corner of the main screen, open a financial dashboard showing:

- Current AC balance.
- Total AC earned.
- Total AC spent.
- Net AC change.
- Individual transactions.
- Where credits were earned.
- Where credits were spent.
- Transaction dates and in-game times.
- Filters for income and expenses.
- Historical financial information.

Do not change the game's existing economy values.

Preserve local accounts, existing saved wallets, offline functionality, and all approved systems.

Current development remains SALTWATER ONLY.

---

## 2. CLICKABLE AQUARIUM CREDITS DISPLAY

Use the existing AC balance area in the top-right main header.

The AC icon and credit amount must become one clickable control.

Example:

737 AC

Clicking anywhere on that control opens:

**Aquarium Credits — Financial Overview**

Requirements:

- Pointer hover indicator.
- Accessible button semantics.
- Keyboard activation using Enter or Space.
- Live wallet balance.
- No unintended aquarium interaction underneath.
- No new permanent sidebar button required.

Do not remove or relocate the existing AC display.

---

## 3. FINANCIAL DASHBOARD MODAL

Open a professional, centered modal matching the existing Aquarium Life design.

At the top, display:

**Aquarium Credits**

Include a clearly visible X in the upper-right corner.

Also allow:
- Escape to close.
- Backdrop click to close.
- Internal scrolling when transaction history exceeds the available space.

The main page must not acquire unnecessary vertical scrolling.

## 3.1 Summary

Display:

Current Balance
Total Income
Total Expenses
Net AC Change

Allow the player to view:

- Current in-game day.
- Last seven in-game days.
- Last thirty in-game days.
- All Time.

Calculate each summary from the matching timeframe.

Never label a period-specific net change as the player's current total balance.

Opening balance, income, expenses, and closing balance must reconcile.

Formula:

Closing Balance = Opening Balance + Income − Expenses

Display all values in whole Aquarium Credits.

---

## 4. INCOME CATEGORIES

Track all real sources of AC income.

Include existing systems where implemented:

### Daily healthy aquarium income

The existing:

+50 AC per qualifying healthy in-game day.

### Livestock survival bonus

The approved:

+200 AC per qualifying death-free in-game day.

Preserve the full recovery-period restriction after a livestock death.

### Livestock sales

Track income from:
- Fish sales.
- Coral sales.
- Coral fragment sales.
- Bottom-dweller sales.
- Diving-collected livestock sales.
- Deep Market sales.

Record the specific livestock sold and the receiving dealer.

### Achievements

Record reward credits received from achievements.

### Quests

Record credits received from completed quests.

### Diving

Track credit rewards from expeditions only where an actual approved credit reward exists.

Do not invent a dive-completion bonus.

Income from selling livestock recovered on a dive belongs in the livestock sales category.

### The Dock Casino

When implemented, record:
- Winnings.
- Payouts.
- Refunds.
- Adjustments.

Do not count returned wagers as additional profit.

### Other income

Allow new income categories to be registered without redesigning the system.

Do not create fictional income transactions for features that are only planned.

---

## 5. EXPENSE CATEGORIES

Track all legitimate AC spending.

Include:

### Aquarium purchases
- Tank purchase price.
- Tank type.
- Tank capacity.
- New 15,000-gallon tank where implemented.

### Livestock purchases
- Fish.
- Coral.
- Bottom dwellers.
- Mystery Eggs.
- Mystery Coral.
- Other approved specimens.

### Equipment
- Filters.
- Lighting.
- Heaters.
- Chillers.
- Pumps.
- Fragging tools.
- Other equipment.

### Water changes
- Tank receiving the change.
- Water-change percentage.
- Water volume changed.
- Total AC charged.

### Feeding and supplies
- Fish food.
- Coral food.
- Bottom-dweller food.
- Supplements.
- Consumables.

### Medical expenses
- Medicines.
- Diagnostic tests.
- Treatment supplies.
- Quarantine-related purchases.

### Diving
- Reef Diving: 1,000 AC per trip.
- Deep Sea Diving: 10,000 AC per trip.

These amounts include approved boat and equipment rental costs.

Do not record the rental twice.

### Deep Market
- Livestock purchases.
- Mystery Eggs.
- Restricted fictional treatments.
- Other authorized purchases.

### The Dock Casino
- Wagers.
- Fees if an explicitly approved fee exists.

### Other expenses
Allow future expense categories through the centralized transaction system.

---

## 6. TRANSACTION HISTORY

Create a chronological transaction history.

Each record must contain:

- Unique transaction ID.
- Account/profile ID.
- Transaction type.
- Category.
- Signed AC amount.
- In-game day.
- In-game time.
- Real timestamp.
- Source or destination.
- Relevant aquarium ID.
- Relevant livestock ID where applicable.
- Related purchase/sale/action ID.
- Optional descriptive note.
- Resulting wallet balance.

Example:

Day 15 — 09:46
Healthy Aquarium Reward
+50 AC

Day 15 — 09:47
Livestock Survival Bonus
+200 AC

Day 15 — 10:12
Purchased Coral Food
−45 AC

Day 15 — 10:28
Sold Coral Frag
+350 AC

Display newest transactions first by default.

Transactions must remain readable and searchable/filterable.

Never invent missing historical transactions.

---

## 7. TRANSACTION FILTERS

Provide:

All Activity
Income
Expenses

Additional category filters:

- Daily Rewards.
- Livestock.
- Aquarium Maintenance.
- Equipment.
- Deep Market.
- Diving.
- Casino.
- Achievements.
- Quests.
- Other.

Only display filters for categories that are supported.

Provide an optional search input to locate:
- Livestock names.
- Aquarium names.
- Transaction descriptions.

The UI must not become overly complicated.

---

## 8. OPTIONAL FINANCIAL CHART

Add a compact historical income and expense chart if supported by the current local UI framework.

Display income and spending across in-game days.

Requirements:
- Use actual financial records.
- Income and expenses must be visually distinguishable.
- Allow timeframe selection.
- Do not display invented data.
- Ensure numerical totals match the transaction ledger.

The chart is secondary to the transaction list and wallet reconciliation.

---

## 9. CENTRALIZED AC TRANSACTION LEDGER

This is the most important engineering requirement.

All AC changes must pass through one authoritative financial transaction service.

Do not let independent game systems modify wallet balance without a corresponding recorded transaction.

Examples:
- Aquarium purchase.
- Livestock sale.
- Healthy-day reward.
- Survival bonus.
- Deep Market trade.
- Equipment purchase.
- Water change.
- Diving fee.
- Casino wager.
- Casino payout.

Each operation must atomically update:
1. Wallet balance.
2. Transaction ledger.
3. Related item or game state.

Use unique transaction IDs and idempotency protection.

Do not allow:
- Negative wallet balances caused by race conditions.
- Duplicate purchases.
- Repeated daily rewards.
- Duplicate casino payouts.
- Double payment for a diving trip.
- Item creation when the wallet deduction fails.
- Lost credits from partial transactions.

Avoid adding multiple competing wallet systems.

---

## 10. EXISTING SAVE MIGRATION

The game already has local save data.

Preserve existing AC balances.

When a pre-ledger account is first loaded:

- Keep its wallet amount exactly as saved.
- Record a migration opening balance or baseline entry.
- Start tracking subsequent transactions.
- Clearly explain that older historical transactions are unavailable unless authoritative records already exist.

Do not fabricate previous earnings or spending.

Do not give migration bonuses.

Account-specific ledgers must stay separate.

Save and restore transaction history consistently.

---

## 11. OFFLINE INCOME TRACKING

The aquarium simulation continues while the game is closed.

Offline income must be recorded accurately.

Examples:
- Qualifying +50 AC healthy-day rewards.
- Qualifying +200 AC livestock-survival rewards.
- Other approved automatically generated income.

Use the established simulation results.

Do not award credits for days that fail eligibility requirements.

Prevent reloads, system-clock changes, or importing old saves from creating repeated rewards.

Use efficient aggregation for large offline histories while preserving accurate totals and meaningful audit information.

The Welcome Back report should agree with the financial ledger.

---

## 12. TANK ASSET VALUE MUST REMAIN SEPARATE

Aquarium Credits and tank asset value are different concepts.

Current AC Balance:
Spendable credits owned by the player.

Tank Asset Value:
Estimated current value of owned tank assets.

Do not add tank asset value to the player's wallet unless an actual sale occurs.

Changes in fish health, coral growth, rarity-based valuation, or equipment depreciation must not create AC income transactions.

The leaderboard preview continues to use aquarium asset value, not wallet balance.

---

## 13. TRANSACTION DETAILS

Clicking an individual ledger entry should open or expand a transaction detail view.

Example:

Transaction: Coral Frag Sale
Amount: +450 AC
Dealer: Deep Market
Species: [Actual species]
Specimen ID: [Persisted ID]
Aquarium: [Aquarium name]
In-game Time: Day 15 — 12:30
Resulting Balance: [Actual AC]

Use actual existing values.

Never expose internal secret material or password credentials.

If a detail was never recorded, show it as unavailable rather than inventing it.

---

## 14. PERFORMANCE

The financial dashboard must remain responsive even after hundreds or thousands of transactions.

Use:
- Efficient filtering.
- Pagination or list virtualization.
- Incremental summaries where appropriate.
- Versioned ledger schema.
- Validated local storage.

Do not rerender the aquarium unnecessarily when filtering transactions.

Preserve the game's existing performance requirements.

---

## 15. REQUIRED TESTS

Verify:

1. Clicking AC opens the financial dashboard.
2. X closes the dashboard.
3. Escape closes the dashboard.
4. Clicking outside the modal closes it.
5. Current wallet balance is accurate.
6. Income transactions are recorded.
7. Expense transactions are recorded.
8. Summary totals reconcile.
9. Timeframe filtering works.
10. Category filtering works.
11. Individual transaction details are correct.
12. Existing accounts retain their balances.
13. Existing saves migrate safely.
14. New accounts start with the approved 5,000 AC.
15. Healthy-day rewards appear in the ledger.
16. Livestock-survival rewards appear correctly.
17. Death-related bonus interruptions are respected.
18. Livestock sale credits appear correctly.
19. Deep Market trading transactions appear correctly.
20. Water-change expenses appear correctly.
21. Diving costs appear correctly.
22. Casino transactions appear correctly where those games are implemented.
23. No duplicate transaction rewards occur.
24. No purchase succeeds without sufficient AC.
25. Offline rewards are recorded exactly once.
26. Account ledgers do not mix.
27. Tank asset value is not counted as wallet income.
28. Game remains fully offline.
29. Freshwater remains locked.
30. Existing aquatic simulation is not interrupted by the dashboard.

Report actual testing outcomes.

---

## 16. DOCUMENTATION

Update the consolidated 31-section MDP and the relevant project files:

- GAME_DESIGN.md.
- UI_SPECIFICATION.md.
- DEVELOPMENT_STATUS.md.
- BALANCE_REPORT.md.
- Financial transaction documentation.
- Existing save-schema documentation.
- PDF continuity and locked rules, if supported.

Add permanent rule:

**Every change to spendable Aquarium Credits must be captured by one authoritative, persisted, auditable financial transaction system.**

The AC display must open the player's Financial Overview modal.

Do not duplicate the economy formulas across different systems.

---

## 17. CODEX COMPLETION RULE

After completing authorized edits, report:

- Files edited.
- Features added.
- Transaction sources integrated.
- Tests passed.
- Tests failed or not run.
- Known limitations.
- Documentation updated.

Clearly inform the player when the editing task is complete.

The final standalone line must be exactly:

Done With Edits

Only use that line after the authorized implementation is genuinely complete.

# FINAL DIRECTIVE

Implement a clickable Aquarium Credits display that opens a financial dashboard showing accurate income, expenses, net changes, current balance, and transaction history.

Centralize all AC changes through one persisted transaction ledger.

Preserve existing accounts, saves, aquarium simulations, and all approved economy rules.

Do not unlock freshwater.

Test thoroughly and notify the user when finished.
