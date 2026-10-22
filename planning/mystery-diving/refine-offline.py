from pathlib import Path
p=Path(__file__).resolve().parents[2]/'js/overnight-ui.js'
s=p.read_text(encoding='utf8');old="function events(list){return list.map(e=>`<details>";assert old in s
s=s.replace(old,"function events(list){return list.map(e=>e.context==='diving-transport'?`<details><summary>${esc(e.name)} · ${AL.Clock.stamp(e.time)} · Expedition transport loss</summary><p>${esc(e.cause)}. ${esc(e.confidence)}.</p><p>${esc(e.evidenceLimit)} Diver oxygen is not transport-water oxygen. Full expedition evidence is retained in Livestock Deaths.</p></details>`:`<details>",1)
p.write_text(s,encoding='utf8')
