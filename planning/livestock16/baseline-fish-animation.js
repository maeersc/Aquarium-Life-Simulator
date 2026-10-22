"use strict";
// Render-only rig: sampled authored pixels, fixed head/body core, integer fin tips.
AL.FishAnimation=(()=>{
 const data=AL.FishAnimationData,rigs=new WeakMap(),sources=new WeakMap(),poses=new Map(),errors=[],maxPoses=768;
 let serial=0,builds=0,hits=0;
 const labels={rest:/Rest|Hide/,guard:/Guard and fan/,nest:/Prepare nest/,court:/Courtship/,spawn:/Synchronized spawning/,burst:/Flee|Chase|Hunt/};
 const clamp=(v,a,b)=>Math.max(a,Math.min(b,v)),tau=Math.PI*2;
 const stage=f=>f.growth<.3?'baby':f.growth<1?'juvenile':'adult';
 function profile(id){const row=data.species[id];if(!row&&AL.Data.species[id]?.water==='marine'&&!errors.includes(id)){errors.push(id);console.error('[FishAnimation] Missing marine motion profile: '+id);}return row?data.families[row.family]:null;}
 function update(f,pos,dt,desired=pos.facing){
  const row=data.species[f.species],p=row&&data.families[row.family];if(!p)return null;
  let v=pos.animation;if(!v){const seed=AL.Random.hash(f.id);v=pos.animation={phase:(seed%1009)/1009,state:'idle',tail:0,fin:0,bob:0,bank:0,rate:0,direction:pos.facing||1,target:pos.facing||1,turn:1};}
  if(f.dead){v.state='dead';v.tail=v.fin=v.bob=v.bank=v.rate=0;v.turn=1;return v;}
  const step=clamp(dt,0,.1),d=AL.Data.species[f.species],speed=Math.hypot(f.vx||0,f.vy||0)/Math.max(.005,.017*d.activity),behavior=f.behavior||'',perched=(row.family==='goby'||row.family==='blenny')&&speed<.3;
  let state=labels.rest.test(behavior)?'rest':behavior==='Eat'?'feed':behavior==='Male mouthbrooding'?'mouthbrood':labels.guard.test(behavior)?'guard':labels.nest.test(behavior)?'nest':labels.court.test(behavior)?'court':labels.spawn.test(behavior)?'spawn':speed>1.2||labels.burst.test(behavior)?'fast':speed<.15?(perched?'perch':'idle'):'swim';
  let symptom='';for(const c of f.healthState?.conditions||[]){if(c.severity>=.12&&c.age>=(AL.Health.conditions[c.type]?.onset??0)&&!c.carrier){symptom=c.type;break;}}
  let rate=p.frequency*(.48+Math.min(1.8,speed)*.52),strength=state==='rest'?.45:state==='idle'||state==='perch'?.65:state==='fast'?1.35:1;
  if(state==='guard'||state==='nest'){rate=p.frequency*1.1;strength=.65;}if(state==='mouthbrood'){rate*=.65;strength=.55;}if(state==='feed'){rate*=1.2;strength=.95;}
  if(f.hp<40||symptom==='injury'||symptom==='bacterial'||symptom==='malnutrition'){state='weak';rate*=.65;strength*=.6;}
  else if(symptom==='velvet'||symptom==='brook'){state='respiratory';rate*=1.25;strength*=.7;}
  else if(symptom==='ich'||symptom==='flukes')state='irritation';
  if(f.stress>55&&state!=='respiratory'){rate*=.8;strength*=.75;}
  const life=data.stages[stage(f)];rate*=life.frequency;v.phase=(v.phase+step*rate)%1;v.rate=rate;v.state=state;
  if(desired!==v.target){v.target=desired;v.turn=0;}
  if(v.turn<1){v.turn=Math.min(1,v.turn+step/.32);if(v.turn>=.5)v.direction=v.target;}
  const wave=Math.sin(v.phase*tau),finWave=Math.sin((v.phase*2+.23)*tau);
  v.tail=Math.round(wave*Math.max(.8,p.tail*strength*life.amplitude));
  v.fin=Math.round(finWave*Math.max(.8,p.fin*(state==='guard'?1.4:state==='respiratory'?1.25:strength)*life.amplitude));
  if(row.appendages?.[stage(f)]==='caudal-fold-only')v.fin=0;
  v.bob=perched||state==='rest'||state==='guard'||state==='nest'?0:Math.round(Math.sin(v.phase*tau*.5)*p.bob*(state==='feed'?2:1));
  const slope=clamp((f.vy||0)*v.direction*1.2,-.04,.04),turnBank=v.turn<1?Math.sin(v.turn*Math.PI)*.065*v.direction:0;
  v.bank=Math.round((slope+turnBank+(state==='feed'?(d.diet.includes('algae')?.045:.025)*wave:state==='nest'?.03:state==='irritation'&&v.phase<.12?.045:0))*100)/100;
  return v;
 }
 function source(f,phase=0){
  const life=stage(f),artStage=data.species[f.species]?.artStages?.[life]||life,dead=f.dead?'dead':'alive';
  if(f.species==='clown'&&!f.variety&&!f.dead&&life==='adult')return AL.Art.sprite(f.species,Math.floor(phase*4)%4,f.genes.color);
  const image=AL.ExpansionArt.frame(f.species,artStage,dead)||AL.ClownArt.frame(f.species,f.variety||null,artStage,dead,phase*4/6,f.genes?.color||1)||AL.LifeStages.frame(f.species,artStage,dead,f.genes?.color||1)||AL.Art.sprite(f.species,Math.floor(phase*4)%4,f.genes.color);
  const eye=data.species[f.species]?.eyes?.[life];if(!f.dead&&eye&&!image.artMeta?.eye)image.artMeta={...image.artMeta,eye};return image;
 }
 function rig(source,w,h,id){
  let sizes=rigs.get(source);if(!sizes){sizes=new Map();rigs.set(source,sizes);}const key=w+':'+h+':'+id;if(sizes.has(key))return sizes.get(key);
  const base=AL.SpriteKit.raster(source,w,h),g=base.getContext('2d'),a=g.getImageData(0,0,w,h).data,columns=[];let left=w,right=0,top=h,bottom=0;
  for(let x=0;x<w;x++){let first=h,last=-1;for(let y=0;y<h;y++)if(a[(y*w+x)*4+3]>0){first=Math.min(first,y);last=y;}columns.push({first,last});if(last>=0){left=Math.min(left,x);right=Math.max(right,x);top=Math.min(top,first);bottom=Math.max(bottom,last);}}
  const row=data.species[id],p=profile(id),bw=Math.max(1,right-left+1),bh=Math.max(1,bottom-top+1),eye=base.eyeBounds,cy=eye?eye.y+eye.h/2+bh*.04:(top+bottom)/2;
  const joint=Math.round(left+bw*row.tailRoot),head=Math.min(Math.round(right-bw*row.headProtection),eye?eye.x-2:w),half=Math.max(1,bh*p.bodyHalf);
  const value={base,columns,left,right,top,bottom,joint,head,cy,half,eye};if(sizes.size>=12)sizes.delete(sizes.keys().next().value);sizes.set(key,value);builds++;return value;
 }
 function pose(source,w,h,id,tail,fin){
  const definition=data.species[id],sourceStage=source.artMeta?.stage;if(definition.appendages?.[sourceStage]==='caudal-fold-only'||w<(definition.outerFinMinimum?.[sourceStage]||0))fin=0;
  w=Math.max(1,Math.round(w));h=Math.max(1,Math.round(h));let sid=sources.get(source);if(!sid){sid=++serial;sources.set(source,sid);}const key=`${sid}:${w}:${h}:${id}:${tail}:${fin}`;if(poses.has(key)){const value=poses.get(key);poses.delete(key);poses.set(key,value);hits++;return value;}
  const r=rig(source,w,h,id),pad=4,c=document.createElement('canvas');c.width=w+pad*2;c.height=h+pad*2;const g=c.getContext('2d');g.imageSmoothingEnabled=false;
  for(let x=0;x<w;x++){
   const col=r.columns[x];if(col.last<0)continue;
   if(x<r.joint){const weight=(r.joint-x)/Math.max(1,r.joint-r.left),dy=Math.round(tail*weight*weight);g.drawImage(r.base,x,0,1,h,x+pad,pad+dy,1,h);continue;}
   if(x>=r.head){g.drawImage(r.base,x,0,1,h,x+pad,pad,1,h);continue;}
   const upper=clamp(Math.floor(r.cy-r.half),0,h),lower=clamp(Math.ceil(r.cy+r.half),0,h),weight=Math.sin((x-r.joint)/Math.max(1,r.head-r.joint)*Math.PI),n=Math.round(fin*weight);
   // The body core stays bit-identical. Only authored outer fin pixels flex,
   // with their body-side hinge fixed and one-pixel overlap at the attachment.
   if(col.first<upper){const len=upper-col.first,dest=Math.max(1,len+n);g.drawImage(r.base,x,col.first,1,len+1,x+pad,pad+upper-dest,1,dest+1);}
   g.drawImage(r.base,x,upper,1,Math.max(1,lower-upper),x+pad,pad+upper,1,Math.max(1,lower-upper));
   if(col.last>=lower){const len=col.last-lower+1,dest=Math.max(1,len-n);g.drawImage(r.base,x,lower-1,1,len+1,x+pad,pad+lower-1,1,dest+1);}
  }
  c.animationMeta={speciesId:id,width:w,height:h,pad,tail,fin,joint:r.joint,head:r.head,cy:r.cy,half:r.half,eye:r.eye};
  if(poses.size>=maxPoses)poses.delete(poses.keys().next().value);poses.set(key,c);return c;
 }
 function draw(ctx,f,sprite,x,y,w,h,pos){
  const v=pos.animation;if(!v||f.dead){AL.SpriteKit.draw(ctx,sprite,x,y,w,h,pos.facing,f.dead&&!sprite.artMeta?.authoredDeath);return;}
  // Keep existing authored adult swim cycles intact rather than warping them.
  const authored=AL.Data.species[f.species].clownfish&&stage(f)==='adult';
  if(authored){ctx.save();ctx.translate(Math.round(x),Math.round(y+v.bob));ctx.rotate(v.bank);AL.SpriteKit.draw(ctx,sprite,0,0,w,h,v.direction);ctx.restore();return;}
  const im=pose(sprite,w,h,f.species,v.tail,v.fin);
  ctx.save();ctx.imageSmoothingEnabled=false;ctx.translate(Math.round(x),Math.round(y+v.bob));ctx.rotate(v.bank);ctx.scale(v.direction===-1?-1:1,1);ctx.drawImage(im,-Math.floor(w/2)-4,-Math.floor(h/2)-4);ctx.restore();
 }
 function audit(){return Object.values(AL.Data.species).filter(d=>d.water==='marine'&&!data.species[d.id]).map(d=>d.id);}
 return {data,profile,stage,update,source,pose,draw,audit,errors,get metrics(){return {rigBuilds:builds,poseHits:hits,poseCache:poses.size,maxPoses};}};
})();
