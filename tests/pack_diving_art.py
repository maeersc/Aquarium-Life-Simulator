"""Copy preserved generated masters once and embed local runtime images."""
from pathlib import Path
import base64,json,shutil
root=Path(__file__).resolve().parent.parent
records=json.loads((root/'assets/diving/art-prompts.json').read_text(encoding='utf-8'))['records']
manifest=[]
def equipment_atlas(source,target):
 from PIL import Image
 image=Image.open(source).convert('RGBA');width,height=image.size
 mask=image.getchannel('A').point(lambda value:255 if value>=40 else 0)
 atlas=Image.new('RGBA',(1024,512));bounds=[]
 for row in range(2):
  top=row*height//2;bottom=(row+1)*height//2
  band=mask.crop((0,top,width,bottom))
  occupied=[band.crop((x,0,x+1,band.height)).histogram()[255]>=2 for x in range(width)]
  runs=[];start=None
  for x,value in enumerate([*occupied,False]):
   if value and start is None:start=x
   elif not value and start is not None:runs.append([start,x]);start=None
  merged=[]
  for start,end in runs:
   if merged and start-merged[-1][1]<=18:merged[-1][1]=end
   else:merged.append([start,end])
  merged=[r for r in merged if r[1]-r[0]>=20]
  assert len(merged)==4,(row,merged)
  for column,(left,right) in enumerate(merged):
   left=max(0,left-3);right=min(width,right+3)
   local=mask.crop((left,top,right,bottom)).getbbox();assert local
   box=(left+local[0],top+local[1],left+local[2],top+local[3])
   tile=image.crop(box);scale=min(232/tile.width,232/tile.height)
   tile=tile.resize((max(1,round(tile.width*scale)),max(1,round(tile.height*scale))),Image.Resampling.NEAREST)
   atlas.alpha_composite(tile,(column*256+(256-tile.width)//2,row*256+(256-tile.height)//2));bounds.append(box)
 atlas.save(target)
 (target.parent/'equipment-atlas-metadata-v1.json').write_text(json.dumps({'source':source.name,'runtime':target.name,'columns':4,'rows':2,'frameWidth':256,'frameHeight':256,'sourceBounds':bounds,'approved':False,'operation':'Technical alpha-gutter cropping and nearest-neighbor packing only; no repainting'},indent=2),encoding='utf-8')
 print('Equipment alpha-gutter source bounds:',bounds)
for r in records:
 target=root/r['path']
 if not target.exists():
  assert r.get('generatedSource'),f"Restore the preserved project source {r['path']} before packing"
  shutil.copyfile(r['generatedSource'],target)
 runtime=target
 if r['id']=='equipment':
  runtime=target.parent/'equipment-atlas-v1.png'
  if not runtime.exists():equipment_atlas(target,runtime)
 manifest.append({'id':r['id'],'path':runtime.relative_to(root).as_posix(),'source':r['path'],'approved':False,'src':'data:image/png;base64,'+base64.b64encode(runtime.read_bytes()).decode()})
(root/'js/diving-art-data.js').write_text('"use strict";\n// Local sources and generation records: assets/diving/art-prompts.json\nAL.DivingArtData='+json.dumps(manifest,separators=(',',':'))+';\n',encoding='utf-8')
print('Embedded',len(manifest),'original diving art sheets and backgrounds for offline use.')
