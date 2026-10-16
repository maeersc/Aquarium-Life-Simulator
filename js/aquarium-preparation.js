"use strict";
// One preparation authority, using the existing save flags rather than a second
// stored phase enum. `prepared` records completed preparation; `emptyDry` only
// describes physical filling. Preparation implies water is present.
AL.Preparation=(()=>{
 const prepared=t=>t?.prepared===true;
 const filled=t=>!!t&&(prepared(t)||t.emptyDry!==true);
 function state(t){const ready=prepared(t),wet=filled(t),cycled=ready&&t.bacteria>=.65&&t.bacteria2>=.5&&!t.cycleActive,phase=!wet?'dry':!ready?'filled':cycled?'cycled':'prepared';return {phase,filled:wet,prepared:ready,cycled,label:phase==='dry'?'Dry aquarium':phase==='filled'?'Filled; water not prepared':phase==='cycled'?'Prepared and cycled':(t.water==='marine'?'Prepared saltwater':'Prepared water')+(t.cycleActive?' — cycling':'')};}
 function record(s,t,event,evidence){if(t.preparationHistory===undefined)t.preparationHistory=[];if(!Array.isArray(t.preparationHistory))throw Error('Invalid preparation history.');t.preparationHistory.push({time:s.time,event,evidence});t.preparationHistory=t.preparationHistory.slice(-32);}
 function fill(s,t){if(t.water!=='marine')throw Error(AL.Update29.lockText);if(filled(t))throw Error('This aquarium already contains water.');t.emptyDry=false;record(s,t,'filled','Player confirmed adding water.');AL.Core.log(s,t.name+': filled with water. Prepare saltwater before cycling or adding livestock.');}
 function prepare(s,t){if(prepared(t))throw Error('This tank is already prepared.');if(!filled(t))record(s,t,'filled','Included in the existing Prepare water action.');t.emptyDry=false;t.prepared=true;record(s,t,'prepared','Player completed the Prepare water action.');s.stats.prepared++;AL.Core.log(s,t.name+': water conditioned and temperature set. Start fishless cycling next.');}
 function migrate(s){for(const t of s.tanks||[]){if(t.water!=='marine'||typeof t.prepared!=='boolean')continue;if(t.prepared&&t.emptyDry!==true)continue;const history=Array.isArray(t.preparationHistory)?t.preparationHistory:[],last=[...history].reverse().find(e=>['dry','filled','prepared','cycled'].includes(e.event)),historyProof=last&&['prepared','cycled'].includes(last.event)&&Number.isFinite(last.time)&&last.time>=0&&last.time<=s.time,cycleProof=!last&&Number.isFinite(t.cycle)&&t.cycle>=AL.Config.cycleHours&&t.cycleActive===false;
   if(t.prepared&&t.emptyDry===true){t.emptyDry=false;record(s,t,'legacy-repair','Saved prepared=true confirms completed preparation; cleared the stale dry marker.');}
   else if(!t.prepared&&(historyProof||cycleProof)){t.prepared=true;t.emptyDry=false;record(s,t,'legacy-repair',historyProof?'Saved per-aquarium preparation history confirms completion.':'Saved completed fishless-cycle progress confirms prior preparation; cycling only progresses after preparation.');}
  }}
 function validate(s){for(const t of s.tanks){if(t.water!=='marine')continue;if(t.prepared&&t.emptyDry===true)throw Error('Prepared aquarium has a stale dry marker; migrate its preparation state.');if(t.preparationHistory!==undefined){if(!Array.isArray(t.preparationHistory)||t.preparationHistory.length>32)throw Error('Invalid preparation history.');let previous=0;for(const e of t.preparationHistory){if(!['dry','filled','prepared','cycled','legacy-repair'].includes(e.event)||!Number.isFinite(e.time)||e.time<previous||e.time>s.time||typeof e.evidence!=='string'||e.evidence.length>300)throw Error('Invalid preparation event.');previous=e.time;}}}}
 return {prepared,filled,state,record,fill,prepare,migrate,validate};
})();
