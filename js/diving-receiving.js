"use strict";
// Explain the same checks used by the final transfer; never hide owned tanks.
AL.DiveReceiving=(()=>{
 const K=AL.Core,D=AL.Data,units=3.785411784;
 const number=n=>Number.isFinite(n)?String(n):'Unavailable',gal=n=>Number.isFinite(n)?(n/units).toFixed(3)+' US gal':'Unavailable';
 function fishReport(s,id,tankId,incoming=1){const t=s.tanks.find(t=>t.id===tankId),d=D.species[id],checks=[],warnings=[];
  const add=(id,label,ok,actual,required,help)=>checks.push({id,label,ok:!!ok,actual:String(actual),required:String(required),help});
  if(!Number.isInteger(incoming)||incoming<1||incoming>24)return failure('Choose a supported incoming fish count from1 to24.');
  if(!t||!d)return {ok:false,reasons:[!t?'Choose an owned receiving aquarium.':'Fish species is not implemented.'],warnings,checks};
  const w=t.waterParams,base=AL.StoreRules.report(s,t,'buyFish',{species:id,count:incoming});
  add('habitat','Water classification',t.water===d.water&&t.water==='marine',t.water==='marine'?'Saltwater':'Freshwater',d.water==='marine'?'Saltwater; freshwater receiving remains locked':'Freshwater is currently locked','Choose a saltwater aquarium.');
  add('volume','Water volume',t.volume>=d.minTank,gal(t.volume),'>= '+gal(d.minTank),'Choose a larger aquarium; nominal gallon labels do not change physical water volume.');
  for(const [key,label,unit,range] of [['temperature','Actual water temperature','°C',d.temp],['salinity','Salinity','ppt',d.salinity],['ph','pH','',d.ph]])add(key,label,Number.isFinite(w[key])&&w[key]>=range[0]&&w[key]<=range[1],number(w[key])+' '+unit,range[0]+'–'+range[1]+' '+unit+' inclusive','Correct the measured water reading; heater setpoint alone does not establish compatibility.');
  for(const [key,label,limit,lower] of [['ammonia','Ammonia',.15,false],['nitrite','Nitrite',.15,false],['oxygen','Dissolved oxygen',5.5,true]])add(key,label,Number.isFinite(w[key])&&(lower?w[key]>=limit:w[key]<=limit),number(w[key])+' mg/L',(lower?'>= ':'<= ')+limit+' mg/L',lower?'Restore aeration/circulation and inspect stocking.':'Finish cycling, check filtration and safely correct water chemistry.');
  add('prepared','Water prepared',AL.Preparation.prepared(t),AL.Preparation.state(t).label,'Prepared saltwater','Use aquarium setup to prepare the water.');
  add('bacteria','Ammonia-processing colony',t.bacteria>=.65,number(t.bacteria),'>= 0.65','Start or finish biological cycling; do not add fish to an uncycled tank.');
  add('bacteria2','Nitrite-processing colony',t.bacteria2>=.5,number(t.bacteria2),'>= 0.5','Allow both bacterial colonies to establish.');
  for(const [type,label]of [['filter','Filtration'],['flow','Circulation']]){const devices=t.equipment.filter(e=>e.type===type),capacity=K.capacity(t,type);add(type,label,K.has(t,type)&&capacity>0,devices.length?devices.map(e=>(e.enabled?'On':'Off')+', condition '+number(e.durability)+'%, rated '+gal(e.capacity)).join('; ')+'; effective '+gal(capacity):'Not installed','Installed, enabled and functioning '+(type==='filter'?'filter':'circulation pump'),'Install or enable the device and repair failed equipment.');if(capacity>0&&capacity<t.volume)warnings.push(label+' condition-adjusted capacity '+gal(capacity)+' is below aquarium '+gal(t.volume)+'. Maintain equipment and monitor water; this capacity warning is not a new full-output gate.');}
  const residents=K.alive(t),reserved=(AL.Breeding?.reservedLoad(t)||0)+t.eggs.filter(e=>e.viability>0).reduce((n,e)=>n+D.species[e.species].load*e.count,0)+(AL.Update29?.reservedLoad(t)||0)+(t.invertebrates||[]).filter(f=>!f.dead).reduce((n,f)=>n+D.invertebrates[f.invertebrate].load,0),adult=residents.reduce((n,f)=>n+D.species[f.species].load,0),limit=K.loadLimit(t);
  add('stocking','Adult stocking capacity',adult+reserved+d.load*incoming<=limit,number(adult)+' resident + '+number(reserved)+' reserved + '+number(d.load*incoming)+' incoming load','Combined adult load <= '+number(limit),'Move livestock to another compatible home or use a larger aquarium. Reserved eggs/offspring also occupy capacity.');
  const count=t.fish.length+(t.water==='marine'?t.eggs.filter(e=>e.viability>0).reduce((n,e)=>n+e.count,0)+(AL.Breeding?.reservedCount(t)||0):0)+incoming;
  add('entities','Livestock entity capacity',count<=AL.Config.maxFish,number(count)+' after receiving','<= '+AL.Config.maxFish+' fish slots including retained remains and reserved viable offspring','Use another aquarium with room for this specimen.');
  const courses=[...t.fish,...t.flora,...(t.invertebrates||[])].filter(f=>!f.dead&&f.hp>0&&f.healthState?.treatment).map(f=>AL.Health.products[f.healthState.treatment.product]);
  const restricted=courses.filter(p=>p?.quarantine);
  add('quarantine','Quarantine restrictions',restricted.length===0,restricted.length?'Active '+restricted.map(p=>p.name).join(', '):t.kind==='quarantine'?'Quarantine; no active restricted course':'Display / reef; no active restricted course','No introduction into an active restricted treatment course; quarantine is optional for this untreated catch','Finish the restricted course or choose a separate prepared, cycled compatible home. A valid quarantine receives the existing survival benefit; it does not waive habitat/water checks.');
  if(d.habitat==='rocks'||d.habitat==='sand'){const shelter=(t.hardscape?.length||0)+t.decorations.filter(x=>x.type==='cave').length;add('shelter','Rock shelter',shelter>0,shelter+' rock / cave shelter(s)','At least one rock shelter or cave','Place suitable rock or a rock cave using the normal aquarium placement tools.');}
  add('social','Species group',residents.filter(f=>f.species===id).length+incoming>=d.group,residents.filter(f=>f.species===id).length+incoming+' same-species fish after receiving','>= '+d.group,'Use a destination that meets the existing species group requirement.');
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
 function resolve(id){const found=[['fish',D.species[id]],['coral',D.flora[id]],['invertebrate',D.invertebrates[id]]].filter(([,d])=>!!d);return found.length===1?{kind:found[0][0],definition:found[0][1],id}:null;}
 function failure(message){return {ok:false,reasons:[message],warnings:[],checks:[{id:'mapping',label:'Species mapping',ok:false,actual:'Missing, ambiguous or unsupported definition',required:message,help:'The content profile must be corrected; another species is never substituted.'}]};}
 function report(s,id,tankId,position=null,incoming=1){const entry=resolve(id);if(!entry||entry.definition.water!=='marine')return failure('Choose one uniquely mapped implemented marine livestock species.');if(entry.kind==='fish')return fishReport(s,id,tankId,incoming);return otherReport(s,entry,tankId,position);}
 function otherReport(s,{id,kind,definition:d},tankId,position){const t=s.tanks.find(t=>t.id===tankId);if(!t)return failure('Choose an owned receiving aquarium.');const coral=kind==='coral',w=t.waterParams,c=D.coralCare,checks=[],warnings=[],add=(id,label,ok,actual,required,help)=>checks.push({id,label,ok:!!ok,actual:String(actual),required:String(required),help:help||'Correct this requirement or choose another compatible aquarium.'});
  const base=AL.StoreRules.report(s,t,coral?'buyFlora':'buyInvertebrate',coral?{type:id,receiving:true}:{species:id,count:1});
  add('habitat','Water classification',t.water==='marine',t.water==='marine'?'Saltwater':'Freshwater','Saltwater; freshwater receiving remains locked');
  add('volume','Water volume',Number.isFinite(d.minTank)&&t.volume>=d.minTank,gal(t.volume),Number.isFinite(d.minTank)?'>= '+gal(d.minTank):'A species-specific minimum volume must be registered');
  for(const [key,label,unit,range]of [['temperature','Actual water temperature','°C',d.temp||(coral?c.temperature:null)],['salinity','Salinity','ppt',d.salinity||(coral?c.salinity:null)],['ph','pH','',d.ph||(coral?[8,8.4]:null)]])add(key,label,Array.isArray(range)&&Number.isFinite(w[key])&&w[key]>=range[0]&&w[key]<=range[1],number(w[key])+' '+unit,range?range.join('–')+' '+unit+' inclusive':'Register this species range');
  for(const [key,label,limit,low]of [['ammonia','Ammonia',.15,false],['nitrite','Nitrite',.15,false],['oxygen','Dissolved oxygen',coral?5.5:6,true]])add(key,label,Number.isFinite(w[key])&&(low?w[key]>=limit:w[key]<=limit),number(w[key])+' mg/L',(low?'>= ':'<= ')+limit+' mg/L');
  add('prepared','Water prepared',AL.Preparation.prepared(t),AL.Preparation.state(t).label,'Prepared saltwater');
  for(const [key,label,minimum]of [['bacteria','Ammonia-processing colony',.65],['bacteria2','Nitrite-processing colony',.5]])add(key,label,t[key]>=minimum,number(t[key]),'>= '+minimum,'Finish biological cycling; both colonies are required.');
  for(const [type,label]of [['filter','Filtration'],['flow','Circulation']]){const capacity=K.capacity(t,type);add(type,label,K.has(t,type)&&capacity>0,t.equipment.filter(e=>e.type===type).map(e=>(e.enabled?'On':'Off')+', condition '+number(e.durability)+'%, rated '+gal(e.capacity)).join('; ')+'; effective '+gal(capacity),'Installed, enabled and functioning '+type);}
  const residents=[...t.fish,...t.flora,...(t.invertebrates||[])].filter(f=>!f.dead&&f.hp>0),courses=residents.map(f=>f.healthState?.treatment).filter(Boolean).map(tr=>AL.Health.products[tr.product]).filter(p=>p?.quarantine);
  add('quarantine','Quarantine restrictions',!courses.length,courses.length?'Active '+courses.map(p=>p.name).join(', '):t.kind+'; no active restricted medication','No new untreated livestock in active restricted medication; host-compatible quarantine only');
  add('keeper','Keeper access',s.level>=(d.level||1),s.level,'Level >= '+(d.level||1));
  if(coral){
   const onlyCoral=!K.alive(t).length&&!(t.invertebrates||[]).some(f=>!f.dead&&f.hp>0)&&!t.eggs.some(e=>e.viability>0)&&!(t.nurseries||[]).some(n=>!n.dead&&n.hp>0);
   add('reef','Coral receiving facility',t.kind==='reef'||t.kind==='quarantine'&&onlyCoral,t.kind+'; '+K.alive(t).length+' living fish; '+(t.invertebrates||[]).filter(f=>!f.dead&&f.hp>0).length+' invertebrates','Prepared reef or separate coral-only quarantine');
   for(const [key,label,minimum]of [['calcium','Calcium',c.minCalcium],['magnesium','Magnesium',c.minMagnesium]])add(key,label,w[key]>=minimum,number(w[key])+' mg/L','>= '+minimum+' mg/L');
   add('alkalinity','Alkalinity',w.alkalinity>=c.alkalinity[0]&&w.alkalinity<=c.alkalinity[1],number(w.alkalinity)+' dKH',c.alkalinity.join('–')+' dKH');
   add('nitrate','Nitrate',w.nitrate<=c.maxNitrate,number(w.nitrate)+' mg/L','<= '+c.maxNitrate+' mg/L');
   const cond=AL.Sim.floraConditions(s,t,{type:id,x:position?.x??.5,y:position?.y??.9,z:position?.z??.5,size:1,hp:100});
   add('light','Species daily light',cond.dailyLight>=d.light,number(cond.dailyLight),'>= '+number(d.light));
   add('species-flow','Species flow',cond.flow>=d.flow,number(cond.flow),'>= '+number(d.flow));
   const mount=position?AL.Habitat.placement(s,t,id,position.x,position.y,{z:position.z}):null;
   add('mount','Coral mounting position',!!mount?.ok,position?'x '+number(position.x)+', y '+number(position.y)+', depth '+number(position.z):'No supported mount selected',mount?.reasons.length?mount.reasons.join(' '):'Choose a supported species-appropriate mount with clearance','Place a permitted rock or rack, then explicitly choose a valid mount.');
   const limit=Math.min(35,Math.floor(t.volume/8));add('entities','Colony capacity',t.flora.length<limit,t.flora.length+' existing colonies','Existing colonies < '+limit);
  }else{
   const total=(t.invertebrates||[]).length+(t.nurseries||[]).filter(n=>!n.dead).length;add('entities','Invertebrate capacity',total<40,total+' adults / reserved nurseries','Existing adults / reserved nurseries < 40');
   const load=AL.Breeding?.admissionLoad(t)??K.load(t);add('stocking','Adult stocking capacity',load+d.load<=K.loadLimit(t),number(load)+' resident / reserved + '+number(d.load)+' incoming load','Combined load <= '+number(K.loadLimit(t)));
   const ratio=K.capacity(t,'flow')/t.volume;if(d.flow)add('species-flow','Species filter-feeding flow',K.has(t,'flow')&&ratio>=d.flow,number(ratio),'>= '+number(d.flow));
   if(['rock','rocks','sand'].includes(d.habitat)){const rocks=(t.hardscape?.length||0)+t.decorations.filter(x=>x.type==='cave').length;add('shelter','Habitat shelter',rocks>0,rocks+' rocks / caves','At least one rock shelter or cave');}
   if(d.habitat==='sand')add('substrate','Species substrate',(t.substrate?.depth??0)>=1.5,number(t.substrate?.depth??0)+' inches','>= 1.5 inches of soft sand');
  }
  // All existing species restrictions remain authoritative; append their exact
  // reason as a row rather than concealing or guessing an alternate requirement.
  for(const reason of base.reasons)add('existing-'+checks.length,'Existing species safeguard',false,'Species '+id+'; habitat age '+number(t.ecosystemAge)+' h; toxin '+number(t.boxToxin??0),reason);
  const failed=checks.filter(c=>!c.ok);return {ok:base.ok&&!failed.length,reasons:failed.map(c=>c.label+': actual '+c.actual+'; requires '+c.required+'.'),warnings:[...new Set([...warnings,...base.warnings])],checks};
 }
 function mountCandidates(t,id){const entry=resolve(id);if(entry?.kind!=='coral')return [null];const points=[],seen=new Set(),add=p=>{const key=[p.x,p.y,p.z].map(n=>Number(n).toFixed(8)).join(':');if(!seen.has(key)){seen.add(key);points.push(p);}};
  for(const support of [...(t.mounts||[]),...(t.hardscape||[])])for(const offset of [0,-.035,.035])add({x:K.clamp(support.x+offset,.05,.95),y:support.y-.015,z:support.z??.5});
  // A rock's anchor is not its top surface. Sample its existing collision
  // geometry, then let Habitat.placement enforce support and clearance.
  if(AL.Habitat.definitions[id]?.allowed.includes('rock'))for(const rock of t.hardscape||[]){const geometry=AL.HabitatGeometry[rock.group]?.[rock.variant];if(!geometry)continue;for(let px=16;px<177;px+=16){const spans=geometry.columns[px];if(!spans?.length)continue;add({x:rock.x-rock.width/960+(px+.5)/192*rock.width/480,y:(rock.y*240-rock.width*184/192+spans[0][0]/192*rock.width)/240,z:rock.z??.5});}}
  if(AL.Habitat.definitions[id]?.allowed.includes('sand'))for(const x of [.2,.4,.6,.8])add({x,y:AL.Habitat.plane(t,.5),z:.5});return points;
 }
 function destinations(s,id){return s.tanks.map(t=>{const mounts=mountCandidates(t,id).filter(p=>report(s,id,t.id,p).ok),position=mounts[0]??null;return {tank:t,position,mounts,report:report(s,id,t.id,position)};});}
 function registryAudit(){const errors=[];for(const p of AL.DivingData.species){const entry=resolve(p.id);if(!AL.Diving.profileValid(p)||!entry||entry.definition.water!=='marine'||!Number.isFinite(entry.definition.minTank)||!entry.definition.scientificName||entry.definition.purchaseVerified===false||!Number.isFinite(p.sensitivity)||!Number.isFinite(p.transport))errors.push({id:p.id,reason:'Incomplete, ambiguous, held or missing marine receiving profile'});}return errors;}
 function holding(s,o){const left=Math.max(0,o.recovery.item.expiresAt-s.time);return {remaining:left,expired:left<=0,text:Math.floor(left/60)+'h '+Math.floor(left%60)+'m game time (~'+Math.ceil(left/AL.Config.minutesPerSecond)+' real seconds at 1×)'};}
 return {report,destinations,holding,resolve,mountCandidates,registryAudit};
})();
