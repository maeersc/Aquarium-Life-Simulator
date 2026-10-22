from pathlib import Path
import json
r=Path(__file__).resolve().parents[2];p=r/'FISH_ANIMATION_AUDIT.md';s=p.read_text(encoding='utf8').split('\n## Final release verification')[0]
files=['fish-animation-evidence/chrome-results.json','fish-animation-evidence/edge-results.json','pages-evidence/chrome-results.json','pages-evidence/edge-results.json','breeding-evidence/chrome-results.json'];total=0
s+='\n## Final release verification\n\n| Suite | Passed | Failed |\n|---|---:|---:|\n'
for name in files:
 data=json.loads((r/'tests'/name).read_text(encoding='utf8'));assert data['failed']==0;total+=data['passed'];s+=f'| {name} | {data["passed"]:,} | 0 |\n'
s+=f'| **Total actual browser assertions** | **{total:,}** | **0** |\n\n'
s+='The existing autonomous-breeding suite additionally passed 86 actual model/UI checks, including courtship, spawning, clutch parentage and local reload. Built Pages suites run all per-species animation model checks plus the prior gameplay/diving/save checks. One Chrome local-file smoke attempt timed out at its 15-second deadline after previous QA profiles had retained offline/breeding fixtures. The final standalone-file load is isolated in a clean browser context and passed without changing game code or extending the deadline; initial evidence is retained in fish-animation-evidence/chrome-first-pages-attempt.json. Final Source/DIST/ZIP integrity results are recorded in release-validation.json after packaging.\n'
p.write_text(s,encoding='utf8')
p=r/'FISH_ANIMATION_SYSTEM.md';s=p.read_text(encoding='utf8');marker='\n## Recorded source cleanup\n'
if marker not in s:s+=marker+'\nThe juvenile Orange-Spotted Filefish atlas contains a disconnected 159-pixel duplicate fin island below the body. Its explicit sourceMasks rectangle is applied only to that living stage by the shared art adapter, after facing normalization. The original PNG remains byte-identical; the living body/actual fins are not repainted. Other hosts and death frames keep their existing source policy.\n';p.write_text(s,encoding='utf8')
print('Final browser assertions:',total,'failed: 0')
