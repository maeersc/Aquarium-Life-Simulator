# Coordinated economy, progression, equipment and casino update

October 20, 2026 · playable v4.1 · consolidated master v4.10 · saltwater development

The seven requested changes are implemented through the existing Core, Finance, StoreRules, receiving, valuation, reliability and breeding authorities. Save schema remains 2; the new extensions are additive. The 20-minute game day, chronological offline progression, local PC/browser saves, existing assets/genetics, freshwater lock and existing care rewards remain.

## Audit and implementation

1. **Ocean Sanctuary price.** The original authoritative addition was `js/update29-catalog.js`: base and marine price 5,000 AC. Both are now **25,000 AC**, without a further marine markup. Core affordability/payment, catalog/configuration and Valuation shell base already consume that record. No retrospective charge is created, and the other nine prices are unchanged. Current shell asset appreciation is separate from wallet income. [Pricing definitions](AQUARIUM_PRICING.md).
2. **Achievements and objectives.** New biological ownership pays **50 XP/50 AC** once per canonical species; first catalog size **100 XP/250 AC**; first completed mode/region destination **50 XP/50 AC**. Every legitimate ownership route converges on one profile record after Core/simulation; temporary catches and unhatched eggs do not count. Old known ownership/history backfills without retroactive payments or invented dates. A new marine starter size qualifies: 5,000 opening AC plus a separately receipted 250-AC award and 100 XP. Thirteen additional objectives show saved progress, with **no unspecified extra cash/XP rewards**. [Registry and migration](ACHIEVEMENT_OBJECTIVES.md).
3. **Maintenance and Replace Part.** The previous catalog had no spare-part prices. Seven explicit rated external-part entries now supply the exact Store and replacement price; owned matching spares may be consumed instead. Replacement renews only the selected supported component to 100%, preserves chassis age/condition/identity/unrelated wear, and records the event. Cleaning retains its original fee coefficient and does not renew hardware or erase filter bacteria. Sealed/unlisted assemblies and zero-condition chassis require complete-unit replacement; the old generic discounted repair/25% zero-chassis restoration is superseded. Multi-year wear/hazards and maintenance intervals remain. [Parts and exact prices](EQUIPMENT_PART_CATALOG.md), [care instructions](EQUIPMENT_MAINTENANCE.md).
4. **Sell Entire Aquarium.** Store → Sell lists owned aquariums and opens an itemized offer with all blockers, exact payout, irreversible warning and separate required confirmation. One validated transaction transfers the shell, installed gear and eligible physical contents, pays once, retains historical records and excludes stored Inventory/parts and other tanks. The shell buyback is newly defined at 50% of current shell value using the existing physical half-value convention; other physical components use their existing valuation/rock quote. Each resident uses the requested ordinary 60%-of-Deep-reference quote, with cumulative dealer budget/count and biological restrictions enforced. Eggs/nurseries lacking an approved resale route block the bundle. Selling the last tank saves a real empty ownership state, with working Inventory/history/settings/Casino and aquarium creation. [Sale policy and restrictions](WHOLE_AQUARIUM_SALES.md).
5. **Gold Fish pairs.** A pair now pays **2× gross**, including stake. A 100-AC wager is debited once, returns 200 AC and shows +100 net. Symbol matching/weights, 25× Gold triple, 3× other triple, losses and every Predator & Prey outcome remain unchanged. Completed rules-v1 records retain their actual old payouts; unresolved old rounds explicitly upgrade to v2 using the same draws/stake, with no reroll or second debit. [Versioned casino rules](CASINO_RULES.md).
6. **Casino Profile.** Profile now owns the sole Optional Spending Limit editor, remaining allowance, Recent Casino Visits and retained round history. The original enforcement remains central across both games. New visits save actual session timestamps and wager/return summaries; earlier sessions are not fabricated. A failure to save an optional closing timestamp cannot trap the player in the dialog. Old limits/rounds are preserved.
7. **Breeding-pair Store offers.** Each eligible listing has configured **5%** availability, cached by profile and legitimate listing refresh. A saved offer has two distinct reserved IDs, individual mature ages, health, genes, appropriate roles and the sum of two legitimate standard-adult retail/dealer prices, without a discount. Reopen/reload does not reroll. Two-fish compatibility plus sequential shared receiving/medical checks include combined adult load, water, habitat, quarantine, stock and level. Confirming transfers those same individuals, charges once, clears preview copies and records a durable receipt. Offers say Compatible Breeding Pair; no established bond or immediate spawn is invented. Existing autonomous breeding is preserved. [Offer rules and coverage](BREEDING_PAIR_OFFERS.md).

