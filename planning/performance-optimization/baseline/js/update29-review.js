"use strict";
AL.ExpansionArt.ready.then(()=>{
 const select=document.getElementById('v29-species'),facing=document.getElementById('v29-facing');
 for(const r of AL.Update29Data.records){const o=document.createElement('option');o.value=r.id;o.textContent=r.name+' · '+r.scientificName;select.append(o);}
 function render(){const r=AL.Update29Data.records.find(r=>r.id===select.value);document.getElementById('v29-title').textContent=r.name;document.getElementById('v29-details').textContent=r.scientificName+' · '+r.proposedRarity+' · '+r.proposedCareDifficulty+' care. '+r.earlyEquivalent+' Artwork unapproved. '+(r.acquisitionHold||'');const host=document.getElementById('v29-stages');host.replaceChildren();
  for(const [stage,label]of [['egg','Earliest equivalent'],['baby','Baby / larva'],['juvenile','Juvenile / growing'],['adult','Adult / mature']])for(const state of ['alive','dead']){const card=document.createElement('section');card.className='resolution-study';const c=document.createElement('canvas');c.width=384;c.height=320;const g=c.getContext('2d');g.imageSmoothingEnabled=false;g.fillStyle='#143444';g.fillRect(0,0,384,320);if(facing.value==='-1'){g.translate(384,0);g.scale(-1,1);}g.drawImage(AL.ExpansionArt.frame(r.id,stage,state),0,0,384,320);const p=document.createElement('p');p.textContent=label+' · '+state;card.append(c,p);host.append(card);}}
 select.onchange=render;facing.onchange=render;render();
});
