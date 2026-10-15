"use strict";
AL.Research=(()=>{
 const D=AL.Data;
 function canonical(id){id=AL.Clownfish?.varieties[id]?.speciesId||id;const d=D.species[id];if(!d||d.water!=='marine')return null;const same=Object.values(D.species).find(f=>f.water==='marine'&&f.scientificName&&f.scientificName===d.scientificName);return same?.id||id;}
 function catalog(){return Object.values(D.species).filter(d=>d.water==='marine').map(d=>({d,id:canonical(d.id),data:AL.ResearchData.species[d.scientificName]||null,eligible:!d.fictional&&!!d.scientificName}));}
 function migrate(s){s.research??={version:1,accountId:s.accountId,unlocks:{}};}
 function buy(s,a){migrate(s);const id=canonical(a.species),d=D.species[id];if(!d||d.fictional||!d.scientificName)throw Error('This entry has no verified biological species identity; free preview only.');if(s.research.unlocks[id])return;AL.Finance.change(s,-5,{category:'research',action:'buyResearch',name:'Species Research: '+d.name,speciesId:id,key:'research:'+id,note:'Permanent species-level report; incomplete evidence is labeled.'});s.stats.expenses+=5;s.research.unlocks[id]={time:s.time,accountId:s.accountId};if(!s.achievements.includes('Research Your First Fish'))s.achievements.push('Research Your First Fish');}
 function progress(s){const ids=new Set(catalog().filter(r=>r.eligible).map(r=>r.id));return {unlocked:[...ids].filter(id=>s.research.unlocks[id]).length,total:ids.size,indexed:catalog().length};}
 function validate(s){const r=s.research;if(!r||r.version!==1||r.accountId!==s.accountId||!r.unlocks||typeof r.unlocks!=='object'||Array.isArray(r.unlocks))throw Error('Invalid research account.');for(const [id,u]of Object.entries(r.unlocks)){if(canonical(id)!==id||D.species[id]?.fictional||!D.species[id]?.scientificName||!Number.isFinite(u.time)||u.time<0||u.time>s.time||u.accountId!==s.accountId)throw Error('Invalid research unlock.');}}
 return {canonical,catalog,migrate,buy,progress,validate};
})();
