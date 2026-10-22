"""Maintain the authorized v2.9 ledgers and consolidated, 31-section handoff.

Does not generate artwork, change player saves, approve art or claim unrun tests.
"""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
def read(name): return (ROOT/name).read_text(encoding='utf-8')
def write(name, value): (ROOT/name).write_text(value.rstrip()+'\n', encoding='utf-8')

if 'VERSION 3.5' in read('MASTER_DEVELOPMENT_PROMPT.md'):
    raise SystemExit('v2.9 documentation migration already applied; edit current documents directly.')

AUTH = ('**Authorized 2026-10-14:** The user approved the complete 25/5/5 roster and rarities, '
        'confirmed saltwater-only, and explicitly requested "Implement v2.9". '
        'Roster approval and artwork approval are separate; new artwork remains unapproved. '
        '[Authorization](planning/v2.9/approval.json).')
SUMMARY = ('Implemented the twelve-step saved/skippable saltwater tutorial with medical guidance, '
           'three-second selection outlines, disabled freshwater UI, separate +50 healthy / +200 survival rewards '
           'with persistent death/recovery tracking, Deep Market display rename, local asset-value leaderboard '
           'preview, exact 15,000-US-gallon / 5,000-AC aquarium, proportional water-change salt consumption, '
           'independent mystery products and the approved 35-species marine batch. '
           'Saves remain local to each player\'s browser on their PC. '
           'The bottom mystery product is content-held because its Legendary host specialist is not eligible. '
           'See [V29_UPDATE_REPORT.md](V29_UPDATE_REPORT.md) for actual checks, care/art limits and release details. '
           'Earlier milestone sections below are historical wherever superseded.')

ledger = json.loads(read('assets/expansion-v29/registry.json'))
ledger['status'] = 'IMPLEMENTED additive saltwater batch; original art awaits user review; Coleman acquisition held'
for r in ledger['records']:
    r['implementationStatus'] = ('REGISTERED; ACQUISITION HELD pending required fire-urchin host support'
                                 if r['purchaseVerified'] is False else 'IMPLEMENTED; game care calibration; art not user approved')
    r['art']['status'] = 'Original eight static stage/state views; not user approved'
write('assets/expansion-v29/registry.json', json.dumps(ledger, ensure_ascii=False, indent=2))
write('js/update29-data.js', '"use strict";\nAL.Update29Data='+json.dumps(ledger,ensure_ascii=False,separators=(',',':'))+';')

table = ['| Common / scientific name / stable ID | Category / approved rarity / care | Batch / status | Art |',
         '|---|---|---|---|']
for r in ledger['records']:
    table.append(f"| {r['name']} / *{r['scientificName']}* / `{r['id']}` | {r['category']} / {r['proposedRarity']} / {r['proposedCareDifficulty']} | v2.9 / 2026-10-14 / {r['implementationStatus']} | [8 stage/state views]({r['art']['atlas']}); NOT APPROVED |")
TABLE = '\n'.join(table)

def clean_header(s):
    s = re.sub(r'\n\*\*Approval recorded 2026-10-14:\*\*[^\n]+\n', '\n', s, count=1)
    s = re.sub(r'\n## Future v2\.9[^\n]*\n.*?(?=\n## |\Z)', '\n', s, count=1, flags=re.S)
    return s

