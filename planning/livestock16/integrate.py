"""One-time render-only integration and calm artistic rate calibration."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[2]
p=root/'assets/animation/fish-registry.json'
d=json.loads(p.read_text())
rates={'clown':.5,'basslet':.48,'goby':.45,'hoverGoby':.52,'blenny':.46,'cruiser':.5,'wrasse':.56,'cardinal':.42,'schooler':.52,'extendedFin':.42,'dartfish':.5,'angel':.5,'butterfly':.48,'filefish':.44,'boxfish':.44,'fictional':.44}
d['version']=2
d['normalPlayback']='Artistic calm cycle rates, normal travel approximately 6-10 requested slots/second; slots are not authored frame counts'
for k,v in d['families'].items():
    v.update(frequency=rates[k],tail=min(v['tail'],1.1),fin=min(v['fin'],1.0),bob=0)
d['stages']['baby']['frequency']=1.08
d['stages']['juvenile']['frequency']=1.04
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
(root/'js/fish-animation-data.js').write_text('"use strict";\n// Generated from assets/animation/fish-registry.json\nAL.FishAnimationData='+json.dumps(d,separators=(',',':'),ensure_ascii=False)+';\n',encoding='utf8')
for name in ['index.html','fish-animation-review.html']:
    p=root/name;s=p.read_text(encoding='utf8')
    needle='<script defer src="js/fish-animation-data.js"></script>'
    assert needle in s
    s=s.replace(needle,'<script defer src="js/livestock-animation-data.js"></script>'+needle).replace('v4.0.3','v4.0.4')
    p.write_text(s,encoding='utf8')
p=root/'js/expansion-ui.js';s=p.read_text(encoding='utf8')
needle="AL.SpriteKit.draw(g,im,p.x*480,p.y*240-h*.3+sway,w,h,f.heading);"
replacement="const life=f.growth<.3?'baby':f.growth<1?'juvenile':'adult',state=f.dead?'dead':/Walk|Crawl|Forage/.test(f.behavior||'')?'walk':'idle';if(!AL.FishAnimation?.drawResident(g,d.id,life,state,p.x*480,p.y*240-h*.3,w,h,renderer.time,f.heading))AL.SpriteKit.draw(g,im,p.x*480,p.y*240-h*.3+sway,w,h,f.heading);"
assert needle in s;s=s.replace(needle,replacement);p.write_text(s,encoding='utf8')
print('Updated calm profiles and shared fish/coral/invertebrate sheet hooks')
