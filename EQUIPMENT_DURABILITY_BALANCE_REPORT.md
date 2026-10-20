# Equipment durability and long-term reliability — 2026-10-19

## October20 authorized service revision

The multi-year wear/major hazard, clock, maintenance intervals and migration preservation remain. Maintenance and Replace Part now differ explicitly. Seven new catalogued serviceable part families cost their exact rated Store new-part prices and renew only themselves to100%; unlisted sealed assemblies/zero-condition chassis require whole-unit replacement. This supersedes the earlier generic discounted repair,80%renewal and25%legacy-zero restoration below. Output also accounts for worn supported parts. Current64-unit/type histories therefore end at major failure OR an unserviceable component fault, not an invented repair of sealed gear. All704 histories,22,528 fixed-seed major-life samples and8/12/24h live/offline parity are rerun in the current reliability suite; actual results are in ECONOMY_UPDATE_REPORT.md and current evidence. Earlier numerical major-risk distribution remains distinct from whole-unit replacement lifetime under the new serviceability policy.

Marine equipment now has independent physical condition, maintenance and persistent probabilistic failure state. The authoritative day remains 20 real minutes, with full chronological offline progression. No products, livestock, remote saving, price tiers, rewards or freshwater biology were added.

## Confirmed original cause

The original `Sim.water` loop applied `durability -= gameHours * 0.018 * (1 + tankVolume / ratedCapacity * 0.15)` once per simulation step. At rated capacity equal to volume, the loss was 0.0207 percentage points per game hour: 100% to zero in **201.288 game days = 0.5515 game years = 67.096 real hours = 2.796 real days**. Every type used that rate. Auto lights also wore during their scheduled dark hours unless switched Off. Old Service restored the entire device to 100%, conflating dirt with chassis age.

Inspection of live stepping, Save restoration and Offline catch-up found one marine wear writer, correctly scaled game hours, and the same five-game-minute step. It did not reveal a repeated offline deduction or a seconds-versus-days conversion bug. The confirmed problem was an excessively fast universal wear rate plus conflated service/condition, not evidence of duplicate application. Original code is retained in `planning/equipment-reliability/simulation-before.js`.

At 8 / 12 / 24 real hours, the old rated device lost 11.9232 / 17.8848 / 35.7696 points respectively. Existing devices retain their exact current condition; no unverifiable historical wear refund, deletion or blanket restoration is applied.

## Service-life distribution and actual player time

The table reports new, clean, quality-1 devices under normal conditions. LED years assume the existing 10-hour daily schedule; continuous manual illumination ages a fixture 2.4 times as fast. One year = 365 game days = 121.667 real hours = 5.069 real days. All real equivalents assume the established clock and continuous progression.

| Equipment | Target / sampled mean game years | p10 / median / p90 game years | Sampled mean real elapsed time | Maintenance game days / real hours | Neglected median first fault, game years |
|---|---:|---:|---:|---:|---:|
| Heater | 5 / 5.057 | 2.666 / 5.016 / 7.414 | 25.64 days | 365 days / 121.7 h | 3.028 |
| Circulation pump | 6 / 6.068 | 3.199 / 6.019 / 8.897 | 30.76 days | 180 days / 60.0 h | 2.366 |
| Filter | 7.5 / 7.586 | 3.999 / 7.523 / 11.121 | 38.45 days | 180 days / 60.0 h | 2.651 |
| Protein skimmer | 7.5 / 7.586 | 3.999 / 7.523 / 11.121 | 38.45 days | 90 days / 30.0 h | 1.920 |
| Aquarium LED light | 7.5 / 7.586 | 3.999 / 7.523 / 11.121 | 38.45 days | 365 days / 121.7 h | 3.751 |
| Reef LED light | 7.5 / 7.586 | 3.999 / 7.523 / 11.121 | 38.45 days | 365 days / 121.7 h | 3.751 |
| Chiller | 7.5 / 7.586 | 3.999 / 7.523 / 11.121 | 38.45 days | 180 days / 60.0 h | 2.651 |
| Automatic feeder | 4.5 / 4.551 | 2.399 / 4.514 / 6.673 | 23.07 days | 120 days / 40.0 h | 1.675 |
| Air pump | 4.5 / 4.551 | 2.399 / 4.514 / 6.673 | 23.07 days | 180 days / 60.0 h | 2.045 |
| Dosing pump | 6 / 6.068 | 3.199 / 6.019 / 8.897 | 30.76 days | 180 days / 60.0 h | 2.366 |
| Containment system | 10 / 10.114 | 5.332 / 10.031 / 14.829 | 51.27 days | 365 days / 121.7 h | 4.344 |

These are game balance expectations, not manufacturer claims, warranties or exact failure dates. The proposed 3–7/4–8/5–10-year ranges inform distribution centers; individuals can fail outside them. Normal replacement averages amount to roughly 23–51 real days with this accelerated clock, not several real years. Early temporary or repairable malfunctions can occur before replacement. The containment and dosing profiles cover existing game equipment, not new store products.

## Formulas and state