The instruction applying ordinary resale at 60% of the Deep reference expressly supersedes the prior diving-only-discount wording. The shared quote and individual fish/invertebrate labels were corrected together so a whole bundle and separate resident sales do not disagree. Existing actual sale receipts are unchanged; retail prices and generic current asset values are not discounted by this change.

## Balance and biological boundaries

Gold Fish has exactly 1 Gold triple, 99 ordinary triples, 600 pairs and 300 losses among 1,000 ordered bucket draws. Its authorized new expected gross return is **1.522 AC per AC wagered (152.2%)**, or +52.2% theoretical net. This favors the player. Other payouts were deliberately preserved as requested; no hidden offset was introduced. Predator & Prey remains 100% theoretical return. These are fictional AC only, with no real-money prize or payment.

The current reproductive authority supports 29 actual catalog fish, including supported clownfish taxa, Banggai, Chalk Bass and Sharknose Goby. Every one was exercised with valid saved offers and two distinct mature fish. The full exact ID list is in the offer rules and `pairSpeciesTested` evidence. Unmodeled fish, group-spawning configurations, acquisition holds and unverified designer inheritance do not receive fabricated pairs. This pass adds no new breeding protocol, livestock species or scientific claim. Unknown legacy coral groups are not invented as distinct biological species for money.

Replacement prices are newly documented game catalog entries under the explicit missing-part instruction. They are not real manufacturer prices or assertions that sealed heaters/fixtures can be opened. The original probabilistic major-life distribution remains, but an unserviceable component fault can now require whole-unit replacement earlier. Current 64-unit/type simulations correctly stop at a logged major **or** nonserviceable fault. They do not pretend to repair sealed components to prolong the sample. Maintained sample means remain multi-year: heater 5.118 game years, circulation/dosing 6.419, filter 8.023, skimmer 8.203, lighting/chiller 7.676, feeder/air 4.815, containment 10.235 (64-unit fixed-seed cohorts; not warranties or the same sample mean as 2,048 theoretical major-life draws).

## Executed tests

| Suite | Executed result |
|---|---|
| October 20 source acceptance, Edge | **85 passed, 0 failed**: 51 model checks and 34 real UI checks, including actual zero-tank page reload/Continue and global tutorial controls |
| Existing Store/research/casino safeguards, Chrome | **139 passed, 0 failed** |
| Physical Inventory ownership, Edge | **70 passed, 0 failed** |
| Preparation/shared receiving, Chrome | **207 passed, 0 failed** |
| Autonomous breeding, Edge | **86 passed, 0 failed** |
| Heater/temperature/mortality, Edge | **108 passed, 0 failed** |
| Long-term equipment reliability, Chrome | **787 passed, 0 failed** |

The source acceptance exercised real Store pair purchase, catalog component purchase/replacement, Casino Profile limit editing, actual whole-sale confirmation, last-tank empty state, actual page reload/Continue/new purchase after that sale, and actual expedition completion. That full reload exposed an older `update29-ui.js` startup guard which assumed an aquarium existed; it now handles absent ownership while keeping resident controls disabled and new-aquarium access available. Recovered placed rocks also retain their original condition and quantity when using the shared rock quote. Fixed 100,000 listing keys produced **5,017 offers (5.017%)**, within the stated sampling tolerance around configured 5%; the sample is not claimed to contain exactly 5,000 offers. All 29 supported fish generated valid, saved individuals. Pair loading/reopening retains both IDs and private genetics.

