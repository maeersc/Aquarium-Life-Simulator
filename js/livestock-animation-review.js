"use strict";
(async()=>{
 await Promise.all([AL.Art.ready,AL.AssetBank.ready,AL.ExpansionArt.ready,AL.ClownArt.ready,AL.LifeStages.ready]);
 const A=AL.FishAnimation,$=id=>document.getElementById(id),entries=A.catalog.entries.filter(e=>e.productionEligible!==false),seed={seed:1616,nextId:1,time:480};let entry,f,pos,paused=false,clock=0,last=performance.now(),record=null,shownRecord=null;
 const option=(value,label)=>{const o=document.createElement('option');o.value=value;o.textContent=label;return o;};
 for(const row of entries)$('gallery-species').append(option(row.id,row.name+' · '+row.category));
 $('gallery-totals').textContent=entries.length+' marine entries · '+A.catalog.batches.length+' audit batches · '+entries.reduce((n,e)=>n+e.clips.length,0)+' validated production sheets · '+entries.filter(e=>e.status!=='complete').length+' entries awaiting artwork';
 function setStates(){const life=$('gallery-stage').value,fish=entry.category==='fish';$('gallery-state').replaceChildren(...(fish?(life==='egg'?['Alive','Dead']:['Swim','Idle','Fast','Rest','Eat','Dead']):entry.category==='coral'?['Healthy','Stressed','Bleached','Tissue loss','Dead']:['Idle','Walk','Rest','Dead']).map(x=>option(x,x)));}
 function reset(){entry=entries.find(e=>e.id===$('gallery-species').value);f=entry.category==='fish'?AL.Core.fish(seed,entry.id,{genes:{color:1,size:1,longevity:1,immunity:1,fertility:1}}):null;pos={facing:1};clock=0;const stages=entry.category==='fish'?['adult','juvenile','baby','egg']:entry.stages;$('gallery-stage').replaceChildren(...stages.map(x=>option(x,x==='baby'?'Early stage':x)));$('gallery-variety').replaceChildren(option('','Natural / standard'),...entry.varieties.map(v=>option(v.id,v.name)));$('gallery-variety').disabled=!entry.varieties.length;setStates();$('gallery-source').src=entry.existingPath;$('gallery-source-path').textContent=entry.existingPath;$('gallery-status').textContent=entry.name+' · '+entry.category+' · '+(entry.scientificName||'Retained legacy identity')+' · '+entry.status+' · '+entry.framesCompleted+' authored frames / '+entry.clips.length+' registered sheets';$('gallery-gap').textContent=entry.missingArtwork;record=null;draw(0);}
 function original(life,dead){
  if(f){if(life==='egg')return AL.ClownArt.frame(entry.id,f.variety,life,dead?'dead':'alive')||AL.LifeStages.frame(entry.id,life,dead?'dead':'alive')||AL.ExpansionArt.frame(entry.id,life,dead?'dead':'alive');return A.source({...f,dead},0,false);}
  if(entry.category==='coral')return AL.ExpansionArt.frame(entry.id,life,dead?'dead':'alive')||AL.AssetBank.coral(entry.id,dead?'dead':'healthy',0);
  return AL.ExpansionArt.frame(entry.id,life,dead?'dead':'alive');
 }
 function paint(canvas,im,render){const g=canvas.getContext('2d');g.clearRect(0,0,canvas.width,canvas.height);g.imageSmoothingEnabled=false;if(!im)return;const width=160,height=Math.round(width*im.height/im.width);if(render)render(g,width,height);else AL.SpriteKit.draw(g,im,200,120,width,height,Number($('gallery-facing').value));}
 function draw(dt){const speed=Number($('gallery-speed').value);clock+=dt*speed;const life=$('gallery-stage').value,state=$('gallery-state').value,dead=state==='Dead',direction=Number($('gallery-facing').value);let current;
  if(f){f.growth={egg:0,baby:.15,juvenile:.6,adult:1.1}[life];f.variety=$('gallery-variety').value||null;f.dead=dead;f.behavior=state==='Idle'?'Hover':state;f.vx=(state==='Swim'?.8:state==='Fast'?1.8:0)*.017*AL.Data.species[f.species].activity;f.vy=0;if(life!=='egg')A.update(f,pos,dt*speed,direction);}
  const base=original(life,dead);paint($('gallery-existing'),base);
  const slot=entry.category==='fish'?'swim':entry.category==='coral'?state==='Healthy'?'polyp_motion':state.toLowerCase().replace(' ','-'):state.toLowerCase();record=dead||life==='egg'?null:f?A.sheetForFish(f):A.sheets.find(entry.id,life,slot);
  if(f&&life!=='egg'){current=A.source(f,pos.animation.phase);paint($('gallery-preview'),current,(g,w,h)=>A.draw(g,f,current,200,120,w,h,pos));}
  else if(record){current=A.sheets.frame(record,clock*record.clip.framesPerSecond/16);paint($('gallery-preview'),current);}
  else if(entry.category==='coral'&&!dead){current=AL.ExpansionArt.frame(entry.id,life,state==='Healthy'?'alive':state.toLowerCase().replace(' ','-'))||AL.AssetBank.coral(entry.id,state==='Healthy'?'healthy':state.toLowerCase().replace(' ','-'),clock*.8);paint($('gallery-preview'),current);}
  else paint($('gallery-preview'),base);
  $('gallery-frame-label').textContent=record?'Authored cell '+(Math.floor((f?pos.animation.phase:clock*record.clip.framesPerSecond/16)*16)%16+1)+'/16':f&&life!=='egg'&&!dead?'Existing '+entry.existingFrameCount+'-pose / procedural preview; '+(pos.animation.rate*16).toFixed(1)+' requested slots/sec':'Existing stage/state artwork; no 16-frame cycle';
  $('gallery-sheet-message').textContent=record?'Validated production sheet; user approval: '+(entry.userApproved?'recorded':'not recorded'):'No completed 16-frame sheet for this slot. Missing authored frames are not replaced by repeated images.';
  $('gallery-sheet').hidden=!record;$('gallery-frame').disabled=!record;
  if(record){if(record!==shownRecord){$('gallery-sheet').src=record.clip.src||record.clip.path;shownRecord=record;}A.sheets.load(record);paint($('gallery-frame-preview'),A.sheets.frame(record,(Number($('gallery-frame').value)-1)/16));}else{shownRecord=null;paint($('gallery-frame-preview'),null);}
 }
 $('gallery-species').onchange=reset;$('gallery-stage').onchange=()=>{setStates();draw(0)};for(const id of ['gallery-state','gallery-variety','gallery-facing','gallery-frame'])$(id).oninput=()=>draw(0);
 $('gallery-speed').oninput=()=>{$('gallery-speed-label').textContent=$('gallery-speed').value+'×';draw(0)};
 $('gallery-play').onclick=()=>{paused=!paused;$('gallery-play').textContent=paused?'Play':'Pause'};$('gallery-step').onclick=()=>{paused=true;$('gallery-play').textContent='Play';draw(.125)};
 reset();window.LivestockGallery={get entry(){return entry},get paused(){return paused},draw};
 function loop(now){const dt=Math.min(.1,(now-last)/1000);last=now;if(!paused)draw(dt);requestAnimationFrame(loop)}requestAnimationFrame(loop);
})().catch(error=>{document.getElementById('gallery-status').textContent='Gallery failed: '+error.message;console.error(error)});
