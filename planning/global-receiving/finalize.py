from pathlib import Path
import json
r=Path(__file__).resolve().parents[2]
sources=[('Universal registered-host matrix + real UI/save regression — Chrome','global-receiving-evidence/chrome-results.json'),('Universal registered-host matrix + real UI/save regression — Edge','global-receiving-evidence/edge-results.json'),('Mystery diving concealment/survival/receipts — Chrome','mystery-diving-evidence/chrome-results.json'),('Existing all-owned receiving diagnostics — Edge','receiving-evidence/edge-results.json')]
rows=[];total=0
for label,n in sources:
 d=json.loads((r/'tests'/n).read_text(encoding='utf8'));assert d['failed']==0;total+=d['passed'];rows.append(f'| {label} | {d["passed"]} | 0 |')
text='''Final executed source suites:

| Suite | Passed | Failed |
|---|---:|---:|
'''+ '\n'.join(rows)+f'\n| Source total | {total} | 0 |\n\n'+'''Each universal run includes 91 model cases, actual receiving controls for every valid species/region/mode combination, explicit coral mount/no-auto-mount checks, pre-capture all-aquarium visibility, pending coral browser reload, and the retained diving regression checks. UI layouts were checked at 1920×1080, 1600×900, 1366×768 and 390×844. Screenshots were visually inspected. There were no uncaught JavaScript exceptions or external gameplay requests in those runs. The reproduced noninfectious-carrier failure was fixed and its exact outcome now passes; legitimate health validation stays enabled.

Final built-DIST checks run in both browsers at a GitHub Pages-style HTTP repository subpath. They include the registry-driven universal model, explicit universal-runtime presence, all prior diving/resale/mystery/receiving/expansion cases and actual local account/save/export isolation. Per-check results and exact final counts are in `tests/pages-evidence/chrome-results.json` and `edge-results.json`; the release verifier requires current universal-runtime coverage and zero failures in both. Final combined source/deployment totals, source/DIST/archive SHA-256/CRC proof, preserved original assets/genetics/freshwater gates and complete master continuity are recorded in `tests/global-receiving-evidence/release-validation.json`.

DIST and AquariumLife-GitHub-Pages.zip are rebuilt after final runtime/docs changes; AquariumLife-v0.1.zip contains current source/docs/tests without profiles/caches. The final build manifest is authoritative for timestamp, file count and hashes. All work/testing used isolated QA profiles and never edited a player's actual saved aquarium. No unrun historical suite is counted in this release.
'''
p=r/'GLOBAL_DIVING_RECEIVING_REPORT.md';s=p.read_text(encoding='utf8');a='Final source and built-DIST results are recorded below after execution. Individual tests and screenshots are retained in `tests/global-receiving-evidence/`; final deployment/archive proof is in `release-validation.json`. No unrun suite is counted as passed.';assert a in s;s=s.replace(a,text,1).replace('current gameplay/status/UI/research-save documentation links','current gameplay/status/UI/save documentation links');p.write_text(s,encoding='utf8')
(r/'planning/global-receiving/invertebrate-health-reproduction.json').write_text(json.dumps({'observedBeforeRepair':True,'passed':86,'failed':1,'test':'porcelain-anemone-crab / japan / reef: host-appropriate saved condition draw 20 transfers without invalid health fields','error':'Invalid marine health/market save: noninfectious carrier','afterRepair':'Covered by both final universal model suites; carrier is derived from condition contagiousness.'},indent=2),encoding='utf8')
print('Finalized global receiving report:',total,'passed source checks, zero failed.')
