from pathlib import Path
r=Path(__file__).resolve().parents[2]
def edit(n,a,b):
 p=r/n;s=p.read_text(encoding='utf8');assert a in s,(n,a[:70]);p.write_text(s.replace(a,b,1),encoding='utf8')
edit('js/diving-receiving.js',' function report(s,id,tankId){',' function fishReport(s,id,tankId){')
p=r/'js/diving-receiving.js';s=p.read_text(encoding='utf8');a=s.index(' function destinations(')
s=s[:a]+''' function resolve(id){const found=[['fish',D.species[id]],['coral',D.flora[id]],['invertebrate',D.invertebrates[id]]].filter(([,d])=>!!d);return found.length===1?{kind:found[0][0],definition:found[0][1],id}:null;}
 function failure(message){return {ok:false,reasons:[message],warnings:[],checks:[{id:'mapping',label:'Species mapping',ok:false,actual:'Missing, ambiguous or unsupported definition',required:message,help:'The content profile must be corrected; another species is never substituted.'}]};}
 function report(s,id,tankId,position=null){const entry=resolve(id);if(!entry||entry.definition.water!=='marine')return failure('Choose one uniquely mapped implemented marine livestock species.');if(entry.kind==='fish')return fishReport(s,id,tankId);return otherReport(s,entry,tankId,position);}
 function otherReport(s,{id,kind,definition:d},tankId,position){const t=s.tanks.find(t=>t.id===tankId);if(!t)return failure('Choose an owned receiving aquarium.');const coral=kind==='coral',w=t.waterParams,c=D.coralCare,checks=[],warnings=[],add=(id,label,ok,actual,required,help)=>checks.push({id,label,ok:!!ok,actual:String(actual),required:String(required),help:help||'Correct this requirement or choose another compatible aquarium.'});
  const base=AL.StoreRules.report(s,t,coral?'buyFlora':'buyInvertebrate',coral?{type:id,receiving:true}:{species:id,count:1});
  add('habitat','Water classification',t.water==='marine',t.water==='marine'?'Saltwater':'Freshwater','Saltwater; freshwater receiving remains locked');
  add('volume','Water volume',Number.isFinite(d.minTank)&&t.volume>=d.minTank,gal(t.volume),Number.isFinite(d.minTank)?'>= '+gal(d.minTank):'A species-specific minimum volume must be registered');
  for(const [key,label,unit,range]of [['temperature','Actual water temperature','°C',d.temp||(coral?c.temperature:null)],['salinity','Salinity','ppt',d.salinity||(coral?c.salinity:null)],['ph','pH','',d.ph||(coral?[8,8.4]:null)]])add(key,label,Array.isArray(range)&&Number.isFinite(w[key])&&w[key]>=range[0]&&w[key]<=range[1],number(w[key])+' '+unit,range?range.join('–')+' '+unit+' inclusive':'Register this species range');
  for(const [key,label,limit,low]of [['ammonia','Ammonia',.15,false],['nitrite','Nitrite',.15,false],['oxygen','Dissolved oxygen',coral?5.5:6,true]])add(key,label,Number.isFinite(w[key])&&(low?w[key]>=limit:w[key]<=limit),number(w[key])+' mg/L',(low?'>= ':'<= ')+limit+' mg/L');
  add('prepared','Water prepared',t.prepared&&!t.emptyDry,t.prepared&&!t.emptyDry?'Prepared water':'Unprepared / dry','Prepared saltwater');
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
 function mountCandidates(t,id){const entry=resolve(id);if(entry?.kind!=='coral')return [null];const points=[];for(const support of [...(t.mounts||[]),...(t.hardscape||[])])for(const offset of [0,-.035,.035])points.push({x:K.clamp(support.x+offset,.05,.95),y:support.y-.015,z:support.z??.5});if(AL.Habitat.definitions[id]?.allowed.includes('sand'))for(const x of [.2,.4,.6,.8])points.push({x,y:AL.Habitat.plane(t,.5),z:.5});return points;}
 function destinations(s,id){return s.tanks.map(t=>{const mounts=mountCandidates(t,id).filter(p=>report(s,id,t.id,p).ok),position=mounts[0]??null;return {tank:t,position,mounts,report:report(s,id,t.id,position)};});}
 function registryAudit(){const errors=[];for(const p of AL.DivingData.species){const entry=resolve(p.id);if(!entry||entry.definition.water!=='marine'||!Number.isFinite(entry.definition.minTank)||entry.definition.purchaseVerified===false||!Number.isFinite(p.sensitivity)||!Number.isFinite(p.transport))errors.push({id:p.id,reason:'Incomplete, ambiguous, held or missing marine receiving profile'});}return errors;}
''' +s[s.index(' function holding(',a):]
s=s.replace('return {report,destinations,holding};','return {report,destinations,holding,resolve,mountCandidates,registryAudit};')
p.write_text(s,encoding='utf8')
edit('js/store-rules.js',"if(t.kind!=='reef'||t.bacteria<.65||t.bacteria2<.5)","if((t.kind!=='reef'&&!(a.receiving===true&&t.kind==='quarantine'&&!AL.Core.alive(t).length&&!(t.invertebrates||[]).some(f=>!f.dead&&f.hp>0)&&!t.eggs.some(e=>e.viability>0)&&!(t.nurseries||[]).some(n=>!n.dead&&n.hp>0)))||t.bacteria<.65||t.bacteria2<.5)")
p=r/'js/diving.js';s=p.read_text(encoding='utf8')
s=s.replace("const category=id=>D.species[id]?'fish':D.flora[id]?'coral':'invertebrate';","const category=id=>D.species[id]?'fish':D.flora[id]?'coral':D.invertebrates[id]?'invertebrate':null;")
s=s.replace("const d=definition(p.id);Object.assign(p,","const d=definition(p.id);if(!d||!category(p.id))continue;Object.assign(p,",1)
s=s.replace("return R.species.filter(p=>p.regions.includes(region)","return R.species.filter(p=>definition(p.id)?.water==='marine'&&definition(p.id).purchaseVerified!==false&&category(p.id)&&p.regions.includes(region)",1)
a=s.index(' function receiving(');b=s.index(' function launch(',a)
s=s[:a]+''' function receiving(s,id,tankId,position){return AL.DiveReceiving.report(s,id,tankId,position);}
 function positions(s,t,id){return AL.DiveReceiving.mountCandidates(t,id).filter(p=>receiving(s,id,t.id,p).ok);}
''' +s[b:]
s=s.replace("function receive(s,a,item){const d=", "function receive(s,a,item){if(!byId[item.species]||!category(item.species)||!eligible(a.region,a.mode,true).some(p=>p.id===item.species))throw Error('Missing or geographically ineligible livestock receiving profile.');if(a.objects?.some(o=>o.objectId===item.id&&o.id))throw Error('This specimen was already received.');const d=",1)
p.write_text(s,encoding='utf8')
edit('build.py',"ROOT / 'DIVING_RECEIVING_REPAIR_REPORT.md'", "ROOT / 'DIVING_RECEIVING_REPAIR_REPORT.md', ROOT / 'GLOBAL_DIVING_RECEIVING_REPORT.md'")
edit('tests/browser_qa.py',"        if '--receiving' in sys.argv:","        if '--global-receiving' in sys.argv:\n            import global_receiving_qa\n            return global_receiving_qa.run(client,ROOT,NAME)\n        if '--receiving' in sys.argv:")
edit('tests/package.py',"'receiving-evidence']", "'receiving-evidence','global-receiving-evidence']")
