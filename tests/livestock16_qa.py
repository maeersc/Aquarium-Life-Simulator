"""Dedicated, offline livestock animation QA. Uses only disposable QA profiles."""
import base64
import hashlib
import json
import time


def run(c, root, name, audit=False):
    out = root / 'tests/livestock16-evidence'
    out.mkdir(exist_ok=True)
    c.navigate(root / 'index.html')
    for _ in range(500):
        if c.evaluate('!!window.AL?.game && AL.ExpansionArt?.loaded===73 && AL.ClownArt?.loaded===AL.ClownArt?.records.length && AL.AssetBank?.loaded===AL.AssetBank?.records.length'):
            break
        time.sleep(.05)
    c.evaluate('localStorage.clear(); AL.Startup.finish(); AL.game.settings.speed=0')
    c.call('Emulation.setDeviceMetricsOverride', {'width':1600,'height':900,'deviceScaleFactor':1,'mobile':False})
    if audit:
        rows = c.evaluate("""(()=>{
          const clean=m=>m?Object.fromEntries(Object.entries(m).filter(([k])=>k!=='src')):null;
          return [['fish',AL.Data.species],['coral',AL.Data.flora],['invertebrate',AL.Data.invertebrates]].flatMap(([category,table])=>Object.entries(table).filter(([id,d])=>d.water==='marine'||category==='invertebrate').map(([id,definition])=>{const d={...definition,id};
            const meta=AL.ExpansionArt.metadata(d.id)||(category==='fish'?(AL.ClownArt.metadata(d.id)||AL.LifeStages.metadata(d.id)):AL.AssetBank.metadata('corals',d.id));
            return {id:d.id,name:d.name,scientificName:d.scientificName||null,category,shape:d.shape,water:d.water||'marine',purchaseVerified:d.purchaseVerified,acquisitionHold:d.acquisitionHold||null,fictional:!!d.fictional,meta:clean(meta),adultFrames:category==='fish'?(d.id==='clown'?4:AL.ClownArt.metadata(d.id)?.swim?.length||1):1,
              varieties:category==='fish'?Object.values(AL.Clownfish.varieties).filter(v=>v.speciesId===d.id).map(v=>({id:v.id,name:v.name,meta:clean(AL.ClownArt.metadata(d.id,v.id))})):[]};
          }));})()""")
        (out/'catalog-before.json').write_text(json.dumps(rows,indent=2),encoding='utf8')
        print(json.dumps({'entries':len(rows),'categories':{k:sum(r['category']==k for r in rows) for k in ['fish','coral','invertebrate']},'varieties':sum(len(r['varieties']) for r in rows)}),flush=True)
        return 0
    report = c.evaluate((root/'tests/livestock16_checks.js').read_text(encoding='utf8'))
    checks = report['checks']
    def ck(label, expression):
        try:
            checks.append({'name':label,'pass':bool(c.evaluate(expression))})
        except Exception as e:
            checks.append({'name':label,'pass':False,'error':str(e)})
    previous=c.evaluate((root/'tests/fish_animation_checks.js').read_text(encoding='utf8'))
    report['previousFishSuite']={'passed':previous['passed'],'failed':previous['failed']}
    checks.extend(previous['checks'])
    c.evaluate("""window.livestock16Fixture=(count=30)=>{const s=AL.Core.newGame('marine',1616),t=s.tanks[0],ids=Object.keys(AL.FishAnimation.data.species);s.settings.speed=0;s.update29.tutorial.status='skipped';t.volume=56781.17676;t.prepared=true;t.emptyDry=false;t.bacteria=t.bacteria2=1;t.fish=[];for(let i=0;i<count;i++){const f=AL.Core.fish(s,ids[i%ids.length]);f.growth=1;f.x=.12+i%5*.18;f.y=.25+Math.floor(i/5)%3*.22;f.vx=f.vy=0;t.fish.push(f)}return s};window.livestock16Renderer=()=>{const c=document.createElement('canvas');c.width=960;c.height=480;return new AL.Renderer(c)};""")
    ck('Every94-fish renderer record remains presentation-only',"(()=>{const s=livestock16Fixture(94),r=livestock16Renderer(),before=JSON.stringify(s);for(let i=0;i<20;i++)r.draw(s,.05);return before===JSON.stringify(s)&&r.positions.size===94})()")
    ck('Every fish remains selectable by its own ID',"(()=>{for(const id of Object.keys(AL.FishAnimation.data.species)){const s=livestock16Fixture(1),f=s.tanks[0].fish[0],r=livestock16Renderer();f.species=id;f.x=f.y=.5;r.draw(s,.05);if(r.hit(.5,.5)!==f.id)return false}return true})()")
    ck('All15 real coral draw paths invoke the shared appropriate sheet slot',"(()=>{const draw=AL.FishAnimation.drawResident,c=document.createElement('canvas'),seen=[];c.width=c.height=200;AL.FishAnimation.drawResident=(...args)=>{seen.push(args.slice(1,4));return false};try{for(const [id,d]of Object.entries(AL.Data.flora).filter(([id,d])=>d.water==='marine'))AL.Art.plant(c.getContext('2d'),id,100,150,1,2,1,1);return seen.length===15&&seen.every(x=>x[1]==='frag'&&x[2]==='polyp_motion')}finally{AL.FishAnimation.drawResident=draw}})()")
    ck('All10 invertebrates use their real renderer hook without mutating specimen state',"(()=>{const s=livestock16Fixture(1),t=s.tanks[0],r=livestock16Renderer();t.invertebrates=Object.keys(AL.Data.invertebrates).map(id=>AL.Invertebrates.make(s,t,id));const before=JSON.stringify(s),draw=AL.FishAnimation.drawResident,seen=[];AL.FishAnimation.drawResident=(...args)=>{seen.push(args.slice(1,4));return false};try{AL.ExpansionUI.draw(r,t);return before===JSON.stringify(s)&&seen.length===10&&seen.every(x=>x[1]==='adult'&&x[2]==='idle')&&r.hitboxes.filter(b=>b.kind==='invertebrate').length===10}finally{AL.FishAnimation.drawResident=draw}})()")
    ck('Conch sand-forage state selects walking, never a fish swim slot',"(()=>{const s=livestock16Fixture(1),t=s.tanks[0],r=livestock16Renderer(),f=AL.Invertebrates.make(s,t,'tiger-sand-conch');f.behavior='Sand forage';t.invertebrates=[f];const draw=AL.FishAnimation.drawResident,seen=[];AL.FishAnimation.drawResident=(...args)=>{seen.push(args[3]);return false};try{AL.ExpansionUI.draw(r,t);return seen.length===1&&seen[0]==='walk'}finally{AL.FishAnimation.drawResident=draw}})()")
    ck('Save migration preserves all94 fish identities and patterns',"(()=>{const s=livestock16Fixture(94),before=JSON.stringify(s.tanks[0].fish);return JSON.stringify(AL.Save.parse(JSON.stringify(s)).tanks[0].fish)===before})()")
    ck('Different render rates cannot alter health, chemistry, RNG or AC',"(()=>{const a=livestock16Fixture(10),b=structuredClone(a),slow=livestock16Renderer(),fast=livestock16Renderer();for(let i=0;i<20;i++)slow.draw(a,.1);for(let i=0;i<240;i++)fast.draw(b,1/120);if(JSON.stringify(a)!==JSON.stringify(b))return false;const now=Date.now,wall=now();try{Date.now=()=>wall;AL.Sim.advance(a,1440);AL.Sim.advance(b,1440)}finally{Date.now=now}return JSON.stringify(a)===JSON.stringify(b)})()")
    c.evaluate("""window.livestock16Perf=[];for(const count of [10,30,94]){const s=livestock16Fixture(count),r=livestock16Renderer();for(let i=0;i<50;i++)r.draw(s,1/60);const start=performance.now();for(let i=0;i<120;i++)r.draw(s,1/60);livestock16Perf.push({fish:count,meanMilliseconds:(performance.now()-start)/120,cache:AL.FishAnimation.metrics})}""")
    report['performance']=c.evaluate('livestock16Perf')
    ck('Thirty-fish render remains under33ms on this QA PC','livestock16Perf[1].meanMilliseconds<33')
    ck('Ninety-four-fish stress render remains under50ms','livestock16Perf[2].meanMilliseconds<50')
    c.evaluate("""(()=>{const s=livestock16Fixture(94),t=s.tanks[0],r=livestock16Renderer();t.invertebrates=Object.keys(AL.Data.invertebrates).map(id=>AL.Invertebrates.make(s,t,id));t.flora=Object.entries(AL.Data.flora).filter(([id,d])=>d.water==='marine').map(([id,d],i)=>({id:'qa-coral-'+i,type:id,hp:100,size:1,x:.08+i%5*.2,y:.85,z:.5}));const before=JSON.stringify(s);for(let i=0;i<50;i++)r.draw(s,1/60);const start=performance.now();for(let i=0;i<120;i++)r.draw(s,1/60);window.livestock16Mixed={residents:119,meanMilliseconds:(performance.now()-start)/120,unchanged:before===JSON.stringify(s),coralHitboxes:r.hitboxes.filter(b=>b.kind==='flora').length,invertHitboxes:r.hitboxes.filter(b=>b.kind==='invertebrate').length};})()""")
    report['mixedPerformance']=c.evaluate('livestock16Mixed')
    ck('All119 mixed resident stress render is read-only and under50ms','livestock16Mixed.unchanged&&livestock16Mixed.meanMilliseconds<50&&livestock16Mixed.coralHitboxes===15&&livestock16Mixed.invertHitboxes===10')
    # Actual click and timer, rather than calling the inspector directly.
    c.evaluate('AL.Store.close(false);AL.Shell.close(false);AL.UI.close();AL.game=livestock16Fixture(10);AL.UI.render();AL.renderer.positions.clear();AL.renderer.draw(AL.game,.05);AL.renderer.canvas.scrollIntoView({block:"center"})')
    point=c.evaluate("(()=>{const id=AL.game.tanks[0].fish[0].id,b=AL.renderer.hitboxes.find(b=>b.id===id),r=AL.renderer.canvas.getBoundingClientRect();return{id,x:r.left+b.x*r.width,y:r.top+b.y*r.height}})()")
    for kind in ['mousePressed','mouseReleased']:
        c.call('Input.dispatchMouseEvent',{'type':kind,'button':'left','clickCount':1,'x':point['x'],'y':point['y']})
    ck('Actual moving-fish canvas click opens correct inspector','AL.renderer.selected==='+json.dumps(point['id'])+"&&document.getElementById('dialog').open")
    time.sleep(3.25)
    ck('Selection outline expires after3 seconds while inspector stays open',"AL.renderer.selected===null&&document.getElementById('dialog').open")
    ck('Freshwater purchasing remains locked',"(()=>{try{AL.Core.act(AL.game,'buyTank',{water:'fresh',size:0});return false}catch{return true}})()")
    # Full current-source freshwater output differential against the original.
    old=(root/'planning/fish-animation/baseline/js__render.js').read_text(encoding='utf8')
    ck('Protected freshwater drawing with all11 fish remains pixel-identical to original engine',"(()=>{const original=AL.Art,Modern=AL.Renderer;"+old.replace('AL.Renderer = class','const Legacy = class')+";const legacyArt=AL.Art;AL.Art=original;const s=AL.Core.newGame('fresh',16);s.tanks[0].prepared=true;s.tanks[0].emptyDry=false;s.tanks[0].fish=Object.values(AL.Data.species).filter(d=>d.water==='fresh').map((d,i)=>{const f=AL.Core.fish(s,d.id);f.x=.1+i%5*.18;f.y=.25+Math.floor(i/5)*.25;return f});const canvas=()=>{const c=document.createElement('canvas');c.width=960;c.height=480;return c},a=new Modern(canvas()),b=new Legacy(canvas());a.draw(s,.05);AL.Art=legacyArt;b.draw(s,.05);AL.Art=original;const aa=a.g.getImageData(0,0,480,240).data,bb=b.g.getImageData(0,0,480,240).data;return aa.every((n,i)=>n===bb[i])})()")
    # Snapshot at the first instruction of the new document, after the game's
    # departing autosave. This distinguishes gallery access from save-on-exit.
    guard=c.call('Page.addScriptToEvaluateOnNewDocument',{'source':"window.galleryStorageCalls=[];window.galleryStorageBefore=JSON.stringify(localStorage);for(const method of ['getItem','setItem','removeItem','clear']){const original=Storage.prototype[method];Storage.prototype[method]=function(...args){galleryStorageCalls.push(method);return original.apply(this,args)}}"})['identifier']
    c.navigate(root/'livestock-animation-review.html')
    for _ in range(300):
        if c.evaluate('!!window.LivestockGallery'):break
        time.sleep(.05)
    ck('Offline gallery lists all119 entries','document.getElementById("gallery-species").options.length===119')
    ck('Every entry/stage/state can be reviewed without missing source exceptions',"""(()=>{
      const $=id=>document.getElementById(id);$('gallery-play').click();
      for(const o of $('gallery-species').options){
        $('gallery-species').value=o.value;$('gallery-species').dispatchEvent(new Event('change'));
        for(const stage of $('gallery-stage').options){
          $('gallery-stage').value=stage.value;$('gallery-stage').dispatchEvent(new Event('change'));
          for(const state of $('gallery-state').options){
            $('gallery-state').value=state.value;$('gallery-state').dispatchEvent(new Event('input'));
          }
        }
      }return true;
    })()""")
    ck('Missing authored sheet has an explicit message, no fake16-pose image',"document.getElementById('gallery-sheet').hidden&&document.getElementById('gallery-frame').disabled&&document.getElementById('gallery-sheet-message').textContent.includes('No completed')")
    ck('Gallery never reads or writes player saves','JSON.stringify(localStorage)===galleryStorageBefore&&galleryStorageCalls.length===0')
    c.call('Page.removeScriptToEvaluateOnNewDocument',{'identifier':guard})
    c.evaluate("document.getElementById('gallery-species').value='clown';document.getElementById('gallery-species').dispatchEvent(new Event('change'));document.getElementById('gallery-speed').value='.2';document.getElementById('gallery-speed').dispatchEvent(new Event('input'))")
    ck('Slow playback control is available offline',"document.getElementById('gallery-speed-label').textContent==='0.2×'")
    (out/f'{name}-gallery.png').write_bytes(base64.b64decode(c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
    checks.append({'name':'No uncaught browser exceptions','pass':not [e for e in c.events if e.get('method')=='Runtime.exceptionThrown']})
    checks.append({'name':'No network asset/save requests','pass':not [e for e in c.events if e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('http:','https:'))]})
    report['passed'] = sum(x['pass'] for x in checks)
    report['failed'] = sum(not x['pass'] for x in checks)
    (out/f'{name}-results.json').write_text(json.dumps(report,indent=2),encoding='utf8')
    print(json.dumps({'passed':report['passed'],'failed':report['failed'],'failures':[x for x in checks if not x['pass']]}),flush=True)
    return int(report['failed']>0)
