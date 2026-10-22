"""Register existing visible eyes from the preserved native-coordinate QA sheets."""
from pathlib import Path
import json
r=Path(__file__).resolve().parents[2];p=r/'assets/animation/fish-registry.json';data=json.loads(p.read_text(encoding='utf8'))
points=[
('centropyge-loriculus',[(165,91),(164,78),(166,77)]),('centropyge-bispinosa',[(160,86),(165,79),(166,81)]),
('centropyge-argi',[(162,74),(160,75),(162,74)]),('centropyge-acanthops',[(158,74),(163,82),(166,82)]),
('centropyge-potteri',[(162,80),(162,84),(167,82)]),('centropyge-joculator',[(160,75),(163,78),(164,80)]),
('pygoplites-diacanthus',[(164,92),(164,79),(167,76)]),('pseudochromis-fridmani',[(163,71),(166,73),(166,73)]),
('forcipiger-flavissimus',[(124,85),(133,86),(138,85)]),('hemitaurichthys-polylepis',[(156,83),(149,88),(151,85)]),
('ctenochaetus-strigosus',[(157,86),(153,78),(155,77)]),('ctenochaetus-tominiensis',[(157,77),(157,75),(158,70)]),
('zebrasoma-xanthurum',[(164,83),(159,78),(158,77)]),('zebrasoma-gemmatum',[(158,88),(149,78),(154,82)]),
('acanthurus-achilles',[(162,81),(162,74),(162,73)]),('siganus-vulpinus',[(140,72),(143,75),(151,80)]),
('siganus-unimaculatus',[(164,80),(159,75),(159,76)]),('ecsenius-midas',[(165,72),(166,72),(171,63)]),
('salarias-fasciatus',[(163,75),(161,70),(164,70)]),('ecsenius-bicolor',[(163,73),(162,67),(162,70)]),
('paracheilinus-angulatus',[(163,80),(166,80),(169,88)]),('halichoeres-melanurus',[(167,82),(164,78),(168,77)]),
('halichoeres-chrysus',[(165,70),(162,77),(166,76)]),('macropharyngodon-meleagris',[(165,81),(165,76),(166,74)]),
('nemanthias-bartlettorum',[(161,80),(164,72),(167,74)])]
for id,stages in points:
 data['species'][id]['eyes']={stage:dict(x=x,y=y,w=18 if stage=='baby' else 12,h=16 if stage=='baby' else 12,registration='Existing eye; native atlas coordinates reviewed in eye-registration sheets') for stage,(x,y) in zip(['baby','juvenile','adult'],stages)}
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
(r/'js/fish-animation-data.js').write_text('"use strict";\n// Generated from assets/animation/fish-registry.json\nAL.FishAnimationData='+json.dumps(data,separators=(',',':'))+';\n',encoding='utf8')
print('Registered 75 existing life-stage eyes without repainting source artwork')
