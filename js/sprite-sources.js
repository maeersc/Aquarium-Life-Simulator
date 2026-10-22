"use strict";
// Per-sheet local script transport keeps file:// pixel reads origin-clean.
// HTTPS loads PNGs directly. Neither route needs a server account or network service.
AL.SpriteSources=(()=>{
 const pending=new Map();let active=0;const queue=[];
 function next(){while(active<4&&queue.length){const task=queue.shift();active++;task();}}
 function load(clip){if(clip.src)return Promise.resolve(clip.src);if(location.protocol!=='file:')return Promise.resolve(clip.path);if(pending.has(clip.path))return pending.get(clip.path).promise;
  let resolve;const promise=new Promise(r=>resolve=r),row={promise,resolve,script:null,src:null};pending.set(clip.path,row);
  queue.push(()=>{const script=document.createElement('script');row.script=script;script.src='assets/livestock/animation-sources/'+clip.sha256+'.js';script.onload=()=>finish(clip.path);script.onerror=()=>finish(clip.path);document.head.append(script);});next();return promise;
 }
 function finish(path){const row=pending.get(path);if(!row)return;pending.delete(path);row.script?.remove();row.resolve(row.src);row.src=null;active--;next();}
 function accept(path,src){const row=pending.get(path);if(row)row.src=src;}
 return {load,accept,get metrics(){return {active,queued:queue.length,pending:pending.size};}};
})();
