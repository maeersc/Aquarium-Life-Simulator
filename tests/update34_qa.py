"""Daily survival reward v3.4: real offline simulation, dialogs and local saves."""
import json,time,base64

def run(c,root,name):
 out=root/'tests/update34-evidence';out.mkdir(exist_ok=True)
 c.call('Emulation.setDeviceMetricsOverride',{'width':1366,'height':900,'deviceScaleFactor':1,'mobile':False})
 c.navigate(root/'index.html')
 for _ in range(250):
  if c.evaluate('!!window.AL?.game&&!!AL.Update31UI'):break
  time.sleep(.04)
 else:raise RuntimeError('Game did not initialize')
 c.evaluate("AL.Startup.finish();AL.UI.close();AL.Shell.close();AL.Store.close();AL.game.settings.speed=0")
 baseline=c.evaluate((root/'tests/update33_checks.js').read_text(encoding='utf-8'))
 result=c.evaluate((root/'tests/update34_checks.js').read_text(encoding='utf-8'))
 (out/f'{name}-logic-results.json').write_text(json.dumps({'baseline':baseline,'reward':result},indent=2),encoding='utf-8')
 print(json.dumps({'baselinePassed':baseline['passed'],'rewardPassed':result['passed'],'failed':baseline['failed']+result['failed'],'failures':[r for r in baseline['checks']+result['checks'] if not r['pass']]},indent=2),flush=True)
 if baseline['failed'] or result['failed']:return 1
 ui=[]
 def check(label,expr):
  try:ui.append({'name':label,'pass':bool(c.evaluate(expr))})
  except Exception as error:ui.append({'name':label,'pass':False,'error':str(error)})
 def shot(label):
  data=c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']
  (out/f'{name}-{label}.png').write_bytes(base64.b64decode(data))
 c.evaluate("AL.game=v34Fixture();AL.Update29UI.settleNotifications(AL.game);AL.Sim.advance(AL.game,1440);AL.UI.render();AL.Update29UI.update()")
 check('The live reward notification says exactly +100 AC',"document.getElementById('toast').textContent==='Livestock Survival Bonus: +100 AC'")
 c.evaluate("document.getElementById('finance-open').click()")
 check('AC dashboard shows the actual +100 payment and the separate +50 reward',"(()=>{const r=AL.game.finance.rows.filter(r=>r.action==='survivalReward');return r.length===1&&r[0].amount===100&&document.getElementById('finance-history').textContent.includes('Livestock Survival Bonus')&&document.getElementById('finance-history').textContent.includes('+100 AC')&&document.getElementById('finance-history').textContent.includes('+50 AC');})()")
 check('Payment details include qualification status and the completed qualifying day',"document.getElementById('finance-history').textContent.includes('Qualification status')&&document.getElementById('finance-history').textContent.includes('qualified')&&document.getElementById('finance-history').textContent.includes('Qualifying day')")
 shot('survival-ledger')
 c.evaluate("document.querySelector('[data-v31=financeClose]').click();AL.game=v34Fixture(2);AL.Update29UI.settleNotifications(AL.game);AL.Core.kill(AL.game,AL.game.tanks[0],AL.game.tanks[0].fish[0],'QA notification');AL.Update29UI.update()")
 check('Confirmed loss shows the required recovery notification',"document.getElementById('toast').textContent===AL.Update29.lossMessage")
 c.evaluate("AL.Shell.open('journal','history')")
 check('Tank History shows +100, the separate +50, 150 combined and recovery countdown',"['+100 AC','+50 AC','150 AC','Recovery remaining:'].every(x=>document.getElementById('primary-content').textContent.includes(x))&&!document.getElementById('primary-content').textContent.includes('+200 AC')")
 shot('recovery-history')
 started=c.evaluate('AL.game.time');time.sleep(4.7)
 check('Field Journal keeps time and recovery countdown moving despite the underlying pause',f"AL.game.time>{started}&&AL.game.settings.speed===0&&document.getElementById('survival-reward-status').textContent.includes('Recovery remaining:')")
 windows=[('Equipment',"AL.Shell.open('equipment','fragging')"),('Aquarium Store',"AL.Store.open('fish','saltwater')"),('Deep Market',"AL.game.stats.nightMarket=1;AL.Store.open('wanted','black')"),('Ocean Diving',"AL.DivingUI.open()"),('Financial Overview',"AL.Update31UI.openFinance()"),('Other game dialog',"AL.UI.dialog('<h2>Living aquarium window</h2>')")]
 for label,open_code in windows:
  c.evaluate("if(document.getElementById('finance-dialog')?.open)document.getElementById('finance-dialog').close();if(AL.DivingUI.ownsDialog)AL.DivingUI.requestDismiss();AL.UI.close();AL.Store.close();AL.Shell.close();AL.game=v34Fixture();AL.UI.render();"+open_code)
  started=c.evaluate('AL.game.time');time.sleep(4.7)
  check(label+' keeps the authoritative simulation and qualification timer running',f'AL.game.time>{started}&&AL.game.update29.survival.tracked>0&&AL.game.settings.speed===0')
 c.evaluate("if(document.getElementById('finance-dialog')?.open)document.getElementById('finance-dialog').close();AL.UI.close();AL.Store.close();AL.Shell.close();AL.game=v34Fixture();AL.Update29UI.settleNotifications(AL.game);window.v34Report=AL.Offline.sync(AL.game,AL.game.simulationCheckpoint+3600000);document.getElementById('toast').textContent='';AL.Update29UI.update();AL.Offline.report(v34Report)")
 check('Long offline catch-up uses a consolidated 300-AC survival summary without individual toast spam',"document.getElementById('dialog-body').textContent.includes('Survival rewards: 300 AC')&&document.getElementById('dialog-body').textContent.includes('Survival days without a payment: 0')&&document.getElementById('toast').textContent===''")
 shot('offline-summary')
 c.evaluate("AL.UI.close();AL.game=v34Fixture(2);AL.Sim.advance(AL.game,500);AL.Core.kill(AL.game,AL.game.tanks[0],AL.game.tanks[0].fish[0],'QA reload');AL.UI.save();window.v34Saved={account:AL.game.accountId,recovery:AL.game.update29.survival.recoveryUntil,lastDeath:AL.game.update29.survival.lastDeath};")
 saved=c.evaluate('v34Saved');c.navigate(root/'index.html')
 for _ in range(250):
  if c.evaluate('!!window.AL?.game&&!!AL.Update31UI'):break
  time.sleep(.04)
 check('Actual local reload preserves account identity, death timestamp and recovery',f"AL.game.accountId==={json.dumps(saved['account'])}&&AL.game.update29.survival.recoveryUntil==={saved['recovery']}&&AL.game.update29.survival.lastDeath==={saved['lastDeath']}&&AL.game.update29.survival.earned===0")
 errors=[e for e in c.events if e.get('method')=='Runtime.exceptionThrown']
 ui.append({'name':'No JavaScript exceptions in the reward flows','pass':not errors,'errors':errors})
 network=[e['params']['request']['url'] for e in c.events if e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('http:','https:'))]
 ui.append({'name':'Reward processing and UI need no internet service','pass':not network,'requests':network})
 report={'passed':baseline['passed']+result['passed']+sum(r['pass'] for r in ui),'failed':sum(not r['pass'] for r in ui),'baseline':baseline,'reward':result,'ui':ui}
 (out/f'{name}-results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
 print(json.dumps({'passed':report['passed'],'failed':report['failed'],'failures':[r for r in ui if not r['pass']]},indent=2),flush=True)
 return int(bool(report['failed']))
