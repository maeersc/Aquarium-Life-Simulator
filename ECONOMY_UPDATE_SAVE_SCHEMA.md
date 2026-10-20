# October20 economy update — additive schema 2 extensions

Save.version remains2. Migration preserves original tanks, livestock, equipment IDs/location/condition/modifications, genetics, breeding journals, old achievements, wallet and actual receipts. No reset, retrocharge or fabricated historical award is performed. All storage/export/import remains on the player's PC/browser; the build has no save server.

## progression.version 1

Profile-bound records keyed by stable first-species:<host>:<canonical ID>, first-size:<catalog ID>, first-destination:<mode>:<region>. Each record retains id, profileId, kind, key, name, time (actual unlock, or null for legacy-known), awardedAt, status (known-before-update, pending, awarded), xp, ac and transactionId. Known/pending records have no invented payments. Awarded rows require exact category amounts and the persistent achievement:<record ID> financial key. Repeated ownership and every acquisition route converge on this record. objectives stores progress and completedAt per the 13 fixed registry IDs. Capped/best progress survives item removal. Old quest and achievement arrays remain independent.

## equipmentParts.version 1

Data.parts is the sole seven-part catalog. The extension saves inventory quantities by <part SKU>@<exact rated liters>, per-SKU store stock and current restock day. New-part price is ceil(base part price×max(1,rating/equipment base capacity)); it is the same for buying into Inventory or buying during replacement. An owned matching rated part may instead be consumed once. No equipment identity is allocated to a consumable quantity or copied from storage into another tank.

The original reliability.version 1 remains. Replacement changes only the identified part to100%, increments repairs and records part-replacement. A matching fault may clear and restart its component-fault cursor/threshold; major lifetime exposure and unrelated conditions are preserved. Normal maintenance and all old recorded repair events persist. A nonserviceable assembly or zero-condition chassis requires physical replacement. The old repairEquipment action is a compatibility alias to the catalog operation, not an alternate discounted repair price or whole-device restoration.

## aquariumSales.version 1

Receipts retain sold tank ID/name, profile, time, total, actual transaction ID, every itemized row and historical observations/values/equipment/reproductive links. Its durable whole-aquarium:<tank ID> Finance key makes the same tank unsellable twice. Sold tanks are absent from active ownership and selectedTank falls back safely or becomes empty string when tanks is empty. Empty ownership is now a valid saved state; it never creates a placeholder resident tank. Breeding records for a sold tank carry soldTank and require a matching actual sale receipt; active courtship is ended, never left orphaned. Historical IDs are evidence, not owned inventory.

## pairOffers.version 1

Profile-bound offers save id, listing, actual refresh, day, species/variety, deterministic draw, availability/status, two reserved fish identities and individual metadata while available, unitPrice/total, original purchase args, creation time, final transaction and destination. Unpurchased old-day offers may be removed; counter-reserved IDs are never reused. Purchases move the actual fish into active ownership and clear preview fish; receipts retain their IDs, total, time and destination. Global identity validation spans active residents, stored gear and still-reserved offer fish. Persistent pair-purchase:<offer ID> Finance keys prevent replay. Biological admission and authoritative price are checked again at commit.

## casino.version 1 / rulesVersion2

The account extension remains compatible. New rounds use rulesVersion2; pair payouts are2×gross. Settled version 1 rounds validate against their original actual1×pair record and are never paid again. A saved unresolved version 1 round upgrades to2 with originalRulesVersion1 retained, identical draws and the same wager receipt; it settles the corrected return once. Optional dailyLimit/dayWagered and old rounds/totals persist. visits (latest 100) and visitNext track actual opening/closing game timestamps and cumulative wager/payout snapshots; no earlier sessions are fabricated. If storage failure prevents closing-visit persistence, UI dismissal is still allowed and the last saved session is resumable. Existing casino/finance local anti-replay heads remain; no offline client can prevent intentional source/save editing or data clearing.
