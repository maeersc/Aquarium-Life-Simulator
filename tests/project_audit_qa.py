"""Audit-only observations and boundary reproductions; never edits game source or user saves."""
import base64,json,time

def run(client,root,name):
    out=root/'tests/audit-evidence';out.mkdir(exist_ok=True)
    client.call('Emulation.setDeviceMetricsOverride',{'width':1440,'height':1100,'deviceScaleFactor':1,'mobile':False})
    client.call('Performance.enable')
    client.navigate(root/'index.html')
    for _ in range(150):
        if client.evaluate('!!window.AL?.game&&!!AL.renderer'):break
        time.sleep(.05)
    client.evaluate("AL.UI.close();AL.Store.close(false);AL.game=AL.Core.newGame('marine');AL.game.settings.speed=0;AL.UI.goto('aquariums')")
    startup={'protocol':client.evaluate('location.protocol'),'stylesheets':client.evaluate('document.styleSheets.length'),'errors':[e for e in client.events if e.get('method')=='Runtime.exceptionThrown']}
    def shot(label):
        r=client.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False});(out/f'{name}-{label}.png').write_bytes(base64.b64decode(r['data']))
    shot('new-installation')
    client.evaluate((root/'tests/project_audit_probes.js').read_text(encoding='utf-8'))
    probes=client.evaluate('runProjectAudit()')
    life=client.evaluate((root/'tests/life_stage_checks.js').read_text(encoding='utf-8'))
    # Exercise the real store quantity event path, which earlier tests kept at defaults.
    client.evaluate("(()=>{const s=AL.Core.newGame('marine');s.settings.speed=0;s.credits=100000;s.xp=2000;s.level=11;s.time=720;const t=s.tanks[0];t.volume=300;t.prepared=true;t.bacteria=t.bacteria2=1;AL.game=s;AL.UI.goto('aquariums');AL.Store.open('fish','saltwater');AL.Store.details('fish:clown');})()")
    before=len(client.events)
    client.evaluate("document.getElementById('purchase-count').value=2;document.getElementById('purchase-count').dispatchEvent(new Event('input',{bubbles:true}))")
    client.call('Runtime.evaluate',{'expression':'0'})
    quantity_errors=[e['params'] for e in client.events[before:] if e.get('method')=='Runtime.exceptionThrown']
    probes.append({'id':'R32','name':'Store quantity input does not throw a JavaScript exception','pass':not quantity_errors,'actual':{'errors':quantity_errors,'confirmDisabled':client.evaluate("document.getElementById('confirm-fish').disabled"),'report':client.evaluate("document.getElementById('compatibility-report').textContent")}})
    shot('quantity-input')
    client.evaluate("AL.UI.close();AL.Store.close(false);AL.UI.goto('collection')")
    for _ in range(100):
        if client.evaluate("Array.from(document.querySelectorAll('#management img'),i=>i.complete&&i.naturalWidth>0).every(Boolean)"):break
        time.sleep(.02)
    probes.append({'id':'R33','name':'All actual collection thumbnails load','pass':client.evaluate("Array.from(document.querySelectorAll('#management img'),i=>i.complete&&i.naturalWidth>0).every(Boolean)"),'actual':{'images':client.evaluate("document.querySelectorAll('#management img').length")}})
    shot('current-catalog')
    # Main-bank diagnostic contact pages include every implemented fish at gameplay scale.
    client.evaluate("""window.auditContact=page=>{const ids=Object.keys(AL.Data.species).slice(page*7,page*7+7);let c=document.getElementById('audit-contact');if(!c){c=document.createElement('canvas');c.id='audit-contact';document.body.append(c);}c.width=1200;c.height=80+ids.length*124;const g=c.getContext('2d');g.fillStyle='#121a27';g.fillRect(0,0,c.width,c.height);g.font='14px Segoe UI';g.fillStyle='#e3e8ee';g.fillText('Actual rendering banks: early stages, authored death, gameplay scale and eye metadata',20,26);const columns=[['baby','alive',1],['juvenile','alive',1],['adult','alive',1],['adult','alive',-1],['adult','dead',1]];for(const [i,id]of ids.entries()){const y=80+i*124;g.fillStyle='#e3e8ee';g.fillText(AL.Data.species[id].name,12,y+10);g.fillStyle='#91b5d3';g.fillText(id,12,y+32);for(const [col,[stage,state,face]]of columns.entries()){const f=id==='clown'&&stage==='adult'&&state==='alive'?AL.Art.sprite(id):AL.ClownArt.frame(id,null,stage,state,0,1,false)||AL.LifeStages.frame(id,stage,state);const width=stage==='adult'?84:stage==='juvenile'?60:35,height=Math.round(width*f.height/f.width),x=330+col*175;AL.SpriteKit.draw(g,f,x,y+30,width,height,face,false);g.fillStyle='#b9c9d9';g.fillText(stage+' '+state+(face<0?' left':''),x-60,y+87);const raster=AL.SpriteKit.raster(f,width,height),e=raster.eyeBounds;if(e){g.strokeStyle='#f4b860';g.strokeRect(x-Math.floor(width/2)+(face<0?width-e.x-e.w:e.x),y+30-Math.floor(height/2)+e.y,e.w,e.h);}}}return c.toDataURL().split(',')[1];};""")
    for page in range(8):
        png=client.evaluate(f'auditContact({page})');(out/f'{name}-fish-contact-{page+1}.png').write_bytes(base64.b64decode(png))
    # Visibility/backdrop/focus checks use the actual dialog, not a mock DOM.
    client.evaluate("document.getElementById('audit-contact').remove();AL.UI.goto('aquariums');AL.Store.open('fish','saltwater')")
    client.call('Input.dispatchKeyEvent',{'type':'keyDown','key':'Tab','code':'Tab','windowsVirtualKeyCode':9})
    client.call('Input.dispatchKeyEvent',{'type':'keyUp','key':'Tab','code':'Tab','windowsVirtualKeyCode':9})
    probes.append({'id':'R34','name':'Native store modal retains keyboard focus','pass':client.evaluate("document.activeElement.closest('#store-dialog')!==null"),'actual':client.evaluate('document.activeElement.outerHTML')})
    selected=client.evaluate('AL.game.selectedTank');client.call('Input.dispatchMouseEvent',{'type':'mousePressed','x':5,'y':5,'button':'left','clickCount':1});client.call('Input.dispatchMouseEvent',{'type':'mouseReleased','x':5,'y':5,'button':'left','clickCount':1})
    probes.append({'id':'R35','name':'Backdrop click does not change the aquarium or dismiss store','pass':client.evaluate('AL.Store.opened&&AL.game.selectedTank==='+json.dumps(selected))})
    client.evaluate('AL.Store.close(false)')
    perf=client.evaluate("""(()=>{const s=AL.Core.newGame('marine',224),t=s.tanks[0];s.settings.speed=1;t.volume=5000;t.prepared=true;t.bacteria=t.bacteria2=1;s.time=720;const ids=Object.keys(AL.Data.species).filter(id=>AL.Data.species[id].water==='marine');for(let i=0;i<250;i++)t.fish.push(AL.Core.fish(s,ids[i%ids.length]));const c=document.createElement('canvas');c.width=960;c.height=480;const r=new AL.Renderer(c);r.draw(s,.016);const costs=[];for(let i=0;i<120;i++){const start=performance.now();r.draw(s,1/60);costs.push(performance.now()-start);}costs.sort((a,b)=>a-b);const start=performance.now();for(let i=0;i<12;i++){const n=JSON.parse(JSON.stringify(t));n.id=AL.Core.id(s,'tank');for(const f of n.fish)f.id=AL.Core.id(s,'fish');if(i)s.tanks.push(n);}const simStart=performance.now();for(let i=0;i<20;i++)AL.Sim.step(s);return {fixture:'Synthetic workload; not a valid mixed-species husbandry recommendation',fishRendered:250,frames:120,meanFrameMs:costs.reduce((a,b)=>a+b,0)/costs.length,p95FrameMs:costs[Math.floor(costs.length*.95)],maxFrameMs:costs.at(-1),simulatedFish:s.tanks.reduce((n,t)=>n+t.fish.length,0),twentyStepsMs:performance.now()-simStart,constructionMs:simStart-start};})()""")
    metrics={e['name']:e['value'] for e in client.call('Performance.getMetrics').get('metrics',[]) if e['name'] in ['JSHeapUsedSize','JSHeapTotalSize','Nodes','Documents','TaskDuration']}
    client.evaluate('AL.UI.goto("vip")');vip=client.evaluate("document.getElementById('management').textContent");shot('vip-preview')
    http=[e['params']['request']['url'] for e in client.events if e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('http:','https:'))]
    output={'browser':name,'startup':startup,'probes':probes,'lifeAssetChecks':life,'performance':perf,'performanceMetrics':metrics,'vipText':vip,'networkRequests':http,'scope':'Read-only audit of game code; runtime changes stay inside an isolated test browser profile.'}
    (out/f'{name}-project-audit.json').write_text(json.dumps(output,indent=2),encoding='utf-8')
    print(json.dumps({'browser':name,'probes':len(probes),'reproducedDefects':[p['id'] for p in probes if not p['pass']],'lifeAssetFailures':[p['name'] for p in life['results'] if not p['pass']],'performance':perf,'HTTP':len(http)}),flush=True)
    return 0
