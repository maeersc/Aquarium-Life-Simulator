"use strict";
AL.Art = (()=>{
  const cache=new Map(),shadeCache=new Map(),plantCache=new Map();
  function shade(hex,m){const key=hex+':'+Math.round(m*1000);if(shadeCache.has(key))return shadeCache.get(key);const n=parseInt(hex.slice(1),16),color='#'+[n>>16,(n>>8)&255,n&255].map(v=>Math.max(0,Math.min(255,Math.round(v*m))).toString(16).padStart(2,'0')).join('');if(shadeCache.size>2048)shadeCache.clear();shadeCache.set(key,color);return color;}
  // Scanline spans retain hard pixel boundaries without thousands of per-pixel draw calls.
  function poly(ctx,points,color){ctx.fillStyle=color;const minY=Math.floor(Math.min(...points.map(p=>p[1]))),maxY=Math.ceil(Math.max(...points.map(p=>p[1])));for(let y=minY;y<=maxY;y++){const intersections=[];for(let i=0,j=points.length-1;i<points.length;j=i++){const [xi,yi]=points[i],[xj,yj]=points[j];if((yi>y+.5)!==(yj>y+.5))intersections.push((xj-xi)*(y+.5-yi)/(yj-yi)+xi);}intersections.sort((a,b)=>a-b);for(let n=0;n+1<intersections.length;n+=2){const start=Math.ceil(intersections[n]-.5),end=Math.ceil(intersections[n+1]-.5);if(end>start)ctx.fillRect(start,y,end-start,1);}}}
  function legacySprite(species,frame=0,tone=1){tone=Math.round(tone*10)/10;const key=species+':'+frame+':'+tone;if(cache.has(key))return cache.get(key);const d=AL.Data.species[species],c=document.createElement('canvas');c.width=64;c.height=40;const ctx=c.getContext('2d');ctx.imageSmoothingEnabled=false;
    const shift=[-2,0,2,0][frame%4],shape=d.shape;let ry=['angel','tang'].includes(shape)?11:shape==='eel'?4:shape==='slim'?5:7,rx=shape==='eel'?24:shape==='tang'?15:17;const cx=35,cy=20;
    const tail=shape==='guppy'?[[19,18],[3,7+shift],[5,31+shift],[20,23]]:shape==='betta'?[[23,15],[8,6+shift],[3,13+shift],[6,21],[3,29+shift],[10,35],[24,25]]:[[21,18],[7,11+shift],[11,20],[7,29+shift],[21,23]];
    poly(ctx,tail,shade(d.color,.65));poly(ctx,tail.map(([x,y])=>[x+2,y*.85+3]),d.secondary);
    for(let i=0;i<5;i++)poly(ctx,[[18,20],[8,12+i*4+shift],[10,13+i*4+shift]],shade(d.color,1+i*.035));
    const dorsal=shape==='angel'?[[25,15],[34,1],[40,14]]:shape==='dart'?[[33,15],[31,2],[35,2],[38,15]]:shape==='cardinal'?[[24,14],[29,2],[32,11],[43,4],[45,16]]:shape==='slim'?[[28,16],[32,10],[37,15]]:shape==='guppy'?[[28,15],[32,9],[38,14]]:[[23,15],[28,8],[38,9],[45,16]];
    poly(ctx,dorsal,shade(d.color,.7));poly(ctx,dorsal.map(([x,y])=>[x,y+2]),d.secondary);
    poly(ctx,shape==='angel'?[[26,24],[33,39],[39,24]]:[[26,24],[31,32+shift],[41,25]],shade(d.color,.75));
    for(let y=cy-ry;y<=cy+ry;y++)for(let x=cx-rx;x<=cx+rx;x++){const nx=(x-cx)/rx,ny=(y-cy)/ry;if(nx*nx+ny*ny>1||x<13)continue;let color=d.color;const band=(x+y*0.2)%9;
      if(d.pattern==='neon'){color=y<19?d.color:y>21&&x<38?d.secondary:'#b6c1b7';if(y===18||y===19)color='#9af2ed';}
      if(d.pattern==='cardinal'){color=y>21?d.secondary:d.color;if(y===18||y===19)color='#a2f2ee';}
      if(d.pattern==='clown'){if((x>22&&x<27)||(x>35&&x<40)||(x>46&&x<50))color=d.secondary;if([22,27,35,40,46,50].includes(x))color='#4c4032';}
      if(d.pattern==='half'&&x<32)color=d.secondary;
      if(d.pattern==='bars'&&Math.floor(x/5)%2===0)color=d.secondary;
      if(d.pattern==='stripes'&&y%4<2)color=d.secondary;
      if(d.pattern==='spots'&&(x*13+y*7)%23<3)color=d.secondary;
      if(d.pattern==='wedge'&&x<34&&x>22&&Math.abs(y-20)<(34-x)*.5)color=d.secondary;
      if(d.pattern==='fire'&&x<33)color=d.secondary;
      if(d.pattern==='tailspot'&&Math.hypot(x-22,y-20)<3)color='#33485a';
      if(d.pattern==='glow'&&((x+y)%8===0||Math.abs(ny)>.75))color=d.secondary;
      const edge=nx*nx+ny*ny>.82;let brightness=edge?.65:ny<-.35?1.17:ny>.45?.75:1;if(!edge&&band<1&&y%2===0)brightness*=1.1;
      ctx.fillStyle=shade(color,brightness*tone);ctx.fillRect(x,y,1,1);
    }
    poly(ctx,[[35,21],[31,25+shift],[39,24]],shade(d.secondary,.75));
    ctx.fillStyle='#152d36';ctx.fillRect(44,18,1,7);ctx.fillStyle=shade(d.color,1.3);ctx.fillRect(45,18,1,6);
    const eyeX=shape==='eel'?54:47;ctx.fillStyle='#eddfb1';ctx.fillRect(eyeX,16,4,4);ctx.fillStyle='#0b2029';ctx.fillRect(eyeX+2,17,2,3);ctx.fillStyle='#fff9dc';ctx.fillRect(eyeX+2,17,1,1);
    ctx.fillStyle='#18323a';ctx.fillRect(cx+rx-2,22,3,1);if(shape==='bottom'){ctx.fillStyle=d.secondary;ctx.fillRect(49,26,5,1);ctx.fillRect(52,24,1,4);}
    c.artMeta={speciesId:species,frame,frameWidth:64,frameHeight:40,frameCount:4,frameDurationMs:1000/6,eye:{x:eyeX+2,y:18,w:4,h:4},nativeFacing:1,anchor:[32,20],facingBehavior:'mirror-side-profile',layer:'livestock'};
    cache.set(key,c);return c;
  }
  const assigned=AL.LivestockArt?.clown,assignedCache=new Map();let assignedImage=null;
  const ready=new Promise(resolve=>{
    if(!assigned){resolve(false);return;}
    const image=new Image();
    image.onload=()=>{assignedImage=image;resolve(true);};
    image.onerror=()=>resolve(false);
    image.src=assigned.src;
  });
  function sprite(species,frame=0,tone=1){
    if(species!=='clown'||!assignedImage)return legacySprite(species,frame,tone);
    frame=((Math.floor(frame)%4)+4)%4;tone=Math.round(AL.Core.clamp(tone,.6,1.4)*10)/10;
    const key=frame+':'+tone;if(assignedCache.has(key))return assignedCache.get(key);
    const c=document.createElement('canvas');c.width=128;c.height=80;
    const ctx=c.getContext('2d');ctx.imageSmoothingEnabled=false;
    const eye=assigned.eyes?.[frame]||[104,60],scale=92/112;
    // Register every frame to the head, rather than the changing tail outline.
    const eyeX=97,eyeY=37;
    ctx.filter=`brightness(${tone})`;
    ctx.drawImage(assignedImage,frame*assigned.frameSize,0,assigned.frameSize,assigned.frameSize,eyeX-eye[0]*scale,eyeY-eye[1]*scale,assigned.frameSize*scale,assigned.frameSize*scale);
    if(frame!==0){const reference=sprite('clown',0,tone);ctx.filter='none';ctx.drawImage(reference,92,32,10,10,92,32,10,10);}
    c.artMeta={speciesId:'clown',frame,frameWidth:128,frameHeight:80,frameCount:4,frameDurationMs:1000/6,eye:{x:eyeX,y:eyeY,w:10,h:10},nativeFacing:1,anchor:[64,40],facingBehavior:'mirror-side-profile',layer:'livestock'};
    assignedCache.set(key,c);return c;
  }
  function thumb(species,variety=null){if(AL.ExpansionArt?.has(species))return AL.ExpansionArt.thumb(species);return (species==='clown'&&!variety?sprite(species):(AL.ClownArt?.frame(species,variety)||AL.LifeStages?.frame(species,'adult','alive')||sprite(species))).toDataURL();}
  function plant(ctx,type,x,y,size,time,seed=1,health=1,state=null){if(AL.ExpansionArt?.has(type)){AL.ExpansionArt.plant(ctx,type,x,y,size,health,state);return;}
    if(AL.Data.flora[type]?.water==='marine'&&AL.AssetBank?.drawCoral(ctx,type,x,y,size,time,health,state))return;
    const quantized=Math.round(size*10)/10,phase=Math.floor(time*3)%8,key=[type,quantized,phase,seed%5,health<.2].join(':');let tile=plantCache.get(key);
    if(!tile){const canvas=document.createElement('canvas');canvas.width=Math.ceil(100*quantized+20);canvas.height=Math.ceil(85*quantized+20);const originX=Math.floor(canvas.width/2),originY=canvas.height-5;paintPlant(canvas.getContext('2d'),type,originX,originY,quantized,phase*Math.PI/4,seed%5,health);tile={canvas,x:originX,y:originY};if(plantCache.size>=192)plantCache.delete(plantCache.keys().next().value);plantCache.set(key,tile);}
    ctx.drawImage(tile.canvas,Math.round(x-tile.x),Math.round(y-tile.y));
  }
  function paintPlant(ctx,type,x,y,size,time,seed=1,health=1){const d=AL.Data.flora[type];if(!d)return;const color=health<.2?'#746b52':d.color,h=Math.round(({grass:72,sword:61,fern:53,leaf:38,branch:43,soft:37}[d.shape]||30)*size),sway=Math.sin(time*0.8+seed)*2;ctx.save();ctx.translate(Math.round(x),Math.round(y));
    if(['fern','sword','grass','leaf'].includes(d.shape)){for(let stem=0;stem<7;stem++){const side=(stem-3)/3,height=h*(.55+((stem*7+seed)%9)/18),tipX=side*height*.4+sway;for(let k=0;k<height;k+=2){const px=Math.round(tipX*k/height+Math.sin(k/height*3)*side*4);ctx.fillStyle=shade(color,.65+stem*.065);ctx.fillRect(px,-k,2,3);if(d.shape==='fern'&&k%6===0){poly(ctx,[[px,-k],[px-8*(1-k/height),-k-4],[px,-k+2]],shade(color,.85));poly(ctx,[[px+1,-k],[px+9*(1-k/height),-k-3],[px+1,-k+3]],shade(color,1.2));}else if(d.shape!=='grass'){const width=(d.shape==='leaf'?7:4)*Math.sin(k/height*Math.PI);ctx.fillRect(Math.round(px-width),-k,Math.round(width*2+1),2);ctx.fillStyle=shade(color,1.25);ctx.fillRect(px,-k,1,2);}}}}
    else if(d.shape==='moss'){for(let i=0;i<65;i++){const px=Math.sin(i*13.7)*20*size,py=-Math.abs(Math.cos(i*3.7))*13*size;ctx.fillStyle=shade(color,.65+(i%5)*.12);ctx.fillRect(Math.round(px),Math.round(py),3,3);}}
    else if(d.shape==='branch'){const branch=(bx,by,len,angle,depth)=>{const tx=bx+Math.sin(angle)*len,ty=by-Math.cos(angle)*len;const steps=Math.ceil(len);for(let j=0;j<steps;j++){ctx.fillStyle=shade(color,.65+depth*.17);ctx.fillRect(Math.round(bx+(tx-bx)*j/steps),Math.round(by+(ty-by)*j/steps),depth+1,depth+1);}if(depth>0){branch(tx,ty,len*.66,angle-.55,depth-1);branch(tx,ty,len*.65,angle+.5,depth-1);}else{ctx.fillStyle=shade(color,1.3);ctx.fillRect(Math.round(tx),Math.round(ty),2,3);}};branch(0,0,h*.65,0,3);}
    else{const count=d.shape==='zoa'?12:d.shape==='mushroom'?5:14;for(let i=0;i<count;i++){const px=Math.sin(i*12.78)*20*size,py=-Math.abs(Math.cos(i*4.14))*h*.55,r=d.shape==='mushroom'?7:3;ctx.fillStyle=shade(color,.6);ctx.fillRect(Math.round(px),Math.round(py),2,Math.round(-py));const wave=Math.sin(time+i)*1.2;for(let k=0;k<8;k++){const angle=k*Math.PI/4;ctx.fillStyle=shade(color,.9+k*.035);ctx.fillRect(Math.round(px+Math.cos(angle)*(r+wave)),Math.round(py+Math.sin(angle)*r),3,3);}ctx.fillStyle=d.shape==='zoa'?'#a7c88e':shade(color,1.25);ctx.fillRect(Math.round(px),Math.round(py),3,3);}}
    ctx.restore();
  }
  function plantBounds(type,size){const d=AL.Data.flora[type];if(d.water==='marine'&&AL.AssetBank?.metadata('corals',type))return {width:Math.max(24,50*size),height:48*size};const h=({grass:72,sword:61,fern:53,leaf:38,branch:43,soft:37}[d.shape]||30)*size;return {width:d.water==='marine'?Math.max(24,48*size):Math.max(28,h*.85+18),height:d.shape==='branch'?h*1.65:d.water==='marine'?h*.6+9:h+6};}
  return {sprite,legacySprite,thumb,plant,plantBounds,shade,poly,ready,get clownfishArtLoaded(){return !!assignedImage;}};
})();
AL.Renderer = class {
  constructor(canvas){this.canvas=canvas;this.ctx=canvas.getContext('2d',{alpha:false});this.scene=document.createElement('canvas');this.scene.width=480;this.scene.height=240;this.g=this.scene.getContext('2d',{alpha:false});this.time=0;this.zoom=1;this.pan=0.5;this.hitboxes=[];this.selected=null;this.fps=60;this.last=0;this.positions=new Map();}
  draw(s,dt){this.time+=dt;const t=AL.Core.selected(s),g=this.g,W=480,H=240,time=this.time;const marine=t.water==='marine',illumination=AL.Sim.light(s,t),lamp=AL.Core.clamp(illumination/1.2,0,1),hour=s.time/60%24,roomNight=hour<6||hour>=19,preview=s.vip.preview;this.hitboxes=[];
    const drawFlora=f=>{
      if(f.relocationRequired)return;
      const x=f.x*W,y=(f.y??0.92)*H,bounds=AL.Art.plantBounds(f.type,f.size);
      g.save();if(this.placement?.id===f.id)g.globalAlpha=.35;
      AL.Art.plant(g,f.type,x,y,f.size,time,Number(f.id.replace(/\D/g,'')),f.hp/100,AL.Health?.visualState(f));g.restore();
      if(this.selected===f.id){g.strokeStyle='#cce4ae';g.setLineDash([2,3]);g.strokeRect(Math.round(x-bounds.width/2-2),Math.round(y-bounds.height-2),Math.round(bounds.width+4),Math.round(bounds.height+5));g.setLineDash([]);}
      this.hitboxes.push({id:f.id,kind:'flora',x:((x-W*this.pan)*this.zoom+W/2)/W,y:((y-bounds.height/2-H/2)*this.zoom+H/2)/H,w:bounds.width*this.zoom/W,h:bounds.height*this.zoom/H});
    };
    this.pan=AL.Core.clamp(this.pan,.5/this.zoom,1-.5/this.zoom);
    const currentIds=new Set(t.fish.map(f=>f.id));for(const id of this.positions.keys())if(!currentIds.has(id))this.positions.delete(id);
    const dry=t.emptyDry===true&&!t.prepared;
    g.imageSmoothingEnabled=false;const bg=g.createLinearGradient(0,0,0,H);bg.addColorStop(0,dry?'#253449':marine?'#174957':'#1c4b4c');bg.addColorStop(.5,dry?'#253449':marine?'#123747':'#153b3e');bg.addColorStop(1,'#102a30');g.fillStyle=bg;g.fillRect(0,0,W,H);
    g.save();g.translate(W/2,H/2);g.scale(this.zoom,this.zoom);g.translate(-W*this.pan,-H/2);
    // Printed backdrop silhouettes provide depth; living vegetation is rendered separately.
    g.globalAlpha=.2;for(let i=0;i<(dry?0:16);i++){const x=(i*43+19)%500;AL.Art.plant(g,marine?'sps':'vallis',x,218,.9+(i%4)*.55,0,i,.8);}g.globalAlpha=1;
    for(let i=0;i<5;i++){const x=40+i*102+Math.sin(time*.05+i)*12;g.globalAlpha=.075*lamp;AL.Art.poly(g,[[x-15,0],[x+4,0],[x+65,210],[x-25,210]],marine?'#bfeaff':'#e4f4c2');}g.globalAlpha=1;
    const sandY=marine&&AL.Habitat?Math.round(AL.Habitat.bed(t)*H):214,sandColor=marine&&t.substrate?AL.Habitat.sandProducts[t.substrate.type].color:null;const sand=g.createLinearGradient(0,sandY-10,0,240);sand.addColorStop(0,sandColor||(marine?'#b2a58c':'#a39877'));sand.addColorStop(.2,'#8a826b');sand.addColorStop(1,'#4f594c');g.fillStyle=sand;g.fillRect(0,sandY,W,H-sandY);
    if(marine&&t.substrate?.depth===0){g.fillStyle='#243847';g.fillRect(0,sandY,W,H-sandY);g.fillStyle='#698695';g.fillRect(0,sandY,W,1);}else{
    g.save();g.translate(0,sandY-214);AL.Art.poly(g,[[0,210],[72,216],[156,210],[240,218],[319,210],[410,216],[480,207],[480,235],[0,235]],marine?(sandColor||'#a69d85'):'#a29977');
    for(let i=0;i<700;i++){const x=(i*131+17)%480,y=214+(i*43)%26;g.fillStyle=(marine&&t.substrate?.type==='hawaiian'?['#99978b','#555a60','#3b424b','#777a7c']:['#c5b996','#777863','#536356','#aaa07c'])[i%4];g.fillRect(x,y,i%3===0?2:1,1);}g.restore();
    }
    const rock=(x,y,w,h,group='fiji',variant=1)=>{if(marine&&AL.AssetBank?.drawObject(g,'rocks',group,variant,x,y,w))return;AL.Art.poly(g,[[x-w*.5,y],[x-w*.44,y-h*.6],[x-w*.18,y-h],[x+w*.22,y-h*.94],[x+w*.5,y-h*.4],[x+w*.53,y]],'#374b4a');AL.Art.poly(g,[[x-w*.44,y-h*.6],[x-w*.18,y-h],[x+w*.22,y-h*.94],[x+w*.03,y-h*.4],[x-w*.12,y-h*.12]],'#66766b');AL.Art.poly(g,[[x+w*.03,y-h*.4],[x+w*.22,y-h*.94],[x+w*.5,y-h*.4],[x+w*.53,y]],'#435e58');for(let i=0;i<15;i++){g.fillStyle=i%2?'#869080':'#263e3e';g.fillRect(Math.round(x-w*.22+(i*7)%Math.max(1,w*.55)),Math.round(y-h*.7+(i*13)%Math.max(1,h*.65)),3,1);}};
    if(!marine&&!dry){rock(89,217,77,58,'fiji',2);rock(52,219,48,36,'fiji',0);rock(391,217,97,76,'caribbean',3);rock(438,219,59,45,'hawaiian',1);rock(361,222,51,27,'hawaiian',0);}
    // Driftwood belongs to the visual starter hardscape, not a purchasable living entity.
    if(!marine&&!dry){AL.Art.poly(g,[[114,218],[136,203],[177,178],[218,164],[224,168],[180,188],[160,205],[143,220]],'#493f35');AL.Art.poly(g,[[139,210],[173,181],[185,142],[190,140],[186,177],[211,163],[217,165],[180,187]],'#6c6350');AL.Art.poly(g,[[128,216],[156,199],[177,189],[150,211]],'#93856a');}
    AL.Placement?.draw(this,t,false,drawFlora);
    if(!marine)for(const f of t.flora.filter(f=>f.x<.45))drawFlora(f);
    for(const e of t.equipment.filter(e=>e.enabled&&e.durability>0)){if(e.type==='filter'){g.fillStyle='#152f32';g.fillRect(458,17,13,38);g.fillStyle='#3a5756';g.fillRect(460,20,8,26);g.fillStyle='#163438';g.fillRect(463,55,3,45);for(let i=0;i<4;i++)g.fillRect(459,24+i*5,10,2);}if(e.type==='heater'){g.fillStyle='#547b75';g.fillRect(15,53,4,68);g.fillStyle='#b9b696';g.fillRect(16,58,1,53);g.fillStyle='#ac7448';g.fillRect(16,114,2,3);}}
    if(s.settings.particles){for(let i=0;i<23;i++){const y=220-((time*(4+i%3)+(i*29))%220),x=453+Math.sin(time*.7+i)*5;g.strokeStyle='#8ac4bd66';g.strokeRect(Math.round(x),Math.round(y),i%4?2:3,i%4?3:4);}for(let i=0;i<35;i++){g.fillStyle='#b8d4be22';g.fillRect(Math.round((i*73+time*.5)%480),Math.round((i*43+Math.sin(time*.1+i)*5)%220),1,1);}}
    for(const f of [...t.fish].sort((a,b)=>a.y-b.y)){
      const d=AL.Data.species[f.species],frame=f.dead?0:Math.floor(time*(f.behavior==='Rest'?3:6)*d.activity)%4;
      const keepApprovedClown=f.species==='clown'&&!f.variety&&!f.dead&&f.growth>=1;
      const stageSprite=AL.ExpansionArt?.forFish(f)|| (keepApprovedClown?null:(AL.ClownArt?.forFish(f,time)||AL.LifeStages?.forFish(f)));
      const baseSprite=stageSprite||AL.Art.sprite(f.species,frame,f.genes.color),sprite=AL.Patterns?.sprite(f,baseSprite)||baseSprite,scale=Math.max(.35,Math.min(1.7,.6+d.size/28)*Math.sqrt(f.growth)*f.genes.size);
      // Renderer interpolation never mutates simulation positions or its random seed.
      const pos=this.positions.get(f.id)||{x:f.x,y:f.y,facing:f.heading||1};const oldX=pos.x,blend=1-Math.exp(-dt*Math.max(.7,s.settings.speed*.7));pos.x+=(f.x-pos.x)*blend;pos.y+=(f.y-pos.y)*blend;if(!f.dead&&blend>0)pos.facing=AL.SpriteKit.facing(pos.facing,f.x-oldX);this.positions.set(f.id,pos);
      const w=Math.round(64*scale),h=stageSprite?Math.round(w*sprite.height/sprite.width):Math.round(40*scale),x=Math.round(pos.x*W),y=Math.round(pos.y*H);
      g.save();g.globalAlpha=f.dead?.65:f.behavior==='Hide'?.65:1;if(f.disease)g.globalAlpha=.75;AL.SpriteKit.draw(g,sprite,x,y,w,h,pos.facing,f.dead&&!stageSprite);g.restore();
      if(!f.dead&&f.reproduction?.pairId){g.fillStyle='#45d6d0';g.fillRect(Math.round(x-3),Math.round(y-h/2-7),2,2);g.fillRect(Math.round(x+1),Math.round(y-h/2-7),2,2);}
      if(!f.dead&&f.behavior==='Male mouthbrooding'){g.fillStyle='#e6cf94';g.fillRect(Math.round(x-2),Math.round(y-h/2-7),4,2);}
      if(this.selected===f.id){g.strokeStyle='#d0e6b7';g.setLineDash([2,3]);g.strokeRect(x-w/2-3,y-h/2-3,w+6,h+6);g.setLineDash([]);}if(f.stress>55&&!f.dead){g.fillStyle='#d7b979';g.fillRect(x,y-h/2-5,2,3);}if(!s.settings.reducedViolence&&f.dead){g.fillStyle='#bc6864';g.fillRect(x+3,y,2,1);}
      this.hitboxes.push({id:f.id,x:((x-W*this.pan)*this.zoom+W/2)/W,y:((y-H/2)*this.zoom+H/2)/H,w:w*this.zoom/W,h:h*this.zoom/H});
    }
    AL.ExpansionUI?.draw(this,t);AL.Update29UI?.drawNurseries(this,t);for(const p of t.food){g.fillStyle=p.type==='algae'?'#aac47d':'#d4b085';g.fillRect(Math.round(p.x*W),Math.round(p.y*H),2,2);}
    if(!marine)for(const f of t.flora.filter(f=>f.x>=.45))drawFlora(f);
    AL.Placement?.draw(this,t,true,drawFlora);
    for(let i=0;i<t.eggs.length;i++){
      const brood=t.eggs[i];if(marine&&AL.Placement&&AL.BroodView)continue;
      // Internal gestation and mouthbrooding do not leave external eggs on sand.
      if(['livebearer','mouthbrood'].includes(brood.strategy))continue;
      if(marine&&AL.BroodView){const p=AL.BroodView.position(t,brood,i),egg=AL.BroodView.image(brood),n=AL.BroodView.size(brood),x=p.x*W,y=p.y*H;
        if(egg)AL.SpriteKit.draw(g,egg,x,y,n,n);else{g.fillStyle=brood.viability<=0?'#746b52':'#e2d3a1';g.fillRect(Math.round(x-n/2),Math.round(y-n/2),n,n);}
        if(this.selected===brood.id){g.strokeStyle='#45D6D0';g.strokeRect(x-n/2-2,y-n/2-2,n+4,n+4);}
        this.hitboxes.push({id:brood.id,kind:'egg',x:((x-W*this.pan)*this.zoom+W/2)/W,y:((y-H/2)*this.zoom+H/2)/H,w:Math.max(12,n)*this.zoom/W,h:Math.max(12,n)*this.zoom/H});
      }else{const egg=AL.ClownArt?.frame(brood.species,null,'egg',brood.viability<=0?'dead':'alive')||AL.LifeStages?.frame(brood.species,'egg',brood.viability<=0?'dead':'alive');if(egg)AL.SpriteKit.draw(g,egg,226+(i%12)*18,214-Math.floor(i/12)*14,16,13,1,false);else{g.fillStyle='#e2d3a1';for(let n=0;n<brood.count;n++)g.fillRect(226+i*8+n*3,217,2,2);}}

    }
    g.restore();
    if(t.waterParams.clarity<85){g.fillStyle=`rgba(84,106,70,${(100-t.waterParams.clarity)/180})`;g.fillRect(0,0,W,H);}
    // Apply the same lamp output used by the ecosystem to the entire scene,
    // so fish, plants and hardscape all become visibly brighter under the light.
    const darkness=(roomNight?.6:.4)*(1-lamp);
    g.fillStyle=`rgba(3,13,25,${darkness})`;g.fillRect(0,0,W,H);
    if(lamp>0){
      g.save();g.globalCompositeOperation='screen';
      const glow=g.createLinearGradient(0,0,0,H);
      const rgb=marine?'157,220,255':'229,245,193';
      glow.addColorStop(0,`rgba(${rgb},${lamp*.25})`);
      glow.addColorStop(.45,`rgba(${rgb},${lamp*.13})`);
      glow.addColorStop(1,`rgba(${rgb},${lamp*.055})`);
      g.fillStyle=glow;g.fillRect(0,0,W,H);g.restore();
      g.fillStyle=marine?'#d2f1ff':'#edf5d4';g.globalAlpha=lamp*.75;g.fillRect(18,2,W-36,2);g.globalAlpha=1;
    }
    if(preview!=='none'){g.fillStyle={moonlight:'#7398dd22',amber:'#dcac6e22',prism:'#bc8ed422'}[preview];g.fillRect(0,0,W,H);}
    if(this.placement){
      const p=this.placement,x=(p.x-this.pan)*W*this.zoom+W/2,y=(p.y-.5)*H*this.zoom+H/2;
      g.save();g.translate(Math.round(x),Math.round(y));g.scale(this.zoom,this.zoom);g.globalAlpha=1;
      g.strokeStyle=p.valid===false?'#EF7075':p.status==='Conditional'?'#F4B860':'#79D6A3';g.setLineDash([2,2]);const bounds=p.kind?{width:p.width||44,height:p.kind==='rock'?p.width*.8:52}:AL.Art.plantBounds(p.type,p.size||1);g.strokeRect(Math.round(-bounds.width/2-3),Math.round(-bounds.height-3),Math.round(bounds.width+6),Math.round(bounds.height+7));g.setLineDash([]);
      g.fillStyle='#eff7bd';g.fillRect(-4,-1,9,2);g.fillRect(0,-5,1,9);g.restore();
    }
    g.fillStyle='#c0e9d011';AL.Art.poly(g,[[8,0],[20,0],[72,H],[61,H]],'#c0e9d00b');g.fillStyle='#c4dedb11';g.fillRect(4,0,2,H);g.fillRect(474,0,1,H);g.fillStyle='#e1f1d933';g.fillRect(0,3,W,1);for(let i=0;i<11;i++){g.fillStyle='#c5e9ce33';g.fillRect(Math.round(i*49+Math.sin(time*.5+i)*7),6+(i%2),23,1);}
    this.ctx.imageSmoothingEnabled=false;this.ctx.drawImage(this.scene,0,0,this.canvas.width,this.canvas.height);
  }
  hit(x,y){return [...this.hitboxes].reverse().find(f=>Math.abs(f.x-x)<f.w/2&&Math.abs(f.y-y)<f.h/2)?.id;}
  worldPoint(x,y){return {x:(x-.5)/this.zoom+this.pan,y:(y-.5)/this.zoom+.5};}
};
