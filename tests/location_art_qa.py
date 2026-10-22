"""Actual destination picker, launched map, result banner and offline reload QA."""
import base64,json,time

def run(c,root,name):
 out=root/'tests/location-art-evidence';out.mkdir(exist_ok=True)
 c.navigate(root/'index.html')
 for _ in range(300):
  if c.evaluate('!!window.AL?.game&&!!AL.DivingUI&&AL.DivingArt.loaded===AL.DivingArtData.length'):break
  time.sleep(.05)
 c.evaluate('localStorage.clear();AL.Startup.finish();AL.game.settings.speed=0')
 c.evaluate((root/'tests/diving_checks.js').read_text(encoding='utf8').split(" test('Two original modes")[0]+' return true;})()')
 checks=[]
 def ck(n,x):
  try:checks.append({'name':n,'pass':bool(c.evaluate(x))})
  except Exception as e:checks.append({'name':n,'pass':False,'error':str(e)})
 def shot(n):
  (out/f'{name}-{n}.png').write_bytes(base64.b64decode(c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
 ck('All 17 offline art records decode without error','AL.DivingArtData.length===17&&AL.DivingArt.loaded===17&&!AL.DivingArt.errors.length')
 scenes=c.evaluate('Object.entries(AL.DivingData.regions).flatMap(([region,r])=>Object.keys(r.art).map(mode=>({region,mode})))')
 for row in scenes:
  region,mode=row['region'],row['mode'];key=region+'-'+mode
  c.evaluate("if(AL.game.diving.active)AL.game=AL.Core.act(AL.game,'diveAbandon',{confirmed:true});if(AL.DivingUI.opened)AL.DivingUI.requestDismiss();AL.game=diveFixture(471);AL.UI.render();AL.DivingUI.open()")
  c.evaluate("document.querySelector('[data-dive-action=mode][data-dive-args*=\""+mode+"\"]').click()")
  c.evaluate("document.getElementById('dive-region').value="+json.dumps(region)+";document.getElementById('dive-region').dispatchEvent(new Event('change',{bubbles:true}))")
  # Browser image decode may complete after assigning the already-preloaded URL.
  for _ in range(100):
   if c.evaluate("document.querySelector('.dive-scene-preview')?.complete&&document.querySelector('.dive-scene-preview').naturalWidth>0"):break
   time.sleep(.02)
  ck(key+': picker loads this destination image',"(()=>{const im=document.querySelector('.dive-scene-preview');return im?.dataset.diveScene==="+json.dumps(key)+"&&im.complete&&im.naturalWidth>0&&im.src===AL.DivingArt.source("+json.dumps(region)+','+json.dumps(mode)+");})()")
  ck(key+': preview keeps source aspect without stretching',"getComputedStyle(document.querySelector('.dive-scene-preview')).objectFit==='cover'")
  ck(key+': artwork reading does not mutate save state',"(()=>{const b=JSON.stringify(AL.game);for(let i=0;i<4;i++)AL.DivingArt.source("+json.dumps(region)+','+json.dumps(mode)+");return b===JSON.stringify(AL.game);})()")
  if region=='hawaii':
   ck(key+': observation-only launch remains disabled',"document.querySelector('[data-dive-action=prepare-launch]').disabled")
   ck(key+': preserved environment draws directly',"(()=>{const c=document.createElement('canvas');c.width=880;c.height=560;return AL.DivingArt.environment(c.getContext('2d'),'hawaii',"+json.dumps(mode)+",880,560);})()")
   continue
  if mode=='reef':shot(key+'-picker')
  c.evaluate("document.querySelector('[data-dive-action=prepare-launch]').click();document.querySelector('[data-dive-action=confirm-launch]').click();AL.DivingUI.draw()")
  ck(key+': actual launched dive has correct region and unchanged resource cost',"AL.game.diving.active?.region==="+json.dumps(region)+"&&AL.game.diving.active.mode==="+json.dumps(mode)+"&&AL.game.diving.active.oxygen===100&&AL.game.diving.active.steps===0&&AL.game.diving.active.inventory.length===0")
  ck(key+': actual canvas uses registered environment with proportional crop',"(()=>{const before=JSON.stringify(AL.game),fn=AL.DivingArt.environment;let called=false;AL.DivingArt.environment=(ctx,r,m,w,h)=>{called=r==="+json.dumps(region)+"&&m==="+json.dumps(mode)+"&&w===880&&h===560;return fn(ctx,r,m,w,h)};try{AL.DivingUI.draw();return called&&JSON.stringify(AL.game)===before;}finally{AL.DivingArt.environment=fn}})()")
  ck(key+': active expedition save/load retains exact capture and inventory state',"(()=>{const s=AL.Save.parse(JSON.stringify(AL.game));return JSON.stringify(s.diving.active)===JSON.stringify(AL.game.diving.active);})()")
  if region in ['indonesia','philippines','sri-lanka','marshall','maldives','australia','florida','mariana']:
   for w,h in [(1920,1080),(1600,900),(1366,768),(390,844)]:
    c.call('Emulation.setDeviceMetricsOverride',{'width':w,'height':h,'deviceScaleFactor':1,'mobile':False})
    ck(f'{key}: map and dialog fit {w}x{h}',"(()=>{const d=document.getElementById('dialog'),m=document.getElementById('dive-map'),r=m.getBoundingClientRect();return d.scrollWidth<=d.clientWidth+1&&document.documentElement.scrollWidth<=innerWidth&&r.width<=d.clientWidth&&Math.abs(r.width/r.height-880/560)<.015;})()")
    if w in [1600,390]:shot(key+'-map-'+str(w))
   c.call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':900,'deviceScaleFactor':1,'mobile':False})
  if region=='mariana':
   ck('Mariana uses drone battery and no living collection',"AL.game.diving.active.remote&&document.getElementById('dive-oxygen').textContent.includes('Drone battery')&&AL.game.diving.active.objects.every(o=>o.kind==='rock')&&AL.DiveMystery.pool('mariana','deep').length===0")
  c.evaluate("document.querySelector('[data-dive-action=return]').click()")
  for _ in range(100):
   if c.evaluate("document.querySelector('.dive-result-scene')?.complete"):break
   time.sleep(.02)
  ck(key+': actual boat return shows correct results accent',"(()=>{const im=document.querySelector('.dive-result-scene');return !AL.game.diving.active&&im?.complete&&im.naturalWidth>0&&im.dataset.diveResultScene==="+json.dumps(key)+"&&im.src===AL.DivingArt.source("+json.dumps(region)+','+json.dumps(mode)+");})()")
  if region=='mariana':shot('mariana-results')
 ck('No missing or failed image elements remain',"[...document.querySelectorAll('img')].every(im=>im.complete&&im.naturalWidth>0)&&!AL.DivingArt.errors.length")
 ck('Freshwater remains unavailable',"(()=>{try{AL.Core.act(AL.game,'buyTank',{water:'fresh',size:0,name:'Forbidden'});return false;}catch{return true}})()")
 c.evaluate('AL.UI.save();window.artReloadId=AL.game.diving.history[0].id')
 previous=c.evaluate('AL.game.diving.history[0].id')
 c.navigate(root/'index.html')
 for _ in range(300):
  if c.evaluate('!!window.AL?.game&&AL.DivingArt?.loaded===17'):break
  time.sleep(.05)
 ck('Actual offline browser reload retains expedition result and local save',"AL.game.diving.history[0]?.id==="+json.dumps(previous))
 errors=[e for e in c.events if e.get('method')=='Runtime.exceptionThrown']
 checks.append({'name':'No uncaught browser runtime exceptions','pass':not errors,'errors':errors})
 network=[e['params']['request']['url'] for e in c.events if e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('http:','https:'))]
 checks.append({'name':'All artwork and saves work fully offline','pass':not network,'requests':network})
 result={'passed':sum(x['pass'] for x in checks),'failed':sum(not x['pass'] for x in checks),'checks':checks}
 (out/f'{name}-results.json').write_text(json.dumps(result,indent=2),encoding='utf8')
 print(json.dumps({**{k:v for k,v in result.items() if k!='checks'},'failures':[x for x in checks if not x['pass']]}),flush=True)
 return int(result['failed']>0)
