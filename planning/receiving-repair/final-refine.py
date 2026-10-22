from pathlib import Path
r=Path(__file__).resolve().parents[2]
def edit(n,a,b):
 p=r/n;s=p.read_text(encoding='utf8');assert a in s,(n,a[:60]);p.write_text(s.replace(a,b,1),encoding='utf8')
edit('tests/receiving_checks.js',"d.water==='marine'&&d.predator>.7&&d.size>20", "d.water==='marine'&&!d.fictional&&d.predator>0&&d.size>AL.Data.species['chalk-bass'].size/.45")
edit('js/diving-ui.js',"const receivingChoices=new Map();", "const receivingChoices=new Map();let receivingOwner=null;")
edit('js/diving-ui.js',"function receivingPanel(o){const rows=", "function receivingPanel(o){if(receivingOwner!==AL.game.worldId){receivingChoices.clear();receivingOwner=AL.game.worldId;}const rows=")
edit('tests/pages_qa.py',"        results.extend(c.evaluate((root/'tests/mystery_diving_checks.js').read_text(encoding='utf8'))['checks'])", "        results.extend(c.evaluate((root/'tests/mystery_diving_checks.js').read_text(encoding='utf8'))['checks'])\n        check('Built receiving repair exposes all destinations and exact compatibility checks', '!!AL.DiveReceiving&&!!AL.DiveReceiving.destinations&&!!AL.DiveReceiving.holding')\n        results.extend(c.evaluate((root/'tests/receiving_checks.js').read_text(encoding='utf8'))['checks'])")
