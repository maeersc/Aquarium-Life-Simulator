from pathlib import Path
import re
r=Path(__file__).resolve().parents[2]
def edit(n,a,b):
 p=r/n;s=p.read_text(encoding='utf8');assert a in s,(n,a[:80]);p.write_text(s.replace(a,b),encoding='utf8')
edit('js/ui.js',"let onboarding=t.water==='marine'&&AL.Preparation.prepared(t)?'<p class=\"notice\">'+AL.Preparation.state(t).label+'</p>':'';", "let onboarding='';")
edit('js/ui.js',"small things. A well-kept aquarium finds its own rhythm.')+onboarding", "small things. A well-kept aquarium finds its own rhythm.')+(t.water==='marine'&&AL.Preparation.prepared(t)?'<p class=\"notice\">'+AL.Preparation.state(t).label+'</p>':'')+onboarding")
edit('js/aquarium-preparation.js',"typeof t.prepared!=='boolean')continue;const history=", "typeof t.prepared!=='boolean')continue;if(t.prepared&&t.emptyDry!==true)continue;const history=")
edit('js/aquarium-preparation.js',"cycleProof=Number.isFinite(t.cycle)", "cycleProof=!last&&Number.isFinite(t.cycle)")
edit('js/store-rules.js',"t.eggs.some(e=>{const other=", "t.eggs.filter(e=>t.water!=='marine'||e.viability>0).some(e=>{const other=")
edit('js/store-rules.js',"broods=t.eggs.filter(e=>AL.Data.species[e.species].clownfish)", "broods=t.eggs.filter(e=>e.viability>0&&AL.Data.species[e.species].clownfish)")
edit('js/simulation.js',"t.eggs.reduce((n,e)=>n+D.species[e.species].load*e.count,0)", "t.eggs.filter(e=>t.water!=='marine'||e.viability>0).reduce((n,e)=>n+D.species[e.species].load*e.count,0)")
# Standalone review pages use the same shared runtime dependencies as the game.
changed=[]
for p in [*r.glob('*.html'),*(r/'tests').glob('*.html')]:
 s=p.read_text(encoding='utf8')
 if 'aquarium-preparation.js' in s:continue
 found=re.search(r'<script([^>]*?)src="((?:\.\./)?js/)core\.js"([^>]*?)></script>',s)
 if not found:continue
 s=s[:found.end()]+f'<script{found[1]}src="{found[2]}aquarium-preparation.js"{found[3]}></script>'+s[found.end():];p.write_text(s,encoding='utf8');changed.append(p.name)
print('Added explicit setup-state label, respected later empty/fill history and synchronized viable capacity reservations. Review pages:',changed)
