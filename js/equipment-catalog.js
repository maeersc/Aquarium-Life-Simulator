"use strict";
// Stable metadata extends existing catalog records; no duplicate products or prices.
AL.EquipmentCatalog=(()=>{
 const categories={all:'All Equipment',heaters:'Heaters',chillers:'Chillers',circulation:'Pumps & Circulation',filtration:'Filters & Filtration',lighting:'Lighting',skimmers:'Protein Skimmers',aeration:'Aeration',feeders:'Automatic Feeders',monitoring:'Testing & Monitoring',fragging:'Coral Fragging Tools',mounting:'Coral Frag Mounting Supplies',other:'Other Equipment'};
 const ids={heater:'heaters',chiller:'chillers',flow:'circulation',filter:'filtration',light:'lighting',reefLight:'lighting',skimmer:'skimmers',air:'aeration',feeder:'feeders',dosing:'other',containment:'other'};
 for(const [id,d]of Object.entries(AL.Data.equipment))d.categoryId=ids[id]||'other';
 for(const [id,d]of Object.entries(AL.Update31.tools)){d.categoryId='fragging';AL.Data.supplies['frag-'+id].categoryId=d.categoryId;}
 for(const [id,d]of Object.entries(AL.Update31.supplies)){d.categoryId='mounting';AL.Data.supplies['frag-'+id].categoryId=d.categoryId;}
 const category=p=>p.kind==='rack'?'mounting':AL.Data.equipment[p.args.type]?.categoryId||AL.Data.supplies[p.args.type]?.categoryId||'other';
 function options(products){const present=new Set(products.map(category));return Object.entries(categories).filter(([id])=>id==='all'||present.has(id));}
 function facts(p,t){if(p.kind!=='equipment')return '';const d=AL.Data.equipment[p.args.type],m=AL.Heaters.get(p.args.heaterModel),capacity=m?.capacity||Math.max(d.capacity,t.volume),watts=d.watts*capacity/d.capacity;
  return (m?'Supported range '+m.range+' US gallons. Recommended: '+(AL.Heaters.recommended(t)?.range||'no supported heater size')+'. ':'Auto-sized to selected aquarium: '+AL.Units.volume(capacity)+' US gallons rated capacity; no separate minimum tank rating is defined. ')+watts.toFixed(1)+' W game equipment rating. '+(p.args.type==='heater'?'Actual heat depends on condition, thermostat and ambient temperature.':'')+' Base catalog rating: '+AL.Units.volume(d.capacity)+'.';
 }
 return {categories,category,options,facts};
})();
