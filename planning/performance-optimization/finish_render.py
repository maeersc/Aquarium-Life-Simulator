from pathlib import Path
r=Path(__file__).resolve().parents[2];p=r/'js/render.js';s=p.read_text(encoding='utf8')
a=s.index('    for(let i=0;i<(water===');b=s.index('\n    const sandY=',a)
old=s[a:b]
new="""    const beamCount=water==='low'?0:water==='medium'?3:5,beamXs=Array.from({length:beamCount},(_,i)=>Math.round(40+i*102+Math.sin(time*.05+i)*12));
    g.drawImage(this.layer('beams',[marine,lamp,water,...beamXs].join(':'),g=>{for(const x of beamXs){g.globalAlpha=.075*lamp;AL.Art.poly(g,[[x-15,0],[x+4,0],[x+65,210],[x-25,210]],marine?'#bfeaff':'#e4f4c2');}}),0,0);"""
s=s[:a]+new+s[b:]
a=s.index("    g.fillStyle='#c0e9d011';");b=s.index("for(let i=0;i<(water===",a)
block=s[a:b];s=s[:a]+"    g.drawImage(this.layer('glass','v1',g=>{"+block+"}),0,0);"+s[b:]
p.write_text(s,encoding='utf8')
# The standalone gallery uses the same small, on-demand source loader.
p=r/'livestock-animation-review.html';s=p.read_text(encoding='utf8');a=s.index('<!-- AL_LIVESTOCK_SHEETS_START -->');b=s.index('<!-- AL_LIVESTOCK_SHEETS_END -->',a)+len('<!-- AL_LIVESTOCK_SHEETS_END -->');s=s[:a]+'<!-- AL_LIVESTOCK_SHEETS_START --><!-- Native sheets load on demand. --><!-- AL_LIVESTOCK_SHEETS_END -->'+s[b:];s=s.replace('<script defer src="js/sprite-kit.js">','<script defer src="js/performance.js"></script><script defer src="js/sprite-sources.js"></script><script defer src="js/sprite-kit.js">');p.write_text(s,encoding='utf8')
# Preserve byte validation and authored metadata, generate small per-sheet transports.
p=r/'livestock_animation_build.py';s=p.read_text(encoding='utf8');a=s.index('    # Keep every deployable file');b=s.index("    target=root/'js/livestock-animation-data.js'",a)
s=s[:a]+'''    # Per-sheet classic scripts keep file:// canvases origin-clean without
    # eagerly parsing every base64 PNG. HTTPS uses the original PNG directly.
    folder=root/'assets/livestock/animation-sources';folder.mkdir(exist_ok=True)
    for entry in ledger['entries']:
        for clip in entry['clips']:
            source=clip.pop('src')
            content='"use strict";\\nAL.SpriteSources.accept('+json.dumps(clip['path'])+','+json.dumps(source)+');\\n'
            (folder/(clip['sha256']+'.js')).write_text(content,encoding='utf8')
    ledger['sourceTransport']='Per-sheet local classic script / original HTTPS PNG'
''' +s[b:]
s=s.replace("block=start+'\\n'+''.join('<script defer src=\"'+name+'\"></script>\\n' for name in chunks)+end","block=start+'<!-- Native sheets load on demand. -->'+end")
p.write_text(s,encoding='utf8')
p=r/'build.py';s=p.read_text(encoding='utf8').replace("*ROOT.glob('js/*.js')","*(p for p in ROOT.glob('js/*.js') if not p.name.startswith('livestock-animation-sheets-'))").replace("'gameContent': 'v4.2.1'","'gameContent': 'v4.3.0'");p.write_text(s,encoding='utf8')
