# Interactive tutorial save extension

The main save schema remains **2**. `update29.version` remains **1** for its unchanged survival/mystery systems. Only `update29.tutorial` upgrades to **version 2**.

| Field | Meaning |
|---|---|
|`version`, `profileId`|Tutorial format 2 and existing account identity|
|`status`|`active`, `paused`, `skipped` or genuinely `completed`|
|`current`|Stable task ID from the 22-entry registry|
|`step`|Zero-based phase 0–11 for legacy numeric compatibility; must match the current task|
|`startedAt`, `completedAt`|Game times or null; completion time exists only after verified completion|
|`tankId`, `fishId`|Pinned aquarium and current owned tutorial fish identity, or null|
|`species`, `productId`|Existing catalog species and actual selected listing; never a new specimen or duplicate offer|
|`completed`|Task-ID map with `id`, `tankId`, verification `time`, bounded `evidence` and `source`|
|`signals`|Validated interface observations; real manual food/meal evidence; supported prior ownership/feeding observations|
|`previousTanks`|Up to eight prior aquarium references, end time and completed task IDs|
|`audit`, `nextAudit`|Last 200 bounded, sequenced profile events and the next sequence|
|`completionSeen`|Whether the completion notice was acknowledged; historical milestones remain|
|`legacy`|Original passive guide's numeric step/status, retained as legacy metadata|

Every new save includes the existing accounts, stock, RNG streams, selected tank, local timeline, receipts, unique equipment/livestock IDs, genes, medical state and history. No fields in those systems are reset by guide migration or Restart.

## Migration and validation

Core creates the extension after Finance establishes the profile identity. Normal save migration upgrades legitimate old passive state before validation. Legacy active guides start interactive guidance and recognize actual physical state. Legacy skipped/completed guides stay opted out; old text navigation is not converted into fabricated verified milestones. Unsupported versions and malformed legacy progress reject rather than silently downgrade.

Validation enforces known tasks, matching phases, allowed statuses, profile identity, supported marine species, bounded IDs/product IDs, finite times, known signal types, milestone/tank association, bounded sequenced diagnostics and complete evidence before a completed status. Historical verified milestones are observations, so ordinary later equipment wear does not falsify earlier history. Current readiness is rechecked before final completion and incoming stocking.

The only control transaction is the existing `tutorialProgress` action, now using explicit operations. Arbitrary old `{step, status}` writes cannot complete the guide. Pause/Resume, explicit owned marine tank selection and completion review mutate guidance only. Skip/Restart require confirmed operations. Interface observations use one-use internal UI tickets; real setup/feeding/cycling/stocking still require their underlying authorities. This is local client validation, not a claim that hand-edited source/JSON is cheat-proof.

Actual successful save diagnostics are included in the encoded main checkpoint. A failed write restores the earlier audit/sequence instead of inventing a saved event. Real `Save.load` adds a restoration event; generic JSON parsing does not repeatedly log loads or advance time. The usual offline service alone processes elapsed time. Browser close/normal autosave and user JSON export/import preserve progress using the existing save path.

Switching the selected aquarium keeps the tutorial's pinned identity. Deliberately choosing another guide tank starts fresh task observations for that tank and preserves previous references. Losing the active guide tank clears its current task evidence safely. Losing the target fish clears that individual's stocking/care observations without removing remains, altering death history or creating another animal.

No remote account, server save, analytics service or external logging endpoint is introduced. Profile/origin separation and the existing local financial replay guards remain unchanged.

## Loop repair compatibility - v4.2.1

No new save version or required field is introduced. Explicit descriptor prerequisites and the observer guard are code-only. Pending capture timers and developer route traces are ephemeral and never persisted as verified actions. Previously verified milestones retain their IDs/times; same-product detail reopening preserves destination checks. Reopening after a browser reload guides the player back to the actual uncommitted form, with the existing transaction guards preventing repeat ownership or payments. Native details/modal state is intentionally not restored as a pending financial transaction. Five real interruption checkpoints are covered in the full audit report.
