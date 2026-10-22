"use strict";
// One collection classification, separate from care, health and price.
AL.Rarity=(()=>{
 const names=['Common','Uncommon','Rare','Very Rare','Ultra Rare','Legendary'],symbols=['Goldfish','Clownfish','Lionfish','Arowana','Great White Shark','Niger Triggerfish'],colors=[['#FFFFFF'],['#F28B30'],['#ED4545'],['#D9A83F','#E2E8EE'],['#368CE8','#FFFFFF'],['#9D52E8','#49C878']];
 const tiers=Object.freeze(names.map((name,i)=>Object.freeze({id:i+1,key:name.toLowerCase().replaceAll(' ','_'),name,symbol:symbols[i],path:'assets/rarity/'+(i+1)+'.svg',colors:colors[i],order:i+1,description:'Collection scarcity tier '+(i+1)+'; independent of care difficulty and conservation status.'})));
 const overrides={gramma:'Uncommon',firefish:'Uncommon',banggai:'Uncommon',sixline:'Uncommon',yellowtang:'Rare',marinebetta:'Rare',voidfin:'Rare',glassfang:'Rare'};
 const flora={zoa:'Common',mushroom:'Common',soft:'Common',lps:'Uncommon',sps:'Rare'};
 function get(value){const r=tiers.find(r=>r.key===value||r.name===value);if(!r)throw Error('Rarity data problem: '+value);return r;}
 function species(id){const d=AL.Data.species[id];if(!d)throw Error('Unknown rarity species: '+id);return get(overrides[id]||d.rarity);}
 function plant(id){if(!AL.Data.flora[id])throw Error('Unknown flora rarity: '+id);return get(AL.Data.flora[id].rarity||flora[id]||'Common');}
 function of(f){if(f.invertebrate)return get(f.rarity||AL.Data.invertebrates[f.invertebrate].rarity);return f.rarity?get(f.rarity):f.variety?get(AL.Clownfish.varieties[f.variety].rarity):f.invertebrate?get(AL.Data.invertebrates[f.invertebrate].rarity):f.species?species(f.species):plant(f.type);}
 function badge(value){const r=typeof value==='string'?get(value):of(value);return `<span class="rarity-symbol"><img src="${r.path}" width="40" height="40" alt="${r.symbol} rarity symbol"> Rarity: ${r.name} — Tier ${r.id}</span>`;}
 function migrate(s,legacy=false){for(const t of s.tanks)for(const f of [...t.fish,...t.flora,...t.eggs,...(t.invertebrates||[])]){if(legacy||!f.rarity||f.rarity==='Fictional contraband')f.rarity=(f.variety?get(AL.Clownfish.varieties[f.variety].rarity):f.invertebrate?get(AL.Data.invertebrates[f.invertebrate].rarity):f.species?species(f.species):plant(f.type)).name;get(f.rarity);}}
 return {tiers,get,species,plant,of,badge,migrate};
})();
// Independent persisted PRNG streams; rejection sampling avoids modulo bias.
AL.Random=Object.freeze({
 hash(text){let n=2166136261;for(const c of String(text)){n^=c.charCodeAt(0);n=Math.imul(n,16777619);}return n>>>0;},
 uint(s,key){s[key]??=this.hash(key+':'+s.seed);s[key]=(s[key]+0x9e3779b9)>>>0;let n=s[key];n=Math.imul(n^(n>>>16),0x21f0aaad);n=Math.imul(n^(n>>>15),0x735a2d97);return (n^(n>>>15))>>>0;},
 int(s,key,n){if(!Number.isInteger(n)||n<1||n>4294967296)throw Error('Invalid random range');const limit=Math.floor(4294967296/n)*n;let r;do{r=this.uint(s,key);}while(r>=limit);return r%n;}
});
