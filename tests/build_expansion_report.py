"""Synchronize the v2.7 permanent registry, continuity sources and QA report.

Does not re-run the pre-registration duplicate audit or overwrite existing art.
Browser results must already exist. PDF output is deliberately not claimed.
"""
from pathlib import Path
from collections import Counter
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE = ROOT / 'tests/expansion-evidence'

def read(path):
    return (ROOT / path).read_text(encoding='utf-8')

def write(path, text):
    (ROOT / path).write_text(text.rstrip() + '\n', encoding='utf-8')

def load(path):
    return json.loads(read(path))

registry = load('assets/expansion-v27/registry.json')
records = registry['records']
audit = load('tests/expansion-evidence/duplicate-audit.json')
assert len(records) == len({r['id'] for r in records}) == 38
assert Counter(r['category'] for r in records) == {'fish': 28, 'coral': 5, 'bottom_dweller': 5}
assert audit['checked'] == 38 and not any(r['duplicate'] for r in audit['entries'])
art = {r['id']: r for r in load('tests/expansion-evidence/art-audit.json')['entries']}
partial = [r for r in records if art[r['id']]['clippedSourceCells']]
for r in records:
    folder = 'assets/expansion-v27/' + r['id']
    meta = load(folder + '/metadata-v1.json')
    r['art']['source'] = meta['path']
    r['artStatus'] = meta['artStatus'] + '; not user approved'
    if r['category'] == 'bottom_dweller':
        r['artStatus'] += '; egg/planktonic larval art unsupported'
    r['status'] = 'IMPLEMENTED; PARTIAL art' if meta['clippedSourceCells'] or r['category'] == 'bottom_dweller' else 'IMPLEMENTED; art pending visual approval'
    r['art']['aliveDeadStatus'] = 'Eight static stage/state views; early settled juvenile through adult' if r['category'] == 'bottom_dweller' else 'Eight static stage/state views, including living and deceased'
    r['art']['framingReviewFrames'] = meta['clippedSourceCells']
    r['art']['approved'] = False
    for field in ('source', 'atlas', 'metadata'):
        assert (ROOT / r['art'][field]).is_file(), (r['id'], field)
write('assets/expansion-v27/registry.json', json.dumps(registry, indent=2))
write('js/expansion-data.js', '"use strict";\n// Generated from assets/expansion-v27/registry.json; edit the central source.\nAL.ExpansionData=' + json.dumps(registry, separators=(',', ':')) + ';')

table = ['| Common name / scientific name | ID / category | Rarity / care / minimum | Implementation / batch / date | Art / alive-dead / notes |', '|---|---|---|---|---|']
for r in records:
    note = r['breedingStatus']
    if r['category'] == 'bottom_dweller':
        note += '. Egg and planktonic larval art not supplied; early settled juveniles are labeled as such.'
    table.append(f"| {r['name']} / *{r['scientificName']}* | `{r['id']}` / {r['category']} | {r['rarity']} / {r['difficulty']} / {r['minGallons']} gal | {r['status']} / v2.7 / 2026-10-14 | {r['artStatus']}. {r['art']['aliveDeadStatus']}. {note} [Atlas]({r['art']['atlas']}) · [metadata]({r['art']['metadata']}) |")
table = '\n'.join(table)

intro = '''## Livestock expansion v2.7 — current, 2026-10-14

MDP **v3.2** retains exactly 31 major sections. Added **38 unique marine entries: 28 fish, five named stony corals and five non-fish invertebrates**. All 38 passed the pre-registration scientific-name/synonym duplicate audit; none were skipped. The runtime now has **80 fish (69 marine, 11 protected freshwater), ten marine coral entries and five non-fish invertebrates**. The six existing freshwater plants are unchanged. Existing art-only and planned entries are excluded from these totals.

All six Mystery Egg rarity pools are now populated; the earlier empty-pool content hold is superseded. Keep independent 50/25/15/7.5/2/0.5 percent odds, 600 AC, three daily eggs, existing level/incubation gates and safe-destination checks. Daily Fish shopping remains exactly eight visible slots: 3 Common, 3 Uncommon, 1 Rare, 1 Mystery Egg. Higher tiers do not add normal Fish cards. Fixed retail, persistent selected aquarium, continuous offline simulation, rarity/genetics and existing specialist clownfish holds remain.

New livestock has inspectors, rarity, care information, value, host-filtered health compatibility and additive save support. Corals use player-selected supported rock/rack placement. Invertebrates are separate bottom residents with feeding, crawling/filtering, condition, death and transfer records. Their egg/planktonic larval reproduction and art are unsupported. New fish natural breeding is enabled only for the five explicitly supported profiles; Mystery Egg development is a simplified game presentation, not evidence of complete captive culture.

There are 38 new transparent sprite sheets / 304 static stage-state views. All are unapproved; 12 sheets carry explicit framing review flags. Existing approved artwork is preserved. Review [the new artwork gallery](expansion-review.html). [Implementation report](LIVESTOCK_EXPANSION_REPORT.md), [permanent registry](assets/expansion-v27/registry.json), [continuity source](PROJECT_CONTINUITY_SOURCE.md) and [PDF workflow](PDF_WORKFLOW.md) record the limits. **PDF regeneration remains pending: PDF authoring/rendering prerequisites are unavailable in this environment.** Earlier milestone material is historical where superseded.
'''

