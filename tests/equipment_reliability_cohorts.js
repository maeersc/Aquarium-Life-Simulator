(()=>{
 const R=AL.EquipmentReliability,checks=[],distributions=[],N=2048,simulated=64,quantile=(a,p)=>a[Math.floor((a.length-1)*p)],test=(name,ok,detail)=>checks.push({name,pass:!!ok,...(detail?{detail}:{})});
 for(const [type,p]of Object.entries(R.profiles)){
  const clean=[],higher=[],neglect=[],firstFault=[],actual=[],calendar=[],paired=[];let temporary=0,repairable=0;
  for(let seed=1;seed<=N;seed++){
   const o=equipmentUnitFixture(type,seed+4000),r=o.e.reliability,eta=R.eta(o.e),life=eta*Math.cbrt(r.lifeThreshold)/R.Y;clean.push(life);const better=JSON.parse(JSON.stringify(o.e));better.reliability.quality=1.3;higher.push(R.eta(better)*Math.cbrt(better.reliability.lifeThreshold)/R.Y);
   const comp=eta*2*r.componentThreshold/(.25+Math.sqrt(.0625+.32*r.componentThreshold))/R.Y;firstFault.push(Math.min(life,comp));
   if(seed<=simulated){paired.push(life);
    o.t.lightMode=p.duty?'auto':'on';o.t.lightHours=10;let days=0,limit=40*365;while(r.state!=='beyond-repair'&&days<limit){equipmentAdvance(o,24);days++;if(r.state==='temporary-malfunction'){temporary++;R.maintain(o.s,o.t,{id:o.e.id});}else if(r.state==='repair-required'){const part=AL.EquipmentParts.supported(o.e).find(p=>p.part===r.failurePart);if(!part)break;repairable++;AL.EquipmentParts.replace(o.s,o.t,{id:o.e.id,sku:part.sku});}if(r.state==='working'&&r.maintenanceHours>=p.interval*24-1e-7)R.maintain(o.s,o.t,{id:o.e.id});}
    calendar.push(days/365);actual.push(o.e.reliability.effectiveHours/R.Y);const major=r.state==='beyond-repair',sealed=r.state==='repair-required'&&!AL.EquipmentParts.supported(o.e).some(p=>p.part===r.failurePart);test(type+' seed '+seed+': actual multi-year history ends through a logged major or nonserviceable fault, retaining identity',(major||sealed)&&o.s.equipmentReliability.events.some(e=>e.kind==='failure')&&o.e.durability>0&&(major?Math.abs(actual.at(-1)-life)<.01:actual.at(-1)<=life),{years:days/365,expectedMajorOperatingEquivalent:life,actualOperatingEquivalent:actual.at(-1),terminalState:r.state,nonserviceable:sealed});
   }else{
    o.t.lightMode=p.duty?'auto':'on';o.t.lightHours=10;const start=o.s.time;equipmentAdvance(o,40*R.Y);const failure=o.s.equipmentReliability.events.find(e=>e.kind==='failure');if(failure)neglect.push((failure.time-start)/60/R.Y);
   }
  }
  clean.sort((a,b)=>a-b);higher.sort((a,b)=>a-b);firstFault.sort((a,b)=>a-b);neglect.sort((a,b)=>a-b);const mean=clean.reduce((a,b)=>a+b)/N;
  test(type+': fixed-seed mean replacement life is within 8% of the configured target',Math.abs(mean/p.years-1)<.08,{mean,target:p.years});test(type+': quality 1.3 lengthens all paired service lives by 30%',quantile(higher,.5)>quantile(clean,.5)*1.29);
  test(type+': neglect cohort reaches its first fault earlier than maintained equipment',neglect.length===N-simulated&&quantile(neglect,.5)<quantile(firstFault,.5));
  distributions.push({type,seedRange:[4001,4000+N],samples:N,simulatedUnits:simulated,targetYears:p.years,meanYears:mean,p10Years:quantile(clean,.1),medianYears:quantile(clean,.5),p90Years:quantile(clean,.9),meanRealDaysAt20MinuteDay:mean*365/72,medianFirstMalfunctionYears:quantile(firstFault,.5),neglectSamples:neglect.length,neglectedMedianFirstFaultYears:quantile(neglect,.5),maintenanceGameDays:p.interval,maintenanceRealHours:p.interval/3,simulatedTemporaryFaults:temporary,simulatedRepairableFaults:repairable,simulatedMeanCalendarYears:calendar.reduce((a,b)=>a+b)/calendar.length,pairedPredictedMeanFor64Units:paired.reduce((a,b)=>a+b)/paired.length});
 }
 return {checks,distributions,samplesPerType:N,simulatedPerType:simulated,passed:checks.filter(c=>c.pass).length,failed:checks.filter(c=>!c.pass).length};
})()
