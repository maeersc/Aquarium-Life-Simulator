(async()=>{
  await AL.LifeStages.ready;
  const bank=AL.LifeStages,results=[];
  const check=(pass,name)=>results.push({pass:!!pass,name});
  check(bank.loaded===27&&!bank.errors.length,'All 27 stage sheets load offline');
  check(bank.records.filter(r=>r.category==='fish').length===18&&bank.records.filter(r=>r.category==='bottom_feeders').length===4&&bank.records.filter(r=>r.category==='corals').length===5,'Audited categories total 27 without double counting');
  check(bank.records.every(r=>!r.approved),'No artwork auto-approved');
  check(bank.stageFor({growth:0})==='baby'&&bank.stageFor({growth:.2999})==='baby'&&bank.stageFor({growth:.3})==='juvenile'&&bank.stageFor({growth:.9999})==='juvenile'&&bank.stageFor({growth:1})==='adult','Existing growth thresholds select the correct art');
  check(bank.frame('unknown')===null&&bank.frame('guppy','unknown')===null,'Missing art keys return a safe fallback');
  let renderCases=0;
  for(const meta of bank.records){
    const images=[],snapshots=[];let alphaOK=true,boundsOK=true,eyeOK=true,mirrorOK=true,transformOK=true;
    for(const stage of ['egg','baby','juvenile','adult'])for(const state of ['alive','dead']){
      const sprite=bank.frame(meta.id,stage,state);images.push(sprite);snapshots.push(sprite.toDataURL());
      const raw=sprite.getContext('2d').getImageData(0,0,192,160).data;let opaque=0;
      for(let i=3;i<raw.length;i+=4){if(raw[i])opaque++;if(raw[i]!==0&&raw[i]!==255)alphaOK=false;}
      boundsOK&&=opaque>20&&opaque<192*160*.9;
      const idx=meta.frames[stage][state],b=meta.bounds[idx];boundsOK&&=b[0]>=4&&b[1]>=4&&b[2]<=188&&b[3]<=156;
      if(meta.runtimeType==='fish'&&stage!=='egg')eyeOK&&=!!sprite.artMeta.eye;
      for(const width of [16,23,41,64,109]){
        const height=Math.round(width*160/192),raster=AL.SpriteKit.raster(sprite,width,height),eye=raster.eyeBounds;
        if(eye){
          eyeOK&&=eye.x>=0&&eye.y>=0&&eye.x+eye.w<=width&&eye.y+eye.h<=height;
          const pixels=raster.getContext('2d').getImageData(eye.x,eye.y,eye.w,eye.h).data;let colors=new Set(),opaqueEye=0;
          for(let i=0;i<pixels.length;i+=4)if(pixels[i+3]){opaqueEye++;colors.add(`${pixels[i]},${pixels[i+1]},${pixels[i+2]}`);}
          eyeOK&&=opaqueEye>=2&&colors.size>=2;
        }
        const canvases=[1,-1].map(direction=>{
          const c=document.createElement('canvas');c.width=256;c.height=192;const ctx=c.getContext('2d');ctx.globalAlpha=.83;const before=ctx.getTransform().toString();
          AL.SpriteKit.draw(ctx,sprite,128,96,width,height,direction,false);
          transformOK&&=ctx.globalAlpha===.83&&ctx.getTransform().toString()===before;
          renderCases++;return ctx.getImageData(0,0,256,192).data;
        });
        for(let y=0;y<192;y++)for(let x=0;x<256;x++)for(let channel=0;channel<4;channel++){
          const mirroredX=width%2?256-x:255-x;if(mirroredX<0||mirroredX>=256)continue;
          if(canvases[0][(y*256+x)*4+channel]!==canvases[1][(y*256+mirroredX)*4+channel])mirrorOK=false;
        }
      }
    }
    check(images.length===8&&new Set(snapshots).size===8,meta.id+': eight distinct authored images');
    check(alphaOK&&boundsOK,meta.id+': transparent assets, nonempty and uncropped');
    check(eyeOK,meta.id+': visible head-local eye detail at five raster sizes');
    check(mirrorOK&&transformOK,meta.id+': exact directional mirrors and restored canvas state');
  }
  return {results,renderCases};
})();
