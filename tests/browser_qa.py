"""No third-party packages: run system and UI checks over Chrome/Edge DevTools.
Usage: python tests/browser_qa.py [chrome|edge]
Browser runs headless in a dedicated test profile, never the user's profile.
"""
import base64
import json
import os
from pathlib import Path
import socket
import struct
import subprocess
import sys
import time
import urllib.request

ROOT = Path(__file__).resolve().parent.parent
NAME = sys.argv[1] if len(sys.argv) > 1 else 'chrome'
BROWSERS = {'chrome': r'C:\Program Files\Google\Chrome\Application\chrome.exe',
            'edge': r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'}
LIVESTOCK16 = '--livestock16' in sys.argv or '--livestock16-audit' in sys.argv
SPRITE_PRODUCTION = any(flag in sys.argv for flag in ['--sprite-production','--sprite-production-refs','--sprite-resident-fixtures'])
PORT = (9357 if NAME == 'chrome' else 9358) if SPRITE_PRODUCTION else (9347 if NAME == 'chrome' else 9348) if LIVESTOCK16 else (9337 if NAME == 'chrome' else 9338)

class CDP:
    def __init__(self, url):
        from urllib.parse import urlparse
        u = urlparse(url)
        self.sock = socket.create_connection((u.hostname, u.port), timeout=20)
        key = base64.b64encode(os.urandom(16)).decode()
        request = (f'GET {u.path} HTTP/1.1\r\nHost: {u.hostname}:{u.port}\r\n'
                   f'Upgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: {key}\r\n'
                   'Sec-WebSocket-Version: 13\r\n\r\n')
        self.sock.sendall(request.encode())
        reply = b''
        while b'\r\n\r\n' not in reply:
            reply += self.sock.recv(1)
        if not reply.startswith(b'HTTP/1.1 101 '):
            raise RuntimeError(reply.decode())
        self.counter = 0
        self.events = []

    def read(self, n):
        data = b''
        while len(data) < n:
            chunk = self.sock.recv(n-len(data))
            if not chunk:
                raise RuntimeError('Browser closed the connection')
            data += chunk
        return data

    def receive(self):
        data = b''
        while True:
            header = self.read(2)
            n = header[1] & 127
            if n == 126:
                n = struct.unpack('!H', self.read(2))[0]
            elif n == 127:
                n = struct.unpack('!Q', self.read(8))[0]
            mask = self.read(4) if header[1] & 128 else None
            payload = self.read(n)
            if mask:
                payload = bytes(b ^ mask[i % 4] for i, b in enumerate(payload))
            if header[0] & 15 == 8:
                raise RuntimeError('WebSocket closed')
            data += payload
            if header[0] & 128:
                return json.loads(data)

    def call(self, method, params=None):
        self.counter += 1
        payload = json.dumps({'id': self.counter, 'method': method, 'params': params or {}}).encode()
        n = len(payload)
        header = bytes([129, 128 | n]) if n < 126 else bytes([129, 254])+struct.pack('!H', n) if n < 65536 else bytes([129, 255])+struct.pack('!Q', n)
        mask = os.urandom(4)
        self.sock.sendall(header+mask+bytes(b ^ mask[i % 4] for i, b in enumerate(payload)))
        while True:
            message = self.receive()
            if message.get('id') == self.counter:
                if 'error' in message:
                    raise RuntimeError(message['error'])
                return message.get('result', {})
            self.events.append(message)

    def evaluate(self, expression):
        result = self.call('Runtime.evaluate', {'expression': expression, 'returnByValue': True, 'awaitPromise': True})
        if 'exceptionDetails' in result:
            raise RuntimeError(json.dumps(result['exceptionDetails']))
        return result.get('result', {}).get('value')

    def navigate(self, path, timeout=10):
        self.call('Page.navigate', {'url': path.as_uri()})
        deadline=time.monotonic()+timeout
        while time.monotonic()<deadline:
            try:
                if self.evaluate("document.readyState === 'complete'"):
                    return
            except RuntimeError:
                pass
            time.sleep(.05)
        raise RuntimeError('Page load timeout')

def check(value, message):
    if not value:
        raise AssertionError(message)
    return {'name': message, 'pass': True}

def main():
    profile = ROOT / 'tests' / (NAME+('-sprite-production-qa-profile' if SPRITE_PRODUCTION else '-livestock16-qa-profile' if LIVESTOCK16 else '-qa-profile'))
    if '--benchmark-development' in sys.argv or '--benchmark-protected' in sys.argv:
        variant='development' if '--benchmark-development' in sys.argv else 'protected'
        profile=ROOT/'tests'/(NAME+'-protection-'+variant+'-'+str(time.time_ns())+'-qa-profile')
    log = open(ROOT / 'tests' / (NAME+'-browser.log'), 'w', encoding='utf-8')
    command = [BROWSERS[NAME], '--headless', '--disable-gpu', '--no-first-run',
               '--no-default-browser-check', '--disable-background-networking',
               '--disable-component-update', '--disable-sync', '--disable-extensions',
               '--disable-features=OptimizationHints,MediaRouter',
               f'--user-data-dir={profile}', f'--remote-debugging-port={PORT}', 'about:blank']
    process = subprocess.Popen(command, stdout=log, stderr=log, creationflags=subprocess.CREATE_NO_WINDOW)
    client = None
    try:
        for _ in range(100):
            try:
                with urllib.request.urlopen(f'http://127.0.0.1:{PORT}/json', timeout=1) as response:
                    pages = json.load(response)
                page = next(p for p in pages if p['type'] == 'page')
                client = CDP(page['webSocketDebuggerUrl'])
                break
            except (OSError, StopIteration):
                time.sleep(.1)
        if client is None:
            raise RuntimeError('Headless browser did not expose a DevTools page; see browser log.')
        client.call('Runtime.enable')
        client.call('Page.enable')
        client.call('Network.enable')
        if '--protection-media' in sys.argv:
            import protection_media_qa
            return protection_media_qa.run(client,ROOT,NAME)
        if '--protection-idle' in sys.argv:
            import protection_idle_qa
            return protection_idle_qa.run(client,ROOT,NAME)
        if '--protection-performance' in sys.argv:
            import protection_performance_qa
            return protection_performance_qa.run(client,ROOT,NAME)
        if '--protected-build' in sys.argv:
            import protected_build_qa
            return protected_build_qa.run(client,ROOT,NAME)
        if '--ui-quantity' in sys.argv:
            import ui_quantity_qa
            return ui_quantity_qa.run(client,ROOT,NAME)
        if '--performance' in sys.argv:
            import performance_qa
            return performance_qa.run(client,ROOT,NAME)
        if '--tutorial-audit' in sys.argv:
            import tutorial_audit_qa
            status=tutorial_audit_qa.run(client,ROOT,NAME)
            if status or '--with-reliability' not in sys.argv:return status
            import equipment_reliability_qa
            return equipment_reliability_qa.run(client,ROOT,NAME)
        if '--tutorial' in sys.argv:
            import tutorial_qa
            status=tutorial_qa.run(client,ROOT,NAME)
            if status or '--with-reliability' not in sys.argv:return status
            import equipment_reliability_qa
            return equipment_reliability_qa.run(client,ROOT,NAME)
        if '--simplify' in sys.argv:
            import simplification_qa
            return simplification_qa.run(client,ROOT,NAME)
        if '--economy20' in sys.argv:
            import economy_update_qa
            status=economy_update_qa.run(client,ROOT,NAME)
            if status or '--with-reliability' not in sys.argv:return status
            import equipment_reliability_qa
            return equipment_reliability_qa.run(client,ROOT,NAME)
        if '--equipment-reliability' in sys.argv:
            import equipment_reliability_qa
            return equipment_reliability_qa.run(client,ROOT,NAME)
        if '--inventory' in sys.argv:
            import inventory_qa
            return inventory_qa.run(client,ROOT,NAME)
        if '--pages' in sys.argv:
            import pages_qa
            return pages_qa.run(client, ROOT, NAME)
        client.call('Network.emulateNetworkConditions', {'offline': True, 'latency': 0, 'downloadThroughput': 0, 'uploadThroughput': 0})
        if SPRITE_PRODUCTION:
            import sprite_production_qa
            if '--sprite-resident-fixtures' in sys.argv:return sprite_production_qa.resident_fixtures(client,ROOT,NAME)
            return sprite_production_qa.run(client,ROOT,NAME,'--sprite-production-refs' in sys.argv)
        if '--livestock16-audit' in sys.argv or '--livestock16' in sys.argv:
            import livestock16_qa
            return livestock16_qa.run(client,ROOT,NAME,'--livestock16-audit' in sys.argv)
        if '--fish-animation-audit' in sys.argv or '--fish-animation' in sys.argv:
            import fish_animation_qa
            return fish_animation_qa.run(client,ROOT,NAME,'--fish-animation-audit' in sys.argv)
        if '--location-art' in sys.argv:
            import location_art_qa
            return location_art_qa.run(client,ROOT,NAME)
        if '--preparation' in sys.argv or '--preparation-baseline' in sys.argv:
            import preparation_qa
            return preparation_qa.run(client,ROOT,NAME,'--preparation-baseline' in sys.argv)
        if '--diving-expansion' in sys.argv:
            import diving_expansion_qa
            return diving_expansion_qa.run(client,ROOT,NAME)
        if '--global-receiving' in sys.argv:
            import global_receiving_qa
            return global_receiving_qa.run(client,ROOT,NAME)
        if '--receiving' in sys.argv:
            import receiving_qa
            return receiving_qa.run(client,ROOT,NAME)
        if '--mystery-diving' in sys.argv:
            import mystery_diving_qa
            return mystery_diving_qa.run(client,ROOT,NAME)
        if '--breeding' in sys.argv:
            import breeding_qa
            return breeding_qa.run(client,ROOT,NAME)
        if '--store-casino' in sys.argv:
            import store_casino_qa
            return store_casino_qa.run(client,ROOT,NAME)
        if '--layout-cleanup' in sys.argv:
            import layout_cleanup_qa
            return layout_cleanup_qa.run(client,ROOT,NAME)
        if '--heater' in sys.argv:
            import heater_qa
            return heater_qa.run(client,ROOT,NAME)
        if '--overnight-before' in sys.argv or '--overnight' in sys.argv:
            import overnight_qa
            return overnight_qa.run(client,ROOT,NAME)
        if '--update34' in sys.argv:
            import update34_qa
            return update34_qa.run(client,ROOT,NAME)
        if '--update33' in sys.argv:
            import update33_qa
            return update33_qa.run(client,ROOT,NAME)
        if '--update29' in sys.argv:
            import update29_qa
            return update29_qa.run(client,ROOT,NAME)
        if '--diving' in sys.argv:
            import diving_qa
            return diving_qa.run(client, ROOT, NAME)
        if '--sprite-audit' in sys.argv:
            from sprite_audit import run
            return run(client, ROOT, NAME)
        if '--expansion' in sys.argv:
            import expansion_qa
            return expansion_qa.run(client,ROOT,NAME)
        if '--ecosystem' in sys.argv:
            import ecosystem_qa
            return ecosystem_qa.run(client,ROOT,NAME)
        if '--gameplay' in sys.argv:
            import gameplay_qa
            return gameplay_qa.run(client,ROOT,NAME)
        if '--shell' in sys.argv:
            import shell_qa
            return shell_qa.run(client,ROOT,NAME)
        if '--economy' in sys.argv:
            import economy_qa
            return economy_qa.run(client,ROOT,NAME)
        if '--audit' in sys.argv:
            import project_audit_qa
            return project_audit_qa.run(client,ROOT,NAME)
        if '--clownfish' in sys.argv:
            import clownfish_qa
            return clownfish_qa.run(client,ROOT,NAME,check)
        if '--store' in sys.argv:
            import store_qa
            return store_qa.run(client,ROOT,NAME,check)
        if '--life-stages' in sys.argv:
            import life_stage_qa
            return life_stage_qa.run(client,ROOT,NAME,check)
        if '--art-review' in sys.argv:
            from art_review_qa import run
            return run(client, ROOT, NAME, check)
        client.navigate(ROOT/'tests'/'index.html')
        report = client.evaluate('window.TEST_REPORT')
        if not report:
            raise RuntimeError('System test runner did not finish')
        print(f"{NAME}: {report['passed']} system checks passed, {report['failed']} failed", flush=True)
        for result in report['results']:
            if not result['pass']:
                print('FAIL:', result['name'], result['error'], flush=True)
        (ROOT/'tests'/f'{NAME}-results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
        if '--systems' in sys.argv:
            return 1 if report['failed'] else 0
        if '--legacy-ui' not in sys.argv:
            import store_qa
            current_ui=store_qa.run(client,ROOT,NAME,check)
            return 1 if report['failed'] else current_ui
        client.navigate(ROOT/'index.html')
        client.evaluate("AL.Save.save=()=>({ok:true,message:'Test reset'}); localStorage.removeItem('aquarium-life-v2'); localStorage.removeItem('aquarium-life-backup');")
        client.call('Page.reload')
        time.sleep(.4)
        for event in client.events:
            if event.get('method') == 'Runtime.exceptionThrown':
                print('BROWSER ERROR:', json.dumps(event['params']), flush=True)
        ui = []
        ui.append(check(client.evaluate("!!window.AL && !!AL.game && document.getElementById('dialog').open"), 'Offline file:// opens with route selection'))
        client.evaluate("document.querySelector('[data-action=start]').click()")
        ui.append(check(client.evaluate("AL.game.credits===3000 && !document.getElementById('dialog').open"), 'Freshwater starter selection works'))
        client.evaluate("document.getElementById('onboard-action').click(); document.querySelector('[data-action=cycle]').click(); document.querySelector('[data-action=finishCycle]').click();")
        ui.append(check(client.evaluate('AL.game.tanks[0].bacteria>=.99'), 'Guided preparation and fishless cycling work'))
        client.evaluate("document.getElementById('store-quick').click(); document.querySelector('[data-action=inspectSpecies]').click(); document.querySelector('form[data-form=buyFish]').requestSubmit();")
        ui.append(check(client.evaluate('AL.game.tanks[0].fish.length===1'), 'Species compatibility dialog purchases a resident'))
        client.evaluate("document.getElementById('feed-quick').click(); document.querySelector('form[data-form=feed]').requestSubmit(); AL.Sim.advance(AL.game,60);")
        ui.append(check(client.evaluate('AL.game.tanks[0].fish[0].hunger<25'), 'Feeding form results in actual food consumption'))
        for nav in ['aquariums','collection','store','black','breeding','equipment','food','flora','quests','marketplace','achievements','vip','settings']:
            client.evaluate(f"document.querySelector('[data-page={nav}]').click()")
            ui.append(check(client.evaluate("document.getElementById('management').textContent.trim().length > 50"), f'{nav} navigation renders functional content'))
        client.evaluate("AL.UI.goto('store');")
        for category in ['fish','tanks','equipment','food','flora','supplies','decor','eggs']:
            client.evaluate(f"document.querySelector('[data-action=category][data-args*=\"{category}\"]').click()")
            ui.append(check(client.evaluate("document.getElementById('management').querySelectorAll('.item-card').length>0"), f'{category} store category renders'))
        client.evaluate("AL.UI.goto('quests'); document.querySelector('[data-action=claim]:not(:disabled)').click(); AL.UI.save();")
        money = client.evaluate('AL.game.credits')
        client.call('Page.reload')
        time.sleep(.3)
        ui.append(check(client.evaluate('AL.game.credits') == money, 'Browser reload preserves wallet and quest transaction'))
        client.evaluate("AL.Save.validate(AL.game)")
        # Exercise the real download/import flow without changing the user's browser profile.
        downloads=ROOT/'tests'/'downloads'
        downloads.mkdir(exist_ok=True)
        client.call('Browser.setDownloadBehavior', {'behavior':'allow','downloadPath':str(downloads)})
        client.evaluate("AL.UI.goto('settings'); document.querySelector('[data-action=export]').click()")
        exported=None
        for _ in range(100):
            files=list(downloads.glob('aquarium-life-day-*.json'))
            if files:
                exported=max(files,key=lambda p:p.stat().st_mtime)
                break
            time.sleep(.05)
        ui.append(check(exported is not None, 'Export button downloads a JSON backup'))
        exported_state=json.loads(exported.read_text(encoding='utf-8'))
        ui.append(check(exported_state['credits']==money, 'Exported file contains the actual wallet'))
        client.evaluate('AL.game.credits=123;')
        document=client.call('DOM.getDocument')
        node=client.call('DOM.querySelector', {'nodeId':document['root']['nodeId'],'selector':'#import-file'})
        client.call('DOM.setFileInputFiles', {'nodeId':node['nodeId'],'files':[str(exported)]})
        for _ in range(100):
            if client.evaluate("!!document.querySelector('[data-action=commitImport]')"):
                break
            time.sleep(.03)
        client.evaluate("document.querySelector('[data-action=commitImport]').click()")
        ui.append(check(client.evaluate('AL.game.credits')==money, 'Import validates and restores the exported game'))
        # Force a corrupt primary save while retaining the previous good backup.
        client.evaluate("AL.UI.save(); AL.Save.save=()=>({ok:true,message:'Test corruption'}); localStorage.setItem('aquarium-life-v2','{corrupt');")
        client.call('Page.reload')
        time.sleep(.3)
        ui.append(check(client.evaluate("AL.Save.locked && document.getElementById('dialog').open && localStorage.getItem('aquarium-life-v2')==='{corrupt'"), 'Corrupt primary save is preserved and recovery UI opens'))
        client.evaluate("document.querySelector('[data-action=recover]').click()")
        ui.append(check(client.evaluate('!AL.Save.locked && AL.game.tanks[0].fish.length===1'), 'Recovery restores previous valid save without duplicating fish'))
        client.evaluate("AL.UI.goto('equipment'); document.querySelector('[data-action=buyEquipment]:not(:disabled)').click()")
        ui.append(check(client.evaluate("AL.Core.has(AL.game.tanks[0],'air')"), 'Equipment installation updates the actual tank'))
        client.evaluate("document.getElementById('water-quick').click(); document.querySelector('[data-action=waterChange]').click()")
        ui.append(check(client.evaluate('AL.game.stats.waterChanges>0'), 'Water laboratory executes a prepared change'))
        client.evaluate("AL.UI.goto('store','tanks'); document.querySelector('[data-action=configureTank]').click(); document.querySelector('form[data-form=buyTank]').requestSubmit()")
        ui.append(check(client.evaluate('AL.game.tanks.length===2'), 'Tank configuration purchases an independent aquarium'))
        client.evaluate("AL.game.selectedTank=AL.game.tanks[0].id; AL.UI.render(); AL.UI.inspectFish(AL.game.tanks[0].fish[0].id)")
        ui.append(check(client.evaluate("document.querySelector('form[data-form=renameFish]')!==null"), 'Individual fish inspection exposes name and lineage'))
        client.evaluate("document.getElementById('dialog-close').click()")
        client.evaluate("AL.game=AL.Core.act(AL.game,'buyFish',{species:'neon',count:6}); AL.game=AL.Core.act(AL.game,'buyFish',{species:'guppy',count:1}); for(const type of ['fern','sword','vallis','anubias','moss','crypt']) AL.game=AL.Core.act(AL.game,'buyFlora',{type}); AL.game.settings.speed=0; AL.UI.goto('aquariums'); AL.renderer.draw(AL.game,1/60);")
        client.evaluate("AL.game.time=Math.floor(AL.game.time/1440)*1440+600; document.getElementById('toast').className=''; AL.UI.render();")
        render_ms=client.evaluate("(()=>{AL.renderer.draw(AL.game,1/60);const start=performance.now();for(let i=0;i<60;i++)AL.renderer.draw(AL.game,1/60);return (performance.now()-start)/60})()")
        unchanged=client.evaluate("(()=>{const before=JSON.stringify(AL.game);AL.renderer.draw(AL.game,1/60);return before===JSON.stringify(AL.game)})()")
        ui.append(check(unchanged, 'Rendering and interpolation never mutate simulation state'))
        client.call('Emulation.setDeviceMetricsOverride', {'width':1600,'height':1050,'deviceScaleFactor':1,'mobile':False})
        def choose_light(mode):
            client.evaluate(f"(()=>{{const control=document.getElementById('tank-light-mode');control.value='{mode}';control.dispatchEvent(new Event('change',{{bubbles:true}}));AL.renderer.draw(AL.game,0)}})()")
        def luminance():
            return client.evaluate("(()=>{const p=AL.renderer.g.getImageData(0,0,480,240).data;let total=0;for(let i=0;i<p.length;i+=4)total+=p[i]*.2126+p[i+1]*.7152+p[i+2]*.0722;return total/(p.length/4)})()")
        choose_light('off')
        off_brightness=luminance()
        ui.append(check(client.evaluate("AL.Sim.light(AL.game,AL.Core.selected(AL.game))===0 && document.getElementById('tank-light-status').textContent==='Light off'"), 'Visible Off control switches the tank light off'))
        off_shot=client.call('Page.captureScreenshot', {'format':'png','captureBeyondViewport':False})
        (ROOT/'tests'/f'{NAME}-light-off.png').write_bytes(base64.b64decode(off_shot['data']))
        client.call('Page.reload')
        time.sleep(.3)
        ui.append(check(client.evaluate("AL.Core.selected(AL.game).lightMode==='off' && document.getElementById('tank-light-mode').value==='off'"), 'Manual light choice survives save and browser reload'))
        choose_light('on')
        on_brightness=luminance()
        ui.append(check(on_brightness>off_brightness*1.35, 'On visibly increases rendered aquarium brightness'))
        on_shot=client.call('Page.captureScreenshot', {'format':'png','captureBeyondViewport':False})
        (ROOT/'tests'/f'{NAME}-light-on.png').write_bytes(base64.b64decode(on_shot['data']))
        client.evaluate('AL.game.time=Math.floor(AL.game.time/1440)*1440; AL.UI.updateVitals(); AL.renderer.draw(AL.game,0)')
        night_on=luminance()
        ui.append(check(client.evaluate('AL.Sim.light(AL.game,AL.Core.selected(AL.game))>0'), 'Manual On lights the aquarium at night'))
        choose_light('auto')
        ui.append(check(client.evaluate('AL.Sim.light(AL.game,AL.Core.selected(AL.game))===0') and luminance()<night_on, 'Auto restores the night-time lighting schedule'))
        choose_light('on')
        client.evaluate("document.querySelectorAll('[data-tank]')[1].click()")
        ui.append(check(client.evaluate("document.getElementById('tank-light-mode').value==='auto'"), 'Changing tanks displays that aquarium’s own lighting mode'))
        choose_light('off')
        client.evaluate("document.querySelectorAll('[data-tank]')[0].click()")
        ui.append(check(client.evaluate("document.getElementById('tank-light-mode').value==='on'"), 'Changing one tank’s lighting does not change another tank'))
        choose_light('auto')
        client.evaluate("AL.game.time=Math.floor(AL.game.time/1440)*1440+600;document.getElementById('toast').className='';AL.UI.updateVitals()")
        client.evaluate('AL.renderer.draw(AL.game,1/60)')
        shot=client.call('Page.captureScreenshot', {'format':'png','captureBeyondViewport':False})
        (ROOT/'tests'/f'{NAME}-aquarium-preview.png').write_bytes(base64.b64decode(shot['data']))
        for width in [1600,1024,760,390]:
            client.call('Emulation.setDeviceMetricsOverride', {'width':width,'height':1000,'deviceScaleFactor':1,'mobile':False})
            ui.append(check(client.evaluate('document.documentElement.scrollWidth <= innerWidth'), f'No horizontal overflow at {width}px'))
        ui.append(check(client.evaluate("getComputedStyle(document.body).backgroundColor==='rgb(8, 11, 16)' && getComputedStyle(document.querySelector('.panel')).backgroundColor==='rgb(52, 70, 92)'"), 'Locked near-black background and slate-blue panel palette are applied'))
        # Coral-only reef fixture exercises the actual placement and inspection controls.
        client.call('Emulation.setDeviceMetricsOverride', {'width':1600,'height':1050,'deviceScaleFactor':1,'mobile':False})
        client.evaluate("AL.game=AL.Core.newGame('marine');AL.game=AL.Core.act(AL.game,'prepare');AL.game=AL.Core.act(AL.game,'cycle');AL.Sim.advance(AL.game,2165);AL.game.settings.speed=0;AL.game.time=600;AL.UI.goto('flora');AL.renderer.draw(AL.game,0)")
        # Browser mouse events quantize CSS coordinates; assertions allow one CSS pixel.
        def click_world(x,y):
            point=client.evaluate(f"(()=>{{const r=document.getElementById('aquarium').getBoundingClientRect();return {{x:r.left+(({x}-AL.renderer.pan)*AL.renderer.zoom+.5)*r.width,y:r.top+(({y}-.5)*AL.renderer.zoom+.5)*r.height}}}})()")
            client.call('Input.dispatchMouseEvent', {'type':'mouseMoved','x':point['x'],'y':point['y']})
            client.call('Input.dispatchMouseEvent', {'type':'mousePressed','x':point['x'],'y':point['y'],'button':'left','clickCount':1})
            client.call('Input.dispatchMouseEvent', {'type':'mouseReleased','x':point['x'],'y':point['y'],'button':'left','clickCount':1})
        coral_money=client.evaluate('AL.game.credits')
        client.evaluate("document.querySelector('[data-action=beginCoral]').click()")
        ui.append(check(client.evaluate('AL.UI.placing && AL.game.tanks[0].flora.length===0 && AL.game.credits')==coral_money, 'Coral placement preview does not spend funds before placement'))
        client.evaluate("document.getElementById('cancel-placement').click()")
        ui.append(check(client.evaluate(f'!AL.UI.placing && AL.game.credits==={coral_money} && AL.game.tanks[0].flora.length===0'), 'Canceling a coral purchase leaves funds and ownership unchanged'))
        client.evaluate("document.querySelector('[data-action=beginCoral]').click();AL.renderer.draw(AL.game,0)")
        # Position the viewport before dispatching real pointer events.
        client.evaluate("document.getElementById('aquarium').scrollIntoView({block:'center',behavior:'instant'})")
        click_world(.64,.82)
        ui.append(check(client.evaluate("!AL.UI.placing && AL.game.tanks[0].flora.length===1 && Math.abs(AL.game.tanks[0].flora[0].x-.64)<.003 && Math.abs(AL.game.tanks[0].flora[0].y-.82)<.003"), 'Pointer placement buys coral at the chosen horizontal and vertical position'))
        click_world(.64,.82)
        ui.append(check(client.evaluate('AL.game.tanks[0].flora.length===1'), 'Repeated placement clicks do not duplicate coral'))
        client.evaluate('AL.renderer.draw(AL.game,0)')
        box=client.evaluate("AL.renderer.hitboxes.find(b=>b.kind==='flora')")
        center=client.evaluate(f"AL.renderer.worldPoint({box['x']},{box['y']})")
        click_world(center['x'],center['y'])
        ui.append(check(client.evaluate("document.getElementById('dialog').open && document.getElementById('flora-info-panel').textContent.includes('Health') && document.getElementById('flora-info-panel').textContent.includes('Age')"), 'Selecting a living coral opens its individual Overview tab'))
        client.evaluate("document.querySelector('[data-action=floraTab][data-args*=care]').click()")
        ui.append(check(client.evaluate("document.getElementById('flora-info-panel').textContent.includes('Water flow') && document.getElementById('flora-info-panel').textContent.includes('Calcium')"), 'Coral Care tab shows actual light, flow and mineral requirements'))
        client.evaluate("document.getElementById('flora-tab-care').dispatchEvent(new KeyboardEvent('keydown',{key:'ArrowLeft',bubbles:true}))")
        ui.append(check(client.evaluate("document.activeElement.id==='flora-tab-overview' && document.getElementById('flora-info-panel').textContent.includes('Health')"), 'Coral information tabs support arrow-key navigation and focus'))
        client.evaluate("document.getElementById('flora-tab-overview').dispatchEvent(new KeyboardEvent('keydown',{key:'End',bubbles:true}))")
        coral_info=client.call('Page.captureScreenshot', {'format':'png','captureBeyondViewport':False})
        (ROOT/'tests'/f'{NAME}-coral-info.png').write_bytes(base64.b64decode(coral_info['data']))
        client.evaluate("document.querySelector('#dialog-body [data-action=positionFlora]').click();document.getElementById('aquarium').scrollIntoView({block:'center',behavior:'instant'});AL.renderer.zoom=1.5;AL.renderer.pan=.6;AL.renderer.draw(AL.game,0)")
        click_world(.74,.68)
        ui.append(check(client.evaluate("AL.game.tanks[0].flora.length===1 && Math.abs(AL.game.tanks[0].flora[0].x-.74)<.003 && Math.abs(AL.game.tanks[0].flora[0].y-.68)<.003"), 'Coral repositioning respects camera zoom and pan without repurchasing'))
        client.evaluate("document.querySelector('[data-action=positionFlora]').click();document.getElementById('aquarium').dispatchEvent(new KeyboardEvent('keydown',{key:'ArrowLeft',bubbles:true}));document.dispatchEvent(new KeyboardEvent('keydown',{key:'Escape',bubbles:true}))")
        ui.append(check(client.evaluate("!AL.UI.placing && Math.abs(AL.game.tanks[0].flora[0].x-.74)<.003"), 'Escape cancels a reposition preview without changing the colony'))
        client.evaluate("document.querySelector('[data-action=positionFlora]').click();document.getElementById('aquarium').dispatchEvent(new KeyboardEvent('keydown',{key:'ArrowLeft',bubbles:true}));document.getElementById('aquarium').dispatchEvent(new KeyboardEvent('keydown',{key:'Enter',bubbles:true}))")
        ui.append(check(client.evaluate("!AL.UI.placing && Math.abs(AL.game.tanks[0].flora[0].x-.72)<.003"), 'Keyboard arrows and Enter place an existing coral'))
        client.call('Page.reload')
        time.sleep(.3)
        ui.append(check(client.evaluate("AL.game.tanks[0].flora.length===1 && Math.abs(AL.game.tanks[0].flora[0].x-.72)<.003 && Math.abs(AL.game.tanks[0].flora[0].y-.68)<.003"), 'Saved coral position and identity survive browser reload'))
        client.evaluate("AL.UI.goto('flora');document.querySelector('[data-action=beginCoral]').click();AL.renderer.draw(AL.game,0)")
        for width in [1600,390]:
            client.call('Emulation.setDeviceMetricsOverride', {'width':width,'height':1050,'deviceScaleFactor':1,'mobile':False})
            ui.append(check(client.evaluate('document.documentElement.scrollWidth <= innerWidth'), f'Coral placement interface fits at {width}px'))
        client.call('Emulation.setDeviceMetricsOverride', {'width':1600,'height':1050,'deviceScaleFactor':1,'mobile':False})
        client.evaluate("document.getElementById('aquarium').scrollIntoView({block:'center',behavior:'instant'});AL.renderer.draw(AL.game,0)")
        coral_placement=client.call('Page.captureScreenshot', {'format':'png','captureBeyondViewport':False})
        (ROOT/'tests'/f'{NAME}-coral-placement.png').write_bytes(base64.b64decode(coral_placement['data']))
        client.evaluate("document.getElementById('cancel-placement').click()")
        # The user-assigned Ocellaris artwork must work in the real game, including file:// thumbnails.
        ui.append(check(client.evaluate("AL.Art.clownfishArtLoaded && AL.Data.species.clown.scientificName==='Amphiprion ocellaris'"), 'Assigned artwork loads for the existing Ocellaris species ID'))
        ui.append(check(client.evaluate("(()=>{const frames=[0,1,2,3].map(f=>AL.Art.sprite('clown',f,1));return frames.every(c=>c.width===128&&c.height===80)&&new Set(frames.map(c=>c.toDataURL())).size===4&&frames[0].toDataURL()!==AL.Art.legacySprite('clown').toDataURL()})()"), 'Ocellaris uses four distinct transparent artwork frames with exportable thumbnails'))
        client.evaluate("AL.game=AL.Core.act(AL.game,'buyFish',{species:'clown',count:1});AL.game.settings.speed=0;AL.game.tanks[0].fish[0].x=.5;AL.game.tanks[0].fish[0].y=.4;AL.UI.goto('store','fish')")
        ui.append(check(client.evaluate("Array.from(document.querySelectorAll('.item-card')).some(c=>c.textContent.includes('Ocellaris clownfish')&&c.querySelector('img')?.src===AL.Art.thumb('clown'))"), 'Store card displays the assigned Ocellaris artwork'))
        client.evaluate("AL.UI.inspectFish(AL.game.tanks[0].fish[0].id)")
        ui.append(check(client.evaluate("(()=>{const img=document.querySelector('#dialog-body img');return img.decode().then(()=>img.naturalWidth===128&&img.naturalHeight===80&&img.src===AL.Art.thumb('clown'))})()"), 'Individual Ocellaris inspection displays the assigned artwork'))
        shot=client.call('Page.captureScreenshot', {'format':'png','captureBeyondViewport':False})
        (ROOT/'assets/previews'/f'{NAME}-ocellaris-inspector.png').write_bytes(base64.b64decode(shot['data']))
        client.evaluate("document.getElementById('dialog-close').click();AL.UI.goto('aquariums');document.getElementById('aquarium').scrollIntoView({block:'center',behavior:'instant'});AL.renderer.zoom=1;AL.renderer.draw(AL.game,0);AL.UI.save()")
        shot=client.call('Page.captureScreenshot', {'format':'png','captureBeyondViewport':False})
        (ROOT/'assets/previews'/f'{NAME}-ocellaris-tank.png').write_bytes(base64.b64decode(shot['data']))
        client.call('Page.reload');time.sleep(.3)
        ui.append(check(client.evaluate("AL.Art.clownfishArtLoaded && AL.game.tanks[0].fish.length===1 && AL.game.tanks[0].fish[0].species==='clown'"), 'Saved Ocellaris keeps its species identity and assigned artwork after reload'))
        errors=[e for e in client.events if e.get('method')=='Runtime.exceptionThrown']
        requests=[e['params']['request']['url'] for e in client.events if e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('http:','https:'))]
        ui.append(check(not errors, 'No browser JavaScript exceptions'))
        ui.append(check(not requests, 'No HTTP or HTTPS gameplay requests while offline'))
        report.update({'uiChecks':ui,'browserErrors':errors,'networkRequests':requests,'screenshot':f'{NAME}-aquarium-preview.png','renderMillisecondsPerFrame':render_ms,'lightingBrightness':{'on':on_brightness,'off':off_brightness}})
        print(f'{len(ui)} UI/browser checks passed', flush=True)
        (ROOT/'tests'/f'{NAME}-results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
        return 1 if report['failed'] else 0
    finally:
        if client:
            try:
                client.call('Browser.close')
            except (OSError, RuntimeError, json.JSONDecodeError):
                pass
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.terminate()
        log.close()

if __name__=='__main__':
    sys.exit(main())
