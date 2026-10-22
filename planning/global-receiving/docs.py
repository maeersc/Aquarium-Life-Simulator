from pathlib import Path
import re
r=Path(__file__).resolve().parents[2]
p=r/'MASTER_DEVELOPMENT_PROMPT.md';old=p.read_text(encoding='utf8');assert '### Universal diving receiving' not in old
new=old.replace('Corals/invertebrates retain explicit pre-capture receiver/mount and existing return assessment; rocks use owned placement inventory.','Corals/invertebrates retain an explicit pre-capture receiving/mount plan, then all newly collected livestock use the same saved post-boat receiving transaction. Corals explicitly confirm a currently supported mount; rocks use owned placement inventory.',1)
at=new.index('## 5.6 ')
new=new[:at]+'''### Universal diving receiving — permanent, 2026-10-16

Every implemented diving-eligible fish, coral and bottom-dwelling invertebrate uses the same receiving authority, all-owned destination diagnostics and saved post-boat ownership transaction. Resolve its actual unique biological ID/category and apply that species' own requirements; never hardcode a Chalk Bass exception or map missing IDs to another host. Validate complete unique region/mode/depth/transport profiles before spawning. Every aquarium remains visible, with disabled unsafe choices and exact actual/required checks. Preserve fish-specific ranges/group/stocking/behavior, coral light/flow/minerals/support/clearance, and invertebrate range/oxygen/flow/habitat/load requirements. A fully prepared compatible coral-only quarantine is allowed, without waiving any environmental, support or medication checks.

Preserve finite saved holding, committed condition/survival draws, explicit destination/mount, identity/health/rarity/origin/genetics where modeled/value, count/value recalculation, atomic local saves and replay receipts. Invalid receiving or a changed mount must leave pending livestock intact so a valid destination/mount can be chosen. Never mark a noninfectious injury as an infectious carrier or relax health validation to accept it. Permanent transport mortality resolves the actual host category without inventing unmeasured causes. Old saved snapshots and completed reports remain compatible; no duplicate grants or resurrection. Regression coverage must enumerate the actual eligible registry across hosts, sizes, regions and both dive modes so future complete registrations automatically use and test this service. See GLOBAL_DIVING_RECEIVING_REPORT.md for current coverage, confirmed causes, files and limits.

'''+new[at:]
assert len(re.findall(r'^# \d+\.',new,re.M))==31;p.write_text(new,encoding='utf8')
p=r/'PROJECT_CONTINUITY_SOURCE.md';s=p.read_text(encoding='utf8');assert old in s;p.write_text(s.replace(old,new,1),encoding='utf8')
note='''## Universal ocean diving receiving — 2026-10-16

All registered diving fish, corals and invertebrates now share species-aware diagnostics and explicit saved post-boat receiving. Every owned aquarium is shown; supported coral mounts and host-compatible quarantine retain all safeguards. The repair also corrects invalid noninfectious carrier flags, rock surface discovery and missing/ambiguous host mappings. Tests enumerate the real eligible registry, plus old-save, condition, expiry, replay and future-registration checks. See [GLOBAL_DIVING_RECEIVING_REPORT.md](GLOBAL_DIVING_RECEIVING_REPORT.md). Earlier host-limited flow descriptions are historical where superseded. Game v3.9 / master v4.2; local saves and freshwater lock remain.

'''
for name in ['README.md','GAME_DESIGN.md','DEVELOPMENT_STATUS.md','UI_SPECIFICATION.md','TEST_REPORT.md','GITHUB_PAGES_BUILD_REPORT.md','MYSTERY_DIVING_RULES.md','DIVING_RECEIVING_REPAIR_REPORT.md']:
 p=r/name;s=p.read_text(encoding='utf8');pos=s.index('\n\n')+2;p.write_text(s[:pos]+note+s[pos:],encoding='utf8')
p=r/'MORTALITY_LOG_SCHEMA.md';s=p.read_text(encoding='utf8');pos=s.index('\n\n')+2;p.write_text(s[:pos]+'''## Universal transport hosts — 2026-10-16

Transport schema 3 now resolves fish, coral and invertebrate identities/categories from the same registry used for receiving. Pending recovery, settlement receipts and expiry are shared; all real transport losses use the existing permanent journal with unknown measurements left unknown. Old fish-only transport and legacy records remain valid. See GLOBAL_DIVING_RECEIVING_REPORT.md.

'''+s[pos:],encoding='utf8')
print('Updated the primary universal receiving specification and full continuity.')
