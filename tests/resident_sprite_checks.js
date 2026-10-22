/* QA-only non-fish fixtures; never loaded by the game or offline art gallery. */
window.SpriteResidentQA=(()=>{
 const A=AL.FishAnimation,K=AL.Core;let lastClick=null;
 function make(e,stage,state){
  let s=K.newGame('marine',16250);s.settings.speed=0;s.settings.particles=false;AL.Finance.change(s,100000-s.credits,{category:'other',action:'qaFixture',name:'Isolated art benchmark funds'});s.xp=3800;s.level=20;
  s=K.act(s,'prepare');
  let t=s.tanks[0],f;t.bacteria=t.bacteria2=.95;t.ecosystemAge=200;
  if(e.category==='coral'){
   s=K.act(s,'buyRack',{glass:'back'});t=s.tanks[0];const size=stage==='frag'?.8:1.3;
   f={id:K.id(s,'flora'),type:e.id,name:AL.Data.flora[e.id].name,...AL.Habitat.position(s,t,e.id,.6,.48,{size}),hp:100,size,age:120,color:1,rarity:AL.Rarity.plant(e.id).name};
   AL.Health.initialize(f);t.flora=[f];
  }else{
   f=AL.Invertebrates.make(s,t,e.id);f.growth={baby:.15,juvenile:.6,adult:1}[stage];f.age=AL.Data.invertebrates[e.id].maturity*f.growth;f.x=.5;f.z=.5;f.behavior=state==='walk'?'Crawl':'Rest';t.invertebrates=[f];
  }
  return {s,t,f};
 }
 const collection=(t,e)=>e.category==='coral'?t.flora:t.invertebrates;
 const identity=f=>JSON.stringify([f.id,f.type||f.invertebrate,f.name,f.hp,f.hunger??null,f.rarity,f.healthState,f.genes??null,f.patternProfile??null,f.provenance??null,f.growth??null,f.size??null]);
 function saveAndClick(e,stage,state,check){
  const {s,t,f}=make(e,stage,state),name=e.id+'/'+stage+'/'+state,expected=identity(f),value=AL.Valuation.livestock(s,f).value;
  const written=AL.Save.save(s),loaded=AL.Save.load(),other=loaded.state&&collection(loaded.state.tanks[0],e)[0];
  check(name+': actual local save/load retains non-fish identity, condition, stage and value',written.ok&&other&&identity(other)===expected&&AL.Valuation.livestock(loaded.state,other).value===value);
  AL.game=s;AL.renderer.positions.clear();AL.UI.close();AL.Shell?.close();AL.Store?.close();
  const before=JSON.stringify(s),calls=[],draw=A.drawResident;
  A.drawResident=function(...args){const result=draw(...args);calls.push({id:args[1],stage:args[2],state:args[3],accepted:result,x:args[4],y:args[5]});return result;};
  try{AL.renderer.draw(s,0);}finally{A.drawResident=draw;}
  check(name+': actual rendering leaves the saved ecosystem untouched',JSON.stringify(s)===before);
  const hit=AL.renderer.hitboxes.find(b=>b.id===f.id),canvas=document.getElementById('aquarium'),rect=canvas.getBoundingClientRect();let selected=false;
  if(hit){const event=new MouseEvent('click',{bubbles:true,clientX:rect.left+hit.x*rect.width,clientY:rect.top+hit.y*rect.height});const normalized={x:(event.clientX-rect.left)/rect.width,y:(event.clientY-rect.top)/rect.height};lastClick={expected:f.id,centerHit:AL.renderer.hit(hit.x,hit.y),eventHit:AL.renderer.hit(normalized.x,normalized.y),hit,normalized,rect:{left:rect.left,top:rect.top,width:rect.width,height:rect.height},viewport:[innerWidth,innerHeight]};canvas.dispatchEvent(event);lastClick.selected=AL.renderer.selected;lastClick.dialog=document.getElementById('dialog').open;lastClick.title=document.getElementById('dialog-body').textContent.slice(0,120);selected=AL.renderer.selected===f.id&&document.getElementById('dialog').open;AL.UI.close();}
  if(!selected)(window.__residentSelectionFailures??=[]).push(lastClick);
  check(name+': actual canvas click opens the correct non-fish resident inspector',selected);
  return {s,t,f,calls};
 }
 function verify(e,clip,frames,check){
  const name=e.id+'/'+clip.stage+'/'+clip.state,{s,t,f,calls}=saveAndClick(e,clip.stage,clip.state,check);
  const expectedX=f.x*480;
  check(name+': real aquarium renderer uses the exact authored stage/state',calls.some(c=>c.id===e.id&&c.stage===clip.stage&&c.state===clip.state&&c.accepted&&Math.abs(c.x-expectedX)<.01));
  check(name+': anatomy metadata retains biological identity',frames.every(im=>im.artMeta.speciesId===e.id&&im.artMeta.stage===clip.stage&&im.artMeta.state===clip.state));
  const w=clip.frameWidth,h=clip.frameHeight,mutable=new Uint8Array(w*h);
  for(const [y,x0,x1] of clip.fixedStructure.mutableRuns)for(let x=x0;x<x1;x++)mutable[y*w+x]=1;
  const base=frames[0].getContext('2d').getImageData(0,0,w,h).data;let protectedVisible=0;
  for(let p=0;p<mutable.length;p++)if(!mutable[p]&&base[p*4+3])protectedVisible++;
  check(name+': actual skeleton/shell/body pixels stay identical through all16 authored cells',protectedVisible>=16&&frames.every(frame=>{const pixels=frame.getContext('2d').getImageData(0,0,w,h).data;for(let p=0;p<mutable.length;p++)if(!mutable[p])for(let c=0;c<4;c++)if(pixels[p*4+c]!==base[p*4+c])return false;return true;}));
  const cv=document.createElement('canvas');cv.width=256;cv.height=256;const g=cv.getContext('2d'),before=JSON.stringify(f);let valid=true;
  for(let i=0;i<32;i++){g.clearRect(0,0,256,256);valid&&=A.drawResident(g,e.id,clip.stage,clip.state,128,128,128,128*h/w,i/clip.framesPerSecond,i<16?1:-1);}
  check(name+': all16 poses draw in both directions without mutating the specimen',valid&&JSON.stringify(f)===before);
  check(name+': deceased resident bypasses living animation',A.drawResident(g,e.id,clip.stage,'dead',128,128,128,128*h/w,1,1)===false);
  const record=A.sheets.find(e.id,clip.stage,clip.state);let a=0,b=0;for(let i=0;i<180;i++)a+=1/60;for(let i=0;i<90;i++)b+=1/30;
  check(name+': absolute resident animation clock is independent of render cadence',Math.abs(a-b)<1e-9&&A.sheets.frame(record,(a*clip.framesPerSecond+1e-7)/16)===A.sheets.frame(record,(b*clip.framesPerSecond+1e-7)/16));
  if(e.category==='coral')check(name+': legacy/expansion aspect and attachment are retained',clip.anchor[0]===w/2&&clip.anchor[1]===(h===192?184:h));
 }
 async function mixedPerformance(check){
  const entries=A.catalog.entries,fish=entries.filter(e=>e.category==='fish'&&e.clips.some(c=>c.stage==='adult'&&!c.variety)),corals=entries.filter(e=>e.category==='coral'&&e.clips.some(c=>c.stage==='colony')),inverts=entries.filter(e=>e.category==='invertebrate'&&e.clips.some(c=>c.stage==='adult'&&c.state==='walk'));
  // An absent category is unfinished production, not a successful mixed test.
  if(!corals.length||!inverts.length)return null;
  const {s,t}=make(corals[0],'colony','polyp_motion');t.fish=[];t.flora=[];t.invertebrates=[];
  for(let i=0;i<AL.Config.maxFish;i++){const f=K.fish(s,fish[i%fish.length].id);f.growth=1;f.x=.08+(i%10)*.09;f.y=.2+Math.floor(i/10)%7*.09;t.fish.push(f);}
  for(let i=0;i<35;i++){const e=corals[i%corals.length],f=make(e,'colony','polyp_motion').f;f.id=K.id(s,'flora');f.x=.06+(i%10)*.095;t.flora.push(f);}
  for(let i=0;i<40;i++){const e=inverts[i%inverts.length],f=AL.Invertebrates.make(s,t,e.id);f.growth=1;f.behavior='Crawl';f.x=.04+(i%10)*.1;f.z=.2+Math.floor(i/10)*.2;t.invertebrates.push(f);}
  const records=[...fish.map(e=>A.sheets.find(e.id,'adult','swim')),...corals.map(e=>A.sheets.find(e.id,'colony','polyp_motion')),...inverts.map(e=>A.sheets.find(e.id,'adult','walk'))];
  await Promise.all(records.map(r=>A.sheets.load(r)));
  check('Mixed maximum-stock benchmark loads every selected authored source',records.every(r=>r.image));
  AL.game=s;AL.renderer.positions.clear();for(let i=0;i<32;i++)AL.renderer.draw(s,1/60);
  const original=JSON.stringify(s),times=[];let accepted=0,staticBackdropDraws=0;const draw=A.drawResident;
  A.drawResident=function(...args){const result=draw(...args);if(result){if(args[8]===AL.renderer.time)accepted++;else staticBackdropDraws++;}return result;};
  try{for(let i=0;i<120;i++){const start=performance.now();AL.renderer.draw(s,1/60);times.push(performance.now()-start);}}finally{A.drawResident=draw;}
  times.sort((a,b)=>a-b);const result={fish:t.fish.length,corals:t.flora.length,invertebrates:t.invertebrates.length,distinctFish:fish.length,distinctCorals:corals.length,distinctInvertebrates:inverts.length,frames:120,medianMs:times[60],p95Ms:times[114],meanMs:times.reduce((n,v)=>n+v,0)/times.length,acceptedResidentDraws:accepted,staticBackdropDraws,minimumTargetFps:30};
  // The unchanged renderer also prints sixteen fixed coral backdrop silhouettes
  // at time zero; those are scenery, not extra owned livestock.
  check('Mixed scene actually draws every owned authored coral and invertebrate each frame',accepted===(35+40)*120);
  check('Mixed maximum-stock drawing leaves the ecosystem and saved identities untouched',JSON.stringify(s)===original);
  check('Mixed maximum-stock authored playback stays within30fps budget at95th percentile',result.p95Ms<1000/30);
  check('Mixed playback preserves bounded image/frame caches',A.sheets.metrics.loaded<=A.sheets.metrics.maxDecodedSheets&&A.sheets.metrics.frameCache<=A.sheets.metrics.maxFrames);
  return result;
 }
 return {make,saveAndClick,verify,mixedPerformance,get lastClick(){return lastClick;}};
})();
