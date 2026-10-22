"""Verify real authored PNGs, current browser evidence and the portable build.

--require-complete is mandatory for the final all-livestock completion claim.
--source-archive additionally compares every archived development source byte.
--check-only prints validation without rewriting evidence inside that archive.
"""
import base64
import hashlib
import json
from pathlib import Path
import re
import sys
from zipfile import ZipFile
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(name,condition):checks.append({'name':name,'pass':bool(condition)})
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
registry=json.loads((ROOT/'assets/animation/livestock-registry.json').read_text(encoding='utf8'))
ledger=json.loads((ROOT/'planning/sprite-production/production-ledger.json').read_text(encoding='utf8'))
entries={e['id']:e for e in registry['entries']}
eligible={e['id']:e for e in ledger['eligible']}
clips=[(entries[id],c) for id in eligible for c in entries[id]['clips']]
generated=(ROOT/'js/livestock-animation-data.js').read_text(encoding='utf8')
runtime=json.loads(generated.split('AL.LivestockAnimationData=',1)[1].strip().removesuffix(';'))
check('Generated metadata retains the exact central registry entries',runtime['entries']==registry['entries'])
assigned=set()
for ei,entry in enumerate(runtime['entries']):
    for ci,clip in enumerate(entry['clips']):
        path=ROOT/'assets/livestock/animation-sources'/(clip['sha256']+'.js')
        content=path.read_text(encoding='utf8') if path.is_file() else ''
        match=re.fullmatch(r'"use strict";\nAL\.SpriteSources\.accept\((".*"),(".*")\);\n',content)
        check('Per-sheet local source transport exists and is GitHub-safe: '+clip['path'],match is not None and path.stat().st_size<8_100_000)
        if not match:continue
        source_path=json.loads(match[1]);url=json.loads(match[2])
        check('Lossless bundled source equals registered native PNG: '+clip['path'],source_path==clip['path'] and url.startswith('data:image/png;base64,') and base64.b64decode(url.split(',',1)[1],validate=True)==(ROOT/clip['path']).read_bytes());assigned.add((ei,ci))
check('Every production sheet has one independently loadable source',len(assigned)==len(clips))
for filename in ['index.html','livestock-animation-review.html']:
    scripts=re.findall(r'<script\b[^>]*\bsrc="([^"]+)"', (ROOT/filename).read_text(encoding='utf8'))
    check('Small source loader precedes animator without eager native banks: '+filename,'js/sprite-sources.js' in scripts and scripts.index('js/sprite-sources.js')<scripts.index('js/fish-animation.js') and not any('livestock-animation-sheets-' in name for name in scripts))
check('Original119 unique biological records retained',len(registry['entries'])==len(entries)==119)
check('Exactly113 usable marine entries and six separate acquisition holds',len(eligible)==113 and len(ledger['excluded'])==6 and set(eligible)=={e['id'] for e in entries.values() if e['productionEligible']})
check('Production batches cover eligible identities exactly once',len(ledger['batches'])==12 and sorted(i for b in ledger['batches'] for i in b['ids'])==sorted(eligible))
check('Twenty-five designer identities remain under their biological species',sum(len(e['varieties']) for e in entries.values())==25)
required=0
for id,e in entries.items():
    check('Retained original source: '+id,(ROOT/e['existingPath']).is_file())
    if id not in eligible:continue
    slots={(e.get('stageAliases',{}).get(stage,stage),state,None) for stage in e['stages'] for state in e['requiredStates']}
    slots|={(stage,'swim',v['id']) for v in e['varieties'] for stage in ['juvenile','adult']}
    required+=len(slots)
    actual={(c['stage'],c['state'],c.get('variety')) for c in e['clips']}
    check('No duplicate physical animation slots: '+id,len(actual)==len(e['clips']))
    check('Completion never conceals missing biological stages or states: '+id,e['status']!='complete' or slots<=actual)
    if '--require-complete' in sys.argv:check('All required reviewed slots and gameplay checks complete: '+id,slots<=actual and eligible[id]['fullyComplete'])