`Y=8760` game hours; configured mean life `L`; existing quality `q` defaults to 1 and clamps to [0.5,1.5]. No current catalog SKU has a numeric quality variant. A larger heater level, higher capacity or higher price is not implicitly higher quality. If an existing item supplies quality, the actual scale `eta=L*Y*q/Gamma(4/3)` increases with it; Gamma(4/3)=0.892979511569249.

Only installed, enabled, working equipment accrues powered wear. Actual lamp schedule overlap is integrated analytically. Lamp on-hours divide by 10/24 for normalized exposure; other equipment uses powered hours. Disabled, failed and stored gear does not gain powered age. Installed tracked age continues while off. Transfers retain both age counters and all thresholds.

Maintenance after normalized powered hours `m` is `M=100*exp(log(0.7)*m/I)`, with `I=24*maintenanceIntervalDays`. It reaches 70% at the advertised interval, producing a recommendation; at 30% it produces an urgent warning. Neither threshold destroys the device. Ordinary overnight absences do not require repetitive cleaning every few real minutes.

Neglect uses the exact integral of squared dirt burden below 70%. Let `k=-log(0.7)/I`, `x=max(0,m-I)`, `F(m)=x-2*(1-exp(-k*x))/k+(1-exp(-2*k*x))/(2*k)`. Environmental burden `b=clamp(organic/100,0,1)+clamp(max(0,temperature-32)/20,0,1)` and baseline damage `d=1+2*(1-baselineCondition/100)^2`. An operating interval `h` adds effective exposure `E=d*(h*(1+b)+6*(F(m+h)-F(m)))`. Cleaning removes future dirt burden; it cannot undo accrued exposure.

Physical condition multiplies by `exp(log(0.8)*E/(L*Y*q))`; a new clean unit has 80% condition at its configured mean life. Component conditions use that same exponent times individual wear coefficients. Major failure is stochastic, rather than a condition-to-zero expiration. A tiny positive numerical floor prevents underflow; failed gear still supplies zero output.

The major cumulative hazard is `(effectiveHours/eta)^3` (Weibull shape 3). One saved exponential threshold `-log(U)` defines the unit's latent failure; reload, rendering and maintenance never reroll it. A separate component hazard `x/4+0.08*x*x`, with `x=effectiveHours/eta`, is measured from its last repaired/cleared component cursor. Threshold crossing is inverted and the crossing timestamp solved, including lamp dark periods. A component fault is 60% temporary malfunction, 40% repair required. A major fault is beyond repair. The affected modeled component is selected uniformly within the equipment's component family; component percentages track differing physical wear, while fault timing uses the shared exposure hazard. This is not an individual-component engineering reliability prediction.

Private seeded randomness hashes the existing account/world and physical item ID, then mixes a saved draw counter using 32-bit integer avalanche operations. It never consumes biology, breeding or store RNG. Failure events are emitted once; saved `lastEnd` prevents interval overlap from deducting wear twice. The production simulator still advances chronological five-minute steps. Warnings and failures retain their actual observed simulation timestamps and the installed tank identity.

## Output, maintenance and repair

Working non-light output factor is `min(1,physicalCondition/80)`; LED output degrades gradually as `sqrt(physicalCondition/100)`. Both multiply by `0.6+0.4*min(1,M/70)`. Thus normal early chassis wear does not immediately weaken a correctly sized heater, dirty pumps lose useful output before stopping, and a normal aging LED does not become an instant blackout. Disabled, temporary-malfunction, repair-required and beyond-repair devices supply zero life support.

Filter capacity, circulation, skimming, aeration, lighting/photosynthesis and heater/chiller wattage use the shared operating/efficiency path; feeders, dosing and containment use shared functioning-device checks. Temperature still follows capacity, thermostat and ambient exchange. No forced temperature or livestock immunity is introduced. Mortality snapshots retain the actual equipment state. Daily energy tariff/rates, existing asset valuation, store prices and all AC reward rules remain unchanged.

Maintain restores maintenance to 100%, not physical condition, age or component wear. It can clear an identified temporary malfunction. It preserves established biological bacteria/media. Repair replaces the identified repairable component to 80% and preserves chassis age/condition and identity. An explicitly paid repair of a migrated old zero-condition device restores only 25% chassis condition; loading alone never does so. Beyond-repair devices must be removed and physically replaced; they remain owned inventory, never automatically deleted.

Fees reuse the existing `ceil(deficit/100 * catalogPrice * 0.3 * max(1,ratedCapacity/catalogCapacity))` coefficient. Maintenance uses maintenance deficit; repair uses failed-component deficit with a 25% minimum. No new tariff, product, arbitrary quality markup, refund or award was introduced. This change deliberately removes the old all-condition-to-100 Service behavior.

## Executed quantitative and regression tests

Source Chrome and Edge each passed **787 checks, zero failed**, including 2,048 fixed seeds (4001–6048) per each of 11 profiles: 22,528 paired replacement-life samples. The same seed set deliberately pairs classes for comparative scaling. Those distributions are computed from the actual saved hazard thresholds and `eta`, not a single survival anecdote. Quality-1.3 paired samples use the actual `eta` API and are 30% longer.

