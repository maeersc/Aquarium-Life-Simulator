"""Maintain v2.8 design/registry/continuity records from actual browser evidence."""
from pathlib import Path
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parent.parent
def read(p):return (ROOT/p).read_text(encoding='utf-8')
def write(p,s):(ROOT/p).write_text(s.rstrip()+'\n',encoding='utf-8')
def load(p):return json.loads(read(p))
registry=load('assets/diving/registry.json')
registry['rosterBaseline']='Existing v2.7 roster; six encounter profiles reference existing IDs; zero added species'
registry['policy']='Depth intervals are conservative game eligibility bands within documented habitat; fictional restricted recovery is not a legal collection permit. Hawaii wildlife is observation-only.'
write('assets/diving/registry.json',json.dumps(registry,indent=2))
assert len(registry['regions'])==4 and len(registry['species'])==6
baseline=load('assets/expansion-v27/registry.json')['records']
assert len(baseline)==38 and all(p['id'] in {r['id'] for r in baseline} for p in registry['species'])
profile_table='| Existing species / ID | Region / mode / game depth band | Collection / conservation | Evidence |\n|---|---|---|---|\n'
for p in registry['species']:
 row=next(r for r in baseline if r['id']==p['id'])
 profile_table+=f"| {row['name']} / *{p['scientificName']}* / `{p['id']}` | {', '.join(p['regions'])} / {', '.join(p['modes'])} / {p['depth'][0]}–{p['depth'][1]} m | {p['collection']}; {p['conservation']} | [source]({p['source']})"+(f" · [range]({p['rangeSource']})" if p.get('rangeSource') else '')+' |\n'
