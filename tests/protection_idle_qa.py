"""Separate steady hidden-tab CPU from transient media/GC transition work."""
import json,sys,time

def run(c,root,name):
 c.sock.settimeout(120);c.call('Performance.enable');out=root/'tests/distribution-protection-evidence';rows=[]
 def metric():return {x['name']:x['value'] for x in c.call('Performance.getMetrics')['metrics']}
 variants=[('development',root/'index.html'),('protected',root/'DIST/index.html')]
 if '--benchmark-development' in sys.argv:variants=variants[:1]
 if '--benchmark-protected' in sys.argv:variants=variants[1:]
 for variant,path in variants:
  c.navigate(path,timeout=90)
  for _ in range(600):
   if c.evaluate('!!window.AL?.game&&!!AL.loop'):break
   time.sleep(.05)
  c.evaluate('window.__small='+(root/'tests/performance-evidence/fixture-small.json').read_text(encoding='utf8')+';'+(root/'tests/performance_probe.js').read_text(encoding='utf8'))
  c.evaluate('__probe.fixture("B");AL.Tutorial.state(AL.game).completionSeen=true;__probe.close()');time.sleep(3)
  other=c.call('Target.createTarget',{'url':'about:blank'})['targetId'];c.call('Target.activateTarget',{'targetId':other});time.sleep(2)
  c.call('Profiler.enable');c.call('Profiler.start');a=metric();c.evaluate('__probe.reset()');start=time.monotonic();time.sleep(5);b=metric();elapsed=time.monotonic()-start;profile=c.call('Profiler.stop')['profile'];result=c.evaluate('__probe.result()')
  functions={n['id']:n['callFrame']['functionName'] for n in profile['nodes']};counts={}
  for sample in profile.get('samples',[]):
   f=functions.get(sample,'unknown');counts[f]=counts.get(f,0)+1
  rows.append({'variant':variant,'hidden':c.evaluate('document.hidden'),'mainThreadCorePercent':100*(b['TaskDuration']-a['TaskDuration'])/elapsed,'draws':result['draws'],'calls':result['calls'],'scheduler':result['scheduler'],'profilerSamples':counts})
  c.call('Target.closeTarget',{'targetId':other});time.sleep(1)
 if len(variants)==1:
  variant=variants[0][0];(out/(name+'-idle-'+variant+'.json')).write_text(json.dumps(rows[0],indent=2),encoding='utf8')
  if variant=='development':print(json.dumps(rows[0],indent=2),flush=True);return 0
  rows.insert(0,json.loads((out/(name+'-idle-development.json')).read_text(encoding='utf8')))
 checks=[{'name':r['variant']+': steady hidden tab has no game draws/timers or unnecessary one-core CPU use','pass':r['hidden'] and r['draws']==0 and r['scheduler']['raf']==0 and r['scheduler']['timer']==0 and r['mainThreadCorePercent']<1} for r in rows]
 result={'buildId':json.loads((root/'DIST/build-manifest.json').read_text())['buildId'],'rows':rows,'checks':checks,'passed':sum(r['pass'] for r in checks),'failed':sum(not r['pass'] for r in checks)}
 (out/(name+'-idle.json')).write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps(result,indent=2),flush=True);return int(result['failed']>0)
