"use strict";
AL.StoreRules=(()=>{
  const purchases=new Set(['buyMysteryCoral','buyMysteryBottom','buyInvertebrate','buyMysteryEgg','buyFish','buyEgg','buyFlora','buyEquipment','buyFood','buySupply','decorate','buyTank','buyRock','buySand','buyRack','buyMedicine']);
  function report(s,t,action,a={}){
    if(action==='buyTank'&&a.water==='fresh'||t?.water==='fresh'&&action!=='buyTank')return {ok:false,reasons:[AL.Update29?.lockText||'Freshwater — Coming in a Future Update.'],warnings:[]};
    if(action==='buyMysteryCoral'||action==='buyMysteryBottom')return AL.Update29.mysteryReport(s,t,action==='buyMysteryCoral'?'coral':'bottom',a);
    if(action==='buyInvertebrate')return AL.Invertebrates.report(s,t,a.species);if(action==='buyMysteryEgg')return AL.DailyStore.report(s,t);const reasons=[],warnings=[];if(!t)return {ok:false,reasons:['Choose an existing destination aquarium.'],warnings};
    if(action==='buyFish'||action==='buyEgg'){
      const d=AL.Data.species[a.species];if(!d)return {ok:false,reasons:['Species is not implemented.'],warnings};
      const added=action==='buyEgg'?1:Number(a.count??1),r=AL.Core.compatibility(s,t,d.id,added);reasons.push(...r.reasons);warnings.push(...r.warnings);
      if(a.market==='black'&&(s.level<4||!s.stats.nightMarket||!AL.Core.nightOpen(s)))reasons.push('Deep Market access and opening hours are required.');const w=t.waterParams;
      for(const [key,range] of [['temperature',d.temp],['ph',d.ph],['salinity',d.salinity]])if(w[key]<range[0]||w[key]>range[1])reasons.push(`${key==='ph'?'pH':key} is outside this species' safe purchase range.`);
      if(w.oxygen<5.5)reasons.push('Increase dissolved oxygen to at least 5.5 mg/L.');
      if(w.ammonia>.15||w.nitrite>.15)reasons.push('Lower ammonia and nitrite to 0.15 mg/L or less before purchase.');
      if(r.status==='High risk')reasons.push('Predatory tankmates make this destination unsafe. Choose a different aquarium.');
      if(t.eggs.some(e=>{const other=AL.Data.species[e.species];return d.predator>0&&other.size<d.size*.45||other.predator>0&&d.size<other.size*.45;}))reasons.push('Reserved offspring and this species would form an unsafe predatory combination.');
      if(d.purchaseVerified===false)reasons.push('This catalog entry is not offered until its care profile is verified.');
      if(d.clownfish){const residents=AL.Core.alive(t).filter(f=>AL.Data.species[f.species].clownfish),broods=t.eggs.filter(e=>AL.Data.species[e.species].clownfish);if(residents.some(f=>f.species!==d.id)||broods.some(e=>e.species!==d.id))reasons.push('Keep different clownfish species in separate established territories. Choose another aquarium.');if(residents.length+broods.reduce((n,e)=>n+e.count,0)+added>2)reasons.push('This aquarium supports one established clownfish pair, including reserved offspring. Choose another aquarium.');}
      if(s.level<d.level)reasons.push(`Requires keeper level ${d.level}.`);
      if(d.fictional&&(s.level<4||!s.stats.nightMarket||!AL.Core.nightOpen(s)))reasons.push(`Discover the night market at level 4 and shop between ${AL.Clock.format(1200)} and ${AL.Clock.format(240)}.`);
    }
    if(action==='buyFlora'){if(t.fish.some(f=>!f.dead&&f.species==='spotted-boxfish'))reasons.push('Do not place corals in the dedicated Spotted Boxfish home.');
      const d=AL.Data.flora[a.type];if(!d||d.water!==t.water)reasons.push('This organism needs a different water habitat.');
      if(!t.prepared)reasons.push('Prepare the water first.');
      if(d?.water==='marine'){
        if(s.level<(d.level||1))reasons.push('Requires keeper level '+d.level+'.');
        const w=t.waterParams,c=AL.Data.coralCare;
        if(t.kind!=='reef'||t.bacteria<.65||t.bacteria2<.5)reasons.push('Corals require a prepared, fully cycled reef aquarium.');
        if(w.ammonia>.15||w.nitrite>.15||w.oxygen<5.5||w.salinity<c.salinity[0]||w.salinity>c.salinity[1]||w.temperature<c.temperature[0]||w.temperature>c.temperature[1]||w.calcium<c.minCalcium||w.magnesium<c.minMagnesium||w.alkalinity<c.alkalinity[0]||w.alkalinity>c.alkalinity[1]||w.nitrate>c.maxNitrate)reasons.push('Correct the reef water conditions before introducing a living colony.');
        if(AL.Sim){const cond=AL.Sim.floraConditions(s,t,{type:a.type,x:.5,y:.9,size:1,hp:100});if(cond.dailyLight<d.light||cond.flow<d.flow)reasons.push('Install suitable lighting and flow before introducing this coral.');}
        if(!AL.Habitat.candidates(t,.5,AL.Habitat.bed(t),a.type).length&&!(t.hardscape?.length||t.mounts?.length))reasons.push('Provide a permitted mounting surface.');
      }
      if(d?.water==='marine'){const extra=AL.Expansion?.report(s,t,a.type);if(extra){reasons.push(...extra.reasons);warnings.push(...extra.warnings);}}if(t.flora.length>=Math.min(35,Math.floor(t.volume/8)))reasons.push('Leave room for existing colonies to grow.');
    }
    if(action==='buyMedicine'){const p=AL.Health.products[a.product];if(!p)reasons.push('Unknown medical product.');if(t.water!=='marine')reasons.push('Choose a marine destination; medicines go to medical inventory.');if(p?.restricted&&(s.level<4||!s.stats.nightMarket||!AL.Core.nightOpen(s)))reasons.push(`Restricted Treatments require unlocked night-market access, ${AL.Clock.format(1200)} to ${AL.Clock.format(240)}.`);if(p?.restricted&&AL.LivestockMarket.listing(s,'medicine:'+a.product)?.id!==a.listingId)reasons.push('Dealer batch changed; reopen details.');}
    if(action==='buyEquipment'&&a.heaterModel!==undefined){const m=AL.Heaters.get(a.heaterModel);if(!m||a.type!=='heater'||t.water!=='marine')reasons.push('Choose a valid marine heater.');else if(m.capacity+.000001<t.volume)reasons.push('This heater is too small for the selected aquarium. Choose a higher heater level or another aquarium.');}if(action==='buyEquipment'){const d=AL.Data.equipment[a.type];if(!d||d.water&&d.water!==t.water)reasons.push('Equipment is incompatible with this aquarium.');if(t.equipment.some(e=>e.type===a.type))reasons.push(a.heaterModel?'A heater is already installed. Use Equipment > Tank Care > Remove to inventory before fitting a different heater level.':'This equipment is already installed.');}
    if(['buyRock','buySand','buyRack','buyMedicine'].includes(action)&&t.water!=='marine')reasons.push('Choose a saltwater aquarium for this product.');
    if(action==='buySand'&&(!Number.isFinite(Number(a.depth))||Number(a.depth)<0||Number(a.depth)>5))reasons.push('Choose a substrate depth between 0 and 5 inches.');
    return {ok:!reasons.length,reasons:[...new Set(reasons)],warnings:[...new Set(warnings)]};
  }
  function enforce(s,t,action,args){if(!purchases.has(action))return;const r=report(s,t,action,args);if(!r.ok)throw Error(r.reasons.join(' '));}
  return {report,enforce,purchases};
})();
