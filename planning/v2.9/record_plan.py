"""Record documentation only. Never register species, build, or edit the game."""
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
DATE = '2026-10-14'
TIERS = ['Common', 'Uncommon', 'Rare', 'Very Rare', 'Ultra Rare', 'Legendary']


def read(name):
    return (ROOT / name).read_text(encoding='utf-8')


def write(name, value):
    (ROOT / name).write_text(value, encoding='utf-8')


def jread(name):
    return json.loads(read(name))


def insert_notice(name, body):
    text = read(name)
    marker = '## Future v2.9 — planning only; implementation NOT authorized'
    if marker in text:
        return
    first, rest = text.split('\n', 1)
    write(name, first + '\n\n' + marker + '\n\n' + body + '\n\n' + rest.lstrip('\n'))


def main():
    if (HERE / "approval.json").exists():
        raise SystemExit("Roster approval is recorded. Preserve approved documents; this initial proposal generator must not reset approval state.")
    prior = jread('assets/expansion-v27/registry.json')['records']
    s = read('js/clownfish-collection-data.js')
    clowns, _ = json.JSONDecoder().raw_decode(s[s.index('{'):])
    old_art = jread('assets/livestock/life-stages/catalog.json')
    assert len(prior) == 38 and len(clowns['species']) == 31
    names, ids = set(), set()
    def add(record):
        ids.add(record['id'])
        for n in [record.get('scientificName'), *record.get('aliases', [])]:
            if n:
                names.add(n.casefold().strip())
    for r in [*prior, *clowns['species'], *old_art]:
        add(r)
    # These existing subjects already have authored art and cannot be new candidates.
    for i, n in [('niger-triggerfish','Odonus niger'),('emperor-angelfish','Pomacanthus imperator'),
                 ('red-lionfish','Pterois volitans'),('dogface-puffer','Arothron nigropunctatus'),
                 ('blue-tang','Paracanthurus hepatus')]:
        add({'id':i,'scientificName':n})
    # Exclusion-only identities inferred from unambiguous legacy common names.
    # Do not write these into runtime taxonomy or pretend the generic corals are identified.
    legacy = ['Gramma loreto','Nemateleotris magnifica','Cryptocentrus cinctus',
              'Pterapogon kauderni','Chromis viridis','Zebrasoma flavescens',
              'Pseudocheilinus hexataenia','Ecsenius stigmatura','Calloplesiops altivelis']
    names.update(n.casefold() for n in legacy)
    # All base IDs, including freshwater and flora, are reserved even without scientific names.
    ids.update(re.findall(r"fish\('([^']+)'", read('js/data.js')))
    ids.update(['zoa','mushroom','sps','lps','soft','fern','anubias','sword','moss','vallis','crypt'])
    proposed, seen = [], set()
    for category, common, scientific, tier, care, notes, aliases in jread('planning/v2.9/candidate-input.json'):
        ident = scientific.lower().replace(' ', '-')
        identity = {n.casefold() for n in [scientific, *aliases]}
        assert not identity & names, f'Existing species collision: {scientific}'
        assert not identity & seen, f'Candidate synonym collision: {scientific}'
        assert ident not in ids, f'Existing ID collision: {ident}'
        seen.update(identity)
        proposed.append(dict(id=ident, name=common, scientificName=scientific,
            category=category, water='marine', proposedTier=tier, proposedRarity=TIERS[tier-1],
            proposedCareDifficulty=care, aliases=aliases, batch='v2.9-proposal-1',
            approvalStatus='PENDING USER REVIEW', approved=False,
            implementationStatus='NOT IMPLEMENTED', implementationDate=None,
            artStatus='NOT STARTED; no artwork approved', aliveDeadSupport='NOT IMPLEMENTED',
            lifeStageStatus='Research and biologically appropriate art pending approval',
            taxonomySource='https://www.marinespecies.org/aphia.php?p=taxlist&tName='+quote(scientific),
            reviewed=DATE, notes=notes))
    counts = Counter(r['category'] for r in proposed)
    assert counts == {'fish':25,'coral':5,'bottom_dweller':5}
    for category in counts:
        tiers = {r['proposedTier'] for r in proposed if r['category']==category}
        assert {5,6} <= tiers
    ledger = dict(version=1, milestone='v2.9', status='PLANNING ONLY — NOT AUTHORIZED',
                  runtimeBaseline='v2.8', scope='Saltwater only; confirmed by user on '+DATE,
                  registrationPolicy='Documentation-only proposed records; never load into AL.Data or a store.',
                  approvalGate='Explicit roster/rarity approval AND separate implementation authorization required.',
                  counts=dict(counts), records=proposed,
                  duplicateCheckLimits='Source-reviewed aliases, current IDs, 38-entry ledger, 31 clownfish records, 25 designer varieties as exclusions, five art-only subjects and legacy common-name exclusions. Generic coral groups cannot prove a precise species identity; no species identification or renaming of those groups is claimed. This is not an exhaustive worldwide synonym database or certified care guide.')
    write('planning/v2.9/candidate-registry.json', json.dumps(ledger, ensure_ascii=False, indent=2)+'\n')
    tables = []
    for category, label in [('fish','25 proposed saltwater fish'),('coral','Five proposed corals'),('bottom_dweller','Five proposed bottom dwellers')]:
        rows = ['| # | Common / scientific name | Proposed rarity | Care | Proposed stable ID |',
                '|---|---|---|---|---|']
        for n,r in enumerate((r for r in proposed if r['category']==category),1):
            rows.append(f"| {n} | {r['name']} / *{r['scientificName']}* | T{r['proposedTier']} — {r['proposedRarity']} | {r['proposedCareDifficulty']} | `{r['id']}` |")
        tables.append('## '+label+'\n\n'+'\n'.join(rows))
    proposal = '''# Aquarium Life — v2.9 livestock proposal and planning record

Recorded 2026-10-14. **PLANNING ONLY. No gameplay implementation is authorized.** The user confirmed **Keep v2.9 saltwater-only** during planning. The current playable release remains **v2.8**; the consolidated documentation is **MDP v3.4 (planning revision)**. Roster approval does not by itself authorize implementation. Review this complete list and proposed rarities, then explicitly authorize development when ready.

The supplied [full specification](planning/v2.9/REQUIREMENTS.md) is preserved verbatim. [Candidate ledger](planning/v2.9/candidate-registry.json) is documentation only, outside runtime assets. All 35 candidates have pending approval, no implementation date and no started or approved artwork. No fish, coral or invertebrate has been added to the game, mysteries, diving, or permanent implemented-species counts.

Care labels below are conservative **proposed game-design assessments**, not fully researched real-world care certification. Rarity means game collection availability, independently of conservation status, scientific novelty, price or care difficulty. All numeric husbandry, equipment sizing, breeding and development need research and verification after authorization. Do not portray unsupported natural reproduction as implemented.

'''+ '\n\n'.join(tables) + '''

## Premium tiers and release constraints

Fish T5 Potter's, Regal and Achilles profiles are proposed advanced-care collection goals with deliberately limited game supply. Joculator T6 has a narrow island distribution, documented by [CSIRO](https://www.cmar.csiro.au/caab/taxon_report.cfm?caab_code=37365096); its Legendary route would be a restricted specialist collection objective. Gem Tang T6 is a proposed scarce game allocation and spacious-exhibit progression goal, not a claim of biological endangerment. These are proposals for rarity review; the user may change them.

Coral T5 Black Sun would require a supported nonphotosynthetic feeding system. T6 Rhizo would be a scarce specialist solitary-coral objective with its own feeding and settlement needs. [Smithsonian](https://invasions.si.edu/nemesis/species_summary/53813) identifies Black Sun as azooxanthellate; [WoRMS Rhizotrochus record](https://www.marinespecies.org/aphia.php?p=taxdetails&id=216159) supplies its distinct identity and synonyms. No generic frag or light-only care can stand in for these requirements. Turbinaria T4 is a deliberate curated architectural-colony tier, not a conservation assessment.

Bottom-dweller T5 Harlequin Shrimp must remain acquisition-held until its sea-star food requirement is supported; [original feeding research](https://micronesica.org/sites/default/files/biology_of_hymenocera_picta_dana-micronesica_vol._9_no.2_dec._1973o.pdf) does not support a generic algae-wafer diet. T6 Coleman's Shrimp is proposed for its specialized urchin association and exceptionally limited game route. [The original Australian Museum description](https://journals.australian.museum/bruce-1975-rec-aust-mus-2918-486501/) documents paired association with *Asthenosoma intermedium*. Host, feeding and welfare behavior must be supported before acquisition; no 36th host species is implicitly authorized. If that support cannot fit the approved milestone, the user must approve a replacement or retain the visible content hold. Fire Shrimp T4 is curated limited game supply. Tier 6 is never justified by calling an ordinary animal endangered.

Proposed coral tiers are 1,2,4,5,6, with existing named T3 corals. Proposed bottom-dweller tiers are 1,2,4,5,6, with existing T2/T3 invertebrates. Thus each **combined** catalog could cover all six tiers after implementation, care/art eligibility and approval. Specialist holds can still leave an eligible pool empty. Both new mystery products MUST stay visibly unavailable while any advertised tier lacks an eligible implemented species. Never substitute, reweight or reroll.

## Duplicate audit and taxonomy decisions

Inspected CURRENT_LIVESTOCK_CATALOG.md, CURRENT_FISH_CATALOG.md, js/data.js, the 31 clownfish catalog records/25 designer varieties, assets/livestock/life-stages/catalog.json, the permanent assets/expansion-v27/registry.json and actual js/expansion.js registration. The v2.7 ledger contains **38 implemented entries: 28 fish, five named corals, five non-fish invertebrates**, with partial/unapproved art honestly recorded. v2.8 adds six regional references and no new species.

Current totals remain **80 fish records (69 marine / 11 protected freshwater), ten marine coral entries (five generic groups plus five named species), five non-fish invertebrates and six protected freshwater plants**. The 31 clownfish records include disputed/hybrid-origin identities; do not equate records or designer morphs with an independently verified biological-species total. Five earlier fish remain art-only and are excluded from this proposal. No existing IDs, art, behavior or implemented-ledger records were changed.

Copperband Butterflyfish was excluded because it is already implemented in v2.7. All 35 proposed accepted-name identities and reviewed aliases are mutually distinct and have no match against the known baseline identities/IDs. Existing generic coral groups lack exact species IDs, so their biological identity cannot be conclusively deduplicated; none is silently relabeled. Proposed named corals are not new designer morph counts. Legacy common names are used only for exclusion screening, never written back as verified runtime taxonomy.

Use **Centropyge loriculus**, with loricula/flammeus as reviewed aliases ([WoRMS Centropyge](https://www.marinespecies.org/aphia.php?p=taxlist&tName=Centropyge)); **Caulastraea furcata**, with Caulastrea spelling aliases ([WoRMS](https://www.marinespecies.org/aphia.php?p=taxlist&tName=Caulastrea)); and **Nemanthias bartlettorum**, retaining Pseudanthias/Anthias names as aliases ([WoRMS Nemanthias](https://www.marinespecies.org/aphia.php?p=taxlist&tName=Nemanthias)). Hymenocera elegans is an alias, not another species ([WoRMS](https://www.marinespecies.org/aphia.php?p=taxdetails&id=210554)). Each candidate ledger record links its taxonomic lookup; reviewed source aliases are not claimed to exhaust every historical synonym. Some direct detail pages returned web-tool errors; genus lists and institutional sources were used where available. Full future species dossiers remain pending.

## All v2.9 systems remain planned

- Twelve-step saltwater tutorial after Start New Game: welcome/navigation; empty tank and values; regional sand/depth; saltwater preparation; Equipment → Tank Care; supported rock placement and wheel depth; real nitrogen cycling; eligible beginner fish within daily rotation; feeding/inspection/value; safe example medical inspection, symptoms, diagnostics, quarantine, journal guide and legitimate medicine; maintenance; achievable achievement/progress/rewards. Next, Back, Skip, Resume, restart in Settings, objective highlight and saved tutorial progress are required. Never bypass setup/cycle checks or make an animal sick for a lesson.
- Livestock outline: three seconds from latest click, transfer on another click, restart on reclick, clear on tank change; inspector stays usable until closed/selection changed.
- Future freshwater UI lock: disabled/greyed purchasing, creation and interactions, with `Freshwater — Coming in a Future Update.` Preserve all old data, saves, artwork and biology. Before every future implementation prompt explicitly ask whether freshwater is next; default to saltwater unless explicitly authorized.
- Preserve separate +50 AC healthy-day reward; plan +200 AC per player per qualifying death-free game day, never per tank. At least one eligible living fish/coral/bottom dweller and valid simulated progression are required. Authoritative death timestamps cancel the current day, restart a complete 1,440-game-minute recovery interval on each confirmed death, and persist checkpoints. Living bleaching/illness is not death. Offline catch-up must evaluate real qualification; reload/system clock must not bypass recovery or duplicate awards. One day remains 20 real minutes. Explain +50/+200 independently and loss/recovery in Tank History. Inspect current +50 offline behavior before changing it; do not assume the existing implementation already matches every historical document.
- Future player-facing rename: Black Market → Deep Market throughout store, notifications, journal, reputation, buying/selling, help and tooltips, inside the same store modal. Keep black internal IDs, reputation, saved listings/inventory, risks and restrictions. No rename is applied to the current v2.8 runtime.
- Field Journal Leaderboards preview: Saltwater and locked Freshwater views, no seventh sidebar tab, accounts, server, networking or fabricated real players. Optional accurately labeled local-tank comparison uses central total tank asset value, not wallet or duplicated inventory. Any demonstration rows must say demonstration. Online rankings would later need server-authoritative values.
- New tank: exactly 15,000 US gal and exactly 5,000 AC total purchase charge; saltwater initially, future freshwater capability locked. Physical dimensions, net usable liters, displacement/substrate area, flow/light/filter load, habitat fit, equipment, water-change volume and running costs still need design. Preserve ceil whole-gallon labels and unrounded simulation volumes. Do not apply the existing 1.25 marine multiplier to turn this approved price into 6,250 AC.
- Mystery Coral and Mystery Bottom-Dweller Egg each use independent 50/25/15/7.5/2/0.5% odds, persisted unique outcomes/viability/stages/health/value and correct art/mounting/receivers. Corals use an appropriate frag/early colony, not a fish egg. Invertebrate embryos/eggs/larvae/juveniles must be researched species by species; abstractions clearly identified, never instant unexplained adults. Ordinary direct-sale livestock stays T1–3; upper-tier acquisition only through eligible authorized routes. Eight daily Fish slots remain 3 Common + 3 Uncommon + 1 Rare + 1 Mystery Egg.
- Each approved new species later needs appropriate earliest/baby/juvenile/adult living/dead art, correct directional swimming and eyes, valid coral supports and approved six-tier silhouettes. No art was generated or auto-approved in this planning task. Save migrations must be versioned/additive, local-only and protect destination, welfare, health, Keeper, reputation, mysteries, diving and prior progress.

## Read-only maintenance and affordability audit

The smallest actual existing aquarium is **20 L**, displayed as **6 gal** under the ceil rule, not a 20-US-gallon tank. js/core.js waterChange charges ceil(changed liters × 0.13) for marine water (freshwater 0.04; protected). Ten percent of 20 L is 2 L: **1 AC water charge**, plus **one salt dose**. Salt costs 35 AC/10 doses, an amortized 3.5 AC per dose; stock refill is an actual 35 AC purchase. Therefore the current small marine-change amortized baseline is 4.5 AC including salt, not a new fee being applied now.

15,000 US gal = **56,781.17676 L**; a 10% change = **5,678.117676 L** = 1,500 gal. The existing marine water component would be **739 AC**, plus the current flat one-dose salt rule (3.5 AC amortized), for **742.5 AC** before any newly designed consumable rule. Water already scales correctly; fixed-dose salt does not scale with volume. Equipment maintenance/energy are separate; no blanket replacement of correct proportional water rates is authorized. Per-volume salt/treatment accounting, inventory migration and rounding need a later design and tests.

739 AC alone exceeds two ideal 250-AC future daily bonuses (about 2.96 ideal days), before salt, energy, food or repairs. The approved 5,000-AC purchase is much cheaper than the existing 5,000-L Ocean Hall (27,000 base / 33,750 marine purchase), despite being over eleven times its volume. This price inversion and substantial upkeep are documented balance concerns; the approved purchase price was NOT secretly changed. No affordability simulation was executed and no new tank or equipment capacity is registered.

## Verification and approval handoff

Executed: static 25/5/5 count, candidate-ID/accepted-name/reviewed-alias collision checks, T5/T6 coverage in all three categories, combined potential mystery-tier coverage, exact odds sum, original-requirements byte check, 31-major-section MDP continuity and source equality, documentation links, and all protected runtime/art/DIST/archive hashes against the pre-edit snapshot. Results are in [planning-checks.json](planning/v2.9/planning-checks.json). No gameplay/browser tests or future-system QA items 1–35 are claimed executed: those features are not implemented. Historical v2.8 test results remain historical.

Documents updated: this proposal; verbatim requirements and proposed ledger; CURRENT_LIVESTOCK_CATALOG.md; GAME_DESIGN.md; UI_SPECIFICATION.md; ART_DIRECTION.md; DEVELOPMENT_STATUS.md; BALANCE_REPORT.md; consolidated MASTER_DEVELOPMENT_PROMPT.md; PROJECT_CONTINUITY_SOURCE.md; PDF_WORKFLOW.md. No new binary PDF was authored; regeneration remains pending. No build or ZIP packaging was run because the user expressly prohibits implementing v2.9 now; the current v2.8 DIST and ZIPs remain byte-identical. Rebuild them after future authorized runtime edits.

**Awaiting the user's roster/rarity review and explicit implementation authorization.** Future freshwater remains unauthorized. Do not treat planning completion as v2.9 gameplay completion or use the implementation completion phrase while that work is pending.
'''
    write('FUTURE_V29_PLAN.md', proposal)
    notices = {
        'CURRENT_LIVESTOCK_CATALOG.md':'The [v2.9 roster proposal](FUTURE_V29_PLAN.md) contains exactly 25 fish, five corals and five non-fish bottom dwellers, all **PROPOSED / UNAPPROVED / NOT IMPLEMENTED**. [Proposed ledger](planning/v2.9/candidate-registry.json) is documentation only, never a runtime registry. Current v2.8 totals and the permanent 38-entry v2.7 ledger below remain unchanged. Scientific aliases and prior art-only entries were screened; generic legacy coral identities remain unverified. No artwork was created. Await roster/rarity approval AND explicit implementation authorization. Saltwater-only confirmed by user on 2026-10-14.',
        'DEVELOPMENT_STATUS.md':'Recorded the full future specification and [complete 25/5/5 candidate list](FUTURE_V29_PLAN.md). MDP v3.4 is a **documentation planning revision**; current playable build remains v2.8. User confirmed saltwater-only on 2026-10-14. Tutorial, selection expiry, freshwater UI lock, survival reward, Deep Market rename, leaderboard preview, large tank, new mysteries and new livestock are all **NOT IMPLEMENTED**. Runtime, old species/art/saves, DIST and release ZIPs are preserved. Static planning checks only; no v2.9 gameplay QA passed or claimed. Roster approval and explicit implementation authorization are both pending. PDF source updated; binary export remains pending.',
        'GAME_DESIGN.md':'[Future v2.9 plan](FUTURE_V29_PLAN.md) and [verbatim specification](planning/v2.9/REQUIREMENTS.md) are recorded. Plan a 12-step saved/skippable saltwater tutorial, separate +50 healthy / +200 death-free player rewards with authoritative one-day recovery and offline qualification, Deep Market display rename, preview-only asset-value leaderboards, exact 5,000-AC / 15,000-US-gallon tank and independent new mystery products. No system or species is implemented by this revision. Preserve v2.8 gameplay and every earlier locked rule. Saltwater-only confirmed; ask whether freshwater is next before each future implementation prompt.',
        'UI_SPECIFICATION.md':'Future-only requirements: 12-step tutorial with control highlights, Next/Back/Skip/Resume/Settings restart and safe medical demonstration; livestock outline expires three seconds after the latest click while inspector remains open; disabled freshwater UI with `Freshwater — Coming in a Future Update.`; Deep Market rename inside store; Journal Leaderboards with saltwater and locked freshwater preview, no seventh sidebar tab. No online claims or fake real ranks. Tank History must later explain distinct daily rewards and death-free recovery. No v2.8 UI changes now. See [complete plan](FUTURE_V29_PLAN.md).',
        'ART_DIRECTION.md':'All 35 [v2.9 candidates](FUTURE_V29_PLAN.md) are proposed only: no new sprites, placeholders, art approval or runtime entries. After roster approval and explicit implementation authorization, research biologically appropriate earliest/baby/juvenile/adult living/dead stages, fish eyes and movement directions, mounting, and six-tier silhouettes. No universal fish-style coral eggs or generic instant adult invertebrates. Preserve approved hybrid style and all existing art; specialist reproductive/host support remains a release gate.',
        'BALANCE_REPORT.md':'Read-only v2.9 findings: actual smallest aquarium is 20 L (ceil label 6 gal). A 10% marine change removes 2 L and currently costs 1 AC plus one salt dose (3.5 AC amortized). For the planned 56,781.17676-L / 15,000-US-gallon tank, 10% removes 5,678.117676 L; existing water rate produces 739 AC. Water already scales; salt is a flat dose and needs later volume accounting. Approved total tank purchase stays exactly 5,000 AC (avoid the current marine 1.25 multiplier). Price inversion versus the 5,000-L Ocean Hall and upkeep exceeding two ideal 250-AC future reward days are flagged; no balance values changed, no affordability simulation run. Proposed rarity coverage/mystery holds and full audit: [future plan](FUTURE_V29_PLAN.md). Existing +50 offline code/document differences require verification before future edits.'
    }
    for name, body in notices.items():
        insert_notice(name, body)
    mdp = read('MASTER_DEVELOPMENT_PROMPT.md')
    if '## 2.6 Future v2.9 Authorization Gate' not in mdp:
        mdp = mdp.replace('VERSION 3.3','VERSION 3.4',1)
        mdp = re.sub(r'^### Revision:.*$', '### Revision: 3.4 records v2.9 PLANNING ONLY; playable runtime remains v2.8. All 31 major sections and prior rules are preserved.', mdp, count=1, flags=re.M)
        mdp = mdp.replace('### Status: Consolidated Source of Truth', '### Status: Consolidated Source of Truth — v2.9 implementation NOT authorized',1)
        mdp = mdp.replace('\n---\n','\n**Current execution gate:** Record v2.9 requirements and propose 25/5/5 species only. Do not implement any v2.9 system, species, art or runtime change until roster/rarity review and explicit implementation authorization. The user confirmed saltwater-only on 2026-10-14. [Complete plan](FUTURE_V29_PLAN.md); [verbatim requirements](planning/v2.9/REQUIREMENTS.md). This gate overrides generic instructions to start implementation below.\n\n---\n',1)
        sections = {
            2:('2.6 Future v2.9 Authorization Gate','All v2.9 requirements are PLANNED, NOT IMPLEMENTED. Only recording and duplicate-checked roster proposal are authorized now. Obtain explicit approval of the complete 25 fish / five corals / five bottom-dweller list and rarities, then explicit implementation authorization. Before every future Aquarium Life implementation prompt, explicitly ask whether freshwater development is next. Current answer: keep v2.9 saltwater-only. Future freshwater UI must be greyed/disabled, including purchase/creation/interactions, with `Freshwater — Coming in a Future Update.` Preserve all existing freshwater saves, species, artwork and biology; do not delete code.'),
            3:('3.12 Planned v2.9 Artwork','After authorization, all new species need researched appropriate earliest/baby/juvenile/adult living/dead art, correct swimming direction and eyes, valid coral supports and six-tier silhouettes. Do not treat placeholders or generated art as approved. No art is authorized now; proposed ledger marks every set not started.'),
            4:('4.6 Planned 15,000-US-Gallon Aquarium','Approved future total purchase charge: exactly 5,000 AC for 15,000 US gal = 56,781.17676 L; do not apply the usual marine markup. Saltwater first; freshwater capability locked. Define physical dimensions, actual usable capacity/displacement, substrate area, equipment/filtration/flow/light demand, habitat fit, running/maintenance costs and changed-water volume before implementation. Nominal labels ceil whole gallons; chemistry/cost volumes stay unrounded. No tank is registered now.'),
            5:('5.6 Planned Beginner Saltwater Tutorial','After Start New Game, guide 12 steps: welcome/six menus/earning; empty first tank and purchase/base/total value; regional sand and depth; real saltwater preparation/salinity/temperature/volume; Equipment → Tank Care/filter/heater/flow/light; supported rock placement and wheel depth/shelter; actual nitrogen cycle/water conditions; eligible beginner fish/daily eight slots/compatibility/selected destination; feeding and inspector health/hunger/stage/rarity/value; safe example medical inspection/symptoms/diagnostics/quarantine/Field Journal Disease & Treatment Guide/legitimate medicines and warnings; maintenance/rewards; implemented achievable achievement requirements/progress/reward/objectives. Include Next/Back/Skip/Resume, objective/control highlight, saved progress and Settings restart. Never bypass setup/cycling, force illness or permanently block skipped players.'),
            6:('6.5 Planned v2.9 Species Approval','Inspect current catalog, permanent registry and actual previous 38-entry implementation, scientific identities/synonyms, 31 clownfish records, designer varieties and art-only entries. Propose exactly 25 new saltwater fish, five named corals and five non-fish bottom dwellers with rarity/care/IDs; each category needs at least one T5 and T6 with a reasonable game rationale. Present the complete list and await explicit approval. Rarity is not conservation status. Proposed-only records remain outside runtime; no designer morph counts as a biological addition. Current proposal and audit are in FUTURE_V29_PLAN.md and planning/v2.9/candidate-registry.json.'),
            9:('9.10 Planned Three-Second Livestock Outline','Clicking livestock starts a three-real-second visual-outline timer. A different selection transfers it, a repeat click restarts it, and tank changes clear it. No stale outline. Expire only the outline: the livestock inspector stays usable until closed or selection changed. No runtime change now.'),
            12:('12.6 Planned Water-Change Cost Audit','Preserve correctly proportional water/equipment costs. Changed volume = actual tank water × fraction; a 10% change uses 0.10. Scale eligible replacement water, salt, treatment and consumables by actual volume without rounding saved liters. The current smallest tank is 20 L, label 6 gal, not 20 US gal: a 10% marine change currently charges 1 AC plus one salt dose. Water already scales at ceil(changed L × 0.13); fixed-dose salt needs review. Future 15,000-gal 10% water component would be 739 AC. Document affordability against 5,000-AC purchase, rewards, livestock, equipment and change frequency; never secretly change the approved purchase price.'),
            16:('16.8 Planned Local Leaderboard Preview','Within Field Journal, provide Saltwater Leaderboard and locked Freshwater Leaderboard preview, without seventh permanent tab. Ranking metric is current total aquarium asset value from central valuation: eligible shell, installed equipment, fish/coral/bottom dwellers, substrate/rocks/decor; exclude wallet and uninstalled inventory, no double counting. Optional local owned-tank comparison must say local; samples must say demonstration. No servers, accounts, network, fake real players or public submissions. Future competitive ranking requires server-authoritative verification; no online leaderboard is implemented now.'),
            17:('17.7 Planned Separate Livestock Survival Bonus','Keep +50 AC healthy-day reward separate; add +200 AC once per player per qualifying death-free in-game day, maximum combined 250 AC, never multiplied by aquarium count. Require valid simulated progression and at least one eligible living fish/coral/bottom dweller across eligible owned stocked tanks. A confirmed livestock death cancels the current survival day, records authoritative simulation time and starts a full 1,440-minute death-free recovery interval; every new death restarts it. No payment before recovery AND qualifying-day conditions complete. Living coral bleaching/illness is not death. Evaluate genuine qualification during offline catch-up; retain 20-real-minute game days, persistent calendar/checkpoints and anti-duplication. Reload/system-clock changes cannot bypass recovery. Notify separately `Daily Healthy Tank Reward: +50 AC`, `Livestock Survival Bonus: +200 AC`, and the one-full-day recovery explanation after loss; expose status in Tank History. Verify current +50 code/offline behavior before changes; no new reward exists yet.'),
            18:('18.9 Planned Mystery Coral and Bottom-Dweller Egg','Saltwater → Corals: Mystery Coral. Saltwater → Bottom Feeders: Mystery Bottom-Dweller Egg. Each independently uses exact 50/25/15/7.5/2/0.5% T1–6 odds; other purchases cannot affect individual probability. Use only implemented, classified, eligible species; any empty advertised pool visibly holds buying, never substitutes/reweights. Persist species/rarity/unique ID/viability/growth/health/stage/value/art and correct receiver/mount. Coral is a frag/appropriate early colony, never universally a fish egg. Invertebrates need appropriate eggs/masses/brooded embryos/larvae/juveniles or clearly labeled researched game abstraction, no unexplained instant adults. Normal direct livestock stays T1–3; eligible upper tiers use authorized mystery/Deep Market/diving. Keep eight daily Fish slots 3 Common + 3 Uncommon + 1 Rare + 1 Mystery Egg. No product is implemented now.'),
            19:('19.5 Planned Deep Market Display Rename','After authorization replace every player-facing Black Market reference with Deep Market in store tabs/headings, messages, tooltips, reputation, journal/help and buying/selling. Keep the market inside Aquarium Store, existing functionality, prices, hidden risks, restricted fictional medicines, rarity/availability, reputation and diving resale gates. Retain black internal IDs/legacy save keys as needed; never reset reputation or purchases. Current runtime remains named Black Market until implementation is authorized.'),
            24:('24.6 Planned v2.9 Persistence','Use additive versioned migrations; preserve old progress, 20-minute days, local saves/offline simulation, +50 reward and future +200 checkpoints/death/recovery, values/IDs/health/rarity/mystery outcomes, market reputation/inventory/rename compatibility, Keeper progress, selected tank and diving. Persist tutorial skip/resume and mystery outcomes without rerolls. Do not alter protected freshwater biology. Browser-local data remains on each player PC; no server or cloud. Rebuild DIST/archives after future authorized runtime edits, not as an implementation during this planning-only task.'),
            27:('27.15 Planned v2.9 Acceptance — Not Yet Executed','Preserve the complete 35-item QA checklist in planning/v2.9/REQUIREMENTS.md §15. Verify tutorial/start/skip/resume/medical guidance; outline at three seconds and retained inspector; disabled freshwater purchases with preserved data; separate +50/+200, death cancellation/recovery/reload safeguards; complete display rename with intact reputation/inventory; preview leaderboards/asset metric/both views/no wallet ranking; exact tank/price/fresh lock/volume maintenance and baseline; no roster duplicates and category T5/T6/approval; both exact odds sums/independence/persistent outcomes/empty-pool holds; approved art and fully offline play. Report actual passed/failed/not-run results. None of these future gameplay acceptance items is claimed complete by planning checks.'),
            30:('30.5 v2.9 Planning Continuity and Locked Additions','Maintain this one 31-section MDP, catalog/permanent species ledger, GAME_DESIGN, UI_SPECIFICATION, ART_DIRECTION, DEVELOPMENT_STATUS and BALANCE_REPORT. Requirements are preserved verbatim in planning/v2.9/REQUIREMENTS.md; proposed ledger records scientific/common names, category, rarity, care, stable proposed ID, batch, art/implementation/approval status. Never mark proposed species implemented. Preserve all earlier locked rules and back-of-PDF handoff rules. Future permanent requirements include tutorial/medical guidance; three-second outline only; freshwater authorization/disabled UI; separate death-free bonus/recovery; Deep Market name; preview asset-value leaderboards; exact large-tank price and proportional upkeep; approved duplicate-free roster with premium categories; independent mystery products and stage/art/save safeguards. Update PROJECT_CONTINUITY_SOURCE.md; if binary PDF export unavailable explicitly keep it pending. Authorized implementation reports must list files/features/species preserved/added, tests passed/failed/not-run, limits and docs; only completed authorized edits end with the required completion line. Do not claim implementation completion while this gate is pending.')
        }
        # Insert each new subsection before the next major heading without removing old text.
        for major, (title, body) in sections.items():
            next_heading = re.search(r'^# '+str(major+1)+r'\. ', mdp, re.M)
            assert next_heading, major
            pos = next_heading.start()
            mdp = mdp[:pos].rstrip()+'\n\n## '+title+'\n\n**PLANNED / NOT IMPLEMENTED.** '+body+'\n\n'+mdp[pos:]
        write('MASTER_DEVELOPMENT_PROMPT.md', mdp)
    assert [int(x) for x in re.findall(r'^# (\d+)\. ',mdp,re.M)] == list(range(1,32))
    # Keep the full existing printable registry and back-of-source handoff.
    continuity = read('PROJECT_CONTINUITY_SOURCE.md')
    split = continuity.index('# AQUARIUM LIFE\n')
    end = continuity.index('## Back-of-source permanent continuity rules',split)
    before, back = continuity[:split], continuity[end:]
    before = before.replace('Revision v2.8 / MDP v3.3, 2026-10-14.', 'Playable v2.8 / MDP v3.4 planning revision, 2026-10-14.')
    if '## v2.9 planning handoff' not in before:
        before += '## v2.9 planning handoff\n\nNo v2.9 implementation is authorized. User confirmed saltwater-only. Full requirements: planning/v2.9/REQUIREMENTS.md. All 35 proposed entries below are UNAPPROVED / NOT IMPLEMENTED; art NOT STARTED; IDs are proposed only. Current implemented 38-entry registry and v2.8 totals above remain authoritative.\n\n'+'\n\n'.join(tables)+'\n\nSee FUTURE_V29_PLAN.md for premium rationales, duplicate limits, source links, maintenance audit and release gates.\n\n'
    if 'Future v2.9 remains planning only' not in back:
        back += '\n\nFuture v2.9 remains planning only until roster/rarity approval AND explicit implementation authorization. Ask whether freshwater development is next before every future implementation prompt; current answer is saltwater-only. Preserve 20-minute days, local saves, all prior 38 species and regional profiles. Future tutorial, welfare bonus/recovery, Deep Market display name, preview-only asset leaderboards, 5,000-AC 15,000-gal tank and exact independent mystery products follow MDP primary sections; none is implemented now. Proposed species/art are never silently promoted to approved content.\n'
    write('PROJECT_CONTINUITY_SOURCE.md',before+mdp+'\n\n'+back)
    insert_notice('PDF_WORKFLOW.md','Printable continuity now includes the complete proposed 35-row v2.9 roster and MDP v3.4 planning revision, retaining the earlier 38-row implemented ledger and locked handoff. Current playable release remains v2.8. **No new binary PDF generated; export/render verification remains pending.** Do not run historical report builders that could overwrite this planning record with older MDP content. Future export must retain unapproved/unimplemented labels and the explicit authorization gate. [Planning record](FUTURE_V29_PLAN.md).')
    print('Recorded complete v2.9 plan, 35 unapproved candidate records, documentation notices and 31-section MDP v3.4. No runtime/build/art edits.')


if __name__ == '__main__':
    main()
