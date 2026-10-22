"""Deterministic, source-preserving classic-script production build."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from collections import deque
from zipfile import ZipFile,ZipInfo,ZIP_DEFLATED
import base64,hashlib,json,re,shutil,subprocess,tempfile

ROOT=Path(__file__).resolve().parents[2]
TOOLS=Path(__file__).resolve().parent
DIST=ROOT/'DIST'
EVIDENCE=ROOT/'planning/distribution-protection/evidence'
CACHE=ROOT/'.build-tools/minified'
ASSET_REFERENCE=re.compile(r'''(?:\.\./)?assets/[^\s"'`<>\\)]+''')
ASSET_TYPES={'.png','.svg','.jpg','.jpeg','.webp','.woff','.woff2','.ogg','.wav','.mp3','.js'}
class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[]
    def handle_starttag(self,tag,attrs):
        for k,v in attrs:
            if k in ('src','href') and v:
                u=urlsplit(v)
                if not u.scheme and not u.netloc and u.path:self.links.append(unquote(u.path))
def sha(path):
    with path.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def checked(p):
    if p.is_symlink() or not p.resolve().is_relative_to(ROOT):raise ValueError('Build input escapes workspace: '+str(p))
    current=ROOT
    for part in p.relative_to(ROOT).parts:
        if part not in {c.name for c in current.iterdir()}:raise ValueError('Wrong URL case: '+str(p))
        current/=part
    if not p.is_file():raise FileNotFoundError(p)
    return p.relative_to(ROOT).as_posix()
def discover():
    html=(ROOT/'index.html').read_text(encoding='utf8');parser=Links();parser.feed(html)
    pending=deque(ROOT/x for x in parser.links);selected={}
    while pending:
        p=pending.popleft();key=checked(p)
        if key in selected:continue
        if p.suffix=='.html':raise ValueError('Unexpected production review page: '+key)
        selected[key]=p
        if p.suffix not in {'.js','.css','.svg'}:continue
        code=p.read_text(encoding='utf8')
        for match in ASSET_REFERENCE.finditer(code):
            target=ROOT/urlsplit(match.group().removeprefix('../')).path
            if target.is_file() and target.suffix in ASSET_TYPES:pending.append(target)
            elif target.is_dir():pending.extend(q for q in sorted(target.rglob('*')) if q.is_file() and q.suffix in ASSET_TYPES)
    return html,selected
def node():
    local=ROOT/'.build-tools/node-v22.23.0-win-x64/node.exe'
    binary=str(local) if local.exists() else shutil.which('node')
    if not binary or not (TOOLS/'node_modules/terser').is_dir() or not (TOOLS/'node_modules/clean-css').is_dir():
        raise RuntimeError('Run python tools/production/bootstrap.py once to prepare build tools; the game itself needs none.')
    return binary
def validate_native_sources():
    registry=json.loads((ROOT/'assets/animation/livestock-registry.json').read_text(encoding='utf8'))
    code=(ROOT/'js/livestock-animation-data.js').read_text(encoding='utf8')
    runtime=json.loads(code.split('AL.LivestockAnimationData=',1)[1].strip().removesuffix(';'))
    if runtime['entries']!=registry['entries']:
        raise ValueError('Native metadata is stale; update development sources with livestock_animation_build.py first.')
    count=0
    for entry in registry['entries']:
        for clip in entry['clips']:
            p=ROOT/clip['path'];checked(p)
            if clip['frameCount']!=16 or sha(p)!=clip['sha256']:raise ValueError('Invalid native sheet source: '+clip['path'])
            transport=ROOT/'assets/livestock/animation-sources'/(clip['sha256']+'.js');checked(transport)
            text=transport.read_text(encoding='utf8');prefix='AL.SpriteSources.accept('
            args=json.loads('['+text.split(prefix,1)[1].strip().removesuffix(';').removesuffix(')')+']')
            if args[0]!=clip['path'] or hashlib.sha256(base64.b64decode(args[1].split(',',1)[1])).hexdigest()!=clip['sha256']:
                raise ValueError('Native file transport is stale: '+clip['path'])
            count+=1
    return count
def build():
    native_count=validate_native_sources()
    html,selected=discover();CACHE.mkdir(parents=True,exist_ok=True);EVIDENCE.mkdir(parents=True,exist_ok=True)
    if DIST.is_symlink() or DIST.resolve()!=ROOT/'DIST':raise ValueError('DIST must be directly inside this workspace')
    original={k:sha(p) for k,p in selected.items()};original['index.html']=sha(ROOT/'index.html')
    with tempfile.TemporaryDirectory(prefix='production-',dir=ROOT/'.build-tools') as temp:
        staging=Path(temp);files=[]
        for k,p in sorted(selected.items()):
            if p.suffix in {'.js','.css'}:
                output=staging/k;output.parent.mkdir(parents=True,exist_ok=True)
                files.append({'name':k,'input':str(p),'output':str(output),'kind':p.suffix})
        task=staging/'task.json';result=staging/'result.json'
        task.write_text(json.dumps({'files':files,'cache':str(CACHE),'result':str(result)}),encoding='utf8')
        subprocess.run([node(),str(TOOLS/'minify.cjs'),str(task)],check=True,cwd=TOOLS)
        minified=json.loads(result.read_text(encoding='utf8'));renamed={}
        for row in minified['results']:
            k=row['name']
            if not k.startswith('assets/'):
                kind=Path(k).suffix;renamed[k]=('js/' if kind=='.js' else 'css/')+'a.'+row['outputSha256'][:20]+kind
        for old,new in sorted(renamed.items(),key=lambda item:-len(item[0])):html=html.replace('"'+old+'"','"'+new+'"')
        html=re.sub(r'<!--.*?-->','',html,flags=re.S)
        payload=staging/'payload';payload.mkdir();records=[]
        for k,p in sorted(selected.items()):
            out=renamed.get(k,k);source=staging/k if p.suffix in {'.js','.css'} else p
            target=payload/out;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target)
            records.append({'input':k,'output':out,'inputSha256':original[k],'sha256':sha(target),'sourceBytes':p.stat().st_size,'bytes':target.stat().st_size})
        (payload/'index.html').write_text(html,encoding='utf8');records.append({'input':'index.html','output':'index.html','inputSha256':original['index.html'],'sha256':sha(payload/'index.html'),'sourceBytes':(ROOT/'index.html').stat().st_size,'bytes':(payload/'index.html').stat().st_size})
        license_text='Aquarium Life production build\n\nGame code and artwork: original project ownership and existing art approvals apply.\n\nThis package is minified and uses shortened internal identifiers. It is not encrypted or tamper-proof.\nBuild-time minifiers are not included. Source maps, development tools and review pages are not distributed.\n'
        (payload/'LICENSE.txt').write_text(license_text,encoding='utf8');(payload/'.nojekyll').write_bytes(b'')
        published=[{'path':p.relative_to(payload).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(payload.rglob('*')) if p.is_file()]
        manifest={'format':2,'production':True,'protection':'minification-and-local-identifier-mangling','reproducible':True,'entryPoint':'index.html','gameContent':'v4.3.1','buildCommand':'python build.py','savePolicy':'Device-local browser storage; existing JSON export/import; no save encryption or profile migration','toolchain':minified['versions'],'files':published,'sourceFiles':len(published),'sourceBytes':sum(x['bytes'] for x in published)}
        manifest['buildId']=hashlib.sha256(json.dumps(manifest,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        (payload/'build-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf8')
        if manifest['sourceBytes']>=1_000_000_000:raise ValueError('Production exceeds Pages size budget')
        for p in payload.rglob('*'):
            if p.is_file() and (p.suffix=='.map' or p.stat().st_size>=100_000_000):raise ValueError('Unsafe distribution file: '+str(p))
        for k,h in original.items():
            if sha(ROOT/k)!=h:raise ValueError('Development input modified: '+k)
        DIST.mkdir(exist_ok=True);existing=list(DIST.rglob('*'))
        for p in existing:
            if p.is_symlink() or not p.resolve().is_relative_to(DIST.resolve()):raise ValueError('Unsafe existing DIST path: '+str(p))
        expected={p.relative_to(payload).as_posix() for p in payload.rglob('*') if p.is_file()}
        for p in existing:
            if p.is_file() and p.relative_to(DIST).as_posix() not in expected:p.unlink()
        for p in sorted(existing,reverse=True):
            if p.is_dir() and not any(p.iterdir()):p.rmdir()
        for p in payload.rglob('*'):
            if p.is_file():
                target=DIST/p.relative_to(payload);target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,target)
        archive=ROOT/'AquariumLife-GitHub-Pages.zip'
        with ZipFile(archive,'w',compression=ZIP_DEFLATED,compresslevel=9) as z:
            for p in sorted(DIST.rglob('*')):
                if p.is_file():
                    info=ZipInfo(p.relative_to(DIST).as_posix(),date_time=(2026,1,1,0,0,0));info.compress_type=ZIP_DEFLATED;info.external_attr=0o644<<16;z.writestr(info,p.read_bytes(),compress_type=ZIP_DEFLATED,compresslevel=9)
        with ZipFile(archive) as z:
            if z.testzip() is not None:raise ValueError('Pages ZIP CRC failure')
        private={'buildId':manifest['buildId'],'nativeSourcesValidated':native_count,'files':records,'minifier':minified,'originalInputs':original,'bytes':manifest['sourceBytes'],'zipSha256':sha(archive),'zipBytes':archive.stat().st_size}
        (EVIDENCE/'build-private.json').write_text(json.dumps(private,indent=2),encoding='utf8')
        print(json.dumps({'buildId':manifest['buildId'],'productionFiles':len(published)+1,'productionBytes':manifest['sourceBytes'],'zipBytes':archive.stat().st_size,'sourcePreserved':True,'sourceMaps':False},indent=2))
        return manifest

if __name__=='__main__':build()
