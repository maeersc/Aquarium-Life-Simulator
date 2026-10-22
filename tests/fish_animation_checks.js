(()=>{
 const A=AL.FishAnimation,K=AL.Core,checks=[],coverage=[],test=(name,fn)=>{try{const v=fn();checks.push({name,pass:!!v});}catch(e){checks.push({name,pass:false,error:e.message});}},eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
 const state=K.newGame('marine',29103),ids=Object.values(AL.Data.species).filter(d=>d.water==='marine').map(d=>d.id);
 const pixels=c=>c.getContext('2d').getImageData(0,0,c.width,c.height).data;
 const different=(a,b,region)=>{const aa=pixels(a),bb=pixels(b),w=a.width;for(let y=region?.top??0;y<(region?.bottom??a.height);y++)for(let x=region?.left??0;x<(region?.right??w);x++){const i=(y*w+x)*4;if(aa[i]!==bb[i]||aa[i+1]!==bb[i+1]||aa[i+2]!==bb[i+2]||aa[i+3]!==bb[i+3])return true;}return false;};
 test('Every current marine runtime fish has an explicit motion profile',()=>ids.length===94&&!A.audit().length);
 test('Five preview-only fish stay absent from the playable roster',()=>A.data.referenceOnly.every(id=>!AL.Data.species[id]));
 test('Clownfish designer morphs are separate varieties, never counted as biological species',()=>Object.values(AL.Clownfish.varieties).length>0&&ids.filter(id=>AL.Data.species[id].clownfish).length===31);
 for(const id of ids){
  const d=AL.Data.species[id],f=K.fish(state,id),row={id,name:d.name,scientificName:d.scientificName,family:A.data.species[id].family,stages:[],states:[],finalClassification:'B',reason:'Visible runtime motion verified; existing authored-stage/anatomy approvals remain provisional.'};
  test(id+': motion is read-only and advances while hovering',()=>{f.vx=f.vy=0;f.behavior='Explore';const original=JSON.stringify(f),pos={facing:1};A.update(f,pos,0,1);const phase=pos.animation.phase;for(let i=0;i<20;i++)A.update(f,pos,.05,1);return JSON.stringify(f)===original&&pos.animation.phase!==phase&&pos.animation.rate>0;});
  for(const [life,growth] of [['baby',.15],['juvenile',.6],['adult',1.1]]){
   // Explicitly exercise the retained source-art fallback articulation here.
   // Actual authored-sheet playback bypasses this rig and has its own suite.
   f.growth=growth;const source=A.source(f,0,false),dead={...f,dead:true},death=A.source(dead,0),w=64,h=Math.round(w*source.height/source.width),base=AL.SpriteKit.raster(source,w,h),a=A.pose(source,w,h,id,-2,0),b=A.pose(source,w,h,id,2,0),c=A.pose(source,w,h,id,0,-2),e=A.pose(source,w,h,id,0,2),m=a.animationMeta;
   const foldOnly=A.data.species[id].appendages?.[life]==='caudal-fold-only',outerFin=different(c,e),tailFin=different(a,b),info={stage:life,source:!!source,dead:!!death?.artMeta?.authoredDeath,eye:!!m.eye,tail:tailFin,fin:foldOnly?tailFin:outerFin,outerFin,caudalFoldOnly:foldOnly,transparent:true,headPreserved:true};
   test(id+' '+life+': dedicated live/dead artwork exists',()=>info.source&&info.dead);
   test(id+' '+life+': tail moves and stays attached to a fixed root',()=>info.tail&&!different(a,b,{left:m.joint+4,right:a.width,top:0,bottom:a.height}));
   test(id+' '+life+(foldOnly?': retained caudal fold moves without inventing a paired-fin layer':': authored outer fins visibly move'),()=>foldOnly?info.tail&&!outerFin:outerFin);
   test(id+' '+life+': head and registered eye stay pixel-identical between rig poses',()=>{info.headPreserved=!!m.eye&&!different(c,e,{left:m.head+4,right:c.width,top:0,bottom:c.height});return info.headPreserved;});
   for(const direction of [1,-1])test(id+' '+life+': correct original eye pixels render facing '+direction,()=>{const target=document.createElement('canvas');target.width=120;target.height=100;const g=target.getContext('2d'),eye=m.eye;A.draw(g,f,source,60,50,w,h,{facing:direction,animation:{direction,tail:1,fin:1,bank:0,bob:0}});const expected=base.getContext('2d').getImageData(eye.x,eye.y,eye.w,eye.h).data,x=direction===1?60-Math.floor(w/2)+eye.x:60+Math.floor(w/2)-eye.x-eye.w,y=50-Math.floor(h/2)+eye.y,actual=g.getImageData(x,y,eye.w,eye.h).data;for(let yy=0;yy<eye.h;yy++)for(let xx=0;xx<eye.w;xx++)for(let k=0;k<4;k++)if(actual[(yy*eye.w+xx)*4+k]!==expected[(yy*eye.w+(direction===1?xx:eye.w-1-xx))*4+k])return false;return true;});
   test(id+' '+life+': all moving pixels fit transparent padding',()=>{for(const im of [a,b,c,e]){const p=pixels(im);for(let x=0;x<im.width;x++)if(p[x*4+3]||p[((im.height-1)*im.width+x)*4+3])return info.transparent=false;for(let y=0;y<im.height;y++)if(p[(y*im.width)*4+3]||p[(y*im.width+im.width-1)*4+3])return info.transparent=false;}return true;});
   test(id+' '+life+': cached poses reuse the same canvas',()=>A.pose(source,w,h,id,-2,0)===a);
   const sceneWidth=Math.round(64*Math.max(.35,Math.min(1.7,.6+d.size/28)*Math.sqrt(growth)*f.genes.size)),sceneHeight=Math.round(sceneWidth*source.height/source.width),smallTailA=A.pose(source,sceneWidth,sceneHeight,id,-1,0),smallTailB=A.pose(source,sceneWidth,sceneHeight,id,1,0),smallFinA=A.pose(source,sceneWidth,sceneHeight,id,0,-1),smallFinB=A.pose(source,sceneWidth,sceneHeight,id,0,1);
   const unresolved=foldOnly||sceneWidth<(A.data.species[id].outerFinMinimum?.[life]||0);info.sceneWidth=sceneWidth;info.sceneTail=different(smallTailA,smallTailB);info.sceneOuterFin=different(smallFinA,smallFinB);info.sceneFin=unresolved?info.sceneTail:info.sceneOuterFin;info.sceneArtGap=unresolved?'Independent outer-fin layer unresolved; retained caudal fold animates':null;
   test(id+' '+life+': tail moves at actual aquarium display size',()=>info.sceneTail);
   test(id+' '+life+(unresolved?': caudal fin fold moves at tank scale; missing paired fins remain an art gap':': fins move at actual aquarium display size'),()=>info.sceneFin&&(!unresolved||!info.sceneOuterFin));
   row.stages.push(info);
  }
  f.growth=1.1;f.behavior='Explore';f.vx=f.vy=0;
  const pos={facing:1};A.update(f,pos,.05,1);const idle=pos.animation.rate;f.vx=.017*d.activity*1.8;A.update(f,pos,.05,1);const fast=pos.animation.rate;
  test(id+': faster propulsion increases beat frequency',()=>fast>idle&&pos.animation.state==='fast');
  f.vx=f.vy=0;for(const [behavior,expected]of [['Rest','rest'],['Hide','rest'],['Eat','feed'],['Prepare nest','nest'],['Guard and fan eggs','guard'],['Courtship circle','court'],['Synchronized spawning rise','spawn'],['Male mouthbrooding','mouthbrood']]){
   f.behavior=behavior;A.update(f,pos,.05,1);row.states.push(pos.animation.state);test(id+': existing '+behavior+' state maps without changing fish data',()=>pos.animation.state===expected);
  }
  f.behavior='Explore';test(id+': banked turn retains a side profile and completes to the left',()=>{pos.animation.direction=pos.animation.target=1;pos.animation.turn=1;for(let i=0;i<8;i++)A.update(f,pos,.05,-1);return pos.animation.direction===-1&&pos.animation.turn===1&&Math.abs(pos.animation.bank)<.1;});
  test(id+': health symptoms have distinct presentation',()=>{const h=f.healthState;f.healthState={conditions:[{type:'velvet',severity:.4,age:48,carrier:false}]};A.update(f,pos,.05,1);const respiratory=pos.animation.state;f.healthState.conditions[0].type='injury';A.update(f,pos,.05,1);const weak=pos.animation.state;f.healthState=h;return respiratory==='respiratory'&&weak==='weak';});
  test(id+': death freezes all active swimming, fins and banking',()=>{f.dead=true;A.update(f,pos,.05,-1);const v=JSON.stringify(pos.animation);A.update(f,pos,.1,1);return v===JSON.stringify(pos.animation)&&pos.animation.state==='dead'&&pos.animation.tail===0&&pos.animation.fin===0&&pos.animation.rate===0;});
  coverage.push(row);
 }
 test('Clown natural pattern source pixels remain fixed through procedural fin phases',()=>{const f=K.fish(state,'clown');f.growth=.6;f.patternProfile.legacy=false;f.patternProfile.phenotype='Misbar / unusual bands';const before=JSON.stringify(f),source=AL.Patterns.sprite(f,A.source(f,0)),a=A.pose(source,64,53,'clown',-2,-1),b=A.pose(source,64,53,'clown',2,1),m=a.animationMeta;return JSON.stringify(f)===before&&!different(a,b,{left:m.joint+4,right:m.head+4,top:Math.ceil(m.cy-m.half)+4,bottom:Math.floor(m.cy+m.half)+4});});
 for(const variety of Object.values(AL.Clownfish.varieties))test('Designer pattern preserved: '+variety.id,()=>{const f=K.fish(state,variety.speciesId);f.variety=variety.id;f.growth=1.1;const before=JSON.stringify(f),a=A.source(f,0),b=A.source(f,.4);return a&&b&&JSON.stringify(f)===before&&a.artMeta.variety===variety.id&&b.artMeta.variety===variety.id;});
 test('Rig pose cache is globally bounded',()=>A.metrics.poseCache<=A.metrics.maxPoses);
 test('Banggai early display uses developed juvenile artwork, never the historical yolk-sac pose',()=>{const f=K.fish(state,'banggai');f.growth=.15;return A.source(f).artMeta.stage==='juvenile'&&AL.Breeding.profile('banggai').mode==='mouthbrood';});
 test('Unattached juvenile filefish fin artifact is masked without repainting the fish',()=>{const im=AL.ExpansionArt.frame('orange-spotted-filefish','juvenile'),a=im.getContext('2d').getImageData(75,110,34,12).data;return a.every((v,i)=>i%4!==3||v===0);});
 const result={passed:checks.filter(x=>x.pass).length,failed:checks.filter(x=>!x.pass).length,checks,coverage};window.fishAnimationResult=result;return result;
})()
