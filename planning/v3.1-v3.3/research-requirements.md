# AQUARIUM LIFE — MARINE RESEARCH CENTER
## Codex GPT-6 Astra — Development Update v3.3
### Authorized Saltwater Research System

## 1. Primary Objective

Add a new Research section inside the existing Aquarium Store.

Players can spend exactly **5 Aquarium Credits (AC)** to permanently unlock detailed information about an individual fish species.

The Research Center must be educational, biologically credible, visually polished, and integrated into the existing Species Encyclopedia, financial ledger, and saved player account.

Current development remains SALTWATER ONLY.

Do not modify or unlock freshwater systems.

Preserve all previously approved Aquarium Life functionality.

---

## 2. Research Tab Location

Within the Aquarium Store, add:

**Saltwater → Research**

Do not add another main sidebar button.

The Saltwater Store category navigation should include Research alongside Fish, Corals, Bottom Feeders, Equipment, and other existing categories.

Keep:
- Existing modal styling.
- Upper-right X.
- Escape dismissal.
- Backdrop-click dismissal.
- Internal scrolling.
- Selected aquarium persistence.

The Research Center must remain accessible regardless of which aquarium the player currently has selected.

---

## 3. Research Cost

Every species has one research unlock cost:

**5 AC per species.**

Research is permanent for that player account.

Rules:
- Deduct 5 AC only when research is successfully purchased.
- Never charge for simply opening the Research tab.
- Never charge for browsing species names or previews.
- Never charge twice for an already researched species.
- Never deduct credits if the transaction fails.
- Require at least 5 AC before confirming the purchase.
- Record the payment in the AC Financial Dashboard.
- Save research completion against the specific species ID.

Example:

Researching Royal Gramma costs 5 AC.

Researching Royal Gramma again costs 0 AC.

Researching Copperband Butterflyfish later costs another 5 AC.

Use stable scientific species identity, not display names, for duplicate prevention.

Designer morphs should inherit their parent species' core biological research, with separate phenotype facts where supported. Do not repeatedly charge 5 AC for identical species-level information under different trade names.

---

## 4. Research Catalog

Include every implemented saltwater fish species in the research catalog, including species that are:

- Common.
- Uncommon.
- Rare.
- Very Rare.
- Ultra Rare.
- Legendary.

Rare species must not be excluded simply because the player has not yet obtained them.

Allow players to research fish before buying or collecting them.

Do not confuse research access with livestock ownership.

The research system should automatically recognize future added fish from the central livestock catalog.

Do not create duplicate species databases.

Fish currently present only as planned concepts or art-only subjects must not be presented as completed verified research records without valid supporting data.

---

## 5. Research Interface

Show a searchable fish list.

Each fish listing should include:
- Common name.
- Scientific name.
- Species artwork, if available.
- Rarity.
- Research cost.
- Research status.

Possible statuses:
- Not Researched.
- Researched.
- Research Data Incomplete.

For unresearched species, display a short free preview including common name, scientific name and rarity.

Once researched, show:

**View Research**

instead of a purchase button.

Support searching by common or scientific name, sorting by rarity, and filtering by research status.

---

## 6. Information Unlocked by Research

Each completed species report should include the following sections.

### A. Species Identification
- Common name.
- Scientific name.
- Scientific classification.
- Recognized common-name variants.
- Distinguishing physical features.

### B. Natural Habitat
- Native geographic distribution.
- Reef, lagoon, coastal, or deeper-water habitat.
- Preferred shelter.
- Typical depth, where reliably documented.
- Natural environmental conditions.

### C. Aquarium Care
- Recommended tank size in US gallons.
- Temperature range.
- Salinity range.
- pH range.
- Suitable flow and lighting.
- Hiding or shelter requirements.
- Environmental stability requirements.

### D. Diet and Feeding
- Wild diet.
- Aquarium feeding requirements.
- Feeding frequency where supported.
- Species-specific nutritional challenges.
- Important warnings.

### E. Temperament
- Peaceful, calm, territorial, aggressive, etc.
- Social behavior.
- Compatible livestock considerations.
- Predator/prey relationships.
- Conditions that may cause stress or aggression.

### F. Growth and Lifespan
- Maximum or typical adult size.
- Growth characteristics.
- Known lifespan information.
- Juvenile-to-adult appearance differences.

### G. Breeding
- General reproductive strategy.
- Courtship or pair formation where known.
- Egg or offspring development.
- Parental care where applicable.
- Difficulty of captive breeding.

### H. Medical Information
- Common aquarium health risks.
- Warning signs of illness.
- Environmental stress indicators.
- Relevant disease susceptibility where supported.
- Quarantine considerations.
- Treatment safety warnings.

Research reports must link to the existing Disease & Treatment Guide.

Do not claim a species-specific disease predisposition without reliable supporting evidence.

Do not imply that every treatment is reef-safe.

### I. Interesting Facts
Include three to five genuinely informative facts about the species.

Examples:
- Unusual swimming behavior.
- Symbiotic relationships.
- Distinct coloration.
- Feeding adaptations.
- Natural predator avoidance.
- Social or breeding behavior.

Avoid invented trivia.

### J. Game Information
Clearly distinguish Aquarium Life gameplay values from real scientific facts.

Include:
- In-game rarity.
- Care difficulty.
- Relevant store acquisition sources.
- Aquarium compatibility.
- Existing discovered/owned count, where supported.

