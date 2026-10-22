from pathlib import Path
import re
r=Path(__file__).resolve().parents[2]
old=(r/'MASTER_DEVELOPMENT_PROMPT.md').read_text(encoding='utf8');c=(r/'PROJECT_CONTINUITY_SOURCE.md').read_text(encoding='utf8');assert old in c
intro='''## Global aquarium preparation repair — v4.0.1, 2026-10-16

Corrected the saved `prepared=true` / stale `emptyDry=true` contradiction across setup, rendering, biological readiness and all receiving hosts. Existing saves repair only from preparation completion evidence; normal chemistry alone never certifies preparation. See [AQUARIUM_PREPARATION_REPAIR_REPORT.md](AQUARIUM_PREPARATION_REPAIR_REPORT.md). Master v4.4 preserves all 31 major sections, local saves, freshwater lock and the 20-minute day. Earlier release reports remain historical where superseded.

'''
m=old.replace('VERSION 4.3','VERSION 4.4').replace('### Offline Browser Edition — playable v4.0,','### Offline Browser Edition — playable v4.0.1,',1)
at=m.index('## Global diving expansion');m=m[:at]+intro+m[at:]
at=m.index('## 12.6 ')
rule='''### Authoritative preparation lifecycle — v4.0.1 permanent

Use `AL.Preparation` for setup and preparation checks across stores, fish/coral/invertebrate receiving, eggs/offspring, quarantine, health, rendering and simulation. The existing `prepared` boolean records completed water preparation; `emptyDry` records physical absence of water. Prepared water implies filled water. Do not add a second persisted phase enum that can diverge from these flags. Derive four displayed stages: dry, filled but unprepared, prepared saltwater, prepared and cycled. Current cycled status additionally requires both established bacterial colonies and no active fishless cycle; preparation alone never certifies chemical safety or species compatibility.

The existing free Prepare water action includes filling and atomically sets `prepared=true`, `emptyDry=false`, recording preparation once. An optional Add water action only fills; it never prepares, cycles or grants livestock. Substrate, rocks and installed equipment are independent setup steps and cannot certify water preparation. Persist per-tank preparation observations, filled/prepared actions and completed cycles in a bounded `preparationHistory`; timestamps are actual game observations, never invented original setup dates.

Migration repairs a stale dry marker when saved `prepared=true` confirms prior completion. A lost false preparation flag can be restored from valid per-tank completed preparation/cycle history, or legacy completed fishless-cycle progress (the original simulation only advanced cycling after preparation). Honor later dry/filled history rather than reusing an earlier completed cycle. Default/normal water values, biomass, equipment, colony percentages, elapsed time and collection-wide preparation statistics alone are insufficient evidence. Never reset chemistry, bacteria, equipment, rocks, living/dead livestock, money or history to repair these flags; never award preparation or cycling a second time. Apply the same normalization at restore, action, save and simulation boundaries, including offline catch-up.

Keep the all-owned-aquarium compatibility table and report actual preparation state. A filled unprepared tank is not labeled dry. Species-specific minimum liters, temperature, salinity, pH, oxygen, toxins, habitat, light/flow, cycling, stocking and treatment/quarantine restrictions remain independent gates. A nominal 20-gal/75-L aquarium still fails a 30-US-gallon species minimum; a correctly prepared compatible 80-gal/300-L home may receive it. Actual physical liters and installed/effective equipment capacities do not change because of rounded nominal gallon labels.

Capacity audit: marine adult-load reservations count viable eggs/offspring once; nonviable eggs reserve no future adult load. Retained dead fish occupy existing physical/save entity slots until removed, while contributing no living adult load. Regular fish compatibility and diving tables use the same counts. Keep independent fish, coral and invertebrate array limits and existing equipment wear advisories; no blanket full-output equipment restriction is introduced. Freshwater biology and its lock remain unchanged.

'''
m=m[:at]+rule+m[at:];assert len(re.findall(r'^# \d+\.',m,re.M))==31
(r/'MASTER_DEVELOPMENT_PROMPT.md').write_text(m,encoding='utf8');(r/'PROJECT_CONTINUITY_SOURCE.md').write_text(c[:c.index(old)].replace('Playable v4.0 / MDP v4.3','Playable v4.0.1 / MDP v4.4')+m+c[c.index(old)+len(old):],encoding='utf8')
for n in ['README.md','GAME_DESIGN.md','DEVELOPMENT_STATUS.md','UI_SPECIFICATION.md','TEST_REPORT.md','GITHUB_PAGES_BUILD_REPORT.md']:
 p=r/n;s=p.read_text(encoding='utf8');a=s.index('\n');p.write_text(s[:a+1]+'\n'+intro+s[a+1:],encoding='utf8')
p=r/'index.html';s=p.read_text(encoding='utf8');assert 'OFFLINE EDITION · v4.0' in s;p.write_text(s.replace('OFFLINE EDITION · v4.0','OFFLINE EDITION · v4.0.1'),encoding='utf8')
p=r/'build.py';s=p.read_text(encoding='utf8').replace("'gameContent': 'v4.0'","'gameContent': 'v4.0.1'").replace("ROOT / 'DIVING_EXPANSION_SAVE_SCHEMA.md'", "ROOT / 'DIVING_EXPANSION_SAVE_SCHEMA.md', ROOT / 'AQUARIUM_PREPARATION_REPAIR_REPORT.md'");p.write_text(s,encoding='utf8')
print('Updated master v4.4 and printable continuity; prepared v4.0.1 release documents.')
