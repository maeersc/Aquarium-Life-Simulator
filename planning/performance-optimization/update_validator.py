from pathlib import Path
r=Path(__file__).resolve().parents[2];p=r/'tests/verify_sprite_production_release.py';s=p.read_text(encoding='utf8');a=s.index('assigned=set()');b=s.index("check('Original119 unique",a)
s=s[:a]+'''assigned=set()
for ei,entry in enumerate(runtime['entries']):
    for ci,clip in enumerate(entry['clips']):
        path=ROOT/'assets/livestock/animation-sources'/(clip['sha256']+'.js')
        content=path.read_text(encoding='utf8') if path.is_file() else ''
        match=re.fullmatch(r'"use strict";\\nAL\\.SpriteSources\\.accept\\((".*"),(".*")\\);\\n',content)
        check('Per-sheet local source transport exists and is GitHub-safe: '+clip['path'],match is not None and path.stat().st_size<8_100_000)
        if not match:continue
        source_path=json.loads(match[1]);url=json.loads(match[2])
        check('Lossless bundled source equals registered native PNG: '+clip['path'],source_path==clip['path'] and url.startswith('data:image/png;base64,') and base64.b64decode(url.split(',',1)[1],validate=True)==(ROOT/clip['path']).read_bytes());assigned.add((ei,ci))
check('Every production sheet has one independently loadable source',len(assigned)==len(clips))
for filename in ['index.html','livestock-animation-review.html']:
    scripts=re.findall(r'<script\\b[^>]*\\bsrc="([^\"]+)"', (ROOT/filename).read_text(encoding='utf8'))
    check('Small source loader precedes animator without eager native banks: '+filename,'js/sprite-sources.js' in scripts and scripts.index('js/sprite-sources.js')<scripts.index('js/fish-animation.js') and not any('livestock-animation-sheets-' in name for name in scripts))
''' +s[b:]
p.write_text(s,encoding='utf8')
