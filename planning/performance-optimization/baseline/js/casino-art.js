"use strict";
// Original code-native pixel art; approved existing livestock art is used on cards.
AL.CasinoArt=(()=>{
 function icon(){return '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" shape-rendering="crispEdges"><g fill="currentColor"><path d="M10 1h4v5h-4zM10 18h4v5h-4zM1 10h5v4H1zM18 10h5v4h-5zM3 3h4v4H3zM17 3h4v4h-4zM3 17h4v4H3zM17 17h4v4h-4z"/><path fill-rule="evenodd" d="M6 4h12v2h2v12h-2v2H6v-2H4V6h2zm2 4v8h8V8z"/><path d="M10 8h4v8h-4zM8 10h8v4H8z"/></g></svg>';}
 function draw(ctx,kind,value=0){ctx.save();ctx.clearRect(0,0,ctx.canvas.width,ctx.canvas.height);ctx.imageSmoothingEnabled=false;ctx.scale(ctx.canvas.width/96,ctx.canvas.height/64);const r=(x,y,w,h,c)=>{ctx.fillStyle=c;ctx.fillRect(x,y,w,h);},p=(points,c)=>AL.Art.poly(ctx,points,c),navy='#142638',teal='#45d6d0',gold='#f4bf56',white='#e1edf5';
  if(kind==='symbol'){const color=['#479bda','#f58b46','#ae8bde',gold][value%4];p([[20,27],[7,17],[7,46],[22,36]],color);p([[18,21],[28,14],[64,14],[79,24],[83,32],[76,43],[29,48],[18,40]],color);p([[30,15],[41,5],[56,15]],'#2f526e');p([[34,46],[48,56],[57,44]],'#2f526e');r(29,19,6,26,value%4===1?white:'#ffffff30');r(49,18,5,28,value%4===1?white:'#ffffff20');r(68,23,7,7,navy);r(69,23,3,3,white);r(79,34,5,2,navy);if(value%4===3){r(40,2,2,7,white);r(37,5,8,2,white);r(83,10,2,7,gold);r(80,13,8,2,gold);}}
  else if(kind==='back'){r(4,3,88,58,navy);for(let x=9;x<88;x+=8)for(let y=8;y<58;y+=8)r(x,y,3,3,'#29475d');r(43,14,10,9,gold);r(46,24,4,25,gold);r(32,44,32,4,gold);p([[27,37],[37,48],[48,52],[59,48],[69,37],[65,52],[48,59],[31,52]],teal);}
  else if(kind==='dealer'){r(33,7,31,9,navy);r(27,16,43,7,white);r(31,23,35,7,'#487a9c');r(35,30,27,19,'#d5ad88');r(39,35,4,4,navy);r(54,35,4,4,navy);r(45,44,9,2,navy);p([[20,64],[25,51],[39,48],[49,57],[60,48],[72,54],[77,64]],navy);r(47,53,4,11,teal);r(43,17,9,5,gold);}
  else if(kind==='title'){r(0,0,96,64,navy);for(let y=40;y<64;y+=7)for(let x=(y%2)*4;x<96;x+=17)r(x,y,10,2,'#2d6981');r(72,8,10,10,gold);r(41,4,3,35,white);p([[45,8],[69,32],[45,32]],teal);p([[39,14],[22,32],[39,32]],'#4f9dd0');p([[17,36],[77,36],[67,45],[28,45]],'#9d7249');r(28,38,40,3,gold);r(7,19,2,13,'#58788a');r(3,24,10,2,'#58788a');}
  else if(kind==='effect'){for(let i=0;i<12;i++){r(4+(i*17)%88,3+(i*13)%53,3,3,value?gold:teal);}r(37,17,22,30,value?gold:teal);r(41,20,14,24,navy);r(47,24,3,16,white);r(43,28,10,3,white);}
  ctx.restore();
 }
 return {icon,draw};
})();
