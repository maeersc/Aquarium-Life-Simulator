"use strict";
// Equipment levels, not keeper-level gates. Legacy heaters keep their exact rating.
AL.Heaters=(()=>{
 const K=AL.Core,D=AL.Data,liters=3.785411784;
 const models=[[5,20],[20,75],[75,250],[250,1000],[1000,3000],[3000,7500],[7500,15000]].map(([min,max],i)=>Object.freeze({id:'marine-heater-'+(i+1),level:i+1,minGallons:min,maxGallons:max,capacity:max*liters,price:Math.ceil(D.equipment.heater.price*Math.max(1,max*liters/D.equipment.heater.capacity)),name:'Level '+(i+1)+' Marine Heater',range:min.toLocaleString('en-US')+'–'+max.toLocaleString('en-US')+' gal'}));
 const get=id=>models.find(m=>m.id===id),recommended=t=>models.find(m=>m.capacity+.000001>=t.volume)||null;
 function products(s,t){const suggestion=recommended(t);return models.map(m=>({id:'equipment:heater:'+m.id,kind:'equipment',name:m.name+' · '+m.range,price:m.price,stock:s.stock.heater??0,action:'buyEquipment',args:{type:'heater',heaterModel:m.id},description:'Rated tank range '+m.range+'. Fixed '+m.maxGallons.toLocaleString('en-US')+' gal output capacity; does not expand when moved. Thermostat and condition govern real output. '+(suggestion?.id===m.id?'Recommended size for selected aquarium.':m.capacity<t.volume?'Stored on purchase; too small to install in the sizing aquarium.':'Larger than the recommended size for selected aquarium.'),habitat:'marine'}));}
 function validate(s){for(const e of [...s.tanks.flatMap(t=>t.equipment),...(s.ownedEquipment||[])])if(e.heaterModel!==undefined){const m=get(e.heaterModel);if(e.type!=='heater'||!m||Math.abs(e.capacity-m.capacity)>.000001)throw Error('Invalid saved heater model or fixed capacity.');}}
 function label(e){const m=get(e?.heaterModel);return m?m.name+' · '+m.range:e?'Legacy heater · '+AL.Units.volume(e.capacity)+' rating':'No heater installed';}
 return {models,get,recommended,products,validate,label};
})();
