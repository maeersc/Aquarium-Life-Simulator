"use strict";
AL.DivingArt=(()=>{
 const images=new Map(),errors=[];
 const ready=Promise.all((AL.DivingArtData||[]).map(r=>new Promise(resolve=>{const image=new Image();image.onload=()=>{images.set(r.id,image);resolve();};image.onerror=()=>{errors.push(r.id);resolve();};image.src=r.src;})));
 function icon(ctx,index,x,y,w,h=w){const im=images.get('equipment');if(!im)return;const side=Math.min(w,h);ctx.imageSmoothingEnabled=false;ctx.drawImage(im,(index%4)*im.width/4,Math.floor(index/4)*im.height/2,im.width/4,im.height/2,x+(w-side)/2,y+(h-side)/2,side,side);}
 return {ready,errors,icon,image:id=>images.get(id),get loaded(){return images.size;}};
})();
