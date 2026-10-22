"""Collect completed per-asset image jobs without losing in-flight provenance.

Generation callbacks persist each exact request before any central-ledger import.
Only --import mutates the central production ledger, sequentially.
"""
import argparse
import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('batch',type=int);p.add_argument('--import',dest='do_import',action='store_true');p.add_argument('--require-all',action='store_true');a=p.parse_args()
ledger=json.loads((ROOT/'planning/sprite-production/production-ledger.json').read_text(encoding='utf8'))
registry=json.loads((ROOT/'assets/animation/livestock-registry.json').read_text(encoding='utf8'))
runtime={e['id']:e for e in registry['entries']};ready=[];missing=[]
for entry in ledger['eligible']:
    if entry['batch']!=a.batch:continue
    states=runtime[entry['id']]['requiredStates']
    slots=list(dict.fromkeys((entry['id'],runtime[entry['id']].get('stageAliases',{}).get(stage,stage),state,None) for stage in entry['stages'] for state in states))
    slots.extend((v['id'],stage,'swim',v['id']) for v in entry['varieties'] for stage in ['juvenile','adult'])
    for art_id,stage,state,variety in slots:
        suffix='' if entry['category']=='fish' else '-'+state
        path=ROOT/'planning/sprite-production/requests'/(art_id+'-'+stage+suffix+'.json')
        if not path.is_file():missing.append(art_id+'/'+stage+suffix);continue
        job=json.loads(path.read_text(encoding='utf8'))
        if not job.get('prompt') or not job.get('source') or not Path(job['source']).is_file():missing.append(art_id+'/'+stage+suffix);continue
        assert job['id']==entry['id'] and job['stage']==stage and job.get('variety')==variety and job.get('state','swim')==state
        ready.append(job)
manifest=ROOT/'planning/sprite-production/requests'/('batch'+str(a.batch)+'-ready.json')
manifest.write_text(json.dumps(ready,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print(json.dumps({'batch':a.batch,'ready':len(ready),'missing':missing}),flush=True)
if a.do_import:subprocess.run([sys.executable,str(ROOT/'tests/import_livestock16_group.py'),str(manifest)],cwd=ROOT,check=True)
raise SystemExit(int(bool(missing) and a.require_all))
