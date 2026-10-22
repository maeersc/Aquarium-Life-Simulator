"""Validate the current expansion's source, browser evidence, DIST and ZIP bytes."""
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
ck('Full current master embedded verbatim with 31 major sections',m in c and len(re.findall(r'^# \d+\.',m,re.M))==31)
ck('Current permanent mechanics reside in primary diving section',all(x in m[m.index('## 5.5 '):m.index('## 5.6 ')] for x in ['### Emergency Sale and diving rock resale','### Mystery eggs','### Mariana Trench']))
old_m=read('planning/global-receiving/before-MASTER_DEVELOPMENT_PROMPT.md');old_c=read('planning/global-receiving/before-PROJECT_CONTINUITY_SOURCE.md')
rows=[x for x in old_c[:old_c.index(old_m)].splitlines() if x.startswith('|')]
ck('Every original roster-ledger row is retained',len(rows)>=73 and all(x in c[:c.index(m)] for x in rows))
ck('Existing genetic inheritance implementation is unchanged',sha(r/'js/patterns.js')==sha(r/'planning/automatic-breeding/baseline/patterns.js'))
old_gate=[x for x in read('planning/global-receiving/before-store-rules.js').splitlines() if "if(action==='buyTank'&&a.water==='fresh'" in x]
ck('Freshwater gate unchanged',len(old_gate)==1 and old_gate[0] in read('js/store-rules.js'))
before=json.loads(read('planning/global-receiving/before-build-manifest.json'))
assets=[x for x in before['files'] if x['path'].startswith('assets/') and x['path']!='assets/diving/registry.json']
ck('All '+str(len(assets))+' prior art and non-diving biological assets unchanged',all(sha(r/x['path'])==x['sha256'] for x in assets))
registry=json.loads(read('assets/diving/registry.json'))
ck('Central registry has 12 destinations, 9 existing profiles and 100% stage weights',len(registry['regions'])==12 and len(registry['species'])==9 and sum(registry['lifeStageWeights'].values())==100)
ck('Mariana is remote/nonliving and egg odds are separate',registry['regions']['mariana']['remote'] and registry['regions']['mariana']['modes']==['deep'] and registry['regions']['mariana']['liveReceiving'] is False and registry['eggDiscoveryChance']==.03)
manifest=json.loads(read('DIST/build-manifest.json'));paths={x['path'] for x in manifest['files']}
ck('Current runtime and complete expansion report/schema deployed',{'js/diving-expansion.js','DIVING_EXPANSION_REPORT.md','DIVING_EXPANSION_SAVE_SCHEMA.md'}<=paths and manifest['gameContent']=='v4.0')
ck('Local-only saves documented','no server saves' in manifest['savePolicy'])
for x in manifest['files']:ck('Source/DIST '+x['path'],sha(r/x['path'])==x['sha256']==sha(r/'DIST'/x['path']))
ck('Manifest counts match actual files',len(manifest['files'])==manifest['sourceFiles'] and sum(x['bytes'] for x in manifest['files'])==manifest['sourceBytes'])
with ZipFile(r/'AquariumLife-GitHub-Pages.zip') as z:
 ck('Pages ZIP CRC',z.testzip() is None)
 ck('Pages ZIP starts at deployment root','index.html' in z.namelist() and '.nojekyll' in z.namelist() and not any(n.startswith(('DIST/','tests/')) for n in z.namelist()))
 ck('Every Pages ZIP byte matches DIST',set(z.namelist())=={p.relative_to(r/'DIST').as_posix() for p in (r/'DIST').rglob('*') if p.is_file()} and all(z.read(n)==(r/'DIST'/n).read_bytes() for n in z.namelist()))
suites=[]
for name in ['diving-expansion-evidence/chrome-results.json','diving-expansion-evidence/edge-results.json','pages-evidence/chrome-results.json','pages-evidence/edge-results.json']:
 d=json.loads(read('tests/'+name));ck('Passed current suite '+name,d['failed']==0)
 items=d.get('checks',d.get('results'))
 ck('Final hidden egg loss case actually executed '+name,any('Abandoned eggs stay unidentified' in x['name'] and x['pass'] for x in items))
 ck('Legacy active and pending fish migration actually executed '+name,all(any(label in x['name'] and x['pass'] for x in items) for label in ['Old pending fish without individual snapshots','Old captured active trips migrate','Future fish profiles without stage metadata']))
 if name.startswith('pages-evidence'):ck('Built expansion actually loaded '+name,any(x['name']=='Built diving expansion is loaded' and x['pass'] for x in items))
 suites.append({'file':name,'passed':d['passed'],'failed':d['failed']})
if '--source-archive' in sys.argv:
 with ZipFile(r/'AquariumLife-v0.1.zip') as z:
  ck('Source ZIP CRC',z.testzip() is None)
  ck('Current source and expansion evidence are packaged',all('AquariumLife/'+n in z.namelist() for n in ['js/diving-expansion.js','DIVING_EXPANSION_REPORT.md','tests/diving-expansion-evidence/release-validation.json']))
  ck('Source ZIP excludes profiles/caches',not any('profile' in n or '__pycache__' in n for n in z.namelist()))
  ck('Every source ZIP byte is current',all(n.startswith('AquariumLife/') and z.read(n)==(r/n[len('AquariumLife/'):]).read_bytes() for n in z.namelist()))
result={'passed':len(checks),'failed':0,'suiteAssertions':sum(x['passed'] for x in suites),'suites':suites,'unchangedPriorAssets':len(assets),'deployment':{k:manifest[k] for k in ['builtAt','gameContent','sourceFiles','sourceBytes']}}
if '--check-only' not in sys.argv:(r/'tests/diving-expansion-evidence/release-validation.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result,indent=2))
