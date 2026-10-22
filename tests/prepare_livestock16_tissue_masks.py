"""Rasterize manually specified technical tissue masks, never motion poses.

Input coordinates must be selected from inspected native proof images. Actual
native contact review and registration remain separate mandatory steps.
"""
import json
import math
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
def ellipse(x,y,rx,ry):
    return [[round(x+rx*math.cos(i*math.tau/32)),round(y+ry*math.sin(i*math.tau/32))] for i in range(32)]

for item in json.loads(Path(sys.argv[1]).read_text()):
    assert item['nativeFirstInspected'] is True and len(item['description'])>40
    polygons=list(item.get('polygons',[]));protected=list(item.get('protectedPolygons',[]))
    for shape in item.get('discs',[]):
        x,y,rx,*rest=shape;polygons.append(ellipse(x,y,rx,rest[0] if rest else rx))
    for x,y,rx,ry,ratio in item.get('rings',[]):
        polygons.append(ellipse(x,y,rx,ry));protected.append(ellipse(x,y,rx*ratio,ry*ratio))
    for shape in item.get('protectedDiscs',[]):
        x,y,rx,*rest=shape;protected.append(ellipse(x,y,rx,rest[0] if rest else rx))
    target=ROOT/'planning/sprite-production/packed'/item['id']/(item['stage']+'-'+item['state']+'-mutable-regions.json')
    target.parent.mkdir(parents=True,exist_ok=True)
    data={'agentInspected':True,'inspectionScope':'First native tissue geometry inspected; final all16-cell review still required before registration.','description':item['description'],'polygons':polygons,'protectedPolygons':protected}
    target.write_text(json.dumps(data,indent=2)+'\n')
    print(item['id'],item['stage'],item['state'])
