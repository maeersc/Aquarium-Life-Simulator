"""Report actual registered production and current evidence; never infer finished art."""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
registry=json.loads((ROOT/'assets/animation/livestock-registry.json').read_text(encoding='utf8'))
ledger=json.loads((ROOT/'planning/sprite-production/production-ledger.json').read_text(encoding='utf8'))
blocker_path=ROOT/'planning/sprite-production/blockers.json'
blocker=json.loads(blocker_path.read_text(encoding='utf8')) if blocker_path.is_file() else {}
runtime={e['id']:e for e in registry['entries']}
reports=[]
for browser in ['chrome','edge']:
    path=ROOT/'tests/sprite-production-evidence'/(browser+'-results.json')
    if path.is_file():reports.append(json.loads(path.read_text(encoding='utf8')))

def covered(clip,report):
    return report['failed']==0 and any(r['path']==clip['path'] and r.get('sha256')==clip['sha256'] for r in report['coverage'])

for entry in ledger['eligible']:
    row=runtime[entry['id']];clips=row['clips']
    for clip in clips:
        assert hashlib.sha256((ROOT/clip['path']).read_bytes()).hexdigest()==clip['sha256']
    entry['gameplayValidation']={r['browser']:all(covered(c,r) for c in clips) if clips else False for r in reports}
    # Full completion requires every stage/morph, both actual browser reports,
    # maximum-stock performance, offline equivalence and per-clip save/click tests.
    full_evidence=all(any(r['browser']==browser and r['failed']==0 and r.get('performance') and all(covered(c,r) for c in clips) for r in reports) for browser in ['chrome','edge'])
    entry['fullyComplete']=row['status']=='complete' and bool(clips) and full_evidence
    if entry['fullyComplete']:entry['state']='complete; agent art review and Chrome/Edge gameplay validation passed; player approval pending'
    if not entry['fullyComplete'] and entry['id'] in blocker.get('affectedIds',[]):
        entry['state']='blocked by image generation daily quota; original artwork retained'
        entry['externalBlocker']=blocker['status']
    else:entry.pop('externalBlocker',None)

complete=[e for e in ledger['eligible'] if e['fullyComplete']]
for batch in ledger['batches']:
    members=[e for e in ledger['eligible'] if e['id'] in batch['ids']]
    batch['status']='complete' if all(e['fullyComplete'] for e in members) else 'blocked' if all(e['fullyComplete'] or e.get('externalBlocker') for e in members) else 'in production' if any(runtime[e['id']]['clips'] for e in members) else 'queued'
clips=[c for e in ledger['eligible'] for c in runtime[e['id']]['clips']]
required_slots={}
for entry in ledger['eligible']:
    row=runtime[entry['id']]
    slots={(row.get('stageAliases',{}).get(stage,stage),state,None) for stage in row['stages'] for state in row['requiredStates']}
    slots|={(stage,'swim',v['id']) for v in row['varieties'] for stage in ['juvenile','adult']}
    required_slots[row['id']]=slots
lines=['# Livestock 16-frame sprite production report','',
       'This is the actual production ledger. Earlier zero-sheet infrastructure audits are historical. Counts below refer to native PNG sheets containing sixteen distinct authored cells, not requested frame slots.','',
       f"Eligible livestock: **{len(ledger['eligible'])}** (89 fish, 9 usable invertebrates, 15 corals). Six acquisition holds remain outside production scope; all119 original records are retained.",
       f"Registered sheets: **{len(clips)}**; authored cells: **{len(clips)*16}**.",
       f"Required physical stage/state/variety sheets: **{sum(len(s) for s in required_slots.values())}**. Shared biological baby sources are counted once; invertebrates require separate idle and walking cycles.",
       f"Fully checked entries: **{len(complete)}**; unfinished: **{len(ledger['eligible'])-len(complete)}**.",
       f"Completed batches: **{sum(b['status']=='complete' for b in ledger['batches'])}/{len(ledger['batches'])}**. Entries blocked by an external condition: **{sum(bool(e.get('externalBlocker')) for e in ledger['eligible'])}**; other unfinished entries remain queued or in production.",
       f"Complete fish: **{sum(e['category']=='fish' for e in complete)}**; complete bottom dwellers/invertebrates: **{sum(e['category']=='invertebrate' for e in complete)}**; complete corals: **{sum(e['category']=='coral' for e in complete)}**.",
       '','Built-in image_gen produces the original sixteen drawings per sheet. Exact prompts and untouched generation sources are retained in `planning/sprite-production/requests` and `raw`. Packing uses nearest-neighbor sampling, actual-alpha gutters, consistent scale and original-pixel eye registration. Declared opposite-facing source cells are mirrored into the central facing convention; no extra poses are synthesized. Original approved source/death art remains separate. Player art approval is not claimed.','',
       'Banggai baby presentation continues to share its developed mouthbrooded-release juvenile source. Designer baby stages continue to share biological-species early artwork. Shared sources are not counted as newly drawn sheets.','',
       'Coral and invertebrate packing registers an inspected visible body/skeleton landmark and assembles only original authored tissue/appendage pixels inside manually reviewed masks. Canonical original body/shell/skeleton/eye pixels remain identical outside those masks. All final16 native cells are inspected after technical assembly; no motion poses are synthesized. Living mouth/inner-disc centers and hard coral structures stay fixed. Rejected disconnected fine-tip masks are corrected before registration.','',
       '## Current validation','']
