"""Integrate this authorized update into current design sections and continuity."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[2]
read=lambda name:(ROOT/name).read_text(encoding='utf8')
def write(name,s):(ROOT/name).write_text(s,encoding='utf8')
old_master=read('MASTER_DEVELOPMENT_PROMPT.md')
assert 'VERSION 4.0' in old_master, 'One-time documentation integration already applied; do not rerun.'
continuity=read('PROJECT_CONTINUITY_SOURCE.md')
assert old_master in continuity
prefix=continuity[:continuity.index(old_master)]
rule='Fish breeding in Aquarium Life happens autonomously when biologically appropriate conditions are satisfied. The player does not manually initiate courtship through the Field Journal. Reproductive condition is visible through individual livestock inspection, and eggs or offspring appear in the same aquarium as their parents according to species-specific reproductive biology.'
overview='''## Automatic marine breeding — v3.8 current, 2026-10-15

Replaced manual marine courtship with autonomous, species-aware breeding, visible swimming/nest behavior, individual reproductive status and a read-only Breeding & Eggs observation dashboard. New clutches use real parent/tank IDs, saved reproductive roles and RNG, species-specific care/losses and bounded offspring reservations. All prior local accounts, art/genetic identities, coral lineage, rewards, heaters, mortality logs, store/casino functionality and the 20-minute day remain. Freshwater stays locked. See [BREEDING_RULES.md](BREEDING_RULES.md), [BREEDING_SAVE_SCHEMA.md](BREEDING_SAVE_SCHEMA.md) and [BREEDING_UPDATE_REPORT.md](BREEDING_UPDATE_REPORT.md). Earlier release entries are historical wherever superseded.

'''
m=old_master.replace('VERSION 4.0','VERSION 4.1',1).replace('playable v3.7,','playable v3.8,',1)
pos=m.index('## Equipment filters, inspector research')
m=m[:pos]+overview+m[pos:]
def section(start,end,text):
 global m
 a=m.index(start);b=m.index(end,a)
 m=m[:a]+text.rstrip()+'\n\n'+m[b:]
section('## 15.1 Reproductive Eligibility','## 15.2 Egg Purchasing',f'''## 15.1 Autonomous Reproductive Eligibility — permanent v3.8

**{rule}**

No marine player action starts courtship. Once per saved game hour, mature same-species partners in the same tank evaluate health ≥85 HP, nutrition ≥75%, hunger ≤40, stress <25, energy ≥20, correct reproductive roles, no active disease/treatment, no other pairing/dependent brood and expired recovery. Designer/genetic holds remain. Prepared cycled water must meet species temperature/pH/salinity ranges, ammonia/nitrite ≤0.05 mg/L, nitrate ≤30 and oxygen ≥6; minimum tank volume applies. Require appropriate hard nest/cavity/cover, separated unoccupied territories, no nearby aggressive disturbance, real adult food and the correct stocked larval ration.

Reserve each potential offspring's adult load plus existing residents, invertebrates, nurseries, eggs and other courting cohorts. Breeding reservations fit within 80% of tank biological capacity, retaining 20% headroom. Preserve 250 fish/entity slots and at most 20 incubating/courting cohorts per tank. Store admissions honor the reservations. Courtship transfers its reservation to eggs once. Unsuitable conditions cancel courtship with 24 game hours of recovery, rather than silently producing eggs.

| Current profile | Courtship / spawning / incubation | Window and probability | Recovery / larval food |
|---|---|---|---|
| 26 eligible catalog clownfish | Protandrous pair, close swimming and hard-nest preparation for 6 game hours; attached clutch and male tending; 168 suitable incubation hours | 07:00–18:00; hourly 0.085 × minimum parental fertility | 336 game hours; fine fry food |
| Banggai cardinalfish | Compatible female/male circling for 8 hours; paternal internal mouthbrooding; 504 suitable hours; small juveniles at release | 06:00–18:00; hourly 0.070 × fertility | 720 hours; fine fry food |
| Chalk bass | Simultaneous hermaphrodites, no F/M requirement; 3-hour water-column display; pelagic drifting eggs; 24 suitable hours | 17:00–20:00; hourly 0.140 × fertility | 240 hours; cultured live plankton |
| Sharknose goby | Compatible female/male cavity preparation for 5 hours; demersal eggs and male tending; 144 suitable hours | 08:00–12:00; hourly 0.110 × fertility | 336 hours; fine fry food |

Every cohort represents two potential offspring, not real egg production. Probabilities, windows, durations and headroom are game calibrations. Egg-donor roles in the chalk-bass model alternate on later spawning events; legacy sex fields are not its sexual system. Clownfish larvae are immature nonbreeders, mature into the male role, and the largest mature male in a group without an established female undergoes a saved 14-day transition. Established females never reverse. Readiness is not a daily guarantee. Complete biological sources, numerical loss rates and limitations are in BREEDING_RULES.md.''')
section('## 15.3 Incubation','## 15.4 Genetics','''## 15.3 Natural Incubation and Survival

New natural clutches retain actual parent IDs, spawning tank/time/site, independent embryo genes/patterns and per-embryo survival. Fertilization chance is clamp(0.72 + 0.25 × minimum parental fertility, 0.72, 0.96). Preserve known Snowflake reference-model nonviability separately from unfertilized eggs. Never guarantee a survivor.

Suitable development adds dtHours × clamp(1.06 ** (temperature − 25), 0.75, 1.2). Unsafe water pauses development and raises egg-loss risk. Independently calibrated water, care, parental disease, hungry-neighbor predation and pelagic dispersal hazards use 1 − exp(−rate × dtHours); record the category that actually caused each simulated loss. Internal broods do not receive external predation. Missing/dead male carriers lose internal broods; lost nest support loses attached broods. A spawn does not receive the preceding simulation interval twice.

Hatching rechecks capacity and creates unique individual IDs in the parents' aquarium, copies the assigned embryo identities once and records outcomes/lineage. Zero survivors and failed spawning are valid recorded outcomes. Legacy and purchased broods keep their original simplified incubation/genetics rather than being reinterpreted as newly observed natural spawning. See BREEDING_RULES.md for the exact authoritative formulas.''')
section('## 15.5 Fry','## 15.6 Persistent Marine Egg Presentation','''## 15.5 Offspring, Nutrition and Responsible Sale

New natural larvae start at age 1 / baby-stage growth and use existing life-stage art; Banggai release small juveniles at 30% of species maturity, a developmental-age game calibration. None are instant adults. Persist unique IDs, parents, generation, appearance seeds, origin clutch and hatch time. Standard Ocellaris inheritance remains independent of survival. Other species receive ordinary catalog-pattern identities, not clownfish bar outcomes or Snowflake alleles.

Pelagic chalk-bass larvae accept cultured live plankton, represented by the marine-only plankton ration; ordinary fry food does not satisfy that saved requirement. Other supported larvae accept fine fry food. Feeders use actual compatible stock and switch to existing adult diets with juvenile growth. Hunger, nutrition, disease, predation and mortality remain active. Naturally bred offspring must reach juvenile growth and at least seven game days after hatch before sale; existing dealer welfare, budget and value checks remain. No automatic AC payout is added. Population growth remains limited by reservations, habitat, fertility, recovery, real nutrition and survival.''')
section('## 15.6 Persistent Marine Egg Presentation','## 15.7 Persistent Pattern Inheritance','''## 15.6 Persistent Marine Eggs and Observations

Clownfish and supported demersal clutches remain attached to a saved physical nest site, with local coordinates that follow a moved supporting rock. Pelagic eggs drift in the water column using saved age; they never become stationary rock clutches. Mouthbroods remain internal with a male carrier and no external egg pile. Existing egg/baby/juvenile artwork is reused; anatomy, eyes and orientation remain unchanged. Attached scene clusters remain 8 logical pixels and pelagic eggs 5; fixed magnified clusters and embryo detail show development instead of literal fivefold egg growth. Click visible eggs or use the journal/parent inspector to inspect internal broods.

Failed external clutches stay inspectable for one game day or until removed, add pollution once and never hatch. Supporting-rock removal remains blocked while an attached clutch exists. Values use the central valuation authority. New natural broods disclose their actual loss categories; legacy/purchased broods disclose their original simplified model.

The Field Journal Breeding & Eggs tab observes current pairs/readiness, actual spawning events, active clutches (species, parents, tank, date, count, progress and estimated suitable hours), offspring stages/survival/lineage, and completed/failed history. It has no manual marine mating trigger. Keep player-fragged coral clone lineage separate. Individual fish inspectors show role, maturity, current partner, Courtship, Gravid — Carrying Eggs only for the modeled egg donor, Preparing to Spawn, male mouthbrooding/tending, last spawn and recovery where applicable. Explain gravid with the beginner tooltip. Update observations live while keeping the inspector open after its selection outline expires at three seconds.''')
section('## 15.8 v2.7 breeding boundaries','# 16. FISH RARITY','''## 15.8 Current Species Boundaries — v3.8

29 existing biological fish IDs have autonomous profiles: 26 purchase-eligible clownfish, Banggai, Chalk Bass and Sharknose Goby. The five existing specialist clownfish acquisition/art holds remain breeding holds. The older generic marine button/rules are superseded. Yellow/Blue Assessor, Greenbanded Goby and other incomplete profiles are held until reproductive role, habitat and larval-rearing details are reviewed; no assertion of biological impossibility is made. Historical v2.7 registry flags remain the earlier batch record; current runtime breedingSupported/breedingStatus/autonomousBreeding metadata is authoritative. Species/art/catalog counts and all unsupported designer holds remain unchanged.

Already saved and legitimately purchased species-identified Mystery Eggs retain their original calibrated model; they do not establish complete natural captive-culture feasibility. No new invertebrate egg/planktonic larval reproduction or freshwater biology is authorized. Coral fragmentation remains governed by section 8.8.''')
m=m.replace('## 9.2 Aging','## 9.12 Individual Reproductive Observations — v3.8\n\nThe existing livestock inspector displays reproductive role, maturity, partner, state, clutch, last spawn and recovery from section 15. Readiness/state refresh without resetting selection outlines, names or input focus. Apply only biologically relevant labels.\n\n## 9.2 Aging',1)
# Keep section numbering in ascending order by moving the new inspector subsection
# immediately before the following major behavior section.
new9=m[m.index('## 9.12 Individual'):m.index('## 9.2 Aging')]
m=m.replace(new9,'',1)
idx=m.index('# 10. ');m=m[:idx]+new9+m[idx:]
idx=m.index('# 11. ');m=m[:idx]+'''## 10.4 Natural Courtship Steering — v3.8

Use section 15 profile-specific nest preparation, circling and water-column spawning targets through the existing smooth velocity/movement system. No teleportation, tank-wide freeze or sprite/anatomy rewrite. Food seeking and severe stress take priority. Other fish continue swimming; small observation markers identify courting or mouthbrooding individuals.\n\n'''+m[idx:]
idx=m.index('# 25. ');m=m[:idx]+'''## 24.11 Autonomous Breeding Persistence — v3.8

Add root breeding v1 RNG/journal/archive, tank next-check/pair/reservation fields, individual role/maturity/mate/state/clutch/last-spawn/recovery/transition fields, natural clutch site/parents/embryo survival/losses, and hatchling origin/IDs/larval ration/minimum sale age. Keep schema 2 and legacy sex fields; roles are authoritative for hermaphrodites and immature clownfish. Migration is additive/idempotent and never rolls, spawns, hatches or assigns unknown genotypes. Validate all active references, species/roles/carriers/sites, unique IDs, reservations and viability; preserve historical parent IDs after sale/death. Detail schema: BREEDING_SAVE_SCHEMA.md.

Shared fixed steps and account/world checkpoints govern live, modal, diving, casino and offline progression. No elapsed interval is replayed on login. Retain up to 600 detailed reproductive records plus archived completed-cohort totals; the dashboard displays the latest 100. Preserve existing keeper, loss and coral histories. No backend, no cloud save and no player-data clearing; retain JSON export/import and the current 5 MB limit.\n\n'''+m[idx:]
idx=m.index('## 26.9 Resident');m=m[:idx]+'''## 26.8 Breeding Observation UI — v3.8

Field Journal → Breeding & Eggs is the observation dashboard specified in 15.6, with links to clutches/internal broods and separate coral frag lineage. No Begin Courtship control or marine action remains. The existing fish inspector refreshes its reproductive section independently of forms/selection outlines. Responsive internal scrolling and readable long IDs must fit desktop and narrow screens.\n\n'''+m[idx:]
idx=m.index('# 28. ');m=m[:idx]+'''## 27.18 Autonomous Breeding Acceptance — v3.8

Verify every authorized 27-case category: automatic eligible breeding, manual-control removal, maturity/species/roles, visible smooth movement, gravid/internal brooding, correct tank/support/pelagic placement, persistent clutches, no replay, incubation, unique hatchling IDs/stages/genetics, 85/10/4/1 and separate Snowflake rules, recovery/capacity, observations/history/coral lineage, matched live/offline timelines, additive saves, freshwater lock and fully offline behavior. Test UI clock progression during Store, Journal, Casino and Diving. Exact pass/fail and not-run evidence belongs in BREEDING_UPDATE_REPORT.md; do not infer an unrun suite passed.\n\n'''+m[idx:]
idx=m.index('# 31. ');m=m[:idx]+'''## 30.8 Automatic Breeding Continuity — v3.8

Preserve the permanent autonomous-breeding rule in 15.1, current species boundaries in 15.8 and additive schema in 24.11. Keep original genetics/art approvals, specialist holds, all 38/35 roster ledger entries and the complete 31-section master in the printable continuity source. Refresh DIST/Pages ZIP and the source ZIP for delivery. If PDF authoring/rendering is unavailable, retain the updated full source and report binary PDF pending.\n\n'''+m[idx:]
assert len(re.findall(r'^# \d+\.',m,re.M))==31
write('MASTER_DEVELOPMENT_PROMPT.md',m)
for name in ['GAME_DESIGN.md','DEVELOPMENT_STATUS.md','UI_SPECIFICATION.md','CURRENT_LIVESTOCK_CATALOG.md','CURRENT_FISH_CATALOG.md','README.md']:
 s=read(name);at=s.index('\n')+1;s=s[:at]+'\n'+overview+s[at:]
 if name=='GAME_DESIGN.md':
  a=s.index('## Breeding and genes');b=s.index('## Economy',a)
  s=s[:a]+'''## Breeding and genes

Marine reproduction is autonomous under the permanent rule in MDP section 15. Player actions do not initiate marine courtship. Species-specific role, maturity, condition, chemistry, nest, territory, food and reserved adult-capacity checks precede persistent hourly chance rolls. The four reviewed profiles cover 26 eligible clownfish, Banggai, Chalk Bass and Sharknose Goby; other incomplete profiles remain held. Preserve established clownfish females, immature nonbreeders and simultaneous chalk-bass roles. Appropriate same-tank attached, drifting pelagic and internal paternal broods progress on the unchanged shared clock.

The Field Journal observes reproduction and retains separate coral frag lineage. The fish inspector refreshes reproductive status without extending its three-second outline. Eggs remain small, losses are meaningful, hatchlings have unique inherited identities and development-specific feeding/art, and sale requires juvenile growth plus establishment. Normal Ocellaris 85/10/4/1 and separate documented Snowflake genetics are unchanged. See BREEDING_RULES.md for formulas, scientific sources, parameter uncertainty and bounded-history limits; BREEDING_SAVE_SCHEMA.md for migration and replay protection. Freshwater biology remains frozen and inaccessible.

'''+s[b:]
 write(name,s)
s=read('UI_SPECIFICATION.md');at=s.index('## Equipment filters, inspector research')
s=s[:at]+'''## Breeding observation interactions — v3.8

Breeding & Eggs has current activity/readiness, active clutches with parent/tank/date/count/progress/hatch estimates, offspring stage/survival/lineage and completed/failed history. Links open existing brood inspectors; mouthbroods are accessed from the journal or father without drawing an external pile. Coral frag clone lineage remains separate. The tab is read-only for mating: no Begin Courtship button.

The existing fish inspector shows sex/reproductive role, maturity, partner, applicable readiness/courtship/gravid/preparing/tending/male-mouthbrooding/recovery states, active brood, last spawn and cooldown. Explain gravid with its tooltip. Refresh that section once per UI heartbeat without closing the inspector, replacing rename forms or resetting the three-second outline. Courtship targets steer existing sprites; markers do not alter eyes/anatomy. Keep responsive internal scrolling and readable IDs at 1920×1080, 1600×900, 1366×768 and 390×844. All modal windows continue the same simulation clock.

'''+s[at:];write('UI_SPECIFICATION.md',s)
catalog='''## Current reproductive metadata — v3.8

No species, scientific identity, rarity, aquarium requirement, sprite or collection count is added or removed. Runtime metadata now uses AL.Breeding's reviewed profiles rather than inferring reproduction from a body shape. All rates/cohort sizes are game calibrations.

| Existing group / ID | Current autonomous status |
|---|---|
| 26 purchase-eligible clownfish including `clown` | Protandrous; hard-substrate eggs, male tending, fine-food larvae |
| `banggai` | Separate reproductive roles; paternal mouthbrooding; developed juvenile release |
| `chalk-bass` | Simultaneous hermaphroditism and alternating egg-donor roles; pelagic eggs; live-plankton larvae |
| `sharknose-goby` | Compatible male/female; demersal cavity nest and male care |
| Specialist clownfish five existing acquisition/art holds | Remain held; no breeding bypass |
| Other incomplete marine profiles, including Royal Gramma, Yellow/Blue Assessor and Greenbanded Goby | Autonomous breeding held pending reviewed roles/nest/larval protocol; not a claim of biological impossibility |
| Already saved/purchased broods | Keep original strategy, incubation and inherited identities; no inferred historical spawning |
| Existing freshwater, corals and non-fish invertebrates | No reproductive-system expansion; freshwater remains locked, coral fragging stays separate |

The historical v2.7 registry's five simplified enabled flags are superseded for current natural reproduction. Current runtime `breedingSupported`, `breedingStatus` and `autonomousBreeding` are authoritative; the batch registries remain intact for continuity. See BREEDING_RULES.md for species boundaries and references, and BREEDING_SAVE_SCHEMA.md for migration.

'''
for name in ['CURRENT_LIVESTOCK_CATALOG.md','CURRENT_FISH_CATALOG.md']:
 s=read(name);at=s.index('## Daily livestock') if '## Daily livestock' in s else s.index('\n\n')+2
 write(name,s[:at]+catalog+s[at:])
for name in ['RARITY_GENETICS_RESEARCH.md','RESEARCH_SOURCES.md']:
 s=read(name);at=s.index('\n')+1
 write(name,s[:at]+'''\n## Autonomous breeding integration — v3.8

The new marine breeding authority reuses the existing embryo/pattern functions unchanged. Normal non-designer Ocellaris retain 85/10/4/1; Snowflake reference-line segregation and explicitly inferred nonviability remain separate. No unrelated species gains those traits. Species biology, primary/institutional sources and calibration boundaries for autonomous courtship/eggs/larvae are recorded in [BREEDING_RULES.md](BREEDING_RULES.md). Existing evidence and uncertainty below are retained.\n'''+s[at:])
for name in ['PDF_WORKFLOW.md','GITHUB_PAGES.md','TEST_REPORT.md']:
 s=read(name);at=s.index('\n')+1
 note='\n## Current v3.8 delivery — 2026-10-15\n\n'
 if name=='PDF_WORKFLOW.md':note+='PROJECT_CONTINUITY_SOURCE.md contains the full MDP v4.1 and both original 38/35-entry ledgers, including the current autonomous breeding rule. Binary PDF generation/render verification remains pending: Node, ReportLab, pypdf/PyMuPDF and Poppler are unavailable. No current binary PDF is claimed.\n'
 elif name=='GITHUB_PAGES.md':note+='DIST is rebuilt from current local source with python build.py; deploy its contents (including .nojekyll) at the Pages site root. The Pages ZIP contains those same contents. Breeding, all account saves and JSON backups remain local to the player\'s browser/PC. Export/import JSON when changing file/site/browser origin. See BREEDING_UPDATE_REPORT.md for actual release verification.\n'
 else:note+='Current autonomous breeding acceptance and regression evidence is recorded in BREEDING_UPDATE_REPORT.md and tests/breeding-evidence. Older milestone totals below describe their historical source state. The retired v2.6 ecosystem UI runner assumes unlocked freshwater and missing mystery tiers; it is not a current-release acceptance gate. Do not count its aborted run as a pass.\n'
 write(name,s[:at]+note+s[at:])
prefix=prefix.replace('Playable v3.7 / MDP v4.0','Playable v3.8 / MDP v4.1',1)
at=prefix.index('## Equipment filters, inspector research');prefix=prefix[:at]+overview+prefix[at:]
write('PROJECT_CONTINUITY_SOURCE.md',prefix+m)
for name in ['index.html','js/ui.js']:
 s=read(name).replace('v3.7','v3.8')
 if name=='js/ui.js':s=s.replace('Aquarium Life v3.6','Aquarium Life v3.8')
 write(name,s)
p=ROOT/'build.py';s=p.read_text(encoding='utf8').replace("'gameContent': 'v3.7'","'gameContent': 'v3.8'").replace("ROOT / 'CASINO_RULES.md'])", "ROOT / 'CASINO_RULES.md', ROOT / 'BREEDING_RULES.md', ROOT / 'BREEDING_SAVE_SCHEMA.md', ROOT / 'BREEDING_UPDATE_REPORT.md'])");p.write_text(s,encoding='utf8')
p=ROOT/'tests/package.py';s=p.read_text(encoding='utf8').replace("'store-casino-evidence']", "'store-casino-evidence','breeding-evidence']");p.write_text(s,encoding='utf8')
print('Updated full 31-section MDP, primary design sections, catalogs, continuity and deployment metadata.')
