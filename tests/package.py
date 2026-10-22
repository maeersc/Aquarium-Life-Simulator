"""Create a portable release without browser profiles or development caches."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

root = Path(__file__).resolve().parent.parent
files = [*root.glob('*.html'), *root.glob('*.md'), *root.glob('*.py'),
         *root.glob('css/*.css'), *root.glob('js/*.js'),
         *[p for p in (root / 'assets').rglob('*') if p.is_file()]]
for path in (root/'tests').iterdir():
    if path.is_file() and path.suffix.lower() in {'.html','.js','.py','.json','.png'}:
        files.append(path)
for folder in ['audit-evidence','economy-evidence','ui-overhaul-evidence','gameplay-evidence','ecosystem-evidence','expansion-evidence','pages-evidence','diving-evidence','update29-evidence','update33-evidence','update34-evidence','overnight-evidence','heater-evidence','layout-cleanup-evidence','store-casino-evidence','breeding-evidence','mystery-diving-evidence','receiving-evidence','global-receiving-evidence','diving-expansion-evidence','preparation-evidence','location-art-evidence','fish-animation-evidence']:
    for path in (root/'tests'/folder).glob('*'):
        if path.is_file() and path.suffix.lower() in {'.json','.png'}:
            files.append(path)

files.extend(p for p in (root/'tests/tutorial-audit-evidence').glob('*') if p.is_file() and p.suffix.lower() in {'.json','.png'})
files.extend(p for p in (root/'tests/tutorial-evidence').glob('*') if p.is_file() and p.suffix.lower() in {'.json','.png'})
files.extend(p for p in (root/'tests/simplification-evidence').glob('*') if p.is_file() and p.suffix.lower() in {'.json','.png'})
files.extend(p for p in (root/'tests/economy-update-evidence').glob('*') if p.is_file() and p.suffix.lower() in {'.json','.png'})
files.extend(p for p in (root/'tests/inventory-evidence').glob('*') if p.is_file() and p.suffix.lower() in {'.json','.png'})
files.extend(p for p in (root/'tests/equipment-reliability-evidence').glob('*') if p.is_file() and p.suffix.lower() in {'.json','.png'})
files.extend(p for p in (root/'tests/livestock16-evidence').glob('*') if p.is_file() and p.suffix.lower() in {'.json','.png'})
files.extend(p for p in (root/'tests/sprite-production-evidence').glob('*') if p.is_file() and p.suffix.lower() in {'.json','.png'})
files.extend(p for p in (root/'tests/performance-evidence').glob('*') if p.is_file() and p.suffix.lower() in {'.json','.png'})
files.extend(p for p in (root/'tests/ui-quantity-evidence').glob('*') if p.is_file() and p.suffix.lower() in {'.json','.png'})
files.extend(p for p in (root/'tests/distribution-protection-evidence').rglob('*') if p.is_file() and p.suffix.lower() in {'.json','.png','.webm'})
files.extend(p for p in (root/'tools/production').glob('*') if p.is_file() and p.suffix.lower() in {'.py','.cjs','.json','.md'})
files.extend(p for p in (root/'planning').rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix.lower() not in {'.pyc','.pyo'})
archive = root / 'AquariumLife-v0.1.zip'
with ZipFile(archive, 'w', ZIP_DEFLATED) as output:
    for path in files:
        output.write(path, 'AquariumLife/' + path.relative_to(root).as_posix())
with ZipFile(archive) as output:
    assert output.testzip() is None
    assert 'AquariumLife/index.html' in output.namelist()
    assert not any('profile' in name or '__pycache__' in name for name in output.namelist())
print(f'{archive.name}: {len(files)} verified files, {archive.stat().st_size:,} bytes')