bodies = {
 '2.6': ('v2.9 Authorization and Freshwater Lock', AUTH+' Freshwater creation, selection, purchases and shared interaction controls display `Freshwater — Coming in a Future Update.` Existing definitions, artwork, saved residents and biological simulation remain retained. Future development milestones must ask whether freshwater is next; the current answer authorizes saltwater-only v2.9.'),
 '3.12': ('v2.9 Artwork', '35 original transparent sprite sheets provide 280 static stage/state views: appropriate early equivalents, baby/larva, juvenile/growing, adult/mature and their authored deceased states. Fish/shrimp art faces right and mirrors as a complete sprite when moving left. Original generated files and prompts are retained. Technical alpha cropping and nearest-neighbor packing do not repaint specimens. One source-boundary review flag and provisional eye metadata remain; no automatic approval or claim of complete swim/feeding animation. Review v29-review.html and assets/expansion-v29/art-generation-record.json.'),
 '4.6': ('15,000-US-Gallon Aquarium', 'Ocean Sanctuary is exactly 56,781.17676 L of simulation water and costs exactly 5,000 AC total for marine purchase at Keeper Level 10, without a 1.25 markup. It starts empty/dry. Defined water envelope: 1,000 × 400 × 141.9529419 cm, substrate area 40 m². Saved water remains the usable game capacity; sand/rock displacement and structural engineering are not modeled. Freshwater is future-locked. Installed equipment scales to actual volume through existing price/capacity/energy/service formulas; filter capacity must cover volume, reef lighting and flow must meet selected livestock profiles. Shell value uses the 5,000-AC base. Water preparation, substrate, shelter, cycling and compatible livestock are separate purchases.'),
 '5.6': ('Beginner Saltwater Tutorial', 'New Game starts a twelve-step guide: six windows, first empty tank/value, substrate/depth, saltwater, equipment, supported rock/depth, real cycling, safe beginner fish, feeding/inspection, medical example/diagnostics/quarantine/legitimate medicine, maintenance/rewards, and the implemented First safe beginning achievement. Next/Back/Show me/Skip, saved Resume and Settings Restart work without forced illness, treatment, purchases or skipped cycling. The overlay highlights available real controls and remains usable over modal windows. Completing text never grants unearned rewards.'),
 '6.5': ('Approved v2.9 Marine Species', 'Exactly 25 fish, five corals and five non-fish bottom dwellers were approved with their rarities before implementation. Additive stable IDs, accepted-name/alias checks, original art, game care profiles, diets, habitat checks, health, value and saves are registered in assets/expansion-v29/registry.json. All three categories contain T5 and T6. Coleman’s shrimp is registered but acquisition-held: its obligatory fire-urchin host is unsupported. No 36th host species was invented. Earlier 38-entry registry, clownfish/designer identities and prior art-only subjects remain preserved. Current totals: 105 fish (94 marine/11 retained freshwater), 15 marine corals, 10 non-fish marine invertebrates, six retained freshwater plants. Rarity is not care difficulty or conservation status.\n\n'+TABLE),
 '9.10': ('Three-Second Livestock Outline', 'Selecting fish, corals, invertebrates or nurseries sets a performance-clock deadline exactly three real seconds after the latest selection. Reclicking resets it; another selection transfers it; switching aquariums clears it. Rendering reads the deadline, so game speed or pause cannot prolong it. The inspector remains open and usable after the outline expires.'),
 '12.6': ('Proportional Water-Change Cost Audit', 'Changed liters = actual saved volume × fraction. Preserve marine water ceil(changed L × 0.13 AC), freshwater water ceil(changed L × 0.04 AC) and existing freshwater conditioner biology. Marine salt is one dose per two changed liters, rounded up, minimum one. Smallest actual catalog tank is 20 L (ceil label 6 gal): 10% changes 2 L, costs 1 AC and one salt dose. Ocean Sanctuary 10% changes exactly 5,678.117676 L: 739 AC water + 2,840 salt doses. Salt packs are 35 AC/10 doses, so 284 packs cost 9,940 AC; combined replacement cost 10,679 AC before energy, food, medicine or repairs. No blanket treatment charge is invented. Preparation, clinical courses and maintenance retain their own rules. This exceeds the approved shell price; see BALANCE_REPORT.md. Never secretly change the 5,000-AC price.'),
 '16.8': ('Local Leaderboard Preview', 'Field Journal → Leaderboards offers Saltwater Leaderboard and a locked Freshwater Leaderboard preview, without a seventh sidebar window. Only the player’s owned marine tanks are locally compared, clearly labeled local/preview. The metric is AL.Valuation current installed aquarium assets, excluding wallet and uninstalled inventory, counted once. No accounts, public submissions, remote saves, servers or fake players. Future competitive rankings need verified server-authoritative values.'),
 '17.7': ('Separate Livestock Survival Bonus', 'Healthy-day +50 AC remains separate from +200 AC survival, each at most once per qualifying player-wide game day, never per tank. Survival requires genuine fully tracked stocked simulation over 1,440 game minutes, no confirmed fish/coral/invertebrate/nursery death and completion of recovery. Every confirmed loss cancels the day and restarts lastDeath + 1,440 minutes; a later complete qualifying day may pay. Illness and living bleaching are not deaths. Dead legacy residents are marked processed during migration. Persistent lastCompleted/lastPaid, counters, loss time, recovery deadline and earned totals prevent reload replay. Offline steps evaluate the same rules; backward clock changes do not rewind the simulation checkpoint. Local device clocks cannot be cryptographically trusted. Notifications remain separate and Tank History shows progress. At 1×, one game day remains twenty real minutes.'),
 '18.9': ('Mystery Coral and Bottom-Dweller Egg', 'Saltwater Corals lists Mystery Coral (450 AC); Bottom Feeders lists Mystery Bottom-Dweller Egg (500 AC). Each has a separate persistent PRNG and independent exact T1–T6 odds 50/25/15/7.5/2/0.5%. All six implemented eligible tier pools and safe destinations are checked before charge or RNG use; missing tiers visibly hold purchase, never substitute or reweight. Three daily units each do not enlarge the eight Fish slots. Coral requires player-chosen supported mounting before purchase and resolves to a living frag. Bottom outcomes use a clearly labeled brooded/larval nursery abstraction for 48 suitable hours, then settle once as the same-ID small juvenile; viability/death/value/capacity reservations persist. Natural reproduction is not claimed. Production bottom purchase is content-held because the Legendary Coleman host specialist is not eligible. Conditional complete-pool QA verifies development without releasing that species. Outcomes, rarity rolls, identity, health, stage, provenance and mounts save without reroll.'),
 '19.5': ('Deep Market Display Name', 'Every current player-facing market heading, message, reputation description and buying/selling label uses Deep Market. Existing black internal IDs, legacy save fields, hidden saved dealer condition/medicine quality, prices, opening hours, reputation, inventory and diving resale remain compatible. Deep Market stays inside Aquarium Store. Eligible upper-tier new corals/invertebrates use saved dealer listings; ordinary direct livestock remains T1–T3.'),
 '24.6': ('v2.9 Local Persistence', 'Schema-2 saves receive additive version-1 update29 tutorial, survival and daily mystery extensions, independent RNG fields and marine nursery arrays. Migration adds inventory/stock and required new market listings without rerolling existing listings, fish slots, old individuals or reputation. Validation rejects invalid extension states, duplicate identities and forged new mystery roll/rarity pairs. Selected aquarium remains authoritative through store opening/closing/tabs/purchases and save/load. Autosave/backup and user JSON export/import remain on the player’s PC in browser localStorage/downloads. Browser/site/profile storage is separate; export/import moves progress between origins. No cloud or server saves. build.py refreshes DIST and Pages ZIP; tests/package.py refreshes the source ZIP.'),
 '27.15': ('v2.9 Acceptance Evidence', 'Actual executed results and the complete original 35-item checklist are mapped in V29_UPDATE_REPORT.md and tests/update29-evidence. Browser checks exercise actual New Game/tutorial controls, reload, selection deadline, store destination, safe coral placement, held bottom product, both leaderboard views, achievement claim and large-tank purchase. Model checks exercise genuine fixed-step/offline rewards, all coral CDF boundaries, nursery persistence/settlement, recovery, transaction rollback and save validation. Source art was visually inspected but is NOT user approved; artwork approval is still an explicit limit. Earlier 31 major sections, protected art/definitions and retained freshwater replay are verified. Report only actual tests; historical failures/fixture adjustments are disclosed.'),
 '30.5': ('v2.9 Continuity and Locked Additions', 'Maintain one consolidated 31-section MDP, current catalog, old/new permanent registries, GAME_DESIGN, UI_SPECIFICATION, ART_DIRECTION, DEVELOPMENT_STATUS and BALANCE_REPORT. Verbatim original requirements and the original proposal remain archived under planning/v2.9; approval.json records later explicit implementation authorization. Never confuse registered/acquisition-held, implemented or art-approved status. Keep the complete 35-row new ledger and prior 38-row ledger in the continuity source with the full MDP and back-of-source rules. Binary PDF regeneration remains pending unsupported authoring/rendering tooling. Preserve future freshwater authorization checks, twenty-minute days, local saves, six windows, Deep Market identity compatibility, exact rewards/odds, large-tank price and volume maintenance, and all prior locked rules. Completed authorized edit reports identify files/features/species/tests/limits/docs, then use the exact completion line.')
}

