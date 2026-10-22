# Marine economy, disease and valuation update — 2026-10-13

Historical milestone report. Current gameplay/time/settings results are in [GAMEPLAY_UPDATE_REPORT.md](GAMEPLAY_UPDATE_REPORT.md); this is not a new full-project audit.

The approved offline update is implemented for the existing marine roster. The consolidated MDP is now **v2.8**, retaining all 31 major sections. The complete game and earlier audit backlog are not declared finished.

Normal retail prices, current individual asset values and eligible dealer resale offers are separate. Normal adult/variety/egg/frag products and eight legitimate medicines have fixed prices. Marine fictional dealer fish/eggs and two fictional Restricted Treatments have saved, bounded price and condition/quality rolls; ordinary reload/open/close cannot reroll them. Dawn rotates listing identities, and stale orders reject. The protected pre-existing freshwater fictional specimen retains its original price/biology path.

Marine health is centralized and host-aware: ich, velvet, Brooklynellosis, flukes, selected bacterial syndrome, malnutrition and injury for fish; distinct bleaching, tissue loss, suspected infectious syndrome, pest damage and environmental stress for corals. Ordinary coral grade is a standard unexamined frag with fixed retail price and a seeded, saved introduction risk. Fish parasites cannot infect coral or future invertebrate hosts. Hidden condition is not automatically named in inspectors; examination reveals confidence-qualified findings, with a delayed follow-up required for selected bacterial care. Diagnosis is separate from treatment.

Owned treatment units start timed courses. Appropriate host/diagnosis, severity, duration, water and persisted batch quality affect recovery. Wrong or contaminated products can fail/harm. Quarantine-only products require an appropriate bare, cycled fish-only environment and cannot follow the animal into a reef during an active course. Corals transfer with valid physical mounts into independently maintained coral quarantine. Fish identity, health state and history persist. Existing fish mortality and coral dead artwork remain the death paths.

Click an individual fish, benthic fish or coral to see **Current Value**, eligible offer and an optional breakdown. Marine value accounts for stage/size, HP, nutrition, disease, condition, age, genetic/designer traits and fertility with bounded modifiers. Living bleaching, tissue and polyps affect coral value. Dead organisms have zero living value. Freshwater individuals keep their previous biology/disease/value formula.

The main **Tank Value** control opens base/current total and categories: physical shell, equipment, fish/viable broods, corals/plants, bottom dwellers, owned rock/substrate/racks and decorations. Each is counted once; attached coral is not included again in rock value. Value is not wallet credits. Calculations are cached per authoritative state/tick and used by periodic UI updates, not every sprite frame. Meaningful marine value history is bounded to 30 entries. Existing transfer stress may reduce arrival value, so value transfer tests account for current condition rather than assuming an unchanged price.

The obsolete modal quantity event conflict was corrected. Marine transfers now check safe water, incompatible clownfish territories/females, predatory destinations and active-course restrictions. The coral transfer UI offers actual permitted destination mounting positions. These changes are necessary to the new quarantine/treatment flow.

## Verification

All tests use isolated Chrome/Edge profiles, `file://` and disabled network access. No private player save was opened or modified.

| Executed suite | Chrome | Edge | Evidence |
|---|---:|---:|---|
| New marine acceptance | 69 passed / 0 failed | 69 passed / 0 failed | [Chrome](tests/economy-evidence/chrome-results.json), [Edge](tests/economy-evidence/edge-results.json) |
| Existing system regression | 68 / 0 | 68 / 0 | [Chrome](tests/chrome-results.json), [Edge](tests/edge-results.json) |
| Current store/UI regression | 90 / 0 | 90 / 0 | [Chrome](tests/chrome-store-results.json), [Edge](tests/edge-store-results.json) |
| Clownfish art, eyes, directions and gallery | 7,583 / 0 | 7,583 / 0 | [Chrome](tests/chrome-clownfish-results.json), [Edge](tests/edge-clownfish-results.json); 1,792 directional cases per browser |

The old night-market assertion for an unconditional 65-HP animal was updated to verify the assigned listing identity and persisted health state; the new requirement explicitly permits multiple condition classes. Store category expectations now allow the authorized additional medicine tabs (8/7/7). Freshwater protection checks strip only the expressly marine hooks before comparing simulation source and also run a ten-day exact biological comparison with the pre-update code. All 144 protected freshwater art/source files and the species definition file are byte-identical.

The user's 20 acceptance requirements map to executed checks as follows:

