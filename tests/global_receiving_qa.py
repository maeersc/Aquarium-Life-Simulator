import json,time,base64
def run(c,root,name):
 out=root/'tests/global-receiving-evidence';out.mkdir(exist_ok=True)
 c.call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':900,'deviceScaleFactor':1,'mobile':False});c.navigate(root/'index.html')
 for _ in range(200):
  if c.evaluate('!!window.AL?.game&&!!AL.DiveReceiving'):break
  time.sleep(.05)
 c.evaluate('localStorage.clear();AL.Startup.finish();AL.game.settings.speed=0')
 old=c.evaluate((root/'tests/diving_checks.js').read_text(encoding='utf8'))
 c.evaluate((root/'tests/mystery_diving_checks.js').read_text(encoding='utf8'))
 report=c.evaluate((root/'tests/global_receiving_checks.js').read_text(encoding='utf8'))
 report['legacyChecks']=old
 (out/f'{name}-model-results.json').write_text(json.dumps(report,indent=2),encoding='utf8')
 print(json.dumps({'browser':name,'passed':report['passed'],'failed':report['failed'],'failures':[x for x in report['checks'] if not x['pass']],'legacyFailures':[x for x in old if not x['pass']]}),flush=True)
 checks=report['checks']
 def js(x):return c.evaluate('(()=>{'+x+'})()')
 def ck(n,x):
  try:checks.append({'name':n,'pass':bool(c.evaluate(x))})
  except Exception as e:checks.append({'name':n,'pass':False,'error':str(e)})
 def shot(n):(out/f'{name}-{n}.png').write_bytes(base64.b64decode(c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
 for row in report['coverage']:
  id,region,mode=row['id'],row['region'],row['mode']
  js(f"if(AL.DivingUI.ownsDialog)AL.DivingUI.requestDismiss();AL.game=globalReturn('{id}','{region}','{mode}');AL.game.settings.speed=0;const o=AL.game.diving.history[0].objects.find(o=>o.species==='{id}');o.recovery.roll=0;o.recovery.conditionRoll=85;const extra=AL.Core.tank(AL.game,'fresh',300,'Protected freshwater');AL.game.tanks.push(extra);AL.UI.render();AL.DivingUI.open()")
  ck(id+' '+mode+': results list owned saltwater and disabled freshwater destination',"document.querySelector('[data-mystery-receiver]').options.length===3&&document.querySelector('[data-mystery-receiver]').options[2].disabled&&document.querySelector('[data-mystery-receiver]').options[2].textContent.includes('Freshwater')")
  js("const select=document.querySelector('[data-mystery-receiver]');select.value=AL.game.tanks[0].id;select.dispatchEvent(new Event('change',{bubbles:true}));select.blur()")
  if row['kind']=='coral':
   js("document.querySelector('[data-dive-action=recover]').click()")
   ck(id+': coral requires a separate explicit mount choice',"AL.game.tanks[0].flora.length===0&&AL.DiveMystery.pending(AL.game).length===1&&document.querySelector('[data-dive-mount]').options.length>1")
   js("const m=document.querySelector('[data-dive-mount]');m.selectedIndex=1;m.dispatchEvent(new Event('change',{bubbles:true}));m.blur();AL.DivingUI.update()")
   ck(id+': chosen coral mount survives live compatibility refresh',"document.querySelector('[data-dive-mount]').value!==''")
  if row['kind']!='fish':
   js("document.querySelector('[data-receiving-panel]').scrollIntoView({block:'start'})")
   shot(id+'-receiving')
  js("document.querySelector('[data-dive-action=recover]').click()")
  ck(id+' '+mode+': actual receiving control grants one correct owned host and clears pending',f"AL.game.diving.history[0].objects.find(o=>o.species==='{id}').recovery.status==='received'&&AL.DiveMystery.pending(AL.game).length===0&&AL.game.tanks.flatMap(t=>[...t.fish,...t.flora,...(t.invertebrates||[])]).length===1&&!document.querySelector('[data-mystery-receiver]')")
 # Verify the pre-capture non-fish receiving plan also lists every tank.
 js("AL.DivingUI.requestDismiss();AL.game=diveFind('pavona-cactus','fiji','reef');AL.game=AL.Core.act(AL.game,'buyRack',{glass:'back'});const o=AL.game.diving.active.objects.find(o=>o.species==='pavona-cactus');AL.game=diveRoute(AL.game,o.x,o.y,1);AL.game.tanks.push(AL.Core.tank(AL.game,'fresh',300,'Protected freshwater'));AL.UI.render();AL.DivingUI.open();window.coralCell={x:o.x,y:o.y}")
 point=c.evaluate("(()=>{const c=document.getElementById('dive-map');c.scrollIntoView({block:'center'});const r=c.getBoundingClientRect();return {x:r.left+(coralCell.x+.5)*r.width/11,y:r.top+(coralCell.y+.5)*r.height/7}})()")
 for typ in ['mousePressed','mouseReleased']:c.call('Input.dispatchMouseEvent',{'type':typ,'x':point['x'],'y':point['y'],'button':'left','clickCount':1})
 ck('Coral pre-capture receiving plan exposes all aquariums including disabled rejected tanks',"!!document.querySelector('#dive-receiving')&&[...document.querySelector('#dive-receiving').options].some(o=>o.disabled&&o.textContent.includes('Protected freshwater'))&&document.querySelectorAll('.dive-object [data-receiving-tank]').length===2")
 shot('coral-capture-plan')
 js("AL.game=AL.Core.act(AL.game,'diveAbandon',{confirmed:true});AL.DivingUI.requestDismiss();AL.game=globalReturn('pavona-cactus','fiji','reef');AL.UI.render();AL.DivingUI.open();const s=document.querySelector('[data-mystery-receiver]');s.value=AL.game.tanks[0].id;s.dispatchEvent(new Event('change',{bubbles:true}));s.blur();document.querySelector('[data-receiving-panel]').scrollIntoView({block:'start'})")
 for w,h in [(1920,1080),(1600,900),(1366,768),(390,844)]:
  c.call('Emulation.setDeviceMetricsOverride',{'width':w,'height':h,'deviceScaleFactor':1,'mobile':False})
  ck(f'{w}x{h}: universal coral receiving UI fits without page overflow',"document.documentElement.scrollWidth<=innerWidth&&document.getElementById('dialog').scrollWidth<=document.getElementById('dialog').clientWidth")
  shot('coral-'+str(w))
 js("AL.UI.save();AL.DivingUI.requestDismiss();AL.game.settings.speed=0;AL.UI.save()")
 c.navigate(root/'index.html')
 for _ in range(200):
  if c.evaluate('!!window.AL?.game'):break
  time.sleep(.05)
 ck('Actual browser reload preserves a single pending coral and its recorded deadline',"AL.DiveMystery.pending(AL.game).length===1&&AL.game.diving.history[0].objects.some(o=>o.species==='pavona-cactus'&&o.recovery.status==='pending')&&AL.game.tanks[0].flora.length===0")
 errors=[e for e in c.events if e.get('method')=='Runtime.exceptionThrown']
 network=[e for e in c.events if e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('http:','https:'))]
 checks.extend([{'name':'No uncaught JavaScript exceptions','pass':not errors,'errors':errors},{'name':'All resources and saves remain fully offline/local','pass':not network}])
 checks.extend({'name':'Legacy regression: '+x['name'],'pass':x['pass'],**({'error':x['error']} if 'error' in x else {})} for x in old)
 report.update(passed=sum(x['pass'] for x in checks),failed=sum(not x['pass'] for x in checks))
 (out/f'{name}-results.json').write_text(json.dumps(report,indent=2),encoding='utf8')
 print(json.dumps({'browser':name,'passed':report['passed'],'failed':report['failed'],'failures':[x for x in checks if not x['pass']]}),flush=True)
 return int(report['failed']>0)
