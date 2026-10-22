"use strict";
AL.StoreRules=(()=>{
  const purchases=new Set(['buyMysteryCoral','buyMysteryBottom','buyInvertebrate','buyMysteryEgg','buyFish','buyEgg','buyFlora','buyEquipment','buyFood','buySupply','decorate','buyTank','buyRock','buySand','buyRack','buyMedicine','buyBreedingPair','buyEquipmentPart']);
  // One quantity policy and quote, used by preview and the existing Core.act guard.
  function policy(action,a={}){
    if(['buyEquipment','buyFood','buyEquipmentPart','buyRock'].includes(action))return {bulk:true,reason:action==='buyRock'?'Multiple rocks go to Inventory; place each separately.':'Delivered to the existing inventory.'};
    if(action==='buySupply'&&!/^frag-(kit|cutters|saw)$/.test(a.type||''))return {bulk:true,reason:'Packs add their existing number of doses to shared inventory.'};
    if(action==='buyMedicine'&&AL.Health.products[a.product]&&!AL.Health.products[a.product].restricted)return {bulk:true,reason:'Packs add course or examination units to medical inventory.'};
    return {bulk:false,reason:action==='buyFish'?'Use the resident count below; each fish still requires a safe destination.':action==='buySupply'?'Reusable tools are purchased individually.':action==='buySand'?'One substrate installation at the chosen depth.':action==='buyMedicine'?'Each restricted dealer batch has individual saved quality and stock.':['buyRock','decorate','buyRack'].includes(action)?'Place or mount one object at a time.':'One living specimen, brood, mystery item or pair offer per assessment; existing safety and rarity rules apply.'};
  }
  function quantity(action,a={}){const n=a.quantity===undefined?1:a.quantity,p=policy(action,a);if(!Number.isSafeInteger(n)||n<1||n>99)throw Error('Quantity must be a whole number from 1 to 99.');if(!p.bulk&&n!==1)throw Error(p.reason);return n;}
  function quote(s,t,action,a={}){
    const reasons=[];let n;try{n=quantity(action,a);}catch(e){return {ok:false,reasons:[e.message],quantity:a.quantity,unitPrice:null,total:null,max:1};}
    let unitPrice=null,available=Infinity,room=Infinity;const D=AL.Data;
    if(action==='buyEquipment'){const d=D.equipment[a.type],m=a.heaterModel!==undefined?AL.Heaters.get(a.heaterModel):null;unitPrice=d&&t?(m?.price??Math.ceil(d.price*Math.max(1,t.volume/d.capacity))):null;available=s.stock[a.type]??0;room=50-(s.ownedEquipment||[]).length;}
    if(action==='buyFood'||action==='buySupply'){const d=(action==='buyFood'?D.foods:D.supplies)[a.type];unitPrice=d?.price??null;available=s.stock[a.type]??0;room=d?Math.floor((1e7-(s.inventory[a.type]||0))/(action==='buyFood'?20:d.amount)):0;if(action==='buySupply'&&/^frag-(kit|cutters|saw)$/.test(a.type||'')&&s.inventory[a.type]>0)reasons.push('Reusable tool already owned.');}
    if(action==='buyMedicine'){const p=AL.Health.products[a.product];unitPrice=p?.restricted?AL.LivestockMarket.listing(s,'medicine:'+a.product)?.price:p?.price;available=s.medicineStock[a.product]??0;if(p?.restricted){available=Math.min(available,AL.LivestockMarket.listing(s,'medicine:'+a.product)?.remaining??0);room=80-s.medicalInventory.length;}if(p&&!p.restricted){const merge=s.medicalInventory.filter(b=>b.product===a.product).reduce((v,b)=>v+1000-b.quantity,0);room=Math.floor((merge+(80-s.medicalInventory.length)*1000)/p.doses);}}
    if(action==='buyEquipmentPart'){try{const p=AL.EquipmentParts.product(a.sku,a.rating);unitPrice=p.price;available=s.equipmentParts.stock[a.sku]??0;room=10000-(s.equipmentParts.inventory[p.id]||0);}catch(e){reasons.push(e.message);}}
    if(action==='buyRock'){const p=AL.Habitat.rockProducts[a.group];unitPrice=p&&Number.isInteger(a.variant)&&a.variant>=0&&a.variant<=3?p.price+a.variant*25:null;available=s.stock['rock:'+a.group+':'+a.variant]??0;room=n>1?100-(s.ownedObjects||[]).length:20-(t?.hardscape||[]).length;}
    if(n>available)reasons.push('Requested '+n+'; only '+available+' in stock.');if(n>room)reasons.push('Requested '+n+'; inventory or placement capacity is '+Math.max(0,room)+'.');
    const total=Number.isSafeInteger(unitPrice)?unitPrice*n:null;if(policy(action,a).bulk&&(!Number.isSafeInteger(total)||total<0))reasons.push('Reopen details for a valid current price.');if(total!==null&&s.credits<total)reasons.push('Total '+total+' AC; wallet '+s.credits+' AC.');
    return {ok:!reasons.length,reasons,quantity:n,unitPrice,total,max:Math.max(0,Math.min(policy(action,a).bulk?99:1,available,room))};
  }
  function report(s,t,action,a={}){const r=baseReport(s,t,action,a);if(!purchases.has(action))return r;const q=quote(s,t,action,a);return {...r,ok:r.ok&&q.ok,reasons:[...new Set([...r.reasons,...q.reasons])]};}
  function baseReport(s,t,action,a={}){
    if(action==='buyTank')return {ok:a.water==='marine',reasons:a.water==='marine'?[]:[AL.Update29.lockText],warnings:[]};
    if(action==='buyBreedingPair')return AL.PairOffers.report(s,t,s.pairOffers.offers[a.offerId]);
    if(action==='buyEquipmentPart')return {ok:t?.water!=='fresh',reasons:t?.water==='fresh'?[AL.Update29.lockText]:[],warnings:['The rated new part is delivered to Inventory.']};
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
      if(t.eggs.filter(e=>t.water!=='marine'||e.viability>0).some(e=>{const other=AL.Data.species[e.species];return d.predator>0&&other.size<d.size*.45||other.predator>0&&d.size<other.size*.45;}))reasons.push('Reserved offspring and this species would form an unsafe predatory combination.');
      if(d.purchaseVerified===false)reasons.push('This catalog entry is not offered until its care profile is verified.');
      if(d.clownfish){const residents=AL.Core.alive(t).filter(f=>AL.Data.species[f.species].clownfish),broods=t.eggs.filter(e=>e.viability>0&&AL.Data.species[e.species].clownfish);if(residents.some(f=>f.species!==d.id)||broods.some(e=>e.species!==d.id))reasons.push('Keep different clownfish species in separate established territories. Choose another aquarium.');if(residents.length+broods.reduce((n,e)=>n+e.count,0)+added>2)reasons.push('This aquarium supports one established clownfish pair, including reserved offspring. Choose another aquarium.');}
      if(s.level<d.level)reasons.push(`Requires keeper level ${d.level}.`);
      if(d.fictional&&(s.level<4||!s.stats.nightMarket||!AL.Core.nightOpen(s)))reasons.push(`Discover the night market at level 4 and shop between ${AL.Clock.format(1200)} and ${AL.Clock.format(240)}.`);
    }
    if(action==='buyFlora'){if(t.fish.some(f=>!f.dead&&f.species==='spotted-boxfish'))reasons.push('Do not place corals in the dedicated Spotted Boxfish home.');
      const d=AL.Data.flora[a.type];if(!d||d.water!==t.water)reasons.push('This organism needs a different water habitat.');
      if(!AL.Preparation.prepared(t))reasons.push('Prepare the water first.');
      if(d?.water==='marine'){
        if(s.level<(d.level||1))reasons.push('Requires keeper level '+d.level+'.');
        const w=t.waterParams,c=AL.Data.coralCare;
        if((t.kind!=='reef'&&!(a.receiving===true&&t.kind==='quarantine'&&!AL.Core.alive(t).length&&!(t.invertebrates||[]).some(f=>!f.dead&&f.hp>0)&&!t.eggs.some(e=>e.viability>0)&&!(t.nurseries||[]).some(n=>!n.dead&&n.hp>0)))||t.bacteria<.65||t.bacteria2<.5)reasons.push('Corals require a prepared, fully cycled reef aquarium.');
        if(w.ammonia>.15||w.nitrite>.15||w.oxygen<5.5||w.salinity<c.salinity[0]||w.salinity>c.salinity[1]||w.temperature<c.temperature[0]||w.temperature>c.temperature[1]||w.calcium<c.minCalcium||w.magnesium<c.minMagnesium||w.alkalinity<c.alkalinity[0]||w.alkalinity>c.alkalinity[1]||w.nitrate>c.maxNitrate)reasons.push('Correct the reef water conditions before introducing a living colony.');
        if(AL.Sim){const cond=AL.Sim.floraConditions(s,t,{type:a.type,x:.5,y:.9,size:1,hp:100});if(cond.dailyLight<d.light||cond.flow<d.flow)reasons.push('Install suitable lighting and flow before introducing this coral.');}
        if(!AL.Habitat.candidates(t,.5,AL.Habitat.bed(t),a.type).length&&!(t.hardscape?.length||t.mounts?.length))reasons.push('Provide a permitted mounting surface.');
      }
      if(d?.water==='marine'){const extra=AL.Expansion?.report(s,t,a.type);if(extra){reasons.push(...extra.reasons);warnings.push(...extra.warnings);}}if(t.flora.length>=Math.min(35,Math.floor(t.volume/8)))reasons.push('Leave room for existing colonies to grow.');
    }
    if(action==='buyMedicine'){const p=AL.Health.products[a.product];if(!p)reasons.push('Unknown medical product.');if(t.water!=='marine')reasons.push('Choose a marine destination; medicines go to medical inventory.');if(p?.restricted&&(s.level<4||!s.stats.nightMarket||!AL.Core.nightOpen(s)))reasons.push(`Restricted Treatments require unlocked night-market access, ${AL.Clock.format(1200)} to ${AL.Clock.format(240)}.`);if(p?.restricted&&AL.LivestockMarket.listing(s,'medicine:'+a.product)?.id!==a.listingId)reasons.push('Dealer batch changed; reopen details.');}
    if(action==='buyEquipment'){const d=AL.Data.equipment[a.type],m=a.heaterModel!==undefined?AL.Heaters.get(a.heaterModel):null;if(!d||d.water&&d.water!==t.water)reasons.push('Equipment is incompatible with the sizing aquarium.');if(a.heaterModel!==undefined&&(!m||a.type!=='heater'))reasons.push('Choose a valid heater model.');if((s.ownedEquipment||[]).length>=50)reasons.push('Equipment storage is full (50 items).');warnings.push('Purchased into Inventory; install separately. The chosen aquarium sizes standard equipment; fixed heater models keep their listed rating.');}
    if(['buyRock','buySand','buyRack','buyMedicine'].includes(action)&&t.water!=='marine')reasons.push('Choose a saltwater aquarium for this product.');
    if(action==='buySand'&&(!Number.isFinite(Number(a.depth))||Number(a.depth)<0||Number(a.depth)>5))reasons.push('Choose a substrate depth between 0 and 5 inches.');
    return {ok:!reasons.length,reasons:[...new Set(reasons)],warnings:[...new Set(warnings)]};
  }
  function enforce(s,t,action,args){if(!purchases.has(action))return;const r=report(s,t,action,args);if(!r.ok)throw Error(r.reasons.join(' '));}
  return {report,enforce,purchases,policy,quantity,quote};
})();
