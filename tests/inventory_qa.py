"""Stored physical ownership, UI routes and responsive acceptance in isolated offline browsers."""
import base64,json,time,sys
def run(c,root,name):
 out=root/'tests/inventory-evidence';out.mkdir(exist_ok=True)
 entry=root/('DIST/index.html' if '--dist' in sys.argv else 'index.html')
 c.navigate(entry);c.sock.settimeout(120)
 for _ in range(300):
  if c.evaluate('!!window.AL?.game&&!!AL.InventoryUI'):break
  time.sleep(.05)
 else:raise RuntimeError('Boot failed: '+str([e for e in c.events if e.get('method')=='Runtime.exceptionThrown']))
 checks=c.evaluate((root/'tests/inventory_checks.js').read_text(encoding='utf8'))['checks']
 def js(s):return c.evaluate('(()=>{'+s+'})()')
 def ck(label,expr):
  try:
   passed=bool(c.evaluate(expr));row={'name':label,'pass':passed}
   if not passed:row['diagnostic']=c.evaluate("({heater:AL.game?.tanks[0].equipment.find(e=>e.type==='heater'),water:AL.game?.tanks[0].waterParams.temperature,saveError:AL.Save.lastError,toast:document.getElementById('toast').textContent,leaderHeight:document.querySelector('[data-page=settings]').getBoundingClientRect().height,sidebarOverflow:getComputedStyle(document.querySelector('.sidebar')).overflowY})")
   checks.append(row)
  except Exception as e:checks.append({'name':label,'pass':False,'error':str(e)})
 js("AL.Startup.finish();AL.Save.unlock();AL.UI.close();AL.Shell.close();AL.game=AL.Core.newGame('marine',Date.now());AL.game.settings.speed=0;AL.game.credits=100000;delete AL.game.finance;delete AL.game.progression;AL.Finance.initialize(AL.game);AL.Progression.migrate(AL.game);AL.game.update29.tutorial.status='skipped';AL.game=AL.Core.act(AL.game,'buyEquipment',{type:'heater',heaterModel:AL.Heaters.models[1].id});AL.UI.render();")
 ck('Sidebar exact requested order',"JSON.stringify([...document.querySelectorAll('#navigation button')].map(b=>b.dataset.page))===JSON.stringify(['aquariums','store','journal','equipment','casino','settings'])")
 js("AL.Shell.open('journal')")
 ck('Removed Field Journal breeding and leaderboard tabs',"![...document.querySelectorAll('#primary-tabs button')].some(b=>['breeding','leaderboards'].includes(b.dataset.primaryTab))")
 for target in ['aquariums','settings']:
  js("AL.Shell.close();document.querySelector('#navigation [data-page="+target+"]').click()")
  ck(target+': existing sidebar route opens its management window',"AL.Shell.active==="+json.dumps(target))
 js("AL.Shell.open('journal','breeding')")
 ck('Legacy breeding route redirects to collection; eggs still accessible',"AL.Shell.subtab==='collection'&&document.getElementById('primary-content').textContent.includes('fish species discovered')")
 js("AL.Shell.open('journal','leaderboards')")
 ck('Legacy leaderboard route opens the single relocated view',"AL.Shell.active==='aquariums'&&!!document.querySelector('.tank-comparison')")
 js("AL.Shell.open('equipment','care')")
 ck('No standalone temperature or readiness panel, thermostat form or stored list in Tank Care',"!document.querySelector('#primary-content #overnight-readiness,#primary-content #heater-diagnostics,#primary-content form[data-form=controls]')&&!document.getElementById('primary-content').textContent.includes('Stored equipment')")
 js("document.querySelector('#primary-content [data-action=inspectEquipment]').click()")
 # First installed item may be a filter: explicitly inspect heater.
 js("AL.InventoryUI.inspect({type:'heater'})")
 ck('Individual heater retains accessible thermostat control',"!!document.querySelector('[data-form=equipmentThermostat]')")
 js("const f=document.querySelector('[data-form=equipmentThermostat]');f.elements.temperature.value='27';f.requestSubmit()")
 ck('Thermostat UI saves setting without instantly changing water',"AL.game.tanks[0].equipment.find(e=>e.type==='heater').temperatureTarget===27&&Math.abs(AL.game.tanks[0].waterParams.temperature-25)<.1")
 js("AL.UI.close();AL.Shell.open('journal','history');window.runCount=AL.game.mortality.runs.length;AL.Shell.open('journal','history')")
 ck('History Reports retained and opening creates no report',"document.getElementById('primary-content').textContent.includes('Reports')&&AL.game.mortality.runs.length===runCount")
 js("AL.Shell.open('equipment','inventory')")
 ck('Inventory tab selected; only stored physical entries and existing supplies',"AL.Shell.subtab==='inventory'&&document.querySelectorAll('#primary-content [data-action=inventoryInstall]').length===1&&!document.getElementById('primary-content').textContent.includes('Installed by Aquarium')")
 for w,h in [(1920,1080),(1600,900),(1366,768),(764,900),(390,844)]:
  c.call('Emulation.setDeviceMetricsOverride',{'width':w,'height':h,'deviceScaleFactor':1,'mobile':False});time.sleep(.15)
  ck(f'{w}x{h}: inventory/cards fit viewport and modal',"document.documentElement.scrollWidth<=innerWidth&&document.getElementById('primary-content').scrollWidth<=document.getElementById('primary-content').clientWidth+1")
  ck(f'{w}x{h}: sidebar controls visible or scrollable',"document.querySelector('#navigation [data-page=settings]').getBoundingClientRect().height<65&&getComputedStyle(document.querySelector('.sidebar')).overflowY==='auto'")
  (out/f'{name}-inventory-{w}.png').write_bytes(base64.b64decode(c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
 js("const q=document.getElementById('inventory-search');q.value='NoMatchingPhysicalItem';q.dispatchEvent(new Event('input',{bubbles:true}))")
 ck('Search filters storage and preserves input focus',"!document.querySelector('#primary-content [data-action=inventoryInstall]')&&document.activeElement.id==='inventory-search'")
 js("document.getElementById('inventory-category').value='heaters';document.getElementById('inventory-category').dispatchEvent(new Event('change',{bubbles:true}));const q=document.getElementById('inventory-search');q.value='';q.dispatchEvent(new Event('input',{bubbles:true}))")
 ck('Category and search combine; clearing search preserves selected category',"document.getElementById('inventory-category').value==='heaters'&&document.querySelectorAll('.inventory-cards .item-card').length===1")
 js("document.getElementById('inventory-category').value='all';document.getElementById('inventory-category').dispatchEvent(new Event('change',{bubbles:true}))")
 js("const q=document.getElementById('inventory-search');q.value='';q.dispatchEvent(new Event('input',{bubbles:true}));document.querySelector('#primary-content [data-action=inventoryInstall]').click()")
 ck('Install dialog lists owned occupied aquarium with exact conflict reason',"document.querySelectorAll('#inventory-destination option').length===AL.game.tanks.length&&document.getElementById('inventory-compatibility').textContent.includes('already installed')&&document.getElementById('inventory-confirm').disabled")
 js("AL.UI.close();const t=AL.Core.tank(AL.game,'marine',75,'Inventory destination','reef');t.equipment=[];AL.game.tanks.push(t);window.installTank=t.id;window.storedUnit=AL.game.ownedEquipment[0].id;AL.Shell.open('equipment','inventory');document.querySelector('#primary-content [data-action=inventoryInstall]').click()")
 ck('Eligible destination appears beside disabled occupied destination',"document.querySelectorAll('#inventory-destination option').length===2&&document.getElementById('inventory-destination').value===installTank&&!document.getElementById('inventory-confirm').disabled")
 js("document.querySelector('[data-form=inventoryDestination]').requestSubmit()")
 ck('Confirm install moves unit exclusively to chosen tank and retains current selection',"!AL.game.ownedEquipment.length&&AL.game.tanks[1].equipment[0].id===storedUnit&&AL.game.selectedTank===AL.game.tanks[0].id")
 js("AL.UI.transact('selectAquarium',{id:installTank});AL.Shell.open('equipment','care');AL.InventoryUI.inspect({id:storedUnit});document.querySelector('#dialog-body [data-action=uninstallEquipment]').click()")
 ck('Removal UI warns of life-support consequences before changing ownership',"document.getElementById('dialog-body').textContent.includes('deteriorating water quality')&&AL.game.tanks[1].equipment.length===1")
 js("document.querySelector('[data-action=inventoryRemoveConfirmed]').click()")
 ck('Confirmed removal returns original instance to Inventory',"AL.game.ownedEquipment.length===1&&AL.game.ownedEquipment[0].id===storedUnit&&!AL.game.tanks[1].equipment.length")
 js("AL.UI.close();AL.Shell.close();AL.Store.open('equipment','saltwater');AL.Store.details('equipment:filter')")
 ck('Store purchase explicitly labels Inventory delivery',"document.getElementById('dialog-body').textContent.includes('purchase goes to Inventory')&&!document.getElementById('confirm-fish').disabled")
 js("document.querySelector('[data-form=storePurchase]').requestSubmit()")
 ck('Store confirmation purchases into storage instead of installing',"AL.game.ownedEquipment.some(e=>e.type==='filter')&&!AL.game.tanks[1].equipment.some(e=>e.type==='filter')&&AL.game.selectedTank===installTank")
 js("AL.UI.close();AL.Store.close();AL.Shell.close();AL.UI.save()")
 expected=c.evaluate('JSON.stringify(AL.game.ownedEquipment)')
 c.navigate(entry)
 for _ in range(300):
  if c.evaluate('!!window.AL?.game'):break
  time.sleep(.05)
 ck('Reload loads exact locally stored equipment identities and condition','JSON.stringify(AL.game.ownedEquipment)==='+json.dumps(expected))
 errors=[e for e in c.events if e.get('method')=='Runtime.exceptionThrown']
 checks.append({'name':'No runtime exceptions','pass':not errors,'errors':errors})
 result={'checks':checks,'passed':sum(x['pass'] for x in checks),'failed':sum(not x['pass'] for x in checks),'networkDisabled':True}
 (out/f'{name}-results.json').write_text(json.dumps(result,indent=2),encoding='utf8')
 print(json.dumps({'passed':result['passed'],'failed':result['failed'],'failures':[x for x in checks if not x['pass']]},indent=2))
 if result['failed']:raise AssertionError('Inventory acceptance failed')
 return 0
