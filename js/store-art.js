"use strict";
// Local canvas object previews for the existing equipment and consumables.
AL.StoreArt={draw(g,p){
  const r=(x,y,w,h,c)=>{g.fillStyle=c;g.fillRect(x,y,w,h);},poly=AL.Art.poly,type=p.args.type;
  if(type?.startsWith('frag-')){
    const steel='#b8d6e6',edge='#62869d',grip='#45d6d0',dark='#183143';
    const cutters=(ox=0,oy=0)=>{poly(g,[[83+ox,62+oy],[61+ox,104+oy],[49+ox,108+oy],[49+ox,98+oy],[75+ox,58+oy]],grip);poly(g,[[93+ox,61+oy],[120+ox,98+oy],[120+ox,109+oy],[108+ox,108+oy],[83+ox,67+oy]],'#f3ad64');poly(g,[[78+ox,61+oy],[60+ox,26+oy],[65+ox,17+oy],[88+ox,51+oy],[110+ox,17+oy],[114+ox,28+oy],[94+ox,64+oy]],edge);poly(g,[[65+ox,25+oy],[69+ox,24+oy],[87+ox,49+oy],[85+ox,55+oy]],steel);poly(g,[[106+ox,24+oy],[111+ox,26+oy],[92+ox,57+oy],[89+ox,51+oy]],steel);r(81+ox,56+oy,13,13,dark);r(85+ox,60+oy,5,5,steel);};
    if(type==='frag-cutters'){cutters();return;}
    if(type==='frag-kit'){r(18,13,156,104,dark);r(22,17,148,96,edge);r(26,21,140,88,'#243b50');g.save();g.translate(-14,4);g.scale(.8,.8);cutters();g.restore();r(116,34,7,61,steel);poly(g,[[116,34],[116,23],[132,23],[122,34]],steel);r(139,25,5,67,grip);r(134,22,15,6,steel);for(let i=0;i<2;i++){r(114+i*24,100,15,5,'#d6c9ae');r(120+i*24,105,4,7,'#ac9d7e');}return;}
    if(type==='frag-saw'){r(44,104,106,9,edge);r(49,95,96,9,steel);r(44,27,17,69,dark);r(49,23,12,12,grip);r(55,21,83,10,edge);r(129,29,9,59,steel);for(let i=0;i<10;i++)r(126,38+i*5,3,3,'#eef8ff');r(65,82,70,9,edge);r(68,75,65,7,steel);r(61,43,27,31,'#334f66');r(65,48,19,19,grip);return;}
    if(type==='frag-plugs'){for(let i=0;i<3;i++){const x=34+i*49,y=35+(i%2)*20;r(x+12,y+13,12,40,'#9c8f75');r(x+15,y+17,4,30,'#d6c9ae');poly(g,[[x,y+6],[x+10,y],[x+30,y],[x+40,y+7],[x+40,y+17],[x+30,y+23],[x+10,y+23],[x,y+17]],'#d6c9ae');r(x+9,y+7,24,7,'#f1e7d0');}return;}
    if(type==='frag-mounting'){r(40,39,37,65,steel);r(46,29,25,13,grip);r(53,11,10,20,'#e1edf5');r(45,59,27,23,'#517fa4');r(95,51,55,50,'#f1e7d0');r(100,56,45,36,'#b5a78b');r(106,63,32,5,'#f1e7d0');r(106,76,23,5,'#f1e7d0');return;}
  }
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
