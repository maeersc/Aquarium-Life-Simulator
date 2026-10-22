"""Record actual final browser results without rewriting the artwork backlog."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[2]
rows=[]
for folder,browser in [('livestock16-evidence','chrome'),('livestock16-evidence','edge'),('pages-evidence','chrome'),('pages-evidence','edge')]:
    result=json.loads((root/'tests'/folder/(browser+'-results.json')).read_text(encoding='utf8'))
    assert result['failed']==0
    rows.append((folder,browser,result))
text='''## Current validation evidence

These are executed software/fallback-art tests. **They do not approve or validate119 missing production animations.** Source timing and existing artwork are tested separately from the synthetic16-cell loader fixtures. Initial Chrome harness failures (malformed nested-loop expression and a snapshot taken before departing autosave) were corrected; the first failure record is retained. The gallery now instruments storage at the first instruction of its own document and verifies zero storage calls and identical contents, rather than confusing the previous game page's autosave with gallery activity.

| Suite | Passed | Failed |
|---|---:|---:|
'''
for folder,browser,result in rows:
    text+=f"|{browser.title()} / {folder}|{result['passed']}|{result['failed']}|\n"
text+='\nPerformance (warm rendering on this QA PC, milliseconds/frame):\n\n| Browser |10 fish |30 fish |94 fish |119 mixed residents |\n|---|---:|---:|---:|---:|\n'
for folder,browser,result in rows[:2]:
    text+='|'+browser.title()+'|'+'|'.join(f"{p['meanMilliseconds']:.2f}" for p in result['performance'])+f"|{result['mixedPerformance']['meanMilliseconds']:.2f}|\n"
text+='''
The first Chrome Pages run timed out at the15-second cold-file readiness check after its hosted checks passed. That failure is retained in `tests/livestock16-evidence/chrome-first-pages-attempt.json`. A rerun with a bounded60-second allowance still required the complete game, renderer and all17 scenery records; it initialized in3.812seconds and passed. No game code or readiness condition was bypassed. The specific reason for that first intermittent timeout was not established; the longer test allowance is not a claim of a repaired game startup calculation.

The mixed workload includes94fish,15coral records and10invertebrates; all resident data remained byte-equivalent. Both browsers tested the actual fish canvas click, correct individual inspector and three-real-second outline expiration; all119entries across supported stages/states in the gallery; offline assets, no network/save traffic; exact11-fish freshwater render output; save migration; anatomy/head/eye/pattern retention; normal6–10requested slots/sec; fixed death; bounded cache; unknown-sheet fallback; malformed/prototype/repeated-cell rejection and a synthetic16-frame anchor/index/loop/rig-bypass fixture. The conch's existing lowercase `Sand forage` label correctly maps to walking. Normal and stress stock numbers are QA fixtures, not a change to real stocking limits.

Performance above is for retained source artwork and current fallbacks. **Decoded/cached production16-frame textures cannot yet be benchmarked across the full roster because zero production sheets exist.** After authored sheets are supplied, every actual cell's visual quality and memory/performance must be rechecked. The frame library is lazy and its extracted cache is bounded at256cells; this does not constitute a measured full-art texture-memory result.

The Pages suites exercise the exact built game at a repository-relative URL, source/manifest hashes, shared119-entry registry, existing global receiving/preparation/economy/offline/local-save regression fixtures, served divingPNG artwork and offline local-file startup. Release verification separately checks source/DIST/ZIP byte identity, original assets/gameplay authority hashes, current local-save policy and exact31-section master continuity. Player saves were not inspected or modified; browsers used dedicated QA profiles.

## Remaining work and completion status

All119 entries remain unfinished for the requested authored16-frame art scope. Source-art requirements are listed individually above; the25 morphs also lack new reviewed sheets. There is no new player artwork approval. No old livestock mortality or biology restriction was bypassed. The rejected image and exact prompt remain reviewable in the development source archive; production DIST contains the gallery and honest report, never that rejected sheet.

**The full16-frame expansion is not complete.** This report must not be used as a claim that all authorized art work is done, and no unconditional completion message is issued for it.
'''
p=root/'LIVESTOCK_ANIMATION_16_FRAME_REPORT.md';s=p.read_text(encoding='utf8');s=s[:s.index('## Current validation evidence')]+text;p.write_text(s,encoding='utf8')
for name in ['TEST_REPORT.md','GITHUB_PAGES_BUILD_REPORT.md']:
    p=root/name;s=p.read_text(encoding='utf8');marker='### Executed v4.0.4 validation\n'
    if marker in s:s=s[:s.index(marker)]+s[s.index('## Livestock16-frame expansion'):]
    heading=s.index('\n');summary='\n'+marker+'\n'+str(sum(r['passed'] for _,_,r in rows))+' browser assertions passed across current Chrome/Edge livestock and Pages suites; zero final failures. Production16-frame sheets completed: **0**. Full artwork expansion remains unfinished; performance and source/DIST checks are detailed in LIVESTOCK_ANIMATION_16_FRAME_REPORT.md. DIST/Pages and source archives are rebuilt after this evidence update.\n\n'
    p.write_text(s[:heading+1]+summary+s[heading+1:],encoding='utf8')
print('Recorded',sum(r['passed'] for _,_,r in rows),'actual browser assertions; full artwork expansion remains unfinished')
