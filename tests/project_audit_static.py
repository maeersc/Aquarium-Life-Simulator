"""Read-only integrity evidence for the October 2026 project audit."""
from pathlib import Path
import base64, hashlib, json, re, zipfile
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent

def embedded(path):
    text = (ROOT/path).read_text(encoding='utf-8')
    return json.JSONDecoder().raw_decode(text[text.index('=')+1:].lstrip())[0]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    banks = []
    for name in ['js/art-assets-data.js', 'js/life-stage-data.js', 'js/clownfish-art-data.js']:
        rows = []
        for record in embedded(name)['records']:
            atlas = ROOT/record['atlas']
            png = base64.b64decode(record['src'].split(',', 1)[1])
            with Image.open(atlas) as im:
                alphas = set(im.convert('RGBA').getchannel('A').getdata())
                count = record.get('frameCount', record.get('frames'))
                dims = (record['frameWidth']*count, record['frameHeight'])
                rows.append({'id':record['id'], 'atlas':record['atlas'],
                             'embeddedMatchesFile': png == atlas.read_bytes(),
                             'dimensions':list(im.size), 'expectedDimensions':list(dims),
                             'dimensionsValid':im.size == dims,
                             'binaryAlpha':alphas <= {0,255}, 'hasTransparency':0 in alphas,
                             'frameCount':count, 'approved':record.get('approved',False)})
        banks.append({'file':name, 'records':rows})
    roots = [*ROOT.glob('*.html'), *ROOT.glob('js/*.js'), *ROOT.glob('css/*.css')]
    paths, missing = set(), []
    for p in roots:
        text = p.read_text(encoding='utf-8')
        # Literal local runtime references. Dynamic paths are additionally exercised in browsers.
        for reference in re.findall(r'''["']((?:assets|js|css)/[^"'<>\s]+\.(?:png|svg|js|css|json))["']''',text):
            if '${' in reference:continue
            paths.add(reference)
            if not (ROOT/reference).is_file():missing.append({'file':p.relative_to(ROOT).as_posix(),'reference':reference})
    hashes = json.loads((ROOT/'tests/audit-code-baseline.json').read_text())
    changed = [p for p,h in hashes.items() if digest(ROOT/p) != h]
    protected = json.loads((ROOT/'tests/freshwater-protection-baseline.json').read_text())
    protected_changes = [p for p,h in protected.items() if digest(ROOT/p) != h]
    # The sole pre-audit simulation change is the previously delivered, explicitly marked marine block.
    sim = (ROOT/'js/simulation.js').read_text(encoding='utf-8')
    old = (ROOT/'tests/freshwater-protected-simulation.js').read_text(encoding='utf-8')
    original = "const clown=K.alive(t).filter(f=>f.species==='clown');if(clown.length===2&&clown[0].sex===clown[1].sex){clown.sort((a,b)=>b.adultSize-a.adultSize);clown[0].sex='F';clown[1].sex='M';}"
    start=sim.index('// Marine-only clownfish pairing:')
    end=sim.index('// End marine-only clownfish pairing.')+len('// End marine-only clownfish pairing.')
    simulation_equal = sim[:start]+original+sim[end:] == old
    mdp = (ROOT/'MASTER_DEVELOPMENT_PROMPT.md').read_text(encoding='utf-8')
    sections = re.findall(r'^# (\d+)\. (.+)$',mdp,re.M)
    collection = embedded('js/clownfish-collection-data.js')
    zippath = ROOT/'AquariumLife-v0.1.zip'
    with zipfile.ZipFile(zippath) as archive:
        zip_report = {'file':zippath.name, 'bytes':zippath.stat().st_size,'members':len(archive.namelist()),'firstBadCRC':archive.testzip()}
    report = {'date':'2026-10-12','banks':banks,'bankRecords':sum(len(b['records']) for b in banks),
              'literalRuntimeAssetReferences':len(paths),'missingLiteralReferences':missing,
              'gameBaselineFiles':len(hashes),'gameFilesChangedDuringAudit':changed,
              'freshwaterBaselineEntries':len(protected),'freshwaterChangesVsProtectedBaseline':protected_changes,
              'simulationMatchesProtectedSourceAfterMarineBlockRemoval':simulation_equal,
              'mdpSectionNumbers':[int(n) for n,_ in sections],
              'clownfishSpecies':len(collection['species']),'designerVarieties':len(collection['varieties']),
              'designerBaseLinksValid':all(v['speciesId'] in {s['id'] for s in collection['species']} for v in collection['varieties']),
              'approvedReferenceExists':(ROOT/'assets/reference/approved_clownfish_hybrid.png').is_file(),
              'archive':zip_report,
              'scope':'Static integrity only. Does not certify anatomy, care science, gameplay behavior, or approval.'}
    target=ROOT/'tests/audit-evidence/static-integrity.json'
    target.write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k != 'banks'}))

if __name__ == '__main__':main()
