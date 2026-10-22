"""Prepare the approved v2.9 data and original-art briefs; no art fabrication."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/expansion-v29'
OUT.mkdir(exist_ok=True)
approved=json.loads((ROOT/'planning/v2.9/candidate-registry.json').read_text(encoding='utf-8'))
assert all(r['approved'] for r in approved['records'])
# size cm, conservative minimum US gal, game retail AC, art anatomy, habitat, foods
profiles=[
 (10,70,420,'deep orange-red dwarf angelfish, four dark vertical flank bars, black rear dorsal and anal edges with blue accents','rocks',['algae','pellets','frozen']),
 (10,70,280,'deep violet-blue dwarf angelfish with orange flanks and fine blue vertical striping','rocks',['algae','pellets','frozen']),
 (8,40,240,'small deep blue dwarf angelfish, orange-yellow head and chest, blue orbital ring','rocks',['algae','pellets','frozen']),
 (8,55,380,'dark navy dwarf angelfish with orange back and yellow-orange tail','rocks',['algae','pellets','frozen']),
 (13,100,1200,'orange angelfish with dense blue vertical squiggles, blue-black rear body and fin edges','rocks',['algae','pellets','frozen']),
 (10,100,2200,'yellow anterior half and dark navy posterior half, yellow tail, bright blue eye ring, NO vertical blue forehead stripe','rocks',['algae','pellets','frozen']),
 (25,180,1400,'tall angelfish with alternating blue-edged white and orange vertical bands; juvenile has rear dorsal eyespot','rocks',['angel-ration','frozen']),
 (6,30,150,'slender magenta-purple dottyback with black line through eye and translucent purple fins','caves',['frozen','pellets']),
 (22,125,400,'bright yellow deep-bodied butterflyfish, long thin forceps snout, black upper mask and white lower face, small rear anal eyespot','rocks',['frozen']),
 (18,150,300,'white triangular flank wedge on yellow butterflyfish, dark brown head and yellow fins','open',['live-plankton','frozen']),
 (18,120,450,'oval brown bristletooth tang with fine pale horizontal lines and distinct golden-yellow eye ring','rocks',['algae','pellets']),
 (16,100,330,'brown bristletooth tang with golden dorsal and anal tips, pale white caudal fin','rocks',['algae','pellets']),
 (25,180,950,'royal purple disc-shaped tang with luminous yellow tail and fine dark flank texture','rocks',['algae','pellets']),
 (22,200,2600,'dark charcoal disc-shaped tang covered with crisp small white spots, bright yellow tail','rocks',['algae','pellets']),
 (24,220,1500,'black tang with orange teardrop at caudal peduncle and thin orange-white fin accents; juvenile smaller orange patch','open',['algae','pellets']),
 (25,150,280,'yellow rabbitfish with elongated white snout and bold black face and chest mask, erect dorsal spines','rocks',['algae','pellets']),
 (22,150,350,'yellow rabbitfish with black-white foxface mask and a single distinct dark rear-flank spot','rocks',['algae','pellets']),
 (13,55,230,'golden-yellow slender blenny, blue eye ring and forked lyre tail, curved blue lips','caves',['live-plankton','frozen','pellets']),
 (14,70,170,'mottled tan-grey algae blenny with blunt head, eyebrow cirri, big normal dark eyes and tall dorsal fin','rocks',['algae','sinking']),
 (11,40,160,'slender blenny, dark slate anterior half, orange posterior half and tail, small eyebrow cirri','caves',['algae','sinking']),
 (8,75,390,'slender orange-red flasher wrasse with violet stripes, angular dorsal and tail fin display','open',['frozen','live-plankton']),
 (12,90,260,'green-blue wrasse with orange horizontal lines, intricate facial markings and juvenile tail eyespot','sand',['frozen','sinking']),
 (12,75,190,'canary-yellow slender wrasse, dark dorsal eyespots especially juvenile, rounded snout','sand',['frozen','sinking']),
 (15,100,850,'leopard wrasse female reference: pale cream body densely patterned with irregular black reticulated spots and orange head markings','sand',['live-plankton','frozen']),
 (9,125,380,'slender anthias with vivid yellow upper back and head, pink-purple lower flanks, forked tail; juvenile paler','open',['live-plankton','frozen']),
 (20,30,180,'Duncan coral: green oral discs, delicate tan tentacles radiating from separate fleshy polyps on branched cream skeleton','rock',['reef-meat']),
 (20,30,220,'candy cane coral: separate round fleshy mint-green trumpet heads on branching cream skeleton; no hammer tentacle tips','rock',['reef-meat']),
 (40,75,650,'yellow scroll coral: ochre-yellow curled upright plates with tiny evenly spaced polyps; juvenile a small cupped plate','rock',['phyto']),
 (50,100,1200,'black sun coral: arborescent dark green-black thick branches with many extended yellow-green starburst polyps; nonphotosynthetic','rock',['reef-meat']),
 (12,40,2400,'Rhizotrochus typus: ONE fleshy solitary cream-orange corallite with broad open oral disc, long translucent pale tentacles and anchoring rootlets; never a branching colony','rock',['reef-meat']),
 (6,30,120,'slender cleaner shrimp, red dorsal band split by continuous white stripe, yellow translucent sides, very long white antennae','rocks',['frozen','sinking']),
 (6,40,650,'deep scarlet red fire shrimp with small white dorsal spots and long white antennae and pale lower legs','rocks',['frozen','sinking']),
 (4,20,150,'small translucent ivory pistol shrimp with vivid red diagonal bands and ONE enlarged snapping claw','sand',['frozen','sinking']),
 (5,40,1400,'ivory harlequin shrimp with purple-blue oval spots, expanded paddle-like claws and leaf-like antennae','rocks',['starfish-tissue']),
 (2,30,2500,'tiny white Colemans shrimp with orange-red round spots, brown-red leg bands and a slender rostrum; no giant claws','rocks',['frozen'])
]
assert len(profiles)==35
records=[]
for r,p in zip(approved['records'],profiles):
 size,minimum,price,appearance,habitat,diet=p
 category=r['category'];scientific=r['scientificName'];ident=r['id']
 early='pelagic egg and developing fish larva' if category=='fish' else 'settled coral polyp or appropriately small propagated frag, NOT a fish egg' if category=='coral' else 'brooded embryonic cluster, then free swimming zoea larva, then settled juvenile; depict shrimp anatomy, NOT miniature adult in a fish egg'
 prompt=f'''Use case: stylized-concept. Asset type: one original Aquarium Life species life-stage sprite sheet, not a poster. Subject: {r['name']} ({scientific}). Anatomy and markings: {appearance}. Style: premium hybrid 16-bit pixel art, clear crisp pixel clusters, restrained textured shading, saturated natural colors, readable dark normal eyes with small highlights, matching the game's existing realistic detailed pixel aquarium livestock. Transparent background with true alpha, no scenery, no letters, numbers, labels, grid lines or watermark.
Strict composition: a 4-column by 2-row contact sheet, eight isolated sprites in equal cells with wide transparent gutters. Top row left to right: earliest appropriate developmental form ({early}); baby/larva or small growing frag; juvenile; adult. Bottom row left to right: the deceased equivalents of those same four stages. Dead forms are authored naturally pale relaxed remains, not red crosses, not inverted copies, no gore. ALL swimming fish and shrimp in side profile face RIGHT, snout and normal visible eye on the RIGHT side. Coral stays upright on a small visible secure skeleton/frag base in every applicable stage; dead coral is bare skeleton, not a dead fish. Each organism must fit entirely within its cell with fins, antennae and tentacles uncropped. One subject only in each cell; no neighboring-cell overlaps. Adult occupies about 75 percent of its cell width; early stages remain smaller and identifiable. Keep stages anatomically distinct, no generic shared fish silhouette.'''
 rec={**r,'batch':'v2.9','rarity':r['proposedRarity'],'difficulty':r['proposedCareDifficulty'],'size':size,'minGallons':minimum,'price':price,'appearance':appearance,'habitat':habitat,'diet':diet,
      'life':5 if category!='coral' else 15,'maturity':100 if category=='fish' else 120,'incubation':72,'reproduction':'eggs','breedingSupported':False,'breedingStatus':'Natural reproduction not implemented; purchased developmental forms use a labeled nursery abstraction.',
      'aggression':.45 if any(w in r['name'].lower() for w in ['angel','tang','dottyback']) else .2,'predator':.15 if ident in ['halichoeres-melanurus','forcipiger-flavissimus'] else 0,
      'light':0 if ident in ['tubastraea-micranthus','rhizotrochus-typus'] else .65 if category=='coral' else 0,'flow':.65 if ident=='tubastraea-micranthus' else .45 if category=='coral' else 0,
      'purchaseVerified':ident!='periclimenes-colemani','acquisitionHold':'Verified living fire-urchin host support is not implemented; no acquisition by any route.' if ident=='periclimenes-colemani' else None,
      'careStatus':'Conservative game calibration; not a real-world aquarium certification. Specialist limitations disclosed.',
      'earlyEquivalent':early,'implementationStatus':'REGISTERED; integration and QA pending','implementationDate':'2026-10-14','art':{'source':f'assets/expansion-v29/{ident}/source-v1.png','atlas':f'assets/expansion-v29/{ident}/atlas-v1.png','metadata':f'assets/expansion-v29/{ident}/metadata-v1.json','approved':False},'sourceLinks':[r['taxonomySource']]}
 if category=='fish':rec['shape']='bottom' if 'blenny' in r['name'].lower() else 'slim' if any(w in r['name'].lower() for w in ['wrasse','anthias','dottyback']) else 'tang'
 elif category=='coral':rec['shape']='lps' if ident in ['duncanopsammia-axifuga','caulastraea-furcata','rhizotrochus-typus'] else 'branch'
 else:rec['shape']='shrimp'
 records.append(rec)
 (OUT/ident).mkdir(exist_ok=True)
 (OUT/ident/'prompt-v1.txt').write_text(prompt,encoding='utf-8')
ledger={'version':'2.9','date':'2026-10-14','status':'IMPLEMENTATION AUTHORIZED; QA pending','numericCare':'Explicit conservative game calibrations','records':records}
(OUT/'registry.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(ROOT/'js/update29-data.js').write_text('"use strict";\n// Generated from assets/expansion-v29/registry.json.\nAL.Update29Data='+json.dumps(ledger,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
print('Prepared 35 approved registry entries and 35 original sprite-sheet prompts.')
