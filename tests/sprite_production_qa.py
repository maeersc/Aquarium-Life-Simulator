"""Isolated production source capture and authored-sheet gameplay checks."""
import base64
import json
import time
import sys


def resident_fixtures(c,root,name):
    """Validate biological save/placement fixtures, never infer art completion."""
    c.sock.settimeout(60);c.navigate(root/'index.html',timeout=60)
    for _ in range(400):
        if c.evaluate('!!window.AL?.game&&!!AL.FishAnimation'):break
        time.sleep(.05)
    else:raise RuntimeError('Resident fixture game did not initialize')
    c.evaluate('localStorage.clear();AL.Startup.finish();AL.game.settings.speed=0')
    c.evaluate((root/'tests/resident_sprite_checks.js').read_text(encoding='utf8'))
    checks=c.evaluate("""(()=>{const checks=[],check=(name,pass)=>checks.push({name,pass:!!pass});
      for(const e of AL.FishAnimation.catalog.entries.filter(e=>e.productionEligible&&e.category!=='fish'))for(const stage of e.stages){
        try{SpriteResidentQA.saveAndClick(e,stage,e.requiredStates[0],check);}catch(error){checks.push({name:e.id+'/'+stage+': non-fish fixture initializes',pass:false,error:error.stack||String(error)});}
      }return checks;})()""")
    report={'browser':name,'scope':'Non-fish fixture validity only; no authored artwork completion inferred','passed':sum(x['pass'] for x in checks),'failed':sum(not x['pass'] for x in checks),'checks':checks}
    out=root/'tests/sprite-production-evidence';out.mkdir(exist_ok=True)
    (out/(name+'-resident-fixtures.json')).write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
    print(json.dumps({k:v for k,v in report.items() if k!='checks'}|{'failures':[r for r in checks if not r['pass']]}),flush=True)
    return int(report['failed']>0)


