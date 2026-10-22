from pathlib import Path
r=Path(__file__).resolve().parents[2]
p=r/'index.html';s=p.read_text(encoding='utf8');needle='<script defer src="js/placement.js"></script>'
assert needle in s;s=s.replace(needle,needle+'<script defer src="js/fish-animation-data.js"></script><script defer src="js/fish-animation.js"></script>',1);p.write_text(s,encoding='utf8')
p=r/'js/render.js';s=p.read_text(encoding='utf8')
s=s.replace('this.positions=new Map();','this.positions=new Map();this.drawFish=[];this.fishOrder=(a,b)=>a.y-b.y;this.visualFrame=0;',1)
s=s.replace('this.hitboxes=[];\n    const drawFlora','this.hitboxes.length=0;this.visualFrame++;\n    const drawFlora',1)
old='    const currentIds=new Set(t.fish.map(f=>f.id));for(const id of this.positions.keys())if(!currentIds.has(id))this.positions.delete(id);'
assert old in s;s=s.replace(old,'    this.drawFish.length=t.fish.length;for(let i=0;i<t.fish.length;i++)this.drawFish[i]=t.fish[i];this.drawFish.sort(this.fishOrder);',1)
start=s.index('    for(const f of [...t.fish].sort((a,b)=>a.y-b.y)){');end=s.index('      if(!f.dead&&f.reproduction?.pairId)',start)
s=s[:start]+'''    for(const f of this.drawFish){
      const d=AL.Data.species[f.species],animated=marine&&AL.FishAnimation?.profile(f.species);
      // Interpolation, turns and fin clocks live only in renderer-owned records.
      const pos=this.positions.get(f.id)||{x:f.x,y:f.y,facing:f.heading||1};const oldX=pos.x,blend=1-Math.exp(-dt*Math.max(.7,s.settings.speed*.7));pos.x+=(f.x-pos.x)*blend;pos.y+=(f.y-pos.y)*blend;
      const desired=!f.dead&&blend>0?AL.SpriteKit.facing(pos.facing,f.x-oldX):pos.facing;
      if(animated){const motion=AL.FishAnimation.update(f,pos,dt,desired);pos.facing=motion.direction;}else pos.facing=desired;
      pos.seen=this.visualFrame;this.positions.set(f.id,pos);
      const scale=Math.max(.35,Math.min(1.7,.6+d.size/28)*Math.sqrt(f.growth)*f.genes.size),w=Math.round(64*scale),x=Math.round(pos.x*W),y=Math.round(pos.y*H);
      // Conservative world-space culling avoids all sprite/rig work offscreen.
      if(animated&&(x+w+12<W*this.pan-W/(2*this.zoom)||x-w-12>W*this.pan+W/(2*this.zoom)||y+w+12<H/2-H/(2*this.zoom)||y-w-12>H/2+H/(2*this.zoom)))continue;
      const frame=f.dead?0:Math.floor(time*(f.behavior==='Rest'?3:6)*d.activity)%4,keepApprovedClown=f.species==='clown'&&!f.variety&&!f.dead&&f.growth>=1;
      const stageSprite=animated?AL.FishAnimation.source(f,pos.animation.phase):AL.ExpansionArt?.forFish(f)||(keepApprovedClown?null:(AL.ClownArt?.forFish(f,time)||AL.LifeStages?.forFish(f)));
      const baseSprite=stageSprite||AL.Art.sprite(f.species,frame,f.genes.color),sprite=AL.Patterns?.sprite(f,baseSprite)||baseSprite,h=stageSprite?Math.round(w*sprite.height/sprite.width):Math.round(40*scale);
      g.save();g.globalAlpha=f.dead?.65:f.behavior==='Hide'?.65:1;if(f.disease)g.globalAlpha=.75;if(animated)AL.FishAnimation.draw(g,f,sprite,x,y,w,h,pos);else AL.SpriteKit.draw(g,sprite,x,y,w,h,pos.facing,f.dead&&!stageSprite);g.restore();
''' + s[end:]
old='w:w*this.zoom/W,h:h*this.zoom/H});\n    }\n    AL.ExpansionUI'
new='w:(w+(animated?16:0))*this.zoom/W,h:(h+(animated?16:0))*this.zoom/H});\n    }\n    for(const [id,pos] of this.positions)if(pos.seen!==this.visualFrame)this.positions.delete(id);\n    AL.ExpansionUI'
assert old in s;s=s.replace(old,new,1);p.write_text(s,encoding='utf8')
print('Marine render-only animation integrated; freshwater path retained')
