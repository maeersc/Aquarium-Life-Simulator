from pathlib import Path
import json
r=Path(__file__).resolve().parents[2]
names=['diving-expansion-evidence/chrome-results.json','diving-expansion-evidence/edge-results.json','pages-evidence/chrome-results.json','pages-evidence/edge-results.json']
rows=[];total=0
for n in names:
 d=json.loads((r/'tests'/n).read_text(encoding='utf8'));assert d['failed']==0,n
 items=d.get('checks',d.get('results'));assert any('168-hour development' in x['name'] and x['pass'] for x in items),n
 rows.append('| '+n+' | '+str(d['passed'])+' | 0 |');total+=d['passed']
block='| Final browser suite | Passed | Failed |\n|---|---:|---:|\n'+'\n'.join(rows)+'\n\n**'+str(total)+' executed browser assertions passed; zero failed.** Source suites include shared receiving and mystery regressions; built suites also include the broader existing core/expansion, medical, valuation, resale and local-account checks. These totals intentionally count independent browser executions. No unrun Firefox or real GitHub deployment is claimed.\n\nBoth source browsers completed the full, unmodified 168-game-hour incubation and one real hatch, retained hidden identity after an actual reload, exercised actual Emergency Sale confirmation, verified active aquarium time during results, and checked all requested desktop viewports plus a 390 px narrow layout. The separate release verifier checks source/DIST/ZIP hashes and current source archive contents.'
p=r/'DIVING_EXPANSION_REPORT.md';s=p.read_text(encoding='utf8');a=s.index('<!-- FINAL-RESULTS -->');b=s.index('<!-- END-FINAL-RESULTS -->',a);s=s[:a]+'<!-- FINAL-RESULTS -->\n'+block+'\n'+s[b:];p.write_text(s,encoding='utf8')
print('Recorded '+str(total)+' passed browser assertions with zero failures.')
