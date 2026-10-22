"use strict";
// Explain the same checks used by the final transfer; never hide owned tanks.
AL.DiveReceiving=(()=>{
 const K=AL.Core,D=AL.Data,units=3.785411784;
 const number=n=>Number.isFinite(n)?String(n):'Unavailable',gal=n=>Number.isFinite(n)?(n/units).toFixed(3)+' US gal':'Unavailable';
 function report(s,id,tankId){const t=s.tanks.find(t=>t.id===tankId),d=D.species[id],checks=[],warnings=[];
  const add=(id,label,ok,actual,required,help)=>checks.push({id,label,ok:!!ok,actual:String(actual),required:String(required),help});
  if(!t||!d)return {ok:false,reasons:[!t?'Choose an owned receiving aquarium.':'Fish species is not implemented.'],warnings,checks};
  const w=t.waterParams,base=AL.StoreRules.report(s,t,'buyFish',{species:id,count:1});
  add('habitat','Water classification',t.water===d.water&&t.water==='marine',t.water==='marine'?'Saltwater':'Freshwater',d.water==='marine'?'Saltwater; freshwater receiving remains locked':'Freshwater is currently locked','Choose a saltwater aquarium.');
  add('volume','Water volume',t.volume>=d.minTank,gal(t.volume),'>= '+gal(d.minTank),'Choose a larger aquarium; nominal gallon labels do not change physical water volume.');
  for(const [key,label,unit,range] of [['temperature','Actual water temperature','°C',d.temp],['salinity','Salinity','ppt',d.salinity],['ph','pH','',d.ph]])add(key,label,Number.isFinite(w[key])&&w[key]>=range[0]&&w[key]<=range[1],number(w[key])+' '+unit,range[0]+'–'+range[1]+' '+unit+' inclusive','Correct the measured water reading; heater setpoint alone does not establish compatibility.');
  for(const [key,label,limit,lower] of [['ammonia','Ammonia',.15,false],['nitrite','Nitrite',.15,false],['oxygen','Dissolved oxygen',5.5,true]])add(key,label,Number.isFinite(w[key])&&(lower?w[key]>=limit:w[key]<=limit),number(w[key])+' mg/L',(lower?'>= ':'<= ')+limit+' mg/L',lower?'Restore aeration/circulation and inspect stocking.':'Finish cycling, check filtration and safely correct water chemistry.');
  add('prepared','Water prepared',t.prepared&&!t.emptyDry,t.prepared&&!t.emptyDry?'Prepared water':'Unprepared / dry','Prepared saltwater','Use aquarium setup to prepare the water.');
  add('bacteria','Ammonia-processing colony',t.bacteria>=.65,number(t.bacteria),'>= 0.65','Start or finish biological cycling; do not add fish to an uncycled tank.');
  add('bacteria2','Nitrite-processing colony',t.bacteria2>=.5,number(t.bacteria2),'>= 0.5','Allow both bacterial colonies to establish.');
  for(const [type,label]of [['filter','Filtration'],['flow','Circulation']]){const devices=t.equipment.filter(e=>e.type===type),capacity=K.capacity(t,type);add(type,label,K.has(t,type)&&capacity>0,devices.length?devices.map(e=>(e.enabled?'On':'Off')+', condition '+number(e.durability)+'%, rated '+gal(e.capacity)).join('; ')+'; effective '+gal(capacity):'Not installed','Installed, enabled and functioning '+(type==='filter'?'filter':'circulation pump'),'Install or enable the device and repair failed equipment.');if(capacity>0&&capacity<t.volume)warnings.push(label+' condition-adjusted capacity '+gal(capacity)+' is below aquarium '+gal(t.volume)+'. Maintain equipment and monitor water; this capacity warning is not a new full-output gate.');}
  const residents=K.alive(t),reserved=(AL.Breeding?.reservedLoad(t)||0)+t.eggs.reduce((n,e)=>n+D.species[e.species].load*e.count,0)+(AL.Update29?.reservedLoad(t)||0)+(t.invertebrates||[]).filter(f=>!f.dead).reduce((n,f)=>n+D.invertebrates[f.invertebrate].load,0),adult=residents.reduce((n,f)=>n+D.species[f.species].load,0),limit=K.loadLimit(t);
  add('stocking','Adult stocking capacity',adult+reserved+d.load<=limit,number(adult)+' resident + '+number(reserved)+' reserved + '+number(d.load)+' incoming load','Combined adult load <= '+number(limit),'Move livestock to another compatible home or use a larger aquarium. Reserved eggs/offspring also occupy capacity.');
  const count=residents.length+(t.water==='marine'?t.eggs.filter(e=>e.viability>0).reduce((n,e)=>n+e.count,0)+(AL.Breeding?.reservedCount(t)||0):0)+1;
  add('entities','Livestock entity capacity',count<=AL.Config.maxFish,number(count)+' after receiving','<= '+AL.Config.maxFish+' fish including reserved viable offspring','Use another aquarium with room for this specimen.');
  const courses=[...t.fish,...t.flora,...(t.invertebrates||[])].filter(f=>!f.dead&&f.hp>0&&f.healthState?.treatment).map(f=>AL.Health.products[f.healthState.treatment.product]);
  const restricted=courses.filter(p=>p?.quarantine);
  add('quarantine','Quarantine restrictions',restricted.length===0,restricted.length?'Active '+restricted.map(p=>p.name).join(', '):t.kind==='quarantine'?'Quarantine; no active restricted course':'Display / reef; no active restricted course','No introduction into an active restricted treatment course; quarantine is optional for this untreated catch','Finish the restricted course or choose a separate prepared, cycled compatible home. A valid quarantine receives the existing survival benefit; it does not waive habitat/water checks.');
  if(d.habitat==='rocks'||d.habitat==='sand'){const shelter=(t.hardscape?.length||0)+t.decorations.filter(x=>x.type==='cave').length;add('shelter','Rock shelter',shelter>0,shelter+' rock / cave shelter(s)','At least one rock shelter or cave','Place suitable rock or a rock cave using the normal aquarium placement tools.');}
  add('social','Species group',residents.filter(f=>f.species===id).length+1>=d.group,residents.filter(f=>f.species===id).length+1+' same-species fish after receiving','>= '+d.group,'Use a destination that meets the existing species group requirement.');
  add('keeper','Keeper access',s.level>=d.level,number(s.level),'Level >= '+d.level,'Reach the required Keeper level; receiving does not bypass existing species gates.');
  // Preserve every existing store/biology rejection, including specialist,
  // predator, toxin, reserved brood and species-only home restrictions.
  const represented=/safe purchase range|dissolved oxygen|Lower ammonia|swimming space|Requires [\d.]+ gal|Prepare and cycle|Reduce ammonia|stocking load|entity limit|rock shelter|social species|Requires keeper level|Freshwater/;
  for(const reason of base.reasons)if(!represented.test(reason))add('existing-'+checks.length,'Existing species safeguard',false,residents.length+' resident fish; '+t.flora.length+' corals; '+(t.invertebrates||[]).filter(f=>!f.dead).length+' invertebrates; '+t.eggs.length+' broods',reason,'Resolve the stated species safeguard; it is rechecked on transfer.');
  const failed=checks.filter(c=>!c.ok),reasons=failed.map(c=>c.label+': actual '+c.actual+'; requires '+c.required+'.');
  // Never silently drop an existing rejection if its explanation mapping changes.
  if(!base.ok&&!failed.length)reasons.push(...base.reasons);
  return {ok:base.ok&&!failed.length,reasons,warnings:[...new Set([...warnings,...base.warnings])],checks};
 }
 function destinations(s,id){return s.tanks.map(t=>({tank:t,report:report(s,id,t.id)}));}
 function holding(s,o){const left=Math.max(0,o.recovery.item.expiresAt-s.time);return {remaining:left,expired:left<=0,text:Math.floor(left/60)+'h '+Math.floor(left%60)+'m game time (~'+Math.ceil(left/AL.Config.minutesPerSecond)+' real seconds at 1×)'};}
 return {report,destinations,holding};
})();
