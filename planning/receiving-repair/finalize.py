from pathlib import Path
import json
r=Path(__file__).resolve().parents[2]
rows=[];total=0
for label,name in [('Receiving model, UI and real reload — Chrome','receiving-evidence/chrome-results.json'),('Receiving model, UI and real reload — Edge','receiving-evidence/edge-results.json'),('Existing mystery capture/reveal/holding/resale/save protections — Edge','mystery-diving-evidence/edge-results.json')]:
 d=json.loads((r/'tests'/name).read_text(encoding='utf8'));assert d['failed']==0;total+=d['passed'];rows.append(f'| {label} | {d["passed"]} | {d["failed"]} |')
body='''The final source suites completed successfully in isolated browser profiles:

| Executed suite | Passed | Failed |
|---|---:|---:|
'''+ '\n'.join(rows)+f'\n| Total source checks | {total} | 0 |\n\n'+'''Each receiving suite contains 31 model checks and 13 browser/layout/save checks. Tests cover all ten requested categories: every owned destination including legacy freshwater, disabled rejection reasons with actual/required values, valid nominal/physical 80-gal Chalk Bass at 27°C, unsafe water/equipment/cycling/shelter/stock/predator rejection, optional quarantine and active-course restrictions, real owned ID/count/value, health/genes/condition persistence, cleared pending inventory, repeated-action and save replay protections, and existing additive save compatibility. Additional checks verify exact 27.000001°C visibility, unchanged finite deadlines, countdown/live clock, corrected eligibility without reopening, and actual browser reload. Existing mystery regressions cover precommitted survival, expiry mortality, replay receipts and all prior transport outcomes. Tests deliberately choose a successful precommitted draw for the receiving example; gameplay survival is still probabilistic.

UI/layout checks ran at 1920×1080, 1600×900, 1366×768 and 390×844. Screenshots were visually inspected; long check tables scroll inside their own container and failed values remain readable. No uncaught JavaScript exceptions or HTTP/HTTPS gameplay requests occurred. Earlier development fixture errors were corrected; there are no remaining source-suite failures.

The final built-DIST tests run in Chrome and Edge at an HTTP repository subpath, re-executing the 31 receiving model cases alongside the existing diving/mystery/expansion and actual local save/account/export checks. Per-check results and exact final counts are recorded in `tests/pages-evidence/chrome-results.json` and `edge-results.json`. The release verifier requires the new receiving-runtime check and zero failures in both; it also verifies all source/DIST SHA-256 values, ZIP CRCs/root entries, unchanged prior assets, the full 31-section continuity and current source archive. Machine-readable final combined counts are in `tests/receiving-evidence/release-validation.json`.

DIST and AquariumLife-GitHub-Pages.zip are rebuilt after source/docs/layout finalization. AquariumLife-v0.1.zip contains current source/docs/tests without profiles/caches. The final build-manifest.json is authoritative for build time, file count and hashes. No public deployment or player-save edit was performed.
'''
p=r/'DIVING_RECEIVING_REPAIR_REPORT.md';s=p.read_text(encoding='utf8');old='Final execution counts and results are recorded here after the completed runs. No unrun suite is claimed passed. Tests run in isolated QA profiles and never access player browser profiles/saves.';assert old in s;p.write_text(s.replace(old,body,1),encoding='utf8')
print('Finalized receiving source verification report:',total,'passed, zero failed.')
