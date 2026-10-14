"use strict";
(async()=>{
  await Promise.all([AL.Art.ready,AL.AssetBank.ready]);
  const $=id=>document.getElementById(id),renderer=new AL.Renderer($('mount-aquarium'));
  let state,point={x:.5,y:.45},lastId=null,serial=0;
  const api=window.CORAL_REVIEW={ready:true,get state(){return state;},renderer,get report(){return renderer.placement?.report;}};
  function reset(){state=AL.Core.newGame('marine',2202);state.credits=100000;state.xp=2000;state.level=11;state.time=720;state.settings.speed=0;
    const t=AL.Core.selected(state);t.name='Coral attachment study';t.volume=150;t.prepared=true;t.bacteria=1;t.bacteria2=1;t.cycle=36;t.lightMode='on';t.lightIntensity=1;t.equipment.find(e=>e.type==='flow').capacity=300;t.equipment.push({type:'reefLight',capacity:300,durability:100,enabled:true});
    for(const glass of ['back','left','right'])state=AL.Core.act(state,'buyRack',{glass});
    lastId=null;point={x:.5,y:.45};$('mount-depth').value=2.4;update();}
  function update(){const type=$('mount-coral').value||'zoa',t=AL.Core.selected(state),report=AL.Habitat.placement(state,t,type,point.x,point.y);
    renderer.placement={type,x:report.ok?report.position.x:point.x,y:report.ok?report.position.y:point.y,size:1,valid:report.ok,status:report.status,report};
    $('mount-status').textContent=report.status+': '+([...report.reasons,...report.warnings].join(' ')||`${report.position.attachment.surface} support. Click or Enter to attach.`);
    $('mount-status').style.borderColor=report.ok?(report.warnings.length?'var(--warning)':'var(--success)'):'var(--danger)';
    $('mount-owned').replaceChildren(...t.flora.map(f=>{const row=document.createElement('p');row.textContent=`${AL.Data.flora[f.type].name}: ${f.attachment.surface}, support ${f.attachment.supportId||'stable sandbed base'}, local (${f.attachment.localX.toFixed(3)}, ${f.attachment.localY.toFixed(3)}).`;return row;}));renderer.draw(state,0);
  }
  function act(action,args){try{state=AL.Core.act(state,action,args,'mount-study-'+(++serial));$('mount-result').textContent='Action completed.';update();return true;}catch(e){$('mount-result').textContent=e.message;return false;}}
  function place(){const p=renderer.placement;if(!p.report.ok){$('mount-result').textContent=p.report.reasons.join(' ');return false;}if(act('buyFlora',{type:p.type,x:p.x,y:p.y,destinationTankId:state.selectedTank})){lastId=AL.Core.selected(state).flora.at(-1).id;return true;}return false;}
  $('mount-coral').append(...Object.entries(AL.Data.flora).filter(([id,d])=>d.water==='marine').map(([id,d])=>new Option(d.name,id)));
  $('mount-coral').onchange=update;$('mount-zoom').onchange=()=>{renderer.zoom=Number($('mount-zoom').value);update();};
  $('mount-aquarium').onpointermove=e=>{const rect=e.target.getBoundingClientRect();point=renderer.worldPoint((e.clientX-rect.left)/rect.width,(e.clientY-rect.top)/rect.height);update();};
  $('mount-aquarium').onclick=e=>{const rect=e.target.getBoundingClientRect();point=renderer.worldPoint((e.clientX-rect.left)/rect.width,(e.clientY-rect.top)/rect.height);update();place();};
  $('mount-aquarium').onkeydown=e=>{if(e.key==='Enter'){e.preventDefault();place();return;}const d={ArrowLeft:[-.01,0],ArrowRight:[.01,0],ArrowUp:[0,-.01],ArrowDown:[0,.01]}[e.key];if(d){e.preventDefault();point={x:point.x+d[0],y:point.y+d[1]};update();}};
  $('mount-set-depth').onclick=()=>act('buySand',{type:AL.Core.selected(state).substrate.type,depth:Number($('mount-depth').value)});
  $('mount-move-support').onclick=()=>{const t=AL.Core.selected(state),f=t.flora.find(f=>f.id===lastId),a=f?.attachment;if(a?.surface==='rack'){const r=t.mounts.find(r=>r.id===a.supportId);act('moveRack',{id:r.id,x:r.x+.015,y:r.y});}else{const r=t.hardscape.find(r=>r.id===a?.supportId)||t.hardscape[0];act('moveRock',{id:r.id,x:r.x+.015});}};
  $('mount-remove-support').onclick=()=>{const t=AL.Core.selected(state),f=t.flora.find(f=>f.id===lastId),a=f?.attachment;if(!a?.supportId){$('mount-result').textContent='Attach a coral to a rock or rack first.';return;}act(a.surface==='rack'?'removeRack':'removeRock',{id:a.supportId});};
  $('mount-roundtrip').onclick=()=>{try{const raw=JSON.stringify(state),restored=AL.Save.parse(raw);if(JSON.stringify(restored)!==raw)throw Error('Unexpected save changes.');state=restored;$('mount-result').textContent='Attachment IDs, local positions and selected aquarium survived save/load.';update();}catch(e){$('mount-result').textContent=e.message;}};
  $('mount-reset').onclick=reset;api.point=(x,y)=>{point={x,y};update();};api.place=place;reset();
})();
