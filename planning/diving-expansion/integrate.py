from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
assert 'js/diving-expansion.js' not in (ROOT/'index.html').read_text(encoding='utf8'), 'One-time integration already applied; do not replay.'
def edit(name,old,new):
 p=ROOT/name;s=p.read_text(encoding='utf8');assert old in s,(name,old[:100]);p.write_text(s.replace(old,new),encoding='utf8')
r=json.loads((ROOT/'assets/diving/registry.json').read_text())
zones=[('indonesia','Coral Triangle — Indonesia','Bunaken reef shelters',10,'fiji'),('philippines','Coral Triangle — Philippines','Puerto Galera sheltered reef',10,'fiji'),('sri-lanka','Sri Lanka','Hikkaduwa outer reef slope',12,'fiji'),('marshall','Marshall Islands','Majuro lagoon reef slope',12,'fiji'),('maldives','Maldives','North Malé outer atoll reef',12,'fiji'),('australia','Australia','Great Barrier Reef outer reef slope',12,'fiji'),('florida','Florida','Florida Keys / Tortugas rubble ledges',18,'caribbean')]
source='https://doi.org/10.2305/IUCN.UK.2010-4.RLTS.T165716A6099950.en'
for id,name,habitat,depth,rock in zones:r['regions'][id]={'name':name,'rock':rock,'reefDepth':depth,'habitat':habitat,'modes':['reef'],'collection':'Fictional restricted research recovery; no real collection authorization.','availability':'verified-existing-species','background':f'assets/diving/{id}-reef.svg','sources':[source] if id!='florida' else ['https://www.floridamuseum.ufl.edu/wp-content/uploads/sites/35/2017/03/Vol-2-No-8.pdf'],'weights':{'rock':1,'fish':1,'egg':.03},'nonFish':'Inert salvage only; no additional coral/invertebrate locality records approved.'}
r['regions']['mariana']={'name':'Mariana Trench','rock':'hawaiian','deepDepth':6000,'habitat':'Southern Mariana hadal slope research grid, 6,000 m','modes':['deep'],'remote':True,'wildlifeClosed':True,'availability':'observation-only','collection':'Fictional remotely operated research drone. No living collection, decompression transport or pressure aquarium is implemented.','background':'assets/diving/mariana-deep.svg','temperature':2,'pressureAtmospheres':600,'liveReceiving':False,'transport':'No pressure-maintained live transport; no living ownership.','sources':['https://oceantoday.noaa.gov/oceanasalab_rovs/','https://www.ncei.noaa.gov/news/planet-postcard-mariana-trench'],'weights':{'rock':1,'fish':0,'egg':0}}
for p in r['species']:
 if p['id']=='forcipiger-flavissimus':p['regions']+=['indonesia','philippines','sri-lanka','marshall','maldives','australia'];p['localitySource']=source;p['lifeStages']=['juvenile','adult']
 if p['id']=='chalk-bass':p['regions']+=['florida'];p['localitySource']=r['regions']['florida']['sources'][0]
r['species'].append({'id':'clown','regions':['indonesia','philippines'],'modes':['reef'],'depth':[1,15],'habitat':'Sheltered anemone-associated reef; settled post-larvae, juveniles, adults and attached substrate eggs','collection':'fictional-restricted','conservation':'Fictional restricted recovery only; no legal collection claim.','sensitivity':.3,'transport':.86,'source':'https://animaldiversity.org/accounts/Amphiprion_ocellaris/','rangeSource':'https://www.fishbase.se/summary/Amphiprion-ocellaris.html','lifeStages':['baby','juvenile','adult'],'eggContext':'attached-substrate','eggSource':'https://animaldiversity.org/accounts/Amphiprion_ocellaris/','eggHours':168})
for p in r['species']:
 if p['id'] not in ['clown','forcipiger-flavissimus']:p['lifeStages']=['juvenile','adult']
