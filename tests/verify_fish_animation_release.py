"""Verify original art/biology preservation, coverage evidence and current packages."""
from pathlib import Path
from zipfile import ZipFile
import hashlib,json,re,sys
r=Path(__file__).resolve().parents[1];checks=[]
def read(n):return (r/n).read_text(encoding='utf8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ck(n,v):
 checks.append({'name':n,'pass':bool(v)})
 if not v:raise AssertionError(n)
b=r/'planning/fish-animation/baseline';hashes=json.loads((b/'hashes.json').read_text(encoding='utf8'))
changed={'js/render.js','js/expansion-art.js'}
preserved=[n for n in hashes if n not in changed]
ck('All original bitmap/registry/biology/save/economy/genetics authorities are unchanged',all(sha(r/n)==hashes[n] for n in preserved))
for n in ['js/core.js','js/simulation.js','js/breeding.js','js/save.js','js/patterns.js','js/finance.js','js/store-rules.js','js/livestock-health.js','js/diving.js','js/diving-mystery.js','js/diving-receiving.js']:
 ck('Exact protected gameplay authority '+n,sha(r/n)==hashes[n])
data=json.loads(read('assets/animation/fish-registry.json'));before=json.loads(read('tests/fish-animation-evidence/before.json'))
ck('Every one of the original 94 registered marine fish is explicitly mapped',set(data['species'])=={x['id'] for x in before} and len(before)==94)
ck('No invented extra biological IDs or counted designer varieties',len(data['species'])==94 and len(data['referenceOnly'])==5)
ck('Original static/partial audit is based on real frame counts',sum(x['adultFrames']==1 for x in before)==63 and sum(x['adultFrames']>1 for x in before)==31)
ck('Banggai early display retains developed-release anatomy mapping',data['species']['banggai']['artStages']['baby']=='juvenile')
ck('Recorded filefish source-art exclusion is narrowly defined',data['species']['orange-spotted-filefish']['sourceMasks']['juvenile'][0]['y']==110)
ck('New living eye registration covers 25 fish times three stages plus one repaired anchor',sum(len(x.get('eyes',{})) for x in data['species'].values())==76)
m=read('MASTER_DEVELOPMENT_PROMPT.md');continuity=read('PROJECT_CONTINUITY_SOURCE.md')
ck('Updated 31-section master is embedded verbatim',m in continuity and len(re.findall(r'^# \d+\.',m,re.M))==31)
ck('Permanent animation rules live in the primary art section','## 3.14 Global saltwater fish animation' in m[m.index('# 3. OFFICIAL'):m.index('# 4. WORLD')])
old_m=(b/'MASTER_DEVELOPMENT_PROMPT.md').read_text(encoding='utf8');old_c=(b/'PROJECT_CONTINUITY_SOURCE.md').read_text(encoding='utf8');rows=[x for x in old_c[:old_c.index(old_m)].splitlines() if x.startswith('|')]
ck('Original 38/35 livestock continuity ledger rows remain intact',len(rows)>=73 and all(x in continuity[:continuity.index(m)] for x in rows))
report=read('FISH_ANIMATION_AUDIT.md')
ck('All 94 marine fish have coverage rows and conservative B status',all(f'[`{x["id"]}`]' in report for x in before) and report.count('→ **B**')==94)
ck('No false fully-animated species claim', '| A — fully authored/working across the requested lifecycle/action scope | 0 | 0 |' in report)
manifest=json.loads(read('DIST/build-manifest.json'));paths={x['path'] for x in manifest['files']}
ck('Current release/runtime/review/reports deployed',manifest['gameContent']=='v4.0.3' and {'js/fish-animation.js','js/fish-animation-data.js','assets/animation/fish-registry.json','FISH_ANIMATION_AUDIT.md','FISH_ANIMATION_SYSTEM.md','fish-animation-review.html'}<=paths)
ck('Saves remain local without server saving','no server saves' in manifest['savePolicy'])
for item in manifest['files']:ck('Source/DIST '+item['path'],sha(r/item['path'])==item['sha256']==sha(r/'DIST'/item['path']))
ck('Manifest totals are exact',len(manifest['files'])==manifest['sourceFiles'] and sum(x['bytes'] for x in manifest['files'])==manifest['sourceBytes'])
with ZipFile(r/'AquariumLife-GitHub-Pages.zip') as z:
 ck('Pages ZIP CRC passes',z.testzip() is None)
 ck('Pages ZIP contains exactly current DIST bytes at its root',set(z.namelist())=={p.relative_to(r/'DIST').as_posix() for p in (r/'DIST').rglob('*') if p.is_file()} and all(z.read(n)==(r/'DIST'/n).read_bytes() for n in z.namelist()))
suites=[]
for file in ['fish-animation-evidence/chrome-results.json','fish-animation-evidence/edge-results.json','pages-evidence/chrome-results.json','pages-evidence/edge-results.json','breeding-evidence/chrome-results.json']:
 d=json.loads(read('tests/'+file));ck('Passed actual suite '+file,d['failed']==0);items=d.get('checks',d.get('results'))
 if file.startswith('fish-animation-evidence'):
  ck('All species and three stages actually covered '+file,len(d['coverage'])==94 and all(len(x['stages'])==3 for x in d['coverage']))
  ck('Every source head/eye/fin/clip and native-scale caudal assertion is actually passing '+file,all(all(s[k] for k in ['source','dead','eye','tail','fin','transparent','headPreserved','sceneTail','sceneFin']) for x in d['coverage'] for s in x['stages']))
  ck('Four unresolved early outer-fin layers are explicitly disclosed, not falsely animated '+file,sum(bool(s.get('sceneArtGap')) for x in d['coverage'] for s in x['stages'])==4 and all(not s['sceneOuterFin'] for x in d['coverage'] for s in x['stages'] if s.get('sceneArtGap')))
  ck('Rendering rates leave equal simulation states '+file,d['frameRateComparison']['sameBeforeSimulation'] and not d['frameRateComparison']['differences'])
  ck('Freshwater renderer differential is tested '+file,any(x['name']=='Protected freshwater renderer matches the pre-upgrade engine pixel-for-pixel' and x['pass'] for x in items))
 if file.startswith('pages-evidence'):
  ck('Built served animation module actually tested '+file,any(x['name']=='Built marine animation profiles cover every current fish' and x['pass'] for x in items))
  ck('Every new marine eye/direction model check runs on served DIST '+file,sum('correct original eye pixels render facing' in x['name'] and x['pass'] for x in items)==564)
 suites.append({'file':file,'passed':d['passed'],'failed':d['failed']})
if '--source-archive' in sys.argv:
 with ZipFile(r/'AquariumLife-v0.1.zip') as z:
  ck('Source ZIP CRC passes',z.testzip() is None)
  ck('Source ZIP includes motion authority, audit and evidence',all('AquariumLife/'+n in z.namelist() for n in ['js/fish-animation.js','FISH_ANIMATION_AUDIT.md','tests/fish-animation-evidence/release-validation.json']))
  ck('Source ZIP excludes private profiles/caches',not any('profile' in n or '__pycache__' in n for n in z.namelist()))
  ck('Source ZIP bytes are current',all(n.startswith('AquariumLife/') and z.read(n)==(r/n[len('AquariumLife/'):]).read_bytes() for n in z.namelist()))
result={'passed':len(checks),'failed':0,'browserAssertions':sum(x['passed'] for x in suites),'suites':suites,'preservedFiles':len(preserved),'classification':{'A':0,'B':94,'C':0,'D':0,'E_referenceOnly':5},'deployment':{k:manifest[k] for k in ['builtAt','gameContent','sourceFiles','sourceBytes']}}
if '--check-only' not in sys.argv:(r/'tests/fish-animation-evidence/release-validation.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result,indent=2))
