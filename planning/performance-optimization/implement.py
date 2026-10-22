from pathlib import Path
import json,hashlib,base64
r=Path(__file__).resolve().parents[2]
p=r/'index.html';s=p.read_text(encoding='utf8');a=s.index('<!-- AL_LIVESTOCK_SHEETS_START -->');b=s.index('<!-- AL_LIVESTOCK_SHEETS_END -->',a)+len('<!-- AL_LIVESTOCK_SHEETS_END -->');s=s[:a]+'<!-- AL_LIVESTOCK_SHEETS_START --><!-- Native sheets load on demand. --><!-- AL_LIVESTOCK_SHEETS_END -->'+s[b:];s=s.replace('<script defer src="js/sprite-kit.js">','<script defer src="js/performance.js"></script><script defer src="js/sprite-sources.js"></script><script defer src="js/sprite-kit.js">');p.write_text(s,encoding='utf8')
data=json.loads((r/'assets/animation/livestock-registry.json').read_text(encoding='utf8'))
folder=r/'assets/livestock/animation-sources';folder.mkdir(exist_ok=True)
count=0
for entry in data['entries']:
 for clip in entry.get('clips',[]):
  if clip.get('status')!='production':continue
  raw=(r/clip['path']).read_bytes();assert hashlib.sha256(raw).hexdigest()==clip['sha256']
  text='"use strict";\nAL.SpriteSources.accept('+json.dumps(clip['path'])+','+json.dumps('data:image/png;base64,'+base64.b64encode(raw).decode())+');\n'
  (folder/(clip['sha256']+'.js')).write_text(text,encoding='utf8');count+=1
print('Generated',count,'lossless per-sheet file:// transports')
# Additive save preferences. Old biological state is not migrated differently.
p=r/'js/save.js';s=p.read_text(encoding='utf8');s=s.replace('AL.Preparation?.migrate(s);AL.Expansion?.migrate(s);','AL.Performance?.normalize(s.settings);AL.Preparation?.migrate(s);AL.Expansion?.migrate(s);');p.write_text(s,encoding='utf8')
# Retain actual DOM nodes when values are unchanged (also prevents observer work).
p=r/'js/ui.js';s=p.read_text(encoding='utf8');a=s.index('  function updateVitals()');b=s.index('  function speciesCard',a);part=s[a:b]
import re
part=re.sub(r"\$\('([^']+)'\)\.textContent=([^;]+);",lambda m:"AL.Performance.text('"+m[1]+"',"+m[2]+");",part)
lines=part.splitlines()
for i,line in enumerate(lines):
 if "$('water-stats').innerHTML=" in line:
  prefix,expr=line.split("$('water-stats').innerHTML=",1);assert expr.endswith(';');lines[i]=prefix+"AL.Performance.html('water-stats',"+expr[:-1]+');'
part='\n'.join(lines)+'\n'
part=re.sub(r"\$\('(quest-progress|event-log)'\)\.innerHTML=([^;]+);",lambda m:"AL.Performance.html('"+m[1]+"',"+m[2]+");",part)
s=s[:a]+part+s[b:]
s=s.replace('<form data-form="settings"><label','<form data-form="settings">${AL.Performance.preferences(s)}<label')
s=s.replace('<label class="inline-check"><input name="particles" type="checkbox" ${s.settings.particles?\'checked\':\'\'}> Ambient particles and bubbles</label>','')
s=s.replace('particles:!!values.particles,reducedViolence:!!values.reducedViolence','graphics:{frameRate:Number(values.frameRate),quality:values.graphicsQuality,water:values.waterEffects,particles:values.decorativeParticles,backgroundSaving:!!values.backgroundSaving},particles:values.decorativeParticles!==\'off\',reducedViolence:!!values.reducedViolence')
# Top-level menu/selector markup is event-driven; do not periodically rebuild it.
for ident in ['navigation','aquarium-selector']:
 s=re.sub(r"\$\('"+ident+r"'\)\.innerHTML=([^;]+);",lambda m:"AL.Performance.html('"+ident+"',"+m[1]+");",s)
p.write_text(s,encoding='utf8')
