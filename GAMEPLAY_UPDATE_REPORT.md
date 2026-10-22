# Aquarium Life — gameplay, time, UI and settings update v2.4

Historical record: earlier survival-reward amounts and results below are superseded by v3.4. Current payments are 100 AC plus a separate independently qualified 50-AC healthy award. Actual historical receipts/test evidence are preserved, not rewritten. See V34_UPDATE_REPORT.md.

Date: 2026-10-13. Implemented in the offline browser build; consolidated MDP v3.0 retains 31 major sections.

## Implemented

US-gallon displays preserve internal liters and old physical capacities. The Field Journal now has separate habitat/category encyclopedia views and real Keeper Progress. Shopping uses a compact fixed destination/balance header. Saved settings add 12/24-hour clocks and truthful browser fullscreen controls. Coral, rock and decoration placement uses wheel/PageUp/PageDown depth, supported mounting and persistent painter order. Marine broods retain aquarium identity and care/exposure metadata, use shared valuation, drift or follow rock anchors as appropriate, and reuse existing art.

The shared clock runs at 20 real minutes per game day at 1×. Daily care pays 50 AC once per eligible player-day, with saved qualification/claim checkpoints. Welcome Back gates simulation and catch-up behind Continue; Start Over requires confirmation and offers export. Corrupt saves remain protected.

## Executed tests

All runs used isolated headless browser profiles under file:// with network access disabled. No actual player save was opened or modified.

| Suite | Chrome | Edge |
|---|---:|---:|
| New gameplay acceptance | 98 passed / 0 failed | 98 passed / 0 failed |
| System regression | 68 passed / 0 failed | 68 passed / 0 failed |
| Store / destination regression | 90 passed / 0 failed | 90 passed / 0 failed |
| Six-window UI regression | 139 passed / 0 failed | 139 passed / 0 failed |
| Health / economy / valuation | 69 passed / 0 failed | 69 passed / 0 failed |
| Clownfish art / direction / mounting | 7,583 passed / 0 failed | 7,583 passed / 0 failed |

New evidence: [Chrome](tests/gameplay-evidence/chrome-results.json), [Edge](tests/gameplay-evidence/edge-results.json), [protected-file/runtime integrity](tests/gameplay-evidence/integrity.json). Existing suites: `python tests/browser_qa.py chrome` (or edge), `--gameplay`, `--shell`, `--economy`, `--clownfish`. System and store counts are separate; directional cases are included in the artwork count, not additional tests.

Two old economy assertions assumed no care income. They now subtract recorded care rewards when comparing the original economy and separately bound the subsidy to 50 AC per day. New rock-purchase UI fixtures commit the requested placement preview; encyclopedia fixtures assert habitat separation. Strict freshwater source comparison excludes only declared marine hooks plus the authorized shared calendar and brood identity additions. Tests were not weakened to accept failed compatibility, biology or transaction safeguards.

## User checklist — actual evidence

PASS here is within the locked saltwater livestock scope and supported browser runtime; limitations below are not claimed complete.

