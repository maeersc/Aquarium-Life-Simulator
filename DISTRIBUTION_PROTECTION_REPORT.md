# Protected production distribution - v1

Protected production is implemented and validated. All7838 executed browser/performance/regression assertions passed. Original source and art remain unchanged; production/source ZIP verification and deterministic rebuild evidence are checked separately.

## Mechanisms and limits

| Mechanism | Implemented | What it does / does not do |
| --- | --- | --- |
| Minification | Terser5.44.0 JS and clean-css5.3.3 CSS | Removes comments/whitespace and compacts syntax. Not encryption. |
| Obfuscation | Scope-local identifier shortening and content-derived runtime filenames | Deters casual reading; preserves global AL/property/species/save identifiers. Browser code can still be recovered and edited. |
| Compression | Deterministic ZIP DEFLATE | Reduces archive/transfer size; extractable, not access control. |
| Integrity checks | Public output SHA-256 manifest, ZIP CRC, private source/output hashes | Detects corruption and verifies the actual build. An attacker controlling both code and manifest can replace them. |
| Encryption | Not applied to game code, assets or saves | No false secrecy claims, passwords, embedded secret master key or online license dependency. |

The first expression-compressed gameplay variant failed the local-video FPS regression check. The final configuration retains internal-name mangling but disables gameplay expression rewrites. Literal art banks and the single-call file transports remain compact; no expensive runtime decoding, control-flow flattening, anti-debugging loops or debugger traps are introduced. Fresh browser processes are used for final development/protected comparisons, with explicit local-video decoder cleanup. Initial evidence is retained separately.

## Development and production separation

Original155 runtime HTML/JS/CSS files and2751 asset files are retained byte-for-byte (2906 files total). Production does not run source generators or overwrite original files. The standard index.html, review galleries and full tests remain usable in development.

DIST contains only index.html, required local assets, hashed/minified scripts/styles, .nojekyll, an output checksum manifest and a short LICENSE.txt notice. No review HTML, Markdown project documentation, art-generation prompts, private mapping records, unminified named code copies, tests, build tools, source maps, archives or player data ship. The Settings developer artwork links are removed only from the transformed CareUI input; its human-readable source remains unchanged. Existing gameplay diagnostics, save recovery and public runtime interfaces remain available.

The public manifest lists output paths and checksums. Private source-to-output mapping, tool versions/options, minifier/cache records and original hashes remain under planning/distribution-protection, outside DIST. Runtime code filenames use SHA-256-derived20-character suffixes. Local property names, species IDs, biology/configuration values and saved fields are not renamed. Deferred classic-script order and relative CSS asset paths remain unchanged.

## Assets and encryption feasibility

Native PNGs are lossless and unchanged. Existing fish/coral/invertebrate/background/interface assets are copied only through the game dependency closure. Development-only records and review pages are excluded.382 native animation sheets retain all6112 authored cells, anchors, eyes and frame metadata; previously missing shrimp sheets keep their original approved fallback art. Normal HTTP uses native PNGs; file:// uses existing per-sheet classic-script callbacks with exactly the same PNG bytes. The two representations support different browser-origin constraints and do not both decode during one load. No decryption occurs during animation frames.

AES-GCM could authenticate/encrypt bytes if an independent key-management system existed, but an offline auto-loading browser game must supply the client all resources required to display its art. A key bundled with the client cannot remain secret from that recipient. Password-based keys would need an approved password/recovery flow; online keys would violate the offline requirement; local-keystore integration would require a different launcher and migration design. None is introduced. Artwork remains viewable, extractable and copyable; packaging is a practical distribution measure, not asset secrecy.

Saves remain local under existing storage keys and schema2/tutorial2. No encryption, automatic profile rewrite, authentication change or recovery-key requirement. The existing DIST/index.html path remains; moving between site/browser origins still requires explicit export/import.

## Build and private source commands

```powershell
python tools/production/bootstrap.py
python build.py
python tests/package.py
```

