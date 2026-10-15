"use strict";
AL.ExpansionArt=(()=>{
 const items=new Map(),cache=new Map(),errors=[],records=[...(AL.ExpansionSpriteData||[]),...(AL.Update29SpriteData||[])];
 const ready=Promise.all(records.map(meta=>new Promise(resolve=>{const im=new Image();im.onload=()=>{items.set(meta.id,{meta,im});resolve();};im.onerror=()=>{errors.push(meta.id);resolve();};im.src=meta.src;})));
 const stages={egg:0,baby:2,larva:2,juvenile:4,adult:6,frag:0,colony:4};
 function frame(id,stage='adult',state='alive'){const item=items.get(id);if(!item)return null;let i=item.meta.batch==='v2.9'&&stage==='colony'?6:stages[stage]??6;if(item.meta.category==='coral'&&item.meta.batch!=='v2.9'){i=state==='dead'?(stage==='frag'?1:7):state==='bleached'?5:state==='tissue-loss'?6:state==='stressed'?3:stage==='frag'?0:stage==='growing'?2:4;}else if(state==='dead')i++;const key=id+':'+i;if(cache.has(key))return cache.get(key);const c=document.createElement('canvas');c.width=192;c.height=160;const g=c.getContext('2d');g.imageSmoothingEnabled=false;const left=item.meta.nativeFacings?.[i]===-1;if(left){g.translate(192,0);g.scale(-1,1);}g.drawImage(item.im,i*192,0,192,160,0,0,192,160);const eye=item.meta.eyes?.[i];c.artMeta={speciesId:id,stage,state,frame:i,frameCount:1,nativeFacing:1,eye:eye?{...eye,x:left?192-eye.x:eye.x}:null,facingBehavior:'mirror-side-profile',authoredDeath:state==='dead',layer:'livestock',anchor:[96,80]};cache.set(key,c);return c;}
 function forFish(f){return frame(f.species,f.growth<.3?'baby':f.growth<1?'juvenile':'adult',f.dead?'dead':'alive');}
 function thumb(id){return frame(id,'adult')?.toDataURL()||'';}
 function plant(g,id,x,y,size,hp=1,state){const im=frame(id,size<1.2?'frag':'colony',hp<=0?'dead':state||'alive');if(!im)return;const w=50*size,h=w*160/192;g.drawImage(im,Math.round(x-w/2),Math.round(y-h+4),Math.round(w),Math.round(h));}
 return {metadata:id=>items.get(id)?.meta,ready,frame,forFish,thumb,plant,errors,records,has:id=>items.has(id),get loaded(){return items.size;}};
})();