| # | Requirement | Result / evidence |
|---:|---|---|
| 1 | All player-facing tank volumes use US gallons | PASS — Main/source volume audit, store selectors and species/equipment/water-change paths; concentration mg/L is intentionally retained. |
| 2 | Numerically correct volume conversions | PASS — Exact factor and 75/150/300 L → 19.8/39.6/79.3 gal executable checks. |
| 3 | Physical capacity unchanged | PASS — Pure display/compatibility state comparison and additive legacy migration test. |
| 4 | Saltwater encyclopedia filtering | PASS — Real habitat/category controls; only marine fish and five coral groups. |
| 5 | Freshwater encyclopedia filtering | PASS — Real controls show nine non-benthic fish, two bottom feeders, six existing plants. |
| 6 | No freshwater expansion | PASS — Eleven original fish entries; 145 protected data/art files hash-identical. |
| 7 | Clownfish eggs on suitable surfaces | PASS — Rock-local clutch anchors, selectable scene hitboxes, support movement/removal guards. |
| 8 | Other fish reproductive placement | PASS — Supported marine demersal/water-column presentation; pelagic drift and Banggai mouthbrooding checks. Freshwater biology remains unchanged. |
| 9 | Egg visual development | PASS — Existing species egg images, 5-pixel early framing, developing clutch framing, 5–25-pixel magnified inspection. |
| 10 | Egg progress persists | PASS — JSON round trip preserves exact brood ID, progress, care metadata and attachment. |
| 11 | No duplicate hatching | PASS — Unique larval IDs/lineage and second post-reload simulation step. |
| 12 | Clickable keeper level | PASS — Real level button opens Field Journal / Keeper Progress. |
| 13 | Real XP breakdown | PASS — Actual level/XP/meter, 100-XP quest claim and repeat-claim rejection. |
| 14 | Actionable real progression suggestions | PASS — Current available prerequisites/objectives and welfare-first guidance; no new XP awards. |
| 15 | Compact store header | PASS — Title/destination/balance/X share header; <100px at 1366×768. |
| 16 | More visible product area | PASS — Product region >55% of desktop store modal, internal scrolling. |
| 17 | Store tabs and purchases | PASS — 90 store regression checks in each browser; exact 8/7/7 categories and destination invariants. |
| 18 | Visible top-right X | PASS — Seven tested viewports from 1920×1080 through 390×844. |
| 19 | Windowed mode | PASS — Real document.exitFullscreen result verified. |
| 20 | Fullscreen mode | PASS — Real user-gesture Fullscreen API succeeded in Chrome and Edge. |
| 21 | Truthful borderless option | PASS — Browser equivalent / future native wrapper explanation checked in Settings. |
| 22 | No fake success on unsupported requests | PASS — Rejected request injected into the API boundary; actual state remains windowed and denial is shown. |
| 23 | 12-hour clock | PASS — Main 3:45 PM, lighting 6:00 AM, feeder 9:00 AM; formatter midnight/noon checks. |
| 24 | 24-hour clock | PASS — Main 15:45 and centralized formatter checks. |
| 25 | Clock preference persistence | PASS — Real reload preserves 12-hour setting and display preference. |
| 26 | Mouse-wheel depth | PASS — Actual canvas wheel events move preview back/front; PageUp/PageDown keyboard checks. |
| 27 | Unrelated scrolling preserved | PASS — Store wheel event remains unprevented; product panel scroll behavior checked. |
| 28 | Supported rocks | PASS — Normalized bed plane across z=0/0.5/1, bounds and saved physical support checks. |
| 29 | Attached corals | PASS — Wrong-depth rock rejected; matching depth accepted; actual commit retains valid attachment. |
| 30 | Depth/layer persistence | PASS — Real reload preserves rock/coral/decoration depth and attachment; painter ordering checked. |
| 31 | Twenty-minute game day | PASS — Exact 1.2 game minutes/real second and 1,200-second day assertions. |
| 32 | Centralized day/night | PASS — Unchanged AL.Sim.light uses s.time; system/shell lighting regressions pass. |
| 33 | Consistent system time | PASS — Sim.step/advance/offline share Config pacing; clock-format biology comparison and fractional-midnight test. |
| 34 | Exactly 50 AC reward | PASS — Full healthy day adds exactly 50 and exact log message; integrated Sim.step boundary test. |
| 35 | No per-tank multiplier | PASS — One versus multiple stocked healthy tank fixtures both earn 50. |
| 36 | Unhealthy tank blocks reward | PASS — Toxins, oxygen, filtration, species ranges, multi-tank, severe and 25/35-minute variation checks. |
| 37 | No duplicate daily reward | PASS — Mid-day save/load, repeated settlement, rewind, offline cap and empty-at-midnight checks. |
| 38 | Welcome Back | PASS — Real saved-state reload displays title and Continue. |
| 39 | Correct Continue restoration | PASS — Actual selected aquarium, count, IDs, money, time and preferences retained. |
| 40 | Confirmed Start Over | PASS — Startup and Settings paths; Cancel preserves saved bytes; reset only after confirmation and habitat choice. |
| 41 | Correct first launch | PASS — No saved game written by welcome; Start New Game creates one empty/dry aquarium. |
| 42 | Protected corrupt saves | PASS — Malformed bytes stay locked through reset cancellation; export/import/recovery remain available. |
| 43 | Six-entry sidebar | PASS — Exact order asserted; 139 shell regression checks per browser. |
| 44 | Offline operation | PASS — file:// with network emulation offline; no HTTP/HTTPS requests or uncaught game exceptions. |
| 45 | Existing artwork/simulation functional | PASS — 7,583 art checks and 1,792 directional cases per browser; exact ten-day freshwater biological comparison. |

