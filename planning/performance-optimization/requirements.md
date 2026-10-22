# AQUARIUM LIFE — COMPLETE PERFORMANCE OPTIMIZATION
## Master Implementation Prompt — Codex GPT-6 Astra
### Critical Optimization Update | Default 60 FPS | Saltwater Only

---

## 1. ROLE AND PRIMARY OBJECTIVE

You are the lead performance engineer, JavaScript architect, Canvas rendering specialist, and optimization engineer for Aquarium Life.

Aquarium Life is an offline, browser-based, 2D saltwater aquarium simulation.

The game currently consumes enough system resources that other applications experience significant lag.

**Reported problem:**

When Aquarium Life runs in the browser alongside Netflix, Netflix experiences video lag and audio/video synchronization problems.

Your assignment is to identify and eliminate unnecessary CPU, GPU, memory, rendering, and background-processing overhead.

### Required results

- Default rendering target: **60 FPS**.
- Maximum normal rendering rate: 60 FPS.
- Optional 30 FPS performance mode.
- No unlimited-FPS rendering.
- Significantly lower unnecessary CPU and GPU usage.
- Stable memory consumption.
- Smooth fish animations.
- Responsive game interface.
- Correct biological simulation.
- Efficient background behavior.
- Better multitasking with other applications.

**60 FPS is the default target, not a promise that every computer will maintain 60 FPS under all conditions.**

Do not make 60 FPS appear stable by slowing down the underlying game simulation.

Do not sacrifice established gameplay systems to improve benchmark results.

---

## 2. MANDATORY PERFORMANCE AUDIT

Before editing the implementation, inspect and profile the actual game.

Audit:

1. Main rendering loop.
2. Canvas drawing pipeline.
3. Fish animation system.
4. Sixteen-frame sprite handling.
5. Coral and invertebrate animation.
6. Background and lighting effects.
7. JavaScript simulation loops.
8. Water chemistry calculations.
9. Fish behavior and pathfinding.
10. Equipment simulation.
11. UI refresh frequency.
12. Tutorial spotlight system.
13. Aquarium Store.
14. Field Journal.
15. Equipment Inventory.
16. The Dock Casino.
17. Ocean Diving.
18. Save and load operations.
19. Memory allocation and cleanup.
20. Browser visibility behavior.

Identify expensive operations using actual profiling data.

Do not guess which subsystem is responsible.

### Baseline measurements

Record, where measurable:

- Average FPS.
- Frame-time percentiles.
- Frame-time spikes.
- JavaScript execution time.
- Rendering time.
- Long main-thread tasks.
- CPU usage.
- GPU usage.
- JavaScript heap usage.
- Sprite memory consumption.
- Number of active timers.
- Save serialization duration.
- Idle resource consumption.

Label unavailable measurements honestly.

Do not invent results.

---

## 3. FRAME-RATE SYSTEM — DEFAULT 60 FPS

Implement a controlled frame-rate system.

### Default

**60 FPS**

The game should target 60 FPS when running in the foreground.

### Available settings

Settings → Graphics & Performance → Frame Rate

Options:

- 30 FPS — Performance Mode.
- 60 FPS — Default.

Do not offer an unlimited mode.

Do not allow a high-refresh-rate monitor to force rendering at 144, 165, 240, or more FPS.

### Important engineering requirements

Use requestAnimationFrame with an appropriate frame pacing mechanism.

Avoid busy-waiting.

Avoid unnecessary rendering when a frame is not due.

Ensure:
- Smooth frame pacing.
- Stable animation timing.
- No duplicate game loops.
- No runaway timers.
- Correct behavior on high-refresh-rate displays.
- Correct behavior after browser focus changes.

Avoid implementations that create irregular timing or excessive animation jitter.

### Simulation independence

Fish behavior, equipment operation, water chemistry, breeding, growth, and in-game time must not depend on rendered frame count.

If rendering slows to 30 FPS, biological simulation must continue at the correct game-time rate.

Preserve:

**One in-game day = 20 real-world minutes.**

