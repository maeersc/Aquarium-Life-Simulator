# Aquarium Life — daily livestock survival reward v3.4

Implemented 2026-10-15. Playable v3.4 / consolidated MDP v3.7. The uploaded specification is retained verbatim in planning/v3.4/requirements.md.

## Reward and recovery

New qualifying survival days pay **100 AC**, once per local account. The existing healthy-care reward stays **50 AC**, evaluated independently: either reward alone, or **150 AC** when both qualify. No new survival payment uses the replaced amount. Existing actual historical receipts, earned totals and wallets remain unchanged; migration does not invent, claw back or top up AC.

Eligible stock includes living marine fish, corals and bottom-dwelling invertebrates. A full calendar day must be simulated with eligible livestock throughout, no confirmed livestock death and no previous settlement for that day. Retained freshwater biology is unchanged and freshwater development/purchases remain locked. Multiple aquariums cannot multiply the payment.

Fish, coral and invertebrate death hooks record the authoritative simulation time and cancel the current day. Recovery lasts exactly 1,440 game minutes. A different confirmed death restarts it; repeatedly processing the same corpse does not. Sick living fish and living bleached corals are not death events. Selection, transfer, corpse removal and reload do not clear the account penalty.

Recovery minutes cannot count toward reward qualification. For example, a death at minute 500 holds recovery until 1,940. The partly recovering calendar day does not qualify; a fully stocked/death-free day from 2,880 to 4,320 can earn 100 AC. This fixes the prior overlap bug without introducing another reward timer or wallet.

## Persistence, finance and time

The existing survival save object now has policyVersion 2. Existing tracked/stocked minutes, last completed/paid day, death time, recovery end, loss flag and earned totals remain. Older partial checkpoints exclude recovery overlap during migration. Prior receipts remain actual historical facts.

Each new payment uses AL.Finance.change with the existing durable survival:DAY key and unique account receipt sequence. It records +100, Livestock Survival Bonus, daily category, qualification qualified, completed qualifying day, period boundaries, actual simulation payment time, PC timestamp, account ID and resulting balance. Dashboard details expose qualification separately from payment time. The healthy payment keeps its independent key and +50 amount.

The existing 20-real-minute day remains. Store, Deep Market, Field Journal, Equipment, Ocean Diving, Financial Overview and other game dialogs continue the authoritative simulation. Existing main-screen pause preferences remain available. No casino is implemented; no casino feature or imaginary transactions were added.

Offline catch-up uses the same actual simulation, not a flat offline grant. Its single return summary reports actual survival AC and completed days without payment. Live reward/death notifications are suppressed during catch-up and settled before returning to the normal UI. Tank History updates the recovery countdown while open.

Backward clock changes cannot lower the processed checkpoint through saving or background transitions. Repeated offline timestamps, repeated boundary calls, reloads and older locally saved financial/timeline imports cannot pay the same qualifying day again. A completely offline client cannot authenticate intentional forward clock changes; it simulates those elapsed conditions once and does not re-pay already settled days. Clearing/editing local storage is outside cryptographic anti-cheat guarantees. No cloud, login or separate account service is introduced.

## UI and notifications

Live payment: **Livestock Survival Bonus: +100 AC**.

Confirmed loss: **Livestock lost! Daily survival bonus interrupted. Complete one full in-game day without a death to restore eligibility.**

Tank History displays separate 100/50 rewards, 150 combined, tracking, last confirmed loss, recovery end and remaining minutes. The financial modal remains accessible through the existing AC header button. Existing six-window navigation and selected aquarium behavior are preserved.

## Validation

Chrome and Edge each pass **98 reward/finance checks: 34 new reward model checks, 16 real UI checks and 48 existing finance/fragging/research model checks**. Each also passes **412 preserved gameplay/migration checks, 362 shared livestock/core/health/economy checks and 108 diving checks**, with zero final failures. Final rebuilt-DIST/local-save checks: **251 passed per browser, zero failures**. The selected suites total **1,231 passed per browser / 2,462 executed assertions**, zero final failures. GITHUB_PAGES_BUILD_REPORT.md records the build and deployment details.

