# AQUARIUM LIFE — THE DOCK CASINO IMPLEMENTATION & SIDEBAR FIX
## Codex GPT-6 Astra | Priority UI and Gameplay Update

### 1. Primary Objective

The Dock Casino was previously requested but is missing from the game's left sidebar.

Inspect the current project and determine whether the casino exists, is partially implemented, or is completely absent.

Implement and connect the required UI and gameplay functionality.

Do not create a decorative button that leads to an empty or nonfunctional page.

Preserve the approved Aquarium Life visual style and offline architecture.

Freshwater development remains locked.

---

## 2. Add The Dock Casino to the Left Sidebar

In the main left navigation, place:

1. Aquariums
2. Aquarium Store
3. Field Journal
4. Equipment
5. **The Dock Casino**
6. VIP Store
7. Settings

The Dock Casino must appear directly above VIP Store.

Use an original nautical-themed pixel-art icon, such as a ship's wheel or anchor.

Style the button consistently with the existing sidebar.

Requirements:
- Clearly visible label: The Dock Casino.
- Proper hover and active states.
- Keyboard accessibility.
- Responsive alignment.
- No overlap with neighboring tabs.
- Persist the navigation entry after reload.

The Dock Casino is an additional authorized sidebar item.

Do not remove existing navigation entries.

---

## 3. Casino Main Window

Clicking The Dock Casino opens a dedicated centered pop-up window.

Title:

**The Dock Casino**

Subtitle:

"Where fortunes rise and fall with the tide."

Include two playable game selections:

- Gold Fish.
- Predator & Prey.

Keep:
- X in the top-right corner.
- Escape-to-close behavior.
- Backdrop-click dismissal when no active wager or unresolved round would be lost.
- Internal scrolling.
- Aquarium Life slate-blue color palette.
- Original crisp pixel-art artwork.

The background aquarium should remain visible behind the modal.

The game's simulation clock must continue operating normally.

---

## 4. Casino Currency

Both casino games use Aquarium Credits (AC).

The casino must use the existing player wallet and centralized AC transaction ledger.

Display the player's actual current AC balance.

Players cannot wager more AC than they own.

Every wager and payout must be recorded in the AC Financial Dashboard.

Do not add real-money deposits, cash prizes, or withdrawal functionality.

---

## 5. Game One — Gold Fish

Implement a simple original fish-themed wagering game.

Working title:

**Gold Fish**

### Gameplay

Create a small, visually polished fish-symbol game.

A round works as follows:

1. Player chooses a wager.
2. Player confirms the wager.
3. The game displays three animated fish symbols.
4. The symbols stop.
5. The game evaluates the result.
6. Any winnings are awarded.
7. The player's balance updates.

Use original aquarium-themed symbols.

Suggested winning categories:
- Three matching symbols.
- Two matching symbols.
- A special Gold Fish combination.

Define exact symbol frequencies and payout multipliers in a central game-rules file.

Calculate and display the actual payout probabilities before enabling wagers.

Do not invent or claim fairness without testing the math.

Ensure losing rounds and winning rounds settle exactly once.

---

## 6. Game Two — Predator & Prey

Implement a card-based game using existing Aquarium Life marine livestock.

### Gameplay

1. Player selects an AC wager.
2. Player receives one random livestock card.
3. The dealer receives one random livestock card.
4. Cards are revealed.
5. Their matchup is evaluated.
6. The winning card determines the outcome.
7. Payout is processed.

Each card should show:
- Livestock artwork.
- Common name.
- Scientific name where appropriate.
- Ecological feeding role.
- Game-defined attack or defense statistics.
- Relevant special traits.

### Food Chain Mechanics

Use biological predator/prey relationships where documented.

Do not automatically make Legendary fish stronger than Common fish.

Rarity and food-chain position must remain separate.

Because real marine ecosystems are complex food webs rather than one universal ranking, implement an explicit, documented comparison rule for card matchups.

The game must handle:
- Player wins.
- Dealer wins.
- Draws.
- Equal-ranking matchups.
- Special interactions.

Display why a card won.

For example:

"Predator wins — the attacking species has a documented feeding advantage in this matchup."

