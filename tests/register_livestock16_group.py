"""Register a batch only from recorded, explicit per-sheet agent inspection notes."""
import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
for review in json.loads(Path(sys.argv[1]).read_text(encoding='utf8')):
    assert review.get('all16NativeCellsInspected') is True and review.get('sourceReferenceInspected') is True
    command=[sys.executable,str(ROOT/'tests/register_livestock16_production.py'),review['id'],review['stage'],'--review-notes',review['notes']]
    if review.get('variety'):command+=['--variety',review['variety']]
    if review.get('state'):command+=['--state',review['state']]
    subprocess.run(command,cwd=ROOT,check=True)