The new tests exercise real fixed-step and offline simulation rather than granting a fake reward from interface code. UI checks use actual buttons, dialogs, local reload and continued time through each window. Two initial fixture failures were corrected: the healthy-only scenario now uses the full healthy day after a prior death, and the hand-authored historical save synchronizes its old daily-store checkpoint. No production precondition was weakened for testing.

| Requested check | Result / evidence |
|---|---|
| 1. Full day pays 100 | Passed: one ledger receipt and reconciled wallet |
| 2. Partial day pays nothing | Passed: 1,439 minutes then final minute |
| 3. No eligible livestock | Passed: empty and retained-freshwater-only accounts |
| 4. Multiple aquariums | Passed: one account payment |
| 5. Fish death | Passed: exact time, canceled day |
| 6. Coral death | Passed: global qualification interrupted |
| 7. Bottom-dweller death | Passed: actual invertebrate kill hook |
| 8. Living sickness | Passed: living illness/bleaching not recorded as death |
| 9. One full recovery day | Passed: exact 1,440-minute interval and no partial-overlap payout |
| 10. Additional deaths | Passed: restart interval; same corpse cannot restart it |
| 11. Reward resumes | Passed: first full qualifying calendar day after recovery |
| 12. Offline rewards | Passed: three simulated days yield 300 survival AC |
| 13. Save/load duplication | Passed: validated reload, repeated boundary and timestamp checks |
| 14. Financial dashboard | Passed: actual +100, qualification/day/account/time/IDs |
| 15. Healthy +50 | Passed: healthy-only, survival-only and combined 150 cases |
| 16. Old amount removed | Passed: all newly generated survival receipts are +100; history retained |
| 17. Central ledger | Passed: rewards reconcile with real wallet, no competing wallet |
| 18. Existing accounts/livestock | Passed: old receipt migration, identity/recovery reload and protected regressions |
| 19. Offline function | Passed: no HTTP requests in new reward/UI session |
| 20. Freshwater lock | Passed: transaction gates and retained biology regression |

Evidence: tests/update34-evidence, tests/update29-evidence, tests/expansion-evidence and tests/diving-evidence. Current release checks use the generated DIST at an HTTP repository subpath, real local export/import and separate browser profiles. Firefox, public GitHub deployment, manual screen-reader use and long human play sessions were not run. Existing artwork is untouched; the full artwork gallery suite was not rerun for this reward-only change.

## Files and documentation

Runtime: js/update29.js, js/update29-ui.js, js/update31-ui.js, js/offline.js, js/main.js, js/ui.js and index.html. The existing central wallet service and healthy-care model remain unchanged. Build/package updates: build.py and tests/package.py. New acceptance suite: tests/update34_checks.js and tests/update34_qa.py; browser_qa.py routes it. Existing executable reward expectations in update29/update33 tests use the new amount and full post-recovery day.

Updated maintained rules/design/UI/status/balance/financial documentation, the 31-section master, full continuity source, README, current catalog guidance, PDF workflow and current test/build reports. Earlier reports and original specifications are explicitly historical where they contain superseded reward amounts; actual historical financial/test evidence is not falsified. Source preservation and edited-file evidence live under planning/v3.4.

All saves, recovery data, research and financial history remain local to each player's PC/browser; no profiles or player saves ship in DIST or release ZIPs. Both release archives are rebuilt from final files. Existing research content remains incomplete as already disclosed; no additional species research or artwork was requested here. The printable continuity source is current; binary PDF export/render verification remains pending the previously unavailable toolchain.

Final DIST: 1,511 source files / 455,939,227 bytes, content v3.4; Pages ZIP 425,579,852 bytes. All source/DIST/Pages ZIP hashes and ZIP CRCs are verified. Upload the contents of DIST. All 1,419 asset files and six protected existing data/core/biology/healthy-care/wallet modules remain unchanged; the complete 31-section master and both 38/35-entry ledgers remain in the continuity source.
