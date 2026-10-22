import json,time,base64
def run(c,root,name):
 out=root/'tests/receiving-evidence';out.mkdir(exist_ok=True)
 c.call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':900,'deviceScaleFactor':1,'mobile':False})
 c.navigate(root/'index.html')
 for _ in range(200):
  if c.evaluate('!!window.AL?.game&&!!AL.DiveReceiving'):break
  time.sleep(.05)
 c.evaluate('localStorage.clear();AL.Startup.finish();AL.game.settings.speed=0')
 c.evaluate((root/'tests/diving_checks.js').read_text(encoding='utf8'))
 c.evaluate((root/'tests/mystery_diving_checks.js').read_text(encoding='utf8'))
 report=c.evaluate((root/'tests/receiving_checks.js').read_text(encoding='utf8'))
 (out/f'{name}-model-results.json').write_text(json.dumps(report,indent=2),encoding='utf8')
 print(json.dumps({'browser':name,'modelPassed':report['passed'],'modelFailed':report['failed'],'failures':[x for x in report['checks'] if not x['pass']]}),flush=True)
 checks=report['checks']
 def js(x):return c.evaluate('(()=>{'+x+'})()')
 def ck(n,x):
  try:checks.append({'name':n,'pass':bool(c.evaluate(x))})
  except Exception as e:checks.append({'name':n,'pass':False,'error':str(e)})
 def shot(n):(out/f'{name}-{n}.png').write_bytes(base64.b64decode(c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
 js("AL.game=receivingFixture();AL.game.settings.speed=0;AL.game.tanks[0].bacteria=.4;const small=AL.Core.tank(AL.game,'marine',75,'Small marine'),fresh=AL.Core.tank(AL.game,'fresh',300,'Legacy freshwater');AL.game.tanks.push(small,fresh);AL.UI.render();AL.DivingUI.open()")
 ck('Dropdown contains every owned tank, including disabled freshwater and incompatible 80gal marine',"document.querySelector('[data-mystery-receiver]').options.length===4&&[...document.querySelector('[data-mystery-receiver]').options].slice(1).every(o=>o.disabled)&&[...document.querySelector('[data-mystery-receiver]').options].some(o=>o.textContent.includes('80 gal')&&o.textContent.includes('27 °C')&&o.textContent.includes('0.4'))&&[...document.querySelector('[data-mystery-receiver]').options].some(o=>o.textContent.includes('Freshwater'))")
 js("document.querySelector('[data-receiving-tank]').open=true;document.querySelector('[data-receiving-tank]').scrollIntoView({block:'start'})")
 ck('Blocked tank has readable actual values, requirements and preparation guidance',"document.querySelector('[data-receiving-tank]').textContent.includes('0.4')&&document.querySelector('[data-receiving-tank]').textContent.includes('0.65')&&document.querySelector('[data-receiving-tank]').textContent.includes('Start or finish biological cycling')&&document.querySelectorAll('[data-receiving-tank] tbody tr').length>30")
 shot('blocked-80gal')
 js("AL.game.tanks[0].bacteria=1;AL.DivingUI.update()")
 ck('Correcting readiness refreshes available destinations without closing or reopening results',"!document.querySelector('[data-mystery-receiver]').options[1].disabled&&!document.querySelector('[data-dive-action=recover]').disabled")
 js("const s=document.querySelector('[data-mystery-receiver]');s.value=AL.game.tanks[0].id;s.dispatchEvent(new Event('change',{bubbles:true}));AL.game.tanks[0].waterParams.temperature=27.000001;s.blur();AL.DivingUI.update()")
 ck('Exact temperature rejection stays visible despite rounded general aquarium readings',"document.querySelector('[data-mystery-receiver]').options[1].disabled&&document.querySelector('[data-receiving-tank]').textContent.includes('27.000001')")
 js("AL.game.tanks[0].waterParams.temperature=27;AL.DivingUI.update();const s=document.querySelector('[data-mystery-receiver]');s.value=AL.game.tanks[0].id;s.dispatchEvent(new Event('change',{bubbles:true}));s.blur();window.receivingHold=AL.game.diving.history[0].objects[0].recovery.item.expiresAt;window.receivingClock=AL.game.time")
 time.sleep(5.2)
 ck('Holding countdown and aquarium clock progress while selection survives automatic refresh',"AL.game.time>=receivingClock+5&&document.querySelector('[data-dive-holding]').textContent.includes('game time')&&document.querySelector('[data-mystery-receiver]').value===AL.game.tanks[0].id&&AL.game.diving.history[0].objects[0].recovery.item.expiresAt===receivingHold")
 for w,h in [(1920,1080),(1600,900),(1366,768),(390,844)]:
  c.call('Emulation.setDeviceMetricsOverride',{'width':w,'height':h,'deviceScaleFactor':1,'mobile':False})
  ck(f'{w}x{h}: receiving and diagnostics have no page/modal overflow',"document.documentElement.scrollWidth<=innerWidth&&document.getElementById('dialog').scrollWidth<=document.getElementById('dialog').clientWidth")
  shot('diagnostics-'+str(w))
 c.call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':900,'deviceScaleFactor':1,'mobile':False})
 js("const o=AL.game.diving.history[0].objects[0];o.recovery.roll=0;o.recovery.conditionRoll=85;document.querySelector('[data-dive-action=recover]').click()")
 ck('Real receive action adds permanent ownership and clears the pending receiving control',"AL.game.tanks[0].fish.length===1&&AL.DiveMystery.pending(AL.game).length===0&&!document.querySelector('[data-mystery-receiver]')&&document.getElementById('dialog-body').textContent.includes('Destination: 80 Gallon Reef')")
 js("AL.UI.save();AL.DivingUI.requestDismiss();AL.game.settings.speed=0;AL.UI.save()")
 c.navigate(root/'index.html')
 for _ in range(200):
  if c.evaluate('!!window.AL?.game'):break
  time.sleep(.05)
 ck('Actual browser save/reload retains one fish, health and settled receiving state',"AL.game.tanks[0].fish.length===1&&AL.game.tanks[0].fish[0].provenance.source==='diving'&&AL.game.tanks[0].fish[0].healthState&&AL.game.diving.history[0].objects[0].recovery.status==='received'&&AL.DiveMystery.pending(AL.game).length===0")
 errors=[e for e in c.events if e.get('method')=='Runtime.exceptionThrown']
 external=[e for e in c.events if e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('http:','https:'))]
 checks.extend([{'name':'No uncaught JavaScript errors','pass':not errors,'errors':errors},{'name':'Fully local offline resources and saves','pass':not external}])
 report.update(passed=sum(x['pass'] for x in checks),failed=sum(not x['pass'] for x in checks))
 (out/f'{name}-results.json').write_text(json.dumps(report,indent=2),encoding='utf8')
 print(json.dumps({'browser':name,'passed':report['passed'],'failed':report['failed'],'failures':[x for x in checks if not x['pass']]}),flush=True)
 return int(report['failed']>0)
