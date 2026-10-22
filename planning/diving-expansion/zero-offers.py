from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def edit(name,old,new):
 p=ROOT/name;s=p.read_text(encoding='utf8');assert old in s,(name,old[:80]);p.write_text(s.replace(old,new),encoding='utf8')
edit('js/diving-expansion.js',"return {ok:offer>0,value,offer,assessment:a,reason:offer>0?'Regular Aquarium Store liquidation; no Deep Market reputation.':'No positive eligible offer.'};", "return {ok:true,value,offer,assessment:a,reason:'Regular Aquarium Store liquidation; no Deep Market reputation. Offers may round down to zero AC.'};")
edit('js/diving-expansion.js',"{key,name:'Emergency Sale — '", "{key,allowZero:true,action:'diveEmergencySale',name:'Emergency Sale — '")
edit('js/diving-expansion.js',"o.recovery.saleAmount<=0", "o.recovery.saleAmount<0")
edit('js/finance.js',"if(!amount)return null;", "if(!amount&&!(details.allowZero===true&&details.action==='diveEmergencySale'))return null;")
edit('js/finance.js',"kind:amount>0?'income':'expense'", "kind:amount>=0?'income':'expense'")
edit('js/finance.js',"!integer(r.amount)||!r.amount||", "!integer(r.amount)||!r.amount&&!(r.allowZero===true&&r.action==='diveEmergencySale')||")
edit('js/finance.js',"r.kind!==(r.amount>0?'income':'expense')", "r.kind!==(r.amount>=0?'income':'expense')")
edit('tests/diving_expansion_checks.js',"const rockFixture=()=>{let s=K.act(diveFixture(),", "const rockFixture=()=>{const initial=diveFixture();initial.tanks[0].hardscape=[];let s=K.act(initial,")
print('Preserved zero-floor emergency offers with one auditable zero-AC income receipt.')
