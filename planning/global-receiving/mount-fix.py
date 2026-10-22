from pathlib import Path
r=Path(__file__).resolve().parents[2]
p=r/'js/diving-receiving.js';s=p.read_text(encoding='utf8');a=s.index(' function mountCandidates(');b=s.index(' function destinations(',a)
s=s[:a]+''' function mountCandidates(t,id){const entry=resolve(id);if(entry?.kind!=='coral')return [null];const points=[],seen=new Set(),add=p=>{const key=[p.x,p.y,p.z].map(n=>Number(n).toFixed(8)).join(':');if(!seen.has(key)){seen.add(key);points.push(p);}};
  for(const support of [...(t.mounts||[]),...(t.hardscape||[])])for(const offset of [0,-.035,.035])add({x:K.clamp(support.x+offset,.05,.95),y:support.y-.015,z:support.z??.5});
  // A rock's anchor is not its top surface. Sample its existing collision
  // geometry, then let Habitat.placement enforce support and clearance.
  if(AL.Habitat.definitions[id]?.allowed.includes('rock'))for(const rock of t.hardscape||[]){const geometry=AL.HabitatGeometry[rock.group]?.[rock.variant];if(!geometry)continue;for(let px=16;px<177;px+=16){const spans=geometry.columns[px];if(!spans?.length)continue;add({x:rock.x-rock.width/960+(px+.5)/192*rock.width/480,y:(rock.y*240-rock.width*184/192+spans[0][0]/192*rock.width)/240,z:rock.z??.5});}}
  if(AL.Habitat.definitions[id]?.allowed.includes('sand'))for(const x of [.2,.4,.6,.8])add({x,y:AL.Habitat.plane(t,.5),z:.5});return points;
 }
''' +s[b:];p.write_text(s,encoding='utf8')
p=r/'js/diving-mystery.js';s=p.read_text(encoding='utf8');a="status:'pending',item:copy(item),arrivalTime";b="status:'pending',item:copy({...item,collected:true}),arrivalTime";assert a in s;p.write_text(s.replace(a,b,1),encoding='utf8')
