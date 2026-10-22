"""Retain all registry IDs, distinguish usable production scope and six holds."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[2]
path=root/'assets/animation/livestock-registry.json';registry=json.loads(path.read_text(encoding='utf8'))
ledger=json.loads((root/'planning/sprite-production/production-ledger.json').read_text(encoding='utf8'))
eligible={e['id']:e for e in ledger['eligible']};held={e['id']:e['reason'] for e in ledger['excluded']}
for e in registry['entries']:
    e['productionEligible']=e['id'] in eligible
    if e['productionEligible']:e['batch']=eligible[e['id']]['batch']
    else:e['productionExclusion']=held[e['id']]
registry['batches']=ledger['batches']
registry['scope']='119 retained marine identities;113 usable production entries;6 existing acquisition holds excluded from sprite production'
path.write_text(json.dumps(registry,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
