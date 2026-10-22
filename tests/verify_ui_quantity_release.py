"""Check the actual built deliverables, protected originals and current QA evidence."""
from pathlib import Path
from zipfile import ZipFile
import hashlib,json,re,sys

R=Path(__file__).resolve().parents[1];checks=[]
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def ck(label,condition):checks.append({'name':label,'pass':bool(condition)})

m=(R/'MASTER_DEVELOPMENT_PROMPT.md').read_text(encoding='utf8');continuity=(R/'PROJECT_CONTINUITY_SOURCE.md').read_text(encoding='utf8')
ck('31 consolidated master homes retained',len(re.findall(r'^# \d+\.',m,re.M))==31)
ck('Exact master is embedded once in continuity',continuity.count(m)==1)
for rule,home in [('Store Quantity Rule:','18.'),('UI Background Rule:','26.'),('UI Preservation Rule:','26.')]:
 i=m.index(rule);heading=list(re.finditer(r'^# (\d+)\.',m[:i],re.M))[-1].group(1)
 ck(rule+' has one relevant authoritative home',m.count(rule)==1 and heading+'.'==home)
protected=json.loads((R/'tests/tutorial-audit-evidence/protected-runtime.json').read_text(encoding='utf8'))['sha256']
assets={p:h for p,h in protected.items() if p.startswith('assets/')}
for p,h in assets.items():ck('Original protected asset unchanged: '+p,(R/p).is_file() and sha(R/p)==h)
baseline=json.loads((R/'planning/performance-optimization/baseline/hashes.json').read_text())
for p in ['js/data.js','js/simulation.js','js/offline.js','js/thermal.js','js/breeding.js','js/progression.js','js/aquarium-preparation.js','js/diving-receiving.js','js/diving.js','js/casino.js','js/update29.js']:
 ck('Biology/economy authority unchanged: '+p,sha(R/p)==baseline[p])
ck('Local SVG is small, static and downward',(R/'assets/ui/downward-scales.svg').stat().st_size<1024 and 'Q0 32 16 0' in (R/'assets/ui/downward-scales.svg').read_text())
manifest=json.loads((R/'DIST/build-manifest.json').read_text());ck('Current game version in build manifest',manifest['gameContent']=='v4.3.1')
for row in manifest['files']:
 p=row['path'];ck('DIST exact source: '+p,sha(R/p)==row['sha256']==sha(R/'DIST'/p))
with ZipFile(R/'AquariumLife-GitHub-Pages.zip') as z:
 ck('Pages ZIP CRC',z.testzip() is None);names=set(z.namelist());files={p.relative_to(R/'DIST').as_posix():p for p in (R/'DIST').rglob('*') if p.is_file()}
 ck('Pages ZIP contains exact DIST paths',names==set(files) and 'index.html' in names and '.nojekyll' in names)
 for p,f in files.items():ck('Pages ZIP exact bytes: '+p,hashlib.sha256(z.read(p)).hexdigest()==sha(f))
suites=[]
for p in ['tests/ui-quantity-evidence/chrome-results.json','tests/ui-quantity-evidence/edge-results.json','tests/tutorial-audit-evidence/chrome-results.json','tests/economy-update-evidence/chrome-results.json','tests/equipment-reliability-evidence/chrome-results.json','tests/pages-evidence/edge-results.json']:
 d=json.loads((R/p).read_text(encoding='utf8'));ck('Executed suite has no failures: '+p,d['failed']==0 and d['passed']>0);suites.append({'path':p,'passed':d['passed'],'failed':d['failed']})
 if 'ui-quantity' in p:
  for f,h in d['runtimeSha256'].items():ck('Quantity suite tested current bytes: '+p+':'+f,sha(R/f)==h)
perf=json.loads((R/'tests/performance-evidence/chrome-checks.json').read_text());ck('Performance regressions pass',all(x['pass'] for x in perf));suites.append({'path':'tests/performance-evidence/chrome-checks.json','passed':sum(x['pass'] for x in perf),'failed':sum(not x['pass'] for x in perf)})
if '--source-archive' in sys.argv:
 with ZipFile(R/'AquariumLife-v0.1.zip') as z:
  ck('Portable source ZIP CRC',z.testzip() is None);names=set(z.namelist())
  for info in z.infolist():
   relative=info.filename.removeprefix('AquariumLife/');p=R/relative
   ck('Portable source ZIP exact bytes: '+relative,p.is_file() and hashlib.sha256(z.read(info)).hexdigest()==sha(p))
  for p in ['index.html','STORE_QUANTITY_RULES.md','UI_POLISH_QUANTITY_REPORT.md','tests/verify_ui_quantity_release.py','tests/ui_quantity_checks.js','tests/ui_quantity_qa.py','tests/ui-quantity-evidence/chrome-results.json','tests/ui-quantity-evidence/edge-results.json']:
   ck('Source ZIP includes updated task files: '+p,'AquariumLife/'+p in names)
result={'passed':sum(x['pass'] for x in checks),'failed':sum(not x['pass'] for x in checks),'originalAssets':len(assets),'browserAssertions':sum(s['passed'] for s in suites),'suites':suites,'failures':[c for c in checks if not c['pass']]}
if '--check-only' not in sys.argv:(R/'tests/ui-quantity-evidence/release-validation.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result,indent=2));sys.exit(bool(result['failed']))
