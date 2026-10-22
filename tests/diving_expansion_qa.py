import json,time,base64
def run(c,root,name):
 out=root/'tests/diving-expansion-evidence';out.mkdir(exist_ok=True)
 c.navigate(root/'index.html')
 for _ in range(200):
  if c.evaluate('!!window.AL?.game&&!!AL.DiveExpansion'):break
  time.sleep(.05)
 c.evaluate('localStorage.clear();AL.Startup.finish();AL.game.settings.speed=0')
 legacy=c.evaluate((root/'tests/diving_checks.js').read_text(encoding='utf8'))
 mystery=c.evaluate((root/'tests/mystery_diving_checks.js').read_text(encoding='utf8'))
 global_report=c.evaluate((root/'tests/global_receiving_checks.js').read_text(encoding='utf8'))
 report=c.evaluate((root/'tests/diving_expansion_checks.js').read_text(encoding='utf8'))
 report['legacy']=legacy;report['sharedReceiving']=global_report;report['mysteryRegression']=mystery
 print(json.dumps({"modelPassed":report["passed"],"modelFailed":report["failed"],"failures":[x for x in report["checks"] if not x["pass"]]}),flush=True)
 checks=report['checks']
 def ck(n,expr):
  try:checks.append({'name':n,'pass':bool(c.evaluate(expr))})
  except Exception as e:checks.append({'name':n,'pass':False,'error':str(e)})
 c.evaluate("AL.game=globalReturn('chalk-bass','florida','reef');AL.game.diving.history[0].objects[0].recovery.roll=0;AL.game.diving.history[0].objects[0].recovery.conditionRoll=85;AL.game.tanks[0].waterParams.ammonia=1;AL.UI.render();AL.DivingUI.open()")
 ck('UI: Emergency Sale remains enabled with all tanks unsafe',"!!document.querySelector('[data-dive-action=emergency]:not([disabled])')&&document.querySelector('[data-dive-action=recover]').disabled")
 c.evaluate("document.querySelector('[data-dive-action=emergency]').click()")
 ck('UI: explicit exact-offer confirmation before sale',"!!document.querySelector('[data-dive-action=emergency-confirm]')&&AL.DiveMystery.pending(AL.game).length===1")
 c.evaluate("document.querySelector('[data-dive-action=emergency-confirm]').click()")
 ck('UI: actual confirmed sale records one receipt and clears specimen',"AL.game.diving.history[0].objects[0].recovery.status==='sold'&&AL.game.finance.rows.filter(r=>r.name.startsWith('Emergency Sale')).length===1&&!document.querySelector('[data-dive-action=emergency]')")
 c.evaluate('AL.game.settings.speed=1;window.saleClock=AL.game.time')
 time.sleep(5)
 ck('UI: selling/results window keeps the main aquarium clock running','AL.game.time>saleClock')
 c.evaluate('AL.game.settings.speed=0')
 c.evaluate("AL.DivingUI.requestDismiss();AL.game=eggReturn();AL.UI.render();AL.DivingUI.open()")
 ck('UI: unknown egg is concealed after boat return',"document.getElementById('dialog-body').textContent.includes('Unknown Fish Egg')&&!document.getElementById('dialog-body').textContent.includes('Ocellaris')")
 for w,h in [(1920,1080),(1600,900),(1366,768),(390,844)]:
  c.call('Emulation.setDeviceMetricsOverride',{'width':w,'height':h,'deviceScaleFactor':1,'mobile':False})
  ck(f'UI: {w}x{h} has no horizontal overflow',"document.documentElement.scrollWidth<=innerWidth&&document.getElementById('dialog').scrollWidth<=document.getElementById('dialog').clientWidth")
  (out/f'{name}-egg-{w}.png').write_bytes(base64.b64decode(c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
 c.evaluate('AL.game.settings.speed=0;AL.UI.save()')
 c.navigate(root/'index.html')
 for _ in range(200):
  if c.evaluate('!!window.AL?.game'):break
  time.sleep(.05)
 ck('Actual browser reload retains one unknown egg',"AL.DiveExpansion.pendingEggs(AL.game).length===1&&AL.game.diving.history[0].objects[0].name==='Unknown Fish Egg'")
 # A navigation intentionally discards JavaScript test helpers; reinstall only
 # fixture definitions, without re-running regression assertions or RNG tests.
 c.evaluate((root/'tests/diving_checks.js').read_text(encoding='utf8').split(" test('Two original modes")[0]+' return true;})()')
 c.evaluate('AL.Startup.finish()')
 c.call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':900,'deviceScaleFactor':1,'mobile':False})
 c.evaluate("AL.game=AL.Core.act(diveFixture(),'diveLaunch',{region:'mariana',mode:'deep',confirmed:true});AL.UI.render();AL.DivingUI.open();AL.DivingUI.draw()")
 ck('UI: actual Mariana map shows drone battery rather than a scuba oxygen HUD',"document.getElementById('dive-oxygen').textContent.includes('Drone battery')&&document.getElementById('dialog-body').textContent.includes('Fictional remote drone')")
 (out/f'{name}-mariana.png').write_bytes(base64.b64decode(c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
 c.evaluate("AL.game=AL.Core.act(AL.game,'diveAbandon',{confirmed:true});AL.DivingUI.requestDismiss();AL.game=diveFixture();AL.UI.render();AL.DivingUI.open()")
 for mode in ['reef','deep']:
  c.evaluate(f"document.querySelector('[data-dive-action=mode][data-dive-args*=\"{mode}\"]').click()")
  ck('UI: correct location selector entries for '+mode,"(()=>{const ids=[...document.getElementById('dive-region').options].map(o=>o.value);return "+("['indonesia','philippines','sri-lanka','marshall','maldives','australia','florida'].every(x=>ids.includes(x))&&!ids.includes('mariana')" if mode=='reef' else "ids.includes('mariana')&&!ids.includes('indonesia')")+"})()")
 errors=[e for e in c.events if e.get('method')=='Runtime.exceptionThrown']
 checks.append({'name':'No uncaught JavaScript errors','pass':not errors,'errors':errors})
 checks.append({'name':'All runtime resources remain offline','pass':not [e for e in c.events if e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('https:','http:'))]})
 checks.extend({'name':'Legacy: '+x['name'],**{k:v for k,v in x.items() if k!='name'}} for x in legacy)
 checks.extend({'name':'Shared receiving: '+x['name'],**{k:v for k,v in x.items() if k!='name'}} for x in global_report['checks'])
 checks.extend({'name':'Mystery regression: '+x['name'],**{k:v for k,v in x.items() if k!='name'}} for x in mystery['checks'])
 report.update(passed=sum(x['pass'] for x in checks),failed=sum(not x['pass'] for x in checks))
 (out/f'{name}-results.json').write_text(json.dumps(report,indent=2),encoding='utf8')
 print(json.dumps({'passed':report['passed'],'failed':report['failed'],'failures':[x for x in checks if not x['pass']],'legacyFailures':[x for x in legacy if not x['pass']],'sharedFailures':[x for x in global_report['checks'] if not x['pass']]}),flush=True)
 return int(report['failed']>0)
