from pathlib import Path
r=Path(__file__).resolve().parents[2]
note='''
### Actual in-tank scale and early fin-layer gaps

All 282 fish/stage combinations are also checked at the renderer's actual size, including the individual's size gene. The core guard now scales down to one scene pixel instead of covering all tiny fin-fold pixels. Separate outer-fin motion remains unsupported by four retained early-stage sources at the relevant size: Hi-fin Red-banded Goby (caudal-fold-only source), Whitebonnet Clownfish, Lubbock's Fairy Wrasse and Redspotted Blenny (outer fin pixels unresolved below 32 scene pixels). The renderer retains caudal fin/fold motion and protects body/yolk pixels; it does not manufacture paired fins. These are explicit art gaps, not passed independent-fin animation requirements. Larger applicable outer-fin poses and every stage's tail/caudal fold are tested. All four species remain class B pending dedicated early-fin artwork.

'''
p=r/'FISH_ANIMATION_SYSTEM.md';s=p.read_text(encoding='utf8');marker='\nFull authored turning,';assert marker in s;s=s.replace(marker,note+marker,1);p.write_text(s,encoding='utf8')
p=r/'MASTER_DEVELOPMENT_PROMPT.md';old=p.read_text(encoding='utf8');needle='Keep missing authored action/turn/anatomy art explicitly partial until delivered and reviewed.'
assert needle in old;new=old.replace(needle,needle+' Validate motion at actual in-tank sizes and preserve body/yolk pixels. When an early source only resolves a caudal fin fold, animate that existing fold and disclose the missing separate fin layer; never fake mature fins or count the source fully complete.',1);p.write_text(new,encoding='utf8')
p=r/'PROJECT_CONTINUITY_SOURCE.md';s=p.read_text(encoding='utf8');assert old in s;p.write_text(s.replace(old,new,1),encoding='utf8')
# Keep the reusable report generator honest when refreshing final evidence.
p=r/'planning/fish-animation/report.py';s=p.read_text(encoding='utf8');needle='## Per-species coverage\n';assert needle in s;s=s.replace(needle,note+'## Per-species coverage\n',1)
s=s.replace('source tail and outer-fin changes, head/core and sampled eye stability','source tail and applicable outer-fin changes (the four early source gaps above use caudal-fold motion only), head/core and sampled eye stability',1)
s=s.replace("if id=='banggai':notes+=", "if id in ['hi-fin-red-banded-goby','amphiprion-leucokranos','lubbocks-fairy-wrasse','redspotted-blenny']:notes+='; tiny early outer-fin layer unresolved, caudal fold only'\n if id=='banggai':notes+=",1)
p.write_text(s,encoding='utf8');print('Native-scale source limitations documented in primary art rules and audit')
