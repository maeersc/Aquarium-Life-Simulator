"""Actual offline store UI, guarded transactions and viewport evidence."""
import base64,hashlib,json,sys,time

def run(c,root,name):
 out=root/'tests/ui-quantity-evidence';out.mkdir(exist_ok=True);c.sock.settimeout(180)
 entry=root/('DIST/index.html' if '--dist' in sys.argv else 'index.html')
 c.call('Network.emulateNetworkConditions',{'offline':True,'latency':0,'downloadThroughput':0,'uploadThroughput':0})
 c.call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':900,'deviceScaleFactor':1,'mobile':False})
 c.navigate(entry,timeout=90)
 for _ in range(600):
  if c.evaluate('!!window.AL?.game&&!!AL.Store'):break
  time.sleep(.05)
 else:raise RuntimeError('Game did not boot')
 c.evaluate('AL.Startup.finish();AL.Save.unlock();AL.UI.close();AL.Store.close();AL.Shell.close();AL.game.settings.speed=0;window.quantityBase='+ (root/'tests/performance-evidence/fixture-small.json').read_text(encoding='utf8'))
 result=c.evaluate((root/'tests/ui_quantity_checks.js').read_text(encoding='utf8'));checks=result['checks']
 print(json.dumps({'stage':'model','passed':result['passed'],'failed':result['failed'],'failures':[r for r in checks if not r['pass']]}),flush=True)
 def js(s):return c.evaluate('(()=>{'+s+'})()')
 def ck(label,expr):
  try:checks.append({'name':label,'pass':bool(c.evaluate('!!('+expr+')'))})
  except Exception as e:checks.append({'name':label,'pass':False,'error':str(e)})
 def click(selector):
  p=c.evaluate('(()=>{const e=document.querySelector('+json.dumps(selector)+');e.scrollIntoView({block:"center"});const r=e.getBoundingClientRect();return {x:r.x+r.width/2,y:r.y+r.height/2};})()')
  c.call('Input.dispatchMouseEvent',{'type':'mousePressed','button':'left','clickCount':1,**p});c.call('Input.dispatchMouseEvent',{'type':'mouseReleased','button':'left','clickCount':1,**p})
 def quantity(value):
  click('#purchase-quantity');js("document.querySelector('#purchase-quantity').select()");c.call('Input.insertText',{'text':str(value)})
 js("AL.game=quantityFixture();AL.UI.render();AL.Store.open('equipment','saltwater');AL.Store.details('equipment:filter')")
 ck('Details exposes unit price, accessible quantity stepper and total',"!!document.querySelector('#purchase-quantity')&&document.querySelector('.purchase-totals').textContent.includes('Unit Price')&&document.querySelector('.purchase-totals').textContent.includes('Total Cost')")
 click('[data-quantity-step="1"]');click('[data-quantity-step="1"]')
 ck('Trusted plus buttons instantly update quantity and exact total',"document.querySelector('#purchase-quantity').value==='3'&&document.querySelector('#purchase-total').textContent===String(AL.StoreRules.quote(AL.game,AL.Core.selected(AL.game),'buyEquipment',{type:'filter',quantity:3}).total)+' AC'")
 click('[data-quantity-step="-1"]')
 ck('Trusted minus preserves whole positive quantities',"document.querySelector('#purchase-quantity').value==='2'")
 quantity(3)
 js("window.beforeQuantity={credits:AL.game.credits,stock:AL.game.stock.filter,owned:AL.game.ownedEquipment.length,rows:AL.game.finance.rows.length,selected:AL.game.selectedTank,total:AL.StoreRules.quote(AL.game,AL.Core.selected(AL.game),'buyEquipment',{type:'filter',quantity:3}).total};window.purchaseForm=document.querySelector('[data-form=storePurchase]')")
 for w,h in [(1920,1080),(1600,900),(1366,768),(390,844)]:
  c.call('Emulation.setDeviceMetricsOverride',{'width':w,'height':h,'deviceScaleFactor':1,'mobile':False});time.sleep(.15)
  ck(f'{w}x{h}: store details and quantity controls do not overflow',"document.documentElement.scrollWidth<=innerWidth&&document.querySelector('#dialog').scrollWidth<=document.querySelector('#dialog').clientWidth+1")
  (out/f'{name}-store-{w}.png').write_bytes(base64.b64decode(c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
 c.call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':900,'deviceScaleFactor':1,'mobile':False})
 click('#confirm-fish');js("purchaseForm.dispatchEvent(new Event('submit',{bubbles:true,cancelable:true}))")
 ck('Actual purchase and immediate duplicate submission charge once and create3 identities',"AL.game.credits===beforeQuantity.credits-beforeQuantity.total&&AL.game.stock.filter===beforeQuantity.stock-3&&AL.game.ownedEquipment.length===beforeQuantity.owned+3&&AL.game.finance.rows.length===beforeQuantity.rows+1&&AL.game.selectedTank===beforeQuantity.selected")
 js("AL.Store.details('equipment:filter')")
 for value in ['0','-2','1.5','99','']:
  quantity(value)
  ck('UI invalid/excessive quantity '+repr(value)+' disables confirmation',"document.querySelector('#confirm-fish').disabled")
 js("AL.UI.close();AL.Store.open('supplies','saltwater');AL.Store.details('food:pellets')")
 quantity(2);js("window.foodBefore=AL.game.inventory.pellets");click('#confirm-fish')
 ck('Actual food UI adds40 portions for2 packs',"AL.game.inventory.pellets===foodBefore+40")
 js("AL.Store.details('supply:salt')");quantity(2);js("window.saltBefore=AL.game.inventory.salt");click('#confirm-fish')
 ck('Actual supply UI retains doses per pack',"AL.game.inventory.salt===saltBefore+AL.Data.supplies.salt.amount*2")
 js("AL.Store.open('medicines','saltwater');AL.Store.details('medicine:diagnostic')");quantity(2)
 click('#confirm-fish')
 ck('Actual ordinary medical purchase records pack count',"AL.game.finance.rows.at(-1).quantity===2&&AL.game.finance.rows.at(-1).action==='buyMedicine'")
 js("AL.Store.open('rocks','saltwater');const p=AL.Store.products().find(p=>p.kind==='rock');window.rockProduct=p;AL.Store.details(p.id)");quantity(2)
 ck('Rock details explicitly explain storage then individual placement',"document.querySelector('#quantity-help').textContent.includes('Inventory')")
 js("window.objectBefore=AL.game.ownedObjects.length");click('#confirm-fish')
 ck('Actual bulk rock UI adds2 stored pieces without entering placement',"AL.game.ownedObjects.length===objectBefore+2&&!AL.UI.placing")
 js("AL.Store.open('sand','saltwater');AL.Store.details(AL.Store.products()[0].id)")
 ck('Substrate stays a single depth installation with explanation',"!document.querySelector('#purchase-quantity')&&document.querySelector('#quantity-help').textContent.includes('One substrate installation')")
 js("AL.UI.close();AL.Store.open('equipment','saltwater');AL.Store.details('supply:frag-kit')")
 ck('Reusable tools remain individually owned',"!document.querySelector('#purchase-quantity')&&document.querySelector('#quantity-help').textContent.includes('Reusable')")
 js("AL.UI.close();AL.Store.close();window.selectedBefore=AL.game.selectedTank;AL.Store.open('fish','saltwater')")
 ck('Store opening retains selected aquarium and shows its name',"AL.game.selectedTank===selectedBefore&&document.querySelector('#store-destination-name').textContent===AL.Core.selected(AL.game).name")
 click('[data-store-action=tab][data-store-args*=freshwater]')
 ck('Freshwater stays locked and preserves destination',"AL.Store.tab==='saltwater'&&AL.game.selectedTank===selectedBefore")
 click('[data-store-action=tab][data-store-args*=black]')
 ck('Deep Market tab preserves selected destination',"AL.Store.tab==='black'&&AL.game.selectedTank===selectedBefore")
 js("AL.game.time=Math.floor(AL.game.time/1440)*1440+1260;AL.game.stats.nightMarket=1;AL.Store.open('equipment','black');AL.Store.details('equipment:containment')")
 quantity(2)
 ck('Deep Market equipment uses the same quantity UI and current quote',"!document.querySelector('#confirm-fish').disabled&&document.querySelector('#purchase-quantity-summary').textContent==='2'")
 click('#confirm-fish')
 ck('Deep Market uses shared equipment delivery and ledger category',"AL.game.ownedEquipment.filter(e=>e.type==='containment').length===2&&AL.game.finance.rows.at(-1).category==='market'&&AL.game.finance.rows.at(-1).quantity===2")
 js("AL.UI.close();AL.Store.close();AL.Store.open('supplies','saltwater')")
 ck('Close/reopen retains current aquarium',"AL.game.selectedTank===selectedBefore&&document.querySelector('#store-destination').value===selectedBefore")
 js("AL.Store.close();AL.UI.render();AL.game.settings.speed=1")
 for w,h in [(1920,1080),(1600,900),(1366,768),(390,844)]:
  c.call('Emulation.setDeviceMetricsOverride',{'width':w,'height':h,'deviceScaleFactor':1,'mobile':False});time.sleep(.25)
  ck(f'{w}x{h}: familiar layout has no horizontal overflow',"document.documentElement.scrollWidth<=innerWidth")
  if w>760:ck(f'{w}x{h}: aquarium header aligns with wellbeing column',"Math.abs(document.querySelector('#new-tank').getBoundingClientRect().right-document.querySelector('.right-column .panel').getBoundingClientRect().right)<5")
  (out/f'{name}-aquarium-{w}.png').write_bytes(base64.b64decode(c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
 ck('Background is black with a static repeat and solid slate panels',"getComputedStyle(document.body).backgroundColor==='rgb(0, 0, 0)'&&getComputedStyle(document.body).backgroundImage.includes('downward-scales.svg')&&getComputedStyle(document.body).animationName==='none'&&getComputedStyle(document.querySelector('.panel')).backgroundColor==='rgb(52, 70, 92)'")
 ck('Aquarium Canvas has no decorative background image or overlay',"getComputedStyle(document.querySelector('#aquarium')).backgroundImage==='none'&&!document.querySelector('.canvas-wrap [data-scales]')")
 for window,tab in [('journal','history'),('equipment','inventory'),('aquariums','owned'),('settings','preferences')]:
  js(f"AL.Shell.open('{window}','{tab}')")
  time.sleep(.2) # Allow the existing short background-color transition to finish.
  ck('Existing sidebar destination '+window+' remains usable',"document.querySelector('#primary-dialog').open&&document.querySelector('#primary-content').textContent.length>0")
  ck('Selected sidebar state '+window+' retains a solid highlighted surface',"getComputedStyle(document.querySelector('#navigation button.active')).backgroundColor==='rgb(64, 86, 110)'")
 js('AL.Shell.close()')
 c.call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':900,'deviceScaleFactor':1,'mobile':False})
 perf=c.evaluate("""(async()=>{const samples=[],draw=AL.renderer.draw;let frames=0,drawMs=0;AL.renderer.draw=function(...a){const start=performance.now();const r=draw.apply(this,a);frames++;drawMs+=performance.now()-start;return r;};const style=document.createElement('style');document.head.append(style);try{for(const enabled of [false,true]){style.textContent=enabled?'':'body,.sidebar{background-image:none!important}';await new Promise(r=>setTimeout(r,500));frames=0;drawMs=0;const start=performance.now();await new Promise(r=>setTimeout(r,3000));const elapsed=performance.now()-start;samples.push({pattern:enabled,frames,elapsed,fps:frames/(elapsed/1000),drawMs,meanDrawMs:drawMs/frames});}return {samples,stats:AL.loop.stats};}finally{style.remove();AL.renderer.draw=draw;}})()""")
 checks.append({'name':'Static texture retains capped scene FPS (within10% in same-scene comparison)','pass':perf['samples'][1]['fps']>=perf['samples'][0]['fps']*.9,'samples':perf['samples']})
 js("AL.game.settings.speed=0;window.beforeLocalReload=JSON.stringify({ownedEquipment:AL.game.ownedEquipment,ownedObjects:AL.game.ownedObjects,inventory:AL.game.inventory,medical:AL.game.medicalInventory,selected:AL.game.selectedTank,credits:AL.game.credits,rows:AL.game.finance.rows});window.saveResult=AL.UI.save()")
 ck('Local save accepts the complete purchased state',"saveResult.ok")
 expected=c.evaluate('beforeLocalReload');c.navigate(entry,timeout=90)
 for _ in range(600):
  if c.evaluate('!!window.AL?.game'):break
  time.sleep(.05)
 ck('Browser reload preserves exact items/stacks/identities/wallet/receipts/destination',"JSON.stringify({ownedEquipment:AL.game.ownedEquipment,ownedObjects:AL.game.ownedObjects,inventory:AL.game.inventory,medical:AL.game.medicalInventory,selected:AL.game.selectedTank,credits:AL.game.credits,rows:AL.game.finance.rows})==="+json.dumps(expected))
 errors=[e for e in c.events if e.get('method')=='Runtime.exceptionThrown'];checks.append({'name':'No uncaught runtime exceptions','pass':not errors,'errors':errors})
 paths=[*json.loads((root/'planning/ui-quantity/baseline/hashes.json').read_text()),'assets/ui/downward-scales.svg']
 runtime={p:hashlib.sha256((entry.parent/p).read_bytes()).hexdigest() for p in paths}
 result={'entry':str(entry),'runtimeSha256':runtime,'checks':checks,'passed':sum(x['pass'] for x in checks),'failed':sum(not x['pass'] for x in checks),'networkDisabled':True,'performance':perf}
 (out/f'{name}-results.json').write_text(json.dumps(result,indent=2),encoding='utf8')
 print(json.dumps({'passed':result['passed'],'failed':result['failed'],'failures':[r for r in checks if not r['pass']]},indent=2),flush=True)
 return int(result['failed']>0)
