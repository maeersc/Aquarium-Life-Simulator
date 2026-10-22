(async()=>{
 const A=AL.FishAnimation,entries=A.catalog.entries,checks=[],coverage=[],check=(name,pass)=>checks.push({name,pass:!!pass});
 check('Shared catalog matches all runtime marine fish/coral/invertebrate keys',Object.values(A.auditCatalog()).every(x=>!x.length));
 check('Catalog includes119 unique records without treating25 morphs as species',entries.length===119&&new Set(entries.map(e=>e.id)).size===119&&entries.reduce((n,e)=>n+e.varieties.length,0)===25);
 check('Twelve batches cover every record once, with final batch of nine',A.catalog.batches.length===12&&A.catalog.batches.slice(0,-1).every(b=>b.ids.length===10)&&A.catalog.batches[11].ids.length===9&&new Set(A.catalog.batches.flatMap(b=>b.ids)).size===119);
 const seed={seed:1616,nextId:1,time:480};
 for(const e of entries){
  const missing=!!e.missingArtwork&&e.status==='artwork-required'&&e.framesCompleted===0&&!e.clips.length&&!e.userApproved;
  check(e.id+': absent authored frames and player approval are reported honestly',missing);
  check(e.id+': correct biological category and original source registered',!!e.existingPath&&['fish','coral','invertebrate'].includes(e.category)&&e.water==='marine');
  if(e.category==='fish'){
   const f=AL.Core.fish(seed,e.id,{genes:{color:1,size:1,longevity:1,immunity:1,fertility:1}}),before=JSON.stringify(f);let stageData=[];
   for(const [stage,growth]of [['baby',.15],['juvenile',.6],['adult',1.1]]){
    f.growth=growth;f.dead=false;f.behavior='Swim';f.vx=.017*AL.Data.species[e.id].activity;f.vy=0;const p={facing:1};A.update(f,p,0,1);const rate=p.animation.rate*16;
    check(e.id+'/'+stage+': normal requested playback is6–10 slots/sec',rate>=6&&rate<=10);
    let peak=0;for(let i=0;i<160;i++){A.update(f,p,.05,1);peak=Math.max(peak,Math.abs(p.animation.tail),Math.abs(p.animation.fin));}
    check(e.id+'/'+stage+': calm tail/fin movement is bounded and body bob suppressed',peak<=1&&p.animation.bob===0);
    const original=A.source(f,.2),same=A.source(f,.2,false);check(e.id+'/'+stage+': missing production sheet preserves the existing source',original===same&&original.width>0);
    const phase=p.animation.phase;A.update(f,p,0,-1);check(e.id+'/'+stage+': changing facing does not restart the animation',p.animation.phase===phase);
    const fast={facing:1};f.vx*=1.8;A.update(f,fast,.05,1);f.vx=0;f.behavior='Rest';const rest={facing:1};A.update(f,rest,.05,1);check(e.id+'/'+stage+': actual fast swimming is faster than resting',fast.animation.rate>rest.animation.rate);
    f.dead=true;A.update(f,p,.05,1);const death=JSON.stringify(p.animation);A.update(f,p,.05,-1);check(e.id+'/'+stage+': dead artwork never resumes live motion',death===JSON.stringify(p.animation)&&p.animation.state==='dead');
    stageData.push({stage,requestedSlotsPerSecond:rate,peakPixels:peak});
   }
   coverage.push({id:e.id,category:e.category,authoredFrames:0,status:e.status,stages:stageData});
  }else{
   for(const stage of e.stages){
    const im=e.category==='coral'?AL.ExpansionArt.frame(e.id,stage)||AL.AssetBank.coral(e.id,'healthy',0):AL.ExpansionArt.frame(e.id,stage);
    check(e.id+'/'+stage+': original living pose remains available',im&&im.width>0);
    const dead=AL.ExpansionArt.frame(e.id,stage,'dead')||(e.category==='coral'?AL.AssetBank.coral(e.id,'dead',0):null);check(e.id+'/'+stage+': original death state remains available',dead&&dead.width>0);
    const c=document.createElement('canvas');c.width=c.height=80;check(e.id+'/'+stage+': absent limb/polyp sheets never use a fish deformation',A.drawResident(c.getContext('2d'),e.id,stage,e.requiredStates[0],40,40,48,40,10)===false);
    check(e.id+'/'+stage+': dead non-fish cannot use any live animation',A.drawResident(c.getContext('2d'),e.id,stage,'dead',40,40,48,40,10)===false);
   }
   coverage.push({id:e.id,category:e.category,authoredFrames:0,status:e.status,stages:e.stages});
  }
 }
 // Synthetic fixtures test the loader, never masquerading as real livestock art.
 const cell=16,cv=document.createElement('canvas');cv.width=cell*4;cv.height=cell*4;const g=cv.getContext('2d');
 for(let i=0;i<16;i++){g.fillStyle='#e5a631';g.fillRect(i%4*cell+3,Math.floor(i/4)*cell+5,9,5);g.fillStyle='#111';g.fillRect(i%4*cell+10,Math.floor(i/4)*cell+6,1,1);g.fillStyle='#68bca3';g.fillRect(i%4*cell+2,Math.floor(i/4)*cell+2,1+i%4,1+Math.floor(i/4));}
 const definition={status:'production',stage:'adult',state:'swim',frameCount:16,frameWidth:cell,frameHeight:cell,columns:4,order:Array.from({length:16},(_,i)=>i),framesPerSecond:8,anchor:[8,8],facing:'mirror-side-profile',src:cv.toDataURL(),validation:{visualReview:true}},fixture=A.createSheetLibrary([{id:'test-fixture',clips:[definition]}]),r=fixture.find('test-fixture','adult');
 check('Synthetic aligned16-frame fixture decodes once and validates',await fixture.load(r));
 check('All16 distinct fixture cells are selected in correct order',Array.from({length:16},(_,i)=>fixture.frame(r,i/16)?.artMeta.frameIndex===i).every(Boolean));
 check('Loop wraps to first frame and handles negative phase',fixture.frame(r,1)===fixture.frame(r,0)&&fixture.frame(r,-1/16)===fixture.frame(r,15/16));
 check('Sheet frame caches reuse decoded cells and stay bounded',fixture.frame(r,0)===fixture.frame(r,0)&&fixture.metrics.frameCache<=fixture.metrics.maxFrames);
 check('A missing designer variety never borrows another variety sheet',!fixture.find('test-fixture','adult','swim','designer-example'));
 check('Life stages never silently substitute adult swim sheets',!fixture.find('test-fixture','baby'));
 const sample=fixture.frame(r,.25),fish=AL.Core.fish(seed,'gramma');fish.growth=1;const p={facing:1,animation:{direction:1,bob:0,bank:0,tail:2,fin:2}},draw=document.createElement('canvas');draw.width=draw.height=64;
 const builds=A.metrics.rigBuilds;A.draw(draw.getContext('2d'),fish,sample,32,32,16,16,p);check('Authored sheet draw bypasses the procedural fin rig',A.metrics.rigBuilds===builds);
 const expected=document.createElement('canvas');expected.width=expected.height=64;expected.getContext('2d').drawImage(sample,24,24);check('Authored anchor is stable and receives no extra deformation',draw.toDataURL()===expected.toDataURL());
 const invalid=A.createSheetLibrary([{id:'wrong-index',clips:[{...definition,order:Array.from({length:16},(_,i)=>i+1)}]}]);check('Out-of-range16-frame indexing is rejected',invalid.records.size===0&&invalid.issues.length===1);
 const duplicate=document.createElement('canvas');duplicate.width=64;duplicate.height=64;const dg=duplicate.getContext('2d');for(let y=0;y<4;y++)for(let x=0;x<4;x++){dg.fillStyle='#ff8800';dg.fillRect(x*16+3,y*16+5,9,5);}
 const dup=A.createSheetLibrary([{id:'repeated-test',clips:[{...definition,src:duplicate.toDataURL()}]}]);check('Sixteen repeated images fail loader validation',!(await dup.load(dup.find('repeated-test','adult')))&&dup.issues.length>0);
 const proto=A.createSheetLibrary([{id:'prototype',clips:[{...definition,status:'prototype'}]}]);check('Prototype cannot enter production rendering',proto.records.size===0&&proto.issues.length===1);
 return {checks,coverage,productionSheets:entries.reduce((n,e)=>n+e.clips.length,0),authoredFramesCompleted:entries.reduce((n,e)=>n+e.framesCompleted,0),notArtApproval:true};
})()