specific = {
    'GAME_DESIGN.md': '''### v2.7 gameplay details

New species are registered once through `ExpansionData`; freshwater species and simulation parameters are not extended. Specialist food inventory is marine-only. Predatory fish are checked against owned invertebrates. Prawn gobies/conch/hermit require sand; cave residents need rock shelter. Grazers require 72 prepared game hours. Purple Queen Anthias requires live plankton inventory, Copperband requires frozen food, and feeding-conditioned Orange-spotted Filefish requires specialist rations plus living branching SPS and can damage it when hungry. Spotted Boxfish requires a dedicated species-only aquarium; severe stress/death can release a bounded modeled toxin that filtration and water changes reduce. These are gameplay calibrations, not universal husbandry prescriptions.

The five supported new natural breeding profiles are Chalk Bass, Yellow Assessor, Blue Assessor, Greenbanded Goby and Sharknose Goby. Assessor broods stay protected in the mouthbrooding presentation. Game incubation of 48/72 hours and compressed lifespan/maturity are not biological timing claims. Remaining 23 new fish display an explicit natural-breeding hold; all five new invertebrates have no reproduction system. Corals use the existing fragmentation/placement system.
''',
    'ART_DIRECTION.md': '''### v2.7 art integration and honest coverage

One original transparent sheet per species, with source masters preserved under `assets/expansion-v27/<id>/`. Fish map egg, larva, juvenile and adult alive/dead. Corals map living/dead frag, young colony, stressed colony, mature colony, living bleaching, tissue loss and bare skeleton. Invertebrates map early settled juvenile, small juvenile, larger juvenile and adult alive/dead; these are not mislabeled as eggs or planktonic larvae. Source correction v2 removes inappropriate fin filaments on Pink-streaked, White-banded Possum and Tanaka's Pygmy Wrasse; v1 files remain archived.

`metadata-v1.json` records native direction, frame bounds, provisional eye registration, source hash, framing flags and approval=false. The technical packer detects transparent gutters and uses nearest-neighbor sizing; it does not repaint generated imagery. Twelve automatic boundary flags require visual review and are listed in the expansion report. Fish use static authored stages with existing runtime movement/mirroring; no new fin-cycle animation is claimed. Flasher/fairy adult references depict males, Boxfish depicts a female reference; alternate sex artwork is not supplied. All new art remains subject to user approval. Generation prompts and correction notes are in `tests/expansion-evidence/art-prompts.json`.
''',
    'UI_SPECIFICATION.md': '''### v2.7 interface behavior

Retain the six-window sidebar and current selected aquarium across store open/close, tab changes, purchases and reload. Fish keep the existing eight-card daily layout. Five invertebrate products appear under Saltwater → Bottom Feeders; named corals appear under Saltwater → Corals with scientific names and difficulty. Unsafe destinations reject or offer an eligible destination before payment. Invertebrates have their own inspector and transfer/remove/sell actions, linked diagnosis, Current Value and rarity. Collection/encyclopedia filter marine fish, corals and invertebrates without adding freshwater entries. The collection links to a separate offline 38-entry art review with category/species/direction/backdrop controls and separately saved review notes; notes never approve art or replace game saves.
''',
    'DEVELOPMENT_STATUS.md': '''### v2.7 delivery status

Implemented: all 38 exact approved species, 0 duplicates; store, journal, inspector, health/value, placement, safe destinations, upper Mystery pools and additive persistence. Chrome and Edge each passed 362 expansion checks plus 7,583 artwork regression checks (7,945 total per browser, zero failures). This includes 1,792 directional cases per browser, 145 protected-file hashes and a ten-game-day freshwater replay comparison. Test evidence is in the expansion report.

Partial/disclosed: 12 art framing flags, provisional eye metadata, static stage poses, selected sex-reference art, unsupported invertebrate egg/planktonic larval art/reproduction and unsupported natural breeding for 23 new fish. The project continuity source is updated; binary PDF export remains pending unavailable authoring/rendering tools. Firefox, native fullscreen modes and superseded milestone-specific full suites were not rerun. Previous artwork approvals and five specialist clownfish purchase holds are preserved.
''',
    'BALANCE_REPORT.md': '''### v2.7 economy and welfare calibration

All 38 retail prices, fixed rarities, minimum gallons and care profiles live in the central registry. Purchases use existing atomic money/stock validation; new stock initializes once (24 per fish/invertebrate, 12 per coral) without rerolling daily listings. Current asset value, tank totals and dealer offers reuse central condition/stage/rarity logic; death gives zero current value and preserves rarity history. Invertebrates add stocking/feeding/pollution load rather than free cleaning income. Marine specialist food prices are 48 AC live plankton, 30 AC suspension blend and 65 AC coral-polyp ration. Invertebrate supportive care is 45 AC and host-filtered; fish copper remains incompatible.

Mystery Egg prices/odds and daily eight-slot structure are unchanged; newly authorized high tiers remove only the empty-pool hold. Eligibility still requires safe space and care in every tier before an independent purchase roll. New rarity assignments are user-approved design decisions; they do not claim real-world trade scarcity. Prices, care gates, disease probabilities, toxin effects, maturity/lifespan and incubation are game parameters, not veterinary or biological measurements. No new paid service or freshwater biology was introduced.
'''
}
docs = ['README.md', 'CURRENT_LIVESTOCK_CATALOG.md', 'CURRENT_FISH_CATALOG.md', 'GAME_DESIGN.md', 'ART_DIRECTION.md', 'UI_SPECIFICATION.md', 'DEVELOPMENT_STATUS.md', 'BALANCE_REPORT.md', 'TEST_REPORT.md']
for path in docs:
    text = read(path)
    # Idempotently replace this batch's lead, retaining all historical milestones.
    text = re.sub(r'\n## Livestock expansion v2\.7.*?(?=\n## Rarity, genetics)', '\n', text, flags=re.S)
    text = text.replace('## Rarity, genetics and continuous ecosystem — v2.5/v2.6 (current)', '## Rarity, genetics and continuous ecosystem — v2.5/v2.6 (historical milestone)')
    # Correct the explicitly historical lead instead of presenting stale holds as current.
    text = text.replace('MDP **v3.1**, with the same 31 major sections, is current.', 'At this historical milestone, MDP **v3.1** retained the same 31 major sections.')
    text = text.replace('**Current limits:** Mystery Egg sales are held', '**Historical v2.6 limits (superseded by v2.7):** Mystery Egg sales were held')
    first, rest = text.split('\n', 1)
    first = re.sub(r'2026-10-\d{2}', '2026-10-14', first)
    if path == 'BALANCE_REPORT.md':
        first = '# Aquarium Life — current balance report'
    if path == 'CURRENT_LIVESTOCK_CATALOG.md':
        first = '# Current livestock catalog — 2026-10-14'
    lead = intro + '\n' + specific.get(path, '')
    if path == 'CURRENT_LIVESTOCK_CATALOG.md':
        lead += '\n### Permanent livestock logging rule\n\nEvery newly added livestock species must be recorded in the permanent registry, catalog, consolidated MDP and project PDF/continuity source in the same update. Log common/scientific name, stable ID, category, rarity, difficulty, implementation status, batch, date, art status, alive/dead support and limits. Never infer approval or count designer phenotypes as species. If PDF export is unavailable, update its source and explicitly mark regeneration pending.\n\n### Exact v2.7 registry — all 38 additions\n\n' + table + '\n\nThe following older catalog tables describe the pre-v2.7 baseline and remain as historical asset provenance. Add the 38 rows above once; do not count the old 52-fish table as the current roster.\n'
    if path == 'CURRENT_FISH_CATALOG.md':
        lead += '\nThe exact 28 new fish identities are listed in [CURRENT_LIVESTOCK_CATALOG.md](CURRENT_LIVESTOCK_CATALOG.md). The older roster below is retained as the pre-expansion provenance, not the current total.\n'
    if path == 'TEST_REPORT.md':
        lead += '\nCurrent results: **362 expansion + 7,583 artwork checks per browser, 0 failed**, Chrome and Edge. See [the v2.7 acceptance report](LIVESTOCK_EXPANSION_REPORT.md) for evidence and not-run coverage. Earlier numerical totals below are historical.\n'
    write(path, first + '\n\n' + lead + '\n' + rest.lstrip())

