"use strict";
window.runClownChecks=()=>{
 const results=[],K=AL.Core,C=AL.Clownfish,A=AL.ClownArt;
 const check=(ok,name)=>results.push({pass:!!ok,name});
 check(C.species.length===31&&new Set(C.species.map(d=>d.scientificName)).size===31,'31 unique catalogued scientific names');
 check(Object.keys(C.varieties).length===25,'25 linked designer varieties');
 check(Object.keys(AL.Data.species).length===80&&Object.values(AL.Data.species).filter(d=>d.water==='fresh').length===11,'Standalone collection gallery: 80 baseline fish records include the protected 11 freshwater records');
 check(C.species.find(d=>d.id==='clown')?.scientificName==='Amphiprion ocellaris','Existing Ocellaris runtime ID retained');
 check(A.loaded===56&&!A.errors.length,'All 56 local collection sheets load');
 check(C.species.filter(d=>d.purchaseVerified===false).length===5,'Five specialist care holds explicitly retained');
 let cases=0;
 for(const [family,entries] of [['species',C.species],['varieties',Object.values(C.varieties)]])for(const e of entries){
  const species=family==='species'?e.id:e.speciesId,variety=family==='varieties'?e.id:null,m=A.metadata(species,variety);
  check(!!m&&!m.approved&&m.reviewStatus.includes('Provisional'),e.id+': no automatic art approval');
  check(AL.Data.species[species].water==='marine'&&(!variety||e.speciesId===species),e.id+': marine base biology');
  for(const state of ['alive','dead'])for(const stage of ['egg','baby','juvenile','adult']){
   const f=A.frame(species,variety,stage,state,0,1,false);check(!!f&&f.width===192&&f.height===160&&f.artMeta.authoredDeath===(state==='dead'),e.id+': '+stage+' '+state+' native pose');
   if(!f)continue;
   if(variety&&['egg','baby'].includes(stage))check(f.toDataURL()===A.frame(species,null,stage,state,0,1,false).toDataURL(),e.id+': '+stage+' '+state+' shares base artwork');
   for(const width of [25,52,73,117]){
    const height=Math.round(width*160/192),r=AL.SpriteKit.raster(f,width,height),eb=r.eyeBounds;
    if(stage!=='egg'){const ep=eb?r.getContext('2d').getImageData(eb.x,eb.y,eb.w,eb.h).data:[];let visible=false;for(let i=0;i<ep.length;i+=4)if(ep[i+3]>128&&Math.max(ep[i],ep[i+1],ep[i+2])<150)visible=true;check(!!eb&&eb.w>=3&&eb.h>=3&&visible,e.id+': '+stage+' '+state+' pupil pixels survive '+width+'px');}
    const right=document.createElement('canvas'),left=document.createElement('canvas');right.width=left.width=160;right.height=left.height=160;
    for(const [c,dir] of [[right,1],[left,-1]]){const g=c.getContext('2d'),before=g.getTransform();AL.SpriteKit.draw(g,f,80,80,width,height,dir);check(g.getTransform().toString()===before.toString(),e.id+': transform restored');}
    const rp=right.getContext('2d').getImageData(0,0,160,160).data,lp=left.getContext('2d').getImageData(0,0,160,160).data;let mirror=true;
    for(let y=0;y<160&&mirror;y++)for(let x=width%2?1:0;x<160&&mirror;x++)for(let k=0;k<4;k++)if(rp[(y*160+x)*4+k]!==lp[(y*160+(width%2?160:159)-x)*4+k]){mirror=false;break;}
    check(mirror,e.id+': '+stage+' '+state+' exact whole-sprite mirror '+width+'px');cases++;
   }
  }
  const cycle=[0,1,2,3].map(i=>A.frame(species,variety,'adult','alive',i/6+.001));
  check(new Set(cycle.map(f=>f.toDataURL())).size===4,e.id+': four distinct adult swim poses');
  check(cycle.every(f=>JSON.stringify(f.artMeta.eye)===JSON.stringify(cycle[0].artMeta.eye)),e.id+': stable eye registration through swim cycle');
  const eye=cycle[0].artMeta.eye,pixels=cycle.map(f=>Array.from(f.getContext('2d').getImageData(Math.round(eye.x-eye.w/2),Math.round(eye.y-eye.h/2),eye.w,eye.h).data).join(','));
  check(pixels.every(p=>p===pixels[0]),e.id+': identical artist eye pixels across swimming poses');
 }
 let s=K.newGame('marine',443),t=K.selected(s);s.credits=100000;s.level=11;s.xp=2000;s.time=720;t.volume=300;t.prepared=true;t.bacteria=t.bacteria2=1;
 try{
  s=K.act(s,'buyFish',{species:'clown',variety:'snowflake-ocellaris',count:2},'var-order');t=K.selected(s);check(t.fish.length===2&&t.fish.every(f=>f.species==='clown'&&f.variety==='snowflake-ocellaris'),'Designer purchase preserves species identity');
  check(new Set(t.fish.map(f=>f.sex)).size===2,'Marine clownfish purchased as one female and one male');
  check(K.act(s,'buyFish',{species:'clown',variety:'snowflake-ocellaris',count:2},'var-order')===s,'Designer transaction token prevents a duplicate charge');
  const female=t.fish.find(f=>f.sex==='F');female.adultSize=1;for(let i=0;i<30;i++)AL.Sim.step(s);check(female.sex==='F','Established female never changes back to male');
 }catch(e){check(false,'Designer purchase/sex fixture: '+e.message);}
 window.CLOWN_MATRIX={cases,results};return {cases,passed:results.filter(r=>r.pass).length,failed:results.filter(r=>!r.pass).length,checks:results};
};
