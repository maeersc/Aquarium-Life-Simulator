"use strict";
// Versioned additive schema-2 extension. Unknown/invalid hidden fields fail rather than reroll.
AL.HealthSave={validate(s,identity){
  const H=AL.Health,P=H.products,C=H.conditions;
  const fail=m=>{throw Error('Invalid marine health/market save: '+m);};
  const num=(v,a,b)=>{if(typeof v!=='number'||!Number.isFinite(v)||v<a||v>b)fail('number outside bounds');};
  const integer=(v,a,b)=>{num(v,a,b);if(!Number.isInteger(v))fail('integer required');};
  const arr=(v,max)=>{if(!Array.isArray(v)||v.length>max)fail('array bounds');};
  const bool=v=>{if(typeof v!=='boolean')fail('boolean required');};
  const text=(v,max)=>{if(typeof v!=='string'||!v.length||v.length>max)fail('text required');};
  const quality=q=>{if(!q||typeof q!=='object')fail('quality missing');for(const k of ['efficacy','contamination','compatibility'])num(q[k],0,1);bool(q.authentic);if(!C[q.target])fail('unknown treatment target');};
  if(s.healthExtensionVersion!==1)fail('unsupported extension version');arr(s.medicalInventory,80);if(!s.medicineStock||typeof s.medicineStock!=='object')fail('stock missing');for(const id of Object.keys(P))integer(s.medicineStock[id],0,100);
  for(const b of s.medicalInventory){identity(b.id);if(!P[b.product])fail('unknown medicine');integer(b.quantity,0,1000);num(b.acquired,0,1e9);bool(b.examined);if(P[b.product].restricted)quality(b.quality);else if(b.quality!==null)fail('ordinary batch cannot have hidden dealer quality');}
  const m=s.livestockMarket;if(!m||m.version!==1||!m.listings||typeof m.listings!=='object')fail('market version');
  const required=AL.LivestockMarket.keys();
  if(Object.keys(m.listings).length!==required.length)fail('listing set mismatch');
  for(const key of required){const l=m.listings[key];if(!l||l.key!==key)fail('listing missing');identity(l.id);integer(l.price,1,1000000);integer(l.remaining,0,100);num(l.created,0,1e9);integer(l.day,0,1e9);if(!['healthy','stressed','malnourished','infected','carrier'].includes(l.state)||!C[l.infection])fail('listing condition');num(l.severity,.01,1);quality(l.quality);}
  for(const t of s.tanks)if(t.water==='marine'){
    integer(t.medicalSeed,0,4294967295);if(!t.pathogens||typeof t.pathogens!=='object')fail('pathogens missing');for(const [id,v] of Object.entries(t.pathogens)){if(!C[id]?.contagious)fail('invalid infectious exposure');num(v,0,1);}
    if(t.valueHistory!==undefined){arr(t.valueHistory,30);for(const r of t.valueHistory){num(r.time,0,1e9);integer(r.value,0,1e9);}}
    for(const f of [...t.fish,...t.flora,...(t.invertebrates||[])]){const h=f.healthState;if(!h||typeof h!=='object')fail('individual health missing');num(h.nutrition,0,100);for(const k of ['tissue','bleaching','polyps'])num(h[k],0,1);num(h.lastExam,-1,1e9);arr(h.history,30);for(const r of h.history){num(r.time,0,1e9);text(r.event,250);}arr(h.conditions,12);const seen=new Set();for(const c of h.conditions){if(!C[c.type]||!H.eligible(C[c.type].hosts,f)||seen.has(c.type))fail('ineligible or duplicate condition');seen.add(c.type);num(c.severity,0,1);num(c.age,0,1e9);num(c.confidence,0,1);bool(c.diagnosed);bool(c.carrier);if(c.carrier&&!C[c.type].contagious)fail('noninfectious carrier');}
      if(h.treatment!==null){const tr=h.treatment,p=P[tr?.product];if(!p||!H.eligible(p.hosts,f)||tr.duration!==p.duration||p.duration<=0)fail('invalid course');for(const k of ['started','elapsed'])num(tr[k],0,1e9);for(const k of ['efficacy','contamination','compatibility','progress'])num(tr[k],0,1);bool(tr.authentic);if(p.restricted){if(!C[tr.target])fail('missing hidden course target');}else if(tr.target!==null)fail('unexpected course target');}
    }
  }
}};
