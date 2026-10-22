"""Mirror the existing stage/morph source policy, without changing biology."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[2]
p=root/'assets/animation/livestock-registry.json';data=json.loads(p.read_text(encoding='utf8'))
motion=json.loads((root/'assets/animation/fish-registry.json').read_text(encoding='utf8'))
for e in data['entries']:
    if e['category']=='fish':e['stageAliases']=motion['species'][e['id']].get('artStages',{})
    for v in e['varieties']:v['sharedEarlyStages']=['baby']
p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
