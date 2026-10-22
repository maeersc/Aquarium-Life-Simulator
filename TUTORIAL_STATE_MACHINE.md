# Interactive saltwater onboarding

Playable v4.2.1 - master v4.13 - October 21, 2026

The authoritative tutorial rule lives in master section 5.6. This document describes the implementation in `js/tutorial.js` and `js/tutorial-ui.js`.

## Model and transitions

There are 22 stable task IDs grouped into twelve phases. Each descriptor defines its ID, phase, explicit prerequisite ID, context, logical target, instruction, expected action, validation, completion event, next ID and interruption recovery. The prerequisite graph is a directed acyclic chain; independently verified physical states may already be satisfied. The current task is always the first missing required evidence. The model observes real Core transactions and fixed simulation steps. The UI resolves actual DOM elements; it never performs the task by clicking a tutorial button.

| Phase | Task IDs | Required evidence |
|---|---|---|
|1 Welcome and selection|`welcome`, `aquarium`, `view`|Actual Aquariums interaction; owned marine tank; visible empty-tank setup button or an unobstructed canvas interaction|
|2 Preparation|`substrate`, `fill`, `prepare`|Actual sand depth where appropriate; authoritative filled and prepared flags|
|3 Life support|`filter`, `controller`, `flow`|Operational installed devices; temperature control where room/species conditions require it|
|4 Shelter|`hardscape`|Actual supported rock/cave where relevant; a preview or canceled placement does not count|
|5 Temperature and salinity|`temperature`|Measured water inside the current species ranges; target temperature alone is insufficient|
|6 Nitrogen cycle|`cycle`|The existing preparation/cycling authority reports established colonies and completed cycling|
|7 Water verification|`quality`|Actual shared receiving checks plus the existing general marine nitrate threshold; player reviews readings after cycling while they pass|
|8 Store navigation|`shop`|Actual Saltwater Fish shop interaction|
|9 Species and price|`details`|Actual compatible starter listing opened, with species requirements and legitimate price|
|10 Receiving and stocking|`destination`, `stocking`, `observe`|Actual destination selector and compatibility review; permanent owned fish after existing purchase; actual aquarium observation|
|11 Care|`feed`, `appetite`, `inspect`|Inventory-consuming compatible manual feed; actual individual meal record; actual living fish inspector opened|
|12 Completion|`complete`|All verified milestones, living owned resident and current passing receiving/water checks|

The current task is the first unsatisfied ID. Physical requirements can already be satisfied, but looking at a page cannot fabricate equipment, water, bacteria, ownership or feeding. Verification time records when the guide verified the evidence, not an invented historical purchase date. Milestones retain their tank ID and evidence source.

The model changes tutorial records only. It does not advance time, change bacteria/chemistry, install items, purchase animals, dispense food, diagnose illness, restore dead livestock or award money/XP. Existing normal speed controls remain. The legacy Finish fishless setup shortcut is unavailable for an active or paused pinned guide; its direct UI dispatch is also guarded. Other ordinary game functionality remains available after deliberate opt-out.

## Contextual targets

The resolver walks the currently open native modal, primary window, Store habitat/category, product details, real destination selector and final action. It points to Close, the existing window selector or a tab when the player has navigated elsewhere. It uses stable IDs/data attributes rather than recorded pixel coordinates.

The small tooltip, outline/ring and four dim regions derive their position from actual DOM bounds, clipped against scroll containers. Placement protects the full active purchase, installation or thermostat form so the tooltip does not cover other required price, quantity or destination fields. Only the tooltip accepts pointer events; the ring and dim regions cannot intercept the target. Resizing, scrolling, native dialogs, dynamic listings and keyboard focus are handled. A missing target produces a logged recoverable message and working Pause/Skip controls. Repeated checks do not continuously log the same failure. Offscreen targets do not leave a misleading ring on unrelated controls.

No Next/Back interface exists. Focus target scrolls and focuses an actual element without clicking it. Pause hides guidance; Resume returns to the saved objective. Skip and Restart use a separate native confirmation dialog, preserving pending Store/details content. Restart resets guide progress only and retains bounded diagnostic history. Completion has an explicit review/dismiss control and shows the recorded completion time separately from current aquarium status.

## Existing ownership and interruptions