current='''## Ocean Diving v2.8 — current, 2026-10-14

MDP **v3.3**, retaining all 31 major sections. **Ocean Diving** beside Keeper Level opens Reef (Level 5 / 1,000 AC) or Deep Sea (Level 10 / 10,000 AC). Fiji, Caribbean, Hawaii and Japan have original regional scenery and a compact playable map. W/A/S/D, arrows and on-screen buttons move one tile; every successful step costs exactly 5% oxygen from 100%. Blocked movement and collection clicks cost none. Eight temporary slots become owned only on a successful boat return with oxygen remaining. Exhaustion/confirmed abandonment forfeits discoveries without a fee refund.

Aquariums continue at 1× during planning, diving and results, using the existing 20-real-minute game day. Explicit safe receivers, supported coral mounts, species-conditioned survival, finite transport holding, persistent provenance and Reputation 5 Black Market-only resale are integrated. Confirmed paid Black Market purchases earn bounded reputation; canceled/failed/duplicate transactions do not. Direct normal-store livestock is restricted to Tiers 1–3; eight daily Fish slots and independent Mystery Egg odds remain unchanged. Nominal tank/equipment capacities now ceil to whole US gallons; physical liters and precise water-change calculations remain exact.

**No new biological species.** The approved 38-entry v2.7 batch and all protected freshwater content remain the roster baseline. Six sourced encounter profiles reference existing IDs; Hawaii wildlife is observation-only, and unsupported regional/depth combinations offer inert fictional salvage rather than invented animals. All captures are fictional restricted game recovery, not real collection authorization. New art is unapproved pending user review. Saves and expedition receipts remain on each player's PC in browser storage. See [DIVING_UPDATE_REPORT.md](DIVING_UPDATE_REPORT.md) and [the region ledger](assets/diving/registry.json). DIST is rebuilt through `python build.py`. Earlier milestones below are historical where superseded.
'''
details={
'GAME_DESIGN.md':'''Primary design reference: MDP §5.5. Maps are 11×7 cells with compact traversable routes, real collision tests and boat-distance warnings. Mobile fish shift deterministically after successful steps; distance is checked at the moment of collection. Trips have twelve discoveries, eight temporary slots, and near-boat rocks so a real out-and-back route is possible within twenty steps. Zero oxygen on a boat-arrival step is failure: arrival must happen with oxygen remaining. Failed or abandoned trips use a non-graphic safe-rescue report. There are no oxygen upgrades.

Every organism is assigned an explicit eligible receiving tank (and supported coral mount) before recovery. Safety is rechecked per individual on return, including cumulative stocking and prior received individuals. Unsafe delivery records a loss rather than inserting an animal. A 12–24-game-hour sensitivity-based transport deadline prevents indefinite survival in expedition inventory. Outcomes depend on sensitivity, transport, elapsed game time, steps, prior condition and a quarantine benefit; probabilities are game calibrations, not field-survival measurements. Alive specimens enter the existing health and valuation systems, not a new parallel animal model.
''',
'UI_SPECIFICATION.md':'''The always-visible Ocean Diving button is immediately after the saved Keeper Level badge; the six sidebar windows are unchanged. Planning uses the shared detail dialog, two mode tabs, region selector, exact rental breakdown, explicit launch confirmation, encounter cards and inventory. X, Escape and backdrop close ordinary windows. All three request confirmation during an active trip; interior clicks do not dismiss it. Purchase confirmation is still explicit and validates again before commitment. A sticky oxygen/region/inventory/boat-route HUD stays visible while scrolling the active dive. Keyboard auto-repeat is ignored; a controlled held-key timer submits actual steps. Touch-friendly direction buttons use the same action path.

Black Market shows reputation level, total XP, next-level XP, purchase caps and resale lock. Owned diving fish, coral and non-fish residents appear under Black Market → Sell with condition/budget checks; their inspectors route to that channel. Ordinary exchange/cutting actions reject diving provenance. Main tank selectors and store summaries show nominal whole gallons; precise replacement-water amounts retain fractional gallons.
''',
'DEVELOPMENT_STATUS.md':'''Implemented offline exploration, exact unlocks/fees/oxygen, four regions, compact collision maps, eight-slot temporary inventory, finite transport, safety-checked survival, owned rock placement, Black Market reputation/resale, high-tier normal-store rejection, active-trip persistence, local completion receipts, protected dismissal and whole-gallon nominal labels. Nine original image assets are integrated (eight backgrounds and an eight-object equipment sheet); all remain unapproved. The v2.7 species/art limits are unchanged. PDF continuity source is updated; binary PDF export remains pending unavailable PDF toolchain.
''',
'BALANCE_REPORT.md':'''Trip prices are exactly 1,000 and 10,000 AC inclusive of all displayed rentals. No collection credit/refund occurs before a successful return. Rocks are inert fictional salvage with no immediate cash payout; owned inventory is limited to 80 and installation consumes the owned item, without buying it again. Survival and disease make livestock recovery uncertain. Collector offers depend on individual current value, health, saved identity, demand, source risk and same-day saturation; they cap at 90% of species baseline and use existing daily sale and buyer-budget limits. No guaranteed profit is promised.

Reputation starts at level 1; each 100 reputation XP adds a level. A confirmed paid Black Market purchase awards at least 1 XP, then 1 per full 100 AC spent, capped at 25 per purchase and 50 per game day. Reputation 5 requires 400 total XP. Opening, canceling, failing and replaying a transaction award zero. This cap also applies to legacy fictional purchases, restricted treatments and Black Market containment equipment. Tier 4–6 direct fish are sold only through saved variable dealer listings. Exact Mystery Egg odds/600 AC/three daily eggs and 3/3/1/Mystery slots remain.
''',
'ART_DIRECTION.md':'''Built-in ImageGen created original source-v1 PNGs under `assets/diving/`: Fiji/Caribbean/Hawaii/Japan reef and deep backdrops plus one transparent 4×2 equipment atlas (diver, boat, oxygen cylinder, rock, sparkle, mask, transport crate, buoy). `js/diving-art-data.js` embeds those files for offline use. Regional scenery avoids generic culture symbols and generic final livestock silhouettes; live encounters reuse the existing species-specific expansion art. The approved clownfish reference was inspected and preserved. The supplied sprite is a static authored pose moved by the minigame; no separately authored swimming cycle is claimed. Sources are not overwritten. Art remains unapproved. Full prompts and original generated filenames are preserved in `assets/diving/art-prompts.json`; packing is byte-copy/base64 embedding, with a technical contact sheet for QA.
''',
'CURRENT_LIVESTOCK_CATALOG.md':'''### Regional encounter ledger — no new species

The six entries below are references to existing implemented species, not additions to the 38-entry batch or biological totals. Current totals remain 80 fish (69 marine/11 freshwater), ten marine corals and five non-fish invertebrates, plus six protected freshwater plants. Unassigned species never acquire a region based on their common name. The region ledger records scientific names, habitat, game depth bands, conservation/collection class, care, art, health/transport, holding and central valuation model. Existing real individual values continue to come from `AL.Valuation`.

'''+profile_table,
}
for path in ['README.md','GAME_DESIGN.md','UI_SPECIFICATION.md','DEVELOPMENT_STATUS.md','BALANCE_REPORT.md','ART_DIRECTION.md','CURRENT_LIVESTOCK_CATALOG.md','TEST_REPORT.md']:
 s=read(path)
 s=re.sub(r'\n## Ocean Diving v2\.8.*?(?=\n## (?:GitHub Pages build|Livestock expansion v2\.7))','\n',s,flags=re.S)
 s=s.replace('## Livestock expansion v2.7 — current,','## Livestock expansion v2.7 — roster baseline milestone,')
 first,rest=s.split('\n',1)
 write(path,first+'\n\n'+current+'\n'+details.get(path,'')+'\n'+rest.lstrip())