Do not change this established timing rule.

---

## 4. CENTRALIZED RENDERING MANAGEMENT

Investigate whether multiple rendering loops are active unnecessarily.

Where beneficial, consolidate rendering into one authoritative scheduler.

Avoid:
- Multiple independent full-aquarium redraw loops.
- Duplicate requestAnimationFrame subscriptions.
- Rendering invisible aquariums.
- High-frequency setInterval rendering.
- Repeated initialization of render loops.
- Canvas rendering while unrelated menus cover the aquarium.

The rendering system must have reliable start, stop, pause, resume, and cleanup behavior.

Do not accidentally start another render loop when:
- Switching aquariums.
- Returning from Ocean Diving.
- Closing the store.
- Reopening an aquarium.
- Reloading UI panels.
- Pausing or resuming the tutorial.

Ensure only intended rendering loops remain active.

---

## 5. RENDER ONLY WHAT IS NECESSARY

Aquarium Life may contain multiple owned aquariums, but the player typically views one at a time.

### Required behavior

Only the currently displayed aquarium requires full visual rendering.

Other aquariums must continue biological simulation without unnecessary visual updates.

Optimize:
- Water backgrounds.
- Decorations.
- Sand.
- Rocks.
- Corals.
- Fish.
- Lighting.
- Equipment visuals.
- Environmental particles.

### Static elements

Cache static artwork where useful.

Examples:
- Stationary rocks.
- Stable aquarium decorations.
- Nonanimated background layers.
- Static portions of aquarium equipment.

Do not redraw or reconstruct expensive static assets unnecessarily.

### Moving elements

Continue animating visible moving livestock at the appropriate rate.

Do not render fish that are outside the visible aquarium viewport.

Preserve their biological state.

---

## 6. SIXTEEN-FRAME LIVESTOCK ANIMATION OPTIMIZATION

Aquarium Life uses detailed sixteen-frame pixel-art animations.

These must remain supported.

Audit the full animation pipeline.

### Asset management

Load image assets once where appropriate.

Reuse:
- Decoded sprite sheets.
- Frame dimensions.
- Frame locations.
- Animation metadata.
- Species animation definitions.
- Life-stage animation information.

Avoid:
- Repeated image decoding.
- Creating new Image objects every frame.
- Generating temporary canvases unnecessarily.
- Rebuilding the same animation frame repeatedly.
- Performing expensive transformations on every sprite draw when a reusable representation is available.

### Preserve visual quality

Do not:
- Remove frames.
- Reduce the artwork to four frames.
- Replace animated fish with static images.
- Blur pixel-art sprites.
- Remove species-specific swimming behavior.
- Break eye positioning.
- Break left/right facing.
- Break life-stage artwork.

### Animation speed

Preserve natural movement.

A 60 FPS renderer does NOT mean fish should cycle through sixty animation frames per second.

Animation playback must use elapsed time and species-specific movement profiles.

Keep the existing slower, realistic swimming behavior.

---

## 7. CANVAS 2D OPTIMIZATION

Inspect all Canvas 2D rendering operations.

Identify expensive:
- drawImage calls.
- save/restore operations.
- Scaling.
- Alpha blending.
- Rotations.
- Gradients.
- Shadows.
- Filters.
- Pixel manipulation.
- Full-canvas redraws.
- Temporary canvas allocations.

Apply optimizations supported by profiling.

### Rendering strategies

Consider:
- Static background caching.
- Offscreen pre-rendering where memory-efficient.
- Sprite culling.
- Cached lighting effects.
- Reduced redundant Canvas state changes.
- Stable reusable buffers.
- Efficient draw ordering.
- Conditional UI and Canvas redraws.

Do not implement complicated new rendering architecture unless measurements justify it.

### Pixel-art requirements

Preserve:
- Sharp sprite edges.
- Existing approved pixel art.
- Correct transparency.
- Accurate sprite positioning.
- Accurate fish selection.
- Correct mouse coordinates.
- Correct animation alignment.

