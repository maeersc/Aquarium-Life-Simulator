from pathlib import Path
r=Path(__file__).resolve().parents[2]
def edit(n,old,new):
 p=r/n;s=p.read_text(encoding='utf8');assert old in s,(n,old[:65]);p.write_text(s.replace(old,new,1),encoding='utf8')
edit('js/mortality-journal.js',"ctx=contexts.get(s);s.mortality.next++;\n  const e={id,schemaVersion:3", "ctx=contexts.get(s),sequence=s.mortality.next++;\n  const e={id,sequence,schemaVersion:3")
edit('js/mortality-journal.js',"conditionRoll:r.conditionRoll,receivingTank:o.receivingTank??null", "conditionRoll:r.conditionRoll,survivalChance:o.survivalChance??null,assessmentElapsedGameHours:Math.max(0,time-h.started)/60,receivingTank:o.receivingTank??null")
edit('js/diving-ui.js',"glint=null,revealStarted=0,releaseChoice=null;", "glint=null,revealStarted=0,releaseChoice=null,resultFingerprint='';")
edit('js/diving-ui.js',"function results(){const h=AL.game.diving.history[0];", "function resultSignature(){return JSON.stringify(AL.game.diving.history[0]?.objects.map(o=>[o.objectId,o.recovery?.status,o.condition]));}\n function results(){resultFingerprint=resultSignature();const h=AL.game.diving.history[0];")
edit('js/diving-ui.js',"Current estimated asset value: ${currentValue(o)} AC", "Current estimated asset value: <span data-dive-current-value=\"${esc(o.objectId)}\">${currentValue(o)}</span> AC")
edit('js/diving-ui.js',"function update(){if(!owned)return;", "function update(){if(!owned)return;if(screen==='results'){if(resultFingerprint!==resultSignature()){render();return;}for(const el of document.querySelectorAll('[data-dive-current-value]')){const o=AL.game.diving.history[0]?.objects.find(o=>o.objectId===el.dataset.diveCurrentValue);if(o)el.textContent=currentValue(o);}}")