master = read('MASTER_DEVELOPMENT_PROMPT.md')
subsection_labels = {
    '6.5 Authorized marine livestock registry v2.7': '6.4 Authorized marine livestock registry v2.7',
    '8.5 Named coral expansion': '8.7 Named coral expansion',
    '9.6 Separate non-fish residents': '9.9 Separate non-fish residents',
    '15.6 v2.7 breeding boundaries': '15.8 v2.7 breeding boundaries',
    '16.5 New livestock rarity and value': '16.7 New livestock rarity and value',
    '24.5 Additive expansion migration': '24.4 Additive expansion migration',
    '27.5 v2.7 acceptance evidence': '27.13 v2.7 acceptance evidence',
    '30.5 Permanent livestock logging and completion rule': '30.3 Permanent livestock logging and completion rule',
}
for old_title, new_title in subsection_labels.items():
    master = master.replace('## ' + old_title, '## ' + new_title)
master = master.replace('current v2.7 roster is in section 6.5', 'current v2.7 roster is in section 6.4')
master = master.replace('VERSION 3.1', 'VERSION 3.2')
master = re.sub(r'^### Revision: .*$', '### Revision: 3.2 integrates the authorized 38-species marine expansion v2.7. All 31 major sections remain intact.', master, count=1, flags=re.M)
master = master.replace('This update does not add a new expansion batch.', 'The later explicit v2.7 authorization adds exactly 28 fish + 5 corals + 5 non-fish bottom dwellers as a one-batch exception; the default future batch target remains 25/5/5.')
master = master.replace('The current audit has 52 fish records (including four benthic fish) and five coral categories;', 'The historical dedicated-collection audit had 52 fish records (including four benthic fish) and five coral categories; the current v2.7 roster is in section 6.5;')
master = master.replace('## 18.7 Mystery Egg — Exact Independent Odds and Content Hold', '## 18.7 Mystery Egg — Exact Independent Odds and Safe Purchase')
old = 'The current approved catalog has no eligible Very Rare, Ultra Rare or Legendary marine species; therefore the eighth card remains visible with the exact odds/key and a transparent content hold, zero purchasable stock and disabled confirmation. No charge or RNG draw occurs. Do not add species, promote approved clownfish, or substitute lower tiers merely to remove the hold. All six pools must be populated through a later authorized content decision before sales unlock.'
new = 'The explicit v2.7 authorization populates all six marine rarity pools, removing the prior empty-pool hold. Retain the level-10 gate, three daily eggs, incubation capacity and compatibility with a safe selected destination for an eligible outcome in every tier before payment or RNG draw. Stock/roll/embryo identity persist exactly once. High-rarity additions enter Mystery pools without increasing the eight normal daily Fish slots, promoting existing clownfish or redistributing odds. Specialized food, coral-prey and isolated Boxfish checks apply. A new species authorization never waives those safety gates.'
master = master.replace(old, new)
additions = {
    6: ('6.5 Authorized marine livestock registry v2.7', 'The permanent source `assets/expansion-v27/registry.json` contains exactly 38 new entries dated 2026-10-14: 28 fish, five named stony corals and five non-fish bottom dwellers. The duplicate/synonym audit found zero prior matches. Current runtime: 80 fish (69 marine, 11 protected freshwater), ten marine coral entries, five invertebrates; six freshwater plants unchanged. Do not count the 25 designer phenotypes, five ART ONLY fish or three PLANNED creatures as added biological species. `CURRENT_LIVESTOCK_CATALOG.md` records every exact name, ID, rarity, difficulty, status, date, art path and limit. New animal artwork remains unapproved; 12 sheets carry framing flags. Invertebrate eggs/planktonic larval art remain partial.'),
    8: ('8.5 Named coral expansion', 'Add Blastomussa wellsi, Micromussa lordhowensis, Cyphastrea serailia, Leptastrea purpurea and Pavona cactus as separate stable species IDs, preserving the five older broad coral groups. Apply stony-coral host restrictions, light/flow, footprint, clearance and player-selected supported rock/rack placement; no unsupported midwater purchase or silent placement. Store scientific identity, rarity, living tissue, bleaching versus death and central value. Existing fragmentation is reused; no sexual reproduction claim.'),
    9: ('9.6 Separate non-fish residents', 'Thor amboinensis, Neopetrolisthes maculatus, Engina mendicaria, Conomurex luhuanus and Ciliopagurus strigatus live in a separate invertebrates array, never as generic fish. Persist identity, rarity, nutrition, condition, settled growth, age, death, treatment, position and transfer. Their crawling, tail sway, fan feeding and sand foraging use actual particles; leftovers/death pollute. Existing malnutrition/injury care is host-filtered through invertSupport; fish parasite/copper treatment is incompatible. This is a simplified game health model, not veterinary dosing. No planktonic larval rearing, egg art or reproduction is claimed.'),
    15: ('15.6 v2.7 breeding boundaries', 'New natural breeding is enabled only for Chalk Bass, Yellow Assessor, Blue Assessor, Greenbanded Goby and Sharknose Goby using the existing simplified system. Assessor presentation is protected oral brooding. The remaining 23 new fish have an explicit natural-breeding hold. All 28 may have species-identified Mystery Egg development with calibrated 48/72-game-hour incubation and authored larval art; this does not claim full real captive-culture success. New invertebrates have no egg/planktonic larval reproduction. Preserve all existing clownfish genetics, parent identities and unsupported designer holds.'),
    16: ('16.5 New livestock rarity and value', 'Use each central registry rarity exactly. New fish/corals/invertebrates reuse condition/stage/health-based asset value and bounded dealer offers. Non-fish bottom resident totals contribute once to tank value. Dead individuals have zero current value and retain immutable rarity in lineage history. New stock and specialist food prices are fixed game parameters. Rarity is a user-approved design assignment, not a conservation/trade status.'),
    24: ('24.5 Additive expansion migration', 'Expansion version 1 adds missing marine invertebrate arrays, ecosystem age, missing species stock, specialist-food inventory/stock and invertSupport stock once. Preserve existing fish/coral IDs, wallet, selected aquarium, daily listing IDs/calendar, RNG streams, disease histories and clown genetic profiles. Existing physical liters remain canonical; UI minimums use US gallons. Validate global animal IDs, host-specific health, stock, bounded toxin state and invertebrate positions/conditions. Persist invertebrateRng in offline checkpoints; include invertebrates in daily-care and offline-death/value summaries. No schema reset or freshwater species/biology expansion.'),
    27: ('27.5 v2.7 acceptance evidence', 'The dated LIVESTOCK_EXPANSION_REPORT.md maps all 24 requested acceptance items to actual results. Each browser passed 362 expansion checks and 7,583 artwork regression checks, zero failures. Evidence covers all 38 inspectors/rarities, save round trips, categories, actual six-tier Mystery purchases/hatching, safe destinations, coral support, non-fish treatment/transfer/death/offline value, eight daily slots, ten-day unchanged freshwater replay, 145 protected file hashes and no gameplay HTTP requests. Do not present older hardcoded roster/empty-pool milestone suites as current passes. Firefox and unsupported biological features were not tested as implemented.'),
    30: ('30.5 Permanent livestock logging and completion rule', 'Every future added livestock species MUST be logged in the permanent registry, CURRENT_LIVESTOCK_CATALOG.md, consolidated MDP and PDF/continuity source in the same batch. Required fields: common/scientific names, stable ID, category, rarity, care difficulty, planned/approved/implemented/art-only/partial status, batch, implementation date, art status, alive/dead support and honest notes. Never auto-approve artwork, hide missing stages or infer unsupported biology. PROJECT_CONTINUITY_SOURCE.md is the printable source; PDF_WORKFLOW.md records generation requirements. If tools cannot generate and verify a PDF, update the source and explicitly report PDF regeneration pending. Completion reports list changed files, species/duplicates, passed/failed/not-run tests, documentation and remaining limits; end the completed authorized editing task with the exact standalone line Done With Edits.')
}
for section, (title, text) in additions.items():
    title = subsection_labels.get(title, title)
    # Preserve the 31 major sections while maintaining the current batch subsections.
    master = re.sub(r'\n## ' + re.escape(title) + r'\n.*?(?=\n# \d+\.|\Z)', '\n', master, flags=re.S)
    marker = '\n# ' + str(section + 1) + '.'
    assert marker in master
    master = master.replace(marker, '\n## ' + title + '\n\n' + text + '\n' + marker, 1)
