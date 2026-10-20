# Aquarium Life interface simplification

October 20, 2026 - playable v4.1.1 - consolidated master v4.11

The authorized first cleanup makes routine aquarium care easier to find while preserving existing simulation, ownership and transactions.

## Player-visible changes

- Six main destinations: Aquariums, Aquarium Store, Field Journal, Tank Care, The Dock Casino and Settings.
- Removed unfinished VIP/leaderboard previews and the premium-currency placeholder from normal navigation. Local aquarium asset comparison is in My Aquariums. Legacy preview links safely return there.
- Moved development art-review links from the aquarium footer/collection into collapsed Settings > Developer tools. Review pages and original assets remain available.
- Tank Care contains Installed Equipment, Feeding, Water Changes, Lighting, Coral Fragging and Inventory. Equipment categories use one dropdown. Feeding retains its existing food and feeder controls.
- Installed equipment lists emphasize operating status, rated capacity, thermostat target when relevant, Maintenance, Replace Part and Inspect. Inspect retains on/off, transfer, warned removal, thermostats and history. Age/component/interval details are collapsed; immediate fault warnings and service controls remain visible.
- The water laboratory retains its readings and routes water changes into the existing cost/resource preview and explicit confirmation in Tank Care. Removed duplicate laboratory quick-change buttons and the outdated one-dose wording.
- Field Journal > Progress groups Keeper Level, Objectives and Achievements. Old shortcuts, automatic milestones, earned rewards and claim controls retain their existing authorities.
- Main care warnings show three distinct notes with every additional note available through expansion. Notes remain expanded during recurring refreshes; the real resident-specific status still controls the health indicator. No chemistry or cause is fabricated.
- Food forecasts show real hours alongside game days at normal speed, using the existing twenty-minute game day. Forecasts remain conditional on compatible food and a working feeder.
- Tutorial routes and labels follow the same menu structure.

## Preservation and scope

No save-schema migration is required. No change to cycling, feeding demand, disease, mortality, water chemistry, heater output, equipment wear, receiving safety, natural breeding, livestock IDs/genetics, payouts, prices, rewards or the clock. Saves/export/import remain local and freshwater remains locked. Inventory storage and last-aquarium sale/empty ownership remain supported.

The optional fantasy setting, a unified new livestock inspector design, casino relocation and payout rebalancing were recommendations for later work and are not part of this first cleanup. The existing casino, mystery products and approved livestock remain functional. Earlier unrelated sprite-production/PDF limitations are not claimed resolved.

## Files changed

Presentation: `index.html`, `js/app-shell.js`, `js/ui.js`, `js/inventory-ui.js`, `js/equipment-maintenance-ui.js`, `js/update29-ui.js`, new `js/care-ui.js`, `css/ui-cleanup.css`.

Documentation: this report, `GAME_DESIGN.md`, `UI_SPECIFICATION.md`, `DEVELOPMENT_STATUS.md`, `MASTER_DEVELOPMENT_PROMPT.md`, exact complete `PROJECT_CONTINUITY_SOURCE.md`. All 31 master sections remain.

Verification/release: `tests/simplification_qa.py`, `tests/browser_qa.py`, affected navigation/removal expectations in Inventory, Store/casino and Pages suites, `tests/package.py`, `build.py`, rebuilt DIST and release ZIPs. Existing test actions follow the new Inspect location for removal; no production safety validation was relaxed.

## Executed verification

| Source suite | Actual result |
|---|---|
| Simplified care, shared model and real UI | 106 passed, 0 failed |
| Existing coordinated economy/service/sale/save acceptance | 85 passed, 0 failed |
| Inventory ownership, installation, thermostat, warned removal, reload | 68 passed, 0 failed |
| Store, research, casino, keyboard and header alignment | 139 passed, 0 failed |
| Protected simulation/economy/save/data/artwork comparison | 2,484 unchanged files |

Simplified care tests execute actual feeding, lighting, prepared water change, maintenance, equipment on/off, transfer-dialog access and removal confirmation, grouped progress routes, warnings, local JSON validation, zero-aquarium views, and five care tabs at 1920x1080, 1600x900, 1366x768 and 390x844. Screenshots were reviewed at desktop and phone widths.

The first development run exposed a duplicate navigation registry during editing; this initialization error was corrected. A test also needed boolean coercion for returned DOM elements. The older Inventory fixture was updated to open Inspect before removal and to expect six destinations. Final listed source runs have no failures or uncaught JavaScript errors.

Final rebuilt-DIST acceptance, Pages/local-save execution, source/DIST hashes and protected-file evidence are recorded in `tests/simplification-evidence/release-results.json` and accompanying actual browser outputs. Release verification compares both ZIPs with the current source and DIST. Reproduction:

```
python tests/browser_qa.py chrome --simplify
python tests/browser_qa.py chrome --economy20
python tests/browser_qa.py edge --inventory
python tests/browser_qa.py chrome --store-casino
python build.py
python tests/browser_qa.py chrome --simplify --dist
python tests/browser_qa.py edge --pages
python tests/package.py
python tests/verify_sprite_production_release.py --source-archive --check-only
```

No normal player browser profile or real player save was used by these disposable tests. No additional approval is needed to use the completed interface cleanup.
