from pathlib import Path
from PIL import Image
for p in Path('assets/expansion-v27').glob('*/source-v1.png'):
 im=Image.open(p).convert('RGBA');a=im.getchannel('A');print(p.parent.name,im.size,a.getextrema(),'transparent',a.histogram()[0], 'corner',im.getpixel((0,0)))
