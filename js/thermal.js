"use strict";
// Game thermal calibration, not a real aquarium wattage recommendation.
AL.Thermal=(()=>{
 const K=AL.Core,D=AL.Data;
 function status(s,t,h=5/60){
  const ambient=22+AL.Sim.light(s,t)*.4,k=.09*Math.sqrt(75/t.volume),decay=Math.exp(-k*h),gain=-Math.expm1(-k*h)/k;
  const passive=ambient+(t.waterParams.temperature-ambient)*decay;
  const device=type=>{const gear=t.equipment.filter(e=>e.type===type),target=gear[0]?.temperatureTarget??t.temperatureTarget,capacity=K.capacity(t,type),rate=k*8*capacity/t.volume,request=type==='heater'?Math.max(0,target-passive):Math.max(0,passive-target),duty=rate>0?Math.min(1,request/(gain*rate)):0;return {target,installed:gear.length>0,enabled:gear.some(e=>e.enabled),operational:K.has(t,type),ratedCapacity:gear.reduce((n,e)=>n+e.capacity,0),effectiveCapacity:capacity,availableWatts:gear.filter(e=>e.enabled&&e.durability>0).reduce((n,e)=>n+D.equipment[type].watts*e.capacity/D.equipment[type].capacity*e.durability/100,0),duty,outputCPerGameHour:rate*duty,maximumCPerGameHour:rate,deliveredWatts:0};};
  const heater=device('heater'),chiller=device('chiller');for(const d of [heater,chiller])d.deliveredWatts=d.availableWatts*d.duty;
  const setpoint=heater.installed?heater.target:chiller.installed?chiller.target:t.temperatureTarget;
  return {ambient,room:22,volume:t.volume,setpoint,temperature:t.waterParams.temperature,heatLossCoefficient:k,heater,chiller,passive,next:passive+gain*(heater.outputCPerGameHour-chiller.outputCPerGameHour),heaterEquilibrium:ambient+8*heater.effectiveCapacity/t.volume,canMaintain:ambient<=setpoint?ambient+8*heater.effectiveCapacity/t.volume>=setpoint:ambient-8*chiller.effectiveCapacity/t.volume<=setpoint};
 }
 function step(s,t,h){const r=status(s,t,h);t.waterParams.temperature=r.next;return r;}
 return {status,step};
})();
AL.TankStatus=(()=>{
 function evaluate(s,t){const K=AL.Core,D=AL.Data,w=t.waterParams,all=[...t.fish,...t.flora,...(t.invertebrates||[]),...(t.nurseries||[])],living=all.filter(f=>!f.dead&&f.hp>0),broods=t.eggs.filter(e=>e.viability>0),dead=all.some(f=>f.dead||f.hp<=0),reasons=[];
  const general=w.ammonia<=.15&&w.nitrite<=.15&&w.nitrate<=40&&w.oxygen>=6&&w.ph>=8&&w.ph<=8.4&&w.salinity>=32&&w.salinity<=36;
  const temperature=[];for(const f of [...living,...broods]){const d=D.species[f.species]||D.invertebrates[f.invertebrate]||D.flora[f.type],range=d?.temp||[24,28];if(w.temperature<range[0]||w.temperature>range[1])temperature.push((f.name||d?.name||f.id)+' requires '+range[0]+'–'+range[1]+' °C');}
  if(temperature.length)reasons.push('Temperature outside resident range: '+temperature.join('; '));if(dead)reasons.push('Remove deceased livestock; normal current chemistry does not explain past losses.');if(!living.length&&!broods.length)reasons.push('No living stocked aquarium.');
  const care=AL.Gameplay.health({...s,tanks:[t]});if(living.length||broods.length)reasons.push(...care.reasons);const heat=AL.Thermal.status(s,t);if((living.length||broods.length)&&!heat.canMaintain)reasons.push('Heating/cooling output cannot maintain the '+t.temperatureTarget+' °C setpoint at its actual capacity/condition.');
  const danger=dead||w.ammonia>.5||w.nitrite>.5||w.oxygen<4||temperature.length>0,stocked=living.length+broods.length;
  return {stocked,general,temperatureUnsafe:temperature.length>0,reasons:[...new Set(reasons)],danger,label:!AL.Preparation.prepared(t)?'Unprepared':!stocked?(dead?'No living livestock':'Empty aquarium'):danger?'Needs care':t.bacteria<.65||t.bacteria2<.5?'Cycling':!care.ok||!general||!heat.canMaintain?'Watch closely':'Suitable for residents'};
 }
 return {evaluate};
})();
