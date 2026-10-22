"use strict";
// Presentation only: use existing biological, equipment and valuation authorities.
AL.CareUI=(()=>{
 const esc=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 function equipmentStatus(e,t){const status=AL.EquipmentReliability.status(e,t);return status==='Working normally'?'Working':status==='Maintenance recommended'?'Needs maintenance':status;}
 function forecast(days){if(!Number.isFinite(days))return 'No reliable duration estimate';return Math.max(0,days/3).toFixed(1)+' real hours ('+days.toFixed(1)+' game days at 1×)';}
 function comparison(){const rows=AL.game.tanks.filter(t=>t.water==='marine').map(t=>({t,value:AL.Valuation.tank(AL.game,t).total})).sort((a,b)=>b.value-a.value||a.t.id.localeCompare(b.t.id));return `<details class="tank-comparison"><summary>Compare aquarium asset values</summary><p>Installed assets in your own aquariums. Wallet balance and stored items are separate.</p><div class="care-table-scroll"><table><thead><tr><th>Aquarium</th><th>Volume</th><th>Asset value</th></tr></thead><tbody>${rows.map(({t,value})=>`<tr><td>${esc(t.name)}</td><td>${AL.Units.volume(t.volume)}</td><td>${Math.floor(value).toLocaleString('en-US')} AC</td></tr>`).join('')}</tbody></table></div></details>`;}
 function developerTools(){return `<details class="developer-tools"><summary>Developer tools</summary><p>Artwork review pages for project development.</p><div class="filter-row">${[['clownfish-review.html','Clownfish art'],['life-stage-review.html','Life-stage art'],['art-review.html','Livestock art'],['livestock-animation-review.html','Animation review']].map(([url,name])=>`<a href="${url}" target="_blank" rel="noopener">${name}</a>`).join('')}</div></details>`;}
 function warnings(warnings,status){
  const node=document.getElementById('water-warning'),messages=[...new Set([...(status?.reasons||[]),...warnings].filter(Boolean))];
  const html=messages.length?`<strong>${status?.danger?'Needs attention':'Care notes'}</strong><ul>${messages.slice(0,3).map(v=>`<li>${esc(v)}</li>`).join('')}</ul>${messages.length>3?`<details><summary>${messages.length-3} more care notes</summary><ul>${messages.slice(3).map(v=>`<li>${esc(v)}</li>`).join('')}</ul></details>`:''}<button class="text-button" data-window="equipment" data-subtab="care">Open Tank Care →</button>`:'<span>No current care warnings.</span>';
  if(node.dataset.careSignature===html&&node.childElementCount)return;
  const expanded=!!node.querySelector('details[open]');node.innerHTML=html;node.dataset.careSignature=html;
  if(expanded&&node.querySelector('details'))node.querySelector('details').open=true;
 }
 return {equipmentStatus,forecast,comparison,developerTools,warnings};
})();