- Existing genuine installed equipment, prepared water, cycling, shelter and owned fish are recognized. No duplicate purchase, emptying or recycling is demanded.
- A real saved individual meal can satisfy existing-player care. A new guide requires a real compatible manual portion and actual consumption; merely opening Feeding does not count.
- Established bare-bottom aquariums are not forced to buy unnecessary sand; sand-dependent species still retain their requirements. Existing species-specific shelter remains required. Bare quarantine does not invent substrate or waive biological checks.
- The guide is pinned to an owned marine tank. Normal aquarium switching does not retarget it. Settings provides an explicit guide-aquarium selection, which does not switch the player's active aquarium or move assets.
- Sold/missing tanks reset the current run safely, preserving bounded past-tank references. Zero-aquarium profiles can create another tank through the normal catalog.
- If the selected tutorial fish dies, is sold or moves away, its care milestones/signals are cleared. The real death/history/ownership is retained; no replacement fish is invented or restored.
- Legacy passive Next clicks are not evidence. Old active guides enter the new guide with real-state recognition. Old skipped/completed guides retain opt-out and their legacy status, with no false interactive completion.

## Shared receiving and economy

The normal Store transaction already performs purchase and permanent stocking atomically. Onboarding teaches its real destination, compatibility, price and confirmation; it creates no second charge, fake holding queue or new acquisition pathway. Core, Finance, StoreRules, medical admission and the existing receiving authority remain responsible for actual ownership.

Current-resident readiness avoids counting that same fish twice. Incoming purchase checks retain every existing resident and active treatment restriction. The shared fish report accepts an explicit incoming quantity for Store group checks; ordinary diving calls still default to one individual. Social group, adult load and entity counts use that same incoming quantity. Existing species, water, quarantine, predator and other safeguards remain.

Starter recommendations use actual implemented care data, minimum volume, level, stock, price and passing receiving checks, rather than rarity alone. Existing group-one starter profiles are used for this guided single-fish path. No stock, daily rotation, breeding protocol or rarity is invented. If no safe affordable listing is available, the guide explains legitimate rotation/objective options. Pair offers retain their configured 5% rule and are not required.

## Diagnostics and accessibility

Settings > Local Debug Log shows the last 200 profile-specific guide events and can export them as a local JSON file. Events include action, validation, step start/completion, target resolution/missing targets, pause/resume, skip/restart, save and restoration. Save success is committed with the main local save; failed storage rolls back the provisional success record. Restoration observes saved state without simulating elapsed time.

The current build had no separate Local Debug Log service before this update; this view exposes the bounded tutorial audit instead of inventing a remote logging dependency. All data stays in the existing local profile save. The guide has visible text and outlines, labeled native controls, keyboard support and static reduced-motion presentation. It requires no rapid reactions. Existing native transaction confirmations and modal-close behavior remain.

## Full route audit and transition safety - v4.2.1

A visible empty-tank panel intercepts pointer input, so its setup button is the actual initial target. The guided viewing action opens Tank Setup and records real navigation; sand, fill and preparation still require their own ordinary actions. A covered canvas is never demanded as the only initial pointer path.

Trusted native input can checkpoint microtasks between event listeners. Capture metadata and arguments immediately, then validate the completed UI outcome in a later timer task. Discard queued observations from a different profile or a task that has since changed. One-use tickets and the bind-once guard remain. The model has a reentrancy guard and idempotent milestone writes. Reopening the same product does not erase reviewed destination evidence; choosing a different listing legitimately invalidates only listing-specific review.

Only open details dialogs supply purchase markers, destination forms and thermostat inputs. A closed dialog may retain HTML, but it supplies no active target. Store/Inventory search and category blockers use their actual visible controls. Existing installed/prepared/cycled/owned/recorded-care states remain valid observations. Current safety is always checked again before stocking and completion.

`AL.Tutorial.diagnostics.enabled` defaults to false. Developers may opt in through DevTools. Its bounded80-event in-memory trace detects six unresolved alternating/repeated routes with unchanged profile/task/milestones, emits one Local Debug Log warning per unchanged progress state, and records previous/current task, triggering event, result and prerequisites. It never changes progress, money, biology or UI navigation. Real cycling/meal waiting produces no diagnostic without repeated user actions. The complete task-by-task map and current executed A-F cases are in TUTORIAL_FULL_AUDIT_AND_REPAIR_REPORT.md.