For each type, 64 physical units were additionally advanced in actual one-game-day increments, maintained at their profile interval and explicitly serviced/repaired when faults occurred, until a logged major failure: **704 complete multi-year histories**, each matching its own analytical exposure life within 0.01 game years. These 64-unit calendar means differ from the 2,048-unit means because the seed subsets differ; their paired predicted means are recorded in evidence. Actual temporary and repairable faults occurred. The remaining 1,984 units/type were advanced to their first neglected fault using the actual integrator (21,824 failure traces); every profile's neglected median was earlier than maintained first-fault median. Neglected results describe first malfunction, not total replacement life.

At 8 / 12 / 24 real hours (24 / 36 / 72 game days), full actual live stepping and `Offline.sync` matched equipment, water, health and history exactly. A second sync at the same checkpoint added no wear or events. Provisioned fixture fish survived. Heater condition after those intervals was 99.707 / 99.561 / 99.123%; filter 99.805 / 99.707 / 99.415%. These are particular fixed-seed test cases, not a guarantee against all future faults or depleted food.

Additional executed source suites: heater 108/108; physical inventory 70/70; preparation/receiving 207/207; autonomous breeding 86/86. The preparation fixture now tests the 79% reduced-output condition instead of obsolete 99%, because healthy non-light gear retains full output until 80%. Real UI checks covered service/repair transactions, local save round trips, tracked history, individual thermostats, removed-panel absence and no horizontal overflow at 1920×1080, 1600×900, 1366×768 and 390×844. Render counts of 30/120 cannot age gear or draw failures. Evidence and final deployment verification are in `tests/equipment-reliability-evidence`; release-stage results are recorded separately there.

The rebuilt DIST also passed **787/787 reliability checks in Chrome**. Edge passed **5,162/5,162 Pages/DIST/local-save checks**, including repository-subpath startup, direct-file offline startup and no external save uploads. All **2,369 protected asset/data files** compared against the prior Inventory release are unchanged. The complete exact 31-section master is retained once in continuity. An initial parallel cold DIST launch exceeded the generic 10-second browser-test timeout; the reliability harness now allows up to 60 seconds for the existing large embedded art banks, while still requiring full initialization and zero uncaught errors. The complete rerun passed. This changes test loading tolerance, not game simulation.

Reproduce: `python tests/browser_qa.py chrome --equipment-reliability` (or edge); add `--dist` for the deployment files. Other regression flags: `--heater`, `--inventory`, `--preparation`, `--breeding`, `--pages`. No player's active save or normal browser profile is used. DIST and the Pages ZIP are rebuilt with source hashes and ZIP CRC checks; the portable source archive uses `python tests/package.py`. Final integrity uses `python tests/verify_sprite_production_release.py --source-archive --check-only`, without claiming completion of unrelated missing art.

## Migration and remaining limits

Migration is additive and idempotent. Installed/stored IDs, condition, locations, capacities, models, modifications, existing records, switch and thermostat persist. Old unknown service age is explicitly labeled unknown; future age starts tracking now. Previously unmodeled maintenance starts at neutral 100% without restoring physical damage. Saved reliability objects are never reset on reload; invalid versions/thresholds/history reject instead of silently rerolling. See EQUIPMENT_RELIABILITY_SAVE_SCHEMA.md.

The game has no separately modeled mains supply, individual electrical relay duty, manufacturer life data, replaceable bulb/media SKU or calendar aging in unpowered storage. Heater/chiller service age counts enabled control-system operation, not measured element energization; observed start counters are diagnostic, not a physical relay-wear model. Filter servicing abstracts accessible mechanical/media cleaning while preserving biology. Hazard factors are game calibrations. Existing generic asset valuation remains physical-condition-based. Legacy real age cannot be reconstructed and old failures cannot be individually diagnosed without historical evidence. These limits are disclosed rather than presented as measured hardware realism. The full continuity Markdown is current; previously pending binary PDF regeneration and unrelated missing livestock artwork remain separate tasks.

## Changed files

Runtime: `index.html`; new `js/equipment-reliability.js`, `js/equipment-maintenance-ui.js`; integrated `js/equipment-inventory.js`, `js/core.js`, `js/save.js`, `js/simulation.js`, `js/thermal.js`, `js/mortality.js`, `js/mortality-journal.js`, `js/render.js`, `js/overnight-ui.js`, `js/offline.js`, `js/ui.js`, `js/app-shell.js`, `js/inventory-ui.js`.

Tests/release: `tests/equipment_reliability_checks.js`, `tests/equipment_reliability_cohorts.js`, `tests/equipment_reliability_qa.py`, `tests/browser_qa.py`, `tests/inventory_checks.js`, `tests/preparation_checks.js`, `tests/overnight_probe.js`, `tests/package.py`, `build.py`, evidence and rebuilt DIST/Pages/source archives. Design, status, UI, balance, maintenance, save-schema, Inventory and the full 31-section master/continuity documents are updated alongside this report.
