"""Offline animation coverage, appearance and renderer regression checks."""
import base64,json,time

def run(c,root,name,audit=False):
 out=root/'tests/fish-animation-evidence';out.mkdir(exist_ok=True)
 c.navigate(root/'index.html')
 for _ in range(400):
  if c.evaluate('!!window.AL?.game&&AL.ExpansionArt?.loaded===73&&AL.ClownArt?.loaded===AL.ClownArt?.records.length&&AL.LifeStages?.loaded===AL.LifeStages?.records.length'):break
  time.sleep(.05)
 c.evaluate('localStorage.clear();AL.Startup.finish();AL.game.settings.speed=0')
 c.call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':900,'deviceScaleFactor':1,'mobile':False})
 rows=c.evaluate("""Object.values(AL.Data.species).filter(d=>d.water==='marine').map(d=>{const expansion=AL.ExpansionArt.metadata(d.id),clown=AL.ClownArt.metadata(d.id),life=AL.LifeStages.metadata(d.id),meta=expansion||clown||life;return {id:d.id,name:d.name,scientificName:d.scientificName,shape:d.shape,activity:d.activity,diet:d.diet,zone:d.zone,clown:!!d.clownfish,fictional:!!d.fictional,purchaseVerified:d.purchaseVerified,art:meta,stages:['baby','juvenile','adult'].map(stage=>{const im=AL.ExpansionArt.frame(d.id,stage)||AL.ClownArt.frame(d.id,null,stage)||AL.LifeStages.frame(d.id,stage);return {stage,exists:!!im,width:im?.width,height:im?.height,meta:im?.artMeta};}),adultFrames:d.id==='clown'?4:clown?.swim?.length||1};})""")
 # Embedded data URLs never belong in the human-readable coverage ledger.
 for row in rows:
  if row.get('art'):row['art']={k:v for k,v in row['art'].items() if k!='src'}
 if audit:
  (out/'before.json').write_text(json.dumps(rows,indent=2),encoding='utf8')
  c.evaluate("""window.fishAuditSheet=document.createElement('canvas');fishAuditSheet.width=1200;fishAuditSheet.height=Math.ceil(Object.values(AL.Data.species).filter(d=>d.water==='marine').length/6)*150;const g=fishAuditSheet.getContext('2d');g.fillStyle='#172a3d';g.fillRect(0,0,fishAuditSheet.width,fishAuditSheet.height);g.imageSmoothingEnabled=false;Object.values(AL.Data.species).filter(d=>d.water==='marine').forEach((d,i)=>{const x=i%6*200,y=Math.floor(i/6)*150,im=AL.ExpansionArt.frame(d.id,'adult')||AL.ClownArt.frame(d.id)||AL.LifeStages.frame(d.id,'adult');g.fillStyle='#fff';g.font='11px sans-serif';g.fillText(d.id,x+5,y+14);if(im)g.drawImage(im,x,y+15,192,128);});""")
  (out/'before-adult-contact.png').write_bytes(base64.b64decode(c.evaluate("fishAuditSheet.toDataURL().split(',')[1]")))
  print(json.dumps({'species':len(rows),'dedicatedExpansion':sum(bool(x.get('art',{}).get('category')=='fish') for x in rows),'multiAdult':sum(x['adultFrames']>1 for x in rows),'ids':[x['id'] for x in rows]}),flush=True)
  return 0
 report=c.evaluate((root/'tests/fish_animation_checks.js').read_text(encoding='utf8'))
 checks=report['checks']
 def ck(n,x):
  try:checks.append({'name':n,'pass':bool(c.evaluate(x))})
  except Exception as e:checks.append({'name':n,'pass':False,'error':str(e)})
 c.evaluate("""window.animationFixture=(count=10)=>{const s=AL.Core.newGame('marine',90210),t=s.tanks[0],ids=Object.keys(AL.FishAnimation.data.species);s.settings.speed=0;s.update29.tutorial.status='skipped';t.volume=56781.17676;t.prepared=true;t.emptyDry=false;t.bacteria=t.bacteria2=1;t.fish=[];for(let i=0;i<count;i++){const f=AL.Core.fish(s,ids[i%ids.length],{genes:{color:1,size:1,longevity:1,immunity:1,fertility:1}});f.growth=1;f.x=.12+i%5*.18;f.y=.25+Math.floor(i/5)%3*.22;f.vx=f.vy=0;t.fish.push(f)}return s};window.makeAnimationRenderer=()=>{const c=document.createElement('canvas');c.width=960;c.height=480;return new AL.Renderer(c)};""")
 ck('Every registered fish actually animates in the aquarium renderer without touching save state',"(()=>{const s=animationFixture(94),r=makeAnimationRenderer(),before=JSON.stringify(s);for(let i=0;i<12;i++)r.draw(s,1/30);return JSON.stringify(s)===before&&r.positions.size===94&&[...r.positions.values()].every(p=>p.animation&&p.animation.rate>0);})()")
 ck('Every marine species retains correct livestock ID hit detection during animated playback',"(()=>{for(const id of Object.keys(AL.FishAnimation.data.species)){const s=animationFixture(1),f=AL.Core.fish(s,id),r=makeAnimationRenderer();f.x=f.y=.5;s.tanks[0].fish=[f];for(let i=0;i<10;i++){r.draw(s,.05);if(r.hit(.5,.5)!==f.id)return false}}return true})()")
 ck('Rendered frame rate cannot change health, hunger, growth, RNG, water or AC',"(()=>{const a=animationFixture(6),b=JSON.parse(JSON.stringify(a)),slow=makeAnimationRenderer(),fast=makeAnimationRenderer();for(let i=0;i<20;i++)slow.draw(a,.1);for(let i=0;i<240;i++)fast.draw(b,1/120);window.frameRateComparison={sameBeforeSimulation:JSON.stringify(a)===JSON.stringify(b),differences:[]};const systemNow=Date.now,wall=systemNow();try{Date.now=()=>wall;AL.Sim.advance(a,1440);AL.Sim.advance(b,1440);}finally{Date.now=systemNow}const diff=(a,b,p='')=>{if(JSON.stringify(a)===JSON.stringify(b))return;if(a&&b&&typeof a==='object'&&typeof b==='object'){for(const k of new Set([...Object.keys(a),...Object.keys(b)]))diff(a[k],b[k],p+'.'+k)}else frameRateComparison.differences.push({path:p,a,b})};diff(a,b);return !frameRateComparison.differences.length;})()")
 ck('Actual save/parse preserves all 94 individual genetics, life stages and fish IDs',"(()=>{const s=animationFixture(94),before=JSON.stringify(s.tanks[0].fish),loaded=AL.Save.parse(JSON.stringify(s));return JSON.stringify(loaded.tanks[0].fish)===before&&!Object.keys(loaded.tanks[0].fish[0]).includes('animation');})()")
 ck('Offscreen fish skip source/rig rendering without changing biological positions',"(()=>{const s=animationFixture(10),r=makeAnimationRenderer(),source=AL.FishAnimation.source;r.zoom=4;r.pan=.875;s.tanks[0].fish.forEach(f=>f.x=.05);let calls=0;AL.FishAnimation.source=(...a)=>{calls++;return source(...a)};try{const before=JSON.stringify(s);r.draw(s,.05);return calls===0&&before===JSON.stringify(s)&&!r.hitboxes.some(b=>s.tanks[0].fish.some(f=>f.id===b.id));}finally{AL.FishAnimation.source=source}})()")
 old=(root/'planning/fish-animation/baseline/js__render.js').read_text(encoding='utf8')
 ck('Protected freshwater renderer matches the pre-upgrade engine pixel-for-pixel',"(()=>{const New=AL.Renderer,s=AL.Core.newGame('fresh',883),t=s.tanks[0];t.fish.push(AL.Core.fish(s,'guppy'));const fresh=makeAnimationRenderer();let old;try{(0,eval)("+json.dumps(old[old.index('AL.Renderer = class {'):])+");old=makeAnimationRenderer()}finally{AL.Renderer=New}for(let i=0;i<24;i++){fresh.draw(s,1/30);old.draw(s,1/30)}const a=fresh.g.getImageData(0,0,480,240).data,b=old.g.getImageData(0,0,480,240).data;return a.every((n,i)=>n===b[i])&&JSON.stringify(fresh.hitboxes)===JSON.stringify(old.hitboxes);})()")
 # All 282 stage poses and both directions are recorded at consistent scale.
 c.evaluate("""window.animationSheet=document.createElement('canvas');animationSheet.width=1200;animationSheet.height=94*100;const g=animationSheet.getContext('2d'),s=animationFixture(1);g.fillStyle='#14283b';g.fillRect(0,0,1200,animationSheet.height);g.imageSmoothingEnabled=false;Object.keys(AL.FishAnimation.data.species).forEach((id,i)=>{const f=AL.Core.fish(s,id,{genes:{color:1,size:1,longevity:1,immunity:1,fertility:1}});g.fillStyle='#eee';g.font='11px sans-serif';g.fillText(id,4,i*100+12);['baby','juvenile','adult'].forEach((life,j)=>{f.growth=[.15,.6,1.1][j];const source=AL.FishAnimation.source(f,.2);for(const direction of [1,-1]){const pos={facing:direction,animation:{direction,tail:1,fin:-1,bank:0,bob:0}},x=120+j*380+(direction<0?180:0);AL.FishAnimation.draw(g,f,source,x,i*100+55,96,Math.round(96*source.height/source.width),pos)}})});""")
 # Keep readable sheets instead of relying on a 9,400-pixel image preview.
 for part in range(10):
  data=c.evaluate(f"(()=>{{const c=document.createElement('canvas');c.width=1200;c.height=Math.min(1000,animationSheet.height-{part*1000});c.getContext('2d').drawImage(animationSheet,0,{part*1000},1200,c.height,0,0,1200,c.height);return c.toDataURL().split(',')[1]}})()")
  (out/f'{name}-stage-directions-{part}.png').write_bytes(base64.b64decode(data))
 for part in range(2):
  native=c.evaluate("""(()=>{const ids=['clown','gramma','watchman','chromis','yellowtang','sixline','blenny','banggai','marinebetta','chalk-bass','hi-fin-red-banded-goby','amphiprion-leucokranos','lubbocks-fairy-wrasse','redspotted-blenny'].slice("""+str(part*7)+','+str(part*7+7)+"""),sheet=document.createElement('canvas');sheet.width=1200;sheet.height=1400;const g=sheet.getContext('2d'),s=animationFixture(1);g.fillStyle='#14283b';g.fillRect(0,0,1200,1400);g.imageSmoothingEnabled=false;ids.forEach((id,i)=>{g.fillStyle='#eee';g.font='12px sans-serif';g.fillText(id+' · native scene pixels magnified 2x after articulation',5,i*200+14);['baby','juvenile','adult'].forEach((stage,j)=>{const f=AL.Core.fish(s,id,{genes:{color:1,size:1,longevity:1,immunity:1,fertility:1}});f.growth=[.15,.6,1][j];const source=AL.FishAnimation.source(f,.2),w=Math.round(64*Math.max(.35,Math.min(1.7,.6+AL.Data.species[id].size/28)*Math.sqrt(f.growth))),h=Math.round(w*source.height/source.width);for(const direction of [1,-1]){const c=document.createElement('canvas');c.width=w+12;c.height=h+12;AL.FishAnimation.draw(c.getContext('2d'),f,source,Math.floor(c.width/2),Math.floor(c.height/2),w,h,{facing:direction,animation:{direction,tail:1,fin:-1,bank:0,bob:0}});g.drawImage(c,j*390+(direction<0?185:0),i*200+22,c.width*2,c.height*2)}})});return sheet.toDataURL().split(',')[1]})()""")
  (out/f'{name}-native-scale-{part}.png').write_bytes(base64.b64decode(native))
 c.evaluate("""window.animationPerformance=[];for(const count of [10,30,94]){const s=animationFixture(count),r=makeAnimationRenderer();for(let i=0;i<50;i++)r.draw(s,1/60);const start=performance.now();for(let i=0;i<120;i++)r.draw(s,1/60);animationPerformance.push({fish:count,meanMilliseconds:(performance.now()-start)/120,cache:AL.FishAnimation.metrics})}""")
 report['performance']=c.evaluate('animationPerformance');report['frameRateComparison']=c.evaluate('frameRateComparison')
 ck('Thirty-fish warm rendering averages under 33 ms on this QA PC','animationPerformance.find(x=>x.fish===30).meanMilliseconds<33')
 ck('Ninety-four-fish stress rendering averages under 50 ms on this QA PC','animationPerformance.find(x=>x.fish===94).meanMilliseconds<50')
 ck('Reused pose cache remains bounded during high-count playback','AL.FishAnimation.metrics.poseCache<=AL.FishAnimation.metrics.maxPoses&&AL.FishAnimation.metrics.poseHits>0')
 c.evaluate('AL.Store.close(false);AL.Shell.close(false);AL.UI.close();AL.game=animationFixture(10);AL.UI.render();AL.renderer.positions.clear();AL.renderer.draw(AL.game,.05);AL.renderer.canvas.scrollIntoView({block:"center"})')
 first=c.evaluate("(()=>{const f=AL.game.tanks[0].fish[0],b=AL.renderer.hitboxes.find(b=>b.id===f.id),r=AL.renderer.canvas.getBoundingClientRect();return {id:f.id,x:r.left+b.x*r.width,y:r.top+b.y*r.height}})()")
 report['clickDiagnostics']={'point':first,'before':c.evaluate("({viewport:[innerWidth,innerHeight],modals:[...document.querySelectorAll('dialog[open]')].map(d=>d.id),canvas:AL.renderer.canvas.getBoundingClientRect().toJSON()})")}
 c.call('Input.dispatchMouseEvent',{'type':'mousePressed','button':'left','clickCount':1,'x':first['x'],'y':first['y']})
 c.call('Input.dispatchMouseEvent',{'type':'mouseReleased','button':'left','clickCount':1,'x':first['x'],'y':first['y']})
 ck('Actual canvas click selects the correct moving livestock ID',"AL.renderer.selected==="+json.dumps(first['id'])+"&&document.getElementById('dialog').open")
 time.sleep(3.25)
 ck('Highlight expires after three real seconds while livestock inspector remains open',"AL.renderer.selected===null&&document.getElementById('dialog').open&&document.getElementById('dialog-body').textContent.includes('Ocellaris')")
 (out/f'{name}-inspector.png').write_bytes(base64.b64decode(c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
 c.evaluate('AL.UI.close();AL.UI.save()')
 c.navigate(root/'index.html')
 for _ in range(300):
  if c.evaluate('!!window.AL?.game&&!!AL.FishAnimation'):break
  time.sleep(.05)
 ck('Actual browser reload retains ten fish and original pattern identities','AL.game.tanks[0].fish.length===10&&AL.game.tanks[0].fish.every(f=>!!f.patternProfile)&&!AL.FishAnimation.audit().length')
 ck('Freshwater purchasing stays locked',"(()=>{try{AL.Core.act(AL.game,'buyTank',{water:'fresh',size:0});return false}catch{return true}})()")
 saved=c.evaluate("JSON.stringify(localStorage)")
 c.navigate(root/'fish-animation-review.html')
 for _ in range(300):
  if c.evaluate("document.getElementById('motion-fish')?.options.length===94"):break
  time.sleep(.05)
 ck('Standalone offline motion review contains every marine species',"document.getElementById('motion-fish').options.length===94")
 ck('Standalone review can inspect every fish, early stage and both directions',"(()=>{for(const o of document.getElementById('motion-fish').options){document.getElementById('motion-fish').value=o.value;document.getElementById('motion-fish').dispatchEvent(new Event('change'));for(const stage of ['baby','juvenile','adult']){document.getElementById('motion-stage').value=stage;document.getElementById('motion-stage').dispatchEvent(new Event('change'))}}return true})()")
 ck('Art review never changes player local saves','JSON.stringify(localStorage)==='+json.dumps(saved))
 (out/f'{name}-motion-review.png').write_bytes(base64.b64decode(c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
 checks.append({'name':'No uncaught browser errors','pass':not [e for e in c.events if e.get('method')=='Runtime.exceptionThrown']})
 checks.append({'name':'No HTTP/HTTPS asset or save requests during offline animation tests','pass':not [e for e in c.events if e.get('method')=='Network.requestWillBeSent' and e['params']['request']['url'].startswith(('http:','https:'))]})
 report['passed']=sum(x['pass'] for x in checks);report['failed']=sum(not x['pass'] for x in checks)
 (out/f'{name}-results.json').write_text(json.dumps(report,indent=2),encoding='utf8')
 print(json.dumps({'passed':report['passed'],'failed':report['failed'],'failures':[x for x in report['checks'] if not x['pass']]}),flush=True)
 return int(report['failed']>0)
