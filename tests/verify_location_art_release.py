"""Audit presentation-only changes, art assignments and current release bytes."""
from pathlib import Path
from zipfile import ZipFile
import hashlib,json,re,sys
r=Path(__file__).resolve().parents[1];checks=[]
def read(n):return (r/n).read_text(encoding='utf8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ck(n,v):
 checks.append({'name':n,'pass':bool(v)})
 if not v:raise AssertionError(n)
b=r/'planning/location-art/baseline'
hashes=json.loads((b/'hashes.json').read_text(encoding='utf8'))
changed={'js/diving-data.js','js/diving-art-data.js','js/diving-art.js','js/diving-ui.js','assets/diving/registry.json','assets/diving/art-prompts.json'}
untouched=[n for n in hashes if n not in changed]
ck('Every prior gameplay authority, species asset and old environment remains byte-identical',all(sha(r/n)==hashes[n] for n in untouched))
old_art=(b/'js__diving-art.js').read_text(encoding='utf8');new_art=read('js/diving-art.js')
ck('Original mystery silhouette and catch reveal artwork functions remain exact',old_art[old_art.index(' function mystery('):old_art.index(' function regionalImage(')]==new_art[new_art.index(' function mystery('):new_art.index(' function scene(')])
old_ui=(b/'js__diving-ui.js').read_text(encoding='utf8');new_ui=read('js/diving-ui.js')
ck('All diving action/transfer handlers remain exact',old_ui[old_ui.index(' function handle('):old_ui.index(' function paintReveals(')]==new_ui[new_ui.index(' function handle('):new_ui.index(' function paintReveals(')])
before=json.loads((b/'assets__diving__registry.json').read_text(encoding='utf8'));now=json.loads(read('assets/diving/registry.json'));normalized=json.loads(json.dumps(now));normalized.pop('presentationVersion')
for region,entry in normalized['regions'].items():
 entry.pop('art')
 if 'background' in entry:entry['background']=before['regions'][region]['background']
ck('All modes, species pools, weights, restrictions and biological registry data unchanged',normalized==before)
records=json.loads(read('assets/diving/art-prompts.json'))['records'];old=json.loads((b/'assets__diving__art-prompts.json').read_text(encoding='utf8'))['records']
ck('Every older art record is retained exactly',records[:len(old)]==old)
ck('Eight new distinct PNG records',len(records)==17 and len({sha(r/x['path']) for x in records[9:]})==8)
for record in records[9:]:
 raw=(r/record['path']).read_bytes()
 ck('Native unmodified 1536x1024 PNG: '+record['id'],raw[:8]==b'\x89PNG\r\n\x1a\n' and int.from_bytes(raw[16:20],'big')==1536 and int.from_bytes(raw[20:24],'big')==1024)
ck('No SVG background remains assigned',all(art['path'].endswith('-v1.png') or art['path'].endswith('-v2.png') for entry in now['regions'].values() for art in entry['art'].values()))
m=read('MASTER_DEVELOPMENT_PROMPT.md');c=read('PROJECT_CONTINUITY_SOURCE.md')
ck('Full updated master is embedded verbatim and retains all 31 major sections',m in c and len(re.findall(r'^# \d+\.',m,re.M))==31)
ck('Permanent artwork rules live in the primary diving section','### Destination identity and artwork' in m[m.index('## 5.5 '):m.index('## 5.6 ')])
old_m=(b/'MASTER_DEVELOPMENT_PROMPT.md').read_text(encoding='utf8');old_c=(b/'PROJECT_CONTINUITY_SOURCE.md').read_text(encoding='utf8');rows=[line for line in old_c[:old_c.index(old_m)].splitlines() if line.startswith('|')]
ck('Original 38/35 roster ledger rows retained',len(rows)>=73 and all(line in c[:c.index(m)] for line in rows))
manifest=json.loads(read('DIST/build-manifest.json'));paths={x['path'] for x in manifest['files']}
ck('Current release and report are deployed',manifest['gameContent']=='v4.0.2' and 'DIVING_LOCATION_ART_REPORT.md' in paths)
ck('Saves remain device-local with no server saves','no server saves' in manifest['savePolicy'])
for item in manifest['files']:ck('Source/DIST '+item['path'],sha(r/item['path'])==item['sha256']==sha(r/'DIST'/item['path']))
ck('Manifest totals match current files',len(manifest['files'])==manifest['sourceFiles'] and sum(x['bytes'] for x in manifest['files'])==manifest['sourceBytes'])
with ZipFile(r/'AquariumLife-GitHub-Pages.zip') as z:
 ck('Pages ZIP CRC passes',z.testzip() is None)
 ck('Pages ZIP contains exactly current DIST bytes at its root',set(z.namelist())=={p.relative_to(r/'DIST').as_posix() for p in (r/'DIST').rglob('*') if p.is_file()} and all(z.read(n)==(r/'DIST'/n).read_bytes() for n in z.namelist()))
suites=[]
for file in ['location-art-evidence/chrome-results.json','location-art-evidence/edge-results.json','pages-evidence/chrome-results.json','pages-evidence/edge-results.json']:
 d=json.loads(read('tests/'+file));ck('Passed actual suite '+file,d['failed']==0)
 items=d.get('checks',d.get('results'))
 if file.startswith('pages-evidence'):
  ck('Built artwork and native URLs actually checked '+file,sum(x['name'].startswith('Native PNG URL loads at Pages') and x['pass'] for x in items)==16)
 else:
  ck('Every new destination launches, draws and returns through actual UI '+file,all(any(x['name']==region+'-'+entry['modes'][0]+': actual boat return shows correct results accent' and x['pass'] for x in items) for region,entry in now['regions'].items() if region not in ['fiji','caribbean','hawaii','japan']))
 suites.append({'file':file,'passed':d['passed'],'failed':d['failed']})
if '--source-archive' in sys.argv:
 with ZipFile(r/'AquariumLife-v0.1.zip') as z:
  ck('Source ZIP CRC passes',z.testzip() is None)
  ck('Source ZIP includes new art, report and evidence',all('AquariumLife/'+n in z.namelist() for n in ['DIVING_LOCATION_ART_REPORT.md','tests/location_art_qa.py','tests/location-art-evidence/release-validation.json',*[x['path'] for x in records[9:]]]))
  ck('Source ZIP excludes browser profiles and caches',not any('profile' in n or '__pycache__' in n for n in z.namelist()))
  ck('Source ZIP bytes are current',all(n.startswith('AquariumLife/') and z.read(n)==(r/n[len('AquariumLife/'):]).read_bytes() for n in z.namelist()))
result={'passed':len(checks),'failed':0,'browserAssertions':sum(x['passed'] for x in suites),'suites':suites,'preservedFiles':len(untouched),'deployment':{k:manifest[k] for k in ['builtAt','gameContent','sourceFiles','sourceBytes']}}
if '--check-only' not in sys.argv:(r/'tests/location-art-evidence/release-validation.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result,indent=2))
