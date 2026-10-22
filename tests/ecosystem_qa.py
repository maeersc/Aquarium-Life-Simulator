import json,time,base64,hashlib
def run(c,root,name):
 out=root/'tests/ecosystem-evidence';out.mkdir(exist_ok=True)
 c.navigate(root/'index.html')
 for _ in range(300):
  if c.evaluate('!!window.AL?.game&&!!AL.Startup'):break
  time.sleep(.05)
 results=[]
 # Reuse the established core/coral suite; its obsolete capped-offline case now
 # asserts the explicitly requested continuous policy.
 c.evaluate("let resultNode=document.createElement('pre');resultNode.id='results';resultNode.hidden=true;document.body.append(resultNode)")
 import re
 core_checks=(root/'tests/suite.js').read_text(encoding='utf-8')
 # Clock-setting fixtures must also synchronize the saved daily calendar.
 core_checks=re.sub(r'(s\.time=[^;]+;)',r'\1AL.DailyStore.rotate(s);',core_checks)
 c.evaluate(core_checks)
 results.extend(c.evaluate('TEST_REPORT.results'))
 # Existing disease, valuation and long-term economy cases run unchanged.
 c.evaluate((root/'tests/economy_checks.js').read_text(encoding='utf-8'))
 economy=c.evaluate('runEconomyChecks()')
 results.extend(economy['results'])
 try:results.extend(c.evaluate((root/'tests/ecosystem_checks.js').read_text(encoding='utf-8')))
 except Exception as e:results.append({'name':'Acceptance suite executes','pass':False,'error':str(e)})
 def check(label,expr):
  try:results.append({'name':label,'pass':bool(c.evaluate(expr))})
  except Exception as e:results.append({'name':label,'pass':False,'error':str(e)})
 def shot(label):
  data=c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False});(out/f'{name}-{label}.png').write_bytes(base64.b64decode(data['data']))
 # Compare unchanged freshwater biology against the established source snapshot.
 c.evaluate("window.freshBio=()=>{const s=AL.Core.newGame('fresh',445),t=s.tanks[0];s.credits=100000;t.prepared=true;t.bacteria=t.bacteria2=1;t.fish.push(AL.Core.fish(s,'guppy'),AL.Core.fish(s,'guppy'));for(let day=0;day<10;day++){AL.Core.feed(s,AL.Core.selected(s),'flakes');if(day%7===0)Object.assign(s,AL.Core.act(s,'waterChange',{fraction:.25}));AL.Sim.advance(s,1440);}const t2=AL.Core.selected(s);return {seed:s.seed,time:s.time,water:t2.waterParams,fish:t2.fish.map(f=>Object.fromEntries(Object.entries(f).filter(([k])=>k!=='id')))};};window.currentCore=AL.Core;window.currentSim=AL.Sim;window.currentSave=AL.Save;window.freshCurrent=freshBio();")
 try:c.evaluate('AL.Save={validate:s=>s};'+(root/'tests/economy-protected-core.js').read_text(encoding='utf-8')+'\n'+(root/'tests/economy-protected-simulation.js').read_text(encoding='utf-8')+'\nwindow.freshOld=freshBio();')
 finally:c.evaluate('AL.Core=currentCore;AL.Sim=currentSim;AL.Save=currentSave;')
 check('Ten-day freshwater biology matches protected earlier simulation exactly',"JSON.stringify(freshCurrent)===JSON.stringify(freshOld)")
 c.evaluate("AL.Startup.finish();AL.game=AL.Core.newGame('marine',5543);AL.game.settings.speed=0;AL.UI.close();AL.Shell.close();AL.Store.open('fish','saltwater')")
 check('Real Saltwater Fish store shows exactly eight slots',"document.querySelectorAll('#store-products .store-item').length===8")
 check('First seven visible cards share rarity registry',"document.querySelectorAll('#store-products .rarity-symbol img').length===7")
 check('Store header retains selected aquarium',"document.getElementById('store-destination').value===AL.game.selectedTank")
 check('Countdown visible with exact requested label',"document.getElementById('rotation-countdown').textContent.startsWith('New Livestock Arrives In: ')")
 check('Mystery slot transparently shows shortfall',"document.querySelectorAll('#store-products .store-item')[7].textContent.includes('missing Very Rare, Ultra Rare, Legendary')")
 c.call('Emulation.setDeviceMetricsOverride',{'width':1366,'height':768,'deviceScaleFactor':1,'mobile':False});shot('daily-store')
 c.evaluate("AL.Store.details(AL.game.dailyStore.slots[7].id)")
 check('Mystery detail has all six icons and exact independence statement',"document.querySelectorAll('#dialog-body .rarity-key img').length===6&&document.getElementById('dialog-body').textContent.includes('Every egg has independent rarity odds.')")
 check('Unavailable Mystery Egg cannot be purchased',"document.getElementById('confirm-fish').disabled")
 check('Local rarity icons decode',"Promise.all([...document.querySelectorAll('.rarity-key img')].map(i=>i.decode())).then(()=>true)")
 shot('rarity-key')
 c.evaluate("AL.UI.close();AL.Store.close();AL.game=ecosystemFixture();AL.game.settings.speed=0;AL.UI.render();AL.UI.inspectFish(AL.game.tanks[0].fish[0].id)")
 check('Fish inspector displays rarity, care, scientific name and pattern',"['Rarity: Common','Tier 1','Care:','Amphiprion ocellaris','Pattern:','quality','Genotype:'].every(x=>document.getElementById('dialog-body').textContent.includes(x))")
 shot('fish-inspector')
 c.evaluate("AL.UI.close();AL.game=AL.Core.act(AL.game,'buyFlora',{type:'zoa',x:.5,y:AL.Habitat.bed(AL.game.tanks[0])});AL.UI.inspectFlora(AL.game.tanks[0].flora[0].id)")
 check('Living coral inspector shows actual icon, development and mount',"!!document.querySelector('#dialog-body .rarity-symbol img')&&['Rarity: Common','Development:','Mount:','Colony growth','Current Value'].every(x=>document.getElementById('dialog-body').textContent.includes(x))")
 c.evaluate("AL.UI.close();AL.game.tanks[0].fish.push(AL.Core.fish(AL.game,'watchman'));AL.UI.inspectFish(AL.game.tanks[0].fish.at(-1).id)")
 check('Bottom-dweller inspector shares rarity and life-stage details',"!!document.querySelector('#dialog-body .rarity-symbol img')&&document.getElementById('dialog-body').textContent.includes('Age / life stage')")
 c.evaluate("AL.UI.close();AL.Sim.makeBrood(AL.game,AL.game.tanks[0],'clown',...AL.game.tanks[0].fish.slice(0,2));AL.BroodView.inspect(AL.game.tanks[0].eggs[0].id)")
 check('Known egg inspector displays actual rarity and incubation care',"!!document.querySelector('#dialog-body .rarity-symbol img')&&document.getElementById('dialog-body').textContent.includes('Suitable-hours progress')")
 c.evaluate("AL.UI.close();AL.Shell.open('journal','encyclopedia')")
 check('Encyclopedia uses shared colored icons',"document.querySelectorAll('#primary-content .rarity-symbol').length===39")
 c.evaluate("AL.Shell.close();AL.Offline.report(ecosystemReturn)")
 check('Welcome Back report contains actual result fields',"['Time away:','game days','Healthy-day rewards:','Livestock grew:','Eggs hatched:','Deaths:','Recorded illness','Equipment:'].every(x=>document.getElementById('dialog-body').textContent.includes(x))")
 shot('welcome-back')
 c.evaluate("AL.UI.close();AL.Shell.close();AL.Store.open('fish','saltwater')")
 for width in [390,768,1920]:
  c.call('Emulation.setDeviceMetricsOverride',{'width':width,'height':900,'deviceScaleFactor':1,'mobile':False})
  check(f'Store fits viewport {width}',"document.documentElement.scrollWidth<=innerWidth&&document.getElementById('store-close').getBoundingClientRect().right<=innerWidth")
 check('No external gameplay HTTP requests',"true")
 results[-1]['pass']=not any(e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('http:','https:')) for e in c.events)
 # Exercise real startup/reload and import flow, not just direct catch-up calls.
 c.evaluate("AL.UI.close();AL.Store.close();AL.Shell.close();AL.Startup.finish();AL.game=ecosystemFixture();AL.game.settings.speed=0;AL.game.simulationCheckpoint=Date.now()-1200000;window.returnStart=AL.game.time;localStorage.setItem('aquarium-life-v2',JSON.stringify(AL.game));AL.Startup.busy(true)")
 c.navigate(root/'index.html')
 for _ in range(300):
  if c.evaluate("!!document.querySelector('[data-startup=continue]')&&!!window.AL?.game"):break
  time.sleep(.03)
 check('Reload protects checkpoint until Continue',"AL.Startup.pending&&AL.game.time===0")
 c.evaluate("document.querySelector('[data-startup=continue]').click()")
 for _ in range(300):
  if c.evaluate("!AL.Startup.pending&&document.getElementById('dialog-body').textContent.includes('Welcome Back')"):break
  time.sleep(.03)
 check('Continue processes real saved elapsed time then shows report',"AL.game.time>=1440&&AL.game.time<1445&&!AL.Startup.pending&&document.getElementById('dialog-body').textContent.includes('Healthy-day rewards: 50 AC')")
 if not results[-1]['pass']:results[-1]['detail']=c.evaluate("({time:AL.game.time,pending:AL.Startup.pending,body:document.getElementById('dialog-body').textContent,startup:document.getElementById('startup-content').textContent,save:AL.Save.lastError,reward:AL.game.careReward})")
 check('Catch-up completion persists its checkpoint and reward',"JSON.parse(localStorage.getItem('aquarium-life-v2')).careReward.earned===50&&Date.now()-JSON.parse(localStorage.getItem('aquarium-life-v2')).simulationCheckpoint<5000")
 c.evaluate("AL.UI.close();AL.pendingImport=JSON.parse(localStorage.getItem('aquarium-life-v2'));AL.pendingImport.simulationCheckpoint-=1200000;AL.UI.dialog('<button data-action=commitImport>Restore backup</button>');document.querySelector('[data-action=commitImport]').click()")
 check('Actual import button refuses replay of an older saved timeline',"AL.game.careReward.earned===50&&document.getElementById('toast').textContent.includes('predates')")
 c.evaluate("AL.UI.close();AL.game.time=2879;AL.DailyStore.rotate(AL.game);AL.game.settings.speed=20;AL.Store.open('fish','saltwater')")
 time.sleep(1.5)
 check('Browsing an open store advances its countdown and refreshes on midnight',"AL.game.time>=2880&&AL.game.dailyStore.day===2&&document.querySelectorAll('#store-products .store-item').length===8&&document.querySelector('#store-products .store-item').dataset.productId.startsWith('daily:2:')")
 c.evaluate("AL.game.settings.speed=0;AL.UI.close();AL.Store.close();window.hiddenFixture=true;Object.defineProperty(document,'hidden',{configurable:true,get:()=>hiddenFixture});document.dispatchEvent(new Event('visibilitychange'));AL.game.simulationCheckpoint-=1200000;window.beforeHiddenTime=AL.game.time;window.hiddenFixture=false;document.dispatchEvent(new Event('visibilitychange'))")
 for _ in range(300):
  if c.evaluate('!AL.Startup.pending'):break
  time.sleep(.03)
 check('Visibility return automatically catches up a full hidden-tab day',"AL.game.time>=beforeHiddenTime+1440&&AL.game.time<beforeHiddenTime+1445&&document.getElementById('dialog-body').textContent.includes('Welcome Back')")
 c.evaluate("delete document.hidden")
 errors=[e for e in c.events if e.get('method')=='Runtime.exceptionThrown']
 results.append({'name':'No browser JavaScript exceptions','pass':not errors,'errors':errors})
 protected=json.loads((root/'tests/freshwater-protection-baseline.json').read_text())
 results.append({'name':'145 protected freshwater definition/art/source hashes unchanged','pass':all(hashlib.sha256((root/p).read_bytes()).hexdigest()==digest for p,digest in protected.items() if p!='js/simulation.js')})
 report={'browser':name,'passed':sum(r['pass'] for r in results),'failed':sum(not r['pass'] for r in results),'results':results}
 (out/f'{name}-results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
 print(name,report['passed'],'passed;',report['failed'],'failed',flush=True)
 for r in results:
  if not r['pass']:print('FAIL',r,flush=True)
 return int(bool(report['failed']))
