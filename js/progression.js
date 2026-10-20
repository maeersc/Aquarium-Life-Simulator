"use strict";
// One-time profile awards, independent of presentation and acquisition route.
AL.Progression=(()=>{
 const D=AL.Data,K=AL.Core,groups={species:{xp:50,ac:50},size:{xp:100,ac:250},destination:{xp:50,ac:50}};
 for(const d of D.sizes)d.catalogId??=d.nominalGallons?'tank-size-'+d.nominalGallons+'gal':'tank-size-'+d.volume+'l';
 function species(id){id=AL.Clownfish?.varieties[id]?.speciesId||id;const entries=[...Object.values(D.species).map(d=>({d,id:d.id,kind:'fish'})),...Object.entries(D.flora).map(([id,d])=>({d,id,kind:'coral'})),...Object.values(D.invertebrates||{}).map(d=>({d,id:d.id,kind:'invertebrate'}))],item=entries.find(x=>x.id===id);if(!item||item.d.water!=='marine'||item.d.fictional||!item.d.scientificName||/\bspp?\./i.test(item.d.scientificName))return null;const canonical=entries.find(x=>x.kind===item.kind&&x.d.scientificName===item.d.scientificName);return {...canonical,key:canonical.kind+':'+canonical.id};}
 const size=t=>D.sizes.find(d=>d.volume===t.volume),destination=h=>h.mode+':'+h.region;
 function award(s,row){const rule=groups[row.kind];if(row.status!=='pending'||s.credits+rule.ac>1e9||s.xp+rule.xp>1e7)return;const receipt=AL.Finance.change(s,rule.ac,{category:'achievements',name:'First '+row.kind+': '+row.name,action:'firstOwnershipReward',achievementId:row.id,key:'achievement:'+row.id});row.transactionId=receipt.id;row.status='awarded';row.xp=rule.xp;row.ac=rule.ac;row.awardedAt=s.time;s.xp+=rule.xp;s.level=1+Math.floor(s.xp/200);s.stats.earnings+=rule.ac;K.log(s,'First '+row.kind+': '+row.name+' — +'+rule.xp+' Keeper XP and +'+rule.ac+' AC.');}
 function remember(s,kind,key,name,legacy=false){const p=s.progression,id='first-'+kind+':'+key;if(p.records[id])return;const row={id,profileId:s.accountId,kind,key,name,time:legacy?null:s.time,awardedAt:null,status:legacy?'known-before-update':'pending',xp:0,ac:0,transactionId:null};p.records[id]=row;if(!legacy)award(s,row);
 }
 function scan(s,legacy=false){const add=id=>{const v=species(id);if(v)remember(s,'species',v.key,v.d.name,legacy);};for(const t of s.tanks){const d=size(t);if(d&&(legacy||t.water==='marine'))remember(s,'size',d.catalogId,AL.Units.volume(d.volume),legacy);if(t.water!=='marine')continue;for(const f of [...t.fish,...t.flora,...(t.invertebrates||[])])if(legacy||!f.dead&&f.hp>0)add(f.species||f.type||f.invertebrate);for(const n of t.nurseries||[])if(n.progress>=24&&!n.dead)add(n.invertebrate);}
  for(const h of s.diving?.history||[])if(h.status==='success')remember(s,'destination',destination(h),AL.DivingData.regions[h.region].name+' · '+AL.DivingData.modes[h.mode].name,legacy);
  if(legacy){for(const id of [...s.discovered,...(s.discoveredInvertebrates||[])])add(id);for(const r of s.finance.rows)if(r.specimenId&&/^(buyFish|buyFlora|buyInvertebrate|sell|sellLivestock|diveSell)$/.test(r.action||''))add(r.speciesId);for(const r of s.update31?.lineage||[])add(r.type);for(const r of s.finance.rows)if(r.action==='buyTank'&&r.note){const d=D.sizes.find(d=>d.volume===Number(r.note.split(' ')[0]));if(d)remember(s,'size',d.catalogId,AL.Units.volume(d.volume),true);}}
 }
 function migrate(s,fresh=false){if(!s?.finance||!s.tanks)return;if(s.progression!==undefined)return;s.progression={version:1,profileId:s.accountId,records:{},objectives:{}};scan(s,!fresh);}
 function observe(s){if(!s.progression)migrate(s);scan(s);for(const row of Object.values(s.progression.records))if(row.status==='pending')award(s,row);}
 const objectives=[
  {id:'cycle-three',name:'Establish three biological filters',stat:'cycled',target:3},
  {id:'care-fifty',name:'Provide fifty meals',stat:'fed',target:50},
  {id:'water-ten',name:'Complete ten prepared water changes',stat:'waterChanges',target:10},
  {id:'coral-propagation',name:'Propagate one supported coral safely',measure:s=>s.update31.lineage.length,target:1},
  {id:'first-natural-clutch',name:'Observe a natural spawning event',measure:s=>s.breeding.records.filter(r=>r.spawnedAt!==null).length+s.breeding.archive.spawns,target:1},
  {id:'hatch-five',name:'Raise five hatchlings',stat:'hatched',target:5},
  {id:'reef-explorer',name:'Complete three distinct reef destinations',measure:s=>Object.values(s.progression.records).filter(r=>r.kind==='destination'&&r.key.startsWith('reef:')).length,target:3},
  {id:'deep-research',name:'Complete a deep-sea expedition',measure:s=>Object.values(s.progression.records).filter(r=>r.kind==='destination'&&r.key.startsWith('deep:')).length,target:1},
  {id:'service-three',name:'Maintain or renew equipment three times',measure:s=>s.equipmentReliability.events.filter(e=>['maintenance','part-replacement','repair'].includes(e.kind)).length,target:3},
  {id:'install-five',name:'Own five installed pieces of life support',measure:s=>s.tanks.reduce((n,t)=>n+t.equipment.length,0),target:5},
  {id:'three-sizes',name:'Own three different aquarium size categories over time',measure:s=>Object.values(s.progression.records).filter(r=>r.kind==='size').length,target:3},
  {id:'ten-species',name:'Discover ten biological species',measure:s=>Object.values(s.progression.records).filter(r=>r.kind==='species').length,target:10},
  {id:'stable-week',name:'Maintain seven game days of safe water',measure:s=>Math.max(0,...s.tanks.map(t=>t.safeHours/24)),target:7}
 ];
 function objectiveRows(s){return objectives.map(d=>{const progress=Math.min(d.target,Math.max(s.progression.objectives[d.id]?.progress||0,d.measure?d.measure(s):s.stats[d.stat]||0));return {...d,progress};});}
 function objectivesStep(s){for(const d of objectiveRows(s)){const r=s.progression.objectives[d.id]??={progress:0,completedAt:null};r.progress=d.progress;if(r.progress>=d.target&&r.completedAt===null)r.completedAt=s.time;}}
 function validate(s){const p=s.progression;if(!p||p.version!==1||p.profileId!==s.accountId||!p.records||!p.objectives||Object.keys(p.records).length>1000)throw Error('Invalid profile progression.');for(const [id,r]of Object.entries(p.records)){const rule=groups[r.kind],known=r.kind==='species'?species(r.key.split(':').slice(1).join(':'))?.key===r.key:r.kind==='size'?D.sizes.some(d=>d.catalogId===r.key):r.kind==='destination'?(()=>{const [mode,region]=r.key.split(':');return !!AL.DivingData.regions[region]&&(AL.DivingData.regions[region].modes||['reef','deep']).includes(mode);})():false;if(!rule||!known||id!=='first-'+r.kind+':'+r.key||r.id!==id||r.profileId!==s.accountId||typeof r.name!=='string')throw Error('Invalid first-time achievement.');if(r.status==='known-before-update'){if(r.time!==null||r.xp!==0||r.ac!==0||r.transactionId!==null)throw Error('Fabricated legacy reward.');}else if(r.status==='pending'){if(!Number.isFinite(r.time)||r.time<0||r.time>s.time||r.xp!==0||r.ac!==0||r.transactionId!==null||r.awardedAt!==null)throw Error('Invalid pending reward.');}else if(r.status!=='awarded'||!Number.isFinite(r.time)||r.time<0||r.time>s.time||r.xp!==rule.xp||r.ac!==rule.ac||!Number.isFinite(r.awardedAt)||r.awardedAt<r.time||r.awardedAt>s.time||!s.finance.keys.includes('achievement:'+id)||!r.transactionId?.startsWith(s.accountId+':ac:'))throw Error('Invalid achievement receipt.');}
  for(const [id,r]of Object.entries(p.objectives)){const d=objectives.find(d=>d.id===id);if(!d||!Number.isFinite(r.progress)||r.progress<0||r.progress>d.target||r.completedAt!==null&&(!Number.isFinite(r.completedAt)||r.completedAt<0||r.completedAt>s.time||r.progress<d.target))throw Error('Invalid objective progress.');}
 }
 return {groups,species,size,destination,migrate,observe,objectives,objectiveRows,objectivesStep,validate};
})();
