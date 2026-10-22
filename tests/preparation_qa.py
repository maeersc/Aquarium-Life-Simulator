import json,time,base64
def run(c,root,name,baseline=False):
 out=root/'tests/preparation-evidence';out.mkdir(exist_ok=True)
 c.navigate(root/'index.html')
 for _ in range(200):
  if c.evaluate('!!window.AL?.game&&!!AL.DivingUI'):break
  time.sleep(.05)
 c.evaluate('localStorage.clear();AL.Startup.finish();AL.game.settings.speed=0')
 c.evaluate((root/'tests/diving_checks.js').read_text(encoding='utf8').split(" test('Two original modes")[0]+' return true;})()')
 if baseline:
  result=c.evaluate("(()=>{let s=AL.Core.newGame('marine',405,{empty:true});s.credits=100000;s.xp=2400;s.level=13;syncFixtureFinance(s);s.tanks[0].volume=300;for(const type of ['filter','heater','flow'])s=AL.Core.act(s,'buyEquipment',{type});s=AL.Core.act(s,'buyRock',{group:'fiji',variant:0,x:.5});s=AL.Core.act(s,'prepare');s=AL.Core.act(s,'cycle');AL.Sim.advance(s,2165);s=AL.Save.parse(JSON.stringify(s));const t=s.tanks[0],r=AL.DiveReceiving.report(s,'chalk-bass',t.id);return {prepared:t.prepared,emptyDry:t.emptyDry,cycle:t.cycle,bacteria:t.bacteria,bacteria2:t.bacteria2,preparation:r.checks.find(x=>x.id==='prepared'),volume:r.checks.find(x=>x.id==='volume'),state:s};})()")
  (out/'before-repair.json').write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps({k:v for k,v in result.items() if k!='state'}),flush=True);return 0
 report=c.evaluate((root/'tests/preparation_checks.js').read_text(encoding='utf8'))
 print(json.dumps({'passed':report['passed'],'failed':report['failed'],'failures':[x for x in report['checks'] if not x['pass']]}),flush=True)
 checks=report['checks']
 def ck(n,x):
  try:checks.append({'name':n,'pass':bool(c.evaluate(x))})
  except Exception as e:checks.append({'name':n,'pass':False,'error':str(e)})
 old_core=(root/'planning/preparation-repair/baseline/js__core.js').read_text(encoding='utf8')
 old_sim=(root/'planning/preparation-repair/baseline/js__simulation.js').read_text(encoding='utf8')
 ck('Seven game days of protected freshwater biology match the pre-repair engine exactly',"(()=>{const core=AL.Core,sim=AL.Sim,s=core.newGame('fresh',9182);s.tanks[0].prepared=true;s.tanks[0].bacteria=s.tanks[0].bacteria2=1;s.tanks[0].fish.push(core.fish(s,'guppy'));const a=JSON.parse(JSON.stringify(s)),b=JSON.parse(JSON.stringify(s));try{sim.advance(a,7*1440);(0,eval)("+json.dumps(old_core)+");(0,eval)("+json.dumps(old_sim)+");AL.Sim.advance(b,7*1440);return a.seed===b.seed&&JSON.stringify(a.tanks)===JSON.stringify(b.tanks)&&JSON.stringify(a.stats)===JSON.stringify(b.stats);}finally{AL.Core=core;AL.Sim=sim;}})()")
 c.evaluate("AL.game=preparationFixture(300);AL.UI.render();AL.Shell.open('aquariums','setup')")
 ck('Actual setup UI offers separate fill and preparation actions',"document.getElementById('primary-content').textContent.includes('Dry aquarium')&&!!document.querySelector('[data-action=fillWater]')&&!!document.querySelector('[data-action=prepare]')")
 c.evaluate("document.querySelector('[data-action=fillWater]').click();AL.Shell.render()")
 ck('Actual fill control yields filled/unprepared label',"AL.Preparation.state(AL.game.tanks[0]).phase==='filled'&&!document.getElementById('primary-content').textContent.includes('Dry aquarium')")
 c.evaluate("document.querySelector('[data-action=prepare]').click();AL.Shell.render()")
 ck('Actual prepare control clears dry marker and shows preparation complete',"AL.game.tanks[0].prepared&&AL.game.tanks[0].emptyDry===false&&document.getElementById('primary-content').textContent.includes('Prepared saltwater')")
 c.evaluate("AL.UI.save();AL.Shell.close();AL.game.settings.speed=0;AL.UI.save()")
 c.navigate(root/'index.html')
 for _ in range(200):
  if c.evaluate('!!window.AL?.game&&!!AL.Preparation'):break
  time.sleep(.05)
 ck('Real browser reload retains filled and prepared state',"AL.game.tanks[0].prepared&&AL.game.tanks[0].emptyDry===false")
 c.evaluate('AL.Startup.finish()')
 c.evaluate((root/'tests/diving_checks.js').read_text(encoding='utf8'))
 c.evaluate((root/'tests/mystery_diving_checks.js').read_text(encoding='utf8'))
 global_result=c.evaluate((root/'tests/global_receiving_checks.js').read_text(encoding='utf8'))
 checks.extend({'name':'Shared receiving: '+x['name'],**{k:v for k,v in x.items() if k!='name'}} for x in global_result['checks'])
 c.evaluate("AL.game=globalReturn('chalk-bass','caribbean','reef');AL.game.tanks[0].prepared=true;AL.game.tanks[0].emptyDry=true;AL.game=AL.Save.parse(JSON.stringify(AL.game));AL.UI.render();AL.DivingUI.open()")
 ck('Diving UI lists repaired destination as prepared',"!!document.querySelector('[data-mystery-receiver]')&&!document.getElementById('dialog-body').textContent.includes('Unprepared / dry')")
 for w,h in [(1920,1080),(1600,900),(1366,768),(390,844)]:
  c.call('Emulation.setDeviceMetricsOverride',{'width':w,'height':h,'deviceScaleFactor':1,'mobile':False})
  ck(f'{w}x{h} receiving diagnostics fit without horizontal overflow',"document.documentElement.scrollWidth<=innerWidth&&document.getElementById('dialog').scrollWidth<=document.getElementById('dialog').clientWidth")
  (out/f'{name}-{w}.png').write_bytes(base64.b64decode(c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
 errors=[e for e in c.events if e.get('method')=='Runtime.exceptionThrown'];checks.append({'name':'No uncaught runtime errors','pass':not errors,'errors':errors})
 checks.append({'name':'Fully offline resources and local saves','pass':not [e for e in c.events if e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('http:','https:'))]})
 report.update(passed=sum(x['pass'] for x in checks),failed=sum(not x['pass'] for x in checks))
 (out/f'{name}-results.json').write_text(json.dumps(report,indent=2),encoding='utf8');print(json.dumps({'passed':report['passed'],'failed':report['failed'],'failures':[x for x in checks if not x['pass']]}),flush=True)
 return int(report['failed']>0)