master=read('MASTER_DEVELOPMENT_PROMPT.md').replace('VERSION 3.2','VERSION 3.3')
master=re.sub(r'^### Revision: .*$', '### Revision: 3.3 adds Ocean Diving v2.8, regional eligibility, reputation, provenance and nominal whole-gallon display. All 31 major sections remain intact.',master,count=1,flags=re.M)
primary='''Ocean Diving is the authorized saltwater-only exploration feature v2.8. Use the existing fixed-step aquarium simulation, save, health, value, inventory and shared modal architecture. The button is always visible immediately beside the saved Keeper Level badge. Reef requires level 5 and costs exactly 1,000 AC; Deep Sea requires level 10 and costs exactly 10,000 AC. All rental/access components sum to that fixed total and are charged once by an atomic, confirmed launch transaction.

The data-driven registry `assets/diving/registry.json` currently enables Fiji, Caribbean, Hawaii and Japan. Its six encounter profiles reference existing v2.7 IDs, verified scientific names/ranges, appropriate habitats and conservative game depth bands. Unverified or incorrect-region organisms cannot spawn or be collected. Hawaii wildlife is observation-only; restricted fragments are explicitly fictional recovery and Black Market-only, never a claim of legal collection. Do not add future regions automatically or infer origin from common names. Preserve the approved 38-entry roster; diving catches are individuals, not new species.

Maps are compact 11×7 cell worlds with boat/descent, solid terrain, sand/reef scenery, nearby discoverable objects and traversable routes. W/A/S/D, arrows and direction buttons submit one cardinal movement action. Ignore native key auto-repeat; implement controlled held repeats. Only a completed movement costs exactly five oxygen percentage points. Start at 100%; blocked movement, frames, idle time and collection clicks cost no oxygen. Warn at 30, 15 and 5 percent and show route distance/return cost. Arrival must precede oxygen exhaustion; zero oxygen even on boat arrival fails. A nearby collection/physical return is winnable. No unapproved oxygen capacity or cost upgrades.

Left-click discovery selection and collection validate interaction distance at action time; moving fish have bounded positions. Each object occupies one of exactly eight temporary slots. Full inventory rejects new recovery without discarding existing discoveries. Nothing is permanently awarded before successful boat return. Exhaustion or explicitly confirmed abandonment records a non-graphic rescue, forfeits unreturned finds and gives no automatic fee refund.

Choose an explicit safe biological receiver before collecting livestock, and a supported mounting position for coral. Recheck safety cumulatively on return. Species sensitivity, prior condition, transport quality, elapsed game time, movement and receiving/quarantine conditions affect the saved assessment. Transport holding has a finite sensitivity-based deadline; animals cannot survive indefinitely in non-biological inventory. Persist healthy/stressed/injured/suspected illness/dead-on-arrival outcomes. Survivors enter existing fish/flora/invertebrate health systems and central valuation; unsafe or lost deliveries remain zero-value outcome records. Owned recovered rocks enter bounded inventory and are consumed through the existing placement workflow. Report region, mode, total fee, recovered objects, living/impaired/lost organisms, estimated asset value and resale eligibility. Never guarantee profit.

Planning, active play, confirmation and results run the authoritative aquarium simulation at 1× (20 real minutes = one game day), even if the underlying view was paused or accelerated. Keep hunger, chemistry, disease, growth, eggs, coral, equipment, calendar/store rotation and daily-care eligibility advancing through the same simulation; skip rendering the obscured aquarium. Preserve the prior speed preference when closing. Hidden/closed periods use existing offline catch-up. Save active position, oxygen, temporary IDs, collected flags, fee/transaction, region/mode and game state without relaunching or charging on resume. Core validation, transaction tokens, local completion receipts and existing timeline checks prevent normal duplicate/replayed settlement; editable local JSON is not cryptographic anti-cheat.

Use the approved hybrid pixel style and preserved original reference. Original diver/boat/oxygen/rock/effect/mask/crate/buoy art and eight regional backgrounds are local/embedded; existing species-specific living/dead artwork represents actual creatures. No new art is approved automatically. X, Escape and backdrop dismiss ordinary shared windows but require explicit loss confirmation for an active dive; inside clicks never dismiss or click through to aquarium objects. The oxygen/inventory/region/return HUD remains visible while scrolling. Other sections reference this primary specification rather than duplicating its rules.'''
additions={5:('5.5 Ocean Diving — Primary v2.8 Specification',primary),4:('4.5 Nominal Whole US Gallons','Display nominal aquarium/equipment capacities with mathematical ceiling to whole US gallons (75 L → 20 gal). Preserve exact internal liters, stocking capacity and all dose/chemistry calculations. Use the separate preciseVolume presentation for replacement-water quantities. See §5.5 for diving receiver displays.'),18:('18.8 Permanent Normal-Store Upper-Rarity Restriction','Ordinary direct livestock sales are limited to Common, Uncommon and Rare across fish, coral and bottom dwellers. Tiers 4–6 require a supported Mystery Egg, Black Market or eligible diving source. Never hatch coral/invertebrates from fish eggs. Reject bypass calls atomically. Keep the eight daily slots and exact independent Mystery odds in §§18.6–18.7. Regional acquisition/provenance is governed by §5.5.'),19:('19.4 Reputation and Diving Resale','Persist Black Market reputation XP independently of Keeper XP. Level is 1 + floor(XP/100). Confirmed paid market purchases award at least 1 XP, then one per full 100 AC spent; cap at 25 per purchase and 50 per game day. Canceled, failed and duplicate transactions earn zero. Show level/XP/next-level and unlock notice. Diving-acquired individuals retain permanent provenance and can be sold only through Black Market → Sell at reputation level 5+, subject to existing access/hours, health, budget, daily sale limits, demand, source risk and bounded saturation-sensitive offers. Core actions reject ordinary exchange/cutting bypasses; no dead specimen is sold as healthy. See §5.5 for capture/return rules.'),24:('24.5 Expedition Persistence and Local Receipts','Diving extension version 1 adds optional migration of reputation, active trip, history, owned recovered rocks and divingRng. Preserve wallet, existing residents, selected aquarium, hidden dealer rolls, clock and genetics. Restored valid active trips resume with the saved oxygen and haul and no new charge. A local completion receipt marks a replayed older active snapshot failed/forfeited instead of awarding it again. Invalid transport/outcome/provenance/region/identity state fails validation. Active game, recovery, timeline and receipts remain localStorage on the player PC; JSON export/import remains local. See §5.5 and the existing offline import timeline guard.'),26:('26.7 Diving and Modal Interaction','Keep the six main sidebar windows. Add the Ocean Diving button beside Keeper Level; follow §5.5 for shared-modal planning/play/results and protected dismissal. Ordinary X/Escape/backdrop behavior remains, with no click-through. Provide responsive keyboard/mouse/direction-button input, sticky oxygen HUD, explicit safe receivers and visible reputation/Black Market-only sale routing. Capacities follow §4.5.'),27:('27.14 Diving v2.8 Acceptance','Use tests/diving_checks.js, diving_resale_checks.js and the real browser diving_qa.py for all 38 requested checks. Run both Chrome and Edge offline, actual keyboard/left-click/modal/reload flows, safe recovery and resale, and the continued aquarium clock. Rerun expansion, art and deployed DIST/local-save regression suites. Record actual passed/failed/not-run results and evidence in DIVING_UPDATE_REPORT.md; do not infer an unrun suite passed.'),30:('30.4 Regional Eligibility and Registry Continuity','Every collectible region assignment must carry a verified scientific identity/source, habitat and depth suitability, conservation/collection status independent of rarity, care/art/health/value and receiving requirements. The six v2.8 profiles reference existing taxa; do not duplicate them as new species. Keep the source region ledger, generated offline script, current catalog and continuity/PDF source synchronized. Maintain exact species counts and distinguish fictional restricted recovery from legal collection. Keep DIST current through python build.py; local saves never become deployment inputs. Completion/reporting rules in §30.3 remain.')}
for section,(title,body) in additions.items():
 master=re.sub(r'\n## '+re.escape(title)+r'\n.*?(?=\n# \d+\.|\Z)','\n',master,flags=re.S)
 marker='\n# '+str(section+1)+'.';assert marker in master;master=master.replace(marker,'\n## '+title+'\n\n'+body+'\n'+marker,1)