Do not invent scientific predator/prey relationships.

If the biological relationship is unknown, use clearly identified fictional card-game statistics rather than presenting them as scientific facts.

---

## 7. Wagering System

Both games require:

- Wager selection.
- Available balance display.
- Confirmation.
- Clear round rules.
- Visible payout table.
- Results screen.
- Transaction history.
- Optional player spending limits.

Use a single authoritative wager and settlement service.

Ensure:
- A wager is deducted only once.
- Payouts are credited only once.
- Failed or interrupted rounds are handled consistently.
- Save/load cannot duplicate winnings.
- AC never becomes negative.

The casino must never use the aquarium's asset value as spendable money.

Only the player's actual wallet AC may be wagered.

---

## 8. Casino Artwork

All casino artwork must match the established Aquarium Life hybrid pixel-art direction:

- Classic 16-bit readability.
- Vibrant arcade colors.
- Recognizable detailed marine livestock.
- Premium indie atmosphere.

Create original assets for:
- The Dock Casino sidebar icon.
- Casino title illustration.
- Gold Fish symbols.
- Predator & Prey cards.
- Card backs.
- Dealer presentation.
- Win/loss effects.

Use existing approved livestock sprites where suitable.

Do not replace animal artwork with generic emojis or unrelated placeholders.

Ensure artwork is crisp at the actual UI display size.

---

## 9. Save and Financial Integration

Persist:
- Casino round IDs.
- Wager amounts.
- Outcomes.
- Payouts.
- Transaction IDs.
- Recent game history.
- Optional player spending preferences.

Keep records tied to the current local account.

Do not mix casino histories between accounts.

Show casino transactions in the AC Financial Dashboard under a Casino category.

Preserve:
- Existing AC balance.
- Aquarium Keeper level.
- Tank progress.
- Livestock.
- Deep Market reputation.
- Offline aquarium simulation.

---

## 10. Required Tests

Verify and report:

1. The Dock Casino appears above VIP Store.
2. Sidebar icon renders correctly.
3. Clicking the tab opens the casino modal.
4. X closes the modal.
5. Escape closes the modal safely.
6. Backdrop click works when appropriate.
7. Gold Fish is accessible and playable.
8. Predator & Prey is accessible and playable.
9. Both games show the player's correct wallet balance.
10. Wagers cannot exceed the wallet.
11. Gold Fish round outcomes follow documented probabilities.
12. Predator & Prey card matchups follow documented rules.
13. Winning payouts are accurate.
14. Losing wagers are deducted correctly.
15. Draws resolve according to documented rules.
16. Double-clicks cannot duplicate transactions.
17. Save/load cannot duplicate payouts.
18. Casino transactions appear in the AC Financial Dashboard.
19. Main aquarium simulation continues during casino gameplay.
20. UI scales correctly at common desktop resolutions.
21. Freshwater remains locked.
22. Game operates fully offline.

Do not report a test as passed unless it was actually performed.

---

## 11. Documentation

Update the appropriate sections of the consolidated Master Development Prompt.

Also update:
- GAME_DESIGN.md.
- UI_SPECIFICATION.md.
- DEVELOPMENT_STATUS.md.
- BALANCE_REPORT.md.
- Casino rules and payout documentation.
- Project continuity notes and PDF where supported.

Record The Dock Casino as an approved permanent sidebar item with two games:

**Gold Fish** and **Predator & Prey**.

Do not duplicate game rules across several files.

---

## 12. Codex Completion Requirement

When all authorized edits and tests are complete, report:

- Files changed.
- Sidebar implementation.
- Gold Fish gameplay.
- Predator & Prey gameplay.
- Artwork created.
- Casino wallet integration.
- Tests performed.
- Remaining limitations.

The final standalone line must be exactly:

Done With Edits

Do not claim completion if the casino is only partially implemented.

# FINAL DIRECTIVE

Fix the missing Dock Casino sidebar entry and implement both playable casino games.

Use Aquarium Credits for wagers, connect all transactions to the existing financial ledger, and preserve the existing aquarium systems.

Keep freshwater development locked.
