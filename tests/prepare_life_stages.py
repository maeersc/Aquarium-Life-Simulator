"""Audit and pack generated life-stage sheets. No creative drawing; sources preserved."""
import base64
import json
import re
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
STAGES = ['egg', 'baby', 'juvenile', 'adult']
STATES = ['alive', 'dead']
BOTTOM = {'cory', 'pleco', 'watchman', 'blenny'}
DESCRIPTIONS = {
 'guppy': 'Guppy: golden orange male with ornate turquoise and orange fan tail. Egg equivalent is an INTERNAL gestating embryo in a translucent membrane, not external laid eggs. Baby has short transparent tail and plain slender body; juvenile develops small colored fan; adult elaborate broad fan.',
 'neon': 'Neon tetra: slender turquoise luminous upper stripe, red restricted to rear half underneath, silver front belly. Tiny scattered translucent amber eggs; larva with yolk and transparent finfold; juvenile short developing stripe; adult fully crisp blue and posterior red.',
 'cardinal': 'Cardinal tetra: intense electric blue stripe and RED entire lower body from head to tail, distinct from neon tetra. Translucent tiny scattered eggs, yolk larva, juvenile with developing red length, adult mature continuous colors.',
 'betta': 'Betta: wine-red and lavender male with flowing veil tail. Few pale eggs in tiny clear bubble nest; yolk larva, short-finned juvenile, mature deep crimson and periwinkle long flowing fins. Recognizable labyrinth fish anatomy.',
 'cory': 'Bronze corydoras: squat armored bottom catfish with bronze olive metallic flank, pale belly, barbels by downturned mouth and triangular dorsal fin. Small adhesive cream egg cluster; tiny translucent whiskered fry; juvenile developing armor and short barbels; mature bronze plates and strong barbels.',
 'danio': 'Zebra danio: slender silver gold fish with crisp longitudinal navy horizontal stripes extending into fins. Small scattered round eggs, nearly clear yolk larva, juvenile with broken developing stripes, adult full horizontal stripes and forked tail.',
 'harlequin': 'Harlequin rasbora: copper salmon body with large BLACK TRIANGULAR WEDGE on rear flank, forked tail. Small adhesive pale eggs; transparent yolk larva; juvenile subtle small wedge; adult vivid copper and strong triangular patch.',
 'platy': 'Platy: compact golden orange livebearer with red speckles, rounded tail, no sword. Egg equivalent is INTERNAL developing embryo in translucent membrane, never external laid eggs. Tiny plain short-finned fry, juvenile faint orange markings, stocky mature bright orange adult.',
 'angel': 'Freshwater angelfish: silver gold vertically flattened diamond body, BLACK VERTICAL BARS, long dorsal and anal triangles, two fine pelvic streamers. Adhesive eggs in short neat row; wriggler larva; juvenile more round with short fins; adult tall diamond and long streamers. Not marine angelfish.',
 'pleco': 'Bristlenose pleco: brown gold speckled armored flattened bottom catfish, downturned sucker mouth, broad pectoral fins, mature male snout bristles. Orange adhesive egg cluster; yellow yolk fry with broad small head; juvenile mottled armor and minimal bristles; adult broad armored body and branching snout bristles. Side profile, head right.',
 'clown': 'Ocellaris clownfish Amphiprion ocellaris, vivid orange three white bands edged fine black, rounded fins. Attached amber elongated eggs in small clutch with embryo eyes; translucent slender larva with finfold and faint orange; juvenile developing bands and shorter fins; adult same identity and style as approved reference. This is life-stage coverage, preserve reference identity.',
 'gramma': 'Royal gramma: purple HEAD and FRONT half, yellow REAR half and tail, small dark dorsal ocellus. Small clustered amber eggs; translucent slender larva; juvenile weak purple/yellow division; adult saturated purple head sharply transitioning yellow tail.',
 'firefish': 'Firefish: pale ivory anterior, orange-red posterior and tail, very long narrow upright first dorsal spine. Tiny clear adhesive eggs, translucent slender larva, juvenile short dorsal spike and light pink tail, mature long dorsal pennant and flame red rear.',
 'watchman': 'Yellow watchman goby: mustard golden yellow stocky bottom goby with turquoise blue spots, broad cheek and large high-set eye, rounded fins and two dorsal fins. Small amber elongated egg clutch; transparent slender larva; juvenile pale lemon developing spots; mature golden blue-spotted goby.',
 'banggai': 'Banggai cardinalfish: silver flattened body, three crisp black vertical bars, white polka dots on tall black fins, deeply forked trailing tail. Large orange egg cluster representing protected mouthbrood; tiny newly hatched fish with residual yolk and short fin tips; juvenile established bars but shorter rays; adult tall dramatic dotted fins.',
 'chromis': 'Blue-green chromis: compact iridescent aqua turquoise damselfish, deep body, forked tail, no invented stripes. Small adhesive transparent eggs; clear slender yolk larva; juvenile pale narrow turquoise body; adult deeper emerald cyan iridescence.',
 'yellowtang': 'Yellow tang: entirely brilliant lemon yellow disk-shaped fish, pointed snout, tall dorsal and anal fins, narrow tail peduncle with small white scalpel mark. Tiny pelagic transparent eggs; transparent elongated larval form; juvenile small translucent disk and emerging yellow; adult opaque bright yellow rounded disk.',
 'sixline': 'Six-line wrasse: slender pink purple body with six narrow longitudinal orange lines, green tail, small eye-striped pointed head. Tiny transparent pelagic eggs; clear slender larva; juvenile faint incomplete orange lines; adult purple/orange six-lined sleek wrasse.',
 'blenny': 'Tailspot blenny: small elongated rusty orange and blue gray benthic fish, blunt head with tiny eyebrow cirri, black ocellus at base of tail, long low dorsal. Small adhesive amber eggs, transparent slender larva, juvenile faint tail ocellus and stubby cirri, mature orange face blue-gray body and bold tailspot.',
 'marinebetta': 'Marine betta: dark midnight navy broad long fins with many pearl white spots and dark rear dorsal eyespot. Small amber egg cluster, delicate translucent larva, juvenile sparse large pale spots and short fins, adult elegant broad flowing navy fins and dense pearl spots.',
 'voidfin': 'FICTIONAL Voidfin specter: deep violet angelfish-like tall silhouette, ghostly mint cyan translucent fin edging, visible dark eye, no extra heads or limbs. Fictional luminous violet embryo eggs, wispy transparent larva, juvenile violet short fins, adult tall violet cyan spectral fins.',
 'glassfang': 'FICTIONAL Glassfang eel: very elongated glassy teal eel with pale yellow bioluminescent spine, small ivory fang at mouth, visible dark eye at right-facing head. Fictional translucent glowing mint eggs, ribbon larva with yolk, juvenile short narrow eel with tiny fang, mature long serpentine glass teal eel. Entire tail must fit each cell.',
 'zoa': 'Garden zoanthids: coral spawn pearl cluster; settled single tiny polyp; juvenile group of THREE button polyps; mature wide colony of many orange-centered violet tentacle-fringed button polyps on small rock. Dead eggs cloudy broken pearls; dead baby/juvenile/adult shriveled collapsed brown SOFT tissue with little dark bare substrate, NEVER white stony cups. No fish eyes.',
 'mushroom': 'Mushroom coral: soft corallimorph spawn pearls; tiny settled single mauve disc; juvenile two small frilled discs; adult three broad overlapping richly textured purple teal mushrooms. Dead states: cloudy failed spawn and progressively collapsed brown wrinkled soft tissue on substrate, NO hard white skeleton, NO tall stalk or terrestrial mushroom gills. No fish eyes.',
 'sps': 'Branching SPS stony coral: small pink spawn bundle; settled minute single calcifying polyp; juvenile sparse THREE-branched frag; mature complex branching cyan turquoise colony with violet and pale mint tips. Dead eggs cloudy; dead settled baby tiny bare skeleton; dead juvenile exposed gray branch skeleton; dead adult bare cream gray skeleton with no living colored tissue. Dead is not living pale bleaching.',
 'lps': 'Hammer LPS stony coral: small pink spawn pearls; baby single tiny settled fleshy polyp on skeletal cup; juvenile two small heads; adult large colony of mint hammer-ended tentacles on purple flesh and branching skeletal bases. Dead spawn cloudy; dead baby empty tiny cup; dead juvenile two bare cups; dead adult exposed gray cream branching skeleton and skeletal ridges, no colorful living tentacles.',
 'soft': 'Soft leather coral: coral spawn pearls; settled tiny polyp nub; juvenile small short stalk with few lobes; adult broad lavender pink leather crown on thick stalk with many fine golden polyps. Dead eggs cloudy; dead baby shriveled speck; dead juvenile collapsed dark limp stalk; dead adult fallen wrinkled brown leathery tissue, NO stony white skeleton.'
}

