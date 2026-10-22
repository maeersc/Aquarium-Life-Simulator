"""Technical alpha crop/nearest-neighbor atlas packing; never repaint source art."""
from pathlib import Path
from PIL import Image,ImageDraw
import json,base64,hashlib
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/expansion-v29'
ledger=json.loads((OUT/'registry.json').read_text(encoding='utf-8'))
bank=[];contact=Image.new('RGB',(7*256,5*210),'#142131')
for number,r in enumerate(ledger['records']):
 folder=OUT/r['id'];source=folder/('source-v3.png' if (folder/'source-v3.png').exists() else 'source-v2.png' if (folder/'source-v2.png').exists() else 'source-v1.png');im=Image.open(source).convert('RGBA');w,h=im.size
 r['art']['source']=source.relative_to(ROOT).as_posix()
 row_boxes=[]
 for row in range(2):
  top,bottom=round(row*h/2),round((row+1)*h/2)
  mask=im.crop((0,top,w,bottom)).getchannel('A').point(lambda a:255 if a>=24 else 0)
  runs=[]
  for x in range(w):
   if not mask.crop((x,0,x+1,mask.height)).getbbox():continue
   if not runs or x-runs[-1][1]>18:runs.append([x,x])
   else:runs[-1][1]=x
  if len(runs)!=4:
   raise RuntimeError('Inspect non-separated source subjects before packing: '+r['id']+' row '+str(row)+' '+str(runs))
  boxes=[]
  for left,right in runs:
   vertical=im.crop((left,0,right+1,h)).getchannel('A').point(lambda a:255 if a>=24 else 0)
   occupied=[y for y in range(h) if vertical.crop((0,y,vertical.width,y+1)).getbbox()]
   gaps=[(a,b) for a,b in zip(occupied,occupied[1:]) if b-a>=20 and h*.25<(a+b)/2<h*.8]
   split=round(sum(min(gaps,key=lambda ab:abs(sum(ab)/2-h/2)))/2) if gaps else round(h/2)
   boxes.append((left,0 if row==0 else split,right+1,split if row==0 else h))
  row_boxes.append(boxes)
 atlas=Image.new('RGBA',(192*8,160));bounds=[];flags=[]
 # Source: living developmental sequence on top; authored deceased equivalents below.
 # Runtime: early alive/dead, baby alive/dead, juvenile alive/dead, adult alive/dead.
 for index,cell in enumerate([0,4,1,5,2,6,3,7]):
  col,row=cell%4,cell//4;box=row_boxes[row][col];tile=im.crop(box)
  mask=tile.getchannel('A').point(lambda a:255 if a>=24 else 0);bb=mask.getbbox()
  if bb is None:raise RuntimeError('Missing sprite cell: '+r['id']+' '+str(cell))
  if box[0]<3 or box[2]>w-3 or bb[1]<3 or bb[3]>tile.height-3:flags.append(index)
  crop=tile.crop(bb);scale=min(176/crop.width,144/crop.height,1);sprite=crop.resize((max(1,round(crop.width*scale)),max(1,round(crop.height*scale))),Image.Resampling.NEAREST)
  x=index*192+(192-sprite.width)//2;y=(160-sprite.height)//2;atlas.alpha_composite(sprite,(x,y));bounds.append({'sourceCell':cell,'sourceBounds':list(bb),'packedBounds':[x-index*192,y,x-index*192+sprite.width,y+sprite.height]})
 atlas.save(folder/'atlas-v1.png')
 meta={'id':r['id'],'category':r['category'],'batch':'v2.9','frameWidth':192,'frameHeight':160,'frameCount':8,'nativeFacings':[1]*8,'eyes':[None]*8,'approved':False,'artStatus':'Original generated sprite sheet; NOT user approved'+('; source boundary review required' if flags else ''),'framingReviewFrames':flags,'sourceSize':[w,h],'sourceSha256':hashlib.sha256(source.read_bytes()).hexdigest(),'packing':'Alpha-only crop, nearest-neighbor fit; no semantic painting or recoloring','frames':bounds,'lifeStageBiology':r['earlyEquivalent'],'limits':'Static authored stage/state poses; full swim/turn/feeding animation is not claimed.'}
 (folder/'metadata-v1.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8')
 bank.append({**{k:meta[k] for k in ['id','category','batch','nativeFacings','eyes','artStatus','framingReviewFrames']},'src':'data:image/png;base64,'+base64.b64encode((folder/'atlas-v1.png').read_bytes()).decode()})
 adult=atlas.crop((6*192,0,7*192,160));thumb=Image.new('RGBA',(256,180));thumb.alpha_composite(adult,(32,10));contact.paste(thumb,(number%7*256,number//7*210),thumb);ImageDraw.Draw(contact).text((number%7*256+5,number//7*210+178),r['name'],fill='#e5e8ee')
 r['art']['framingReviewFrames']=flags;r['art']['aliveDeadSupport']='Eight authored static stage/state views';r['art']['approved']=False
contact.save(OUT/'adult-contact-v1.png')
for batch in range(5):
 page=Image.new('RGB',(1536,7*188),'#142131');draw=ImageDraw.Draw(page)
 for row,r in enumerate(ledger['records'][batch*7:(batch+1)*7]):
  atlas=Image.open(OUT/r['id']/'atlas-v1.png').convert('RGBA');page.paste(atlas,(0,row*188+25),atlas);draw.text((8,row*188+5),r['name']+' | early alive/dead, baby alive/dead, juvenile alive/dead, adult alive/dead',fill='#e5e8ee')
 page.save(OUT/f'stage-contact-{batch+1}-v1.png')
(OUT/'registry.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(ROOT/'js/update29-data.js').write_text('"use strict";\nAL.Update29Data='+json.dumps(ledger,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
(ROOT/'js/update29-art-data.js').write_text('"use strict";\nAL.Update29SpriteData='+json.dumps(bank,separators=(',',':'))+';\n',encoding='utf-8')
print('Packed 35 original atlases / 280 stage-state views; art remains unapproved. Framing flags:',sum(bool(r['art']['framingReviewFrames']) for r in ledger['records']))
