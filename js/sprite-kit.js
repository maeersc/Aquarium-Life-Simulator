"use strict";
/* Shared head-local detail, final-size rasterization, and transform boundary. */
AL.SpriteKit = (()=>{
  const rasters=new WeakMap(),ids=new WeakMap(),bounded=AL.Performance?new AL.Performance.PixelCache(32*1024*1024,8192):null;let serial=0;
  function facing(previous,dx,threshold=.00025){return Math.abs(dx)>threshold?(dx<0?-1:1):(previous===-1?-1:1);}
  function raster(source,width,height){
    width=Math.max(1,Math.round(width));height=Math.max(1,Math.round(height));
    if(!ids.has(source))ids.set(source,++serial);const identity=source.cacheKey||ids.get(source),boundedKey=identity+':'+width+':'+height,cached=bounded?.get(boundedKey);if(cached)return cached;
    let cache=rasters.get(source);if(!cache){cache=new Map();rasters.set(source,cache);}
    const key=width+':'+height;if(cache.has(key))return cache.get(key);
    const c=document.createElement('canvas');c.width=width;c.height=height;
    const g=c.getContext('2d');g.imageSmoothingEnabled=false;g.drawImage(source,0,0,width,height);
    const eye=source.artMeta?.eye;
    if(eye){
      // Sample the artist's eye as a local sprite component. It is rasterized
      // once at the final scene size, then mirrors/scales with the whole animal.
      const ew=Math.max(3,Math.round(eye.w*width/source.width)),eh=Math.max(3,Math.round(eye.h*height/source.height));
      const ex=Math.round(eye.x*width/source.width),ey=Math.round(eye.y*height/source.height);
      const x=AL.Core.clamp(ex-Math.floor(ew/2),0,Math.max(0,width-ew)),y=AL.Core.clamp(ey-Math.floor(eh/2),0,Math.max(0,height-eh));
      g.clearRect(x,y,ew,eh);g.drawImage(source,Math.round(eye.x-eye.w/2),Math.round(eye.y-eye.h/2),eye.w,eye.h,x,y,ew,eh);
      c.eyeBounds={x,y,w:ew,h:eh};
    }
    if(cache.size>=32)cache.delete(cache.keys().next().value);
    c.cacheKey='raster:'+boundedKey;if(bounded)return bounded.set(boundedKey,c);cache.set(key,c);return c;
  }
  function draw(ctx,source,x,y,width,height,direction=1,dead=false){
    const separateLeft=direction===-1&&source.leftSprite,flip=direction===-1&&!separateLeft;
    const image=raster(separateLeft||source,width,height);ctx.save();ctx.imageSmoothingEnabled=false;
    ctx.translate(Math.round(x),Math.round(y));ctx.scale(flip?-1:1,dead?-1:1);
    ctx.drawImage(image,flip?-Math.ceil(image.width/2):-Math.floor(image.width/2),dead?-Math.ceil(image.height/2):-Math.floor(image.height/2));ctx.restore();return image;
  }
  return {facing,raster,draw,get metrics(){return bounded?.metrics||null;}};
})();
