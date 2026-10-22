from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'index.html';s=p.read_text(encoding='utf8');assert 'OFFLINE EDITION · v3.9' in s;p.write_text(s.replace('OFFLINE EDITION · v3.9','OFFLINE EDITION · v4.0'),encoding='utf8')
p=ROOT/'tests/pages_qa.py';s=p.read_text(encoding='utf8');s=s.replace('Built v3.9 mystery authority','Built v4.0 mystery authority').replace('AL.DivingData.species.length===8','AL.DivingData.species.length===9').replace('textContent.includes("v3.9")','textContent.includes("v4.0")');p.write_text(s,encoding='utf8')
print('Updated playable build label and deployed runtime acceptance.')
