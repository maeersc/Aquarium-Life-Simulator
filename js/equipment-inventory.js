"use strict";
// Arrays are authoritative physical locations. Never infer installation from profile ownership.
AL.Inventory=(()=>{
 const K=AL.Core,D=AL.Data;
 function migrate(s){
  s.ownedEquipment??=[];s.ownedObjects??=[];
  // Only allocate missing legacy IDs; existing identities and all attributes survive.
  const used=new Set();function scan(o){if(!o||typeof o!=='object')return;if(typeof o.id==='string')used.add(o.id);for(const v of Object.values(o))if(v&&typeof v==='object')scan(v);}scan(s);
  for(const e of [...s.tanks.flatMap(t=>t.equipment),...s.ownedEquipment]){if(e.id===undefined||e.id===null){do{e.id=K.id(s,'equipment');}while(used.has(e.id));used.add(e.id);}}
  s.itemLocationVersion??=1;
 }
 function equipmentReport(s,e,t){const reasons=[],d=e&&D.equipment[e.type];
  if(!e||!d)reasons.push('Stored equipment no longer exists.');
  if(!t||!s.tanks.includes(t))reasons.push('Choose an owned aquarium.');
  if(t){if(t.water!=='marine')reasons.push(AL.Update29.lockText);if(d?.water&&d.water!==t.water)reasons.push('Requires '+d.water+' water.');
   if(e&&e.capacity+.000001<t.volume)reasons.push('Rated '+AL.Units.volume(e.capacity)+'; aquarium requires '+AL.Units.volume(t.volume)+' capacity.');
   if(t.equipment.length>=20)reasons.push('All 20 equipment positions are occupied.');if(e&&t.equipment.some(n=>n.type===e.type))reasons.push('A '+d.name+' is already installed; remove it first.');
  }return {ok:!reasons.length,reasons};
 }
 function objectReport(s,o,t){const reasons=[];if(!o)reasons.push('Stored object no longer exists.');if(!t||!s.tanks.includes(t))reasons.push('Choose an owned aquarium.');
  if(t){if(t.water!=='marine')reasons.push(AL.Update29.lockText);if(o?.kind==='rock'&&(t.hardscape||[]).length>=20)reasons.push('Maximum of 20 hardscape pieces.');if(o?.kind==='rack'&&(t.mounts||[]).length>=4)reasons.push('Maximum of four mounted frag racks.');if(o?.kind==='decor'&&t.decorations.length>=12)reasons.push('Maximum of 12 decorations.');}return {ok:!reasons.length,reasons};
 }
 function buy(s,t,a){const d=D.equipment[a.type],m=a.heaterModel!==undefined?AL.Heaters.get(a.heaterModel):null;
  if(!d||a.heaterModel!==undefined&&(!m||a.type!=='heater'))throw Error('Unknown equipment model.');
  if(t.water!=='marine'||d.water&&d.water!==t.water)throw Error('Choose a compatible saltwater sizing aquarium.');
  if(s.ownedEquipment.length>=50)throw Error('Equipment storage is full (50 items).');if(!(s.stock[a.type]>0))throw Error('Sold out.');
  const capacity=m?.capacity||Math.max(d.capacity,t.volume),price=m?.price||Math.ceil(d.price*Math.max(1,t.volume/d.capacity));K.pay(s,price);s.stock[a.type]--;
  const e={id:K.id(s,'equipment'),type:a.type,capacity,durability:100,enabled:true,...(m?{heaterModel:m.id}: {})};
  if(['heater','chiller'].includes(a.type))e.temperatureTarget=t.temperatureTarget;
  s.ownedEquipment.push(e);s.stats.equipmentBought++;K.log(s,d.name+' purchased into Equipment → Inventory.');
 }
 function install(s,t,a){const e=s.ownedEquipment.find(e=>e.id===a.id),r=equipmentReport(s,e,t);if(!r.ok)throw Error(r.reasons.join(' '));t.equipment.push(e);s.ownedEquipment=s.ownedEquipment.filter(n=>n!==e);K.log(s,D.equipment[e.type].name+' installed in '+t.name+'.');}
 function installed(t,a){return t.equipment.find(e=>a.id?e.id===a.id:e.type===a.type);}
 function retainThermostat(e,t){if(['heater','chiller'].includes(e.type))e.temperatureTarget??=t.temperatureTarget;}
 function remove(s,t,a){const e=installed(t,a);if(!e)throw Error('Equipment no longer installed.');if(a.confirmed!==true)throw Error('Confirm removal: this aquarium loses the equipment’s life-support effects.');if(s.ownedEquipment.length>=50)throw Error('Equipment storage is full.');retainThermostat(e,t);t.equipment=t.equipment.filter(n=>n!==e);s.ownedEquipment.push(e);K.log(s,D.equipment[e.type].name+' removed from '+t.name+' into storage.','warning');}
 function move(s,t,a){const e=installed(t,a),target=s.tanks.find(n=>n.id===a.target);if(!e||target===t)throw Error('Choose another aquarium.');const r=equipmentReport(s,e,target);if(!r.ok)throw Error(r.reasons.join(' '));if(a.confirmed!==true)throw Error('Confirm transfer: the source aquarium loses this equipment’s effects.');retainThermostat(e,t);t.equipment=t.equipment.filter(n=>n!==e);target.equipment.push(e);K.log(s,D.equipment[e.type].name+' transferred from '+t.name+' to '+target.name+'.','warning');}
 function thermostat(s,t,a){const e=installed(t,a),v=Number(a.temperature);if(!e||!['heater','chiller'].includes(e.type)||!Number.isFinite(v)||v<18||v>30)throw Error('Choose an installed heater or chiller and a thermostat from 18–30 °C.');e.temperatureTarget=v;t.temperatureTarget=v;K.log(s,D.equipment[e.type].name+' thermostat set to '+v+' °C in '+t.name+'. Water changes gradually.');}
 function removeObject(s,t,a){const list=a.kind==='rock'?t.hardscape:a.kind==='decor'?t.decorations:a.kind==='rack'?t.mounts:null,o=list?.find(o=>o.id===a.id);if(!o)throw Error('Placed object not found.');
  if(t.flora.some(f=>f.attachment?.supportId===o.id)||t.eggs.some(e=>e.anchor?.supportId===o.id))throw Error('Relocate attached corals or wait for attached clutches to hatch before removing this support.');
  if(o.recoveredRock){AL.DiveExpansion.removeRock(s,t,o);}else{if(s.ownedObjects.length>=100)throw Error('Object storage is full.');s.ownedObjects.push({...o,kind:a.kind});}
  if(a.kind==='rock')t.hardscape=list.filter(n=>n!==o);else if(a.kind==='rack')t.mounts=list.filter(n=>n!==o);else t.decorations=list.filter(n=>n!==o);K.log(s,'Object returned from '+t.name+' to Inventory.');
 }
 function place(s,t,a){const o=s.ownedObjects.find(o=>o.id===a.id),r=objectReport(s,o,t);if(!r.ok)throw Error(r.reasons.join(' '));if(o.kind==='rack'){const {kind,...rack}=o;t.mounts.push({...rack,mounted:true});s.ownedObjects=s.ownedObjects.filter(n=>n!==o);K.log(s,'Stored frag rack remounted in '+t.name+'.');return;}const p=AL.Placement.report(t,{...o,z:Number(a.z??.5)},Number(a.x));if(!p.ok)throw Error(p.reasons.join(' '));
  const {kind,...item}=o;Object.assign(item,p.position);if(kind==='rock'){item.baseOffset??=.0125;t.hardscape.push(item);}else t.decorations.push(item);s.ownedObjects=s.ownedObjects.filter(n=>n!==o);K.log(s,'Stored object placed in '+t.name+'.');
 }
 function validate(s,identity){if(s.itemLocationVersion!==1||!Array.isArray(s.ownedObjects)||s.ownedObjects.length>100)throw Error('Invalid physical storage.');
  for(const e of [...s.tanks.flatMap(t=>t.equipment),...(s.ownedEquipment||[])])if(e.temperatureTarget!==undefined&&(!['heater','chiller'].includes(e.type)||!Number.isFinite(e.temperatureTarget)||e.temperatureTarget<18||e.temperatureTarget>30))throw Error('Invalid individual thermostat.');
  for(const o of s.ownedObjects){identity(o.id);if(o.kind==='rock'&&(!AL.Habitat.rockProducts[o.group]||!Number.isInteger(o.variant)||o.variant<0||o.variant>3||o.width!==[38,55,77,90][o.variant])||o.kind==='decor'&&!['cave','wood','lantern'].includes(o.type)||o.kind==='rack'&&(!['back','left','right'].includes(o.glass)||!Number.isFinite(o.x)||o.x<.05||o.x>.95||!Number.isFinite(o.y)||o.y<.25||o.y>.8)||!['rock','decor','rack'].includes(o.kind))throw Error('Invalid stored object.');}
 }
 return {migrate,equipmentReport,objectReport,buy,install,remove,move,thermostat,removeObject,place,validate};
})();