---

## 8. GRAPHICS QUALITY SETTINGS

Add a compact Graphics & Performance section within Settings.

### Frame Rate

- 30 FPS.
- 60 FPS — Default.

### Graphics Quality

- Low.
- Medium.
- High — Default where appropriate.

### Water Effects

- Low.
- Medium.
- High.

### Decorative Particles

- Off.
- Low.
- Full.

### Background Resource Saving

- Enabled by default.

### Render Scale

Provide a sensible render-scale or resolution setting only if profiling demonstrates meaningful benefit.

Preserve crisp pixel-art scaling.

### Quality rules

All graphics settings affect presentation only.

They must not modify:
- Fish health.
- Water chemistry.
- Nitrogen cycling.
- Breeding.
- Fish growth.
- Equipment durability.
- AC earnings.
- Achievements.
- Mortality.
- Diving rewards.

The default graphics settings should look good while remaining resource-conscious.

Do not use High quality as justification for uncontrolled resource consumption.

---

## 9. CPU OPTIMIZATION — GAME SIMULATION

The biological simulation must not run unnecessarily at 60 updates per second.

Inspect all simulation systems.

### Water chemistry

Review:
- Ammonia.
- Nitrite.
- Nitrate.
- Oxygen.
- Temperature.
- Salinity.
- pH.
- Organic waste.
- Bacterial filtration.
- Coral chemistry.

Use appropriate time-based update intervals.

Do not calculate slow biological changes every visual frame unless technically necessary.

### Livestock behavior

Optimize:
- Fish movement decisions.
- Aggression checks.
- Feeding searches.
- Schooling.
- Courtship.
- Collision checks.
- Pathfinding.
- Habitat checks.
- Species compatibility calculations.

Avoid recalculating expensive global decisions unnecessarily.

### Equipment

Optimize:
- Operating efficiency.
- Maintenance condition.
- Wear.
- Reliability.
- Failure checks.
- Heater and chiller operation.

Preserve the longer equipment lifespan established in the recent durability update.

### Time-step accuracy

Use elapsed simulation time consistently.

Prevent different outcomes merely because one player has a 30 FPS display and another uses 60 FPS.

---

## 10. GPU OPTIMIZATION

Investigate whether the aquarium renderer places excessive load on the graphics processor.

Pay attention to:
- High-resolution Canvas buffers.
- Device pixel ratio.
- Large transparent overlays.
- Full-screen visual effects.
- Expensive shadows.
- Excessive compositing.
- Repeated texture uploads.
- Unnecessary scaling.
- Large offscreen buffers.

Reduce needless GPU work without damaging the appearance of the aquarium.

The player should be able to use another hardware-accelerated application while Aquarium Life is running.

Do not solve GPU contention by indiscriminately disabling the aquarium's visual features.

---

## 11. BACKGROUND AND MULTITASKING PERFORMANCE

Optimize behavior when Aquarium Life is not visible.

### Hidden browser tabs

When the game becomes hidden:

- Stop visible Canvas rendering.
- Stop decorative animation.
- Avoid unnecessary UI updates.
- Reduce nonessential polling.
- Release temporary resources when safe.

Preserve authoritative elapsed-time accounting.

Use the existing offline/catch-up simulation when the tab becomes visible again.

Do not advance time twice.

### Visible side-by-side windows

If Aquarium Life remains visible while Netflix or another video player runs beside it, the game must still minimize unnecessary CPU/GPU usage.

The game should not consume extra rendering frames beyond its configured 60 FPS target.

Maintain efficient active rendering.

### Media playback test

Where possible, perform a side-by-side multitasking test with browser video playback.

Measure:
- Game FPS.
- Game frame times.
- Main-thread utilization.
- Media dropped frames where accessible.
- Memory growth.
- Responsiveness.

Report limitations if the exact Netflix scenario cannot be reproduced.

Do not falsely claim that Netflix was tested.

---

## 12. MEMORY OPTIMIZATION

Audit memory usage during long sessions.

