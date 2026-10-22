from pathlib import Path
R=Path(__file__).resolve().parents[2]
p=R/'js/core.js';s=p.read_text(encoding='utf8');s=s.replace('s.finance?.keys.includes(token)','s.finance?.keys?.includes(token)');p.write_text(s,encoding='utf8')
p=R/'js/store.js';s=p.read_text(encoding='utf8');old="'<br>Choose another eligible aquarium above; nothing has been purchased.'):''}";new="quote.ok?'<br>Choose another eligible aquarium above; nothing has been purchased.':'<br>Adjust quantity, funds or inventory capacity; nothing has been purchased.'):''}";assert old in s;s=s.replace(old,new,1);p.write_text(s,encoding='utf8')
p=R/'UI_POLISH_QUANTITY_REPORT.md';s=p.read_text(encoding='utf8').replace('A634-byte-class64×32 local SVG','A small64×32 local SVG');p.write_text(s,encoding='utf8')
