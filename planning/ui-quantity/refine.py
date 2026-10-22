from pathlib import Path
R=Path(__file__).resolve().parents[2]
def edit(f,a,b):
 p=R/f;s=p.read_text(encoding='utf8');assert a in s,(f,a);p.write_text(s.replace(a,b,1),encoding='utf8')
edit('js/store.js',"label=r.ok?'Suitable destination':'Choose a suitable aquarium'","label=r.ok?'Suitable destination':'Review purchase requirements'")
edit('js/store.js',"?'Catalog content hold':'Incompatible destination'","?'Catalog content hold':'Purchase unavailable'")
p=R/'js/core.js';p.write_text(p.read_text(encoding='utf8').replace('stock(s,a.type,n);','stock(s,a.type);'),encoding='utf8')
edit('js/store-rules.js',"available=s.medicineStock[a.product]??0;if(p&&!p.restricted)","available=s.medicineStock[a.product]??0;if(p?.restricted){available=Math.min(available,AL.LivestockMarket.listing(s,'medicine:'+a.product)?.remaining??0);room=80-s.medicalInventory.length;}if(p&&!p.restricted)")
edit('js/store-rules.js',"room=d?Math.floor((1e7-(s.inventory[a.type]||0))/(action==='buyFood'?20:d.amount)):0;}","room=d?Math.floor((1e7-(s.inventory[a.type]||0))/(action==='buyFood'?20:d.amount)):0;if(action==='buySupply'&&/^frag-(kit|cutters|saw)$/.test(a.type||'')&&s.inventory[a.type]>0)reasons.push('Reusable tool already owned.');}")
edit('js/finance.js',"if(r.amount<0&&/buyFish|", "if(r.amount<0&&['buyEquipment','buyRock'].includes(context.action)){const old=new Set([...(previous.ownedEquipment||[]),...(previous.ownedObjects||[]),...previous.tanks.flatMap(t=>t.hardscape||[])].map(o=>o.id));r.itemIds=[...(s.ownedEquipment||[]),...(s.ownedObjects||[]),...s.tanks.flatMap(t=>t.hardscape||[])].filter(o=>!old.has(o.id)).map(o=>o.id);}if(r.amount<0&&/buyFish|")
