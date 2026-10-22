"""v2.7 integration checks in isolated file:// browser profiles with networking off."""
import json,time,base64,hashlib
def run(c,root,name):
 out=root/'tests/expansion-evidence';out.mkdir(exist_ok=True)
 c.navigate(root/'index.html')
 c.call('Emulation.setDeviceMetricsOverride',{'width':1366,'height':900,'deviceScaleFactor':1,'mobile':False})
 for _ in range(300):
  if c.evaluate('!!window.AL?.game&&!!AL.ExpansionUI'):break
  time.sleep(.05)
 else:
  print(c.evaluate("({errors:typeof AL,body:document.body.innerText.slice(0,300)})"));print(c.events[-10:]);return 1
 c.evaluate("AL.Startup.finish();AL.game.settings.speed=0;AL.UI.close();AL.Store.close();AL.Shell.close()")
 results=c.evaluate((root/'tests/expansion_checks.js').read_text(encoding='utf-8'))
 # Existing core/coral and disease/value/economy cases, with only the fixture
 # calendar synchronized when it deliberately changes game time.
 import re
 c.evaluate("let resultNode=document.createElement('pre');resultNode.id='results';resultNode.hidden=true;document.body.append(resultNode)")
 core=(root/'tests/suite.js').read_text(encoding='utf-8')
 core=re.sub(r'(s\.time=[^;]+;)',r'\1delete s.update29;AL.Update29.migrate(s);AL.DailyStore.rotate(s);window.syncFixtureFinance?.(s);for(const t of s.tanks)if(t.water==="marine"){t.environmentHistory=t.environmentHistory.filter(e=>e.time<=s.time);t.autoFeedSlot=Math.min(t.autoFeedSlot,Math.floor((s.time-60)/240));if(t.mortalityHistory)t.mortalityHistory.samples=t.mortalityHistory.samples.filter(e=>e.time<=s.time);}',core)
 core=re.sub(r'(s\.credits=[^;]+;)',r'\1window.syncFixtureFinance?.(s);',core)
 # Exercise retained freshwater mechanics in an explicitly unlocked test adapter only.
 # Production gates are separately exercised by all v2.9 model/UI acceptance checks.
 c.evaluate("window.guard29=AL.Update29;window.guardStore=AL.StoreRules;AL.Update29={...guard29,beforeAction:()=>{}}")
 legacy_rules=(root/'js/store-rules.js').read_text(encoding='utf-8')
 legacy_rules='\n'.join(line for line in legacy_rules.splitlines() if "if(action==='buyTank'&&a.water==='fresh'||t?.water==='fresh'" not in line)
 c.evaluate(legacy_rules)
 try:c.evaluate(core);results.extend(c.evaluate('TEST_REPORT.results'))
 finally:c.evaluate('AL.Update29=guard29;AL.StoreRules=guardStore')
 c.evaluate((root/'tests/economy_checks.js').read_text(encoding='utf-8'));results.extend(c.evaluate('runEconomyChecks().results'))
 (out/f'{name}-logic-results.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
 def check(label,s):
  try:results.append({'name':label,'pass':bool(c.evaluate(s))})
  except Exception as e:results.append({'name':label,'pass':False,'error':str(e)})
 def shot(label):
  r=c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False});(out/f'{name}-{label}.png').write_bytes(base64.b64decode(r['data']))
 c.evaluate("window.freshBio=()=>{const s=AL.Core.newGame('fresh',445),t=s.tanks[0];s.credits=100000;t.prepared=true;t.bacteria=t.bacteria2=1;t.fish.push(AL.Core.fish(s,'guppy'),AL.Core.fish(s,'guppy'));for(let day=0;day<10;day++){AL.Core.feed(s,AL.Core.selected(s),'flakes');AL.Sim.advance(s,1440);}const t2=AL.Core.selected(s);return {seed:s.seed,time:s.time,water:t2.waterParams,fish:t2.fish.map(f=>Object.fromEntries(Object.entries(f).filter(([k])=>k!=='id')))};};window.currentCore=AL.Core;window.currentSim=AL.Sim;window.currentSave=AL.Save;window.freshCurrent=freshBio();")
 try:c.evaluate('AL.Save={validate:s=>s};'+(root/'tests/economy-protected-core.js').read_text(encoding='utf-8')+'\n'+(root/'tests/economy-protected-simulation.js').read_text(encoding='utf-8')+'\nwindow.freshOld=freshBio();')
 finally:c.evaluate('AL.Core=currentCore;AL.Sim=currentSim;AL.Save=currentSave;')
 check('Ten-day freshwater biology exactly matches protected earlier code',"JSON.stringify(freshCurrent)===JSON.stringify(freshOld)")
 c.evaluate("AL.game=expansionFixture();AL.game.settings.speed=0;AL.UI.render();AL.Store.open('fish','saltwater')")
 check('Live daily Fish store still has exactly eight listings',"document.querySelectorAll('#store-products .store-item').length===8")
 check('Mystery Egg no longer has missing-tier content hold',"AL.DailyStore.shortfall().length===0&&AL.Store.products()[7].stock===3")
 c.evaluate("AL.Store.details(AL.game.dailyStore.slots[7].id)")
 check('Real Mystery purchase has a safe eligible destination',"!document.getElementById('confirm-fish').disabled")
 c.evaluate("document.querySelector('[data-form=storePurchase]').requestSubmit()")
 check('Actual Mystery UI purchase creates one persistent brood',"AL.game.tanks[0].eggs.length===1&&AL.game.tanks[0].eggs[0].mystery.revealed&&AL.game.selectedTank===AL.game.tanks[0].id")
 shot('mystery-unlocked')
 c.evaluate("AL.Store.open('bottom','saltwater')")
 check('Bottom shop keeps original five and adds only eligible ordinary-tier invertebrates',"AL.Store.products().filter(p=>p.kind==='invertebrate').length===7&&document.querySelectorAll('[data-product-id^=\"invertebrate:\"]').length===7")
 c.evaluate("AL.Store.details('invertebrate:sexy-anemone-shrimp');document.querySelector('[data-form=storePurchase]').requestSubmit()")
 check('Actual invertebrate purchase goes into non-fish collection',"AL.game.tanks[0].invertebrates.length===1&&!AL.game.tanks[0].fish.length")
 shot('bottom-store')
 c.evaluate("AL.UI.close();AL.Store.close();AL.ExpansionUI.inspect(AL.game.tanks[0].invertebrates[0].id)")
 check('Invertebrate inspector has name, science, rarity, care, life stage, health and value',"['Thor amboinensis','Rarity: Uncommon','NON-FISH','Current Value','Age / life stage','Diet:'].every(t=>document.getElementById('dialog-body').textContent.includes(t))")
 shot('invertebrate-inspector')
 c.evaluate("AL.UI.close();AL.Shell.open('journal','encyclopedia');document.querySelector('[data-encyclopedia-category=other]').click()")
 check('Other Marine Invertebrates lists all ten scientific identities',"document.querySelectorAll('#primary-content [data-action=invertebrateNotes]').length===10")
 c.evaluate("document.querySelector('[data-encyclopedia-category=flora]').click()")
 check('Saltwater coral encyclopedia contains fifteen entries',"document.querySelectorAll('#primary-content [data-action=journalFlora]').length===15")
 c.evaluate("AL.Shell.close();AL.Store.open('flora','saltwater')")
 check('Coral shop preserves allowed prior groups and adds two ordinary corals plus Mystery Coral',"AL.Store.products().filter(p=>p.kind==='flora').length===12&&AL.Store.products().some(p=>p.id==='mystery:coral')")
 shot('coral-store')
 for width in [390,768,1366,1920]:
  c.call('Emulation.setDeviceMetricsOverride',{'width':width,'height':900,'deviceScaleFactor':1,'mobile':False})
  check(f'Expanded store fits {width}px viewport',"document.documentElement.scrollWidth<=innerWidth&&document.getElementById('store-dialog').getBoundingClientRect().right<=innerWidth")
 protected=json.loads((root/'tests/freshwater-protection-baseline.json').read_text())
 results.append({'name':'145 protected freshwater definitions/art/source hashes unchanged','pass':all(hashlib.sha256((root/p).read_bytes()).hexdigest()==h for p,h in protected.items() if p!='js/simulation.js')})
 errors=[e for e in c.events if e.get('method')=='Runtime.exceptionThrown'];network=[e for e in c.events if e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('http:','https:'))]
 results.append({'name':'No browser JavaScript exceptions','pass':not errors,'errors':errors})
 results.append({'name':'No HTTP/HTTPS gameplay requests','pass':not network})
 # Standalone gallery uses only local generated atlases and a separate notes key.
 c.evaluate('AL.UI.save()')
 c.navigate(root/'expansion-review.html')
 for _ in range(300):
  if c.evaluate("!!document.querySelector('#review-stages canvas')"):break
  time.sleep(.03)
 saved=c.evaluate("localStorage.getItem('aquarium-life-v2')")
 check('Offline v2.7 review gallery loads all 38 sprite sheets',"AL.ExpansionArt.loaded===38&&AL.ExpansionArt.errors.length===0&&document.querySelectorAll('#review-stages canvas').length===8")
 for category,total in [('fish',28),('coral',5),('bottom_dweller',5)]:
  c.evaluate("document.getElementById('review-category').value="+json.dumps(category)+";document.getElementById('review-category').dispatchEvent(new Event('change'))")
  check(f'Review category {category} has exactly {total} entries',f"document.getElementById('review-species').options.length==={total}")
 c.evaluate("document.getElementById('review-direction').value='-1';document.getElementById('review-direction').dispatchEvent(new Event('change'));document.getElementById('review-notes').value='Automated QA note';document.getElementById('save-review').click()")
 check('Review notes do not replace gameplay save',"localStorage.getItem('aquarium-life-v2')==="+json.dumps(saved))
 c.call('Emulation.setDeviceMetricsOverride',{'width':1366,'height':900,'deviceScaleFactor':1,'mobile':False});shot('review-gallery')
 report={'browser':name,'passed':sum(r['pass'] for r in results),'failed':sum(not r['pass'] for r in results),'results':results}
 (out/f'{name}-results.json').write_text(json.dumps(report,indent=2),encoding='utf-8');print(name,report['passed'],'passed;',report['failed'],'failed',flush=True)
 for r in results:
  if not r['pass']:print('FAIL',r,flush=True)
 return int(bool(report['failed']))
