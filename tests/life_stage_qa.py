"""Offline life-stage gallery and actual renderer verification via the existing CDP harness."""
import base64
import json
import time

def run(client,root,name,check):
    checks=[]
    client.navigate(root/'life-stage-review.html')
    for _ in range(100):
        if client.evaluate('window.LIFE_REVIEW?.ready'):break
        time.sleep(.05)
    before=client.evaluate("localStorage.getItem('aquarium-life-v2')")
    report=client.evaluate((root/'tests/life_stage_checks.js').read_text(encoding='utf-8'))
    checks.extend(report['results'])
    def choose(key,value):client.evaluate(f"document.getElementById('{key}').value='{value}';document.getElementById('{key}').dispatchEvent(new Event('change'))")
    def shot(label):
        image=client.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})
        (root/'assets/previews'/f'{name}-life-{label}.png').write_bytes(base64.b64decode(image['data']))
    client.call('Emulation.setDeviceMetricsOverride',{'width':1440,'height':1250,'deviceScaleFactor':1,'mobile':False})
    for category,count in [('fish',18),('corals',5),('bottom_feeders',4)]:
        client.evaluate(f"document.querySelector('[data-category={category}]').click()")
        checks.append(check(client.evaluate(f"document.getElementById('species').options.length==={count}"),f'{category}: correct audited entries'))
        for id in client.evaluate("Array.from(document.getElementById('species').options,o=>o.value)"):
            choose('species',id)
            checks.append(check(client.evaluate("document.querySelectorAll('.pose').length===8&&document.querySelectorAll('.scale').length===8&&LIFE_REVIEW.id===document.getElementById('species').value"),f'{id}: all stages shown with scale comparisons'))
            for direction in ['-1','1']:choose('direction',direction)
            for pose in ['baby','adult']:
                client.evaluate(f"document.querySelector('[data-stage={pose}][data-state=dead]').click()")
                checks.append(check(client.evaluate(f"LIFE_REVIEW.selectedState==='dead'&&LIFE_REVIEW.selectedStage==='{pose}'"),f'{id}: selectable {pose} death art'))
        choose('species',{'fish':'clown','corals':'sps','bottom_feeders':'cory'}[category])
        client.evaluate('scrollTo(0,0)');shot(category)
    for background in ['dark','bright','checker']:
        choose('backdrop',background)
        checks.append(check(client.evaluate(f"document.body.className==='{background}'"),f'{background}: background comparison'))
    for zoom in ['1','2','3']:choose('zoom',zoom)
    client.evaluate("document.getElementById('eyes').click();document.getElementById('swim').click()")
    old=client.evaluate('LIFE_REVIEW.draws');time.sleep(.25)
    checks.append(check(client.evaluate('LIFE_REVIEW.draws')>old,'Swim and directional preview advances'))
    client.evaluate("document.getElementById('swim').click()")
    old=client.evaluate('LIFE_REVIEW.draws');time.sleep(.15)
    checks.append(check(client.evaluate('LIFE_REVIEW.draws')==old,'Static preview stays frozen'))
    client.evaluate("document.getElementById('review-status').value='Needs Improvement';document.getElementById('review-notes').value='<img src=x onerror=alert(1)> test note';document.getElementById('review-form').requestSubmit()")
    client.call('Page.reload');time.sleep(.35)
    client.evaluate("document.querySelector('[data-category=bottom_feeders]').click()")
    checks.append(check(client.evaluate("document.getElementById('review-status').value==='Needs Improvement'&&document.getElementById('review-notes').value.includes('<img')&&!document.querySelector('img[src=x]')"),'Review persists as plain text without automatic approval'))
    checks.append(check(client.evaluate("localStorage.getItem('aquarium-life-v2')")==before,'Gallery leaves game save bytes unchanged'))
    for width in [1440,1024,760,390]:
        client.call('Emulation.setDeviceMetricsOverride',{'width':width,'height':1100,'deviceScaleFactor':1,'mobile':False})
        checks.append(check(client.evaluate('document.documentElement.scrollWidth<=innerWidth'),f'Gallery fits {width}px viewport'))
    shot('mobile')
    client.navigate(root/'tests/life-stage-contact.html')
    for _ in range(100):
        if client.evaluate('window.CONTACT_READY'):break
        time.sleep(.05)
    client.call('Emulation.setDeviceMetricsOverride',{'width':1450,'height':1430,'deviceScaleFactor':1,'mobile':False})
    for page in range(3):
        client.evaluate(f'showContact({page})');shot(f'contact-{page+1}')
    client.navigate(root/'index.html')
    for _ in range(100):
        if client.evaluate('!!window.AL?.game'):break
        time.sleep(.05)
    checks.append(check(client.evaluate("AL.LifeStages.loaded===27&&!!document.querySelector('a[href=\"life-stage-review.html\"]')"),'Main index loads stage assets and links the offline gallery'))
    integration=client.evaluate("""(()=>{
      const s=AL.Core.newGame(121),t=s.tanks[0];s.settings.speed=0;
      t.fish=Object.keys(AL.Data.species).flatMap(species=>[.15,.6,1].flatMap(growth=>[false,true].map(dead=>{const f=AL.Core.fish(s,species);f.growth=growth;f.dead=dead;f.x=.5;f.y=.4;return f;})));
      const before=JSON.stringify(s),c=document.createElement('canvas');c.width=960;c.height=480;const r=new AL.Renderer(c);let seen=0,deaths=0,badFlip=0;
      const original=AL.SpriteKit.draw;AL.SpriteKit.draw=function(ctx,sprite,x,y,w,h,direction,inverted){if(sprite.artMeta?.stage){seen++;if(sprite.artMeta.state==='dead'){deaths++;if(inverted)badFlip++;}}return original(...arguments);};
      try{r.draw(s,.016);}finally{AL.SpriteKit.draw=original;}
      return {seen,deaths,badFlip,immutable:JSON.stringify(s)===before};
    })()""")
    checks.append(check(integration['seen']==131 and integration['deaths']==66 and integration['badFlip']==0,'All fish stage/death poses reach the actual renderer; authored deaths never double-invert'))
    checks.append(check(integration['immutable'],'Rendering stages does not mutate simulation or save state'))
    checks.append(check(client.evaluate("AL.Art.clownfishArtLoaded&&AL.Art.sprite('clown',0).width===128&&AL.Art.thumb('clown')===AL.Art.sprite('clown',0).toDataURL()"),'Approved adult Ocellaris art and thumbnail preserved'))
    errors=[e for e in client.events if e.get('method')=='Runtime.exceptionThrown']
    network=[e['params']['request']['url'] for e in client.events if e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('http:','https:'))]
    checks.append(check(not errors,'No JavaScript exceptions'))
    checks.append(check(not network,'No HTTP/HTTPS requests in offline operation'))
    failed=[r for r in checks if not r['pass']]
    output={'browser':name,'passed':len(checks)-len(failed),'failed':len(failed),'renderCases':report['renderCases'],'checks':checks,'errors':errors,'networkRequests':network,'integration':integration}
    (root/'tests'/f'{name}-life-stage-results.json').write_text(json.dumps(output,indent=2),encoding='utf-8')
    print(json.dumps({k:output[k] for k in ['browser','passed','failed','renderCases']}),flush=True)
    for result in failed:print('FAIL:',result['name'],flush=True)
    return 1 if failed else 0
