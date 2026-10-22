"""Require an independently regenerated manifest and Pages ZIP to be byte-identical."""
from pathlib import Path
import hashlib,json,subprocess,sys
R=Path(__file__).resolve().parents[2];E=R/'tests/distribution-protection-evidence'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
manifest=R/'DIST/build-manifest.json';archive=R/'AquariumLife-GitHub-Pages.zip'
before={'manifestSha256':sha(manifest),'zipSha256':sha(archive),'buildId':json.loads(manifest.read_text())['buildId']}
subprocess.run([sys.executable,str(R/'build.py')],cwd=R,check=True)
after={'manifestSha256':sha(manifest),'zipSha256':sha(archive),'buildId':json.loads(manifest.read_text())['buildId']}
result={**after,'passed':before==after,'before':before,'method':'Second build process, same pinned tools/sources; exact manifest and complete compressed ZIP hashes.'}
(E/'reproducibility.json').write_text(json.dumps(result,indent=2),encoding='utf8')
if not result['passed']:raise RuntimeError('Protected output is not reproducible')
print(json.dumps(result,indent=2))
