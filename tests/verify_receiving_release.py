"""Validate the receiving repair's final deployment, evidence and source ZIP."""
from pathlib import Path
from zipfile import ZipFile
import hashlib,json,re,sys
r=Path(__file__).resolve().parents[1];checks=[]
def read(n):return (r/n).read_text(encoding='utf8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ck(n,v):
 checks.append({'name':n,'pass':bool(v)})
 if not v:raise AssertionError(n)
m=read('MASTER_DEVELOPMENT_PROMPT.md');c=read('PROJECT_CONTINUITY_SOURCE.md')
ck('Full current 31-section master embedded verbatim',m in c and len(re.findall(r'^# \d+\.',m,re.M))==31)
ck('Receiving rule is in the primary diving section', '### Receiving diagnostics repair' in m[m.index('## 5.5 '):m.index('## 5.6 ')])
ck('One report authority serves both UI and transfer','AL.DiveReceiving.report(s,id,tankId)' in read('js/diving.js') and 'AL.DiveReceiving.destinations' in read('js/diving-ui.js'))
ck('Prior genetic implementation remains untouched',sha(r/'js/patterns.js')==sha(r/'planning/automatic-breeding/baseline/patterns.js'))
manifest=json.loads(read('DIST/build-manifest.json'));paths={x['path'] for x in manifest['files']}
ck('Current receiving module/report are deployed',{'js/diving-receiving.js','DIVING_RECEIVING_REPAIR_REPORT.md'}<=paths)
ck('Device-local saves retained','no server saves' in manifest['savePolicy'])
for x in manifest['files']:ck('Source/DIST hash '+x['path'],sha(r/x['path'])==x['sha256']==sha(r/'DIST'/x['path']))
ck('Exact manifest count/bytes',len(manifest['files'])==manifest['sourceFiles'] and sum(x['bytes'] for x in manifest['files'])==manifest['sourceBytes'])
before=json.loads(read('planning/receiving-repair/before-build-manifest.json'));assets=[x for x in before['files'] if x['path'].startswith('assets/')]
ck('All '+str(len(assets))+' previous assets remain byte-identical',all(sha(r/x['path'])==x['sha256'] for x in assets))
with ZipFile(r/'AquariumLife-GitHub-Pages.zip') as z:
 ck('Pages ZIP CRC',z.testzip() is None)
 ck('Correct deployment-root ZIP','index.html' in z.namelist() and '.nojekyll' in z.namelist() and not any(n.startswith(('DIST/','tests/')) for n in z.namelist()))
 ck('Every Pages byte matches current DIST',set(z.namelist())=={p.relative_to(r/'DIST').as_posix() for p in (r/'DIST').rglob('*') if p.is_file()} and all(z.read(n)==(r/'DIST'/n).read_bytes() for n in z.namelist()))
suites=[]
for n in ['receiving-evidence/chrome-results.json','receiving-evidence/edge-results.json','mystery-diving-evidence/edge-results.json','pages-evidence/chrome-results.json','pages-evidence/edge-results.json']:
 d=json.loads(read('tests/'+n));ck('Passing current suite '+n,d['failed']==0)
 if n.startswith('pages-evidence'):ck('Built receiving runtime was tested '+n,any(x['name'].startswith('Built receiving repair exposes') and x['pass'] for x in d['results']))
 suites.append({'file':n,'passed':d['passed'],'failed':d['failed']})
if '--source-archive' in sys.argv:
 with ZipFile(r/'AquariumLife-v0.1.zip') as z:
  ck('Source ZIP CRC',z.testzip() is None)
  ck('Current source/report/evidence in ZIP',all('AquariumLife/'+n in z.namelist() for n in ['js/diving-receiving.js','DIVING_RECEIVING_REPAIR_REPORT.md','tests/receiving-evidence/release-validation.json']))
  ck('No profile/cache included',not any('profile' in n or '__pycache__' in n for n in z.namelist()))
  ck('Every source ZIP byte is current',all(n.startswith('AquariumLife/') and z.read(n)==(r/n[len('AquariumLife/'):]).read_bytes() for n in z.namelist()))
result={'passed':len(checks),'failed':0,'suiteAssertions':sum(x['passed'] for x in suites),'suites':suites,'deployment':{k:manifest[k] for k in ['builtAt','gameContent','sourceFiles','sourceBytes']},'unchangedAssets':len(assets),'checks':checks}
if '--check-only' not in sys.argv:(r/'tests/receiving-evidence/release-validation.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
