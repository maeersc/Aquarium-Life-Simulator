(() => {
  const results=[],issues=[],subjects=[...Object.keys(AL.Data.species),...AL.AssetBank.records.filter(r=>r.family==='fish').map(r=>r.id)];
  const get=(id,f,t)=>AL.Data.species[id]?AL.Art.sprite(id,f,t):AL.AssetBank.frame('fish',id,f,t);
  const check=(pass,name)=>{results.push({name,pass:!!pass});if(!pass)issues.push(name);};
  function pixels(c){return c.getContext('2d').getImageData(0,0,c.width,c.height).data;}
  for(const id of subjects){
    let visible=true,mirror=true,stable=true,bounds=true;
    for(const tone of [.8,1,1.2])for(const width of [16,22,33,59,109]){
      let canonicalEye=null;
      for(let frame=0;frame<4;frame++){
        const src=get(id,frame,tone),height=Math.round(width*src.height/src.width),base=AL.SpriteKit.raster(src,width,height),e=base.eyeBounds;
        if(!e){visible=false;continue;}const data=pixels(base),sample=[];let pupil=0;
        for(let y=e.y;y<e.y+e.h;y++)for(let x=e.x;x<e.x+e.w;x++){const i=(y*width+x)*4;sample.push(...data.slice(i,i+4));if(data[i+3]>0&&data[i]<80&&data[i+1]<90&&data[i+2]<115)pupil++;}
        visible&&=pupil>0;bounds&&=e.x>=0&&e.y>=0&&e.x+e.w<=width&&e.y+e.h<=height;
        const eye=sample.join(',');if(canonicalEye===null)canonicalEye=eye;else stable&&=canonicalEye===eye;
        for(const dead of [false,true])for(const face of [1,-1]){
          const c=document.createElement('canvas');c.width=width;c.height=height;const g=c.getContext('2d');
          AL.SpriteKit.draw(g,src,Math.floor(width/2),Math.floor(height/2),width,height,face,dead);
          const actual=pixels(c);for(let y=0;y<height;y++)for(let x=0;x<width;x++){const i=(y*width+x)*4,j=((dead?height-1-y:y)*width+(face<0?width-1-x:x))*4;for(let k=0;k<4;k++)if(actual[i+k]!==data[j+k])mirror=false;}
          const m=g.getTransform();bounds&&=m.a===1&&m.b===0&&m.c===0&&m.d===1&&m.e===0&&m.f===0&&g.globalAlpha===1&&g.globalCompositeOperation==='source-over';
        }
      }
    }
    check(visible,id+': pupil detail retained in every tested frame/size/tone');check(stable,id+': eye component identical across frames');check(mirror,id+': exact left/right and death-pose pixel transforms');check(bounds,id+': eye bounds and canvas transform isolation');
  }
  check(AL.SpriteKit.facing(-1,.00001)===-1&&AL.SpriteKit.facing(1,-.00001)===1&&AL.SpriteKit.facing(-1,.01)===1&&AL.SpriteKit.facing(1,-.01)===-1,'Facing threshold prevents jitter and follows meaningful movement');
  let s=AL.Core.newGame();s.settings.speed=1;const a=AL.Core.fish(s,'guppy'),b=AL.Core.fish(s,'guppy');a.x=.4;a.y=.4;b.x=.6;b.y=.6;a.heading=1;b.heading=-1;s.tanks[0].fish=[a,b];
  const c=document.createElement('canvas');c.width=960;c.height=480;const renderer=new AL.Renderer(c);renderer.draw(s,0);a.x=.5;b.x=.5;a.heading=-1;b.heading=1;const before=JSON.stringify(s);renderer.draw(s,.1);
  check(renderer.positions.get(a.id).facing===1&&renderer.positions.get(b.id).facing===-1,'Visible interpolation faces each fish movement, independently of prematurely reversed simulation headings');
  check(JSON.stringify(s)===before,'Rendering correction does not mutate authoritative saved fish state');
  a.x=renderer.positions.get(a.id).x-.0004;renderer.draw(s,.001);check(renderer.positions.get(a.id).facing===-1,'Slow interpolation uses meaningful target displacement instead of a frame-rate-dependent flip threshold');
  check(AL.AssetBank.loaded===13&&AL.AssetBank.errors.length===0,'All thirteen new asset families load');
  for(const r of AL.AssetBank.records){let clean=true,opaque=false;
    for(let i=0;i<r.frames;i++){const f=AL.AssetBank.frame(r.family,r.id,i),p=pixels(f);for(let j=3;j<p.length;j+=4){if(p[j]!==0&&p[j]!==255)clean=false;if(p[j]===255)opaque=true;}}
    check(clean&&opaque,r.id+': usable RGBA frames with binary transparent edges');
  }
  for(const id of ['zoa','mushroom','sps','lps','soft']){const pale=AL.AssetBank.coral(id,'bleached',0),dead=AL.AssetBank.coral(id,'dead',0);check(pale.toDataURL()!==dead.toDataURL(),id+': bleached and dead artwork are distinct');}
  const sps0=pixels(AL.AssetBank.coral('sps','healthy',0)),sps1=pixels(AL.AssetBank.coral('sps','healthy',1));let sameGeometry=true;for(let i=3;i<sps0.length;i+=4)if(sps0[i]!==sps1[i])sameGeometry=false;check(sameGeometry,'SPS highlight animation keeps rigid geometry unchanged');
  for(const id of ['fiji','caribbean','hawaiian']){const arch=AL.AssetBank.frame('rocks',id,3),y=id==='hawaiian'?120:140;check(arch.getContext('2d').getImageData(96,y,1,1).data[3]===0,id+': inspected arch opening is transparent');}
  const right=document.createElement('canvas'),left=document.createElement('canvas'),out=document.createElement('canvas');for(const c of [right,left,out]){c.width=33;c.height=21;}left.getContext('2d').fillStyle='#f4b860';left.getContext('2d').fillRect(2,3,5,4);right.leftSprite=left;AL.SpriteKit.draw(out.getContext('2d'),right,16,10,33,21,-1);check(out.toDataURL()===left.toDataURL(),'Optional authored left-side art is used without mirroring its asymmetry');
  for(const id of Object.keys(AL.Data.species)){
    const d=AL.Data.species[id],state=AL.Core.newGame(d.water);state.time=d.nocturnal?0:600;const t=state.tanks[0],f=AL.Core.fish(state,id);t.fish=[f];f.hunger=0;f.aiTimer=100;f.x=.5;f.y=.4;f.targetY=.4;f.vx=0;f.targetX=.8;AL.Sim.motion(state,t,.5);const rightMotion=f.x>.5&&f.vx>0;f.x=.5;f.vx=0;f.targetX=.2;AL.Sim.motion(state,t,.5);check(rightMotion&&f.x<.5&&f.vx<0,id+': actual movement supports both directions');
  }
  return {results,issues,subjects:subjects.length,renderCases:subjects.length*4*3*5*4,manualReview:'Pixel presence and registration checks do not establish perfect anatomical placement; inspect the contact sheets.'};
})()
