# Global ocean diving receiving repair — v3.9, 2026-10-16

The shared receiving system now covers **every currently registered diving-eligible fish, coral and bottom-dwelling invertebrate**, and automatically reads future registered definitions. There is no Chalk Bass special case. Previous receiving reports are historical where this universal flow supersedes them.

## Confirmed causes

1. The original UI filtered out incompatible destinations and hid their reasons. The earlier repair addressed all fish, but corals/invertebrates still used that older branch and a separate automatic return-time ownership path. All hosts now use `AL.DiveReceiving.report` / `destinations` and the same saved, explicit post-boat `diveRecover` transaction.
2. **A reproduced invertebrate health bug prevented valid receiving.** Condition draws 15–24 assigned the noninfectious `injury` condition with `carrier:true`; health save validation correctly rejected it with `Invalid marine health/market save: noninfectious carrier`. The Porcelain Anemone Crab test failed before the repair. The receiver now derives the carrier flag from the actual condition's contagiousness. That invertebrate outcome remains an injury, labeled injured; it does not invent a fish disease or weaken validation. Fish bacterial syndromes and coral pests retain their own valid host/contagion behavior.
3. Coral destination discovery sampled near each rock's anchor rather than its actual upper surface, omitting valid rock mounts. It now samples the existing collision geometry and delegates support, depth, footprint and clearance validation to `Habitat.placement`. A rack is not required when a valid allowed rock surface exists.
4. Receiving mappings previously defaulted unknown IDs to invertebrates and assumed fish definitions in transport mortality. Missing/ambiguous IDs now fail explicitly. Registry validation rejects incomplete/duplicate/held/geographically invalid transport profiles before spawning them; mortality records resolve the real host category.

An unsupplied player's original tank state still cannot be reconstructed from volume and temperature alone. The repaired diagnostics display its exact actual/required checks instead of guessing or overriding them.

## Shared flow and biological requirements

All newly collected diving livestock return as saved pending recovery, with precommitted survival/condition draws and a finite species-conditioned holding deadline. Permanent ownership requires an explicit safe destination. Corals retain the pre-capture receiving/mount plan and must explicitly confirm a currently valid mount after return. Invertebrates also retain their receiving plan, then confirm through the same receiving transaction. Mystery fish remain concealed until boat return. Rocks keep their existing inventory/placement flow.

Every owned aquarium appears before collection when a receiving plan is required and after boat return, including disabled incompatible/freshwater tanks with exact reasons. All host types use the same diagnostic table, actual values, requirements and preparation advice. Selection/focus, live refresh, countdown and existing local saves remain. A changed or removed mount/unsafe receiver blocks receiving while preserving the pending specimen/deadline; another compatible destination/mount can be chosen.

Fish use their own volume, temperature, pH, salinity, adult load, group, predator, habitat, Keeper and existing specialist requirements. Corals use their own minimum volume, permitted mounts/spacing, light/flow requirements and the existing coral water/mineral rules (including the coral 24–28°C range, not the fish 24–27°C range). Invertebrates use their own volume/ranges/load/habitat, filter-feeding flow, 40-host/nursery capacity and oxygen ≥6 mg/L, not the fish 5.5 mg/L threshold. All retain prepared/cycled water, functioning equipment, toxicity limits and all existing species safeguards.

A coral may use a properly equipped, cycled, mounted **coral-only quarantine**, without fish, invertebrates or reserved viable offspring. This corrects the previous blanket reef-only admission gate for that valid receiving facility. Water, minerals, light, flow, support/clearance and active-medication safeguards remain mandatory. Fish/invertebrate quarantine follows their own requirements. Quarantine never bypasses compatibility; the existing transport survival bonus is retained.

The common transfer creates one permanent individual through the correct existing constructor, keeping rarity, origin/trip/region/mode, health/condition, existing genetics/pattern identity where modeled, and central individual value. Core transactions update counts/value and validate/save atomically. Settled status and local receipts prevent double receiving and older-save replay. Historical transport snapshots remain audit records, not extra livestock. Corals/invertebrates now use the existing permanent transport-death journal too, with their real category and unknown measurements left unknown.

Older settled saves remain unchanged. Older active non-fish transport snapshots that stored `collected:false` are accepted and normalized to a collected recovery snapshot only at the saved boat handoff, preserving identity/deadline. No animal is restored, deleted because a report fails, or given unlimited holding. Existing genuine transport mortality remains possible. All data stays on the player's PC/browser. Freshwater data/biology stays unchanged and its interaction lock remains enforced.

## Species and locations tested

The test matrix is generated from the actual diving registry and `eligible(region, mode, true)` result; it is not an eight-species allowlist. Current coverage:

| Species / stable ID | Host | Valid tested destination/mode |
|---|---|---|
| Chalk Bass — `chalk-bass` | Fish | Caribbean Reef |
| Candy Basslet — `candy-basslet` | Fish | Caribbean Deep Sea |
| Cactus Coral — `pavona-cactus` | Coral | Fiji Reef |
| Porcelain Anemone Crab — `porcelain-anemone-crab` | Invertebrate | Japan Reef |
| Blotched Anthias — `blotched-anthias` | Fish | Japan Deep Sea |
| Spotted Boxfish — `spotted-boxfish` | Fish | Japan Reef |
| Yellow longnose butterflyfish — `forcipiger-flavissimus` | Fish | Fiji Reef and Deep Sea |
| Exquisite fairy wrasse — `exquisite-fairy-wrasse` | Fish | Fiji Reef |

