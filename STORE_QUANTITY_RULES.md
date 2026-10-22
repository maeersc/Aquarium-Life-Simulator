# Aquarium Store quantities — playable v4.3.1

The permanent requirement lives in consolidated master section18.1. Quantity preview and transaction enforcement share `AL.StoreRules.policy`, `quantity` and `quote`; all purchases continue through `AL.Core.act`, `AL.Finance` and the existing immediate local save. This is an extension of the existing pipeline.

| Category | Quantity behavior | Delivery / limits |
| --- | --- | --- |
| Equipment, including fixed heaters and Deep Market containment | Whole units1–99 | Separate permanent IDs and reliability state in Equipment → Inventory;50 stored units; existing catalog stock and tank sizing |
| Food | Packs1–99 |20 portions per pack in shared inventory |
| Consumable supplies and mounting packs | Packs1–99 | Existing doses per pack; shared inventory limit10million units |
| Ordinary medicines / diagnostic supplies | Packs1–99 | Existing course/exam doses; merge to1000 units per batch;80 total batches |
| Rated service parts | Units1–99 | Existing SKU@rating stacks,10000 maximum;30 daily stock per SKU |
| Ordinary rocks | Units1–99 | One: existing direct placement. Multiple: separate IDs in ordinary Inventory,100 object limit; place each separately |
| Sand | Single | One existing depth-based substrate installation |
| Decorations, mounted frag racks | Single | Existing placement/mounting and tank limits |
| Reusable fragging tools | Single | Existing one-owned-tool guard |
| Restricted Deep Market medicines | Single | Existing quality-bearing dealer batch, access, hours and listing stock |
| Fish | Existing resident count | Unit price/count/total visible; species compatibility, group size, stock, daily rotation and receiving remain enforced |
| Corals / bottom invertebrates | Individual | Existing assessment, compatibility and coral mounting |
| Eggs, mystery listings, breeding pairs | Existing individual offer | No generic bulk multiplier; preserve rarity, genetics, saved rolls, offspring space and exact offer identity |

Details show Unit Price, Quantity and Total Cost. Bulk categories have labelled minus/input/plus controls. Quantity totals update on input without rebuilding the store. Controls retain keyboard focus. Restrictions appear in the details help text. All destination selection uses existing persistent selectedTank; store open/close, tab changes and completion do not silently change it.

Each supported order uses one full cost debit and receipt. Full quantity, current stock, available storage, destination and wallet are checked again in the cloned transaction. Fractional, zero, negative, nonnumeric and excessive quantities reject. Rejected drafts cannot partially charge, consume stock or create items. UI submission locks and permanent finance receipt keys protect double clicks and save/reload replay, including after the recent100-token ring expires. Existing anti-rollback checks remain.

No schema reset or migration is required. Receipt quantity/unitPrice/totalCost/itemIds are optional additions. All item arrays, stocks, stacks, medicine batches and identities use existing save validators. Livestock are never placed in ordinary inventory or granted a bulk receiving override.

Actual tests, viewport screenshots and performance samples: [UI_POLISH_QUANTITY_REPORT.md](UI_POLISH_QUANTITY_REPORT.md). The original artwork, biological models,20-minute day, AC reward rules and freshwater lock remain intact.
