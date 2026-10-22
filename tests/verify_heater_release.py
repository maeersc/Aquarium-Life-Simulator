"""Verify heater/journal acceptance, final deployment bytes and protected continuity."""
from pathlib import Path
from zipfile import ZipFile
import json,hashlib,re
root=Path(__file__).resolve().parent.parent
def read(path):return json.loads((root/path).read_text(encoding='utf-8'))
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
m=read('DIST/build-manifest.json');rows=[]
for browser in ['chrome','edge']:
 o=read(f'tests/overnight-evidence/{browser}-after.json')
 assert o['failed']==0 and not o['healthyFailed'] and o['equivalencePassed']==60
 for r in o['rows']:
  obs=r['offline'];assert r['equivalent'] and len(obs['diagnostics'])==len(obs['deaths'])==obs['total']-obs['alive']
  for e in obs['diagnostics']:
   assert e['cause']!='Cause of death undetermined.' and all(k in e['water'] for k in ['ammonia','nitrite','oxygen','temperature','ph','salinity']) and e['intervalStart']<e['time']
 totals={'overnight':o['equivalencePassed']+o['logic']['passed']+sum(x['pass'] for x in o['ui'])}
 for folder,label in [('heater','heaterPermanentJournal'),('update34','rewardFinance'),('update29','gameplay'),('expansion','healthEconomyFreshwater'),('diving','diving'),('pages','builtPagesLocalSave')]:
  r=read(f'tests/{folder}-evidence/{browser}-results.json');assert r['failed']==0;totals[label]=r['passed']
  if folder=='heater':assert r['logic']==read(f'tests/heater-evidence/{browser}-logic.json')
 rows.append({'browser':browser,'passed':sum(totals.values()),'failed':0,'suites':totals})
originals={browser:read(f'tests/heater-evidence/{browser}-original-thermal.json') for browser in ['chrome','edge']}
assert all(len(r)==21 and all(x['equivalent'] for x in r) for r in originals.values())
for f in m['files']:assert sha(root/f['path'])==f['sha256']==sha(root/'DIST'/f['path']),f['path']
with ZipFile(root/'AquariumLife-GitHub-Pages.zip') as z:
 assert z.testzip() is None
 for f in m['files']:assert hashlib.sha256(z.read(f['path'])).hexdigest()==f['sha256']
 assert z.read('build-manifest.json')==(root/'DIST/build-manifest.json').read_bytes() and z.read('.nojekyll')==b''
text=(root/'MASTER_DEVELOPMENT_PROMPT.md').read_text(encoding='utf-8');continuity=(root/'PROJECT_CONTINUITY_SOURCE.md').read_text(encoding='utf-8')
assert m['gameContent']=='v3.6' and 'MORTALITY_LOG_SCHEMA.md' in [f['path'] for f in m['files']]
assert len(re.findall(r'^# \d+\.',text,re.M))==31 and text in continuity
prefix=continuity[:continuity.index('# AQUARIUM LIFE')]
for version in ['27','29']:
 for record in read(f'assets/expansion-v{version}/registry.json')['records']:assert record['id'] in prefix,record['id']
old=read('planning/heater-mortality/before.json');assets=[f for f in read('planning/heater-mortality/previous-build-manifest.json')['files'] if f['path'].startswith('assets/')]
assert all(sha(root/f['path'])==f['sha256'] for f in assets) and sha(root/'js/data.js')==old['js/data.js']
evidence={'browsers':rows,'repairChecks':sum(r['passed'] for r in rows),'originalThermalComparisons':sum(len(r) for r in originals.values()),'build':{k:m[k] for k in ['builtAt','gameContent','sourceFiles','sourceBytes']},'pagesZipBytes':(root/'AquariumLife-GitHub-Pages.zip').stat().st_size,'pagesZipCrcAndAllSourceHashes':True,'unchangedAssetFiles':len(assets),'unchangedBaseCatalog':True,'full31SectionMasterEmbeddedInContinuity':True,'bothPermanentRosterLedgersRetained':True}
(root/'tests/heater-evidence/release-verification.json').write_text(json.dumps(evidence,indent=2),encoding='utf-8')
print(json.dumps(evidence,indent=2))