Check:
- Sprite-sheet caches.
- Image references.
- Canvas buffers.
- Event listeners.
- Timers.
- Modal instances.
- Aquarium switching.
- Diving sessions.
- Casino history.
- Tank History.
- Debug logs.
- Removed livestock.
- Removed equipment.
- Sold aquariums.

Clean up obsolete references.

Prevent unlimited cache growth.

Use bounded caching where appropriate.

Do not clear required game state to reduce memory measurements.

### Long-session requirements

Memory usage should stabilize over time rather than grow without bound.

Test repeated navigation and sustained aquarium operation.

---

## 13. UI UPDATE OPTIMIZATION

The interface should not rebuild itself unnecessarily.

Audit:
- Water & Wellbeing.
- AC wallet.
- Aquarium value.
- Aquarium level.
- Equipment condition.
- Inventory.
- Store products.
- Achievements.
- Objectives.
- Field Journal.
- The Dock Casino.
- Diving menus.
- Tutorial highlighting.

Only update displayed values when necessary.

Avoid repeatedly replacing identical DOM elements.

Avoid repeated expensive layout measurements.

Prevent:
- Event-listener duplication.
- Unnecessary style recalculation.
- Repeated full-panel rendering.
- Unnecessary polling.
- UI operations running every animation frame.

Preserve all player interactions.

---

## 14. SAVE SYSTEM OPTIMIZATION

Review how often Aquarium Life saves progress.

Identify expensive:
- State serialization.
- Large object traversal.
- History processing.
- Storage writes.
- Duplicate save triggers.

Reduce unnecessary saves without compromising data integrity.

Use appropriate save coalescing and event-triggered persistence.

Do not remove important save checkpoints.

Do not store decoded image assets in save files.

Preserve:
- Player profiles.
- Aquarium ownership.
- Livestock identities.
- Genetics.
- Breeding.
- Equipment.
- Inventory.
- AC.
- Achievements.
- Diving progress.
- Casino history.
- Tutorial progress.

Ensure no save migrations duplicate or delete player assets.

---

## 15. PERFORMANCE TEST SCENARIOS

Use repeatable benchmarks.

### Test A — Small Aquarium

- One active 20-gallon aquarium.
- One fish.
- Basic equipment.
- Basic rock layout.

### Test B — Medium Aquarium

- Multiple fish.
- Several corals.
- Working equipment.
- Normal environmental effects.

### Test C — Large Aquarium

- Large aquarium capacity.
- Dense but realistic livestock population.
- Complex hardscape.
- Multiple animated specimens.

### Test D — Multiple Aquariums

- Several owned aquariums.
- One displayed.
- Others simulating in the background.

### Test E — Long Session

- Extended gameplay.
- Repeated navigation.
- Equipment updates.
- Regular autosaves.

### Test F — Multitasking

- Aquarium Life visible.
- A separate video playback workload active.
- Compare before and after performance.

### Test G — Background

- Game hidden or minimized.
- Return to the game.
- Verify simulation catch-up and resource savings.

### Test H — Frame Rate

- 60 FPS default.
- 30 FPS optional.
- High-refresh-rate display simulation where supported.

Do not use impossible livestock combinations in production saves.

Synthetic stress scenarios must remain isolated from actual player data.

---

## 16. ACCEPTANCE CRITERIA

The optimization is complete only when the implementation demonstrates:

1. Default rendering target is 60 FPS.
2. FPS does not run uncapped.
3. Optional 30 FPS mode works.
4. Rendering remains independent from biological simulation.
5. Only the visible aquarium receives full visual updates.
6. Hidden views do not waste substantial rendering resources.
7. Sixteen-frame animations remain intact.
8. CPU overhead is measurably reduced where baseline bottlenecks exist.
9. GPU workload is reduced where profiling identifies waste.
10. Memory usage remains stable during long sessions.
11. UI remains responsive.
12. Save operations remain correct.
13. No duplicate game loops are introduced.
14. No simulation-speed regressions occur.
15. All aquarium systems remain functional.
16. Offline progression remains accurate.
17. The game remains fully offline.
18. Freshwater remains locked.

