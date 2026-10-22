from pathlib import Path
import re
r=Path(__file__).resolve().parents[2]
def read(n):return (r/n).read_text(encoding='utf8')
def write(n,s):(r/n).write_text(s,encoding='utf8')
rule='Every valid Reef Diving and Deep Sea Diving expedition must provide at least one reachable mystery fish encounter. Its species is concealed using a question-mark silhouette until successful return to the boat. Geographic eligibility, inventory, oxygen, post-dive survival, and save persistence remain mandatory.'
summary='''## Mystery fish diving — v3.9 current, 2026-10-15

Implemented the authorized Mystery Fish update (request v3.5) on top of playable v3.8. New valid Reef/Deep trips guarantee a reachable regional fish, concealed until boat return, with saved assignments, original question-mark art/reveal, explicit safe receiving and permanent transport-loss evidence. Empty/closed collectible pools block launch. Existing oxygen, fees, resale, local accounts, biology, genetics, breeding, care rewards and freshwater lock remain. See [MYSTERY_DIVING_RULES.md](MYSTERY_DIVING_RULES.md) and [MYSTERY_DIVING_UPDATE_REPORT.md](MYSTERY_DIVING_UPDATE_REPORT.md). Current master is v4.2; earlier release entries are historical where superseded.

'''
old=read('MASTER_DEVELOPMENT_PROMPT.md');assert 'VERSION 4.1' in old and rule not in old
m=old.replace('VERSION 4.1','VERSION 4.2',1).replace('playable v3.8, 2026-10-15','playable v3.9, 2026-10-15',1)
m=m.replace('## Automatic marine breeding — v3.8 current, 2026-10-15',summary+'## Automatic marine breeding — v3.8 historical, 2026-10-15',1)
start=m.index('## 5.5 Ocean Diving');end=m.index('## 5.6 ',start)
primary='''## 5.5 Ocean Diving — Primary Mystery Fish Specification (playable v3.9)

'''+rule+'''

Ocean Diving remains saltwater-only and uses the existing fixed-step simulation, shared modal, health, value, inventory and local save authority. Its button remains beside saved Keeper Level. Reef requires Keeper 5 and exactly 1,000 AC; Deep Sea requires Keeper 10 and exactly 10,000 AC, all rentals included once in an atomic confirmed launch.

The data-driven registry `assets/diving/registry.json` now has eight encounter profiles referencing existing approved fish/coral/invertebrate IDs, with science, region, habitat, depth, art and transport evidence. No species or rarity is added. Select a guaranteed fish uniformly from implemented, verified, collectible fish matching region/mode/survey depth; never use Mystery Egg odds. Fiji Reef: Exquisite fairy wrasse / Yellow longnose butterflyfish, 50% each; Fiji Deep: Yellow longnose butterflyfish, 100%; Caribbean Reef: Chalk Bass, 100%; Caribbean Deep: Candy Basslet, 100%; Japan Reef: Spotted Boxfish, 100%; Japan Deep: Blotched Anthias, 100%. These small verified pools contain no Legendary; preserve all six rarities globally. Hawaii retains observation-only wildlife and has no collectible pool, so both launches are blocked before charge. Any missing valid fish pool likewise blocks its destination clearly, without invented or incorrect-region substitutes. Species-specific geographic/depth evidence and selection details are in MYSTERY_DIVING_RULES.md. Existing 38/35-entry roster ledgers and art approval boundaries remain.

Both compact 11×7 maps retain terrain, regional scenery, boat and twelve encounter positions. First eight rocks remain; object 9 at (4,1) is a guaranteed mystery fish. Its safe round trip costs six movements / 30% oxygen, or four movements / 20% when capturing from an adjacent cell. Optional final three objects retain existing regional selection/presence rules; all optional fish are also concealed. Each fish swims smoothly inside its saved logical cell, so animation cannot move the guarantee beyond its safe route. Use one shared original dark generic pixel silhouette and large question mark for every fish. Do not expose names, scientific names, rarity, asset value or identifying shapes/markings through planner, map, interaction panel, temporary inventory or failed report. A local offline client/save is inspectable, not cryptographically secret; single-species pools limit uncertainty.

WASD, arrows and direction buttons move cardinally. Native key repeat is ignored in favor of controlled held repeats. Start at 100% oxygen; each successful movement consumes exactly five percentage points. Blocked movement, idle time, frames and collection clicks use none. Preserve warnings at 30/15/5%, route cost and return reserve. Zero oxygen fails even on boat arrival. Left-click within one Manhattan cell attempts capture; farther clicks select only. Recheck range, eight-slot capacity and duplicate status in the authority. Captured fish display `Unknown Fish — ?`, take one temporary slot and grant no permanent ownership. Inventory cannot overflow or discard existing finds. Failure/confirmed abandonment forfeits finds without identity reveal, fee refund or livestock grant.

Successful positive-oxygen boat return saves revealed results with actual common/scientific name, rarity, existing species art, original short pixel wipe and origin. Reduced-motion uses final art immediately. Pending recovery is explicitly labeled Awaiting receiving assessment, destination Not received, owned asset value zero. Choose a safe compatible cycled aquarium or quarantine after reveal; never auto-select or auto-place. Recheck safety cumulatively on each receive action. Final results display actual condition, destination and current central asset value. Close/reopen resumes pending results; block another launch until pending fish are received, explicitly released or expired. Corals/invertebrates retain explicit pre-capture receiver/mount and existing return assessment; rocks use owned placement inventory.

Preserve the existing survival formula using species sensitivity, transport quality, elapsed game time, movement, prior condition and receiving/quarantine. Commit survival/condition draws at boat return; retries or reloads do not reroll. Preserve healthy/stressed/injured/suspected illness/DOA, finite sensitivity-based holding deadlines and real mortality. Pending expiry runs on the shared live/offline simulation. Transport DOA adds an event to the existing permanent account mortality journal with identity, actual loss time, known trigger and available expedition evidence. Unmeasured water, temperature, hunger, health history and equipment remain unknown; do not invent a physiological cause. Do not count unowned transport loss as an owned-tank death or alter care reward rules. Survivors enter the existing health system with permanent origin/trip provenance. Existing regular resale is floor(0.60 × Deep reference); Deep requires Reputation 5, matching active Wanted request and all existing eligibility limits under 19.6. Do not guarantee profit.

Planning, play, confirmation and results keep the authoritative aquarium clock at 1×, 20 real minutes per game day, while preserving the prior speed preference. Keep hunger, chemistry, disease, eggs, coral, growth, equipment, calendar/store rotation and rewards advancing. Save active region/mode, guarantee ID, hidden assignment, position, collected flags, inventory, oxygen, fee/transaction and RNG; save report reveal state, precommitted assessment, deadline, recovery result/destination and death-record link. Local completion/recovery receipts prevent ordinary replay grants. Legacy active trips resume unchanged without retroactive rerolls. Keep all data on the player's PC/browser and existing export/import/timeline safeguards.

Preserve existing diver/boat/equipment/scenery and approved species art. No new art is automatically approved. X/Escape/backdrop dismiss ordinary windows but protect active trips with explicit loss confirmation; inside clicks cannot click through. Sticky oxygen/inventory HUD and responsive mouse/keyboard/touch controls remain. Full implementation/testing/limits: MYSTERY_DIVING_UPDATE_REPORT.md. Other master sections reference this primary specification instead of duplicating it.

'''
m=m[:start]+primary+m[end:]
m=m.replace('Diving extension version 1 adds optional migration', 'Mystery encounter/reveal/recovery fields and transport journal schema 3 are additive under the existing save schema; see §5.5 and MYSTERY_DIVING_RULES.md. Diving extension version 1 adds optional migration',1)
idx=m.index('# 29. PROJECT FILE STRUCTURE')
m=m[:idx]+'''## 28.1 Future Ocean Exploration — concept only

Future separately authorized exploration may include larger original maps, varied depths/ecosystems, habitat discovery, photography, observation/research, hidden locations and rare environmental encounters. Use original mechanics/UI/art; never copy another game's protected assets, maps, interface, characters or distinctive creative content. This concept is documentation only; no expanded exploration system is part of the current release. Current diving remains governed only by §5.5.

'''+m[idx:]
assert len(re.findall(r'^# \d+\.',m,re.M))==31
write('MASTER_DEVELOPMENT_PROMPT.md',m)
c=read('PROJECT_CONTINUITY_SOURCE.md');assert old in c
c=c.replace(old,m,1).replace('Playable v3.8 / MDP v4.1','Playable v3.9 / MDP v4.2',1)
first=c.index('## Automatic marine breeding');c=c[:first]+summary+c[first:];write('PROJECT_CONTINUITY_SOURCE.md',c)
for n in ['README.md','DEVELOPMENT_STATUS.md','GAME_DESIGN.md','UI_SPECIFICATION.md','TEST_REPORT.md','GITHUB_PAGES_BUILD_REPORT.md','DIVING_UPDATE_REPORT.md']:
 s=read(n);end=s.index('\n\n')+2;s=s[:end]+summary+s[end:]
 s=s.replace('## Ocean Diving v2.8 — current, 2026-10-14','## Ocean Diving v2.8 — historical, 2026-10-14')
 write(n,s)