That is eight biological definitions across nine valid species/region/mode combinations. Hawaii remains observation-only/blocked; no current verified coral/invertebrate Deep Sea profile exists, so none was invented. Tests include nominal 20/80/661-gallon destinations plus retained incompatible freshwater; valid species-specific quarantine; unsafe chemistry/equipment/cycling/habitat/stocking; all modeled arrival conditions; removed/reselected mounts; rock-only support; finite expiry and correctly categorized mortality; pending/received save round trips, old snapshot compatibility, receipt replay and no duplicate ownership. Synthetic temporary test definitions verify that new fish/coral/invertebrate definitions automatically enter the shared service and use their own 600-L minimum; these QA-only definitions are never registered or shipped as real species. Malformed future transport metadata is reported and blocked rather than creating NaN deadlines.

## Files changed

- `js/diving-receiving.js`: universal identity resolution, host-specific diagnostic adapters, shared destination/mount discovery, registry audit.
- `js/diving.js`: one receiving authority for every host, validated profiles, common post-return handoff, correct health carrier flags and unknown/duplicate transfer guards.
- `js/diving-mystery.js`: saved pending/receiving/release/expiry/receipt handling generalized to every host; old captured snapshot compatibility.
- `js/diving-ui.js`: shared all-tank checks and selectors before capture/after return, explicit coral mount control, all-host individual value and live refresh.
- `js/store-rules.js`: narrowly scoped receiving support for valid coral-only quarantine; all biological checks retained.
- `js/mortality-journal.js`: transport identity/category resolution for fish/coral/invertebrates through the same permanent logger.
- `tests/global_receiving_checks.js`, `tests/global_receiving_qa.py`, `tests/verify_global_receiving_release.py`, `tests/browser_qa.py`, `tests/pages_qa.py`, `tests/diving_checks.js`, `tests/diving_resale_checks.js`, `tests/package.py`, `build.py`; evidence/backups/scripts under `tests/global-receiving-evidence/` and `planning/global-receiving/`.
- This report, primary master §5.5, complete printable continuity, current gameplay/status/UI/save documentation links, and regenerated DIST/Pages/source ZIPs. Approved species data, art and genetics implementation are unchanged.

## Execution results

Final executed source suites:

| Suite | Passed | Failed |
|---|---:|---:|
| Universal registered-host matrix + real UI/save regression — Chrome | 167 | 0 |
| Universal registered-host matrix + real UI/save regression — Edge | 167 | 0 |
| Mystery diving concealment/survival/receipts — Chrome | 61 | 0 |
| Existing all-owned receiving diagnostics — Edge | 44 | 0 |
| Source total | 439 | 0 |

Each universal run includes 91 model cases, actual receiving controls for every valid species/region/mode combination, explicit coral mount/no-auto-mount checks, pre-capture all-aquarium visibility, pending coral browser reload, and the retained diving regression checks. UI layouts were checked at 1920×1080, 1600×900, 1366×768 and 390×844. Screenshots were visually inspected. There were no uncaught JavaScript exceptions or external gameplay requests in those runs. The reproduced noninfectious-carrier failure was fixed and its exact outcome now passes; legitimate health validation stays enabled.

Final built-DIST checks run in both browsers at a GitHub Pages-style HTTP repository subpath. They include the registry-driven universal model, explicit universal-runtime presence, all prior diving/resale/mystery/receiving/expansion cases and actual local account/save/export isolation. Per-check results and exact final counts are in `tests/pages-evidence/chrome-results.json` and `edge-results.json`; the release verifier requires current universal-runtime coverage and zero failures in both. Final combined source/deployment totals, source/DIST/archive SHA-256/CRC proof, preserved original assets/genetics/freshwater gates and complete master continuity are recorded in `tests/global-receiving-evidence/release-validation.json`.

DIST and AquariumLife-GitHub-Pages.zip are rebuilt after final runtime/docs changes; AquariumLife-v0.1.zip contains current source/docs/tests without profiles/caches. The final build manifest is authoritative for timestamp, file count and hashes. All work/testing used isolated QA profiles and never edited a player's actual saved aquarium. No unrun historical suite is counted in this release.


## Remaining restrictions

Safety and eligibility are not waived: incompatible water, insufficient volume/cycling/equipment, unsafe tankmates, restricted medications, missing food/habitat and unsupported/occupied coral mounts still block receiving. Guaranteed encounters do not guarantee capture, survival or profit. Genetic data is preserved where the existing host model actually has it; unknown wild-coral/invertebrate genotypes are not invented. New content must register a complete biological and diving profile, plus coral support geometry where applicable; incomplete profiles are explicitly blocked and audited. Existing completed legacy reports are retained, not retroactively converted into new animals. No public deployment was performed.
