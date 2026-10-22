"""Pack generated marine sheets, register artist eye pixels and map shared early stages."""
import base64
import json
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parent.parent
STAGES=['egg','baby','juvenile','adult']

def find_eye(im,threshold=35):
    # Tighter pupil-only threshold avoids selecting lips or a shaded iris edge.
    w,h=im.size;points=set()
    for y in range(int(h*.15),int(h*.9)):
      for x in range(int(w*.74),int(w*.99)):
        r,g,b,a=im.getpixel((x,y))
        if a and max(r,g,b)<threshold and min(r,g,b)<threshold-10:points.add((x,y))
    candidates=[]
    while points:
      q=[points.pop()];part=[]
      while q:
        x,y=q.pop();part.append((x,y))
        for p in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
          if p in points:points.remove(p);q.append(p)
      xs=[p[0] for p in part];ys=[p[1] for p in part];bw=max(xs)-min(xs)+1;bh=max(ys)-min(ys)+1
      if len(part)<8 or bw>w*.14 or bh>h*.38 or not .6<bw/bh<1.7:continue
      cx=(max(xs)+min(xs))/2;cy=(max(ys)+min(ys))/2
      score=abs(cx/w-.89)*2+abs(cy/h-.43)*.6-min(len(part),500)/1200
      candidates.append((score,cx,cy,max(bw,bh)+6))
    if not candidates:
      if threshold<80:return find_eye(im,55 if threshold==35 else 80)
      raise ValueError('No pupil candidate; manual eye registration needed')
    return min(candidates)[1:]
# Source-pixel registration inspected against the generated dark-face artwork.
# These coordinates sample existing artist pixels; no pupil is painted or replaced.
MANUAL_EYES={
 'black-ocellaris':[(304,294,30),(703,282,32),(1075,359,30),(1468,363,30),(342,685,32),(719,685,32),(1098,683,32),(1483,684,32)],
 'black-snowflake':[(311,340,34),(731,330,36),(1086,406,34),(1480,398,34),(348,730,36),(731,730,36),(1109,730,36),(1493,728,36)],
 'midnight':[(289,343,38),(710,330,38),(1070,428,38),(1472,417,38),(338,710,38),(726,710,38),(1093,710,38),(1483,710,38)],
 'domino':[(335,304,36),(742,295,36),(1088,364,36),(1472,374,36),(341,703,36),(723,704,36),(1099,705,36),(1472,703,36)]
}