The first command is one-time private build tooling setup. Windows uses portable Node22.23.0 downloaded from nodejs.org and checked against its official SHA256 list; npm packages are version-pinned and lockfile-integrity-checked with install scripts/audit/network notices disabled. No global PATH or runtime installation is changed. Afterwards the build uses local tools with no package download. A fresh checkout/private source archive needs that one-time setup (or equivalent installed Node and locked local modules). Players need only their browser and the generated folder, never Node/npm/Python or a server.

Upload only DIST's contents or AquariumLife-GitHub-Pages.zip. AquariumLife-v0.1.zip is the separate private human-readable development archive and must not be deployed. Rebuilds stage/validate outputs before replacing the generated DIST, verify source preservation and CRC-check the ZIP. Fixed ZIP entry timestamps and stable output manifests make repeated builds byte-identical under the same pinned environment; actual creation evidence lives privately. Checksums are not encryption or independent signatures.

## Performance & Optimization

The final expression-preserving configuration passed all matched comparisons. Gameplay expression rewrites are disabled; scope-local identifier shortening, whitespace/comment removal, hashed code filenames and lightweight CSS minification remain. No runtime decoding, animation loop, timer or render work is added. Build output is cached by source/options/tool versions and active native sources/transports are checked before deployment. Original gameplay rendering/simulation code is not edited.

Initial evidence exposed an unpaired-media FPS failure and a15.36-second startup outlier. Investigation found the comparisons were mixing warm source code with newly named code and independently recorded video streams. The exact cause of that single slow start was not proven. Final measurements use a clean disposable browser profile/process per build; the media follow-up uses the exact same50361-byte640x360VP8 WebM and3 warmed5-second windows per build. Initial evidence is retained under initial-compression and expression-preserving-initial. These method corrections retain strict relative regression checks; they do not claim that the earlier differences were conclusively caused by expression compression.

| Metric | Development | Protected |
| --- | ---: | ---: |
| Clean-profile document startup |2.328s|2.453s|
| Startup main-thread task time |1.169s|1.225s|
| SceneA, 1 fish / 1 tank(s), FPS |60.01|60.06|
| SceneA main-thread cost, one CPU core |9.81%|6.93%|
| SceneB, 8 fish / 1 tank(s), FPS |59.98|59.97|
| SceneB main-thread cost, one CPU core |11.67%|8.93%|
| SceneC, 32 fish / 1 tank(s), FPS |60.04|59.91|
| SceneC main-thread cost, one CPU core |14.88%|13.74%|
| SceneD, 32 fish / 4 tank(s), FPS |59.98|60.14|
| SceneD main-thread cost, one CPU core |14.82%|11.77%|
| Post-GC JavaScript heap |7,332,280bytes|7,335,808bytes|
| Same-video median game FPS |59.38|59.97|
| Same-video median one-core main-thread cost |16.07%|16.05%|
| Same-video median Canvas draw p95 |2.50ms|2.40ms|
| Same-video dropped/total video frames |3/541|3/541|
| Fresh-process steady hidden one-core cost |0.036%|0.022%|

Both60 and30FPS pacing checks passed, as did exact mixed-tank biological/water/clock/wallet state after3456 five-minute steps (12game days). Covered store/equipment/journal/diving and hidden aquariums produced no Canvas draws. Fresh-process hidden traces contained no game callbacks or scheduled RAF/timer. A shared-process diagnostic had garbage-collector work after disposing the previous large document; clean-process profiler samples were idle. The original transient post-video observation is retained in the full benchmark rather than misrepresented as steady game work.

The five-minute run made60 menu round trips and15 ordinary autosaves. Post-warm-up GC heap changed by1,273,804bytes; listener counts ranged from480 to480. Native/frame/raster/color caches remained within their existing byte limits. All four soak assertions passed.

Measurements are headless Chromium with software Canvas (--disable-gpu), not whole-system CPU or physical GPU telemetry. JS heap excludes compiled source, decoded images, Canvas buffers and GPU memory; cache ceilings are reported separately in evidence. Short samples vary and do not establish a general speedup. Physical GPU/VRAM, real Netflix/DRM/audio-sync and all-hardware cold-start performance remain unmeasured. Large original embedded fallback banks and PNGs still dominate distribution size; their approved quality was preserved.

## Actual validation

