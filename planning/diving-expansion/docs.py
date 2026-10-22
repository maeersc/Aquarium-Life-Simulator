from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[2]
old=(ROOT/'MASTER_DEVELOPMENT_PROMPT.md').read_text(encoding='utf8');c=(ROOT/'PROJECT_CONTINUITY_SOURCE.md').read_text(encoding='utf8')
assert old in c
intro='''## Global diving expansion and liquidation — playable v4.0, 2026-10-16

Implemented the authorized Emergency Diving Sales & Rock Resale and Global Ocean Diving Expansion request (specification v3.6). Seven new reef selections and Mariana remote exploration use the central registry. Catch development, medical assessment, concealed attached eggs and regular-store liquidation extend the existing receiving authority. See [DIVING_EXPANSION_REPORT.md](DIVING_EXPANSION_REPORT.md) and [DIVING_EXPANSION_SAVE_SCHEMA.md](DIVING_EXPANSION_SAVE_SCHEMA.md). Earlier milestone reports remain historical where superseded. All saves stay local; freshwater remains locked; one game day remains 20 real minutes.

'''
m=old.replace('VERSION 4.2','VERSION 4.3').replace('### Offline Browser Edition — playable v3.9, 2026-10-15','### Offline Browser Edition — playable v4.0, 2026-10-16')
m=m.replace('## Mystery fish diving — v3.9 current, 2026-10-15',intro+'## Mystery fish diving — v3.9 historical, 2026-10-15',1)
start=m.index('The data-driven registry `assets/diving/registry.json` now has eight encounter profiles')
end=m.index('\n',start)
m=m[:start]+'''The data-driven `assets/diving/registry.json` contains nine encounter profiles referencing existing species IDs and twelve destination selections; no biological species was added. Original Fiji, Caribbean, Hawaii and Japan remain. New reef selections: Coral Triangle—Indonesia (Bunaken), Coral Triangle—Philippines (Puerto Galera), Sri Lanka (Kayankerni), Marshall Islands (Majuro), Maldives (Madivaru Beyru), Australia (Lady Musgrave Island/Great Barrier Reef), and Florida (Tortugas/Keys). Existing Yellow longnose butterflyfish is eligible at the six new Indo-Pacific zones; existing Ocellaris clownfish additionally inhabits the two Coral Triangle zones; Chalk Bass inhabits Florida. Country range evidence is supplemented by locality records bundled in the registry. Existing 38/35-entry livestock and art ledgers remain unchanged. See DIVING_EXPANSION_REPORT.md for sources and conservative content limits. Hawaii remains wildlife-closed. Missing valid living pools block ordinary collection launches; the explicitly approved Mariana remote survey is a nonliving-only exception, never an exception to livestock receiving safety.'''+m[end:]
pos=m.index('## 5.6 ')
rules='''### Regional collection, random development and medical assessment — v4.0 permanent

Every living encounter must resolve through the existing species registry, verified region/habitat/depth profile and shared receiving rules. Never substitute fish to fill empty pools. All eligible ordinary expeditions retain the reachable concealed mystery-fish opportunity, eight slots, movement controls, 5% oxygen per successful movement and mandatory boat return. Fish identity, rarity, value and developmental art stay concealed before return.

Approved configurable stage weights are baby 20%, juvenile 35%, adult 45%. Restrict and normalize to biologically eligible stages: settled Ocellaris in anemone-associated Coral Triangle habitat supports all three; remaining current profiles conservatively allow juveniles/adults. No free-swimming larva is mislabeled a settled baby. Save the actual individual at capture with ID, approximate accelerated age, growth, adult size, sex/temperament, genetics/pattern, source and expedition. Receiving never recreates it as an adult. Young fish retain existing fine-food metabolism, protection and sale development checks. Dedicated refuge and fine fry food are required for baby receiving.

Use the same saved survival/medical draws for receiving and emergency valuation, never redraw in UI or after load. Transport assessment includes species sensitivity, transport quality, elapsed exposure, movements, pre-existing risk, young-stage fragility and quarantine benefit. Healthy, stressed, malnourished, injured, suspected infection, severely compromised and dead-on-arrival outcomes are possible. Existing host-eligible conditions are used; symptoms are not diagnoses. Show HP, signs, quarantine advice, treatment host restrictions and Disease & Treatment Guide access. Actual finite holding and permanent transport mortality records remain.

### Mystery eggs — v4.0 permanent

An eligible expedition has one independent 3% discovery opportunity; store Mystery Egg rarity odds are untouched. Current external egg pool: existing Ocellaris in the two Coral Triangle zones, attached to a removable substrate chip near anemone habitat. Never float demersal eggs in open water or collect mouthbrooded/liveborn offspring as eggs. Assign permanent hidden species, clutch ID, genetics/embryo pattern, provenance, approximate development and viability at collection. Parents remain unknown. One representative egg uses an explicitly simplified recovery model with 85% initial estimated viability and a 24-game-hour finite holding deadline; no incubation occurs in inventory. Save/load cannot reroll identity.

List every owned aquarium with the shared species checks and additional empty dedicated marine incubation, fine-food and gentle-flow requirements. Development uses the existing species water/oxygen and suitable-hour model, with operating filter/circulation and protected support required. Ordinary wear tolerance is explicit. Poor conditions pause progress and reduce viability; failure is retained in the expedition report. Identity, rarity, coloration, genetic pattern and expected asset value stay concealed in map, results, aquarium scene, inspector and Journal until hatch. Hatching creates a unique actual early larva, transfers established genetics/provenance, reveals the report and updates the Field Journal. Larvae need fine food and retain accelerated game growth; this does not claim complete real-world captive culture. Store-purchased identified Mystery Eggs retain their old reveal policy.

### Emergency Sale and diving rock resale — v4.0 permanent

Unreceived living diving fish/coral/invertebrates may use regular Aquarium Store Emergency Sale without a suitable receiver: `max(0, floor(central eligible specimen value × 0.25))`. Calculate using the actual saved specimen, stage, genetics/quality, health and transport survival; dead/expired/protected specimens are ineligible. Show and confirm the exact offer. This service is unavailable after receiving, does not satisfy Wanted requests and earns no Deep Market reputation. Preserve regular owned diving resale at exactly floor(Deep reference × 0.60), and preserve Deep Market Reputation 5, active Wanted request, condition/access/budget checks.

Recovered nonliving rocks retain unique item ID, product group/variant, size/one-piece quantity, condition, region and expedition. Keep/place or explicitly sell after successful boat return, through expedition results or Aquarium Store → Saltwater → Sell. Central rock estimate is `floor((existing product price + variant × 25) × quantity × condition)`; buyback is floor(estimate × 0.40). This stays below retail. Placing/removing preserves the same identity/provenance; removal still refuses attached coral or eggs and requires inventory space. Store-bought rocks cannot masquerade as recovered salvage. Finite inventory limits remain.

Each confirmed sale produces exactly one account ledger receipt with item/species ID, expedition, dealer, actual amount, time and resulting balance; a valid zero-AC emergency offer records one explicit zero income receipt. Atomic ownership/status changes, financial keys and local settled receipts prevent double clicks and stale-save replay. No server is added. See DIVING_EXPANSION_SAVE_SCHEMA.md.

### Mariana Trench — v4.0 permanent

Deep Sea only, Keeper 10 and 10,000 AC. Represent a fictional tethered research drone at a 6,000 m southern Mariana hadal slope with battery presentation (100%, 5% per successful movement) and return to dock. Never draw an ordinary diver at hadal depth. Registry records approximately 2 °C, approximately 600 atmospheres, no decompression-safe livestock transport and no approved pressure aquarium. There is no valid living pool, egg pool or ordinary reef receiving path; only nonliving fictional sample recovery. No specialized pressure containment or fabricated hadal livestock is authorized.

'''
m=m[:pos]+rules+m[pos:]
m=m.replace('## 24.5 Expedition Persistence and Local Receipts','## 24.5 Expedition Persistence and Local Receipts')
m=m.replace('Mystery encounter/reveal/recovery fields and transport journal schema 3 are additive', 'The v4.0 catch, sale, rock and concealed diving-egg fields are documented in DIVING_EXPANSION_SAVE_SCHEMA.md. Mystery encounter/reveal/recovery fields and transport journal schema 3 are additive')
assert len(re.findall(r'^# \d+\.',m,re.M))==31
(ROOT/'MASTER_DEVELOPMENT_PROMPT.md').write_text(m,encoding='utf8')
prefix=c[:c.index(old)].replace('Playable v3.9 / MDP v4.2, 2026-10-15.','Playable v4.0 / MDP v4.3, 2026-10-16.')
(ROOT/'PROJECT_CONTINUITY_SOURCE.md').write_text(prefix.split('\n',4)[0]+'\n\n'+intro+'\n'.join(prefix.split('\n')[2:])+m+c[c.index(old)+len(old):],encoding='utf8')
for name in ['README.md','GAME_DESIGN.md','DEVELOPMENT_STATUS.md','BALANCE_REPORT.md','UI_SPECIFICATION.md','CURRENT_LIVESTOCK_CATALOG.md','ART_DIRECTION.md','MYSTERY_DIVING_RULES.md','GITHUB_PAGES_BUILD_REPORT.md','TEST_REPORT.md']:
 p=ROOT/name;s=p.read_text(encoding='utf8');a=s.find('\n');p.write_text(s[:a+1]+'\n'+intro+s[a+1:],encoding='utf8')
