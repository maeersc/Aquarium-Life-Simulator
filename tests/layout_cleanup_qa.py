"""Main-screen acceptance checks in an isolated offline browser profile."""
import base64,json,time

def run(c,root,name):
 out=root/'tests/layout-cleanup-evidence';out.mkdir(exist_ok=True)
 checks=[];sizes={}
 def js(s):return c.evaluate('(()=>{'+s+'})()')
 def ck(label,expr):
  try:checks.append({'name':label,'pass':bool(c.evaluate(expr))})
  except Exception as e:checks.append({'name':label,'pass':False,'error':str(e)})
 def viewport(w,h):
  c.call('Emulation.setDeviceMetricsOverride',{'width':w,'height':h,'deviceScaleFactor':1,'mobile':False});time.sleep(.15)
 def shot(label):
  (out/f'{name}-{label}.png').write_bytes(base64.b64decode(c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
 def boot(path):
  c.navigate(path)
  for _ in range(300):
   if c.evaluate('!!window.AL?.game&&!!AL.renderer'):break
   time.sleep(.05)
  else:raise RuntimeError('Game did not boot')
  js("AL.Startup.finish();AL.UI.close();AL.Store.close();AL.Shell.close();AL.game=AL.Core.newGame('marine',223);AL.game.settings.speed=0;AL.game.update29.tutorial.status='skipped';AL.game.credits=100000;delete AL.game.finance;AL.Finance.initialize(AL.game);AL.game.level=11;AL.game.xp=2000;let t=AL.game.tanks[0];t.prepared=true;t.bacteria=t.bacteria2=1;AL.game=AL.Core.act(AL.game,'buyFish',{species:'clown',count:2});AL.UI.render();AL.renderer.draw(AL.game,0);")
 measure="(()=>{const r=document.getElementById('aquarium').getBoundingClientRect();return {width:r.width,height:r.height,top:r.top,bottom:r.bottom,right:r.right}})()"
 # Archived markup/styles retain the exact previous layout for a controlled comparison.
 boot(root/'tests/layout-cleanup-before.html')
 for w,h in [(1366,768),(1440,900),(1920,1080)]:
  viewport(w,h);sizes[f'{w}x{h}']={'before':c.evaluate(measure)}
 shot('before-desktop')
 boot(root/'index.html')
 for w,h in [(1366,768),(1440,900),(1920,1080),(1024,650),(764,900),(390,844)]:
  viewport(w,h);key=f'{w}x{h}';sizes.setdefault(key,{})['after']=c.evaluate(measure)
  ck(key+': proportional canvas visible without page overflow',"(()=>{const r=document.getElementById('aquarium').getBoundingClientRect();return Math.abs(r.width/r.height-2)<.02&&r.width>150&&r.top>=0&&r.bottom<=innerHeight&&r.right<=innerWidth&&document.documentElement.scrollWidth<=innerWidth&&document.documentElement.scrollHeight<=innerHeight})()")
  ck(key+': selector and new aquarium fit without overlap',"(()=>{const s=document.getElementById('aquarium-selector').getBoundingClientRect(),b=document.getElementById('new-tank').getBoundingClientRect();return s.width>60&&s.right<=b.left&&Math.abs(s.top+s.height/2-b.top-b.height/2)<2&&b.right<=innerWidth})()")
  ck(key+': status, quest and activity panels accessible',"['water-panel','next-panel','log-panel'].every(k=>{let e=document.querySelector('.'+k);return e.getBoundingClientRect().width>0&&!!e.textContent.trim()})")
  if key in ['1366x768','1440x900','1920x1080']:
   checks.append({'name':key+': visible aquarium area increased','pass':sizes[key]['after']['width']*sizes[key]['after']['height']>sizes[key]['before']['width']*sizes[key]['before']['height']})
  shot('main-'+key)
 viewport(1366,768)
 ck('Level numeral centered horizontally and optically in badge',"(()=>{const e=document.getElementById('level'),r=e.getBoundingClientRect(),range=document.createRange();range.selectNodeContents(e);const n=range.getBoundingClientRect();return Math.abs(n.x+n.width/2-r.x-r.width/2)<1&&Math.abs(n.y+n.height/2-(r.y+(r.height-3)/2))<2&&getComputedStyle(e).paddingLeft==='0px'})()")
 ck('Level, Diving and Keeper share the header centerline',"(()=>{const a=['level','ocean-diving'].map(id=>document.getElementById(id).getBoundingClientRect());a.push(document.querySelector('.keeper').getBoundingClientRect());return a.every(r=>Math.abs(r.y+r.height/2-30)<1)})()")
 ck('Three bottom care cards are removed from DOM',"!document.querySelector('.care-actions,#feed-quick,#water-quick,#store-quick')")
 ck('Decorative slogan removed and heading retained',"!document.body.textContent.includes('A LITTLE CARE. A WORLD OF LIFE.')&&document.getElementById('page-title').textContent==='Your aquariums.'")
 ck('Compact named selector beside New aquarium replaces tab row',"!document.getElementById('tank-tabs')&&document.getElementById('aquarium-selector').closest('.aquarium-controls').contains(document.getElementById('new-tank'))&&document.getElementById('aquarium-selector').selectedOptions[0].textContent===AL.Core.selected(AL.game).name")
 js("AL.UI.goto('food')")
 ck('Feeding remains available through Equipment / Tank Care',"!!document.querySelector('#primary-content [data-form=feed]')")
 js("AL.Shell.open('equipment','change')")
 ck('Water change remains available in its menu',"!!document.querySelector('#primary-content [data-action=waterChange]')")
 js("AL.Shell.close();document.getElementById('new-tank').click()")
 ck('New aquarium button opens purchase catalog',"AL.Shell.active==='aquariums'&&AL.Shell.subtab==='new'&&!!document.querySelector('[data-action=configureTank]')")
 js("document.querySelector('[data-action=configureTank]').click()")
 ck('Freshwater stays disabled in tank creation',"document.querySelector('[data-form=buyTank] [name=water] option[value=fresh]').disabled")
 js("document.querySelector('[data-form=buyTank] [name=name]').value='Second reef';document.querySelector('[data-form=buyTank]').requestSubmit();AL.Shell.close()")
 ck('Actual aquarium purchase populates compact selector',"AL.game.tanks.length===2&&document.getElementById('aquarium-selector').options.length===2&&AL.game.tanks.some(t=>t.name==='Second reef')")
 js("window.layoutFirst=AL.game.tanks[0].id;window.layoutSecond=AL.game.tanks[1].id;const e=document.getElementById('aquarium-selector');e.value=layoutFirst;e.dispatchEvent(new Event('change',{bubbles:true}));")
 ck('Selector switches to original aquarium and synchronizes header',"AL.game.selectedTank===layoutFirst&&document.getElementById('tank-name').textContent===AL.game.tanks[0].name")
 js("const e=document.getElementById('aquarium-selector');e.value=layoutSecond;e.dispatchEvent(new Event('change',{bubbles:true}));AL.UI.save();window.layoutRoundtrip=AL.Save.parse(JSON.stringify(AL.game));")
 ck('Switch to second tank survives local save and schema roundtrip',"AL.game.selectedTank===layoutSecond&&layoutRoundtrip.selectedTank===layoutSecond&&layoutRoundtrip.tanks.length===2&&AL.Save.load().state.selectedTank===layoutSecond")
 js("AL.Store.open('fish','saltwater')")
 ck('Adding residents still available with preserved destination',"AL.Store.opened&&AL.game.selectedTank===layoutSecond&&document.getElementById('store-destination').value===layoutSecond")
 js("AL.Store.open('fish','freshwater')")
 ck('Freshwater store remains locked',"AL.Store.tab==='saltwater'&&document.getElementById('toast').textContent.includes('Future Update')")
 js("AL.Store.close();AL.game.selectedTank=layoutFirst;AL.UI.render();AL.renderer.zoom=1;AL.renderer.draw(AL.game,0);window.layoutHit=AL.renderer.hitboxes.find(b=>AL.Core.selected(AL.game).fish.some(f=>f.id===b.id)&&AL.renderer.hit(b.x,b.y)===b.id);")
 hit=c.evaluate("(()=>{let b=layoutHit,r=document.getElementById('aquarium').getBoundingClientRect();return b?{x:r.x+b.x*r.width,y:r.y+b.y*r.height}:null})()")
 if hit:
  c.call('Input.dispatchMouseEvent',{'type':'mousePressed','button':'left','clickCount':1,**hit});c.call('Input.dispatchMouseEvent',{'type':'mouseReleased','button':'left','clickCount':1,**hit})
 ck('Actual pointer selects fish at its rendered position',"!!layoutHit&&document.getElementById('dialog').open&&AL.renderer.selected===layoutHit.id")
 ck('Livestock selection retains its three-second deadline',"AL.renderer.selectionUntil-performance.now()>2500&&AL.renderer.selectionUntil-performance.now()<=3000")
 time.sleep(3.2)
 ck('Livestock selection highlight expires after three seconds',"AL.renderer.selected===null")
 js("AL.UI.close();document.getElementById('tank-value').click()")
 ck('Total Aquarium Value opens correct breakdown',"AL.Shell.active==='aquariums'&&AL.Shell.subtab==='value'")
 js("AL.Shell.close();document.getElementById('zoom-in').click();document.querySelector('[data-speed=\"5\"]').click()")
 ck('Zoom and time controls remain functional',"AL.renderer.zoom===1.25&&AL.game.settings.speed===5")
 js("AL.game.settings.speed=0;document.getElementById('settings-button').click()")
 ck('Settings and saves remain accessible',"AL.Shell.active==='settings'")
 js("AL.Shell.close();document.getElementById('ocean-diving').click()")
 ck('Ocean Diving opens its interface',"document.getElementById('dialog').open&&document.getElementById('dialog-body').textContent.includes('Ocean Diving')")
 js("AL.DivingUI.requestDismiss();AL.UI.close();window.layoutValid=JSON.stringify(AL.game)")
 c.evaluate((root/'tests/overnight_probe.js').read_text(encoding='utf8'))
 js("AL.game=overnightFixture('mixed-feeder');AL.UI.render();AL.renderer.zoom=1;AL.renderer.draw(AL.game,0);window.layoutCoral=AL.renderer.hitboxes.find(b=>b.kind==='flora'&&AL.renderer.hit(b.x,b.y)===b.id);")
 hit=c.evaluate("(()=>{const b=layoutCoral,r=document.getElementById('aquarium').getBoundingClientRect();return b?{x:r.x+b.x*r.width,y:r.y+b.y*r.height}:null})()")
 if hit:
  c.call('Input.dispatchMouseEvent',{'type':'mousePressed','button':'left','clickCount':1,**hit});c.call('Input.dispatchMouseEvent',{'type':'mouseReleased','button':'left','clickCount':1,**hit})
 ck('Coral pointer target opens its living-resident inspector',"!!layoutCoral&&document.getElementById('dialog').open&&AL.renderer.selected===layoutCoral.id")
 js("AL.UI.close();AL.UI.beginCoral('zoa')")
 time.sleep(.2)
 ck('Placement banner fits with the resized tank',"AL.UI.placing&&!document.getElementById('placement-banner').hidden&&document.querySelector('.tank-card').getBoundingClientRect().bottom<=document.querySelector('.aquarium-column').getBoundingClientRect().bottom+1")
 js("AL.UI.cancelPlacement();AL.game=AL.Save.parse(layoutValid);AL.UI.render();window.layoutSaveResult=AL.UI.save();window.layoutSaved=JSON.stringify({account:AL.game.accountId,selected:AL.game.selectedTank,tanks:AL.game.tanks.map(t=>t.id)});")
 ck('Final fixture saves successfully before actual reload',"layoutSaveResult.ok")
 saved=c.evaluate('layoutSaved')
 c.navigate(root/'index.html')
 for _ in range(300):
  if c.evaluate('!!window.AL?.game&&!!AL.MortalityUI'):break
  time.sleep(.05)
 ck('Actual browser reload retains account, tanks and selection',f"JSON.stringify({{account:AL.game.accountId,selected:AL.game.selectedTank,tanks:AL.game.tanks.map(t=>t.id)}})==={json.dumps(saved)}")
 errors=[e for e in c.events if e.get('method')=='Runtime.exceptionThrown'];requests=[e['params']['request']['url'] for e in c.events if e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('http:','https:'))]
 checks.extend([{'name':'No uncaught JavaScript errors','pass':not errors,'errors':errors},{'name':'Fully offline: no remote HTTP requests','pass':not requests,'requests':requests}])
 result={'passed':sum(x['pass'] for x in checks),'failed':sum(not x['pass'] for x in checks),'checks':checks,'sizes':sizes}
 (out/f'{name}-results.json').write_text(json.dumps(result,indent=2),encoding='utf8')
 print(json.dumps({'browser':name,'passed':result['passed'],'failed':result['failed'],'failures':[x for x in checks if not x['pass']]}),flush=True)
 return int(result['failed']>0)
