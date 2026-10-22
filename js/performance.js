"use strict";
// Presentation policy only. No husbandry, rewards or authoritative clock changes.
AL.Performance=(()=>{
 function normalize(settings){const old=settings.graphics||{},one=(v,list,fallback)=>list.includes(v)?v:fallback;settings.graphics={frameRate:one(old.frameRate,[30,60],60),quality:one(old.quality,['low','medium','high'],'high'),water:one(old.water,['low','medium','high'],'high'),particles:one(old.particles,['off','low','full'],settings.particles===false?'off':'full'),backgroundSaving:old.backgroundSaving!==false};return settings.graphics;}
 class Pacer{
  reset(now){this.due=now;this.previous=now;this.fps=0;}
  take(now,fps=60){fps=fps===30?30:60;const interval=1000/fps;if(this.due===undefined||this.fps!==fps){this.due=now;this.previous=now;this.fps=fps;}
   // Retain fractional cadence on120/144/165/240Hz displays. Never replay old frames.
   if(now+.5<this.due)return null;const dt=Math.max(0,(now-this.previous)/1000);this.previous=now;this.due+=Math.max(1,Math.floor((now+.5-this.due)/interval)+1)*interval;return dt;
  }
 }
 class SimClock{
  constructor(){this.pending=0;}
  add(minutes,s,budget=8){this.pending+=Math.max(0,minutes);const end=performance.now()+budget;while(this.pending+1e-9>=AL.Config.stepMinutes){AL.Sim.step(s,AL.Config.stepMinutes);this.pending=Math.max(0,this.pending-AL.Config.stepMinutes);if(performance.now()>=end)break;}}
  flush(s){this.add(0,s,Infinity);const remaining=Math.round(this.pending*1e6)/1e6;if(remaining>0)AL.Sim.step(s,remaining);this.pending=0;}
 }
 class PixelCache{
  constructor(maxBytes,maxEntries=1024){this.maxBytes=maxBytes;this.maxEntries=maxEntries;this.items=new Map();this.bytes=0;this.hits=0;this.misses=0;this.evictions=0;}
  get(key){const image=this.items.get(key);if(!image){this.misses++;return null;}this.items.delete(key);this.items.set(key,image);this.hits++;return image;}
  set(key,image){if(this.items.has(key)){this.bytes-=this.items.get(key).width*this.items.get(key).height*4;this.items.delete(key);}const bytes=image.width*image.height*4;if(bytes>this.maxBytes)return image;while(this.items.size&&(this.items.size>=this.maxEntries||this.bytes+bytes>this.maxBytes)){const first=this.items.keys().next().value,old=this.items.get(first);this.items.delete(first);this.bytes-=old.width*old.height*4;this.evictions++;}this.items.set(key,image);this.bytes+=bytes;return image;}
  clear(){this.items.clear();this.bytes=0;}
  get metrics(){return {entries:this.items.size,bytes:this.bytes,maxBytes:this.maxBytes,maxEntries:this.maxEntries,hits:this.hits,misses:this.misses,evictions:this.evictions};}
 }
 const text=(id,value)=>{const n=document.getElementById(id);value=String(value);if(n&&n.textContent!==value)n.textContent=value;};
 const html=(id,value)=>{const n=document.getElementById(id);if(n&&n.innerHTML!==value)n.innerHTML=value;};
 function preferences(s){const p=normalize(s.settings),select=(name,label,values,current)=>`<label class="field">${label}<select name="${name}">${values.map(([id,title])=>`<option value="${id}" ${String(id)===String(current)?'selected':''}>${title}</option>`).join('')}</select></label>`;
  return `<fieldset class="performance-settings"><legend>Graphics &amp; Performance</legend>${select('frameRate','Frame Rate',[[30,'30 FPS — Performance Mode'],[60,'60 FPS — Default']],p.frameRate)}${select('graphicsQuality','Graphics Quality',[['low','Low'],['medium','Medium'],['high','High']],p.quality)}${select('waterEffects','Water Effects',[['low','Low'],['medium','Medium'],['high','High']],p.water)}${select('decorativeParticles','Decorative Particles',[['off','Off'],['low','Low'],['full','Full']],p.particles)}<label class="inline-check"><input name="backgroundSaving" type="checkbox" ${p.backgroundSaving?'checked':''}> Background Resource Saving</label><p>Graphics affect appearance only. Hidden tabs stop drawing and use offline progression when you return. Resource saving also reduces polling while management windows cover the tank.</p></fieldset>`;
 }
 return {normalize,Pacer,SimClock,PixelCache,text,html,preferences};
})();
