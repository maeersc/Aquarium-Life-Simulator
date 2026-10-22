"""Build the v2.4 report from executed evidence; fail if any required suite failed."""
from pathlib import Path
import hashlib,json,re
R=Path(__file__).resolve().parent.parent
evidence=R/'tests/gameplay-evidence'
suites=[('New gameplay acceptance','tests/gameplay-evidence/{browser}-results.json'),('System regression','tests/{browser}-results.json'),('Store / destination regression','tests/{browser}-store-results.json'),('Six-window UI regression','tests/ui-overhaul-evidence/{browser}-results.json'),('Health / economy / valuation','tests/economy-evidence/{browser}-results.json'),('Clownfish art / direction / mounting','tests/{browser}-clownfish-results.json')]
reports={};rows=[]
for label,path in suites:
 counts=[]
 for browser in ['chrome','edge']:
  d=json.loads((R/path.format(browser=browser)).read_text(encoding='utf-8'));assert d['failed']==0,(label,browser,d['failed']);reports[(label,browser)]=d;counts.append(d['passed'])
 rows.append(f'| {label} | {counts[0]:,} passed / 0 failed | {counts[1]:,} passed / 0 failed |')
protected=json.loads((R/'tests/freshwater-protection-baseline.json').read_text())
changed=[p for p,h in protected.items() if p!='js/simulation.js' and hashlib.sha256((R/p).read_bytes()).hexdigest()!=h]
assert not changed,changed
mdp=(R/'MASTER_DEVELOPMENT_PROMPT.md').read_text(encoding='utf-8');assert len(re.findall(r'^# \d+\.',mdp,re.M))==31 and 'VERSION 3.0' in mdp and 'Done With Edits' in mdp
source=['js/gameplay.js','js/gameplay-ui.js','js/placement.js','js/core.js','js/simulation.js','js/save.js','js/ui.js','js/app-shell.js','js/store.js','js/store-rules.js','js/habitat.js','js/render.js','js/brood-view.js','js/valuation.js','index.html','css/gameplay.css']
integrity={'protectedFilesUnchanged':len(protected)-1,'protectedDifferences':changed,'mdpMajorSections':31,'mdpVersion':'3.0','runtimeHashes':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in source},'suiteResults':{label:{b:reports[(label,b)]['passed'] for b in ['chrome','edge']} for label,_ in suites}}
(evidence/'integrity.json').write_text(json.dumps(integrity,indent=2),encoding='utf-8')
items=[
('All player-facing tank volumes use US gallons','Main/source volume audit, store selectors and species/equipment/water-change paths; concentration mg/L is intentionally retained.'),
('Numerically correct volume conversions','Exact factor and 75/150/300 L → 19.8/39.6/79.3 gal executable checks.'),
('Physical capacity unchanged','Pure display/compatibility state comparison and additive legacy migration test.'),
('Saltwater encyclopedia filtering','Real habitat/category controls; only marine fish and five coral groups.'),
('Freshwater encyclopedia filtering','Real controls show nine non-benthic fish, two bottom feeders, six existing plants.'),
('No freshwater expansion','Eleven original fish entries; 145 protected data/art files hash-identical.'),
('Clownfish eggs on suitable surfaces','Rock-local clutch anchors, selectable scene hitboxes, support movement/removal guards.'),
('Other fish reproductive placement','Supported marine demersal/water-column presentation; pelagic drift and Banggai mouthbrooding checks. Freshwater biology remains unchanged.'),
('Egg visual development','Existing species egg images, 5-pixel early framing, developing clutch framing, 5–25-pixel magnified inspection.'),
('Egg progress persists','JSON round trip preserves exact brood ID, progress, care metadata and attachment.'),
('No duplicate hatching','Unique larval IDs/lineage and second post-reload simulation step.'),
('Clickable keeper level','Real level button opens Field Journal / Keeper Progress.'),
('Real XP breakdown','Actual level/XP/meter, 100-XP quest claim and repeat-claim rejection.'),
('Actionable real progression suggestions','Current available prerequisites/objectives and welfare-first guidance; no new XP awards.'),
('Compact store header','Title/destination/balance/X share header; <100px at 1366×768.'),
('More visible product area','Product region >55% of desktop store modal, internal scrolling.'),
('Store tabs and purchases','90 store regression checks in each browser; exact 8/7/7 categories and destination invariants.'),
('Visible top-right X','Seven tested viewports from 1920×1080 through 390×844.'),
('Windowed mode','Real document.exitFullscreen result verified.'),
('Fullscreen mode','Real user-gesture Fullscreen API succeeded in Chrome and Edge.'),
('Truthful borderless option','Browser equivalent / future native wrapper explanation checked in Settings.'),
('No fake success on unsupported requests','Rejected request injected into the API boundary; actual state remains windowed and denial is shown.'),
('12-hour clock','Main 3:45 PM, lighting 6:00 AM, feeder 9:00 AM; formatter midnight/noon checks.'),
('24-hour clock','Main 15:45 and centralized formatter checks.'),
('Clock preference persistence','Real reload preserves 12-hour setting and display preference.'),
('Mouse-wheel depth','Actual canvas wheel events move preview back/front; PageUp/PageDown keyboard checks.'),
('Unrelated scrolling preserved','Store wheel event remains unprevented; product panel scroll behavior checked.'),
('Supported rocks','Normalized bed plane across z=0/0.5/1, bounds and saved physical support checks.'),
('Attached corals','Wrong-depth rock rejected; matching depth accepted; actual commit retains valid attachment.'),
('Depth/layer persistence','Real reload preserves rock/coral/decoration depth and attachment; painter ordering checked.'),
('Twenty-minute game day','Exact 1.2 game minutes/real second and 1,200-second day assertions.'),
('Centralized day/night','Unchanged AL.Sim.light uses s.time; system/shell lighting regressions pass.'),
('Consistent system time','Sim.step/advance/offline share Config pacing; clock-format biology comparison and fractional-midnight test.'),
('Exactly 50 AC reward','Full healthy day adds exactly 50 and exact log message; integrated Sim.step boundary test.'),
('No per-tank multiplier','One versus multiple stocked healthy tank fixtures both earn 50.'),
('Unhealthy tank blocks reward','Toxins, oxygen, filtration, species ranges, multi-tank, severe and 25/35-minute variation checks.'),
('No duplicate daily reward','Mid-day save/load, repeated settlement, rewind, offline cap and empty-at-midnight checks.'),
('Welcome Back','Real saved-state reload displays title and Continue.'),
('Correct Continue restoration','Actual selected aquarium, count, IDs, money, time and preferences retained.'),
('Confirmed Start Over','Startup and Settings paths; Cancel preserves saved bytes; reset only after confirmation and habitat choice.'),
('Correct first launch','No saved game written by welcome; Start New Game creates one empty/dry aquarium.'),
('Protected corrupt saves','Malformed bytes stay locked through reset cancellation; export/import/recovery remain available.'),
('Six-entry sidebar','Exact order asserted; 139 shell regression checks per browser.'),
('Offline operation','file:// with network emulation offline; no HTTP/HTTPS requests or uncaught game exceptions.'),
('Existing artwork/simulation functional','7,583 art checks and 1,792 directional cases per browser; exact ten-day freshwater biological comparison.')]
assert len(items)==45
report='''# Aquarium Life — gameplay, time, UI and settings update v2.4

Date: 2026-10-13. Implemented in the offline browser build; consolidated MDP v3.0 retains 31 major sections.

## Implemented

US-gallon displays preserve internal liters and old physical capacities. The Field Journal now has separate habitat/category encyclopedia views and real Keeper Progress. Shopping uses a compact fixed destination/balance header. Saved settings add 12/24-hour clocks and truthful browser fullscreen controls. Coral, rock and decoration placement uses wheel/PageUp/PageDown depth, supported mounting and persistent painter order. Marine broods retain aquarium identity and care/exposure metadata, use shared valuation, drift or follow rock anchors as appropriate, and reuse existing art.

The shared clock runs at 20 real minutes per game day at 1×. Daily care pays 50 AC once per eligible player-day, with saved qualification/claim checkpoints. Welcome Back gates simulation and catch-up behind Continue; Start Over requires confirmation and offers export. Corrupt saves remain protected.

## Executed tests

All runs used isolated headless browser profiles under file:// with network access disabled. No actual player save was opened or modified.

| Suite | Chrome | Edge |
|---|---:|---:|
'''+ '\n'.join(rows)+'''

New evidence: [Chrome](tests/gameplay-evidence/chrome-results.json), [Edge](tests/gameplay-evidence/edge-results.json), [protected-file/runtime integrity](tests/gameplay-evidence/integrity.json). Existing suites: `python tests/browser_qa.py chrome` (or edge), `--gameplay`, `--shell`, `--economy`, `--clownfish`. System and store counts are separate; directional cases are included in the artwork count, not additional tests.

Two old economy assertions assumed no care income. They now subtract recorded care rewards when comparing the original economy and separately bound the subsidy to 50 AC per day. New rock-purchase UI fixtures commit the requested placement preview; encyclopedia fixtures assert habitat separation. Strict freshwater source comparison excludes only declared marine hooks plus the authorized shared calendar and brood identity additions. Tests were not weakened to accept failed compatibility, biology or transaction safeguards.

## User checklist — actual evidence

PASS here is within the locked saltwater livestock scope and supported browser runtime; limitations below are not claimed complete.

| # | Requirement | Result / evidence |
|---:|---|---|
'''+ '\n'.join(f'| {i} | {label} | PASS — {e} |' for i,(label,e) in enumerate(items,1))+'''

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
'''
(R/'GAMEPLAY_UPDATE_REPORT.md').write_text(report,encoding='utf-8',newline='')
print(f'45 acceptance rows; 145 protected files unchanged; MDP 31 sections; {sum(reports[(label,"chrome")]["passed"] for label,_ in suites):,} checks per browser, zero failures.')