def run(c,root,name,references=False):
    out=root/'tests/sprite-production-evidence';out.mkdir(exist_ok=True)
    c.call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':900,'deviceScaleFactor':1,'mobile':False})
    # The complete offline embedded banks are large. Keep real initialization
    # mandatory, allow a bounded cold parse, and record its measured duration.
    c.sock.settimeout(60)
    started=time.monotonic();c.navigate(root/('DIST/livestock-animation-review.html' if '--dist' in sys.argv else 'livestock-animation-review.html'),timeout=60)
    for _ in range(400):
        if c.evaluate('!!window.LivestockGallery'):break
        time.sleep(.05)
    else:raise RuntimeError('Offline sprite gallery did not initialize')
    gallery_load_seconds=time.monotonic()-started
    if not references:
        gallery=c.evaluate("""(async()=>{const A=AL.FishAnimation,checks=[],check=(name,pass)=>checks.push({name,pass:!!pass}),control=(id,value,event='input')=>{const el=document.getElementById(id);el.value=value;el.dispatchEvent(new Event(event,{bubbles:true}));};
          document.getElementById('gallery-play').click();check('Local gallery pauses actual playback',LivestockGallery.paused);
          for(const e of A.catalog.entries.filter(e=>e.productionEligible))for(const clip of e.clips){
            control('gallery-species',e.id,'change');control('gallery-stage',clip.stage,'change');control('gallery-variety',clip.variety||'');
            control('gallery-state',e.category==='fish'?'Swim':e.category==='coral'?'Healthy':clip.state==='walk'?'Walk':'Idle');
            const r=A.sheets.find(e.id,clip.stage,clip.state,clip.variety);await A.sheets.load(r);LivestockGallery.draw(0);
            check(e.id+'/'+(clip.variety||'standard')+'/'+clip.stage+': local gallery exposes the correct sheet and manual frame control',!document.getElementById('gallery-sheet').hidden&&!document.getElementById('gallery-frame').disabled&&document.getElementById('gallery-sheet').getAttribute('src')===(clip.src||clip.path));
            control('gallery-frame','1');const first=document.getElementById('gallery-frame-preview').toDataURL();control('gallery-frame','16');check(e.id+'/'+(clip.variety||'standard')+'/'+clip.stage+': gallery frame stepping visibly changes original authored pixels',first!==document.getElementById('gallery-frame-preview').toDataURL());
          }
          check('Local gallery exposes all113 usable entries and excludes six acquisition holds',document.getElementById('gallery-species').options.length===113);
          check('Local gallery does not load the player save system',!AL.Save&&!AL.game);
          return checks;})()""")
        return validate(c,root,name,out,gallery,gallery_load_seconds)
    ledger=json.loads((root/'planning/sprite-production/production-ledger.json').read_text(encoding='utf8'))
    c.evaluate("""window.productionRefs={};const seed={seed:161616,nextId:1,time:480};for(const e of AL.FishAnimation.catalog.entries){
      if(!"""+json.dumps([e['id'] for e in ledger['eligible']])+""".includes(e.id))continue;
      const rows={};for(const life of e.stages){let image,meta;
        if(e.category==='fish'){const f=AL.Core.fish(seed,e.id,{genes:{color:1,size:1,longevity:1,immunity:1,fertility:1}});f.growth={baby:.15,juvenile:.6,adult:1.1}[life];image=AL.FishAnimation.source(f,0,false);meta=image.artMeta;}
        else{image=AL.ExpansionArt.frame(e.id,life)||AL.AssetBank.coral(e.id,'healthy',0);meta=image.artMeta||AL.AssetBank.metadata('corals',e.id);}
        rows[life]={src:image.toDataURL(),meta,width:image.width,height:image.height};
      }productionRefs[e.id]=rows;
    }""")
    for entry in ledger['eligible']:
        references=c.evaluate('productionRefs['+json.dumps(entry['id'])+']')
        folder=root/'planning/sprite-production/references'/entry['id'];folder.mkdir(parents=True,exist_ok=True)
        metadata={}
        for life,data in references.items():
            (folder/(life+'.png')).write_bytes(base64.b64decode(data.pop('src').split(',',1)[1]))
            metadata[life]=data
        (folder/'metadata.json').write_text(json.dumps(metadata,indent=2)+'\n',encoding='utf8')
    c.evaluate("""window.productionVarietyRefs={};const varSeed={seed:16262,nextId:1,time:480};for(const v of Object.values(AL.Clownfish.varieties)){
      const rows={};for(const life of ['juvenile','adult']){const f=AL.Core.fish(varSeed,v.speciesId,{genes:{color:1,size:1,longevity:1,immunity:1,fertility:1}});f.variety=v.id;f.growth=life==='juvenile'?.6:1.1;const im=AL.FishAnimation.source(f,0,false);rows[life]={src:im.toDataURL(),meta:im.artMeta,width:im.width,height:im.height};}productionVarietyRefs[v.id]=rows;
    }""")
    for entry in ledger['eligible']:
        for variety in entry['varieties']:
            data=c.evaluate('productionVarietyRefs['+json.dumps(variety['id'])+']');folder=root/'planning/sprite-production/variety-references'/variety['id'];folder.mkdir(parents=True,exist_ok=True);metadata={}
            for life,row in data.items():
                (folder/(life+'.png')).write_bytes(base64.b64decode(row.pop('src').split(',',1)[1]));metadata[life]=row
            (folder/'metadata.json').write_text(json.dumps(metadata,indent=2)+'\n',encoding='utf8')
    (out/'references.json').write_text(json.dumps({'usable':len(ledger['eligible']),'excluded':ledger['excluded'],'captured':sum(len(e['stages']) for e in ledger['eligible']),'playerStorageAccess':False},indent=2)+'\n',encoding='utf8')
    print(json.dumps({'usable':len(ledger['eligible']),'capturedNativeReferences':sum(len(e['stages']) for e in ledger['eligible'])}),flush=True)
    return 0


