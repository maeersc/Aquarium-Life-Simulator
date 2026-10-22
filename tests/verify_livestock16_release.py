"""Current partial-artwork release checks; never labels missing artwork complete."""
import hashlib
import json
from pathlib import Path
import re
import sys
from zipfile import ZipFile

root=Path(__file__).resolve().parents[1]
checks=[]
def check(label,condition):
    checks.append({'name':label,'pass':bool(condition)})
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

ledger=json.loads((root/'assets/animation/livestock-registry.json').read_text(encoding='utf8'))
entries=ledger['entries'];before=json.loads((root/'tests/livestock16-evidence/catalog-before.json').read_text(encoding='utf8'))
check('Exact runtime119 identity/category mapping',{(r['id'],r['category']) for r in entries}=={(r['id'],r['category']) for r in before} and len(entries)==119)
check('Twelve batches with exhaustive once-only membership',len(ledger['batches'])==12 and sorted(i for b in ledger['batches'] for i in b['ids'])==sorted(e['id'] for e in entries))
check('Zero production sheets and119 unfinished entries reported truthfully',all(e['status']=='artwork-required' and not e['clips'] and e['framesCompleted']==0 and e['userApproved'] is False for e in entries))
check('Twenty-five existing varieties preserved under their biological IDs',sum(len(e['varieties']) for e in entries)==25)
for e in entries:
    check('Original source exists: '+e['id'],(root/e['existingPath']).is_file())
    check('Specific missing artwork recorded: '+e['id'],len(e['missingArtwork'])>90)
    for v in e['varieties']:
        check('Original variety source: '+v['id'],(root/v['existingPath']).is_file())
baseline=json.loads((root/'planning/livestock16/baseline-hashes.json').read_text(encoding='utf8'))
allowed={'js/fish-animation.js','js/fish-animation-data.js','js/render.js','js/expansion-ui.js','build.py','index.html','MASTER_DEVELOPMENT_PROMPT.md','PROJECT_CONTINUITY_SOURCE.md'}
preserved=0
for name,value in baseline.items():
    if name in allowed:continue
    ok=(root/name).is_file() and sha(root/name)==value
    check('Retained original: '+name,ok);preserved+=int(ok)
master=(root/'MASTER_DEVELOPMENT_PROMPT.md').read_text(encoding='utf8')
continuity=(root/'PROJECT_CONTINUITY_SOURCE.md').read_text(encoding='utf8')
check('Master retains all31 numbered major sections',len(re.findall(r'^# \d+\. ',master,re.M))==31)
check('Continuity contains the complete exact current master once',continuity.count(master)==1)
check('One authoritative16-frame requirement section','## 3.14 Marine livestock animation' in master and 'VERSION 4.7' in master)
report=(root/'LIVESTOCK_ANIMATION_16_FRAME_REPORT.md').read_text(encoding='utf8')
check('Coverage report includes all119 stable IDs',all('`'+e['id']+'`' in report for e in entries))
check('Report discloses unfinished expansion and rejected candidate','not finished' in report and '0**' in report and 'rejected' in report)
for name in ['js/livestock-animation-review.js','livestock-animation-review.html']:
    text=(root/name).read_text(encoding='utf8')
    check('Isolated gallery has no save/main/storage dependency: '+name,all(x not in text for x in ['localStorage','js/save.js','js/main.js','js/startup.js']))
check('Rejected image retained only as a development candidate',(root/'planning/livestock16/ocellaris-adult-candidate-rejected.png').is_file() and not (root/'DIST/planning').exists())
suites=[]
for folder,name in [('livestock16-evidence','chrome'),('livestock16-evidence','edge'),('pages-evidence','chrome'),('pages-evidence','edge')]:
    path=root/'tests'/folder/(name+'-results.json')
    result=json.loads(path.read_text(encoding='utf8'))
    check('Latest browser suite passes: '+folder+'/'+name,result.get('failed')==0 and result.get('passed',0)>100)
    if folder=='livestock16-evidence':
        check(name+': zero fake authored frames',result['productionSheets']==0 and result['authoredFramesCompleted']==0)
        check(name+': all119 entries covered',len(result['coverage'])==119 and {r['id'] for r in result['coverage']}=={e['id'] for e in entries})
        check(name+': mixed119-resident render remains within budget',result['mixedPerformance']['unchanged'] and result['mixedPerformance']['residents']==119 and result['mixedPerformance']['meanMilliseconds']<50)
    suites.append({'file':str(path.relative_to(root)),'passed':result['passed'],'failed':result['failed']})
manifest=json.loads((root/'DIST/build-manifest.json').read_text(encoding='utf8'))
check('Current build version4.0.4',manifest['gameContent']=='v4.0.4')
check('Local PC/browser save policy retained','localStorage' in manifest['savePolicy'] and 'no server saves' in manifest['savePolicy'])
with ZipFile(root/'AquariumLife-GitHub-Pages.zip') as archive:
    check('Pages ZIP CRC',archive.testzip() is None)
    check('Pages ZIP root entry','index.html' in archive.namelist() and not any(p.startswith('DIST/') for p in archive.namelist()))
    for record in manifest['files']:
        name=record['path'];source=root/name;published=root/'DIST'/name
        check('Exact source/DIST/ZIP: '+name,sha(source)==record['sha256']==sha(published)==hashlib.sha256(archive.read(name)).hexdigest())
    check('Generated manifest copied to ZIP',archive.read('build-manifest.json')==(root/'DIST/build-manifest.json').read_bytes())
    check('Full offline gallery and report are deployed',all(p in archive.namelist() for p in ['livestock-animation-review.html','js/livestock-animation-review.js','LIVESTOCK_ANIMATION_16_FRAME_REPORT.md','assets/animation/livestock-registry.json']))
if '--source-archive' in sys.argv:
    with ZipFile(root/'AquariumLife-v0.1.zip') as archive:
        check('Source ZIP CRC',archive.testzip() is None)
        for name in archive.namelist():
            path=root/name.removeprefix('AquariumLife/')
            check('Source ZIP current: '+str(path.relative_to(root)),path.is_file() and path.read_bytes()==archive.read(name))
        check('Source archive includes new QA evidence','AquariumLife/tests/livestock16-evidence/chrome-results.json' in archive.namelist())
result={'passed':sum(c['pass'] for c in checks),'failed':sum(not c['pass'] for c in checks),'expansionComplete':False,'marineEntriesAudited':119,'batches':12,'newProductionSheets':0,'unfinishedEntries':119,'preservedOriginals':preserved,'browserAssertions':sum(s['passed'] for s in suites),'suites':suites,'builtAt':manifest['builtAt'],'failures':[c for c in checks if not c['pass']]}
print(json.dumps(result,indent=2))
if '--check-only' not in sys.argv:
    (root/'tests/livestock16-evidence/release-validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
sys.exit(bool(result['failed']))
