"use strict";
// Render-only rig: sampled authored pixels, fixed head/body core, integer fin tips.
AL.FishAnimation=(()=>{
 const data=AL.FishAnimationData,rigs=new WeakMap(),sources=new WeakMap(),poses=new Map(),errors=[],maxPoses=768;
 // The same presentation service owns authored sheets for fish and non-fish.
 // No production assets are inferred from the number of requested frame slots.
 function createSheetLibrary(entries,options={}){
  const records=new Map(),issues=[],frames=new Map(),decoded=new Map(),maxFrames=options.maxFrames||512,maxDecodedSheets=options.maxDecodedSheets||128,maxFrameBytes=options.maxFrameBytes||32*1024*1024,maxDecodedBytes=options.maxDecodedBytes||256*1024*1024;
  let frameHits=0,frameMisses=0,frameEvictions=0,frameBytes=0,decodedBytes=0;
  function touch(record){if(!record.image)return;if(!decoded.has(record))decodedBytes+=record.image.width*record.image.height*4;decoded.delete(record);decoded.set(record,true);while(decoded.size>maxDecodedSheets||decodedBytes>maxDecodedBytes){const old=decoded.keys().next().value;decoded.delete(old);decodedBytes-=old.image.width*old.image.height*4;old.image=null;old.pending=null;}}
  for(const entry of entries)for(const clip of entry.clips||[]){
   if(clip.status!=='production'||clip.frameCount!==16||clip.order?.length!==16||new Set(clip.order).size!==16||clip.order.some(i=>!Number.isInteger(i)||i<0||i>15)||!clip.validation?.visualReview){issues.push(entry.id+': unvalidated sheet');continue;}
   const key=[entry.id,clip.stage,clip.state,clip.variety||''].join(':');if(records.has(key)){issues.push(key+': duplicate');continue;}
   records.set(key,{clip,id:entry.id,image:null,pending:null,failed:false});
  }
  function find(id,life,state='swim',variety=null){return records.get([id,life,state,variety||''].join(':'))||null;}
  function load(record){
   if(!record||record.failed)return Promise.resolve(false);if(record.image){touch(record);return Promise.resolve(true);}if(record.pending)return record.pending;
   record.pending=new Promise(resolve=>{const im=new Image();im.onload=()=>{
    const c=record.clip,cols=c.columns;if(im.width!==c.frameWidth*cols||im.height!==c.frameHeight*(16/cols)){record.failed=true;issues.push(record.id+': cell dimensions');resolve(false);return;}
    // Validate real decoded cells once. Never accept blank or repeated poses.
    if(!record.validated){const cv=document.createElement('canvas');cv.width=c.frameWidth;cv.height=c.frameHeight;const g=cv.getContext('2d',{willReadFrequently:true}),unique=new Set();
    for(let i=0;i<16;i++){g.clearRect(0,0,cv.width,cv.height);g.drawImage(im,i%cols*cv.width,Math.floor(i/cols)*cv.height,cv.width,cv.height,0,0,cv.width,cv.height);const pixels=g.getImageData(0,0,cv.width,cv.height).data;let hash=2166136261,visible=0;
     for(let n=0;n<pixels.length;n++){hash=Math.imul(hash^pixels[n],16777619);if(n%4===3&&pixels[n])visible++;}
     if(!visible||unique.has(hash)){record.failed=true;issues.push(record.id+': blank/repeated cell '+i);resolve(false);return;}unique.add(hash);
    }
    }record.validated=true;record.image=im;touch(record);resolve(true);
   };im.onerror=()=>{record.failed=true;issues.push(record.id+': image failed');resolve(false);};if(AL.SpriteSources)AL.SpriteSources.load(record.clip).then(src=>{if(src)im.src=src;else im.onerror();}).catch(()=>im.onerror());else im.src=record.clip.src||record.clip.path;});return record.pending;
  }
  function frame(record,phase=0){if(!record)return null;const c=record.clip,index=c.order[((Math.floor(phase*16)%16)+16)%16],key=[record.id,c.stage,c.state,c.variety||'',index].join(':');if(frames.has(key)){frameHits++;const im=frames.get(key);frames.delete(key);frames.set(key,im);touch(record);return im;}if(!record.image){load(record);return null;}frameMisses++;touch(record);
   const cv=document.createElement('canvas');cv.width=c.frameWidth;cv.height=c.frameHeight;const g=cv.getContext('2d');g.imageSmoothingEnabled=false;g.drawImage(record.image,index%c.columns*cv.width,Math.floor(index/c.columns)*cv.height,cv.width,cv.height,0,0,cv.width,cv.height);
   cv.artMeta={speciesId:record.id,variety:c.variety||null,stage:c.stage,state:c.state,frame:'sheet16:'+record.id+':'+c.stage+':'+c.state+':'+(c.variety||'')+':'+index,frameIndex:index,frameCount:16,anchor:c.anchor,eye:c.eye||null,nativeFacing:1,facingBehavior:c.facing,authoredAnimation:true,frameDurationMs:1000/c.framesPerSecond,layer:'livestock'};cv.cacheKey='source:'+key;
   const bytes=cv.width*cv.height*4;while(frames.size&&(frames.size>=maxFrames||frameBytes+bytes>maxFrameBytes)){const first=frames.keys().next().value,old=frames.get(first);frameBytes-=old.width*old.height*4;frames.delete(first);frameEvictions++;}frames.set(key,cv);frameBytes+=bytes;return cv;
  }
  return {find,load,frame,issues,records,get metrics(){return {loaded:decoded.size,maxDecodedSheets,frameCache:frames.size,maxFrames,frameHits,frameMisses,frameEvictions,frameBytes,maxFrameBytes,decodedBytes,maxDecodedBytes};}};
 }
 const catalog=AL.LivestockAnimationData||{entries:[],batches:[]},sheets=createSheetLibrary(catalog.entries),tintedFrames=new WeakMap(),catalogById=new Map(catalog.entries.map(e=>[e.id,e]));
 function sheetForFish(f){if(f.dead)return null;const life=stage(f),entry=catalogById.get(f.species),sourceStage=entry?.stageAliases?.[life]||life,shared=f.variety&&entry?.varieties.find(v=>v.id===f.variety)?.sharedEarlyStages?.includes(life);return sheets.find(f.species,sourceStage,'swim',shared?null:f.variety);}
 const toneIds=new WeakMap(),toneCache=AL.Performance?new AL.Performance.PixelCache(64*1024*1024,8192):null;let toneSerial=0;
 function toneFrame(image,tone=1){tone=Math.round(clamp(Number(tone)||1,.6,1.4)*10)/10;if(tone===1)return image;if(!toneIds.has(image))toneIds.set(image,++toneSerial);const identity=image.cacheKey||toneIds.get(image),key=identity+':'+image.width+':'+image.height+':'+tone,hit=toneCache?.get(key);if(hit)return hit;let cache=tintedFrames.get(image);if(!cache){cache=new Map();tintedFrames.set(image,cache);}if(cache.has(tone))return cache.get(tone);const c=document.createElement('canvas');c.width=image.width;c.height=image.height;const g=c.getContext('2d');g.imageSmoothingEnabled=false;g.filter=`brightness(${tone})`;g.drawImage(image,0,0);c.artMeta={...image.artMeta,presentationTone:tone};c.cacheKey='tone:'+key;if(toneCache)return toneCache.set(key,c);cache.set(tone,c);return c;}
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
  const clip=sheetForFish(f),frequency=clip?clip.clip.framesPerSecond/16:p.frequency;
  let rate=frequency*(.7+Math.min(1.8,speed)*.3),strength=state==='rest'?.3:state==='idle'||state==='perch'?.5:state==='fast'?1.15:1;
  if(state==='rest'||state==='perch')rate*=.45;
  if(state==='guard'||state==='nest'){rate=frequency*.75;strength=.55;}if(state==='mouthbrood'){rate*=.65;strength=.45;}if(state==='feed'){rate*=1.1;strength=.85;}
  if(f.hp<40||symptom==='injury'||symptom==='bacterial'||symptom==='malnutrition'){state='weak';rate*=.65;strength*=.6;}
  else if(symptom==='velvet'||symptom==='brook'){state='respiratory';rate*=1.25;strength*=.7;}
  else if(symptom==='ich'||symptom==='flukes')state='irritation';
  if(f.stress>55&&state!=='respiratory'){rate*=.8;strength*=.75;}
  const life=data.stages[stage(f)];rate*=life.frequency;v.phase=(v.phase+step*rate)%1;v.rate=rate;v.state=state;
  if(desired!==v.target){v.target=desired;v.turn=0;}
  if(v.turn<1){v.turn=Math.min(1,v.turn+step/.32);if(v.turn>=.5)v.direction=v.target;}
  const wave=Math.sin(v.phase*tau),finWave=Math.sin((v.phase+.23)*tau);
  v.tail=Math.round(wave*Math.max(.55,p.tail*strength*life.amplitude));
  v.fin=Math.round(finWave*Math.max(.55,p.fin*(state==='guard'?1.15:state==='respiratory'?1.1:strength)*life.amplitude));
  if(row.appendages?.[stage(f)]==='caudal-fold-only')v.fin=0;
  v.bob=perched||state==='rest'||state==='guard'||state==='nest'?0:Math.round(Math.sin(v.phase*tau*.5)*p.bob*(state==='feed'?2:1));
  const slope=clamp((f.vy||0)*v.direction*.8,-.025,.025),turnBank=v.turn<1?Math.sin(v.turn*Math.PI)*.025*v.direction:0;
  v.bank=Math.round((slope+turnBank+(state==='feed'?(d.diet.includes('algae')?.045:.025)*wave:state==='nest'?.03:state==='irritation'&&v.phase<.12?.045:0))*100)/100;
  return v;
 }
 function source(f,phase=0,useSheets=true,deferTone=false){
  const life=stage(f),artStage=data.species[f.species]?.artStages?.[life]||life,dead=f.dead?'dead':'alive';
  if(!f.dead&&useSheets){const authored=sheets.frame(sheetForFish(f),phase);if(authored)return deferTone?authored:toneFrame(authored,f.genes?.color);}
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
 function draw(ctx,f,sprite,x,y,w,h,pos,deferTone=false){
  const v=pos.animation;if(!v||f.dead){AL.SpriteKit.draw(ctx,sprite,x,y,w,h,pos.facing,f.dead&&!sprite.artMeta?.authoredDeath);return;}
  // Keep existing authored adult swim cycles intact rather than warping them.
  const authored=sprite.artMeta?.authoredAnimation||(AL.Data.species[f.species].clownfish&&stage(f)==='adult');
  if(authored){ctx.save();ctx.translate(Math.round(x),Math.round(y+v.bob));ctx.rotate(v.bank);
   if(sprite.artMeta?.authoredAnimation){const raster=AL.SpriteKit.raster(sprite,w,h),im=deferTone?toneFrame(raster,f.genes?.color):raster,anchor=sprite.artMeta.anchor;ctx.imageSmoothingEnabled=false;ctx.scale(v.direction===-1?-1:1,1);ctx.drawImage(im,-Math.round(anchor[0]*w/sprite.width),-Math.round(anchor[1]*h/sprite.height));}
   else AL.SpriteKit.draw(ctx,sprite,0,0,w,h,v.direction);
   ctx.restore();return;}
  const im=pose(sprite,w,h,f.species,v.tail,v.fin);
  ctx.save();ctx.imageSmoothingEnabled=false;ctx.translate(Math.round(x),Math.round(y+v.bob));ctx.rotate(v.bank);ctx.scale(v.direction===-1?-1:1,1);ctx.drawImage(im,-Math.floor(w/2)-4,-Math.floor(h/2)-4);ctx.restore();
 }
 function audit(){return Object.values(AL.Data.species).filter(d=>d.water==='marine'&&!data.species[d.id]).map(d=>d.id);}
 function drawResident(ctx,id,life,state,x,y,width,height,time,direction=1){
  if(state==='dead')return false;const entry=catalogById.get(id);if(!entry||entry.category==='fish')return false;
  const record=sheets.find(id,life,state);if(!record)return false;const image=sheets.frame(record,time*record.clip.framesPerSecond/16);if(!image)return false;
  const anchor=record.clip.anchor;ctx.save();ctx.imageSmoothingEnabled=false;ctx.translate(Math.round(x),Math.round(y));if(record.clip.facing!=='fixed'&&direction===-1)ctx.scale(-1,1);ctx.drawImage(image,Math.round(-anchor[0]*width/image.width),Math.round(-anchor[1]*height/image.height),Math.round(width),Math.round(height));ctx.restore();return true;
 }
 function auditCatalog(){const expected=[...Object.entries(AL.Data.species).filter(([id,d])=>d.water==='marine'),...Object.entries(AL.Data.flora).filter(([id,d])=>d.water==='marine'),...Object.entries(AL.Data.invertebrates||{})].map(([id])=>id),ids=catalog.entries.map(e=>e.id);return {missing:expected.filter(id=>!ids.includes(id)),extra:ids.filter(id=>!expected.includes(id)),duplicates:ids.filter((id,i)=>ids.indexOf(id)!==i)};}
 return {data,catalog,sheets,sheetForFish,createSheetLibrary,profile,stage,update,source,pose,draw,drawResident,audit,auditCatalog,errors,get metrics(){return {rigBuilds:builds,poseHits:hits,poseCache:poses.size,maxPoses};}};
})();
