from pathlib import Path
r=Path(__file__).resolve().parents[2]
def edit(n,old,new):
 p=r/n;s=p.read_text(encoding='utf8');assert old in s;p.write_text(s.replace(old,new,1),encoding='utf8')
edit('tests/mystery_diving_checks.js',"t.equipment.forEach(e=>{if(e.id)e.id=K.id(s,'equipment');});", "const reidentify=obj=>{if(!obj||typeof obj!=='object')return;if(typeof obj.id==='string')obj.id=K.id(s,'fixture');for(const v of Object.values(obj))if(v&&typeof v==='object')reidentify(v);};reidentify(t);")
edit('tests/diving_checks.js',"s.xp=2400;s.level=13;", "s.update29.tutorial.status='skipped';s.xp=2400;s.level=13;")
edit('tests/mystery_diving_qa.py',"downloads=out/(name+'-downloads');downloads.mkdir(exist_ok=True)", "downloads=out/(name+'-downloads')/str(time.time_ns());downloads.mkdir(parents=True,exist_ok=True)")