mdp=read('MASTER_DEVELOPMENT_PROMPT.md')
first=mdp.index('# 1. ROLE')
mdp=('# AQUARIUM LIFE\n\n## COMPLETE MASTER DEVELOPMENT PROMPT — VERSION 3.5\n'
     '### Offline Browser Edition — playable v2.9, 2026-10-14\n\n'+AUTH+'\n\n'+SUMMARY+'\n\n---\n\n'+mdp[first:])
for number,(title,body) in bodies.items():
    pattern=r'^## '+re.escape(number)+r' [^\n]+\n.*?(?=^## |^# |\Z)'
    mdp,count=re.subn(pattern,lambda m:'## '+number+' '+title+'\n\n'+body+'\n\n',mdp,count=1,flags=re.M|re.S)
    assert count==1,number
mdp=mdp.replace('BLACK MARKET','DEEP MARKET').replace('Black Market','Deep Market').replace('Black-Market','Deep-Market').replace('black market','Deep Market')
assert [int(n) for n in re.findall(r'^# (\d+)\. ',mdp,re.M)]==list(range(1,32))
write('MASTER_DEVELOPMENT_PROMPT.md',mdp)

special={
 'CURRENT_LIVESTOCK_CATALOG.md': 'Current totals: **105 fish (94 saltwater / 11 retained freshwater), 15 marine coral records, 10 non-fish marine invertebrates and six retained freshwater plants.** Five generic legacy coral groups remain legacy identities, not newly verified biological species. Designer clownfish patterns are varieties, not species. Coleman’s shrimp is registered/acquisition-held.\n\n'+TABLE,
 'GAME_DESIGN.md': 'Tutorial, care/survival rewards, preview ranking and new mystery purchases use the actual simulation and transaction rules. Saltwater-only applies to this milestone. Retained freshwater biology is regression tested through an isolated test adapter; the production UI and transactions stay locked.',
 'UI_SPECIFICATION.md': 'Keep six main windows. Settings contains Resume/Restart Tutorial. The guide can Skip/Back/Next/Show me and highlights actual available controls over native dialogs. Expiring three-second outlines do not close inspectors. Freshwater controls are disabled with the coming-update message. Field Journal contains local Leaderboards and survival progress in Tank History. Store coral purchase asks for a valid supported mount before completing.',
 'ART_DIRECTION.md': '35 original generated species sheets / 280 static stage-state views are integrated, with source originals, prompts, atlases and metadata. All remain NOT USER APPROVED. Original approved Ocellaris clownfish art and older batches are preserved. Five contact pages were visually inspected. One source-boundary flag (Yellow scroll coral adult), provisional eye-coordinate metadata, static poses and stylized earliest developmental equivalents are disclosed. Do not claim validated captive breeding, sex-specific poses or full animation. Review [v29-review.html](v29-review.html).',
 'DEVELOPMENT_STATUS.md': 'Playable v2.9 / MDP v3.5. Approved batch registered additively; Coleman’s shrimp and bottom mystery purchase remain explicitly held. New artwork is unapproved. Final test evidence and current DIST hashes are recorded in V29_UPDATE_REPORT.md and DIST/build-manifest.json. Binary PDF regeneration remains pending; the complete printable source is current.',
 'BALANCE_REPORT.md': 'Ocean Sanctuary: 15,000 US gal = 56,781.17676 L, shell purchase exactly 5,000 AC. Existing 5,000-L Ocean Hall costs 27,000 base / 33,750 marine: the approved new shell creates a deliberate documented price inversion. A 10% change needs 739 AC water and 2,840 salt doses (284 packs × 35 = 9,940 AC), **10,679 AC total** before power, feeding and repairs: 42.716 ideal 250-AC bonus days, about 14.24 real hours at 1×. One such weekly change averages 1,525.57 AC/game day, far above both bonuses combined; it requires other income. The 20-L baseline stays 1 AC + one salt dose for 10%. Mystery Coral 450 / bottom nursery 500 AC are disclosed game calibrations with three daily stock each. Rarity is independent of care. Numeric care, nutrition, incubation and budgets are conservative game parameters, not real husbandry advice.',
 'PDF_WORKFLOW.md': 'Current printable source contains the old 38-row ledger, new 35-row implemented/held ledger and the complete MDP v3.5 with all 31 sections and permanent handoff rules. **Binary PDF export/render verification remains pending.** No new PDF is claimed. Future export must retain these statuses, all 73 batch IDs, back-of-source rules and art limits. Do not run historical generators that overwrite this source.'
}
for name,extra in special.items():
    s=clean_header(read(name));pos=s.find('\n')
    s=s[:pos]+'\n\n'+AUTH+'\n\n## v2.9 — current implementation\n\n'+SUMMARY+'\n\n'+extra+'\n\n## Earlier milestone record\n'+s[pos:]
    write(name,s)

