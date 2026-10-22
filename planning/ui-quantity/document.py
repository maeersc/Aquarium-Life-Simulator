from pathlib import Path
import re
R=Path(__file__).resolve().parents[2]
p=R/'MASTER_DEVELOPMENT_PROMPT.md';old=p.read_text(encoding='utf8');s=old.replace('VERSION 4.14','VERSION 4.15',1).replace('playable v4.3.0','playable v4.3.1',1)
quantity='Store Quantity Rule: The Aquarium Store supports multi-quantity purchasing where appropriate, with clear unit price, quantity, and total cost display. Bulk purchasing must not bypass inventory, ownership, receiving, compatibility, or transaction integrity rules.'
background='UI Background Rule: Aquarium Life uses a black base UI background with a subtle low-contrast dark-grey fish-scale texture overlay. The fish-scale pattern points downward and is used only in general interface background areas, not inside the aquarium tank scene.'
preserve='UI Preservation Rule: UI polish updates should refine the current Aquarium Life layout and styling rather than redesigning the game into a different interface structure.'
s=s.replace('Prevent double-click duplication.','''Prevent double-click duplication.

'''+quantity+'''

The shared StoreRules policy/quote validates integer quantities1–99, actual stock, wallet and inventory capacity inside the existing cloned Core.act transaction. Equipment, food packs, consumable supply packs, ordinary medical packs, rated service parts and ordinary rocks support bulk. One total debit/receipt; separate physical equipment/rock identities; original supply dose semantics. Multiple rocks enter ordinary Inventory for separate safe placement; one rock retains direct placement. Sand, decorations and mounted racks remain one installation/placement; reusable tools one owned tool; restricted medicine one quality-bearing batch. Livestock keep the existing resident-count compatibility system or individual assessment/placement, mystery roll and pair-offer authorities. No generic livestock bulk override. Details explain restrictions and show unit price, quantity and total. Deep Market equipment uses this same policy; access/hours remain enforced. Replay keys survive the recent100 transaction window through the existing financial receipt index. Optional receipt quantity/unitPrice/totalCost/itemIds preserve schema2 compatibility. See STORE_QUANTITY_RULES.md and UI_POLISH_QUANTITY_REPORT.md.
''',1)
s=s.replace('Black/near-black background.',background+'\n\n'+preserve+'''

The page and sidebar use a black#000 base with one static64×32 SVG tile: hanging quadratic scallops, dark-grey#16191d strokes at45% opacity. No animation, JavaScript drawing or aquarium Canvas overlay. Panels remain solid slate-blue, with protected navigation labels/buttons. Utility/header alignment, panel padding, field spacing, selected/hover/focus states and store button heights retain the familiar layout. See UI_SPECIFICATION.md and UI_POLISH_QUANTITY_REPORT.md.''',1)
s=s.replace('## 24.16 Graphics Preference Persistence','''## 24.17 Store Quantity Persistence

Quantity purchasing retains main schema2 and all authoritative inventory arrays, stock maps, medicine batches, rated part stacks, local checkpoints and wallet sequence. New receipt metadata is additive; historic receipts are never rewritten. A rejected draft cannot partially charge or deliver. Successful purchases use existing immediate local saving and finance anti-rollback checks. No server/account service is introduced.

## 24.16 Graphics Preference Persistence''',1)
s=s.replace('# 28. DEVELOPMENT ROADMAP & EXECUTION ORDER','''## 27.22 UI Polish and Quantity Acceptance

Use tests/browser_qa.py --ui-quantity for actual offline native-input controls, immediate totals, integer/funds/stock/storage failures, distinct equipment IDs, supply/medical/part stacks, rock storage/placement, single-item safeguards, financial reconciliation, replay after recent-token eviction, local reload and destination retention. Capture1920×1080,1600×900,1366×768 and390×844. Verify downward scale orientation visually, opaque panels, unaffected Canvas and an identical-scene pattern-off/on render sample. Preserve full tutorial, economy, Pages/local-save, equipment/offline and performance regressions; record actual outcomes in UI_POLISH_QUANTITY_REPORT.md.

# 28. DEVELOPMENT ROADMAP & EXECUTION ORDER''',1)
assert len(re.findall(r'^# \d+\.',s,re.M))==31
p.write_text(s,encoding='utf8')
lead='''## UI polish and store quantities — 2026-10-22

Playable v4.3.1 / master v4.15. The familiar aquarium layout now uses a very subtle static downward fish-scale background, opaque slate-blue panels and consistent controls. The existing guarded store supports quantities for equipment, food, consumables, ordinary medicines, rated parts and rocks. Multiple rocks enter Inventory for separate placement; sensitive livestock, unique tools and installations retain their established individual safeguards. One total charge, distinct physical IDs, capacity/stock checks, persistent receipt replay protection and local saving remain authoritative. Main schema2/tutorial2, biological simulation, economy rates, offline time and freshwater lock are unchanged. STORE_QUANTITY_RULES.md defines category behavior; UI_POLISH_QUANTITY_REPORT.md records files, actual tests and limitations. Earlier release sections below are historical where superseded.

'''
for f in ['UI_SPECIFICATION.md','DEVELOPMENT_STATUS.md','README.md','FINANCIAL_TRANSACTIONS.md','EQUIPMENT_INVENTORY.md','TEST_REPORT.md','GITHUB_PAGES_BUILD_REPORT.md']:
 p=R/f;content=p.read_text(encoding='utf8');i=content.index('\n')+1;p.write_text(content[:i]+'\n'+lead+content[i:].lstrip('\n'),encoding='utf8')
p=R/'PROJECT_CONTINUITY_SOURCE.md';content=p.read_text(encoding='utf8');assert content.count(old)==1;content=content.replace(old,s,1);i=content.index('\n')+1;content=content[:i]+'\n'+lead.replace('Earlier release sections below are historical where superseded.','The exact complete31-section master is embedded below. Earlier release sections are historical where superseded.')+content[i:].lstrip('\n');p.write_text(content,encoding='utf8')
p=R/'FINANCIAL_TRANSACTIONS.md';p.write_text(p.read_text(encoding='utf8')+'''
## Quantity receipts — v4.3.1

The existing Finance.begin context attaches quantity, unitPrice and totalCost for supported products. Equipment and rock receipts also record newly created itemIds. Existing receipt category, action, tank, sequence, before/after wallet and time remain unchanged. Core.act checks the existing permanent finance.keys as well as recent transaction tokens before replaying a settled action. Each bulk action performs one Finance.change; failure discards its entire cloned draft. There is no nested per-unit financial transaction. Older receipts do not require new fields. Existing financial rollback protection remains. See STORE_QUANTITY_RULES.md.
''',encoding='utf8')
p=R/'EQUIPMENT_INVENTORY.md';p.write_text(p.read_text(encoding='utf8')+'''
## Quantity delivery — v4.3.1

Each purchased equipment unit receives a different permanent ID and independent new reliability state, fixed/rated capacity and thermostat. A bulk order must fit all50 stored slots. Rocks bought in multiples enter the existing100-object ordinary storage; each piece is placed through existing compatibility/placement validation. Single rocks keep the established direct placement flow. No stored item supplies life support. Supply packs add their existing portions/doses; ordinary medical packs merge to1000 units per batch before creating further batches within the80-batch cap. Rated service parts remain stacks keyed by SKU and capacity, capped10000. All orders validate full stock, capacity and funds before commit.
''',encoding='utf8')