def audit():
    data=(ROOT/'js/data.js').read_text(encoding='utf-8')
    entries=[]
    for id,name in re.findall(r"fish\('([^']+)','([^']+)'",data):
        category='bottom_feeders' if id in BOTTOM else 'fish'
        entries.append(dict(id=id,name=name,category=category,status='IMPLEMENTED',scientificName='Amphiprion ocellaris' if id=='clown' else None,fictional=id in ['voidfin','glassfang'],runtimeType='fish'))
    for id,name in re.findall(r"(\w+):\{name:'([^']+)',water:'marine',price:\d+,color:",data):
        entries.append(dict(id=id,name=name,category='corals',status='IMPLEMENTED',scientificName=None,runtimeType='coral'))
    assert len(entries)==27 and len({e['id'] for e in entries})==27
    for e in entries:
        e['folder']=f"assets/livestock/life-stages/{e['category']}/{e['id']}"
        e['earlyEquivalent']='Internal embryo / gestation' if e['id'] in ['guppy','platy'] else 'Spawn / settled polyp / juvenile colony' if e['runtimeType']=='coral' else 'Protected mouthbrood' if e['id']=='banggai' else 'Egg / larva or fry'
        e['brief']=DESCRIPTIONS[e['id']]
    return entries

def scaffold(entries):
    base=ROOT/'assets/livestock/life-stages';base.mkdir(parents=True,exist_ok=True)
    (base/'catalog.json').write_text(json.dumps(entries,indent=2)+'\n',encoding='utf-8')
    for e in entries:
        folder=ROOT/e['folder'];folder.mkdir(parents=True,exist_ok=True)
        prompt=("Use case: stylized-concept. Asset: one production pixel-art life-stage sprite sheet for Aquarium Life. "
          "Reference image is STYLE ONLY: match its crisp intentional pixel clusters, 16-bit readability, vibrant arcade colors, detailed believable anatomy, premium indie lighting. "
          "Create EXACTLY 8 isolated sprites in a strict FOUR COLUMN by TWO ROW equal-cell grid on genuinely transparent alpha background. NO text, no labels, no grid lines, no scenery, no shadows outside sprites. "
          "TOP ROW left to right: viable EGG equivalent, living BABY, living JUVENILE, living ADULT. BOTTOM ROW left to right: nonviable EGG equivalent, dead BABY, dead JUVENILE, dead ADULT. "
          "Each stage is individually authored, not scaled duplicates: clear anatomical maturation. Each sprite centered inside its own cell with at least 12% transparent gutters on every side, no overlap or cropped parts. "
          "Use a landscape 1536 by 1024 sheet. Each cell about 384 by 512. Fit long fish horizontally within each cell. Egg and baby occupy less of cell than adult. "
          "Fish all face RIGHT, including dead fish. Living right-side profiles, eye clearly attached on head with dark pupil and bright glint. Dead fish right-facing side-fallen or belly-up with limp folded fins, desaturated but recognizable species colors, intact visible eyes, NO gore, no cross eyes. Coral remain attached at bottom, dead soft corals collapse, stony corals expose skeleton. "
          + e['brief'] + " Keep crisp pixel edges, avoid smooth painted gradients and excessive tiny noise. All eight cells must be present.")
        (folder/'GENERATION_PROMPT.md').write_text('# Life-stage generation prompt\n\nMethod: built-in imagegen. Reference: `assets/reference/approved_clownfish_hybrid.png`. Status: unapproved, awaiting user review.\n\n'+prompt+'\n',encoding='utf-8')
    catalog(entries,False)

