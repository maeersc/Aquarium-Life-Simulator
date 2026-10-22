"use strict";
// Add only the approved marine batch; old definitions and identities are untouched.
AL.Update29Catalog=(()=>{
 const D=AL.Data,records=AL.Update29Data.records,byId=Object.fromEntries(records.map(r=>[r.id,r]));
 for(const r of records){
  const existing=[...Object.values(D.species),...Object.values(D.flora),...Object.values(D.invertebrates)].find(d=>d.id===r.id||d.scientificName&&[r.scientificName,...r.aliases].includes(d.scientificName));
  if(existing)throw Error('v2.9 duplicate identity: '+r.scientificName);
  const base={...r,water:'marine',minTank:r.minGallons*3.785411784,level:[1,2,4,6,8,10][r.proposedTier-1],expansion:'v2.9',temp:[24,27],ph:[8,8.4],salinity:[33,36],notes:r.name+': '+r.notes+' '+r.careStatus,artStatus:'Original eight-stage/state artwork; pending user visual approval.'};
  if(r.category==='fish')D.species[r.id]={...D.species.gramma,...base,clownfish:false,color:'#d8ae65',secondary:'#e9dcd0',pattern:r.shape,load:r.size*1.6,maxLife:r.life*1.7,group:1,activity:r.shape==='slim'?1.2:.9,zone:r.shape==='bottom'?.78:.45,immune:.75,fertility:.65,brood:2,breedCooldown:168,nocturnal:false,fictional:false};
  else if(r.category==='coral'){
   D.flora[r.id]={...base,color:'#c9b071',growth:.007,stony:true,habitat:'corals',nonPhotosynthetic:r.light===0};
   AL.Habitat.definitions[r.id]={allowed:['rock','rack'],preferred:'rock',method:'Secure the specimen base on a supported rock or mounted rack; leave tissue and tentacle clearance.',footprint:16,clearance:26,light:r.light,flow:r.flow};
  }else D.invertebrates[r.id]={...base,load:Math.max(1,r.size*.8),flow:0,aggression:.05};
  // Extend the species-aware report lookup without changing the approved old batch array.
  AL.Expansion.byId[r.id]=r;
 }
 Object.assign(D.foods,{
  'angel-ration':{name:'Feeding-conditioned angelfish ration',price:52,protein:.55,plant:.25,quality:1,particle:.6,pollution:.8,water:'marine'},
  'reef-meat':{name:'Fine coral meaty ration',price:42,protein:.7,plant:0,quality:1,particle:.15,pollution:1,water:'marine'},
  'starfish-tissue':{name:'Sea-star tissue ration',price:85,protein:.7,plant:0,quality:1,particle:.4,pollution:1,water:'marine'}
 });
 D.supplies.salt.description='Marine salt: one dose prepares up to 2 liters of actual replacement water; larger changes consume proportionally more doses.';
 const capacity=56781.17676;
 D.sizes.push({volume:capacity,name:'Ocean Sanctuary',price:25000,marinePrice:25000,level:10,nominalGallons:15000,waterDimensionsCm:[1000,400,141.9529419],substrateAreaM2:40,capacityNote:'15,000 US gallons of usable simulation water. Engineering and structural loads are outside this game; substrate displacement is not modeled.',supports:['marine','fresh']});
 return {records,byId,capacity};
})();
