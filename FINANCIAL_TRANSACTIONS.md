# Aquarium Life — financial ledger v1

## UI polish and store quantities — 2026-10-22

Playable v4.3.1 / master v4.15. The familiar aquarium layout now uses a very subtle static downward fish-scale background, opaque slate-blue panels and consistent controls. The existing guarded store supports quantities for equipment, food, consumables, ordinary medicines, rated parts and rocks. Multiple rocks enter Inventory for separate placement; sensitive livestock, unique tools and installations retain their established individual safeguards. One total charge, distinct physical IDs, capacity/stock checks, persistent receipt replay protection and local saving remain authoritative. Main schema2/tutorial2, biological simulation, economy rates, offline time and freshwater lock are unchanged. STORE_QUANTITY_RULES.md defines category behavior; UI_POLISH_QUANTITY_REPORT.md records files, actual tests and limitations. Earlier release sections below are historical where superseded.

## Equipment filters, inspector research and The Dock Casino - v3.7 current

Implemented the equipment-category dropdown and original fragging-tool previews, moved paid species research to living owned-fish inspectors, and added the authorized seventh sidebar entry The Dock Casino with playable Gold Fish and Predator & Prey. All wagers and returns use the existing account wallet/ledger and saved round authority; all research remains 5 AC once per canonical species. The aquarium header controls share the information-column grid and align to its actual panel edge. See STORE_CASINO_UPDATE_REPORT.md and CASINO_RULES.md for the release, verified probabilities, local persistence and limitations. Existing biological simulation, 20-minute day, rewards, freshwater lock, livestock/art approvals and local saves remain. Earlier release sections are historical where superseded.

## Daily livestock survival reward v3.4 - current rule, 2026-10-15

Players earn **100 AC** for every completed qualifying in-game day without a livestock death. The player must own eligible living marine livestock throughout the full simulated day. This is one account-wide payment, not one per aquarium. The separate healthy-aquarium award remains **50 AC**; both independently qualified awards total **150 AC**.

A confirmed fish, coral or bottom-invertebrate death cancels the current qualifying day and starts 1,440 game minutes of recovery. Another confirmed death restarts recovery. Recovery time cannot count toward a qualifying reward day. Illness or living coral bleaching is not a death. The authoritative game calendar remains 20 real minutes per day; legitimate offline catch-up processes the same conditions. Game windows do not stop simulation. Casino requirements apply only if that game is implemented.

Existing balances and actual historical ledger receipts remain unchanged. Every future survival payment is 100 AC through the existing financial service, with canonical account/transaction IDs, actual payment time and completed qualifying day/status. Local save, financial sequence and offline timeline guards prevent re-awarding a settled day. See [V34_UPDATE_REPORT.md](V34_UPDATE_REPORT.md) and [FINANCIAL_TRANSACTIONS.md](FINANCIAL_TRANSACTIONS.md).

## Earlier milestone material - superseded where inconsistent

Current implementation: playable v3.3, 2026-10-14. The existing AC header button opens Financial Overview; no additional main window is added.

## Authoritative wallet

AL.Finance.change is the sole wallet writer in the main game. Core transactions clone the state, check destination/access/stock/price, record the actual change, apply ownership, validate the ledger, then commit. A rejected transaction leaves the original state unchanged. Old standalone artwork review pages retain their pre-ledger fallback; that path is inactive in the main game and DIST entry point.

The service covers livestock, eggs and mystery livestock, food/supplies, equipment/service, tanks, rocks/sand/racks/decorations, medicine/examinations/treatments, water changes, energy, sales, actual quest rewards, +50 healthy-day rewards, +100 survival rewards, expedition rentals and 5-AC research. Existing achievement labels have no invented cash payout. There is no implemented casino; casino receipts are not fabricated.

New profiles begin at the explicitly requested 5,000 AC. Existing wallets become the opening balance unchanged. Migration creates no income, expense or reward for unavailable historical activity. Legacy stats remain intact. There is no server, login, cloud wallet or shared account; the stable local world/account ID scopes the ledger and research.

## Persisted schema

