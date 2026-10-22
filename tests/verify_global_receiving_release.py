"""Verify universal receiving coverage, deployed bytes, preserved data and archives."""
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
ck('Universal receiving rule is in the existing primary section','### Universal diving receiving' in m[m.index('## 5.5 '):m.index('## 5.6 ')])
old_m=read('planning/global-receiving/before-MASTER_DEVELOPMENT_PROMPT.md');old_c=read('planning/global-receiving/before-PROJECT_CONTINUITY_SOURCE.md');old_rows=[line for line in old_c[:old_c.index(old_m)].splitlines() if line.startswith('|')]
ck('Every old 38/35 roster ledger row is retained',len(old_rows)>=73 and all(line in c[:c.index(m)] for line in old_rows))
ck('Species checks contain no Chalk Bass exception','chalk-bass' not in read('js/diving-receiving.js'))
ck('The exact same validator serves all transfer host types','return AL.DiveReceiving.report(s,id,tankId,position)' in read('js/diving.js') and "item.kind==='livestock'" in read('js/diving.js'))
ck('Contagiousness is derived from the actual condition','!!AL.Health.conditions[type].contagious' in read('js/diving.js'))
ck('Original genetics implementation unchanged',sha(r/'js/patterns.js')==sha(r/'planning/automatic-breeding/baseline/patterns.js'))
old_gate=[x for x in read('planning/global-receiving/before-store-rules.js').splitlines() if "if(action==='buyTank'&&a.water==='fresh'" in x]
ck('Existing freshwater purchase/interaction gate unchanged',len(old_gate)==1 and old_gate[0] in read('js/store-rules.js'))
manifest=json.loads(read('DIST/build-manifest.json'));paths={x['path'] for x in manifest['files']}
ck('Universal report and runtime are deployed',{'GLOBAL_DIVING_RECEIVING_REPORT.md','js/diving-receiving.js','js/diving-mystery.js'}<=paths)
ck('Saves remain device-local','no server saves' in manifest['savePolicy'])
for x in manifest['files']:ck('Source/DIST '+x['path'],sha(r/x['path'])==x['sha256']==sha(r/'DIST'/x['path']))
ck('Manifest counts are exact',len(manifest['files'])==manifest['sourceFiles'] and sum(x['bytes'] for x in manifest['files'])==manifest['sourceBytes'])
before=json.loads(read('planning/global-receiving/before-build-manifest.json'));assets=[x for x in before['files'] if x['path'].startswith('assets/')]
ck('All '+str(len(assets))+' prior assets/biological registries unchanged',all(sha(r/x['path'])==x['sha256'] for x in assets))
with ZipFile(r/'AquariumLife-GitHub-Pages.zip') as z:
 ck('Pages ZIP CRC',z.testzip() is None)
 ck('Correct deployment-root ZIP','index.html' in z.namelist() and '.nojekyll' in z.namelist() and not any(n.startswith(('DIST/','tests/')) for n in z.namelist()))
 ck('Every Pages byte equals current DIST',set(z.namelist())=={p.relative_to(r/'DIST').as_posix() for p in (r/'DIST').rglob('*') if p.is_file()} and all(z.read(n)==(r/'DIST'/n).read_bytes() for n in z.namelist()))
suites=[];coverage=[]
for n in ['global-receiving-evidence/chrome-results.json','global-receiving-evidence/edge-results.json','mystery-diving-evidence/chrome-results.json','receiving-evidence/edge-results.json','pages-evidence/chrome-results.json','pages-evidence/edge-results.json']:
 d=json.loads(read('tests/'+n));ck('Passed suite '+n,d['failed']==0)
 if n.startswith('pages-evidence'):ck('Built universal runtime was actually tested '+n,any(x['name'].startswith('Built universal receiving covers') and x['pass'] for x in d['results']))
 if n.startswith('global-receiving-evidence'):
  coverage=d['coverage'];ck('All three host categories and both dive modes are tested '+n,{x['kind'] for x in coverage}=={'fish','coral','invertebrate'} and {x['mode'] for x in coverage}=={'reef','deep'})
 suites.append({'file':n,'passed':d['passed'],'failed':d['failed']})
if '--source-archive' in sys.argv:
 with ZipFile(r/'AquariumLife-v0.1.zip') as z:
  ck('Source ZIP CRC',z.testzip() is None)
  ck('Current universal source/report/evidence are included',all('AquariumLife/'+n in z.namelist() for n in ['js/diving-receiving.js','GLOBAL_DIVING_RECEIVING_REPORT.md','tests/global-receiving-evidence/release-validation.json']))
  ck('No profiles/caches included',not any('profile' in n or '__pycache__' in n for n in z.namelist()))
  ck('Every source archive byte is current',all(n.startswith('AquariumLife/') and z.read(n)==(r/n[len('AquariumLife/'):]).read_bytes() for n in z.namelist()))
result={'passed':len(checks),'failed':0,'suiteAssertions':sum(x['passed'] for x in suites),'suites':suites,'coverage':coverage,'deployment':{k:manifest[k] for k in ['builtAt','gameContent','sourceFiles','sourceBytes']},'unchangedAssets':len(assets),'checks':checks}
if '--check-only' not in sys.argv:(r/'tests/global-receiving-evidence/release-validation.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k not in ['checks','coverage']},indent=2))