schema='''# Diving expansion save schema — v4.0 (additive schema 2)

All data remains in the player's browser localStorage and local JSON export/import. No server storage, account upload or network call was introduced. Keep the existing `diving.version=1`, schema 2, clocks and financial account IDs. The data registry is version 2; this is a content registry version, not a save reset.

- Captured fish inventory items optionally contain `individual` (actual stable fish ID, genes/pattern and developmental state) and `captureStage`. Existing old pending specimens without this optional snapshot retain their legacy biological interpretation; new captures always persist it. Returned older captures receive a snapshot once, never from a render.
- Boat `recovery` retains saved survival and medical draws and adds terminal `sold` with `finishedAt`, `transactionId`, `saleAmount`. Pending/received/failed/released saves remain supported. Emergency sale never creates a permanent owned fish.
- `diving.saleReceipts` contains stable recovery, rock-sale and egg-settlement keys. It extends the existing world-scoped diving local receipt ledger. Finance rows add expedition/item IDs; zero-value emergency sales explicitly permit a zero income row. All other zero wallet operations retain old behavior.
- Rocks add `region`, `quantity=1`, `size`, `condition`, `acquired`; missing legacy values migrate deterministically without reroll. Installed recovered hardscape retains the same ID plus a `recoveredRock` audit/return payload. Sale requires recovered inventory ownership. Stale already-sold inventory is removed through receipts; a stale placed sold rock is rejected rather than removing coral support.
- New active `kind=egg` objects use fixed registry identity with an attached-substrate context. Captured items save an actual brood ID, species, genes/embryos, provenance, progress=0, required suitable hours, viability, finite deadline and `diveHidden=true`.
- Returned `eggRecovery` status is pending/incubating/hatched/failed/released; hidden identity remains authoritative but is concealed from player UI. Incubation creates one same-ID brood. Hatching records its one new offspring ID and preserves genes/pattern/source. `diveLarva` records unknown-parent wild egg origin separately from natural captive `naturalOrigin`/pair records.
- Mariana saves use the original `deep` mode plus region `mariana` and `active.remote=true`, retaining exact 100-minus-5-times-steps movement accounting. No live ownership profile exists.

Current Save validation checks all existing tank/entities, health, financial reconciliation and genetic profiles in addition to new active snapshots, regional eggs, recovery sales and rock ownership. Main simulation, finite deadlines and egg incubation run from the same fixed-step model while active or catching up offline. The last-aquarium invariant is preserved; the liquidation service itself does not depend on a receiver.

Full permanent mechanics are in Master §5.5. PDF continuity notes are updated in PROJECT_CONTINUITY_SOURCE.md; no binary PDF regeneration is claimed.
'''
(ROOT/'DIVING_EXPANSION_SAVE_SCHEMA.md').write_text(schema,encoding='utf8')
build=ROOT/'build.py';s=build.read_text(encoding='utf8').replace("'gameContent': 'v3.9'","'gameContent': 'v4.0'").replace("ROOT / 'GLOBAL_DIVING_RECEIVING_REPORT.md'", "ROOT / 'GLOBAL_DIVING_RECEIVING_REPORT.md', ROOT / 'DIVING_EXPANSION_REPORT.md', ROOT / 'DIVING_EXPANSION_SAVE_SCHEMA.md'");build.write_text(s,encoding='utf8')
print('Updated master v4.3 (31 sections), complete printable continuity and release documentation.')
