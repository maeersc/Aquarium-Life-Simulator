from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'js/diving-ui.js';s=p.read_text(encoding='utf8');s=s.replace('data-dive-icon="2" width="28"','data-dive-icon="${a.remote?8:2}" width="28"').replace('Collection uses no oxygen.</p>','Collection uses no ${a.remote?\'battery\':\'oxygen\'}.</p>');p.write_text(s,encoding='utf8')
p=ROOT/'js/diving-art.js';s=p.read_text(encoding='utf8');old="function icon(ctx,index,x,y,w,h=w){const im=";assert old in s;s=s.replace(old,"function icon(ctx,index,x,y,w,h=w){if(index===8){ctx.fillStyle='#bdd9cb';ctx.fillRect(x,y+h*.2,w*.85,h*.6);ctx.fillRect(x+w*.85,y+h*.4,w*.12,h*.2);ctx.fillStyle='#45bda1';ctx.fillRect(x+3,y+h*.2+3,w*.85-6,h*.6-6);return;}const im=");p.write_text(s,encoding='utf8')
print('Completed separate remote battery icon and resource wording.')
