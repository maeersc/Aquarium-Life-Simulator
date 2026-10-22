"""Import an original built-in image_gen drawing into the development ledger."""
import argparse
import json
from pathlib import Path
import re
import shutil
from pack_livestock16_production import pack,pack_resident

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('id');parser.add_argument('stage');parser.add_argument('source');parser.add_argument('--revision',type=int,default=1);parser.add_argument('--variety');parser.add_argument('--state');args=parser.parse_args()
ledger_path=ROOT/'planning/sprite-production/production-ledger.json'
ledger=json.loads(ledger_path.read_text(encoding='utf8'));entry=next(e for e in ledger['eligible'] if e['id']==args.id)
assert re.fullmatch('[a-z0-9-]+',args.id) and args.stage in entry['stages']
if args.variety:assert args.variety in [v['id'] for v in entry['varieties']]
category=entry['category'];motion=args.state or ('swim' if category=='fish' else 'polyp_motion' if category=='coral' else 'idle')
assert motion in {'fish':['swim'],'coral':['polyp_motion'],'invertebrate':['idle','walk']}[category]
art_id=args.variety or args.id;slot=('variety:'+args.variety+':' if args.variety else '')+args.stage+(':'+motion if category!='fish' else '')
source=Path(args.source).resolve();assert source.is_file() and source.suffix.lower()=='.png'
raw=ROOT/'planning/sprite-production/raw'/art_id/(args.stage+('-'+motion if category!='fish' else '')+'-source-v'+str(args.revision)+'.png');raw.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,raw)
destination=ROOT/'planning/sprite-production/packed'/art_id/(args.stage+'_'+motion+'_16.png')
try:
    data=pack(raw,destination) if category=='fish' else pack_resident(raw,destination,category,args.stage,motion)
    entry['production'][slot]={'stage':args.stage,'variety':args.variety,'state':'packed; visual review pending','source':raw.relative_to(ROOT).as_posix(),'packed':destination.relative_to(ROOT).as_posix(),'metadata':destination.with_suffix('.json').relative_to(ROOT).as_posix()}
    entry['state']='in production'
    print(json.dumps({'id':args.id,'stage':args.stage,'frames':16,'packed':str(destination.relative_to(ROOT))}))
except Exception as error:
    entry['production'][slot]={'stage':args.stage,'variety':args.variety,'state':'packing failed; correction required','source':raw.relative_to(ROOT).as_posix(),'error':str(error)}
    print(json.dumps({'id':args.id,'stage':args.stage,'error':str(error)}))
ledger_path.write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
