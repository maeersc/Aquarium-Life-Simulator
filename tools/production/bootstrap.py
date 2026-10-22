"""Install a verified portable build runtime and pinned minifiers, never player dependencies."""
from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile
import hashlib,json,os,shutil,subprocess

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
VERSION='22.23.0'
CACHE=ROOT/'.build-tools'
NODE=CACHE/('node-v'+VERSION+'-win-x64')

def setup():
    CACHE.mkdir(exist_ok=True)
    if os.name!='nt':
        node=shutil.which('node')
        if not node:raise RuntimeError('Install Node.js22 or later for this platform before building.')
        npm=shutil.which('npm')
        command=[npm,'ci' if (HERE/'package-lock.json').exists() else 'install']
    else:
        if not (NODE/'node.exe').exists():
            name='node-v'+VERSION+'-win-x64.zip'
            base='https://nodejs.org/dist/v'+VERSION+'/'
            sums=urlopen(base+'SHASUMS256.txt',timeout=60).read().decode('ascii')
            expected=next(row.split()[0] for row in sums.splitlines() if row.split()[-1]==name)
            archive=CACHE/name
            with urlopen(base+name,timeout=60) as response,archive.open('wb') as output:shutil.copyfileobj(response,output)
            actual=hashlib.sha256(archive.read_bytes()).hexdigest()
            if actual!=expected:raise RuntimeError('Official Node archive checksum mismatch')
            with ZipFile(archive) as z:
                for entry in z.infolist():
                    target=(CACHE/entry.filename).resolve()
                    if not target.is_relative_to(NODE.resolve()):raise RuntimeError('Unexpected Node archive path')
                z.extractall(CACHE)
            (CACHE/'node-download.json').write_text(json.dumps({'url':base+name,'sha256':actual,'checksumSource':base+'SHASUMS256.txt'},indent=2),encoding='utf8')
        command=[str(NODE/'node.exe'),str(NODE/'node_modules/npm/bin/npm-cli.js'),'ci' if (HERE/'package-lock.json').exists() else 'install']
    env={**os.environ,'npm_config_cache':str(CACHE/'npm-cache'),'npm_config_update_notifier':'false'}
    if os.name=='nt':env['PATH']=str(NODE)+os.pathsep+env.get('PATH','')
    subprocess.run(command+['--ignore-scripts','--no-audit','--no-fund'],cwd=HERE,env=env,check=True)
    print('Build tools ready; no runtime or global installation was changed.')

if __name__=='__main__':setup()
