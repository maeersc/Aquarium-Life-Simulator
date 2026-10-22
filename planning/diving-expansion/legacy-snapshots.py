from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'js/diving-expansion.js';s=p.read_text(encoding='utf8')
old="f=item.individual?copy(item.individual):kind==='coral'?";assert old in s;s=s.replace(old,"f=item.individual?copy(item.individual):kind==='fish'?K.fish(copy(s),d.id,{age:d.maturity+10,bought:false}):kind==='coral'?")
old="function migrate(s){s.diving.saleReceipts??=[];";assert old in s;s=s.replace(old,"function migrate(s){s.diving.saleReceipts??=[];for(const {o}of M.pending(s)){if(D.species[o.species]&&!o.recovery.item.individual){const seed=s.seed,f=K.fish(s,o.species,{age:D.species[o.species].maturity+10,bought:false});s.seed=seed;f.captureStage='adult';Object.assign(o.recovery.item,{individual:f,captureStage:'adult',legacySnapshot:true});}}")
old="!V.byId[item.species].lifeStages.includes(item.captureStage)";assert old in s;s=s.replace(old,"!(V.byId[item.species].lifeStages||['adult']).includes(item.captureStage)")
p.write_text(s,encoding='utf8');print('Migrated old pending fish deterministically; future profiles safely default to adult stages.')
