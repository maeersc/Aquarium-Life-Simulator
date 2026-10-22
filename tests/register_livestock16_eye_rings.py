"""Register existing artist iris-ring pixels for high-contrast head art."""
import json
from pathlib import Path
import sys
from PIL import Image
root=Path(__file__).resolve().parents[1]
id=sys.argv[1];stage=sys.argv[2] if len(sys.argv)>2 else 'adult'
path=root/'planning/sprite-production/packed'/id/(stage+'_swim_16.json');meta=json.loads(path.read_text());im=Image.open(meta['source']).convert('RGBA');eyes=[]
for box in meta['sourceBoxes']:
    frame=im.crop(box);w,h=frame.size;points=[]
    for y in range(round(h*.42),round(h*.60)):
        for x in range(round(w*.83),round(w*.96)):
            r,g,b,a=frame.getpixel((x,y))
            match=b>80 and r<110 and b>r*1.5 and b>g*1.32 if id=='banggai' else r>120 and g>90 and b<130 and r>b*1.5 and g>b*1.3
            if a>=128 and match:points.append((x,y))
    if len(points)<10:raise ValueError('Iris ring unresolved: '+str(len(eyes)))
    xs=[x for x,y in points];ys=[y for x,y in points]
    eyes.append([(min(xs)+max(xs))/2,(min(ys)+max(ys))/2,max(max(xs)-min(xs)+1,max(ys)-min(ys)+1)+2])
destination=path.with_name(stage+'-eye-anchors.json');destination.write_text(json.dumps({'method':'Existing iris pixels registered in inspected head region; no eye repaint','eyes':eyes},indent=2)+'\n')
print(json.dumps(eyes))