for e,c in clips:
    name=e['id']+'/'+str(c.get('variety') or 'standard')+'/'+c['stage']+'/'+c['state']
    path=ROOT/c['path'];check('Exact registered PNG SHA: '+name,sha(path)==c['sha256'])
    im=Image.open(path).convert('RGBA');w,h=c['frameWidth'],c['frameHeight'];cols=c['columns']
    check('Correct full16-cell geometry: '+name,im.size==(w*cols,h*(16//cols)) and c['frameCount']==16)
    hashes=[];valid=True
    for i in range(16):
        f=im.crop((i%cols*w,i//cols*h,(i%cols+1)*w,(i//cols+1)*h));alpha=f.getchannel('A');b=alpha.getbbox()
        hashes.append(hashlib.sha256(f.tobytes()).hexdigest())
        valid=valid and b is not None and b[0]>0 and b[1]>0 and b[2]<w and b[3]<h and set(alpha.getdata())<={0,255}
    check('Sixteen distinct whole silhouettes and transparent crisp margins: '+name,valid and len(set(hashes))==16)
    check('Physical pixels match reviewed original-pose evidence: '+name,hashes==c['validation']['frameHashes'] and c['validation']['visualReview'])
for browser in ['chrome','edge']:
    result=json.loads((ROOT/'tests/sprite-production-evidence'/(browser+'-results.json')).read_text(encoding='utf8'))
    covered={(r['path'],r['sha256']) for r in result['coverage']}
    check(browser+': current authored paths tested in real gameplay',result['failed']==0 and all((c['path'],c['sha256']) in covered for _,c in clips))
    check(browser+': maximum stock meets measured30fps budget',result['performance']['fish']==250 and result['performance']['p95Ms']<1000/30)
    if '--require-complete' in sys.argv:
        mixed=result.get('mixedPerformance') or {}
        check(browser+': full mixed marine scene meets measured30fps budget',mixed.get('fish')==250 and mixed.get('corals')==35 and mixed.get('invertebrates')==40 and mixed.get('distinctCorals')==15 and mixed.get('distinctInvertebrates')==9 and mixed.get('acceptedResidentDraws')==75*120 and mixed.get('p95Ms',float('inf'))<1000/30)
master=(ROOT/'MASTER_DEVELOPMENT_PROMPT.md').read_text(encoding='utf8')
continuity=(ROOT/'PROJECT_CONTINUITY_SOURCE.md').read_text(encoding='utf8')
check('Master preserves31 sections and exact embedded continuity',len(re.findall(r'^# \d+\. ',master,re.M))==31 and continuity.count(master)==1)
report=(ROOT/'LIVESTOCK_16_FRAME_SPRITE_PRODUCTION_REPORT.md').read_text(encoding='utf8')
check('Current production report lists every eligible identity',all('`'+id+'`' in report for id in eligible))
manifest=json.loads((ROOT/'DIST/build-manifest.json').read_text(encoding='utf8'))
check('Device-local saves and no server saves remain the build policy','localStorage' in manifest['savePolicy'] and 'no server saves' in manifest['savePolicy'])
with ZipFile(ROOT/'AquariumLife-GitHub-Pages.zip') as archive:
    names=set(archive.namelist())
    check('Portable Pages ZIP CRC and root entry',archive.testzip() is None and 'index.html' in names and not any(n.startswith('DIST/') for n in names))
    check('Current production gallery, registry and report included',{'livestock-animation-review.html','assets/animation/livestock-registry.json','LIVESTOCK_16_FRAME_SPRITE_PRODUCTION_REPORT.md'}<=names)
    for row in manifest['files']:
        name=row['path'];check('Exact current source/DIST/ZIP: '+name,sha(ROOT/name)==row['sha256']==sha(ROOT/'DIST'/name)==hashlib.sha256(archive.read(name)).hexdigest())
    check('Manifest included exactly',archive.read('build-manifest.json')==(ROOT/'DIST/build-manifest.json').read_bytes())
if '--source-archive' in sys.argv:
    with ZipFile(ROOT/'AquariumLife-v0.1.zip') as archive:
        check('Source archive CRC',archive.testzip() is None)
        for name in archive.namelist():
            path=ROOT/name.removeprefix('AquariumLife/')
            check('Exact source archive: '+str(path.relative_to(ROOT)),path.is_file() and path.read_bytes()==archive.read(name))
result={'passed':sum(c['pass'] for c in checks),'failed':sum(not c['pass'] for c in checks),'eligible':len(eligible),'fullyComplete':sum(bool(e['fullyComplete']) for e in eligible.values()),'registeredSheets':len(clips),'requiredPhysicalSlots':required,'authoredCells':16*len(clips),'fullCompletionRequested':'--require-complete' in sys.argv,'builtAt':manifest['builtAt'],'failures':[c for c in checks if not c['pass']]}
print(json.dumps(result,indent=2))
if '--check-only' not in sys.argv:(ROOT/'tests/sprite-production-evidence/release-validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
raise SystemExit(int(result['failed']>0))
