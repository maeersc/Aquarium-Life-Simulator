"""Sequential technical import of completed built-in image jobs; no art approval."""
import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
jobs=json.loads(Path(sys.argv[1]).read_text(encoding='utf8'))
for job in jobs:
    art_id=job.get('variety') or job['id'];stage=job['stage']
    motion=job.get('state','swim')
    request=ROOT/'planning/sprite-production/requests'/(art_id+'-'+stage+('-'+motion if motion!='swim' else '')+'.json')
    request.parent.mkdir(parents=True,exist_ok=True);request.write_text(json.dumps(job,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    ledger=json.loads((ROOT/'planning/sprite-production/production-ledger.json').read_text(encoding='utf8'))
    entry=next(e for e in ledger['eligible'] if e['id']==job['id']);slot=('variety:'+job['variety']+':' if job.get('variety') else '')+stage+(':'+motion if entry['category']!='fish' else '')
    if entry['production'].get(slot,{}).get('state','').startswith('registered') and not job.get('replace'):continue
    command=[sys.executable,str(ROOT/'tests/import_livestock16_source.py'),job['id'],stage,job['source']]
    if job.get('variety'):command+=['--variety',job['variety']]
    if job.get('revision'):command+=['--revision',str(job['revision'])]
    if job.get('state'):command+=['--state',job['state']]
    subprocess.run(command,cwd=ROOT,check=True)
