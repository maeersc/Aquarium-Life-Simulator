from pathlib import Path
import json
R=Path(__file__).resolve().parents[2]
E=R/'tests/distribution-protection-evidence'
paths=[('Chrome protected file://',E/'chrome-protected.json'),('Edge protected file://',E/'edge-protected.json'),('Matched startup/render/biology benchmark',E/'chrome-benchmark.json'),('Identical-video repeated benchmark',E/'chrome-media.json'),('Fresh-process hidden CPU check',E/'chrome-idle.json'),('Edge Pages/subpath/local-save suite',R/'tests/pages-evidence/edge-results.json'),('Chrome protected tutorial',R/'tests/tutorial-audit-evidence/chrome-results.json'),('Chrome protected economy/casino',R/'tests/economy-update-evidence/chrome-results.json'),('Chrome protected equipment/offline',R/'tests/equipment-reliability-evidence/chrome-results.json'),('Chrome protected breeding',R/'tests/breeding-evidence/chrome-results.json')]
rows=[]
for title,p in paths:
 d=json.loads(p.read_text(encoding='utf8'));assert d['failed']==0,(title,d['failed']);rows.append((title,d['passed'],d['failed']))
soak=json.loads((E/'chrome-soak.json').read_text(encoding='utf8'));assert all(x['pass'] for x in soak['checks']);rows.append(('Five-minute protected navigation/heap/listener soak',sum(x['pass'] for x in soak['checks']),0))
total=sum(x[1] for x in rows)
bench=json.loads((E/'chrome-benchmark.json').read_text(encoding='utf8'));media=json.loads((E/'chrome-media.json').read_text(encoding='utf8'));idle=json.loads((E/'chrome-idle.json').read_text(encoding='utf8'))
before=bench['measurements']['development'];after=bench['measurements']['protected'];b={x['label']:x for x in before['samples']};a={x['label']:x for x in after['samples']}
measure='''The final expression-preserving configuration passed all matched comparisons. Gameplay expression rewrites are disabled; scope-local identifier shortening, whitespace/comment removal, hashed code filenames and lightweight CSS minification remain. No runtime decoding, animation loop, timer or render work is added. Build output is cached by source/options/tool versions and active native sources/transports are checked before deployment. Original gameplay rendering/simulation code is not edited.

Initial evidence exposed an unpaired-media FPS failure and a15.36-second startup outlier. Investigation found the comparisons were mixing warm source code with newly named code and independently recorded video streams. The exact cause of that single slow start was not proven. Final measurements use a clean disposable browser profile/process per build; the media follow-up uses the exact same50361-byte640x360VP8 WebM and3 warmed5-second windows per build. Initial evidence is retained under initial-compression and expression-preserving-initial. These method corrections retain strict relative regression checks; they do not claim that the earlier differences were conclusively caused by expression compression.

| Metric | Development | Protected |
| --- | ---: | ---: |
'''
measure+=f'| Clean-profile document startup |{before["startupSeconds"]:.3f}s|{after["startupSeconds"]:.3f}s|\n'
measure+=f'| Startup main-thread task time |{before["startupTaskSeconds"]:.3f}s|{after["startupTaskSeconds"]:.3f}s|\n'
for key in ['A','B','C','D']:
 measure+=f'| Scene{key}, {b[key]["state"]["fish"]} fish / {b[key]["state"]["tanks"]} tank(s), FPS |{b[key]["fps"]:.2f}|{a[key]["fps"]:.2f}|\n'
 measure+=f'| Scene{key} main-thread cost, one CPU core |{b[key]["mainThreadCorePercent"]:.2f}%|{a[key]["mainThreadCorePercent"]:.2f}%|\n'
