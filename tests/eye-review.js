"use strict";
(async()=>{
  await Promise.all([AL.Art.ready,AL.AssetBank.ready]);
  const subjects=[...Object.keys(AL.Data.species),...AL.AssetBank.records.filter(r=>r.family==='fish').map(r=>r.id)],c=document.getElementById('contact');c.width=1280;c.height=subjects.length*126;
  const ctx=c.getContext('2d');ctx.fillStyle='#102633';ctx.fillRect(0,0,c.width,c.height);
  for(const [row,id]of subjects.entries()){
    ctx.fillStyle='#eef4fb';ctx.font='13px Arial';ctx.fillText(id,8,row*126+20);
    for(let frame=0;frame<4;frame++)for(const [i,facing]of [1,-1].entries()){
      const src=AL.Data.species[id]?AL.Art.sprite(id,frame,1):AL.AssetBank.frame('fish',id,frame),w=118,h=Math.round(w*src.height/src.width),x=200+frame*276+i*130,y=row*126+57;
      const image=AL.SpriteKit.draw(ctx,src,x,y,w,h,facing),e=image.eyeBounds;
      ctx.strokeStyle='#f4b860';ctx.strokeRect(x-Math.floor(w/2)+(facing===1?e.x:w-e.x-e.w),y-Math.floor(h/2)+e.y,e.w,e.h);
      ctx.fillStyle='#b9c9d9';ctx.fillText('F'+frame+(facing>0?' R':' L'),x-20,row*126+112);
    }
  }
  window.EYE_REVIEW_READY=true;
})();