def validate(c,root,name,out,gallery,gallery_load_seconds):
    started=time.monotonic();c.navigate(root/('DIST/index.html' if '--dist' in sys.argv else 'index.html'),timeout=60)
    for _ in range(400):
        if c.evaluate('!!window.AL?.game&&!!AL.FishAnimation'):break
        time.sleep(.05)
    else:raise RuntimeError('Game did not initialize for sprite validation')
    game_load_seconds=time.monotonic()-started
    c.evaluate('localStorage.clear();AL.Startup.finish();AL.game.settings.speed=0')
    c.evaluate((root/'tests/resident_sprite_checks.js').read_text(encoding='utf8'))
    checks=list(gallery)
    def ck(label,expression):
        try:checks.append({'name':label,'pass':bool(c.evaluate(expression))})
        except Exception as error:checks.append({'name':label,'pass':False,'error':str(error)})
    result=c.evaluate("""(async()=>{const A=AL.FishAnimation,checks=[],coverage=[],check=(name,pass)=>checks.push({name,pass:!!pass}),seed={seed:16200,nextId:1,time:480};
      for(const e of A.catalog.entries)for(const clip of e.clips){
        const r=A.sheets.find(e.id,clip.stage,clip.state,clip.variety),ok=await A.sheets.load(r);check(e.id+'/'+clip.stage+': actual production PNG decodes and passes16-cell checks',ok);if(!ok)continue;
        const frames=Array.from({length:16},(_,i)=>A.sheets.frame(r,i/16)),hash=new Set(frames.map(c=>c.toDataURL()));
        check(e.id+'/'+clip.stage+': exactly16 distinct nonblank authored cells',frames.length===16&&hash.size===16&&frames.every(f=>f.width===clip.frameWidth&&f.height===clip.frameHeight));
        check(e.id+'/'+clip.stage+':16-to1 wrap uses first pose',A.sheets.frame(r,1)===frames[0]);
        if(e.category!=='fish'){
          SpriteResidentQA.verify(e,clip,frames,check);
          coverage.push({id:e.id,variety:null,stage:clip.stage,state:clip.state,frames:16,path:clip.path,sha256:clip.sha256});continue;
        }
        const f=AL.Core.fish(seed,e.id,{genes:{color:1,size:1,longevity:1,immunity:1,fertility:1}});f.growth={baby:.15,juvenile:.6,adult:1.1}[clip.stage];if(clip.variety)f.variety=clip.variety;
        check(e.id+'/'+clip.stage+': real source authority selects the new sheet',A.source(f,.25).artMeta.authoredAnimation===true);
        const before=JSON.stringify(f),position={facing:1},canvas=document.createElement('canvas');canvas.width=256;canvas.height=160;const g=canvas.getContext('2d');let valid=true;
        for(let i=0;i<32;i++){A.update(f,position,.05,i<16?1:-1);const image=A.source(f,position.animation.phase),builds=A.metrics.rigBuilds;A.draw(g,f,image,128,80,64,Math.round(64*image.height/image.width),position);valid&&=A.metrics.rigBuilds===builds&&image.artMeta.authoredAnimation;}
        check(e.id+'/'+clip.stage+': actual playback bypasses procedural fin warping in both directions',valid);
        check(e.id+'/'+clip.stage+': graphics never mutate saved specimen data',JSON.stringify(f)===before);
        f.dead=true;check(e.id+'/'+clip.stage+': death returns to original authored mortality art',!A.source(f,.25).artMeta.authoredAnimation&&A.source(f,.25).artMeta.authoredDeath);
        const eye=clip.eye;if(eye){const box=[Math.round(eye.x-eye.w/2),Math.round(eye.y-eye.h/2),eye.w,eye.h],base=frames[0].getContext('2d').getImageData(...box).data;check(e.id+'/'+clip.stage+': sampled original eye patch stays identical across all16 poses',frames.every(frame=>frame.getContext('2d').getImageData(...box).data.every((v,i)=>v===base[i])));}
        check(e.id+'/'+clip.stage+': biological and designer identity metadata survives playback',frames.every(im=>im.artMeta.speciesId===e.id&&(im.artMeta.variety||null)===(clip.variety||null)));
        const saved=AL.Core.newGame('marine',16204),tank=saved.tanks[0],resident=AL.Core.fish(saved,e.id,{genes:{color:1,size:1,longevity:1,immunity:1,fertility:1}});resident.growth={baby:.15,juvenile:.6,adult:1}[clip.stage];if(clip.variety)resident.variety=clip.variety;resident.x=resident.y=.5;tank.fish=[resident];saved.settings.speed=0;
        const signature=f=>JSON.stringify([f.id,f.species,f.variety||null,f.hp,f.hunger,f.rarity,f.genes,f.patternProfile,f.provenance||null]);
        try{const written=AL.Save.save(saved),loaded=AL.Save.load();check(e.id+'/'+clip.stage+': real local save/load preserves individual health, rarity, genes and designer identity',written.ok&&!!loaded.state&&signature(loaded.state.tanks[0].fish[0])===signature(resident));}catch(error){check(e.id+'/'+clip.stage+': real local save/load preserves individual health, rarity, genes and designer identity',false);}
        AL.game=saved;AL.renderer.positions.clear();AL.UI.close();AL.Shell?.close();AL.renderer.draw(saved,0);const hit=AL.renderer.hitboxes.find(b=>b.id===resident.id),element=document.getElementById('aquarium'),rect=element.getBoundingClientRect();let selected=false;
        if(hit){element.dispatchEvent(new MouseEvent('click',{bubbles:true,clientX:rect.left+hit.x*rect.width,clientY:rect.top+hit.y*rect.height}));selected=AL.renderer.selected===resident.id&&document.getElementById('dialog').open;AL.UI.close();}
        check(e.id+'/'+clip.stage+': real canvas click opens the correct resident inspection',selected);
        const a={facing:1},b={facing:1};A.update(resident,a,0,1);A.update(resident,b,0,1);for(let n=0;n<180;n++)A.update(resident,a,1/60,1);for(let n=0;n<90;n++)A.update(resident,b,1/30,1);check(e.id+'/'+clip.stage+': playback clock is independent of30/60fps render cadence',Math.abs(a.animation.phase-b.animation.phase)<1e-9);
        coverage.push({id:e.id,variety:clip.variety||null,stage:clip.stage,state:clip.state,frames:16,path:clip.path,sha256:clip.sha256});
      }
      const candidates=A.catalog.entries.filter(e=>e.category==='fish'&&e.clips.some(c=>!c.variety&&c.stage==='adult')),stress=AL.Core.newGame('marine',16206),tank=stress.tanks[0];stress.settings.speed=0;stress.settings.particles=false;
      await Promise.all(candidates.map(e=>A.sheets.load(A.sheets.find(e.id,'adult','swim'))));
      check('Maximum-stock benchmark preloads every selected authored adult source',candidates.every(e=>A.sheets.find(e.id,'adult','swim').image));
      for(let i=0;i<AL.Config.maxFish;i++){const entry=candidates[i%candidates.length],f=AL.Core.fish(stress,entry.id);f.growth=1;f.x=.08+(i%10)*.09;f.y=.2+Math.floor(i/10)%7*.09;tank.fish.push(f);}
      AL.game=stress;AL.renderer.positions.clear();for(let i=0;i<16;i++)AL.renderer.draw(stress,1/60);const original=JSON.stringify(stress),times=[],cacheBefore={...A.sheets.metrics};for(let i=0;i<120;i++){const start=performance.now();AL.renderer.draw(stress,1/60);times.push(performance.now()-start);}times.sort((a,b)=>a-b);
      check('Actual maximum-stock renderer keeps biology/save state untouched',JSON.stringify(stress)===original);
      const metrics=A.sheets.metrics,performanceResult={fish:tank.fish.length,distinctSpecies:candidates.length,frames:120,medianMs:times[60],p95Ms:times[114],meanMs:times.reduce((n,v)=>n+v,0)/120,minimumTargetFps:30,frameCache:{entries:metrics.frameCache,limit:metrics.maxFrames,hits:metrics.frameHits-cacheBefore.frameHits,misses:metrics.frameMisses-cacheBefore.frameMisses,evictions:metrics.frameEvictions-cacheBefore.frameEvictions}};check('Actual maximum-stock authored playback stays within30fps budget at95th percentile',performanceResult.p95Ms<1000/30);
      const first=AL.Core.newGame('marine',16207),testFish=AL.Core.fish(first,candidates[0].id);testFish.growth=1;first.tanks[0].fish=[testFish];first.settings.speed=0;first.simulationCheckpoint=Date.now()-5000;const second=AL.Save.parse(JSON.stringify(first));
      AL.game=first;AL.renderer.positions.clear();for(let i=0;i<180;i++)AL.renderer.draw(first,1/60);const now=first.simulationCheckpoint+5000;AL.Offline.sync(first,now);AL.Offline.sync(second,now);
      check('Offline ecosystem results are identical with or without live animation rendering',JSON.stringify(first.tanks)===JSON.stringify(second.tanks)&&first.seed===second.seed&&first.time===second.time&&first.credits===second.credits);
      check('Production sheet frame cache stays bounded under maximum-stock playback',A.sheets.metrics.frameCache<=A.sheets.metrics.maxFrames);
      check('Decoded production-sheet memory remains bounded while browsing the catalog',A.sheets.metrics.loaded<=A.sheets.metrics.maxDecodedSheets);
      const sampleClips=A.catalog.entries.flatMap(e=>e.clips).slice(0,3),library=A.createSheetLibrary(sampleClips.map((c,i)=>({id:'cache-fixture-'+i,clips:[c]})),{maxDecodedSheets:2}),records=sampleClips.map((c,i)=>library.find('cache-fixture-'+i,c.stage,c.state,c.variety));
      await library.load(records[0]);const expected=library.frame(records[0],0).toDataURL();await library.load(records[1]);await library.load(records[2]);check('Decoded sheet LRU evicts an unseen sheet at its configured bound',library.metrics.loaded===2&&!records[0].image&&!!records[2].image);
      check('Evicted sheet retains cached cells without blanking its visible pose',library.frame(records[0],0)?.toDataURL()===expected);
      await library.load(records[0]);check('Evicted original PNG reloads successfully without changing its authored pixels',!!records[0].image&&library.metrics.loaded===2&&library.frame(records[0],0).toDataURL()===expected&&!library.issues.length);
      const mixedPerformance=await SpriteResidentQA.mixedPerformance(check);
      return {checks,coverage,performance:performanceResult,mixedPerformance};})()""")
    checks.extend(result['checks'])
    ck('All113 usable identities remain recorded; six holds remain excluded',"AL.FishAnimation.catalog.entries.filter(e=>e.productionEligible).length===113&&Object.values(AL.FishAnimation.auditCatalog()).every(a=>!a.length)")
    ck('No accepted-sheet errors are hidden','AL.FishAnimation.sheets.issues.length===0')
    ck('Freshwater acquisition remains locked',"(()=>{try{AL.Core.act(AL.game,'buyTank',{water:'fresh',size:0});return false}catch{return true}})()")
    report={'browser':name,'passed':sum(x['pass'] for x in checks),'failed':sum(not x['pass'] for x in checks),'checks':checks,'coverage':result['coverage'],'productionSheetsTested':len(result['coverage']),'performance':result['performance'],'mixedPerformance':result['mixedPerformance'],'coldLoadSeconds':{'offlineGallery':round(gallery_load_seconds,3),'game':round(game_load_seconds,3)}}
    report['selectionDiagnostics']=c.evaluate('window.__residentSelectionFailures||[]');report['entry']='DIST/index.html' if '--dist' in sys.argv else 'index.html'
    (out/(name+'-results.json')).write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'passed':report['passed'],'failed':report['failed'],'productionSheetsTested':report['productionSheetsTested'],'failures':[x for x in checks if not x['pass']]}),flush=True)
    return int(report['failed']>0)
