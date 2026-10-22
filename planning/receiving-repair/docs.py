from pathlib import Path
r=Path(__file__).resolve().parents[2]
p=r/'MASTER_DEVELOPMENT_PROMPT.md';old=p.read_text(encoding='utf8');assert '### Receiving diagnostics repair' not in old
at=old.index('## 5.6 ')
addition='''### Receiving diagnostics repair — 2026-10-16

Every owned aquarium must appear in the fish receiving selector, showing name, US gallons, water classification, actual temperature and eligibility. Disable rejected destinations and expose exact reasons with actual values/requirements; never hide them. Expandable checks cover habitat, volume, species temperature range, salinity, pH, ammonia/nitrite/oxygen, prepared/cycled water and both bacterial colonies, working filter/circulation, stocking/reserved offspring, entity capacity, quarantine/course restrictions and all existing species safeguards. Quarantine is optional for an untreated catch, with its existing survival benefit; introducing untreated livestock into an active restricted course is unavailable. Show equipment condition/output without demanding perfect condition. Actual readings, not rounded display text or thermostat target, control compatibility. Preserve explicit selection/focus and refresh eligibility when aquarium conditions change.

Show the unchanged finite holding deadline and time remaining in game time with an approximate 1× real-time equivalent. Read-only UI/validation errors must not delete, kill, reroll or alter the specimen/deadline. Only existing expiry or actual transport assessment causes mortality. Successful receiving must use the existing validated transaction, permanent ID/health/genes/provenance, count/value recalculation and local save/receipts, clearing pending status without duplicates. Preserve old saves and freshwater lock. See DIVING_RECEIVING_REPAIR_REPORT.md for the Chalk Bass audit, precise confirmed UI cause and diagnostic limitations; 80 gallons and 27°C alone do not prove a particular saved tank's eligibility.

'''
new=old[:at]+addition+old[at:];p.write_text(new,encoding='utf8')
p=r/'PROJECT_CONTINUITY_SOURCE.md';c=p.read_text(encoding='utf8');assert old in c;p.write_text(c.replace(old,new,1),encoding='utf8')
note='''## Diving receiving diagnostics repair — 2026-10-16

All owned aquariums now remain visible in receiving, with disabled incompatible options, exact actual/required checks, preparation/quarantine guidance, live eligibility refresh and the unchanged finite holding countdown. Properly prepared 80-gal marine tanks at exactly 27°C can receive Chalk Bass subject to existing transport survival; legitimate safeguards remain enforced. See [DIVING_RECEIVING_REPAIR_REPORT.md](DIVING_RECEIVING_REPAIR_REPORT.md) for the confirmed UI cause, data audit, files, tests and the limits of identifying an unsupplied player save. Current gameplay stays v3.9 / master v4.2, with local saves and freshwater lock preserved.

'''
for n in ['DEVELOPMENT_STATUS.md','TEST_REPORT.md','GITHUB_PAGES_BUILD_REPORT.md']:
 p=r/n;s=p.read_text(encoding='utf8');pos=s.index('\n\n')+2;p.write_text(s[:pos]+note+s[pos:],encoding='utf8')
p=r/'MYSTERY_DIVING_RULES.md';s=p.read_text(encoding='utf8');pos=s.index('## Interaction and reveal');s=s[:pos]+'''## Receiving diagnostics repair — 2026-10-16

All owned destinations are listed, including disabled incompatible tanks with precise reasons and actual/required checks. Working filter/circulation and absence of an active restricted medication course are checked alongside all prior biological safeguards. Eligibility updates with live aquarium state; explicit selection/focus is retained. Holding displays remaining game time and approximate real seconds, without changing the original finite deadline or simulation. Report/validation queries never alter health, assignment, survival draws or deadline. The original player's particular failed predicate cannot be reconstructed from volume/temperature alone. See [DIVING_RECEIVING_REPAIR_REPORT.md](DIVING_RECEIVING_REPAIR_REPORT.md).

'''+s[pos:];p.write_text(s,encoding='utf8')
print('Updated primary receiving specification and complete continuity.')
