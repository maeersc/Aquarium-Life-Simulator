"use strict";
AL.LifeStages.ready.then(()=>{
  window.showContact=page=>{
    document.querySelector('main').replaceChildren();
    for(const m of AL.LifeStages.records.slice(page*9,page*9+9)){
      const row=document.createElement('article'),title=document.createElement('strong');title.textContent=m.name;row.append(title);
      for(const state of ['alive','dead'])for(const stage of ['egg','baby','juvenile','adult']){
        const c=document.createElement('canvas');c.width=192;c.height=160;const ctx=c.getContext('2d'),sprite=AL.LifeStages.frame(m.id,stage,state);ctx.drawImage(sprite,0,0);
        const e=sprite.artMeta.eye;if(e){ctx.strokeStyle='#f8d88e';ctx.strokeRect(Math.round(e.x-e.w/2),Math.round(e.y-e.h/2),e.w,e.h);}row.append(c);
      }document.querySelector('main').append(row);
    }window.CONTACT_READY=true;
  };showContact(0);
});
