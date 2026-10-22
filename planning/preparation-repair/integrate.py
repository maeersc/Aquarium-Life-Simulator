from pathlib import Path
import shutil
r=Path(__file__).resolve().parents[2]
assert 'js/aquarium-preparation.js' not in (r/'index.html').read_text(encoding='utf8'),'One-time integration already applied.'
baseline=r/'planning/preparation-repair/baseline';baseline.mkdir(parents=True,exist_ok=True)
files=['index.html','js/core.js','js/save.js','js/simulation.js','js/diving-receiving.js','js/app-shell.js','js/ui.js','js/render.js','js/gameplay.js','js/breeding.js','js/habitat.js','js/invertebrates.js','js/livestock-health.js','js/marine-care.js','js/store-rules.js','js/thermal.js','js/update29.js','js/expansion.js','MASTER_DEVELOPMENT_PROMPT.md','PROJECT_CONTINUITY_SOURCE.md','DIST/build-manifest.json']
for n in files:shutil.copyfile(r/n,baseline/n.replace('/','__'))
def edit(n,a,b):
 p=r/n;s=p.read_text(encoding='utf8');assert a in s,(n,a[:100]);p.write_text(s.replace(a,b),encoding='utf8')
edit('index.html','<script defer src="js/core.js"></script>','<script defer src="js/core.js"></script><script defer src="js/aquarium-preparation.js"></script>')
edit('js/core.js',"    prepare(s,t){", "    fillWater(s,t){AL.Preparation.fill(s,t);},\n    prepare(s,t){if(t.water==='marine')return AL.Preparation.prepare(s,t);")
# Use the same persisted preparation completion flag via the shared authority.
for n in ['js/core.js','js/simulation.js','js/gameplay.js','js/habitat.js','js/invertebrates.js','js/livestock-health.js','js/marine-care.js','js/store-rules.js','js/thermal.js','js/update29.js','js/expansion.js','js/breeding.js']:
 p=r/n;s=p.read_text(encoding='utf8')
 # No new freshwater biology: the helper returns exactly the existing boolean.
 s=s.replace('!t.prepared','!AL.Preparation.prepared(t)').replace('t.prepared&&','AL.Preparation.prepared(t)&&').replace('(t.prepared?h:0)','(AL.Preparation.prepared(t)?h:0)').replace("!target.prepared","!AL.Preparation.prepared(target)")
 p.write_text(s,encoding='utf8')
edit('js/core.js',"const draft=JSON.parse(JSON.stringify(s)),originalSelection=draft.selectedTank;", "const draft=JSON.parse(JSON.stringify(s)),originalSelection=draft.selectedTank;AL.Preparation.migrate(draft);")
edit('js/save.js',"    AL.Finance?.validate(s);", "    AL.Preparation?.validate(s);AL.Finance?.validate(s);")
edit('js/save.js',"      AL.Expansion?.migrate(s);", "      AL.Preparation?.migrate(s);AL.Expansion?.migrate(s);")
edit('js/save.js',"try{AL.Offline?.beforeSave(s);validate(s);", "try{AL.Preparation?.migrate(s);AL.Offline?.beforeSave(s);validate(s);")
edit('js/simulation.js',"const previous=s.time;AL.Finance", "AL.Preparation.migrate(s);const previous=s.time;AL.Finance")
edit('js/simulation.js',"s.stats.cycled++;K.log(s,", "s.stats.cycled++;if(t.water==='marine')AL.Preparation.record(s,t,'cycled','Fishless cycling completed through the existing simulation.');K.log(s,")
edit('js/diving-receiving.js',"t.prepared&&!t.emptyDry,t.prepared&&!t.emptyDry?'Prepared water':'Unprepared / dry'", "AL.Preparation.prepared(t),AL.Preparation.state(t).label")
edit('js/render.js',"const dry=t.emptyDry===true&&!t.prepared;", "const dry=t.water==='marine'?!AL.Preparation.filled(t):t.emptyDry===true&&!t.prepared;")
edit('js/app-shell.js',"${t.prepared?t.bacteria>=.65?'Cycled':'Cycling / setup':'Empty and dry'}", "${t.water==='marine'?AL.Preparation.state(t).label:t.prepared?t.bacteria>=.65?'Cycled':'Cycling / setup':'Empty and dry'}")
edit('js/app-shell.js',"This aquarium is empty and dry. Fill and prepare it in Tank Setup before changing water.", "'+(t.water==='marine'?AL.Preparation.state(t).label:'Water is not prepared')+'. Fill and prepare it in Tank Setup before changing water.")
edit('js/ui.js',"if(!t.prepared)onboarding=`<div class=\"notice\">", "if(!AL.Preparation.prepared(t))onboarding=`<div class=\"notice\">${t.water==='marine'?'<strong>'+AL.Preparation.state(t).label+'</strong><br>':''}")
edit('js/ui.js',"${button('Prepare water','prepare',{},'primary')}", "${t.water==='marine'&&!AL.Preparation.filled(t)?button('Add water','fillWater',{},'')+' ':''}${button('Prepare water','prepare',{},'primary')}")
edit('js/ui.js',"let onboarding='';", "let onboarding=t.water==='marine'&&AL.Preparation.prepared(t)?'<p class=\"notice\">'+AL.Preparation.state(t).label+'</p>':'';")
# Audit correction: only viable embryos reserve adult load; physical remains
# still occupy the existing hard entity limit until removal. Freshwater unchanged.
edit('js/core.js',"t.eggs.reduce((n,e)=>n+D.species[e.species].load*e.count,0)", "t.eggs.filter(e=>t.water!=='marine'||e.viability>0).reduce((n,e)=>n+D.species[e.species].load*e.count,0)")
edit('js/core.js',"if(residents.length+(t.water==='marine'?", "if((t.water==='marine'?t.fish.filter(f=>!ignoreIds.includes(f.id)).length:residents.length)+(t.water==='marine'?")
edit('js/diving-receiving.js',"t.eggs.reduce((n,e)=>n+D.species[e.species].load*e.count,0)", "t.eggs.filter(e=>e.viability>0).reduce((n,e)=>n+D.species[e.species].load*e.count,0)")
edit('js/diving-receiving.js',"const count=residents.length+", "const count=t.fish.length+")
edit('js/diving-receiving.js',"fish including reserved viable offspring", "fish slots including retained remains and reserved viable offspring")
edit('js/breeding.js',"return t.fish.length+broods", "return t.fish.length+broods")
# Deployed acceptance includes preparation regressions and an exact runtime marker.
edit('tests/pages_qa.py',"        results.extend(c.evaluate((root/'tests/expansion_checks.js')", "        check('Built shared aquarium preparation authority is loaded', '!!AL.Preparation&&!!AL.Preparation.state&&!!AL.Preparation.migrate')\n        results.extend(c.evaluate((root/'tests/preparation_checks.js').read_text(encoding='utf8'))['checks'])\n        results.extend(c.evaluate((root/'tests/expansion_checks.js')")
edit('tests/package.py',"'diving-expansion-evidence']", "'diving-expansion-evidence','preparation-evidence']")
print('Unified preparation flags, setup transitions, safe legacy restoration, labels and shared receiving checks.')
