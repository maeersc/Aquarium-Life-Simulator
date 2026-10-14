"use strict";
(async () => {
  await Promise.all([AL.Art.ready,AL.AssetBank.ready,AL.LifeStages?.ready,AL.ClownArt?.ready,AL.ExpansionArt?.ready]);
  const loaded=AL.Save.load();AL.game=loaded.state||AL.Core.newGame();AL.renderer=new AL.Renderer(document.getElementById('aquarium'));AL.UI.bind();AL.Store.bind();AL.Shell.bind();AL.UI.render();
  AL.GameplayUI.bind();AL.Startup.open(loaded);
  if(loaded.unavailable){document.getElementById('save-status').textContent='Browser storage unavailable — export JSON to save.';AL.UI.toast('This browser blocks local storage. Use Settings → Export JSON to preserve progress.',true);}
  AL.Offline.setFlush(()=>{if(accumulator>0){AL.Sim.step(AL.game,Math.min(5,accumulator));accumulator=0;}});
  let last=performance.now(),accumulator=0,vitals=0,panels=0,autosave=0,drawBudget=0,renderCost=0,fpsCap=60;
  function frame(now){const dt=Math.min(.25,Math.max(0,(now-last)/1000));last=now;
    if(!document.hidden){const s=AL.game,t=AL.Core.selected(s),running=!AL.Startup.pending&&s.settings.speed>0&&(!AL.UI.modalOpen||AL.Store.opened&&!document.getElementById('dialog').open)&&!AL.UI.placing;
      if(running){accumulator+=dt*AL.Config.minutesPerSecond*s.settings.speed;while(accumulator>=AL.Config.stepMinutes){AL.Sim.step(s,AL.Config.stepMinutes);accumulator-=AL.Config.stepMinutes;}}
      drawBudget+=dt;const interval=s.settings.particles?1/fpsCap:1/30;if(drawBudget>=interval){const started=performance.now();AL.renderer.draw(s,drawBudget);renderCost=renderCost*.9+(performance.now()-started)*.1;if(renderCost>14)fpsCap=30;else if(renderCost<8)fpsCap=60;drawBudget=0;}
      vitals+=dt;panels+=dt;autosave+=dt;
      if(vitals>=1){if(AL.Store.opened&&document.getElementById('store-dialog').dataset.calendarDay!==String(AL.game.dailyStore.day))AL.Store.render();const timer=document.getElementById('rotation-countdown');if(timer)timer.textContent=AL.DailyStore.countdown(AL.game);AL.UI.updateVitals();vitals=0;}
      if(panels>=10&&!AL.UI.modalOpen&&!['INPUT','SELECT','TEXTAREA'].includes(document.activeElement.tagName)){AL.UI.render();panels=0;}
      if(autosave>=AL.Config.autosaveSeconds){if(!AL.Startup.pending&&!AL.Save.locked&&(!AL.UI.modalOpen||loaded.state))AL.UI.save();autosave=0;}
    }requestAnimationFrame(frame);
  }
  document.addEventListener('visibilitychange',()=>{last=performance.now();if(document.hidden&&!AL.Save.locked&&!AL.Startup.pending){if(accumulator>0){AL.Sim.step(AL.game,accumulator);accumulator=0;}AL.game.simulationCheckpoint=Date.now();AL.UI.save();}else if(!document.hidden&&!AL.Save.locked&&!AL.Startup.pending)AL.Offline.resume();});
  window.addEventListener('beforeunload',()=>{if(!AL.Save.locked)AL.UI.save();});requestAnimationFrame(frame);
})();
