# Rendering, simulation and graphics — v4.3.0

The only gameplay scheduler lives in `js/main.js`. It owns at most one pending requestAnimationFrame or one covered-view timeout. Aquarium changes, transactions, navigation and tutorial updates do not create another scheduler. `AL.loop.start/stop` are idempotent; disposal cancels work and disconnects its observer.

The frame pacer retains fractional deadlines instead of zeroing elapsed time after every draw. It renders the newest frame once when due, drops obsolete visual deadlines, and uses the browser animation timestamp. Targets are60(default) or30FPS; there is no unlimited mode or automatic coupling to the particle preference. Virtual60/120/144/165/240Hz input tests cover both targets. Frame counts over short observation windows can include an endpoint frame; this is not an uncapped mode.

Only the selected aquarium draws. A modal covering the aquarium stops its Canvas updates while biology continues. Diving owns the visible scene during expeditions. Hidden tabs cancel scheduling and decorative work, save their exact checkpoint and use the existing offline authority once on return. The welcome-back summary itself covers the aquarium; closing it resumes presentation. Visibility handling prevents a second catch-up from starting during the first.

## Authoritative time

Biology continues in existing5-game-minute steps, independent of visual frames. A foreground simulation-work budget yields between complete steps and retains all remaining minutes; it never discards them. Checkpoint saves drain complete steps and the final partial interval before moving the wall-clock checkpoint. Partial minutes round only at the checkpoint to the same micro-minute precision used by offline progression. A transaction cloning the current state retains pending time; a different world or restored checkpoint resets it. Long foreground callback gaps are accounted for rather than silently clamped to250ms. No chemistry, feeding, growth, breeding, heater, reliability, mortality or economic formula changed. One day remains1200real seconds at1×.

## Pixels and memory

Six480×240 scenery layers retain the current background, printed silhouettes, sand, water beams, glass and lamp gradient (2.64MiB maximum). Sand/material/depth, graphics controls, light output and asynchronous native backdrop readiness invalidate the relevant layer. Beam positions quantize to scene pixels. Living corals, invertebrates, fish and selection overlays remain dynamic; existing offscreen fish culling is retained.

Native animation loads per sheet. On HTTPS it uses the original same-origin PNG. On `file://`, a generated per-sheet classic script supplies identical PNG bytes through a short-lived promise, preserving origin-clean pixel reads. At most four transports run concurrently. Script elements and pending source strings are released after delivery. Startup no longer parses all25 native banks (190,418,618bytes). Native PNGs, eye/anchor metadata, life stages, all16 cells and fallback artwork are unchanged. The standalone gallery uses the same loader.

Caches allocate on demand; their limits are ceilings, not startup allocations. Decoded native sheets have128-entry/256MiB limits; extracted frames512-entry/32MiB limits; final-size rasters8192-entry/32MiB limits; color variants8192-entry/64MiB limits. Static UI thumbnails retain at most256 data URLs. Original fallback pose and legacy caches retain their existing bounded/weak ownership. These are known pixel-buffer estimates, not measurements of total browser/GPU memory.

Stable frame identities let final-size rasters survive raw-frame eviction. Ordinary genetic color treatment occurs after final-size nearest-neighbor rasterization, avoiding repeated full-size brightness canvases. Inherited Ocellaris pattern transformations keep their existing color/pattern ordering and individual cache identity. Pixel comparisons cover16frames, five tones and both facings. Artwork is never embedded in a player save.

## Settings and UI

Settings → Graphics & Performance contains Frame Rate30/60, Graphics Quality Low/Medium/High, Water Effects Low/Medium/High, Decorative Particles Off/Low/Full and Background Resource Saving (default on). Defaults are60/High/High/Full/on, except legacy particle-off preferences remain off. Quality changes sand detail; water quality changes decorative beams and surface glints; particle quality changes decorative bubbles/specks. Actual lamp brightness and all biological light requirements remain independent. Resource saving lowers covered-menu polling to4Hz; hidden drawing always stops. No render-scale setting was added because the profile did not identify native480×240 buffer resolution as a reason to lower art resolution.

HUD text and markup are compared before replacement. The inactive ten-second whole-navigation rebuild is removed; transaction/navigation renders and one-second vital updates remain. Store rotation and receiving deadlines still update. Thumbnails reuse their PNG encoding. Diving key repeat is serviced by the gameplay scheduler instead of a permanent25Hz idle interval. Casino settlement timers remain authoritative; their decorative reel drawing skips hidden tabs.

Autosave remains20seconds, with immediate transaction, hide, unload and tutorial checkpoints. Measured serialization is small relative to rendering and source loading, so checkpoints were retained rather than coalesced speculatively. Save validation, recovery backups, anti-replay ledgers and local-only storage remain intact.

See `AQUARIUM_LIFE_PERFORMANCE_OPTIMIZATION_REPORT.md` and machine-readable `tests/performance-evidence/` for executed measurements and limitations. Headless software Canvas results do not establish physical GPU usage or Netflix audio/video synchronization.
