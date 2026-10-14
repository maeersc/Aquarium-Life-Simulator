"use strict";
AL.HabitatDrawing={
  rack(ctx,r,width=480,height=240){const x=Math.round(r.x*width),y=Math.round(r.y*height),w=Math.round(r.width);ctx.save();ctx.imageSmoothingEnabled=false;ctx.fillStyle='#162a35';ctx.fillRect(x-w/2,y,w,4);ctx.fillStyle='#66899b';ctx.fillRect(x-w/2,y-2,w,2);for(let i=0;i<5;i++){ctx.fillStyle='#a2bac1';ctx.fillRect(Math.round(x-w*.42+i*w*.21),y,2,10);}ctx.fillStyle='#8ebcc8';ctx.fillRect(x-w/2,y-13,3,13);ctx.fillRect(x+w/2-3,y-13,3,13);ctx.strokeStyle='#4e707b';ctx.strokeRect(x-w/2-4,y-17,11,8);ctx.strokeRect(x+w/2-7,y-17,11,8);ctx.restore();}
};
