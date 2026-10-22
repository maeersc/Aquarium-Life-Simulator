"""Technical sprite-sheet extraction/nearest-neighbor packing; no semantic edits.
Original generated RGBA sheets are preserved beside each atlas.
"""
from pathlib import Path
from PIL import Image,ImageDraw
import json,base64,hashlib
root=Path(__file__).resolve().parent.parent
registry=json.loads((root/'assets/expansion-v27/registry.json').read_text(encoding='utf-8'))
manifest=[];audit=[]
for d in registry['records']:
 folder=root/'assets/expansion-v27'/d['id'];source=folder/('source-v2.png' if (folder/'source-v2.png').exists() else 'source-v1.png')
 if not source.exists():continue
 im=Image.open(source).convert('RGBA');w,h=im.size
 mask=im.getchannel('A').point(lambda a:255 if a>=200 else 0)
 def gutter(axis,center,radius,box):
  lo=max(1,round(center-radius));hi=min((w if axis=='x' else h)-1,round(center+radius))
  candidates=[]
  for p in range(lo,hi+1):
   strip=mask.crop((p,box[1],p+1,box[3]) if axis=='x' else (box[0],p,box[2],p+1))
   ink=strip.histogram()[255];candidates.append((ink,abs(p-center),p))
  return min(candidates)[2]
 # AI sheets have regular rows but may use asymmetric gutters. Locate the empty
 # gutters rather than clipping heads/fins at an assumed arithmetic midpoint.
 row_edges=[0]+[gutter('y',h*n/4,h*.075,(0,0,w,h)) for n in range(1,4)]+[h]
 splits=[gutter('x',w/2,w*.18,(0,row_edges[row],w,row_edges[row+1])) for row in range(4)]
 atlas=Image.new('RGBA',(192*8,160));eyes=[];clip=[];bounds=[]
 for i in range(8):
  col,row=i%2,i//2;box=(0 if col==0 else splits[row],row_edges[row],splits[row] if col==0 else w,row_edges[row+1]);cell=im.crop(box)
  # Ignore near-zero transparency only when locating bounds; preserve source alpha.
  bb=cell.getchannel('A').point(lambda a:255 if a>=200 else 0).getbbox()
  if not bb:raise ValueError(f'Empty generated cell: {d["id"]} {i}')
  silhouette=cell.getchannel('A').point(lambda a:255 if a>=200 else 0)
  # Sparse generated alpha noise at gutters is not proof of clipped anatomy.
  # Flag a material opaque run on the physical extraction boundary.
  edge_count=max(silhouette.crop((0,0,1,cell.height)).histogram()[255],silhouette.crop((cell.width-1,0,cell.width,cell.height)).histogram()[255],silhouette.crop((0,0,cell.width,1)).histogram()[255],silhouette.crop((0,cell.height-1,cell.width,cell.height)).histogram()[255])
  clip.append(edge_count>12)
  tile=cell.crop(bb);scale=min(166/tile.width,132/tile.height)
  if d['category']=='fish':scale*= [.34,.34,.6,.6,.8,.8,1,1][i]
  elif d['category']=='bottom_dweller':scale*= [.45,.45,.65,.65,.8,.8,1,1][i]
  tile=tile.resize((max(1,round(tile.width*scale)),max(1,round(tile.height*scale))),Image.Resampling.NEAREST)
  left=(192-tile.width)//2;top=148-tile.height if d['category']=='coral' else (160-tile.height)//2
  atlas.alpha_composite(tile,(i*192+left,top));bounds.append([left,top,tile.width,tile.height])
  eyes.append(None if d['category']=='coral' or i<2 else {'x':left+round(tile.width*.84),'y':top+round(tile.height*.43),'w':4,'h':4,'status':'source-eye registration provisional; visually review'})
 atlas.save(folder/'atlas-v1.png')
 facings=[1]*8
 if d['id']=='blue-assessor':facings[2]=facings[3]=-1
 meta={'id':d['id'],'category':d['category'],'path':source.relative_to(root).as_posix(),'atlas':(folder/'atlas-v1.png').relative_to(root).as_posix(),'frameWidth':192,'frameHeight':160,'frames':8,'nativeFacings':facings,'eyes':eyes,'bounds':bounds,'clippedSourceCells':[i for i,c in enumerate(clip) if c],'artStatus':'PARTIAL: source framing needs review' if any(clip) else 'Ready for user visual review','approved':False,'earliestStageStatus':'Illustrative study only; reproductive simulation unsupported' if d['category']=='bottom_dweller' else 'Game-calibrated development','sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
 (folder/'metadata-v1.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
 manifest.append({**meta,'src':'data:image/png;base64,'+base64.b64encode((folder/'atlas-v1.png').read_bytes()).decode()})
 audit.append({k:meta[k] for k in ['id','artStatus','clippedSourceCells','sha256']})
(root/'js/expansion-art-data.js').write_text('"use strict";\n// Generated local atlas manifest; no requests are needed for file:// canvas.\nAL.ExpansionSpriteData='+json.dumps(manifest,separators=(',',':'))+';\n',encoding='utf-8')
(root/'tests/expansion-evidence/art-audit.json').write_text(json.dumps({'sheets':len(manifest),'frames':len(manifest)*8,'entries':audit},indent=2),encoding='utf-8')
# Contact sheets are QA artifacts; source art and each stage remain unmodified.
for category in ['fish','coral','bottom_dweller']:
 subset=[d for d in registry['records'] if d['category']==category and (root/'assets/expansion-v27'/d['id']/'atlas-v1.png').exists()]
 if not subset:continue
 sheet=Image.new('RGB',(800,200*((len(subset)+3)//4)),(18,32,43));g=ImageDraw.Draw(sheet)
 for j,d in enumerate(subset):
  frame=4 if category=='coral' else 6
  tile=Image.open(root/'assets/expansion-v27'/d['id']/'atlas-v1.png').crop((frame*192,0,(frame+1)*192,160));x=(j%4)*200;y=(j//4)*200;sheet.paste(tile,(x+4,y+4),tile);g.text((x+5,y+166),d['name'][:29],fill=(235,241,244))
 sheet.save(root/'tests/expansion-evidence'/f'{category}-adult-contact.png')
print('Packed',len(manifest),'of 38 sheets;',sum(bool(x['clippedSourceCells']) for x in audit),'sheets flagged for framing review')
