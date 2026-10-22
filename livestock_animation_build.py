"""Validate and embed explicitly registered, local 16-frame livestock sheets."""
import base64
import hashlib
import json
import re
import struct
from pathlib import Path


def generate(root):
    path = root/'assets/animation/livestock-registry.json'
    ledger = json.loads(path.read_text(encoding='utf8'))
    if ledger['frameCount'] != 16 or ledger['frameOrder'] != list(range(16)):
        raise ValueError('Livestock animation requires sixteen ordered authored cells')
    ids = [e['id'] for e in ledger['entries']]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate livestock animation identity')
    for entry in ledger['entries']:
        if entry['water'] != 'marine' or entry['category'] not in ['fish','coral','invertebrate']:
            raise ValueError('Protected or unknown livestock category')
        if not (root/entry['existingPath']).is_file():
            raise ValueError('Missing original livestock source: '+entry['id'])
        keys = set()
        if entry['framesCompleted'] != 16*len(entry['clips']):
            raise ValueError('Authored-frame total does not match real sheets')
        for clip in entry['clips']:
            key = (clip['stage'],clip['state'],clip.get('variety'))
            if key in keys:
                raise ValueError('Duplicate animation slot: '+entry['id'])
            keys.add(key)
            allowed={'fish':['swim','idle','rest','feed'],'coral':['polyp_motion','stressed','bleached','tissue-loss'],'invertebrate':['idle','walk','feed','rest']}
            if clip['stage'] not in entry['stages'] or clip['state'] not in allowed[entry['category']]:
                raise ValueError('Wrong biological stage/state')
            if clip['status'] != 'production':
                raise ValueError('Prototypes belong in the separate candidate ledger')
            if clip['frameCount'] != 16 or sorted(clip['order']) != list(range(16)):
                raise ValueError('Invalid frame indexing: '+entry['id'])
            width,height = clip['frameWidth'],clip['frameHeight']
            columns = clip['columns']
            if not all(isinstance(n,int) and n>0 for n in [width,height,columns]) or 16%columns or max(width,height)>256:
                raise ValueError('Invalid frame geometry')
            image = (root/clip['path']).resolve()
            if not image.is_relative_to(root.resolve()) or image.is_symlink():
                raise ValueError('Nonlocal animation path')
            raw = image.read_bytes()
            if raw[:8] != b'\x89PNG\r\n\x1a\n' or struct.unpack('>II',raw[16:24]) != (width*columns,height*(16//columns)):
                raise ValueError('PNG/cell dimensions do not match')
            if hashlib.sha256(raw).hexdigest() != clip['sha256']:
                raise ValueError('Unvalidated animation PNG changed')
            evidence=clip['validation']
            if any(evidence.get(k) is not True for k in ['alignment','identity','eyesOrAnatomy','patterns','attachment','loop','transparent','visualReview']):
                raise ValueError('Incomplete art validation')
            if len(set(evidence.get('frameHashes',[]))) != 16:
                raise ValueError('Blank/repeated frames cannot be counted as sixteen authored poses')
            if not isinstance(clip['anchor'],list) or len(clip['anchor'])!=2 or not 0<=clip['anchor'][0]<=width or not 0<=clip['anchor'][1]<=height:
                raise ValueError('Invalid anchor')
            if clip['facing'] not in ['mirror-side-profile','fixed'] or not 0<clip['framesPerSecond']<=16:
                raise ValueError('Invalid facing/timing')
            if entry['category']=='fish' and (clip['facing']!='mirror-side-profile' or clip['anchor']!=[width/2,height/2]):
                raise ValueError('Fish sheets need a stable centered head/body registration')
            if entry['category']=='fish' and clip['state']=='swim' and not 6<=clip['framesPerSecond']<=10:
                raise ValueError('Normal fish swim playback must begin within 6–10 fps')
            clip['src']='data:image/png;base64,'+base64.b64encode(raw).decode()
        if entry['status']=='complete' and any((entry.get('stageAliases',{}).get(stage,stage),state,None) not in keys for stage in entry['stages'] for state in entry['requiredStates']):
            raise ValueError('Required life-stage animation is missing')
    # Per-sheet classic scripts keep file:// canvases origin-clean without
    # eagerly parsing every base64 PNG. HTTPS uses the original PNG directly.
    folder=root/'assets/livestock/animation-sources';folder.mkdir(exist_ok=True)
    for entry in ledger['entries']:
        for clip in entry['clips']:
            source=clip.pop('src')
            content='"use strict";\nAL.SpriteSources.accept('+json.dumps(clip['path'])+','+json.dumps(source)+');\n'
            (folder/(clip['sha256']+'.js')).write_text(content,encoding='utf8')
    ledger['sourceTransport']='Per-sheet local classic script / original HTTPS PNG'
    target=root/'js/livestock-animation-data.js'
    target.write_text('"use strict";\n// Generated from assets/animation/livestock-registry.json\nAL.LivestockAnimationData='+json.dumps(ledger,separators=(',',':'),ensure_ascii=False)+';\n',encoding='utf8')
    tag='<script defer src="js/livestock-animation-data.js"></script>'
    start='<!-- AL_LIVESTOCK_SHEETS_START -->';end='<!-- AL_LIVESTOCK_SHEETS_END -->'
    block=start+'<!-- Native sheets load on demand. -->'+end
    for filename in ['index.html','livestock-animation-review.html']:
        html=root/filename;text=html.read_text(encoding='utf8')
        pattern=re.escape(tag)+'(?:'+re.escape(start)+'.*?'+re.escape(end)+')?'
        updated,count=re.subn(pattern,lambda m:tag+block,text,flags=re.S)
        if count!=1:raise ValueError('Missing/duplicate livestock metadata script in '+filename)
        html.write_text(updated,encoding='utf8')
    return ledger


if __name__=='__main__':
    result=generate(Path(__file__).resolve().parent)
    print('Livestock animation registry:',len(result['entries']),'entries;',sum(len(e['clips']) for e in result['entries']),'validated production sheets')
