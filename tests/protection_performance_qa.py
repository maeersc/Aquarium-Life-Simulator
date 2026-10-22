"""Matched development/protected file-origin CPU, frames, heap and local-video samples."""
import json,sys,time

def run(c,root,name):
 out=root/'tests/distribution-protection-evidence';out.mkdir(exist_ok=True);c.sock.settimeout(180)
 c.call('Network.emulateNetworkConditions',{'offline':True,'latency':0,'downloadThroughput':0,'uploadThroughput':0})
 c.call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':900,'deviceScaleFactor':1,'mobile':False})
 c.call('Page.addScriptToEvaluateOnNewDocument',{'source':"localStorage.clear();window.__long=[];new PerformanceObserver(l=>{for(const e of l.getEntries())__long.push({start:e.startTime,duration:e.duration})}).observe({type:'longtask',buffered:true});"})
 c.call('Performance.enable');fixture=json.loads((root/'tests/performance-evidence/fixture-small.json').read_text(encoding='utf8'))
 def metrics():return {m['name']:m['value'] for m in c.call('Performance.getMetrics')['metrics']}
 def sample(label,seconds):
  c.evaluate('__probe.reset()');a=metrics();start=time.monotonic();time.sleep(seconds);b=metrics();r=c.evaluate('__probe.result()');elapsed=time.monotonic()-start
  r.update(label=label,wallSeconds=elapsed,mainThreadCorePercent=100*(b['TaskDuration']-a['TaskDuration'])/elapsed,heapBytes=b['JSHeapUsedSize'],listeners=b.get('JSEventListeners'),nodes=b.get('Nodes'));return r
 results={}
 variants=[('development',root/'index.html'),('protected',root/'DIST/index.html')]
 if '--benchmark-development' in sys.argv:variants=variants[:1]
 if '--benchmark-protected' in sys.argv:variants=variants[1:]
 for kind,entry in variants:
  start=time.monotonic();c.navigate(entry,timeout=90)
  for _ in range(600):
   if c.evaluate('!!window.AL?.game&&!!AL.loop'):break
   time.sleep(.05)
  else:raise RuntimeError('Benchmark did not boot: '+kind)
  startup=time.monotonic()-start;initial=metrics();startup_tasks=c.evaluate('__long');startup_resources=c.evaluate('performance.getEntriesByType("resource").map(e=>({name:e.name.split("/").pop(),duration:e.duration,responseEnd:e.responseEnd}))')
  c.evaluate('window.__small='+json.dumps(fixture)+';'+(root/'tests/performance_probe.js').read_text(encoding='utf8'))
  projection=c.evaluate("(()=>{__probe.fixture('B');const s=JSON.parse(JSON.stringify(AL.game));for(let i=0;i<3456;i++)AL.Sim.step(s,5);return JSON.stringify({time:s.time,seed:s.seed,tanks:s.tanks,stats:s.stats,credits:s.credits,inventory:s.inventory,finance:s.finance},(k,v)=>k==='realTime'?undefined:v)})()")
  rows=[]
  for scene in ['A','B','C','D']:
   c.evaluate('__probe.fixture('+json.dumps(scene)+');AL.Tutorial.state(AL.game).completionSeen=true;__probe.close()');time.sleep(2);rows.append(sample(scene,6))
   print(json.dumps({'build':kind,'scene':scene,'fps':rows[-1]['fps'],'corePercent':rows[-1]['mainThreadCorePercent'],'drawP95':rows[-1]['drawMsP95']}),flush=True)
  for menu in ['store','equipment','journal','diving']:
   c.evaluate('__probe.menu('+json.dumps(menu)+')');rows.append(sample(menu,3));c.evaluate('__probe.close()')
  c.evaluate('__probe.fixture("B");AL.Tutorial.state(AL.game).completionSeen=true;__probe.close()')
  for fps in [30,60]:
   c.evaluate('AL.game.settings.graphics.frameRate='+str(fps));rows.append(sample(str(fps)+'fps',4))
  media=c.evaluate("""(async()=>{const cv=document.createElement('canvas');cv.width=640;cv.height=360;const g=cv.getContext('2d'),stream=cv.captureStream(30),rec=new MediaRecorder(stream,{mimeType:'video/webm'}),parts=[];rec.ondataavailable=e=>parts.push(e.data);const done=new Promise(r=>rec.onstop=r);rec.start();let frame=0;const t=setInterval(()=>{g.fillStyle=frame++%2?'#345678':'#789abc';g.fillRect(0,0,640,360);g.fillStyle='#fff';g.fillRect(frame*11%600,50,40,180)},33);await new Promise(r=>setTimeout(r,2200));clearInterval(t);rec.stop();await done;stream.getTracks().forEach(t=>t.stop());const v=document.createElement('video');v.src=URL.createObjectURL(new Blob(parts,{type:'video/webm'}));v.muted=true;v.loop=true;v.style='position:fixed;right:0;bottom:0;width:320px;z-index:9999';document.body.append(v);window.__video=v;await v.play();return {codec:rec.mimeType,width:640,height:360,audio:false}})()""")
  rows.append(sample('local-video',8));media['quality']=c.evaluate('(()=>{const v=__video,q=v.getVideoPlaybackQuality(),url=v.src;v.pause();v.removeAttribute("src");v.load();v.remove();URL.revokeObjectURL(url);window.__video=null;return {total:q.totalVideoFrames,dropped:q.droppedVideoFrames}})()')
  target=c.call('Target.createTarget',{'url':'about:blank'})['targetId'];c.call('Target.activateTarget',{'targetId':target});hidden=c.evaluate('document.hidden');rows.append(sample('hidden',3));c.call('Target.closeTarget',{'targetId':target});time.sleep(1);c.evaluate('__probe.close()')
  c.call('HeapProfiler.collectGarbage');after=metrics()
  results[kind]={'entry':str(entry),'startupSeconds':startup,'startupTaskSeconds':initial.get('TaskDuration'),'startupScriptSeconds':initial.get('ScriptDuration'),'startupLongTasks':startup_tasks,'startupResources':startup_resources,'startupHeap':initial.get('JSHeapUsedSize'),'gcHeapBytes':after['JSHeapUsedSize'],'samples':rows,'media':media,'hiddenMeasured':hidden,'biologyProjection':projection}
  (out/(name+'-benchmark-'+kind+'.json')).write_text(json.dumps(results[kind],indent=2),encoding='utf8')
 if '--benchmark-development' in sys.argv:
  print(json.dumps({'stage':'fresh-browser development benchmark recorded','entry':'index.html'}),flush=True);return 0
 if '--benchmark-protected' in sys.argv:results['development']=json.loads((out/(name+'-benchmark-development.json')).read_text(encoding='utf8'))
 checks=[];ck=lambda label,ok:checks.append({'name':label,'pass':bool(ok)})
 before,after=results['development'],results['protected'];a={r['label']:r for r in before['samples']};b={r['label']:r for r in after['samples']}
 ck('Protected startup is within source+25%+0.4s measurement allowance',after['startupSeconds']<=before['startupSeconds']*1.25+.4)
 ck('Identical mixed tank retains exact biology/water/clock/wallet after3456 five-minute steps (12game days)',before['biologyProjection']==after['biologyProjection'])
 for scene in ['A','B','C','D','local-video']:
  minimum=max(55,a[scene]['fps']*.95) if scene!='local-video' else a[scene]['fps']*.95
  ck(scene+': protected frame rate retains at least95% of source'+(' and at least55FPS' if scene!='local-video' else ' under the same software-video workload'),b[scene]['fps']>=minimum)
  ck(scene+': no material Canvas draw-time regression',b[scene]['drawMsP95']<=a[scene]['drawMsP95']*1.25+2)
  ck(scene+': no material one-core main-thread CPU increase',b[scene]['mainThreadCorePercent']<=a[scene]['mainThreadCorePercent']*1.25+3)
 for mode in ['30fps','60fps']:
  fps=int(mode[:-3]);ck(mode+': protected renderer remains capped near selected target',abs(b[mode]['fps']-fps)<2)
 for menu in ['store','equipment','journal','diving','hidden']:ck(menu+': covered/hidden aquarium does not render',b[menu]['draws']==0)
 ck('Actual hidden-tab state was measured in both builds',before['hiddenMeasured'] and after['hiddenMeasured'])
 ck('Protected post-GC heap stays within source+16MiB',after['gcHeapBytes']<=before['gcHeapBytes']+16*1024*1024)
 result={'buildId':json.loads((root/'DIST/build-manifest.json').read_text())['buildId'],'browser':name,'environment':'headless Chromium, software Canvas (--disable-gpu); no physical GPU telemetry','freshProcesses':'--benchmark-protected' in sys.argv,'measurements':results,'checks':checks,'passed':sum(x['pass'] for x in checks),'failed':sum(not x['pass'] for x in checks),'limitations':['Local640x360VP8 video has no audio; Netflix/DRM/audio sync and physical GPU use were not measured.','Short matched scenarios measure browser main-thread one-core cost, not whole-system CPU or worst-case hardware.']}
 (out/(name+'-benchmark.json')).write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps({'passed':result['passed'],'failed':result['failed'],'failures':[x for x in checks if not x['pass']]},indent=2),flush=True)
 return int(result['failed']>0)
