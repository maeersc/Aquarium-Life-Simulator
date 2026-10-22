from pathlib import Path
p=Path(__file__).resolve().parents[2]/'js/diving.js';s=p.read_text(encoding='utf8')
a="AL.Health.infect(s,f,kind==='coral'?'pests':kind==='invertebrate'?'injury':'bacterial',.16,true);report.condition='Alive, suspected illness';"
b="const type=kind==='coral'?'pests':kind==='invertebrate'?'injury':'bacterial';AL.Health.infect(s,f,type,.16,!!AL.Health.conditions[type].contagious);report.condition=type==='injury'?'Alive, injured':'Alive, suspected illness';"
assert a in s;p.write_text(s.replace(a,b,1),encoding='utf8')
