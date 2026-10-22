"""Verify source preservation, protected artifact integrity, local assets and executed evidence."""
from pathlib import Path
from zipfile import ZipFile
import base64,hashlib,json,re,sys,tempfile

R=Path(__file__).resolve().parents[1];D=R/'DIST';checks=[]
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def ck(name,value):checks.append({'name':name,'pass':bool(value)})

baseline=json.loads((R/'planning/distribution-protection/baseline/originals.json').read_text())
for p,row in baseline.items():ck('Original development/art bytes unchanged: '+p,(R/p).is_file() and sha(R/p)==row['sha256'])
m=json.loads((D/'build-manifest.json').read_text());private=json.loads((R/'planning/distribution-protection/evidence/build-private.json').read_text())
ck('Protected manifest identifies the exact private build record',m['production'] and m['buildId']==private['buildId'])
ck('No source maps or unsafe mangling/expression options',private['minifier']['options']['sourceMap'] is False and private['minifier']['options']['mangle']['properties'] is False and private['minifier']['options']['mangle']['toplevel'] is False and private['minifier']['runtimeOptions']['compress'] is False)
paths={p.relative_to(D).as_posix() for p in D.rglob('*') if p.is_file()}
ck('Public manifest covers exactly all files except itself',paths=={f['path'] for f in m['files']}|{'build-manifest.json'})
ck('Only the playable entry is distributed, with no review pages',[p for p in paths if p.endswith('.html')]==['index.html'])
ck('No development documents, test files, tools, saves or maps shipped',all(Path(p).suffix not in {'.md','.map','.py','.cjs','.zip'} and not any(x in Path(p).parts for x in ['tests','planning','node_modules','.build-tools']) for p in paths))
ck('Only required top-level production files are present',all('/' in p or p in {'index.html','LICENSE.txt','.nojekyll','build-manifest.json'} for p in paths))
for f in m['files']:ck('Production manifest checksum: '+f['path'],sha(D/f['path'])==f['sha256'] and (D/f['path']).stat().st_size==f['bytes'])
for f in private['files']:ck('Source-to-output private mapping: '+f['input'],sha(R/f['input'])==f['inputSha256'] and sha(D/f['output'])==f['sha256'])
ck('Runtime code and styles use content-derived names',all(re.fullmatch(r'(js|css)/a\.[0-9a-f]{20}\.(js|css)',p) for p in paths if p.startswith(('js/','css/'))))
html=(D/'index.html').read_text(encoding='utf8')
ck('HTML dependencies are local classic deferred scripts without maps/modules',all((D/p).is_file() for p in re.findall(r'(?:src|href)="((?:js|css)/[^"]+)"',html)) and 'type="module"' not in html and not re.search(r'<script[^>]+src="https?://',html))
registry=json.loads((R/'assets/animation/livestock-registry.json').read_text(encoding='utf8'));clips=[clip for e in registry['entries'] for clip in e['clips']]
for clip in clips:
 p=D/clip['path'];ck('Original native PNG in distribution: '+clip['path'],p.is_file() and sha(p)==clip['sha256'])
 transport=D/'assets/livestock/animation-sources'/(clip['sha256']+'.js');code=transport.read_text(encoding='utf8');match=re.search(r'AL\.SpriteSources\.accept\((.*)\);',code)
 try:
  args=json.loads('['+match.group(1)+']') if match else [];valid=len(args)==2 and args[0]==clip['path'] and hashlib.sha256(base64.b64decode(args[1].split(',',1)[1])).hexdigest()==clip['sha256']
 except Exception:valid=False
 ck('Minified file-origin transport retains exact PNG bytes: '+clip['path'],valid)
with ZipFile(R/'AquariumLife-GitHub-Pages.zip') as z:
 ck('Pages ZIP CRC',z.testzip() is None);ck('Pages ZIP contains exact production paths',set(z.namelist())==paths)
 for p in paths:ck('Pages ZIP exact bytes: '+p,hashlib.sha256(z.read(p)).hexdigest()==sha(D/p))
ck('Changed file content fails checksum comparison',hashlib.sha256(b'altered'+(D/'index.html').read_bytes()).hexdigest()!=next(f['sha256'] for f in m['files'] if f['path']=='index.html'))
master=(R/'MASTER_DEVELOPMENT_PROMPT.md').read_text(encoding='utf8');continuity=(R/'PROJECT_CONTINUITY_SOURCE.md').read_text(encoding='utf8')
ck('31 master homes and exact continuity retained',len(re.findall(r'^# \d+\.',master,re.M))==31 and continuity.count(master)==1)
suites=[]
if '--artifacts-only' not in sys.argv:
 for p in ['tests/distribution-protection-evidence/chrome-protected.json','tests/distribution-protection-evidence/edge-protected.json','tests/distribution-protection-evidence/chrome-benchmark.json','tests/distribution-protection-evidence/chrome-media.json','tests/distribution-protection-evidence/chrome-idle.json','tests/pages-evidence/edge-results.json','tests/tutorial-audit-evidence/chrome-results.json','tests/economy-update-evidence/chrome-results.json','tests/equipment-reliability-evidence/chrome-results.json','tests/breeding-evidence/chrome-results.json']:
  d=json.loads((R/p).read_text(encoding='utf8'));ck('Executed suite passes: '+p,d['failed']==0 and d['passed']>0);suites.append({'path':p,'passed':d['passed'],'failed':d['failed']})
  if 'buildId' in d:ck('Suite tested this protected build: '+p,d['buildId']==m['buildId'])
 soak=json.loads((R/'tests/distribution-protection-evidence/chrome-soak.json').read_text(encoding='utf8'));ck('Five-minute protected soak passes',all(x['pass'] for x in soak['checks']));suites.append({'path':'tests/distribution-protection-evidence/chrome-soak.json','passed':sum(x['pass'] for x in soak['checks']),'failed':sum(not x['pass'] for x in soak['checks'])})
 repro=json.loads((R/'tests/distribution-protection-evidence/reproducibility.json').read_text());ck('Independent rebuild reproduces exact manifest and ZIP bytes',repro['passed'] and repro['buildId']==m['buildId'] and repro['zipSha256']==sha(R/'AquariumLife-GitHub-Pages.zip'))
if '--source-archive' in sys.argv:
 with ZipFile(R/'AquariumLife-v0.1.zip') as z:
  ck('Private development archive CRC',z.testzip() is None)
  for info in z.infolist():
   p=info.filename.removeprefix('AquariumLife/');ck('Private source archive exact bytes: '+p,(R/p).is_file() and hashlib.sha256(z.read(info)).hexdigest()==sha(R/p))
  for p in ['tools/production/package-lock.json','tools/production/minify.cjs','tools/production/protected_build.py','tools/production/bootstrap.py','DISTRIBUTION_PROTECTION_REPORT.md','AGENTS.md']:
   ck('Private source tooling included: '+p,'AquariumLife/'+p in z.namelist())
result={'buildId':m['buildId'],'passed':sum(x['pass'] for x in checks),'failed':sum(not x['pass'] for x in checks),'originalFiles':len(baseline),'nativeSheets':len(clips),'browserAssertions':sum(s['passed'] for s in suites),'suites':suites,'failures':[x for x in checks if not x['pass']]}
if '--check-only' not in sys.argv:(R/'tests/distribution-protection-evidence/release-validation.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result,indent=2));sys.exit(bool(result['failed']))