r['lifeStageWeights']={'baby':20,'juvenile':35,'adult':45};r['eggDiscoveryChance']=.03;r['reviewDate']='2026-10-16';r['version']=2
(ROOT/'assets/diving/registry.json').write_text(json.dumps(r,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
(ROOT/'js/diving-data.js').write_text('"use strict";\nAL.DivingData='+json.dumps(r,separators=(',',':'),ensure_ascii=False)+';\n',encoding='utf8')
edit('index.html','<script defer src="js/diving-mystery.js"></script>','<script defer src="js/diving-mystery.js"></script><script defer src="js/diving-expansion.js"></script>')
edit('js/core.js',"    diveRecover(s,t,a)","    diveEmergencySale(s,t,a){AL.DiveExpansion.emergencySale(s,a);},\n    diveSellRock(s,t,a){AL.DiveExpansion.sellRock(s,a);},\n    diveReceiveEgg(s,t,a){AL.DiveExpansion.receiveEgg(s,a);},\n    diveReleaseEgg(s,t,a){AL.DiveExpansion.releaseEgg(s,a);},\n    diveRecover(s,t,a)")
edit('js/core.js',"if(!destination)throw Error('The destination aquarium no longer exists. Choose another aquarium.');","if(!destination&&!['diveEmergencySale','diveSellRock','diveRelease','diveReleaseEgg'].includes(action))throw Error('The destination aquarium no longer exists. Choose another aquarium.');")
edit('js/core.js',"t.hardscape=t.hardscape.filter(r=>r.id!==a.id);},","AL.DiveExpansion?.removeRock(s,t,r);t.hardscape=t.hardscape.filter(r=>r.id!==a.id);},")
edit('js/diving.js',"...(AL.DiveMystery?.settledTokens(s)||[])","...(AL.DiveMystery?.settledTokens(s)||[]),...(s.diving.saleReceipts||[])")
edit('js/diving.js',"AL.DiveMystery?.migrate(s);}","AL.DiveMystery?.migrate(s);AL.DiveExpansion?.migrate(s);}")
edit('js/diving.js',"if(!mode||!region)throw", "if(!mode||!region||region.modes&&!region.modes.includes(a.mode))throw")
edit('js/diving.js',"if(o.mystery)return", "if(o.kind==='egg')return AL.DiveExpansion.collectEgg(s,a,o);if(o.mystery)return")
edit('js/diving.js',"if(kind==='fish'){f=K.fish(s,item.species,{sex:d.referenceSex});", "if(kind==='fish'){f=item.individual?JSON.parse(JSON.stringify(item.individual)):K.fish(s,item.species,{sex:d.referenceSex});")
edit('js/diving.js',"f.rarity=d.rarity;f.provenance=provenance(a);", "f.rarity=d.rarity;f.provenance=provenance(a);f.captureStage=item.captureStage||null;")
edit('js/diving.js',"if(condition<15)","if(item.assessment?.preview){Object.assign(f,JSON.parse(JSON.stringify(item.assessment.preview)));report.condition=item.assessment.label;}else if(condition<15)")
edit('js/diving.js',"for(const item of a.inventory){if(item.mystery", "for(const item of a.inventory){if(item.kind==='egg'){report.objects.push(AL.DiveExpansion.returnEgg(s,a,item));continue;}if(item.mystery")
edit('js/diving.js',"const rock={id:K.id(s,'recoveredRock'),group:item.group,variant:item.variant,tripId:a.id,source:'diving'};", "const rock=AL.DiveExpansion.makeRock(s,a,item);")
edit('js/diving.js',"report.objects.push({id:rock.id,name:R.regions[a.region].name+' inert rock salvage',condition:'Recovered to inventory',value:0});", "report.objects.push({id:rock.id,kind:'rock',region:a.region,name:R.regions[a.region].name+' inert rock salvage',condition:'Recovered to inventory',value:AL.DiveExpansion.rockQuote(rock).offer});")
edit('js/diving.js',"t.hardscape.push({id:K.id(s,'rock'),group:rock.group", "t.hardscape.push({id:rock.id,recoveredRock:JSON.parse(JSON.stringify(rock)),group:rock.group")
edit('js/diving.js',"!['rock','livestock'].includes(o.kind)","!['rock','livestock','egg'].includes(o.kind)")
edit('js/diving.js',"AL.DiveMystery?.validate(s);}","AL.DiveMystery?.validate(s);AL.DiveExpansion?.validate(s,identity);}")
edit('js/diving-mystery.js',"if(R.regions[region].wildlifeClosed)","if(R.regions[region].modes&&!R.regions[region].modes.includes(mode))return {ok:false,reason:'This destination does not support the selected diving mode.'};if(R.regions[region].remote)return {ok:!pending(s).length&&!AL.DiveExpansion?.pendingEggs(s).length,reason:'Remote research drone: 100% battery, 5% per movement. Inert samples only; no pressure-safe living collection pool.'};if(R.regions[region].wildlifeClosed)")
edit('js/diving-mystery.js',"if(pending(s).length)","if(pending(s).length||AL.DiveExpansion?.pendingEggs(s).length)")
edit('js/diving-mystery.js',"const p=pool(a.region,a.mode);if(!p.length)","if(R.regions[a.region].remote){a.remote=true;return;}const p=pool(a.region,a.mode);if(!p.length)")
edit('js/diving-mystery.js',"assessment:{roll:o.recovery.roll,condition:o.recovery.conditionRoll}","assessment:{roll:o.recovery.roll,condition:o.recovery.conditionRoll,...(o.recovery.item.individual?AL.DiveExpansion.assessment(s,h,o,args.destination):{})}")
edit('js/diving-mystery.js',"['pending','received','failed','released'].includes", "['pending','received','failed','released','sold'].includes")
edit('js/diving-mystery.js',"function step(s){for", "function step(s){AL.DiveExpansion?.step(s);for")
edit('js/valuation.js',"function brood(e){", "function brood(e){if(e.diveHidden)return 0;")
edit('js/simulation.js',"f.hunger=20;AL.Patterns?.inherit(f,e,i);t.fish.push(f);", "f.hunger=20;AL.Patterns?.inherit(f,e,i);if(e.diveHidden)AL.DiveExpansion.hatched(s,t,e,f);t.fish.push(f);")
edit('js/simulation.js',"const suitable=outside(w.temperature,d.temp)","const suitable=(!e.diveHidden||AL.DiveExpansion.incubationSafe(s,t,e))&&outside(w.temperature,d.temp)")
edit('js/brood-view.js',"function image(e){", "function image(e){if(e.diveHidden)return AL.DiveExpansion.eggImage(e);")
edit('js/brood-view.js',"if(!e)return;AL.renderer.selected=id;", "if(!e)return;if(e.diveHidden){AL.DiveExpansion.inspectEgg(t,e);return;}AL.renderer.selected=id;")
edit('js/app-shell.js',"${esc(D.species[e.species].name)} · ${esc(e.strategy)} brood</strong>${AL.Rarity.badge(e)}", "${e.diveHidden?'Unknown Fish Egg':esc(D.species[e.species].name)+' · '+esc(e.strategy)+' brood'}</strong>${e.diveHidden?'':AL.Rarity.badge(e)}")
edit('js/update31-ui.js',"||'<p>No owned specimens in this aquarium.</p>'}`;}","||'<p>No owned specimens in this aquarium.</p>'}${market==='regular'?AL.DiveExpansion.rockRows(s):''}`;}")
edit('js/update31-ui.js',"else if(op==='sale'){", "else if(op==='sellRock'){if(confirm('Sell this recovered rock for '+a.offer+' AC? This cannot be undone.')){if(AL.UI.transact('diveSellRock',a))AL.Store.render();}}else if(op==='sale'){")
print('Integrated shared expansion hooks and central regional registry.')
