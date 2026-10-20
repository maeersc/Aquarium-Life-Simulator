"use strict";
// Marine equipment only. Biological RNG, the game clock and physical ownership are unchanged.
AL.EquipmentReliability=(()=>{
 const K=AL.Core,D=AL.Data,Y=365*24,GAMMA=0.892979511569249;
 const profiles={
  heater:{years:5,interval:365,parts:{element:1,thermostat:.8}},
  flow:{years:6,interval:180,parts:{motor:.7,impeller:1.3}},
  filter:{years:7.5,interval:180,parts:{housing:.25,impeller:1}},
  skimmer:{years:7.5,interval:90,parts:{pump:.8,intake:1.2}},
  light:{years:7.5,interval:365,duty:10/24,parts:{LEDs:1,driver:.8}},
  reefLight:{years:7.5,interval:365,duty:10/24,parts:{LEDs:1,driver:.8}},
  chiller:{years:7.5,interval:180,parts:{compressor:.8,heatExchanger:1}},
  feeder:{years:4.5,interval:120,parts:{motor:.8,dispenser:1.1}},
  air:{years:4.5,interval:180,parts:{motor:.7,diaphragm:1.3}},
  dosing:{years:6,interval:180,parts:{motor:.8,tubing:1.3}},
  containment:{years:10,interval:365,parts:{housing:.3,interlock:1}}
 };
 const states=['working','temporary-malfunction','repair-required','beyond-repair'];
 const partNames={element:'heating element',thermostat:'thermostat',motor:'motor',impeller:'impeller',housing:'housing',pump:'pump',intake:'intake',LEDs:'LED array',driver:'LED driver',compressor:'compressor',heatExchanger:'heat exchanger',dispenser:'dispenser',diaphragm:'diaphragm',tubing:'tubing',interlock:'interlock'};
 function random(r){let n=(r.seed+Math.imul(++r.draw,0x9e3779b9))>>>0;n=Math.imul(n^(n>>>16),0x21f0aaad);n=Math.imul(n^(n>>>15),0x735a2d97);return (((n^(n>>>15))>>>0)+.5)/4294967296;}
 const threshold=r=>-Math.log(random(r));
 function initialize(s,e,fresh=false){if(e.reliability!==undefined)return e.reliability;const r={version:1,legacy:!fresh,baselineCondition:e.durability,quality:typeof e.quality==='number'?K.clamp(e.quality,.5,1.5):1,seed:AL.Random.hash((s.accountId||s.worldId||s.seed)+':'+e.id+':equipment'),draw:0,trackedHours:0,operatingHours:0,effectiveHours:0,maintenanceHours:0,maintenance:100,componentStart:0,state:e.durability>0?'working':'repair-required',failurePart:null,failures:0,repairs:0,lastEnd:null,cycles:0,wasOperating:false,warning:false,critical:false,history:[],parts:Object.fromEntries(Object.keys(profiles[e.type].parts).map(k=>[k,e.durability]))};r.lifeThreshold=threshold(r);r.componentThreshold=threshold(r);e.reliability=r;return r;}
 function migrate(s){if(!s?.tanks)return;s.equipmentReliability??={version:1,nextEvent:1,events:[]};for(const t of s.tanks)if(t.water==='marine')for(const e of t.equipment)initialize(s,e);for(const e of s.ownedEquipment||[])initialize(s,e);}
 function operational(e,t){return !!e.enabled&&e.durability>0&&(t?.water==='fresh'||!e.reliability||e.reliability.state==='working');}
 function efficiency(e,t){if(!operational(e,t))return 0;if(t?.water==='fresh'||!e.reliability)return e.durability/100;const r=e.reliability;
  const physical=['light','reefLight'].includes(e.type)?Math.sqrt(e.durability/100):Math.min(1,e.durability/80);
  return physical*(.6+.4*Math.min(1,r.maintenance/70));
 }
 function status(e,t){const r=e.reliability;if(!e.enabled)return 'Off';if(!r)return e.durability>0?'Working normally':'Repair required';if(r.state==='beyond-repair')return 'Failed beyond repair';if(r.state==='repair-required'||e.durability<=0)return 'Repair required';if(r.state==='temporary-malfunction')return 'Temporary malfunction';if(efficiency(e,t)<.9)return 'Reduced efficiency';return r.maintenance<=70?'Maintenance recommended':'Working normally';}
 const eta=e=>profiles[e.type].years*Y/GAMMA*e.reliability.quality;
 // Integral of squared dirt burden below 70% maintenance: exact across step partitions.
 function dirt(hours,p){const k=-Math.log(.7)/(p.interval*24),x=Math.max(0,hours-p.interval*24);if(x===0)return 0;return Math.max(0,x-2*(-Math.expm1(-k*x))/k+(-Math.expm1(-2*k*x))/(2*k));}
 function exposure(e,h,environment){const r=e.reliability,p=profiles[e.type],damage=1+2*Math.pow(1-r.baselineCondition/100,2);return damage*(h*(1+environment)+6*(dirt(r.maintenanceHours+h,p)-dirt(r.maintenanceHours,p)));}
 function componentHazard(age,e){const x=age/eta(e);return x/4+.08*x*x;}
 function componentLimit(e){const r=e.reliability,z=r.componentThreshold+componentHazard(r.componentStart,e);return eta(e)*(2*z/(.25+Math.sqrt(.0625+.32*z)));}
 function operatingHours(t,e,start,end){const h=(end-start)/60;if(!e.enabled)return 0;if(!['light','reefLight'].includes(e.type))return h;if(t.lightMode==='off')return 0;if(t.lightMode==='on')return h;
  const length=t.lightHours,left=12-length/2,F=m=>{const d=Math.floor(m/1440),hour=(m-d*1440)/60;return d*length+K.clamp(hour-left,0,length);};return F(end)-F(start);
 }
 function event(s,t,e,kind,message,time=s.time){const ledger=s.equipmentReliability,r=e.reliability,row={id:'equipment-event-'+ledger.nextEvent++,equipmentId:e.id,type:e.type,tankId:t.id,tankName:t.name,time,kind,message,condition:e.durability,maintenance:r.maintenance,state:r.state,operatingHours:r.operatingHours};ledger.events.push(row);ledger.events=ledger.events.slice(-600);r.history.push({...row});r.history=r.history.slice(-40);K.log(s,t.name+': '+D.equipment[e.type].name+' — '+message,kind==='failure'?'danger':kind==='maintenance-warning'?'warning':'info');if(kind==='failure')AL.Mortality?.event?.(s,t,'equipmentFailure',{equipmentId:e.id,equipmentType:e.type,state:r.state,part:r.failurePart,condition:e.durability});return row;}
 function advance(s,t,e,h){if(t.water!=='marine')return;const r=initialize(s,e),end=s.time,start=end-h*60,from=r.lastEnd===null?start:Math.max(start,r.lastEnd);if(from>=end)return;r.lastEnd=end;r.trackedHours+=(end-from)/60;
  if(!operational(e,t)){r.wasOperating=false;return;}let active=operatingHours(t,e,from,end);if(!(active>0)){r.wasOperating=false;return;}if(!r.wasOperating)r.cycles++;r.wasOperating=true;
  const p=profiles[e.type],normalized=active/(p.duty||1),w=t.waterParams,environment=K.clamp((w.organic||0)/100,0,1)+K.clamp(Math.max(0,(w.temperature||25)-32)/20,0,1);
  const oldAge=r.effectiveHours,limitLife=eta(e)*Math.cbrt(r.lifeThreshold),limitComponent=componentLimit(e),limit=Math.min(limitLife,limitComponent),added=exposure(e,normalized,environment);let duration=normalized;
  if(oldAge+added>=limit){let lo=0,hi=normalized;for(let i=0;i<45;i++){const mid=(lo+hi)/2;if(oldAge+exposure(e,mid,environment)<limit)lo=mid;else hi=mid;}duration=(lo+hi)/2;}
  let observedTime=end;if(duration<normalized){let lo=from,hi=end;const required=duration*(p.duty||1);for(let i=0;i<45;i++){const mid=(lo+hi)/2;if(operatingHours(t,e,from,mid)<required)lo=mid;else hi=mid;}observedTime=(lo+hi)/2;}
  const increase=exposure(e,duration,environment);r.effectiveHours+=increase;r.operatingHours+=duration*(p.duty||1);r.maintenanceHours+=duration;r.maintenance=100*Math.exp(Math.log(.7)*r.maintenanceHours/(p.interval*24));
  const wear=Math.log(.8)/(p.years*Y*r.quality);e.durability=Math.max(1e-9,e.durability*Math.exp(wear*increase));for(const [part,rate]of Object.entries(p.parts))r.parts[part]=Math.max(1e-9,r.parts[part]*Math.exp(wear*increase*rate));
  if(!r.warning&&r.maintenance<=70){r.warning=true;event(s,t,e,'maintenance-warning','Maintenance recommended; inspect and clean before performance deteriorates.',observedTime);}if(!r.critical&&r.maintenance<=30){r.critical=true;event(s,t,e,'maintenance-warning','Maintenance is seriously overdue; output and reliability are reduced.',observedTime);}
  if(oldAge+added+1e-8>=limit){r.failures++;r.failurePart=Object.keys(p.parts)[Math.floor(random(r)*Object.keys(p.parts).length)];r.state=limitLife<=limitComponent?'beyond-repair':random(r)<.6?'temporary-malfunction':'repair-required';
   event(s,t,e,'failure',r.state==='beyond-repair'?'Major component/chassis failure; replacement required.':r.state==='temporary-malfunction'?'Temporary '+partNames[r.failurePart]+' malfunction; maintenance required.':partNames[r.failurePart]+' malfunction; component repair required.',observedTime);r.wasOperating=false;
  }
 }
 function step(s,t,h){if(t.water!=='marine')return;migrateLedger(s);for(const e of t.equipment)advance(s,t,e,h);}
 function migrateLedger(s){s.equipmentReliability??={version:1,nextEvent:1,events:[]};}
 function quote(e,repair=false){const r=e.reliability,d=D.equipment[e.type],loss=repair?Math.max(25,100-(r?.parts[r.failurePart]??e.durability)):100-(r?.maintenance??100);return Math.ceil(loss/100*d.price*.3*Math.max(1,e.capacity/d.capacity));}
 function find(t,a){return t.equipment.find(e=>a.id?e.id===a.id:e.type===a.type);}
 function maintain(s,t,a){const e=find(t,a);if(!e)throw Error('Choose an installed device.');const r=initialize(s,e);if(['beyond-repair','repair-required'].includes(r.state)||e.durability<=0)throw Error('This device needs repair or replacement, not cleaning.');if(r.maintenance>95&&r.state!=='temporary-malfunction')throw Error('Maintenance is not needed yet.');K.pay(s,quote(e));r.maintenanceHours=0;r.maintenance=100;r.warning=r.critical=false;if(r.state==='temporary-malfunction'){r.state='working';r.componentStart=r.effectiveHours;r.componentThreshold=threshold(r);r.failurePart=null;}event(s,t,e,'maintenance',e.type==='filter'?'Cleaned mechanical intake/media; established biological media and bacteria preserved. Physical wear unchanged.':'Cleaned/inspected accessible parts and intakes. Physical wear unchanged.');}
 function repair(s,t,a){const e=find(t,a);if(!e)throw Error('Choose an installed device.');const r=initialize(s,e);if(r.state==='beyond-repair')throw Error('This unit is beyond repair. Remove it and install a replacement.');if(r.state!=='repair-required')throw Error('No repairable component fault has been identified.');K.pay(s,quote(e,true));const part=r.failurePart||Object.keys(r.parts)[0];r.parts[part]=80;if(e.durability===0){e.durability=25;r.baselineCondition=25;}r.repairs++;r.state='working';r.failurePart=null;r.componentStart=r.effectiveHours;r.componentThreshold=threshold(r);event(s,t,e,'repair','Repaired '+(partNames[part]||part)+'; unit identity and tracked age preserved. The chassis is not new.');}
 function validate(s){const all=[...s.tanks.filter(t=>t.water==='marine').flatMap(t=>t.equipment),...(s.ownedEquipment||[])],ledger=s.equipmentReliability;if(!ledger||ledger.version!==1||!Number.isSafeInteger(ledger.nextEvent)||ledger.nextEvent<1||!Array.isArray(ledger.events)||ledger.events.length>600)throw Error('Invalid equipment reliability ledger.');
  const finite=(v,min,max)=>typeof v==='number'&&Number.isFinite(v)&&v>=min&&v<=max;
  function row(v){return v&&typeof v.id==='string'&&typeof v.equipmentId==='string'&&D.equipment[v.type]&&typeof v.tankId==='string'&&typeof v.tankName==='string'&&finite(v.time,0,s.time)&&['maintenance','repair','failure','maintenance-warning'].includes(v.kind)&&typeof v.message==='string'&&v.message.length<=1000&&finite(v.condition,0,100)&&finite(v.maintenance,0,100)&&states.includes(v.state)&&finite(v.operatingHours,0,1e12);}
  if(ledger.events.some(v=>!row(v)||!/^equipment-event-[1-9]\d*$/.test(v.id)||Number(v.id.split('-').at(-1))>=ledger.nextEvent)||new Set(ledger.events.map(v=>v.id)).size!==ledger.events.length)throw Error('Invalid equipment history.');
  for(const e of all){const r=e.reliability,p=profiles[e.type];if(!r||r.version!==1||typeof r.legacy!=='boolean'||!states.includes(r.state)||!finite(r.baselineCondition,0,100)||!finite(r.quality,.5,1.5)||!Number.isInteger(r.seed)||r.seed<0||r.seed>4294967295||!Number.isSafeInteger(r.draw)||r.draw<2||!finite(r.lifeThreshold,Number.MIN_VALUE,1000)||!finite(r.componentThreshold,Number.MIN_VALUE,1000)||!Array.isArray(r.history)||r.history.length>40||r.history.some(v=>!row(v)||v.equipmentId!==e.id)||r.failurePart!==null&&!Object.hasOwn(p.parts,r.failurePart))throw Error('Invalid equipment reliability instance.');
   for(const key of ['trackedHours','operatingHours','effectiveHours','maintenanceHours','componentStart'])if(!finite(r[key],0,1e12))throw Error('Invalid equipment age.');if(!finite(r.maintenance,0,100)||r.componentStart>r.effectiveHours||r.lastEnd!==null&&!finite(r.lastEnd,0,s.time))throw Error('Invalid equipment maintenance checkpoint.');for(const key of ['failures','repairs','cycles'])if(!Number.isSafeInteger(r[key])||r[key]<0)throw Error('Invalid equipment counter.');for(const key of ['wasOperating','warning','critical'])if(typeof r[key]!=='boolean')throw Error('Invalid equipment status.');if(!r.parts||Object.keys(r.parts).length!==Object.keys(p.parts).length||Object.keys(p.parts).some(k=>!finite(r.parts[k],0,100)))throw Error('Invalid equipment component condition.');
  }
 }
 return {profiles,partNames,Y,GAMMA,initialize,migrate,operational,efficiency,status,advance,step,maintain,repair,quote,validate,eta};
})();
