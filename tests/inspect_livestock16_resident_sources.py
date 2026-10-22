"""Prepare first original-pose contact proofs for manual landmark selection."""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageDraw
from pack_livestock16_production import split16

ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('batch',type=int);p.add_argument('--native',action='store_true');p.add_argument('--pending',action='store_true');a=p.parse_args()
base=ROOT/'planning/sprite-production'
ledger=json.loads((base/'production-ledger.json').read_text())
rows=[]
for entry in ledger['eligible']:
    if entry['batch']!=a.batch or entry['category']=='fish':continue
    for stage in entry['stages']:
        for state in (['polyp_motion'] if entry['category']=='coral' else ['idle','walk']):
            if a.pending and entry['production'].get(stage+':'+state,{}).get('state','').startswith('registered'):continue
            path=base/'raw'/entry['id']/(stage+'-'+state+'-source-v1.png')
            if a.native:
                path=base/'packed'/entry['id']/(stage+'-'+state+'-unapproved-first.png')
                if path.is_file():rows.append((entry['id'],stage,state,Image.open(path).convert('RGBA'),[0,0,*Image.open(path).size]))
            elif path.is_file():
                frames,boxes=split16(path)
                rows.append((entry['id'],stage,state,frames[0],boxes[0]))
for page in range((len(rows)+7)//8):
    subset=rows[page*8:(page+1)*8]
    cv=Image.new('RGBA',(1024,560),(18,38,53,255));draw=ImageDraw.Draw(cv)
    transforms=[]
    for i,(identity,stage,state,frame,box) in enumerate(subset):
        x=i%4*256;y=i//4*280
        scale=1 if a.native else min(232/frame.width,224/frame.height)
        w,h=round(frame.width*scale),round(frame.height*scale)
        ox=x+(256-w)//2;oy=y+48+(224-h)//2
        cv.alpha_composite(frame.resize((w,h),Image.Resampling.NEAREST),(ox,oy))
        draw.text((x+3,y+3),identity,fill='white');draw.text((x+3,y+17),stage+' '+state,fill='white')
        draw.text((x+3,y+31),'origin '+str(box[:2])+' scale '+str(round(scale,3)),fill='white')
        transforms.append({'id':identity,'stage':stage,'state':state,'sourceBox':box,'previewOrigin':[ox,oy],'previewScale':scale,'previewSize':[w,h]})
    target=base/'packed'/('batch'+str(a.batch)+('-native-firsts-' if a.native else '-source-firsts-')+str(page))
    cv.save(target.with_suffix('.png'));target.with_suffix('.json').write_text(json.dumps(transforms,indent=2)+'\n')
print(json.dumps({'poses':len(rows),'pages':(len(rows)+7)//8}))
