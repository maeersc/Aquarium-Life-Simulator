"""Verify current source, complete continuity, deployment and portable archives.

Run after build/QA, then package.py; use --source-archive --check-only for the
final immutable check so the evidence included in that archive stays current.
"""
from pathlib import Path
from zipfile import ZipFile
import hashlib,json,re,sys

ROOT=Path(__file__).resolve().parent.parent
checks=[]
def ck(name,ok):
 checks.append({'name':name,'pass':bool(ok)})
 if not ok:raise AssertionError(name)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return (ROOT/p).read_text(encoding='utf8')

m=read('MASTER_DEVELOPMENT_PROMPT.md');c=read('PROJECT_CONTINUITY_SOURCE.md')
ck('Full current 31-section MDP v4.1 is embedded verbatim in continuity',len(re.findall(r'^# \d+\.',m,re.M))==31 and 'VERSION 4.1' in m and m in c)
old_m=read('planning/automatic-breeding/baseline/MASTER_DEVELOPMENT_PROMPT.md')
old_c=read('planning/automatic-breeding/baseline/PROJECT_CONTINUITY_SOURCE.md')
def genetics(s):return s[s.index('## 15.7 Persistent Pattern Inheritance'):s.index('## 15.8 ')]
ck('Previously approved genetics design is preserved verbatim',genetics(m)==genetics(old_m))
prefix=c[:c.index(m)];old_prefix=old_c[:old_c.index(old_m)]
old_rows=[line for line in old_prefix.splitlines() if line.startswith('|')]
ck('Every prior continuity registry row remains unchanged',len(old_rows)>=73 and all(row in prefix for row in old_rows))
rule='Fish breeding in Aquarium Life happens autonomously when biologically appropriate conditions are satisfied. The player does not manually initiate courtship through the Field Journal. Reproductive condition is visible through individual livestock inspection, and eggs or offspring appear in the same aquarium as their parents according to species-specific reproductive biology.'
ck('Permanent autonomous-breeding rule is present in the primary master',rule in m)
ck('Original genetics implementation remains byte-identical',sha(ROOT/'js/patterns.js')==sha(ROOT/'planning/automatic-breeding/baseline/patterns.js'))
ck('Runtime UI has no manual courtship button',"button('Begin courtship'" not in read('js/ui.js') and 'data-action="breed"' not in read('js/app-shell.js'))
ck('Current UI version is v3.8','OFFLINE EDITION · v3.8' in read('index.html'))

manifest=json.loads(read('DIST/build-manifest.json'))
ck('DIST declares current version and device-local saves',manifest['gameContent']=='v3.8' and 'no server saves' in manifest['savePolicy'])
for row in manifest['files']:
 p=ROOT/row['path'];q=ROOT/'DIST'/row['path']
 ck('Current source equals DIST: '+row['path'],p.is_file() and q.is_file() and sha(p)==row['sha256']==sha(q))
ck('Manifest source-file count is exact',len(manifest['files'])==manifest['sourceFiles'])
ck('Manifest source byte count is exact',sum((ROOT/'DIST'/r['path']).stat().st_size for r in manifest['files'])==manifest['sourceBytes'])
before=json.loads(read('planning/automatic-breeding/before-build-manifest.json'))
assets=[r for r in before['files'] if r['path'].startswith('assets/')]
ck('All '+str(len(assets))+' prior deployed assets remain byte-identical',all(sha(ROOT/r['path'])==r['sha256'] for r in assets))
with ZipFile(ROOT/'AquariumLife-GitHub-Pages.zip') as z:
 ck('Pages ZIP CRC passes',z.testzip() is None)
 ck('Pages ZIP starts at the deployment root','index.html' in z.namelist() and '.nojekyll' in z.namelist() and not any(n.startswith('DIST/') for n in z.namelist()))
 ck('Pages ZIP exactly matches current DIST entries',set(z.namelist())=={p.relative_to(ROOT/'DIST').as_posix() for p in (ROOT/'DIST').rglob('*') if p.is_file()})
 ck('Every Pages ZIP byte matches current DIST',all(z.read(n)==(ROOT/'DIST'/n).read_bytes() for n in z.namelist()))

suites=[
 'breeding-evidence/chrome-results.json','breeding-evidence/edge-results.json',
 'expansion-evidence/chrome-results.json','update29-evidence/edge-results.json',
 'store-casino-evidence/edge-results.json','heater-evidence/edge-results.json',
 'update34-evidence/chrome-results.json','pages-evidence/chrome-results.json',
 'pages-evidence/edge-results.json'
]
results=[]
for name in suites:
 r=json.loads(read('tests/'+name));ck('Current acceptance suite: '+name,r['failed']==0)
 results.append({'file':name,'passed':r['passed'],'failed':r['failed']})
for browser in ['chrome','edge']:
 r=json.loads(read('tests/breeding-evidence/'+browser+'-results.json'))
 ck(browser+': 29 existing supported species with 26 attached clownfish profiles',len(r['supportedSpecies'])==29 and sum(f['profile']=='attached' for f in r['supportedSpecies'])==26)
 ck(browser+': genuine live/offline parity at 8/12/24 real hours',all(any(x['pass'] and x['name'].startswith(str(hours)+' real hours:') for x in r['checks']) for hours in [8,12,24]))

if '--source-archive' in sys.argv:
 with ZipFile(ROOT/'AquariumLife-v0.1.zip') as z:
  ck('Source ZIP CRC passes',z.testzip() is None)
  ck('Source ZIP contains current game, breeding evidence and full continuity',all('AquariumLife/'+p in z.namelist() for p in ['index.html','js/breeding.js','BREEDING_UPDATE_REPORT.md','PROJECT_CONTINUITY_SOURCE.md','tests/breeding-evidence/release-validation.json']))
  ck('Source ZIP excludes browser profiles and caches',not any('profile' in n or '__pycache__' in n for n in z.namelist()))
  ck('Every source ZIP entry matches current workspace source',all(n.startswith('AquariumLife/') and z.read(n)==(ROOT/n[len('AquariumLife/'):]).read_bytes() for n in z.namelist()))

report={'passed':len(checks),'failed':0,'suiteAssertions':sum(r['passed'] for r in results),'suites':results,'deployment':{k:manifest[k] for k in ['builtAt','gameContent','sourceFiles','sourceBytes']},'unchangedAssets':len(assets),'checks':checks}
if '--check-only' not in sys.argv:
 (ROOT/'tests/breeding-evidence/release-validation.json').write_text(json.dumps(report,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k!='checks'},indent=2))
