"use strict";
(async()=>{
  await AL.Art.ready;
  const ctx=document.getElementById('sheet').getContext('2d');ctx.imageSmoothingEnabled=false;
  ctx.fillStyle='#142c36';ctx.fillRect(0,0,1100,720);ctx.fillStyle='#eef5fa';ctx.font='16px Arial';
  const samples=[];
  for(const [row,width]of [16,20,24,32,44,59].entries()){
    const height=Math.round(width*40/64);ctx.fillText(width+' x '+height+' scene pixels',12,45+row*105);
    for(let frame=0;frame<4;frame++)for(const [index,facing]of [1,-1].entries()){
      const src=AL.Art.sprite('clown',frame,1),c=document.createElement('canvas');c.width=width;c.height=height;
      const g=c.getContext('2d');g.imageSmoothingEnabled=false;const raster=AL.SpriteKit.draw(g,src,Math.floor(width/2),Math.floor(height/2),width,height,facing);
      const data=g.getImageData(0,0,width,height).data;
      // Approximate baked-eye ROI, diagnostic only; this is not an anatomy proof.
      const {x:x0,y:y0,w:ew,h:eh}=raster.eyeBounds,x1=x0+ew,y1=y0+eh;
      let dark=0;
      for(let y=y0;y<y1;y++)for(let x=x0;x<x1;x++){const px=facing===1?x:width-1-x,i=(y*width+px)*4;if(data[i+3]&&data[i]<55&&data[i+1]<55&&data[i+2]<90)dark++;}
      samples.push({width,height,frame,facing,eyeRegionDarkPixels:dark});
      const x=220+frame*210+index*90,y=25+row*105;ctx.drawImage(c,x,y,width*2,height*2);ctx.fillStyle='#eef5fa';ctx.fillText('F'+frame+' '+(facing>0?'R':'L'),x,y+height*2+20);
    }
  }
  window.SPRITE_AUDIT={ready:true,samples};document.getElementById('report').textContent=JSON.stringify(samples,null,2);
})();