The additive finance object contains version, accountId, opening, started game time, next receipt sequence, rows, archives, durable idempotency keys, income, expenses and an unavailable-history notice. Each receipt stores account/transaction IDs, direction, signed integer amount, category, actual game time/day, PC timestamp, before/resulting balances, action identity and available name/species/specimen/tank/dealer/source/destination/note fields. Successful mystery purchases resolve the created animal identity into the receipt. Sale details additionally retain origin, parent/clone IDs and the calculated dealer reference when applicable. Missing legacy metadata is explicitly unavailable.

opening + income − expenses = closing = actual wallet. Day/seven-day/thirty-day/all-time summaries use recorded transactions, never asset valuation. Category/search/direction filters affect the receipt list, not the all-category period summary. Entries show newest first, twenty per page. Charts use the most recent fourteen recorded days in the selected period and include actual archived totals.

At more than 2,000 detailed rows, the oldest 1,000 become actual per-day/category aggregates, retaining receipt count, sequence bounds, opening/closing and income/expenses. Individual archived details are unavailable and labeled as such. Duplicate keys survive this compaction. Validation checks sequence, account, timing, balances and aggregate reconciliation. Large-history tests process 2,100+ actual changes.

## Persistence and replay

Main save and recovery backup use device-local browser localStorage. JSON download/import remains player controlled. A local account sequence high-water record rejects financial imports older than a newer saved receipt. Existing offline timeline and expedition settlement receipts still prevent replay of simulated days and trips. Research is permanently keyed by canonical species ID. Ordinary UI double clicks use action tokens; the ledger also rejects duplicate durable receipt keys.

This is an offline game, not a cryptographic anti-cheat service. Explicit recovery backups and manual edits/browser-storage deletion are outside tamper-proof guarantees. Browser profiles/origins isolate saves; moving a deployment URL or clearing site data requires the player's exported backup. No save files or browser profiles enter DIST or either release archive.

Implementation: js/finance.js, js/core.js, js/save.js, js/offline.js, existing income/spending modules and js/update31-ui.js. See V33_UPDATE_REPORT.md for current evidence and remaining limits.

## Survival payment metadata and recovery v3.4

Each new survival receipt has action survivalReward, name Livestock Survival Bonus, amount +100, category daily, qualification qualified, qualifyingDay (zero-based completed day), periodStart/periodEnd in game minutes, actual payment time/day, PC timestamp, account ID, unique account sequence ID, resulting balance and durable survival:DAY key. The dashboard displays qualification day/status separately from actual payment time. Historical amounts remain actual facts. Healthy rewards retain their own healthy:DAY key and +50 amount.

Survival policyVersion 2 preserves lastCompleted, lastPaid, lastDeath, recoveryUntil, lost, tracked, stocked (eligible minutes) and earned. Migrating an older partial counter excludes recovery overlap without altering wallet/history. Recovery cannot be bypassed through tank selection, transfers or reload. Offline summary reports actual survival AC and completed days without payments, with no individual offline reward toasts. Clock checkpoints are monotonic through save/background transitions. Local import high-water guards complement idempotent receipt keys; browser-local data is not cryptographic anti-cheat.

## October20 one-time rewards, parts, bundles and pair purchases

The5,000-AC new-profile opening remains; the starter size award is a separate 250-AC achievement receipt. Subject-specific achievement keys, pair-purchase:<offer ID> and whole-aquarium:<tank ID> keys retain actual payments once. New catalog part purchases/replacements use Equipment receipts; owned spare consumption has no second payment. Shell asset appreciation to25,000 is not an AC transaction or retrocharge. Unresolved old casino draws explicitly adopt rules2; old settled receipts are untouched. See ECONOMY_UPDATE_SAVE_SCHEMA.md.

## Quantity receipts — v4.3.1

The existing Finance.begin context attaches quantity, unitPrice and totalCost for supported products. Equipment and rock receipts also record newly created itemIds. Existing receipt category, action, tank, sequence, before/after wallet and time remain unchanged. Core.act checks the existing permanent finance.keys as well as recent transaction tokens before replaying a settled action. Each bulk action performs one Finance.change; failure discards its entire cloned draft. There is no nested per-unit financial transaction. Older receipts do not require new fields. Existing financial rollback protection remains. See STORE_QUANTITY_RULES.md.
