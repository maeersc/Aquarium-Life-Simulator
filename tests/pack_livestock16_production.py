"""Technical PNG extraction/registration, not an animation drawing generator.

The16 distinct drawings must come from the image_gen source. This packer finds
clear row/column gutters, thresholds transparent edges and samples with NEAREST.
Existing artist-eye pixels are registered consistently using the project's
established canonical-eye convention. No fin/body geometry is synthesized.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys
from PIL import Image,ImageDraw

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tests'))
from pack_clownfish_art import split,find_eye


def split16(source):
    try:return split(source,4)
    except ValueError as error:
        # Some authored grids have an unusually large outer transparent margin.
        # Locate the three largest genuinely empty interior gutters instead of
        # assuming that row centers occur at canvas quarter coordinates.
        im=Image.open(source).convert('RGBA');im.putalpha(im.getchannel('A').point(lambda a:255 if a>=128 else 0))
        def cuts(image,vertical=False):
            a=image.getchannel('A');length=image.width if vertical else image.height
            occupied=[bool(a.crop((i,0,i+1,image.height) if vertical else (0,i,image.width,i+1)).getbbox()) for i in range(length)]
            first=occupied.index(True);last=length-1-occupied[::-1].index(True);gaps=[];start=None
            for i in range(first,last+1):
                if not occupied[i] and start is None:start=i
                if occupied[i] and start is not None:gaps.append((i-start,(start+i)//2));start=None
            if len(gaps)<3:raise ValueError('Four authored grid groups cannot be separated by transparent gutters') from error
            return [0]+sorted(g[1] for g in sorted(gaps,reverse=True)[:3])+[length]
        rowcuts=cuts(im);frames=[];boxes=[]
        for y0,y1 in zip(rowcuts,rowcuts[1:]):
            strip=im.crop((0,y0,im.width,y1));columns=cuts(strip,True)
            for x0,x1 in zip(columns,columns[1:]):
                cell=strip.crop((x0,0,x1,strip.height));b=cell.getchannel('A').getbbox()
                if not b:raise ValueError('Missing authored cell') from error
                frames.append(cell.crop(b));boxes.append([x0+b[0],y0+b[1],x0+b[2],y0+b[3]])
        assert len(frames)==16
        return frames,boxes


def pack(source,destination,manual_eyes=None):
    source=Path(source);destination=Path(destination)
    assert destination.resolve().is_relative_to(ROOT.resolve())
    frames,boxes=split16(source)
    assert len(frames)==16
    facing_path=destination.with_name(destination.stem.replace('_swim_16','')+'-source-facings.json')
    native_facings=json.loads(facing_path.read_text())['facings'] if facing_path.is_file() else [1]*16
    assert len(native_facings)==16 and all(f in [-1,1] for f in native_facings)
    frames=[f.transpose(Image.Transpose.FLIP_LEFT_RIGHT) if facing==-1 else f for f,facing in zip(frames,native_facings)]
    overrides=destination.with_name(destination.stem.replace('_swim_16','')+'-eye-anchors.json')
    if manual_eyes is None and overrides.is_file():manual_eyes=json.loads(overrides.read_text())['eyes']
    eyes=[find_eye(f) for f in frames] if manual_eyes is None else manual_eyes
    width,height=192,160;ex,ey=150,72;reference_bounds=None
    reference_folder=ROOT/'planning/sprite-production/references'/source.parent.name
    if not reference_folder.is_dir():reference_folder=ROOT/'planning/sprite-production/variety-references'/source.parent.name
    stage=source.stem.split('-source')[0]
    reference_path=reference_folder/(stage+'.png')
    if reference_path.is_file():
        reference=Image.open(reference_path).convert('RGBA');width,height=reference.size
        ref_meta=json.loads((reference_folder/'metadata.json').read_text())[stage]['meta']
        ref_eye=ref_meta.get('eye')
        if ref_eye:ex,ey=ref_eye['x'],ref_eye['y']
        reference_bounds=reference.getchannel('A').point(lambda a:255 if a>=128 else 0).getbbox()
    scale=min((ex-4)/max(e[0] for e in eyes),(width-4-ex)/max(f.width-e[0] for f,e in zip(frames,eyes)),(ey-4)/max(e[1] for e in eyes),(height-4-ey)/max(f.height-e[1] for f,e in zip(frames,eyes)))
    if reference_bounds:
        scale=min(scale,(reference_bounds[2]-reference_bounds[0])/max(f.width for f in frames),(reference_bounds[3]-reference_bounds[1])/max(f.height for f in frames))
    canvases=[]
    for f,e in zip(frames,eyes):
        cv=Image.new('RGBA',(width,height));sample=f.resize((round(f.width*scale),round(f.height*scale)),Image.Resampling.NEAREST)
        cv.paste(sample,(round(ex-e[0]*scale),round(ey-e[1]*scale)));canvases.append(cv)
    eye_size=max(4,min(12,round(eyes[0][2]*scale)));eye_box=(ex-eye_size//2,ey-eye_size//2,ex-eye_size//2+eye_size,ey-eye_size//2+eye_size)
    eye=canvases[0].crop(eye_box)
    for cv in canvases[1:]:cv.paste(eye,eye_box[:2])
    hashes=[hashlib.sha256(cv.tobytes()).hexdigest() for cv in canvases]
    if len(set(hashes))!=16:raise ValueError('Not16 distinct drawn poses after native sampling')
    bounds=[cv.getchannel('A').getbbox() for cv in canvases]
    if any(not b or b[0]<=0 or b[1]<=0 or b[2]>=width or b[3]>=height for b in bounds):raise ValueError('Clipped native pose')
    atlas=Image.new('RGBA',(width*4,height*4))
    contact=Image.new('RGBA',(width*4,height*4),(18,38,53,255))
    for i,cv in enumerate(canvases):
        xy=(i%4*width,i//4*height);atlas.paste(cv,xy);contact.alpha_composite(cv,xy)
    destination.parent.mkdir(parents=True,exist_ok=True);atlas.save(destination)
    contact.save(destination.with_name(destination.stem+'-contact.png'))
    data={'source':str(source),'reference':str(reference_path) if reference_path.is_file() else None,'referenceBounds':reference_bounds,'sourceBoxes':boxes,'sourceNativeFacings':native_facings,'sourceEyeAnchors':eyes,'scale':scale,'frameWidth':width,'frameHeight':height,'columns':4,'frameCount':16,'anchor':[width/2,height/2],'eye':{'x':ex,'y':ey,'w':eye_size,'h':eye_size},'frameHashes':hashes,'bounds':bounds,'sha256':hashlib.sha256(destination.read_bytes()).hexdigest(),'technicalChecks':{'allCells':True,'binaryAlpha':True,'unique':True,'transparentMargins':True,'registeredEyes':True},'visualReview':'pending','playerApproved':False}
    destination.with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf8')
    return data


def pack_resident(source,destination,category,stage,motion):
    """Assemble authored appendages/tissue around an inspected stable body.

    No fish-eye heuristic is applied to compound eyes, shells or coral polyps.
    Body points and mutable polygons must come from actual native-cell review.
    A canonical first-pose skeleton/shell remains unchanged outside those areas.
    The only moving pixels are sampled from the sixteen original tool drawings.
    """
    source=Path(source);destination=Path(destination)
    assert category in ['coral','invertebrate'] and destination.resolve().is_relative_to(ROOT.resolve())
    frames,boxes=split16(source)
    stem=stage+'-'+motion
    registration=json.loads(destination.with_name(stem+'-body-anchors.json').read_text(encoding='utf8'))
    points=registration['points'];assert len(points)==16 and registration['agentInspected'] is True
    reference_path=ROOT/'planning/sprite-production/references'/source.parent.name/(stage+'.png')
    reference=Image.open(reference_path).convert('RGBA');width,height=reference.size
    reference_bounds=reference.getchannel('A').point(lambda v:255 if v>=128 else 0).getbbox()
    nx,ny=registration['nativePoint'];assert 4<nx<width-4 and 4<ny<height-4
    facing_path=destination.with_name(stem+'-source-facings.json')
    facings=json.loads(facing_path.read_text())['facings'] if facing_path.is_file() else [1]*16
    assert len(facings)==16 and all(f in [-1,1] for f in facings)
    frames=[f.transpose(Image.Transpose.FLIP_LEFT_RIGHT) if facing==-1 else f for f,facing in zip(frames,facings)]
    assert all(0<x<f.width and 0<y<f.height for f,(x,y) in zip(frames,points))
    scale=min((nx-4)/max(p[0] for p in points),(width-4-nx)/max(f.width-p[0] for f,p in zip(frames,points)),(ny-4)/max(p[1] for p in points),(height-4-ny)/max(f.height-p[1] for f,p in zip(frames,points)),(reference_bounds[2]-reference_bounds[0])/max(f.width for f in frames),(reference_bounds[3]-reference_bounds[1])/max(f.height for f in frames))
    canvases=[]
    for frame,(x,y) in zip(frames,points):
        cv=Image.new('RGBA',(width,height));sample=frame.resize((round(frame.width*scale),round(frame.height*scale)),Image.Resampling.NEAREST)
        cv.paste(sample,(round(nx-x*scale),round(ny-y*scale)));canvases.append(cv)
    regions_path=destination.with_name(stem+'-mutable-regions.json')
    regions=json.loads(regions_path.read_text(encoding='utf8'));assert regions['agentInspected'] is True and len(regions['description'])>40
    mask=Image.new('L',(width,height));draw=ImageDraw.Draw(mask)
    for polygon in regions['polygons']:
        assert len(polygon)>=3 and all(0<=x<width and 0<=y<height for x,y in polygon)
        draw.polygon([tuple(p) for p in polygon],fill=255)
    for polygon in regions.get('protectedPolygons',[]):
        assert len(polygon)>=3 and all(0<=x<width and 0<=y<height for x,y in polygon)
        draw.polygon([tuple(p) for p in polygon],fill=0)
    assert mask.getbbox() and len(set(mask.getdata()))==2
    mutable_runs=[]
    for y in range(height):
        start=None
        for x in range(width+1):
            active=x<width and mask.getpixel((x,y))!=0
            if active and start is None:start=x
            if not active and start is not None:mutable_runs.append([y,start,x]);start=None
    canonical=canvases[0].copy()
    protected_visible=sum(1 for a,m in zip(canonical.getchannel('A').getdata(),mask.getdata()) if a and not m)
    assert protected_visible>=16 and not mask.getpixel((round(nx),round(ny))) and canonical.getpixel((round(nx),round(ny)))[3]>0,'Registration must protect visible real body/skeleton pixels, not just empty background'
    canvases=[Image.composite(cv,canonical,mask) for cv in canvases]
    protected=Image.eval(mask,lambda v:255-v)
    static_hashes=[hashlib.sha256(Image.composite(cv,Image.new('RGBA',(width,height)),protected).tobytes()).hexdigest() for cv in canvases]
    assert len(set(static_hashes))==1
    hashes=[hashlib.sha256(cv.tobytes()).hexdigest() for cv in canvases]
    if len(set(hashes))!=16:raise ValueError('Tissue/appendage regions do not retain16 distinct authored poses')
    bounds=[cv.getchannel('A').getbbox() for cv in canvases]
    if any(not b or b[0]<=0 or b[1]<=0 or b[2]>=width or b[3]>=height for b in bounds):raise ValueError('Clipped native resident pose')
    atlas=Image.new('RGBA',(width*4,height*4));contact=Image.new('RGBA',atlas.size,(18,38,53,255))
    for i,cv in enumerate(canvases):
        xy=(i%4*width,i//4*height);atlas.paste(cv,xy);contact.alpha_composite(cv,xy)
    destination.parent.mkdir(parents=True,exist_ok=True);atlas.save(destination);contact.save(destination.with_name(destination.stem+'-contact.png'))
    # Match the existing bed attachment, including square legacy coral frames.
    anchor=[width/2,height/2] if category=='invertebrate' else [width/2,184 if height==192 else height]
    data={'source':str(source),'reference':str(reference_path),'referenceBounds':reference_bounds,'sourceBoxes':boxes,'sourceNativeFacings':facings,'sourceBodyAnchors':points,'bodyRegistrationPoint':[nx,ny],'scale':scale,'frameWidth':width,'frameHeight':height,'columns':4,'frameCount':16,'anchor':anchor,'eye':None,'frameHashes':hashes,'bounds':bounds,'sha256':hashlib.sha256(destination.read_bytes()).hexdigest(),'fixedStructure':{'canonicalPose':0,'mutableRegions':regions,'mutableMaskSha256':hashlib.sha256(mask.tobytes()).hexdigest(),'protectedPixelHashes':static_hashes},'technicalChecks':{'allCells':True,'binaryAlpha':True,'unique':True,'transparentMargins':True,'registeredBody':True,'fixedSkeletonOrShell':True},'visualReview':'pending','playerApproved':False}
    data['category']=category;data['stage']=stage;data['motion']=motion
    data['fixedStructure'].update(protectedVisiblePixels=protected_visible,mutableRuns=mutable_runs)
    destination.with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf8');return data


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('source');parser.add_argument('destination');args=parser.parse_args()
    result=pack(args.source,args.destination)
    print(json.dumps({'destination':args.destination,'frames':result['frameCount'],'scale':result['scale'],'visualReview':result['visualReview']}))
