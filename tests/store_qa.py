"""Real offline store interaction, destination invariants, and coral mounting checks."""
import base64
import hashlib
import json
import time

def run(client,root,name,check):
    results=[]
    client.navigate(root/'index.html')
    for _ in range(100):
        if client.evaluate('!!window.AL?.game'):break
        time.sleep(.05)
    client.evaluate("""(()=>{
      if(document.getElementById('dialog').open)AL.Startup?.finish();AL.UI.close();if(AL.Store.opened)AL.Store.close(false);
      const s=AL.Core.newGame('fresh',320),fresh=s.tanks[0];s.credits=100000;s.xp=2000;s.level=11;s.settings.speed=0;
      const reef=AL.Core.tank(s,'marine',150,'The reef destination','reef'),unsafe=AL.Core.tank(s,'marine',150,'Unprepared reef','reef');s.tanks.push(reef,unsafe);
      for(const t of [fresh,reef]){t.prepared=true;t.bacteria=1;t.bacteria2=1;t.cycle=36;}
      reef.equipment.push({type:'reefLight',capacity:300,durability:100,enabled:true});s.selectedTank=fresh.id;
      AL.game=s;AL.Save.unlock();AL.UI.goto('aquariums');AL.UI.save();window.STORE_FIXTURE={fresh:fresh.id,reef:reef.id,unsafe:unsafe.id};
    })()""")
    def evaluate(expr,message):results.append(check(client.evaluate(expr),message))
    def choose(main=None,sub=None):
        if main:client.evaluate(f"document.querySelector('#store-main-tabs [data-store-args*=\"{main}\"]').click()")
        if sub:client.evaluate(f"document.querySelector('#store-sub-tabs [data-store-args*=\"{sub}\"]').click()")
    def shot(label):
        data=client.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})
        (root/'assets/previews'/f'{name}-store-{label}.png').write_bytes(base64.b64decode(data['data']))
    client.call('Emulation.setDeviceMetricsOverride',{'width':1440,'height':1100,'deviceScaleFactor':1,'mobile':False})
    client.evaluate("document.getElementById('store-quick').click()")
    evaluate("AL.Store.opened&&AL.UI.modalOpen&&AL.game.selectedTank===STORE_FIXTURE.fresh",'Opening store is modal and preserves freshwater destination')
    evaluate("AL.Store.tab==='saltwater'&&document.querySelectorAll('#store-main-tabs [role=tab]').length===3",'Saltwater defaults with exactly three main store tabs')
    evaluate("document.getElementById('store-destination-name').textContent==='The quiet shallows'",'Selected aquarium is visible in fixed store header')
    evaluate("AL.Store.products().filter(p=>p.kind==='fish').every(p=>p.habitat==='marine')",'Saltwater fish products are filtered by structured habitat')
    for tab,subcount in [('freshwater',7),('black',7),('saltwater',8)]:
        choose(tab)
        evaluate(f"AL.game.selectedTank===STORE_FIXTURE.fresh&&document.querySelectorAll('#store-sub-tabs button').length==={subcount}",f'{tab}: tabs preserve destination and render required subcategories')
        for category in client.evaluate("Array.from(document.querySelectorAll('#store-sub-tabs button'),b=>JSON.parse(b.dataset.storeArgs).id)"):
            choose(sub=category)
            evaluate("AL.game.selectedTank===STORE_FIXTURE.fresh",f'{tab}/{category}: destination never changes')
    choose('freshwater','sand')
    evaluate("document.getElementById('store-products').textContent.includes('No implemented freshwater items in this category.')",'Empty freshwater category has an honest empty state')
    choose('black','fish')
    client.evaluate('AL.game.level=1;AL.game.xp=0;AL.Store.render()')
    evaluate("document.getElementById('store-products').textContent.includes('locked')&&!document.querySelector('#store-products .item-card')",'Black Market progression lock is shown without purchasable cards')
    client.evaluate('AL.game.level=11;AL.game.xp=2000;AL.Store.render()')
    choose('saltwater','fish');shot('desktop')
    client.evaluate("AL.Store.details('fish:clown')")
    evaluate("document.getElementById('dialog').open&&document.getElementById('confirm-fish').disabled&&document.getElementById('compatibility-report').textContent.includes('Incompatible')",'Incompatible aquarium warns and disables livestock purchase')
    evaluate("document.querySelector('#purchase-destination option[value=\"'+STORE_FIXTURE.reef+'\"]').disabled===false&&document.querySelector('#purchase-destination option[value=\"'+STORE_FIXTURE.unsafe+'\"]').disabled===true",'Eligible alternative offered; unprepared alternative disabled')
    money=client.evaluate('AL.game.credits')
    client.evaluate("document.querySelector('[data-form=storePurchase]').requestSubmit()")
    evaluate(f'AL.game.credits==={money}&&AL.game.tanks.every(t=>t.fish.length===0)', 'Submitting an incompatible destination cannot charge or place livestock')
    client.evaluate("const sel=document.getElementById('purchase-destination');sel.value=STORE_FIXTURE.reef;sel.dispatchEvent(new Event('change'))")
    evaluate("AL.game.selectedTank===STORE_FIXTURE.reef&&document.getElementById('store-destination').value===STORE_FIXTURE.reef&&!document.getElementById('confirm-fish').disabled",'Explicit eligible destination choice updates selected aquarium and header')
    client.evaluate("const form=document.querySelector('[data-form=storePurchase]');form.requestSubmit();form.requestSubmit()")
    evaluate(f'AL.game.credits==={money}-180&&AL.Core.selected(AL.game).fish.length===1&&AL.game.tanks[0].fish.length===0','Repeated confirmation charges once and places only in chosen reef')
    evaluate("AL.game.selectedTank===STORE_FIXTURE.reef&&AL.Store.opened",'Completed purchase preserves aquarium selection and shopping session')
    client.evaluate("AL.Store.details('fish:clown');AL.Core.selected(AL.game).waterParams.oxygen=1;document.querySelector('[data-form=storePurchase]').requestSubmit()")
    evaluate(f'AL.game.credits==={money}-180&&AL.Core.selected(AL.game).fish.length===1','Purchase revalidates changed oxygen at submission')
    client.evaluate("AL.Core.selected(AL.game).waterParams.oxygen=7.5;AL.Startup?.finish();AL.UI.close();document.getElementById('store-close').click()")
    evaluate("!AL.Store.opened&&AL.game.selectedTank===STORE_FIXTURE.reef&&document.activeElement.id==='store-quick'",'X closes modal, retains destination and restores Store focus')
    client.evaluate("document.getElementById('store-quick').click()")
    evaluate("AL.game.selectedTank===STORE_FIXTURE.reef",'Closing and reopening retains destination')
    client.call('Input.dispatchKeyEvent',{'type':'keyDown','key':'Escape','code':'Escape','windowsVirtualKeyCode':27})
    client.call('Input.dispatchKeyEvent',{'type':'keyUp','key':'Escape','code':'Escape','windowsVirtualKeyCode':27})
    evaluate('!AL.Store.opened&&AL.game.selectedTank===STORE_FIXTURE.reef','Escape closes store without changing selection')
    client.evaluate("document.getElementById('store-quick').click();AL.Store.details('fish:clown')")
    client.call('Input.dispatchKeyEvent',{'type':'keyDown','key':'Escape','code':'Escape','windowsVirtualKeyCode':27})
    client.call('Input.dispatchKeyEvent',{'type':'keyUp','key':'Escape','code':'Escape','windowsVirtualKeyCode':27})
    evaluate("!document.getElementById('dialog').open&&AL.Store.opened",'Escape closes higher-priority details before store')
    choose('freshwater','equipment');client.evaluate('AL.Store.chooseDestination(STORE_FIXTURE.fresh);AL.Store.details("equipment:air");document.querySelector("[data-form=storePurchase]").requestSubmit()')
    evaluate("AL.game.selectedTank===STORE_FIXTURE.fresh&&AL.Core.selected(AL.game).equipment.some(e=>e.type==='air')&&!AL.game.tanks.find(t=>t.id===STORE_FIXTURE.reef).equipment.some(e=>e.type==='air')",'Shared equipment purchase installs in explicit chosen aquarium')
    choose(sub='supplies');food_before=client.evaluate('AL.game.inventory.flakes')
    client.evaluate('AL.Store.details("food:flakes");document.querySelector("[data-form=storePurchase]").requestSubmit()')
    evaluate(f'AL.game.inventory.flakes==={food_before}+20&&AL.game.selectedTank===STORE_FIXTURE.fresh','Consumables go to inventory and preserve aquarium selection')
    client.evaluate('AL.Store.chooseDestination(STORE_FIXTURE.reef)');choose('saltwater','rocks')
    client.evaluate('AL.Store.details("rock:fiji:0");document.querySelector("[data-form=storePurchase]").requestSubmit();document.getElementById("aquarium").dispatchEvent(new KeyboardEvent("keydown",{key:"Enter",bubbles:true}));AL.Store.open("rocks","saltwater")')
    evaluate("AL.Core.selected(AL.game).hardscape.length===6&&AL.game.tanks[0].hardscape===undefined",'Marine rock purchase goes to chosen reef only')
    choose(sub='sand');client.evaluate('AL.Store.details("sand:caribbean");document.querySelector("[name=depth]").value="3.2";document.querySelector("[data-form=storePurchase]").requestSubmit()')
    evaluate("AL.Core.selected(AL.game).substrate.type==='caribbean'&&AL.Core.selected(AL.game).substrate.depth===3.2",'Sand type and chosen depth are installed and saved')
    choose(sub='flora');client.evaluate('AL.Store.details("flora:zoa");document.querySelector("[data-form=storePurchase]").requestSubmit()')
    evaluate('AL.UI.placing&&!AL.Store.opened','Coral purchase hands off to actual placement without spending first')
    reef_money=client.evaluate('AL.game.credits')
    client.evaluate("(()=>{const c=document.getElementById('aquarium'),r=c.getBoundingClientRect();c.dispatchEvent(new MouseEvent('click',{clientX:r.left+r.width*.5,clientY:r.top+r.height*.45,bubbles:true}));})()")
    evaluate(f'AL.game.credits==={reef_money}&&AL.Core.selected(AL.game).flora.length===0&&AL.UI.placing','Unsupported open-water coral placement rejected without charging')
    client.evaluate("(()=>{const c=document.getElementById('aquarium'),r=c.getBoundingClientRect(),y=AL.Habitat.bed(AL.Core.selected(AL.game));c.dispatchEvent(new MouseEvent('click',{clientX:r.left+r.width*.62,clientY:r.top+r.height*y,bubbles:true}));})()")
    evaluate("!AL.UI.placing&&AL.Core.selected(AL.game).flora.length===1&&AL.Core.selected(AL.game).flora[0].attachment.surface==='sand'",'Suitable stable sandbed placement succeeds with persistent attachment')
    client.evaluate("AL.UI.inspectFlora(AL.Core.selected(AL.game).flora[0].id)")
    evaluate("document.getElementById('flora-tab-overview')&&document.getElementById('flora-tab-care')&&document.getElementById('flora-info-panel').textContent.includes('Health')",'Coral remains a living organism with Overview and Care inspection tabs')
    client.evaluate("document.getElementById('flora-tab-care').click()")
    evaluate("document.getElementById('flora-tab-care').getAttribute('aria-selected')==='true'&&document.getElementById('flora-info-panel').textContent.toLowerCase().includes('light')",'Coral Care tab exposes living light and water requirements')
    client.evaluate("AL.Startup?.finish();AL.UI.close();AL.UI.inspectFish(AL.Core.selected(AL.game).fish[0].id)")
    evaluate("document.getElementById('dialog').textContent.includes('Ocellaris')",'Existing assigned Ocellaris resident remains inspectable')
    client.evaluate("AL.Startup?.finish();AL.UI.close();AL.game.time=720;AL.game=AL.Core.act(AL.game,'setLighting',{mode:'on'});AL.renderer.draw(AL.game,0);window.LAMP_ON=Array.from(AL.renderer.scene.getContext('2d').getImageData(0,0,480,240).data).filter((v,i)=>i%4<3).reduce((a,b)=>a+b,0);AL.game=AL.Core.act(AL.game,'setLighting',{mode:'off'});AL.renderer.draw(AL.game,0);window.LAMP_OFF=Array.from(AL.renderer.scene.getContext('2d').getImageData(0,0,480,240).data).filter((v,i)=>i%4<3).reduce((a,b)=>a+b,0)")
    evaluate("LAMP_ON>LAMP_OFF*1.5",'Aquarium light visibly brightens the complete tank view')
    client.evaluate("AL.game=AL.Core.act(AL.game,'setLighting',{mode:'auto'})")
    for page in ['aquariums','collection','equipment','food','flora','breeding','quests','marketplace','achievements','vip','settings','water']:
        client.evaluate(f"AL.UI.goto('{page}')")
        evaluate("((AL.Shell.opened&&document.getElementById('primary-content').textContent.length>20)||(AL.Store.opened&&document.getElementById('store-products').textContent.length>20))&&AL.game.selectedTank===STORE_FIXTURE.reef",f'{page}: moved management modal renders and preserves selected aquarium')
    client.evaluate("AL.UI.goto('aquariums')")
    # Core-level mounting and atomic rollback checks use real current data.
    mounting=client.evaluate("""(()=>{
      let s=JSON.parse(JSON.stringify(AL.game)),t=AL.Core.selected(s),results=[];const assert=(ok,name)=>results.push({pass:!!ok,name});
      function reject(action,args){const before=JSON.stringify(s);try{AL.Core.act(s,action,args);return false;}catch{return JSON.stringify(s)===before;}}
      assert(reject('buyFlora',{type:'sps',x:.5,y:.4}),'Core rejects open-water placement atomically');
      let point=null;for(let x=.06;x<.94&&!point;x+=.003)for(let y=.2;y<.9;y+=.008){const r=AL.Habitat.placement(s,t,'sps',x,y);if(r.ok&&r.position.attachment.surface==='rock'){point=r.position;break;}}
      assert(!!point,'A real existing rock surface is detected');
      if(point){s=AL.Core.act(s,'buyFlora',{type:'sps',x:point.x,y:point.y});t=AL.Core.selected(s);const coral=t.flora.at(-1),rock=t.hardscape.find(r=>r.id===coral.attachment.supportId),oldX=coral.x;
        assert(reject('removeRock',{id:rock.id}),'Supporting rock removal blocked while coral attached');
        s=AL.Core.act(s,'moveRock',{id:rock.id,x:rock.x+.01});t=AL.Core.selected(s);assert(Math.abs(t.flora.at(-1).x-oldX-.01)<.000001,'Moving rock carries attached coral local position');
        assert(reject('reposition',{id:coral.id,x:.5,y:.4}),'Existing colony cannot be moved into open water');
      }
      s=AL.Core.act(s,'buyRack',{glass:'back'});t=AL.Core.selected(s);const rack=t.mounts.at(-1);
      s=AL.Core.act(s,'buyFlora',{type:'mushroom',x:rack.x,y:rack.y});t=AL.Core.selected(s);assert(t.flora.at(-1).attachment.surface==='rack','Supported back-glass frag rack accepts a colony');
      assert(reject('removeRack',{id:rack.id}),'Occupied rack cannot be removed');
      assert(reject('buySand',{type:'fiji',depth:0}),'Removing sand cannot strand sandbed coral');
      assert(reject('buyFlora',{type:'zoa',x:t.flora[0].x,y:t.flora[0].y}),'Overlapping coral mounting footprints are rejected');
      const raw=JSON.stringify(s),loaded=AL.Save.parse(raw);assert(JSON.stringify(loaded)===raw&&loaded.selectedTank===s.selectedTank,'Mounted colonies and selected destination round-trip without changes');
      const legacy=JSON.parse(raw);delete legacy.tanks.find(n=>n.id===legacy.selectedTank).flora[0].attachment;legacy.tanks.find(n=>n.id===legacy.selectedTank).flora[0].x=.5;legacy.tanks.find(n=>n.id===legacy.selectedTank).flora[0].y=.4;
      const restored=AL.Save.parse(JSON.stringify(legacy));assert(restored.tanks.find(n=>n.id===restored.selectedTank).flora[0].relocationRequired===true,'Unsupported legacy coral is preserved with relocation flag');
      const eggState=AL.Core.newGame('marine'),eggTank=eggState.tanks[0];eggState.credits=100000;eggTank.volume=300;eggTank.prepared=true;eggTank.bacteria=eggTank.bacteria2=1;eggTank.fish.push(AL.Core.fish(eggState,'clown'),AL.Core.fish(eggState,'clown'));
      assert(!AL.StoreRules.report(eggState,eggTank,'buyEgg',{species:'clown'}).ok,'Purchased clownfish egg cannot exceed the established pair territory');
      eggTank.fish=[];AL.Sim.makeBrood(eggState,eggTank,'clown',null,null,true);assert(!AL.StoreRules.report(eggState,eggTank,'buyFish',{species:'amphiprion-percula',count:1}).ok,'Reserved clownfish eggs prevent unsafe mixed-species future stocking');
      const freshState=AL.Core.newGame('fresh'),freshTank=freshState.tanks[0];freshTank.prepared=true;freshTank.bacteria=freshTank.bacteria2=1;
      assert(!AL.StoreRules.report(freshState,freshTank,'buyEgg',{species:'danio'}).ok,'A purchased single egg cannot bypass freshwater social-school purchase safeguards');
      return results;
    })()""")
    results.extend(mounting)
    client.evaluate("AL.UI.save();document.getElementById('store-quick').click()")
    for width in [1440,1024,760,390]:
        client.call('Emulation.setDeviceMetricsOverride',{'width':width,'height':950,'deviceScaleFactor':1,'mobile':False})
        evaluate("document.documentElement.scrollWidth<=innerWidth&&document.getElementById('store-dialog').getBoundingClientRect().bottom<=innerHeight&&document.getElementById('store-close').getBoundingClientRect().top>=0",f'Store fits {width}px and X stays visible')
    shot('mobile')
    evaluate("getComputedStyle(document.getElementById('store-products')).overflowY==='auto'&&getComputedStyle(document.body).overflow==='hidden'",'Product scroll is inside modal while page remains fixed')
    client.call('Page.reload');time.sleep(.4)
    evaluate("AL.game.selectedTank===STORE_FIXTURE?.reef" if client.evaluate('!!window.STORE_FIXTURE') else "AL.Core.selected(AL.game).name==='The reef destination'",'Reload restores the saved aquarium destination')
    client.evaluate("document.getElementById('store-quick').click()")
    evaluate("document.getElementById('store-destination-name').textContent==='The reef destination'",'Reopened store displays saved destination')
    protected=json.loads((root/'tests/freshwater-protection-baseline.json').read_text())
    unchanged=all(hashlib.sha256((root/p).read_bytes()).hexdigest()==digest for p,digest in protected.items() if p!='js/simulation.js')
    results.append(check(unchanged,'Freshwater definition file and all 144 protected art/source files are byte-identical'))
    old=(root/'tests/freshwater-protected-simulation.js').read_text(encoding='utf-8')
    current=(root/'js/simulation.js').read_text(encoding='utf-8')
    # Restore only the expressly marine health hooks before comparing protected biology bytes.
    replacements=[("const untilMidnight=1440-s.time%1440;if(AL.Gameplay&&minutes>untilMidnight){step(s,untilMidnight);return step(s,minutes-untilMidnight);}",""),
      ("AL.Gameplay?.observe(s,minutes);",""),("AL.Gameplay?.step(s,previous,minutes);",""),
      ("aquariumId:t.id,",""),
      ("AL.Gameplay?.setOffline(s,true);try{advance(s,hours*60);}finally{AL.Gameplay?.setOffline(s,false);}","advance(s,hours*60);"),("if(f.disease&&(d.water==='fresh'||!AL.Health))damage+=0.7;","if(f.disease)damage+=0.7;"),
      ("if((d.water==='fresh'||!AL.Health)&&f.stress>45&&!f.disease&&K.random(s)","if(f.stress>45&&!f.disease&&K.random(s)"),
      ("AL.Health?.fed(f,D.foods[p.type].quality);", ""),
      ("if(t.water==='marine')AL.BroodView?.initialize(t,t.eggs.at(-1));", ""),
      ("AL.Health?.step(s,t,h);", ""), ("AL.Valuation?.record(s,t);", ""),
      ("AL.LivestockMarket?.rotate(s);", ""),
      ("if(d.water==='marine'&&parents.some(f=>f.healthState?.treatment||f.healthState?.conditions.some(c=>c.severity>.15)))return {ok:false,reason:'Resolve illness and treatment before breeding.'};", "")]
    failed="e.done=true;t.waterParams.organic+=0.1;K.log(s,`${d.name} brood failed under unsuitable conditions.`,'warning');"
    current=current.replace("if(t.water==='marine'&&AL.BroodView?.failed(s,t,e))continue;","").replace("if(t.water==='marine'&&AL.BroodView?.failed(s,t,e)){}else{"+failed+"}",failed)
    for added,protected_text in replacements:current=current.replace(added,protected_text)
    original="const clown=K.alive(t).filter(f=>f.species==='clown');if(clown.length===2&&clown[0].sex===clown[1].sex){clown.sort((a,b)=>b.adultSize-a.adultSize);clown[0].sex='F';clown[1].sex='M';}"
    start=current.index('// Marine-only clownfish pairing:');end=current.index('// End marine-only clownfish pairing.')+len('// End marine-only clownfish pairing.')
    results.append(check(current[:start]+original+current[end:]==old,'Freshwater biology bytes preserved after removing marine hooks and authorized shared calendar / brood identity hooks'))
    errors=[e for e in client.events if e.get('method')=='Runtime.exceptionThrown']
    network=[e['params']['request']['url'] for e in client.events if e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('http:','https:'))]
    results.append(check(not errors,'No JavaScript exceptions'))
    results.append(check(not network,'No HTTP/HTTPS requests during offline shopping'))
    failed=[r for r in results if not r['pass']]
    output={'browser':name,'passed':len(results)-len(failed),'failed':len(failed),'checks':results,'errors':errors,'networkRequests':network}
    (root/'tests'/f'{name}-store-results.json').write_text(json.dumps(output,indent=2))
    print(json.dumps({k:output[k] for k in ['browser','passed','failed']}),flush=True)
    for r in failed:print('FAIL:',r['name'],flush=True)
    return 1 if failed else 0
