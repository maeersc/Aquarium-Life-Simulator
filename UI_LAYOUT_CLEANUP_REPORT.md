# Aquarium Life - UI layout cleanup

Completed 2026-10-15, playable v3.6. This is a presentation update; no save schema or simulation formula changed.

The Aquarium Keeper badge now has zero horizontal button padding, a fixed flex size, tabular numerals and vertical centering within the shield. The decorative slogan and the three large bottom care cards are removed from the markup. Feeding remains in Equipment > Tank Care > Feeding; water changes remain in Equipment > Water Change; livestock purchases remain in Aquarium Store.

A labeled native aquarium dropdown now sits beside + New aquarium. It lists owned aquarium names, selects the current aquarium, clears placement/selection when switching, updates the main view and saves the destination through the existing local save service. The existing management-window and store destination controls remain available.

The workspace has three rows instead of four, tighter margins, a narrower navigation rail and status column, and no space reserved for the removed cards. The existing resize observer now sizes the tank against actual toolbar, footer and placement-banner heights without requiring the deleted card row. The scene retains its original 480 x 240 rendering coordinates and 2:1 display proportions. Sprites, hitboxes, zoom and camera coordinates are unchanged.

## Verification

Chrome: 48 passed, 0 failed. Edge: 48 passed, 0 failed. Both used isolated QA profiles with networking disabled, never player profiles. Commands:

```
python tests/browser_qa.py chrome --layout-cleanup
python tests/browser_qa.py edge --layout-cleanup
```

Before/after measurements use the archived previous index, UI and shell scripts with the same fixture, browser and viewport. Results were identical in both browsers:

| Browser viewport | Previous visible canvas | Updated visible canvas |
| --- | --- | --- |
| 1366 x 768 | 578 x 289 | 898 x 449 |
| 1440 x 900 | 912 x 456 | 972 x 486 |
| 1920 x 1080 | 1316 x 658 | 1452 x 726 |

All six tested viewports (the three above, 1024 x 650, 764 x 900 and 390 x 844) retained proportional, fully visible canvases, no page overflow, paired selector controls and accessible status/quest/activity panels. Narrow screens use the existing horizontally scrollable panel strip; desktop panels scroll internally when necessary. Screenshots were inspected at desktop and mobile sizes.

Checks verified badge centering and header alignment; removal of all three cards and slogan; retained heading; named selector placement; actual New Aquarium purchase and dropdown refresh; switching both directions; schema and local-storage round trips; actual browser reload preserving account/tanks/selection; preserved store destination; freshwater creation/store lockout; actual pointer selection of fish and coral; the three-second selection deadline and expiry; placement-banner fit; value breakdown; zoom/time controls; settings; Ocean Diving; feeding and water-change menu access. No uncaught JavaScript errors or remote HTTP requests occurred.

Detailed results and before/after screenshots: `tests/layout-cleanup-evidence/{chrome,edge}-results.json` and adjacent PNGs. Tests cover menu access for feeding/water changes; their unchanged biological calculations were not retested in this layout-only suite. No manual Firefox or fullscreen testing was performed. No known outstanding layout defects in the tested configurations. Portrait screens retain some vertical space to preserve natural sprite proportions.

The rebuilt DIST also passed 258 GitHub Pages/local-save integration checks in each browser, including repository-subpath resources, extracted-folder startup, device/profile isolation, offline saving and no server save writes. Combined current cleanup and built-delivery checks: 612 passed, 0 failed. Hash comparison with the previous source release confirmed 1,655 protected JavaScript/art files unchanged. The complete master remains embedded in the continuity source.

## Files changed

- `index.html`: remove slogan/cards/tab row, add labeled selector beside New aquarium, load cleanup stylesheet.
- `css/ui-cleanup.css`: badge, compact header controls, margins, proportional tank and responsive layout.
- `js/ui.js`: populate/bind owned-aquarium selector; remove bindings to deleted cards.
- `js/app-shell.js`: calculate available tank size without deleted controls, retain placement space.
- `tests/browser_qa.py`, `tests/layout_cleanup_qa.py`, `tests/layout-cleanup-before.html`: offline acceptance suite and controlled baseline.
- `tests/package.py`: include new evidence in the source archive.
- `build.py`: include this report in DIST.
- `README.md`, `UI_SPECIFICATION.md`, `DEVELOPMENT_STATUS.md`, `MASTER_DEVELOPMENT_PROMPT.md`, `PROJECT_CONTINUITY_SOURCE.md`: record current layout while preserving historical content and full rosters.
- `planning/layout-cleanup/`: original request and previous-layout references.
- `DIST/`, GitHub Pages ZIP and portable source ZIP: regenerated delivery files.

All simulation, health, thermal, mortality, feeding, reward and freshwater biology source files and artwork remain unchanged. Existing player saves were not opened or altered. Saves remain device-local browser storage with user-controlled JSON export/import. The game remains fully offline; no new external dependencies were introduced.
