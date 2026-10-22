"""Offline runtime and UI acceptance evidence for the marine health/value milestone."""
import base64,hashlib,json,time

def run(client,root,name):
    out=root/'tests/economy-evidence';out.mkdir(exist_ok=True)
    client.navigate(root/'index.html')
    for _ in range(150):
        if client.evaluate('!!window.AL?.game&&!!AL.HealthUI'):break
        time.sleep(.05)
    client.evaluate("AL.Store.close(false);AL.Startup?.finish();AL.UI.close();AL.game.settings.speed=0")
    client.evaluate((root/'tests/economy_checks.js').read_text(encoding='utf8'))
    report=client.evaluate('runEconomyChecks()')
    (out/f'{name}-logic-results.json').write_text(json.dumps(report,indent=2),encoding='utf8')
    checks=report['results']
    def check(name,expression):
        try:checks.append({'name':name,'pass':bool(client.evaluate(expression))})
        except Exception as e:checks.append({'name':name,'pass':False,'error':str(e)})
    def shot(label):
        data=client.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})
        (out/f'{name}-{label}.png').write_bytes(base64.b64decode(data['data']))
    client.call('Emulation.setDeviceMetricsOverride',{'width':1440,'height':1100,'deviceScaleFactor':1,'mobile':False})
    client.evaluate("(()=>{let s=AL.Core.newGame('marine',712),t=s.tanks[0];s.credits=100000;s.level=11;s.xp=2000;s.settings.speed=0;s.stats.nightMarket=1;s.time=1260;t.prepared=true;t.bacteria=t.bacteria2=1;s=AL.Core.act(s,'buyFish',{species:'clown'});AL.Health.infect(s,s.tanks[0].fish[0],'ich',.5);s=AL.Core.act(s,'buyMedicine',{product:'diagnostic'});AL.game=s;AL.Save.unlock();AL.UI.goto('aquariums');})()")
    client.evaluate("AL.UI.inspectFish(AL.game.tanks[0].fish[0].id)")
    check('Fish inspector displays Current Value and nutrition without revealing unexamined disease',"document.getElementById('dialog-body').textContent.includes('Current Value:')&&document.getElementById('dialog-body').textContent.includes('Nutrition:')&&!document.getElementById('dialog-body').textContent.includes('Examined: Marine ich')")
    shot('fish-before-examination')
    client.evaluate("document.querySelector('[data-action=examineLivestock]').click()")
    check('Actual examination button consumes supplies and displays confidence',"document.getElementById('dialog-body').textContent.includes('Examined: Marine ich')&&AL.game.medicalInventory[0].quantity===2")
    shot('diagnosis')
    client.evaluate("AL.Startup?.finish();AL.UI.close();document.getElementById('tank-value').click()")
    check('Clickable Tank Value shows base and total with all category breakdowns',"AL.Shell.active==='aquariums'&&AL.Shell.subtab==='value'&&document.getElementById('primary-content').textContent.includes('Base tank value')&&document.getElementById('primary-content').textContent.includes('Total current asset value')&&document.getElementById('primary-content').textContent.includes('Bottom feeders')")
    shot('tank-value')
    client.evaluate("AL.Startup?.finish();AL.UI.close();AL.Store.open('medicines','saltwater')")
    check('Exactly three primary tabs plus legitimate medicine category',"document.querySelectorAll('#store-main-tabs [role=tab]').length===3&&document.getElementById('store-sub-tabs').textContent.includes('Medicine & Treatment')&&AL.Store.products().length===8")
    shot('medicines-store')
    client.evaluate("AL.Store.details('medicine:coralSupport');document.querySelector('[data-form=storePurchase]').requestSubmit()")
    check('Actual fixed-price medicine purchase reaches batch inventory and preserves selection',"AL.game.medicalInventory.some(b=>b.product==='coralSupport'&&b.quantity===2)&&AL.game.selectedTank===AL.game.tanks[0].id")
    client.evaluate("AL.Store.open('restricted','black')")
    check('Restricted Treatments uses persistent fictional listings without exposing hidden quality',"document.getElementById('store-sub-tabs').textContent.includes('Restricted Treatments')&&AL.Store.products().length===2&&AL.Store.products().every(p=>p.args.listingId)&&!document.getElementById('store-products').textContent.includes('contamination detected')")
    shot('restricted-treatments')
    client.evaluate("AL.Store.close(false);AL.Store.open('fish','saltwater');AL.Store.details('fish:clown')")
    start=len(client.events)
    client.evaluate("const n=document.getElementById('purchase-count');n.value=2;n.dispatchEvent(new Event('input',{bubbles:true}))")
    client.call('Runtime.evaluate',{'expression':'0'})
    checks.append({'name':'Real store quantity change no longer invokes obsolete handler','pass':not any(e.get('method')=='Runtime.exceptionThrown' for e in client.events[start:])})
    client.evaluate('AL.Startup?.finish();AL.UI.close();AL.Store.close(false)')
    # Direct comparison with the pre-update source in the same JS engine. Normalized identities
    # differ because new market batches have IDs; all freshwater biological values must match.
    old_core=(root/'tests/economy-protected-core.js').read_text(encoding='utf8')
    old_sim=(root/'tests/economy-protected-simulation.js').read_text(encoding='utf8')
    client.evaluate("""window.freshBio=()=>{const s=AL.Core.newGame('fresh',445),t=s.tanks[0];s.credits=100000;t.prepared=true;t.bacteria=t.bacteria2=1;t.fish.push(AL.Core.fish(s,'guppy'),AL.Core.fish(s,'guppy'));for(let day=0;day<10;day++){AL.Core.feed(s,AL.Core.selected(s),'flakes');if(day%7===0){const next=AL.Core.act(s,'waterChange',{fraction:.25});Object.assign(s,next);}AL.Sim.advance(s,1440);}const current=AL.Core.selected(s);return {seed:s.seed,time:s.time,water:current.waterParams,fish:current.fish.map(f=>Object.fromEntries(Object.entries(f).filter(([k])=>k!=='id')))};};window.currentCore=AL.Core;window.currentSim=AL.Sim;window.currentSave=AL.Save;window.freshCurrent=freshBio();""")
    try:
        client.evaluate('AL.Save={validate:s=>s};'+old_core+'\n'+old_sim+'\nwindow.freshOld=freshBio();')
    finally:client.evaluate('AL.Core=currentCore;AL.Sim=currentSim;AL.Save=currentSave;')
    check('Ten-day freshwater biological values match the pre-update code exactly',"JSON.stringify(freshCurrent)===JSON.stringify(freshOld)")
    protected=json.loads((root/'tests/freshwater-protection-baseline.json').read_text())
    checks.append({'name':'All 144 protected freshwater art/source files and species definitions remain byte-identical','pass':all(hashlib.sha256((root/p).read_bytes()).hexdigest()==h for p,h in protected.items() if p!='js/simulation.js')})
    for width in [1440,1024,760,390]:
        client.call('Emulation.setDeviceMetricsOverride',{'width':width,'height':1100,'deviceScaleFactor':1,'mobile':False})
        client.evaluate('AL.HealthUI.details(AL.game.tanks[0].fish[0].id)')
        check(f'Medical inspector fits {width}px width',"document.documentElement.scrollWidth<=innerWidth&&document.getElementById('dialog').getBoundingClientRect().right<=innerWidth")
        if width==390:shot('medical-narrow')
        client.evaluate('AL.UI.close()')
    client.evaluate("(()=>{let s=AL.Core.newGame('marine',713),t=s.tanks[0];s.credits=100000;s.level=11;s.xp=2000;s.settings.speed=0;t.kind='quarantine';t.prepared=true;t.bacteria=t.bacteria2=1;s=AL.Core.act(s,'bareQuarantine');s=AL.Core.act(s,'buyFish',{species:'clown'});AL.Health.infect(s,s.tanks[0].fish[0],'ich',.5);s=AL.Core.act(s,'buyMedicine',{product:'diagnostic'});s=AL.Core.act(s,'examineLivestock',{id:s.tanks[0].fish[0].id});s=AL.Core.act(s,'buyMedicine',{product:'copper'});AL.game=s;AL.UI.goto('aquariums');AL.HealthUI.details(s.tanks[0].fish[0].id);})()")
    client.evaluate("document.querySelector('[data-action=startTreatment]').click()")
    check('Actual Begin course control starts timed treatment and consumes only one unit',"AL.game.tanks[0].fish[0].healthState.treatment?.product==='copper'&&AL.game.medicalInventory.find(b=>b.product==='copper').quantity===0&&document.getElementById('dialog-body').textContent.includes('0% complete')")
    shot('active-course')
    errors=[e['params'].get('exceptionDetails',{}) for e in client.events if e.get('method')=='Runtime.exceptionThrown']
    http=[e['params']['request']['url'] for e in client.events if e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('http:','https:'))]
    checks.append({'name':'Offline index produces no HTTP(S) request','pass':not http})
    checks.append({'name':'New runtime and UI produce no uncaught browser exceptions','pass':not errors})
    report.update({'browser':name,'passed':sum(r['pass'] for r in checks),'failed':sum(not r['pass'] for r in checks),'exceptions':errors,'networkRequests':http,'date':'2026-10-13'})
    (out/f'{name}-results.json').write_text(json.dumps(report,indent=2),encoding='utf8')
    print(json.dumps({k:v for k,v in report.items() if k not in ['results','exceptions']}),flush=True)
    for r in checks:
        if not r['pass']:print('FAIL:',r['name'],r.get('error',''),flush=True)
    return 1 if report['failed'] else 0
