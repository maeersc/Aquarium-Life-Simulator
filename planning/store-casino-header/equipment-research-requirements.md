# AQUARIUM LIFE — EQUIPMENT STORE FILTERING & FISH RESEARCH UI
## Codex GPT-6 Astra — UI and Artwork Update
### Saltwater Only

## 1. Development Objective

Update the Aquarium Life interface based on the attached Aquarium Store screenshot.

Focus on three improvements:

1. Add an equipment-category dropdown beside the existing store search bar.
2. Correct the artwork for coral fragging cutters and precision kits.
3. Move the fish research action from the Aquarium Store to the individual fish inspection window.

Preserve the existing game systems, saves, purchases, and financial transaction ledger.

Do not rewrite functioning store logic.

Freshwater development remains locked.

---

## 2. Equipment Category Dropdown

Location:

Aquarium Store → Saltwater → Equipment

In the screenshot, the search bar appears directly above the equipment product cards.

Place a compact dropdown immediately to the right of that search field.

### Equipment filter options

The dropdown should contain:

- All Equipment
- Heaters
- Chillers
- Pumps & Circulation
- Filters & Filtration
- Lighting
- Protein Skimmers
- Aeration
- Automatic Feeders
- Testing & Monitoring
- Coral Fragging Tools
- Coral Frag Mounting Supplies
- Other Equipment

Only show a category if matching equipment exists in the current catalog, unless it is intentionally labeled as future content.

### Filtering behavior

When the player selects Heaters:
- Display only heaters.
- Hide pumps, lights, filters, and unrelated equipment.

When the player selects Lighting:
- Display only aquarium lighting products.

When the player selects Coral Fragging Tools:
- Display only appropriate fragging tools, cutting equipment, and eligible kits.

When All Equipment is selected:
- Display every equipment product currently available in that store category.

### Search integration

The existing text search must work together with the dropdown.

Example:

Category: Heaters

Search: Level 2

Result: Only matching Level 2 heater products.

Clearing the search must not reset the chosen category.

Changing the category may preserve the text query, provided the resulting filtering behavior is clear.

Include an empty-result message when no equipment matches.

### Category metadata

Classify equipment through stable product category IDs in the central equipment catalog.

Do not identify heaters merely by whether their names contain the word "heater."

Do not create duplicate equipment records to support filtering.

### Tank compatibility

Preserve the current tank-capacity compatibility rules.

For every applicable equipment product, clearly show:
- Supported tank-size range in US gallons.
- Recommended capacity.
- Equipment output or rating.
- Price.
- Stock availability.
- Compatibility with the selected aquarium.

Selecting a filter must never disable existing compatibility checks.

Future 15,000-gallon equipment must be supported by the same category and capacity system.

Do not invent equipment performance ratings.

---

## 3. Improve Equipment Store Layout

The search box and dropdown should share the same toolbar.

Suggested layout:

Search Items: [Search field] [Equipment Category ▼]

Maintain:
- Original dark aquarium-themed styling.
- Slate-blue panels.
- Readable labels.
- Compact spacing.
- Responsive layout.
- Internal scrolling.
- Existing product-card functionality.

The dropdown must not cover product cards permanently or introduce unnecessary horizontal scrolling.

On narrower windows, allow the filter to wrap below the search field.

Keep the existing Aquarium Store's X, Escape, and backdrop-click dismissal behaviors.

---

## 4. Fix Coral Fragging Equipment Artwork

The current artwork for coral-cutting equipment is not sufficiently representative of the actual items.

Update the product images for:

- Coral Fragging Kit.
- Precision Coral Cutters.
- Coral Frag Saw, if implemented.
- Relevant coral-cutting or mounting tools with incorrect generic images.

### Required visual direction

Follow the approved Aquarium Life hybrid pixel-art style:

- Classic 16-bit readability.
- Vibrant arcade colors.
- Realistic recognizable tool anatomy.
- Premium indie visual polish.
- Crisp edges.
- Transparent or correctly integrated background.
- Consistent product thumbnail size.

### Specific images

**Precision Coral Cutters**

Show recognizable compact cutting pliers or coral bone cutters, with distinct handles, hinge, and cutting jaws.

**Coral Fragging Kit**

Show a compact set of appropriate coral fragging tools and supplies arranged together.

**Coral Frag Saw**

Show a recognizable specialized precision cutting tool, not a heater or aquarium thermometer.

**Frag Plugs and Mounting Supplies**

Show actual plug, rack, or mounting-supply silhouettes appropriate to their product type.

Do not reuse heater, thermometer, filter, or generic rectangular equipment artwork for these products.

Do not download copyrighted retail product images or copy branding.

Create original artwork.

### Artwork verification

Check:
- Product-image mapping.
- Sprite atlas coordinates.
- Cropping.
- Transparency.
- Scale.
- Inventory preview.
- Store preview.
- Product-detail preview.

All views must display the correct image for the selected equipment.

Do not change equipment prices or functionality just to replace artwork.

---

## 5. Relocate Fish Research

Remove the Research subcategory from:

Aquarium Store → Saltwater

The fish research action should instead appear when the player clicks an owned living fish in the aquarium.

Use the existing livestock inspector rather than creating another unrelated inspection system.

### New inspector action

Add:

**Research Fish**

When the clicked fish's biological species has not yet been researched, show:

Research Fish — 5 AC

When already researched, show:

View Research — Unlocked

The button must be easy to locate without crowding the livestock inspector.

### Research purchase

Preserve the established research price:

