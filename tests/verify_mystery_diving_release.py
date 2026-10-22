"""Verify current mystery release, full continuity, immutable assets and archives."""
from pathlib import Path
from zipfile import ZipFile
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parent.parent
checks=[]
def ck(name,ok):
 checks.append({'name':name,'pass':bool(ok)})
 if not ok:raise AssertionError(name)
def read(p):return (ROOT/p).read_text(encoding='utf8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
m=read('MASTER_DEVELOPMENT_PROMPT.md');c=read('PROJECT_CONTINUITY_SOURCE.md')
old_m=read('planning/mystery-diving/baseline/MASTER_DEVELOPMENT_PROMPT.md');old_c=read('planning/mystery-diving/baseline/PROJECT_CONTINUITY_SOURCE.md')
rule='Every valid Reef Diving and Deep Sea Diving expedition must provide at least one reachable mystery fish encounter. Its species is concealed using a question-mark silhouette until successful return to the boat. Geographic eligibility, inventory, oxygen, post-dive survival, and save persistence remain mandatory.'
ck('Full 31-section MDP v4.2 is embedded verbatim in continuity',len(re.findall(r'^# \d+\.',m,re.M))==31 and 'VERSION 4.2' in m and m in c)
primary=m[m.index('## 5.5 '):m.index('## 5.6 ')]
ck('Permanent rule appears exactly once in primary diving section',rule in primary and m.count(rule)==1)
ck('Expanded exploration remains future documentation only','concept only' in m and 'no expanded exploration system' in m.lower())
old_prefix=old_c[:old_c.index(old_m)];prefix=c[:c.index(m)];rows=[x for x in old_prefix.splitlines() if x.startswith('|')]
ck('All previous 38/35 roster ledger rows remain intact',len(rows)>=73 and all(x in prefix for x in rows))
for a,b in [('## 15.1 ','# 16.'),('## 9.12 ','# 10.'),('## 10.4 ','# 11.')]:
 ck('Existing breeding authority preserved: '+a,m[m.index(a):m.index(b)]==old_m[old_m.index(a):old_m.index(b)])
ck('Original genetics implementation unchanged',sha(ROOT/'js/patterns.js')==sha(ROOT/'planning/automatic-breeding/baseline/patterns.js'))
manifest=json.loads(read('DIST/build-manifest.json'))
ck('Current DIST version and device-local save policy',manifest['gameContent']=='v3.9' and 'no server saves' in manifest['savePolicy'])
ck('New module and rules/report are deployed',all(n in {r['path'] for r in manifest['files']} for n in ['js/diving-mystery.js','MYSTERY_DIVING_RULES.md','MYSTERY_DIVING_UPDATE_REPORT.md']))
for row in manifest['files']:
 p=ROOT/row['path'];q=ROOT/'DIST'/row['path'];ck('Source/DIST SHA-256: '+row['path'],p.is_file() and q.is_file() and sha(p)==row['sha256']==sha(q))
ck('Exact manifest file and byte counts',len(manifest['files'])==manifest['sourceFiles'] and sum(r['bytes'] for r in manifest['files'])==manifest['sourceBytes'])
before=json.loads(read('planning/mystery-diving/before-build-manifest.json'));assets=[r for r in before['files'] if r['path'].startswith('assets/') and r['path']!='assets/diving/registry.json']
ck('All '+str(len(assets))+' prior raster/art assets are byte-identical',all(sha(ROOT/r['path'])==r['sha256'] for r in assets))
prior=json.loads(read('planning/mystery-diving/baseline/registry.json'));current=json.loads(read('assets/diving/registry.json'))
ck('Existing regions/modes and six encounter profiles remain unchanged',prior['regions']==current['regions'] and prior['modes']==current['modes'] and prior['species']==current['species'][:len(prior['species'])])
ck('Exactly two already implemented Fiji profiles, zero added species',len(current['species'])==8 and {p['id'] for p in current['species'][6:]}=={'forcipiger-flavissimus','exquisite-fairy-wrasse'})
with ZipFile(ROOT/'AquariumLife-GitHub-Pages.zip') as z:
 ck('Pages ZIP CRC passes',z.testzip() is None)
 ck('Pages ZIP starts at deployment root','index.html' in z.namelist() and '.nojekyll' in z.namelist() and not any(n.startswith('DIST/') for n in z.namelist()))
 ck('Pages ZIP exactly matches current DIST',set(z.namelist())=={p.relative_to(ROOT/'DIST').as_posix() for p in (ROOT/'DIST').rglob('*') if p.is_file()} and all(z.read(n)==(ROOT/'DIST'/n).read_bytes() for n in z.namelist()))
suites=['mystery-diving-evidence/chrome-results.json','mystery-diving-evidence/edge-results.json','diving-evidence/edge-results.json','breeding-evidence/chrome-results.json','heater-evidence/edge-results.json','store-casino-evidence/edge-results.json','pages-evidence/chrome-results.json','pages-evidence/edge-results.json']
results=[]
for name in suites:
 r=json.loads(read('tests/'+name));ck('Passed acceptance suite: '+name,r['failed']==0);results.append({'file':name,'passed':r['passed'],'failed':r['failed']})
 if name.startswith('pages-evidence/'):
  ck('Pages evidence includes current v3.9 mystery runtime: '+name,any(x['name'].startswith('Built v3.9 mystery authority') and x['pass'] for x in r['results']))
if '--source-archive' in sys.argv:
 with ZipFile(ROOT/'AquariumLife-v0.1.zip') as z:
  ck('Source ZIP CRC passes',z.testzip() is None)
  ck('Source ZIP includes current feature, full master and release evidence',all('AquariumLife/'+n in z.namelist() for n in ['js/diving-mystery.js','MASTER_DEVELOPMENT_PROMPT.md','PROJECT_CONTINUITY_SOURCE.md','MYSTERY_DIVING_RULES.md','MYSTERY_DIVING_UPDATE_REPORT.md','tests/mystery-diving-evidence/release-validation.json']))
  ck('No browser profile or cache in source ZIP',not any('profile' in n or '__pycache__' in n for n in z.namelist()))
  ck('Every source ZIP byte equals current workspace source',all(n.startswith('AquariumLife/') and z.read(n)==(ROOT/n[len('AquariumLife/'):]).read_bytes() for n in z.namelist()))
report={'passed':len(checks),'failed':0,'suiteAssertions':sum(x['passed'] for x in results),'suites':results,'deployment':{k:manifest[k] for k in ['builtAt','gameContent','sourceFiles','sourceBytes']},'unchangedAssets':len(assets),'checks':checks}
if '--check-only' not in sys.argv:(ROOT/'tests/mystery-diving-evidence/release-validation.json').write_text(json.dumps(report,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k!='checks'},indent=2))