def catalog(entries,complete):
    lines=['# Current livestock catalog','', 'Audit source: `js/data.js`, `js/core.js`, `js/simulation.js`, `js/render.js`, and existing local asset metadata. Updated 2026-10-11.','',
      '## Counts (no duplicate categories)','',
      '- Fish: 18 IMPLEMENTED; 5 additional ART ONLY.',
      '- Bottom feeders / benthic fish: 4 IMPLEMENTED (cory, pleco, watchman, blenny). These are part of the 22 playable fish, not four extra animals.',
      '- Corals: 5 IMPLEMENTED category-level entries; precise species are not defined in game data.',
      '- Total implemented livestock: 27 (22 fish + 5 corals). Six freshwater plants are flora, not animal livestock.',
      f'- Implemented entries with all eight authored stage/state images: {27 if complete else 0}. Missing stage sets: {0 if complete else 27}. Approval remains pending.',
      '- ART ONLY extras: 5, all lack full life-stage sets. DATA ONLY livestock: 0. PLANNED named fictional species: 3; excluded from implemented totals.','',
      '## Implemented entries','',
      '| Common name | Scientific name in data | ID | Category | Status | Current stage support | Missing art | Alive / dead art | Sprite path | Animation / quality | Notes |',
      '|---|---|---|---|---|---|---|---|---|---|---|']
    for e in entries:
        fish=e['runtimeType']=='fish';id=e['id'];folder=e['folder']
        old='`assets/livestock/fish/clownfish/clownfish-benchmark-v1-128.png`' if id=='clown' else f'`assets/livestock/corals/{id}/atlas-v11.png`' if not fish else '`js/render.js::legacySprite`'
        support='Simulation: brood, fry, juvenile, adult; art before update: shared adult scaled for growth' if fish else 'Simulation: colony size and health only; art before update: adult health states'
        art='8 distinct images; alive + dead for Egg/Baby/Juvenile/Adult' if complete else 'Missing dedicated Egg/Baby/Juvenile and all-stage authored death (corals have adult death)'
        path=f'[{id} atlas]({folder}/atlas-v1.png); prior {old}' if complete else old
        lines.append(f"| {e['name']} | {e['scientificName'] or ('Fictional' if e.get('fictional') else 'Not defined; do not infer')} | `{id}` | {e['category']} | IMPLEMENTED | {support} | {'None in static stage coverage' if complete else 'Dedicated stage sets'} | {art} | {path} | {'Static stage poses, Ready for Review; approved adult clown animation and existing coral health art retained' if complete else 'Legacy four-frame fish / adult coral states'} | {e['earlyEquivalent']}; no new simulation stages |")
    lines+=['','## Existing art-only subjects','', '| Name | Scientific name | ID | Status | Stages / missing | Alive / dead | Sprite path / animation / quality |','|---|---|---|---|---|---|---|']
    for id in ['niger-triggerfish','emperor-angelfish','red-lionfish','dogface-puffer','blue-tang']:
        m=json.loads((ROOT/f'assets/livestock/fish/{id}/metadata-v11.json').read_text())
        lines.append(f"| {m['name']} | {m['scientificName']} | `{id}` | ART ONLY | Adult only; Egg/Baby/Juvenile and dedicated death missing | Alive only; old inverted preview is not authored death art | `{m['atlas']}`; four swim frames; unapproved prior submission |")
    lines+=['','## Planned and absent content','',
      'Emberjaw Leviathan, Abyssal Crownfish and Prismheart Ray: PLANNED documentation mentions only; no working data, stage art, sprites or animations. No internal runtime IDs or scientific names. All stages missing; no claim of completion.',
      'Snails, shrimp, hermit crabs, starfish, sea cucumbers and urchins: no implemented records or dedicated sprites found. These are scope examples, not new species added by this update.',
      '## Boundaries','',
      'Existing growth thresholds (<0.3 fry, >=0.3 juvenile, 1 adult), reproduction and mortality remain authoritative. Coral early stages are review-only future art support. Egg for guppy/platy is an internal embryo equivalent, never a claim that they lay external eggs. Category-level coral spawn artwork is illustrative, not species-specific reproductive guidance.',
      'New assets are static stage poses. No separate fin-cycle animation is claimed. The approved adult clownfish and all prior sources remain preserved. The next planned task, only after this update is reviewed, is clownfish-only refinement.']
    (ROOT/'CURRENT_LIVESTOCK_CATALOG.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')

