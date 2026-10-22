"""One-time explicit roster assignment. No biological data or assets are edited."""
from pathlib import Path
import json
r=Path(__file__).resolve().parents[2];rows=json.loads((r/'tests/fish-animation-evidence/before.json').read_text(encoding='utf8'))
families={
 'clown':dict(name='Clownfish short-tail hover',frequency=2.8,tail=1.15,fin=1.25,bodyHalf=.30,bob=.35),
 'basslet':dict(name='Rock-shelter hover and short excursions',frequency=2.2,tail=1.1,fin=1,bodyHalf=.27,bob=.28),
 'goby':dict(name='Substrate perch and short darts',frequency=3,tail=1.35,fin=.9,bodyHalf=.25,bob=0),
 'hoverGoby':dict(name='Small reef hover and dart',frequency=3.3,tail=1,fin=1,bodyHalf=.25,bob=.2),
 'blenny':dict(name='Rock perch and short repositioning',frequency=2.6,tail=1.2,fin=1.15,bodyHalf=.27,bob=0),
 'cruiser':dict(name='Steady caudal cruising',frequency=2.5,tail=1.6,fin=.85,bodyHalf=.32,bob=.15),
 'wrasse':dict(name='Fin-led reef swimming',frequency=3.4,tail=1.1,fin=1.55,bodyHalf=.23,bob=.2),
 'cardinal':dict(name='Gentle station-keeping',frequency=1.65,tail=.8,fin=1.3,bodyHalf=.17,bob=.22),
 'schooler':dict(name='Water-column cruising and hover',frequency=3,tail=1.4,fin=1.1,bodyHalf=.26,bob=.3),
 'extendedFin':dict(name='Deliberate extended-fin hover',frequency=1.5,tail=.85,fin=1.4,bodyHalf=.20,bob=.25),
 'dartfish':dict(name='Hover with brief caudal bursts',frequency=2.6,tail=1.3,fin=1.3,bodyHalf=.13,bob=.35),
 'angel':dict(name='Measured reef cruise and median fins',frequency=2.1,tail=1.1,fin=1.25,bodyHalf=.31,bob=.2),
 'butterfly':dict(name='Deep-body controlled reef cruise',frequency=2.2,tail=1.15,fin=1.1,bodyHalf=.32,bob=.2),
 'filefish':dict(name='Median-fin station keeping',frequency=2.4,tail=.7,fin=1.35,bodyHalf=.29,bob=.25),
 'boxfish':dict(name='Rigid-body fin paddling',frequency=2.3,tail=.7,fin=1.3,bodyHalf=.34,bob=.2),
 'fictional':dict(name='Existing fictional extended-fin glide',frequency=1.7,tail=.9,fin=1.2,bodyHalf=.18,bob=.3)
}
groups={
 'basslet':'gramma chalk-bass lantern-bass yellow-assessor blue-assessor candy-basslet pseudochromis-fridmani',
 'goby':'watchman greenbanded-goby sharknose-goby orange-spotted-prawn-goby randalls-prawn-goby hi-fin-red-banded-goby',
 'hoverGoby':'blue-striped-trimma-goby',
 'blenny':'blenny redspotted-blenny starry-blenny two-spot-blenny ecsenius-midas salarias-fasciatus ecsenius-bicolor',
 'cruiser':'yellowtang ctenochaetus-strigosus ctenochaetus-tominiensis zebrasoma-xanthurum zebrasoma-gemmatum acanthurus-achilles siganus-vulpinus siganus-unimaculatus',
 'wrasse':'sixline pink-streaked-wrasse white-banded-possum-wrasse tanakas-pygmy-wrasse carpenters-flasher-wrasse mccoskers-flasher-wrasse exquisite-fairy-wrasse lubbocks-fairy-wrasse ruby-longfin-fairy-wrasse yellow-candy-hogfish paracheilinus-angulatus halichoeres-melanurus halichoeres-chrysus macropharyngodon-meleagris',
 'schooler':'chromis blotched-anthias purple-queen-anthias nemanthias-bartlettorum',
 'cardinal':'banggai','extendedFin':'marinebetta','dartfish':'firefish','fictional':'voidfin',
 'angel':'centropyge-loriculus centropyge-bispinosa centropyge-argi centropyge-acanthops centropyge-potteri centropyge-joculator pygoplites-diacanthus',
 'butterfly':'copperband-butterflyfish forcipiger-flavissimus hemitaurichthys-polylepis',
 'filefish':'orange-spotted-filefish','boxfish':'spotted-boxfish'
}
mapping={id:family for family,ids in groups.items() for id in ids.split()}
for row in rows:
 if row['clown']:mapping[row['id']]='clown'
assert set(mapping)=={row['id'] for row in rows}
species={row['id']:{'family':mapping[row['id']],'tailRoot':.24,'headProtection':.26,'review':'Runtime rig tested; authored life-stage/side-specific anatomy remains subject to the existing art review'} for row in rows}
# Explicit anatomy exceptions use existing source geometry, not diet assumptions.
for id in ['banggai','marinebetta','voidfin']:species[id]['tailRoot']=.29
for id in ['firefish','watchman','blenny']:species[id]['tailRoot']=.25
data={'version':1,'scope':'Presentation-only artistic motion calibrations, not new biological claims','families':families,'species':species,'stages':{'baby':{'frequency':1.2,'amplitude':.7},'juvenile':{'frequency':1.1,'amplitude':.9},'adult':{'frequency':1,'amplitude':1}},'referenceOnly':['blue-tang','dogface-puffer','emperor-angelfish','niger-triggerfish','red-lionfish']}
p=r/'assets/animation';p.mkdir(exist_ok=True)
(p/'fish-registry.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
(r/'js/fish-animation-data.js').write_text('"use strict";\n// Generated from assets/animation/fish-registry.json\nAL.FishAnimationData='+json.dumps(data,separators=(',',':'))+';\n',encoding='utf8')
print('Explicit profiles for',len(species),'marine runtime records')