def split_components(path):
    """Lossless engineering extraction when separate fins share column ranges.

    The inspected eight animals do not touch in 2D. Preserve each whole alpha
    component instead of slicing through a projecting fin at a cell boundary.
    """
    im=Image.open(path).convert('RGBA');im.putalpha(im.getchannel('A').point(lambda a:255 if a>=128 else 0))
    w,h=im.size;a=im.getchannel('A').tobytes();remaining={i for i,v in enumerate(a) if v};components=[]
    while remaining:
      q=[remaining.pop()];part=[]
      while q:
        i=q.pop();part.append(i);x=i%w;y=i//w
        for p in ([i-1] if x else [])+([i+1] if x<w-1 else [])+([i-w] if y else [])+([i+w] if y<h-1 else []):
          if p in remaining:remaining.remove(p);q.append(p)
      if len(part)>1000:components.append(part)
    if len(components)!=8:raise ValueError(f'{path}: expected eight separated complete animals, found {len(components)}')
    components.sort(key=lambda p:(round(sum(i//w for i in p)/len(p)/h),sum(i%w for i in p)/len(p)))
    frames=[];boxes=[]
    for part in components:
      xs=[i%w for i in part];ys=[i//w for i in part];box=[min(xs),min(ys),max(xs)+1,max(ys)+1];c=im.crop(box);mask=Image.new('L',c.size);pixels=mask.load()
      for i in part:pixels[i%w-box[0],i//w-box[1]]=255
      c.putalpha(mask);frames.append(c);boxes.append(box)
    return frames,boxes

def split(path,rows):
    im=Image.open(path).convert('RGBA');im.putalpha(im.getchannel('A').point(lambda a:255 if a>=128 else 0));alpha=im.getchannel('A')
    rowcuts=[0]
    for row in range(1,rows):
        target=im.height*row/rows
        choices=[y for y in range(round(target-im.height*.12),round(target+im.height*.12)) if not alpha.crop((0,y,im.width,y+1)).getbbox()]
        if not choices:raise ValueError(str(path)+': overlapping row sprites; revise source')
        rowcuts.append(min(choices,key=lambda y:abs(y-target)))
    rowcuts.append(im.height);frames=[];boxes=[]
    for y0,y1 in zip(rowcuts,rowcuts[1:]):
        strip=im.crop((0,y0,im.width,y1));a=strip.getchannel('A');cuts=[0]
        for col in range(1,4):
            target=im.width*col/4;choices=[x for x in range(round(target-im.width*.12),round(target+im.width*.12)) if not a.crop((x,0,x+1,strip.height)).getbbox()]
            if not choices:raise ValueError(str(path)+': overlapping column sprites; revise source')
            cuts.append(min(choices,key=lambda x:abs(x-target)))
        cuts.append(im.width)
        for x0,x1 in zip(cuts,cuts[1:]):
            c=strip.crop((x0,0,x1,strip.height));b=c.getchannel('A').getbbox()
            if not b:raise ValueError('Missing frame: '+str(path))
            boxes.append([x0+b[0],y0+b[1],x0+b[2],y0+b[3]]);frames.append(c.crop(b))
    return frames,boxes

def pack():
    catalog=json.loads((ROOT/'assets/livestock/fish/clownfish/collection.json').read_text());records=[];failures=[]
    for family in ['species','varieties']:
      for e in catalog[family]:
        folder=ROOT/e['folder'];source=folder/('source-v2.png' if (folder/'source-v2.png').exists() else 'source-v1.png')
        if not source.exists():continue
        try:
          if e['id'] in ['longfin-ocellaris','lightning-maroon']:frames,boxes=split_components(source)
          else:frames,boxes=split(source,3 if family=='species' else 2)
          if family=='species':frame_map={stage:{'alive':i,'dead':i+4} for i,stage in enumerate(STAGES)};swim=[8,9,10,11];eyeless={0,4}
          else:frame_map={'juvenile':{'alive':0,'dead':2},'adult':{'alive':1,'dead':3}};swim=[4,5,6,7];eyeless=set()
          native_facings=[-1 if e['id']=='amphiprion-nigripes' and i==5 else 1 for i in range(len(frames))]
          eyes=[]
          for i,f in enumerate(frames):
            if i in eyeless:eyes.append(None)
            elif e['id']=='amphiprion-perideraion' and i==6:eyes.append((865-boxes[i][0],748-boxes[i][1],28))
            elif e['id'] in MANUAL_EYES:
              x,y,d=MANUAL_EYES[e['id']][i];eyes.append((x-boxes[i][0],y-boxes[i][1],d))
            elif native_facings[i]==-1:
              x,y,d=find_eye(f.transpose(Image.Transpose.FLIP_LEFT_RIGHT));eyes.append((f.width-1-x,y,d))
            else:eyes.append(find_eye(f))
          # Stable adult head registration, with one scale shared by the swim cycle.
          ex,ey=150,70
          scale=min((ex-8)/max(eyes[i][0] for i in swim),(192-8-ex)/max(frames[i].width-eyes[i][0] for i in swim),(ey-8)/max(eyes[i][1] for i in swim),(160-8-ey)/max(frames[i].height-eyes[i][1] for i in swim))
          canvases=[];registered=[]
          for i,f in enumerate(frames):
            c=Image.new('RGBA',(192,160))
            if i in swim:
              sc=scale;ox=round(ex-eyes[i][0]*sc);oy=round(ey-eyes[i][1]*sc)
            else:sc=min(176/f.width,144/f.height);ox=(192-round(f.width*sc))//2;oy=(160-round(f.height*sc))//2
            sampled=f.resize((round(f.width*sc),round(f.height*sc)),Image.Resampling.NEAREST);c.paste(sampled,(ox,oy));canvases.append(c)
            if eyes[i]:
              px,py,diam=eyes[i];d=max(4,min(14,round(diam*sc)));registered.append({'x':ex if i in swim else round(ox+px*sc),'y':ey if i in swim else round(oy+py*sc),'w':d,'h':d})
            else:registered.append(None)
          # Canonical local artist-eye pixels survive pose-to-pose resampling.
          e0=registered[swim[0]];box=(e0['x']-e0['w']//2,e0['y']-e0['h']//2,e0['x']-e0['w']//2+e0['w'],e0['y']-e0['h']//2+e0['h']);eye_patch=canvases[swim[0]].crop(box)
          for i in swim[1:]:canvases[i].paste(eye_patch,(box[0],box[1]));registered[i]=dict(e0)
          atlas=Image.new('RGBA',(192*len(canvases),160))
          for i,c in enumerate(canvases):atlas.paste(c,(i*192,0))
          atlas.save(folder/'atlas-v1.png')
          for stage,states in frame_map.items():
            for state,i in states.items():canvases[i].save(folder/f'{stage}_{state}.png')
          for number,i in enumerate(swim):canvases[i].save(folder/f'adult_swim_{number}.png')
          meta={'id':e['id'],'family':family,'speciesId':e['id'] if family=='species' else e['speciesId'],'name':e['name'],'scientificName':e['scientificName'],'source':source.name,'sourceBoxes':boxes,'atlas':e['folder']+'/atlas-v1.png','frameWidth':192,'frameHeight':160,'frameCount':len(canvases),'frameDurationMs':1000/6,'frames':frame_map,'swim':swim,'eyes':registered,'nativeFacings':native_facings,'anchor':[96,80],'bounds':[list(c.getchannel('A').getbbox()) for c in canvases],'sharedEarlySpeciesId':e['speciesId'] if family=='varieties' else None,'facing':'mirrored side profile; asymmetric individual markings provisional','reviewStatus':'Provisional - pending anatomy and user review','approved':False,'version':1}
          (folder/'metadata-v1.json').write_text(json.dumps(meta,indent=2)+'\n')
          meta['src']='data:image/png;base64,'+base64.b64encode((folder/'atlas-v1.png').read_bytes()).decode();records.append(meta)
        except Exception as exc:failures.append({'id':e['id'],'error':str(exc)})
    (ROOT/'js/clownfish-art-data.js').write_text('"use strict";\nAL.ClownArtManifest='+json.dumps({'records':records,'version':1})+';\n')
    (ROOT/'tests/clownfish-packing-report.json').write_text(json.dumps({'packed':len(records),'failures':failures},indent=2)+'\n')
    print(json.dumps({'packed':len(records),'failures':failures}))

if __name__=='__main__':pack()
