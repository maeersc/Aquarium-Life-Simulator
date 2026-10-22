from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
def edit(name,old,new):
 p=ROOT/name;s=p.read_text(encoding='utf8');assert old in s,(name,old[:80]);p.write_text(s.replace(old,new),encoding='utf8')
edit('js/diving-expansion.js',"K.capacity(t,'flow')>=t.volume", "K.capacity(t,'flow')>=t.volume*.95")
edit('js/diving-expansion.js',"t.volume+'–'+(t.volume*2)", "(t.volume*.95).toFixed(0)+'–'+(t.volume*2)")
edit('js/diving-expansion.js',"function incubationSafe(s,t,e){", "function failedEgg(s,e){const h=s.diving.history.find(h=>h.id===e.provenance.tripId),o=h?.objects.find(o=>o.objectId===e.originObjectId);if(o){o.eggRecovery.status='failed';o.condition='Egg nonviable — incubation conditions';}}\n function incubationSafe(s,t,e){")
edit('js/diving-expansion.js',"function step(s){", "function step(s){for(const t of s.tanks)for(const e of t.eggs)if(e.diveHidden&&e.viability<=0)failedEgg(s,e);")
edit('js/diving-expansion.js',"o.eggRecovery.status='hatched';", "o.eggRecovery.status='hatched';o.value=AL.Valuation.livestock(s,f).value;o.reason='Species revealed after successful incubation; early larval care and fine food are required.';")
edit('js/diving-expansion.js',"return {snapshot,assessment,", "return {failedEgg,snapshot,assessment,")
edit('js/simulation.js',"if(e.viability<=0){if(t.water", "if(e.viability<=0){if(e.diveHidden)AL.DiveExpansion.failedEgg(s,e);if(t.water")
# Explicit catch-context requirements extend the shared biological checks.
p=ROOT/'js/diving-expansion.js';s=p.read_text(encoding='utf8');marker=' function protectedSale(id)'
assert marker in s
s=s.replace(marker,''' function specimenReport(s,h,o,t){const base=AL.DiveReceiving.report(s,o.species,t?.id),checks=[...base.checks];if(o.recovery?.item.captureStage==='baby'&&t){const f=o.recovery.item.individual,protectedTank=['incubation','quarantine'].includes(t.kind)&&!K.alive(t).length&&!(t.invertebrates||[]).some(x=>!x.dead);checks.push({label:'Post-larval refuge',ok:protectedTank,actual:t.kind+'; '+K.alive(t).length+' fish',required:'Unoccupied dedicated incubation or quarantine',help:'Protect small settled fish from predators and adult aggression.'},{label:'Fine food',ok:(s.inventory.fry??0)>0,actual:s.inventory.fry??0,required:'Fine fry food available',help:'More frequent small feeds; existing young-fish metabolism applies.'});}return {...base,checks,ok:base.ok&&checks.every(c=>c.ok),reasons:checks.filter(c=>!c.ok).map(c=>c.label+': actual '+c.actual+'; requires '+c.required+'.')};}
 function destinations(s,h,o){return AL.DiveReceiving.destinations(s,o.species).map(row=>V.category(o.species)==='fish'?{...row,report:specimenReport(s,h,o,row.tank)}:row);}
 function medical(s,h,o){const a=assessment(s,h,o),f=a.preview,conditions=f.healthState.conditions,symptoms=[...new Set(conditions.flatMap(c=>AL.Health.conditions[c.type].symptoms))];return {hp:f.hp,label:a.label,symptoms,quarantine:conditions.some(c=>AL.Health.conditions[c.type].contagious)?'Suspected infection: quarantine recommended; a diagnosis is not confirmed.':'Quarantine recommended for observation; no mandatory treatment is inferred.',treatments:Object.values(AL.Health.products).filter(p=>AL.Health.eligible(p.hosts,f)&&p.uses.some(type=>conditions.some(c=>c.type===type))).map(p=>p.name+' — '+p.restriction)};}
 function protectedSale(id)''')
s=s.replace('return {failedEgg,snapshot','return {specimenReport,destinations,medical,failedEgg,snapshot')
p.write_text(s,encoding='utf8')
edit('js/diving-mystery.js',"const r=V.receiving(s,o.species,args.destination,args.position??null);", "const destination=s.tanks.find(t=>t.id===args.destination),r=V.category(o.species)==='fish'?AL.DiveExpansion.specimenReport(s,h,o,destination):V.receiving(s,o.species,args.destination,args.position??null);")
edit('js/diving-ui.js',"AL.DiveReceiving.destinations(AL.game,o.species),available=", "AL.DiveExpansion.destinations(AL.game,AL.game.diving.history[0],o),available=")
edit('js/diving-ui.js',"const rows=AL.DiveReceiving.destinations(AL.game,o.species),signature=", "const rows=AL.DiveExpansion.destinations(AL.game,AL.game.diving.history[0],o),signature=")
edit('js/diving-ui.js',"stage=o.recovery.item.captureStage||'Legacy specimen';", "stage=o.recovery.item.captureStage||'Legacy specimen',medical=pending?AL.DiveExpansion.medical(AL.game,h,o):null;")
edit('js/diving-ui.js',"${pending?`<p>Emergency Sale", "${pending?`<p>Symptoms: ${esc(medical.symptoms.join(', ')||'No visible signs recorded')}. ${esc(medical.quarantine)}</p><p>Compatible care: ${esc(medical.treatments.join(' ')||'Monitor water and intake; no medication indicated from current signs.')}</p><p>Emergency Sale")
edit('tests/global_receiving_checks.js',"if(entry?.recovery)return s;", "if(entry?.recovery){if(entry.recovery.item.captureStage==='baby')s.tanks[0].kind='incubation';return s;}")
edit('js/diving-expansion.js',"s.diving.rocks=s.diving.rocks.filter", "for(const t of s.tanks)for(const r of t.hardscape||[])if(r.recoveredRock&&receipts.includes('rock-sale:'+r.id))throw Error('This placed rock was sold in a newer local save. Load the current save.');s.diving.rocks=s.diving.rocks.filter")
# Hidden eggs never reveal identity through species filtering.
edit('js/app-shell.js',"filters.species==='all'||filters.species===e.species", "filters.species==='all'||!e.diveHidden&&filters.species===e.species")
print('Repaired wear tolerance; added catch-stage receiving, medical detail, egg-loss tracking and replay guards.')