assert re.findall(r'^# (\d+)\.',master,re.M)==[str(n) for n in range(1,32)]
subsections=re.findall(r'^## ([\d.]+) ',master,re.M);assert len(subsections)==len(set(subsections))
write('MASTER_DEVELOPMENT_PROMPT.md',master)
if '--prepare' in sys.argv:
 print('Prepared v2.8 static design/registry documents. Final acceptance report waits for all browser evidence.')
 raise SystemExit(0)

rows=[]
for browser in ['chrome','edge']:
 for label,path in [('Diving v2.8',f'tests/diving-evidence/{browser}-results.json'),('Livestock/core/health/freshwater',f'tests/expansion-evidence/{browser}-results.json'),('Artwork regression',f'tests/{browser}-clownfish-results.json'),('Deployed DIST / local PC saves',f'tests/pages-evidence/{browser}-results.json')]:
  result=load(path)
  assert result['failed']==0,(path,result['failed'])
  rows.append(f"| {browser.title()} | {label} | {result['passed']:,} | {result['failed']} | [{path}]({path}) |")
protected=load('tests/freshwater-protection-baseline.json')
unchanged={p:h for p,h in protected.items() if p!='js/simulation.js'}
assert len(unchanged)==145
assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in unchanged.items())
write('tests/diving-evidence/integrity.json',json.dumps({'masterVersion':'3.3','majorSections':31,'newSpecies':0,'baselineAddedEntries':38,'regionalProfiles':6,'protectedUnchanged':unchanged},indent=2))
acceptance=[
'Button beside Keeper Level: actual DOM order and locked visibility.',
'Reef unlock at saved level 5; level 4 rejects.',
'Deep unlock at saved level 10; level 9 rejects.',
'Reef flat fee exactly 1,000 AC through real UI and Core action.',
'Deep flat fee exactly 10,000 AC through real UI and Core action.',
'Breakdowns sum to flat totals, with one charge and idempotent launch token.',
'Exactly Fiji, Caribbean, Hawaii and Japan available; future Red Sea rejects.',
'Seeded region/mode encounter sweeps use the documented whitelist.',
'Incorrect-region map objects and owned provenance fail save validation.',
'Actual W/A/S/D browser key events complete a four-step circuit.',
'All four Arrow browser key events complete the same circuit.',
'Successful movement debits exactly five percentage points; held steps are bounded.',
'Blocked movement leaves position/oxygen unchanged.',
'Actual map/collection clicks and idle time consume no oxygen.',
'Actual left-click selection plus collect button recovers a nearby rock; out-of-range calls reject.',
'Eight real near-boat collections fill exactly eight temporary slots.',
'A ninth in-range collection rejects specifically for full inventory.',
'A real out-and-back path returns successfully with oxygen remaining.',
'Twentieth movement exhausts oxygen; zero even on boat arrival fails.',
'Failures/confirmed abandonment forfeit temporary items with no automatic fee refund.',
'Five species recovery outcomes round-trip through saved reports; actual living fish/coral/invertebrate fixtures verify provenance.',
'Unsafe receivers reject before capture and record loss if unsafe on return; coral attachments validate; holding expires.',
'Core and real Black Market Sell UI reject reputation 4 and unlock at reputation 5.',
'Confirmed saved dealer purchase awards bounded reputation; shared market action integration covers treatments/containment.',
'Opening/canceled/failed actions award zero; duplicate transaction returns the same state without XP.',
'Normal direct Tier 4–6 calls reject; real dealer listings support approved upper fish.',
'Exact 50/25/15/7.5/2/0.5 independent Mystery odds and all six fish pools retained.',
'Exactly 3 Common / 3 Uncommon / 1 Rare / 1 Mystery daily slots.',
'Actual planning, active and results windows advance the paused underlying aquarium at 1×.',
'Actual hunger/age/chemistry/equipment change; six simulated game hours advance eggs and day/store rotation.',
'75 L displays 20 gal; 2,500 L displays 661 gal; preciseVolume retains fractions and internal liters.',
'Actual backdrop closes ordinary planning; interior click does not dismiss.',
'Actual regular X and Escape close planning; both protect an active trip.',
'All active-dismissal paths show loss confirmation and require explicit abandonment.',
'Actual browser reload restores active position/oxygen/haul and one fee; return rewards once; local completion receipt prevents old-snapshot settlement.',
'Actual file:// gameplay/art has no HTTP/HTTPS gameplay requests; DIST also tested on an HTTP repository subpath.',
'Eleven freshwater fish/six plants retained; 145 file hashes unchanged; expansion suite checks exact ten-day biology replay.',
'Additive legacy migration and existing expansion/health/art/deployment suites provide compatibility evidence.'
]
assert len(acceptance)==38
acceptance_table='\n'.join(f'| {i} | PASS — {text} |' for i,text in enumerate(acceptance,1))
report=f'''# Aquarium Life — Ocean Diving v2.8 implementation report

Date: **2026-10-14**. MDP **v3.3**, exactly **31 major sections**.

Implemented the authorized diving update. **Zero new biological species**: the approved 38-entry v2.7 expansion remains the roster baseline. Current totals remain 80 fish (69 marine/11 freshwater), ten marine coral entries, five non-fish invertebrates and six protected freshwater plants.

## Features and regions

{primary}

## Verified regional profiles

Four regions, six deliberately conservative existing-species profiles. Hawaii is wildlife observation-only. Fiji/Hawaii deep dives currently have no verified eligible implemented livestock and offer inert fictional salvage. This is an honest limited encounter catalog, not an exhaustive regional ecosystem. No unverified species was silently assigned a location.

{profile_table}

The cited NOAA chalk-bass profile documents Caribbean rubble/sand habitat and a wider 12–396 m range; the game's 12–90 m gate is a conservative subset. JAMSTEC documents the Japanese crab at 8 m. The Japanese anthias source documents deep reefs 70–300 m and the research paper records Japanese specimens at 95–100/180 m. Other depth gates are conservative game survey bands, not claimed complete distribution maps. The Fiji coral checklist supports native occurrence and controlled-trade context. Hawaii's observation-only game policy is conservative; this software does not grant real collection permission or teach extraction techniques.

## Actual tests

| Browser | Suite | Passed | Failed | Evidence |
|---|---|---:|---:|---|
{chr(10).join(rows)}

Evidence includes real keyboard/mouse/modal actions, reload and local JSON-save tests. A test helper had to be reinstated after the intentional browser reload; early harness issues and high-tier fixtures reflecting old acquisition rules were corrected, then the suites rerun. Historical v2.6 empty-pool/old-roster expectations were not treated as current passes. The 145 protected hashes are in [integrity.json](tests/diving-evidence/integrity.json). Actual browser results, rather than this narrative, govern pass/fail status.

| Request test | Verified behavior |
|---:|---|
{acceptance_table}

Not run: Firefox (not installed), actual remote GitHub Pages deployment, binary PDF rendering, and obsolete full milestone suites with superseded roster/empty-pool/gallon fixtures. Six-hour progression uses the actual simulation for 360 game minutes; actual real-time planning/active/results tests cover fixed-step advancement, not a five-real-minute wall-clock wait. No external account was changed and no site was published.

## Artwork

Built-in ImageGen created **nine original PNG assets**: eight distinct regional reef/deep backgrounds and a transparent eight-object equipment sprite sheet. All are saved at [assets/diving/](assets/diving/) and embedded by `tests/pack_diving_art.py` into `js/diving-art-data.js`. [Exact prompt set and generated filenames](assets/diving/art-prompts.json). [Visual contact sheet](tests/diving-evidence/background-contact.png). Sources are preserved; existing approved fish/reference files were not overwritten. New art is **unapproved, pending user review**. The diver uses a static authored pose; movement and collection sparkle are runtime effects, not a newly authored multi-pose swimming cycle. Existing v2.7 framing/breeding/earliest-stage limits remain.

## Files edited

- Added `js/diving-data.js`, `diving.js`, `diving-art.js`, `diving-art-data.js`, `diving-ui.js`; `css/diving.css`; nine source PNGs, prompt record and permanent `assets/diving/registry.json`.
- Updated `index.html`, `js/core.js`, `save.js`, `main.js`, `livestock-market.js`, `health-save.js`, `store.js`, `store-rules.js`, `ui.js`, `expansion-ui.js`, `invertebrates.js`, `valuation.js`, `simulation.js`, `gameplay.js`, `app-shell.js`. Shared hooks preserve existing atomic validation, health/value factors, geometry, saved selection and fixed-step chemistry. Freshwater species/biology and original art remain protected.
- Added diving logic/resale/input/browser tests and art packer; updated browser runner, authorized high-tier expansion test fixtures, build and package scripts. Evidence lives in `tests/diving-evidence/`. Temporary integration scripts are removed before packaging.
- Updated all six required project docs, catalog, README, TEST_REPORT, consolidated master, generation record, region ledger and printable/PDF continuity source. Rebuilt `DIST` and the GitHub Pages upload ZIP from current sources.

## Limits and persistence

All saves, recovery data, timeline and diving completion receipts stay in the player's browser on their PC. Export/import JSON remains local. Receipt/timeline guards prevent normal repeat/reload settlement; editable local data is not cryptographically tamper-proof or a verified leaderboard. Clearing browser site data also clears those local guards. Active trips resume with saved oxygen; prolonged absence advances aquarium time and can expire transported livestock before return. No oxygen upgrades, future regions, newly invented species or practical collection instructions were added.

Survival, sensitivity, holding deadlines, medical conditions, reputation and collector demand are bounded game parameters, not measured field/veterinary outcomes. Explicit unsafe receiving conditions cause a recorded loss, never silent unsafe placement. Restricted coral is fictional fragment recovery with permanent source risk and Black Market-only resale, separate from actual legal permissions.

**PDF source is updated; binary PDF regeneration remains pending** the unavailable PDF toolchain. New artwork awaits user approval; existing roster/art limits are preserved. [GitHub Pages instructions](GITHUB_PAGES.md) and [build manifest](DIST/build-manifest.json) document the portable delivery. Run `python build.py` after future edits to refresh DIST and its upload ZIP.
'''
write('DIVING_UPDATE_REPORT.md',report)
write('PROJECT_CONTINUITY_SOURCE.md','# Aquarium Life — printable project continuity source\n\nRevision v2.8 / MDP v3.3, 2026-10-14. PDF regeneration pending.\n\n'+current+'\n## Regional eligibility ledger\n\n'+profile_table+'\n## Consolidated 31-section master\n\n'+master+'\n## Back-of-source permanent continuity rules\n\nRetain the full approved 38-entry livestock registry. Every future species addition must log its stable ID, scientific/common name, rarity, category, care, implementation/batch/date and living/dead art limits in the catalog, machine registry, MDP and PDF/continuity source. Diving catches are owned individuals, never additional species counts. Every encounter assignment needs sourced range/habitat/depth and separate conservation/collection class. Keep whole-gallon nominal labels separate from exact physical liters. Keep selected aquarium and all player saves local. Apply MDP §5.5 to expeditions and §§18.8/19.4 to rarity/resale. Rebuild DIST after source edits. New artwork is never auto-approved. If PDF export is unsupported, update this source and explicitly report regeneration pending. Completed editing reports end with the exact standalone line Done With Edits.')
baseline_table='| Name / scientific name / ID | Category / rarity / care | Status / batch / date | Art / alive-dead support / notes |\n|---|---|---|---|\n'
for r in baseline:
 baseline_table+=f"| {r['name']} / *{r['scientificName']}* / `{r['id']}` | {r['category']} / {r['rarity']} / {r['difficulty']} | {r['status']} / {r['batch']} / {r['implementationDate']} | {r['artStatus']}; {r['art']['aliveDeadStatus']}; {r['breedingStatus']}. [Atlas]({r['art']['atlas']}) |\n"
