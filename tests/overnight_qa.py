"""Reproducible marine absence matrix, before and after the mortality repair."""
import json,time,sys,base64
def run(c,root,name):
 c.sock.settimeout(180)
 out=root/'tests/overnight-evidence';out.mkdir(exist_ok=True)
 c.navigate(root/'index.html')
 for _ in range(300):
  if c.evaluate('!!window.AL?.game&&!!AL.Update31UI'):break
  time.sleep(.04)
 c.evaluate('AL.Startup.finish();AL.UI.close();AL.Store.close();AL.Shell.close();AL.game.settings.speed=0')
 baseline='--overnight-before' in sys.argv
 if baseline:
  c.evaluate("AL.MarineCare=undefined;AL.Mortality=undefined")
  for module in ['invertebrates','livestock-health','simulation','update29','offline']:
   c.evaluate((root/'planning/overnight-repair'/f'{module}-before.js').read_text(encoding='utf-8'))
 # This runner uses a disposable QA browser profile, never the player's profile.
 c.evaluate("for(let i=localStorage.length-1;i>=0;i--){const k=localStorage.key(i);if(k.startsWith('aquarium-life-mortality-v2:'))localStorage.removeItem(k);}")
 c.evaluate((root/'tests/overnight_probe.js').read_text(encoding='utf-8'))
 scenarios=['healthy-feeder','mixed-feeder','no-feeder','food-shortage','failed-flow','immature-cycle','disease','coral-photosynthetic','coral-feeding','grazers-scavengers','juvenile','multiple']
 durations=[1/3,2,8,12,24]
 rows=[]
 for scenario in scenarios:
  for hours in durations:
   row=c.evaluate(f'overnightRun({json.dumps(scenario)},{hours})');rows.append(row)
  print(scenario+': '+', '.join(str(r['realHours'])+'h '+str(r['offline']['alive'])+'/'+str(r['offline']['total']) for r in rows if r['scenario']==scenario),flush=True)
 supported=['healthy-feeder','mixed-feeder','coral-photosynthetic','coral-feeding','grazers-scavengers','juvenile','multiple']
 healthy_failed=[{'scenario':r['scenario'],'hours':r['realHours']} for r in rows if r['scenario'] in supported and r['offline']['alive']!=r['offline']['total']]
 report={'healthyFailed':healthy_failed,'phase':'before' if baseline else 'after','browser':name,'rows':rows,'equivalencePassed':sum(r['equivalent'] for r in rows),'equivalenceFailed':sum(not r['equivalent'] for r in rows)}
 if not baseline:
  report['logic']=c.evaluate((root/'tests/overnight_checks.js').read_text(encoding='utf-8'))
  print(json.dumps(report['logic'],indent=2),flush=True)
  report['speciesRates']=c.evaluate("[...Object.keys(AL.Data.species).filter(id=>AL.Data.species[id].water==='marine').flatMap(id=>[1,.08].map(growth=>{const f={species:id,growth,hunger:100,healthState:{nutrition:0}},p=AL.MarineCare.profile(f);return {id,stage:growth===1?'adult':'juvenile',hungerPerDay:p.hungerPerHour*24,maxStarvationDamagePerDay:AL.MarineCare.starving(f)*24,foods:p.foods};})),...Object.keys(AL.Data.flora).filter(id=>AL.Data.flora[id].water==='marine').map(id=>{const f={type:id,hunger:100,coralHunger:100,healthState:{nutrition:0}},p=AL.MarineCare.profile(f);return {id,stage:'coral',hungerPerDay:p.hungerPerHour*24,maxStarvationDamagePerDay:p.foods.length?AL.MarineCare.starving(f)*24:0,foods:p.foods};}),...Object.keys(AL.Data.invertebrates).filter(id=>AL.Data.invertebrates[id].water==='marine').map(id=>{const f={invertebrate:id,growth:1,hunger:100,healthState:{nutrition:0}},p=AL.MarineCare.profile(f);return {id,stage:'adult',hungerPerDay:p.hungerPerHour*24,maxStarvationDamagePerDay:AL.MarineCare.starving(f)*24,foods:p.foods};})]")
  ui=[]
  def check(label,expr):
   try:ui.append({'name':label,'pass':bool(c.evaluate(expr))})
   except Exception as error:ui.append({'name':label,'pass':False,'error':str(error)})
  def shot(label):
   data=c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']
   (out/f'{name}-{label}.png').write_bytes(base64.b64decode(data))
  c.call('Emulation.setDeviceMetricsOverride',{'width':1366,'height':900,'deviceScaleFactor':1,'mobile':False})
  c.evaluate("AL.game=overnightFixture('mixed-feeder');AL.Shell.open('equipment','care')")
  check('Equipment care shows actual readiness, equipment and the approved day conversion',"['Overnight Readiness','24 / 36 / 72 game days','Equipment condition:','Automatic feeder: operational'].every(x=>document.getElementById('primary-content').textContent.includes(x))")
  shot('readiness-desktop')
  c.evaluate("AL.Shell.close();AL.game=overnightFixture('food-shortage');AL.game.tanks[0].equipment.find(e=>e.type==='feeder').enabled=false;AL.Shell.open('journal','history')")
  check('Journal warns of disabled feeder and genuinely limited food',"['Overnight Readiness','not automatic feeding','shorter than eight real hours'].every(x=>document.getElementById('primary-content').textContent.includes(x))")
  c.call('Emulation.setDeviceMetricsOverride',{'width':390,'height':900,'deviceScaleFactor':1,'mobile':False})
  check('Readiness fits the mobile viewport',"document.documentElement.scrollWidth<=innerWidth")
  shot('readiness-mobile')
  c.evaluate("AL.Shell.close();AL.game=overnightFixture('food-shortage');window.overnightReport=AL.Offline.sync(AL.game,AL.game.simulationCheckpoint+86400000);AL.Offline.report(overnightReport)")
  check('Welcome Back exposes actual starvation and death-time evidence',"['Welcome Back','Prolonged severe malnutrition','Death-time water:','Hunger','nutrition','Compatible food stock at death (exhausted)','Equipment at death:','Modeled health conditions:','Recent recorded warnings:'].every(x=>document.getElementById('dialog-body').textContent.includes(x))")
  check('Welcome Back retains time conversion and no resurrection',"overnightReport.days===72&&AL.game.tanks[0].fish[0].dead&&AL.game.mortality.events.length===1")
  c.evaluate("document.querySelectorAll('#dialog-body details').forEach(d=>d.open=true)")
  shot('mortality-mobile')
  c.call('Emulation.setDeviceMetricsOverride',{'width':1366,'height':900,'deviceScaleFactor':1,'mobile':False})
  shot('mortality-desktop')
  c.evaluate("AL.UI.close();AL.Shell.open('journal','history')")
  check('History retains the same loss and historical observations',"['Prolonged severe malnutrition','Historical water observations','Livestock Deaths'].every(x=>document.getElementById('primary-content').textContent.includes(x))")
  c.evaluate("AL.Shell.close();AL.game=overnightFixture('mixed-feeder');AL.Offline.sync(AL.game,AL.game.simulationCheckpoint+28800000);AL.UI.save();window.overnightSaved={account:AL.game.accountId,time:AL.game.time,inventory:AL.game.inventory.pellets,events:AL.game.mortality.events.length,earned:AL.game.update29.survival.earned,fish:AL.game.tanks[0].fish.map(f=>({id:f.id,dead:f.dead,hp:f.hp}))}")
  saved=c.evaluate('overnightSaved');c.navigate(root/'index.html')
  for _ in range(300):
   if c.evaluate('!!window.AL?.game&&!!AL.Update31UI'):break
   time.sleep(.04)
  check('Actual browser reload preserves IDs, health, inventory, rewards and completed progression',f"AL.game.accountId==={json.dumps(saved['account'])}&&AL.game.time>={saved['time']}&&AL.game.time<{saved['time']}+10&&AL.game.inventory.pellets==={saved['inventory']}&&AL.game.mortality.events.length==={saved['events']}&&AL.game.update29.survival.earned==={saved['earned']}&&JSON.stringify(AL.game.tanks[0].fish.map(f=>({{id:f.id,dead:f.dead,hp:f.hp}})))==={json.dumps(json.dumps(saved['fish'],separators=(',',':')))}")
  errors=[e for e in c.events if e.get('method')=='Runtime.exceptionThrown']
  network=[e['params']['request']['url'] for e in c.events if e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('http:','https:'))]
  ui.extend([{'name':'No uncaught JavaScript exceptions','pass':not errors,'errors':errors},{'name':'No internet requests during local progression','pass':not network,'requests':network}])
  report['ui']=ui;report['failed']=report['logic']['failed']+sum(not r['pass'] for r in ui)+report['equivalenceFailed']+len(healthy_failed)
  print(json.dumps({'failed':report['failed'],'ui':ui},indent=2),flush=True)
 (out/f'{name}-{"before" if baseline else "after"}.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
 print(json.dumps({'equivalent':report['equivalencePassed'],'diverged':report['equivalenceFailed']}),flush=True)
 return int(not baseline and bool(report['failed']))
