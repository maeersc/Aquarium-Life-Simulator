from pathlib import Path
r=Path(__file__).resolve().parents[2]
def edit(n,a,b):
 p=r/n;s=p.read_text(encoding='utf8');assert a in s,(n,a[:70]);p.write_text(s.replace(a,b,1),encoding='utf8')
p=r/'tests/global_receiving_checks.js';s=p.read_text(encoding='utf8')
s=s.replace("const s=diveFixture(),t=s.tanks[0];t.waterParams.temperature=27.5;", "const s=K.act(diveFixture(),'buyRack',{glass:'back'}),t=s.tanks[0];t.waterParams.temperature=27.5;",1)
s=s.replace("const id='pavona-cactus',s=diveFixture(),t=s.tanks[0]", "const id='pavona-cactus',s=K.act(diveFixture(),'buyRack',{glass:'back'}),t=s.tanks[0]",1)
s=s.replace("const s=diveFixture(),t=s.tanks[0];t.kind='quarantine';const p=", "const s=K.act(diveFixture(),'buyRack',{glass:'back'}),t=s.tanks[0];t.kind='quarantine';const p=",1)
s=s.replace("const s=diveFixture(),ids=['__future_fish'", "const s=K.act(diveFixture(),'buyRack',{glass:'back'}),ids=['__future_fish'",1)
p.write_text(s,encoding='utf8')
edit('js/diving.js',"definition(p.id)?.water==='marine'&&definition(p.id).purchaseVerified!==false", "definition(p.id)?.water==='marine'&&(!AL.DiveReceiving||AL.DiveReceiving.resolve(p.id))&&Number.isFinite(definition(p.id).minTank)&&!!definition(p.id).scientificName&&definition(p.id).purchaseVerified!==false")
edit('js/diving-receiving.js',"!Number.isFinite(entry.definition.minTank)||entry.definition.purchaseVerified", "!Number.isFinite(entry.definition.minTank)||!entry.definition.scientificName||entry.definition.purchaseVerified")
edit('js/diving-ui.js',"V.migrate(AL.game);mode=", "V.migrate(AL.game);if(receivingOwner!==AL.game.worldId){receivingChoices.clear();mountChoices.clear();captureChoices.clear();receivingOwner=AL.game.worldId;}mode=")
edit('js/diving-ui.js',"const a=AL.game.diving.active;if(a&&$('dive-return-route'))", "const a=AL.game.diving.active;if(a&&chosen&&document.activeElement?.id!=='dive-receiving'){const o=a.objects.find(o=>o.id===chosen),panel=document.querySelector('.dive-object');if(o?.kind==='livestock'&&!o.mystery&&!o.collected&&panel){const html=selectedObject();if(panel.dataset.snapshot!==html){panel.innerHTML=html;panel.dataset.snapshot=html;}}}if(a&&$('dive-return-route'))")
