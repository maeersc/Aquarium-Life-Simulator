"""One-time presentation integration; no simulation or saved state changes."""
from pathlib import Path
import json
r=Path(__file__).resolve().parents[2]
p=r/'js/diving-ui.js';s=p.read_text(encoding='utf8')
old="${AL.DivingArt.image(region+'-'+mode)?.src||r.background||''}"
assert old in s
s=s.replace(old,"${AL.DivingArt.source(region,mode)}")
old='class="dive-scene-preview"'
s=s.replace(old,'class="dive-scene-preview" data-dive-scene="${esc(region)}-${esc(mode)}"')
old='return `<h3>${R.regions[h.region].name}'
new='return `<img class="dive-result-scene" data-dive-result-scene="${esc(h.region)}-${esc(h.mode)}" src="${AL.DivingArt.source(h.region,h.mode)}" alt="${esc(R.regions[h.region].name)} expedition scenery"><h3>${R.regions[h.region].name}'
assert old in s;s=s.replace(old,new)
old="const a=AL.game.diving.active,c=$('dive-map'),ctx=c.getContext('2d'),bg=AL.DivingArt.image(a.region+'-'+a.mode);ctx.imageSmoothingEnabled=false;ctx.clearRect(0,0,880,560);if(bg)ctx.drawImage(bg,0,0,880,560);"
new="const a=AL.game.diving.active,c=$('dive-map'),ctx=c.getContext('2d');ctx.imageSmoothingEnabled=false;ctx.clearRect(0,0,880,560);AL.DivingArt.environment(ctx,a.region,a.mode,880,560);"
assert old in s;s=s.replace(old,new);p.write_text(s,encoding='utf8')
p=r/'css/diving.css'
s=p.read_text(encoding='utf8')
s+='\n/* Destination identity uses one registered source in planning, map and results. */\n.dive-planning{align-items:start}.dive-scene-preview{height:auto;min-height:0;max-height:none;aspect-ratio:3/2;object-fit:cover;object-position:center;background:#071d2b}.dive-result-scene{display:block;width:100%;height:160px;object-fit:cover;object-position:50% 62%;image-rendering:pixelated;border-radius:7px;border:1px solid #425b72;margin:16px 0;background:#071d2b}@media(max-width:850px){.dive-scene-preview{height:auto;max-height:300px;aspect-ratio:3/2}.dive-result-scene{height:120px}}\n'
p.write_text(s,encoding='utf8')
print('Presentation integrated')
