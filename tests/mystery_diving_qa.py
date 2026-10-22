import base64,json,time
def run(c,root,name):
 out=root/'tests/mystery-diving-evidence';out.mkdir(exist_ok=True)
 c.call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':900,'deviceScaleFactor':1,'mobile':False})
 c.navigate(root/'index.html')
 for _ in range(200):
  if c.evaluate('!!window.AL?.game&&!!AL.DiveMystery&&AL.DivingArt.loaded===9'):break
  time.sleep(.05)
 else:
  print(json.dumps([e for e in c.events if e.get('method')=='Runtime.exceptionThrown']));return 1
 c.evaluate('localStorage.clear();AL.Startup.finish();AL.game.settings.speed=0')
 c.evaluate((root/'tests/diving_checks.js').read_text(encoding='utf8'))
 report=c.evaluate((root/'tests/mystery_diving_checks.js').read_text(encoding='utf8'))
 (out/f'{name}-model-results.json').write_text(json.dumps(report,indent=2),encoding='utf8')
 print(json.dumps({'browser':name,'passed':report['passed'],'failed':report['failed'],'failures':[r for r in report['checks'] if not r['pass']]}),flush=True)
 checks=report['checks']
 def js(s):return c.evaluate('(()=>{'+s+'})()')
 def ck(label,expr):
  try:checks.append({'name':label,'pass':bool(c.evaluate(expr))})
  except Exception as e:checks.append({'name':label,'pass':False,'error':str(e)})
 def shot(label):
  (out/f'{name}-{label}.png').write_bytes(base64.b64decode(c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
 def key(k):
  c.call('Input.dispatchKeyEvent',{'type':'keyDown','key':k})
  c.call('Input.dispatchKeyEvent',{'type':'keyUp','key':k})
 def click_cell(x,y,button='left'):
  p=c.evaluate(f"(()=>{{const r=document.getElementById('dive-map').getBoundingClientRect();return {{x:r.left+({x}+.5)*r.width/11,y:r.top+({y}+.5)*r.height/7}}}})()")
  for t in ['mousePressed','mouseReleased']:c.call('Input.dispatchMouseEvent',{'type':t,'x':p['x'],'y':p['y'],'button':button,'clickCount':1})
 js("AL.game=diveFixture(17);AL.game.settings.speed=0;AL.UI.render();AL.DivingUI.open()")
 ck('Planner does not expose any mystery fish names, scientific names or assigned rarity',"!['Chalk Bass','Spotted Boxfish','Forcipiger','Exquisite','Yellow Longnose','Cirrhilabrus'].some(n=>document.getElementById('dialog-body').textContent.toLowerCase().includes(n.toLowerCase()))")
 js("document.getElementById('dive-region').value='hawaii';document.getElementById('dive-region').dispatchEvent(new Event('change'))")
 ck('UI blocks observation-only destination clearly',"document.querySelector('[data-dive-action=prepare-launch]').disabled&&document.getElementById('dialog-body').textContent.includes('observation-only')")
 js("document.getElementById('dive-region').value='caribbean';document.getElementById('dive-region').dispatchEvent(new Event('change'));document.querySelector('[data-dive-action=prepare-launch]').click();document.querySelector('[data-dive-action=confirm-launch]').click()")
 click_cell(4,1)
 ck('Far click selects generic question-mark fish without exposing species or permitting capture',"document.querySelector('[data-mystery-preview]')&&document.querySelector('[data-dive-action=collect]').disabled&&!document.getElementById('dialog-body').textContent.toLowerCase().includes('chalk')&&AL.game.diving.active.inventory.length===0")
 key('d');key('d')
 click_cell(4,1,'right')
 ck('Right click cannot capture a fish',"AL.game.diving.active.inventory.length===0")
 shot('hidden-encounter')
 click_cell(4,1)
 ck('Actual nearby left click immediately captures once, with zero oxygen cost and concealed inventory',"AL.game.diving.active.inventory.length===1&&AL.game.diving.active.oxygen===90&&document.querySelector('.dive-inventory').textContent.includes('Unknown Fish')&&!document.getElementById('dialog-body').textContent.toLowerCase().includes('chalk')&&!AL.game.tanks[0].fish.length")
 click_cell(4,1)
 ck('Repeated pointer click cannot capture the same fish twice',"AL.game.diving.active.inventory.length===1&&AL.game.diving.active.oxygen===90")
 js("AL.UI.save();window.mysterySavedIdentity=AL.game.diving.active.objects[8].species")
 c.navigate(root/'index.html')
 for _ in range(200):
  if c.evaluate('!!window.AL?.game'):break
  time.sleep(.05)
 ck('Actual local save reload retains captured mystery, oxygen and single charge',"AL.game.diving.active?.inventory.length===1&&AL.game.diving.active.oxygen===90&&AL.game.diving.active.objects[8].species==='chalk-bass'&&AL.game.credits===99000")
 js("AL.Startup.finish();AL.DivingUI.open()")
 ck('Reloaded temporary inventory remains concealed',"document.querySelector('.dive-inventory').textContent.includes('Unknown Fish')&&!document.getElementById('dialog-body').textContent.toLowerCase().includes('chalk')")
 key('a');key('a')
 time.sleep(.8)
 ck('Boat return reveals actual name, science, rarity, original art, origin, value and explicit receiver',"!AL.game.diving.active&&document.querySelector('[data-mystery-reveal]')?.dataset.mysteryReveal==='chalk-bass'&&['Chalk','Serranus tortugarum','Common','Caribbean','Condition:','Current estimated asset value:','Destination:'].every(t=>document.getElementById('dialog-body').textContent.includes(t))&&document.querySelector('[data-mystery-receiver]')&&!AL.game.tanks[0].fish.length")
 for w,h in [(1920,1080),(1600,900),(1366,768),(390,844)]:
  c.call('Emulation.setDeviceMetricsOverride',{'width':w,'height':h,'deviceScaleFactor':1,'mobile':False})
  ck(f'{w}x{h}: reveal fits viewport without horizontal overflow',"document.documentElement.scrollWidth<=innerWidth&&document.getElementById('dialog').scrollWidth<=document.getElementById('dialog').clientWidth")
  shot('reveal-'+str(w))
 c.call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':900,'deviceScaleFactor':1,'mobile':False})
 js("AL.game.diving.history[0].objects[0].recovery.roll=0;AL.game.diving.history[0].objects[0].recovery.conditionRoll=85;document.querySelector('[data-dive-action=recover]').click()")
 ck('Receive button requires an explicit destination',"AL.game.tanks[0].fish.length===0&&AL.game.diving.history[0].objects[0].recovery.status==='pending'")
 js("document.querySelector('[data-mystery-receiver]').value=AL.game.tanks[0].id;document.querySelector('[data-dive-action=recover]').click()")
 ck('Actual receive control grants exactly one fish and displays its real destination and condition',"AL.game.tanks[0].fish.length===1&&document.getElementById('dialog-body').textContent.includes('Alive, healthy')&&document.getElementById('dialog-body').textContent.includes(AL.game.tanks[0].name)&&!document.querySelector('[data-mystery-receiver]')")
 shot('received')
 js("window.mysteryClock=AL.game.time;AL.game.settings.speed=0")
 time.sleep(5.2)
 ck('Results keep the aquarium, hunger and equipment on the shared 1x clock',"AL.game.time>=mysteryClock+5&&AL.game.tanks[0].fish[0].age>0&&AL.game.tanks[0].equipment[0].durability<100")
 js("AL.DivingUI.requestDismiss();AL.game.settings.speed=0;AL.UI.save()")
 c.navigate(root/'index.html')
 for _ in range(200):
  if c.evaluate('!!window.AL?.game'):break
  time.sleep(.05)
 ck('A second actual login preserves one received animal and one recovery receipt',"AL.game.tanks[0].fish.length===1&&AL.game.diving.history[0].objects[0].recovery.status==='received'")
 js("AL.Startup.finish();AL.game.settings.speed=0")
 c.evaluate((root/'tests/diving_checks.js').read_text(encoding='utf8'))
 c.evaluate((root/'tests/mystery_diving_checks.js').read_text(encoding='utf8'))
 js("AL.game=mysteryReceive(85,.9999);const o=AL.game.diving.history[0].objects[0];AL.UI.dialog(AL.MortalityUI.detail(AL.Mortality.records(AL.game).find(e=>e.id===o.deathRecordId)))")
 ck('Transport death report explicitly preserves unknown physiology and chemistry',"document.getElementById('dialog-body').textContent.includes('physiological cause unknown')&&document.getElementById('dialog-body').textContent.includes('No transport water')&&!!document.querySelector('[data-mortality-export]')")
 shot('transport-loss')
 downloads=out/(name+'-downloads')/str(time.time_ns());downloads.mkdir(parents=True,exist_ok=True)
 c.call('Browser.setDownloadBehavior',{'behavior':'allow','downloadPath':str(downloads)})
 js("document.querySelector('[data-mortality-export]').click()")
 for _ in range(100):
  if (downloads/'LIVESTOCK_DEATH_REPORT.json').exists():break
  time.sleep(.05)
 try:
  export=json.loads((downloads/'LIVESTOCK_DEATH_REPORT.json').read_text(encoding='utf8'))
  checks.append({'name':'Real local JSON download retains transport evidence and explicit unknown chemistry','pass':export['record']['context']=='diving-transport' and export['record']['water']=={} and export['record']['hpBefore'] is None})
 except Exception as e:checks.append({'name':'Real local transport mortality export','pass':False,'error':str(e)})
 errors=[e for e in c.events if e.get('method')=='Runtime.exceptionThrown']
 requests=[e['params']['request']['url'] for e in c.events if e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('http:','https:'))]
 checks.extend([{'name':'No uncaught browser JavaScript exceptions','pass':not errors,'errors':errors},{'name':'No HTTP/HTTPS gameplay requests; saves and art stay local','pass':not requests}])
 report.update(passed=sum(r['pass'] for r in checks),failed=sum(not r['pass'] for r in checks))
 (out/f'{name}-results.json').write_text(json.dumps(report,indent=2),encoding='utf8')
 print(json.dumps({'browser':name,'passed':report['passed'],'failed':report['failed'],'failures':[r for r in checks if not r['pass']]}),flush=True)
 return int(report['failed']>0)