| Executed suite | Passed | Failed |
| --- | ---: | ---: |
|Chrome protected file://|805|0|
|Edge protected file://|805|0|
|Matched startup/render/biology benchmark|26|0|
|Identical-video repeated benchmark|4|0|
|Fresh-process hidden CPU check|2|0|
|Edge Pages/subpath/local-save suite|5162|0|
|Chrome protected tutorial|72|0|
|Chrome protected economy/casino|85|0|
|Chrome protected equipment/offline|787|0|
|Chrome protected breeding|86|0|
|Five-minute protected navigation/heap/listener soak|4|0|
|**Total**|**7838**|**0**|

Both Chrome and Edge execute the actual protected file-origin game with network disabled. Each805-check suite validates all382 native sheets/all6112 cells, frame geometry/eyes/anchors, stable public interfaces, performance settings/clock independence, bulk Store delivery, separate equipment IDs, Inventory, freshwater lock and exact local profile reload. The hosted suite independently checks the protected manifest/private source mapping, HTTP repository subpath/native URLs, global receiving/diving/mystery systems, financial/medical/research features, exports/imports and local file launch. It includes large deterministic Monte Carlo batches; its CDP evaluation timeout was extended from the generic20 seconds to300 seconds so the unchanged assertions can finish. Final5162 checks passed.

The full trusted-input tutorial completed all22 milestones with the genuine90-second accelerated fishless cycle; economy/casino/pair offers, equipment/8-12-24-hour live-offline parity/repeated-login guards and natural breeding all passed against DIST. Original gameplay code/art hashes remain unchanged. No test result is inferred from a source-only run.

`python tests/verify_protected_release.py --source-archive --check-only` checks original2906 files, public/private checksums, exact PNG callback bytes, no source maps/development files, both ZIPs, every private archived source byte, current benchmark build IDs and exact31-section master/continuity. Repeated same-environment builds must reproduce the exact output manifest and Pages ZIP checksum. Original named-code mirror verifiers describe older unprotected releases; use this production-aware verifier for the protected folder. Review-gallery browser QA remains available against the unchanged development root; production deliberately omits galleries.

## Files changed

- Build: build.py; tools/production/bootstrap.py, minify.cjs, protected_build.py, package.json and package-lock.json. Original build.py is retained in planning/distribution-protection/baseline.
- QA/package: tests/browser_qa.py, pages_qa.py, performance_qa.py, package.py; new protected_build_qa.py, protection_performance_qa.py, protection_media_qa.py, protection_idle_qa.py and verify_protected_release.py; tests/distribution-protection-evidence.
- Documentation: this report, master v4.17, exact continuity source, README.md, GITHUB_PAGES.md, DEVELOPMENT_STATUS.md, GITHUB_PAGES_BUILD_REPORT.md and TEST_REPORT.md.
- Generated deliverables: DIST and both ZIPs. No original game runtime code or art is edited.

## Sources and scope

Build option references: [Terser API](https://terser.org/docs/api-reference/), [clean-css project](https://github.com/clean-css/clean-css), [official Node22.23.0 archive/checksums](https://nodejs.org/en/download/archive/v22.23.0). Toolchain metadata and exact download checksum are stored privately in the local build cache/lockfile.

This is deterrence against casual copying, not DRM or tamper-proof execution. Stable runtime APIs and scientific/specimen metadata remain inspectable where required by gameplay. User-owned local saves and offline play take priority over ineffective protection. The historical18 missing shrimp sheets and unregenerated binary PDF are separate pre-existing limitations and are not claimed complete by this update.

## Final protected build verification

The protected folder contains2020 files and835,160,368 bytes including its manifest. The Pages ZIP is748,336,651 bytes. The build preflight validated all382 native sources and their exact file-origin PNG transports without regenerating or modifying development inputs.

Two separate build processes reproduced the exact manifest and Pages ZIP bytes under the same pinned environment. Build ID: `7bd9f68bd6bd060f7c28de238fa7fd5dc146150f62d8a69ca1355ab0feeb1658`. Pages ZIP SHA-256: `87c6c8f6853a2403f680b17683f49d627b0ffccc3e3fd345a00ef000b0639457`. This is a reproducibility/integrity result, not encryption, an independent signature or tamper-proofing.
