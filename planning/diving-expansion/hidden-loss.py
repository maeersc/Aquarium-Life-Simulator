from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'js/diving.js';s=p.read_text(encoding='utf8');old="a.inventory.map(i=>i.mystery?AL.DiveMystery.forfeited(s,a,i):";assert old in s;s=s.replace(old,"a.inventory.map(i=>i.kind==='egg'?{objectId:i.id,name:'Unknown Fish Egg',kind:'egg',condition:'Forfeited',value:0,revealed:false}:i.mystery?AL.DiveMystery.forfeited(s,a,i):");p.write_text(s,encoding='utf8')
print('Kept failed and abandoned egg identities concealed.')