assert re.findall(r'^# (\d+)\.', master, re.M) == [str(n) for n in range(1, 32)]
subsections = re.findall(r'^## ([\d.]+) ', master, re.M)
assert len(subsections) == len(set(subsections)), 'Duplicate master subsection numbers'
assert 'no eligible Very Rare' not in master
write('MASTER_DEVELOPMENT_PROMPT.md', master)

baseline = load('tests/ecosystem-evidence/integrity.json')['protectedUnchanged']
for path, digest in baseline.items():
    assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest, path
integrity = {'date': '2026-10-14', 'masterVersion': '3.2', 'majorSections': 31, 'registryEntries': 38, 'duplicateEntries': 0, 'protectedUnchanged': baseline}
write('tests/expansion-evidence/integrity.json', json.dumps(integrity, indent=2))
assert len(baseline) == 145

results = []
for browser in ['chrome', 'edge']:
    for name, path in [('Expansion', f'tests/expansion-evidence/{browser}-results.json'), ('Artwork/clownfish regression', f'tests/{browser}-clownfish-results.json')]:
        result = load(path)
        assert result['failed'] == 0
        results.append(f"| {browser.title()} | {name} | {result['passed']:,} | {result['failed']} | [{path}]({path}) |")

changed = {
    'Central registry and new systems': 'assets/expansion-v27/registry.json; js/expansion-data.js; js/expansion.js; js/invertebrates.js; js/expansion-art-data.js; js/expansion-art.js; js/expansion-ui.js; js/expansion-review.js; expansion-review.html; assets/expansion-v27/<38 species>/{source-v1.png,atlas-v1.png,metadata-v1.json}; preserved source-v2.png for three corrected wrasses',
    'Shared runtime integration': 'js/core.js; js/simulation.js; js/save.js; js/store-rules.js; js/rarity.js; js/offline.js; js/gameplay.js; js/valuation.js; js/livestock-health.js; js/health-save.js; js/health-ui.js; js/store.js; js/render.js; js/brood-view.js; js/ui.js; js/app-shell.js; js/main.js; js/clownfish-review.js',
    'Local script loaders': 'index.html; clownfish-review.html; coral-placement-review.html; art-review.html; life-stage-review.html (where present, expansion loaders added without module/network dependencies)',
    'Verification and packaging': 'tests/expansion_checks.js; tests/expansion_qa.py; tests/browser_qa.py; tests/clownfish_checks.js; tests/clownfish_qa.py; tests/pack_expansion_art.py; tests/check_expansion_sources.py; tests/build_expansion_report.py; tests/package.py; tests/expansion-evidence/*; updated browser result JSON/screenshots',
    'Documentation': ', '.join(docs + ['MASTER_DEVELOPMENT_PROMPT.md', 'LIVESTOCK_EXPANSION_REPORT.md', 'PROJECT_CONTINUITY_SOURCE.md', 'PDF_WORKFLOW.md', 'ART_GENERATION_RECORD.md'])
}
changes = '\n'.join(f'- **{label}:** {files}.' for label, files in changed.items())
loaders = '; '.join(p.name for p in ROOT.glob('*.html') if 'js/expansion-data.js' in read(p.name))
changes = re.sub(r'- \*\*Local script loaders:\*\* .*', '- **Local script loaders:** ' + loaders + '.', changes)
flags = '\n'.join(f"- {r['name']} (`{r['id']}`): source cells {', '.join(map(str,art[r['id']]['clippedSourceCells']))} (zero-based)." for r in partial)
acceptance = [
    ('All 38 checked for duplicates', 'PASS — pre-registration catalog/runtime/store/art-metadata audit includes scientific synonyms; duplicate-audit.json'),
    ('No duplicate records', 'PASS — zero matches/skips; 38 distinct IDs and scientific identities'),
    ('Valid new IDs', 'PASS — canonical IDs, actual purchase/placement and save validation for each record'),
    ('28 new fish', 'PASS — all 28 registered and inspected; runtime fish total 80'),
    ('Five new corals', 'PASS — five species IDs, ten marine coral definitions total'),
    ('Five bottom dwellers', 'PASS — five separate non-fish definitions/owned records'),
    ('Rarity on every new entry', 'PASS — all approved rarity values checked'),
    ('Rarity in every inspector', 'PASS — actual dialogs opened for all 38 records'),
    ('Correct store/journal categories', 'PASS — daily Fish subset, ten coral products, five Bottom Feeders, marine encyclopedia and collection'),
    ('Gallon-based fish requirements', 'PASS — registry minimums and canonical liter conversion'),
    ('New livestock values', 'PASS — all species purchase/placement value checks, condition/death behavior'),
    ('Tank value integration', 'PASS — corals, fish and separate bottomDwellers contribution'),
    ('Disease/treatment compatibility', 'PASS — fish/stony/invert host filters, invertSupport and copper rejection, treatment/health save state'),
    ('Art stages available or marked partial', 'PASS WITH DISCLOSURE — 38 sheets/304 views load; twelve framing flags, no invertebrate egg/planktonic larval art; no user approval inferred'),
    ('Coral placement', 'PASS — supported real placement/save and rejection of unsupported midwater'),
    ('Non-fish bottom behavior', 'PASS — actual particle feeding, separate array, transfer, illness, death/pollution, value and offline survival'),
    ('Upper Mystery pools', 'PASS — all six real production pools and seeded purchase/reveal/save/hatch, including Very Rare, Ultra Rare, Legendary'),
    ('Eight visible rotation slots', 'PASS — 3 Common / 3 Uncommon / 1 Rare / 1 Mystery, no extra cards'),
    ('Save/load', 'PASS — all 38 real owned records survive validation and retain identities/rarities'),
    ('Permanent registry', 'PASS — canonical JSON and generated runtime copy, complete 38-row catalog and source paths'),
    ('PDF/source continuity', 'SOURCE UPDATED — MDP v3.2 / 31 sections and printable source; PDF regeneration pending unavailable tools'),
    ('No freshwater expansion', 'PASS — eleven fish/six plants retained, 145 protected hashes and exact ten-game-day replay unchanged'),
    ('Offline game', 'PASS — actual file:// browser execution, embedded local assets, no HTTP/HTTPS gameplay requests'),
    ('Existing saves', 'PASS — additive migration with missing expansion fields; selected tank, daily listings, wallet and existing identities preserved')
]
acceptance_table = '\n'.join(f'| {n}. {name} | {status} |' for n,(name,status) in enumerate(acceptance,1))
sources = '''- [ORA captive-bred Chalk Bass](https://www.orafarm.com/blog/2020/07/31/ora-chalk-bass/) supports using a simplified captive-spawning profile.
- [ORA Yellow Assessor](https://www.orafarm.com/product/yellow-assessor/) and [Blue Assessor](https://www.orafarm.com/product/blue-assessor/) support shelter/feeding profiles. [Western Australian Museum original Assessor review](https://museum.wa.gov.au/sites/default/files/A%20REVIEW%20OF%20THE%20PLESIOPID%20FISH%20GENUS%20ASSESSOR%2C%20WITH%20DESCRIPTIONS%20OF%20TWO%20NEW%20SPECIES.pdf) supports protected oral brooding, not the game's compressed timings.
- [University of Florida marine ornamental goby culture](https://ask.ifas.ufl.edu/publication/FA226) supports the two explicitly enabled new goby breeding profiles and attached-egg/larval distinctions.
- [LiveAquaria Purple Queen care](https://www.liveaquaria.com/products/queen-purple-anthias), [Top Shelf Aquatics specialist Filefish profile](https://topshelfaquatics.com/pages/saltwater-fish/orange-spotted-filefish), [Fluval Copperband profile](https://fluvalaquatics.com/uk/wp-content/uploads/2024/01/Species-Spotlight_Copperband-Butterflyfish_EN.pdf) and [Petco Boxfish care](https://s7d1.scene7.com/is/content/PETCO/public/finallib/ecom-team/petco/Caresheets/aquatic/caresheet-boxfish-and-cowfish-2016.pdf) inform special feeding/risk flags. Numeric requirements and toxin/health rates are game design inferences, not measured care guarantees.
- Approved names and rarity assignments come from the user's exact v2.7 list. Historical alias checks are retained in duplicate-audit.json. New rarity is not an asserted scientific scarcity ranking.
'''
report = f'''# Aquarium Life — livestock expansion v2.7 implementation report

Date: **2026-10-14**. Consolidated MDP: **v3.2**, exactly **31 major sections**.

Implemented all **38 approved additions: 28 marine fish, five named corals, five non-fish bottom dwellers**. **Zero duplicates, zero skipped species.** New runtime totals: 80 fish (69 marine / 11 freshwater), ten marine coral definitions, five invertebrates. Existing six freshwater plants, 31 clownfish names/25 designer phenotypes and historical art-only/planned studies are not new species in this batch.

## What changed

Purchases/placement, inspectors, store/journal categories, rarity, condition-based value, tank totals, host-filtered health, transfer, death history and additive save migration now support the new livestock. Five invertebrates have a separate owned-resident model, actual food consumption and non-fish movement. Specialized feeding, sand/shelter, predation, isolated Boxfish and coral-prey requirements participate in destination safety. The selected aquarium persists. All six Mystery Egg rarity pools are populated without changing exact odds, fixed price, existing eligibility or eight daily Fish cards.

## Exact species and permanent registry

Canonical [registry JSON](assets/expansion-v27/registry.json), generated `js/expansion-data.js`, [full catalog](CURRENT_LIVESTOCK_CATALOG.md). All entries are batch v2.7, implemented 2026-10-14. Catalog presence, natural breeding support and art approval remain separate claims.

{table}

## Files changed

{changes}

## Actual verification

| Browser | Suite | Passed | Failed | Evidence |
|---|---|---:|---:|---|
{chr(10).join(results)}

**7,945 passed / zero failed per browser; 15,890 checks across both browsers.** Artwork regression includes 1,792 directional cases per browser. Existing broad milestone suites with obsolete roster/empty-pool fixtures were not represented as new passes. During development one obsolete 52-fish assertion failed; it was updated to the authorized 80-record roster, then both final artwork runs passed. Two attempted invocations used an unsupported `--browser` argument and exited before launching; the documented positional commands below are the successful final runs.

Reproduce from the project folder:

```powershell
python tests/browser_qa.py chrome --expansion
python tests/browser_qa.py edge --expansion
python tests/browser_qa.py chrome --clownfish
python tests/browser_qa.py edge --clownfish
python tests/build_expansion_report.py
python tests/package.py
```

Commands launching headless browsers may require the host's existing browser-run approval. Direct `file://` use needs no install or server. Protected-file hashes: **145 unchanged**; exact ten-game-day freshwater simulation replay is unchanged. [Integrity evidence](tests/expansion-evidence/integrity.json). No HTTP/HTTPS gameplay requests or uncaught JavaScript errors in tested flows. Width checks cover 387, 681 and 1366 pixels. Chrome/Edge evidence includes actual store, mystery purchase, invertebrate inspector and gallery screenshots.

| Requested acceptance item | Result / evidence |
|---|---|
{acceptance_table}

Not run: Firefox (not installed); obsolete complete v2.6 ecosystem/gameplay/shell suites with superseded catalog assumptions; unimplemented natural breeding/sex-specific art features; native application fullscreen testing; PDF rendering (prerequisites unavailable). Historical test totals remain in their dated reports.

## Artwork and remaining limits

Built-in ImageGen produced 38 original transparent source sheets and three corrective wrasse edits. Source v1 masters are preserved; corrected source-v2 files are used for Pink-streaked, White-banded Possum and Tanaka's Pygmy Wrasse. The atlas packer only crops transparent gutters, rescales nearest-neighbor and packs frames. All 38 local sheets / 304 stage-state views load in both browsers. [Prompts and correction record](tests/expansion-evidence/art-prompts.json); [technical art audit](tests/expansion-evidence/art-audit.json); [review gallery](expansion-review.html). Every species' source/atlas/metadata is linked in the exact registry above.

All new art is **unapproved**. Twelve sheets have automated physical-boundary flags requiring visual review; a flag is a framing concern, not a confirmed anatomy diagnosis:

{flags}

Fish have authored egg/larva/juvenile/adult living and deceased poses, but static stage poses do not provide new fin cycles. Eye metadata is approximate/provisional. Flasher/fairy wrasses use male reference artwork; Spotted Boxfish uses female reference artwork; alternate sex art is not authored. Invertebrates cover **settled juvenile through adult** living/deceased, with **no egg or planktonic larval art/rearing/reproduction**. New natural fish breeding is supported only for Chalk Bass, Yellow Assessor, Blue Assessor, Greenbanded Goby and Sharknose Goby; the other 23 explicitly refuse invented natural breeding. Mystery Egg development is a calibrated presentation, not a captive-culture claim. Corals reuse fragmentation; no sexual reproduction system was added.

Care minimums, prices, maturity/lifespan, incubation, disease/support outcomes and Boxfish toxin kinetics are conservative game calibrations. They are not real-world dosing or stocking instructions. Existing five specialist clownfish purchase holds and older provisional art/taxonomic limits remain.

## Documentation and PDF status

Updated all six requested project documents, current catalog/fish index, README, test report, consolidated 31-section MDP, art-generation record and permanent registry. **PROJECT_CONTINUITY_SOURCE.md is updated; binary PDF regeneration remains pending.** Node CLI, ReportLab, pypdf/PyMuPDF and Poppler are unavailable, so no generated/render-verified PDF is claimed. [PDF_WORKFLOW.md](PDF_WORKFLOW.md) preserves the export prerequisites, source and permanent logging/completion rules near its back.

## Research boundaries

{sources}

## Portable delivery

Open [index.html](index.html) offline after extracting the entire `AquariumLife-v0.1.zip` folder. The retained archive name is historical; its contents include v2.7. Browser profiles/caches are excluded. `tests/package.py` rebuilds the archive and verifies CRC plus the offline entry point; its console result is the package verification, separate from browser test counts. Export a Settings JSON backup before moving a save between folders or browsers.
'''
report = report.replace('Width checks cover 387, 681 and 1366 pixels.', 'Width checks cover 390, 768, 1366 and 1920 pixels.')
write('LIVESTOCK_EXPANSION_REPORT.md', report)