## Reward and save policy

Each qualifying full observed game day earns exactly 50 AC, regardless of aquarium count. At least one living resident or viable brood must remain at settlement. All stocked tanks must meet prepared/cycled/filter and safe water requirements; empty tanks are ignored. Minor unsafe variation up to 30 game minutes is tolerated. Severe toxin/oxygen/welfare problems or deceased residents block that day even if repaired just before midnight. Invalid days log a concise reason; a partial initial/migrated day does not pay. The exact reward log is `Daily Aquarium Care Reward: +50 AC`.

Accelerated play uses the same calendar and requirements. Offline survival catch-up retains its existing at-most-eight-game-hour cap but never earns care rewards; any affected partial day is ineligible. Relaxed return freezes the simulation. Current energy expenses and showcase income remain separate, so the wallet's midnight net change need not equal the reward alone. Existing 30/90/365-day marine scenarios retained both residents and received 1,450 / 4,450 / 18,200 care credits, bounded to full eligible days.

Schema stays 2, with additive gameplayVersion 1. Old saves gain display preferences, deterministic middle/support z, brood aquarium IDs and a fresh nonretroactive care checkpoint. Known incomplete gameplay extensions reject. No old volumes, identities, cash, selected aquarium, hidden medical rolls or livestock definitions are rescaled/rerolled. Depth is separate from sand thickness. Startup autosaving/catch-up is suspended until the player chooses to continue. Import/reset is explicitly confirmed.

## Files and documentation

New runtime files: `js/gameplay.js` (units/clock/qualification/migration), `js/gameplay-ui.js` (settings/progress/startup), `js/placement.js` (depth rendering/geometry), `css/gameplay.css` (compact header/startup/settings). Integrated into `index.html`, Core, Sim, Save, UI/Shell, Store/StoreRules, Habitat, Renderer, BroodView and Valuation. Review entry points load the shared helpers; the clownfish care review also displays gallons. Health UI volume/schedule presentation stays consistent. Species data and approved sprite assets are unchanged.

New verification: `tests/gameplay_checks.js`, `tests/gameplay_qa.py`, `tests/build_gameplay_report.py`, `tests/gameplay-evidence/`; existing regression fixtures and package manifest updated. Documentation updated: MASTER_DEVELOPMENT_PROMPT, README, UI_SPECIFICATION, GAME_DESIGN, DEVELOPMENT_STATUS, TEST_REPORT, ART_DIRECTION, and this report. Earlier audit/milestone reports explicitly point here as the later update. The permanent exact final-line rule is integrated into MDP section 31.3.

## Visual evidence

- [Compact store at 1366×768](tests/gameplay-evidence/chrome-compact-store.png)
- [Coral depth preview](tests/gameplay-evidence/chrome-coral-depth-preview.png)
- [Keeper Progress](tests/gameplay-evidence/chrome-keeper-progress.png)
- [Settings](tests/gameplay-evidence/chrome-settings.png)
- [First launch](tests/gameplay-evidence/chrome-first-launch.png)
- [Protected unreadable save](tests/gameplay-evidence/chrome-protected-save.png)

Screenshots were visually inspected for store layout and coral placement; automated geometry checks cover all seven viewport sizes. Matching Edge screenshots are alongside them.

## Remaining limits

- Borderless Fullscreen is the browser Fullscreen API equivalent. Native OS borderless/exclusive modes and resolution selection require a future desktop wrapper. Preferences do not bypass the browser gesture requirement.
- Marine reproductive groups use existing supported surface/water/protected presentations. Exact rare-species nest microstructure and species-specific egg predation are not simulated; exposure metadata and inspector text say this explicitly. Freshwater reproduction/art remains its existing model under the scope lock.
- Existing provisional stage artwork and broader historical full-project audit gaps remain; no new artwork, livestock roster, online services, payments or leaderboard were introduced. This is a feature-update verification, not a new full-project audit.
- Firefox, multi-hour performance soak, native wrappers and real private player collections were not tested. Offline local JSON is not tamper-proof; backups deliberately permit restoring an earlier game and are not online score authority.
