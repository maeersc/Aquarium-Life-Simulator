from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
def edit(name,old,new):
 p=ROOT/name;s=p.read_text(encoding='utf8');assert old in s,(name,old[:100]);p.write_text(s.replace(old,new),encoding='utf8')
edit('js/diving-expansion.js',"AL.Health.infect(s,f,'malnutrition',.45)","AL.Health.infect(s,f,kind==='coral'?'injury':'malnutrition',.45)")
edit('js/diving-expansion.js',"AL.Health.infect(s,f,'malnutrition',.25)","AL.Health.infect(s,f,kind==='coral'?'injury':'malnutrition',.25)")
edit('js/diving.js',"if(!r.ok)throw Error(r.reasons.join(' '));if(a.inventory", "if(args.destination&&!r.ok)throw Error(r.reasons.join(' '));if(a.inventory")
edit('js/diving.js',"o.kind==='livestock'&&!(o.mystery&&o.destination===null)&&typeof o.destination!=='string'", "o.kind==='livestock'&&o.destination!==null&&typeof o.destination!=='string'")
edit('js/diving-ui.js',"!near||!allowed||!has||a.inventory.length>=8", "!near||!allowed||a.inventory.length>=8")
edit('js/diving-ui.js',"if($('dive-receiving')&&!val){AL.UI.toast('Choose a safe receiving aquarium first.',true);return;}", "")
edit('js/diving-ui.js',"This is a receiving plan. Return to the boat", "An optional receiving plan. Without a safe receiver you can still return and choose Emergency Sale or release. Return to the boat")
edit('js/marine-care.js',"young=f.growth<.3||", "young=f.growth<.3||f.captureStage==='juvenile'&&f.growth<1||")
# Stage-specific art uses approved existing atlases, including clownfish collection art.
edit('js/diving-art.js',"function reveal(ctx,species,progress=1)","function reveal(ctx,species,progress=1,stage='adult')")
edit('js/diving-art.js',"AL.ExpansionArt.frame(species,'adult','alive')", "AL.ExpansionArt.frame(species,stage,'alive')||AL.ClownArt?.frame(species,null,stage,'alive')||AL.LifeStages?.frame(species,stage,'alive')")
edit('js/diving-ui.js',"data-mystery-reveal=\"${esc(o.species)}\"", "data-mystery-reveal=\"${esc(o.species)}\" data-catch-stage=\"${esc(o.recovery.item.captureStage||'adult')}\"")
edit('js/diving-ui.js',"Math.min(1,(performance.now()-revealStarted)/650));", "Math.min(1,(performance.now()-revealStarted)/650),c.dataset.catchStage||'adult');")
# Preserve the existing region artwork; author new code-native scenes for new zones.
r=json.loads((ROOT/'assets/diving/registry.json').read_text(encoding='utf8'))
for i,(id,zone) in enumerate((x for x in r['regions'].items() if x[1].get('background'))):
 remote=zone.get('remote',False);water='#071525' if remote else ['#103c55','#164e60','#214d5b','#144661','#105062','#194d62','#234458'][i%7];bottom='#1a2634' if remote else '#435456'
 features=''.join(f'<path d="M{x} 480v-{30+(x+i*17)%80}h12v18h14v-26h9v52h15v70z" fill="{["#667965","#9d7866","#528b84"][j%3]}"/>' for j,x in enumerate(range(40,870,99))) if not remote else '<path d="M0 390 170 340 290 470 440 510 590 390 740 350 880 440V560H0Z" fill="#1e2a38"/><path d="M260 560 380 420 470 550 600 560" fill="#101a28"/>'
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="880" height="560" viewBox="0 0 880 560" shape-rendering="crispEdges"><title>{zone["name"]} — {zone["habitat"]}</title><rect width="880" height="560" fill="{water}"/><path d="M0 80 270 0H350L90 420H0Z" fill="#b9ece5" opacity="{.02 if remote else .08}"/><path d="M0 480H880V560H0Z" fill="{bottom}"/>{features}<g fill="#b7dce1" opacity=".2"><rect x="130" y="180" width="3" height="3"/><rect x="420" y="290" width="3" height="3"/><rect x="700" y="120" width="3" height="3"/></g></svg>'
 (ROOT/zone['background']).write_text(svg,encoding='utf8')
edit('tests/browser_qa.py',"        if '--global-receiving' in sys.argv:","        if '--diving-expansion' in sys.argv:\n            import diving_expansion_qa\n            return diving_expansion_qa.run(client,ROOT,NAME)\n        if '--global-receiving' in sys.argv:")
edit('tests/diving_checks.js',"test('Exact two modes and four authorized regions',()=>Object.keys(AL.DivingData.modes).join(',')==='reef,deep'&&Object.keys(AL.DivingData.regions).join(',')==='fiji,caribbean,hawaii,japan');", "test('Two original modes and all original authorized regions are retained',()=>Object.keys(AL.DivingData.modes).join(',')==='reef,deep'&&['fiji','caribbean','hawaii','japan'].every(id=>AL.DivingData.regions[id]));")
print('Refined host eligibility, optional pre-capture receiving, stage art and local region scenes.')