def split_sheet(path):
    im=Image.open(path).convert('RGBA')
    # Binary alpha is a pixel-art packing choice. Preserve the original RGBA source.
    im.putalpha(im.getchannel('A').point(lambda a:255 if a>=128 else 0))
    # The generated layout is ordered, but not always exactly evenly spaced.
    # Find transparent gutters near expected boundaries; never slice an animal.
    frames=[];boxes=[]
    alpha=im.getchannel('A')
    gaps=[y for y in range(round(im.height*.38),round(im.height*.65)) if alpha.crop((0,y,im.width,y+1)).getbbox() is None]
    if not gaps:raise ValueError(f'{path}: rows overlap; needs a revised source')
    middle=min(gaps,key=lambda y:abs(y-im.height/2));rowcuts=[0,middle,im.height]
    for row in range(2):
        y0,y1=rowcuts[row:row+2]
        strip=im.crop((0,y0,im.width,y1));alpha=strip.getchannel('A')
        occupied=[alpha.crop((x,0,x+1,strip.height)).getbbox() is not None for x in range(im.width)]
        cuts=[0]
        for col in range(1,4):
            target=im.width*col/4
            if path.parent.name=='pleco':target=[250,575,945][col-1]*im.width/1536
            choices=[x for x in range(round(target-im.width*.12),round(target+im.width*.12)) if not occupied[x]]
            if not choices:raise ValueError(f'{path}: no clear gutter at row {row}, column {col}')
            cuts.append(min(choices,key=lambda x:abs(x-target)))
        cuts.append(im.width)
        for a,b in zip(cuts,cuts[1:]):
            c=strip.crop((a,0,b,strip.height));bb=c.getchannel('A').getbbox()
            if not bb:raise ValueError(f'{path}: empty stage')
            frames.append(c.crop(bb));boxes.append([a+bb[0],y0+bb[1],a+bb[2],y0+bb[3]])
    return frames,boxes

