# Aquarium Life performance optimization report

Playable v4.3.0 / master4.14 — 2026-10-22. Freshwater remains locked. Device-local saves, protected artwork, main schema2/tutorial2 and biological/economic rules are retained.

## Measurement method

Actual browser: Chrome/155.0.8059.85; Windows-10-10.0.26300-SP0. Windows CIM reports AMD Ryzen 7 5800X 8-Core Processor (8cores/16logical processors), 31.92GiB usable physical RAM, and display adapters Meta Virtual Monitor, NVIDIA GeForce RTX 3090. Browser-reported device memory: 32GB. Headless Chrome uses `--disable-gpu`, so these are software Canvas measurements, not RTX hardware benchmarks. Physical GPU utilization, hardware video decoding, audio sync and Netflix were not measured. CIM's32-bit AdapterRAM field is not used as a VRAM-capacity measurement.

The actual unmodified game was profiled before runtime edits. Its143 runtime/CSS/HTML files and hashes are preserved under `planning/performance-optimization/baseline/`. The final matched A–D fixtures use real supported tank sizes, heater models, mounted corals and the normal save validator. Test A restores an actual completed20-gallon tutorial aquarium with one Onyx Percula, basic rock, sand and working equipment. B uses eight peaceful small marine fish and three mounted corals. C uses32small marine fish in a large tank. D adds three biologically simulated background aquariums. Synthetic fixtures stay in disposable test profiles. The separate250-fish/35-coral/40-invertebrate art stress test is explicitly artificial and never becomes a production save.

Rows are short7-second active/4-second covered samples; media lasts10seconds. E is a60-second navigation soak plus a final6-second active sample, including normal autosaves and four forced-GC observations. This is not a multi-hour endurance test. Frame gaps measure actual renderer invocation timestamps; CPU is CDP TaskDuration/wall time as a percentage of one main-thread core, not whole-machine/process CPU. JS heap excludes native decoded images and compositor storage. CPU profile and subsystem timings, p50/p95/p99 gaps, maximum draw costs, long tasks, heap, DOM/listeners, cache bounds and save durations are in the JSON evidence. Short samples and test instrumentation add noise.

## Confirmed causes

1. Resetting the visual time budget to zero discarded fractional deadlines and produced roughly40FPS with alternating17/33ms gaps on a60Hz schedule. The old adaptive cap was also tied to the particle Boolean.
2. Covered Store, Journal, Tank Care, Settings and Casino views continued full aquarium drawing. The pre-edit profile sampled `drawImage`156times, polygon scan conversion23times and fillRect7times in its4-second sample; rendering dominated sampled active work.
3. The main page eagerly parsed25native animation source banks totaling190,418,618bytes. Those base64 strings remained resident even for a one-fish aquarium.
4. Static printed silhouettes,700sand grains, gradients, beam polygons and glass were rebuilt each frame. Repeated identical HUD markup also invalidated DOM; whole navigation/selector markup rebuilt every10seconds.
5. Native-frame tint and final-size caches lacked a global byte budget. An initial small-budget implementation exposed eviction churn in the maximum-population regression (164.1ms fish-only p95). Stable source identities and final-size color caching corrected that regression; the failed attempt is not counted as successful optimization.
6. Diving installed an always-running40ms key polling interval while idle. Hidden main rendering relied on browser rAF throttling rather than canceling scheduled work.

## Before and after

| Scenario | FPS before → after | p95 gap ms before → after | p95 draw ms before → after | Main-thread core % before → after | JS heap MiB before → after |
| --- | ---: | ---: | ---: | ---: | ---: |
| A | 39.27 → 59.53 | 34.20 → 17.70 | 2.90 → 0.70 | 11.06 → 6.23 | 308.34 → 126.98 |
| B | 40.23 → 60.00 | 34.00 → 17.70 | 3.00 → 1.10 | 11.86 → 7.54 | 311.78 → 9.00 |
| C | 39.84 → 59.99 | 34.30 → 18.20 | 3.50 → 1.40 | 12.71 → 9.42 | 312.50 → 8.76 |
| C-complex | 39.92 → 59.99 | 34.10 → 17.50 | 3.80 → 1.20 | 13.91 → 9.05 | 310.61 → 11.22 |
| D | 39.56 → 59.99 | 34.30 → 17.80 | 3.20 → 1.20 | 11.78 → 8.95 | 314.51 → 9.31 |
| store | 39.73 → 0.00 | 34.10 → — | 3.40 → — | 14.33 → 0.69 | 182.77 → 9.84 |
| journal | 40.48 → 0.00 | 34.10 → — | 2.70 → — | 11.60 → 0.97 | 182.14 → 8.83 |
| equipment | 39.48 → 0.00 | 34.30 → — | 2.60 → — | 11.05 → 1.07 | 182.50 → 9.20 |
| casino | 39.98 → 0.00 | 34.30 → — | 2.10 → — | 10.61 → 1.27 | 187.25 → 10.24 |
| diving | 0.00 → 0.00 | — → — | — → — | 1.74 → 0.46 | 186.12 → 10.39 |
| settings | 38.98 → 0.00 | 34.30 → — | 2.10 → — | 9.72 → 1.13 | 188.89 → 8.04 |
| F-local-video | 39.99 → 59.49 | 34.10 → 18.00 | 2.50 → 1.00 | 11.08 → 7.92 | 188.64 → 9.00 |
| G-hidden | 0.00 → 0.00 | — → — | — → — | 1.20 → 0.03 | 181.11 → 9.97 |
| H-30 | 41.49 → 29.99 | 34.20 → 34.70 | 2.80 → 1.10 | 12.06 → 4.74 | 184.45 → 8.93 |
| H-60 | 38.99 → 60.15 | 34.20 → 17.80 | 2.60 → 1.00 | 11.11 → 7.58 | 184.92 → 9.26 |
| E-sustained-end | 39.49 → 59.98 | 34.20 → 17.80 | 2.50 → 0.80 | 11.41 → 6.55 | 182.08 → 8.12 |

