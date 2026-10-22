"""Heater/mortality evidence in isolated network-disabled browsers."""
import json,time,base64
def run(c,root,name):
 out=root/'tests/heater-evidence';out.mkdir(exist_ok=True);c.sock.settimeout(180)
 c.navigate(root/'index.html')
 for _ in range(300):
  if c.evaluate('!!window.AL?.game&&!!AL.MortalityUI'):break
  time.sleep(.05)
 else:raise RuntimeError('Heater/mortality game did not boot: '+str([e for e in c.events if e.get('method')=='Runtime.exceptionThrown']))
 c.evaluate('AL.Startup.finish();AL.UI.close();AL.Store.close();AL.Shell.close();AL.game.settings.speed=0')
 # This runner uses a disposable QA browser profile, never the player's profile.
 c.evaluate("for(let i=localStorage.length-1;i>=0;i--){const k=localStorage.key(i);if(k.startsWith('aquarium-life-mortality-v2:'))localStorage.removeItem(k);}")
 c.evaluate((root/'tests/overnight_probe.js').read_text(encoding='utf-8'))
 result=c.evaluate((root/'tests/heater_checks.js').read_text(encoding='utf-8'))
 (out/f'{name}-logic.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
 print(json.dumps({'passed':result['passed'],'failed':result['failed'],'failures':[r for r in result['checks'] if not r['pass']]},indent=2),flush=True)
 if result['failed']:return 1
 c.evaluate('window.repairedSim=AL.Sim')
 try:
  c.evaluate((root/'planning/heater-mortality/simulation-before.js').read_text(encoding='utf-8'))
  baseline=c.evaluate('heaterThermalMatrix()')
 finally:c.evaluate('AL.Sim=repairedSim')
 (out/f'{name}-original-thermal.json').write_text(json.dumps(baseline,indent=2),encoding='utf-8')
 ui=[]
 def check(label,expr):
  try:ui.append({'name':label,'pass':bool(c.evaluate(expr))})
  except Exception as error:ui.append({'name':label,'pass':False,'error':str(error)})
 def shot(label):
  data=c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data'];(out/f'{name}-{label}.png').write_bytes(base64.b64decode(data))
 c.call('Emulation.setDeviceMetricsOverride',{'width':1366,'height':900,'deviceScaleFactor':1,'mobile':False})
 c.evaluate("AL.game=overnightFixture('mixed-feeder');AL.game.tanks[0].waterParams.temperature=22;AL.UI.updateVitals()")
 check('Sidebar warns of actual resident temperature despite normal chemistry',"document.getElementById('condition').textContent==='Needs care'&&document.getElementById('water-warning').textContent.includes('Temperature outside resident range')")
 shot('temperature-warning')
 c.evaluate("AL.game=overnightFixture('healthy-feeder');AL.game.tanks[0].fish=[];AL.UI.updateVitals()")
 check('An empty tank is not called biologically balanced',"document.getElementById('condition').textContent==='Empty aquarium'")
 c.evaluate("AL.game=overnightFixture('mixed-feeder');window.heaterReturn=AL.Offline.sync(AL.game,AL.game.simulationCheckpoint+28800000);AL.Core.kill(AL.game,AL.game.tanks[0],AL.game.tanks[0].fish[0],'Unknown');AL.Shell.open('equipment','care');AL.InventoryUI.inspect({type:'heater'})")
 check('Equipment shows actual output separately from target',"['Temperature control','thermostat 25','Available','currently delivered'].every(x=>document.getElementById('dialog-body').textContent.includes(x))")
 c.evaluate("AL.UI.close();AL.Shell.close();AL.game=overnightFixture('healthy-feeder');AL.game.tanks[0].equipment=AL.game.tanks[0].equipment.filter(e=>e.type!=='heater');AL.Store.open('equipment','saltwater')")
 check('Store lists seven distinct heater ranges and recommends the actual tank size',"AL.Store.products().filter(p=>p.args.heaterModel).length===7&&document.getElementById('store-products').textContent.includes('15,000 gal')&&document.getElementById('store-products').textContent.includes('Recommended size for selected aquarium')")
 shot('heater-store')
 c.evaluate("AL.Store.details('equipment:heater:marine-heater-1')")
 check('A smaller heater can be stored but installation checks reject this tank capacity',"!document.getElementById('confirm-fish').disabled&&document.getElementById('compatibility-report').textContent.includes('Inventory')&&!AL.Inventory.equipmentReport(AL.game,{type:'heater',capacity:AL.Heaters.models[0].capacity},AL.game.tanks[0]).ok")
 c.evaluate("AL.UI.close();AL.Store.details('equipment:heater:marine-heater-4');window.heaterMoney=AL.game.credits;window.heaterDestination=AL.game.selectedTank;document.querySelector('[data-form=storePurchase]').requestSubmit()")
 check('Real purchase stores the chosen fixed model with correct price and persistent aquarium',"AL.game.ownedEquipment.some(e=>e.heaterModel==='marine-heater-4')&&!AL.game.tanks[0].equipment.some(e=>e.type==='heater')&&AL.game.credits===heaterMoney-AL.Heaters.get('marine-heater-4').price&&AL.game.selectedTank===heaterDestination")
 c.evaluate("AL.UI.close();AL.Store.close();AL.UI.transact('installOwnedEquipment',{id:AL.game.ownedEquipment.find(e=>e.heaterModel==='marine-heater-4').id});AL.UI.updateVitals()")
 check('Main tank view exposes heater state, model rating and condition',"['Heater','L4','Heater condition'].every(x=>document.getElementById('water-stats').textContent.includes(x))")
 c.evaluate("AL.Shell.close();AL.game=overnightFixture('disease');window.heaterReturn=AL.Offline.sync(AL.game,AL.game.simulationCheckpoint+28800000);AL.Offline.report(heaterReturn)")
 check('Welcome Back has accurate recorded loss count and View Death Reports',"document.getElementById('dialog-body').textContent.includes('During your absence, 1 livestock deaths were recorded.')&&!!document.querySelector('[data-view-deaths]')")
 c.evaluate("document.querySelector('[data-view-deaths]').click()")
 check('Welcome Back opens Livestock Deaths filtered to this offline run',"document.getElementById('primary-content').textContent.includes('Livestock Deaths')&&document.getElementById('primary-content').textContent.includes('latest selected offline simulation period')&&document.querySelectorAll('[data-death-report]').length===1")
 c.evaluate("document.querySelector('[data-death-report]').click()")
 check('Full report distinguishes before/after health, actual/target heat, evidence and mode',"['Livestock Death Report','Health before fatal update','heater target 25','offline simulation','Preceding condition history','Marine velvet'].every(x=>document.getElementById('dialog-body').textContent.includes(x))")
 shot('death-report-desktop')
 downloads=out/(name+'-downloads')/str(time.time_ns());downloads.mkdir(parents=True,exist_ok=True)
 c.call('Browser.setDownloadBehavior',{'behavior':'allow','downloadPath':str(downloads.resolve())})
 c.evaluate("document.querySelector('#dialog-body [data-mortality-export]').click()")
 for _ in range(100):
  if list(downloads.glob('LIVESTOCK_DEATH_REPORT*.json')):break
  time.sleep(.05)
 selected=list(downloads.glob('LIVESTOCK_DEATH_REPORT*.json'))
 ui.append({'name':'Selected report downloads valid exact structured death evidence offline','pass':bool(selected) and json.loads(selected[0].read_text(encoding='utf-8'))['record']['cause']=='Marine velvet'})
 c.evaluate("AL.UI.close();document.querySelector('[data-mortality-clear]').click();document.querySelector('[data-mortality-export=all]').click()")
 for _ in range(100):
  if list(downloads.glob('LIVESTOCK_MORTALITY_LOG*.json')):break
  time.sleep(.05)
 logs=list(downloads.glob('LIVESTOCK_MORTALITY_LOG*.json'));export=json.loads(logs[0].read_text(encoding='utf-8')) if logs else {}
 ui.append({'name':'Full local mortality export contains this account events and offline audit runs without credentials','pass':bool(export.get('records')) and bool(export.get('offlineRuns')) and export.get('accountId')==c.evaluate('AL.game.accountId') and 'password' not in json.dumps(export).lower()})
 c.evaluate("document.querySelector('[data-mortality-filter=mode]').value='live';document.querySelector('[data-mortality-filter=mode]').dispatchEvent(new Event('change',{bubbles:true}))")
 check('Live filter excludes this offline death',"document.querySelectorAll('[data-death-report]').length===0")
 c.evaluate("document.querySelector('[data-mortality-clear]').click()")
 for field,value in [('tank',c.evaluate('AL.game.tanks[0].id')),('species','clown'),('cause','Marine velvet'),('date',c.evaluate("new Date(AL.game.mortality.events[0].realTimestamp).toLocaleDateString('en-CA')")),('day',str(c.evaluate('AL.game.mortality.events[0].gameDay')))]:
  c.evaluate(f"document.querySelector('[data-mortality-filter={field}]').value={json.dumps(value)};document.querySelector('[data-mortality-filter={field}]').dispatchEvent(new Event('change',{{bubbles:true}}))")
  check(field+' filter retains the matching recorded death',"document.querySelectorAll('[data-death-report]').length===1")
 c.call('Emulation.setDeviceMetricsOverride',{'width':390,'height':900,'deviceScaleFactor':1,'mobile':False})
 check('Mortality filters fit mobile viewport',"document.documentElement.scrollWidth<=innerWidth&&document.getElementById('primary-content').scrollWidth<=document.getElementById('primary-content').clientWidth")
 c.evaluate("document.getElementById('livestock-deaths').scrollIntoView({block:'start'})")
 shot('history-mobile')
 c.evaluate("AL.Shell.close();AL.UI.save();window.heaterSaved={account:AL.game.accountId,ids:AL.Mortality.records(AL.game).map(e=>e.id),time:AL.game.time}")
 saved=c.evaluate('heaterSaved');c.navigate(root/'index.html')
 for _ in range(300):
  if c.evaluate('!!window.AL?.game&&!!AL.MortalityUI'):break
  time.sleep(.04)
 check('Actual reload keeps the account and permanent death IDs without duplicating a death',f"AL.game.accountId==={json.dumps(saved['account'])}&&JSON.stringify(AL.Mortality.records(AL.game).map(e=>e.id))==={json.dumps(json.dumps(saved['ids'],separators=(',',':')))}")
 errors=[e for e in c.events if e.get('method')=='Runtime.exceptionThrown'];network=[e['params']['request']['url'] for e in c.events if e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('http:','https:'))]
 ui.extend([{'name':'No uncaught JS errors','pass':not errors,'errors':errors},{'name':'No external network requests','pass':not network,'requests':network}])
 report={'passed':result['passed']+sum(r['pass'] for r in ui),'failed':sum(not r['pass'] for r in ui),'logic':result,'ui':ui}
 (out/f'{name}-results.json').write_text(json.dumps(report,indent=2),encoding='utf-8');print(json.dumps({'passed':report['passed'],'failed':report['failed'],'failures':[r for r in ui if not r['pass']]},indent=2),flush=True)
 return int(bool(report['failed']))
