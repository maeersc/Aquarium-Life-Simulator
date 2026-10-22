"""Art update 1.1 offline gallery, sprite and regression verification."""
import base64
import json
import time


def run(client,root,name,check):
    checks=[]
    client.navigate(root/'art-review.html')
    for _ in range(100):
        if client.evaluate('window.ART_REVIEW?.ready'):break
        time.sleep(.05)
    game_before=client.evaluate("localStorage.getItem('aquarium-life-v2')")
    client.evaluate("localStorage.removeItem('aquarium-life-art-review-v11')")
    client.call('Page.reload');time.sleep(.4)
    checks.append(check(client.evaluate('ART_REVIEW.ready && ART_REVIEW.loadedAssets===13 && ART_REVIEW.errors.length===0'), 'Offline gallery initializes all assets'))
    checks.append(check(client.evaluate('ART_REVIEW.runtimeSpeciesCount===22 && ART_REVIEW.priorityFish.length===6 && document.getElementById("subject-select").options.length===27'), 'Twenty-two gameplay fish and five art-only subjects remain distinct'))
    sprite_report=client.evaluate((root/'tests/sprite_checks.js').read_text(encoding='utf-8'))
    failures=[r['name'] for r in sprite_report['results'] if not r['pass']]
    for failure in failures:print('SPRITE FAIL:',failure,flush=True)
    checks.extend(sprite_report['results'])
    def choose(id,value):client.evaluate(f"document.getElementById('{id}').value='{value}';document.getElementById('{id}').dispatchEvent(new Event('change'))")
    def category(value):client.evaluate(f"document.querySelector('[data-category={value}]').click()")
    def screenshot(label):
        image=client.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})
        (root/'assets/previews'/f'{name}-art11-{label}.png').write_bytes(base64.b64decode(image['data']))
    client.call('Emulation.setDeviceMetricsOverride',{'width':1440,'height':1100,'deviceScaleFactor':1,'mobile':False})
    client.evaluate("document.getElementById('show-eyes').click();scrollTo(0,0)")
    screenshot('fish')
    for id in client.evaluate('ART_REVIEW.priorityFish'):
        choose('subject-select',id)
        checks.append(check(client.evaluate(f"ART_REVIEW.selected==='{id}'"),f'Priority artwork selectable: {id}'))
    for mode in ['idle','swim','turn','death']:
        choose('motion-select',mode)
        checks.append(check(client.evaluate("document.getElementById('motion-note').textContent.length>35"),f'{mode} presentation and limitations described'))
    choose('motion-select','swim')
    old=client.evaluate('ART_REVIEW.framesDrawn');time.sleep(.3)
    checks.append(check(client.evaluate('ART_REVIEW.framesDrawn')>old,'Animation advances'))
    client.evaluate("document.getElementById('play-toggle').click()")
    old=client.evaluate('ART_REVIEW.framesDrawn');time.sleep(.15)
    checks.append(check(client.evaluate('ART_REVIEW.framesDrawn')==old,'Pause freezes animation'))
    for backdrop in ['checker','bright','dark']:
        choose('background-select',backdrop)
        checks.append(check(client.evaluate(f"document.querySelector('.stage').classList.contains('{backdrop}')"),f'{backdrop} preview works'))
    category('corals')
    for id in ['zoa','mushroom','sps','lps','soft']:
        choose('subject-select',id)
        for state in ['healthy','stressed','bleached','tissue-loss','dead']:
            choose('state-select',state)
            checks.append(check(client.evaluate('document.querySelectorAll(".art-study").length===5'),f'{id} {state} state and comparison grid render'))
    choose('subject-select','mushroom');choose('state-select','healthy')
    client.evaluate('scrollTo(0,0)');screenshot('corals')
    category('rocks')
    for id in ['fiji','caribbean','hawaiian']:
        choose('subject-select',id)
        for variant in range(4):
            choose('state-select',str(variant))
            checks.append(check(client.evaluate('document.querySelectorAll(".art-study").length===4'),f'{id} rock variant {variant} renders'))
    client.evaluate("document.getElementById('place-rock').click();const c=document.getElementById('tank-preview'),r=c.getBoundingClientRect();c.dispatchEvent(new MouseEvent('click',{clientX:r.left+r.width*.65,clientY:r.top+r.height*.8,bubbles:true}))")
    position=client.evaluate('ART_REVIEW.layout.hawaiian')
    client.call('Page.reload');time.sleep(.4)
    checks.append(check(client.evaluate('ART_REVIEW.layout.hawaiian')==position,'Rock preview layout persists through reload'))
    client.evaluate('scrollTo(0,0)');screenshot('rocks')
    for width in [1440,1024,760,390]:
        client.call('Emulation.setDeviceMetricsOverride',{'width':width,'height':1100,'deviceScaleFactor':1,'mobile':False})
        checks.append(check(client.evaluate('document.documentElement.scrollWidth<=innerWidth'),f'Gallery fits {width}px'))
    checks.append(check(client.evaluate("localStorage.getItem('aquarium-life-v2')")==game_before,'Gallery leaves gameplay save bytes intact'))
    errors=[e for e in client.events if e.get('method')=='Runtime.exceptionThrown']
    requests=[e['params']['request']['url'] for e in client.events if e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('http:','https:'))]
    checks.append(check(not errors,'No browser exceptions'));checks.append(check(not requests,'No HTTP(S) artwork requests'))
    client.navigate(root/'tests/eye-review.html')
    for _ in range(100):
        if client.evaluate('window.EYE_REVIEW_READY'):break
        time.sleep(.05)
    checks.append(check(client.evaluate('window.EYE_REVIEW_READY===true'),'All-species eye contact sheet renders'))
    client.call('Emulation.setDeviceMetricsOverride',{'width':1360,'height':1300,'deviceScaleFactor':1,'mobile':False})
    for part,y in enumerate([0,1230,2460]):
        client.evaluate(f'scrollTo(0,{y})')
        screenshot('eyes-'+str(part+1))
    failed=sum(not r['pass'] for r in checks)
    report={'passed':len(checks)-failed,'failed':failed,'checks':checks,'spriteReport':sprite_report,'errors':errors,'networkRequests':requests,'browser':client.evaluate('navigator.userAgent')}
    (root/'tests'/f'{name}-art11-results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(name+': '+str(report['passed'])+' art/sprite checks passed; '+str(failed)+' failed; '+str(sprite_report['renderCases'])+' directional render cases',flush=True)
    return 1 if failed else 0
