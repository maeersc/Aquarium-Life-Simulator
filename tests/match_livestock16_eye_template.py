"""Track an inspected original iris patch; no new eye pixels are painted."""
import argparse
import json
from pathlib import Path
from PIL import Image,ImageChops,ImageStat
root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('id');p.add_argument('stage');p.add_argument('x',type=int,nargs='?');p.add_argument('y',type=int,nargs='?');p.add_argument('--first-detected',action='store_true',help='Use only after inspecting that the first packed pose has the correct true iris.');p.add_argument('--size',type=int,default=24);p.add_argument('--kind',choices=['eye','body'],default='eye');p.add_argument('--state',choices=['swim','idle','walk','polyp_motion'],default='swim');p.add_argument('--native-x',type=int);p.add_argument('--native-y',type=int);a=p.parse_args()
path=root/'planning/sprite-production/packed'/a.id/(a.stage+'_'+a.state+'_16.json')
stem=a.stage+('-'+a.state if a.state!='swim' else '')
if path.is_file():meta=json.loads(path.read_text())
else:
    from pack_livestock16_production import split16
    source_path=root/'planning/sprite-production/raw'/a.id/(stem+'-source-v1.png')
    _,boxes=split16(source_path);meta={'source':str(source_path),'sourceBoxes':boxes}
if a.first_detected:
    assert a.kind=='eye'
    first_box=meta['sourceBoxes'][0];first_eye=meta['sourceEyeAnchors'][0];a.x=round(first_box[0]+first_eye[0]);a.y=round(first_box[1]+first_eye[1])
assert a.x is not None and a.y is not None
im=Image.open(meta['source']).convert('RGB');radius=a.size//2
template=im.crop((a.x-radius,a.y-radius,a.x-radius+a.size,a.y-radius+a.size))
first=meta['sourceBoxes'][0];ex=a.x-first[0];ey=a.y-first[1];right=first[2]-a.x;eyes=[];scores=[]
facing_path=path.with_name(stem+'-source-facings.json');facings=json.loads(facing_path.read_text())['facings'] if facing_path.is_file() else [1]*16
for box,facing in zip(meta['sourceBoxes'],facings):
    frame=im.crop(box)
    if facing==-1:frame=frame.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    w,h=frame.size;guessx=w-right;guessy=ey*h/(first[3]-first[1]);best=None
    for y in range(max(radius,round(guessy)-24),min(h-radius,round(guessy)+24)+1):
        for x in range(max(radius,round(guessx)-14),min(w-radius,round(guessx)+14)+1):
            crop=frame.crop((x-radius,y-radius,x-radius+a.size,y-radius+a.size));score=sum(ImageStat.Stat(ImageChops.difference(crop,template)).sum)
            if best is None or score<best[0]:best=(score,x,y)
    scores.append(best[0]);eyes.append([best[1],best[2],a.size])
output={'method':'Manually inspected first true iris, original-pixel template registration across16poses','firstSourceCenter':[a.x,a.y],'eyes':eyes,'matchingScores':scores}
if a.kind=='body':
    assert a.native_x is not None and a.native_y is not None
    output={'method':'Inspected first fixed body/skeleton landmark, original-pixel template tracking','agentInspected':True,'inspectionScope':'First source landmark manually identified; remaining matches require complete native contact review before production registration','firstSourceCenter':[a.x,a.y],'nativePoint':[a.native_x,a.native_y],'points':[p[:2] for p in eyes],'matchingScores':scores}
target=path.with_name(stem+('-body-anchors.json' if a.kind=='body' else '-eye-anchors.json'));target.parent.mkdir(parents=True,exist_ok=True);target.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'eyes':eyes,'scores':scores}))
