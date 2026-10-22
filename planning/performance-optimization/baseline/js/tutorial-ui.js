"use strict";
AL.TutorialUI=(()=>{
 const T=AL.Tutorial,K=AL.Core,D=AL.Data,$=id=>document.getElementById(id),esc=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const tickets=new WeakSet();let layer,tip,ring,shades=[],target=null,observer,pending=false,lastKey='',lastMissing='',lastValidation='',htmlKey='',scrollKey='',confirmDialog,started=false;
 const q=(s,root=document)=>root.querySelector(s),all=(s,root=document)=>[...root.querySelectorAll(s)];
 const args=n=>{try{return JSON.parse(n.dataset.storeArgs||n.dataset.args||'{}');}catch{return {};}};
 const find=(selector,predicate)=>all(selector).find(predicate);
 const answer=(target,instruction,key,extra={})=>({target,instruction,key,...extra});
 const detail=selector=>$('dialog').open?q(selector,$('dialog')):null;
 const button=(op,text)=>`<button type="button" data-guide="${op}">${text}</button>`;
 function topDialog(){return all('dialog[open]').filter(n=>n!==confirmDialog).at(-1)||null;}
 function route(name,tab,resolve,instruction){
  const modal=topDialog();if(modal?.id==='dialog')return answer($('dialog-close'),'Close these details to continue the current objective.','close-details');
  if(modal?.id==='casino-dialog')return answer($('casino-close'),'Close The Dock Casino to return to aquarium care.','close-casino');
  if(name==='store'){
   if(AL.Shell.opened)return answer($('window-switch'),'Choose Aquarium Store in this window selector.','switch-store');
   if(!AL.Store.opened)return answer(q('#navigation [data-page=store]'),'Open Aquarium Store.','open-store');
   if(q('[data-store-mode=buy]')&&!q('[data-store-mode=buy]').classList.contains('active'))return answer(q('[data-store-mode=buy]'),'Choose Buy.','store-buy');
   if(AL.Store.tab!=='saltwater')return answer(find('[data-store-action=tab]',n=>args(n).id==='saltwater'),'Choose Saltwater; freshwater remains locked.','saltwater');
   if(AL.Store.category!==tab)return answer(find('[data-store-action=category]',n=>args(n).id===tab),'Open '+({sand:'Sand & Substrate',equipment:'Equipment',rocks:'Rocks & Environment',fish:'Fish',supplies:'Food & Supplies'}[tab]||tab)+'.','store-'+tab);
  }else if(name==='scene'){
   if(AL.Store.opened)return answer($('store-close'),'Close Aquarium Store to return to the aquarium.','close-store');
   if(AL.Shell.opened)return answer($('primary-close'),'Close this window to view the aquarium and its current readings.','close-primary');
  }else{
   if(AL.Store.opened)return answer($('store-close'),'Close Aquarium Store, then open '+(name==='equipment'?'Tank Care':name==='journal'?'Field Journal':'Aquariums')+'.','close-store');
   if(!AL.Shell.opened)return answer(q('#navigation [data-page='+name+']'),'Open '+(name==='equipment'?'Tank Care':name==='journal'?'Field Journal':'Aquariums')+'.','open-'+name);
   if(AL.Shell.active!==name)return answer($('window-switch'),'Choose '+(name==='equipment'?'Tank Care':name==='journal'?'Field Journal':'Aquariums')+' in this window selector.','switch-'+name);
   if(AL.Shell.subtab!==tab)return answer(q('[data-primary-tab="'+tab+'"]'),'Choose '+(q('[data-primary-tab="'+tab+'"]')?.textContent||tab)+'.','tab-'+tab);
  }
  return answer(typeof resolve==='function'?resolve():q(resolve),instruction,name+'-'+tab);
 }
 function purchase(p,instruction){const r=T.state(AL.game),selector=detail('#purchase-destination');if(selector?.value!==r.tankId)return answer(selector,'Choose '+T.tank(AL.game).name+' as the destination. Every owned aquarium is listed.','purchase-destination');if($('confirm-fish')?.disabled)return answer($('compatibility-report'),'This purchase is blocked. Read the reason and check your AC and stock. Close these details to fix the requirement.','blocked-purchase');return answer($('confirm-fish'),instruction,'confirm-'+p.id);}
 function stockItem(category,predicate,instruction){let selection;const result=route('store',category,()=>{
  if($('store-search')?.value)return $('store-search');
  const products=AL.Store.products().filter(predicate).sort((a,b)=>a.price-b.price);
  selection=products.find(p=>p.stock>0&&p.price<=AL.game.credits)||products.find(p=>p.stock>0)||products[0];if(!selection)return $('store-products');
  return find('[data-store-action=details]',n=>args(n).id===selection.id&&!n.disabled)||$('equipment-filter');
 },instruction);
  if(result.target?.id==='store-search')result.instruction='Clear Search items to see the needed products.';
  else if(result.target?.id==='equipment-filter')result.instruction='Choose All Equipment in Equipment category to see the required item.';
  else if(selection&&result.target?.dataset.storeAction==='details')result.instruction=selection.stock<1?selection.name+' is sold out. View Details to check availability; another suitable item or the next normal restock is needed. Pause the guide while waiting if you wish.':selection.price>AL.game.credits?selection.name+' costs '+selection.price+' AC; you have '+Math.floor(AL.game.credits)+' AC. View Details to review costs. Earn existing objective rewards in Field Journal > Progress > Objectives, then return.':'Click View Details for '+selection.name+' ('+selection.price+' AC).';
  return result;
 }

 function equipment(type){const s=AL.game,t=T.tank(s),e=t.equipment.find(e=>e.type===type),owned=s.ownedEquipment.find(e=>e.type===type&&AL.Inventory.equipmentReport(s,e,t).ok);
  if($('dialog').open){
   if(detail('#inventory-destination'))return answer($('inventory-destination').value===t.id&&!$('inventory-confirm').disabled?$('inventory-confirm'):$('inventory-destination'),'Choose '+t.name+' and click Confirm installation. The unit moves from Inventory into this aquarium.','install-'+type);
   const marker=q('[data-tutorial-product]');if(marker&&marker.dataset.productKind==='equipment'&&marker.dataset.productType===type)return purchase({id:marker.dataset.tutorialProduct},'Check the rating, price and Sizing aquarium, then click Confirm purchase. Next, install the unit from Tank Care > Inventory.');
   if(e&&q('[data-inspected-equipment="'+e.id+'"]')){
    const toggle=find('#dialog-body [data-action=toggleEquipment]',n=>args(n).type===type);
    if(!e.enabled)return answer(toggle,'Turn on this installed '+D.equipment[type].name+'.','enable-'+type);
    const service=q('#dialog-body [data-action=service]:not(:disabled)');if(service)return answer(service,'Inspect the fault and use Maintenance if appropriate. This does not reset physical age.','service-'+type);
    if(e.durability<=0||e.reliability?.state==='beyond-repair')return answer(q('#dialog-body [data-action=uninstallEquipment]'),'This unavailable unit requires whole-device replacement. Read the removal warning before returning it to Inventory.','failed-'+type);
    if(AL.EquipmentParts.supported?.(e)?.length)return answer(q('#dialog-body [data-economy=parts]'),'Inspect the supported replacement parts and exact prices.','parts-'+type);
    return answer(q('#dialog-body [data-action=uninstallEquipment]'),'This device needs attention. Inspect its condition; a failed sealed unit may require warned removal and a replacement.','replace-'+type);
   }
   if(q('#dialog-body [data-action=inventoryRemoveConfirmed]'))return answer(q('#dialog-body [data-action=inventoryRemoveConfirmed]'),'Read the life-support warning. Confirm only if you intend to replace this unavailable device.','remove-confirm');
   if(q('#dialog-body [data-economy=replace]'))return answer(q('#dialog-body [data-economy=replace]:not(:disabled)'),'Review the listed new-part price and confirm a supported repair.','part-confirm');
  }
  if(e)return route('equipment','care',()=>find('#primary-content [data-action=inspectEquipment]',n=>args(n).id===e.id)||$('care-category'),'Inspect the installed device and resolve its actual on/off, maintenance or fault state.');
  if(owned)return route('equipment','inventory',()=>find('#primary-content [data-action=inventoryInstall]',n=>args(n).id===owned.id)||($('inventory-search')?.value?$('inventory-search'):$('inventory-category')),'Find your '+D.equipment[type].name+' and click Install. Clear Search storage or choose All stored items if it is hidden.');
  return stockItem('equipment',p=>p.kind==='equipment'&&p.args.type===type&&(type!=='heater'||AL.Heaters.get(p.args.heaterModel)?.capacity>=t.volume),'Choose a correctly rated '+D.equipment[type].name+'. Nothing is installed or charged until you confirm the real controls.');
 }
 function resolve(){const s=AL.game,r=T.state(s),t=T.tank(s),d=T.current(s),modal=topDialog();
  if(modal&&!['dialog','casino-dialog','primary-dialog','store-dialog'].includes(modal.id))return answer(q('[id$="close"],[aria-label*="Close"]',modal),'Close this window using its normal controls to return to the current objective.','close-'+modal.id);
  if(!t){if(s.tanks.some(t=>t.water==='marine'))return route('aquariums','owned',()=>find('[data-tank]',n=>s.tanks.find(t=>t.id===n.dataset.tank)?.water==='marine'),'Choose an owned saltwater aquarium. Existing tanks do not need to be repurchased.');
   if(detail('[data-form=buyTank]'))return answer(detail('[data-form=buyTank] button[type=submit]'),'Review the saltwater aquarium, name, purpose and price, then confirm the existing purchase.','create-tank');
   return route('aquariums','new',()=>find('[data-action=configureTank]',n=>!n.disabled),'Choose an affordable aquarium from the existing catalog.','new-aquarium');}
  if(s.selectedTank!==t.id){if(modal)return answer(q('#'+modal.id+' [id$="close"]')||q('#'+modal.id+' [aria-label*=Close]'),'Close this window, then select '+t.name+' above the aquarium. The guide remains pinned to that aquarium.','wrong-tank-close');return answer($('aquarium-selector'),'Select '+t.name+' to continue this guide. Change the guide’s aquarium deliberately in Settings if desired.','pinned-tank');}
  if(d.id==='welcome')return route('aquariums','owned','[data-primary-tab=owned]','Select My Aquariums to review your owned saltwater aquarium.');
  if(d.id==='view'&&!$('empty-tank').classList.contains('hidden'))return route('scene',null,'#onboard-action','Click '+$('onboard-action').textContent.replace(/\s*\u2192\s*$/,'')+' to review Tank Setup. A dry aquarium needs sand, saltwater and life support before fish.');
  if(['view','observe'].includes(d.id))return route('scene',null,'#aquarium',d.instruction);
  if(d.id==='substrate'){
   if(detail('[data-tutorial-product][data-product-kind=sand]')){const depth=detail('[data-form=storePurchase] [name=depth]');if(Number(depth?.value)<=0)return answer(depth,'Enter a sand depth, such as 2 inches. The price updates before you confirm. Sand-dependent fish may need a deeper bed.','sand-depth');return purchase({id:'sand'},'Check the price and Destination aquarium, then click Confirm purchase to install this sand depth.');}
   return stockItem('sand',p=>p.kind==='sand',d.instruction);
  }
  if(['fill','prepare'].includes(d.id))return route('aquariums','setup','[data-action='+(d.id==='fill'?'fillWater':'prepare')+']',d.instruction);
  if(['filter','flow','controller'].includes(d.id))return equipment(d.id==='controller'?(t.waterParams.temperature>T.species(s).temp[1]?'chiller':'heater'):d.id);
  if(d.id==='hardscape'){
   if(AL.UI.placing)return route('scene',null,'#aquarium','Move the rock near the sandbed until the preview is valid, then click. You can also use arrows and Enter. Canceling leaves the rock unplaced.');
   if(detail('#inventory-destination'))return answer($('inventory-destination').value===t.id&&!$('inventory-confirm').disabled?$('inventory-confirm'):$('inventory-destination'),'Choose '+t.name+' for this owned rock, then continue to actual supported placement.','owned-rock-destination');
   if(detail('[data-tutorial-product][data-product-kind=rock]'))return purchase({id:'rock'},'Check the price and Destination aquarium, then click Confirm purchase and place the rock. The cost is charged when you confirm its position.');
   const owned=(s.ownedObjects||[]).find(o=>o.kind==='rock');if(owned)return route('equipment','inventory',()=>find('[data-action=inventoryPlace]',n=>args(n).id===owned.id)||$('inventory-category'),'Use Place for your owned rock. Keep its original identity.');
   return stockItem('rocks',p=>p.kind==='rock',d.instruction);
  }
  if(d.id==='temperature'){
   const def=T.species(s),w=t.waterParams;if(w.salinity<def.salinity[0]||w.salinity>def.salinity[1])return route('equipment','change','[data-action=waterChange]','Use a prepared, matched water change. Review its costs, salt requirement and expected readings.');
   const type=w.temperature>def.temp[1]?'chiller':'heater',e=t.equipment.find(e=>e.type===type);if(!e&&!T.heatNeeded(s,t))return route('scene',null,'[data-water-stat=temperature]','Room temperature is suitable. Wait for the actual water to approach '+def.temp.join(' to ')+' C; a controller is optional in these room conditions.');if(!e||!K.has(t,type))return equipment(type);
   if(e.temperatureTarget!==undefined&&(e.temperatureTarget<def.temp[0]||e.temperatureTarget>def.temp[1])){if(detail('[data-form=equipmentThermostat]')){const form=detail('[data-form=equipmentThermostat]'),value=Number(form.elements.temperature.value);return answer(value>=def.temp[0]&&value<=def.temp[1]?q('button',form):form.elements.temperature,'Set Thermostat setting (°C) to '+def.temp.join('–')+' °C and click Save thermostat. The water warms or cools gradually.','thermostat');}return route('equipment','care',()=>find('[data-action=inspectEquipment]',n=>args(n).id===e.id),'Inspect the installed controller to adjust its thermostat.');}
   if(!AL.Thermal.status(s,t).canMaintain)return route('equipment','care',()=>find('[data-action=inspectEquipment]',n=>args(n).id===e.id),'Actual controller capacity/condition cannot maintain the target. Inspect maintenance and appropriately sized replacement options. No temperature is forced.');
   return route('scene',null,'[data-water-stat=temperature]','Actual water is '+w.temperature.toFixed(2)+' °C; '+def.name+' needs '+def.temp.join('–')+' °C. Wait for the real controller output. Stored or weak equipment cannot force the temperature.');
  }
  if(d.id==='cycle'){
   if(!K.has(t,'filter'))return equipment('filter');
   if(!t.cycleActive)return route('aquariums','setup','[data-action=cycle]',d.instruction);
   return route('scene',null,'[data-water-stat=ammonia]','Fishless cycle: '+Math.min(100,t.cycle/AL.Config.cycleHours*100).toFixed(1)+'%. Remaining '+Math.max(0,AL.Config.cycleHours-t.cycle).toFixed(1)+' game hours (~'+(Math.max(0,AL.Config.cycleHours-t.cycle)/AL.Config.minutesPerSecond).toFixed(1)+' real minutes at 1x). Watch ammonia, nitrite and nitrate. Existing 1×/5×/20× controls change simulation speed; this guide never skips days or edits bacteria.');
  }
  if(d.id==='quality'){
   const check=T.report(s);if(!check.ok){const failed=check.checks.find(c=>!c.ok);if(['filter','flow'].includes(failed?.id))return equipment(failed.id);if(failed?.id==='temperature')return route('scene',null,'[data-water-stat=temperature]','Actual temperature is outside the required range. Inspect the controller and allow real adjustment.');return route('scene',null,'#water-stats','Receiving is blocked: '+check.reasons.join(' ')+' Use existing care controls to correct the actual readings.');}
   return route('scene',null,'#water-stats','Review the actual water readings now that biological cycling is established. Click the readings, or focus them and press Enter. The full checks are available below.');
  }
  if(['shop','details','destination','stocking'].includes(d.id)){
   const marker=detail('[data-tutorial-product][data-product-kind=fish]');if(marker){const id=marker.dataset.tutorialProduct;if(id!==r.productId)return answer($('dialog-close'),'Choose a currently compatible starter listing. The guide never unlocks an unsafe fish.','other-listing');
    if($('confirm-fish')?.disabled)return answer($('compatibility-report'),'Check the reason below, your AC, Number of residents and stock. Close these details to fix the requirement. No fish has been purchased. Earn existing rewards in Field Journal > Progress > Objectives if you need AC.','blocked-fish');
    if(!r.signals.destination||$('purchase-destination')?.value!==t.id)return answer($('purchase-destination'),'Review '+t.name+' in the real destination selector. Every aquarium is listed with eligibility.','fish-destination');
    if(!r.signals.compatibility)return answer($('compatibility-report'),'Read the compatibility checks and total price. Click this report, or focus it and press Enter.','fish-compatibility');
    return answer($('confirm-fish'),'Check the destination and total price. Click Confirm purchase to add this fish to '+t.name+'.','stock-fish');
   }
   const p=T.candidate(s);return route('store','fish',()=>p?find('[data-store-action=details]',n=>args(n).id===p.id):$('rotation-countdown'),p?'Read '+p.name+' ('+p.price+' AC). This listing fits the actual tank and supported care profile.':'No suitable listing is available at your current level, AC and water conditions. Check the shop countdown for its next rotation, or earn existing rewards in Field Journal > Progress > Objectives. You can pause and return here later.');
  }
  if(d.id==='feed'){
   const f=T.resident(s),foods=D.species[f.species].diet,stocked=foods.filter(id=>s.inventory[id]>0);if(!stocked.length)return stockItem('supplies',p=>p.kind==='food'&&foods.includes(p.args.type),'Buy a compatible ration from the resident’s actual diet. It goes to shared inventory.');
   return route('equipment','feeding',()=>{const select=q('[data-form=feed] [name=type]');return !select||!stocked.includes(select.value)?select:q('[data-form=feed] button[type=submit]')||q('[data-form=feed] button');},'Choose '+stocked.map(id=>D.foods[id].name).join(' or ')+', then Feed one portion. A real inventory-consuming feed is required.');
  }
  if(d.id==='appetite')return route('scene',null,'#aquarium','Wait for your fish to eat the food already in the water. Do not add more while a portion remains. Its feeding record will update after a meal.');
  if(d.id==='inspect')return route('journal','collection',()=>find('[data-inspect-resident]',n=>n.dataset.inspectResident===r.fishId)||q('[data-journal-filter=tank]'),'Inspect the tutorial fish and read its hunger, stress and health. If filters hide it, choose the tutorial aquarium or All.');
  return route('scene',null,'#aquarium',d.instruction);
 }
 function consumeInteraction(s,a){if(!tickets.has(a))return false;tickets.delete(a);return s.accountId===a.profileId;}
 function record(kind,data={}){const s=AL.game,r=T.state(s);if(!r||r.status!=='active'||s.selectedTank!==r.tankId)return;
  if(r.signals[kind]&&(!data.productId||r.signals[kind].productId===data.productId)&&(!data.fishId||r.signals[kind].fishId===data.fishId))return;
  const a={op:'interaction',kind,profileId:s.accountId,...data};tickets.add(a);try{AL.game=K.act(s,'tutorialProgress',a);AL.UI.save();}catch(e){T.note(AL.game,'validation-failed',e.message);}schedule();
 }
 function capture(e){if(e.target.closest?.('#tutorial-layer,#tutorial-confirm,[data-guide]'))return;const node=e.target,profileId=AL.game?.accountId,stepId=T.state(AL.game)?.current,meta={page:node.closest?.('[data-page]')?.dataset.page,tab:node.closest?.('[data-primary-tab]')?.dataset.primaryTab,store:node.closest?.('[data-store-action]'),water:!!node.closest?.('#water-stats'),canvas:node.id==='aquarium',onboard:node.id==='onboard-action',destination:node.id==='purchase-destination',compatibility:!!node.closest?.('#compatibility-report'),switcher:node.id==='window-switch',inspector:node.closest?.('[data-inspect-resident]')?.dataset.inspectResident,action:node.closest?.('[data-action]')};
  const shopArgs=meta.store?args(meta.store):{};setTimeout(()=>{
   const s=AL.game,r=T.state(s);if(!r||r.status!=='active'||s.accountId!==profileId||AL.Startup.pending||AL.Offline.busy)return;const id=r.current;if(id!==stepId){schedule();return;}
   if(id==='welcome'&&AL.Shell.active==='aquariums'&&(meta.page==='aquariums'||meta.tab==='owned'||meta.switcher))record('welcome');
   if(meta.canvas&&['view','observe'].includes(id)&&!AL.UI.placing)record(id);
   if(meta.onboard&&id==='view'&&AL.Shell.active==='aquariums'&&AL.Shell.subtab==='setup')record('view');
   if(meta.water&&id==='quality')record('readings');
   if(AL.Store.opened&&AL.Store.tab==='saltwater'&&AL.Store.category==='fish'&&(meta.page==='store'||meta.store||meta.switcher)&&id==='shop')record('shop');
   const marker=detail('[data-tutorial-product][data-product-kind=fish]');if(meta.store?.dataset.storeAction==='details'&&marker&&['details','destination','stocking','shop'].includes(T.state(AL.game).current))record('details',{productId:shopArgs.id});
   if(meta.destination&&marker)record('destination',{productId:marker.dataset.tutorialProduct});if(meta.compatibility&&marker)record('compatibility',{productId:marker.dataset.tutorialProduct});
   const inspected=detail('[data-tutorial-inspected-fish]');if(inspected&&((meta.inspector||meta.action?.dataset.action==='inspectFish')||meta.canvas)&&T.state(AL.game).current==='inspect')record('inspect',{fishId:inspected.dataset.tutorialInspectedFish});
   T.diagnostics.sample(AL.game,{previous:stepId,current:T.state(AL.game).current,route:resolve().key,trigger:e.type+':'+(node.id||node.dataset?.page||node.dataset?.storeAction||node.tagName),result:T.state(AL.game).current!==stepId?'advanced':'pending'});schedule();
  },0);
 }
 function visibleRect(el){let r=el.getBoundingClientRect(),left=Math.max(6,r.left),top=Math.max(6,r.top),right=Math.min(innerWidth-6,r.right),bottom=Math.min(innerHeight-6,r.bottom);for(let p=el.parentElement;p&&p!==document.body;p=p.parentElement){const style=getComputedStyle(p),b=p.getBoundingClientRect();if(/auto|scroll|hidden|clip/.test(style.overflowY)){top=Math.max(top,b.top);bottom=Math.min(bottom,b.bottom);}if(/auto|scroll|hidden|clip/.test(style.overflowX)){left=Math.max(left,b.left);right=Math.min(right,b.right);}}return {left,top,right,bottom,width:Math.max(0,right-left),height:Math.max(0,bottom-top)};}
 function position(){if(!layer||layer.hidden||!target?.isConnected)return;let r=visibleRect(target);if(r.width<=0||r.height<=0){if(scrollKey!==lastKey){target.scrollIntoView({block:'nearest',inline:'nearest',behavior:'instant'});scrollKey=lastKey;r=visibleRect(target);}if(r.width<=0||r.height<=0){ring.hidden=true;for(const shade of shades)shade.hidden=true;return;}}
  ring.hidden=false;for(const shade of shades)shade.hidden=false;
  const origin=layer.getBoundingClientRect(),x=r.left-origin.left,y=r.top-origin.top;Object.assign(ring.style,{left:x-4+'px',top:y-4+'px',width:r.width+8+'px',height:r.height+8+'px'});
  const boxes=[[0,0,innerWidth,Math.max(0,y-7)],[0,y-7,Math.max(0,x-7),r.height+14],[x+r.width+7,y-7,Math.max(0,innerWidth-x-r.width-7),r.height+14],[0,y+r.height+7,innerWidth,Math.max(0,innerHeight-y-r.height-7)]];boxes.forEach(([l,t,w,h],i)=>Object.assign(shades[i].style,{left:l+'px',top:t+'px',width:w+'px',height:h+'px'}));
  const w=tip.offsetWidth,h=tip.offsetHeight,margin=10,context=target.closest('[data-form=storePurchase],[data-form=inventoryDestination],[data-form=equipmentThermostat],#water-stats'),protectedRect=context?visibleRect(context):r,c=protectedRect,candidates=[[c.right+14,r.top],[c.left-w-14,r.top],[c.left,c.top-h-14],[c.left,c.bottom+14],[r.right+14,r.top],[r.left-w-14,r.top],[r.left,r.bottom+14],[r.left,r.top-h-14]],clamp=(n,a,b)=>Math.max(a,Math.min(b,n)),area=(l,t,b)=>Math.max(0,Math.min(l+w,b.right)-Math.max(l,b.left))*Math.max(0,Math.min(t+h,b.bottom)-Math.max(t,b.top));
  const choices=candidates.map(([l,t])=>{l=clamp(l,margin,innerWidth-w-margin);t=clamp(t,margin,innerHeight-h-margin);const overlap=area(l,t,r),contextOverlap=area(l,t,c);return {l,t,overlap,score:overlap*100+contextOverlap};}).sort((a,b)=>a.score-b.score),p=choices[0];Object.assign(tip.style,{left:p.l-origin.left+'px',top:p.t-origin.top+'px'});
  // On constrained screens keep a small button/field entirely clickable. The
  // tooltip may share a large canvas region, but never intercepts a required button.
  if(p.overlap&&r.height<90&&r.width<w){const available=Math.max(r.top-20,innerHeight-r.bottom-20);tip.style.maxHeight=Math.max(70,Math.min(260,available))+'px';}else tip.style.maxHeight='min(330px, 42dvh)';
 }
 function summary(){const s=AL.game,r=T.state(s),t=T.tank(s),f=T.resident(s);return `<h3>Your First Saltwater Aquarium Is Ready!</h3><p>Completion recorded ${esc(AL.Clock.stamp(r.completedAt))}. Current status:</p><p>${esc(t?.name||'Recorded aquarium')} · ${esc(t?AL.TankStatus.evaluate(s,t).label:'No longer owned')}<br>First livestock: ${esc(f?.name||'See recorded milestones')}</p><details><summary>Verified milestones (${Object.keys(r.completed).length})</summary><ul>${Object.values(r.completed).map(v=>`<li>${esc(T.byId[v.id].title)}: ${esc(v.evidence)}</li>`).join('')}</ul></details><p>Approved first-size/species rewards and quests stay in Progress. This guide grants no extra AC or XP.</p>`;}
 function update(){pending=false;if(!started||!AL.game?.update29)return;T.migrate(AL.game);const r=T.state(AL.game);if(AL.Startup?.pending||AL.Offline.busy||confirmDialog.open||r.status!=='active'&&(r.status!=='completed'||r.completionSeen)){hide();return;}
  const before=JSON.stringify([r.current,r.status,Object.keys(r.completed)]);T.observe(AL.game,'state');if(before!==JSON.stringify([r.current,r.status,Object.keys(r.completed)]))AL.UI.save();
  const next=r.status==='completed'?answer(q('dialog[open] [data-tutorial-inspected-fish]')||q('dialog[open] h2')||$('aquarium'),'','complete'):resolve(),host=topDialog()||document.body;if(host!==layer.parentElement)host.append(layer);layer.hidden=false;
  target?.classList.remove('tutorial-target');const missing=!next.target||!next.target.isConnected||!next.target.getClientRects().length;
  if(missing){const key=r.current+':'+next.key;if(lastMissing!==key){T.note(AL.game,'missing-target',key);lastMissing=key;}target=all('button:not(:disabled)',host).find(n=>!layer.contains(n)&&n.getClientRects().length)||$('tutorial-current');}else{target=next.target;lastMissing='';}
  const key=safeKey(r,next)+':'+missing;if(lastKey!==key){lastKey=key;T.note(AL.game,'target-resolved',next.key+(missing?' (recovery control)':''));scrollKey='';if(target)target.scrollIntoView({block:'nearest',inline:'nearest',behavior:'instant'});}
  if(target)target.classList.add('tutorial-target');
  let body=r.status==='completed'?summary()+button('acknowledge','Done'): `<div class="guide-caption">SALTWATER GUIDE · PHASE ${T.current(AL.game).phase+1} / 12</div><h3>${esc(T.current(AL.game).title)}</h3><p>${esc(missing?'The expected control is not available in this view. Close unrelated details or return to the indicated section, then retry. You can pause or skip safely.':next.instruction)}</p>${r.current==='quality'?checksMarkup():''}<div class="guide-actions">${button('pause','Pause')}${button('objective','Focus target')}${button('skip','Skip…')}</div>`;
  if(body!==htmlKey){tip.innerHTML=body;htmlKey=body;}position();
  const validation=r.current+':'+(r.current==='quality'?T.report(AL.game).reasons.join('|'):missing?'target missing':'pending');if(validation!==lastValidation){lastValidation=validation;if(missing||r.current==='quality'&&!T.report(AL.game).ok)T.note(AL.game,'validation-failed',validation);}
 }
 function safeKey(r,next){return AL.game.accountId+':'+r.current+':'+r.tankId+':'+(topDialog()?.id||'scene')+':'+next.key;}
 function checksMarkup(){const r=T.report(AL.game);return `<details class="guide-checks"><summary>Actual receiving and water checks</summary>${r.checks.map(c=>`<p><strong>${esc(c.label)}: ${c.ok?'Pass':'Blocked'}</strong><br>Actual ${esc(c.actual)}; requires ${esc(c.required)}.</p>`).join('')}</details>`;}
 function hide(){target?.classList.remove('tutorial-target');target=null;if(layer)layer.hidden=true;}
 function schedule(){if(!started||pending)return;pending=true;requestAnimationFrame(update);}
 function focusObjective(){const r=T.state(AL.game);if(['paused','skipped'].includes(r?.status)){AL.Shell.open('settings','preferences');return;}if(r?.status==='completed'&&r.completionSeen){AL.game=K.act(AL.game,'tutorialProgress',{op:'review'});AL.UI.save();}update();if(target){target.scrollIntoView({block:'nearest',inline:'nearest',behavior:'instant'});target.focus({preventScroll:true});position();}}
 function control(op){if(op==='objective'){focusObjective();return;}if(['skip','restart'].includes(op)){confirmDialog.innerHTML=`<h2>${op==='skip'?'Skip the tutorial?':'Restart the guide?'}</h2><p>${op==='skip'?'This only opts out of guidance. It does not prepare water, complete setup, grant rewards or change livestock.':'Only guide progress resets. Aquariums, equipment, livestock, credits and earned achievements are preserved; existing setup is recognized.'}</p><div class="guide-actions">${button('cancel-confirm','Keep current guide')}<button data-guide-confirm="${op}">Confirm ${op==='skip'?'skip':'restart'}</button></div>`;hide();confirmDialog.showModal();return;}
  try{AL.game=K.act(AL.game,'tutorialProgress',{op});AL.UI.save();if(op==='pause')hide();else schedule();AL.Shell.render();}catch(e){AL.UI.toast(e.message,true);}
 }
 function preferences(){const r=T.state(AL.game);return `<section class="notice" id="interactive-tutorial-settings"><h3>Interactive saltwater guide</h3><p>${esc(r.status)} · ${esc(T.current(AL.game).title)}. Progress and verified milestones are saved for this profile.</p><div class="guide-actions">${r.status==='completed'?'':button(r.status==='active'?'pause':'resume',r.status==='active'?'Pause Tutorial':'Resume Tutorial')}${button('objective',r.status==='completed'?'View Completion':'View Current Objective')}${button('restart','Restart Tutorial')}${button('skip','Skip Tutorial')}</div><label class="field">Tutorial aquarium<select id="tutorial-aquarium"><option value="">Choose an owned saltwater aquarium</option>${AL.game.tanks.map(t=>`<option value="${esc(t.id)}" ${r.tankId===t.id?'selected':''} ${t.water==='marine'?'':'disabled'}>${esc(t.name)} · ${AL.Units.volume(t.volume)} · ${t.water==='marine'?'Saltwater':'Freshwater (locked)'}</option>`).join('')}</select></label><details><summary>Verified tutorial milestones (${Object.keys(r.completed).length})</summary>${Object.values(r.completed).map(v=>`<p>${esc(T.byId[v.id].title)}: ${esc(v.evidence)}</p>`).join('')||'<p>No tasks have been verified yet.</p>'}</details></section>`+debugLog();}
 function debugLog(){const r=T.state(AL.game);return `<details id="local-debug-log"><summary>Local Debug Log</summary><p>Last 200 tutorial events for this profile. No network logging. Last main save: ${new Date(AL.game.savedAt).toLocaleString()}.</p><button data-guide="export-debug">Export debug JSON</button>${r.audit.slice().reverse().map(e=>`<p><strong>${esc(e.kind)}</strong> · ${esc(e.stepId)} · ${esc(AL.Clock.stamp(e.time))}<br>${esc(e.detail)}</p>`).join('')||'<p>No events yet.</p>'}</details>`;}
 function bind(){if(started)return;started=true;layer=document.createElement('div');layer.id='tutorial-layer';layer.hidden=true;layer.innerHTML='<div class="tutorial-ring" aria-hidden="true"></div>'+Array(4).fill('<div class="tutorial-shade" aria-hidden="true"></div>').join('')+'<aside id="tutorial-tooltip" aria-label="Current saltwater tutorial objective" aria-live="polite" aria-atomic="false"></aside>';document.body.append(layer);tip=$('tutorial-tooltip');ring=q('.tutorial-ring',layer);shades=all('.tutorial-shade',layer);
  confirmDialog=document.createElement('dialog');confirmDialog.id='tutorial-confirm';confirmDialog.setAttribute('aria-label','Confirm tutorial choice');document.body.append(confirmDialog);confirmDialog.addEventListener('cancel',()=>schedule());confirmDialog.addEventListener('close',()=>schedule());
  const launch=document.createElement('button');launch.id='tutorial-current';launch.className='quiet';launch.textContent='Guide';launch.dataset.guide='objective';launch.setAttribute('aria-label','View current tutorial objective');q('.tank-tools').prepend(launch);
  for(const type of ['click','change'])document.addEventListener(type,capture,true);document.addEventListener('keydown',e=>{if(['Enter',' '].includes(e.key))capture(e);});
  document.addEventListener('click',e=>{const confirm=e.target.closest('[data-guide-confirm]');if(confirm){const op=confirm.dataset.guideConfirm;confirmDialog.close();try{AL.game=K.act(AL.game,'tutorialProgress',{op,confirmed:true});AL.UI.save();AL.Shell.render();}catch(err){AL.UI.toast(err.message,true);}schedule();return;}const b=e.target.closest('[data-guide]');if(!b)return;const op=b.dataset.guide;if(op==='cancel-confirm'){confirmDialog.close();return;}if(op==='export-debug'){const blob=new Blob([JSON.stringify({profileId:AL.game.accountId,events:T.state(AL.game).audit},null,2)],{type:'application/json'}),url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download='AquariumLife-Tutorial-Debug.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);return;}control(op);});
  document.addEventListener('change',e=>{if(e.target.id!=='tutorial-aquarium'||!e.target.value)return;try{AL.game=K.act(AL.game,'tutorialProgress',{op:'chooseTank',tankId:e.target.value});AL.UI.save();AL.Shell.render();schedule();}catch(err){AL.UI.toast(err.message,true);}});
  observer=new MutationObserver(records=>{if(records.every(e=>layer.contains(e.target)||e.target===layer||confirmDialog.contains(e.target)))return;schedule();});observer.observe(document.body,{childList:true,subtree:true,attributes:true,attributeFilter:['open','hidden']});window.addEventListener('resize',()=>{position();schedule();});document.addEventListener('scroll',position,true);schedule();
 }
 return {bind,update,schedule,preferences,debugLog,consumeInteraction,focusObjective,resolve,position,get target(){return target;},legacy:op=>control(op==='show'?'objective':op)};
})();