for name in ['README.md','TEST_REPORT.md','ART_GENERATION_RECORD.md','GITHUB_PAGES_BUILD_REPORT.md']:
    s=read(name)
    if '## v2.9 — current implementation' not in s:
        pos=s.find('\n');s=s[:pos]+'\n\n## v2.9 — current implementation\n\n'+SUMMARY+'\n\nSee [the current release report](V29_UPDATE_REPORT.md), [new art gallery](v29-review.html), [DIST](DIST/) and [build manifest](DIST/build-manifest.json).\n\n## Historical milestone record\n'+s[pos:]
        write(name,s)

proposal=read('FUTURE_V29_PLAN.md')
if '## Later implementation authorization' not in proposal:
    write('FUTURE_V29_PLAN.md','# v2.9 proposal — archived planning record\n\n## Later implementation authorization\n\n'+AUTH+'\n\nThis retained proposal describes the earlier planning state, not current runtime. Its pending-authorization/no-art/no-build statements are historical and superseded by [V29_UPDATE_REPORT.md](V29_UPDATE_REPORT.md). The original candidate ledger remains an unchanged planning snapshot; the implementation ledger is assets/expansion-v29/registry.json.\n\n---\n\n'+proposal)

# Retain the old full species table and established back-of-source rules.
continuity=read('PROJECT_CONTINUITY_SOURCE.md')
oldtable_start=continuity.index('## Permanent v2.7 roster baseline')
oldtable_end=continuity.find('## ',oldtable_start+3)
oldtable=continuity[oldtable_start:oldtable_end]
back=continuity[continuity.index('## Back-of-source permanent continuity rules'):]
back=back.split('\n\nFuture v2.9 remains planning only')[0]
back+='\n\n'+bodies['30.5'][1]+' Future development must ask whether freshwater is next; current v2.9 scope remains saltwater-only. Artwork approval is never inferred from roster approval.\n'
write('PROJECT_CONTINUITY_SOURCE.md','# Aquarium Life — printable continuity source\n\nPlayable v2.9 / MDP v3.5, 2026-10-14. Binary PDF regeneration pending.\n\n'+AUTH+'\n\n'+SUMMARY+'\n\n'+oldtable+'\n\n## Permanent v2.9 additive ledger\n\n'+TABLE+'\n\n'+mdp+'\n\n'+back)

# Verify retained assets against the pre-implementation snapshot, not changed runtime/DIST.
before=json.loads(read('planning/v2.9/protected-before.json'))
protected={p:h for p,h in before.items() if p.startswith('assets/')}
changed=[p for p,h in protected.items() if not (ROOT/p).is_file() or hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h]
assert not changed,changed
write('tests/update29-evidence/protected-assets.json',json.dumps({'retainedAssetFiles':len(protected),'changed':changed,'freshwaterDefinitionFileUnchanged':hashlib.sha256((ROOT/'js/data.js').read_bytes()).hexdigest()==before['js/data.js']},indent=2))
print('Updated 31-section MDP v3.5, catalogs, six project documents and printable continuity; retained assets:',len(protected))
