(()=>{
 const K=AL.Core,D=AL.Data,S=AL.Sim,copy=s=>JSON.parse(JSON.stringify(s));
 function fixture(scenario){const s=K.newGame('marine',20261015),t=s.tanks[0];s.settings.speed=0;s.time=0;s.credits=1000000;s.level=20;s.xp=3800;s.update29.tutorial.status='skipped';delete s.update29;AL.Update29.migrate(s);delete s.finance;delete s.progression;AL.Finance.initialize(s);AL.Progression.migrate(s);AL.DailyStore.rotate(s);AL.Update31.rotate(s);s.careReward.day=0;s.careReward.lastCompleted=s.careReward.lastClaimed=-1;
  t.volume=1000;t.prepared=true;t.emptyDry=false;t.bacteria=t.bacteria2=1;t.ecosystemAge=500;t.lightHours=10;t.lightIntensity=.8;t.foodType='pellets';t.equipment=['filter','heater','reefLight','flow','air','skimmer','feeder','dosing'].map(type=>({id:K.id(s,'equipment'),type,capacity:2000,durability:100,enabled:true}));t.substrate.depth=2;t.hardscape=[.25,.55,.8].map(x=>({id:K.id(s,'rock'),group:'fiji',variant:3,x,y:AL.Habitat.plane(t,.5)+.0125,z:.5,width:90,baseOffset:.0125}));
  for(const key of Object.keys(s.inventory))s.inventory[key]=key.startsWith('frag-')?0:1000;
  const addFish=id=>{const f=K.fish(s,id);f.hunger=10;t.fish.push(f);return f;};
  const coral=type=>{const p=AL.Update29.mounting(s,t,type);if(!p)throw Error('No fixture coral mount: '+type);const f={id:K.id(s,'flora'),type,name:D.flora[type].name,...p,hp:100,size:1,age:60,color:1};AL.Health.initialize(f);t.flora.push(f);return f;};
  if(scenario==='coral-photosynthetic'){coral('zoa');coral('mushroom');}
  else if(scenario==='coral-feeding'){coral('tubastraea-micranthus');}
  else if(scenario==='grazers-scavengers'){for(const id of ['tiger-sand-conch','halloween-hermit-crab','lysmata-amboinensis'])t.invertebrates.push(AL.Invertebrates.make(s,t,id));}
  else if(scenario==='mixed-feeder'){for(const id of ['clown','gramma','watchman','blenny'])addFish(id);coral('zoa');for(const id of ['tiger-sand-conch','lysmata-amboinensis'])t.invertebrates.push(AL.Invertebrates.make(s,t,id));}
  else{addFish('clown');if(scenario==='juvenile'){const f=t.fish[0];f.age=5;f.growth=.08;t.foodType='fry';}if(scenario==='disease')AL.Health.infect(s,t.fish[0],'velvet',.6);}
  if(scenario==='no-feeder')t.equipment=t.equipment.filter(e=>e.type!=='feeder');
  if(scenario==='food-shortage'){for(const k of Object.keys(D.foods))s.inventory[k]=0;s.inventory.pellets=2;}
  if(scenario==='failed-flow'){coral('sps');t.equipment.filter(e=>['air','flow'].includes(e.type)).forEach(e=>e.durability=0);t.waterParams.oxygen=3;}
  if(scenario==='immature-cycle'){t.bacteria=.02;t.bacteria2=.01;t.waterParams.ammonia=1;}
  if(scenario==='multiple'){const second=copy(t);second.id=K.id(s,'tank');second.name='Second reef';second.fish=[];second.hardscape=[];for(const e of second.equipment)e.id=K.id(s,'equipment');for(const id of ['clown'])second.fish.push(K.fish(s,id));s.tanks.push(second);}
  delete s.progression;AL.Progression.migrate(s);for(const t of s.tanks)for(const e of t.equipment)AL.EquipmentReliability?.initialize({...s,accountId:'overnight-fixture:'+scenario},e,true);AL.MarineCare?.migrate(s);AL.Mortality?.migrate(s);return s;
 }
 const all=s=>s.tanks.flatMap(t=>[...t.fish,...t.flora,...t.invertebrates].map(f=>({t,f})));
 function run(scenario,hours){const initial=fixture(scenario),minutes=hours*3600*AL.Config.minutesPerSecond,a=copy(initial),b=copy(initial),out=[];const oldDeath=AL.Update29.death,oldStep=S.step;
  function process(s,offline){const deaths=[],seen=new Set(),range={};function capture(state,t,f){if(state===s&&(f.dead||f.hp<=0)&&!seen.has(f.id)){seen.add(f.id);deaths.push({id:f.id,species:f.species||f.type||f.invertebrate,time:state.time,cause:f.deathCause||'Cause of death undetermined.',hp:f.hp,hunger:f.hunger??f.coralHunger??null,nutrition:f.healthState?.nutrition,conditions:copy(f.healthState?.conditions||[]),water:copy(t.waterParams),feeder:t.equipment.filter(e=>e.type==='feeder').map(e=>({...e})),foodType:t.foodType,foodStock:Object.fromEntries(Object.keys(D.foods).map(k=>[k,state.inventory[k]||0]))});}}AL.Update29.death=function(state,t,f){capture(state,t,f);return oldDeath(state,t,f);};
   S.step=function(state,n){const result=oldStep(state,n);if(state===s)for(const {t,f}of all(s))capture(state,t,f);if(state===s)for(const t of s.tanks)for(const [k,v]of Object.entries(t.waterParams)){range[k]??={min:v,max:v};range[k].min=Math.min(range[k].min,v);range[k].max=Math.max(range[k].max,v);}return result;};
   try{if(offline)AL.Offline.sync(s,s.simulationCheckpoint+hours*3600000);else for(let n=0;n<minutes;n+=5)S.step(s,Math.min(5,minutes-n));}finally{AL.Update29.death=oldDeath;S.step=oldStep;}
   return {diagnostics:copy(s.mortality?.events||[]),alive:all(s).filter(o=>!o.f.dead&&o.f.hp>0).length,total:all(s).length,deaths,range,final:all(s).map(({t,f})=>({id:f.id,species:f.species||f.type||f.invertebrate,hp:f.hp,hunger:f.hunger??f.coralHunger,nutrition:f.healthState?.nutrition,conditions:f.healthState?.conditions})),water:s.tanks.map(t=>t.waterParams),rewards:s.update29.survival.earned,healthy:s.careReward.earned,food:Object.fromEntries(Object.keys(D.foods).map(k=>[k,s.inventory[k]||0])),tanks:s.tanks.map(t=>({id:t.id,feeder:t.lastAutoFeed,autoFeedSlot:t.autoFeedSlot,equipment:t.equipment,forage:t.forage})),time:s.time};
  }
  const continuous=process(a,false),offline=process(b,true);const comparable=v=>{const x=copy(v);for(const e of x.diagnostics){for(const k of ['realTimestamp','recordedAt','simulation','runId'])delete e[k];}return x;};return {scenario,realHours:hours,gameDays:minutes/1440,equivalent:JSON.stringify(comparable(continuous))===JSON.stringify(comparable(offline)),continuous,offline};
 }
 window.overnightFixture=fixture;window.overnightRun=run;return true;
})()
