from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
def edit(name,old,new):
 p=ROOT/name;s=p.read_text(encoding='utf8');assert old in s,(name,old[:80]);p.write_text(s.replace(old,new),encoding='utf8')
edit('js/diving-expansion.js',"f.naturalOrigin={clutchId:e.id,larvalFood:'fry',hatchedAt:s.time,minimumSaleAge:D.species[f.species].maturity*.3};", "f.diveLarva={clutchId:e.id,larvalFood:'fry',hatchedAt:s.time,minimumSaleAge:D.species[f.species].maturity*.3};")
edit('js/diving-expansion.js',"const type=kind==='fish'?'ich':", "const type=kind==='fish'?['ich','bacterial','flukes'][(AL.Random.hash(o.species)+Math.floor(item.preExisting*100))%3]:")
# One shared transport formula for ordinary receiving, medical preview and liquidation.
p=ROOT/'js/diving-expansion.js';s=p.read_text(encoding='utf8');start=s.index('  const duration=Math.max(0,s.time-h.started)/60,quarantine=');end=s.index('\n }',start)
s=s[:start]+"  const chance=transportChance(s,h,item,destination),alive=s.time<item.expiresAt&&o.recovery.roll<chance;return {preview:f,label:alive?label:'Dead on arrival',alive,chance};"+s[end:]
idx=s.index(' function specimenReport')
s=s[:idx]+" function transportChance(s,h,item,destination){const p=V.byId[item.species],duration=Math.max(0,s.time-h.started)/60,holding=s.tanks.find(t=>t.id===destination)?.kind==='quarantine'?.1:0,young=item.captureStage==='baby'?.03:item.captureStage==='juvenile'?.01:0;return K.clamp(.96-p.sensitivity*.3-(1-item.transport)*.2-Math.min(.4,duration*.012)-h.steps*.004-(item.preExisting<.15?.15:0)-young+holding,.1,.98);}\n"+s[idx:]
s=s.replace('return {specimenReport','return {transportChance,specimenReport');p.write_text(s,encoding='utf8')
p=ROOT/'js/diving.js';s=p.read_text(encoding='utf8');start=s.index('const chance=K.clamp(');end=s.index(',roll=item.assessment?',start)
s=s[:start]+"const chance=AL.DiveExpansion.transportChance(s,a,item,item.destination)"+s[end:];p.write_text(s,encoding='utf8')
# Keep captured juvenile and hatchling feeding/sale development separate from captive parentage.
edit('js/update31.js',"if(AL.Breeding?.saleHold(f))reasons.push", "if(f.diveLarva&&f.age<f.diveLarva.minimumSaleAge)reasons.push('Diving hatchlings must reach juvenile age before sale.');if(AL.Breeding?.saleHold(f))reasons.push")
r=json.loads((ROOT/'assets/diving/registry.json').read_text(encoding='utf8'))
sources={
 'indonesia':'https://www.reef.org/db/reports/geo?region_code=CIP&zones=43130021',
 'philippines':'https://www.reef.org/db/reports/geo?region_code=CIP&zones=7102',
 'sri-lanka':'https://kayankerni.org/wp-content/uploads/2022/11/01.-A-preliminary-report-on-the-status-of-Kayankerni-coral-reef-Sri-Lanka_2019.pdf',
 'marshall':'https://repository.library.noaa.gov/view/noaa/45869/noaa_45869_DS1.pdf',
 'maldives':'https://www.reef.org/db/reports/geo?region_code=IORS&zones=23010046',
 'australia':'https://fishesofaustralia.net.au/home/species/2410',
 'florida':'https://www.floridamuseum.ufl.edu/wp-content/uploads/sites/35/2017/03/Vol-2-No-8.pdf'}
for id,source in sources.items():r['regions'][id]['sources'].append(source)
r['regions']['sri-lanka']['habitat']='Kayankerni coral and rock reef';r['regions']['australia']['habitat']='Lady Musgrave Island, Great Barrier Reef';r['regions']['indonesia']['habitat']='Bunaken / Lekuan sheltered reef';r['regions']['maldives']['habitat']='Madivaru Beyru, North Malé Atoll'
for p in r['species']:
 p['localityEvidence']={id:sources[id] for id in p['regions'] if id in sources}
r['eggPolicy']='One 3% opportunity per eligible expedition, independent of store egg odds; attached Ocellaris egg on a removable support chip. Fictional recovery; unknown fertilization estimated as 85% viability; accelerated captive incubation remains a game model.'
r['rosterBaseline']='Nine encounter profiles reference existing implemented IDs; zero added biological species.'
(ROOT/'assets/diving/registry.json').write_text(json.dumps(r,indent=2,ensure_ascii=False)+'\n',encoding='utf8');(ROOT/'js/diving-data.js').write_text('"use strict";\nAL.DivingData='+json.dumps(r,separators=(',',':'),ensure_ascii=False)+';\n',encoding='utf8')
print('Shared stage-sensitive transport; retained unknown wild parentage and locality evidence.')
