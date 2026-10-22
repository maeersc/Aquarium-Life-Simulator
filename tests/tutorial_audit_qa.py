"""Follow actual highlights with trusted pointer/key input in disposable saves."""
import base64,json,time,sys,traceback

def run(c,root,name):
 out=root/'tests/tutorial-audit-evidence';out.mkdir(exist_ok=True)
 entry=root/('DIST/index.html' if '--dist' in sys.argv else 'index.html')
 c.sock.settimeout(300);checks=[];trace=[];fixtures={};timing={}
 clear=c.call('Page.addScriptToEvaluateOnNewDocument',{'source':'localStorage.clear();'})['identifier']
 c.call('Network.emulateNetworkConditions',{'offline':True,'latency':0,'downloadThroughput':0,'uploadThroughput':0})
 def js(s):return c.evaluate('(()=>{'+s+'})()')
 def ck(label,expr):
  try:checks.append({'name':label,'pass':bool(c.evaluate('!!('+expr+')'))})
  except Exception as e:checks.append({'name':label,'pass':False,'error':str(e)})
 def wait(expr,seconds=30):
  until=time.monotonic()+seconds
  while time.monotonic()<until:
   if c.evaluate(expr):return
   time.sleep(.08)
  raise RuntimeError('Timed out: '+expr)
 def key(value):
  for kind in ['keyDown','keyUp']:c.call('Input.dispatchKeyEvent',{'type':kind,'key':value,'code':value})
 def click(selector=None):
  r=js("const n="+('document.querySelector('+json.dumps(selector)+')' if selector else 'AL.TutorialUI.target')+";if(!n)throw Error('No target');n.scrollIntoView({block:'nearest'});AL.TutorialUI.position();const r=n.getBoundingClientRect();for(const a of [.5,.15,.85])for(const b of [.5,.15,.85]){const x=r.left+r.width*a,y=r.top+r.height*b;if(n.contains(document.elementFromPoint(x,y)))return {x,y}}throw Error('Target covered or inert: '+n.outerHTML.slice(0,140))")
  for typ in ['mousePressed','mouseReleased']:c.call('Input.dispatchMouseEvent',{'type':typ,**r,'button':'left','clickCount':1})
 def snapshot():return js("AL.TutorialUI.update();const n=AL.TutorialUI.target,r=AL.Tutorial.state(AL.game);return {step:r.current,instruction:document.querySelector('#tutorial-tooltip p')?.textContent,route:AL.TutorialUI.resolve().key,target:n?{id:n.id,tag:n.tagName,name:n.name,text:n.textContent?.slice(0,100),html:n.outerHTML.slice(0,400),disabled:!!n.disabled,stat:n.dataset.waterStat}:null,completed:Object.keys(r.completed),shell:AL.Shell.active,store:AL.Store.opened,status:r.status}")
 def shot(label):(out/(name+'-'+label+'.png')).write_bytes(base64.b64decode(c.call('Page.captureScreenshot',{'format':'png'})['data']))
 def restore(data):js('AL.UI.close();AL.Shell.close();AL.Store.close();AL.game=AL.Save.parse('+json.dumps(json.dumps(data))+');AL.UI.render();AL.TutorialUI.update()')
 def perform(row):
  n=row['target']
  if not n or n['disabled']:raise RuntimeError('Unusable target: '+json.dumps(row))
  if n['tag']=='INPUT':
   js('AL.TutorialUI.target.focus();AL.TutorialUI.target.select()');c.call('Input.insertText',{'text':'2' if n['name']=='depth' else '25' if n['name']=='temperature' else '1' if n['name']=='count' else ''});key('Tab')
  elif n['tag']=='SELECT':
   if n['id']=='window-switch':value=next(v for k,v in {'Aquarium Store':'store','Aquariums':'aquariums','Tank Care':'equipment','Field Journal':'journal'}.items() if k in row['instruction'])
   elif n['id'] in ['equipment-filter','inventory-category','care-category']:value='all'
   elif n['name']=='type':value=c.evaluate('AL.Data.species[AL.Tutorial.resident(AL.game).species].diet.find(id=>AL.game.inventory[id]>0)')
   else:value=c.evaluate('AL.Tutorial.state(AL.game).tankId')
   i=js('const n=AL.TutorialUI.target;n.focus();return [...n.options].findIndex(o=>o.value==='+json.dumps(value)+')')
   if i<0:raise RuntimeError('Required dropdown option missing')
   click();key('Home')
   for _ in range(i):key('ArrowDown')
   key('Enter');time.sleep(.08)
  elif c.evaluate('!!AL.UI.placing'):js("document.getElementById('aquarium').focus()");key('Enter')
  else:click()
 def follow(label,limit=120,until=None,collect=False):
  for i in range(limit):
   time.sleep(.1);row=snapshot();row.update({'walkthrough':label,'index':i});trace.append(row)
   if row['status']=='completed' or until and c.evaluate(until):return
   if collect:
    phase='preparation' if row['step']=='substrate' and row['target']['name']=='depth' else 'installation' if row['target']['id']=='inventory-confirm' and row['step']=='filter' else 'cycling' if row['step']=='cycle' and c.evaluate('AL.Tutorial.tank(AL.game).cycleActive') else 'purchasing' if row['step']=='details' and not c.evaluate("document.getElementById('dialog').open") else 'receiving' if row['step']=='stocking' else None
    if phase and phase not in fixtures:fixtures[phase]=c.evaluate('JSON.parse(JSON.stringify(AL.game))')
   if row['step']=='cycle' and row['target'].get('stat')=='ammonia' and c.evaluate('AL.Tutorial.tank(AL.game).cycleActive'):
    start=time.monotonic();timing['cycleStartGame']=c.evaluate('AL.game.time');click('[data-speed="20"]');wait('AL.Preparation.state(AL.Tutorial.tank(AL.game)).cycled',150);timing['cycleWallSeconds']=time.monotonic()-start;timing['cycleEndGame']=c.evaluate('AL.game.time');click('[data-speed="1"]');continue
   if row['step']=='appetite' and row['target']['id']=='aquarium':wait("AL.Tutorial.state(AL.game).current!=='appetite'",45);continue
   recent=[r for r in trace if r['walkthrough']==label][-8:]
   if len(recent)==8 and all((r['step'],r['route'],r['completed'])==(row['step'],row['route'],row['completed']) for r in recent):raise RuntimeError('Unresolved route repeated: '+row['step']+'/'+row['route'])
   perform(row)
  raise RuntimeError('Walkthrough did not reach its required result: '+label)
 try:
  c.navigate(entry,timeout=60);wait('!!window.AL?.TutorialUI&&!!AL.renderer')
  c.call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':900,'deviceScaleFactor':1,'mobile':False})
  click('[data-startup=new]');wait("!!document.querySelector('.welcome-routes [data-action=start][data-args*=marine]')");click('.welcome-routes [data-action=start][data-args*=marine]');wait("!!AL.Tutorial.state(AL.game)?.version&&!AL.Startup.pending")
  c.call('Page.removeScriptToEvaluateOnNewDocument',{'identifier':clear})
  if '--tutorial-recovery' in sys.argv:
   saved=json.loads((out/'walkthrough-fixtures.json').read_text());fixtures=saved['fixtures'];completed=saved['completed'];restore(completed)
  else:
   ck('A: real new player has the standard starting balance and dry tank',"AL.game.credits===5250&&AL.game.credits===AL.Core.newGame('marine',127563).credits&&AL.Tutorial.tank(AL.game).emptyDry")
   follow('A-new-player',collect=True)
   ck('A: actual highlighted walkthrough completed all22 milestones',"AL.Tutorial.state(AL.game).status==='completed'&&Object.keys(AL.Tutorial.state(AL.game).completed).length===22")
   ck('A: one owned fish actually ate a manual portion',"AL.Tutorial.tank(AL.game).fish.length===1&&AL.Tutorial.resident(AL.game).careObservation.lastFed>=AL.Tutorial.state(AL.game).signals.feed.time")
   ck('A: devices are installed exclusively and absent from Inventory',"AL.Tutorial.tank(AL.game).equipment.length===3&&!AL.game.ownedEquipment.length")
   ck('A: cycle used real time and the unchanged biological clock',json.dumps(timing['cycleWallSeconds']>=70 and timing['cycleEndGame']-timing['cycleStartGame']>=2100)+"&&AL.Config.cycleHours===36&&AL.Config.minutesPerSecond*1200===1440")
   ck('C: five interrupted stages were captured from real gameplay',json.dumps(set(fixtures)=={'preparation','installation','cycling','purchasing','receiving'}))
   ck('A: initial setup navigation did not auto-fill or prepare the tank',json.dumps(fixtures['preparation']['tanks'][0]['emptyDry'] and not fixtures['preparation']['tanks'][0]['prepared']));completed=c.evaluate('JSON.parse(JSON.stringify(AL.game))');shot('completed')
   model=c.evaluate((root/'tests/tutorial_audit_checks.js').read_text(encoding='utf-8'));checks.extend(model['checks'])
   (out/'walkthrough-fixtures.json').write_text(json.dumps({'fixtures':fixtures,'completed':completed}),encoding='utf-8')
  import tutorial_audit_extra
  tutorial_audit_extra.run(c,root,name,entry,checks,fixtures,completed,js,ck,wait,click,snapshot,follow,restore,shot)
  ck('No uncaught browser errors',json.dumps(not any(e.get('method')=='Runtime.exceptionThrown' for e in c.events)))
  ck('No external gameplay or save requests',json.dumps(not any(e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('http:','https:')) for e in c.events)))
 except Exception as e:
  checks.append({'name':'Complete interactive audit A-F','pass':False,'error':str(e),'traceback':traceback.format_exc()})
  try:shot('failure')
  except Exception:pass
 result={'entry':entry.relative_to(root).as_posix(),'browser':name,'passed':sum(r['pass'] for r in checks),'failed':sum(not r['pass'] for r in checks),'checks':checks,'walkthroughTrace':trace,'realCycleTiming':timing,'interruptionFixtures':list(fixtures),'graph':c.evaluate('AL.Tutorial.steps'),'diagnostic':js("return {state:AL.Tutorial.state(AL.game),target:AL.TutorialUI.target?.outerHTML,tooltip:document.getElementById('tutorial-tooltip')?.textContent}")}
 (out/(name+('-recovery-results.json' if '--tutorial-recovery' in sys.argv else '-results.json'))).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'passed':result['passed'],'failed':result['failed'],'cycle':timing,'failures':[r for r in checks if not r['pass']]},indent=2),flush=True)
 return int(result['failed']>0)
