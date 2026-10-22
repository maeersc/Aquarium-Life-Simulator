/* Classic scripts deliberately support file:// without imports or requests. */
"use strict";
window.AL = window.AL || {};
AL.Config = Object.freeze({version:2,startCredits:3000,minutesPerSecond:1,stepMinutes:5,autosaveSeconds:20,maxTanks:12,maxFish:250,offlineCapHours:8,dayBuyerBudget:1200,saleLimit:8,cycleHours:36});
AL.Data = (() => {
  // Husbandry ranges are conservative game parameters; see GAME_DESIGN.md for sources and limits.
  const species = {};
  function fish(id,name,water,price,size,minTank,load,color,pattern,options={}) {
    species[id]={id,name,water,price,size,minTank,load,color,pattern,secondary:'#e7d9a4',shape:'oval',temp:[23,27],ph:water==='fresh'?[6.5,7.8]:[8,8.4],salinity:water==='fresh'?[0,1]:[32,36],diet:['flakes','pellets','frozen'],group:1,aggression:0.1,predator:0,activity:1,zone:0.45,habitat:'plants',life:4,maxLife:7,maturity:80,reproduction:'eggs',incubation:48,brood:2,breedCooldown:168,fertility:0.75,rarity:'Common',level:1,immune:0.8,nocturnal:false,fictional:false,notes:'Peaceful community fish; stable water and appropriate shelter matter.',...options};
  }
  fish('guppy','Guppy','fresh',65,5,40,5,'#ed9959','fan',{shape:'guppy',secondary:'#54bbb5',ph:[7,8.2],reproduction:'livebearer',incubation:96,breedCooldown:168,life:2,maxLife:4,notes:'Livebearer. Fry need fine food and dense plant cover.'});
  fish('neon','Neon tetra','fresh',40,3.5,60,3,'#4fd9e5','neon',{shape:'slim',secondary:'#e25557',group:6,temp:[22,26],ph:[6,7.5],incubation:24,notes:'Keep a school of at least six. Soft, slightly acidic water is preferred.'});
  fish('cardinal','Cardinal tetra','fresh',55,4.5,75,4,'#44cce9','cardinal',{shape:'slim',secondary:'#ea5057',group:6,temp:[24,28],ph:[5.5,7],level:2,notes:'Warm-water schooling tetra. Red coloration extends along the underside.'});
  fish('betta','Betta','fresh',130,6,20,9,'#c96076','flowing',{shape:'betta',secondary:'#819ed8',aggression:0.65,activity:0.65,life:3,maxLife:5,incubation:36,notes:'Keep one male per tank. Long-finned tankmates can trigger territorial attacks.'});
  fish('cory','Bronze corydoras','fresh',85,7,75,6,'#bfb589','spots',{shape:'bottom',secondary:'#586c62',zone:0.86,group:6,diet:['sinking','frozen'],temp:[22,27],notes:'Social bottom-dweller. Needs a group, soft substrate and sinking food.'});
  fish('danio','Zebra danio','fresh',45,5,75,4,'#a8c6cb','stripes',{shape:'slim',secondary:'#3e5688',group:6,temp:[20,25],activity:1.8,notes:'Fast, active schooling fish. Needs open horizontal swimming space.'});
  fish('harlequin','Harlequin rasbora','fresh',55,4.5,60,4,'#dc997b','wedge',{shape:'slim',secondary:'#394b65',group:6,ph:[6,7.5],notes:'A peaceful schooler with a dark triangular flank patch.'});
  fish('platy','Platy','fresh',80,6,60,6,'#ec9b43','spots',{secondary:'#ad5039',ph:[7,8.2],reproduction:'livebearer',incubation:120,life:3,maxLife:5,notes:'Hard-water livebearer. Young benefit from planted refuge.'});
  fish('angel','Freshwater angelfish','fresh',210,15,150,19,'#dfd9b2','bars',{shape:'angel',secondary:'#4c535f',aggression:0.45,predator:0.3,temp:[25,29],ph:[6,7.5],level:3,life:8,maxLife:12,notes:'Tall, territorial cichlid. Small tetras and fry may be eaten.'});
  fish('pleco','Bristlenose pleco','fresh',185,13,150,20,'#827660','spots',{shape:'bottom',secondary:'#c4b786',zone:0.91,diet:['algae','sinking'],nocturnal:true,life:8,maxLife:12,level:2,notes:'Grazing bottom-dweller. Needs wood, caves and plant-rich food.'});
  fish('clown','Ocellaris clownfish','marine',180,9,75,12,'#f2a34b','clown',{scientificName:'Amphiprion ocellaris',secondary:'#f1e6c8',aggression:0.3,habitat:'rocks',reproduction:'pair',incubation:144,life:10,maxLife:16,notes:'Protandrous pair strategy: the larger established individual becomes female. No anemone required in this game.'});
  fish('gramma','Royal gramma','marine',230,8,110,12,'#b476d2','half',{secondary:'#f0c94c',aggression:0.4,habitat:'caves',notes:'Purple forebody and yellow tail. Defends a small rock shelter.'});
  fish('firefish','Firefish','marine',170,8,75,8,'#e4ddd1','fire',{shape:'dart',secondary:'#ce5864',activity:0.7,habitat:'caves',notes:'Shy dartfish. Rock shelter helps it retreat from boisterous tankmates.'});
  fish('watchman','Yellow watchman goby','marine',210,10,110,13,'#d9bb4a','spots',{shape:'bottom',secondary:'#7ad5cb',zone:0.86,habitat:'caves',diet:['frozen','sinking'],notes:'Bottom-dwelling goby with blue spotting and a burrow territory.'});
  fish('banggai','Banggai cardinalfish','marine',245,8,110,11,'#d2d6c8','bars',{shape:'cardinal',secondary:'#414753',activity:0.55,habitat:'rocks',reproduction:'mouthbrood',incubation:168,notes:'Male mouthbrooder. This build uses a compressed, protected brood phase.'});
  fish('chromis','Blue-green chromis','marine',120,9,150,10,'#77cfbb','plain',{secondary:'#549cb9',group:5,activity:1.4,habitat:'open',notes:'Active social damselfish. Group requirements and space are enforced.'});
  fish('yellowtang','Yellow tang','marine',520,20,500,35,'#edca4d','plain',{shape:'tang',secondary:'#f8e090',diet:['algae','pellets'],aggression:0.45,activity:1.5,habitat:'open',level:5,life:15,maxLife:25,notes:'Large active grazer. A long, spacious aquarium is essential.'});
  fish('sixline','Six-line wrasse','marine',290,10,150,16,'#c68bad','stripes',{shape:'slim',secondary:'#d49d43',aggression:0.6,activity:1.6,habitat:'rocks',level:3,notes:'Active, potentially aggressive rock forager. Avoid timid companions.'});
  fish('blenny','Tailspot blenny','marine',195,6,75,8,'#d5a26c','tailspot',{shape:'bottom',secondary:'#79a6ae',zone:0.75,diet:['algae','pellets'],habitat:'caves',notes:'Small grazing blenny with a dark spot at the base of its tail.'});
  fish('marinebetta','Marine betta','marine',480,20,300,30,'#576c97','spots',{shape:'betta',secondary:'#d7d3c4',aggression:0.35,predator:0.65,nocturnal:true,diet:['frozen','predator'],habitat:'caves',level:4,life:12,maxLife:20,notes:'Shy nocturnal predator. Small fish and fry can be eaten.'});
  fish('voidfin','Voidfin specter','marine',900,16,300,29,'#9b83df','glow',{shape:'angel',secondary:'#6ee2d4',nocturnal:true,habitat:'caves',level:4,rarity:'Fictional contraband',fictional:true,aggression:0.5,predator:0.4,notes:'FICTIONAL. Bright light causes stress. Requires containment; inspections can confiscate it.'});
  fish('glassfang','Glassfang eel','fresh',1100,35,500,45,'#83c5b3','glow',{shape:'eel',secondary:'#d9f3bf',nocturnal:true,habitat:'caves',level:5,rarity:'Fictional contraband',fictional:true,aggression:0.8,predator:0.9,diet:['predator','frozen'],notes:'FICTIONAL ambush predator. High hunger triggers attacks; requires reinforced containment.'});
  const sizes=[{volume:20,name:'Nano',price:220,level:1},{volume:40,name:'Small',price:330,level:1},{volume:75,name:'Starter',price:450,level:1},{volume:150,name:'Community',price:900,level:2},{volume:300,name:'Gallery',price:1850,level:3},{volume:500,name:'Showcase',price:3200,level:4},{volume:1000,name:'Grand aquarium',price:6200,level:6},{volume:2500,name:'Public exhibit',price:14000,level:8},{volume:5000,name:'Ocean hall',price:27000,level:10}];
  const equipment={
    filter:{name:'Biological filter',price:180,capacity:150,watts:8,description:'Processes ammonia and nitrite once bacteria establish.'},
    heater:{name:'Thermostatic heater',price:110,capacity:150,watts:50,description:'Gradually brings water toward the chosen temperature.'},
    light:{name:'Planted LED',price:95,capacity:150,watts:14,description:'Scheduled light supports plants and soft corals.'},
    air:{name:'Air pump',price:65,capacity:200,watts:4,description:'Increases gas exchange and dissolved oxygen.'},
    skimmer:{name:'Protein skimmer',price:280,capacity:300,watts:12,water:'marine',description:'Removes marine organic waste before it decomposes.'},
    reefLight:{name:'Reef spectrum LED',price:340,capacity:300,watts:40,water:'marine',description:'High intensity light for demanding corals.'},
    flow:{name:'Circulation pump',price:130,capacity:300,watts:8,description:'Water flow supports corals and oxygen exchange.'},
    feeder:{name:'Automatic feeder',price:240,capacity:300,watts:2,description:'Feeds once daily at 09:00 from your chosen food stock.'},
    chiller:{name:'Water chiller',price:350,capacity:300,watts:70,description:'Cools a warm tank toward your temperature target.'},
    dosing:{name:'Reef dosing unit',price:330,capacity:300,watts:3,water:'marine',description:'Restores calcium, magnesium and alkalinity using reef buffer.'},
    containment:{name:'Reinforced containment',price:450,capacity:1000,watts:6,description:'Required for fictional contraband; reduces escape and inspection risk.'}
  };
  const foods={flakes:{name:'Community flakes',price:18,protein:0.45,plant:0.35,quality:0.85,particle:1,pollution:0.6},pellets:{name:'Balanced pellets',price:24,protein:0.5,plant:0.3,quality:0.9,particle:2,pollution:0.7},sinking:{name:'Sinking wafers',price:22,protein:0.4,plant:0.4,quality:0.9,particle:2,pollution:0.6},algae:{name:'Algae wafers',price:20,protein:0.25,plant:0.7,quality:0.9,particle:2,pollution:0.5},frozen:{name:'Frozen mysis',price:32,protein:0.65,plant:0.05,quality:1,particle:1,pollution:0.9},fry:{name:'Fine fry food',price:28,protein:0.6,plant:0.2,quality:1,particle:0.1,pollution:0.8},predator:{name:'Predator ration',price:45,protein:0.8,plant:0,quality:0.95,particle:4,pollution:1.1}};
  const coralCare={temperature:[24,28],salinity:[33,36],maxNitrate:20,minCalcium:390,minMagnesium:1200,alkalinity:[7,10],stingDistance:0.05};
  const flora={
    fern:{name:'Java fern',water:'fresh',price:45,color:'#508c65',shape:'fern',light:0.25,growth:0.016,habitat:'plants'},
    anubias:{name:'Anubias',water:'fresh',price:55,color:'#68976b',shape:'leaf',light:0.2,growth:0.009,habitat:'plants'},
    sword:{name:'Amazon sword',water:'fresh',price:70,color:'#7aa479',shape:'sword',light:0.45,growth:0.02,habitat:'plants'},
    moss:{name:'Java moss',water:'fresh',price:35,color:'#699c70',shape:'moss',light:0.2,growth:0.02,habitat:'plants'},
    vallis:{name:'Vallisneria',water:'fresh',price:55,color:'#719d69',shape:'grass',light:0.4,growth:0.022,habitat:'plants'},
    crypt:{name:'Cryptocoryne',water:'fresh',price:65,color:'#aa9271',shape:'leaf',light:0.3,growth:0.014,habitat:'plants'},
    zoa:{name:'Garden zoanthids',water:'marine',price:130,color:'#d9a576',shape:'zoa',light:0.45,growth:0.012,flow:0.3,habitat:'corals'},
    mushroom:{name:'Mushroom coral',water:'marine',price:110,color:'#a295c4',shape:'mushroom',light:0.3,growth:0.01,flow:0.2,habitat:'corals'},
    sps:{name:'Branching SPS',water:'marine',price:260,color:'#82c9bf',shape:'branch',light:0.8,growth:0.008,flow:0.7,habitat:'corals'},
    lps:{name:'Hammer LPS',water:'marine',price:220,color:'#adcba0',shape:'lps',light:0.55,growth:0.008,flow:0.4,habitat:'corals'},
    soft:{name:'Soft leather coral',water:'marine',price:160,color:'#cc9d9b',shape:'soft',light:0.4,growth:0.013,flow:0.35,habitat:'corals'}
  };
  const supplies={conditioner:{name:'Water conditioner',price:20,amount:10,description:'One dose prepares a freshwater water change.'},salt:{name:'Marine salt mix',price:35,amount:10,description:'One dose prepares a salinity-matched water change.'},medicine:{name:'Broad treatment',price:65,amount:3,description:'Treats the simplified stress-related infection model.'},buffer:{name:'Reef buffer',price:40,amount:10,description:'Restores consumed reef minerals.'}};
  const quests=[
    ['prepare','A safe beginning','Prepare your first aquarium.', 'prepared',1,120,[]],
    ['cycle','The invisible gardeners','Establish a biological filter in any tank. Fishless cycling takes 36 simulated hours.', 'cycled',1,180,['prepare']],
    ['residents','Life moves in','Purchase your first compatible fish.', 'bought',1,150,['cycle']],
    ['feed','Dinner in the shallows','Feed your residents suitable food.', 'fed',1,90,['residents']],
    ['water','A fresh start','Perform a prepared partial water change.', 'waterChanges',1,100,['prepare']],
    ['plant','Room to hide','Add three live plants or corals.', 'floraBought',3,200,['prepare']],
    ['keeper','Water keeper','Maintain safe, occupied water for three consecutive days.', 'safeDays',3,320,['residents']],
    ['community','Peaceful company','Keep at least six healthy fish with low stress for five consecutive days.', 'peaceDays',5,450,['keeper']],
    ['upgrade','Better by design','Purchase two equipment upgrades.', 'equipmentBought',2,180,['residents']],
    ['expand','A second little world','Own a second aquarium.', 'tankCount',2,350,['residents']],
    ['pair','A new generation','Start a viable brood from a compatible pair.', 'broods',1,250,['residents']],
    ['hatch','First hatch','Raise your first viable offspring.', 'hatched',1,400,['pair']],
    ['breeder','Small beginnings','Raise five offspring into juveniles.', 'raised',5,700,['hatch']],
    ['reef','Into the reef','Keep three healthy coral colonies in a reef aquarium.', 'healthyCorals',3,600,['expand']],
    ['collection','Living colors','Discover eight different species.', 'discovered',8,500,['residents']],
    ['trade','A fair exchange','Sell a healthy, legal fish to a local buyer.', 'sold',1,160,['residents']],
    ['market','After dark','Reach keeper level 4 and discover the fictional night market.', 'nightMarket',1,200,['keeper']],
    ['magnate','The living gallery','Reach 10,000 AC in aquarium assets.', 'assets',10000,1000,['expand']],
    ['season','A seasonal sanctuary','Place a seasonal lantern in an aquarium.', 'seasonDecor',1,100,['plant']]
  ].map(([id,title,description,stat,target,reward,prerequisites])=>({id,title,description,stat,target,reward,prerequisites}));
  return {species,sizes,equipment,foods,flora,coralCare,supplies,quests};
})();
