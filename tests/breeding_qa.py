"""Autonomous marine breeding, shared clock, UI, migration and offline evidence."""
import base64,json,time,sys

def run(c,root,name):
 out=root/'tests/breeding-evidence';out.mkdir(exist_ok=True)
 c.call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':900,'deviceScaleFactor':1,'mobile':False})
 entry=root/('DIST/index.html' if '--dist' in sys.argv else 'index.html');c.sock.settimeout(300);c.navigate(entry,timeout=60)
 for _ in range(300):
  if c.evaluate('!!window.AL?.game&&!!AL.Breeding'):break
  time.sleep(.05)
 c.evaluate("localStorage.clear();AL.Startup.finish();AL.game.settings.speed=0")
 c.evaluate((root/'tests/overnight_probe.js').read_text(encoding='utf8'))
 report=c.evaluate((root/'tests/breeding_checks.js').read_text(encoding='utf8'))
 (out/f'{name}-model-results.json').write_text(json.dumps(report,indent=2),encoding='utf8')
 print(json.dumps({'browser':name,'modelPassed':report['passed'],'modelFailed':report['failed'],'failures':[r for r in report['checks'] if not r['pass']]}),flush=True)
 checks=report['checks']
 def js(s):return c.evaluate('(()=>{'+s+'})()')
 def ck(label,expr):
  try:checks.append({'name':label,'pass':bool(c.evaluate(expr))})
  except Exception as e:checks.append({'name':label,'pass':False,'error':str(e)})
 def shot(label):
  (out/f'{name}-{label}.png').write_bytes(base64.b64decode(c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
 js("AL.game=breedCourtFixture();AL.game.settings.speed=0;for(let n=0;n<4;n++)AL.Sim.step(AL.game,5);AL.UI.render();AL.renderer.draw(AL.game,0)")
 shot('courtship-aquarium')
 js("AL.UI.inspectFish(AL.game.tanks[0].fish[0].id)")
 ck('Inspector contains correct reproductive role, mate, maturity and courtship',"document.querySelector('[data-reproduction-panel]').textContent.includes('Courtship')&&document.querySelector('[data-reproduction-panel]').textContent.includes('Female')&&document.querySelector('[data-reproduction-panel]').textContent.includes('Maturity')")
 js("window.selectedExpiry=AL.renderer.selectionUntil;AL.game.time+=140;AL.BreedingUI.update()")
 ck('Inspector refreshes female gravid state without resetting the selection timer',"document.querySelector('[data-reproduction-panel]').textContent.includes('Gravid')&&document.querySelector('abbr[title*=Gravid]')&&AL.renderer.selectionUntil===selectedExpiry")
 time.sleep(3.2)
 ck('Selection outline expires after three seconds while inspector stays open',"AL.renderer.selected===null&&document.getElementById('dialog').open")
 js("document.querySelector('[data-reproduction-panel]').scrollIntoView({block:'start',behavior:'instant'})")
 shot('gravid-inspector')
 js("AL.UI.close();AL.Shell.open('journal','history')")
 ck('Journal is a read-only observation dashboard with all four sections',"['Breeding Activity','Active Clutches','Offspring','Breeding History'].every(s=>document.getElementById('primary-content').textContent.includes(s))&&!document.querySelector('[data-action=breed]')")
 ck('Separate coral fragging lineage remains in journal',"document.getElementById('primary-content').textContent.includes('Player-fragged clone lineage')")
 shot('journal-courtship')
 js("AL.Shell.close();AL.game=breedSpawnFixture();AL.game.settings.speed=0;AL.UI.render();AL.renderer.draw(AL.game,0);window.savedClutch=JSON.stringify(AL.game.tanks[0].eggs)")
 ck('Attached natural clutch renders a selectable egg hitbox',"AL.game.tanks[0].eggs.length===1&&AL.renderer.hitboxes.some(b=>b.kind==='egg')")
 js("AL.BroodView.inspect(AL.game.tanks[0].eggs[0].id)")
 ck('Clutch inspector has small fixed-size cluster preview and real parents',"document.getElementById('egg-inspector')&&document.getElementById('dialog-body').textContent.includes('fixed-size')&&AL.game.tanks[0].eggs[0].parents.every(id=>document.getElementById('dialog-body').textContent.includes(AL.game.tanks[0].fish.find(f=>f.id===id).name))")
 shot('attached-clutch')
 js("AL.UI.close()")
 for label,open_js,close_js in [
  ('Store',"AL.Store.open('fish','saltwater')","AL.Store.close()"),
  ('Field Journal',"AL.Shell.open('journal','history')","AL.Shell.close()"),
  ('Dock Casino',"AL.CasinoUI.open()","AL.CasinoUI.close()"),
  ('Diving',"AL.DivingUI.open()","AL.DivingUI.requestDismiss()")]:
  js("AL.game=breedCourtFixture();AL.game.settings.speed=20;AL.UI.render();window.modalBreedTime=AL.game.time;"+open_js)
  time.sleep(5 if label=='Diving' else .6)
  ck(label+': courtship and normal swimming continue on the shared game clock',"AL.game.time>modalBreedTime&&AL.game.tanks[0].fish.some(f=>f.behavior==='Prepare nest')&&AL.game.tanks[0].breeding.pairs.length===1")
  js(close_js+";AL.game.settings.speed=0")
 js("AL.game=breedSpawnFixture();AL.game.settings.speed=0;AL.UI.render()")
 js("AL.UI.close();AL.game.settings.speed=0;AL.UI.save();window.breedingBeforeReload=JSON.stringify(AL.game.breeding);window.breedingAccount=AL.game.accountId")
 c.navigate(root/'index.html')
 for _ in range(300):
  if c.evaluate('!!window.AL?.game'):break
  time.sleep(.05)
 ck('Actual local save reload retains a single clutch and exact parentage',"AL.game.tanks[0].eggs.length===1&&AL.game.tanks[0].eggs[0].naturalBreeding&&AL.game.breeding.records.filter(r=>r.clutchId===AL.game.tanks[0].eggs[0].id).length===1")
 js("AL.Startup.finish();AL.game.settings.speed=0;AL.Shell.open('journal','history')")
 for w,h in [(1920,1080),(1600,900),(1366,768),(390,844)]:
  c.call('Emulation.setDeviceMetricsOverride',{'width':w,'height':h,'deviceScaleFactor':1,'mobile':False})
  ck(f'{w}x{h}: breeding journal has no horizontal overflow',"document.documentElement.scrollWidth<=innerWidth&&document.getElementById('primary-content').scrollWidth<=document.getElementById('primary-content').clientWidth")
  shot('journal-'+str(w))
 errors=[e for e in c.events if e.get('method')=='Runtime.exceptionThrown']
 requests=[e['params']['request']['url'] for e in c.events if e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('http:','https:'))]
 checks.extend([{'name':'No browser JavaScript exceptions','pass':not errors,'errors':errors},{'name':'Fully offline without HTTP/HTTPS gameplay requests','pass':not requests,'requests':requests}])
 report.update(entry=entry.relative_to(root).as_posix(),passed=sum(r['pass'] for r in checks),failed=sum(not r['pass'] for r in checks))
 (out/f'{name}-results.json').write_text(json.dumps(report,indent=2),encoding='utf8')
 print(json.dumps({'browser':name,'passed':report['passed'],'failed':report['failed'],'failures':[r for r in checks if not r['pass']]}),flush=True)
 return int(report['failed']>0)