Rarity is game collection scarcity, not conservation status.

---

## 7. Source Accuracy

Research should reflect reliable marine biology and aquarium husbandry.

Use existing verified project sources where available.

Do not invent:
- Geographic ranges.
- Scientific names.
- Breeding methods.
- Lifespans.
- Disease claims.
- Conservation status.

When information cannot be verified:
- Mark it as unverified.
- Avoid fabricated precision.
- Identify limitations in the research entry.

Since Aquarium Life runs offline, research information must be bundled locally.

No internet connection may be required at runtime.

If external sources are used during development, record the source name, URL, access date, and the facts supported in project documentation.

---

## 8. Field Journal Integration

Research must connect to:

**Field Journal → Species Encyclopedia**

When a player has researched a species, its full Research Report becomes available in the Encyclopedia.

For species not researched, display:

"Research available for 5 AC in Aquarium Store."

Do not duplicate the report into a separate conflicting database.

Use one authoritative species research data source for both views.

A previously purchased research unlock must persist even if the player sells all individuals of that species.

---

## 9. Financial Dashboard Integration

Research purchases must appear in the player's Aquarium Credits transaction history.

Example:

Transaction: Species Research
Species: Royal Gramma
Amount: −5 AC
Category: Research
Time: Actual in-game time
Resulting balance: Actual player balance

Use the existing centralized AC ledger.

Do not deduct AC directly from random interface code.

Research unlock and credit deduction must succeed atomically.

Avoid repeated charges from double-clicks or reloads.

---

## 10. Tutorial Integration

Add a short optional tutorial objective:

**Research Your First Fish**

Guide the player to:

Aquarium Store → Saltwater → Research.

Explain:
- Research costs 5 AC.
- Reports are permanent.
- Research can help prevent unsuitable livestock purchases.
- Medical information links to the Disease & Treatment Guide.

Do not require research to purchase an ordinary fish unless the user separately authorizes that restriction.

---

## 11. Research Progress Tracking

Add research progress to the Field Journal.

Example:

Saltwater Fish Researched: 12 / 86

Use the actual implemented research-eligible species count.

Do not hardcode an assumed catalog size.

Optionally support research-related achievements such as:
- First Discovery — research one fish.
- Marine Student — research ten fish.
- Marine Biologist — research fifty fish.

Do not add AC reward amounts without checking and balancing the existing achievement economy.

---

## 12. Save/Load Requirements

Persist:
- Account ID.
- Researched species IDs.
- Unlock timestamps.
- Research transactions.
- Research completion count.
- Associated achievements where implemented.

Use stable species IDs.

Preserve research unlocks across:
- Save/load.
- Logout/login.
- Tank transfers.
- Livestock sales.
- Offline simulation.
- Save migration.

Prevent importing old account data from replaying the same research purchase or award.

---

## 13. Required Tests

Verify:

1. Research tab appears under Saltwater Store.
2. Existing Saltwater Store categories still work.
3. All implemented saltwater fish are indexed.
4. Unimplemented species are not falsely represented as complete.
5. Researching one fish costs exactly 5 AC.
6. Research unlocks the correct species.
7. Already researched species remain free to view.
8. Double-clicking cannot duplicate charges.
9. Insufficient credits prevent purchases.
10. Every valid research transaction appears in the AC ledger.
11. Researched information opens in the Species Encyclopedia.
12. Research survives save/load.
13. Research is isolated between local player accounts.
14. Designer morphs do not trigger duplicate core-species research charges.
15. Research reports show care, habitat, diet, temperament, medical information, and facts.
16. Game-specific rarity is clearly separate from scientific facts.
17. Unverified claims are labeled appropriately.
18. Research progress totals update correctly.
19. Existing game simulation continues while the Research modal is open.
20. Game remains fully offline.
21. Freshwater remains disabled.
22. Existing livestock and aquarium saves remain intact.

Report actual passed, failed, and untested results.

---

## 14. Documentation

Update:
- Consolidated 31-section Master Development Prompt.
- GAME_DESIGN.md.
- UI_SPECIFICATION.md.
- CURRENT_LIVESTOCK_CATALOG.md where research metadata is applicable.
- DEVELOPMENT_STATUS.md.
- AC financial ledger documentation.
- Project continuity notes and PDF source where supported.

Add permanent rule:

**All implemented saltwater fish species may be researched for exactly 5 AC per biological species per account. Research unlocks are permanent and provide verified biological, husbandry, behavioral, and medical information.**

Do not recreate the Species Encyclopedia as a second incompatible feature.

---

## 15. Completion Requirement

When authorized edits are genuinely finished, report:
- Files edited.
- Research functionality implemented.
- Number of researchable species.
- Number of complete versus incomplete research entries.
- AC transaction integration.
- Journal integration.
- Tests passed or failed.
- Remaining limitations.
- Documentation updated.

End the final response with the exact standalone line:

Done With Edits

Do not use that line if work is incomplete or blocked.

# FINAL DIRECTIVE

Implement the Marine Research Center inside the Saltwater Aquarium Store.

Charge 5 AC for a permanent fish-species research unlock.

Provide detailed care guidance, interesting real-world facts, temperament, dietary information, reproductive information, and medical guidance.

Connect the system to the Field Journal, AC Financial Dashboard, local account saves, and future marine livestock additions.

Preserve all approved systems, remain fully offline, and keep freshwater locked.
