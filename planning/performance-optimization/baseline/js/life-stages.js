"use strict";
// Presentation only: never creates livestock or changes simulation/save fields.
AL.LifeStages=(()=>{
  const records=AL.LifeStageManifest?.records||[],items=new Map(),cache=new Map(),errors=[];
  const ready=Promise.all(records.map(meta=>new Promise(resolve=>{
    const image=new Image();image.onload=()=>{items.set(meta.id,{meta,image});resolve();};
    image.onerror=()=>{errors.push(meta.id);resolve();};image.src=meta.src;
  })));
  function stageFor(fish){return fish.growth<.3?'baby':fish.growth<1?'juvenile':'adult';}
  function frame(id,stage='adult',state='alive',tone=1){
    const item=items.get(id),index=item?.meta.frames[stage]?.[state];if(index===undefined)return null;
    tone=Math.round(Math.min(1.4,Math.max(.6,Number(tone)||1))*10)/10;
    const key=[id,stage,state,tone].join(':');if(cache.has(key))return cache.get(key);
    const {meta,image}=item,c=document.createElement('canvas');c.width=meta.frameWidth;c.height=meta.frameHeight;
    const ctx=c.getContext('2d');ctx.imageSmoothingEnabled=false;ctx.filter=`brightness(${tone})`;
    ctx.drawImage(image,index*c.width,0,c.width,c.height,0,0,c.width,c.height);
    c.artMeta={speciesId:id,stage,state,frame:index,frameCount:1,eye:meta.eyes[index],anchor:[96,80],nativeFacing:1,facingBehavior:meta.facing,authoredDeath:state==='dead',layer:'livestock'};
    if(cache.size>=256)cache.delete(cache.keys().next().value);cache.set(key,c);return c;
  }
  function forFish(fish){return frame(fish.species,stageFor(fish),fish.dead?'dead':'alive',fish.genes?.color||1);}
  function size(id,stage){
    if(stage==='egg')return {width:16,height:13};
    const d=AL.Data.species[id];
    if(!d){const width={baby:16,juvenile:30,adult:50}[stage];return {width,height:Math.round(width*160/192)};}
    const growth={baby:.15,juvenile:.6,adult:1}[stage],scale=Math.max(.35,Math.min(1.7,.6+d.size/28)*Math.sqrt(growth));
    const width=Math.round(64*scale);return {width,height:Math.round(width*160/192)};
  }
  return {ready,records,errors,frame,forFish,stageFor,size,metadata:id=>items.get(id)?.meta,get loaded(){return items.size;}};
})();
