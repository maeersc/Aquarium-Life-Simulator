"use strict";
(async()=>{
  const $=id=>document.getElementById(id),bank=AL.AssetBank,D=AL.Data,key='aquarium-life-art-review-v11';
  const diagnostic=window.ART_REVIEW={ready:false,framesDrawn:0,errors:[],runtimeSpeciesCount:Object.keys(D.species).length};
  await Promise.all([AL.Art.ready,bank.ready]);
  let saved={};try{saved=JSON.parse(localStorage.getItem(key)||'{}')||{};}catch{}
  const defaults={fiji:{x:.25,y:.88,variant:2},caribbean:{x:.52,y:.88,variant:3},hawaiian:{x:.78,y:.88,variant:1}},layout={};
  for(const [id,v]of Object.entries(defaults)){const s=saved.layout?.[id];layout[id]=s&&Number.isFinite(s.x)&&Number.isFinite(s.y)&&Number.isInteger(s.variant)&&s.variant>=0&&s.variant<4?{x:AL.Core.clamp(s.x,.12,.88),y:AL.Core.clamp(s.y,.6,.94),variant:s.variant}:{...v};}
  const reviews=saved.reviews&&typeof saved.reviews==='object'?saved.reviews:{};
  let category=['fish','corals','rocks'].includes(saved.category)?saved.category:'fish',selected='clown',state='healthy',mode='swim',backdrop='dark',frame=0,elapsed=0,playing=!matchMedia('(prefers-reduced-motion: reduce)').matches,placing=false,previous=0,budget=0,direction=1,lastX=480;
  const fixture=AL.Core.newGame('marine');fixture.time=600;fixture.settings.speed=0;fixture.settings.particles=false;fixture.tanks[0].prepared=true;
  const renderer=new AL.Renderer($('tank-preview')),overlay=document.createElement('canvas');overlay.width=960;overlay.height=480;
  const priority=['clown',...bank.records.filter(r=>r.family==='fish').map(r=>r.id)];
  function subjects(){return category==='fish'?[...priority,...Object.keys(D.species).filter(id=>id!=='clown')]:bank.records.filter(r=>r.family===category).map(r=>r.id);}
  function meta(){return category==='fish'&&D.species[selected]?{name:D.species[selected].name,scientificName:D.species[selected].scientificName||'Scientific name not defined',status:selected==='clown'?'Approved':'Needs Improvement',frames:4}:bank.metadata(category,selected);}
  function status(){const r=reviews[category+':'+selected];return ['Not Started','Needs Improvement','Ready for Review','Approved'].includes(r?.status)?r.status:meta()?.status||'Needs Improvement';}
  function source(index=frame,visualState=state){if(category==='fish')return D.species[selected]?AL.Art.sprite(selected,index,1):bank.frame('fish',selected,index);if(category==='corals')return bank.coral(selected,visualState,index);return bank.frame('rocks',selected,Number(visualState));}
  function persist(){try{localStorage.setItem(key,JSON.stringify({reviews,layout,category}));return true;}catch{return false;}}
  function study(label,index,visualState){const a=document.createElement('article');a.className='art-study';const c=document.createElement('canvas');c.width=300;c.height=240;a.append(c);const p=document.createElement('p');p.textContent=label;a.append(p);$('art-studies').append(a);a.draw={canvas:c,index,visualState};}
  function paint(canvas,src,face=1,eyes=false){
    const ctx=canvas.getContext('2d');ctx.clearRect(0,0,canvas.width,canvas.height);if(!src)return;
    if(category==='fish'){
      const w=Math.round(canvas.width*.82),h=Math.round(w*src.height/src.width),r=AL.SpriteKit.draw(ctx,src,canvas.width/2,canvas.height/2,w,h,face,mode==='death');
      if(eyes&&r.eyeBounds){const e=r.eyeBounds,ox=canvas.width/2-Math.floor(w/2),oy=canvas.height/2-Math.floor(h/2),x=face===1?ox+e.x:ox+w-e.x-e.w,y=mode==='death'?oy+h-e.y-e.h:oy+e.y;ctx.strokeStyle='#f4b860';ctx.lineWidth=2;ctx.strokeRect(x-2,y-2,e.w+4,e.h+4);}
    }else{const size=Math.min(canvas.width*.85,canvas.height*.85);ctx.imageSmoothingEnabled=false;ctx.drawImage(src,(canvas.width-size)/2,(canvas.height-size)/2,size,size);}
  }
  function render(){
    const src=source();paint($('right-preview'),src,1,$('show-eyes').checked);paint($('left-preview'),category==='corals'?source(frame,'bleached'):category==='rocks'?source(0,'3'):src,-1,$('show-eyes').checked);
    const native=$('native-preview');if(src){native.width=src.width;native.height=src.height;native.getContext('2d').drawImage(src,0,0);}
    for(const a of $('art-studies').children)paint(a.draw.canvas,source(a.draw.index,a.draw.visualState));
    const zoom=Number($('camera-select').value);renderer.zoom=zoom;fixture.tanks[0].lightMode=backdrop==='dark'?'off':'on';renderer.draw(fixture,0);
    const ctx=overlay.getContext('2d');ctx.clearRect(0,0,960,480);
    if(category==='fish'&&src){
      const d=D.species[selected],scale=d?Math.max(.35,Math.min(1.7,.6+d.size/28)):1.3,w=Math.round(64*scale*2*zoom),h=Math.round(w*src.height/src.width),x=mode==='turn'?480+Math.sin(elapsed*.9)*170:480;
      direction=AL.SpriteKit.facing(direction,x-lastX,.25);lastX=x;AL.SpriteKit.draw(ctx,src,x,210,w,h,mode==='turn'?direction:1,mode==='death');
      $('scale-note').textContent=`${d?'Current gameplay':'Art-only display'} scale: ${Math.round(w/2/zoom)} scene-pixel canvas width at 1x. Turning follows visible horizontal movement.`;
    }else if(category==='corals'&&src){const size=100*zoom;ctx.imageSmoothingEnabled=false;ctx.drawImage(src,480-size/2,410-size*.96,size,size);$('scale-note').textContent='50 scene-pixel colony width at 1x. Pale living tissue and dead remains are distinct art studies.';
    }else if(category==='rocks'){
      for(const [id,p]of Object.entries(layout)){const x=((p.x-.5)*zoom+.5)*960,y=((p.y-.5)*zoom+.5)*480,width=[75,115,170,145][p.variant]*zoom;bank.drawObject(ctx,'rocks',id,p.variant,x,y,width);if(id===selected){ctx.save();ctx.strokeStyle='#45d6d0';ctx.setLineDash([5,4]);ctx.strokeRect(x-width/2,y-width*.93,width,width*.95);ctx.restore();}}
      $('scale-note').textContent=placing?'Click to position the selected rock. Escape cancels.':'The selected rock has a separate outline. Preview placement survives gallery reload.';
    }
    if(backdrop==='dark'){ctx.globalCompositeOperation='source-atop';ctx.fillStyle='rgba(3,13,25,.4)';ctx.fillRect(0,0,960,480);ctx.globalCompositeOperation='source-over';}
    $('tank-preview').getContext('2d').drawImage(overlay,0,0);
    $('frame-label').textContent=category==='rocks'?'Static rock artwork':`Frame ${frame+1} / ${category==='fish'?4:2}`;
    $('eye-report').textContent=category==='fish'?'Eyes use head-local anchors and a consistent canonical eye component across frames. Eye overlays aid inspection; pixel checks alone do not establish anatomical accuracy.':'Bottom anchors and transparent margins are consistent across these views. Inspect against both backgrounds.';
    Object.assign(diagnostic,{framesDrawn:diagnostic.framesDrawn+1,category,selected,frame,direction,placing,layout:JSON.parse(JSON.stringify(layout)),loadedAssets:bank.loaded});
  }
  function update(loadReview=false){
    const m=meta();$('specimen-name').textContent=m?.name||selected;$('classification').textContent=category.toUpperCase()+' / '+(D.species[selected]?'IMPLEMENTED':'ART REVIEW');
    $('asset-details').textContent=category==='fish'?(m.scientificName+' · '+(D.species[selected]?'Existing gameplay species':'ART ONLY — not a store species')):category==='rocks'?(m.name+' · material is an art product definition; no new chemistry'):'Five visual states, independently selectable for review.';
    $('review-badge').textContent=status();if(loadReview){const r=reviews[category+':'+selected];$('status-select').value=status();$('review-notes').value=r?.notes||'';$('review-message').textContent='';}
    $('right-title').textContent=category==='fish'?'Right-facing':category==='corals'?'Selected coral state':'Selected rock';$('left-title').textContent=category==='fish'?'Left-facing':category==='corals'?'Bleached · still living':'Cave / arch';
    $('motion-select').disabled=category==='rocks';$('show-eyes').disabled=category!=='fish';$('state-select').disabled=category==='fish';$('rock-tools').hidden=category!=='rocks';
    $('motion-note').textContent=category==='fish'?(mode==='turn'?'Stable mirrored side profiles face the displayed movement. Authored perspective-turn frames remain unfinished.':mode==='idle'?'Four swim poses at a slower cadence, with stable head-local eye detail.':mode==='death'?'Frozen inverted frame-zero pose; eyes transform with the head.':'Four-frame swim study. Eyes retain the same registered component; small body/pattern differences remain for art review.'):category==='corals'?'Healthy, stressed, bleached, tissue-loss and dead states are separate. SPS keeps a rigid silhouette; soft tissue uses subtle two-pose flow studies.':'Small, medium, large and cave variants share consistent pixel density. Outer margins and arch openings are transparent.';
    $('play-toggle').textContent=playing?'Pause animation':'Play animation';$('play-toggle').setAttribute('aria-pressed',String(playing));$('step-frame').disabled=category==='rocks'||mode==='death';
    $('studies-title').textContent=category==='fish'?'Every swim frame':category==='corals'?'Living tissue and remains':'Size and cave variations';$('art-studies').replaceChildren();
    if(category==='fish')for(let i=0;i<4;i++)study('Swim frame '+(i+1),i,state);else if(category==='corals')for(const s of ['healthy','stressed','bleached','tissue-loss','dead'])study(s.replace('-',' '),frame,s);else for(let i=0;i<4;i++)study(['Small','Medium','Large','Cave / arch'][i],0,String(i));
    $('native-note').textContent='Native pixels without smoothing. Original generated sources, previous artwork and exact prompts are preserved.';
    document.querySelectorAll('.stage').forEach(e=>e.className='stage '+backdrop);document.querySelectorAll('[data-category]').forEach(b=>{b.classList.toggle('active',b.dataset.category===category);b.setAttribute('aria-pressed',String(b.dataset.category===category));});render();
  }
  function selectCategory(next){category=next;selected=category==='fish'?'clown':category==='corals'?'zoa':'fiji';state=category==='rocks'?'2':'healthy';frame=0;elapsed=0;placing=false;
    $('subject-select').replaceChildren(...subjects().map(id=>{const o=document.createElement('option');o.value=id;o.textContent=category==='fish'&&D.species[id]?D.species[id].name:bank.metadata(category,id).name;return o;}));$('subject-select').value=selected;
    $('state-select').replaceChildren(...(category==='rocks'?['Small','Medium','Large','Cave / arch']:['Healthy','Stressed','Bleached','Tissue loss','Dead']).map((label,i)=>{const o=document.createElement('option');o.value=category==='rocks'?String(i):['healthy','stressed','bleached','tissue-loss','dead'][i];o.textContent=label;return o;}));$('state-select').value=state;update(true);}
  document.querySelectorAll('[data-category]').forEach(b=>b.onclick=()=>selectCategory(b.dataset.category));
  $('subject-select').onchange=e=>{selected=e.target.value;frame=0;elapsed=0;if(category==='rocks'){state=String(layout[selected].variant);$('state-select').value=state;}update(true);};
  $('state-select').onchange=e=>{state=e.target.value;if(category==='rocks'){layout[selected].variant=Number(state);persist();}update();};
  $('motion-select').onchange=e=>{mode=e.target.value;frame=0;elapsed=0;direction=1;lastX=480;update();};$('background-select').onchange=e=>{backdrop=e.target.value;update();};$('camera-select').onchange=render;$('show-eyes').onchange=render;
  $('play-toggle').onclick=()=>{playing=!playing;update();};$('step-frame').onclick=()=>{playing=false;frame=(frame+1)%(category==='fish'?4:2);update();};
  $('save-review').onclick=()=>{reviews[category+':'+selected]={status:$('status-select').value,notes:$('review-notes').value.slice(0,2000),recordedBy:'user'};$('review-badge').textContent=status();$('review-message').textContent=persist()?'Your review is saved locally.':'Storage is unavailable; copy your feedback before leaving.';};
  $('place-rock').onclick=()=>{placing=true;$('tank-preview').focus();render();};$('tank-preview').onclick=e=>{if(!placing)return;const r=e.target.getBoundingClientRect(),p=renderer.worldPoint((e.clientX-r.left)/r.width,(e.clientY-r.top)/r.height);layout[selected]={x:AL.Core.clamp(p.x,.12,.88),y:AL.Core.clamp(p.y,.6,.94),variant:Number(state)};placing=false;persist();render();};
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&placing){placing=false;render();}});$('reset-layout').onclick=()=>{for(const id of Object.keys(layout))layout[id]={...defaults[id]};persist();render();};
  if(bank.errors.length)diagnostic.errors.push(...bank.errors);
  selectCategory(category);diagnostic.ready=true;diagnostic.priorityFish=priority;
  function tick(now){const dt=previous?Math.min(.1,(now-previous)/1000):0;previous=now;if(!document.hidden&&playing&&mode!=='death'&&category!=='rocks'){elapsed+=dt;budget+=dt;if(budget>=1/30){budget=0;frame=Math.floor(elapsed*(category==='fish'?(mode==='idle'?3:6):.8))%(category==='fish'?4:2);render();}}requestAnimationFrame(tick);}
  requestAnimationFrame(tick);
})();
