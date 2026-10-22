"use strict";
// v2.7 adapters consume one generated registry; existing biology remains authoritative.
AL.Expansion=(()=>{
 const records=AL.ExpansionData.records,byId=Object.fromEntries(records.map(d=>[d.id,d]));
 function register(){
  const D=AL.Data,template=D.species.gramma;D.invertebrates??={};
  for(const r of records){
   const existing=[...Object.values(D.species),...Object.values(D.flora),...Object.values(D.invertebrates)].find(d=>d.scientificName&&[r.scientificName,...r.aliases].includes(d.scientificName));if(existing)throw Error('Expansion duplicate scientific identity: '+r.scientificName);
   const minTank=r.minGallons*3.785411784,level={Common:1,Uncommon:2,Rare:4,'Very Rare':6,'Ultra Rare':8,Legendary:10}[r.rarity];
   const base={...r,minTank,level,purchaseVerified:true,expansion:'v2.7',status:'IMPLEMENTED; art pending user review',notes:r.name+': '+r.appearance+'. '+r.breedingStatus+'. Numeric care and development rates are game calibrations.'};
   if(r.category==='fish'){
    const bottom=['goby','prawn-goby','blenny'].includes(r.shape),active=['flasher','fairy','anthias'].includes(r.shape);
    D.species[r.id]={...template,...base,clownfish:false,color:'#dc9b75',secondary:'#d8d8d5',pattern:r.shape,shape:['butterfly','boxfish'].includes(r.shape)?'tang':bottom?'bottom':'oval',artShape:r.shape,load:Math.max(3,r.size*1.6),life:r.life,maxLife:r.life*1.7,maturity:r.maturity,temp:[24,27],ph:[8,8.4],salinity:[33,36],group:1,aggression:r.aggression,predator:r.predator,activity:active?1.6:bottom?.55:.8,zone:bottom?.84:active?.4:.55,habitat:r.habitat,immune:.75,fertility:.65,brood:2,breedCooldown:168,nocturnal:false,fictional:false,reproduction:r.shape==='assessor'?'mouthbrood':r.reproduction,incubation:r.incubation,breedingSupported:r.breedingSupported};
   }else if(r.category==='coral'){
    D.flora[r.id]={...base,color:r.id==='pavona-cactus'?'#6acb83':r.id==='leptastrea-purpurea'?'#a77bdb':'#dd957f',shape:r.shape==='lps'?'lps':'branch',growth:r.shape==='lps'?.008:.006,light:r.light,flow:r.flow,habitat:'corals',stony:true};
    if(AL.Habitat)AL.Habitat.definitions[r.id]={allowed:['rock','rack'],preferred:'rock',method:'secure live frag base on rock or mounted rack',footprint:r.shape==='lps'?16:14,clearance:r.shape==='lps'?25:22,light:r.light,flow:r.flow};
   }else D.invertebrates[r.id]={...base,load:Math.max(1,r.size*.8),temp:[24,27],ph:[8,8.4],salinity:[33,36],aggression:r.shape==='hermit'?.15:0,flow:r.shape==='crab'?.25:0,habitat:r.habitat};
  }
  // Marine-only foods are never added to freshwater purchase categories.
  Object.assign(D.foods,{'live-plankton':{name:'Cultured marine zooplankton',price:48,protein:.6,plant:.05,quality:1,particle:.1,pollution:1,water:'marine'},phyto:{name:'Marine suspension-feeder blend',price:30,protein:.25,plant:.65,quality:.9,particle:.05,pollution:.7,water:'marine'},'coral-polyp':{name:'Specialist filefish feeding ration',price:65,protein:.65,plant:.05,quality:.9,particle:.3,pollution:1.2,water:'marine'}});
 }
 register();
 function migrate(s){if(!s?.tanks||!s.stock||!s.inventory)return;for(const d of records)s.stock[d.id]??=d.category==='coral'?12:24;for(const id of ['live-plankton','phyto','coral-polyp']){s.inventory[id]??=0;s.stock[id]??=30;}for(const t of s.tanks)if(t.water==='marine'){t.invertebrates??=[];t.ecosystemAge??=0;}if(s.medicineStock&&AL.Health?.products.invertSupport)s.medicineStock.invertSupport??=20;s.expansionVersion??=1;}
 function report(s,t,species){const d=byId[species],reasons=[],warnings=[];if(!d||!t)return {ok:true,reasons,warnings};const r=AL.Data.species[species]||AL.Data.invertebrates[species]||AL.Data.flora[species];
  if(t.volume<r.minTank)reasons.push('Requires '+d.minGallons+' gal or more.');if(r.purchaseVerified===false)reasons.push(r.acquisitionHold||'Care requirements are not yet supported.');if(d.batch==='v2.9'){if(['centropyge-potteri','salarias-fasciatus','macropharyngodon-meleagris','ctenochaetus-strigosus','ctenochaetus-tominiensis'].includes(species)&&(t.ecosystemAge??0)<72)reasons.push('This specialist needs at least 72 game hours of prepared mature habitat.');if(['pygoplites-diacanthus','hymenocera-picta','nemanthias-bartlettorum','macropharyngodon-meleagris','tubastraea-micranthus','rhizotrochus-typus'].includes(species)&&r.diet.some(id=>(s.inventory[id]??0)<5))reasons.push('Keep at least five portions of each listed specialist food before introduction.');if(species==='acanthurus-achilles'&&(!AL.Core.has(t,'flow')||t.waterParams.oxygen<7))reasons.push('Achilles tang requires strong circulation and at least 7 mg/L oxygen.');}
  if(d.category==='coral')return {ok:!reasons.length,reasons,warnings};
  const rocks=t.hardscape?.length||t.decorations.some(x=>x.type==='cave');
  if(['sand','rocks'].includes(d.habitat)&&!rocks)reasons.push('Provide rock shelter or a rock cave before introduction.');
  if(d.habitat==='sand'&&(t.substrate?.depth??0)<1.5)reasons.push('Provide at least 1.5 inches of established soft sand.');
  if(d.category==='fish'&&d.predator>0&&(t.invertebrates||[]).some(f=>!f.dead&&AL.Data.invertebrates[f.invertebrate].size<d.size*.5))reasons.push('Small owned invertebrates are unsafe with this predator.');
  if(d.category==='bottom_dweller'&&t.fish.some(f=>!f.dead&&AL.Data.species[f.species].predator>0&&d.size<AL.Data.species[f.species].size*.5))reasons.push('Predatory fish make this destination unsafe for the invertebrate.');
  if(species==='orange-spotted-filefish'){if(t.kind!=='reef'||!t.flora.some(f=>f.hp>70&&f.type==='sps'))reasons.push('Specialist filefish needs an established reef with living branching SPS.');if(s.inventory['coral-polyp']<5)reasons.push('Keep at least five specialist feeding rations before introduction.');warnings.push('Wild diet is Acropora polyps. This feeding-conditioned game stock can accept specialist rations; living SPS may lose tissue when it is hungry.');}
  if(species==='purple-queen-anthias'&&s.inventory['live-plankton']<5)reasons.push('Keep at least five live-plankton portions; this expert planktivore needs frequent meals.');
  if(['blotched-anthias','purple-queen-anthias'].includes(species))warnings.push('High feeding demand: monitor hunger and nutrition; one daily feeder event may be insufficient.');
  if(species==='copperband-butterflyfish'){if(s.inventory.frozen<5)reasons.push('Keep at least five meaty frozen-food portions for this demanding specialist.');warnings.push('Demanding feeder; worms, ornamental invertebrates and coral polyps may be at risk.');}
  if(species==='spotted-boxfish'){if(t.fish.some(f=>!f.dead)||t.invertebrates?.some(f=>!f.dead)||t.flora.length||t.eggs.length)reasons.push('Spotted Boxfish requires a dedicated species-only home because stress/death may release toxin.');warnings.push('Species-specific toxin risk is simulated; quiet conditions and immediate removal of remains matter.');}
  if(t.boxToxin>.05)reasons.push('Resolve residual boxfish toxin before adding livestock.');if(species!=='spotted-boxfish'&&t.fish.some(f=>!f.dead&&f.species==='spotted-boxfish'))reasons.push('Do not introduce tankmates into the dedicated Spotted Boxfish aquarium.');
  if(['starry-blenny','redspotted-blenny','tiger-sand-conch'].includes(species)&&(t.ecosystemAge??0)<72)reasons.push('Let this prepared marine habitat mature for at least 72 game hours before adding a grazing specialist.');
  return {ok:!reasons.length,reasons,warnings};
 }
 function step(s,t,h){if(t.water!=='marine')return;t.ecosystemAge=(t.ecosystemAge||0)+(t.prepared?h:0);
  for(const f of t.fish){const d=byId[f.species];if(!d||f.dead)continue;const demand=f.species==='purple-queen-anthias'?1.4:f.species==='blotched-anthias'?.6:0;if(demand&&!AL.MarineCare)f.hunger=AL.Core.clamp(f.hunger+h*demand,0,100);
   if(f.species==='orange-spotted-filefish'&&f.hunger>55){const coral=t.flora.find(c=>c.hp>0&&c.type==='sps');if(coral){AL.Mortality?.note(s,t,coral,'Coral predation',h*.4);coral.hp=AL.Core.clamp(coral.hp-h*.4,0,100);f.hunger=AL.Core.clamp(f.hunger-h*2,0,100);}}
   if(['assessor','possum'].includes(d.shape)&&f.behavior==='Explore')f.behavior='Hover near shelter';
  }
  const risky=t.fish.find(f=>f.species==='spotted-boxfish'&&(f.dead||f.stress>85));if(risky){t.boxToxin=AL.Core.clamp((t.boxToxin||0)+h*(risky.dead?.12:.025),0,1);if(!t.toxinWarned){t.toxinWarned=true;AL.Core.log(s,t.name+': Spotted Boxfish toxin risk. Correct stress, remove remains and change water.','danger');}}
  t.boxToxin=Math.max(0,(t.boxToxin||0)*Math.exp(-h*(AL.Core.has(t,'skimmer')?.15:.04)));if(t.boxToxin>0){for(const f of [...t.fish,...(t.invertebrates||[])].filter(f=>!f.dead)){AL.Mortality?.note(s,t,f,'Boxfish toxin exposure',h*t.boxToxin*4);f.hp=AL.Core.clamp(f.hp-h*t.boxToxin*4,0,100);if(f.hp===0){if(f.species)AL.Core.kill(s,t,f,'Boxfish toxin exposure');else AL.Invertebrates.kill(s,t,f,'Boxfish toxin exposure');}}}
  AL.Invertebrates.step(s,t,h);
 }
 return {records,byId,migrate,report,step};
})();
