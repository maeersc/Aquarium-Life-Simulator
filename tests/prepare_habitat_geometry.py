"""Extract collision columns from existing rock alpha; preserve all artwork."""
import json
from pathlib import Path
from PIL import Image
root=Path(__file__).resolve().parent.parent
groups={}
for group in ['fiji','caribbean','hawaiian']:
    im=Image.open(root/f'assets/livestock/rocks/{group}/atlas-v11.png').convert('RGBA')
    variants=[]
    for v in range(4):
        c=im.crop((v*192,0,(v+1)*192,192));cols=[]
        for x in range(192):
            spans=[];start=None
            for y in range(193):
                occupied=y<192 and c.getpixel((x,y))[3]>=128
                if occupied and start is None:start=y
                if not occupied and start is not None:spans.append([start,y]);start=None
            cols.append(spans)
        variants.append({'width':192,'height':192,'anchor':[96,184],'columns':cols})
    groups[group]=variants
(root/'js/habitat-geometry.js').write_text('"use strict";\nAL.HabitatGeometry='+json.dumps(groups)+';\n')
print('Extracted alpha collision columns for 12 existing rock variants.')
