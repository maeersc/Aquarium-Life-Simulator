"""Test the generated DIST at an HTTP repository subpath, including local saves."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from urllib.parse import urlsplit
import base64
import hashlib
import json
import time
import urllib.request

PREFIX = '/aquarium-life/'


def run(c, root, name):
    # This suite includes cold native-sheet validation and large deterministic
    # diving Monte Carlo batches; allow those test evaluations to finish.
    c.sock.settimeout(300)
    out = root / 'tests/pages-evidence'
    out.mkdir(exist_ok=True)
    dist = root / 'DIST'
    requests = []
    results = []

    class Handler(SimpleHTTPRequestHandler):
        def do_GET(self):
            original = self.path
            requests.append({'method': 'GET', 'path': original})
            if not urlsplit(original).path.startswith(PREFIX):
                # Browsers may request the hostname's default favicon.
                self.send_error(404)
                return
            self.path = '/' + original[len(PREFIX):]
            super().do_GET()

        def do_POST(self):
            requests.append({'method': 'POST', 'path': self.path})
            self.send_error(405)

        def log_message(self, *args):
            pass

    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(Handler, directory=str(dist)))
    Thread(target=server.serve_forever, daemon=True).start()
    origin = f'http://127.0.0.1:{server.server_port}'
    url = origin + PREFIX + 'index.html'

    def check(label, expression=None, value=None, client=c):
        try:
            ok = bool(client.evaluate(expression)) if expression is not None else bool(value)
            results.append({'name': label, 'pass': ok})
        except Exception as error:
            results.append({'name': label, 'pass': False, 'error': str(error)})

    def wait(expression, client=c, seconds=15):
        until = time.monotonic() + seconds
        while time.monotonic() < until:
            try:
                if client.evaluate(expression):
                    return
            except RuntimeError:
                pass
            time.sleep(.05)
        raise RuntimeError(f'Timed out: {expression}')

    def navigate(address, client=c):
        client.call('Page.navigate', {'url': address})
        wait("document.readyState==='complete'&&!!window.AL?.game&&!!AL.ExpansionUI", client)

    browser_client = isolated = local_file = None
    file_target = None
    file_context = None
    context = None
    try:
        manifest = json.loads((dist / 'build-manifest.json').read_text(encoding='utf-8'))
        if manifest.get('production'):
            private=json.loads((root/'planning/distribution-protection/evidence/build-private.json').read_text(encoding='utf8'))
            check('All protected outputs match their manifest and unchanged development inputs', value=all(
                hashlib.sha256((dist/f['path']).read_bytes()).hexdigest()==f['sha256'] for f in manifest['files']) and
                private['buildId']==manifest['buildId'] and all(
                    hashlib.sha256((root/f['input']).read_bytes()).hexdigest()==f['inputSha256'] and
                    hashlib.sha256((dist/f['output']).read_bytes()).hexdigest()==f['sha256'] for f in private['files']))
        else:
            check('All published files match the current source and build manifest', value=all(
                hashlib.sha256((dist/f['path']).read_bytes()).hexdigest() == f['sha256']
                == hashlib.sha256((root/f['path']).read_bytes()).hexdigest()
                for f in manifest['files']))
        check('No test profiles, development archives or player saves in DIST', value=all(
            Path(f['path']).parts[0] in {'assets','js','css'} or
            (len(Path(f['path']).parts)==1 and f['path'] in {'index.html','LICENSE.txt','.nojekyll'}) or
            (not manifest.get('production') and len(Path(f['path']).parts)==1 and Path(f['path']).suffix in {'.html','.md'})
            for f in manifest['files']))
        check('Pages index and .nojekyll are present', value=(dist/'index.html').is_file() and (dist/'.nojekyll').is_file())
        navigate(url)
        check('DIST loads at a GitHub Pages-style HTTP repository subpath', 'location.pathname==="/aquarium-life/index.html"&&!!AL.renderer')
        wait('AL.DivingArt?.loaded===17')
        check('Built destination art decodes all 17 offline records without errors', 'AL.DivingArtData.length===17&&!AL.DivingArt.errors.length')
        for region, entry in json.loads((root/'assets/diving/registry.json').read_text(encoding='utf8'))['regions'].items():
            for mode in entry.get('modes',['reef','deep']):
                key = region+'-'+mode
                check('Built destination identity and environment: '+key, "(()=>{const art=AL.DivingArt.scene("+json.dumps(region)+','+json.dumps(mode)+"),im=AL.DivingArt.image(art.id),canvas=document.createElement('canvas');canvas.width=880;canvas.height=560;return art.id==="+json.dumps(key)+"&&im.complete&&im.naturalWidth>0&&AL.DivingArt.source("+json.dumps(region)+','+json.dumps(mode)+")===im.src&&AL.DivingArt.environment(canvas.getContext('2d'),"+json.dumps(region)+','+json.dumps(mode)+",880,560);})()")
                check('Native PNG URL loads at Pages repository subpath: '+key, "new Promise(resolve=>{const im=new Image();im.onload=()=>resolve(im.naturalWidth>0);im.onerror=()=>resolve(false);im.src="+json.dumps(entry['art'][mode]['path'])+";})")
        check('A new browser/origin starts without someone else\'s saved game', "localStorage.getItem('aquarium-life-v2')===null&&document.getElementById('startup-title').textContent.includes('Welcome to')")
        check('All v2.7 livestock and embedded art load from DIST', 'AL.Expansion.records.length===38&&Object.keys(AL.Data.species).length===105&&AL.ExpansionArt.loaded===73&&AL.ExpansionArt.errors.length===0')
        check('Built current game loads the financial, fragging and shared research services', '!!AL.Finance&&!!AL.Update31&&!!AL.Update31UI&&!!AL.Research&&AL.Research.catalog().length===94&&document.getElementById("finance-open").tagName==="BUTTON"')
        check('Built game includes casino, physical inventory, category filters and the six-item sidebar', '!!AL.CasinoUI&&!!AL.Casino&&!!AL.InventoryUI&&!!AL.Inventory&&!!AL.EquipmentCatalog&&AL.CasinoRules.probabilities("gold").returnRate===1.522&&document.querySelectorAll("#navigation [data-page]").length===6&&!!document.getElementById("equipment-filter")')
        check('Built new-profile wallet has a valid5,000-AC opening plus250-AC first-size award', 'AL.game.credits===5250&&AL.Finance.summary(AL.game).closing===5250&&AL.Save.validate(AL.game)===AL.game')
        check('Built research transaction atomically charges exactly 5 AC once', "(()=>{const owned=JSON.parse(JSON.stringify(AL.game));owned.tanks[0].fish.push(AL.Core.fish(owned,'gramma'));delete owned.progression;AL.Progression.migrate(owned);const s=AL.Core.act(owned,'buyResearch',{species:'gramma'}),r=AL.Core.act(s,'buyResearch',{species:'gramma'});return r.credits===AL.game.credits-5&&r.research.unlocks.gramma&&r.finance.rows.filter(t=>t.category==='research').length===1;})()")
        check('Built survival policy pays 100 with the preserved twenty-minute game day', 'AL.Update29.survivalAmount===100&&AL.Config.minutesPerSecond*1200===1440&&AL.game.update29.survival.policyVersion===2')
        check('Existing sprite banks load from DIST', '!!AL.Art.ready&&[AL.AssetBank,AL.LifeStages,AL.ClownArt].every(b=>b.errors.length===0&&b.loaded===b.records.length)')
        # Meaningful existing expansion checks run against the actual built HTTP
        # payload, not source files; the test fixture itself stays outside DIST.
        c.evaluate('AL.Startup.finish();AL.game.settings.speed=0;AL.UI.close();AL.Store.close();AL.Shell.close()')
        check('Built current-version mystery authority, silhouette and recovery actions load at the repository URL', '!!AL.DiveMystery&&!!AL.DivingArt.mystery&&!!AL.DivingArt.reveal&&AL.DivingData.species.length===9&&document.querySelector(".version").textContent.includes('+json.dumps(manifest['gameContent'])+')')
        expected_clips=[{'path':clip['path'],'sha256':clip['sha256']} for entry in json.loads((root/'assets/animation/livestock-registry.json').read_text(encoding='utf8'))['entries'] for clip in entry['clips']]
        check('Hosted shared registry preserves119 records and113 usable production identities','!!AL.FishAnimation.sheets&&AL.FishAnimation.catalog.entries.length===119&&AL.FishAnimation.catalog.entries.filter(e=>e.productionEligible).length===113&&Object.values(AL.FishAnimation.auditCatalog()).every(a=>!a.length)&&AL.FishAnimation.catalog.entries.every(e=>e.framesCompleted===e.clips.reduce((n,c)=>n+c.frameCount,0))')
        check('Hosted production clip paths and hashes match the actual current central registry','JSON.stringify(AL.FishAnimation.catalog.entries.flatMap(e=>e.clips.map(c=>({path:c.path,sha256:c.sha256}))))==='+json.dumps(json.dumps(expected_clips,separators=(',',':'))))
        check('Every hosted production sheet decodes16 actual distinct cells',"(async()=>{const A=AL.FishAnimation;for(const e of A.catalog.entries)for(const clip of e.clips){const record=A.sheets.find(e.id,clip.stage,clip.state,clip.variety);if(!await A.sheets.load(record))return false;}return !A.sheets.issues.length;})()")
        for clip in expected_clips:
            check('Native production PNG resolves at the Pages repository subpath: '+clip['path'],"new Promise(resolve=>{const im=new Image();im.onload=()=>resolve(im.naturalWidth>0);im.onerror=()=>resolve(false);im.src="+json.dumps(clip['path'])+";})")
        results.extend(c.evaluate((root/'tests/diving_checks.js').read_text(encoding='utf8')))
        results.extend(c.evaluate((root/'tests/diving_resale_checks.js').read_text(encoding='utf8')))
        results.extend(c.evaluate((root/'tests/mystery_diving_checks.js').read_text(encoding='utf8'))['checks'])
        check('Built receiving repair exposes all destinations and exact compatibility checks', '!!AL.DiveReceiving&&!!AL.DiveReceiving.destinations&&!!AL.DiveReceiving.holding')
        results.extend(c.evaluate((root/'tests/receiving_checks.js').read_text(encoding='utf8'))['checks'])
        check('Built universal receiving covers every registered fish, coral and invertebrate host', 'AL.Diving.profileValid&&AL.DiveReceiving.registryAudit().length===0&&AL.DiveReceiving.resolve("pavona-cactus").kind==="coral"&&AL.DiveReceiving.resolve("porcelain-anemone-crab").kind==="invertebrate"')
        results.extend(c.evaluate((root/'tests/global_receiving_checks.js').read_text(encoding='utf8'))['checks'])
        check('Built diving expansion is loaded', '!!AL.DiveExpansion&&!!AL.DiveExpansion.emergencyQuote')
        results.extend(c.evaluate((root/'tests/diving_expansion_checks.js').read_text(encoding='utf8'))['checks'])
        check('Built shared aquarium preparation authority is loaded', '!!AL.Preparation&&!!AL.Preparation.state&&!!AL.Preparation.migrate')
        check('Built marine animation profiles cover every current fish', '!!AL.FishAnimation&&Object.keys(AL.FishAnimation.data.species).length===94&&!AL.FishAnimation.audit().length')
        results.extend(c.evaluate((root/'tests/fish_animation_checks.js').read_text(encoding='utf8'))['checks'])
        results.extend(c.evaluate((root/'tests/preparation_checks.js').read_text(encoding='utf8'))['checks'])
        results.extend(c.evaluate((root/'tests/expansion_checks.js').read_text(encoding='utf-8')))
        check('Built game contains the repaired marine care, mortality and readiness modules', '!!AL.MarineCare&&!!AL.Mortality&&!!AL.OvernightUI&&AL.game.marineCareVersion===1')
        check('Built permanent journal and seven heater levels are loaded at the repository URL', '!!AL.MortalityUI&&!!AL.Thermal&&AL.Heaters.models.length===7&&AL.Heaters.models.at(-1).maxGallons===15000&&AL.game.mortality.journalVersion===1')
        c.evaluate("AL.game=AL.Core.newGame('marine',447799);delete AL.game.marineCareVersion;window.qaOriginalRaw=JSON.stringify(AL.game);localStorage.setItem('aquarium-life-v2',qaOriginalRaw);AL.game=AL.Save.load().state;AL.Shell.open('settings','preferences')")
        check('Hosted legacy load preserves an exact original snapshot before migration', 'AL.Save.hasPreRepair(AL.game)&&localStorage.getItem("aquarium-life-before-overnight-repair-v1:"+AL.game.accountId)===qaOriginalRaw')
        pre_downloads=out/(name+'-downloads')/('pre-repair-'+str(time.time_ns()))
        pre_downloads.mkdir(parents=True,exist_ok=True)
        c.call('Browser.setDownloadBehavior',{'behavior':'allow','downloadPath':str(pre_downloads.resolve())})
        c.evaluate("document.querySelector('#primary-content [data-action=exportPreRepair]').click()")
        until=time.monotonic()+10
        while not list(pre_downloads.glob('*.json')) and time.monotonic()<until:time.sleep(.05)
        original_export=list(pre_downloads.glob('*.json'))
        check('Settings downloads the untouched pre-repair JSON onto this PC',value=bool(original_export) and original_export[0].read_text(encoding='utf-8')==c.evaluate('qaOriginalRaw'))
        check('Snapshot migration preserves original identities, wallet and selected aquarium', '(()=>{const old=JSON.parse(qaOriginalRaw);return old.accountId===AL.game.accountId&&old.credits===AL.game.credits&&old.selectedTank===AL.game.selectedTank;})()')
        c.evaluate("window.qaLoss=AL.Core.fish(AL.game,'clown');AL.game.tanks[0].fish.push(qaLoss);AL.Core.kill(AL.game,AL.game.tanks[0],qaLoss,'Unknown')")
        check('Hosted death writes the separate account-local permanent journal without changing credits', 'AL.Mortality.records(AL.game).length===1&&AL.game.credits===JSON.parse(qaOriginalRaw).credits&&!!localStorage.getItem("aquarium-life-mortality-v2:"+encodeURIComponent(AL.game.accountId)+":event:"+encodeURIComponent(qaLoss.deathRecordId))')
        c.evaluate('AL.Mortality.exportLog(AL.game)')
        until=time.monotonic()+10
        while not list(pre_downloads.glob('LIVESTOCK_MORTALITY_LOG*.json')) and time.monotonic()<until:time.sleep(.05)
        mortality_exports=list(pre_downloads.glob('LIVESTOCK_MORTALITY_LOG*.json'))
        check('Hosted mortality JSON export downloads actual account evidence to this PC',value=bool(mortality_exports) and json.loads(mortality_exports[0].read_text(encoding='utf-8'))['records'][0]['specimenId']==c.evaluate('qaLoss.id'))
        c.evaluate('AL.Shell.close()')
        c.evaluate("AL.UI.close();AL.Store.close();AL.Shell.close();AL.game=AL.Core.newGame('marine',445799);AL.game.settings.speed=0;AL.game.credits=4321;delete AL.game.finance;AL.Finance.initialize(AL.game);const extra=AL.Core.tank(AL.game,'marine',AL.Data.sizes[1].volume,'Pages local destination','display');AL.game.tanks.push(extra);AL.game.selectedTank=extra.id;extra.lightMode='off';delete AL.game.progression;AL.Progression.migrate(AL.game);AL.Save.migrate(AL.game);AL.UI.render();document.getElementById('save-button').click()")
        check('Save now writes the active game to device-local browser storage', "JSON.parse(localStorage.getItem('aquarium-life-v2')).credits===4321&&AL.Save.available")
        check('The offline timeline is also stored locally', "!!localStorage.getItem('aquarium-life-timeline-v1')")
        check('Saved selected aquarium and light preference are preserved', "(()=>{const s=JSON.parse(localStorage.getItem('aquarium-life-v2'));return s.tanks[1].id===s.selectedTank&&s.tanks[1].lightMode==='off';})()")
        c.evaluate("AL.game.tanks[1].name='Autosaved on this PC'")
        wait("JSON.parse(localStorage.getItem('aquarium-life-v2')).tanks[1].name==='Autosaved on this PC'", seconds=24)
        check('The real 20-second autosave persists locally without manual saving', "JSON.parse(localStorage.getItem('aquarium-life-v2')).tanks[1].name==='Autosaved on this PC'")
        c.evaluate("AL.Finance.change(AL.game,1,{name:'QA local-save fixture income'});document.getElementById('save-button').click()")
        check('Previous valid local save is retained as a recovery backup', "JSON.parse(localStorage.getItem('aquarium-life-backup')).credits===4321")
        navigate(url)
        check('Reload restores the same local wallet, destination and settings', "AL.game.credits===4322&&AL.game.tanks[1].name==='Autosaved on this PC'&&AL.game.selectedTank===AL.game.tanks[1].id&&AL.game.tanks[1].lightMode==='off'")
        check('Reload opens Welcome Back rather than resetting progress', "document.getElementById('startup-title').textContent.includes('Welcome Back')")
        c.evaluate("document.querySelector('[data-startup=continue]').click()")
        wait('!AL.Startup.pending&&!AL.Offline.busy')
        c.evaluate("AL.game.settings.speed=0;AL.Shell.open('settings','preferences')")
        check('Hosted Settings offers local JSON export/import and save recovery', "['Export JSON backup','Import JSON backup','Recover previous autosave'].every(s=>document.getElementById('primary-content').textContent.includes(s))")
        downloads = out / (name + '-downloads') / str(time.time_ns())
        downloads.mkdir(parents=True, exist_ok=True)
        c.call('Browser.setDownloadBehavior', {'behavior': 'allow', 'downloadPath': str(downloads.resolve())})
        existing = set(downloads.glob('*.json'))
        c.evaluate("document.querySelector('#primary-content [data-action=export]').click()")
        until = time.monotonic() + 10
        exported = None
        exported_state = None
        readiness_retries = 0
        while time.monotonic() < until:
            fresh = [p for p in downloads.glob('*.json') if p not in existing]
            if fresh:
                # Edge can expose the final filename while the download writer
                # or Windows scanner still holds it. Require a readable complete
                # JSON file within the existing deadline, not just its name.
                try:
                    candidate = max(fresh, key=lambda p: p.stat().st_mtime)
                    exported_state = json.loads(candidate.read_text(encoding='utf-8'))
                    exported = candidate
                    break
                except (PermissionError,FileNotFoundError,json.JSONDecodeError):
                    readiness_retries += 1
            time.sleep(.05)
        check('Export downloads a real JSON save file onto this PC', value=exported is not None)
        results[-1]['fileReadinessRetries'] = readiness_retries
        if exported:
            check('Downloaded backup contains this player\'s actual progress', value=exported_state['credits']==4322 and exported_state['tanks'][1]['name']=='Autosaved on this PC')
            c.evaluate('AL.game.credits=17')
            doc = c.call('DOM.getDocument')['root']['nodeId']
            node = c.call('DOM.querySelector', {'nodeId': doc, 'selector': '#import-file'})['nodeId']
            c.call('DOM.setFileInputFiles', {'files': [str(exported.resolve())], 'nodeId': node})
            wait('!!AL.pendingImport')
            check('Import validates a user-selected local backup before replacement', 'AL.pendingImport.credits===4322&&document.getElementById("dialog").open')
            c.evaluate("document.querySelector('[data-action=commitImport]').click()")
            wait('!AL.pendingImport&&!AL.Startup.pending')
            check('Confirmed local import restores the exported player progress', "AL.game.credits===4322&&AL.game.tanks[1].name==='Autosaved on this PC'")
        check('Blocked local storage gives an export warning instead of cloud saving', "(()=>{const original=Storage.prototype.setItem;let r;try{Storage.prototype.setItem=()=>{throw new DOMException('Test storage blocked','QuotaExceededError')};r=AL.Save.save(AL.game);}finally{Storage.prototype.setItem=original;}return !r.ok&&r.message.includes('Export a JSON backup');})()")
        c.evaluate('AL.Save.save(AL.game)')
        # A second independent browser context loads the exact same HTTP origin.
        # This verifies that save ownership belongs to the browser profile, not
        # the static hosting server or an origin-wide server-side player record.
        debug_port = 9337 if name == 'chrome' else 9338
        with urllib.request.urlopen(f'http://127.0.0.1:{debug_port}/json/version') as response:
            browser_url = json.load(response)['webSocketDebuggerUrl']
        browser_client = type(c)(browser_url)
        context = browser_client.call('Target.createBrowserContext')['browserContextId']
        target = browser_client.call('Target.createTarget', {'url': 'about:blank', 'browserContextId': context})['targetId']
        with urllib.request.urlopen(f'http://127.0.0.1:{debug_port}/json/list') as response:
            pages = json.load(response)
        isolated = type(c)(next(p['webSocketDebuggerUrl'] for p in pages if p['id']==target))
        for method in ['Runtime.enable', 'Page.enable', 'Network.enable']:
            isolated.call(method)
        navigate(url, isolated)
        check('Another browser profile at the same URL has no access to this player\'s save', "localStorage.getItem('aquarium-life-v2')===null&&AL.game.credits!==4322", client=isolated)
        isolated.evaluate('AL.Startup.finish();AL.game.settings.speed=0;AL.game.credits=99;delete AL.game.finance;delete AL.game.progression;AL.Finance.initialize(AL.game);AL.Progression.migrate(AL.game);AL.Save.save(AL.game)')
        check('Another profile writes only its own local save', "JSON.parse(localStorage.getItem('aquarium-life-v2')).credits===99", client=isolated)
        check('The original player\'s local progress stays unchanged', "JSON.parse(localStorage.getItem('aquarium-life-v2')).credits===4322")
        c.call('Network.emulateNetworkConditions', {'offline': True, 'latency': 0, 'downloadThroughput': 0, 'uploadThroughput': 0})
        check('Saving works with networking disabled after the hosted game loads', "AL.Save.save(AL.game).ok&&AL.Save.load().state.credits===4322")
        c.call('Network.emulateNetworkConditions', {'offline': False, 'latency': 0, 'downloadThroughput': -1, 'uploadThroughput': -1})
        screenshot = c.call('Page.captureScreenshot', {'format': 'png', 'captureBeyondViewport': False})
        (out/f'{name}-local-settings.png').write_bytes(base64.b64decode(screenshot['data']))
        # Direct extracted-folder use starts from a fresh tab, not a navigation
        # from the synthetic HTTP site after repeated network-emulation changes.
        # Preserve the tested HTTP player/profile and observe all file requests.
        browser_client.call('Target.disposeBrowserContext', {'browserContextId': context})
        context = None
        # The hosted save/profile is already tested and stays on disk. Release
        # its embedded sprite banks before the cold file-origin launch; keeping
        # two full game renderers resident can starve a small QA machine.
        c.call('Page.navigate', {'url':'about:blank'})
        wait("document.readyState==='complete'&&location.href==='about:blank'")
        # The file-origin smoke test also needs a clean profile: earlier suites
        # intentionally leave long-absence breeding/mortality fixtures in the
        # shared QA file:// storage. Those must not become this load-time test.
        file_context = browser_client.call('Target.createBrowserContext')['browserContextId']
        file_target = browser_client.call('Target.createTarget', {'url': 'about:blank', 'browserContextId':file_context})['targetId']
        with urllib.request.urlopen(f'http://127.0.0.1:{debug_port}/json/list') as response:
            pages = json.load(response)
        local_file = type(c)(next(p['webSocketDebuggerUrl'] for p in pages if p['id']==file_target))
        for method in ['Runtime.enable','Page.enable','Network.enable']:
            local_file.call(method)
        browser_client.call('Target.activateTarget', {'targetId':file_target})
        # This assertion is a clean extracted-folder first launch. Explicitly
        # clear only this throwaway QA target before app scripts, independently
        # of Chromium's file-origin storage/context implementation.
        local_file.call('Page.addScriptToEvaluateOnNewDocument', {'source':'localStorage.clear();'})
        local_file.call('Network.emulateNetworkConditions', {'offline': True, 'latency': 0, 'downloadThroughput': 0, 'uploadThroughput': 0})
        navigation = local_file.call('Page.navigate', {'url': (dist/'index.html').as_uri()})
        if navigation.get('errorText'):
            raise RuntimeError('Direct file navigation failed: '+str(navigation))
        file_load_started = time.monotonic()
        # Cold parsing/decoding of the pre-existing embedded sprite banks can
        # exceed15s after several full hosted-game context loads. Still require
        # complete game initialization and all17 scenery records, with a bounded
        # wait and measured duration; do not bypass a failed/missing script.
        wait("document.readyState==='complete'&&location.protocol==='file:'&&!!window.AL?.game&&AL.DivingArt.loaded===17",local_file,seconds=60)
        file_load_seconds = time.monotonic() - file_load_started
        check('DIST also runs directly from the player\'s extracted local folder', '!!AL.renderer&&AL.ExpansionArt.loaded===73&&!AL.DivingArt.errors.length',client=local_file)
        results[-1]['coldFileLoadSeconds'] = round(file_load_seconds,3)
        errors = [e for client in [c, isolated, local_file] for e in client.events if e.get('method')=='Runtime.exceptionThrown']
        requests_seen = [e['params']['request'] for client in [c, isolated, local_file] for e in client.events if e.get('method')=='Network.requestWillBeSent']
        external = [r['url'] for r in requests_seen if r['url'].startswith(('http:', 'https:')) and not r['url'].startswith(origin+'/')]
        check('No JavaScript exceptions in the built game/local save flows', value=not errors)
        check('No external service, analytics or save-upload network requests', value=not external and all(r.get('method') in ['GET','HEAD'] for r in requests_seen))
        check('The static server receives only file reads, never player-save writes', value=all(r['method']=='GET' for r in requests))
        bad = [e['params']['response']['url'] for client in [c, isolated, local_file] for e in client.events if e.get('method')=='Network.responseReceived' and e['params']['response']['status']>=400 and not e['params']['response']['url'].endswith('/favicon.ico')]
        check('All requested game resources resolve at the repository subpath', value=not bad)
    except Exception as error:
        results.append({'name': 'Pages/local-save integration completed', 'pass': False, 'error': str(error), 'diagnostic': c.evaluate("({toast:document.getElementById('toast')?.textContent,saveError:window.AL?.Save?.lastError,pendingImport:!!window.AL?.pendingImport,inputFiles:[...(document.getElementById('import-file')?.files||[])].map(f=>({name:f.name,size:f.size})),title:document.getElementById('startup-title')?.textContent})"), 'fileDiagnostic':local_file.evaluate("({url:location.href,ready:document.readyState,visible:document.visibilityState,game:!!window.AL?.game,art:window.AL?.DivingArt?.loaded,errors:window.AL?.DivingArt?.errors,title:document.getElementById('startup-title')?.textContent,resources:performance.getEntriesByType('resource').length})") if local_file else None})
    finally:
        if browser_client and file_target:
            browser_client.call('Target.closeTarget', {'targetId':file_target})
        if browser_client and file_context:
            browser_client.call('Target.disposeBrowserContext', {'browserContextId':file_context})
        if browser_client and context:
            browser_client.call('Target.disposeBrowserContext', {'browserContextId': context})
        server.shutdown()
        server.server_close()
    passed = sum(r['pass'] for r in results)
    failed = len(results) - passed
    (out/f'{name}-results.json').write_text(json.dumps({'browser':name,'passed':passed,'failed':failed,'results':results},indent=2),encoding='utf-8')
    print(f'{name}: {passed} Pages/DIST/local-save checks passed; {failed} failed')
    for result in results:
        if not result['pass']:
            print(result)
    return 1 if failed else 0
