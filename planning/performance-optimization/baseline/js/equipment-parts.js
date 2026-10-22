"use strict";
// Catalogued external service parts; sealed assemblies require whole-unit replacement.
AL.EquipmentParts=(()=>{
 const D=AL.Data,K=AL.Core,R=AL.EquipmentReliability;
 D.parts=Object.freeze({
  'flow-impeller':{type:'flow',part:'impeller',name:'Circulation pump impeller',price:45},
  'filter-impeller':{type:'filter',part:'impeller',name:'Filter impeller',price:50},
  'skimmer-intake':{type:'skimmer',part:'intake',name:'Skimmer intake assembly',price:55},
  'skimmer-pump':{type:'skimmer',part:'pump',name:'Skimmer service pump',price:95},
  'air-diaphragm':{type:'air',part:'diaphragm',name:'Air-pump diaphragm',price:20},
  'feeder-dispenser':{type:'feeder',part:'dispenser',name:'Feeder dispensing cartridge',price:60},
  'dosing-tubing':{type:'dosing',part:'tubing',name:'Dosing tubing set',price:35}
 });
 function product(sku,rating){const d=D.parts[sku];if(!d||!Number.isFinite(rating)||rating<D.equipment[d.type].capacity||rating>100000)throw Error('Choose a catalogued part and valid equipment rating.');return {...d,sku,rating,id:sku+'@'+rating,price:Math.ceil(d.price*Math.max(1,rating/D.equipment[d.type].capacity))};}
 function migrate(s){s.equipmentParts??={version:1,inventory:{},day:Math.floor(s.time/1440),stock:Object.fromEntries(Object.keys(D.parts).map(id=>[id,30]))};const p=s.equipmentParts;if(p.day!==Math.floor(s.time/1440)){p.day=Math.floor(s.time/1440);for(const sku of Object.keys(D.parts))p.stock[sku]=30;}}
 function supported(e){return Object.entries(D.parts).filter(([,d])=>d.type===e.type).map(([sku])=>product(sku,Math.max(e.capacity,D.equipment[e.type].capacity)));}
 function buy(s,t,a){migrate(s);if(t?.water==='fresh')throw Error(AL.Update29.lockText);const p=product(a.sku,a.rating);if(s.equipmentParts.stock[p.sku]<1)throw Error('This part is sold out.');AL.Finance.change(s,-p.price,{category:'equipment',name:p.name,action:'buyEquipmentPart',partId:p.id,note:AL.Units.volume(p.rating)+' rated new part; catalog price'});s.stats.expenses+=p.price;s.equipmentParts.stock[p.sku]--;s.equipmentParts.inventory[p.id]=(s.equipmentParts.inventory[p.id]||0)+1;}
 function report(s,t,e,sku){const reasons=[],p=sku&&D.parts[sku]?product(sku,Math.max(e.capacity,D.equipment[e.type].capacity)):null,r=e.reliability;if(!p||p.type!==e.type)reasons.push('This device has no such supported replaceable part.');if(t.water!=='marine')reasons.push(AL.Update29.lockText);if(e.durability<=0||r.state==='beyond-repair')reasons.push('The chassis requires whole-unit replacement; replacing one part cannot restore it.');if(p&&r.parts[p.part]>95&&r.failurePart!==p.part)reasons.push('This component is not worn enough to need replacement.');return {ok:!reasons.length,reasons,product:p,owned:p?(s.equipmentParts.inventory[p.id]||0):0};}
 function replace(s,t,a){migrate(s);const e=t.equipment.find(e=>e.id===a.id);if(!e)throw Error('Choose an installed device.');const sku=a.sku||supported(e).find(p=>p.part===e.reliability.failurePart)?.sku,q=report(s,t,e,sku);if(!q.ok)throw Error(q.reasons.join(' '));const p=q.product;if(a.source==='inventory'){if(q.owned<1)throw Error('No matching rated replacement part is owned.');s.equipmentParts.inventory[p.id]--;}else {if(s.equipmentParts.stock[p.sku]<1)throw Error('This new part is sold out; use an owned matching part or wait for restock.');AL.Finance.change(s,-p.price,{category:'equipment',name:p.name,action:'replaceEquipmentPart',equipmentId:e.id,partId:p.id,note:'New-part catalog price; '+AL.Units.volume(p.rating)+' rating'});s.stats.expenses+=p.price;s.equipmentParts.stock[p.sku]--;}
  e.reliability.parts[p.part]=100;R.renewPart(s,t,e,p.part);K.log(s,p.name+' replaced in '+t.name+'. Chassis identity, condition and age retained.');
 }
 function validate(s){const p=s.equipmentParts;if(!p||p.version!==1||p.day!==Math.floor(s.time/1440)||!p.inventory||!p.stock)throw Error('Invalid replacement-part inventory.');for(const [id,n]of Object.entries(p.inventory)){const [sku,rating]=id.split('@'),d=product(sku,Number(rating));if(d.id!==id||!Number.isSafeInteger(n)||n<0||n>10000)throw Error('Invalid owned replacement part.');}for(const sku of Object.keys(D.parts))if(!Number.isInteger(p.stock[sku])||p.stock[sku]<0||p.stock[sku]>30)throw Error('Invalid replacement-part stock.');}
 return {product,migrate,supported,buy,report,replace,validate};
})();
