from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def edit(name,old,new):
 p=ROOT/name;s=p.read_text(encoding='utf8');assert old in s,(name,old[:100]);p.write_text(s.replace(old,new),encoding='utf8')
edit('tests/diving_expansion_qa.py',' print(json.dumps(report),flush=True)',' print(json.dumps({"modelPassed":report["passed"],"modelFailed":report["failed"],"failures":[x for x in report["checks"] if not x["pass"]]}),flush=True)')
edit('tests/diving_checks.js',"if(r.wildlifeClosed)return reject", "if(r.modes&&!r.modes.includes(mode))return reject(()=>launch(diveFixture(),mode,region));if(r.wildlifeClosed&&!r.remote)return reject")
edit('tests/global_receiving_checks.js',"const expected=draw<15||draw===20&&kind==='invertebrate'?'Alive, injured':draw===20?'Alive, suspected illness':'Alive, stressed';", "const expected=kind==='fish'?(draw===5?'Alive, severely compromised':draw===20?'Alive, parasite/infection suspected':'Alive, stressed'):draw<15||draw===20&&kind==='invertebrate'?'Alive, injured':draw===20?'Alive, suspected illness':'Alive, stressed';")
edit('tests/mystery_diving_checks.js',"[5,'Alive, injured'],[20,'Alive, suspected illness']", "[5,'Alive, severely compromised'],[20,'Alive, parasite/infection suspected']")
edit('tests/diving_expansion_checks.js',"return !!f&&f.growth<.3&&f.diveEggId===e.id&&f.provenance.region==='indonesia'&&o.revealed&&o.eggRecovery.offspringId===f.id&&s.discovered.includes(f.species)&&t.eggs.length===0;", "if(!f||!o.revealed)throw Error(JSON.stringify({fish:t.fish,egg:t.eggs,report:o,water:t.waterParams}));return !!f&&f.growth<.3&&f.diveEggId===e.id&&f.provenance.region==='indonesia'&&o.revealed&&o.eggRecovery.offspringId===f.id&&s.discovered.includes(f.species)&&t.eggs.length===0;")
print('Updated regression expectations only for explicitly authorized destinations and condition expansion.')
