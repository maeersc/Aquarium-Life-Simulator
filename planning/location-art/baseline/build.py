"""Build the current static game into DIST using only Python's standard library.

Run: python build.py
Copies current runtime files, follows local asset references, removes stale build
files, verifies hashes/case-sensitive URLs, and zips DIST's contents for Pages.
Player/browser data and development test profiles are never build inputs.
"""
from collections import deque
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile, ZIP_DEFLATED
import hashlib
import json
import re
import shutil

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'DIST'
ARCHIVE = ROOT / 'AquariumLife-GitHub-Pages.zip'
ASSET_REFERENCE = re.compile(r'''(?:\.\./)?assets/[^\s"'`<>\\)]+''')
TEXT_SUFFIXES = {'.html', '.css', '.js', '.json', '.svg'}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative_file(path):
    resolved = path.resolve()
    if not resolved.is_relative_to(ROOT) or path.is_symlink():
        raise ValueError(f'Build input escapes workspace: {path}')
    return path.relative_to(ROOT).as_posix()


def check_case(path):
    """Windows tolerates the wrong case; GitHub Pages does not."""
    current = ROOT
    for part in path.relative_to(ROOT).parts:
        if part not in {p.name for p in current.iterdir()}:
            raise ValueError(f'Incorrect URL filename case: {path}')
        current /= part


class LocalLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('src', 'href') and value:
                parsed = urlsplit(value)
                if not parsed.scheme and not parsed.netloc and parsed.path:
                    if parsed.path.startswith('/'):
                        raise ValueError(f'Root-relative URL breaks repository Pages: {value}')
                    self.links.append(unquote(parsed.path))


def gather():
    # Classic scripts are already browser-ready; no Node, dependency downloads,
    # transpilation or art regeneration is necessary for a fresh deployment.
    pending = deque([*ROOT.glob('*.html'), *ROOT.glob('js/*.js'),
                     *ROOT.glob('css/*.css'), ROOT / 'GITHUB_PAGES.md',
                     ROOT / 'HEATER_MORTALITY_REPORT.md', ROOT / 'MORTALITY_LOG_SCHEMA.md',
                     ROOT / 'UI_LAYOUT_CLEANUP_REPORT.md', ROOT / 'STORE_CASINO_UPDATE_REPORT.md', ROOT / 'CASINO_RULES.md', ROOT / 'BREEDING_RULES.md', ROOT / 'BREEDING_SAVE_SCHEMA.md', ROOT / 'BREEDING_UPDATE_REPORT.md', ROOT / 'MYSTERY_DIVING_RULES.md', ROOT / 'MYSTERY_DIVING_UPDATE_REPORT.md', ROOT / 'DIVING_RECEIVING_REPAIR_REPORT.md', ROOT / 'GLOBAL_DIVING_RECEIVING_REPORT.md', ROOT / 'DIVING_EXPANSION_REPORT.md', ROOT / 'DIVING_EXPANSION_SAVE_SCHEMA.md', ROOT / 'AQUARIUM_PREPARATION_REPAIR_REPORT.md'])
    selected = {}
    while pending:
        path = pending.popleft()
        key = relative_file(path)
        if key in selected:
            continue
        if not path.is_file():
            raise FileNotFoundError(f'Missing deployment dependency: {key}')
        check_case(path)
        selected[key] = path
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        content = path.read_text(encoding='utf-8')
        if path.suffix == '.html':
            parser = LocalLinks()
            parser.feed(content)
            for link in parser.links:
                pending.append(path.parent / link)
        for match in ASSET_REFERENCE.finditer(content):
            candidate = ROOT / urlsplit(match.group().removeprefix('../')).path
            if candidate.is_file():
                pending.append(candidate)
            elif candidate.is_dir():
                # Covers dynamic paths such as 'assets/rarity/' + tier + '.svg'.
                pending.extend(p for p in candidate.rglob('*') if p.is_file())
    return selected


def build():
    # The regional ledger is authoritative; publish a fresh classic-script
    # representation without needing a JavaScript bundler or online fetch.
    ledger = ROOT / 'assets/diving/registry.json'
    if ledger.is_file():
        regions = json.loads(ledger.read_text(encoding='utf-8'))
        (ROOT / 'js/diving-data.js').write_text(
            '"use strict";\n// Generated from assets/diving/registry.json; edit the permanent registry.\n'
            + 'AL.DivingData=' + json.dumps(regions, separators=(',', ':')) + ';\n', encoding='utf-8')
    extension = ROOT / 'assets/expansion-v29/registry.json'
    if extension.is_file():
        data = json.loads(extension.read_text(encoding='utf-8'))
        (ROOT / 'js/update29-data.js').write_text('"use strict";\nAL.Update29Data=' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';\n', encoding='utf-8')
    if DIST.is_symlink() or DIST.resolve() != ROOT / 'DIST':
        raise ValueError('DIST must be a normal folder directly inside this workspace')
    selected = gather()
    if not selected or 'index.html' not in selected:
        raise ValueError('Missing game entry point')
    for key, path in selected.items():
        if key.split('/')[0] not in {'assets', 'css', 'js'} and path.parent != ROOT:
            raise ValueError(f'Non-runtime file selected: {key}')
        if path.stat().st_size >= 100_000_000:
            raise ValueError(f'File is too large for a normal GitHub upload: {key}')
    DIST.mkdir(exist_ok=True)
    # Rebuilding a generated DIST is authorized. Only remove obsolete files
    # after validating every resolved target remains inside this exact folder.
    expected = set(selected) | {'.nojekyll', 'build-manifest.json'}
    existing = list(DIST.rglob('*'))
    for path in existing:
        if path.is_symlink() or not path.resolve().is_relative_to(DIST.resolve()):
            raise ValueError(f'Unsafe existing DIST path: {path}')
    for path in existing:
        if path.is_file() and path.relative_to(DIST).as_posix() not in expected:
            path.unlink()
    files = []
    for key, source in sorted(selected.items()):
        target = DIST / key
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        checksum = digest(source)
        if digest(target) != checksum:
            raise ValueError(f'Source/DIST mismatch: {key}')
        files.append({'path': key, 'bytes': target.stat().st_size, 'sha256': checksum})
    (DIST / '.nojekyll').write_text('', encoding='utf-8')
    total = sum(r['bytes'] for r in files)
    if total >= 1_000_000_000:
        raise ValueError('DIST exceeds the GitHub Pages site size limit')
    manifest = {
        'builtAt': datetime.now(timezone.utc).isoformat(),
        'entryPoint': 'index.html', 'gameContent': 'v4.0.1',
        'buildCommand': 'python build.py',
        'savePolicy': 'Device-local browser localStorage; user-controlled JSON download/import; no server saves',
        'sourceFiles': len(files), 'sourceBytes': total, 'files': files,
    }
    (DIST / 'build-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    with ZipFile(ARCHIVE, 'w', ZIP_DEFLATED) as archive:
        for path in sorted(DIST.rglob('*')):
            if path.is_file():
                archive.write(path, path.relative_to(DIST).as_posix())
    with ZipFile(ARCHIVE) as archive:
        assert archive.testzip() is None
        assert 'index.html' in archive.namelist() and '.nojekyll' in archive.namelist()
        assert not any(p.startswith(('DIST/', 'tests/')) for p in archive.namelist())
    print(f'DIST rebuilt: {len(files)} source files, {total:,} bytes; all source hashes match.')
    print(f'{ARCHIVE.name}: {ARCHIVE.stat().st_size:,} bytes; ZIP CRC verified; contents start at index.html.')


if __name__ == '__main__':
    build()
