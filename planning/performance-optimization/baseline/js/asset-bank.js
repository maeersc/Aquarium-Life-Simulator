"use strict";
AL.AssetBank=(()=>{
  const records=AL.ArtUpdateManifest?.records||[],items=new Map(),cache=new Map(),errors=[];
  const ready=Promise.all(records.map(meta=>new Promise(resolve=>{
    const image=new Image();image.onload=()=>{items.set(meta.family+':'+meta.id,{meta,image});resolve();};image.onerror=()=>{errors.push(meta.id);resolve();};image.src=meta.src;
  })));
  function metadata(family,id){return items.get(family+':'+id)?.meta;}
  function frame(family,id,index=0,tone=1){
    const item=items.get(family+':'+id);if(!item)return null;const {meta,image}=item;
    index=((Math.floor(index)%meta.frames)+meta.frames)%meta.frames;tone=Math.round(AL.Core.clamp(tone,.6,1.4)*10)/10;
    const key=[family,id,index,tone].join(':');if(cache.has(key))return cache.get(key);
    const c=document.createElement('canvas');c.width=meta.frameWidth;c.height=meta.frameHeight;
    const ctx=c.getContext('2d');ctx.imageSmoothingEnabled=false;ctx.filter=`brightness(${tone})`;ctx.drawImage(image,index*c.width,0,c.width,c.height,0,0,c.width,c.height);
    if(meta.eye){
      const e=meta.eye;
      // A canonical local eye component prevents frame-to-frame pupil flicker.
      if(index){const base=frame(family,id,0,tone),x=Math.round(e.x-e.w/2),y=Math.round(e.y-e.h/2);ctx.filter='none';ctx.clearRect(x,y,e.w,e.h);ctx.drawImage(base,x,y,e.w,e.h,x,y,e.w,e.h);}
      c.artMeta={speciesId:id,frame:index,frameWidth:c.width,frameHeight:c.height,frameCount:meta.frames,frameDurationMs:meta.frameDurationMs,eye:e,anchor:meta.anchor,nativeFacing:1,facingBehavior:meta.facingBehavior,layer:meta.layer};
    }
    if(cache.size>=256)cache.delete(cache.keys().next().value);cache.set(key,c);return c;
  }
  function coralState(health){return health<=0?'dead':health<.35?'tissue-loss':health<.7?'stressed':'healthy';}
  function coral(id,state='healthy',phase=0){
    const meta=metadata('corals',id);if(!meta)return null;const indices=meta.stateFrames[state]||meta.stateFrames.healthy,beat=Math.abs(Math.floor(phase))%2;
    if(!meta.rigid||!beat||state==='dead')return frame('corals',id,indices[meta.rigid?0:beat]);
    // Preserve the rigid skeleton. Only selected existing polyp/tip highlights pulse.
    const key='polyp-pulse:'+id+':'+state;if(cache.has(key))return cache.get(key);
    const base=frame('corals',id,indices[0]),c=document.createElement('canvas');c.width=base.width;c.height=base.height;const ctx=c.getContext('2d');ctx.drawImage(base,0,0);
    const image=ctx.getImageData(0,0,c.width,c.height),p=image.data;
    for(let y=0;y<c.height;y+=3)for(let x=0;x<c.width;x+=3){const i=(y*c.width+x)*4;if(p[i+3]&&p[i+1]>170&&p[i+2]>170){p[i]=Math.min(255,p[i]+12);p[i+1]=Math.min(255,p[i+1]+12);p[i+2]=Math.min(255,p[i+2]+12);}}
    ctx.putImageData(image,0,0);if(cache.size>=256)cache.delete(cache.keys().next().value);cache.set(key,c);return c;
  }
  function drawObject(ctx,family,id,index,x,y,width){const image=frame(family,id,index);if(!image)return false;const meta=metadata(family,id),height=width*image.height/image.width;ctx.save();ctx.imageSmoothingEnabled=false;ctx.drawImage(image,Math.round(x-meta.anchor[0]/image.width*width),Math.round(y-meta.anchor[1]/image.height*height),Math.round(width),Math.round(height));ctx.restore();return true;}
  function drawCoral(ctx,id,x,y,size,time,health,state=null){const image=coral(id,health<=0?'dead':state||coralState(health),time*.8);if(!image)return false;const meta=metadata('corals',id),width=Math.max(10,Math.round(50*size));ctx.save();ctx.imageSmoothingEnabled=false;ctx.drawImage(image,Math.round(x-width/2),Math.round(y-meta.anchor[1]/image.height*width),width,width);ctx.restore();return true;}
  return {ready,frame,metadata,coral,coralState,drawCoral,drawObject,errors,get loaded(){return items.size;},records};
})();
