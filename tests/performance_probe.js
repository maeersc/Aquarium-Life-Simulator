AL.Startup.finish();AL.Save.unlock();
window.__probe=(()=>{
 let stamps=[],costs=[],calls={},start=0;
 const wrap=(owner,key,label)=>{if(!owner||typeof owner[key]!=='function')return;const fn=owner[key];owner[key]=function(...args){const a=performance.now();try{return fn.apply(this,args)}finally{const ms=performance.now()-a,r=calls[label]||(calls[label]={count:0,ms:0,max:0});r.count++;r.ms+=ms;r.max=Math.max(r.max,ms);if(label==='draw'){stamps.push(a);costs.push(ms)}}}};
 for(const [o,k,l] of [[AL.renderer,'draw','draw'],[AL.Sim,'step','simulation'],[AL.UI,'updateVitals','vitals'],[AL.UI,'render','UI'],[AL.TutorialUI,'update','tutorial'],[AL.Store,'render','store'],[AL.Shell,'render','shell'],[AL.Save,'save','save'],[AL.DivingUI,'draw','divingDraw']])wrap(o,k,l);
 const close=()=>{if(AL.DivingUI?.ownsDialog)AL.DivingUI.requestDismiss();AL.UI.close();AL.Store.close();AL.Shell.close();AL.CasinoUI.close?.();document.querySelectorAll('dialog[open]').forEach(d=>d.close());};
 function fixture(kind){close();AL.game=AL.Save.parse(JSON.stringify(__small));const s=AL.game,t=s.tanks[0];s.settings.speed=1;s.savedAt=Date.now();s.simulationCheckpoint=Date.now();
  if(kind!=='A'){
   t.volume=AL.Data.sizes.find(d=>d.volume>=(kind==='B'?370:3700)).volume;t.name='Isolated benchmark '+kind;
   for(const e of t.equipment){e.capacity=t.volume;if(e.type==='heater'){const model=AL.Heaters.recommended(t);e.heaterModel=model.id;e.capacity=model.capacity;}}
   // Peaceful reef community, conservative load in a large reef. No live player data.
   const ids=Object.values(AL.Data.species).filter(d=>d.water==='marine'&&!d.fictional&&d.purchaseVerified!==false&&d.aggression<.25&&d.minTank<=300&&d.temp[0]<=25&&d.temp[1]>=25&&d.size<=12).map(d=>d.id).slice(0,kind==='B'?4:10);
   t.fish=[];for(const id of ids){const d=AL.Data.species[id];for(let n=0;n<Math.max(d.group||1,kind==='B'?1:3);n++){const f=AL.Core.fish(s,id);f.growth=1;f.hunger=5;t.fish.push(f);}}
   const coral=Object.keys(AL.Data.flora).filter(id=>AL.Data.flora[id].water==='marine').slice(0,3);t.flora=[];t.mounts=[];for(const [i,type] of coral.entries()){const x=.2+i*.3;t.mounts.push({id:'rack'+s.nextId++,x,y:.48,width:80,glass:'back',mounted:true});const f={id:'flora'+s.nextId++,type,...AL.Habitat.position(s,t,type,x,.48,{size:.8}),size:.8,hp:100,age:10,color:1};AL.Health.initialize(f);t.flora.push(f);}
   if(kind==='D'){for(let i=0;i<3;i++){const copy=AL.Core.tank(s,'marine',t.volume,'Background '+i,'reef');copy.prepared=true;copy.bacteria=copy.bacteria2=1;copy.fish=[AL.Core.fish(s,ids[0])];s.tanks.push(copy);}}
  }
  AL.Save.migrate(s);AL.Save.validate(s);AL.UI.render();AL.Performance?.normalize(s.settings);return {fish:t.fish.length,corals:t.flora.length,tanks:s.tanks.length};
 }
 function menu(name){close();if(name==='store')AL.Store.open();else if(name==='diving')AL.DivingUI.open();else if(name==='casino')AL.CasinoUI.open();else AL.Shell.open(name);}
 const q=(v,p)=>v.length?[...v].sort((a,b)=>a-b)[Math.min(v.length-1,Math.floor(v.length*p))]:null;
 return {fixture,close,menu,reset(){stamps=[];costs=[];calls={};__long=[];start=performance.now()},result(){const gaps=stamps.slice(1).map((v,i)=>v-stamps[i]),elapsed=performance.now()-start;return {elapsedMs:elapsed,draws:stamps.length,fps:stamps.length*1000/elapsed,frameGapP50:q(gaps,.5),frameGapP95:q(gaps,.95),frameGapP99:q(gaps,.99),drawMsP50:q(costs,.5),drawMsP95:q(costs,.95),drawMsMax:Math.max(0,...costs),calls,longTasks:__long,scheduler:AL.loop?.stats||null,caches:{sheets:AL.FishAnimation.sheets.metrics,animation:AL.FishAnimation.metrics,rasters:AL.SpriteKit.metrics,sources:AL.SpriteSources?.metrics,layers:AL.renderer.layers?{entries:AL.renderer.layers.size,bytes:AL.renderer.layers.size*480*240*4,builds:AL.renderer.layerBuilds}:null},state:{fish:AL.Core.selected(AL.game).fish.length,tanks:AL.game.tanks.length,gameTime:AL.game.time,hidden:document.hidden}}}};
})();
