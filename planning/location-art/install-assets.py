"""Copy unmodified ImageGen PNGs and connect central destination presentation."""
from pathlib import Path
import json,shutil,hashlib
r=Path(__file__).resolve().parents[2]
generated=json.loads((r/'planning/location-art/generated-records.json').read_text(encoding='utf8'))
p=r/'assets/diving/art-prompts.json';ledger=json.loads(p.read_text(encoding='utf8'))
assert not any(x['id']==generated[0]['id'] for x in ledger['records'])
for row in generated:
 target=r/row['path'];assert not target.exists()
 shutil.copyfile(row['generatedSource'],target)
 assert hashlib.sha256(target.read_bytes()).digest()==hashlib.sha256(Path(row['generatedSource']).read_bytes()).digest()
 ledger['records'].append({k:v for k,v in row.items() if k!='generatedSource'}|{'originalGeneratedFilename':Path(row['generatedSource']).name,'originalPreservedBy':'Built-in ImageGen; unmodified original PNG copied into project','usage':['destination-preview','in-dive-environment','expedition-result-accent']})
ledger['date']='2026-10-16';p.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
p=r/'assets/diving/registry.json';registry=json.loads(p.read_text(encoding='utf8'))
records={x['id']:x for x in ledger['records']}
for region,row in registry['regions'].items():
 row['art']={}
 for mode in row.get('modes',['reef','deep']):
  key=region+'-'+mode;record=records[key]
  row['art'][mode]={'id':key,'path':record['path'],'description':row['name']+' — '+row['habitat']}
 if 'background' in row:row['background']=row['art'][row['modes'][0]]['path']
registry['presentationVersion']=1
p.write_text(json.dumps(registry,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
(r/'js/diving-data.js').write_text('"use strict";\n// Generated from assets/diving/registry.json; edit the permanent registry.\nAL.DivingData='+json.dumps(registry,separators=(',',':'))+';\n',encoding='utf8')
print('Installed 8 unmodified PNGs; 16 mode-specific destination mappings assigned.')