### Important success definition

A stable 60 FPS counter is not enough.

**Performance improvements must also reduce unnecessary system-resource consumption.**

Record actual before-and-after measurements.

If some bottlenecks remain, identify them clearly.

---

## 17. PERFORMANCE REPORT

Create or update:

AQUARIUM_LIFE_PERFORMANCE_OPTIMIZATION_REPORT.md

Include:

### Baseline Measurements

- Browser version.
- Available hardware information.
- Test scenarios.
- Initial FPS.
- Main-thread cost.
- Rendering cost.
- Memory usage.
- CPU/GPU measurements where available.

### Root Causes

Explain which specific systems caused unnecessary work.

### Optimization Changes

List:
- Files modified.
- Rendering improvements.
- Animation changes.
- Simulation changes.
- Memory improvements.
- UI changes.
- Save changes.
- Graphics settings.

### Before-and-After Comparison

Provide real performance measurements.

### Multitasking Results

Describe whether other media playback workloads improved.

Distinguish actual Netflix testing from substitute video playback tests.

### Remaining Issues

Identify anything unresolved.

Do not invent successful results.

---

## 18. REGRESSION TESTS

After optimization, verify:

- Fish movement.
- Sixteen-frame fish animation.
- Fish eye positions.
- Left/right facing.
- Livestock selection.
- Water chemistry.
- Temperature.
- Equipment durability.
- Equipment repair.
- Shared storage Inventory.
- Individual aquarium equipment.
- Autonomous breeding.
- Eggs and offspring.
- Aquarium Store.
- Quantity purchasing if already implemented.
- Aquarium buying and selling.
- First-time discovery achievements.
- Field Journal.
- Ocean Diving.
- The Dock Casino.
- Interactive tutorial.
- Tutorial highlighting.
- Tutorial progression without loops.
- Offline simulation.
- Save/load.
- Aquarium switching.
- Browser resizing.
- Freshwater restrictions.

Do not remove existing functionality to improve performance.

---

## 19. MASTER DOCUMENTATION

Update the correct home section in Aquarium Life's consolidated 31-section Master Development Prompt.

Update:
- DEVELOPMENT_STATUS.md.
- Rendering documentation.
- Animation documentation.
- Simulation documentation.
- Graphics settings documentation.
- Save-system documentation.
- Project continuity/handoff notes.

Add this permanent rule:

**Aquarium Life defaults to a maximum target of 60 FPS, with an optional 30 FPS performance mode. Rendering must be efficiently frame-paced, uncapped rendering is prohibited, and visual updates must remain independent of authoritative biological simulation. CPU, GPU and memory usage must be optimized so the game can operate alongside other desktop applications without unnecessary system-wide resource contention.**

---

## 20. FINAL COMPLETION REQUIREMENT

When all authorized optimization tasks are complete, provide:

1. Root causes of excessive resource usage.
2. Files modified.
3. Performance improvements implemented.
4. Default FPS confirmation.
5. Optional 30 FPS confirmation.
6. CPU measurements.
7. GPU measurements where available.
8. Memory measurements.
9. Before-and-after benchmarks.
10. Multitasking test results.
11. Save/load regression results.
12. Known remaining problems.

Do not claim successful optimization without testing.

Do not claim unperformed hardware or Netflix tests passed.

When all authorized work is genuinely complete, end with the exact standalone line:

Done With Edits

# FINAL DIRECTIVE

Optimize Aquarium Life for smooth, efficient gameplay with **60 FPS as the default**.

Do not allow the game to consume excessive system resources unnecessarily.

The player should be able to run Aquarium Life alongside Netflix, Discord, browsers and ordinary desktop applications without avoidable lag.

Profile first, repair identified bottlenecks, and validate the results.

Preserve Aquarium Life's 16-frame pixel artwork, gameplay systems, biological realism, player saves and offline functionality.

Freshwater remains locked and noninteractive.
