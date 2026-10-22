"""Repeatable instrumented baseline/optimized samples in disposable browser data."""
import json,time,sys,platform,os,hashlib

def run(c,root,name):
 out=root/('tests/distribution-protection-evidence' if '--protection-soak' in sys.argv else 'tests/performance-evidence');out.mkdir(exist_ok=True)
 phase='before' if '--baseline' in sys.argv else 'after'
 c.sock.settimeout(180)
 entry=root/('DIST/index.html' if '--dist' in sys.argv else 'index.html')
 if '--snapshot' in sys.argv:
  import re
  html=(root/'planning/performance-optimization/baseline/index.html').read_text(encoding='utf8').replace('<head>','<head><base href="'+root.as_uri()+'/">',1)
  html=re.sub(r'src="js/([^"]+)"',r'src="planning/performance-optimization/baseline/js/\1"',html)
  entry=root/'tests/performance-baseline.html';entry.write_text(html,encoding='utf8')
 c.call('Page.addScriptToEvaluateOnNewDocument',{'source':"localStorage.clear();window.__long=[];new PerformanceObserver(list=>{for(const e of list.getEntries())__long.push({start:e.startTime,duration:e.duration});}).observe({type:'longtask',buffered:true});"})
 started=time.monotonic();c.navigate(entry,timeout=90)
 for _ in range(600):
  if c.evaluate('!!window.AL?.game&&!!AL.renderer'):break
  time.sleep(.05)
 else:raise RuntimeError('Game startup timed out')
 load=time.monotonic()-started
 fixture=json.loads((root/'tests/performance-evidence/fixture-small.json').read_text(encoding='utf8'))
 c.evaluate('window.__small='+json.dumps(fixture)+';'+(root/'tests/performance_probe.js').read_text(encoding='utf8'))
 if '--selection-probe' in sys.argv:
  c.evaluate((root/'tests/resident_sprite_checks.js').read_text(encoding='utf8'))
  for width,height in [(800,600),(1600,900)]:
   c.call('Emulation.setDeviceMetricsOverride',{'width':width,'height':height,'deviceScaleFactor':1,'mobile':False});time.sleep(.2)
   print(json.dumps(c.evaluate('(()=>{const out=[];for(const [id,stage,state] of [["blastomussa-wellsi","frag","polyp_motion"],["sexy-anemone-shrimp","baby","idle"]]){const entry=AL.FishAnimation.catalog.entries.find(e=>e.id===id);SpriteResidentQA.saveAndClick(entry,stage,state,()=>{});out.push({id,...SpriteResidentQA.lastClick});}return out})()')),flush=True)
  return 0
 if '--checks-only' in sys.argv:
  c.evaluate('__probe.fixture("A")');checks=c.evaluate((root/'tests/performance_checks.js').read_text(encoding='utf8'))
  import base64
  c.call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':900,'deviceScaleFactor':1,'mobile':False});c.evaluate('document.querySelector("[data-guide=acknowledge]")?.click();AL.Shell.open("settings");document.querySelector(".performance-settings").scrollIntoView({block:"center"})');time.sleep(.2)
  (out/(name+'-settings.png')).write_bytes(base64.b64decode(c.call('Page.captureScreenshot',{'format':'png'})['data']))
  (out/(name+'-checks.json')).write_text(json.dumps(checks,indent=2),encoding='utf8');print(json.dumps({'checks':len(checks),'failures':[x for x in checks if not x['pass']]}),flush=True);return int(any(not x['pass'] for x in checks))
 c.call('Performance.enable')
 if '--fixture-check' in sys.argv:
  for kind in ['A','B','C','D']:
   c.evaluate('__probe.fixture('+json.dumps(kind)+')')
   print(kind,c.evaluate('AL.Save.save(AL.game)'),flush=True)
  return 0
 def metrics():return {m['name']:m['value'] for m in c.call('Performance.getMetrics')['metrics']}
 def sample(label,seconds=7):
  c.evaluate('__probe.reset()');a=metrics();start=time.monotonic();time.sleep(seconds);b=metrics()
  r=c.evaluate('__probe.result()');r.update(label=label,wallSeconds=time.monotonic()-start,metrics={k:b.get(k,0)-a.get(k,0) for k in ['TaskDuration','ScriptDuration','LayoutDuration','RecalcStyleDuration']},heapBytes=b.get('JSHeapUsedSize'),nodes=b.get('Nodes'),listeners=b.get('JSEventListeners'))
  r['mainThreadCorePercent']=100*r['metrics']['TaskDuration']/r['wallSeconds']
  (out/(name+'-'+phase+'-'+label+'.json')).write_text(json.dumps(r,indent=2),encoding='utf8')
  print(json.dumps({k:v for k,v in r.items() if k not in ['calls','longTasks','caches']}),flush=True);return r
 def complex_scene():
  c.evaluate('__probe.fixture("C");(()=>{const s=AL.game,t=AL.Core.selected(s),rock=t.hardscape[0];for(let i=0;i<5;i++){const z=.15+i*.15;t.hardscape.push({...rock,id:AL.Core.id(s,"rock"),x:.14+i*.18,z,y:AL.Habitat.plane(t,z)+rock.baseOffset});}AL.Save.validate(s);})()');time.sleep(2);return sample('C-complex')
 if '--complex-only' in sys.argv:
  complex_scene();return 0
 if '--soak' in sys.argv:
  c.call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':900,'deviceScaleFactor':1,'mobile':False});c.evaluate('__probe.fixture("B")');time.sleep(3);c.evaluate('__probe.reset()');heaps=[];started=time.monotonic()
  for i in range(60):
   c.evaluate('__probe.menu('+json.dumps(['journal','equipment','store','settings'][i%4])+')');time.sleep(.5);c.evaluate('__probe.close()');time.sleep(4.5)
   if i%6==5:
    c.call('HeapProfiler.collectGarbage');m=metrics();row={'seconds':time.monotonic()-started,'heapBytes':m.get('JSHeapUsedSize'),'nodes':m.get('Nodes'),'listeners':m.get('JSEventListeners'),'caches':c.evaluate('__probe.result().caches')};heaps.append(row);print(json.dumps({k:v for k,v in row.items() if k!='caches'}),flush=True)
  result=c.evaluate('__probe.result()');result.update(entry=entry.relative_to(root).as_posix(),wallSeconds=time.monotonic()-started,heapSamples=heaps)
  result['checks']=[{'name':'Five-minute foreground navigation soak retains bounded pixel caches','pass':all(x['caches']['sheets']['frameBytes']<=x['caches']['sheets']['maxFrameBytes'] and x['caches']['sheets']['decodedBytes']<=x['caches']['sheets']['maxDecodedBytes'] for x in heaps)},{'name':'Post-warmup five-minute heap growth remains below2MiB','pass':heaps[-1]['heapBytes']-heaps[0]['heapBytes']<2*1024*1024},{'name':'Repeated menu navigation does not accumulate listeners','pass':max(x['listeners'] for x in heaps)-min(x['listeners'] for x in heaps)<15},{'name':'Normal periodic autosaves occur during sustained play','pass':result['calls'].get('save',{}).get('count',0)>=12}]
  (out/(name+'-soak.json')).write_text(json.dumps(result,indent=2),encoding='utf8');return int(any(not x['pass'] for x in result['checks']))
 rows=[]
 for scenario in ['A','B','C','D']:
  c.evaluate('__probe.fixture('+json.dumps(scenario)+')');time.sleep(2);rows.append(sample(scenario))
 if phase=='after':rows.append(complex_scene());c.evaluate('__probe.fixture("D")');time.sleep(2)
 # Profile actual visible scene, then covered views using the same scene.
 c.call('Profiler.enable');c.call('Profiler.start');time.sleep(4);profile=c.call('Profiler.stop')['profile']
 counts={}
 nodes={n['id']:n['callFrame'] for n in profile['nodes']}
 for i in profile.get('samples',[]):
  f=nodes[i];key=f['functionName']+' @ '+f['url'].split('/')[-1]+':'+str(f['lineNumber']+1);counts[key]=counts.get(key,0)+1
 for menu in ['store','journal','equipment','casino','diving','settings']:
  if menu=='casino':c.evaluate('__probe.fixture("A")')
  c.evaluate('__probe.menu('+json.dumps(menu)+')');rows.append(sample(menu,4));c.evaluate('__probe.close()')
 c.evaluate('__probe.fixture("B")')
 # A real browser-encoded local video substitute; no Netflix or audio claim.
 media=c.evaluate("""(async()=>{const cv=document.createElement('canvas');cv.width=640;cv.height=360;const g=cv.getContext('2d'),stream=cv.captureStream(30),rec=new MediaRecorder(stream,{mimeType:'video/webm'}),chunks=[];rec.ondataavailable=e=>chunks.push(e.data);const done=new Promise(r=>rec.onstop=r);rec.start();let n=0;const timer=setInterval(()=>{g.fillStyle=n++%2?'#345678':'#789abc';g.fillRect(0,0,640,360);g.fillStyle='#fff';g.fillRect(n*11%600,50,40,180)},33);await new Promise(r=>setTimeout(r,2200));clearInterval(timer);rec.stop();await done;stream.getTracks().forEach(t=>t.stop());const blob=new Blob(chunks,{type:'video/webm'}),v=document.createElement('video');v.src=URL.createObjectURL(blob);v.muted=true;v.loop=true;v.style='position:fixed;right:0;bottom:0;width:320px;z-index:9999';document.body.append(v);window.__video=v;await v.play();return {codec:rec.mimeType,width:640,height:360,audio:false};})()""")
 rows.append(sample('F-local-video',10));media['quality']=c.evaluate('(()=>{const q=__video.getVideoPlaybackQuality();__video.pause();__video.remove();URL.revokeObjectURL(__video.src);return {total:q.totalVideoFrames,dropped:q.droppedVideoFrames,corrupted:q.corruptedVideoFrames}})()')
 # Target activation changes actual Page Visibility in supported headless builds.
 timelineBefore=c.evaluate('({wall:Date.now(),time:AL.game.time+(AL.loop?.stats.pendingMinutes||0)})')
 other=c.call('Target.createTarget',{'url':'about:blank'})['targetId'];c.call('Target.activateTarget',{'targetId':other})
 hidden=c.evaluate('document.hidden');rows.append(sample('G-hidden' if hidden else 'G-visibility-unavailable',5));c.call('Target.closeTarget',{'targetId':other});time.sleep(3)
 rows.append(sample('G-return-covered',3));c.evaluate('__probe.close()');rows.append(sample('G-resumed',5))
 timelineAfter=c.evaluate('({wall:Date.now(),time:AL.game.time+(AL.loop?.stats.pendingMinutes||0),rate:AL.Config.minutesPerSecond})')
 c.evaluate('__probe.fixture("B")')
 for fps in [30,60]:
  c.evaluate('if(AL.Performance)AL.game.settings.graphics.frameRate='+str(fps));rows.append(sample('H-'+str(fps),6))
 # Repeated navigation/sustained foreground operation includes normal autosaves.
 heaps=[]
 for i in range(12):
  c.evaluate('__probe.menu('+json.dumps(['journal','equipment','store','settings'][i%4])+')');time.sleep(.3);c.evaluate('__probe.close()');time.sleep(4.7)
  if i%3==2:
   c.call('HeapProfiler.collectGarbage');heaps.append(metrics().get('JSHeapUsedSize'))
 rows.append(sample('E-sustained-end',6))
 saves=c.evaluate('(()=>{const r=[];for(let i=0;i<10;i++){const a=performance.now(),encoded=JSON.stringify(AL.game),b=performance.now(),saved=AL.Save.save(AL.game);r.push({serializeMs:b-a,totalMs:performance.now()-b,bytes:encoded.length,ok:saved.ok});}return r})()')
 checks=[]
 if phase=='after':
  checks=c.evaluate((root/'tests/performance_checks.js').read_text(encoding='utf8'))
  checks.append({'name':'Actual hidden/return transition advances elapsed time once (within250ms scheduler observation tolerance)','pass':hidden and abs((timelineAfter['time']-timelineBefore['time'])-(timelineAfter['wall']-timelineBefore['wall'])/1000*timelineAfter['rate'])<.3,'diagnostic':{'before':timelineBefore,'after':timelineAfter}})
  for width,height in [(1920,1080),(1600,900),(1366,768)]:
   c.call('Emulation.setDeviceMetricsOverride',{'width':width,'height':height,'deviceScaleFactor':1,'mobile':False});time.sleep(.2)
   checks.append({'name':str(width)+'x'+str(height)+': actual viewport has no horizontal overflow; canvas remains crisp and selectable','pass':c.evaluate('document.documentElement.scrollWidth<=innerWidth&&AL.renderer.ctx.imageSmoothingEnabled===false&&!!AL.renderer.hitboxes.length')})
 report={'phase':phase,'entry':entry.relative_to(root).as_posix(),'browser':c.call('Browser.getVersion'),'hardware':{'platform':platform.platform(),'logicalCPUs':os.cpu_count(),'navigator':c.evaluate('({cores:navigator.hardwareConcurrency,memoryGB:navigator.deviceMemory,agent:navigator.userAgent})')},'conditions':'Headless, --disable-gpu, disposable profile; no hardware GPU/Netflix/audio-sync measurement. Instrumentation adds overhead. Six-to-ten-second samples and 60-second navigation soak, not a multi-hour soak.','coldLoadSeconds':load,'rows':rows,'cpuProfileTop':sorted(counts.items(),key=lambda p:-p[1])[:35],'media':media,'actualHidden':hidden,'postGCHeapSamples':heaps,'saves':saves,'checks':checks,'runtimeSHA256':{p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in [*root.glob('js/*.js'),*root.glob('css/*.css'),root/'index.html']}}
 (out/(name+'-'+phase+'.json')).write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
 print(json.dumps({'phase':phase,'checks':len(checks),'failures':[x for x in checks if not x['pass']],'top':report['cpuProfileTop'][:12],'soakHeap':heaps,'media':media,'saves':saves}),flush=True)
 return int(any(not x['pass'] for x in checks))
