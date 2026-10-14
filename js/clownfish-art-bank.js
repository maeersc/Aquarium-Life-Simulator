"use strict";
AL.ClownArt=(()=>{
  const items=new Map(),cache=new Map(),records=AL.ClownArtManifest?.records||[],errors=[];
  const ready=Promise.all(records.map(meta=>new Promise(resolve=>{const image=new Image();image.onload=()=>{items.set(meta.family+':'+meta.id,{meta,image});resolve();};image.onerror=()=>{errors.push(meta.id);resolve();};image.src=meta.src;})));
  function metadata(species,variety){return items.get((variety?'varieties:'+variety:'species:'+species))?.meta;}
  function frame(species,variety=null,stage='adult',state='alive',time=0,tone=1,animate=true){
    let item=items.get(variety?'varieties:'+variety:'species:'+species);
    if(variety&&['egg','baby'].includes(stage))item=items.get('species:'+AL.Clownfish.varieties[variety]?.speciesId);
    if(!item)return null;const {meta,image}=item,map=meta.frames[stage];if(!map)return null;
    const index=stage==='adult'&&state==='alive'&&animate?meta.swim[Math.floor(Math.max(0,time)*6)%meta.swim.length]:map[state];
    if(index===undefined)return null;tone=Math.round(AL.Core.clamp(tone,.6,1.4)*10)/10;const key=meta.family+':'+meta.id+':'+index+':'+tone;if(cache.has(key))return cache.get(key);
    const c=document.createElement('canvas');c.width=192;c.height=160;const ctx=c.getContext('2d');ctx.imageSmoothingEnabled=false;ctx.filter=`brightness(${tone})`;
    const nativeLeft=meta.nativeFacings?.[index]===-1;ctx.save();if(nativeLeft){ctx.translate(192,0);ctx.scale(-1,1);}ctx.drawImage(image,index*192,0,192,160,0,0,192,160);ctx.restore();
    const eye=meta.eyes[index]?{...meta.eyes[index]}:null;if(nativeLeft&&eye)eye.x=192-eye.x;
    c.artMeta={speciesId:species,variety,stage,state,frame:index,frameCount:meta.swim.length,frameDurationMs:meta.frameDurationMs,eye,nativeFacing:1,anchor:meta.anchor,facingBehavior:meta.facing,authoredDeath:state==='dead',layer:'livestock'};
    if(cache.size>=512)cache.delete(cache.keys().next().value);cache.set(key,c);return c;
  }
  function forFish(f,time){if(!AL.Data.species[f.species]?.clownfish)return null;const stage=AL.LifeStages.stageFor(f);return frame(f.species,f.variety||null,stage,f.dead?'dead':'alive',f.behavior==='Rest'?time*.5:time,f.genes?.color||1);}
  function thumb(species,variety=null){return frame(species,variety)?.toDataURL()||null;}
  return {ready,records,errors,metadata,frame,forFish,thumb,get loaded(){return items.size;}};
})();
