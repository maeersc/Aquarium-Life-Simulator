"""Update primary documentation and verbatim printable continuity."""
from pathlib import Path
r=Path(__file__).resolve().parents[2]
heading='## Ocean diving destination artwork — playable v4.0.2, 2026-10-16\n\n'
summary='Eight original pixel-art PNG environments replace the simplified expansion scenery for Indonesia, Philippines, Sri Lanka, Marshall Islands, Maldives, Australia, Florida and Mariana Trench. A central per-mode art mapping drives selection previews, proportional in-dive backgrounds and expedition-result accents. Older regional PNGs, native encounter pools, all diving gameplay, local saves and freshwater lock are preserved. See [DIVING_LOCATION_ART_REPORT.md](DIVING_LOCATION_ART_REPORT.md). Art is implemented for review; no prior livestock/art approval is changed.\n\n'
p=r/'MASTER_DEVELOPMENT_PROMPT.md';old=p.read_text(encoding='utf8');assert 'VERSION 4.4' in old
new=old.replace('VERSION 4.4','VERSION 4.5',1).replace('playable v4.0.1, 2026-10-16','playable v4.0.2, 2026-10-16',1)
new=new.replace('## Global aquarium preparation repair',heading+summary+'## Global aquarium preparation repair',1)
rule='''### Destination identity and artwork — v4.0.2 permanent

Every selectable diving destination must have a defined regional identity, a valid geographically native species pool for each supported mode, and assigned selection/in-dive artwork. An explicitly observation-only or remote nonliving research destination may retain its intentionally empty collectible living pool; artwork never authorizes new species or collection. Preserve all existing depth, wildlife-closed and transport restrictions.

The primary destination registry is `assets/diving/registry.json`. Each supported mode has one `art` entry with a unique region-mode ID, original PNG path and description. The same registered source serves the picker, proportionally cropped map and result accent. Complete prompts and original filenames live in `assets/diving/art-prompts.json`; new source-v2 PNGs are unmodified built-in ImageGen outputs, integrated for user review. Fiji/Caribbean/Hawaii/Japan source PNGs remain unchanged. Do not silently substitute unrelated scenery. Build must reject missing, duplicate or incorrectly assigned art; runtime records failed loads explicitly. Embed local assets for file/offline play and package native files with case-correct relative paths for Pages.

Seven new reefs have distinct coral/rock/lagoon/shelf compositions. Mariana uses black-navy hadal terrain, sediment, a tethered research lander and localized lamp illumination without sunlight, reef corals or living collectibles. Existing drone controls, oxygen/battery cost, catch/reveal silhouettes, receiving, emergency sale and saving remain authoritative. Art rendering is read-only and must not consume simulation RNG or alter expedition state. Keep text on solid UI panels, preserve image aspect ratio and check desktop/mobile scaling. Do not add network asset dependencies or saved art state.

'''
assert '## 5.6 Beginner Saltwater Tutorial' in new
new=new.replace('## 5.6 Beginner Saltwater Tutorial',rule+'## 5.6 Beginner Saltwater Tutorial',1)
p.write_text(new,encoding='utf8')
p=r/'PROJECT_CONTINUITY_SOURCE.md';s=p.read_text(encoding='utf8');assert old in s
s=s.replace(old,new,1).replace('Playable v4.0.1 / MDP v4.4','Playable v4.0.2 / MDP v4.5',1)
first=s.index('\n\n');s=s[:first+2]+heading+summary+s[first+2:];p.write_text(s,encoding='utf8')
for name in ['DEVELOPMENT_STATUS.md','UI_SPECIFICATION.md','ART_DIRECTION.md','ART_GENERATION_RECORD.md','README.md','GAME_DESIGN.md','TEST_REPORT.md','GITHUB_PAGES_BUILD_REPORT.md']:
 p=r/name;s=p.read_text(encoding='utf8');pos=s.index('\n\n');s=s[:pos+2]+heading+summary+s[pos+2:];p.write_text(s,encoding='utf8')
p=r/'index.html';s=p.read_text(encoding='utf8');assert 'v4.0.1' in s;p.write_text(s.replace('v4.0.1','v4.0.2'),encoding='utf8')
p=r/'build.py';s=p.read_text(encoding='utf8');assert "ROOT / 'AQUARIUM_PREPARATION_REPAIR_REPORT.md'" in s
s=s.replace("ROOT / 'AQUARIUM_PREPARATION_REPAIR_REPORT.md'","ROOT / 'AQUARIUM_PREPARATION_REPAIR_REPORT.md', ROOT / 'DIVING_LOCATION_ART_REPORT.md'",1);p.write_text(s,encoding='utf8')
p=r/'tests/package.py';s=p.read_text(encoding='utf8');s=s.replace("'preparation-evidence']","'preparation-evidence','location-art-evidence']",1);p.write_text(s,encoding='utf8')
print('Primary documentation and continuity updated to master v4.5 / playable v4.0.2')
