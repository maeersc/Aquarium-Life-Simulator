from pathlib import Path
import re
r=Path(__file__).resolve().parents[2]
rule='Aquarium Life defaults to a maximum target of 60 FPS, with an optional 30 FPS performance mode. Rendering must be efficiently frame-paced, uncapped rendering is prohibited, and visual updates must remain independent of authoritative biological simulation. CPU, GPU and memory usage must be optimized so the game can operate alongside other desktop applications without unnecessary system-wide resource contention.'
p=r/'MASTER_DEVELOPMENT_PROMPT.md';old=p.read_text(encoding='utf8');new=old.replace('VERSION 4.13','VERSION 4.14',1).replace('playable v4.2.1, 2026-10-21','playable v4.3.0, 2026-10-22',1)
a=new.index('## 25.1 Rendering');b=new.index('\n---',a)
new=new[:a]+'''## 25.1 Rendering

'''+rule+'''

Use one authoritative gameplay scheduler, phase-preserving requestAnimationFrame deadlines and no visual catch-up bursts. Render only the selected visible aquarium; covered management views and hidden tabs stop its Canvas updates. Preserve16 authored frames, individual patterns, sharp eyes, facing, life stages and species-specific elapsed-time motion. Cache current static scenery with bounded ownership. Load native PNGs on demand; generated per-sheet scripts preserve file:// pixel reads without eager embedded banks. See PERFORMANCE_SYSTEM.md.

## 25.2 Simulation Performance

Preserve the existing5-game-minute simulation steps and20-real-minute day. Rendering cadence must not alter biology, equipment, rewards or clock speed. Bound foreground catch-up work per callback while retaining every pending minute; drain pending time before checkpoint saves. Keep pending time across transaction clones, reset on genuine profile/checkpoint restoration, and use existing offline catch-up once per hidden interval. Never count elapsed time twice or silently discard long frame gaps. Simulate other owned aquariums without drawing them.

## 25.3 Graphics & Performance Settings

Frame Rate:30FPS Performance Mode or60FPS Default. Graphics Quality:Low/Medium/High(default). Water Effects:Low/Medium/High(default). Decorative Particles:Off/Low/Full(default, respecting an older off preference). Background Resource Saving:on by default. These controls affect presentation only. No unlimited option or automatic particle-linked FPS. Add render scale only with measured benefit; preserve native pixel sharpness. Hidden tabs always stop drawing; resource saving also reduces covered-menu polling.

## 25.4 Profiling and Memory Acceptance

Profile actual game scenes before optimizing. Record repeatable before/after frame times, main-thread cost, heap and known pixel-cache budgets; state when physical GPU/Netflix/audio-sync measurements are unavailable. Verify small/mixed/dense/multiple-tank scenes, sustained navigation, local video, hidden/return accounting and virtual high-refresh cadence. Test full gameplay and every existing native sheet. Keep exact original art and biological/economic authorities. Cache ceilings must prevent unlimited accumulation while accommodating the active scene; stress-test final-size color/raster reuse to avoid eviction churn. See AQUARIUM_LIFE_PERFORMANCE_OPTIMIZATION_REPORT.md for executed results and limitations.
''' +new[b:]
anchor='\n# 25. GRAPHICS ENGINE, ANIMATION & PERFORMANCE'
new=new.replace(anchor,'\n## 24.16 Graphics Preference Persistence\n\nAdditive `settings.graphics` under main schema2 stores the five presentation controls. Missing or invalid presentation choices normalize without resetting any player assets. Existing particle-off settings remain off. Keep20-second autosave and immediate transaction/tutorial/visibility checkpoints, validation, backups, anti-replay ledgers, and device-local JSON export/import. Never serialize decoded artwork. See PERFORMANCE_SETTINGS_SAVE_SCHEMA.md.\n'+anchor,1)
assert len(re.findall(r'^# \d+\. ',new,re.M))==31
p.write_text(new,encoding='utf8')
p=r/'PROJECT_CONTINUITY_SOURCE.md';s=p.read_text(encoding='utf8');assert s.count(old)==1;s=s.replace(old,new);lead='''## Performance optimization — 2026-10-22

Playable v4.3.0 / master v4.14. One capped60/30FPS scheduler, independent fixed biological steps, on-demand lossless native sources, bounded caches, cached scenery, covered/hidden render suspension, changed-value HUD updates and five graphics preferences. Main schema2/tutorial2, all player assets, protected art, local saves, freshwater lock and biological/economic formulas remain intact. PERFORMANCE_SYSTEM.md and PERFORMANCE_SETTINGS_SAVE_SCHEMA.md describe runtime/persistence; AQUARIUM_LIFE_PERFORMANCE_OPTIMIZATION_REPORT.md records actual measurements and executed regressions. Exact complete31-section master remains embedded below. Earlier art/PDF limitations remain separate.

''';s=s.replace('\n\n','\n\n'+lead,1);p.write_text(s,encoding='utf8')
for filename in ['DEVELOPMENT_STATUS.md','README.md','GAME_DESIGN.md','UI_SPECIFICATION.md','FISH_ANIMATION_SYSTEM.md']:
 p=r/filename;s=p.read_text(encoding='utf8');s=s.replace('\n\n','\n\n'+lead,1);p.write_text(s,encoding='utf8')
p=r/'build.py';s=p.read_text(encoding='utf8').replace("ROOT / 'TUTORIAL_FULL_AUDIT_AND_REPAIR_REPORT.md',","ROOT / 'AQUARIUM_LIFE_PERFORMANCE_OPTIMIZATION_REPORT.md', ROOT / 'PERFORMANCE_SYSTEM.md', ROOT / 'PERFORMANCE_SETTINGS_SAVE_SCHEMA.md', ROOT / 'TUTORIAL_FULL_AUDIT_AND_REPAIR_REPORT.md',",1);p.write_text(s,encoding='utf8')