**5 AC per fish species, once per player account.**

Rules:
- Permanent research unlock.
- No repeat charge for the same biological species.
- Insufficient AC prevents purchase.
- Confirmation before deduction.
- Successful purchase and unlock are atomic.
- Purchase appears in the AC Financial Dashboard.
- Unlock persists through save/load.
- Research remains unlocked after the fish dies or is sold.

Designer clownfish morphs share their parent species' core biological research, with additional verified morph information where available.

Do not charge again for the same species just because it has a different color pattern.

---

## 6. Fish Research Report

Clicking Research Fish should open a report or a purchase confirmation followed by the unlocked report.

The research report must include:

- Common name.
- Scientific name.
- Natural habitat.
- Native geographical range.
- Recommended tank size in gallons.
- Water-temperature range.
- Salinity and appropriate chemistry.
- Diet and feeding.
- Temperament.
- Compatibility.
- Adult size and growth.
- Breeding facts.
- Known husbandry risks.
- Medical warning signs.
- Disease and quarantine guidance.
- Interesting real-world facts.
- In-game rarity and care difficulty, clearly separated from biological facts.

Use verified local research data.

Do not invent scientific information.

If information is unavailable, identify that limitation instead of making unsupported claims.

The game must remain playable completely offline.

---

## 7. Field Journal Research Access

Preserve:

Field Journal → Species Encyclopedia

Once a fish has been researched, its unlocked report must be available from the Encyclopedia.

Do not require the player to own the fish permanently to access purchased research.

The Encyclopedia should clearly distinguish:
- Research not unlocked.
- Research unlocked.
- Research data incomplete.

For unresearched entries, tell the player:

"Select an owned fish in your aquarium to unlock its research for 5 AC."

Do not leave a broken link pointing to the removed Store Research tab.

The previous Research Store interface must not remain active through hidden navigation routes.

---

## 8. Inspectors and Livestock Selection

Preserve the existing three-second selection-highlight rule.

Clicking a fish should:
1. Select the correct individual.
2. Open the existing livestock inspector.
3. Display the Research Fish or View Research action.
4. Allow the highlight around the fish to expire after three seconds.

The inspector should remain open even after the visual selection highlight disappears.

Do not close the research window automatically after three seconds.

Coral and bottom-dweller inspectors must remain functional.

This update does not authorize a separate paid research mechanic for coral or bottom dwellers.

---

## 9. Financial and Save Integration

Use the existing central AC transaction ledger.

A successful fish research purchase must generate one transaction:

Category: Species Research
Amount: −5 AC
Species: Actual species
Account: Current local player
Time: Current in-game time

Do not bypass the wallet transaction system.

Preserve research unlocks through account switching and save/load.

Equipment filter choices may be persisted as UI preferences, but must not corrupt store state.

Do not alter existing livestock identities or equipment ownership.

---

## 10. Required Testing

Verify:

1. Equipment dropdown appears beside the search box.
2. All Equipment displays all eligible products.
3. Heaters shows only heaters.
4. Lighting shows only lights.
5. Pumps & Circulation shows only matching products.
6. Filters & Filtration works correctly.
7. Coral Fragging Tools displays only appropriate tools.
8. Search and dropdown filters work together.
9. Empty results show an informative message.
10. Tank-size compatibility checks still work.
11. Prices and stock remain unchanged.
12. Precision cutters display correct artwork.
13. Fragging kits display correct artwork.
14. No heater artwork appears on cutting tools.
15. Research is removed from the Saltwater Store category bar.
16. Clicking an owned fish opens its inspector.
17. Research Fish appears for unresearched species.
18. Research costs exactly 5 AC.
19. Already researched species remain free to view.
20. Research data appears in the Species Encyclopedia.
21. Research persists through save/load.
22. Research payments appear in the AC Financial Dashboard.
23. Three-second livestock highlight behavior still works.
24. Coral and bottom-dweller inspection remains unaffected.
25. Game works without internet access.
26. Freshwater content remains disabled.

Do not mark a test as passed unless it was actually executed.

---

## 11. Documentation

Update the relevant primary sections of the consolidated 31-section Master Development Prompt.

Also update:
- UI_SPECIFICATION.md.
- GAME_DESIGN.md.
- ART_DIRECTION.md.
- DEVELOPMENT_STATUS.md.
- Research-system documentation.
- Equipment product metadata where applicable.
- Project PDF/continuity documentation where supported.

Add these permanent rules:

**Equipment Filtering:** Every equipment product must have a stable category assignment, and the Equipment Store must support category filtering alongside text search.

**Equipment Artwork:** Product artwork must visually represent the item being sold; fragging tools must not reuse unrelated heater or equipment sprites.

**Fish Research:** Fish species research costs 5 AC per species per player account and is initiated from an owned fish's inspector. Completed research remains available in the Species Encyclopedia.

Avoid duplicating research and equipment definitions across unrelated files.

---

## 12. Completion Requirement

When all authorized changes are complete, Codex must report:

- Files edited.
- Equipment filter categories implemented.
- Artwork replaced.
- Research UI changes.
- Save and AC ledger integration.
- Tests passed, failed, or not run.
- Remaining limitations.

The final standalone line must be exactly:

Done With Edits

Do not claim completion when the work remains unfinished.

# FINAL DIRECTIVE

Implement the equipment-category dropdown next to the store search field, correct the pixel artwork for coral fragging tools, and move the existing fish research action to the individual fish inspector.

Preserve all existing functionality and offline compatibility.

Do not enable freshwater development.