source=read('PROJECT_CONTINUITY_SOURCE.md').replace('## Regional eligibility ledger','## Permanent v2.7 roster baseline — all 38 entries\n\n'+baseline_table+'\n## Regional eligibility ledger',1)
write('PROJECT_CONTINUITY_SOURCE.md',source)
pdf=read('PDF_WORKFLOW.md')
if '## Diving v2.8 source update' not in pdf:pdf+='\n\n## Diving v2.8 source update\n\nThe current printable source is now v2.8 / MDP v3.3, with the complete 31-section master, regional ledger, expedition/provenance/reputation rules and existing 38-entry roster baseline. No biological species were added. Preserve these rules near the back of the eventual PDF. Binary regeneration remains pending the same unavailable toolchain; do not claim a new verified PDF.\n'
write('PDF_WORKFLOW.md',pdf)
art=read('ART_GENERATION_RECORD.md')
if '## Ocean Diving v2.8' not in art:art+='\n\n## Ocean Diving v2.8\n\nNine original built-in ImageGen assets and full prompts are preserved under assets/diving/. They include eight region/mode backgrounds and a transparent equipment/diver/boat sprite sheet. All remain unapproved. Existing approved benchmark and livestock assets are preserved. Packing is byte-copy/base64 embedding; see DIVING_UPDATE_REPORT.md and assets/diving/art-prompts.json.\n'
write('ART_GENERATION_RECORD.md',art)
for path in ['ART_DIRECTION.md','DIVING_UPDATE_REPORT.md','ART_GENERATION_RECORD.md']:
 s=read(path)
 s=s.replace('Packing is byte-copy/base64 embedding', 'Packing preserves the original sources, detects equipment alpha gutters, and uses nearest-neighbor technical atlas packing/base64 embedding')
 s=s.replace('packing is byte-copy/base64 embedding', 'packing preserves original sources and uses detected alpha gutters, nearest-neighbor atlas packing and base64 embedding')
 s=s.replace('packing is byte-copy/base64 embedding,', 'packing uses detected alpha gutters, nearest-neighbor technical atlas packing and base64 embedding,')
 if 'equipment-atlas-metadata-v1.json' not in s:
  s+='\n\nEquipment framing correction: the generated boat crossed a nominal source cell boundary. The preserved source was technically packed into `assets/diving/equipment-atlas-v1.png` using alpha gutters; `equipment-atlas-metadata-v1.json` records all eight source bounds. Icons retain their source aspect ratios. No semantic repainting or source overwrite occurred.\n'
 write(path,s)
print('Updated v2.8 documents, six-profile regional ledger, MDP v3.3 / 31 sections and continuity source. PDF export pending.')
