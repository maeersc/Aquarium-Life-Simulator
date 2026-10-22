from pathlib import Path
import json
r=Path(__file__).resolve().parents[2]
suites=[('Mystery model + real controls/reload/export — Chrome','mystery-diving-evidence/chrome-results.json'),('Mystery model + real controls/reload/export — Edge','mystery-diving-evidence/edge-results.json'),('Existing diving/oxygen/receiving/resale — Edge','diving-evidence/edge-results.json'),('Automatic breeding + live/offline parity — Chrome','breeding-evidence/chrome-results.json'),('Heater + permanent mortality journal — Edge','heater-evidence/edge-results.json'),('Store destinations/equipment/research/casino/header — Edge','store-casino-evidence/edge-results.json'),('Built DIST / Pages subpath / local saves + mystery model — Chrome','pages-evidence/chrome-results.json'),('Built DIST / Pages subpath / local saves + mystery model — Edge','pages-evidence/edge-results.json')]
rows=[];total=0
for label,n in suites:
 d=json.loads((r/'tests'/n).read_text());assert d['failed']==0,(n,d['failed'])
 if n.startswith('pages-evidence'):assert any(x['name'].startswith('Built v3.9 mystery authority') and x['pass'] for x in d['results'])
 total+=d['passed'];rows.append(f'| {label} | {d["passed"]} | 0 |')
evidence='''All final selected checks passed. Commands use isolated QA browser profiles, never player profiles/saves. Full evidence JSON/screenshots remain in the corresponding tests folders.

| Suite | Passed | Failed |
|---|---:|---:|
'''+ '\n'.join(rows)+f'\n| **Total** | **{total}** | **0** |\n\n'+'''The mystery model covers 100 seeded expeditions in each of six valid region/mode combinations, plus an 800-seed Fiji Reef selection check (392 Exquisite wrasse / 408 butterflyfish). It tests range/capacity/eight slots, duplicate clicks, abandoned/exhausted forfeiture, geographic/depth/closed/empty-pool guards, save/reveal/recovery/receipt persistence, all five transport outcomes, alternate safe receivers, unsafe/missing receiver rejection, actual offline expiry/live parity/repeated login, account journal isolation and legacy trip compatibility. The actual browser suite exercises left/right clicks, question-mark art, pre-return concealment, real reloads, explicit receiving, live clock/equipment, responsive results at 1920×1080 / 1600×900 / 1366×768 / 390×844, and a real local mortality JSON download. Screenshots were visually inspected. No uncaught JavaScript exceptions or external gameplay requests were found.

All 19 requested acceptance categories are covered: (1–3) both modes + reachability/return; (4–5) hidden identity + original silhouette; (6–7) range/capacity/eight slots; (8) failed-dive forfeiture; (9) boat reveal; (10–11) region/depth eligibility; (12–13) persisted identity/no duplicate; (14–15) all survival states/safe receiving; (16) existing resale regressions; (17) real shared clock and breeding/live-offline regressions; (18) production freshwater lock; (19) offline resources/local saves. Built-DIST checks repeat the diving/mystery model and actual origin/profile/save/export protections under a repository URL subpath.

During development one new receiver fixture initially reused a rock ID; that test fixture was corrected to allocate unique identities. An initial UI assertion returned a DOM element rather than a Boolean; it was corrected. Final suites have zero failures. Older broad legacy runners that expect unlocked freshwater were not used as current production acceptance; no production lock was removed. No unrun historical suite is counted in this release total.

DIST, AquariumLife-GitHub-Pages.zip and the compatibility-named AquariumLife-v0.1.zip source archive are rebuilt from current source. Final SHA-256/source/DIST/archive checks, CRCs, manifest counts and protected-art/continuity verification are recorded in tests/mystery-diving-evidence/release-validation.json. The build-manifest.json is authoritative for the final timestamp and byte count. Only report text/evidence is finalized after runtime QA; no game calculation changes follow those tests.
'''
p=r/'MYSTERY_DIVING_UPDATE_REPORT.md';s=p.read_text(encoding='utf8');old='Final suite counts, deployment hashes and acceptance mapping are recorded below after the final runs. Current evidence JSON records individual checks and any failures; no unrun suite is treated as passed.';assert old in s;p.write_text(s.replace(old,evidence,1),encoding='utf8')
note=f'''## v3.9 final verified release — 2026-10-15

**{total} selected browser/model/deployment checks passed, zero failed.** Both browsers passed the mystery feature and built Pages/local-save flows; existing diving/resale, automatic breeding, heater/mortality and store/casino/header regressions passed. Viewports: 1920×1080, 1600×900, 1366×768 and 390×844. See [MYSTERY_DIVING_UPDATE_REPORT.md](MYSTERY_DIVING_UPDATE_REPORT.md) for exact suites, all 19 acceptance categories, changed files and limits. DIST and both ZIPs are current; source/DIST/ZIP hashes and CRC checks are independently verified. Browser saves, receipts and mortality history remain local. No public deployment was performed.

'''
for n in ['DEVELOPMENT_STATUS.md','TEST_REPORT.md','GITHUB_PAGES_BUILD_REPORT.md']:
 p=r/n;s=p.read_text(encoding='utf8');pos=s.index('\n\n')+2;p.write_text(s[:pos]+note+s[pos:],encoding='utf8')
print(f'Finalized report: {total} passed, zero failed.')
