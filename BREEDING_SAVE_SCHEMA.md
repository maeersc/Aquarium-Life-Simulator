# Autonomous breeding save extension — schema 2, breeding v1

The root save version remains 2. Existing browser-local accounts, tank/livestock IDs, credits, finance/casino receipts, mortality history, coral frag lineage, genetic profiles and legacy/purchased clutches are preserved. `AL.Save.migrate` initializes missing fields only; repeated migration neither advances RNG nor creates a courtship, egg or hatchling.

| Location | Persisted fields |
|---|---|
| `state.breeding` | `version:1`, independent unsigned 32-bit `rng`, detailed `records`, archived courtship/spawning/hatch/failure totals |
| Marine `tank.breeding` | Next hourly eligibility checkpoint, active pair-record IDs, reserved adult load and offspring entity count |
| Marine `fish.reproduction` | Reproductive role (`M`, `F`, `simultaneous`, `immature`, `unverified`), maturity observation, partner/pair/clutch IDs, observed state, last spawning time, recovery end; optional male-to-female transition end |
| Courtship/history record | Unique `court<N>` ID from the existing entity counter, tank/species/parent IDs, saved spawning site, start/spawn/end times, lifecycle status, clutch ID, modeled egg count, offspring ID/species/parent/hatch records, observed result and egg-loss totals |
| Natural clutch | Original brood schema/genetics plus `naturalBreeding:true`, reproductive mode, courtship-record ID, spawn time, male carrier ID where applicable, saved site/anchor, fertilization probability, individual modeled embryo survival flags and counted loss categories |
| Natural offspring | Original fish schema and inherited embryo pattern, exact parent/generation IDs, captive-bred provenance, `naturalOrigin` with clutch/pair IDs, larval ration, hatch time and minimum sale age |

Legacy `.sex` stays F/M for compatibility; the reproductive role is authoritative for simultaneous hermaphrodites and immature clownfish. No old unknown genotype or old spawning timestamp is invented. Existing nonnegative `lastBreed` can initialize last-spawn/recovery, while `-99999` initializes no prior spawning. Old clutches retain their original `.strategy`, incubation duration, genes and embryo identities. New strategy-specific behavior uses the additive `reproductiveMode`, without rewriting the legacy strategy vocabulary.

Sites store `surface`, support ID, local attachment coordinates and fallback normalized x/y. Rock movement follows local coordinates; pelagic positions drift deterministically from saved age. Mouthbroods store a cover site for parental swimming but have `anchor:null`, so no external eggs render.

Validation rejects duplicate courtship/global entity identities, invalid RNG, broken active pair references, parents of the wrong biological species, a parent in multiple active pairs, missing incubating clutches, incompatible carrier/site/strategy changes, malformed embryo state, forged known genetic viability, inconsistent displayed viability, repeated offspring IDs and incorrect adult/entity reservations. Historical parent IDs may refer to fish no longer owned. Completed old records can be compacted only after their active clutch is gone; original legacy event and frag histories are not rewritten.

Spawning replaces the pair reservation once; successful hatching removes the clutch once and records each new fish ID once. Save/load/inspect do not hatch. Both live and offline progression call the same bounded simulation steps and persistent RNG; the existing account/world checkpoint guards prevent replaying elapsed time on repeated login. A just-created clutch does not receive the preceding five-minute interval again.

Save/export/import/recovery and all records remain local to the player's PC/browser. Export JSON when moving from file:// to GitHub Pages, changing browser/profile/site origin or clearing browser storage. The latest 600 detailed reproductive records are retained with permanent aggregate archive totals; this extension does not claim an unlimited full-detail breeding archive or cryptographic protection against manual file editing. The existing 5 MB save-file import limit remains.
