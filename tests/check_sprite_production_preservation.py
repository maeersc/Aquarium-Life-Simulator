"""Compare original runtime/art authorities to the pre-production snapshot."""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
baseline=json.loads((ROOT/'planning/sprite-production/baseline-hashes.json').read_text(encoding='utf8'))
allowed={'js/fish-animation.js','js/fish-animation-data.js','js/livestock-animation-data.js','js/livestock-animation-review.js','js/render.js','js/expansion-ui.js','index.html','MASTER_DEVELOPMENT_PROMPT.md','PROJECT_CONTINUITY_SOURCE.md'}
checks=[]
for name,expected in baseline.items():
    if name in allowed:continue
    path=ROOT/name;actual=hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None
    checks.append({'path':name,'pass':actual==expected,'sha256':actual,'expected':expected})
report={'passed':sum(c['pass'] for c in checks),'failed':sum(not c['pass'] for c in checks),'checks':checks,'scope':'Original PNGs and unchanged runtime, biology, economy, account/save and freshwater authorities; explicitly authorized presentation/docs changes excluded.'}
out=ROOT/'tests/sprite-production-evidence/preservation.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(json.dumps({'passed':report['passed'],'failed':report['failed'],'failures':[c['path'] for c in checks if not c['pass']]}))
raise SystemExit(int(report['failed']>0))
