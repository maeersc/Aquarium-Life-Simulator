"""Isolated gallery QA, invoked through browser_qa.py --art-review."""
import base64
import json
import time
from pathlib import Path
from PIL import Image


def run(client, root, name, check):
    results=[]
    client.navigate(root/'art-review.html')
    for _ in range(100):
        if client.evaluate('window.ART_REVIEW?.ready'): break
        time.sleep(.05)
    before=client.evaluate("localStorage.getItem('aquarium-life-v2')")
    client.evaluate("localStorage.removeItem('aquarium-life-art-review-v1')")
    client.call('Page.reload')
    time.sleep(.3)
    results.append(check(client.evaluate('ART_REVIEW.ready && ART_REVIEW.loadedAtlases===4 && ART_REVIEW.errors.length===0'), 'Four local PNG atlases load while offline'))
    results.append(check(client.evaluate('ART_REVIEW.speciesCount===22 && document.getElementById("species-select").options.length===22'), 'Gallery catalog contains exactly the 22 runtime species'))
    results.append(check(client.evaluate("document.getElementById('review-badge').textContent==='Approved' && ART_BENCHMARK.approved && ART_BENCHMARK.speciesId==='clown'"), 'User-assigned artwork is recorded for the Ocellaris species only'))
    for species in client.evaluate('Object.keys(AL.Data.species)'):
        client.evaluate(f"document.getElementById('species-select').value='{species}';document.getElementById('species-select').dispatchEvent(new Event('change'))")
        results.append(check(client.evaluate(f"ART_REVIEW.species==='{species}' && document.getElementById('current-preview').width===512"), f'Current sprite and details render: {species}'))
        if species!='clown':
            assert client.evaluate("document.getElementById('proposal-caption').textContent.includes('Not Started')")
    client.evaluate("document.getElementById('species-select').value='clown';document.getElementById('species-select').dispatchEvent(new Event('change'))")
    for size in [96,128,192,256]:
        client.evaluate(f"document.getElementById('resolution-select').value='{size}';document.getElementById('resolution-select').dispatchEvent(new Event('change'))")
        results.append(check(client.evaluate(f"ART_REVIEW.resolution==={size} && document.getElementById('native-preview').width==={size}"), f'{size}-pixel native comparison works'))
        atlas=Image.open(root/f'assets/livestock/fish/clownfish/clownfish-benchmark-v1-{size}.png')
        results.append(check(atlas.size==(size*4,size) and set(atlas.getchannel('A').getdata())=={0,255}, f'{size}-pixel atlas has four frames and crisp transparent alpha'))
    client.evaluate("document.getElementById('resolution-select').value='128';document.getElementById('resolution-select').dispatchEvent(new Event('change'))")
    old=client.evaluate('ART_REVIEW.framesDrawn');time.sleep(.3)
    results.append(check(client.evaluate('ART_REVIEW.framesDrawn')>old, 'Swim animation advances'))
    client.evaluate("document.getElementById('play-toggle').click()")
    old=client.evaluate('ART_REVIEW.framesDrawn');time.sleep(.2)
    results.append(check(client.evaluate('ART_REVIEW.framesDrawn')==old, 'Pause freezes animation'))
    old=client.evaluate('ART_REVIEW.frame');client.evaluate("document.getElementById('step-frame').click()")
    results.append(check(client.evaluate('ART_REVIEW.frame')==(old+1)%4, 'Frame stepping advances one pose'))
    for mode in ['idle','turn','death']:
        client.evaluate(f"document.getElementById('motion-select').value='{mode}';document.getElementById('motion-select').dispatchEvent(new Event('change'))")
        results.append(check(client.evaluate("document.getElementById('motion-note').textContent.length>40"), f'{mode} concept explicitly describes its completeness'))
    results.append(check(client.evaluate("ART_REVIEW.frame===0 && document.getElementById('step-frame').disabled"), 'Death pose freezes frame zero'))
    for backdrop in ['bright','checker','dark']:
        client.evaluate(f"document.getElementById('background-select').value='{backdrop}';document.getElementById('background-select').dispatchEvent(new Event('change'))")
        results.append(check(client.evaluate(f"document.querySelector('.stage').classList.contains('{backdrop}')"), f'{backdrop} background comparison works'))
    client.evaluate("document.getElementById('camera-select').value='2';document.getElementById('camera-select').dispatchEvent(new Event('change'))")
    results.append(check(client.evaluate("document.getElementById('scale-note').textContent.includes('2× camera')"), 'Camera changes preserve equal comparison scale'))
    client.evaluate("document.getElementById('review-notes').value='Draft feedback';document.getElementById('resolution-select').value='192';document.getElementById('resolution-select').dispatchEvent(new Event('change'))")
    results.append(check(client.evaluate("document.getElementById('review-notes').value==='Draft feedback'"), 'Comparison controls preserve unsaved review feedback'))
    client.evaluate("document.getElementById('status-select').value='Needs Improvement';document.getElementById('review-notes').value='QA review persistence';document.getElementById('save-review').click()")
    client.call('Page.reload');time.sleep(.3)
    results.append(check(client.evaluate("document.getElementById('status-select').value==='Needs Improvement' && document.getElementById('review-notes').value==='QA review persistence'"), 'User-entered review status and notes survive reload'))
    results.append(check(client.evaluate("localStorage.getItem('aquarium-life-v2')")==before, 'Gallery leaves gameplay save bytes untouched'))
    client.evaluate("localStorage.removeItem('aquarium-life-art-review-v1')")
    client.call('Page.reload');time.sleep(.3)
    for width in [1440,1024,760,390]:
        client.call('Emulation.setDeviceMetricsOverride', {'width':width,'height':1100,'deviceScaleFactor':1,'mobile':False})
        results.append(check(client.evaluate('document.documentElement.scrollWidth<=innerWidth'), f'Gallery fits {width}px viewport'))
    client.call('Emulation.setDeviceMetricsOverride', {'width':1440,'height':1100,'deviceScaleFactor':1,'mobile':False})
    client.evaluate("document.getElementById('play-toggle').click();scrollTo(0,0)")
    shot=client.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})
    (root/'assets/previews'/f'{name}-art-review.png').write_bytes(base64.b64decode(shot['data']))
    client.evaluate("document.getElementById('tank-preview').scrollIntoView({block:'center'})")
    shot=client.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})
    (root/'assets/previews'/f'{name}-art-scale.png').write_bytes(base64.b64decode(shot['data']))
    errors=[e for e in client.events if e.get('method')=='Runtime.exceptionThrown']
    network=[e['params']['request']['url'] for e in client.events if e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('http:','https:'))]
    results.append(check(not errors,'No gallery JavaScript exceptions'))
    results.append(check(not network,'No gallery HTTP(S) requests'))
    report={'passed':len(results),'failed':0,'checks':results,'browser':client.evaluate('navigator.userAgent'),'errors':errors,'networkRequests':network}
    (root/'tests'/f'{name}-art-results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(f'{name}: {len(results)} art gallery checks passed',flush=True)
    return 0
