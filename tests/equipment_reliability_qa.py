"""Quantitative marine equipment reliability and UI checks; disposable offline browser profiles."""
import base64,json,sys,time
def run(c,root,name):
 out=root/'tests/equipment-reliability-evidence';out.mkdir(exist_ok=True);c.sock.settimeout(300)
 # The unchanged embedded art banks can exceed the generic ten-second cold
 # load allowance. Still require complete initialization and no script errors.
 entry=root/('DIST/index.html' if '--dist' in sys.argv else 'index.html');started=time.monotonic();c.navigate(entry,timeout=60);load_seconds=time.monotonic()-started
 for _ in range(400):
  if c.evaluate('!!window.AL?.game&&!!AL.EquipmentMaintenanceUI'):break
  time.sleep(.05)
 else:raise RuntimeError('Reliability game did not boot')
 c.evaluate('AL.Startup.finish();AL.Save.unlock();AL.UI.close();AL.Store.close();AL.Shell.close();AL.game.settings.speed=0')
 checks=c.evaluate((root/'tests/equipment_reliability_checks.js').read_text(encoding='utf8'))['checks']
 cohorts=c.evaluate((root/'tests/equipment_reliability_cohorts.js').read_text(encoding='utf8'));checks.extend(cohorts['checks'])
 c.evaluate((root/'tests/overnight_probe.js').read_text(encoding='utf8'))
 matrix=c.evaluate("""(()=>{const rows=[];for(const hours of [8,12,24]){const s=overnightFixture('healthy-feeder'),a=JSON.parse(JSON.stringify(s)),b=JSON.parse(JSON.stringify(s)),before=JSON.parse(JSON.stringify(s.tanks[0].equipment));for(let n=0;n<hours*4320;n+=5)AL.Sim.step(a,5);AL.Offline.sync(b,b.simulationCheckpoint+hours*3600000);const projection=s=>JSON.stringify({time:s.time,equipment:s.tanks.map(t=>t.equipment),water:s.tanks.map(t=>t.waterParams),fish:s.tanks.map(t=>t.fish.map(f=>({hp:f.hp,dead:f.dead,hunger:f.hunger,health:f.healthState}))),events:s.equipmentReliability.events});const equal=projection(a)===projection(b),old=JSON.stringify(b.equipmentReliability);AL.Offline.sync(b,b.simulationCheckpoint);rows.push({hours,gameDays:hours*3,equal,noReplay:old===JSON.stringify(b.equipmentReliability),survived:b.tanks[0].fish.every(f=>!f.dead),gear:b.tanks[0].equipment.map(e=>({type:e.type,condition:e.durability,maintenance:e.reliability.maintenance,state:e.reliability.state,operatingHours:e.reliability.operatingHours})),events:b.equipmentReliability.events});}return rows;})()""")
 for r in matrix:
  checks.extend([{'name':str(r['hours'])+'h: full live/offline equipment, chemistry and health equivalence','pass':r['equal']},{'name':str(r['hours'])+'h: repeated login does not repeat equipment events','pass':r['noReplay']},{'name':str(r['hours'])+'h: properly equipped fed aquarium survives','pass':r['survived']}])
 def js(s):return c.evaluate('(()=>{'+s+'})()')
 def ck(label,expr):
  try:checks.append({'name':label,'pass':bool(c.evaluate(expr))})
  except Exception as e:checks.append({'name':label,'pass':False,'error':str(e)})
 js("AL.game=equipmentReliabilityFixture();const t=AL.game.tanks[0],e=t.equipment.find(e=>e.type==='filter');e.reliability.maintenance=40;e.reliability.maintenanceHours=365*24;e.durability=74;window.testEquipment=e.id;window.testCondition=e.durability;window.testBacteria=[t.bacteria,t.bacteria2];AL.UI.render();AL.Shell.open('equipment','care');AL.InventoryUI.inspect({id:e.id})")
 ck('Inspector exposes condition, maintenance, tracked service age, efficiency and maintenance action',"['Physical condition','Maintenance','Tracked service age','Operating efficiency','Maintenance'].every(t=>document.getElementById('dialog-body').textContent.includes(t))")
 js("document.querySelector('#dialog-body [data-action=service]').click()")
 ck('Actual inspector maintenance preserves chassis and cycle while saving the service event',"(()=>{const t=AL.game.tanks[0],e=t.equipment.find(e=>e.id===testEquipment);return e.durability<=testCondition&&e.durability>testCondition-.01&&e.reliability.maintenance>99.99&&JSON.stringify([t.bacteria,t.bacteria2])===JSON.stringify(testBacteria)&&AL.game.equipmentReliability.events.at(-1).kind==='maintenance'})()")
 js("const e=AL.game.tanks[0].equipment.find(e=>e.type==='heater');AL.InventoryUI.inspect({id:e.id})")
 ck('Separate Replace Part and individual thermostat are available in installed inspection',"!!document.querySelector('#dialog-body [data-economy=parts]')&&!!document.querySelector('[data-form=equipmentThermostat]')")
 js("const e=AL.game.tanks[0].equipment.find(e=>e.type==='filter');e.reliability.parts.impeller=40;e.reliability.state='repair-required';e.reliability.failurePart='impeller';AL.EconomyUI.parts(e.id);document.querySelector('#dialog-body [data-economy=replace]').click();AL.UI.close();AL.Shell.open('journal','history');window.eventCount=AL.game.equipmentReliability.events.length;AL.Shell.render()")
 ck('Tank History keeps actual maintenance and part replacement without creating new records',"document.getElementById('primary-content').textContent.includes('Equipment maintenance & failures')&&document.getElementById('primary-content').textContent.includes('Replaced impeller')&&AL.game.equipmentReliability.events.length===eventCount")
 js("AL.Shell.open('equipment','care')")
 ck('Removed standalone temperature/readiness panels stay removed',"!document.querySelector('#primary-content #heater-diagnostics,#primary-content #overnight-readiness')")
 for w,h in [(1920,1080),(1600,900),(1366,768),(390,844)]:
  c.call('Emulation.setDeviceMetricsOverride',{'width':w,'height':h,'deviceScaleFactor':1,'mobile':False});js("AL.InventoryUI.inspect({type:'heater'})")
  ck(str(w)+'x'+str(h)+': equipment inspector has a visible heading and no horizontal overflow',"document.documentElement.scrollWidth<=innerWidth&&document.getElementById('dialog-body').scrollWidth<=document.getElementById('dialog-body').clientWidth&&document.querySelector('#dialog-body h2').getBoundingClientRect().top>=document.getElementById('dialog').getBoundingClientRect().top")
  (out/f'{name}-inspector-{w}.png').write_bytes(base64.b64decode(c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
 errors=[e for e in c.events if e.get('method')=='Runtime.exceptionThrown'];checks.append({'name':'No uncaught browser errors','pass':not errors,'errors':errors})
 result={'entry':entry.relative_to(root).as_posix(),'coldLoadSeconds':round(load_seconds,3),'checks':checks,'distributions':cohorts['distributions'],'offline':matrix,'passed':sum(x['pass'] for x in checks),'failed':sum(not x['pass'] for x in checks)}
 (out/f'{name}-results.json').write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps({'passed':result['passed'],'failed':result['failed'],'failures':[x for x in checks if not x['pass']][:20],'distributions':cohorts['distributions']},indent=2),flush=True)
 return int(result['failed']>0)
