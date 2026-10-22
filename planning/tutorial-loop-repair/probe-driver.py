"""Follow the guide's actual highlighted route, in an isolated browser save."""
import json,time,sys,traceback,base64

def run(c,root,name):
 out=root/'tests/tutorial-audit-evidence';out.mkdir(exist_ok=True)
 entry=root/('DIST/index.html' if '--dist' in sys.argv else 'index.html')
 c.sock.settimeout(300)
 c.call('Page.addScriptToEvaluateOnNewDocument',{'source':'localStorage.clear();'})
 c.call('Network.emulateNetworkConditions',{'offline':True,'latency':0,'downloadThroughput':0,'uploadThroughput':0})
 trace=[];checks=[]
 def js(s):return c.evaluate('(()=>{'+s+'})()')
 def wait(expr,seconds=30):
  until=time.monotonic()+seconds
  while time.monotonic()<until:
   if c.evaluate(expr):return
   time.sleep(.05)
  raise RuntimeError('Timed out: '+expr)
 def click(selector=None):
  r=js("const n="+('document.querySelector('+json.dumps(selector)+')' if selector else 'AL.TutorialUI.target')+";if(!n)throw Error('No click target');n.scrollIntoView({block:'nearest'});const r=n.getBoundingClientRect();for(const a of [.5,.15,.85])for(const b of [.5,.15,.85]){const x=r.left+r.width*a,y=r.top+r.height*b;if(n.contains(document.elementFromPoint(x,y)))return {x,y}}throw Error('Target is covered: '+n.outerHTML.slice(0,120))")
  for typ in ['mousePressed','mouseReleased']:c.call('Input.dispatchMouseEvent',{'type':typ,**r,'button':'left','clickCount':1})
 def snapshot():return js("AL.TutorialUI.update();const n=AL.TutorialUI.target,r=AL.Tutorial.state(AL.game);return {step:r.current,instruction:document.querySelector('#tutorial-tooltip p')?.textContent,target:n?{id:n.id,tag:n.tagName,text:n.textContent?.slice(0,120),html:n.outerHTML.slice(0,500),disabled:n.disabled}:null,completed:Object.keys(r.completed),shell:AL.Shell.active,tab:AL.Shell.subtab,store:AL.Store.opened,category:AL.Store.category,status:r.status}")
 try:
  c.navigate(entry,timeout=60);wait('!!window.AL?.TutorialUI&&!!AL.renderer')
  c.call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':900,'deviceScaleFactor':1,'mobile':False})
  click('[data-startup=new]');wait("!!document.querySelector('.welcome-routes [data-action=start][data-args*=marine]')")
  click('.welcome-routes [data-action=start][data-args*=marine]');wait("!!AL.Tutorial.state(AL.game)?.version&&!AL.Startup.pending")
  for i in range(200):
   time.sleep(.1);row=snapshot();row['index']=i;trace.append(row)
   if row['status']=='completed':break
   if row['step']=='cycle' and c.evaluate('AL.Tutorial.tank(AL.game).cycleActive'):
    js("AL.UI.close();AL.Shell.close();AL.Store.close()");click('[data-speed="20"]');wait("AL.Preparation.state(AL.Tutorial.tank(AL.game)).cycled",150);click('[data-speed="1"]');continue
   if row['target']['tag']=='INPUT':
    js("const n=AL.TutorialUI.target;n.value=n.name==='depth'?'2':n.name==='temperature'?'25':n.name==='count'?'1':'';n.dispatchEvent(new Event('input',{bubbles:true}));n.dispatchEvent(new Event('change',{bubbles:true}));AL.TutorialUI.update()");continue
   if row['target']['tag']=='SELECT':
    if row['target']['id']=='window-switch':
     text=row['instruction'];mapping={'Aquarium Store':'store','Aquariums':'aquariums','Tank Care':'equipment','Field Journal':'journal'}
     value=next((v for k,v in mapping.items() if k in text),None)
     if not value:raise RuntimeError('No switch value: '+text)
     js('const n=AL.TutorialUI.target;n.value='+json.dumps(value)+";n.dispatchEvent(new Event('change',{bubbles:true}))")
    else:js("const n=AL.TutorialUI.target;n.value=n.id==='equipment-filter'?'all':n.id==='inventory-category'?'all':n.closest('[data-form=feed]')?[...n.options].find(o=>AL.Data.species[AL.Tutorial.resident(AL.game).species].diet.includes(o.value)&&AL.game.inventory[o.value]>0).value:AL.Tutorial.state(AL.game).tankId;n.dispatchEvent(new Event('change',{bubbles:true}))")
   else:
    if c.evaluate('!!AL.UI.placing'):
     js("document.getElementById('aquarium').focus()");c.call('Input.dispatchKeyEvent',{'type':'keyDown','key':'Enter','code':'Enter'});c.call('Input.dispatchKeyEvent',{'type':'keyUp','key':'Enter','code':'Enter'})
    else:click()
  checks.append({'name':'Probe completed','pass':True})
 except Exception as e:checks.append({'name':'Probe context','pass':False,'error':str(e),'traceback':traceback.format_exc()})
 diagnostic=js("const n=AL.TutorialUI.target,r=n?.getBoundingClientRect();return {dialogs:[...document.querySelectorAll('dialog[open]')].map(n=>n.id),rect:r?.toJSON(),tip:document.getElementById('tutorial-tooltip').getBoundingClientRect().toJSON(),hit:r?[.15,.5,.85].map(a=>[.15,.5,.85].map(b=>document.elementFromPoint(r.left+r.width*a,r.top+r.height*b)?.outerHTML.slice(0,200))):[],log:AL.Tutorial.state(AL.game).audit.slice(-10)}")
 (out/(name+'-probe.png')).write_bytes(base64.b64decode(c.call('Page.captureScreenshot',{'format':'png'})['data']))
 result={'entry':entry.relative_to(root).as_posix(),'browser':name,'trace':trace,'checks':checks,'diagnostic':diagnostic}
 (out/(name+'-probe.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'trace':[{k:r.get(k) for k in ['index','step','instruction']} for r in trace][-25:],'checks':checks,'diagnostic':diagnostic},indent=2),flush=True)
 return 0