continuity = f'''# Aquarium Life — printable project continuity source

Revision **v2.7 / MDP v3.2**, 2026-10-14. **PDF regeneration pending**; this is the maintained source, not an exported PDF. The consolidated master immediately follows the registry snapshot so the entire 31-section specification travels with this source.

## Current batch registry snapshot

38 approved unique additions, zero duplicates/skips. Current totals: 80 fish (69 marine / 11 freshwater), ten marine coral entries and five invertebrates; existing six freshwater plants unchanged. The canonical JSON is `assets/expansion-v27/registry.json`; this printable snapshot is generated from it.

{table}

## Verification and known limits

Chrome and Edge: 7,945 passed, zero failed per browser across expansion and artwork regression. See LIVESTOCK_EXPANSION_REPORT.md for the 24-item acceptance mapping and exact evidence. All new art is unapproved; 12 framing flags remain; invertebrate egg/planktonic larval artwork and reproduction are unsupported; 23 new fish natural-breeding profiles remain held. Five new fish use a simplified researched breeding model. Earlier provisional artwork and specialist clownfish purchase holds remain.

## Consolidated 31-section master

{master}

## Back-of-source continuity rules — permanent

Every future added livestock species must be logged in the central registry, current catalog, consolidated MDP and printable/PDF continuity source in the same batch. Record common/scientific name, stable ID, category, rarity, difficulty, implementation status, batch, date, art status, living/dead support, sources and limits. Do not duplicate synonyms, silently approve art or fabricate missing biological stages. Preserve freshwater biology and existing saves. Store selection must persist throughout shopping; unsafe purchases must not proceed. Retain the exact eight-card rotation and independent Mystery odds. Record actual tests and not-run work. When PDF export tools are unavailable, update this source and report regeneration pending explicitly. Completed editing reports must end with the exact standalone line Done With Edits.
'''
write('PROJECT_CONTINUITY_SOURCE.md', continuity)
workflow = '''# Aquarium Life — PDF workflow and continuity rules

Source revision: **2026-10-14, livestock v2.7 / MDP v3.2**.

## Current export status

**PDF regeneration is pending.** The environment does not provide Node CLI, ReportLab, pypdf/PyMuPDF or Poppler, so no PDF has been generated or render-verified for this batch. The user explicitly permits an updated source when direct PDF generation is unsupported.

`PROJECT_CONTINUITY_SOURCE.md` is the full maintained printable source: current 38-row registry snapshot, known limits and the complete 31-section consolidated master. `MASTER_DEVELOPMENT_PROMPT.md` remains the authoritative editable master; `assets/expansion-v27/registry.json` remains the authoritative species ledger. `tests/build_expansion_report.py` updates both the printable snapshot and related documentation from these sources after browser results exist. Do not treat an older binary PDF as current.

## Regeneration in a capable environment

1. Install/enable a permitted Node runtime, a PDF authoring tool and a PDF renderer; use the applicable PDF skill. Read its current SKILL.md rather than assuming an old script path still applies.
2. Run `python tests/build_expansion_report.py` after current browser checks to synchronize the registry and source.
3. Immediately before the first PDF-authoring operation, invoke the PDF skill's `container_tools/mark_artifact_operation_started.mjs` using Node with `--operation-kind create --expected-output-count 1 --output-format pdf`, as required by that skill. Resolve the script relative to the active PDF skill installation.
4. Typeset `PROJECT_CONTINUITY_SOURCE.md` as a readable document. Repeat long-table headings and wrap species names, notes and asset links. Preserve all 38 rows and 31 major master sections; do not shrink the complete catalog to illegible text.
5. Render every page with the permitted PDF renderer. Inspect for clipping, missing glyphs, broken table rows, orphan headings and adequate margins. Correct and rerender until clean. Verify text extraction retains all 38 stable IDs and the final continuity rule.
6. Save the verified PDF as `AquariumLife-Project-Continuity-v2.7.pdf`, record page count/export date and validation in LIVESTOCK_EXPANSION_REPORT.md, then update tests/package.py to include the verified PDF. Remove the pending status only after actual export and inspection.

## Back-of-workflow permanent rules

Every newly added livestock species MUST be logged in the permanent registry, CURRENT_LIVESTOCK_CATALOG.md, consolidated MDP and PDF/continuity source in the same update. Required fields: common name, scientific name, stable ID, category, rarity, care difficulty, planned/approved/implemented/art-only/partial status, update batch, implementation date, art status, living/dead support and honest notes. Synonyms must be checked before registration. Designer patterns do not add species counts.

Never automatically approve new artwork or conceal unsupported stages/reproduction. Preserve protected freshwater content, existing approved assets, saves and the selected store destination. Unsafe homes cannot receive automatic livestock placement. Keep eight daily Fish slots and independent Mystery odds unchanged unless separately authorized.

Record tests actually run, failures and not-run coverage. If PDF generation is unavailable, maintain this source and explicitly report regeneration pending. When authorized edits are complete, provide a concise report listing files, species, duplicates, tests, documentation and limits; end with the exact standalone line **Done With Edits**. Never use that completion line while authorized implementation work remains unfinished.
'''
write('PDF_WORKFLOW.md', workflow)

art_record = read('ART_GENERATION_RECORD.md')
marker = '## Livestock expansion v2.7 — generation record'
art_record = re.sub(r'\n' + re.escape(marker) + r'\n.*\Z', '', art_record, flags=re.S)
write('ART_GENERATION_RECORD.md', art_record + '\n\n' + marker + '\n\n2026-10-14: Built-in ImageGen produced 38 transparent species sheets plus three corrective wrasse edits. Source masters and prior versions are preserved in assets/expansion-v27/<id>/. The technical packer detects alpha gutters, nearest-neighbor scales and packs eight authored views without semantic repainting. All 304 views load offline. Prompts/correction notes: [art-prompts.json](tests/expansion-evidence/art-prompts.json). All new art is unapproved; twelve framing flags, provisional eyes and unsupported invertebrate egg/planktonic larval artwork are explicitly recorded in [the report](LIVESTOCK_EXPANSION_REPORT.md). Review [the gallery](expansion-review.html).')
print(f'Synchronized {len(records)} registry entries; {len(partial)} framing flags; 31 MDP sections; {len(baseline)} protected files unchanged. PDF export pending.')
