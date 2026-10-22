"""Persist the complete authorized non-fish prompt manifest before generation."""
import json
from pathlib import Path

base=Path(__file__).resolve().parent
subjects={
 'sexy-anemone-shrimp':'Orange-red Thor shrimp with white round spots and raised abdomen. Lock raised body contour, markings and paired stalk eyes; tiny leg and antenna-tip movements only.',
 'porcelain-anemone-crab':'Cream porcelain crab with red spots, paired stalk eyes and large spotted claws. Lock carapace, body/eye positions and claw markings. Tiny attached leg steps and subtle feathery feeding-fan movements.',
 'bumblebee-snail':'Black/gold banded rigid conical shell, dark foot and two small eye tips. Shell/bands/eyes remain fixed. Extremely subtle foot-edge and tiny sensory tentacle-base changes only, no shell bounce or rotation.',
 'tiger-sand-conch':'Cream/brown patterned rigid shell, orange foot, proboscis and two black stalked eyes. Shell/markings/eye endpoints remain fixed; tiny foot/proboscis changes only, no shell bounce.',
 'halloween-hermit-crab':'Orange/red banded hermit in cream/brown spotted rigid spiral shell. Lock shell, eyes, trunk pattern and claw roots. Tiny alternating exposed leg steps, claw-tip/antenna-tip adjustments only.',
 'lysmata-amboinensis':'Red/yellow skunk cleaner shrimp with fixed white dorsal stripe, tail and head eyes. Tiny careful leg steps and small long pale antenna-tip changes only.',
 'lysmata-debelius':'Vivid red fire shrimp with discrete fixed white spots and pale antenna/leg tips. Lock trunk/head eyes. Very small attached leg and antenna-tip changes only.',
 'alpheus-randalli':'Red/cream segmented Randall pistol shrimp with oversized closed snapping claw. Lock trunk pattern, head eye and claw roots. Tiny bottom-oriented leg and antenna-tip motions; no claw snapping.',
 'hymenocera-picta':'Cream harlequin shrimp with purple/blue spots and broad petal-like appendages. Lock trunk pattern and eyes. Small careful leg steps and very slight petal-tip/antenna-tip changes, no broad flapping.'
}
layout=json.loads((base/'requests/sexy-anemone-shrimp-adult-idle.json').read_text())['prompt'].split(' ONE square transparent PNG')[1]
jobs=[]
for identity,subject in subjects.items():
 for stage in ['baby','juvenile','adult']:
  for state in ['idle','walk']:
   development=' Preserve supplied developing early-stage anatomy and original existing appendages. If larval, locomotion uses only small existing swimming appendage/antenna motions; never shrink an adult or invent adult legs.' if stage=='baby' else ''
   motion=' IDLE: nearly still resting posture, tiny distal appendage settling/feeding movements, no walking.' if state=='idle' else ' LOCOMOTION: calm alternating attached leg/foot motions appropriate to the species and life stage, drawn in place. Whole-body displacement is handled by the game.'
   prompt=f'Aquarium Life {identity} {stage.upper()} {state.upper()} actual16-frame pixel livestock sheet. Attached PNG is the exact approved stage anatomy, proportions, markings and detailed classic16-bit pixel-art identity. {subject}{development}{motion} ONE square transparent PNG'+layout
   jobs.append({'id':identity,'stage':stage,'state':state,'ref':str((base/'references'/identity/(stage+'.png')).resolve()),'prompt':prompt})
(base/'requests/invertebrate-all-prompts.json').write_text(json.dumps(jobs,indent=2)+'\n')
missing=[j for j in jobs if not (base/'requests'/(j['id']+'-'+j['stage']+'-'+j['state']+'.json')).is_file()]
print(json.dumps(missing))
