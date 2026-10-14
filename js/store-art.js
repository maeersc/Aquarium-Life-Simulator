"use strict";
// Local canvas object previews for the existing equipment and consumables.
AL.StoreArt={draw(g,p){
  const r=(x,y,w,h,c)=>{g.fillStyle=c;g.fillRect(x,y,w,h);},poly=AL.Art.poly,type=p.args.type;
  if(p.kind==='medicine'){const colors={diagnostic:'#91b5d3',copper:'#be996b',ciliate:'#8cbba5',fluke:'#98b3d3',antibacterial:'#d3a2b7',support:'#b5c88b',coralDip:'#c7a2d9',coralSupport:'#7ec7bf',mystery:'#e39172',experimental:'#a594dc'},id=p.args.product;r(68,30,56,81,'#253449');r(77,20,38,17,'#536B83');r(74,55,44,44,colors[id]||'#91b5d3');r(88,62,15,5,'#F3F7FC');r(93,57,5,16,'#F3F7FC');if(id==='diagnostic'){r(135,44,13,65,'#91b5d3');r(137,43,9,8,'#F3F7FC');}if(AL.Health.products[id]?.restricted){r(80,85,30,4,'#EF7075');r(94,79,4,15,'#EF7075');}return;}
  if(p.kind==='decor'){
    if(type==='cave'){AL.AssetBank.drawObject(g,'rocks','fiji',3,96,118,124);return;}
    if(type==='wood'){poly(g,[[34,114],[79,24],[89,18],[89,64],[155,39],[106,80],[83,115]],'#746049');poly(g,[[69,110],[84,63],[130,53],[92,82],[80,110]],'#a08a69');return;}
    r(93,29,6,91,'#355653');r(67,42,58,46,'#c3a371');r(73,48,46,33,'#f2d091');r(81,52,8,23,'#fff0c4');r(62,35,68,7,'#41504f');r(62,88,68,7,'#41504f');return;
  }
  if(p.kind==='equipment'){
    if(type==='heater'){r(87,8,18,107,'#6c8b9c');r(91,12,10,91,'#ccd2bd');r(86,6,20,19,'#233f50');for(let i=0;i<9;i++)r(92,55+i*5,8,2,'#ac7448');r(78,34,8,8,'#293946');r(78,83,8,8,'#293946');return;}
    if(type.toLowerCase().includes('light')){r(17,36,158,21,'#6c8b9c');r(23,42,146,9,'#233f50');for(let i=0;i<12;i++)r(28+i*12,55,5,5,'#d5f6ff');r(22,58,5,48,'#293946');r(165,58,5,48,'#293946');return;}
    if(type==='air'||type==='flow'){r(52,31,74,65,'#6c8b9c');r(56,35,66,54,'#233f50');for(let i=0;i<5;i++)r(64,44+i*8,48,3,'#85aebe');r(122,62,21,8,'#293946');r(137,68,6,37,'#6c8b9c');for(let i=0;i<4;i++)r(143+i*6,100-i*15,3,3,'#d5f6ff');return;}
    if(type==='dosing'){for(let i=0;i<3;i++){r(31+i*47,33,34,76,'#91b5d3');r(38+i*47,24,20,11,'#233f50');r(34+i*47,64,28,30,['#adbd88','#d3b996','#9c9fc9'][i]);}r(43,15,99,5,'#6c8b9c');return;}
    r(56,19,80,74,'#6c8b9c');r(62,25,68,61,'#233f50');for(let i=0;i<7;i++)r(66,31+i*7,60,3,'#85aebe');r(91,93,11,29,'#293946');r(48,26,8,24,'#6c8b9c');if(type==='feeder'){r(66,10,60,24,'#b5c88b');r(90,103,14,8,'#c3a371');}if(type==='containment'){r(49,15,7,83,'#adbd88');r(136,15,7,83,'#adbd88');}return;
  }
  // Food tubs and treatment bottles have distinct silhouettes.
  const food=p.kind==='food';r(food?52:64,food?26:38,food?88:64,food?87:75,'#233f50');r(food?49:72,food?17:21,food?94:48,food?12:20,'#6c8b9c');r(food?59:70,55,food?74:52,42,food?'#b5c88b':'#91b5d3');r(78,63,36,3,'#dce8dd');if(food){for(let i=0;i<9;i++)r(72+(i*13)%44,74+(i*7)%17,3,2,'#746049');}else{r(91,73,10,19,'#dce8dd');r(86,78,20,9,'#dce8dd');}
}};
