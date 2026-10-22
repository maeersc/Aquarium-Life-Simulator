"""Pack generated art; no creative drawing. Preserve all generated sources.
Pillow is developer-only. Runtime reads a classic embedded PNG resource.
"""
import base64
import json
import math
from pathlib import Path
from PIL import Image

ROOT=Path(__file__).resolve().parent.parent
fish=[('niger-triggerfish','Niger triggerfish','Odonus niger',(.88,.47)),
      ('emperor-angelfish','Emperor angelfish','Pomacanthus imperator',(.88,.47)),
      ('red-lionfish','Red lionfish','Pterois volitans',(.895,.51)),
      ('dogface-puffer','Dogface pufferfish','Arothron nigropunctatus',(.85,.45)),
      ('blue-tang','Blue tang','Paracanthurus hepatus',(.88,.45))]
corals=[('zoa','Zoanthids'),('mushroom','Mushroom corals'),('sps','Branching SPS'),('lps','Hammer LPS'),('soft','Soft leather coral')]
rocks=[('fiji','Fiji reef limestone'),('caribbean','Caribbean reef limestone'),('hawaiian','Hawaiian volcanic-inspired rock')]
records=[]

def cells(path,cols,rows):
    im=Image.open(path).convert('RGBA');frames=[]
    for row in range(rows):
        for col in range(cols):
            box=(round(col*im.width/cols),round(row*im.height/rows),round((col+1)*im.width/cols),round((row+1)*im.height/rows))
            c=im.crop(box);c.putalpha(c.getchannel('A').point(lambda v:255 if v>=128 else 0));bounds=c.getchannel('A').getbbox()
            if not bounds:raise ValueError(str(path)+' has an empty frame')
            frames.append(c.crop(bounds))
    return frames

def eye_center(frame,expected):
    # Locate a pupil near the declared head region; all anchors are visually reviewed.
    w,h=frame.size;points=set()
    for y in range(int(h*.22),int(h*.72)):
        for x in range(int(w*.72),int(w*.98)):
            r,g,b,a=frame.getpixel((x,y))
            if a and r<35 and g<45 and b<65:points.add((x,y))
    candidates=[]
    while points:
        start=points.pop();part=[start];queue=[start]
        while queue:
            x,y=queue.pop()
            for p in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if p in points:points.remove(p);queue.append(p);part.append(p)
        if len(part)<4:continue
        xs=[p[0] for p in part];ys=[p[1] for p in part];cx=sum(xs)/len(xs);cy=sum(ys)/len(ys)
        bw=max(xs)-min(xs)+1;bh=max(ys)-min(ys)+1
        if bw>w*.12 or bh>h*.18:continue
        score=((cx/w-expected[0])**2+(cy/h-expected[1])**2)*100+abs(math.log(bw/bh))*.01
        candidates.append((score,cx,cy,bw,bh))
    if not candidates:raise ValueError('Pupil candidate needs manual metadata')
    _,x,y,w,h=min(candidates);return x,y,w,h

def save_record(kind,id,name,frames,canvases,details):
    folder=ROOT/'assets/livestock'/kind/id;cw,ch=canvases[0].size
    atlas=Image.new('RGBA',(cw*len(canvases),ch))
    for i,c in enumerate(canvases):atlas.paste(c,(i*cw,0))
    atlas_name='atlas-v11.png';atlas.save(folder/atlas_name)
    bounds=[list(c.getchannel('A').getbbox()) for c in canvases]
    record={'id':id,'name':name,'family':kind,'status':'Ready for Review','approved':False,'frameWidth':cw,'frameHeight':ch,'frames':len(frames),'frameDurationMs':1000/6 if kind=='fish' else 1250,'atlas':f'assets/livestock/{kind}/{id}/{atlas_name}','bounds':bounds,'anchor':[cw//2,ch//2 if kind=='fish' else ch-8],**details}
    (folder/'metadata-v11.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    record['src']='data:image/png;base64,'+base64.b64encode((folder/atlas_name).read_bytes()).decode('ascii');records.append(record)

for id,name,scientific,expected in fish:
    folder=ROOT/f'assets/livestock/fish/{id}';path=folder/('source-v2.png' if (folder/'source-v2.png').exists() else 'source-v1.png');frames=cells(path,2,2);eyes=[eye_center(f,expected) for f in frames]
    ex,ey=150,56;pad=8
    scale=min((ex-pad)/max(e[0] for e in eyes),(192-pad-ex)/max(f.width-e[0] for f,e in zip(frames,eyes)),(ey-pad)/max(e[1] for e in eyes),(128-pad-ey)/max(f.height-e[1] for f,e in zip(frames,eyes)))
    out=[]
    for f,e in zip(frames,eyes):
        c=Image.new('RGBA',(192,128));resized=f.resize((round(f.width*scale),round(f.height*scale)),Image.Resampling.NEAREST);c.paste(resized,(round(ex-e[0]*scale),round(ey-e[1]*scale)));out.append(c)
    ew=max(6,round(eyes[0][2]*scale*2));eh=max(6,round(eyes[0][3]*scale*2))
    save_record('fish',id,name,frames,out,{'scientificName':scientific,'runtimeSpeciesId':None,'usage':'ART ONLY; no gameplay species added','eye':{'x':ex,'y':ey,'w':ew,'h':eh},'facingBehavior':'mirror-side-profile','animations':{'swim':[0,1,2,3],'idle':[0,1,2,3],'death':[0]},'turning':'stable mirrored side views; no intermediate perspective frames','layer':'livestock'})

for id,name in corals:
    folder=ROOT/f'assets/livestock/corals/{id}';path=folder/('source-v2.png' if (folder/'source-v2.png').exists() else 'source-v1.png');frames=cells(path,5,2)
    scale=min(174/max(f.width for f in frames),174/max(f.height for f in frames));out=[]
    for f in frames:
        c=Image.new('RGBA',(192,192));f=f.resize((round(f.width*scale),round(f.height*scale)),Image.Resampling.NEAREST);c.paste(f,((192-f.width)//2,184-f.height));out.append(c)
    save_record('corals',id,name,frames,out,{'runtimeFloraId':id,'states':['healthy','stressed','bleached','tissue-loss','dead'],'stateFrames':{s:[i,i+5] for i,s in enumerate(['healthy','stressed','bleached','tissue-loss','dead'])},'facingBehavior':'stationary','layer':'flora','source':path.name,'rigid':id=='sps'})

for id,name in rocks:
    folder=ROOT/f'assets/livestock/rocks/{id}';path=folder/('source-v2.png' if (folder/'source-v2.png').exists() else 'source-v1.png');frames=cells(path,2,2);scale=min(174/max(f.width for f in frames),174/max(f.height for f in frames));out=[]
    for f in frames:
        c=Image.new('RGBA',(192,192));f=f.resize((round(f.width*scale),round(f.height*scale)),Image.Resampling.NEAREST);c.paste(f,((192-f.width)//2,184-f.height));out.append(c)
    save_record('rocks',id,name,frames,out,{'variants':['small','medium','large','arch'],'facingBehavior':'stationary','layer':'hardscape','material':'volcanic-inspired' if id=='hawaiian' else 'reef-limestone','chemistryEffects':'none assigned by this art update'})

manifest={'version':'art-1.1','records':records}
(ROOT/'js/art-assets-data.js').write_text('"use strict";\nAL.ArtUpdateManifest = '+json.dumps(manifest)+';\n',encoding='utf-8')
print('Packed',len(records),'asset families; all sources preserved.')
