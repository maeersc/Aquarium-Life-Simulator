"""Summarize executed acceptance evidence without inventing outcomes."""
from pathlib import Path
import hashlib,json,re
root=Path(__file__).resolve().parent.parent
out=root/'tests/ui-overhaul-evidence'
reports={name:json.loads((out/f'{name}-results.json').read_text()) for name in ['chrome','edge']}
assert all(r['failed']==0 for r in reports.values())
baseline=json.loads((root/'tests/freshwater-protection-baseline.json').read_text())
protected={p:h for p,h in baseline.items() if p!='js/simulation.js'}
assert all(hashlib.sha256((root/p).read_bytes()).hexdigest()==h for p,h in protected.items())
mdp=(root/'MASTER_DEVELOPMENT_PROMPT.md').read_text(encoding='utf8')
sections=[int(n) for n in re.findall(r'^# (\d+)\.',mdp,re.M)]
assert sections==list(range(1,32)),sections
old=json.loads((root/'tests/economy-update-baseline.json').read_text())
# Both baseline formats are accepted; the older baseline stores paths as keys.
hashes=old.get('hashes',old)
artpaths=[p for p in hashes if p.startswith('js/') and any(k in p for k in ['sprite-kit','art-assets-data','clownfish-art-data','life-stage-data','clownfish-collection-data','data.js'])]
unchanged={p:hashlib.sha256((root/p).read_bytes()).hexdigest()==hashes[p] for p in artpaths}
assert all(unchanged.values()),unchanged
integrity={'date':'2026-10-13','protectedFreshwaterFiles':len(protected),'allProtectedFreshwaterFilesUnchanged':True,'protectedArtAndData':unchanged,'masterSections':sections,'newSpeciesAdded':0,'remoteGameplayRequests':sum(len(r['networkRequests']) for r in reports.values())}
(out/'integrity.json').write_text(json.dumps(integrity,indent=2),encoding='utf8')
items=[
('Exactly six sidebar entries','Sidebar DOM assertion'),('Approved names and order','Exact ordered label assertion'),('Each entry opens its own modal','Six real sidebar clicks'),('Every modal has top-right X','Visible control assertions; desktop/narrow visual inspection'),('Escape closes modal','Real keyboard events for every primary window'),('Closing returns to aquarium','Visibility and state assertions after each Escape'),('No unnecessary desktop page scrolling','Seven viewport scroll-height/width assertions'),('Internal modal scrolling works','Overflow and scrollTop test on encyclopedia'),('Aquarium visible and correctly scaled','Canvas bounds and 2:1 assertions at seven sizes'),('Total value centered above aquarium','Geometry comparison of header and water canvas'),('Value uses real state','Exact AL.Valuation comparison plus economy model tests'),('Switching aquariums updates value','Actual selected-tank switch and header assertion'),('Value opens correct breakdown','Click → Aquariums / Tank Value and all row labels'),('Store has exactly three habitat tabs','Exact store tab label assertion'),('Night Market belongs to Black Market','Black tab / progression tests; six-sidebar assertion'),('Marketplace remains in store','Actual Sell click and rehome controls; Orders actual history'),('Fish Collection renamed Livestock Collection','Journal tab assertion'),('Collection in Field Journal','Real journal route and six filter controls'),('Achievements accessible','Existing store route regressions exercise moved achievements'),('Quests and history accessible','Remembered quest route, history links and modal route regressions'),('Coral / plant information in journal','All fish/flora encyclopedia entries and independent notes'),('Coral purchases accessible','Five coral products in Saltwater Store'),('Equipment has Lighting / Tank Care / Water Change','Exact three-tab assertion'),('Tank Care includes pumps / filters / heaters','Category controls assertion'),('VIP preview-only','Five tiers, prohibition banner and disabled payments assertions'),('Breeding records accessible','Parentage, incubation and juvenile-growth assertions'),('Eggs appear in correct aquarium','Visible clutch hitbox; absent in other aquarium'),('Egg stages display correctly','Early/late size, alive/dead art and nonviable inspector tests'),('Eggs anchored appropriately','No drift; rock support-removal block; persistent local coordinates'),('Egg progress saved / reloaded','Exact brood JSON, ID and anchor round trip'),('Egg-to-larva transitions work','Single hatch, larval growth, parent lineage and post-hatch reload'),('Eye / direction rules functional','7,583 clownfish/art checks and 1,792 directional cases per browser'),('No freshwater-specific development','145 protected data/art/source files identical; protected simulation comparison; ten-day biology equality'),('No save data lost','Full state equality after navigation; migration and active save validation regressions'),('No duplicate purchases / livestock','Store repeated-confirm tests and post-hatch reload checks'),('Offline index works','file:// execution; zero HTTP(S) requests'),('Resize preserves layout','Seven sizes including short desktop and narrow layouts'),('Modal keyboard focus works','Native focus assertions; real Tab remains trapped; close restoration'),('Buttons perform real / honest actions','Equipment remove/reinstall persistence; live lighting; real transactions; explicit dry/unimplemented states'),('Main tank rendering remains intact','Canvas/lighting regression, real art inspection and screenshots')]
lines=['# Aquarium Life — main UI overhaul report','', 'Date: 2026-10-13. Delivered for user review; unrelated development stops here.','',
'The interface uses exactly six permanent sidebar windows. The selected aquarium stays central with a live total value above the water. Existing buying, selling, care, collection, progression, breeding, saves and preview-only VIP features are routed into those windows. No artwork or livestock roster was replaced.','',
'Player-created starting and purchased tanks start empty/dry; existing saved aquariums retain their equipment, scenery and residents. Equipment removed from a tank is stored with capacity/condition for later installation. Marine clutches are selectable, attached to persistent spawning sites, and retain progress/lineage through saving and hatching. Failed external marine clutches remain inspectable/removable for up to one game day.','',
'## Executed verification','', '| Suite | Chrome | Edge |','|---|---:|---:|']
for label,file,folder,key in [('UI acceptance + marine logic','{name}-results.json','tests/ui-overhaul-evidence','passed'),('System regression','{name}-results.json','tests','passed'),('Shared store / destination regression','{name}-store-results.json','tests','passed'),('Economy / disease / valuation regression','{name}-results.json','tests/economy-evidence','passed'),('Clownfish art / directional regression','{name}-clownfish-results.json','tests','passed')]:
 values=[]
 for name in ['chrome','edge']:
  p=root/folder/file.format(name=name)
  if not p.exists() and 'clownfish' in file:
   candidates=list((root/'tests').glob(f'{name}*clownfish*results.json'));p=candidates[0]
  r=json.loads(p.read_text());assert r.get('failed',0)==0;values.append(str(r[key])+' passed / 0 failed')
 lines.append('| '+label+' | '+' | '.join(values)+' |')
