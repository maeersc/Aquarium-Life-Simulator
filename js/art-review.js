"use strict";
(() => {
  const $=id=>document.getElementById(id), D=AL.Data, metadata=window.ART_BENCHMARK;
  const reviewKey='aquarium-life-art-review-v1';
  const statuses=['Not Started','Needs Improvement','Ready for Review','Approved'];
  const images=new Map(), boundsCache=new Map();
  let reviews={}, species='clown', resolution=128, mode='swim', background='dark';
  let playing=!matchMedia('(prefers-reduced-motion: reduce)').matches, elapsed=0, frame=0, previous=0, budget=0;
  const diagnostic=window.ART_REVIEW={ready:false,framesDrawn:0,frame:0,loadedAtlases:0,gameplayWrites:0,errors:[],speciesCount:Object.keys(D.species).length};
  try { reviews=JSON.parse(localStorage.getItem(reviewKey)||'{}'); if(!reviews||typeof reviews!=='object'||Array.isArray(reviews))reviews={}; } catch { reviews={}; }
  const fixture=AL.Core.newGame('marine');
  fixture.time=600;fixture.settings.speed=0;fixture.settings.particles=false;fixture.tanks[0].prepared=true;
  const renderer=new AL.Renderer($('tank-preview'));
  const layer=document.createElement('canvas');layer.width=960;layer.height=480;
  const subject=()=>D.species[species];
  const reviewStatus=()=>statuses.includes(reviews[species]?.status)?reviews[species].status:species==='clown'?metadata.status:'Needs Improvement';

  function bounds(canvas,key){
    if(boundsCache.has(key))return boundsCache.get(key);
    const {width:w,height:h}=canvas,pixels=canvas.getContext('2d').getImageData(0,0,w,h).data;
    let left=w,top=h,right=0,bottom=0;
    for(let y=0;y<h;y++)for(let x=0;x<w;x++)if(pixels[(y*w+x)*4+3]){left=Math.min(left,x);top=Math.min(top,y);right=Math.max(right,x+1);bottom=Math.max(bottom,y+1);}
    const box={x:left,y:top,w:right-left,h:bottom-top};boundsCache.set(key,box);return box;
  }
  function current(f=frame){const image=AL.Art.legacySprite(species,f,1);return {image,box:bounds(image,species+':'+f)};}
  function proposed(size=resolution,f=frame){
    const image=images.get(size);if(species!=='clown'||!image)return null;
    const [x,y,right,bottom]=metadata.atlases[size].bounds[f];
    return {image,box:{x:x+f*size,y,w:right-x,h:bottom-y}};
  }
  function drawFish(ctx,asset,cx,cy,width,pose=true){
    if(!asset)return;const {image,box}=asset,height=width*box.h/box.w;
    ctx.save();ctx.imageSmoothingEnabled=false;ctx.translate(Math.round(cx),Math.round(cy));
    if(pose&&mode==='turn'&&Math.floor(elapsed/2)%2)ctx.scale(-1,1);
    if(pose&&mode==='death')ctx.scale(1,-1);
    ctx.drawImage(image,box.x,box.y,box.w,box.h,-Math.round(width/2),-Math.round(height/2),Math.round(width),Math.round(height));ctx.restore();
  }
  function blank(canvas,message){const c=canvas.getContext('2d');c.clearRect(0,0,canvas.width,canvas.height);c.fillStyle='#d1e0eb';c.textAlign='center';c.font='18px Segoe UI';c.fillText(message,canvas.width/2,canvas.height/2);}
  function render(){
    const old=current(),fresh=proposed();
    for(const [id,asset]of [['current-preview',old],['proposed-preview',fresh]]){
      const canvas=$(id),ctx=canvas.getContext('2d');ctx.clearRect(0,0,canvas.width,canvas.height);
      if(asset)drawFish(ctx,asset,256,160,336);else blank(canvas,species==='clown'?'Artwork unavailable':'Replacement not started');
    }
    const native=$('native-preview'),nc=native.getContext('2d');nc.clearRect(0,0,native.width,native.height);nc.imageSmoothingEnabled=false;
    if(fresh)nc.drawImage(fresh.image,frame*resolution,0,resolution,resolution,0,0,resolution,resolution);
    else blank(native,'Not started');
    for(const size of [96,128,192,256]){const c=$('study-'+size),ctx=c.getContext('2d');ctx.clearRect(0,0,c.width,c.height);const art=proposed(size);if(art)drawFish(ctx,art,128,96,176);else blank(c,'Not started');}
    const camera=Number($('camera-select').value);renderer.zoom=camera;
    fixture.tanks[0].lightMode=background==='dark'?'off':'on';
    renderer.draw(fixture,0);
    const ctx=layer.getContext('2d');ctx.clearRect(0,0,960,480);
    const scale=Math.max(.35,Math.min(1.7,.6+subject().size/28));
    const allocation=Math.round(64*scale),inkWidth=old.box.w*allocation/64;
    drawFish(ctx,old,280,225,inkWidth*2*camera);drawFish(ctx,fresh,680,225,inkWidth*2*camera);
    if(background==='dark'){ctx.globalCompositeOperation='source-atop';ctx.fillStyle='rgba(3,13,25,.4)';ctx.fillRect(0,0,960,480);ctx.globalCompositeOperation='source-over';}
    const tankCtx=$('tank-preview').getContext('2d');tankCtx.drawImage(layer,0,0);tankCtx.fillStyle='#f3f7fc';tankCtx.textAlign='center';tankCtx.font='16px Segoe UI';tankCtx.fillText('CURRENT',280,330);tankCtx.fillText(fresh?'PROPOSED · NOT APPROVED':'PROPOSAL NOT STARTED',680,330);
    $('scale-note').textContent=`Neutral adult at ${camera}× camera: ${allocation} × ${Math.round(40*scale)} scene-pixel sprite allocation at 1×. Both fish use the current sprite’s ${inkWidth.toFixed(1)}-pixel visible width × camera scale. Tank source: 480 × 240; display shrinks responsively.`;
    $('frame-label').textContent=`Frame ${frame+1} / 4${mode==='death'?' · frozen':''}`;
    diagnostic.framesDrawn++;diagnostic.frame=frame;diagnostic.species=species;diagnostic.resolution=resolution;diagnostic.status=reviewStatus();
  }
  function update(loadReview=false){
    const d=subject();
    $('specimen-name').textContent=d.name;
    $('species-classification').textContent=`${d.water==='marine'?'SALTWATER':'FRESHWATER'} / ${d.fictional?'FICTIONAL / ':''}ID: ${species}`;
    $('review-badge').textContent=reviewStatus();
    if(loadReview){$('status-select').value=reviewStatus();$('review-notes').value=typeof reviews[species]?.notes==='string'?reviews[species].notes:'';$('review-message').textContent='';}
    $('asset-details').textContent=species==='clown'?'Amphiprion ocellaris ? gameplay ID: clown. This artwork is now assigned to Ocellaris clownfish in the aquarium, store and inspector.':'Scientific name not defined in the current database. Existing procedural artwork shown; replacement awaits the approved clownfish standard.';
    $('proposal-caption').textContent=species==='clown'?`${resolution} × ${resolution} native canvas · four packed PNG frames · unapproved v1`:'Not Started · no replacement asset created';
    $('native-preview').width=resolution;$('native-preview').height=resolution;
    $('motion-note').textContent={swim:'Four-frame swim study. Fin and tail poses change; minor body/band drift remains a cleanup item.',idle:'The same four poses at a slower cadence: an idle timing concept, not a separate authored idle set.',turn:'Turning concept: right/left mirrored endpoints every two seconds. Intermediate perspective frames are not yet drawn.',death:'Static inverted frame-0 pose: no fin motion. Dedicated death transition, sinking and decomposition artwork remain unfinished.'}[mode];
    $('play-toggle').textContent=playing?'Pause animation':'Play animation';$('play-toggle').setAttribute('aria-pressed',String(playing));
    $('step-frame').disabled=mode==='death';
    document.querySelectorAll('.stage').forEach(e=>e.className='stage '+background);
    render();
  }
  $('species-select').replaceChildren(...Object.values(D.species).map(d=>{const o=document.createElement('option');o.value=d.id;o.textContent=`${d.name}${d.fictional?' · fictional':''}`;return o;}));$('species-select').value='clown';
  $('priority-list').innerHTML='<li>Clownfish · benchmark ready for review</li><li>Niger triggerfish · planned</li><li>Marine angelfish · species unresolved</li><li>Lionfish · species unresolved</li><li>Dogface pufferfish · planned</li><li>Blue tang · planned</li>';
  for(const size of [96,128,192,256]){const item=document.createElement('div');item.className='resolution-study';item.innerHTML=`<canvas id="study-${size}" width="256" height="192" aria-label="${size}-pixel candidate at equal display size"></canvas><p>${size} × ${size} native${size===128?' · suggested':''}</p>`;$('resolution-studies').append(item);}
  $('species-select').onchange=e=>{species=e.target.value;frame=0;elapsed=0;update(true);};
  $('resolution-select').onchange=e=>{resolution=Number(e.target.value);update();};
  $('motion-select').onchange=e=>{mode=e.target.value;elapsed=0;frame=0;update();};
  $('background-select').onchange=e=>{background=e.target.value;update();};
  $('camera-select').onchange=render;
  $('play-toggle').onclick=()=>{playing=!playing;update();};
  $('step-frame').onclick=()=>{playing=false;frame=(frame+1)%4;elapsed=frame/(mode==='idle'?3:6);update();};
  $('save-review').onclick=()=>{
    const status=$('status-select').value,notes=$('review-notes').value.slice(0,2000);
    reviews[species]={status,notes,recordedBy:'user',assetVersion:species==='clown'?metadata.id:'current-procedural',recordedAt:new Date().toISOString()};
    try{localStorage.setItem(reviewKey,JSON.stringify(reviews));$('review-message').textContent='Your review is saved locally. Your notes are recorded; the assigned gameplay artwork stays active.';}
    catch{$('review-message').textContent='Browser storage is unavailable. This review is kept for this page session; copy your feedback before leaving.';}
    $('review-badge').textContent=status;diagnostic.status=status;
  };
  update(true);
  Promise.all([96,128,192,256].map(size=>new Promise((resolve,reject)=>{
    const image=new Image();image.onload=()=>{images.set(size,image);diagnostic.loadedAtlases++;resolve();};image.onerror=()=>reject(Error('Cannot load the local '+size+'-pixel atlas. Keep the assets folder with this page.'));image.src='assets/livestock/fish/clownfish/'+metadata.atlases[size].file;
  }))).then(()=>{diagnostic.ready=true;update();}).catch(error=>{diagnostic.errors.push(error.message);$('proposal-caption').textContent=error.message;});
  function tick(now){
    const dt=previous?Math.min(.1,(now-previous)/1000):0;previous=now;
    if(!document.hidden&&playing&&diagnostic.ready&&mode!=='death'){
      elapsed+=dt;budget+=dt;
      if(budget>=1/30){budget=0;frame=Math.floor(elapsed*(mode==='idle'?3:6))%4;render();}
    }
    requestAnimationFrame(tick);
  }
  requestAnimationFrame(tick);
})();
