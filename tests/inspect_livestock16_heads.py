"""Magnified original head pixels for manual eye-anchor QA; not game artwork."""
import argparse
import json
from pathlib import Path
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('id');p.add_argument('stage',nargs='?',default='adult');p.add_argument('--state',choices=['swim','idle','walk','polyp_motion'],default='swim');p.add_argument('--crop-width',type=int,default=80);p.add_argument('--crop-height',type=int,default=85);a=p.parse_args()
id=a.id;stage=a.stage;stem=stage+('-'+a.state if a.state!='swim' else '')
assert 20<=a.crop_width<=400 and 20<=a.crop_height<=300
meta_path=root/'planning/sprite-production/packed'/id/(stage+'_'+a.state+'_16.json')
if meta_path.is_file():meta=json.loads(meta_path.read_text())
else:
    from pack_livestock16_production import split16
    source_path=root/'planning/sprite-production/raw'/id/(stem+'-source-v1.png')
    _,boxes=split16(source_path);meta={'source':str(source_path),'sourceBoxes':boxes}
source=Image.open(meta['source']).convert('RGBA');cw,ch=a.crop_width*2,a.crop_height*2+30;out=Image.new('RGBA',(cw*4,ch*4),(18,38,53,255));draw=ImageDraw.Draw(out)
for i,b in enumerate(meta['sourceBoxes']):
    x0=b[2]-a.crop_width;y0=b[1]+round((b[3]-b[1])*.10);im=source.crop((x0,y0,b[2],y0+a.crop_height)).resize((cw,a.crop_height*2),Image.Resampling.NEAREST)
    x=i%4*cw;y=i//4*ch;out.alpha_composite(im,(x,y+25));draw.text((x+2,y+2),f'{i}: origin{x0},{y0}',fill='white')
path=root/'planning/sprite-production/packed'/id/(stem+'-head-inspection.png');path.parent.mkdir(parents=True,exist_ok=True);out.save(path);print(path)
