"use strict";
AL.Casino=(()=>{
 const R=AL.CasinoRules,integer=Number.isSafeInteger;
 function migrate(s){if(!s?.accountId)return;s.casino??={version:1,accountId:s.accountId,next:1,pending:null,history:[],lifetimeWagered:0,lifetimePaid:0,dailyLimit:0,day:Math.floor(s.time/1440),dayWagered:0};}
 const id=s=>s.accountId+':casino:'+s.casino.next;
 function sequence(s,value){const prefix=s.accountId+':casino:';if(typeof value!=='string'||!value.startsWith(prefix)||!/^\d+$/.test(value.slice(prefix.length)))throw Error('Invalid casino round identity.');const n=Number(value.slice(prefix.length));if(!integer(n)||n<1||value!==prefix+n)throw Error('Invalid casino round identity.');return n;}
 function wager(s,a){migrate(s);const c=s.casino,n=sequence(s,a.id);if(n<c.next)return;if(n!==c.next)throw Error('Casino round sequence changed. Reopen confirmation.');if(c.pending)throw Error('Finish the saved round before wagering again.');
  const amount=a.wager;if(!integer(amount)||amount<1||amount>R.maxBet||amount>s.credits)throw Error('Wager must be 1–'+R.maxBet+' AC within your wallet balance.');if(a.confirmed!==true)throw Error('Confirm this wager first.');if(!['gold','predator'].includes(a.game))throw Error('Choose a casino game.');
  const today=Math.floor(s.time/1440);if(c.day!==today){c.day=today;c.dayWagered=0;}if(c.dailyLimit&&c.dayWagered+amount>c.dailyLimit)throw Error('Your optional daily wager limit would be exceeded.');if(s.credits-amount+amount*Math.max(...Object.values(R.payouts[a.game]))>1e9)throw Error('Leave wallet space for the maximum possible payout.');
  const draws=R.draw(a.game),receipt=AL.Finance.change(s,-amount,{category:'casino',action:'casinoWager',actionId:a.id+':wager',key:a.id+':wager',name:(a.game==='gold'?'Gold Fish':'Predator & Prey')+' wager',roundId:a.id,note:'Outcome committed locally at wager confirmation; rules v'+R.version});
  s.stats.expenses+=amount;c.pending={id:a.id,accountId:s.accountId,game:a.game,rulesVersion:R.version,wager:amount,draws,time:s.time,wagerTransaction:receipt.id};c.next++;c.dayWagered+=amount;c.lifetimeWagered+=amount;
 }
 function settle(s,a){migrate(s);const c=s.casino,n=sequence(s,a.id),p=c.pending;if(!p){if(n<c.next)return;throw Error('No matching pending round.');}if(p.id!==a.id){if(n<c.next-1)return;throw Error('Finish the current pending round.');}
  const result=R.resolve(p.game,p.draws,p.wager);if(s.credits+result.payout>1e9)throw Error('The wallet cap currently prevents this payout. Make room in your wallet before settlement.');let receipt=null;if(result.payout)receipt=AL.Finance.change(s,result.payout,{category:'casino',action:'casinoPayout',actionId:p.id+':payout',key:p.id+':payout',name:(p.game==='gold'?'Gold Fish':'Predator & Prey')+' '+result.outcome,roundId:p.id,note:result.reason});
  s.stats.earnings+=result.payout;c.lifetimePaid+=result.payout;c.history.push({...p,...result,settledAt:s.time,payoutTransaction:receipt?.id||null});c.history=c.history.slice(-100);c.pending=null;
 }
 function limit(s,a){migrate(s);if(!integer(a.limit)||a.limit<0||a.limit>1e9)throw Error('Daily wager limit must be a whole AC amount, or zero for no limit.');s.casino.dailyLimit=a.limit;}
 const headKey='aquarium-life-casino-heads-v1';
 function progress(s){const c=s.casino;return c?{next:c.next,settled:c.next-(c.pending?2:1)}:{next:1,settled:0};}
 function heads(){try{const h=JSON.parse(localStorage.getItem(headKey)||'{}');return h&&typeof h==='object'&&!Array.isArray(h)?h:{};}catch{return {};}}
 function importable(s){const h=heads()[s.accountId],p=progress(s);if(h&&((integer(h.next)&&h.next>p.next)||(integer(h.settled)&&h.settled>p.settled)))throw Error('This backup predates newer saved casino rounds for this local account. Use the latest save; the older file is preserved.');}
 function remember(s){if(!s.casino)return;try{const h=heads(),p=progress(s),old=h[s.accountId]||{};h[s.accountId]={next:Math.max(old.next||1,p.next),settled:Math.max(old.settled||0,p.settled)};localStorage.setItem(headKey,JSON.stringify(h));}catch{/* The committed main save still contains the authoritative round. */}}
 function validate(s){if(s.casino===undefined)return;const c=s.casino;if(c.version!==1||c.accountId!==s.accountId||!integer(c.next)||c.next<1||!Array.isArray(c.history)||c.history.length>100||![c.lifetimeWagered,c.lifetimePaid,c.dailyLimit,c.day,c.dayWagered].every(n=>integer(n)&&n>=0)||c.day>Math.floor(s.time/1440)||c.dailyLimit>1e9||c.dayWagered>c.lifetimeWagered)throw Error('Invalid casino account.');
  const seen=new Set();let last=0,total=0,paid=0;
  function round(p,settled){const n=sequence(s,p.id);if(n>=c.next||n<=last||seen.has(p.id)||p.accountId!==s.accountId||p.rulesVersion!==R.version||!integer(p.wager)||p.wager<1||p.wager>R.maxBet||!Number.isFinite(p.time)||p.time<0||p.time>s.time||!s.finance.keys.includes(p.id+':wager')||!/^.+:ac:\d+$/.test(p.wagerTransaction)||!p.wagerTransaction.startsWith(s.accountId+':ac:'))throw Error('Invalid casino round.');const result=R.resolve(p.game,p.draws,p.wager);seen.add(p.id);last=n;total+=p.wager;
   const wager=s.finance.rows.find(r=>r.id===p.wagerTransaction);if(wager&&(wager.amount!==-p.wager||wager.roundId!==p.id||wager.category!=='casino'||wager.key!==p.id+':wager'))throw Error('Casino wager receipt mismatch.');
   if(settled){if(p.outcome!==result.outcome||p.payout!==result.payout||p.multiplier!==result.multiplier||p.reason!==result.reason||!Number.isFinite(p.settledAt)||p.settledAt<p.time||p.settledAt>s.time)throw Error('Invalid casino settlement.');paid+=p.payout;if(p.payout){if(!s.finance.keys.includes(p.id+':payout')||typeof p.payoutTransaction!=='string'||!p.payoutTransaction.startsWith(s.accountId+':ac:'))throw Error('Missing casino payout receipt.');const r=s.finance.rows.find(r=>r.id===p.payoutTransaction);if(r&&(r.amount!==p.payout||r.roundId!==p.id||r.category!=='casino'||r.key!==p.id+':payout'))throw Error('Casino payout receipt mismatch.');}else if(p.payoutTransaction!==null)throw Error('Unexpected loss payout.');}
   else if(s.finance.keys.includes(p.id+':payout'))throw Error('Pending round already paid.');
  }
  for(const p of c.history)round(p,true);if(c.pending){round(c.pending,false);if(sequence(s,c.pending.id)!==c.next-1)throw Error('Invalid pending round sequence.');}if(total>c.lifetimeWagered||paid>c.lifetimePaid)throw Error('Invalid casino totals.');
 }
 return {migrate,id,wager,settle,limit,validate,importable,remember};
})();