| # | Requirement | Executed evidence in the new acceptance results |
|---|---|---|
| 1 | Fixed standard retail | Marine retail across seeds/stock/reload and all linked designer prices; actual store quantity event |
| 2 | Designed black-market variation | Saved price creation, condition mapping, dawn-only rotation and stale-listing rejection |
| 3 | No reload condition reroll | Ten repeated parses/view accesses leave the exact serialized state unchanged |
| 4 | Each livestock value | All 52 fish definitions/benthic entries plus coral value/inspector cases |
| 5 | Growth/maturity changes value | Juvenile/adult/elder modifiers and frag/colony size cases |
| 6 | Illness reduces value | Nutrition/disease/condition and tissue/pigment/polyp modifiers |
| 7 | Recovery restores value | Maintained-food diagnosed ich course and corrected bleaching/support case |
| 8 | Dead living value lost | Dead fish and coral return zero living value/offer |
| 9 | No tank double counting | Exact sum of categories, separately counted attached coral and owned supports |
| 10 | Transfer moves value | Quarantine transfer preserves ID/history and source/destination current-value deltas |
| 11 | Symptoms/progression | Marine velvet progression/symptoms and existing mortality count; coral condition response |
| 12 | Correct treatment can work | Timed diagnosed ich, coral pest dip, bleaching support, delayed bacterial eligibility |
| 13 | Incorrect treatment can fail/harm | Wrong fluke course for ich and controlled contaminated fictional course |
| 14 | Reef contraindications | Copper rejects reef/coral/juveniles/occupied hardscape quarantine/unsafe water; active course cannot transfer to reef |
| 15 | Quarantine identity | Fish/coral identity, history, condition and coral attachment survive moves |
| 16 | Fixed ordinary medicines | All eight products match fixed prices/dose counts and have no dealer-quality object |
| 17 | Persistent hidden medicine quality | Exact listing → batch → save quality and assay without reroll |
| 18 | No duplicated charge/dose/save state | Core token replay, active-course rejection, no refund on stop, malformed/duplicate IDs/quality rejection and exact round trips |
| 19 | UI/art preserved | Actual exam/start controls, four responsive widths, 90 store checks and 7,583 sprite/gallery checks |
| 20 | Offline startup | No HTTP(S) requests or uncaught browser exceptions in new acceptance runs |

Clinical/medical tests are game-model acceptance, not real treatment efficacy studies. Seeded 30/90/365-day marine care results are recorded in [BALANCE_REPORT.md](BALANCE_REPORT.md): both fish survive, with ending wallets 2,535 / 2,214 / 568 AC respectively after a 2,640 AC post-purchase starting wallet. One scenario does not prove full-roster balance.

Visual evidence reviewed: [examined fish](tests/economy-evidence/chrome-diagnosis.png), [tank breakdown](tests/economy-evidence/chrome-tank-value.png), [ordinary medicine store](tests/economy-evidence/chrome-medicines-store.png), [restricted treatments](tests/economy-evidence/chrome-restricted-treatments.png), [narrow medical inspector](tests/economy-evidence/chrome-medical-narrow.png), [active course](tests/economy-evidence/chrome-active-course.png). The screenshots retain the existing black/slate styling and local art.

## Persistence and files

New services: [marine health](js/livestock-health.js), [dealer listings](js/livestock-market.js), [valuation](js/valuation.js), [extension validation](js/health-save.js), [medical/value UI](js/health-ui.js). Core actions, simulation marine hooks, local save migration, current store/rules/art previews and existing inspectors connect these services. Existing artwork/asset banks and approved reference are preserved; the coral renderer selects the existing bleached/tissue/dead bank when appropriate.

Schema remains 2 with marine extension version 1. Legacy migrations preserve existing wallet, HP, identities, art assignments and selection. Current invalid/missing medical/market records are protected/rejected rather than silently regenerated. Listing/batch IDs are checked with the entity counter. Hidden quality persists in both acquired batches and active course parameters.

Required design/status/catalog/UI/balance documents were updated along with README and TEST_REPORT. All new requirements are integrated in the existing primary MDP sections; there is no replacement master prompt or extra major section. The October 12 FULL_PROJECT_AUDIT is preserved as a dated historical snapshot with a notice linking this milestone; its original completion counts were not re-audited.

## Research basis and limits

Host/treatment families and diagnostic/contraindication principles use [Merck fish parasites](https://www.merckvetmanual.com/exotic-and-laboratory-animals/aquarium-fish/parasitic-diseases-of-fish), [UF marine ich](https://ask.ifas.ufl.edu/publication/FA164), [UF marine copper](https://ask.ifas.ufl.edu/publication/FA165), [UF monogeneans](https://ask.ifas.ufl.edu/publication/FA033), [Merck bacterial diseases](https://www.merckvetmanual.com/exotic-and-laboratory-animals/aquarium-fish/bacterial-diseases-of-fish), [NOAA living bleaching](https://oceanservice.noaa.gov/facts/coral_bleach.html) and [NOAA coral disease uncertainty](https://floridakeys.noaa.gov/coral-disease/disease.html). Numerical durations/rates/confidences and introduction probabilities are documented accelerated game calibrations, not clinical doses or measured disease prevalence. No real adulteration/toxic-mixture recipe was generated.

Still incomplete/deferred: exact taxon-specific coral/rare-fish clinical profiles, expanded laboratory/isolate testing and medicine resistance modeling, actual invertebrate livestock and medical profiles, full decomposition, completely dry construction, substrate biology, categorical designer pattern inheritance and remaining unrelated audit findings. Fish disease symptoms are communicated through the inspector; new disease-specific fish atlases were not produced. No private-save collection, Firefox, multi-hour memory soak or clinical validation was performed.

The verified aquarium-value leaderboard remains an end-stage documented objective requiring server-authoritative ownership/transactions/valuation. Browser-local values are not trusted online scores. **No networking, account, backend, cloud save or functioning online leaderboard was built.**

Open [index.html](index.html) to play, or extract the rebuilt AquariumLife-v0.1.zip. This report describes the authorized marine milestone, not completion of the entire project.