measure+=f'| Post-GC JavaScript heap |{before["gcHeapBytes"]:,}bytes|{after["gcHeapBytes"]:,}bytes|\n'
md,mp=media['development'],media['protected']
measure+=f'| Same-video median game FPS |{md["medianFps"]:.2f}|{mp["medianFps"]:.2f}|\n| Same-video median one-core main-thread cost |{md["medianCorePercent"]:.2f}%|{mp["medianCorePercent"]:.2f}%|\n| Same-video median Canvas draw p95 |{md["medianDrawP95"]:.2f}ms|{mp["medianDrawP95"]:.2f}ms|\n| Same-video dropped/total video frames |{md["quality"]["dropped"]}/{md["quality"]["total"]}|{mp["quality"]["dropped"]}/{mp["quality"]["total"]}|\n'
measure+=f'| Fresh-process steady hidden one-core cost |{idle["rows"][0]["mainThreadCorePercent"]:.3f}%|{idle["rows"][1]["mainThreadCorePercent"]:.3f}%|\n'
measure+='''
Both60 and30FPS pacing checks passed, as did exact mixed-tank biological/water/clock/wallet state after3456 five-minute steps (12game days). Covered store/equipment/journal/diving and hidden aquariums produced no Canvas draws. Fresh-process hidden traces contained no game callbacks or scheduled RAF/timer. A shared-process diagnostic had garbage-collector work after disposing the previous large document; clean-process profiler samples were idle. The original transient post-video observation is retained in the full benchmark rather than misrepresented as steady game work.

'''
heaps=soak['heapSamples'];growth=heaps[-1]['heapBytes']-heaps[0]['heapBytes'];listeners=[x['listeners'] for x in heaps];saves=soak['calls'].get('save',{}).get('count',0)
measure+=f'The five-minute run made60 menu round trips and{saves} ordinary autosaves. Post-warm-up GC heap changed by{growth:,}bytes; listener counts ranged from{min(listeners)} to{max(listeners)}. Native/frame/raster/color caches remained within their existing byte limits. All four soak assertions passed.\n\n'
measure+='''Measurements are headless Chromium with software Canvas (--disable-gpu), not whole-system CPU or physical GPU telemetry. JS heap excludes compiled source, decoded images, Canvas buffers and GPU memory; cache ceilings are reported separately in evidence. Short samples vary and do not establish a general speedup. Physical GPU/VRAM, real Netflix/DRM/audio-sync and all-hardware cold-start performance remain unmeasured. Large original embedded fallback banks and PNGs still dominate distribution size; their approved quality was preserved.
'''
validation='| Executed suite | Passed | Failed |\n| --- | ---: | ---: |\n'+''.join(f'|{title}|{passed}|{failed}|\n' for title,passed,failed in rows)+f'|**Total**|**{total}**|**0**|\n\n'
validation+='''Both Chrome and Edge execute the actual protected file-origin game with network disabled. Each805-check suite validates all382 native sheets/all6112 cells, frame geometry/eyes/anchors, stable public interfaces, performance settings/clock independence, bulk Store delivery, separate equipment IDs, Inventory, freshwater lock and exact local profile reload. The hosted suite independently checks the protected manifest/private source mapping, HTTP repository subpath/native URLs, global receiving/diving/mystery systems, financial/medical/research features, exports/imports and local file launch. It includes large deterministic Monte Carlo batches; its CDP evaluation timeout was extended from the generic20 seconds to300 seconds so the unchanged assertions can finish. Final5162 checks passed.

The full trusted-input tutorial completed all22 milestones with the genuine90-second accelerated fishless cycle; economy/casino/pair offers, equipment/8-12-24-hour live-offline parity/repeated-login guards and natural breeding all passed against DIST. Original gameplay code/art hashes remain unchanged. No test result is inferred from a source-only run.

`python tests/verify_protected_release.py --source-archive --check-only` checks original2906 files, public/private checksums, exact PNG callback bytes, no source maps/development files, both ZIPs, every private archived source byte, current benchmark build IDs and exact31-section master/continuity. Repeated same-environment builds must reproduce the exact output manifest and Pages ZIP checksum. Original named-code mirror verifiers describe older unprotected releases; use this production-aware verifier for the protected folder. Review-gallery browser QA remains available against the unchanged development root; production deliberately omits galleries.
'''
p=R/'DISTRIBUTION_PROTECTION_REPORT.md';s=p.read_text(encoding='utf8');s=s.replace('The protected pipeline is implemented. Final performance and regression validation is in progress; this report is finalized with actual results before completion.',f'Protected production is implemented and validated. All{total} executed browser/performance/regression assertions passed. Original source and art remain unchanged; production/source ZIP verification and deterministic rebuild evidence are checked separately.')
start=s.index('Final matched benchmark, soak and regression results pending.');end=s.index('\n## Actual validation',start);s=s[:start]+measure+s[end:]
start=s.index('Chrome and Edge each passed805 protected-runtime checks');end=s.index('\n## Files changed',start);s=s[:start]+validation+s[end:]
s=s.replace('protection_performance_qa.py and verify_protected_release.py','protection_performance_qa.py, protection_media_qa.py, protection_idle_qa.py and verify_protected_release.py')
p.write_text(s,encoding='utf8')
for f in ['DEVELOPMENT_STATUS.md','TEST_REPORT.md','GITHUB_PAGES_BUILD_REPORT.md']:
 p=R/f;s=p.read_text(encoding='utf8');needle='Earlier build descriptions are historical where superseded.';s=s.replace(needle,f'All{total} executed protected browser/performance/regression assertions passed; exact results, methods and limits are in the protection report and tests/distribution-protection-evidence. '+needle,1);p.write_text(s,encoding='utf8')
print(json.dumps({'browserAssertions':total,'allPassed':True,'soakHeapGrowth':growth,'soakAutosaves':saves},indent=2))
