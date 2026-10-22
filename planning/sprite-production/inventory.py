"""Snapshot usable runtime identities before actual bitmap production."""
import hashlib
import json
from pathlib import Path
root=Path(__file__).resolve().parents[2]
source=json.loads((root/'tests/livestock16-evidence/catalog-before.json').read_text(encoding='utf8'))
registry=json.loads((root/'assets/animation/livestock-registry.json').read_text(encoding='utf8'))
original={e['id']:e for e in registry['entries']}
eligible=[];excluded=[]
for row in source:
    if row.get('purchaseVerified') is False or row.get('acquisitionHold'):
        excluded.append({'id':row['id'],'reason':row.get('acquisitionHold') or 'Existing acquisition hold; not usable livestock'})
        continue
    e=original[row['id']]
    eligible.append({'id':row['id'],'name':row['name'],'scientificName':row.get('scientificName'),'category':row['category'],'batch':len(eligible)//10+1,'existingPath':e['existingPath'],'profile':e['profile'],'stages':e['stages'],'varieties':e['varieties'],'production':{},'fullyComplete':False,'state':'queued'})
assert len(eligible)==113 and len(excluded)==6
folder=root/'planning/sprite-production';folder.mkdir(exist_ok=True)
out={'version':1,'scope':'Usable saltwater livestock only; original119-record audit retained separately','eligible':eligible,'excluded':excluded,'batches':[{'number':b,'ids':[e['id'] for e in eligible if e['batch']==b],'status':'queued'} for b in range(1,13)]}
(folder/'production-ledger.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
paths=[*root.glob('js/*.js'),*root.glob('assets/**/*.png'),root/'index.html',root/'MASTER_DEVELOPMENT_PROMPT.md',root/'PROJECT_CONTINUITY_SOURCE.md']
(folder/'baseline-hashes.json').write_text(json.dumps({p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},indent=2)+'\n',encoding='utf8')
print('Logged113 usable entries (89fish,15corals,9invertebrates),12 production batches;6 held records excluded')