The old application had no selectable30FPS control: its H-30 row is the same old automatic renderer, not an existing performance mode. Covered rows correctly report0FPS after optimization because the aquarium is hidden by those windows. Active default60FPS may use more per-second drawing work than the previous broken40FPS cadence in very dense scenes; do not infer every scene has a lower core percentage. Per-frame costs, covered-view work and resident source text are reduced. Default High retains all16animation frames and pixel sharpness.

## Changes and files

- `js/main.js`, new `js/performance.js`: one scheduler, fractional60/30FPS pacing, retained fixed-step simulation backlog, safe transaction/checkpoint transitions, covered-menu heartbeat, hidden cancellation and guarded catch-up.
- `js/render.js`: six bounded current scenery layers, stable cached thumbnail encoding, display-size color path and unchanged selected-tank-only/offscreen fish handling.
- `js/fish-animation.js`, `js/sprite-kit.js`: globally bounded pixel caches, stable source identities, display-size tint reuse, unchanged native cells/eyes/anchors and individual pattern ordering.
- New `js/sprite-sources.js`, `livestock_animation_build.py`,382generated `assets/livestock/animation-sources/*.js`, `js/livestock-animation-data.js`, `index.html`, `livestock-animation-review.html`: lossless per-sheet local loading. Legacy25native banks remain in development history but are excluded from DIST and no longer load in gameplay/gallery.
- `js/ui.js`, `css/ui-cleanup.css`, `js/save.js`: compact five-control Graphics & Performance form, changed-value HUD markup/text, additive graphics preferences, legacy particle-off migration. Main schema stays2.
- `js/diving-ui.js`, `js/casino-ui.js`: central input-repeat servicing and hidden decorative-reel guard; existing settlement/save rules remain.
- `build.py`, release verifier, performance/browser probes and art-fixture funding: package current transports, validate lossless PNG bytes and exercise new performance rules. The older art test fixture now funds through the existing Finance service so current first-size achievement receipts remain valid.
- Master sections24.16 and25.1–25.4, DEVELOPMENT_STATUS, GAME_DESIGN, UI_SPECIFICATION, FISH_ANIMATION_SYSTEM, README, exact PROJECT_CONTINUITY_SOURCE, PERFORMANCE_SYSTEM and PERFORMANCE_SETTINGS_SAVE_SCHEMA document the changes.

No Core/Sim/health/heater/reliability/breeding/economy/progression formula or original PNG was edited. Autosave20seconds and immediate purchase/sale/tutorial/hide/unload checkpoints remain. Save serialization was small, so no speculative checkpoint coalescing was introduced.

## Memory, timers and saves

Before forced-GC navigation samples: [180.54, 180.58, 180.75, 180.54]MiB. After: [7.2, 7.35, 7.41, 7.47]MiB. The limited soak supports stable short-session behavior, not an unlimited-session leak-free claim.

Native decoded images are capped at128/256MiB, extracted frames512/32MiB, final rasters8192/32MiB, color variants8192/64MiB. Six480×240 static layers total2.64MiB. These allocate on demand. JSON evidence records actual occupied buffers where exposed; neither JavaScript heap nor these estimates equals total GPU/browser memory. Up to four source scripts load concurrently and are removed after delivery. Individual removal/tank changes prune renderer positions. Casino outcomes, financial history and livestock state are retained.

