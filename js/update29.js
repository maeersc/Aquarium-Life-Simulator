"use strict";
// Versioned marine milestone. All mutations run within Core.act or fixed simulation steps.
AL.Update29=(()=>{
 const K=AL.Core,D=AL.Data,day=s=>Math.floor(s.time/1440),tiers=['Common','Uncommon','Rare','Very Rare','Ultra Rare','Legendary'];
 const survivalAmount=100;
 const lossMessage='Livestock lost! Daily survival bonus interrupted. Complete one full in-game day without a death to restore eligibility.';
 const lockText='Freshwater — Coming in a Future Update.';
 function initial(s){return {version:1,tutorial:{step:0,status:'skipped'},survival:{policyVersion:2,day:day(s),tracked:0,stocked:0,lost:false,lastDeath:null,recoveryUntil:0,lastCompleted:day(s)-1,lastPaid:-1,earned:0},mysteryStock:{day:day(s),coral:3,bottom:3}};}
 function migrate(s){if(!s?.tanks||!s.inventory||!s.stock)return;if(s.update29===undefined){s.update29=initial(s);for(const t of s.tanks)for(const f of [...t.fish,...t.flora,...(t.invertebrates||[])])if(f.dead||f.hp<=0)f.survivalLossRecorded=true;}if(s.update29?.version!==1)throw Error('Unsupported v2.9 save extension.');
  const survival=s.update29.survival;if(survival?.policyVersion===undefined){survival.policyVersion=2;survival.stocked=Math.min(survival.stocked,Math.max(0,s.time-Math.max(survival.day*1440,survival.recoveryUntil)));}
  for(const r of AL.Update29Catalog.records)s.stock[r.id]??=r.purchaseVerified===false?0:r.category==='coral'?12:24;
  for(const key of ['angel-ration','reef-meat','starfish-tissue']){s.inventory[key]??=0;s.stock[key]??=30;}
  for(const t of s.tanks)if(t.water==='marine')t.nurseries??=[];
 }
 function newGame(s){migrate(s);s.update29.tutorial={step:0,status:'active'};}
 function eligibleResidents(s){return s.tanks.filter(t=>t.prepared&&t.water==='marine').flatMap(t=>[...t.fish,...(t.water==='marine'?t.flora:[]),...(t.invertebrates||[]),...(t.nurseries||[])]).filter(f=>!f.dead&&f.hp>0);}
 function death(s,t,f){migrate(s);const r=s.update29.survival;if((!f.dead&&f.hp>0)||f.survivalLossRecorded)return;AL.Mortality?.record(s,t,f);f.survivalLossRecorded=true;r.lost=true;r.lastDeath=s.time;r.recoveryUntil=s.time+1440;K.log(s,lossMessage,'warning');}
 function beforeStep(s,minutes){migrate(s);const r=s.update29.survival;if(r.day!==day(s)){r.day=day(s);r.tracked=0;r.stocked=0;r.lost=false;}r.tracked=Math.min(1440,r.tracked+minutes);if(s.time>=r.recoveryUntil&&eligibleResidents(s).length)r.stocked=Math.min(1440,r.stocked+minutes);}
 function afterStep(s,previous,minutes){
  const r=s.update29.survival,d=day(s),oldDay=Math.floor(previous/1440);
  if(s.update29.mysteryStock.day!==d)s.update29.mysteryStock={day:d,coral:3,bottom:3};
  for(const t of s.tanks)if(t.water==='marine'){
   for(const n of t.nurseries||[]){if(n.dead)continue;const d=D.invertebrates[n.invertebrate],safe=AL.Health.safe(t,{invertebrate:n.invertebrate});n.age+=minutes/60;n.stage=n.progress<24?"Brooded embryo nursery":"Larval nursery";n.progress+=safe?minutes/60:0;if(!safe)AL.Mortality?.note(s,t,n,'Unsuitable nursery conditions',minutes/30);n.viability=K.clamp(n.viability-(safe?0:minutes/30),0,100);
    if(n.viability<=0){n.dead=true;n.hp=0;death(s,t,n);K.log(s,d.name+' nursery specimen lost under unsuitable conditions.','warning');continue;}
    if(n.progress>=n.required){const report=AL.Invertebrates.report(s,{...t,nurseries:t.nurseries.filter(other=>other!==n)},n.invertebrate);if(!report.ok){n.progress=n.required;continue;}const f=AL.Invertebrates.make(s,t,n.invertebrate);f.id=n.id;f.age=d.maturity*.3;f.growth=.3;f.hp=n.viability;f.provenance=n.provenance;f.mystery=n.mystery;f.healthState.nutrition=Math.max(0,100-n.age*.1);AL.Health.arrival(s,t,f);t.invertebrates.push(f);n.settled=true;s.discoveredInvertebrates??=[];if(!s.discoveredInvertebrates.includes(d.id))s.discoveredInvertebrates.push(d.id);K.log(s,d.name+' settled as a small juvenile; development uses the labeled nursery abstraction.');}
   }t.nurseries=t.nurseries.filter(n=>!n.settled);
   for(const f of t.flora){if(f.hp<=0&&!f.survivalLossRecorded)death(s,t,f);const def=D.flora[f.type];if(!def.nonPhotosynthetic||f.hp<=0)continue;AL.MarineCare.coralFood(s,t,f,minutes/60);}
   t.food=t.food.filter(p=>!p.eaten);
  }  if(d!==oldDay){if(oldDay>r.lastCompleted){if(r.tracked>=1440-1e-6&&r.stocked>=1440-1e-6&&!r.lost&&s.time>=r.recoveryUntil&&oldDay>r.lastPaid){if(AL.Finance)AL.Finance.change(s,survivalAmount,{category:'daily',action:'survivalReward',name:'Livestock Survival Bonus',actionId:'survival:'+oldDay,key:'survival:'+oldDay,qualification:'qualified',qualifyingDay:oldDay,periodStart:oldDay*1440,periodEnd:(oldDay+1)*1440});else s.credits+=survivalAmount;s.stats.earnings+=survivalAmount;r.earned+=survivalAmount;r.lastPaid=oldDay;K.log(s,'Livestock Survival Bonus: +'+survivalAmount+' AC');}r.lastCompleted=oldDay;}r.day=d;r.tracked=0;r.stocked=0;r.lost=false;}

 }
 function waterQuote(t,fraction){const changed=t.volume*fraction,marine=t.water==='marine';return {liters:changed,water:Math.ceil(changed*(marine?.13:.04)),supply:marine?'salt':'conditioner',doses:marine?Math.max(1,Math.ceil(changed/2-1e-10)):1};}
 function beforeAction(s,t,name,a){migrate(s);
  if(name==='buyTank'&&a.water==='fresh'||name==='selectAquarium'&&s.tanks.find(n=>n.id===a.id)?.water==='fresh')throw Error(lockText);
  if(t.water==='fresh'&&!['buyTank','selectAquarium','claim','discoverMarket','tutorialProgress','buyResearch','casinoWager','casinoSettle','casinoLimit'].includes(name))throw Error(lockText);
  if(name==='buyFish'&&D.species[a.species]?.water==='fresh'||name==='buyFlora'&&D.flora[a.type]?.water==='fresh'||name==='buyEgg'&&D.species[a.species]?.water==='fresh')throw Error(lockText);
  const id=a.species||a.type,d=D.species[id]||D.flora[id]||D.invertebrates[id];
  if(['buyFish','buyFlora','buyInvertebrate','buyEgg'].includes(name)&&d?.purchaseVerified===false)throw Error(d.acquisitionHold||'This species is held until its care requirements are supported.');
  if(name==='waterChange'){const q=waterQuote(t,Number(a.fraction??.25));if(s.inventory[q.supply]<q.doses)throw Error('This change needs '+q.doses+' '+q.supply+' doses for '+AL.Units.preciseVolume(q.liters)+' of replacement water.');}
  if(['moveFish','moveFlora','moveInvertebrate'].includes(name)&&s.tanks.find(n=>n.id===a.target)?.water==='fresh')throw Error(lockText);
 }
 function afterAction(s,t,name,a,previous){migrate(s);
  if(name==='claim'&&a.id==='prepare'&&!s.achievements.includes('First safe beginning'))s.achievements.push('First safe beginning');
 }
 function pool(category,tier){const all=category==='coral'?Object.entries(D.flora).filter(([,d])=>d.water==='marine').map(([id,d])=>({...d,id})):Object.values(D.invertebrates);return all.filter(d=>d.purchaseVerified!==false&&AL.Rarity.get(d.rarity||AL.Rarity.plant(d.id).name).name===tier);}
 function missing(category){return tiers.filter(tier=>!pool(category,tier).length);}
 function mounting(s,t,id,a={}){if(Number.isFinite(a.x)){const r=AL.Habitat.placement(s,t,id,a.x,a.y,{size:1,z:a.z});return r.ok?r.position:null;}const points=[];for(const r of t.hardscape||[]){for(const fraction of [-.25,0,.25]){const x=r.x+fraction*r.width/480,m=AL.HabitatGeometry[r.group]?.[r.variant],px=Math.floor((x*480-(r.x*480-r.width/2))/r.width*192),top=m?.columns[px]?.[0]?.[0];if(top!==undefined)points.push({x,y:(r.y*240-r.width*184/192+top/192*r.width)/240,z:r.z??.5});}}for(const r of t.mounts||[])for(const dx of [-.25,0,.25])points.push({x:r.x+dx*r.width/480,y:r.y,z:r.z??.5});for(const p of points){const r=AL.Habitat.placement(s,t,id,p.x,p.y,{size:1,z:p.z});if(r.ok)return r.position;}return null;}
 function outcomeReport(s,t,d,category,a={}){if(category==='coral'){const r=AL.StoreRules.report(s,t,'buyFlora',{type:d.id,mysteryOutcome:true});if(r.ok&&!mounting(s,t,d.id,a)){r.ok=false;r.reasons.push('No free valid supported mounting position.');}return r;}return AL.Invertebrates.report(s,t,d.id);}
 function mysteryReport(s,t,category,a={}){const reasons=[],warnings=[],short=missing(category);if(short.length)reasons.push('Catalog content hold: missing eligible '+short.join(', ')+' '+(category==='coral'?'coral':'bottom-dweller')+' outcomes. Exact odds require all six tiers; no charge or substitution.');if(t?.water!=='marine')reasons.push('Choose a saltwater destination.');if(category==='bottom'&&(t?.nurseries?.length??0)>=20)reasons.push('Nursery is full.');
  if(!short.length&&t?.water==='marine')for(const tier of tiers)if(!pool(category,tier).some(d=>outcomeReport(s,t,d,category,a).ok))reasons.push('No safe '+tier+' outcome: choose another prepared home with suitable space, equipment, food and mounting.');return {ok:!reasons.length,reasons,warnings};}
 function mystery(s,t,a,category){const report=mysteryReport(s,t,category,a);if(!report.ok)throw Error(report.reasons.join(' '));const key=category==='coral'?'coral':'bottom',price=category==='coral'?450:500,stock=s.update29.mysteryStock;if(stock[key]<1||s.credits<price)throw Error('Check mystery item funds and daily stock.');
  const roll=AL.Random.int(s,category==='coral'?'coralMysteryRng':'bottomMysteryRng',10000),index=[5000,7500,9000,9750,9950,10000].findIndex(v=>roll<v),tier=tiers[index],eligible=pool(category,tier).filter(d=>outcomeReport(s,t,d,category,a).ok),d=eligible[AL.Random.int(s,category==='coral'?'coralMysteryRng':'bottomMysteryRng',eligible.length)];
  if(AL.Finance)AL.Finance.change(s,-price);else s.credits-=price;s.stats.expenses+=price;stock[key]--;const mystery={product:key,rarity:tier,revealed:true,roll},provenance={source:category==='coral'?'mystery-coral':'mystery-bottom',acquired:s.time};
  if(category==='coral'){const f={id:K.id(s,'flora'),type:d.id,name:d.name,...mounting(s,t,d.id,a),hp:100,size:1,age:0,color:1,rarity:tier,mystery,provenance};AL.Health.initialize(f);AL.Health.arrival(s,t,f);t.flora.push(f);s.stats.floraBought++;}
  else t.nurseries.push({id:K.id(s,'nursery'),invertebrate:d.id,name:d.name,rarity:tier,viability:100,hp:100,progress:0,required:48,age:0,dead:false,mystery,provenance,stage:'brooded embryo / larval nursery',abstraction:'An enclosed aquaculture nursery is a game abstraction, not a claim that every species has a transferable egg. Settlement creates a small juvenile, never an adult.'});
  K.log(s,(category==='coral'?'Mystery Coral':'Mystery Bottom-Dweller Egg')+' revealed: '+d.name+' · '+tier+'.');
 }
 function products(s,category){const type=category==='flora'?'coral':'bottom',name=type==='coral'?'Mystery Coral':'Mystery Bottom-Dweller Egg',short=missing(type);return [{id:'mystery:'+type,kind:'mystery',mysteryCategory:type,name,price:type==='coral'?450:500,stock:short.length?0:s.update29.mysteryStock[type],action:type==='coral'?'buyMysteryCoral':'buyMysteryBottom',args:{},habitat:'marine',description:'Independent Common 50%, Uncommon 25%, Rare 15%, Very Rare 7.5%, Ultra Rare 2%, Legendary 0.5%. '+(short.length?'Catalog content hold: missing eligible '+short.join(', ')+'. No substitution or charge.':type==='coral'?'Resolves to a living frag on an existing valid supported mount; reposition it afterward.':'Species-appropriate early specimen in a labeled nursery abstraction; never instant adult.')}];}
 function validate(s,identity){const v=s.update29;if(!v||v.version!==1)throw Error('Invalid v2.9 extension.');const r=v.survival,t=v.tutorial,ms=v.mysteryStock;
  const integer=(n,min,max)=>Number.isInteger(n)&&n>=min&&n<=max,num=(n,min,max)=>Number.isFinite(n)&&n>=min&&n<=max;
  if(!t||!integer(t.step,0,11)||!['active','skipped','completed'].includes(t.status))throw Error('Invalid tutorial progress.');
  if(!r||r.policyVersion!==2||r.day!==day(s)||!num(r.tracked,0,1440)||!num(r.stocked,0,r.tracked)||typeof r.lost!=='boolean'||!num(r.recoveryUntil,0,1e9+1440)||r.lastDeath!==null&&!num(r.lastDeath,0,s.time)||r.lastDeath!==null&&r.recoveryUntil!==r.lastDeath+1440||!integer(r.lastCompleted,-1,day(s)-1)||!integer(r.lastPaid,-1,r.lastCompleted)||!integer(r.earned,0,1e9)||r.earned%survivalAmount)throw Error('Invalid survival reward checkpoint.');
  if(!ms||ms.day!==day(s)||!integer(ms.coral,0,3)||!integer(ms.bottom,0,3))throw Error('Invalid new mystery stock.');
  for(const key of ['coralMysteryRng','bottomMysteryRng'])if(s[key]!==undefined&&!integer(s[key],0,4294967295))throw Error('Invalid independent mystery stream.');
  const outcome=(f,product,rarity)=>{if(!f.mystery)return;const m=f.mystery;if(m.product!==product||m.revealed!==true||!integer(m.roll,0,9999)||m.rarity!==rarity||tiers[[5000,7500,9000,9750,9950,10000].findIndex(v=>m.roll<v)]!==rarity)throw Error('Invalid saved mystery outcome.');};
  for(const tank of s.tanks){for(const f of tank.flora)outcome(f,'coral',f.rarity);for(const f of tank.invertebrates||[])outcome(f,'bottom',D.invertebrates[f.invertebrate]?.rarity);for(const f of tank.nurseries||[])outcome(f,'bottom',f.rarity);}
  for(const tank of s.tanks){if(tank.water!=='marine')continue;if(!Array.isArray(tank.nurseries)||tank.nurseries.length>20)throw Error('Invalid nursery collection.');for(const n of tank.nurseries){identity(n.id);if(!D.invertebrates[n.invertebrate]||n.rarity!==D.invertebrates[n.invertebrate].rarity||!num(n.viability,0,100)||!num(n.hp,0,100)||!num(n.progress,0,48)||n.required!==48||!num(n.age,0,1e9)||typeof n.dead!=='boolean'||n.dead&&n.hp!==0||n.mystery?.product!=='bottom'||n.mystery?.rarity!==n.rarity||n.mystery?.revealed!==true||!integer(n.mystery.roll,0,9999))throw Error('Invalid persistent nursery outcome.');}}
 }
 function reservedLoad(t){return (t.nurseries||[]).filter(n=>!n.dead).reduce((total,n)=>total+(D.invertebrates[n.invertebrate]?.load||0),0);}
 function nurseryValue(n){return n.dead?0:Math.floor((D.invertebrates[n.invertebrate]?.price||0)*.25*n.viability/100);}
 function tutorial(s,a){if(!Number.isInteger(a.step)||a.step<0||a.step>11||!['active','skipped','completed'].includes(a.status))throw Error('Invalid tutorial request.');s.update29.tutorial={step:a.step,status:a.status};}
 return {survivalAmount,lossMessage,migrate,newGame,beforeAction,afterAction,beforeStep,afterStep,death,eligibleResidents,waterQuote,pool,missing,mounting,mysteryReport,mystery,products,validate,tutorial,nurseryValue,reservedLoad,lockText};
})();
