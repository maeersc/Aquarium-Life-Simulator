"use strict";
AL.Sim = (() => {
  const K=AL.Core,D=AL.Data,clamp=K.clamp;
  const outside=(v,r)=>Math.max(r[0]-v,0,v-r[1]);
  function lightPower(t){if(t.water!=='marine')return K.has(t,'reefLight')?1.5:K.has(t,'light')?1:0;return Math.max(0,...t.equipment.filter(e=>['light','reefLight'].includes(e.type)).map(e=>(e.type==='reefLight'?1.5:1)*AL.EquipmentReliability.efficiency(e,t)));}
  function light(s,t){
    const mode=t.lightMode||'auto';
    if(mode==='off')return 0;
    const intensity=t.lightIntensity*lightPower(t);
    if(mode==='on')return intensity;
    const h=s.time/60%24,start=12-t.lightHours/2,end=12+t.lightHours/2;
    return clamp(Math.min((h-start)*2,(end-h)*2),0,1)*intensity;
  }
  function water(s,t,h){
    const w=t.waterParams,live=K.alive(t),filter=K.capacity(t,'filter')/t.volume;
    if(t.water!=='marine')for(const e of t.equipment){if(!e.enabled||e.durability<=0||(t.lightMode==='off'&&['light','reefLight'].includes(e.type)))continue;const before=e.durability;e.durability=clamp(e.durability-h*0.018*(1+t.volume/e.capacity*0.15),0,100);if(before>0&&e.durability===0){AL.Mortality?.event?.(s,t,'equipmentFailure',{equipmentType:e.type});K.log(s,`${t.name}: ${D.equipment[e.type].name} failed from wear. Service it now.`,'danger');}}
    const room=22,thermal=Math.min(1,h*0.09*Math.sqrt(75/t.volume));
    const heater=K.capacity(t,'heater')/t.volume,chiller=K.capacity(t,'chiller')/t.volume;
    let target=room+light(s,t)*0.4;
    if(heater&&t.temperatureTarget>target)target=Math.min(t.temperatureTarget,target+heater*8);
    if(chiller&&t.temperatureTarget<target)target=Math.max(t.temperatureTarget,target-chiller*8);
    if(t.water==='marine')AL.Thermal.step(s,t,h);else w.temperature+=(target-w.temperature)*thermal;
    if(!AL.Preparation.prepared(t))return;
    const waste=live.reduce((n,f)=>n+D.species[f.species].load*(0.2+f.growth*0.8),0)*0.0025*75/t.volume;
    w.organic+=h*(waste+t.fish.filter(f=>f.dead).length*0.06*75/t.volume);
    if(K.has(t,'skimmer'))w.organic*=Math.exp(-h*0.12*Math.min(2,K.capacity(t,'skimmer')/t.volume));
    const decomposed=w.organic*(1-Math.exp(-h*0.12));w.organic-=decomposed;w.ammonia+=decomposed;
    if(t.cycleActive&&filter>0){t.cycle+=h;t.bacteria=clamp(t.bacteria+h/AL.Config.cycleHours,0,1);t.bacteria2=clamp(t.bacteria2+h/AL.Config.cycleHours,0,1);if(t.cycle>=AL.Config.cycleHours){t.cycleActive=false;t.bacteria=1;t.bacteria2=1;w.ammonia=0.04;w.nitrite=0.03;w.nitrate+=4;s.stats.cycled++;if(t.water==='marine')AL.Preparation.record(s,t,'cycled','Fishless cycling completed through the existing simulation.');K.log(s,`${t.name}: biological cycling is complete. Check stocking compatibility before adding residents.`);}}
    else if(filter>0&&w.oxygen>4){t.bacteria=clamp(t.bacteria+h*0.008*w.ammonia,0,1);t.bacteria2=clamp(t.bacteria2+h*0.008*w.nitrite,0,1);}
    else{t.bacteria=Math.max(0.005,t.bacteria-h*0.002);t.bacteria2=Math.max(0.005,t.bacteria2-h*0.002);}
    // Sequential conversions conserve the simplified nitrogen quantity.
    const oxidized=Math.min(w.ammonia,h*0.55*t.bacteria*filter*clamp(w.oxygen/5,0,1));w.ammonia-=oxidized;w.nitrite+=oxidized;
    const nitrated=Math.min(w.nitrite,h*0.5*t.bacteria2*filter*clamp(w.oxygen/5,0,1));w.nitrite-=nitrated;w.nitrate+=nitrated;
    const plants=t.flora.filter(f=>D.flora[f.type].water==='fresh'&&f.hp>0).reduce((n,f)=>n+f.size,0);
    const illumination=light(s,t);w.nitrate=Math.max(0,w.nitrate-h*plants*0.028*illumination);w.phosphate=Math.max(0,w.phosphate+h*waste*0.01-h*plants*0.0002*illumination);
    const aeration=t.water==='marine'?.35+.5*Math.min(1,K.capacity(t,'air')/t.volume)+.15*Math.min(1,K.capacity(t,'flow')/t.volume):0.35+(K.has(t,'air')?0.5:0)+(K.has(t,'flow')?0.15:0);
    const saturation=8.4-(w.temperature-22)*0.14-(t.water==='marine'?0.6:0);
    const respiration=K.load(t)/t.volume*0.6+plants*0.004+(oxidized+nitrated)*0.15/h;
    w.oxygen=clamp(w.oxygen+h*(aeration*(saturation-w.oxygen)-respiration+plants*0.02*illumination),0,12);
    w.ph=clamp(w.ph-h*0.00025*w.organic/Math.max(1,w.kh),4,10);
    w.clarity=clamp(100-w.organic*14-w.nitrate*0.2,15,100);
    if(K.has(t,'dosing')&&s.inventory.buffer>0&&(w.calcium<390||w.alkalinity<7)){s.inventory.buffer--;w.calcium=Math.min(440,w.calcium+35);w.magnesium=Math.min(1350,w.magnesium+45);w.alkalinity=Math.min(9,w.alkalinity+1);}
    const safe=w.ammonia<0.25&&w.nitrite<0.25&&w.nitrate<40&&w.oxygen>5&&w.temperature>=22&&w.temperature<=28&&live.length>0;
    t.safeHours=safe?t.safeHours+h:0;t.peaceHours=safe&&live.length>=6&&live.every(f=>f.hp>80&&f.stress<25)?t.peaceHours+h:0;
  }
  function food(s,t,h){
    for(const p of t.food){p.age+=h;p.y=clamp(p.y+h*0.5,0.08,0.94);const candidates=K.alive(t).filter(f=>(!p.targetId||p.targetId===f.id)&&(t.water==='marine'?AL.MarineCare.profile(f).foods.includes(p.type):(f.growth<0.3?p.type==='fry':D.species[f.species].diet.includes(p.type)))&&f.hunger>8).sort((a,b)=>b.hunger-a.hunger);
      if(candidates.length){const f=candidates[0];const distance=Math.hypot(f.x-p.x,(f.y-p.y)*0.5);if(distance<0.25||p.age>0.5){f.hunger=clamp(f.hunger-p.nutrition,0,100);f.energy=clamp(f.energy+4,0,100);f.behavior='Eat';AL.Health?.fed(f,D.foods[p.type].quality);AL.Mortality?.fed?.(s,t,f,p.type,p.nutrition);p.eaten=true;s.stats.fed++;}}
      if(!p.eaten&&p.age>2){t.waterParams.organic+=D.foods[p.type].pollution*0.12*75/t.volume;p.eaten=true;}
    }t.food=t.food.filter(p=>!p.eaten);
  }
  function fishHealth(s,t,h){
    const w=t.waterParams,living=K.alive(t);
    for(const f of t.fish){if(f.dead){f.deadHours+=h;continue;}if(D.species[f.species].water==='marine'&&f.hp<=0){K.kill(s,t,f,f.deathCause||'Cause of death undetermined.');continue;}const d=D.species[f.species];
      f.age+=h/24;f.growth=clamp(f.age/d.maturity,0.08,1);f.hunger=clamp(f.hunger+h*(d.water==='marine'?AL.MarineCare.profile(f).hungerPerHour:(f.growth<0.3?2.4:1.25)),0,100);f.attackCooldown=Math.max(0,f.attackCooldown-h);
      if(!f.raised&&!f.bought&&f.growth>=0.3){f.raised=true;s.stats.raised++;K.log(s,`${f.name} has grown into a juvenile.`);}
      const school=living.filter(n=>n.species===f.species).length;
      const shelter=t.flora.filter(n=>n.hp>0).length+t.decorations.length;
      const toxins=w.ammonia*(0.7+Math.pow(10,clamp(w.ph-7,0,2))*0.08)+w.nitrite*1.5+Math.max(0,w.nitrate-40)*0.012;
      const thermal=outside(w.temperature,d.temp),salt=outside(w.salinity,d.salinity),oxygen=Math.max(0,5-w.oxygen);
      const social=school<d.group?12:0;
      const stressTarget=clamp(toxins*22+thermal*12+salt*10+oxygen*15+outside(w.ph,d.ph)*18+social+(shelter===0?8:0)+Math.max(0,f.hunger-65)*0.7+(d.id==='voidfin'&&light(s,t)>0.4?35:0),0,100);
      f.stress=clamp(f.stress+(stressTarget-f.stress)*Math.min(1,h*0.15),0,100);f.happiness=clamp(100-f.stress*0.65-f.hunger*0.2-(100-f.hp)*0.3,0,100);
      let damage=toxins*1.5+thermal*0.8+salt*0.8+oxygen*1.5+(d.water==='marine'?AL.MarineCare.starving(f):Math.max(0,f.hunger-85)*0.16)+Math.max(0,f.stress-65)*0.03;
      if(f.disease&&(d.water==='fresh'||!AL.Health))damage+=0.7;
      if((d.water==='fresh'||!AL.Health)&&f.stress>45&&!f.disease&&K.random(s)<h*0.008*(1-f.immune)){f.disease='Stress infection';K.log(s,`${f.name} developed a stress-related infection. Improve conditions and consider treatment.`,'warning');}
      if(d.water==='marine'){for(const [cause,value]of [['Ammonia toxicity',w.ammonia*(.7+Math.pow(10,clamp(w.ph-7,0,2))*.08)*1.5],['Nitrite toxicity',w.nitrite*2.25],['Nitrate toxicity',Math.max(0,w.nitrate-40)*.018],['Extreme temperature',thermal*.8],['Salinity shock',salt*.8],['Oxygen deprivation',oxygen*1.5],['Prolonged severe malnutrition',AL.MarineCare.starving(f)],['Sustained severe stress',Math.max(0,f.stress-65)*.03]])if(damage>.15)AL.Mortality.note(s,t,f,cause,value*h);}
      f.hp=clamp(f.hp+h*(damage>0.15?-damage:f.hunger<65&&f.stress<25?0.8:0),0,100);
      const night=light(s,t)<0.1,rest=d.nocturnal?!night:night;f.energy=clamp(f.energy+h*(rest?3:-1.2),5,100);
      if(f.hp<=0){const causes=[[toxins*1.5,'Water toxicity'],[thermal*0.8,'Extreme temperature'],[salt*0.8,'Salinity shock'],[oxygen*1.5,'Oxygen deprivation'],[Math.max(0,f.hunger-85)*0.16,'Starvation'],[f.disease?0.7:0,'Disease']];causes.sort((a,b)=>b[0]-a[0]);K.kill(s,t,f,d.water==='marine'?AL.Mortality.cause(s,t,f,causes[0][1]):causes[0][1]);}
      else if(f.age>=f.maxLifespan||(f.age>f.lifeExpectancy&&K.random(s)<h/24*0.0005*Math.pow(f.age/f.lifeExpectancy,3)))K.kill(s,t,f,'Old age');
    }
    // Encounters are probabilistic, cooldown-bound, and allow shelter to reduce risk.
    const cover=1+t.flora.length*0.35+t.decorations.length*0.4;
    for(const f of living){if(f.dead||f.attackCooldown>0)continue;const d=D.species[f.species];if(d.aggression<0.35&&d.predator===0)continue;
      const victim=living.find(n=>n!==f&&!n.dead&&Math.abs(n.x-f.x)<0.17&&Math.abs(n.y-f.y)<0.25);if(!victim)continue;
      const preySize=victim.adultSize*victim.growth;
      if(d.predator>0&&f.hunger>55&&preySize<f.adultSize*f.growth*0.45&&K.random(s)<h*d.predator*0.18/cover){K.kill(s,t,victim,'Predation');f.hunger=Math.max(0,f.hunger-35);f.behavior='Hunt';f.attackCooldown=12;}
      else if((f.stress>30||f.hunger>60||victim.species===f.species)&&K.random(s)<h*f.aggression*0.1/cover){AL.Mortality?.note(s,t,victim,'Aggressive tankmate',4+f.aggression*4);victim.hp=clamp(victim.hp-4-f.aggression*4,0,100);victim.stress=clamp(victim.stress+12,0,100);victim.behavior='Flee';victim.targetX=f.x>0.5?0.1:0.9;f.behavior='Chase';f.attackCooldown=6;if(victim.hp===0)K.kill(s,t,victim,'Aggressive tankmate');else K.log(s,`${f.name} chased ${victim.name}. Add cover or separate territorial fish.`,'warning');}
    }
  }
  function floraConditions(s,t,f){
    const d=D.flora[f.type],w=t.waterParams,c=D.coralCare;
    const hours=t.lightMode==='off'?0:t.lightMode==='on'?24:t.lightHours;
    const dailyLight=t.lightIntensity*lightPower(t)*hours/10;
    const flow=K.has(t,'flow')?Math.min(1,K.capacity(t,'flow')/t.volume):0.15;
    const stinging=d.water==='marine'&&t.flora.some(n=>n!==f&&n.id!==f.id&&n.hp>0&&D.flora[n.type].shape==='lps'&&Math.hypot(n.x-f.x,((n.y??0.92)-(f.y??0.92))*0.5)<c.stingDistance);
    const issues=[];let stress=Math.max(0,d.light-dailyLight)*4+(hours>12?0.2:0);
    if(dailyLight<d.light)issues.push('Not enough daily light. Increase intensity, schedule duration or upgrade the lamp.');
    if(hours>12)issues.push('The light period is long. Auto allows a regular dark period.');
    if(d.water==='marine'){
      stress+=outside(w.salinity,c.salinity)*3+outside(w.temperature,c.temperature)*2+Math.max(0,w.nitrate-c.maxNitrate)*0.15+w.ammonia*8+Math.max(0,c.minCalcium-w.calcium)*0.03+Math.max(0,c.minMagnesium-w.magnesium)*0.005+outside(w.alkalinity,c.alkalinity)+Math.max(0,d.flow-flow)*3+(stinging?0.6:0);
      if(outside(w.temperature,c.temperature))issues.push('Temperature is outside the preferred range.');
      if(outside(w.salinity,c.salinity))issues.push('Salinity is outside the preferred range.');
      if(w.ammonia>0.02||w.nitrate>c.maxNitrate)issues.push('Water pollutants are stressing this colony.');
      if(w.calcium<c.minCalcium||w.magnesium<c.minMagnesium||outside(w.alkalinity,c.alkalinity))issues.push('Reef minerals need attention.');
      if(flow<d.flow)issues.push('Increase circulation to meet this coral’s flow requirement.');
      if(stinging)issues.push('A nearby LPS colony can sting this organism. Give it more space.');
    }
    return {hours,dailyLight,flow,stinging,stress,issues};
  }
  function ecosystems(s,t,h){const w=t.waterParams,l=light(s,t);
    for(const f of t.flora){if(f.hp<=0)continue;const d=D.flora[f.type];f.age+=h/24;
      // Inspection and simulation use the same care conditions and 2D spacing.
      const {stress}=floraConditions(s,t,f);
      if(d.water==='marine'){w.calcium=Math.max(0,w.calcium-h*f.size*0.09*(75/t.volume)*(d.stony||['sps','lps'].includes(f.type)?1:0));w.magnesium=Math.max(0,w.magnesium-h*f.size*0.01*(75/t.volume)*(d.stony||['sps','lps'].includes(f.type)?1:0));w.alkalinity=Math.max(0,w.alkalinity-h*f.size*0.0008*(75/t.volume)*(d.stony||['sps','lps'].includes(f.type)?1:0));}
      if(d.water==='marine'&&stress>.15)AL.Mortality.note(s,t,f,'Sustained coral environmental stress',h*stress);f.hp=clamp(f.hp+h*(stress>0.15?-stress:d.water==='marine'&&(f.healthState?.nutrition<30||d.nonPhotosynthetic&&(f.coralHunger??20)>65)?0:0.4),0,100);f.color=clamp(f.hp/100,0.3,1);
      if(f.hp>70&&l>0.1){const nutrient=d.water==='fresh'?clamp(w.nitrate/3,0.1,1):clamp((w.nitrate+w.phosphate*10)/3,0.15,1);f.size=clamp(f.size+h*d.growth*0.15*nutrient,0.2,2.5);}
      if(f.hp===0&&d.water==='marine')AL.Update29?.death(s,t,f);if(f.hp===0)K.log(s,`${d.name} died in ${t.name}. Check light, water and space.`,'warning');
    }
  }
  function breedingReady(s,t,species){if(t.water==='marine'&&AL.Breeding)return AL.Breeding.ready(s,t,species);const d=D.species[species];if(!d)return {ok:false,reason:'Unknown species.'};if(d.breedingSupported===false)return {ok:false,reason:d.breedingStatus};if(species==='betta')return {ok:false,reason:'Specialist betta spawning is not modeled in this slice.'};const parents=K.alive(t).filter(f=>f.species===species&&f.age>=d.maturity&&f.hp>=85&&f.hunger<=40&&f.stress<25&&s.time-f.lastBreed>=d.breedCooldown*60);
    const female=parents.find(f=>f.sex==='F'),male=parents.find(f=>f.sex==='M');if(d.water==='marine'&&parents.some(f=>f.healthState?.treatment||f.healthState?.conditions.some(c=>c.severity>.15)))return {ok:false,reason:'Resolve illness and treatment before breeding.'};if(!female||!male)return {ok:false,reason:'Needs a mature male and female, each ≥85 HP, ≤40 hunger, <25 stress, outside the breeding cooldown.'};
    const geneticHold=AL.Patterns?.ready(female,male);if(geneticHold)return {ok:false,reason:geneticHold};const w=t.waterParams;if(w.ammonia>0.15||w.nitrite>0.15||w.oxygen<6||outside(w.temperature,d.temp)||outside(w.ph,d.ph)||outside(w.salinity,d.salinity))return {ok:false,reason:'Water must be within species ranges, with low toxins and oxygen ≥6 mg/L.'};
    if(t.flora.length+t.decorations.length<1)return {ok:false,reason:'Add live plants, coral or a shelter before courtship.'};
    if(t.eggs.length>=20||t.fish.length+d.brood>AL.Config.maxFish)return {ok:false,reason:'No incubation space remains.'};
    if(t.fish.reduce((n,f)=>n+(f.dead?0:D.species[f.species].load),0)+t.eggs.filter(e=>t.water!=='marine'||e.viability>0).reduce((n,e)=>n+D.species[e.species].load*e.count,0)+d.brood*d.load>K.loadLimit(t))return {ok:false,reason:'Reserve enough adult stocking space for the offspring.'};
    return {ok:true,female,male,reason:'A healthy pair is ready to breed.'};
  }
  function makeBrood(s,t,species,a,b,purchased=false){const d=D.species[species],genes={};for(const key of ['color','size','longevity','immunity','fertility'])genes[key]=clamp(a&&b?(a.genes[key]+b.genes[key])/2+(K.random(s)-0.5)*0.08:0.9+K.random(s)*0.2,0.8,1.2);
    t.eggs.push({id:K.id(s,'brood'),aquariumId:t.id,species,strategy:d.reproduction,parents:a&&b?[a.id,b.id]:[],genes,generation:a&&b?Math.max(a.generation,b.generation)+1:1,progress:0,required:d.incubation,viability:100,fertilized:true,count:purchased?1:d.brood,age:0,purchased});AL.Patterns?.embryos(s,t.eggs.at(-1),a,b);if(t.water==='marine')AL.BroodView?.initialize(t,t.eggs.at(-1));s.stats.broods++;K.log(s,`${d.name}: ${d.reproduction==='livebearer'?'gestation':d.reproduction==='mouthbrood'?'mouthbrooding':'egg incubation'} has begun.`);
  }
  function breed(s,t,species){if(t.water==='marine')throw Error('Marine courtship happens autonomously. Observe breeding in the Field Journal.');const r=breedingReady(s,t,species);if(!r.ok)throw Error(r.reason);r.female.lastBreed=s.time;r.male.lastBreed=s.time;r.female.behavior='Court';r.male.behavior='Court';makeBrood(s,t,species,r.female,r.male);}
  function eggs(s,t,h){for(const e of t.eggs){const d=D.species[e.species],w=t.waterParams;if(e.naturalBreeding){if(e.spawnedAt<s.time)AL.Breeding.incubate(s,t,e,h);continue;}if(t.water==='marine'&&AL.BroodView?.failed(s,t,e))continue;e.age+=h;const suitable=(!e.diveHidden||AL.DiveExpansion.incubationSafe(s,t,e))&&outside(w.temperature,d.temp)===0&&outside(w.salinity,d.salinity)===0&&outside(w.ph,d.ph)===0&&w.oxygen>=5.5&&w.ammonia<0.25&&w.nitrite<0.25;const protectedBrood=['livebearer','mouthbrood'].includes(e.strategy);const carrier=e.parents[0];if(protectedBrood&&carrier&&!K.alive(t).some(f=>f.id===(e.strategy==='mouthbrood'?e.parents[1]:carrier)))e.viability=0;
      if(suitable)e.progress+=h*clamp((w.temperature-d.temp[0]+2)/4,0.5,1.3);else e.viability=clamp(e.viability-h*2,0,100);
      if(e.viability<=0){if(e.diveHidden)AL.DiveExpansion.failedEgg(s,e);if(t.water==='marine'&&AL.BroodView?.failed(s,t,e)){}else{e.done=true;t.waterParams.organic+=0.1;K.log(s,`${d.name} brood failed under unsuitable conditions.`,'warning');}}
      else if(e.progress>=e.required){const free=AL.Config.maxFish-t.fish.length;const candidates=Array.from({length:e.count},(_,i)=>i).filter(i=>e.embryos?.[i]?.viable!==false);const number=candidates.length?Math.min(free,Math.max(1,Math.floor(candidates.length*e.viability/100))):0;let hatched=0;for(let j=0;j<number;j++){const i=candidates[j];hatched++;const f=K.fish(s,e.species,{age:1,genes:{...e.genes},parents:e.parents,generation:e.generation,bought:false});f.name=`${d.name} fry`;if(d.water==='marine')f.provenance=e.provenance?{...e.provenance}:{source:e.mystery?'mystery-egg':'captive-bred',acquired:s.time};f.hunger=20;AL.Patterns?.inherit(f,e,i);if(e.diveHidden)AL.DiveExpansion.hatched(s,t,e,f);t.fish.push(f);}s.stats.hatched+=hatched;K.discover(s,e.species);e.done=true;K.log(s,`${hatched} ${d.name} offspring arrived. Feed fine fry food and provide shelter.`);}
    }t.eggs=t.eggs.filter(e=>!e.done);
  }
  function daily(s,day){s.market.day=day;s.market.budget=AL.Config.dayBuyerBudget;s.market.sales=0;for(const key of Object.keys(s.stock)){const max=D.species[key]?(D.species[key].fictional?2:24):D.flora[key]?12:D.equipment[key]?8:30;s.stock[key]=Math.min(max,s.stock[key]+(D.species[key]?.fictional?1:4));}for(const key of Object.keys(s.market.demand))s.market.demand[key]=clamp(s.market.demand[key]+0.08,0.35,1.1);
    AL.DailyStore?.rotate(s);AL.LivestockMarket?.rotate(s);const cost=Math.ceil(s.tanks.reduce((n,t)=>n+t.equipment.filter(e=>e.enabled&&e.durability>0&&!(t.lightMode==='off'&&['light','reefLight'].includes(e.type))).reduce((k,e)=>k+D.equipment[e.type].watts*e.capacity/D.equipment[e.type].capacity*0.035,0),0));const paid=Math.min(cost,s.credits);if(AL.Finance)AL.Finance.change(s,-paid,{category:'maintenance',name:'Daily energy',action:'energy',actionId:'energy:'+day,key:'energy:'+day});else s.credits-=paid;s.stats.expenses+=paid;K.log(s,`Day ${day+1}: energy cost ${paid} AC. Local buyers and shop stock refreshed.`);
    if(paid<cost)K.log(s,'Your emergency utility allowance covered the shortfall. Fish welfare equipment stays on.','warning');
    if(day%7===0){for(const t of s.tanks){const contraband=K.alive(t).find(f=>D.species[f.species].fictional);if(contraband&&K.random(s)<(K.has(t,'containment')?0.12:0.65)){t.fish=t.fish.filter(f=>f!==contraband);K.log(s,`Fictional inspection: ${contraband.name} was confiscated. Night-market ownership carries risk.`,'warning');}}}
    if(s.discovered.length>=5&&!s.achievements.includes('Five living colors')){s.achievements.push('Five living colors');K.log(s,'Collection achievement: Five living colors.');}
    if(s.stats.hatched>=1&&!s.achievements.includes('A new generation'))s.achievements.push('A new generation');
    if(s.tanks.some(t=>t.safeHours>=168)&&!s.achievements.includes('A week in balance'))s.achievements.push('A week in balance');
  }
  function step(s,minutes=5){if(!Number.isFinite(minutes)||minutes<=0||minutes>5)throw Error('Simulation steps must be between 0 and 5 minutes.');const untilMidnight=1440-s.time%1440;if(AL.Gameplay&&minutes>untilMidnight){step(s,untilMidnight);return step(s,minutes-untilMidnight);}AL.Preparation.migrate(s);const previous=s.time;AL.Finance?.initialize(s);AL.Update31?.migrate(s);AL.Update29?.beforeStep(s,minutes);AL.Gameplay?.observe(s,minutes);s.time+=minutes;AL.Mortality?.step?.(s);const h=minutes/60;
    for(const t of s.tanks){AL.Mortality?.begin(s,t,previous);AL.EquipmentReliability?.step(s,t,h);AL.MarineCare?.forage(s,t,h);AL.MarineCare?.autofeed(s,t,previous);motion(s,t,minutes);water(s,t,h);food(s,t,h);fishHealth(s,t,h);AL.Expansion?.step(s,t,h);AL.Update31?.step(s,t,h);ecosystems(s,t,h);AL.Health?.step(s,t,h);AL.Breeding?.step(s,t,minutes);eggs(s,t,h);AL.Valuation?.record(s,t);
      const day=Math.floor(s.time/1440),hour=s.time/60%24;if(t.water!=='marine'&&K.has(t,'feeder')&&hour>=9&&t.lastAutoFeed!==day&&(K.alive(t).length||(t.invertebrates||[]).some(f=>!f.dead))){t.lastAutoFeed=day;try{K.feed(s,t,t.foodType);}catch(e){K.log(s,`${t.name}: automatic feeder needs ${D.foods[t.foodType].name}.`,'warning');}}

    }
    AL.Update29?.afterStep(s,previous,minutes);AL.Gameplay?.step(s,previous,minutes);AL.DiveMystery?.step(s);if(Math.floor(previous/1440)!==Math.floor(s.time/1440))daily(s,Math.floor(s.time/1440));return s;
  }
  function advance(s,minutes){const bounded=clamp(Number(minutes)||0,0,60*24*365);for(let n=0;n<bounded;n+=5)step(s,Math.min(5,bounded-n));return s;}
  function motion(s,t,dt){const living=K.alive(t),illumination=light(s,t);for(const f of t.fish){if(f.dead){f.y=clamp(f.y-dt*0.004,0.09,0.94);continue;}const d=D.species[f.species];f.aiTimer-=dt;const hungry=f.hunger>20;const food=hungry?t.food.find(p=>(t.water==='marine'?AL.MarineCare.profile(f).foods.includes(p.type):(f.growth<0.3?p.type==='fry':d.diet.includes(p.type)))):null;const night=illumination<0.1,rest=d.nocturnal?!night:night;
      if(f.aiTimer<=0){f.aiTimer=2+K.random(s)*5;if(food){f.behavior='Seek food';f.targetX=food.x;f.targetY=food.y;}else if(f.stress>45){f.behavior='Hide';f.targetX=t.flora[0]?.x??0.1;f.targetY=0.83;}else if(rest){f.behavior='Rest';f.targetX=clamp(f.x+(K.random(s)-0.5)*0.1,0.1,0.9);f.targetY=clamp(d.zone+0.12,0.1,0.93);}else if(d.group>1){const school=living.filter(n=>n!==f&&n.species===f.species);f.behavior='School';f.targetX=school.length?clamp(school.reduce((n,a)=>n+a.x,0)/school.length+(K.random(s)-0.5)*0.3,0.08,0.92):K.random(s);f.targetY=clamp(d.zone+(K.random(s)-0.5)*0.25,0.12,0.88);}else{f.behavior='Explore';f.targetX=0.08+K.random(s)*0.84;f.targetY=clamp(d.zone+(K.random(s)-0.5)*0.4,0.12,0.9);}}
      AL.Breeding?.motionTarget(s,t,f);
      const speed=0.017*d.activity*(rest?0.2:1)*(f.hp<40?0.5:1)*(f.behavior==='Seek food'?1.7:1);const dx=f.targetX-f.x,dy=f.targetY-f.y,length=Math.max(0.01,Math.hypot(dx,dy));f.vx+=(dx/length*speed-f.vx)*Math.min(1,dt*1.8);f.vy+=(dy/length*speed*0.65-f.vy)*Math.min(1,dt*1.8);f.x=clamp(f.x+f.vx*dt,0.04,0.96);f.y=clamp(f.y+f.vy*dt,0.1,0.93);if(Math.abs(f.vx)>0.001)f.heading=f.vx>=0?1:-1;
    }}
  function offline(s,now=Date.now()){return AL.Offline.sync(s,now);}
  return {step,advance,motion,light,floraConditions,breed,breedingReady,makeBrood,offline};
})();
