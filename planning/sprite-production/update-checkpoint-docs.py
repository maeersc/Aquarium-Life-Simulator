"""Publish an honest verified partial checkpoint, retaining the full master."""
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
paragraph=('The verified production checkpoint contains382 native sixteen-frame sheets (6112 actual authored cells), covering110 of113 usable marine entries: all89 fish, all15 corals and6 of9 invertebrates. Batches1–11 are complete. The remaining18 sheets belong to Fire Shrimp (Lysmata debelius), Randall\'s pistol shrimp (Alpheus randalli) and Harlequin Shrimp (Hymenocera picta). Built-in image generation returned HTTP429 daily usage_limit_reached; four Fire Shrimp source candidates were rejected for alpha noise and webbed appendages, and14 sources were not generated. No rejected candidate enters gameplay. The reported reset is2026-10-20 at09:37AM America/New_York. Original approved art remains active for these three species. All119 biological records, six acquisition holds, freshwater lock, local saves, biology and economy are preserved. Full production is NOT complete. Exact per-entry paths, missing work and current Chrome/Edge evidence are in [LIVESTOCK_16_FRAME_SPRITE_PRODUCTION_REPORT.md](LIVESTOCK_16_FRAME_SPRITE_PRODUCTION_REPORT.md). Player visual approval is separate.')
pattern=r'(## Full livestock sprite production — current work\n\n).*?(?=\n\n)'
def replace(text):
    updated,n=re.subn(pattern,lambda m:m[1]+paragraph,text,count=1,flags=re.S)
    assert n==1
    return updated
master_path=ROOT/'MASTER_DEVELOPMENT_PROMPT.md';before=master_path.read_text(encoding='utf8');after=replace(before)
assert len(re.findall(r'^# \d+\. ',after,re.M))==31
master_path.write_text(after,encoding='utf8')
for filename in ['ART_DIRECTION.md','CURRENT_LIVESTOCK_CATALOG.md','DEVELOPMENT_STATUS.md','FISH_ANIMATION_SYSTEM.md']:
    path=ROOT/filename;path.write_text(replace(path.read_text(encoding='utf8')),encoding='utf8')
path=ROOT/'PROJECT_CONTINUITY_SOURCE.md';text=path.read_text(encoding='utf8');assert text.count(before)==1
text=text.replace(before,after)
head,marker,tail=text.partition(after)
if re.search(pattern,head,re.S):head=replace(head)
text=head+marker+tail;assert text.count(after)==1;path.write_text(text,encoding='utf8')
path=ROOT/'FISH_ANIMATION_SYSTEM.md';text=path.read_text(encoding='utf8')
text=text.replace('# Marine fish animation architecture — v4.0.3','# Marine fish and resident animation architecture — v4.0.4 checkpoint',1)
text=text.replace('Approved authored adult clownfish cycles bypass procedural deformation. Other poses use final-size rasters and thin column strips:','Validated authored sixteen-frame cycles bypass procedural deformation. Only retained fallback poses use final-size rasters and thin column strips:',1)
text=text.replace('Poses use a global 768-entry LRU.','Procedural fallback poses use a global 768-entry LRU.',1)
text=text.replace('### Actual in-tank scale and early fin-layer gaps','### Historical v4.0.3 procedural scale audit and early fin-layer gaps',1)
old='All 94 are therefore classified B (partial), with zero falsely labeled fully authored/complete species. Sixty-three lack dedicated adult swim-cycle keyframes; 31 retain them. See FISH_ANIMATION_AUDIT.md for every species, actual tests and pending art.'
new='The historical full-action audit classified all94 fish records B (partial); its63 static adult sources and31 existing cycles describe the preproduction baseline. The current normal-motion production pass covers all89 usable fish and is tracked separately below. Dedicated yaw, occluded-side and action-specific artwork is not claimed by normal swim-sheet completion. See FISH_ANIMATION_AUDIT.md for the historical baseline.'
assert old in text;text=text.replace(old,new,1)
marker='### Validated sheet contract and caches'
contract=('### Original non-fish poses and fixed anatomy\n\nCoral and invertebrate sheets contain16 original image-tool drawings at each supported stage/state. Technical packing tracks an inspected visible body/skeleton landmark, samples with nearest-neighbor and assembles only the reviewed moving tissue/appendage areas around a canonical first-pose body. Explicit protected regions preserve oral centers, eyes and rigid shell/carapace/skeleton pixels; no procedural pose geometry is generated. Tiny polyp/feeding tissue responds while hard coral structures remain fixed. Shrimp/crab legs and appropriate feeding fans, snail/conch foot edges and larval existing appendages use separate real idle/walk drawings. Fine antenna masks that severed tips were rejected and corrected before registration. Original mortality art remains separate.\n\nReal per-sheet browser tests verify native16-cell uniqueness, protected pixels, actual rendering/selection, local save identities/value, renderer-rate independence and original death fallback. The mixed benchmark preloads actual adult source PNGs and draws250 fish,35 corals and40 invertebrates; it counts owned residents separately from the renderer\'s16 static printed backdrop silhouettes. Timing and exact accepted-sheet hashes are retained in the production evidence.\n\n')
assert marker in text;text=text.replace(marker,contract+marker,1);path.write_text(text,encoding='utf8')
print('Honest382-sheet checkpoint published;31 master sections and exact continuity retained.')
