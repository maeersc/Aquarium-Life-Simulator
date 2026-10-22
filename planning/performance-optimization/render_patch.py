from pathlib import Path
r=Path(__file__).resolve().parents[2];p=r/'js/render.js';s=p.read_text(encoding='utf8')
s=s.replace('this.visualFrame=0;}','this.visualFrame=0;this.layers=new Map();this.layerBuilds=0;}\n  layer(name,key,paint){let row=this.layers.get(name);if(!row||row.key!==key){const image=document.createElement(\'canvas\');image.width=480;image.height=240;const g=image.getContext(\'2d\');g.imageSmoothingEnabled=false;paint(g);row={key,image};this.layers.set(name,row);this.layerBuilds++;}return row.image;}')
s=s.replace('const marine=t.water',"const quality=s.settings.graphics?.quality||'high',water=s.settings.graphics?.water||'high',particles=s.settings.graphics?.particles||(s.settings.particles?'full':'off');const marine=t.water",1)
a=s.index('g.imageSmoothingEnabled=false;const bg=');b=s.index('\n    g.save();g.translate(W/2',a)
block=s[a:b];s=s[:a]+"g.drawImage(this.layer('background',[marine,dry].join(':'),g=>{"+block+"}),0,0);"+s[b:]
a=s.index('    g.globalAlpha=.2;for(let i=0;');b=s.index('\n    for(let i=0;i<5;',a)
block=s[a:b];s=s[:a]+"    g.drawImage(this.layer('backdrop',[marine,dry,quality,!!AL.FishAnimation?.sheets.find('sps','frag','polyp_motion')?.image,!!AL.FishAnimation?.sheets.find('sps','colony','polyp_motion')?.image].join(':'),g=>{"+block+"}),0,0);"+s[b:]
s=s.replace('for(let i=0;i<5;i++){const x=40+i*102',"for(let i=0;i<(water==='low'?0:water==='medium'?3:5);i++){const x=40+i*102")
a=s.index('const sand=g.createLinearGradient');b=s.index('    const rock=',a)
block=s[a:b].rstrip();s=s[:a]+"g.drawImage(this.layer('sand',[marine,sandY,sandColor,t.substrate?.depth,t.substrate?.type,quality].join(':'),g=>{"+block+"}),0,0);\n"+s[b:]
s=s.replace('for(let i=0;i<700;i++)',"for(let i=0;i<(quality==='low'?175:quality==='medium'?350:700);i++)")
s=s.replace('if(s.settings.particles){for(let i=0;i<23;i++)',"if(particles!=='off'){for(let i=0;i<(particles==='low'?8:23);i++)").replace('for(let i=0;i<35;i++){g.fillStyle=\'#b8d4be22\'',"for(let i=0;i<(particles==='low'?10:35);i++){g.fillStyle='#b8d4be22'")
a=s.index('      const glow=g.createLinearGradient');b=s.index('g.restore();',a)
block=s[a:b];s=s[:a]+"      g.drawImage(this.layer('lamp',[marine,lamp].join(':'),g=>{"+block+"}),0,0);"+s[b:]
s=s.replace('for(let i=0;i<11;i++){g.fillStyle',"for(let i=0;i<(water==='low'?0:water==='medium'?5:11);i++){g.fillStyle")
# Reusing generated thumbnails avoids PNG encoding on each Store/Journal rebuild.
s=s.replace('  function thumb(species,variety=null){',"  const thumbnails=new Map();\n  function buildThumb(species,variety=null){")
a=s.index('  function plant(ctx,');s=s[:a]+"  function thumb(species,variety=null){const key=species+':'+(variety||'');if(thumbnails.has(key))return thumbnails.get(key);const result=buildThumb(species,variety);if(thumbnails.size>=256)thumbnails.delete(thumbnails.keys().next().value);thumbnails.set(key,result);return result;}\n"+s[a:]
p.write_text(s,encoding='utf8')
# Replace permanent idle diving key polling with authoritative scheduler input sampling.
p=r/'js/diving-ui.js';s=p.read_text(encoding='utf8');a=s.index('setInterval(()=>{if(!owned||screen!==\'trip\'||!keys.size');b=s.index('},40);',a)+len('},40);');code=s[a:b];body=code[len('setInterval(()=>{'):-len('},40);')];s=s[:a]+s[b:];pos=s.index(' function bind()');s=s[:pos]+' function updateInput(now=performance.now()){'+body.replace(',now=performance.now()', '')+'}\n'+s[pos:];s=s.replace('return {bind,','return {updateInput,bind,');p.write_text(s,encoding='utf8')
# Decorative casino reel drawing stops in hidden tabs; saved outcome settlement stays intact.
p=r/'js/casino-ui.js';s=p.read_text(encoding='utf8').replace('animation=setInterval(()=>{frame++;','animation=setInterval(()=>{if(document.hidden||!modal.open)return;frame++;');p.write_text(s,encoding='utf8')
