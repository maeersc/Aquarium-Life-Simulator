from pathlib import Path
r=Path(__file__).resolve().parents[2]
for name in ['DEVELOPMENT_STATUS.md','README.md','GAME_DESIGN.md','UI_SPECIFICATION.md','FISH_ANIMATION_SYSTEM.md']:
 p=r/name;s=p.read_text(encoding='utf8').replace('Exact complete31-section master remains embedded below. Earlier art/PDF limitations remain separate.','The31-section authority is MASTER_DEVELOPMENT_PROMPT.md, with an exact handoff copy in PROJECT_CONTINUITY_SOURCE.md. Earlier art/PDF limitations remain separate.',1)
 if name=='DEVELOPMENT_STATUS.md':s=s.replace('2026-10-20','2026-10-22',1)
 if name=='FISH_ANIMATION_SYSTEM.md':
  s=s.replace('# Marine fish and resident animation architecture — v4.0.4 checkpoint','# Marine fish and resident animation architecture — v4.3.0',1)
  a=s.index('It embeds native PNG dataURLs in ordered local classic-script chunks');b=s.index('Actual registered production PNGs now use this contract;',a)
  s=s[:a]+'''It generates lossless per-sheet classic-script transports for file:// use and original same-origin PNG loading on HTTPS. Neither game nor gallery eagerly parses the old25native banks. The browser validates actual decoded cells on first load and rejects blank/repeated poses. Decoded sheets retain at most128entries/256MiB; extracted frames512entries/32MiB. Final rasters and tint canvases use stable source identities with32MiB/64MiB limits, preserving already prepared display-size pixels when raw frames are evicted. The earlier1024-cell/weakly owned tint strategy is superseded: repeated full-size tint/raster creation under a smaller cache exposed a164.1ms stress p95, and final-size color treatment plus stable cache keys corrected that regression. Individual Ocellaris pattern processing retains its original color/pattern order. Performance evidence records occupied bytes, entry limits, hits, misses, evictions and actual frame times. '''+s[b:]
 p.write_text(s,encoding='utf8')
