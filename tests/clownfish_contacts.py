"""Diagnostic atlas contact sheets; copies authored PNG pixels without drawing art."""
import json
from pathlib import Path
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parent.parent
catalog=json.loads((ROOT/'assets/livestock/fish/clownfish/collection.json').read_text())
species={e['id']:e for e in catalog['species']}
labels=[s+' '+life for life in ['alive','dead'] for s in ['egg','baby','juvenile','adult']]+['swim '+str(i) for i in range(4)]
for family in ['species','varieties']:
 entries=catalog[family]
 for page,start in enumerate(range(0,len(entries),7),1):
  batch=entries[start:start+7];contact=Image.new('RGB',(1340,40+len(batch)*128),'#121a27');g=ImageDraw.Draw(contact)
  for i,label in enumerate(labels):g.text((184+i*96,12),label,fill='#e3e8ee')
  for row,e in enumerate(batch):
   folder=ROOT/e['folder'];meta=json.loads((folder/'metadata-v1.json').read_text());atlas=Image.open(folder/'atlas-v1.png').convert('RGBA');y=40+row*128
   g.text((6,y+8),e['name'][:26],fill='#e3e8ee');g.text((6,y+26),e['id'][:26],fill='#91b5d3')
   pairs=[(s,life) for life in ['alive','dead'] for s in ['egg','baby','juvenile','adult']]
   for col,(stage,life) in enumerate(pairs):
    m=meta;a=atlas
    if family=='varieties' and stage in ['egg','baby']:
     base=ROOT/species[e['speciesId']]['folder'];m=json.loads((base/'metadata-v1.json').read_text());a=Image.open(base/'atlas-v1.png').convert('RGBA')
    index=m['frames'][stage][life];f=a.crop((192*index,0,192*(index+1),160));eye=m['eyes'][index]
    if m['nativeFacings'][index]==-1:
     f=f.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
     if eye:eye={**eye,'x':192-eye['x']}
    contact.paste(f.resize((96,80),Image.Resampling.NEAREST),(184+col*96,y+40),f.resize((96,80),Image.Resampling.NEAREST))
    if eye:g.rectangle((184+col*96+(eye['x']-eye['w']/2)/2,y+40+(eye['y']-eye['h']/2)/2,184+col*96+(eye['x']+eye['w']/2)/2,y+40+(eye['y']+eye['h']/2)/2),outline='#ffdc83')
   for i,index in enumerate(meta['swim']):
    f=atlas.crop((192*index,0,192*(index+1),160)).resize((96,80),Image.Resampling.NEAREST);contact.paste(f,(184+(8+i)*96,y+40),f)
  contact.save(ROOT/f'assets/previews/clownfish-{family}-contact-{page}.png')
print('Saved nine collection diagnostic sheets.')
