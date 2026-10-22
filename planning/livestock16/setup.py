"""One-time audit import; does not synthesize missing authored artwork."""
import json
import shutil
from pathlib import Path

root=Path(__file__).resolve().parents[2]
rows=json.loads((root/'tests/livestock16-evidence/catalog-before.json').read_text(encoding='utf8'))
assert len(rows)==119 and len({r['id'] for r in rows})==119
entries=[]
for index,r in enumerate(rows):
    meta=r['meta'] or {}
    source=meta.get('atlas') or meta.get('path')
    if not source:
        if meta.get('batch')=='v2.9':
            source=f"assets/expansion-v29/{r['id']}/atlas-v1.png"
        else:
            # AssetBank original legacy corals use an explicit path in metadata.
            source=meta.get('file')
    assert source and (root/source).is_file(), (r['id'],source,list(meta))
    if r['category']=='fish':
        stages=['baby','juvenile','adult']
        required=['swim']
        missing='Separate aligned 16-pose life-stage swim cycles and exposed pectoral clean plates; preserve existing head, markings and early anatomy. Existing one/four-pose sources cannot supply sixteen authored poses.'
        profile=json.loads((root/'assets/animation/fish-registry.json').read_text())['species'][r['id']]['family']
    elif r['category']=='coral':
        stages=['frag','colony']; required=['polyp_motion'];profile='polyp-only'
        missing='Isolated polyp/tentacle layers and sixteen reviewed polyp poses; retain a fixed skeleton, attachment and existing health-state art. Do not bend the whole colony or fabricate visible motion on rigid tissue.'
    else:
        stages=['baby','juvenile','adult']; required=['idle','walk'];profile=r.get('shape') or 'invertebrate'
        missing='Separate leg/antenna/foot or filtering-fan layers and sixteen reviewed idle/walk poses; preserve shell/body anchor. Settled early artwork is not a verified planktonic larva.'
    if r['id']=='clown':
        source='assets/livestock/fish/clownfish/clownfish-benchmark-v1-128.png'
        missing+=' Generated adult candidate rejected for cell-boundary overlap and head/body drift.'
    entries.append(dict(id=r['id'],name=r['name'],scientificName=r['scientificName'],category=r['category'],water='marine',batch=index//10+1,profile=profile,existingPath=source,existingFrameCount=r['adultFrames'],stages=stages,requiredStates=required,status='artwork-required',framesCompleted=0,clips=[],missingArtwork=missing,userApproved=False,acquisitionHold=r.get('acquisitionHold'),varieties=[{'id':v['id'],'name':v['name'],'existingPath':v['meta'].get('atlas') or v['meta'].get('path')} for v in r['varieties']]))
registry={'version':1,'scope':'All runtime marine livestock; visual-only; incomplete artwork is never counted as a production sheet','frameCount':16,'frameOrder':list(range(16)),'normalFishFramesPerSecond':[6,10],'entries':entries,'batches':[{'number':b,'ids':[e['id'] for e in entries if e['batch']==b],'status':'audited; missing authored artwork recorded; no production completion claimed'} for b in range(1,13)],'candidates':[]}
p=root/'assets/animation/livestock-registry.json';p.write_text(json.dumps(registry,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print('Audited',len(entries),'entries in',len(registry['batches']),'batches;',sum(len(e['varieties']) for e in entries),'varieties retained')
