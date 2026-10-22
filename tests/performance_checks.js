(async()=>{
 const checks=[],ck=(name,pass)=>checks.push({name,pass:!!pass}),P=AL.Performance;
 const settings={particles:true};P.normalize(settings);
 ck('New graphics settings default to60fps/high/full/background saving',settings.graphics.frameRate===60&&settings.graphics.quality==='high'&&settings.graphics.water==='high'&&settings.graphics.particles==='full'&&settings.graphics.backgroundSaving);
 const legacy={particles:false};P.normalize(legacy);ck('Existing particle-off preference migrates without enabling it',legacy.graphics.particles==='off');
 for(const hz of [60,120,144,165,240])for(const fps of [30,60]){
  const pacer=new P.Pacer(),stamps=[];pacer.reset(0);
  for(let i=1;i<=hz*60;i++){const now=i*1000/hz;if(pacer.take(now,fps)!==null)stamps.push(now);}
  const gaps=stamps.slice(1).map((v,i)=>v-stamps[i]);
  ck(hz+'Hz virtual display / '+fps+'fps: bounded target, stable elapsed pacing',Math.abs(stamps.length-fps*60)<=1&&Math.max(...gaps)<=1000/fps+1000/hz+.6&&Math.min(...gaps)>0);
 }
 const clockRun=(hz)=>{const s=JSON.parse(JSON.stringify(__small));s.settings.speed=1;const clock=new P.SimClock();for(let i=0;i<hz*60;i++)clock.add(1/hz*AL.Config.minutesPerSecond,s,Infinity);clock.flush(s);return JSON.stringify({seed:s.seed,time:s.time,tanks:s.tanks,stats:s.stats,finance:s.finance});};
 ck('30/60/144Hz biology and elapsed game time are identical for equivalent60-second input',clockRun(30)===clockRun(60)&&clockRun(60)===clockRun(144));
 ck('One day remains1200 real seconds',Math.abs(1440/AL.Config.minutesPerSecond-1200)<1e-8);
 __probe.fixture('A');const s=AL.game;s.settings.speed=0;const before=JSON.stringify(s);for(let i=0;i<32;i++)AL.renderer.draw(s,1/60);ck('Rendering leaves complete saved biological state untouched',before===JSON.stringify(s));
 const f=s.tanks[0].fish[0],r=AL.FishAnimation.sheetForFish(f);await AL.FishAnimation.sheets.load(r);const frames=[];for(let i=0;i<16;i++)frames.push(AL.FishAnimation.sheets.frame(r,i/16));
 ck('Actual owned fish retains16 distinct authored frame canvases with eye and anchor metadata',new Set(frames).size===16&&frames.every(im=>im.artMeta.frameCount===16&&im.artMeta.eye&&im.artMeta.anchor));
 let faithful=true;const ca=document.createElement('canvas'),cb=document.createElement('canvas');ca.width=cb.width=128;ca.height=cb.height=96;const ga=ca.getContext('2d',{willReadFrequently:true}),gb=cb.getContext('2d',{willReadFrequently:true}),test={...f,genes:{...f.genes}};
 for(const tone of [.6,.8,1,1.2,1.4])for(const direction of [-1,1])for(let n=0;n<16;n++){test.genes.color=tone;const a=AL.FishAnimation.source(test,n/16),b=AL.FishAnimation.source(test,n/16,true,true),pos={animation:{direction,bob:0,bank:0}};ga.clearRect(0,0,128,96);gb.clearRect(0,0,128,96);AL.FishAnimation.draw(ga,test,a,64,48,64,Math.round(64*a.height/a.width),pos);AL.FishAnimation.draw(gb,test,b,64,48,64,Math.round(64*b.height/b.width),pos,true);const pixels=ga.getImageData(0,0,128,96).data,other=gb.getImageData(0,0,128,96).data;faithful&&=pixels.every((v,i)=>Math.abs(v-other[i])<=1);}
 ck('Final-size tint retains every authored pixel/eye across16 frames, five tones and both facings (1-channel rounding tolerance)',faithful);
 AL.renderer.draw(s,1/60);const hit=AL.renderer.hitboxes.find(h=>h.id===f.id);ck('Resident selection still uses displayed aquarium coordinates',!!hit&&AL.renderer.hit(hit.x,hit.y)===f.id);
 const node=document.querySelector('#event-log').firstElementChild;AL.UI.updateVitals();AL.UI.updateVitals();ck('Unchanged event log retains its actual DOM nodes',node===document.querySelector('#event-log').firstElementChild);
 const old=JSON.parse(JSON.stringify(s));delete old.settings.graphics;const restored=AL.Save.parse(JSON.stringify(old));ck('Old schema2 save receives additive graphics defaults without asset loss',restored.version===2&&restored.settings.graphics.frameRate===60&&restored.tanks[0].fish[0].id===f.id);
 s.settings.speed=1;AL.UI.save();const continuityBefore={wall:Date.now(),time:AL.game.time+(AL.loop.stats.pendingMinutes||0)};await new Promise(r=>setTimeout(r,1500));AL.game=JSON.parse(JSON.stringify(AL.game));AL.UI.save();const continuityAfter={wall:Date.now(),time:AL.game.time+(AL.loop.stats.pendingMinutes||0)};ck('Transaction state cloning and its immediate checkpoint retain unsimulated partial time',Math.abs(continuityAfter.time-continuityBefore.time-(continuityAfter.wall-continuityBefore.wall)/1000*AL.Config.minutesPerSecond)<.15);AL.game.settings.speed=0;
 for(const fps of [30,60]){AL.game.settings.graphics.frameRate=fps;const saved=AL.Save.save(AL.game),loaded=AL.Save.load();ck(fps+'fps local save/load preserves preferences and resident identity',saved.ok&&loaded.state.settings.graphics.frameRate===fps&&loaded.state.tanks[0].fish[0].id===f.id);}
 const cache=new P.PixelCache(128,2);for(let i=0;i<10;i++){const c=document.createElement('canvas');c.width=c.height=4;cache.set(i,c);}ck('Pixel cache enforces both byte and entry bounds',cache.metrics.bytes<=128&&cache.metrics.entries<=2);
 ck('One scheduler owns at most one pending rAF or covered-view timer',AL.loop.stats.raf<=1&&AL.loop.stats.timer<=1&&AL.loop.stats.raf+AL.loop.stats.timer<=1);
 const meta=AL.FishAnimation.sheets.metrics;ck('Sprite caches respect declared byte and entry limits',meta.frameBytes<=meta.maxFrameBytes&&meta.decodedBytes<=meta.maxDecodedBytes&&meta.frameCache<=meta.maxFrames&&meta.loaded<=meta.maxDecodedSheets);
 ck('Freshwater remains locked',AL.Access?AL.Access.freshwaterUnlocked!==true:!document.querySelector('[data-new-water="fresh"]:not([disabled])'));
 s.settings.graphics.frameRate=60;AL.Shell.open('settings');ck('Settings exposes all five compact presentation controls', ['frameRate','graphicsQuality','waterEffects','decorativeParticles','backgroundSaving'].every(name=>document.querySelector('[name="'+name+'"]')));
 const form=document.querySelector('[data-form="settings"]');for(const [name,value] of Object.entries({frameRate:'30',graphicsQuality:'low',waterEffects:'low',decorativeParticles:'off'}))form.elements[name].value=value;form.requestSubmit();
 ck('Actual settings form persists all presentation choices locally',(()=>{const g=AL.Save.load().state.settings.graphics;return g.frameRate===30&&g.quality==='low'&&g.water==='low'&&g.particles==='off'&&g.backgroundSaving})());
 AL.Shell.close();AL.game.settings.graphics.frameRate=60;
 return checks;
})()
