"use strict";
(async()=>{
  await AL.LifeStages.ready;
  const $=id=>document.getElementById(id),bank=AL.LifeStages,storageKey='aquarium-life-stage-reviews-v1';
  let category='fish',id='guppy',selectedStage='adult',selectedState='alive',reviews={},clock=0,last=0;
  try{const v=JSON.parse(localStorage.getItem(storageKey)||'{}');if(v&&typeof v==='object'&&!Array.isArray(v))reviews=v;}catch{}
  const api=window.LIFE_REVIEW={ready:true,errors:bank.errors,loaded:bank.loaded,category,id,selectedStage,selectedState,draws:0};
  function draw(canvas,stage,state,width,height,direction=Number($('direction').value),x=canvas.width/2,y=canvas.height/2){
    const ctx=canvas.getContext('2d');ctx.clearRect(0,0,canvas.width,canvas.height);ctx.imageSmoothingEnabled=false;
    const source=bank.frame(id,stage,state);if(!source)return;
    AL.SpriteKit.draw(ctx,source,x,y,width,height,category==='corals'?1:direction,false);
    if($('eyes').checked&&source.artMeta.eye){
      const raster=AL.SpriteKit.raster(source,width,height),e=raster.eyeBounds;
      if(e){ctx.save();ctx.translate(Math.round(x),Math.round(y));ctx.scale(direction,1);ctx.strokeStyle='#f6d389';ctx.lineWidth=1;ctx.strokeRect(-Math.floor(width/2)+e.x-1,-Math.floor(height/2)+e.y-1,e.w+2,e.h+2);ctx.restore();}
    }
  }
  function detail(time=0){
    const canvas=$('detail'),moving=$('swim').checked&&selectedStage!=='egg'&&selectedState==='alive'&&category!=='corals',scale=Number($('zoom').value);
    const travel=Math.max(0,Math.min(145,(canvas.width-192*scale)/2-12));
    const x=moving?canvas.width/2+Math.sin(time*.8)*travel:canvas.width/2,direction=moving?(Math.cos(time*.8)>=0?1:-1):Number($('direction').value);
    draw(canvas,selectedStage,selectedState,192*scale,160*scale,direction,x,canvas.height/2);
    $('detail-title').textContent=selectedStage[0].toUpperCase()+selectedStage.slice(1)+' · '+(selectedState==='alive'?'Alive':'Dead / nonviable');
    api.selectedStage=selectedStage;api.selectedState=selectedState;api.draws++;
  }
  function paint(){
    document.body.className=$('backdrop').value;
    document.querySelectorAll('.pose').forEach(button=>{
      const stage=button.dataset.stage,state=button.dataset.state;
      button.classList.toggle('selected',stage===selectedStage&&state===selectedState);
      draw(button.querySelector('.plate'),stage,state,288,240);
      const size=bank.size(id,stage);draw(button.querySelector('.scale'),stage,state,size.width*2,size.height*2);
    });detail(clock);
  }
  function resident(){
    id=$('species').value;api.id=id;
    const meta=bank.metadata(id);if(!meta)return;
    $('name').textContent=meta.name;$('category').textContent=category.replace('_',' ')+' / '+id;
    $('scientific').textContent=meta.scientificName|| (meta.fictional?'Fictional species':'Scientific species not specified in current game data');
    $('notes').textContent=meta.earlyEquivalent+'. '+(category==='corals'?'Egg → settled starter → juvenile colony → mature colony. Early coral stages are preview-only; healthy/dead adult states already exist in the aquarium.':'Distinct stage poses use the existing fry, juvenile and adult growth thresholds. Dead poses are authored and remain static.')+(id==='clown'?' The approved adult swim animation is preserved in gameplay; this adult plate is an unapproved stage study.':'');
    $('direction').disabled=category==='corals';
    const review=reviews[id]||{};$('review-status').value=['Ready for Review','Needs Improvement','Approved'].includes(review.status)?review.status:'Ready for Review';$('review-notes').value=typeof review.notes==='string'?review.notes:'';$('saved').textContent='';
    $('stages').replaceChildren();
    for(const stage of ['egg','baby','juvenile','adult']){
      const column=document.createElement('article');column.className='stage-column';
      const title=document.createElement('h3');title.textContent=stage[0].toUpperCase()+stage.slice(1);const small=document.createElement('small');small.textContent='2 states';title.append(small);column.append(title);
      for(const state of ['alive','dead']){
        const button=document.createElement('button');button.className='pose '+state;button.dataset.stage=stage;button.dataset.state=state;button.setAttribute('aria-label',`${meta.name}, ${stage}, ${state}`);
        const heading=document.createElement('span');heading.className='pose-heading';heading.textContent=state==='alive'?(stage==='egg'?'Viable / living':'Alive'):(stage==='egg'?'Nonviable':'Dead');button.append(heading);
        const plate=document.createElement('canvas');plate.className='plate';plate.width=384;plate.height=280;button.append(plate);
        const actual=document.createElement('canvas');actual.className='scale';actual.width=320;actual.height=120;button.append(actual);
        const caption=document.createElement('span');caption.className='scale-caption';caption.textContent=stage==='egg'?'Brood icon scale · 2× scene pixels':category==='corals'&&stage!=='adult'?'Future stage scale reference · 2×':'Gameplay scale reference · 2× scene pixels';button.append(caption);
        button.onclick=()=>{selectedStage=stage;selectedState=state;paint();};column.append(button);
      }$('stages').append(column);
    }paint();
  }
  function chooseCategory(value){
    category=value;api.category=value;document.querySelectorAll('[data-category]').forEach(b=>b.classList.toggle('active',b.dataset.category===value));
    $('species').replaceChildren(...bank.records.filter(r=>r.category===value).map(r=>new Option(r.name,r.id)));resident();
  }
  document.querySelectorAll('[data-category]').forEach(b=>b.onclick=()=>chooseCategory(b.dataset.category));
  $('species').onchange=resident;for(const key of ['direction','backdrop','zoom','eyes','swim'])$(key).onchange=paint;
  $('review-form').onsubmit=e=>{e.preventDefault();reviews[id]={status:$('review-status').value,notes:$('review-notes').value.slice(0,4000)};try{localStorage.setItem(storageKey,JSON.stringify(reviews));$('saved').textContent='Review saved on this device.';}catch{$('saved').textContent='Storage unavailable. Copy your notes before leaving.';}};
  $('load-status').textContent=bank.errors.length?'Some artwork failed to load: '+bank.errors.join(', '):`${bank.loaded} local sheets loaded · ${bank.loaded*8} stage/state images`;
  chooseCategory('fish');
  function animate(now){if(last)clock+=Math.min(.1,(now-last)/1000);last=now;if($('swim').checked&&!document.hidden)detail(clock);requestAnimationFrame(animate);}requestAnimationFrame(animate);
})();
