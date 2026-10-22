from pathlib import Path
r=Path(__file__).resolve().parents[2]
def edit(n,a,b):
 p=r/n;s=p.read_text(encoding='utf8');assert a in s,(n,a[:50]);p.write_text(s.replace(a,b,1),encoding='utf8')
edit('tests/receiving_checks.js',"t.temperatureTarget=27;return s;", "t.temperatureTarget=27;const o=s.diving.history[0].objects[0];o.recovery.roll=0;o.recovery.conditionRoll=85;AL.Valuation.invalidate(s);return s;")
edit('tests/receiving_checks.js',"o.recovery.roll=0;o.recovery.conditionRoll=85;return K.act(s", "return K.act(s")
edit('tests/receiving_checks.js',"AL.Save.validate(s);return rows.length===3", "AL.Mortality.migrate(s);AL.Breeding.migrate(s);AL.MarineCare.migrate(s);AL.Update29.migrate(s);AL.Save.validate(s);return rows.length===3")
edit('tests/receiving_checks.js',"K.fish(s,'lion')", "K.fish(s,Object.values(AL.Data.species).find(d=>d.water==='marine'&&d.predator>.7&&d.size>20).id)")
p=r/'js/diving-ui.js';s=p.read_text(encoding='utf8');a=s.index(' function refreshReceiving()');b=s.index(' function currentValue(',a)
s=s[:a]+''' function refreshReceiving(){for(const panel of document.querySelectorAll('[data-receiving-panel]')){
  const o=AL.game.diving.history[0]?.objects.find(o=>o.objectId===panel.dataset.receivingPanel);if(!o||o.recovery.status!=='pending')continue;
  const holding=panel.querySelector('[data-dive-holding]');if(holding)holding.textContent=AL.DiveReceiving.holding(AL.game,o).text;
  const rows=AL.DiveReceiving.destinations(AL.game,o.species),signature=JSON.stringify(rows.map(x=>[x.tank.id,x.tank.name,x.tank.volume,x.tank.kind,x.tank.water,x.report.checks,x.report.warnings]));if(panel.dataset.signature===signature)continue;
  const open=new Set([...panel.querySelectorAll('details[open]')].map(d=>d.dataset.receivingTank)),top=$('dialog').scrollTop,active=document.activeElement,focusTank=active?.closest('[data-receiving-tank]')?.dataset.receivingTank;
  const temp=document.createElement('div');temp.innerHTML=receivingPanel(o);const oldSelect=panel.querySelector('select'),freshSelect=temp.querySelector('select'),value=receivingChoices.get(o.objectId)||oldSelect.value;
  // Retain the select node itself: live measurements must not dismiss a native
  // dropdown, lose keyboard focus or silently choose a different aquarium.
  if(oldSelect.innerHTML!==freshSelect.innerHTML){oldSelect.innerHTML=freshSelect.innerHTML;const valid=[...oldSelect.options].some(x=>x.value===value&&!x.disabled);oldSelect.value=valid?value:'';}
  const oldChildren=[...panel.children],freshChildren=[...temp.children];for(let i=1;i<freshChildren.length;i++){if(oldChildren[i])oldChildren[i].replaceWith(freshChildren[i]);else panel.append(freshChildren[i]);}for(let i=freshChildren.length;i<oldChildren.length;i++)oldChildren[i].remove();
  panel.dataset.signature=signature;for(const d of panel.querySelectorAll('details')){if(open.has(d.dataset.receivingTank))d.open=true;if(d.dataset.receivingTank===focusTank)d.querySelector('summary')?.focus({preventScroll:true});}if(active?.matches('[data-dive-action=recover]'))panel.querySelector('[data-dive-action=recover]')?.focus({preventScroll:true});$('dialog').scrollTop=top;
 }}
''' +s[b:];p.write_text(s,encoding='utf8')
