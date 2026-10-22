"""Real file-origin protected-runtime checks, all native sheets and gameplay interfaces."""
import base64,hashlib,json,sys,time

def run(c,root,name):
 out=root/'tests/distribution-protection-evidence';out.mkdir(exist_ok=True);c.sock.settimeout(300)
 entry=root/'DIST/index.html';manifest=json.loads((root/'DIST/build-manifest.json').read_text(encoding='utf8'))
 c.call('Network.emulateNetworkConditions',{'offline':True,'latency':0,'downloadThroughput':0,'uploadThroughput':0})
 c.call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':900,'deviceScaleFactor':1,'mobile':False})
 clear=c.call('Page.addScriptToEvaluateOnNewDocument',{'source':'localStorage.clear();'})['identifier']
 started=time.monotonic();c.navigate(entry,timeout=90)
 for _ in range(600):
  if c.evaluate('!!window.AL?.game&&!!AL.loop'):break
  time.sleep(.05)
 else:raise RuntimeError('Protected game did not boot')
 startup=time.monotonic()-started;c.call('Page.removeScriptToEvaluateOnNewDocument',{'identifier':clear})
 c.evaluate('AL.Startup.finish();AL.Save.unlock();AL.UI.close();AL.game.settings.speed=0;window.__small='+ (root/'tests/performance-evidence/fixture-small.json').read_text(encoding='utf8'))
 c.evaluate((root/'tests/performance_probe.js').read_text(encoding='utf8'))
 checks=c.evaluate((root/'tests/performance_checks.js').read_text(encoding='utf8'))
 def js(code):return c.evaluate('(()=>{'+code+'})()')
 def ck(label,expr):
  try:checks.append({'name':label,'pass':bool(c.evaluate('!!('+expr+')'))})
  except Exception as e:checks.append({'name':label,'pass':False,'error':str(e)})
 ck('Protected build runs with network disabled at the local file origin',"location.protocol==='file:'&&!!AL.Core&&!!AL.Save&&!!AL.Store&&!!AL.Breeding&&!!AL.Casino&&!!AL.Diving")
 ck('Public biological registry and authored animation interfaces remain stable',"Object.keys(AL.Data.species).length===105&&AL.FishAnimation.catalog.entries.length===119&&AL.FishAnimation.catalog.entries.filter(e=>e.productionEligible).length===113&&AL.DiveReceiving.registryAudit().length===0")
 ck('Only protected runtime scripts are loaded, without review tools',"[...document.scripts].filter(s=>s.src).every(s=>/js\/a\.[a-f0-9]{20}\.js$/.test(s.src))&&AL.CareUI.developerTools()===''")
 js("__probe.fixture('A');AL.game.settings.speed=0;AL.Shell.open('settings')")
 ck('Production Settings excludes artwork developer review links',"!document.querySelector('.developer-tools')&&!document.querySelector('#primary-content a[href*=review]')")
 js("AL.Shell.close();AL.Finance.change(AL.game,10000,{category:'other',action:'qaFixture',name:'Isolated protected-build funds'});window.savedSelection=AL.game.selectedTank;AL.Store.open('equipment','saltwater');AL.Store.details('equipment:filter');window.beforePurchase={balance:AL.game.credits,stock:AL.game.stock.filter,owned:AL.game.ownedEquipment.length};const n=document.querySelector('#purchase-quantity');n.value='2';n.dispatchEvent(new Event('input',{bubbles:true}));window.purchaseCost=Number(document.querySelector('#purchase-total').textContent.replace(/[^0-9]/g,''));document.querySelector('[data-form=storePurchase]').requestSubmit()")
 ck('Protected Store bulk purchase creates distinct equipment and charges exact total',"AL.game.ownedEquipment.length===beforePurchase.owned+2&&AL.game.credits===beforePurchase.balance-purchaseCost&&AL.game.stock.filter===beforePurchase.stock-2&&AL.game.ownedEquipment.at(-1).id!==AL.game.ownedEquipment.at(-2).id&&AL.game.selectedTank===savedSelection")
 js("AL.Store.close();AL.Shell.open('equipment','inventory')")
 ck('Equipment Inventory exposes both purchased units',"document.querySelectorAll('#primary-content [data-action=inventoryInstall]').length>=2")
 js("AL.Shell.close();AL.Store.open('fish','saltwater');document.querySelector('[data-store-action=tab][data-store-args*=freshwater]').click()")
 ck('Freshwater remains locked and current tank remains selected',"AL.Store.tab==='saltwater'&&AL.game.selectedTank===savedSelection")
 js("AL.Store.close();AL.game.settings.speed=0;AL.UI.render()")
 print(json.dumps({'stage':'boot and interfaces','checks':len(checks),'failed':sum(not x['pass'] for x in checks)}),flush=True)
 native=c.evaluate("""(async()=>{const rows=[],A=AL.FishAnimation;for(const e of A.catalog.entries)for(const clip of e.clips){const r=A.sheets.find(e.id,clip.stage,clip.state,clip.variety),loaded=await A.sheets.load(r);rows.push({name:e.id+'/'+(clip.variety||'standard')+'/'+clip.stage+'/'+clip.state+': original16-frame file transport decodes and validates distinct nonblank cells',pass:!!loaded&&!r.failed&&clip.frameCount===16});if(loaded){const frames=Array.from({length:16},(_,i)=>A.sheets.frame(r,i/16));rows.push({name:e.id+'/'+clip.stage+'/'+clip.state+': all16 cells retain geometry and metadata',pass:frames.every((f,i)=>f&&f.width===clip.frameWidth&&f.height===clip.frameHeight&&f.artMeta.frameCount===16&&f.artMeta.frameIndex>=0&&f.artMeta.anchor)});}}return {rows,issues:A.sheets.issues,metrics:A.sheets.metrics};})()""")
 checks.extend(native['rows']);checks.append({'name':'All382 native sprite sheets load locally with no transport/pixel-validation issues','pass':len(native['rows'])==764 and not native['issues'],'issues':native['issues']})
 ck('Native sheet loading releases all temporary classic scripts and pending strings',"AL.SpriteSources.metrics.pending===0&&AL.SpriteSources.metrics.active===0&&AL.SpriteSources.metrics.queued===0&&!document.querySelector('script[src*=animation-sources]')")
 js("__probe.fixture('A');AL.game.settings.speed=0;window.expectedSave=JSON.stringify({worldId:AL.game.worldId,accountId:AL.game.accountId,tanks:AL.game.tanks,inventory:AL.game.inventory,finance:AL.game.finance,selectedTank:AL.game.selectedTank,credits:AL.game.credits});window.written=AL.Save.save(AL.game)")
 ck('Existing migrated profile validates and saves locally without rewriting identities',"written.ok&&AL.Save.validate(AL.game)===AL.game")
 expected=c.evaluate('expectedSave');c.navigate(entry,timeout=90)
 for _ in range(600):
  if c.evaluate('!!window.AL?.game'):break
  time.sleep(.05)
 ck('Protected local reload preserves profile, residents, tank, finance and supplies',"JSON.stringify({worldId:AL.game.worldId,accountId:AL.game.accountId,tanks:AL.game.tanks,inventory:AL.game.inventory,finance:AL.game.finance,selectedTank:AL.game.selectedTank,credits:AL.game.credits})==="+json.dumps(expected))
 errors=[e for e in c.events if e.get('method')=='Runtime.exceptionThrown'];checks.append({'name':'No uncaught protected-runtime errors','pass':not errors,'errors':errors})
 (out/f'{name}-protected.png').write_bytes(base64.b64decode(c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
 result={'buildId':manifest['buildId'],'entry':'DIST/index.html','startupSeconds':startup,'networkDisabled':True,'passed':sum(x['pass'] for x in checks),'failed':sum(not x['pass'] for x in checks),'checks':checks,'sheets':native['metrics']}
 (out/f'{name}-protected.json').write_text(json.dumps(result,indent=2),encoding='utf8')
 print(json.dumps({'passed':result['passed'],'failed':result['failed'],'failures':[x for x in checks if not x['pass']][:20]},indent=2),flush=True)
 return int(result['failed']>0)