The durability suite ran 2,048 fixed major-risk seeds per each of 11 profiles, 704 actual maintained multi-year histories and 21,824 neglected first-fault traces. Actual 8/12/24-real-hour offline and equivalent live simulation matched equipment, water, health and history; repeated sync did not replay wear or events. Normal provisioned livestock survived. Supported replacement parts do not restore chassis age or bypass life support. The approved 20-minute game day remains unchanged.

Responsive UI checks and screenshots cover **1920×1080, 1600×900, 1366×768 and 390×844**. The original casino suite additionally checks intermediate header layouts, save-failure recovery, committed-round reload, wallet cap, cross-account isolation and replay after history pruning. Some early regression failures were obsolete fixtures: manual wallet resets needed legitimate milestone backfill; direct fixture size changes now earn real first-size awards; old seven-window, blocked-equipment-purchase, 1×pair and “Maintain” label expectations were superseded by approved updates. Those expectations were corrected rather than weakening production validation. Final listed source suites have zero failures.

Final rebuilt-DIST execution, repository-subpath/direct-file local-save acceptance, protected-file comparison and release hash/CRC verification are recorded in **`tests/economy-update-evidence/release-results.json`** and the corresponding actual browser results. They are run after source/documentation freeze; this report does not infer passes for browsers or workflows not executed. Reproduce with:

```
python tests/browser_qa.py edge --economy20
python tests/browser_qa.py chrome --economy20 --dist --with-reliability
python tests/browser_qa.py edge --pages
python build.py
python tests/package.py
python tests/verify_sprite_production_release.py --source-archive --check-only
```

## Required 42-case coverage

| Request cases | Evidence exercised |
|---|---|
|1–3 Tank price, old owners, other prices|Exact catalog, Core purchase debit/size award/shell value; legacy parse no debit; all nine old prices asserted|
|4–5 First species/repeated ownership|Real Core fish/coral ownership, canonical morph identity, repeat purchase and sell/rebuy/reload tests|
|6–7 First size/repeated size|Exact catalog ID award, repeated category no award; shared legacy freshwater category backfill without biology change|
|8–9 Destination/repeated destination|Distinct Indonesia/Philippines, failed Mariana excluded; actual repeated Caribbean launch/return through Core; original-region validation|
|10 Reward persistence|Real receipt IDs/keys, local JSON round trips, post-sale history and pending-cap retry once|
|11–15 Service options, catalog price, ID, wear, longevity|Actual separate inspector controls; purchased/owned rated part; exact debit, unrelated component/chassis/age preserved; 787 durability checks|
|16–18 Sale inclusion/storage/other tanks|Full physical item rows, installed gear IDs, storage quantities and other tank JSON preserved|
|19–22 Confirmation/once-only/load/failure|Actual required checkbox and exact itemized form, atomic Core sale, duplicate sale rejection, saved last-tank state and no mutation on blocked/stale/unconfirmed sale|
|23–25 Pair gross/net/other outcomes|50/100/250/1000-AC exact pair returns; real ledger settlement; exhaustive 1,000 Gold outcomes and preserved Predator/card tests|
|26–29 Profile placement/limit/settlement|Actual Profile form, actual visit tracking, one editor, cross-game daily limit, no duplicate settlement, legacy closed/pending version tests and storage failure recovery|
|30–32 Chance/reopen/biology|Configured .05; fixed100,000-listing sample; actual details reopen/save; all29 supported species and existing profile/inheritance/group holds|
|33–37 IDs/cost/receiving/autonomy/save|Two actual transferred permanent IDs; one expense receipt; combined load where one fish fits and two do not; unsafe-water checks; existing86-check breeding suite; persistent offers/receipts|
|38–42 Preservation/offline/freshwater/economy|Legacy ownership parse, Inventory/receiving/heater suites, exact master/continuity, protected assets/data, Pages/local-save execution, locked freshwater actions, unchanged other prices/biology/rewards plus only documented authorized additions|