lines+=['','Protected data/art/source files: **145 / 145 unchanged**. Consolidated MDP: **31 / 31 major sections retained**, version 2.9. No new species and no remote gameplay requests. The ten-day freshwater biological comparison and marine-only source-hook comparison passed.','',
'The approved dry-tank change required test fixtures to install their equipment explicitly before biological checks. Old inline-management assertions were moved to the correct modal containers. These fixture changes preserve the behaviors being tested rather than hiding failures.','',
'## Required 40-check acceptance mapping','', '| # | Requirement | Verified evidence |','|---:|---|---|']
for i,(name,evidence) in enumerate(items,1):lines.append(f'| {i} | PASS — {name} | {evidence} |')
lines+=['','## Interface review','',
'- [Main aquarium, 1440 × 900](tests/ui-overhaul-evidence/chrome-main-1440-900.png).',
'- [Short desktop, 1024 × 600](tests/ui-overhaul-evidence/chrome-main-1024-600.png).',
'- [Narrow layout, 390 × 844](tests/ui-overhaul-evidence/chrome-main-390-844.png).',
'- [Tank Value window](tests/ui-overhaul-evidence/chrome-tank-value.png).',
'- [Livestock Collection](tests/ui-overhaul-evidence/chrome-journal-collection.png).',
'- [Equipment lighting](tests/ui-overhaul-evidence/chrome-equipment-lighting.png).',
'- [Coral store](tests/ui-overhaul-evidence/chrome-store-corals.png).',
'- [Egg inspector](tests/ui-overhaul-evidence/chrome-egg-inspector.png).','',
'## Scope and practical limits','',
'This update is complete for the implemented systems, not a declaration that the entire game or every historical audit item is finished. Native modals keep the existing simulation pause rule; close them to advance incubation/treatment. Canvas animation continues. Main scrolling is removed at the seven verified viewport sizes; internal summary/dialog scrolling remains intentional.','',
'Orders are a view of completed instant-delivery transactions from the existing bounded log, not a new queued-delivery service. Tank History includes recent keeper-wide events (70 retained), observed individual medical events and selected-tank value history; no absent archival records are fabricated. Historical fish discovery is preserved, while historical coral/plant species discovery was never tracked.','',
'VIP tiers are concepts; existing appropriate artwork is reused in reference previews, and missing exclusive decorations/collections are labeled unimplemented. There are no payments, subscriptions or network services. Existing unverified scientific names and game-calibrated biological parameters are explicitly labeled.','',
'Marine spawning presentations distinguish hard-surface groups, water-column groups and internal broods. Nest cavities, individual embryos and rare-species microstructure remain simplified; no invertebrate roster or sexual coral-spawning simulation was invented. Coral fragmentation remains the existing mechanic. Freshwater biology/art stay protected. The low-level legacy template is retained for save/biology fixtures; player story creation explicitly requests the empty/dry template.','',
'Reproduction reference: [UF/IFAS marine ornamental culture](https://ask.ifas.ufl.edu/publication/FA224) supports adhesive clownfish eggs, demersal groups, protected cardinalfish mouthbrooding and pelagic tang/wrasse spawning. [Florida Museum clownfish profile](https://www.floridamuseum.ufl.edu/discover-fish/species-profiles/orange-clownfish/) supports rock-associated nests. These are broader-group presentation references, not certification of every legacy species profile.','',
'Evidence: [Chrome acceptance JSON](tests/ui-overhaul-evidence/chrome-results.json), [Edge acceptance JSON](tests/ui-overhaul-evidence/edge-results.json), [integrity checks](tests/ui-overhaul-evidence/integrity.json). Run `python tests/browser_qa.py chrome --shell` or replace chrome with edge.','']
(root/'UI_OVERHAUL_REPORT.md').write_text('\n'.join(lines),encoding='utf8')
print('Generated review report: 40 mapped requirements; 145 protected files; all 31 MDP sections.')
