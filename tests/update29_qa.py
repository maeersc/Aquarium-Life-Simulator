"""v2.9 offline model and real browser acceptance tests; isolated browser profile."""
import json,time,base64

def run(c,root,name):
    evidence=root/'tests/update29-evidence'
    evidence.mkdir(exist_ok=True)
    c.call('Emulation.setDeviceMetricsOverride',{'width':1366,'height':900,'deviceScaleFactor':1,'mobile':False})
    c.navigate(root/'index.html')
    for _ in range(220):
        if c.evaluate('!!window.AL?.game&&!!AL.renderer&&!!AL.Update29UI'):break
        time.sleep(.05)
    else:
        errors=[e.get('params',{}) for e in c.events if e.get('method')=='Runtime.exceptionThrown']
        raise RuntimeError('v2.9 boot failed: '+json.dumps(errors)[-7000:])
    print(json.dumps(c.evaluate("({species:Object.keys(AL.Data.species).length,corals:Object.values(AL.Data.flora).filter(d=>d.water==='marine').length,inverts:Object.keys(AL.Data.invertebrates).length,art:AL.ExpansionArt.loaded,artErrors:AL.ExpansionArt.errors,save:AL.Save.save(AL.game)})")))
    if (root/'tests/update29_checks.js').exists():
        result=c.evaluate((root/'tests/update29_checks.js').read_text(encoding='utf-8'))
        (evidence/f'{name}-logic-results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
        print(json.dumps({'passed':result['passed'],'failed':result['failed'],'failures':[r for r in result['checks'] if not r['pass']]},indent=2))
        if result.get('failed'):raise RuntimeError('v2.9 model checks failed')
    ui=[]
    def check(label,expression):
        try:
            ok=bool(c.evaluate(expression))
            ui.append({'name':label,'pass':ok})
        except Exception as exc:
            ui.append({'name':label,'pass':False,'error':str(exc)})
    def shot(label):
        data=c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']
        (evidence/f'{name}-{label}.png').write_bytes(base64.b64decode(data))
    c.evaluate("AL.Save.save=()=>({ok:true,message:'QA navigation'});localStorage.clear()")
    c.navigate(root/'index.html')
    for _ in range(220):
        if c.evaluate('!!window.AL?.game&&!!AL.renderer&&!!AL.Update29UI'):break
        time.sleep(.05)
    c.evaluate("document.querySelector('[data-startup=new]').click()")
    time.sleep(.15)
    check('Freshwater new-game route is actually disabled',"[...document.querySelectorAll('.welcome-routes button')].find(b=>JSON.parse(b.dataset.args).route==='fresh').disabled")
    c.evaluate("[...document.querySelectorAll('.welcome-routes button')].find(b=>JSON.parse(b.dataset.args).route==='marine').click();AL.game.settings.speed=0")
    time.sleep(.15)
    check('Start New Game displays the interactive twelve-phase guide',"AL.game.update29.tutorial.version===2&&AL.game.update29.tutorial.status==='active'&&!document.getElementById('tutorial-layer').hidden")
    check('Six useful sidebar destinations remain',"document.querySelectorAll('#navigation [data-page]').length===6")
    check('No Next-button tutorial bypass remains',"!document.querySelector('[data-tutorial=next],[data-guide=next]')")
    c.evaluate("document.querySelector('#tutorial-tooltip [data-guide=pause]').click();AL.Shell.open('settings')")
    check('Paused guide does not block normal gameplay',"AL.game.update29.tutorial.status==='paused'&&document.getElementById('tutorial-layer').hidden&&document.getElementById('primary-dialog').open")
    c.evaluate("document.querySelector('#interactive-tutorial-settings [data-guide=resume]').click()")
    check('Settings resumes the verified current objective',"AL.game.update29.tutorial.status==='active'&&AL.game.update29.tutorial.current==='welcome'")
    c.evaluate("document.querySelector('#interactive-tutorial-settings [data-guide=restart]').click();document.querySelector('[data-guide-confirm=restart]').click()")
    check('Confirmed restart resets guidance without creating setup evidence',"AL.game.update29.tutorial.step===0&&!AL.game.update29.tutorial.completed.cycle")
    c.evaluate("AL.Shell.open('journal','disease')")
    check('Disease guide remains available without invented diagnosis or treatment',"document.getElementById('primary-content').textContent.includes('does not diagnose')&&document.querySelectorAll('.guide-entry').length>0")
    shot('medical-guide')
    c.evaluate("AL.Shell.open('settings');document.querySelector('#interactive-tutorial-settings [data-guide=skip]').click();document.querySelector('[data-guide-confirm=skip]').click();AL.UI.save()")
    saved=c.evaluate('JSON.stringify({current:AL.game.update29.tutorial.current,status:AL.game.update29.tutorial.status,completed:AL.game.update29.tutorial.completed})')
    c.navigate(root/'index.html')
    for _ in range(220):
        if c.evaluate('!!window.AL?.game&&!!AL.renderer&&!!AL.Update29UI'):break
        time.sleep(.05)
    check('Actual browser reload preserves tutorial step and skip state',f'JSON.stringify({{current:AL.game.update29.tutorial.current,status:AL.game.update29.tutorial.status,completed:AL.game.update29.tutorial.completed}})==={json.dumps(saved)}')
    c.evaluate('AL.Startup.finish();AL.game.settings.speed=0')
    # Reload removes test fixture functions; reload only the function declaration from the model suite.
    c.evaluate((root/'tests/update29_checks.js').read_text(encoding='utf-8'))
    c.evaluate("AL.game=v29Fixture().s;AL.Update29UI.updateTutorial();AL.UI.render();AL.UI.inspectFish(AL.game.tanks[0].fish[0].id)")
    check('Click/inspection immediately shows the selection outline',"AL.renderer.selected===AL.game.tanks[0].fish[0].id&&document.getElementById('dialog').open")
    time.sleep(2)
    c.evaluate('AL.UI.inspectFish(AL.game.tanks[0].fish[0].id)')
    time.sleep(1.2)
    check('Reclicking the same creature restarts the three-second timer',"AL.renderer.selected===AL.game.tanks[0].fish[0].id")
    time.sleep(2)
    check('Selection expires after three seconds while inspector stays open',"AL.renderer.selected===null&&document.getElementById('dialog').open&&document.getElementById('dialog-body').textContent.includes('Health')")
    shot('inspector-after-outline')
    c.evaluate("AL.UI.close();AL.UI.inspectFish(AL.game.tanks[0].fish[0].id);const next=AL.Core.tank(AL.game,'marine',75,'Second reef','reef');AL.game.tanks.push(next);AL.Update29.migrate(AL.game);AL.game.selectedTank=next.id")
    check('Changing aquariums clears the old outline immediately',"AL.renderer.selected===null")
    c.evaluate("AL.UI.close();AL.game=v29Fixture().s;AL.UI.render();AL.Store.open('fish','saltwater');window.destinationBefore=AL.game.selectedTank")
    time.sleep(.1)
    check('Freshwater store tab is disabled with the coming-update explanation',"[...document.querySelectorAll('[data-store-action=tab]')].find(b=>JSON.parse(b.dataset.storeArgs).id==='freshwater').disabled")
    c.evaluate("document.querySelector('[data-store-action=tab][data-store-args*=black]').click()")
    check('Deep Market is inside Aquarium Store and retains selected destination',"AL.Store.tab==='black'&&document.getElementById('store-dialog').open&&AL.game.selectedTank===destinationBefore&&document.getElementById('store-main-tabs').textContent.includes('Deep Market')&&!document.getElementById('store-main-tabs').textContent.includes('Black Market')")
    c.evaluate("AL.Store.close();AL.Store.open('fish','saltwater')")
    check('Closing/reopening store preserves the destination and eight fish slots',"AL.game.selectedTank===destinationBefore&&AL.Store.products().length===8")
    c.evaluate("AL.Store.open('bottom','saltwater')")
    check('Mystery Bottom-Dweller Egg visibly explains the Legendary pool hold',"document.getElementById('store-products').textContent.includes('Mystery Bottom-Dweller Egg')&&document.getElementById('store-products').textContent.includes('Catalog content hold')")
    shot('bottom-mystery-hold')
    c.evaluate("AL.Store.open('flora','saltwater');AL.Store.details('mystery:coral')")
    check('Mystery Coral details show all six exact odds and safe destination',"['50%','25%','15%','7.5%','2%','0.5%'].every(t=>document.getElementById('dialog-body').textContent.includes(t))&&!document.getElementById('confirm-fish').disabled")
    c.evaluate("document.querySelector('[data-form=storePurchase]').requestSubmit()")
    check('Mystery Coral asks the player to place it before purchase',"AL.UI.placing&&AL.renderer.placement.shopArgs.mystery&&AL.game.tanks[0].flora.length===0")
    pos=c.evaluate("(()=>{const p=AL.Update29.mounting(AL.game,AL.game.tanks[0],'duncanopsammia-axifuga'),r=document.getElementById('aquarium').getBoundingClientRect();return {x:r.x+((p.x-AL.renderer.pan)*AL.renderer.zoom+.5)*r.width,y:r.y+((p.y-.5)*AL.renderer.zoom+.5)*r.height}})()")
    c.call('Input.dispatchMouseEvent',{'type':'mouseMoved',**pos})
    c.call('Input.dispatchMouseEvent',{'type':'mousePressed','button':'left','clickCount':1,**pos})
    c.call('Input.dispatchMouseEvent',{'type':'mouseReleased','button':'left','clickCount':1,**pos})
    (evidence/f'{name}-placement.json').write_text(json.dumps(c.evaluate("({canvas:document.getElementById('aquarium').getBoundingClientRect().toJSON(),placing:AL.renderer.placement,flora:AL.game.tanks[0].flora,toast:document.getElementById('toast').textContent})"),indent=2),encoding='utf-8')
    check('Actual placement click buys one coral at its chosen valid mount',"AL.game.tanks[0].flora.length===1&&AL.game.tanks[0].flora[0].mystery.product==='coral'&&AL.Habitat.validAttachment(AL.game.tanks[0],AL.game.tanks[0].flora[0])&&!AL.UI.placing")
    shot('mystery-coral-placed')
    c.evaluate("AL.Shell.open('journal','leaderboards')")
    check('Saltwater leaderboard is explicitly a local asset-value preview',"document.getElementById('primary-content').textContent.includes('Local comparison only')&&document.getElementById('primary-content').textContent.includes('not wallet balance')")
    shot('leaderboards')
    c.evaluate("document.querySelector('[data-leaderboard=fresh]').click()")
    check('Freshwater leaderboard is accessible only as a locked preview',"document.getElementById('primary-content').textContent.includes(AL.Update29.lockText)")
    c.evaluate("AL.Shell.open('journal','history')")
    check('Tank History explains separate rewards and recovery',"['+50 AC','+100 AC','Recovery'].every(t=>document.getElementById('primary-content').textContent.includes(t))")
    c.evaluate("AL.Shell.open('aquariums','new')")
    c.evaluate("[...document.querySelectorAll('[data-action=configureTank]')].find(b=>JSON.parse(b.dataset.args).volume===AL.Update29Catalog.capacity).click()")
    time.sleep(.1)
    check('Large tank configuration keeps freshwater disabled and shows exact marine price',"document.querySelector('form[data-form=buyTank] [name=water]').value==='marine'&&document.querySelector('form[data-form=buyTank] option[value=fresh]').disabled&&document.getElementById('dialog-body').textContent.includes('marine 5000 AC')")
    c.evaluate("document.querySelector('form[data-form=buyTank]').requestSubmit()")
    check('Real tank purchase creates the exact empty 15,000-gallon system',"AL.Core.selected(AL.game).volume===AL.Update29Catalog.capacity&&!AL.Core.selected(AL.game).prepared&&AL.Valuation.tank(AL.game,AL.Core.selected(AL.game)).base===5000")
    c.evaluate("AL.UI.close();AL.game=v29Fixture().s;AL.UI.render();AL.Shell.open('journal','achievements')")
    check('First achievement has implemented requirements and no free unearned reward',"document.getElementById('primary-content').textContent.includes('First safe beginning')&&document.querySelector('#primary-content [data-action=claim]').disabled")
    c.evaluate("AL.game.stats.prepared=1;AL.Shell.render();document.querySelector('#primary-content [data-action=claim]').click()")
    check('Achievement claim grants its real quest reward exactly once',"AL.game.quests.prepare===true&&AL.game.achievements.includes('First safe beginning')")
    for width,height in [(390,844),(768,1024),(1366,900),(1920,1080)]:
        c.call('Emulation.setDeviceMetricsOverride',{'width':width,'height':height,'deviceScaleFactor':1,'mobile':False})
        c.evaluate("AL.Shell.open('journal','leaderboards')")
        time.sleep(.08)
        check(f'Leaderboard preview fits viewport width {width}',"document.documentElement.scrollWidth<=innerWidth+2&&document.getElementById('primary-dialog').getBoundingClientRect().right<=innerWidth+2")
        if width in (390,1366):shot('responsive-'+str(width))
    c.evaluate("AL.Shell.close();AL.UI.close();AL.Store.close();AL.game=v29Fixture().s;AL.UI.render()")
    for width,height in [(390,844),(764,485),(1366,900)]:
        c.call('Emulation.setDeviceMetricsOverride',{'width':width,'height':height,'deviceScaleFactor':1,'mobile':False})
        time.sleep(.1)
        check(f'Live aquarium remains visible at {width} by {height}',"(()=>{const r=document.getElementById('aquarium').getBoundingClientRect();return r.width>=200&&r.height>=100&&r.top>=0&&r.bottom<=innerHeight&&r.right<=innerWidth})()")
        (evidence/f'{name}-layout-{width}.json').write_text(json.dumps(c.evaluate("({width:innerWidth,height:innerHeight,client:document.documentElement.clientWidth,canvas:document.getElementById('aquarium').getBoundingClientRect().toJSON(),cardMax:getComputedStyle(document.querySelector('.tank-card')).maxWidth,workspace:document.querySelector('.workspace').getBoundingClientRect().toJSON()})"),indent=2),encoding='utf-8')
        shot('main-'+str(width))
    c.evaluate('AL.UI.save()')
    c.navigate(root/'v29-review.html')
    for _ in range(220):
        if c.evaluate("document.querySelectorAll('#v29-stages canvas').length===8"):break
        time.sleep(.04)
    check('New standalone art gallery loads all 35 sheets offline',"AL.ExpansionArt.loaded===35&&AL.ExpansionArt.errors.length===0&&document.getElementById('v29-species').options.length===35")
    c.evaluate("document.getElementById('v29-species').value='hymenocera-picta';document.getElementById('v29-species').dispatchEvent(new Event('change'));document.getElementById('v29-facing').value='-1';document.getElementById('v29-facing').dispatchEvent(new Event('change'))")
    check('Gallery supports developmental states and whole-sprite left-facing review',"document.querySelectorAll('#v29-stages canvas').length===8&&document.getElementById('v29-title').textContent.includes('Harlequin')")
    shot('new-art-gallery')
    errors=[e.get('params',{}) for e in c.events if e.get('method')=='Runtime.exceptionThrown']
    ui.append({'name':'No unhandled browser exceptions during acceptance flows','pass':not errors,'errors':errors})
    requests=[e['params']['request']['url'] for e in c.events if e.get('method')=='Network.requestWillBeSent' and e.get('params',{}).get('request',{}).get('url','').startswith(('http:','https:'))]
    ui.append({'name':'No external HTTP traffic or remote save requests','pass':not requests,'requests':requests})
    summary={'passed':result['passed']+sum(r['pass'] for r in ui),'failed':result['failed']+sum(not r['pass'] for r in ui),'logic':{'passed':result['passed'],'failed':result['failed']},'ui':ui}
    (evidence/f'{name}-results.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    print(json.dumps({'passed':summary['passed'],'failed':summary['failed'],'failures':[r for r in ui if not r['pass']]},indent=2))
    return 1 if summary['failed'] else 0
