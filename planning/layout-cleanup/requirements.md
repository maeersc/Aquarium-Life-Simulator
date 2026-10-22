AQUARIUM LIFE — UI LAYOUT CLEANUP UPDATE
Codex GPT-6 Astra

ROLE
You are the lead UI/UX developer and front-end layout engineer for Aquarium Life.

Your task is to clean up and improve the main Aquarium screen layout based on the latest UI review screenshots.

IMPORTANT
- This update is for the Aquarium Life browser game.
- Saltwater only right now.
- Do not unlock or expand freshwater systems.
- Preserve all current game functionality unless a layout change below explicitly says otherwise.
- Do not remove any underlying feature logic just because a visual element is removed from the screen.
- Keep the current Aquarium Life visual style: dark background, slate-blue panels, clean premium UI, and the approved aquarium game art style.
- Keep existing save compatibility.
- Keep the game fully offline.
- When done, provide a short report and end with: Done With Edits

==================================================
1. MAIN GOAL
==================================================

Fix the main aquarium screen so it feels cleaner and gives more space to the aquarium itself.

The aquarium/tank should become the visual focus of the screen.

This update should:
- center the Aquarium Keeper level badge properly
- remove unnecessary UI elements
- move the aquarium tab/selector beside the New Aquarium button
- reclaim unused space
- enlarge the tank area so it fills the open space better

==================================================
2. CENTER THE LEVEL BADGE
==================================================

The Aquarium Keeper level badge in the top header (example: "01") is not centered properly.

Fix it so that:
- the level badge is visually centered within its container
- it aligns properly with the Ocean Diving button and Aquarium Keeper text
- vertical alignment looks clean and intentional
- spacing around it matches the rest of the top bar

Do not change the level number logic.
This is a layout/alignment fix only.

==================================================
3. REMOVE THE THREE BOTTOM ACTION CARDS
==================================================

Remove these three large action cards from underneath the tank:

- Feed fish
- Water change
- Add a resident

These cards should no longer appear in that bottom row.

IMPORTANT:
- Do not delete the underlying features
- Do not remove the actual ability to feed fish
- Do not remove the actual ability to do water changes
- Do not remove the actual ability to add livestock

Only remove those large visible cards from this location in the main UI.

Those functions can remain accessible through their proper menus, store flows, inspectors, equipment pages, or other existing systems.

==================================================
4. REMOVE THE EXTRA TOP TEXT
==================================================

Remove the decorative text above "Your aquariums.":

"A LITTLE CARE. A WORLD OF LIFE."

This text is not needed.

Keep:
- "Your aquariums."

Remove only the decorative line above it.

==================================================
5. MOVE THE AQUARIUM TAB / SELECTOR
==================================================

The current aquarium tab/selector (example: "A pocket of ocean") should no longer remain under the "Your aquariums." heading.

Move the tank selector over beside the "+ New aquarium" button.

Expected result:
- the active tank selector should be placed in the same top row area as the New Aquarium button
- it should appear near the top-right area
- it should feel like part of the aquarium management controls
- it should replace the current awkward placement under the heading

Preferred behavior:
- use a dropdown or compact selector for the current aquarium
- it should show the currently selected aquarium name
- it should allow switching between owned aquariums
- it should remain compact and clean

Keep the + New aquarium button.

The tank selector and the + New aquarium button should feel like paired controls in the same control area.

==================================================
6. ENLARGE THE MAIN TANK
==================================================

After removing the unnecessary top text, moving the tank selector, and removing the three bottom cards, use the reclaimed space to make the aquarium/tank itself larger.

The tank should visually expand to fill the open space better.

Requirements:
- increase the visible size of the central tank panel
- expand vertically into the freed bottom space
- expand into the freed top space where appropriate
- reduce wasted empty margins
- keep the tank centered and balanced on screen
- preserve crisp rendering of fish, rock, coral, sand, and tank elements
- do not stretch sprites unnaturally
- keep click targets aligned correctly
- maintain responsive behavior for the main browser layout

The goal is:
the tank should feel like the main focus and should no longer look too small in the middle of a large page.

==================================================
7. KEEP THESE ELEMENTS WORKING
==================================================

Do not break or remove:
- Total Aquarium Value display
- Water & wellbeing side panel
- quest/progress side panel
- life/activity side panel
- Ocean Diving button
- Aquarium Keeper display
- Aquarium Credits display
- save/settings controls
- tank zoom/time controls if currently working
- aquarium livestock counts
- tank interaction/click behavior

Preserve the three-second selection highlight behavior for livestock if already implemented.

==================================================
8. LAYOUT / SPACING REQUIREMENTS
==================================================

After the UI cleanup:
- the page should look less cluttered
- the tank should dominate the center
- there should be less dead space
- the heading area should be tighter and cleaner
- the aquarium selector should feel more natural beside New Aquarium
- the main screen should not require unnecessary vertical scrolling on a normal desktop layout

Maintain a premium polished game UI look.

==================================================
9. TESTING REQUIREMENTS
==================================================

Verify and report:

1. Aquarium Keeper level badge is centered correctly.
2. Feed fish card is removed from the bottom row.
3. Water change card is removed from the bottom row.
4. Add a resident card is removed from the bottom row.
5. "A LITTLE CARE. A WORLD OF LIFE." is removed.
6. "Your aquariums." remains visible.
7. The aquarium selector is moved beside the New Aquarium button.
8. The + New aquarium button still works.
9. Aquarium switching still works.
10. The tank is visibly larger than before.
11. Tank contents remain aligned correctly.
12. Click targets in the tank still work.
13. Right-side status panels still display correctly.
14. The layout works on a standard desktop browser view.
15. No existing save data is broken.
16. Freshwater remains locked.
17. The game remains fully offline.

Do not mark tests as passed unless you actually verify them.

==================================================
10. COMPLETION REPORT
==================================================

When complete, provide:
- files changed
- what layout changes were made
- what was removed
- what was moved
- whether the tank size was increased successfully
- test results
- any remaining issues

The final standalone line must be exactly:

Done With Edits