write('RESEARCH_SOURCES.md',read('RESEARCH_SOURCES.md').replace('\n\n','\n\n## Fiji mystery-fish eligibility — v3.9\n\nTwo existing implemented fish gain Fiji encounter profiles only. See the primary Fiji checklist and museum depth/range sources linked in [MYSTERY_DIVING_RULES.md](MYSTERY_DIVING_RULES.md); these support regional eligibility, not gameplay survival rates, conservation assumptions or collection authorization. No new biological species are introduced.\n\n',1))
write('MORTALITY_LOG_SCHEMA.md',read('MORTALITY_LOG_SCHEMA.md').replace('\n\n','\n\n## Additive transport evidence — playable v3.9\n\nThe same journal accepts schemaVersion 3 / context diving-transport events for unowned mystery-fish DOA. Stable account/trip/encounter IDs prevent duplicate events. Evidence stores actual simulated loss time, live/offline run context, species, expedition, diver movement/oxygen, collection/deadline, transport quality, prior-condition and committed assessment draws. Water and equipment are empty, hunger/nutrition/hpBefore are null: these were not measured in transport. No invented biological diagnosis or owned-tank death/reward mutation. Existing detailed schema 2 and legacy records remain valid and unchanged; full exports include these transport records. See MYSTERY_DIVING_RULES.md and §5.5 of the master.\n\n',1))
for n in ['index.html','js/ui.js','build.py']:
 write(n,read(n).replace('v3.8','v3.9'))
s=read('build.py').replace("ROOT / 'BREEDING_UPDATE_REPORT.md'", "ROOT / 'BREEDING_UPDATE_REPORT.md', ROOT / 'MYSTERY_DIVING_RULES.md', ROOT / 'MYSTERY_DIVING_UPDATE_REPORT.md'");write('build.py',s)
s=read('tests/package.py').replace("'breeding-evidence']", "'breeding-evidence','mystery-diving-evidence']");write('tests/package.py',s)
s=read('MYSTERY_DIVING_RULES.md').replace('| Fiji / Deep Sea | 80 m |','| Fiji / Deep Sea | 75 m |').replace('Deep 80 m','Deep 75 m').replace(' (PDF p.42 / printed p.40)','').replace(' (PDF p.47 / printed p.45)','');write('MYSTERY_DIVING_RULES.md',s)
print('Updated primary diving specification, complete continuity, current docs and build version.')
