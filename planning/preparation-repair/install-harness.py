from pathlib import Path
r=Path(__file__).resolve().parents[2]
p=r/'tests/browser_qa.py';s=p.read_text(encoding='utf8');needle="        if '--diving-expansion' in sys.argv:";assert needle in s;s=s.replace(needle,"        if '--preparation' in sys.argv or '--preparation-baseline' in sys.argv:\n            import preparation_qa\n            return preparation_qa.run(client,ROOT,NAME,'--preparation-baseline' in sys.argv)\n"+needle);p.write_text(s,encoding='utf8')
