"use strict";
// Saved encounter/return/recovery authority. Rendering never consumes this RNG.
AL.DiveMystery=(()=>{
 const K=AL.Core,V=AL.Diving,D=AL.Data,R=AL.DivingData,copy=v=>JSON.parse(JSON.stringify(v));
 const token=(h,o)=>h.id+':recovery:'+o.objectId;
 function receipts(s){try{return JSON.parse(localStorage.getItem(V.receiptKey)||'{}')[s.worldId]||[];}catch{return [];}}
 function pending(s){return (s.diving?.history||[]).flatMap(h=>h.objects.filter(o=>o.recovery?.status==='pending').map(o=>({h,o})));}
 function pool(region,mode){return V.eligible(region,mode,true).filter(p=>!!D.species[p.id]&&D.species[p.id].water==='marine'&&!D.species[p.id].fictional&&D.species[p.id].purchaseVerified!==false);}
 function availability(s,region,mode){if(!R.regions[region]||!R.modes[mode])return {ok:false,reason:'Choose an available destination and mode.'};if(R.regions[region].wildlifeClosed)return {ok:false,reason:'This destination is observation-only. No collectible fish pool is authorized; mystery-fish expeditions are unavailable here.'};if(!pool(region,mode).length)return {ok:false,reason:'Missing content: no verified collectible fish for this region and survey depth. This destination is blocked until a proper pool exists.'};if(pending(s).length)return {ok:false,reason:'Finish receiving or explicitly release the previous expedition’s fish before launching another trip.'};return {ok:true,reason:'At least one reachable mystery fish is guaranteed. Capture and safe return are required; survival is not guaranteed.'};}
 function initialize(s,a){const p=pool(a.region,a.mode);if(!p.length)throw Error('No eligible mystery fish pool.');const species=p[AL.Random.int(s,'divingRng',p.length)].id,o=a.objects[8];Object.assign(o,{kind:'livestock',species,mystery:true,guaranteed:true,mobile:false,collected:false});delete o.group;delete o.variant;a.mysteryVersion=1;a.guaranteedEncounterId=o.id;a.selectionModel='uniform-regional-fish-v1';
  for(const item of a.objects)if(item.kind==='livestock'&&D.species[item.species]){item.mystery=true;item.mobile=false;}
  // Shared logical encounter cells are stable; the canvas supplies smooth local
  // swimming. The guaranteed object has a round trip of six movements at most.
  if(!V.walkable(a,o.x,o.y)||V.distance(a,o.x,o.y)*2*5>=100)throw Error('Mystery fish route exceeds the safe return budget.');
 }
 function collect(s,a,o){if(!pool(a.region,a.mode).some(p=>p.id===o.species))throw Error('This encounter is not collectible in the selected region and habitat.');
  if(a.inventory.some(n=>n.species==='spotted-boxfish'||o.species==='spotted-boxfish'&&n.kind==='livestock'))throw Error('Transport safety requires a dedicated livestock trip for this encounter.');
  const p=V.byId[o.species];a.inventory.push({...o,collected:true,destination:null,position:null,collectedAt:s.time,expiresAt:s.time+Math.round(1440*(1-p.sensitivity*.5)),transport:p.transport,preExisting:AL.Random.int(s,'divingRng',100)/100});o.collected=true;
 }
 function returned(s,a,item){const d=V.definition(item.species);return {objectId:item.id,species:item.species,name:d.name,scientificName:d.scientificName,rarity:d.rarity,mystery:!!item.mystery,revealed:true,source:'diving',region:a.region,mode:a.mode,condition:'Awaiting receiving assessment',value:0,receivingTank:null,reason:'Choose a compatible receiving aquarium or quarantine. No permanent livestock has been granted.',recovery:{status:'pending',item:copy({...item,collected:true}),arrivalTime:s.time,roll:AL.Random.int(s,'divingRng',10000)/10000,conditionRoll:AL.Random.int(s,'divingRng',100)}};}
 function forfeited(s,a,item){return {objectId:item.id,species:item.species,name:'Unknown Fish — ?',mystery:true,revealed:false,condition:'Forfeited',value:0,reason:'The expedition did not return successfully; identity remains concealed.'};}
 function report(s,args){const h=s.diving.history.find(h=>h.id===args.tripId),o=h?.objects.find(o=>o.objectId===args.id);if(!h||h.status!=='success'||!o?.recovery||!V.definition(o.species)||!o.revealed||o.recovery?.status!=='pending')throw Error('This revealed specimen is no longer awaiting recovery.');if(receipts(s).includes(token(h,o)))throw Error('This expedition specimen was already settled locally. Use the current save.');return {h,o};}
 function loss(s,h,o,reason,time=s.time){o.condition='Dead on arrival';o.value=0;o.reason=reason;o.recovery.status='failed';o.recovery.finishedAt=time;o.recovery.deathReason=reason;o.deathRecordId=AL.Mortality.recordTransport(s,h,o,time);}
 function recover(s,args){const {h,o}=report(s,args);if(s.time>=o.recovery.item.expiresAt){loss(s,h,o,'Transport holding time expired before a safe receiver was confirmed.',o.recovery.item.expiresAt);return;}
  const r=V.receiving(s,o.species,args.destination,args.position??null);if(!r.ok)throw Error('Choose a safe receiver: '+r.reasons.join(' '));
  const item={...o.recovery.item,destination:args.destination,position:args.position??null,assessment:{roll:o.recovery.roll,condition:o.recovery.conditionRoll}},result=V.receive(s,h,item);
  const recovery=o.recovery;Object.assign(o,result,{scientificName:V.definition(o.species).scientificName,mystery:!!o.mystery,revealed:true,recovery});recovery.finishedAt=s.time;
  if(o.condition==='Dead on arrival')loss(s,h,o,o.reason);else {recovery.status='received';const t=s.tanks.find(t=>t.id===args.destination);o.destinationName=t.name;}
 }
 function release(s,args){if(args.confirmed!==true)throw Error('Confirm release; this specimen will not enter your collection.');const {o}=report(s,args);o.recovery.status='released';o.recovery.finishedAt=s.time;o.condition='Released without ownership';o.reason='Player explicitly released the expedition specimen instead of receiving it.';o.value=0;}
 function step(s){for(const {h,o}of pending(s))if(s.time>=o.recovery.item.expiresAt)loss(s,h,o,'Transport holding time expired before a safe receiver was confirmed.',o.recovery.item.expiresAt);}
 function migrate(s){if(!s.diving)return;const settled=receipts(s);for(const {h,o}of pending(s))if(settled.includes(token(h,o))){o.recovery.status='released';o.condition='Forfeited';o.reason='A newer local recovery receipt already settled this specimen; the older snapshot cannot grant it twice.';o.value=0;o.recovery.finishedAt=s.time;}}
 function settledTokens(s){return s.diving.history.flatMap(h=>h.objects.filter(o=>o.recovery&&o.recovery.status!=='pending').map(o=>token(h,o)));}
 function validate(s){const fail=m=>{throw Error('Mystery diving save: '+m);},finite=(v,a,b)=>Number.isFinite(v)&&v>=a&&v<=b;
  const a=s.diving.active;if(a?.mysteryVersion!==undefined){if(a.mysteryVersion!==1||a.selectionModel!=='uniform-regional-fish-v1'||!pool(a.region,a.mode).length)fail('invalid expedition profile');const g=a.objects.find(o=>o.id===a.guaranteedEncounterId);if(!g?.mystery||!g.guaranteed||!pool(a.region,a.mode).some(p=>p.id===g.species)||g.x!==4||g.y!==1||g.mobile!==false||V.distance(a,g.x,g.y)*10>=100)fail('invalid guaranteed reachable encounter');
   for(const o of a.objects)if(o.kind==='livestock'&&D.species[o.species]&&(!o.mystery||o.mobile!==false))fail('fish identity presentation missing');
   for(const i of a.inventory)if(i.mystery){const o=a.objects.find(o=>o.id===i.id);if(!o?.mystery||i.destination!==null||i.position!==null||i.transport!==V.byId[i.species].transport)fail('invalid concealed transport');}
  }
  for(const h of s.diving.history){const seen=new Set();for(const o of h.objects)if(o.mystery||o.recovery){if(seen.has(o.objectId)||typeof o.objectId!=='string'||!V.definition(o.species)||!V.eligible(h.region,h.mode,true).some(p=>p.id===o.species)||typeof o.revealed!=='boolean')fail('invalid returned identity');seen.add(o.objectId);
    if(h.status!=='success'){if(o.revealed||o.name!=='Unknown Fish — ?'||o.value!==0||o.recovery)fail('failed expedition revealed or granted a specimen');continue;}
    const r=o.recovery,i=r?.item;if(!o.revealed||o.name!==V.definition(o.species).name||o.scientificName!==V.definition(o.species).scientificName||!['pending','received','failed','released'].includes(r?.status)||!i||i.id!==o.objectId||i.species!==o.species||(!!i.mystery!==!!o.mystery)||!i.collected||!finite(i.collectedAt,h.started,h.ended)||!finite(i.expiresAt,i.collectedAt,1e9)||!finite(i.preExisting,0,.99)||i.transport!==V.byId[o.species].transport||!finite(r.arrivalTime,h.started,h.ended)||!finite(r.roll,0,.9999)||!Number.isInteger(r.conditionRoll)||r.conditionRoll<0||r.conditionRoll>99)fail('invalid saved recovery assessment');
    if(r.status==='received'&&(typeof o.id!=='string'||!o.receivingTank||!o.condition.startsWith('Alive')))fail('invalid ownership receipt');if(r.status==='pending'&&(o.id||o.value!==0||o.condition!=='Awaiting receiving assessment'))fail('pending specimen was already received');if(r.status==='failed'&&(o.value!==0||o.condition!=='Dead on arrival'||typeof o.deathRecordId!=='string'))fail('missing transport loss record');
  }}
 }
 return {pool,availability,initialize,collect,returned,forfeited,pending,recover,release,step,migrate,settledTokens,validate};
})();
