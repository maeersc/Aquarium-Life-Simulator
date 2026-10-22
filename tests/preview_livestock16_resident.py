"""Unapproved native registration proof for manual tissue-mask inspection.

This only re-packs original image-tool poses. It neither authors motion nor
registers production art, and deliberately does not write approval metadata.
"""
import argparse
import json
from pathlib import Path
from PIL import Image
from pack_livestock16_production import split16

ROOT = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser()
p.add_argument('id')
p.add_argument('stage')
p.add_argument('state')
a = p.parse_args()
folder = ROOT / 'planning/sprite-production/packed' / a.id
stem = a.stage + '-' + a.state
registration = json.loads((folder / (stem + '-body-anchors.json')).read_text())
source = ROOT / 'planning/sprite-production/raw' / a.id / (stem + '-source-v1.png')
frames, boxes = split16(source)
reference = Image.open(ROOT / 'planning/sprite-production/references' / a.id / (a.stage + '.png')).convert('RGBA')
width, height = reference.size
rb = reference.getchannel('A').point(lambda v: 255 if v >= 128 else 0).getbbox()
nx, ny = registration['nativePoint']
points = registration['points']
scale = min((nx-4)/max(q[0] for q in points), (width-4-nx)/max(f.width-q[0] for f,q in zip(frames,points)), (ny-4)/max(q[1] for q in points), (height-4-ny)/max(f.height-q[1] for f,q in zip(frames,points)), (rb[2]-rb[0])/max(f.width for f in frames), (rb[3]-rb[1])/max(f.height for f in frames))
contact = Image.new('RGBA', (width*4,height*4), (18,38,53,255))
for i, (frame, (x,y)) in enumerate(zip(frames,points)):
    cv = Image.new('RGBA',(width,height))
    cv.paste(frame.resize((round(frame.width*scale),round(frame.height*scale)),Image.Resampling.NEAREST),(round(nx-x*scale),round(ny-y*scale)))
    contact.alpha_composite(cv, (i%4*width,i//4*height))
    if i == 0:
        cv.save(folder / (stem + '-unapproved-first.png'))
contact.save(folder / (stem + '-unapproved-contact.png'))
print(json.dumps({'sourceSize':Image.open(source).size,'scale':scale,'referenceBounds':rb,'preview':str(folder / (stem + '-unapproved-contact.png'))}))
