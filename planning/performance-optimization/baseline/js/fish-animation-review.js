"use strict";
(async()=>{
 await Promise.all([AL.Art.ready,AL.ExpansionArt.ready,AL.ClownArt.ready,AL.LifeStages.ready]);
 const $=id=>document.getElementById(id),A=AL.FishAnimation,seed={seed:8923,nextId:1,time:480},ids=Object.keys(A.data.species);let f,pos,other,paused=false,last=performance.now(),clock=0;
 for(const id of ids){const d=AL.Data.species[id],o=document.createElement('option');o.value=id;o.textContent=d.name+(d.purchaseVerified===false?' · acquisition held':'');$('motion-fish').append(o);}
 function reset(){const id=$('motion-fish').value;f=AL.Core.fish(seed,id,{genes:{color:1,size:1,longevity:1,immunity:1,fertility:1}});pos={facing:1};other={facing:-1};$('motion-variety').innerHTML='<option value="">Natural / standard</option>';for(const v of Object.values(AL.Clownfish.varieties).filter(v=>v.speciesId===id)){const o=document.createElement('option');o.value=v.id;o.textContent=v.name;$('motion-variety').append(o);}}
 function draw(dt){clock+=dt;const mode=$('motion-state').value,d=AL.Data.species[f.species];f.growth={baby:.15,juvenile:.6,adult:1.1}[$('motion-stage').value];f.variety=$('motion-variety').value||null;f.behavior=mode;f.vx=['Swim','Fast'].includes(mode)?.017*d.activity*(mode==='Fast'?1.8:.8):0;f.vy=0;f.dead=mode==='Dead';f.healthState.conditions=mode==='Respiratory'?[{type:'velvet',severity:.5,age:48}]:mode==='Weak'?[{type:'injury',severity:.5,age:48}]:[];
  A.update(f,pos,dt,mode==='Turn'?(Math.floor(clock/2)%2?-1:1):1);A.update(f,other,dt,-1);const source=A.source(f,pos.animation.phase);
  for(const [id,p] of [['motion-right',pos],['motion-left',other]]){const canvas=$(id),g=canvas.getContext('2d');g.clearRect(0,0,320,180);g.imageSmoothingEnabled=false;A.draw(g,f,source,160,90,128,Math.round(128*source.height/source.width),p);}
  $('motion-description').textContent=d.name+' · '+d.scientificName+' · '+A.profile(f.species).name+' · '+pos.animation.state+(A.data.species[f.species].earlyArtNote&&f.growth<.3?' · '+A.data.species[f.species].earlyArtNote:'');
 }
 $('motion-fish').onchange=()=>{reset();draw(0)};for(const id of ['motion-stage','motion-state','motion-variety'])$(id).onchange=()=>draw(0);
 $('motion-pause').onclick=()=>{paused=!paused;$('motion-pause').textContent=paused?'Play':'Pause'};$('motion-step').onclick=()=>draw(.1);
 reset();draw(0);function loop(now){const dt=Math.min(.05,(now-last)/1000);last=now;if(!paused)draw(dt);requestAnimationFrame(loop)}requestAnimationFrame(loop);
})();