## Save migration and remaining limits

[Full additive schema](ECONOMY_UPDATE_SAVE_SCHEMA.md) defines profile award/objective records, exact rated part quantities/stock, itemized whole-sale/history receipts, valid zero-aquarium ownership and persisted pair offers/individuals. Reserved preview fish participate in global identity validation and leave previews after transfer. Whole-sale receipts validate historical sold-tank reproductive links without owning those individuals. Existing finance/casino local heads continue rejecting ordinary stale imports. No active player save or normal browser profile was used by these disposable test suites.

Existing reliable discoveries/sizes/destination histories become known-before-update, not paid-back awards. Earlier unrecorded acquisitions cannot be reconstructed. Wallet/XP caps remain; queued rewards retain their real unlock time and wait for space. Unknown legacy equipment age remains unknown. Biological/group/pattern/breeding protocols unsupported before this update remain unsupported; no fish is promised immediate spawning. Spares cover only the explicitly serviceable catalog. Live eggs/nurseries, animal health/maturation/market budget/daily limits and active receiving plans can legitimately block an entire sale, with reasons before confirmation. Source/JSON editing and clearing local data cannot be made cheat-proof by an offline client.

The complete exact 31-section master and printable/PDF continuity **source** are updated. Binary PDF regeneration and the previously recorded 18 missing unrelated livestock art sheets are separate earlier limitations; this equipment/economy task does not claim those art/PDF jobs complete. No new permission is required to use these authorized seven features. Future additional reproductive protocols, nonserviceable part products or changes to unrelated casino payouts remain outside this pass.

## Files changed

New runtime modules: `js/progression.js`, `js/equipment-parts.js`, `js/aquarium-sale.js`, `js/pair-offers.js`, `js/economy-update-ui.js`.

Integration: `index.html`, `js/update29-catalog.js`, `js/core.js`, `js/save.js`, `js/simulation.js`, `js/store-rules.js`, `js/store.js`, `js/update31.js`, `js/update29.js`, `js/update29-ui.js`, `js/diving.js`, `js/breeding.js`, `js/equipment-reliability.js`, `js/equipment-maintenance-ui.js`, `js/equipment-catalog.js`, `js/inventory-ui.js`, `js/store-art.js`, `js/expansion-ui.js`, `js/ui.js`, `js/render.js`, `js/app-shell.js`, `js/casino-rules.js`, `js/casino.js`, `js/casino-ui.js`. `js/valuation.js` continues to read the authoritative catalog; its consumers were aligned without adding a duplicate price table there.

Tests/release: `tests/economy_update_checks.js`, `tests/economy_update_qa.py`, `tests/browser_qa.py`, reward-aware existing Inventory/diving/overnight/heater/reliability/store-casino/Pages fixtures, `tests/package.py`, `build.py`, new evidence, rebuilt `DIST`, `AquariumLife-GitHub-Pages.zip` and `AquariumLife-v0.1.zip`. Original requirements and pre-edit audit modules are retained under `planning/economy-progression`.

Documentation: this report; pricing, achievements/objectives, part catalog, whole-sale, pair and schema documents; `CASINO_RULES.md`, `EQUIPMENT_MAINTENANCE.md`, reliability/Inventory save and balance notes, `FINANCIAL_TRANSACTIONS.md`, `BREEDING_RULES.md`, `GAME_DESIGN.md`, `UI_SPECIFICATION.md`, `DEVELOPMENT_STATUS.md`, `BALANCE_REPORT.md`, `MASTER_DEVELOPMENT_PROMPT.md` and exact `PROJECT_CONTINUITY_SOURCE.md`.
