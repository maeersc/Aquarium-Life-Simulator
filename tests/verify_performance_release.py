"""Check performance changes, protected authorities and final release bytes."""
from pathlib import Path
from zipfile import ZipFile
import json,hashlib,re,sys
r=Path(__file__).resolve().parents[1];checks=[]
def ck(name,condition):checks.append({'name':name,'pass':bool(condition)})
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
baseline=json.loads((r/'planning/performance-optimization/baseline/hashes.json').read_text())
allowed={'index.html','js/main.js','js/render.js','js/fish-animation.js','js/sprite-kit.js','js/ui.js','js/save.js','js/diving-ui.js','js/casino-ui.js','js/livestock-animation-data.js','css/ui-cleanup.css'}
changed=[]
for name,old in baseline.items():
 actual=sha(r/name)
 if actual!=old:changed.append(name)
 ck('Preserved pre-optimization runtime authority or explicitly scoped edit: '+name,actual==old or name in allowed)
protected=json.loads((r/'tests/tutorial-audit-evidence/protected-runtime.json').read_text())['sha256']
assets={n:v for n,v in protected.items() if n.startswith('assets/')}
for name,old in assets.items():ck('Original asset unchanged: '+name,sha(r/name)==old)
manifest=json.loads((r/'DIST/build-manifest.json').read_text())
ck('Current release version and local-only save policy',manifest['gameContent']=='v4.3.0' and 'localStorage' in manifest['savePolicy'] and 'no server saves' in manifest['savePolicy'])
ck('DIST excludes obsolete native startup banks',not any('livestock-animation-sheets-' in row['path'] for row in manifest['files']))
with ZipFile(r/'AquariumLife-GitHub-Pages.zip') as z:
 ck('Pages ZIP CRC and root index',z.testzip() is None and 'index.html' in z.namelist() and not any(n.startswith(('DIST/','tests/')) for n in z.namelist()))
 for row in manifest['files']:
  name=row['path'];ck('Exact source / DIST / Pages bytes: '+name,sha(r/name)==row['sha256']==sha(r/'DIST'/name)==hashlib.sha256(z.read(name)).hexdigest())
 ck('Exact Pages manifest',z.read('build-manifest.json')==(r/'DIST/build-manifest.json').read_bytes())
master=(r/'MASTER_DEVELOPMENT_PROMPT.md').read_text(encoding='utf8');continuity=(r/'PROJECT_CONTINUITY_SOURCE.md').read_text(encoding='utf8')
ck('31 complete master sections and exact embedded continuity',len(re.findall(r'^# \d+\. ',master,re.M))==31 and continuity.count(master)==1)
suites=[]
for file in ['performance-evidence/chrome-after.json','sprite-production-evidence/chrome-results.json','sprite-production-evidence/edge-results.json','tutorial-audit-evidence/chrome-results.json','equipment-reliability-evidence/chrome-results.json','economy-update-evidence/edge-results.json','pages-evidence/edge-results.json','breeding-evidence/chrome-results.json']:
 d=json.loads((r/'tests'/file).read_text(encoding='utf8'));rows=d.get('checks',d.get('results',[]));passed=d.get('passed',sum(bool(x['pass']) for x in rows));failed=d.get('failed',sum(not x['pass'] for x in rows));ck('Passing executed suite '+file,failed==0);suites.append({'file':file,'passed':passed,'failed':failed})
 if file=='performance-evidence/chrome-after.json':
  for name,digest in d['runtimeSHA256'].items():ck('Final performance run used current runtime: '+name,sha(r/name)==digest)
  ck('Final performance targeted DIST',d.get('entry')=='DIST/index.html')
  modes={x['label']:x for x in d['rows']};ck('30 and60FPS modes measured',28<=modes['H-30']['fps']<=31 and 55<=modes['H-60']['fps']<=61)
  ck('Hidden and covered aquarium drawing stopped',all(modes[k]['draws']==0 for k in ['store','journal','equipment','casino','settings','G-hidden']))
soak=json.loads((r/'tests/performance-evidence/chrome-soak.json').read_text());ck('Five-minute DIST soak completed with all checks passing',soak['entry']=='DIST/index.html' and soak['wallSeconds']>=300 and all(x['pass'] for x in soak['checks']));suites.append({'file':'performance-evidence/chrome-soak.json','passed':sum(x['pass'] for x in soak['checks']),'failed':sum(not x['pass'] for x in soak['checks'])})
if '--source-archive' in sys.argv:
 with ZipFile(r/'AquariumLife-v0.1.zip') as z:
  ck('Source ZIP CRC and no browser profiles',z.testzip() is None and not any('profile' in n or '__pycache__' in n for n in z.namelist()))
  for name in z.namelist():ck('Exact source archive byte: '+name,(r/name.removeprefix('AquariumLife/')).read_bytes()==z.read(name))
result={'passed':sum(x['pass'] for x in checks),'failed':sum(not x['pass'] for x in checks),'checks':checks,'runtimeEdits':changed,'unchangedOriginalAssets':len(assets),'suites':suites,'suiteAssertions':sum(x['passed'] for x in suites),'build':{k:manifest[k] for k in ['builtAt','gameContent','sourceFiles','sourceBytes']}}
if '--check-only' not in sys.argv:(r/'tests/performance-evidence/release-validation.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k not in ['checks']}|{'failures':[x for x in checks if not x['pass']]},indent=2))
raise SystemExit(int(result['failed']>0))
