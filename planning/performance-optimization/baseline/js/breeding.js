"use strict";
// Marine reproduction authority. All durations are game hours; probability and
// cohort sizes are husbandry-game calibrations, not real fecundity predictions.
AL.Breeding = (() => {
  const K=AL.Core,D=AL.Data,clamp=K.clamp;
  const profiles=Object.freeze({
    clown:Object.freeze({mode:'attached',roles:'protandrous',habitat:'hard',care:'male',hours:168,court:6,cooldown:336,window:[7,18],chance:.085,larvalFood:'fry',cohort:2}),
    banggai:Object.freeze({mode:'mouthbrood',roles:'separate',habitat:'cover',care:'male',hours:504,court:8,cooldown:720,window:[6,18],chance:.07,larvalFood:'fry',cohort:2,direct:true}),
    'chalk-bass':Object.freeze({mode:'pelagic',roles:'simultaneous',habitat:'open',care:'none',hours:24,court:3,cooldown:240,window:[17,20],chance:.14,larvalFood:'plankton',cohort:2}),
    'sharknose-goby':Object.freeze({mode:'demersal',roles:'separate',habitat:'cavity',care:'male',hours:144,court:5,cooldown:336,window:[8,12],chance:.11,larvalFood:'fry',cohort:2})
  });
  // Do not infer a sexual system, parental role or larval protocol from body shape.
  function profile(species){const d=D.species[species];if(!d||d.water!=='marine'||d.fictional||d.purchaseVerified===false||d.breedingSupported===false)return null;return d.clownfish||species==='clown'?profiles.clown:profiles[species]||null;}
  function hold(species){const d=D.species[species];return d?.breedingSupported===false&&d.breedingStatus?d.breedingStatus:'Autonomous breeding unavailable: a complete species-specific reproductive and rearing profile is not verified.';}
  function description(species){const p=profile(species);return p?'Autonomous '+p.mode+' breeding; '+p.roles+' reproductive roles. '+p.hours+' suitable incubation hours, '+p.cooldown+' game hours of recovery. Larval ration: '+D.foods[p.larvalFood].name+'. Cohort and timing are game calibrations.':hold(species);}
  D.foods.plankton={name:'Cultured live plankton',price:45,quality:.95,pollution:.8,water:'marine',description:'A game ration representing size-appropriate cultured rotifers and copepod nauplii for pelagic larvae. Keep stocked for automatic feeding.'};
  for(const d of Object.values(D.species))if(d.water==='marine'){
    const p=profile(d.id),old=d.breedingStatus,message=description(d.id);d.autonomousBreeding={supported:!!p,mode:p?.mode||null,roles:p?.roles||'unverified'};
    d.breedingSupported=!!p;d.breedingStatus=message;if(old&&d.notes)d.notes=d.notes.replace(old,message);
  }
  const active=r=>r.status==='courtship',living=f=>f&&!f.dead&&f.hp>0;
  function role(f){const p=profile(f.species);return !p?'Unverified reproductive role':p.roles==='simultaneous'?'Simultaneous hermaphrodite':p.roles==='protandrous'&&f.age<D.species[f.species].maturity?'Immature clownfish / nonbreeder':f.reproduction?.roleChangeUntil?'Transitioning to female':f.sex==='F'?'Female':'Male';}
  function ensureFish(s,f){if(D.species[f.species]?.water!=='marine')return;const p=profile(f.species);f.reproduction??={role:p?.roles==='simultaneous'?'simultaneous':p?.roles==='protandrous'&&f.age<D.species[f.species].maturity?'immature':p?f.sex:'unverified',mature:f.age>=D.species[f.species].maturity,partnerId:null,pairId:null,clutchId:null,state:'not-ready',lastSpawn:f.lastBreed>=0?f.lastBreed:null,cooldownUntil:f.lastBreed>=0?f.lastBreed+(p?.cooldown||168)*60:0};}
  function migrate(s){if(!s?.tanks)return;
    s.breeding??={version:1,rng:AL.Random.hash('breeding:'+s.seed),records:[],archive:{courtships:0,spawns:0,hatched:0,failed:0}};
    for(const t of s.tanks)if(t.water==='marine'){
      t.breeding??={nextCheck:Math.floor(s.time/60)*60+60,pairs:[],reservedLoad:0,reservedCount:0};
      t.breeding.reservedLoad??=0;t.breeding.reservedCount??=0;
      for(const f of t.fish)ensureFish(s,f);
    }
    s.inventory.plankton??=0;s.stock.plankton??=30;
  }
  function random(s){return AL.Random.uint(s.breeding,'rng')/4294967296;}
  function site(t,p,f){
    if(p.habitat==='open')return {surface:'water',supportId:null,localX:0,localY:0,x:clamp(f.x,.15,.85),y:.4};
    if(t.hardscape?.length){const r=[...t.hardscape].sort((a,b)=>Math.abs(a.x-f.x)-Math.abs(b.x-f.x))[0],meta=AL.HabitatGeometry[r.group][r.variant];let px=96;while(px<191&&!meta.columns[px]?.length)px++;const top=meta.columns[px]?.[0]?.[0]??100;
      const localX=px/192-.5,localY=-184/192+top/192,x=r.x+localX*r.width/480,y=r.y+localY*r.width/240;
      if(x>=.04&&x<=.96&&y>=.1&&y<=.93)return {surface:'rock',supportId:r.id,localX,localY,x,y};
    }
    const cave=t.decorations.find(d=>d.type==='cave');if(p.habitat!=='hard'&&cave)return {surface:'glass',supportId:null,localX:0,localY:0,x:cave.x,y:.8};
    if(p.habitat==='cover'&&t.flora.some(f=>f.hp>0))return {surface:'glass',supportId:null,localX:0,localY:0,x:clamp(t.flora[0].x,.1,.9),y:.7};
    return null;
  }
  function validSite(t,a){return !!a&&(a.surface!=='rock'||t.hardscape?.some(r=>r.id===a.supportId));}
  function position(t,a){const r=a?.surface==='rock'&&t.hardscape?.find(r=>r.id===a.supportId);return r?{x:r.x+a.localX*r.width/480,y:r.y+a.localY*r.width/240}:{x:a?.x??.5,y:a?.y??.5};}
  function pairRecords(s,t){return (t.breeding?.pairs||[]).map(id=>s.breeding.records.find(r=>r.id===id)).filter(r=>r&&active(r));}
  // Reserve adult load and actual entity slots before courtship, then transfer
  // that same reservation to eggs. Do not double-count a spawned cohort.
  function reservedLoad(t){return (t.breeding?.reservedLoad||0);}
  function reservedCount(t){return (t.breeding?.reservedCount||0);}
  function admissionLoad(t){return K.alive(t).reduce((n,f)=>n+D.species[f.species].load,0)+(t.invertebrates||[]).filter(living).reduce((n,f)=>n+D.invertebrates[f.invertebrate].load,0)+(AL.Update29?.reservedLoad(t)||0)+t.eggs.filter(e=>e.viability>0).reduce((n,e)=>n+D.species[e.species].load*e.count,0)+reservedLoad(t);}
  function reservations(s,t){const pairs=pairRecords(s,t);t.breeding.reservedLoad=pairs.reduce((n,r)=>n+D.species[r.species].load*r.eggCount,0);t.breeding.reservedCount=pairs.reduce((n,r)=>n+r.eggCount,0);}
  function room(s,t,species,count,ignorePair=null){const d=D.species[species],pairs=pairRecords(s,t).filter(r=>r.id!==ignorePair),broods=t.eggs.filter(e=>e.viability>0&&!e.done),fish=K.alive(t);
    const adults=fish.reduce((n,f)=>n+D.species[f.species].load,0)+(t.invertebrates||[]).filter(living).reduce((n,f)=>n+D.invertebrates[f.invertebrate].load,0)+(AL.Update29?.reservedLoad(t)||0),reserved=broods.reduce((n,e)=>n+D.species[e.species].load*e.count,0)+pairs.reduce((n,r)=>n+D.species[r.species].load*r.eggCount,0);
    return t.fish.length+broods.reduce((n,e)=>n+e.count,0)+pairs.reduce((n,r)=>n+r.eggCount,0)+count<=AL.Config.maxFish&&adults+reserved+d.load*count<=K.loadLimit(t)*.8&&broods.length+pairs.length<20;
  }
  function illness(f){return !!f.disease||!!f.healthState?.treatment||(f.healthState?.conditions||[]).some(c=>c.severity>.15);}
  function water(t,species){const w=t.waterParams,d=D.species[species];return AL.Preparation.prepared(t)&&t.bacteria>=.65&&t.bacteria2>=.5&&w.ammonia<=.05&&w.nitrite<=.05&&w.nitrate<=30&&w.oxygen>=6&&w.temperature>=d.temp[0]&&w.temperature<=d.temp[1]&&w.ph>=d.ph[0]&&w.ph<=d.ph[1]&&w.salinity>=d.salinity[0]&&w.salinity<=d.salinity[1];}
  function condition(s,f,ignorePair=false){if(!living(f))return 'This individual is deceased.';const p=profile(f.species);if(!p)return hold(f.species);const d=D.species[f.species],r=f.reproduction;
    if(f.age<d.maturity)return 'Not sexually mature.';if(r?.roleChangeUntil)return 'Reproductive transition is still developing.';
    if(f.hp<85||f.hunger>40||(f.healthState?.nutrition??90)<75||f.stress>=25||f.energy<20)return 'Needs at least 85 HP, 75% nutrition, energy 20, hunger at most 40 and stress below 25.';
    if(illness(f))return 'Resolve illness and treatment before reproduction.';
    if(s.time<(r?.cooldownUntil||0))return 'Recovering after spawning.';
    if(!ignorePair&&r?.pairId)return 'Already in courtship.';
    return null;
  }
  function report(s,t,a,b,ignorePair=null){const p=profile(a?.species);if(!p)return {ok:false,reason:hold(a?.species)};
    if(!b||a===b||a.species!==b.species||!t.fish.includes(a)||!t.fish.includes(b))return {ok:false,reason:'Needs another compatible individual of the same biological species in this aquarium.'};
    for(const f of [a,b]){const reason=condition(s,f,!!ignorePair);if(reason)return {ok:false,reason};}
    if(p.roles!=='simultaneous'&&(a.sex!=='F'||b.sex!=='M'))return {ok:false,reason:'Needs compatible egg-producing female and male roles. Established clownfish females never reverse sex.'};
    if(p.roles==='protandrous'){const group=K.alive(t).filter(f=>f.species===a.species&&f.age>=D.species[a.species].maturity),males=group.filter(f=>f.sex==='M').sort((x,y)=>y.adultSize*y.growth-x.adultSize*x.growth||x.id.localeCompare(y.id));if(group.filter(f=>f.sex==='F').length!==1||males[0]?.id!==b.id)return {ok:false,reason:'Only one established female and the dominant mature male breed; subordinate clownfish do not form extra breeding pairs.'};}
    const genetics=AL.Patterns?.ready(a,b);if(genetics)return {ok:false,reason:genetics};
    if(t.eggs.some(e=>e.viability>0&&e.parents?.some(id=>id===a.id||id===b.id)))return {ok:false,reason:'A parent is caring for an existing brood.'};
    if(t.volume<D.species[a.species].minTank)return {ok:false,reason:'The aquarium is below this species minimum volume.'};
    if(!water(t,a.species))return {ok:false,reason:'Needs stable, cycled species-appropriate water, oxygen at least 6 mg/L and low pollutants.'};
    const nest=ignorePair?s.breeding.records.find(r=>r.id===ignorePair)?.site:site(t,p,a);if(!validSite(t,nest))return {ok:false,reason:'Add a suitable hard rock nest, cavity or protected cover for this species.'};
    const occupied=[...pairRecords(s,t).filter(r=>r.id!==ignorePair).map(r=>r.site),...t.eggs.filter(e=>e.viability>0).map(e=>e.anchor)].filter(Boolean);
    if(p.mode!=='pelagic'&&occupied.some(x=>x.surface==='rock'&&x.supportId===nest.supportId||Math.hypot(x.x-nest.x,x.y-nest.y)<.18))return {ok:false,reason:'The spawning territory is already occupied. Add separated nesting habitat.'};
    if(K.alive(t).some(f=>![a,b].includes(f)&&f.aggression>.55&&Math.hypot(f.x-nest.x,f.y-nest.y)<.22))return {ok:false,reason:'An aggressive neighbor is disturbing the spawning territory.'};
    if(!room(s,t,a.species,p.cohort,ignorePair))return {ok:false,reason:'Reserve adult stocking space, including 20% breeding headroom, and entity slots for the offspring.'};
    const foods=D.species[a.species].diet;if(!foods.some(k=>(s.inventory[k]||0)>0)||!(s.inventory[p.larvalFood]>0))return {ok:false,reason:'Keep compatible adult rations and '+D.foods[p.larvalFood].name+' available for rearing.'};
    return {ok:true,reason:'A compatible pair is ready; spawning remains probabilistic within its daily window.',site:nest};
  }
  function ready(s,t,species){const p=profile(species);if(!p)return {ok:false,reason:hold(species)};if(!room(s,t,species,p.cohort))return {ok:false,reason:'Reserve adult stocking space, including 20% breeding headroom, and entity slots for the offspring.'};const fish=K.alive(t).filter(f=>f.species===species),as=fish.filter(f=>p.roles==='simultaneous'||f.sex==='F'),bs=fish.filter(f=>p.roles==='simultaneous'||f.sex==='M');let first=null;
    for(const a of as)for(const b of bs)if(a!==b){const r=report(s,t,a,b);if(r.ok)return {...r,female:a,male:b};first??=r;}return first||{ok:false,reason:'Needs two mature, compatible same-species reproductive partners.'};
  }
  function status(s,t,f){const r=f.reproduction,p=profile(f.species),base={role:role(f),mature:f.age>=D.species[f.species].maturity,partnerId:r?.partnerId||null,clutchId:r?.clutchId||null,lastSpawn:r?.lastSpawn??null,cooldown:Math.max(0,(r?.cooldownUntil||0)-s.time)};
    if(!living(f))return {...base,state:'deceased',label:'Deceased',reason:f.deathCause};
    if(!base.mature)return {...base,state:'immature',label:'Immature',reason:'Sexual maturity at '+D.species[f.species].maturity+' game days.'};
    if(!p)return {...base,state:'unsupported',label:'Breeding Not Modeled',reason:hold(f.species)};
    const clutch=t.eggs.find(e=>e.naturalBreeding&&e.viability>0&&e.parents.includes(f.id));
    if(clutch&&p.mode==='mouthbrood'&&f.id===clutch.carrierId)return {...base,state:'mouthbrooding',label:'Male Mouthbrooding',reason:'Developing offspring are carried internally; no external egg pile.'};
    if(clutch&&p.care==='male'&&f.id===clutch.carrierId)return {...base,state:'tending',label:'Tending Nest',reason:'The male guards and fans the attached clutch.'};
    const pair=pairRecords(s,t).find(pair=>pair.parents.includes(f.id));if(pair){const q=(s.time-pair.startedAt)/(p.court*60),eggRole=pair.parents[0]===f.id;return {...base,state:q>=.82?'preparing':q>=.35&&eggRole?'gravid':'courtship',label:q>=.82?'Preparing to Spawn':q>=.35&&eggRole?'Gravid — Carrying Eggs':'Courtship',reason:p.roles==='simultaneous'?'Simultaneous hermaphrodites alternate egg-donor roles between modeled spawning events.':'Pair display and nest preparation are in progress.'};}
    if(base.cooldown>0)return {...base,state:'recovering',label:'Recovering After Spawning',reason:'Parental reserves must recover before another courtship.'};
    const reason=condition(s,f);if(reason)return {...base,state:'not-ready',label:'Not Ready to Breed',reason};
    if(!room(s,t,f.species,p.cohort))return {...base,state:'not-ready',label:'Not Ready to Breed',reason:'Reserve adult stocking space, including 20% breeding headroom, and entity slots for the offspring.'};
    const partners=K.alive(t).filter(n=>n!==f&&n.species===f.species);let issue='Needs a compatible partner in this aquarium.';for(const b of partners){const a=p.roles==='simultaneous'||f.sex==='F'?f:b,mate=a===f?b:f,rp=report(s,t,a,mate);if(rp.ok)return {...base,state:'ready',label:'Ready to Breed',reason:rp.reason};issue=rp.reason;}
    return {...base,state:'not-ready',label:'Not Ready to Breed',reason:issue};
  }
  function normalize(s,t){for(const f of t.fish){ensureFish(s,f);const r=f.reproduction;if(profile(f.species)?.roles==='protandrous'&&r.role==='immature'&&f.age>=D.species[f.species].maturity)f.sex='M';r.mature=f.age>=D.species[f.species].maturity;if(r.roleChangeUntil&&s.time>=r.roleChangeUntil){const other=t.fish.some(n=>living(n)&&n!==f&&n.species===f.species&&n.sex==='F');if(!other)f.sex='F';delete r.roleChangeUntil;}r.role=profile(f.species)?.roles==='simultaneous'?'simultaneous':profile(f.species)?.roles==='protandrous'&&!r.mature?'immature':profile(f.species)?f.sex:'unverified';}
    for(const species of new Set(K.alive(t).filter(f=>profile(f.species)?.roles==='protandrous').map(f=>f.species))){const adults=K.alive(t).filter(f=>f.species===species&&f.age>=D.species[species].maturity);if(adults.length>=2&&!adults.some(f=>f.sex==='F'||f.reproduction.roleChangeUntil)){adults.sort((a,b)=>b.adultSize*b.growth-a.adultSize*a.growth||a.id.localeCompare(b.id));adults[0].reproduction.roleChangeUntil=s.time+14*1440;}}
  }
  function trim(s){const done=s.breeding.records.filter(r=>!active(r)&&!s.tanks.some(t=>t.eggs.some(e=>e.id===r.clutchId)));while(s.breeding.records.length>600&&done.length){const r=done.shift(),a=s.breeding.archive;a.courtships++;if(r.spawnedAt!==null)a.spawns++;a.hatched+=r.offspring.length;if(['failed','cancelled'].includes(r.status))a.failed++;s.breeding.records=s.breeding.records.filter(n=>n!==r);}}
  function release(s,t,r){for(const id of r.parents){const f=t.fish.find(f=>f.id===id);if(f?.reproduction.pairId===r.id)f.reproduction.pairId=null;}t.breeding.pairs=t.breeding.pairs.filter(id=>id!==r.id);reservations(s,t);}
  function cancel(s,t,r,reason){r.status='cancelled';r.finishedAt=s.time;r.reason=reason;release(s,t,r);for(const id of r.parents){const f=t.fish.find(f=>f.id===id);if(f){f.reproduction.cooldownUntil=Math.max(f.reproduction.cooldownUntil,s.time+24*60);f.reproduction.partnerId=null;}}K.log(s,D.species[r.species].name+': courtship ended. '+reason,'warning');}
  function spawn(s,t,r){const p=profile(r.species),[a,b]=r.parents.map(id=>t.fish.find(f=>f.id===id));AL.Sim.makeBrood(s,t,r.species,a,b);const e=t.eggs.at(-1);e.naturalBreeding=true;e.reproductiveMode=p.mode;e.pairId=r.id;e.spawnedAt=s.time;e.count=p.cohort;e.required=p.hours;e.carrierId=p.care==='male'?b.id:null;e.anchor=p.mode==='mouthbrood'?null:{...r.site};e.site={...r.site};e.fertilization=clamp(.72+.25*Math.min(a.fertility,b.fertility),.72,.96);e.viability=100;e.losses={genetic:0,unfertilized:0,water:0,care:0,disease:0,predation:0,dispersal:0,capacity:0};e.eggState=Array.from({length:e.count},(_,i)=>{const genetic=e.embryos?.[i]?.viable!==false,alive=genetic&&random(s)<e.fertilization;if(!genetic)e.losses.genetic++;else if(!alive)e.losses.unfertilized++;return {index:i,alive};});e.viability=e.eggState.filter(x=>x.alive).length/e.count*100;
    r.status='spawning';r.clutchId=e.id;r.spawnedAt=s.time;r.eggCount=e.count;
    for(const f of [a,b]){f.lastBreed=s.time;f.reproduction.lastSpawn=s.time;f.reproduction.cooldownUntil=s.time+p.cooldown*60;f.reproduction.clutchId=e.id;f.reproduction.partnerId=f===a?b.id:a.id;f.energy=clamp(f.energy-8,0,100);f.healthState&&(f.healthState.nutrition=clamp(f.healthState.nutrition-3,0,100));}
    release(s,t,r);K.log(s,D.species[r.species].name+': natural spawning in '+t.name+' ('+e.id+').');if(!e.viability)finish(s,t,e,'Clutch failed at fertilization: '+e.losses.unfertilized+' unfertilized, '+e.losses.genetic+' genetically nonviable.');
  }
  function step(s,t,minutes){if(t.water!=='marine')return;migrate(s);normalize(s,t);
    for(const r of pairRecords(s,t)){
      const [a,b]=r.parents.map(id=>t.fish.find(f=>f.id===id)),reportNow=a&&b?report(s,t,a,b,r.id):{ok:false,reason:'A partner left the aquarium.'};
      if(!reportNow.ok){cancel(s,t,r,reportNow.reason);continue;}
      if(s.time-r.startedAt>=profile(r.species).court*60)spawn(s,t,r);
    }
    if(s.time>=t.breeding.nextCheck){t.breeding.nextCheck=Math.floor(s.time/60)*60+60;for(const species of [...new Set(K.alive(t).map(f=>f.species))].sort()){
      const p=profile(species);if(!p)continue;const hour=s.time/60%24;if(hour<p.window[0]||hour>=p.window[1])continue;const q=ready(s,t,species);if(!q.ok)continue;if(random(s)>=p.chance*Math.min(q.female.fertility,q.male.fertility))continue;
      let a=q.female,b=q.male;if(p.roles==='simultaneous'){
        const last=[...s.breeding.records].reverse().find(r=>r.species===species&&r.parents.includes(a.id)&&r.parents.includes(b.id)&&r.spawnedAt!==null);if(last?.parents[0]===a.id)[a,b]=[b,a];
      }
      const r={id:K.id(s,'court'),tankId:t.id,species,parents:[a.id,b.id],startedAt:s.time,spawnedAt:null,finishedAt:null,status:'courtship',site:{...q.site},clutchId:null,eggCount:p.cohort,offspring:[],reason:''};s.breeding.records.push(r);t.breeding.pairs.push(r.id);
      for(const f of [a,b]){f.reproduction.pairId=r.id;f.reproduction.partnerId=f===a?b.id:a.id;f.reproduction.state='courtship';}reservations(s,t);K.log(s,D.species[species].name+': natural courtship observed in '+t.name+'.');
    }}
    for(const f of t.fish)f.reproduction.state=status(s,t,f).state;trim(s);
  }
  function motionTarget(s,t,f){if(t.water!=='marine'||!living(f)||f.stress>45||f.hunger>55||f.behavior==='Seek food')return;
    const pair=pairRecords(s,t).find(r=>r.parents.includes(f.id)),p=profile(f.species),clutch=t.eggs.find(e=>e.naturalBreeding&&e.viability>0&&e.carrierId===f.id);if(!p||(!pair&&!clutch))return;
    const phase=s.time/8+(pair?.parents[0]===f.id?0:Math.PI),point=position(t,pair?.site||clutch.site);
    if(pair&&p.mode==='pelagic'){f.behavior='Synchronized spawning rise';f.targetX=clamp(point.x+Math.sin(phase)*.11,.07,.93);f.targetY=clamp(.4+Math.cos(phase*.5)*.13,.12,.8);}
    else if(pair&&p.mode==='mouthbrood'){f.behavior='Courtship circle';f.targetX=clamp(point.x+Math.cos(phase)*.10,.07,.93);f.targetY=clamp(point.y-.09+Math.sin(phase)*.07,.12,.88);}
    else {f.behavior=pair?'Prepare nest':'Guard and fan eggs';f.targetX=clamp(point.x+Math.sin(phase)*.075,.07,.93);f.targetY=clamp(point.y-.05+Math.cos(phase)*.035,.12,.88);}
    if(clutch&&p.mode==='mouthbrood'){f.behavior='Male mouthbrooding';f.targetX=clamp(point.x+Math.sin(phase)*.035,.07,.93);f.targetY=clamp(point.y-.07,.12,.88);}
  }
  function finish(s,t,e,reason){const r=s.breeding.records.find(r=>r.id===e.pairId);if(r){r.status=r.offspring.length?'hatched':'failed';r.finishedAt=s.time;r.reason=reason;r.losses={...e.losses};}e.done=true;if(!r?.offspring.length){e.viability=0;t.waterParams.organic+=.03;if(e.anchor){e.failedAt=s.time;e.done=false;}}K.log(s,D.species[e.species].name+': '+reason,r?.offspring.length?'info':'warning');}
  function incubate(s,t,e,h){const p=profile(e.species),d=D.species[e.species],w=t.waterParams;if(!p){finish(s,t,e,'Reproductive profile unavailable; brood cannot continue.');return;}
    if(e.failedAt!==undefined){if(s.time-e.failedAt>=1440)e.done=true;return;}
    e.age+=h;const care=e.carrierId?t.fish.find(f=>f.id===e.carrierId):null,well=water(t,e.species),sick=[...e.parents.map(id=>t.fish.find(f=>f.id===id))].some(f=>f&&illness(f)),guard=living(care)&&care.hp>=70&&care.hunger<65&&care.stress<40;
    if(p.mode==='mouthbrood'&&!living(care)){for(const egg of e.eggState)if(egg.alive){egg.alive=false;e.losses.care++;}finish(s,t,e,'Brooding male died or left the aquarium.');return;}
    if(p.mode!=='pelagic'&&!validSite(t,e.site)){for(const egg of e.eggState)if(egg.alive){egg.alive=false;e.losses.care++;}finish(s,t,e,'Spawning habitat was removed.');return;}
    if(well)e.progress+=h*clamp(Math.pow(1.06,w.temperature-25),.75,1.2);
    const predators=K.alive(t).filter(f=>!e.parents.includes(f.id)&&f.hunger>35).reduce((n,f)=>n+Math.max(.05,D.species[f.species].predator)*(f.hunger>60?2:1),0);
    const hazards={water:well?0:.08+(w.oxygen<4?.3:0)+w.ammonia*.15+w.nitrite*.15,care:p.care==='male'&&!guard?.025:0,disease:sick?.012:0,predation:p.mode==='mouthbrood'?0:predators*(guard?.0004:.003),dispersal:p.mode==='pelagic'?.004:0};
    for(const egg of e.eggState)if(egg.alive){for(const [cause,rate]of Object.entries(hazards))if(rate>0&&random(s)<1-Math.exp(-rate*h)){egg.alive=false;e.losses[cause]++;break;}}
    e.viability=e.eggState.filter(x=>x.alive).length/e.count*100;
    if(!e.viability){finish(s,t,e,'Clutch failed: '+Object.entries(e.losses).filter(([,n])=>n).map(([k,n])=>k+' '+n).join(', ')+'.');return;}
    if(e.progress<e.required)return;
    const record=s.breeding.records.find(r=>r.id===e.pairId);if(!record){finish(s,t,e,'Missing parentage record.');return;}
    for(const egg of e.eggState.filter(x=>x.alive)){
      // Other admissions honor reservations; nevertheless recheck after imports,
      // habitat changes and deaths, and never manufacture at least one hatchling.
      const alive=K.alive(t),load=alive.reduce((n,f)=>n+D.species[f.species].load,0)+(t.invertebrates||[]).filter(living).reduce((n,f)=>n+D.invertebrates[f.invertebrate].load,0)+(AL.Update29?.reservedLoad(t)||0)+t.eggs.filter(x=>x!==e&&x.viability>0).reduce((n,x)=>n+D.species[x.species].load*x.count,0)+reservedLoad(t);
      if(t.fish.length>=AL.Config.maxFish||load+d.load>K.loadLimit(t)){e.losses.capacity++;continue;}
      const f=K.fish(s,e.species,{age:p.direct?d.maturity*.3:1,genes:{...e.genes},parents:[...e.parents],generation:e.generation,bought:false});f.name=(d.name+(p.direct?' juvenile':' larva')).slice(0,36);f.hunger=20;f.provenance={source:'captive-bred',acquired:s.time};f.naturalOrigin={clutchId:e.id,pairId:e.pairId,larvalFood:p.larvalFood,hatchedAt:s.time,minimumSaleAge:Math.max(d.maturity*.3,f.age+7)};AL.Patterns?.inherit(f,e,egg.index);const point=p.mode==='mouthbrood'?{x:care.x,y:care.y}:AL.BroodView.position(t,e);f.x=clamp(point.x+(random(s)-.5)*.035,.05,.95);f.y=clamp(point.y-.04,.12,.9);ensureFish(s,f);t.fish.push(f);record.offspring.push({id:f.id,hatchedAt:s.time,parents:[...e.parents],species:f.species});s.stats.hatched++;K.discover(s,f.species);
    }
    finish(s,t,e,record.offspring.length+' offspring hatched in '+t.name+'. '+(p.mode==='pelagic'?'Pelagic larvae require cultured live plankton.':'Provide fine fry food and protected nursery habitat.'));
  }
  function saleHold(f){return !!f.naturalOrigin&&(f.growth<.3||f.age<f.naturalOrigin.minimumSaleAge);}
  function reconcile(s){migrate(s);for(const t of s.tanks)if(t.water==='marine'){
    for(const r of pairRecords(s,t))if(!r.parents.every(id=>t.fish.some(f=>living(f)&&f.id===id))||!validSite(t,r.site))cancel(s,t,r,'A parent or spawning site left the aquarium.');
    reservations(s,t);
  }for(const t of s.tanks)if(t.water==='marine')for(const f of t.fish){const r=f.reproduction;if(r.pairId&&!pairRecords(s,t).some(p=>p.id===r.pairId)){r.pairId=null;r.partnerId=null;r.cooldownUntil=Math.max(r.cooldownUntil,s.time+24*60);}}}
  function validateLinks(s,fail){const childIds=new Set();for(const r of s.breeding.records){const t=s.tanks.find(t=>t.id===r.tankId);if(active(r)&&!t?.breeding.pairs.includes(r.id))fail('orphaned courtship record');if(r.status==='spawning'&&!t?.eggs.some(e=>e.id===r.clutchId&&e.naturalBreeding))fail('missing incubating clutch');for(const f of r.offspring){if(!/^fish\d+$/.test(f.id)||Number(f.id.slice(4))>=s.nextId||childIds.has(f.id))fail('duplicate offspring identity');childIds.add(f.id);}}
    for(const t of s.tanks)if(t.water==='marine'){
      const parents=new Set();for(const r of pairRecords(s,t))for(const id of r.parents){const f=t.fish.find(f=>f.id===id);if(!f||f.species!==r.species||f.reproduction.pairId!==r.id||parents.has(id))fail('incompatible or repeated active parent');parents.add(id);}
      for(const e of t.eggs)if(e.naturalBreeding){const r=s.breeding.records.find(r=>r.id===e.pairId),p=profile(e.species);if(e.spawnedAt!==r.spawnedAt||e.count!==p.cohort||JSON.stringify(e.site)!==JSON.stringify(r.site)||p.mode!=='mouthbrood'&&JSON.stringify(e.anchor)!==JSON.stringify(e.site)||e.carrierId!==(p.care==='male'?e.parents[1]:null)||e.eggState.some(x=>x.alive&&e.embryos?.[x.index]?.viable===false))fail('altered natural clutch biology');
        if(e.viability!==e.eggState.filter(x=>x.alive).length/e.count*100&&e.failedAt===undefined)fail('clutch viability disagrees with embryos');
      }
    }
  }
  function validate(s,identity){const fail=message=>{throw Error('Breeding save: '+message);},num=(n,a,b)=>Number.isFinite(n)&&n>=a&&n<=b,ids=new Set();if(!s.breeding)return;const b=s.breeding;
    if(b.version!==1||!Number.isInteger(b.rng)||b.rng<0||b.rng>4294967295||!Array.isArray(b.records)||b.records.length>620||!b.archive||!Object.values(b.archive).every(n=>Number.isInteger(n)&&n>=0))fail('invalid journal or random stream');
    for(const r of b.records){if(ids.has(r.id)||!profile(r.species)||!Array.isArray(r.parents)||r.parents.length!==2||r.parents[0]===r.parents[1]||!r.parents.every(id=>typeof id==='string'&&id.length<50)||!num(r.startedAt,0,s.time)||!['courtship','cancelled','spawning','hatched','failed'].includes(r.status)||!Array.isArray(r.offspring)||r.offspring.length>30||!num(r.eggCount,1,30)||typeof r.reason!=='string'||r.reason.length>1000)fail('invalid parentage record');identity(r.id);ids.add(r.id);if(!s.tanks.some(t=>t.id===r.tankId)&&!(r.soldTank&&s.aquariumSales?.receipts.some(a=>a.tankId===r.tankId))||!r.site||!['rock','glass','water'].includes(r.site.surface)||!['x','y','localX','localY'].every(k=>num(r.site[k],-1,1))||!num(r.site.x,0,1)||!num(r.site.y,0,1))fail('invalid spawning site');for(const n of [r.spawnedAt,r.finishedAt])if(n!==null&&!num(n,r.startedAt,s.time))fail('invalid event timestamp');const offspring=new Set();for(const f of r.offspring){if(typeof f.id!=='string'||offspring.has(f.id)||f.species!==r.species||JSON.stringify(f.parents)!==JSON.stringify(r.parents)||!num(f.hatchedAt,0,s.time))fail('invalid offspring lineage');offspring.add(f.id);}}
    for(const t of s.tanks)if(t.water==='marine'){
      const tb=t.breeding;if(!tb||!num(tb.nextCheck,0,1e12)||!Array.isArray(tb.pairs)||tb.pairs.length>20||new Set(tb.pairs).size!==tb.pairs.length)fail('invalid observation schedule');const pairs=tb.pairs.map(id=>b.records.find(r=>r.id===id));if(pairs.some(r=>!r||r.tankId!==t.id||!active(r))||pairs.some(r=>!r.parents.every(id=>t.fish.some(f=>f.id===id))))fail('invalid active courtship');const load=pairs.reduce((n,r)=>n+D.species[r.species].load*r.eggCount,0),count=pairs.reduce((n,r)=>n+r.eggCount,0);if((tb.reservedLoad||0)!==load||(tb.reservedCount||0)!==count)fail('incorrect offspring reservation');
      for(const f of t.fish){const r=f.reproduction;if(!r||!['M','F','simultaneous','immature','unverified'].includes(r.role)||typeof r.mature!=='boolean'||!num(r.cooldownUntil,0,1e12)||(r.lastSpawn!==null&&!num(r.lastSpawn,0,s.time))||typeof r.state!=='string'||r.state.length>30)fail('invalid individual reproductive state');for(const key of ['partnerId','pairId','clutchId'])if(r[key]!==null&&(typeof r[key]!=='string'||r[key].length>50))fail('invalid individual relationship');if(r.roleChangeUntil!==undefined&&!num(r.roleChangeUntil,0,1e12))fail('invalid reproductive transition');if(f.naturalOrigin){const n=f.naturalOrigin;if(!['fry','plankton'].includes(n.larvalFood)||!num(n.hatchedAt,0,s.time)||!num(n.minimumSaleAge,D.species[f.species].maturity*.3,1e9)||typeof n.clutchId!=='string'||typeof n.pairId!=='string')fail('invalid hatchling origin');}}
      for(const e of t.eggs)if(e.naturalBreeding){const p=profile(e.species),r=b.records.find(r=>r.id===e.pairId);if(!p||!r||!(r.status==='spawning'||r.status==='failed'&&e.failedAt!==undefined&&e.viability===0)||r.clutchId!==e.id||r.tankId!==t.id||JSON.stringify(r.parents)!==JSON.stringify(e.parents)||e.reproductiveMode!==p.mode||e.required!==p.hours||!num(e.spawnedAt,0,s.time)||!num(e.fertilization,0,1)||!Array.isArray(e.eggState)||e.eggState.length!==e.count||e.eggState.some((a,i)=>a.index!==i||typeof a.alive!=='boolean')||!e.losses||!Object.values(e.losses).every(n=>Number.isInteger(n)&&n>=0))fail('invalid natural clutch');if(p.mode==='mouthbrood'&&(e.anchor!==null||e.carrierId!==e.parents[1]))fail('invalid brooding parent');if(p.mode!=='mouthbrood'&&(!e.anchor||e.anchor.surface!==(p.mode==='pelagic'?'water':r.site.surface)))fail('invalid external clutch');}
    }
    validateLinks(s,fail);
  }
  return {profiles,profile,hold,description,migrate,ensureFish,role,site,position,ready,report,status,step,motionTarget,incubate,room,reservedLoad,reservedCount,admissionLoad,saleHold,validate,reconcile};
})();
