# Mystery fish diving rules — playable v3.9 / MDP v4.2

## Universal ocean diving receiving — 2026-10-16

All registered diving fish, corals and invertebrates now share species-aware diagnostics and explicit saved post-boat receiving. Every owned aquarium is shown; supported coral mounts and host-compatible quarantine retain all safeguards. The repair also corrects invalid noninfectious carrier flags, rock surface discovery and missing/ambiguous host mappings. Tests enumerate the real eligible registry, plus old-save, condition, expiry, replay and future-registration checks. See [GLOBAL_DIVING_RECEIVING_REPORT.md](GLOBAL_DIVING_RECEIVING_REPORT.md). Earlier host-limited flow descriptions are historical where superseded. Game v3.9 / master v4.2; local saves and freshwater lock remain.

Every valid Reef Diving and Deep Sea Diving expedition must provide at least one reachable mystery fish encounter. Its species is concealed using a question-mark silhouette until successful return to the boat. Geographic eligibility, inventory, oxygen, post-dive survival, and save persistence remain mandatory.

This release implements the requested Mystery Fish update, labeled v3.5 in the request, on top of playable v3.8. It does not downgrade prior features or save schema 2. Freshwater remains locked; existing freshwater data and biology are preserved.

## Encounters and selection probabilities

The authoritative registry is `assets/diving/registry.json`, embedded by the build as `js/diving-data.js`. A fish is eligible only when its implemented marine definition, region, mode, survey depth and collectible recovery policy all match. Fictional/held/unverified fish are excluded. No new biological species or rarity changes are introduced.

| Destination / mode | Survey depth | Guaranteed fish selection | Rarity probability for guaranteed encounter |
|---|---:|---|---|
| Fiji / Reef | 12 m | Exquisite fairy wrasse 50%; Yellow longnose butterflyfish 50% | Uncommon 50%; Rare 50% |
| Fiji / Deep Sea | 75 m | Yellow longnose butterflyfish 100% | Rare 100% |
| Caribbean / Reef | 18 m | Chalk Bass 100% | Common 100% |
| Caribbean / Deep Sea | 55 m | Candy Basslet 100% | Ultra Rare 100% |
| Japan / Reef | 8 m | Spotted Boxfish 100% | Rare 100% |
| Japan / Deep Sea | 100 m | Blotched Anthias 100% | Very Rare 100% |
| Hawaii / either | Existing policy retained | Blocked: observation-only, no collectible fish pool | No paid launch |

Selection is **uniform among eligible fish** for the chosen region/mode/depth, using saved `divingRng` at launch. Tier probabilities are the sums of species probabilities, not a separate rarity draw. The six-tier rarity system remains; current verified pools contain no Legendary fish. Mystery Egg odds remain exactly 50/25/15/7.5/2/0.5 and are not used for diving. An empty eligible fish pool blocks launch before charging or consuming random draws.

The first eight existing rock encounters remain. Object 9 is always replaced by the guaranteed mystery fish at (4,1); optional objects 10–12 retain the earlier region pool and presence rolls (35% for tier 4–6, 85% for lower tiers). Those optional draws include non-fish and may repeat species. Every optional fish also uses the same generic silhouette and concealed inventory. The table describes the guaranteed encounter, not the distribution of all optional objects.

Both existing terrain layouts admit a six-movement round trip to the fish cell (30% oxygen), or four movements when capturing from an adjacent cell (20%). A logical fish cell stays fixed while the shared original canvas silhouette swims smoothly within it. This avoids moving the guaranteed encounter out of its safe return budget. Guarantee means encounter availability, not automatic capture, survival, profit or ownership. A player can fill all eight slots with rocks and must return rather than discard or overflow them.

## Receiving diagnostics repair — 2026-10-16

All owned destinations are listed, including disabled incompatible tanks with precise reasons and actual/required checks. Working filter/circulation and absence of an active restricted medication course are checked alongside all prior biological safeguards. Eligibility updates with live aquarium state; explicit selection/focus is retained. Holding displays remaining game time and approximate real seconds, without changing the original finite deadline or simulation. Report/validation queries never alter health, assignment, survival draws or deadline. The original player's particular failed predicate cannot be reconstructed from volume/temperature alone. See [DIVING_RECEIVING_REPAIR_REPORT.md](DIVING_RECEIVING_REPAIR_REPORT.md).

## Interaction and reveal

Left-click a mystery fish within one Manhattan cell to capture it; the side button offers the same action. Out-of-range clicks only select it. The authority rechecks range, capacity and duplicate status. Capture takes one temporary slot and no oxygen, and shows exactly `Unknown Fish — ?`. The same dark generic pixel silhouette and large pixel question mark are used for every fish, without characteristic shape, markings, names, science, rarity or value.

Reef still requires Keeper 5 / 1,000 AC; Deep Sea Keeper 10 / 10,000 AC. Every successful cardinal movement costs 5 percentage points from 100%; blocked movement, time and clicks cost none. The existing WASD, arrows, direction buttons, return-route estimate and warnings remain. Zero oxygen fails even on boat arrival. Failed or abandoned trips keep mystery identities concealed and grant nothing.

