"use strict";
// Marine mounting geometry. Freshwater data and biology are intentionally untouched.
AL.Habitat=(()=>{
  const definitions={
    zoa:{allowed:['rock','sand','rack'],preferred:'rock',method:'stable plug or rock attachment',footprint:12,clearance:17,light:.45,flow:.3},
    mushroom:{allowed:['rock','sand','rack'],preferred:'rock',method:'attached rubble or stable plug',footprint:14,clearance:20,light:.3,flow:.2},
    sps:{allowed:['rock','rack'],preferred:'rock',method:'securely mounted branching frag',footprint:12,clearance:20,light:.8,flow:.7},
    lps:{allowed:['rock','sand','rack'],preferred:'sand',method:'stable skeletal base for this hammer colony',footprint:18,clearance:28,light:.55,flow:.4},
    soft:{allowed:['rock','sand','rack'],preferred:'rock',method:'attached hard base or stable plug',footprint:16,clearance:22,light:.4,flow:.35}
  };
  const rockProducts={fiji:{name:'Fiji reef rock',material:'porous reef limestone',price:90},caribbean:{name:'Caribbean reef rock',material:'porous reef limestone',price:95},hawaiian:{name:'Hawaiian rock',material:'volcanic-inspired game hardscape',price:85}};
  const sandProducts={fiji:{name:'Fiji sand',grain:'fine reef-sand visual',price:40,color:'#b2a58c'},caribbean:{name:'Caribbean sand',grain:'mixed pale grains',price:40,color:'#c0b398'},hawaiian:{name:'Hawaiian sand',grain:'dark volcanic-inspired grains',price:40,color:'#686c71'}};
  const clamp=(v,a,b)=>Math.max(a,Math.min(b,v)),bed=t=>(226-(t.substrate?.depth??2.4)*5)/240;
  const plane=(t,z=.5)=>bed(t)+(z-.5)*.06;
  function initialize(s,t){if(t.water!=='marine')return;
    if(!t.substrate)t.substrate={type:'fiji',depth:2.4};
    if(!t.hardscape)t.hardscape=[[89,217,77,'fiji',2],[52,219,48,'fiji',0],[391,217,97,'caribbean',3],[438,219,59,'hawaiian',1],[361,222,51,'hawaiian',0]].map(([x,y,width,group,variant])=>({id:AL.Core.id(s,'rock'),group,variant,x:x/480,y:y/240,width,baseOffset:y/240-bed(t)}));
    if(!t.mounts)t.mounts=[];for(const r of [...t.hardscape,...t.mounts])r.z??=.5;
  }
  function solid(rock,x,y){const m=AL.HabitatGeometry[rock.group]?.[rock.variant];if(!m)return false;
    const px=Math.floor((x*480-(rock.x*480-rock.width/2))/rock.width*192),py=(y*240-(rock.y*240-rock.width*184/192))/rock.width*192;
    return px>=0&&px<192&&m.columns[px].some(([a,b])=>py>=a&&py<b);
  }
  function candidates(t,x,y,type,size=1,z){const d=definitions[type];if(!d)return [];
    const found=[];
    if(d.allowed.includes('rock'))for(const r of t.hardscape||[]){
      if(z!==undefined&&Math.abs((r.z??.5)-z)>.051)continue;
      const px=Math.floor((x*480-(r.x*480-r.width/2))/r.width*192),m=AL.HabitatGeometry[r.group]?.[r.variant];if(px<0||px>=192||!m?.columns[px].length)continue;
      const top=m.columns[px][0][0],surface=(r.y*240-r.width*184/192+top/192*r.width)/240;
      if((y-surface)*240>1)continue;
      if(Math.abs(y-surface)*240>11)continue;
      if((t.hardscape||[]).some(other=>other!==r&&Math.abs((other.z??.5)-(r.z??.5))<=.051&&solid(other,x,surface-1/240)))continue;
      found.push({x,z:r.z??.5,y:surface,attachment:{surface:'rock',supportId:r.id,localX:(x-r.x)*480/r.width,localY:(surface-r.y)*240/r.width,orientation:'upright',mounted:true,footprint:d.footprint*size},distance:Math.abs(y-surface)*240});
    }
    if(d.allowed.includes('sand')&&t.substrate?.depth>0&&Math.abs(y-plane(t,z))*240<=11&&!t.hardscape?.some(r=>Math.abs((r.z??.5)-(z??.5))<=.051&&solid(r,x,plane(t,z)-1/240))){
      found.push({x,z:z??.5,y:plane(t,z),attachment:{surface:'sand',supportId:null,localX:x,localY:0,orientation:'upright',mounted:true,footprint:d.footprint*size},distance:Math.abs(y-plane(t,z))*240});
    }
    if(d.allowed.includes('rack'))for(const r of t.mounts||[]){if(z!==undefined&&Math.abs((r.z??.5)-z)>.051)continue;
      if(!r.mounted||!['back','left','right'].includes(r.glass))continue;
      if(Math.abs(x-r.x)*480<=r.width/2&&Math.abs(y-r.y)*240<=11&&!t.hardscape?.some(rock=>Math.abs((rock.z??.5)-(r.z??.5))<=.051&&solid(rock,x,r.y)))found.push({x,z:r.z??.5,y:r.y,attachment:{surface:'rack',supportId:r.id,localX:(x-r.x)*480/r.width,localY:0,orientation:'upright',mounted:true,footprint:d.footprint*size},distance:Math.abs(y-r.y)*240});
    }
    return found.sort((a,b)=>a.distance-b.distance||String(a.attachment.supportId).localeCompare(String(b.attachment.supportId)));
  }
  function placement(s,t,type,x,y,{size=1,ignoreId=null,z}={}){
    const d=definitions[type],reasons=[],warnings=[];
    if(!d||t.water!=='marine')return {ok:false,status:'Invalid',reasons:['Choose an implemented marine coral.'],warnings:[]};
    if(!Number.isFinite(x)||!Number.isFinite(y)||x<.05||x>.95||y<.15||y>.95)return {ok:false,status:'Invalid',reasons:['Keep the whole mounting footprint inside the aquarium.'],warnings:[]};
    const choices=candidates(t,x,y,type,size,z),choice=choices[0];
    if(!choice)return {ok:false,status:'Invalid',reasons:[t.hardscape?.some(r=>solid(r,x,y))?'The mounting point is inside solid rock.':'Unsupported open water at this depth. Match a suitable rock surface, stable sandbed base or mounted frag rack.'],warnings:[]};
    if(choice.x-d.footprint*size/960<.02||choice.x+d.footprint*size/960>.98)reasons.push('The mounting footprint crosses the glass boundary.');
    if(choice.x-50*size/960<.02||choice.x+50*size/960>.98||choice.y-48*size/240<.03)reasons.push('The coral silhouette would cross the aquarium boundary. Choose more clearance.');
    for(const f of t.flora.filter(f=>f.id!==ignoreId&&Math.abs((f.z??.5)-(choice.z??.5))<=.051&&!f.relocationRequired&&AL.Data.flora[f.type]?.water==='marine')){
      const dist=Math.hypot((choice.x-f.x)*480,(choice.y-(f.y??.92))*240),other=definitions[f.type];
      if(dist<(d.footprint*size+(other?.footprint||12)*f.size)/2)reasons.push('This footprint overlaps another colony.');
      else if(dist<Math.max(d.clearance,other?.clearance||0)&&('lps'===type||f.type==='lps'))warnings.push('Leave more clearance from stinging LPS tissue.');
    }
    const w=t.waterParams;if(!AL.Preparation.prepared(t)||t.bacteria<.65||t.bacteria2<.5||t.kind!=='reef')warnings.push('Use a prepared, cycled reef aquarium.');
    if(AL.Sim){const c=AL.Sim.floraConditions(s,t,{type,x:choice.x,y:choice.y,size,hp:100,id:ignoreId||'preview'});warnings.push(...c.issues);}
    if(w.ammonia>.15||w.nitrite>.15)warnings.push('Reduce toxic ammonia and nitrite before introducing coral.');
    return {ok:!reasons.length,status:reasons.length?'Invalid':warnings.length?'Conditional':'Suitable',reasons:[...new Set(reasons)],warnings:[...new Set(warnings)],position:{x:choice.x,y:choice.y,z:choice.z,attachment:choice.attachment},alternatives:choices.length};
  }
  function position(s,t,type,x,y,options){const r=placement(s,t,type,Number(x),Number(y),options);if(!r.ok)throw Error(r.reasons.join(' '));return r.position;}
  function validAttachment(t,f){const a=f.attachment;if(!a||a.orientation!=='upright'||a.mounted!==true||!definitions[f.type]?.allowed.includes(a.surface)||![a.localX,a.localY,a.footprint].every(Number.isFinite)||a.footprint<=0||a.footprint>64)return false;
    if(a.surface==='sand')return !a.supportId&&Math.abs(f.y-plane(t,f.z))<.00001&&!t.hardscape?.some(r=>Math.abs((r.z??.5)-(f.z??.5))<=.051&&solid(r,f.x,f.y-1/240));
    const objects=a.surface==='rock'?t.hardscape:t.mounts,r=objects?.find(r=>r.id===a.supportId);if(!r||Math.abs((f.z??.5)-(r.z??.5))>.051)return false;
    const x=r.x+a.localX*r.width/480,y=r.y+a.localY*r.width/240;
    if(Math.abs(x-f.x)>.00001||Math.abs(y-f.y)>.00001)return false;
    if(a.surface==='rack')return r.mounted&&Math.abs(a.localX)<=.5&&a.localY===0;
    return candidates(t,f.x,f.y,f.type,f.size,f.z).some(c=>c.attachment.supportId===a.supportId&&Math.abs(c.y-f.y)<.00001);
  }
  function migrate(s){let relocations=0;for(const t of s.tanks){if(t.water!=='marine')continue;initialize(s,t);
    for(const f of t.flora){if(f.relocationRequired)continue;
      if(f.attachment){
        if(f.y===undefined){const a=f.attachment,r=(a.surface==='rock'?t.hardscape:t.mounts)?.find(r=>r.id===a.supportId);f.y=a.surface==='sand'?bed(t):r&&Number.isFinite(a.localY)?r.y+a.localY*r.width/240:.92;}
        if(!validAttachment(t,f)){f.relocationRequired=true;relocations++;}continue;
      }
      const r=placement(s,t,f.type,f.x,f.y??.92,{size:f.size,ignoreId:f.id});
      if(r.ok&&r.alternatives===1)Object.assign(f,r.position);else{f.relocationRequired=true;relocations++;}
    }}return relocations;
  }
  function sync(t){for(const f of t.flora){const a=f.attachment;if(!a)continue;if(a.surface==='sand'){f.y=plane(t,f.z);continue;}const r=(a.surface==='rock'?t.hardscape:t.mounts)?.find(r=>r.id===a.supportId);if(r){f.z=r.z??.5;f.x=r.x+a.localX*r.width/480;f.y=r.y+a.localY*r.width/240;}else f.relocationRequired=true;}}
  const initialStock={'rack:frag':8};for(const id of Object.keys(sandProducts))initialStock['sand:'+id]=30;for(const id of Object.keys(rockProducts))for(let v=0;v<4;v++)initialStock['rock:'+id+':'+v]=6;
  return {definitions,rockProducts,sandProducts,initialStock,bed,plane,initialize,solid,candidates,placement,position,validAttachment,migrate,sync};
})();
