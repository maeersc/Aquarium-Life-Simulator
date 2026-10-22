from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def edit(name,old,new):
 p=ROOT/name;s=p.read_text(encoding='utf8');assert old in s,(name,old[:80]);p.write_text(s.replace(old,new),encoding='utf8')
edit('js/diving-mystery.js',"...(o.recovery.item.individual?AL.DiveExpansion.assessment(s,h,o,args.destination):{})", "...AL.DiveExpansion.assessment(s,h,o,args.destination)")
edit('tests/global_receiving_checks.js',"const expected=kind==='fish'?(draw===5?'Alive, severely compromised':draw===20?'Alive, parasite/infection suspected':'Alive, stressed'):draw<15||draw===20&&kind==='invertebrate'?'Alive, injured':draw===20?'Alive, suspected illness':'Alive, stressed';", "const expected=draw===5?'Alive, severely compromised':draw===20?(kind==='invertebrate'?'Alive, injured':'Alive, parasite/infection suspected'):'Alive, stressed';")
# Exact display requirements must match the species record, including legacy Ocellaris range.
edit('js/diving-expansion.js',"Keep cycled marine water, 24–27 °C, oxygen ≥5.5 mg/L, ammonia/nitrite below 0.15 mg/L and gentle circulation.", "Keep cycled marine water, '+D.species[e.species].temp.join('–')+' °C, salinity '+D.species[e.species].salinity.join('–')+' ppt, pH '+D.species[e.species].ph.join('–')+', oxygen ≥5.5 mg/L, ammonia/nitrite below 0.15 mg/L and gentle circulation.")
# Avoid a broken image on the initial lazy-loaded planning preview.
edit('js/diving-ui.js',"${AL.DivingArt.image(region+'-'+mode)?.src||''}", "${AL.DivingArt.image(region+'-'+mode)?.src||r.background||''}")
edit('js/diving.js',"if(a.oxygen<=0)finish(s,'failed','Oxygen exhausted; rescue complete, unreturned discoveries lost. No fee refund.');", "if(a.oxygen<=0)finish(s,'failed',a.remote?'Drone battery exhausted; unreturned inert samples lost. No fee refund.':'Oxygen exhausted; rescue complete, unreturned discoveries lost. No fee refund.');")
edit('js/diving-ui.js',"const r=AL.game.diving.rocks.find(r=>r.id===args.id);", "const r=AL.game.diving.rocks.find(r=>r.id===args.id);")
# Expanded tests participate in deployed Pages acceptance too.
edit('tests/pages_qa.py',"        results.extend(c.evaluate((root/'tests/global_receiving_checks.js').read_text(encoding='utf8'))['checks'])", "        results.extend(c.evaluate((root/'tests/global_receiving_checks.js').read_text(encoding='utf8'))['checks'])\n        check('Built diving expansion is loaded', '!!AL.DiveExpansion&&!!AL.DiveExpansion.emergencyQuote')\n        results.extend(c.evaluate((root/'tests/diving_expansion_checks.js').read_text(encoding='utf8'))['checks'])")
edit('tests/package.py',"'global-receiving-evidence']", "'global-receiving-evidence','diving-expansion-evidence']")
print('Unified actual health across all hosts and enabled built-release expansion checks.')