Successful boat return saves a revealed results entry with actual common/scientific name, rarity, original existing species art, origin and a short original 650 ms pixel wipe. Reduced-motion preferences show the final art immediately. Before receiving, condition is honestly **Awaiting receiving assessment**, destination **Not received**, owned asset value **0**. Select a compatible cycled aquarium or quarantine explicitly; no aquarium is chosen automatically. Final assessment then shows healthy/stressed/injured/suspected illness/DOA, actual destination and current central asset value. A pending fish never counts as an owned animal or a saleable asset. Close/reopen returns to pending results; another launch is blocked until fish are received, released or expired.

Transport compatibility is checked cumulatively for each receiving action. Invalid receivers block that action without silently killing or inserting a fish. Existing dedicated transport restrictions remain for boxfish. Corals and invertebrates retain the earlier explicit pre-capture receiver/mount flow and return assessment; rocks retain owned placement inventory.

## Survival, mortality and resale

The existing model is retained:

`chance = clamp(0.96 − sensitivity×0.30 − (1−transportQuality)×0.20 − min(0.40, elapsedGameHours×0.012) − movements×0.004 − (priorConditionDraw<0.15 ? 0.15 : 0) + (quarantine ? 0.10 : 0), 0.10, 0.98)`.

Holding deadline: `collectedAt + round(1440 × (1 − sensitivity×0.5))` game minutes. Survival fails at/after that deadline or when the saved survival draw is at least the computed chance. After survival: condition draw 0–14 injured; 15–24 suspected illness; 25–64 stressed; 65–99 healthy. These are existing gameplay calibrations, not measured real-world rates. Transport quality, sensitivity, elapsed time and safe receiving/quarantine still matter. Survival and condition draws are committed at boat return; retries/reloads cannot reroll them. A valid choice of quarantine can still improve the existing chance legitimately.

Expiry progresses through the same fixed simulation as aquarium care, including offline catch-up. Every mystery-fish DOA records a permanent account-local mortality event with identity, actual simulated loss time, known assessment/expiry trigger, origin, trip steps, diver oxygen and saved transport evidence. Unmeasured transport chemistry, temperature, hunger, prior health and equipment telemetry remain unknown. Diver oxygen is not transport-water oxygen. No physiological cause is invented; transport events do not create an owned animal or change existing owned-livestock death/reward rules. Owned survivors subsequently use the existing full health/mortality system.

Regular resale remains `floor(0.60 × current Deep reference)` when eligible. Deep Market requires reputation ≥5, a matching active Wanted request, condition, hours, budget and daily-limit checks. Permanent expedition provenance is preserved. Prices, fees, care rewards, account economy and Mystery Egg rules are unchanged.

## Local saves and compatibility

Active trips store mystery version, selection model, guaranteed encounter ID, region/mode, hidden species, logical position, captured flags, temporary snapshots, oxygen, steps, fee and RNG. Successful reports store revealed identities, temporary snapshot/deadline, precommitted assessment draws, arrival time, pending/received/failed/released recovery state, receiving identity and death-record link where applicable. Receipts add `tripId:recovery:objectId` alongside existing trip completion IDs. Replayed older pending snapshots are forfeited without another animal; older settled trips remain guarded. Existing saved pre-update trips are resumed as-is rather than rerolled or retroactively hidden.

Mortality transport records add `schemaVersion:3, context:'diving-transport'` to the existing journal; prior schema 2 and legacy evidence remain valid. All game, journal and receipt data remain in device-local browser storage, with existing JSON export/import. The offline client is not cryptographic anti-cheat: someone inspecting/editing local source or save JSON can read hidden assignments. Single-species regional pools also constrain surprise; the UI never reveals assignment before boat return. Clearing browser storage removes its local receipts/history unless separately exported. Historical reports are capped at 100 expeditions; pending reports cannot be pruned by launching another trip.

## Evidence for the two Fiji profiles

The [University of the South Pacific Fiji checklist (Seeto & Baldwin, 2010)](https://www.marineecologyfiji.com/wp-content/uploads/2010/04/SeetoBaldwin_2010_FishesofFiji.pdf) records *Cirrhilabrus exquisitus* and *Forcipiger flavissimus*. Both already exist in the approved implemented roster. The [museum profile for Exquisite fairy wrasse](https://fishesofaustralia.net.au/home/species/2968) gives depth 2–40 m; the [museum profile for Yellow longnose butterflyfish](https://fishesofaustralia.net.au/home/species/2410) gives 2–145 m. The game uses conservative 2–40 m and 2–114 m encounter bands, respectively. Fiji Reef 12 m admits both, Deep 75 m admits only the butterflyfish. Sources reviewed 2026-10-15; no claim of real collection permission or new art approval is made.

## Future concept — documentation only

Consider larger original maps, connected depths/ecosystems, habitat discovery, photography, observation/research, hidden locations and environmental encounters in a future separately authorized milestone. Draw inspiration only from the sense of underwater discovery; do not copy another game's protected assets, maps, interface, characters or distinctive creative content. No expanded exploration system is implemented here.
