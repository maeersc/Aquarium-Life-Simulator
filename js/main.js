"use strict";
(async () => {
  await Promise.all([AL.Art.ready,AL.AssetBank.ready,AL.LifeStages?.ready,AL.ClownArt?.ready,AL.ExpansionArt?.ready,AL.DivingArt?.ready]);
  const loaded=AL.Save.load();AL.game=loaded.state||AL.Core.newGame();AL.renderer=new AL.Renderer(document.getElementById('aquarium'));AL.UI.bind();AL.Store.bind();AL.Shell.bind();AL.CasinoUI.bind();AL.UI.render();
  AL.GameplayUI.bind();AL.DivingUI?.bind();AL.Update29UI?.bind();AL.Update31UI?.bind();AL.MortalityUI?.bind();AL.Startup.open(loaded);
  if(loaded.unavailable){document.getElementById('save-status').textContent='Browser storage unavailable — export JSON to save.';AL.UI.toast('This browser blocks local storage. Use Settings → Export JSON to preserve progress.',true);}
  const P=AL.Performance,clock=new P.SimClock(),pacer=new P.Pacer();
  let last=performance.now(),vitals=0,autosave=0,raf=0,timer=0,stopped=false,state=AL.game,returning=false,mode='';
  P.normalize(state.settings);pacer.reset(last);
  const diving=()=>!!AL.DivingUI?.opened;
  const visibleDive=()=>diving()&&AL.DivingUI.animating!==false;
  const covered=()=>AL.Startup.pending||AL.Offline.busy||!!document.querySelector('dialog[open]');
  function advance(now){const dt=Math.max(0,(now-last)/1000);last=now;const s=AL.game;
    if(state!==s){const restored=state.worldId!==s.worldId||state.simulationCheckpoint!==s.simulationCheckpoint||state.time!==s.time;state=s;if(restored){clock.pending=0;pacer.reset(now);return 0;}}
    const live=!!AL.Update31UI?.liveModal||!!AL.Shell?.active||AL.UI.modalOpen||AL.CasinoUI.opened,run=!AL.Startup.pending&&!AL.Offline.busy&&(diving()||live||s.settings.speed>0&&!AL.UI.placing);
    if(run)clock.add(dt*AL.Config.minutesPerSecond*(diving()?1:live?Math.max(1,s.settings.speed):s.settings.speed),s);
    return dt;
  }
  AL.Offline.setFlush(()=>{advance(performance.now());clock.flush(AL.game);});
  function cancel(){if(raf)cancelAnimationFrame(raf);if(timer)clearTimeout(timer);raf=timer=0;}
  function schedule(){if(stopped||document.hidden||returning||raf||timer)return;const p=AL.game.settings.graphics||P.normalize(AL.game.settings),next=visibleDive()?'diving':covered()?'covered':'tank';if(next!==mode){if(mode==='diving'&&next==='covered'&&diving())AL.DivingUI.draw();mode=next;pacer.reset(performance.now());}
    if(next==='covered')timer=setTimeout(tick,p.backgroundSaving?250:50);else raf=requestAnimationFrame(tick);
  }
  function tick(now){raf=timer=0;if(stopped||document.hidden||returning)return;const visualNow=Number.isFinite(now)?now:performance.now();now=performance.now();const dt=advance(now),s=AL.game,p=s.settings.graphics||P.normalize(s.settings);
    AL.DivingUI?.updateInput?.(now);
    if(visibleDive()||!covered()){const visualDt=pacer.take(visualNow,p.frameRate);if(visualDt!==null){if(diving())AL.DivingUI.draw();else AL.renderer.draw(s,visualDt);}}
    vitals+=dt;autosave+=dt;
    if(vitals>=1){if(AL.Store.opened&&document.getElementById('store-dialog').dataset.calendarDay!==String(s.dailyStore.day))AL.Store.render();const countdown=document.getElementById('rotation-countdown');if(countdown&&countdown.textContent!==AL.DailyStore.countdown(s))countdown.textContent=AL.DailyStore.countdown(s);AL.UI.updateVitals();AL.DivingUI?.update();AL.Update29UI?.update();AL.Update31UI?.update();AL.CasinoUI.update();AL.BreedingUI?.update();vitals%=1;}
    if(autosave>=AL.Config.autosaveSeconds){if(!AL.Startup.pending&&!AL.Save.locked)AL.UI.save();autosave%=AL.Config.autosaveSeconds;}
    schedule();
  }
  // Modal changes wake this scheduler, never create another full-scene loop.
  const observer=new MutationObserver(()=>{if(document.hidden||returning||stopped)return;cancel();schedule();});observer.observe(document.body,{subtree:true,attributes:true,attributeFilter:['open']});
  document.addEventListener('visibilitychange',async()=>{
    cancel();if(document.hidden){if(!AL.Save.locked&&!AL.Startup.pending){advance(performance.now());clock.flush(AL.game);AL.game.simulationCheckpoint=Math.max(AL.game.simulationCheckpoint,Date.now());AL.UI.save();}last=performance.now();return;}
    last=performance.now();pacer.reset(last);if(returning)return;returning=true;
    try{if(!AL.Save.locked&&!AL.Startup.pending)await AL.Offline.resume();}finally{returning=false;last=performance.now();pacer.reset(last);schedule();}
  });
  window.addEventListener('beforeunload',()=>{if(!AL.Save.locked)AL.UI.save();});
  AL.loop={start(){if(!stopped)return;stopped=false;last=performance.now();pacer.reset(last);schedule();},stop(){stopped=true;cancel();},dispose(){this.stop();observer.disconnect();},get stats(){return {raf:raf?1:0,timer:timer?1:0,mode,returning,pendingMinutes:clock.pending};}};
  schedule();
})();