for report in reports:
    current=sum(covered(c,report) for c in clips)
    lines.append(f"- {report['browser']}: {report['passed']} passed, {report['failed']} failed; current-SHA coverage {current}/{len(clips)} sheets.")
    if report.get('performance'):lines.append('  Maximum-stock rendering: '+json.dumps(report['performance'])+'.')
    if report.get('mixedPerformance'):lines.append('  Mixed250fish/35coral/40invertebrate rendering (static backdrop excluded from owned counts): '+json.dumps(report['mixedPerformance'])+'.')
if any(e.get('externalBlocker') for e in ledger['eligible']):
    lines+=['','## Recorded external blocker','',blocker['reason'],'',f"The tool reports a reset at {blocker['resetAtPlayerTime']}. The API fallback has no locally configured credential and has not been authorized. Remaining required sheets: {blocker['missingPhysicalSheets']}. Original approved sprites continue to serve these three species; no rejected drawings or fabricated completion are used.",'']
lines+=['','Full completion requires all supported standard and designer stage slots, agent inspection of all16 cells, and current Chrome/Edge tests for PNG loading, distinct frames, stable iris, source authority, procedural-warp bypass, both facings, canvas clicking, real local save/load, frame-rate-independent playback, offline equivalence, bounded caches, maximum-stock rendering and freshwater lock.','',
        '## Per-entry production','',
        '| Batch | Species / ID | Category | Original source | Registered new sheets / life stages | Validation | Remaining work | Fully complete |',
        '|---|---|---|---|---|---|---|---|']
for entry in ledger['eligible']:
    row=runtime[entry['id']];assets='<br>'.join(f"[{c.get('variety','standard')}/{c['stage']}/{c['state']}]({c['path']})" for c in row['clips']) or 'None yet'
    validation=', '.join(k+': '+('current pass' if v else 'pending') for k,v in entry['gameplayValidation'].items()) if row['clips'] else 'Not processed'
    remaining='None within this normal-motion production scope; player approval pending' if entry['fullyComplete'] else row['missingArtwork']+' Remaining browser/gallery/release validation where not yet recorded.'
    if entry.get('externalBlocker'):remaining+=' BLOCKED: image_gen daily quota; six original stage/state sheets still required.'
    lines.append(f"| {entry['batch']} | {entry['name']} / `{entry['id']}` | {entry['category']} | [{entry['existingPath']}]({entry['existingPath']}) | {assets} | {validation} | {remaining} | {'Yes' if entry['fullyComplete'] else 'No'} |")
lines+=['','## Excluded acquisition holds','']
for entry in ledger['excluded']:lines.append('- `'+entry['id']+'`: '+entry.get('reason',entry.get('exclusionReason','Existing acquisition hold retained.')))
lines+=['','## Release state','',
        'Production is in progress. Interim DIST builds contain the sheets integrated at their build timestamp. After all batches, rebuild and verify DIST and both release archives against the final source; an interim build is not the completed all-livestock release.','']
(ROOT/'LIVESTOCK_16_FRAME_SPRITE_PRODUCTION_REPORT.md').write_text('\n'.join(lines),encoding='utf8')
(ROOT/'planning/sprite-production/production-ledger.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print(json.dumps({'sheets':len(clips),'authoredCells':len(clips)*16,'fullyComplete':len(complete),'remaining':len(ledger['eligible'])-len(complete)}))