def find_eye(im):
    # Find a compact dark pupil in the right-facing head, preserving authored pixels.
    w,h=im.size;points=set()
    for y in range(int(h*.15),int(h*.92)):
        for x in range(int(w*.72),int(w*.99)):
            r,g,b,a=im.getpixel((x,y))
            if a and max(r,g,b)<105 and min(r,g,b)<50:points.add((x,y))
    candidates=[]
    while points:
        q=[points.pop()];part=[]
        while q:
            x,y=q.pop();part.append((x,y))
            for p in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
                if p in points:points.remove(p);q.append(p)
        xs=[p[0] for p in part];ys=[p[1] for p in part];bw=max(xs)-min(xs)+1;bh=max(ys)-min(ys)+1
        if len(part)<3 or bw>w*.18 or bh>h*.55 or not .45<bw/bh<2.2:continue
        cx=(max(xs)+min(xs))/2;cy=(max(ys)+min(ys))/2
        score=abs(cx/w-.90)*3+abs(cy/h-.55)*.3- min(len(part),400)/1000
        candidates.append((score,cx,cy,bw,bh))
    if not candidates:raise ValueError('No pupil candidate; manual eye registration needed')
    _,x,y,w,h=min(candidates)
    return x,y,max(w,h)+4

def pack(entries):
    records=[]
    for e in entries:
        folder=ROOT/e['folder'];source=folder/('source-v2.png' if (folder/'source-v2.png').exists() else 'source-v1.png')
        if not source.exists():continue
        frames,boxes=split_sheet(source);out=[];eyes=[]
        for i,f in enumerate(frames):
            scale=min(176/f.width,144/f.height)
            resized=f.resize((round(f.width*scale),round(f.height*scale)),Image.Resampling.NEAREST)
            c=Image.new('RGBA',(192,160));x=(192-resized.width)//2;y=(160-resized.height)//2
            c.paste(resized,(x,y));out.append(c)
            if e['runtimeType']=='fish' and i%4:
                ex,ey,diam=find_eye(f)
                # The pleco's snout bristles fooled pupil detection. Use inspected
                # source-image head landmarks, not an arbitrary screen offset.
                if e['id']=='pleco':
                    source_eye={1:(514,333,32),2:(877,315,30),3:(1397,289,38),5:(498,837,30),6:(882,813,30),7:(1398,839,38)}[i]
                    ex,ey,diam=source_eye[0]-boxes[i][0],source_eye[1]-boxes[i][1],source_eye[2]
                eyes.append(dict(x=round(x+ex*scale),y=round(y+ey*scale),w=max(4,min(14,round(diam*scale))),h=max(4,min(14,round(diam*scale)))))
            else:eyes.append(None)
        atlas=Image.new('RGBA',(192*8,160))
        for i,c in enumerate(out):
            atlas.paste(c,(i*192,0))
            c.save(folder/f'{STAGES[i%4]}_{STATES[i//4]}.png')
        atlas.save(folder/'atlas-v1.png')
        record={k:v for k,v in e.items() if k!='brief'}
        record.update(version=1,approved=False,reviewStatus='Ready for Review',source=source.name,sourceBoxes=boxes,frameWidth=192,frameHeight=160,frameCount=8,frameDurationMs=None,animation='Static authored poses; no new fin-cycle animation',facing='mirrored right profile' if e['runtimeType']=='fish' else 'stationary',frames={stage:{state:j*4+i for j,state in enumerate(STATES)} for i,stage in enumerate(STAGES)},eyes=eyes,bounds=[list(c.getchannel('A').getbbox()) for c in out],atlas=e['folder']+'/atlas-v1.png')
        (folder/'metadata-v1.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
        record['src']='data:image/png;base64,'+base64.b64encode((folder/'atlas-v1.png').read_bytes()).decode()
        records.append(record)
    (ROOT/'js/life-stage-data.js').write_text('"use strict";\nAL.LifeStageManifest = '+json.dumps(dict(version=1,stages=STAGES,states=STATES,records=records))+';\n',encoding='utf-8')
    if len(records)==27:catalog(entries,True)
    print('Packed',len(records),'life-stage sheets /',len(records)*8,'individually authored stage-state images.')

if __name__=='__main__':
    import sys
    entries=audit()
    if '--pack' in sys.argv:pack(entries)
    else:
        scaffold(entries)
        print('Audited and scaffolded 27 implemented livestock: 18 fish, 4 benthic fish, 5 coral categories.')
