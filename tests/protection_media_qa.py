"""Compare exact same offline video bytes in fresh game processes; use repeated windows."""
import base64,hashlib,json,statistics,sys,time

def run(c,root,name):
 c.sock.settimeout(180);out=root/'tests/distribution-protection-evidence';out.mkdir(exist_ok=True)
 variant='development' if '--benchmark-development' in sys.argv else 'protected';clip=out/'multitasking.webm'
 if not clip.exists():
  encoded=c.evaluate("""(async()=>{const cv=document.createElement('canvas');cv.width=640;cv.height=360;const g=cv.getContext('2d'),stream=cv.captureStream(30),rec=new MediaRecorder(stream,{mimeType:'video/webm'}),parts=[];rec.ondataavailable=e=>parts.push(e.data);const done=new Promise(r=>rec.onstop=r);rec.start();let frame=0;const tick=setInterval(()=>{g.fillStyle=frame++%2?'#345678':'#789abc';g.fillRect(0,0,640,360);g.fillStyle='#fff';g.fillRect(frame*11%600,50,40,180)},33);await new Promise(r=>setTimeout(r,2200));clearInterval(tick);rec.stop();await done;stream.getTracks().forEach(t=>t.stop());const blob=new Blob(parts,{type:'video/webm'});return await new Promise(r=>{const f=new FileReader();f.onload=()=>r(f.result.split(',')[1]);f.readAsDataURL(blob)})})()""")
  clip.write_bytes(base64.b64decode(encoded))
 entry=root/('index.html' if variant=='development' else 'DIST/index.html')
 c.call('Network.emulateNetworkConditions',{'offline':True,'latency':0,'downloadThroughput':0,'uploadThroughput':0});c.call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':900,'deviceScaleFactor':1,'mobile':False});c.call('Page.addScriptToEvaluateOnNewDocument',{'source':'localStorage.clear();window.__long=[];'})
 c.navigate(entry,timeout=90)
 for _ in range(600):
  if c.evaluate('!!window.AL?.game&&!!AL.loop'):break
  time.sleep(.05)
 c.evaluate('window.__small='+(root/'tests/performance-evidence/fixture-small.json').read_text(encoding='utf8')+';'+(root/'tests/performance_probe.js').read_text(encoding='utf8'))
 c.evaluate('__probe.fixture("B");AL.Tutorial.state(AL.game).completionSeen=true;__probe.close()')
 c.evaluate('(async()=>{const v=document.createElement("video");v.src='+json.dumps(clip.as_uri())+';v.muted=true;v.loop=true;v.style="position:fixed;right:0;bottom:0;width:320px;z-index:9999";document.body.append(v);window.__video=v;await v.play()})()');time.sleep(3)
 c.call('Performance.enable');samples=[]
 def metrics():return {x['name']:x['value'] for x in c.call('Performance.getMetrics')['metrics']}
 for i in range(3):
  c.evaluate('__probe.reset()');a=metrics();start=time.monotonic();time.sleep(5);b=metrics();elapsed=time.monotonic()-start;r=c.evaluate('__probe.result()');r['mainThreadCorePercent']=100*(b['TaskDuration']-a['TaskDuration'])/elapsed;samples.append(r)
 quality=c.evaluate('(()=>{const v=__video,q=v.getVideoPlaybackQuality();v.pause();v.removeAttribute("src");v.load();v.remove();return {total:q.totalVideoFrames,dropped:q.droppedVideoFrames}})()')
 result={'variant':variant,'videoSha256':hashlib.sha256(clip.read_bytes()).hexdigest(),'videoBytes':clip.stat().st_size,'samples':samples,'medianFps':statistics.median(s['fps'] for s in samples),'medianCorePercent':statistics.median(s['mainThreadCorePercent'] for s in samples),'medianDrawP95':statistics.median(s['drawMsP95'] for s in samples),'quality':quality,'freshProcess':True,'audio':False}
 (out/(name+'-media-'+variant+'.json')).write_text(json.dumps(result,indent=2),encoding='utf8')
 if variant=='development':print(json.dumps({k:v for k,v in result.items() if k!='samples'},indent=2),flush=True);return 0
 before=json.loads((out/(name+'-media-development.json')).read_text(encoding='utf8'));checks=[{'name':'Both builds use exact same recorded video bytes','pass':before['videoSha256']==result['videoSha256']},{'name':'Protected video multitasking retains95% of source game FPS','pass':result['medianFps']>=before['medianFps']*.95},{'name':'Protected video median one-core CPU does not materially increase','pass':result['medianCorePercent']<=before['medianCorePercent']*1.25+1},{'name':'Protected video median draw cost stays within source allowance','pass':result['medianDrawP95']<=before['medianDrawP95']*1.25+1}]
 report={'buildId':json.loads((root/'DIST/build-manifest.json').read_text())['buildId'],'development':before,'protected':result,'checks':checks,'passed':sum(r['pass'] for r in checks),'failed':sum(not r['pass'] for r in checks),'method':'Same640x360VP8WebM, no audio; fresh process per variant;3x5-second warmed samples; medians; no Netflix/DRM/GPU claim.'}
 (out/(name+'-media.json')).write_text(json.dumps(report,indent=2),encoding='utf8');print(json.dumps({'passed':report['passed'],'failed':report['failed'],'development':{k:v for k,v in before.items() if k!='samples'},'protected':{k:v for k,v in result.items() if k!='samples'},'failures':[x for x in checks if not x['pass']]},indent=2),flush=True);return int(report['failed']>0)
