"""Verify preparation repair evidence, preserved source data and release artifacts."""
from pathlib import Path
from zipfile import ZipFile
import hashlib,json,re,sys
r=Path(__file__).resolve().parents[1];checks=[]
def read(n):return (r/n).read_text(encoding='utf8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ck(n,v):
 checks.append({'name':n,'pass':bool(v)})
 if not v:raise AssertionError(n)
baseline=json.loads(read('tests/preparation-evidence/before-repair.json'))
ck('Confirmed original normal-workflow reproduction',baseline['prepared'] and baseline['emptyDry'] and baseline['cycle']>=36 and not baseline['preparation']['ok'] and baseline['volume']['ok'])
m=read('MASTER_DEVELOPMENT_PROMPT.md');c=read('PROJECT_CONTINUITY_SOURCE.md')
ck('Full master embedded verbatim with all 31 major sections',m in c and len(re.findall(r'^# \d+\.',m,re.M))==31)
ck('Preparation rules live in the primary readiness section','### Authoritative preparation lifecycle' in m[m.index('## 12.5 '):m.index('## 12.6 ')])
old_m=read('planning/global-receiving/before-MASTER_DEVELOPMENT_PROMPT.md');old_c=read('planning/global-receiving/before-PROJECT_CONTINUITY_SOURCE.md');rows=[x for x in old_c[:old_c.index(old_m)].splitlines() if x.startswith('|')]
ck('Every original 38/35 roster ledger row retained',len(rows)>=73 and all(x in c[:c.index(m)] for x in rows))
before=json.loads(read('planning/preparation-repair/baseline/DIST__build-manifest.json'))
assets=[x for x in before['files'] if x['path'].startswith('assets/')]
ck('Every '+str(len(assets))+' prior asset and biological registry is unchanged',all(sha(r/x['path'])==x['sha256'] for x in assets))
ck('Genetics and diving state authority unchanged',sha(r/'js/patterns.js')==sha(r/'planning/automatic-breeding/baseline/patterns.js'))
gate=[x for x in read('planning/preparation-repair/baseline/js__store-rules.js').splitlines() if "if(action==='buyTank'&&a.water==='fresh'" in x]
ck('Freshwater lock remains exact',len(gate)==1 and gate[0] in read('js/store-rules.js'))
ck('No Chalk Bass special case in preparation authority','chalk-bass' not in read('js/aquarium-preparation.js'))
manifest=json.loads(read('DIST/build-manifest.json'));paths={x['path'] for x in manifest['files']}
ck('Current runtime/report are deployed',{'js/aquarium-preparation.js','AQUARIUM_PREPARATION_REPAIR_REPORT.md'}<=paths and manifest['gameContent']=='v4.0.1')
ck('Device-local save policy preserved','no server saves' in manifest['savePolicy'])
for x in manifest['files']:ck('Source/DIST '+x['path'],sha(r/x['path'])==x['sha256']==sha(r/'DIST'/x['path']))
ck('Manifest totals are exact',len(manifest['files'])==manifest['sourceFiles'] and sum(x['bytes'] for x in manifest['files'])==manifest['sourceBytes'])
with ZipFile(r/'AquariumLife-GitHub-Pages.zip') as z:
 ck('Pages ZIP CRC',z.testzip() is None)
 ck('Correct Pages-root archive','index.html' in z.namelist() and '.nojekyll' in z.namelist() and not any(n.startswith(('DIST/','tests/')) for n in z.namelist()))
 ck('Every ZIP byte matches DIST',set(z.namelist())=={p.relative_to(r/'DIST').as_posix() for p in (r/'DIST').rglob('*') if p.is_file()} and all(z.read(n)==(r/'DIST'/n).read_bytes() for n in z.namelist()))
suites=[]
for n in ['preparation-evidence/chrome-results.json','preparation-evidence/edge-results.json','pages-evidence/chrome-results.json','pages-evidence/edge-results.json']:
 d=json.loads(read('tests/'+n));ck('Passed current suite '+n,d['failed']==0);items=d.get('checks',d.get('results'))
 for phrase in ['Real prepared 80-gallon workflow','Reported 75 L','Legacy stale dry marker','actual offline service','Newly purchased second aquarium']:
  ck('Actual acceptance '+phrase+' '+n,any(phrase in x['name'] and x['pass'] for x in items))
 if n.startswith('pages-evidence'):ck('Built preparation authority actually tested '+n,any(x['name']=='Built shared aquarium preparation authority is loaded' and x['pass'] for x in items))
 else:ck('Freshwater seven-day differential replay '+n,any('pre-repair engine exactly' in x['name'] and x['pass'] for x in items))
 suites.append({'file':n,'passed':d['passed'],'failed':d['failed']})
if '--source-archive' in sys.argv:
 with ZipFile(r/'AquariumLife-v0.1.zip') as z:
  ck('Source ZIP CRC',z.testzip() is None)
  ck('Source ZIP includes repair and evidence',all('AquariumLife/'+n in z.namelist() for n in ['js/aquarium-preparation.js','AQUARIUM_PREPARATION_REPAIR_REPORT.md','tests/preparation-evidence/release-validation.json']))
  ck('Source ZIP excludes private browser profiles/caches',not any('profile' in n or '__pycache__' in n for n in z.namelist()))
  ck('All source ZIP bytes are current',all(n.startswith('AquariumLife/') and z.read(n)==(r/n[len('AquariumLife/'):]).read_bytes() for n in z.namelist()))
result={'passed':len(checks),'failed':0,'browserAssertions':sum(x['passed'] for x in suites),'suites':suites,'unchangedAssets':len(assets),'deployment':{k:manifest[k] for k in ['builtAt','gameContent','sourceFiles','sourceBytes']}}
if '--check-only' not in sys.argv:(r/'tests/preparation-evidence/release-validation.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result,indent=2))