The gameplay scheduler exposes at most one pending rAF or one covered-view timeout and none while hidden. The permanent idle diving interval was removed. Tutorial/layout rAF requests are event-driven one-shot updates, not additional full-scene loops. Short-lived toast/tutorial/casino/offline timers remain necessary. A browser-wide active-timer census was not available for the original baseline; scheduler counters and source audit are reported rather than an invented timer total.

Ten synchronous test saves before: median serialization 0.60ms, total save 6.05ms; after: 0.60ms / 7.70ms. All final sample saves succeed. These intentionally repeated test writes are not the normal20-second autosave cadence. Critical durability of a save is favored over saving a few milliseconds.

## Multitasking and limitations

The substitute is a real looping640×360 VP8 WebM encoded by the browser, displayed beside the game in the same test document. It has no audio and is not Netflix. Before playback quality: {'total': 303, 'dropped': 1, 'corrupted': 0}; after: {'total': 303, 'dropped': 6, 'corrupted': 0}. The game’s F row records simultaneous FPS, core time and heap. A few dropped video frames and short-sample variance remain; this does not prove improved video playback or audio synchronization. The exact reported Netflix/hardware-accelerated desktop scenario still needs observation on the player's normal browser/hardware.

No physical GPU percentage or driver/hardware video-decoder contention was measurable in the software/headless harness. Fewer covered draws and cached static layers demonstrably reduce submitted Canvas work, but are not a measured physical GPU percentage. No render-scale setting was added. Diverse maximum-population scenes remain heavier than ordinary tanks;30FPS and presentation quality controls are available without slowing biology. A multi-hour endurance session and normal-window Netflix/audio-sync verification remain environmental validation limits.

The separate historical artwork gap remains18sheets for three shrimp species;110/113usable entries currently have full native production. This performance update neither removes their original fallback art nor claims those missing drawings were produced.

## Executed regressions

- `tests/performance-evidence/chrome-after.json`: 33passed, 0failed. See release validation for final freshness/entry-point checks.
- `tests/sprite-production-evidence/chrome-results.json`: 5398passed, 0failed. See release validation for final freshness/entry-point checks.
- `tests/sprite-production-evidence/edge-results.json`: 5398passed, 0failed. See release validation for final freshness/entry-point checks.
- `tests/tutorial-audit-evidence/chrome-results.json`: 72passed, 0failed. See release validation for final freshness/entry-point checks.
- `tests/equipment-reliability-evidence/chrome-results.json`: 787passed, 0failed. See release validation for final freshness/entry-point checks.
- `tests/economy-update-evidence/edge-results.json`: 85passed, 0failed. See release validation for final freshness/entry-point checks.
- `tests/pages-evidence/edge-results.json`: 5162passed, 0failed. See release validation for final freshness/entry-point checks.
- `tests/breeding-evidence/chrome-results.json`: 86passed, 0failed. See release validation for final freshness/entry-point checks.

Additional E endurance run: 300.9seconds,60management-window round trips, 15normal autosaves, and post-GC heap samples [6.23, 6.64, 6.74, 6.79, 6.86, 7.03, 7.14, 7.17, 7.28, 7.46]MiB. End-to-end warm heap growth 1.22MiB; listener range 480–480. 4/4soak checks passed. This supports bounded five-minute operation and repeated navigation, not a claim of multi-hour certification. See `tests/performance-evidence/chrome-soak.json`.

Regression setup corrections: Edge inherited a756×488headless viewport, shrinking the canvas to28×14pixels and rounding synthetic small-resident clicks outside their hitboxes. The complete art suite now explicitly uses the required1600×900viewport; all382sheets and resident selections pass there. A Pages-only fixture directly constructed an extra tank without running the normal migration that creates its empty mortality history. That fixture now follows migration before save validation. Production mortality safeguards were not weakened. The earlier art-funding fixture also uses normal Finance receipts rather than discarding current achievement receipts.

Performance checks cover defaults/old preference migration, actual settings submission/local persistence, virtual refresh rates, exact biological projections across render cadences, native16frame/eye/color/facing fidelity, selection, unchanged DOM-node retention, hidden elapsed-time conservation, state-clone checkpoint conservation, cache limits, one scheduler and actual1920×1080/1600×900/1366×768viewport resizing. Full art validation covers all382sheets/6112cells, both facings, eye patches, stages, individual save/load and selection. Tutorial tests follow all22tasks with trusted input and real fishless cycling. Equipment tests cover heater sizing, maintenance/parts, inventory, and8/12/24-hour live/offline equivalence. Economy/Pages suites cover quantities, buying/selling tanks, first-discovery receipts, journal, casino, diving/receiving, breeding/eggs, local recovery and freshwater lock. Final release verification checks current source/DIST/archive hashes; old unrelated evidence is not counted as a fresh run.
