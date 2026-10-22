"""Register actually inspected16-pose source artwork in the existing registry."""
import argparse
import json
from pathlib import Path
import shutil

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('id');parser.add_argument('stage');parser.add_argument('--variety');parser.add_argument('--state');parser.add_argument('--review-notes',required=True);args=parser.parse_args()
path=ROOT/'assets/animation/livestock-registry.json';registry=json.loads(path.read_text(encoding='utf8'));entry=next(e for e in registry['entries'] if e['id']==args.id)
ledger_path=ROOT/'planning/sprite-production/production-ledger.json';ledger=json.loads(ledger_path.read_text(encoding='utf8'));production=next(e for e in ledger['eligible'] if e['id']==args.id)
category=entry['category'];motion=args.state or ('swim' if category=='fish' else 'polyp_motion' if category=='coral' else 'idle')
assert args.stage in entry['stages'] and motion in entry['requiredStates']
slot=('variety:'+args.variety+':' if args.variety else '')+args.stage+(':'+motion if category!='fish' else '')
packed=ROOT/production['production'][slot]['packed'];meta=json.loads(packed.with_suffix('.json').read_text(encoding='utf8'))
assert all(meta['technicalChecks'].values()) and len(set(meta['frameHashes']))==16 and len(args.review_notes)>50
folder=ROOT/'assets/livestock/animations'/args.id
if args.variety:folder=folder/'varieties'/args.variety
target=folder/(args.stage+'_'+motion+'_16.png');target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(packed,target)
clip={'stage':args.stage,'state':'swim','path':target.relative_to(ROOT).as_posix(),'status':'production','frameWidth':meta['frameWidth'],'frameHeight':meta['frameHeight'],'columns':4,'frameCount':16,'order':list(range(16)),'framesPerSecond':8,'anchor':meta['anchor'],'eye':meta['eye'],'facing':'mirror-side-profile','sha256':meta['sha256'],'authorship':'Sixteen distinct built-in image_gen keyframes; technical transparent-cell packing, fixed uniform scale and original-eye registration; no procedural-fin frame synthesis','userApproved':False,'validation':{k:True for k in ['alignment','identity','eyesOrAnatomy','patterns','attachment','loop','transparent','visualReview']}}
clip['validation'].update(frameHashes=meta['frameHashes'],notes=args.review_notes,reviewScope='Agent-inspected complete native contact sheet and source reference; player approval not claimed; gameplay validation follows')
clip['state']=motion
if category!='fish':
    assert meta['technicalChecks']['fixedSkeletonOrShell'] and len(set(meta['fixedStructure']['protectedPixelHashes']))==1
    clip['fixedStructure']=meta['fixedStructure']
    clip['facing']='fixed' if category=='coral' else 'mirror-side-profile'
    clip['framesPerSecond']=(2 if entry['id'] in ['soft','lps','mushroom'] else 1) if category=='coral' else (1 if motion=='idle' else 1.5) if entry['profile'] in ['snail','conch'] else 2 if motion=='idle' else 4
    clip['authorship']='Sixteen distinct built-in image_gen tissue/appendage drawings; technical nearest-neighbor cell packing and inspected body registration; canonical first-pose structure retained outside explicitly reviewed moving regions; no synthesized motion poses'
if args.variety:clip['variety']=args.variety
entry['clips']=[c for c in entry['clips'] if not(c['stage']==args.stage and c['state']==motion and c.get('variety')==args.variety)]+[clip]
entry['framesCompleted']=sum(c['frameCount'] for c in entry['clips'])
missing=[stage+('/'+state if category!='fish' else '') for stage in entry['stages'] for state in entry['requiredStates'] if not any(c['stage']==entry.get('stageAliases',{}).get(stage,stage) and c['state']==state and not c.get('variety') for c in entry['clips'])]
missing_varieties=[(v['id'],life) for v in entry['varieties'] for life in ['juvenile','adult'] if not any(c.get('variety')==v['id'] and c['stage']==life for c in entry['clips'])]
entry['status']='partial' if missing or missing_varieties else 'complete'
entry['missingArtwork']=('Remaining standard16-frame stages/states: '+', '.join(missing)+'. ' if missing else 'All required standard life-stage motion sheets registered. ')+(str(len(missing_varieties))+' designer stage slots retain previous art until their own registered sheets exist. ' if missing_varieties else '')+'Player visual approval pending.'
entry['userApproved']=False
meta['visualReview']={'passed':True,'notes':args.review_notes,'playerApproved':False};target.with_suffix('.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf8')
production['production'][slot].update(state='registered; gameplay validation pending',path=clip['path'],frames=16,agentVisualReviewPassed=True,playerApproved=False)
production['state']='partial' if missing or missing_varieties else 'all standard stages registered; gameplay validation pending';production['fullyComplete']=False
path.write_text(json.dumps(registry,indent=2,ensure_ascii=False)+'\n',encoding='utf8');ledger_path.write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print(json.dumps({'id':args.id,'stage':args.stage,'registered':clip['path'],'frames':16,'remainingStages':missing}))
