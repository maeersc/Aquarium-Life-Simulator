"""Synchronize production authority without dropping the consolidated master."""
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
master_path=ROOT/'MASTER_DEVELOPMENT_PROMPT.md'
before=master_path.read_text(encoding='utf8')
heading='## Livestock16-frame expansion — playable v4.0.4 / MDPv4.7'
current='''## Full livestock sprite production — current work

Actual sprite production is now authorized and underway. The authoritative usable roster contains113 marine entries:89 fish,15 corals and9 invertebrates. All119 existing registered records and six acquisition holds are retained. Current registered assets, completed batches, browser evidence and remaining work are tracked in [LIVESTOCK_16_FRAME_SPRITE_PRODUCTION_REPORT.md](LIVESTOCK_16_FRAME_SPRITE_PRODUCTION_REPORT.md). The earlier zero-sheet infrastructure report is historical. Production is not complete until every eligible entry and final release have passed their required checks. Player visual approval is separate.

'''

def replace_status(text):
    if heading not in text:return text
    start=text.index(heading);end=text.find('\n#',start+len(heading))
    assert end>start
    return text[:start]+current+text[end+1:]

after=replace_status(before)
after=after.replace('LIVESTOCK_ANIMATION_16_FRAME_REPORT.md is the per-entry evidence/status ledger','LIVESTOCK_16_FRAME_SPRITE_PRODUCTION_REPORT.md is the current per-entry production/evidence ledger; LIVESTOCK_ANIMATION_16_FRAME_REPORT.md remains the historical infrastructure audit')
after=after.replace('current authored-art coverage is in LIVESTOCK_ANIMATION_16_FRAME_REPORT.md.','current authored-art coverage is in LIVESTOCK_16_FRAME_SPRITE_PRODUCTION_REPORT.md.')
needle='The sole presentation authority remains AL.FishAnimation'
if 'Production sources and exact prompts are retained' not in after:
    at=after.index(needle)
    after=after[:at]+'''Production sources and exact prompts are retained under planning/sprite-production. Produce actual sixteen-pose drawings with the built-in image tool, pack and inspect every native cell before central registration, and run real gameplay/gallery checks for each batch before continuing. Technical alpha extraction, nearest-neighbor packing, consistent original-eye registration and declared native-facing normalization do not create extra drawn poses. Preserve the biological-species early source shared by designer babies and Banggai's existing baby-to-developed-juvenile alias; do not double-count shared source sheets. Completion is based on actual assets and current file-hash evidence, never requested frame slots or player approval inferred from agent inspection.

'''+after[at:]
master_path.write_text(after,encoding='utf8')
for filename in ['ART_DIRECTION.md','CURRENT_LIVESTOCK_CATALOG.md','DEVELOPMENT_STATUS.md']:
    path=ROOT/filename;path.write_text(replace_status(path.read_text(encoding='utf8')),encoding='utf8')
continuity=ROOT/'PROJECT_CONTINUITY_SOURCE.md';text=continuity.read_text(encoding='utf8')
assert text.count(before)==1
text=text.replace(before,after);text=replace_status(text)
assert text.count(after)==1
continuity.write_text(text,encoding='utf8')
path=ROOT/'FISH_ANIMATION_SYSTEM.md';text=replace_status(path.read_text(encoding='utf8'))
text=text.replace('This release has zero production sheet records; fixture tests exercise the code without pretending they are animal art.','Actual registered production PNGs now use this contract; current sheet counts and file-hash-matched browser evidence are in LIVESTOCK_16_FRAME_SPRITE_PRODUCTION_REPORT.md. Synthetic loader fixtures remain explicitly separate from animal artwork.')
text=text.replace('`source` selects only an exact-stage/exact-variety swim sheet, otherwise the existing source.','`source` selects the registered stage/variety swim sheet, with only explicit existing stage aliases and designer early-stage sharing permitted; otherwise it retains the original source. The metadata includes biological and designer identity.')
text=text.replace('`source` preserves asset priority and approved natural adult Ocellaris benchmark frames. Other adult clownfish retain their four authored swim frames.','`source` now prioritizes validated sixteen-frame production sheets for covered stages/varieties. Original natural Ocellaris benchmark and four-pose adult clownfish sources remain the unchanged reference/fallback authorities.')
text=text.replace('Full status, remaining layers and candidate rejection are in LIVESTOCK_ANIMATION_16_FRAME_REPORT.md.','Current per-entry production, remaining work and validation are in LIVESTOCK_16_FRAME_SPRITE_PRODUCTION_REPORT.md; older infrastructure/candidate evidence remains historical.')
path.write_text(text,encoding='utf8')
print('Production documentation synchronized; exact consolidated master retained in continuity.')
