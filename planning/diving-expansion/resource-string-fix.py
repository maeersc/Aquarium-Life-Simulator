from pathlib import Path
p=Path(__file__).resolve().parents[2]/'js/diving-ui.js';s=p.read_text(encoding='utf8');old="return '<p>Click a nearby discovery to inspect it. Only objects within one map step can be recovered. Collection uses no ${a.remote?'battery':'oxygen'}.</p>';";assert old in s;s=s.replace(old,"return `<p>Click a nearby discovery to inspect it. Only objects within one map step can be recovered. Collection uses no ${a.remote?'battery':'oxygen'}.</p>`;");p.write_text(s,encoding='utf8')
print('Fixed template quoting in the remote resource message.')
