"use strict";
// Sole source of casino probabilities, payouts and fictional card mechanics.
AL.CasinoRules=(()=>{
 const symbols=Object.freeze([{id:'blue',name:'Blue Reef Fish',weight:4},{id:'clown',name:'Clownfish',weight:3},{id:'reef',name:'Reef Angelfish',weight:2},{id:'gold',name:'Gold Fish',weight:1}].map(Object.freeze));
 const cards=Object.freeze([
  {species:'clown',role:'Reef shelter',attack:2,defense:5,trait:'shelter'},
  {species:'gramma',role:'Reef shelter',attack:4,defense:4,trait:'shelter'},
  {species:'watchman',role:'Reef shelter',attack:3,defense:6,trait:'shelter'},
  {species:'blenny',role:'Grazer',attack:2,defense:6,trait:'forage'},
  {species:'marinebetta',role:'Hunter',attack:7,defense:3,trait:'surge'},
  {species:'yellowtang',role:'Grazer',attack:4,defense:4,trait:'forage'}
 ].map(Object.freeze));
 const maxBet=1000,version=1,payouts=Object.freeze({gold:Object.freeze({gold:25,triple:3,pair:1,loss:0}),predator:Object.freeze({win:2,draw:1,loss:0})}),traits=Object.freeze({shelter:Object.freeze({opponent:'Hunter',bonus:2}),forage:Object.freeze({opponent:'Reef shelter',bonus:1}),surge:Object.freeze({opponent:'Grazer',bonus:2})});
 function symbol(n){if(!Number.isInteger(n)||n<0||n>=10)throw Error('Invalid symbol draw.');let total=0;return symbols.find(s=>(total+=s.weight)>n);}
 function gold(draws){const a=draws.map(n=>symbol(n).id),count=new Set(a).size;return count===1?{outcome:a[0]==='gold'?'gold':'triple',reason:a[0]==='gold'?'Three Gold Fish!':'Three matching fish.'}:count===2?{outcome:'pair',reason:'Two matching fish: wager returned.'}:{outcome:'loss',reason:'Three different fish.'};}
 function score(a,b){const trait=traits[a.trait],bonus=trait?.opponent===b.role?trait.bonus:0;return {total:a.attack+a.defense+bonus,bonus};}
 function predator(draws){const a=cards[draws[0]],b=cards[draws[1]];if(!a||!b)throw Error('Invalid card draw.');const player=score(a,b),dealer=score(b,a),outcome=player.total===dealer.total?'draw':player.total>dealer.total?'win':'loss';return {outcome,player,dealer,reason:(outcome==='draw'?'Draw':outcome==='win'?'Player wins':'Dealer wins')+' — fictional card score '+player.total+' vs '+dealer.total+'. Attack + defense + matchup bonus; not a scientific predator/prey claim.'};}
 function resolve(game,draws,wager){if(!Array.isArray(draws)||draws.length!==(game==='gold'?3:game==='predator'?2:0)||draws.some(n=>!Number.isInteger(n)||n<0||n>=(game==='gold'?10:cards.length)))throw Error('Invalid casino game or draws.');const result=game==='gold'?gold(draws):predator(draws),multiplier=payouts[game][result.outcome];return {...result,multiplier,payout:multiplier*wager};}
 function probabilities(game){const counts={},total=game==='gold'?1000:cards.length**2;let returned=0;
  if(game==='gold'){for(let a=0;a<10;a++)for(let b=0;b<10;b++)for(let c=0;c<10;c++){const r=resolve(game,[a,b,c],1);counts[r.outcome]=(counts[r.outcome]||0)+1;returned+=r.payout;}}
  else if(game==='predator'){for(let a=0;a<cards.length;a++)for(let b=0;b<cards.length;b++){const r=resolve(game,[a,b],1);counts[r.outcome]=(counts[r.outcome]||0)+1;returned+=r.payout;}}
  else throw Error('Unknown casino game.');return {counts,total,returnRate:returned/total};
 }
 function bounded(n){if(!globalThis.crypto?.getRandomValues)throw Error('Secure local randomness is unavailable; wagering is disabled.');const data=new Uint32Array(1),ceiling=Math.floor(4294967296/n)*n;do{crypto.getRandomValues(data);}while(data[0]>=ceiling);return data[0]%n;}
 function draw(game){if(!['gold','predator'].includes(game))throw Error('Unknown casino game.');return Array.from({length:game==='gold'?3:2},()=>bounded(game==='gold'?10:cards.length));}
 return {symbols,cards,maxBet,version,payouts,traits,symbol,score,resolve,probabilities,draw};
})();
