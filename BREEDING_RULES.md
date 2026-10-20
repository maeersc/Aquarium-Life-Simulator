# Aquarium Life — autonomous marine breeding, v3.8

Fish breeding in Aquarium Life happens autonomously when biologically appropriate conditions are satisfied. The player does not manually initiate courtship through the Field Journal. Reproductive condition is visible through individual livestock inspection, and eggs or offspring appear in the same aquarium as their parents according to species-specific reproductive biology.

The 20-real-minute game day, species maturity/growth, mortality, maintenance, existing AC rewards, freshwater lock and local save policy are preserved. Numerical probabilities, brood sizes, windows and development times below are **game calibrations**. They are not real aquarium husbandry instructions or claims of commercial culture success.

## Supported reproductive profiles

| Biological group / existing IDs | Roles and courtship | Spawning / development | Recovery and rearing |
|---|---|---|---|
| 26 purchase-eligible catalog clownfish, including `clown` / Ocellaris | Protandry; close swimming and hard-nest preparation; 6 game hours of courtship | Attached rock clutch; father guards/fans; 168 suitable game hours of incubation | 336 game hours; fine fry food |
| `banggai` / *Pterapogon kauderni* | Compatible female and male; circling; 8 courtship hours | Male internal mouthbrooding; 504 suitable hours; releases small juveniles, with existing juvenile artwork | 720 hours; fine fry food |
| `chalk-bass` / *Serranus tortugarum* | Simultaneous hermaphrodites; legacy F/M fields are ignored for partnering; modeled egg-donor roles alternate on later spawnings; 3 courtship hours | Synchronized water-column rise; drifting pelagic eggs; 24 suitable hours; no parental guarding | 240 hours; cultured live plankton for larvae |
| `sharknose-goby` / *Elacatinus evelynae* | Compatible female and male; cavity preparation; 5 courtship hours | Demersal rock/cavity eggs; male care; 144 suitable hours | 336 hours; fine fry food |

Each clutch represents **two modeled potential offspring**, not the hundreds or thousands of eggs a real species may produce. The chalk-bass cohort abstracts reciprocal egg trading rather than rendering every parcel. Banggai mouthbrooding stays internal: no external egg pile or pelagic larval stage is created. Parent/offspring identities remain independent of appearance and retail varieties.

Five existing specialist clownfish purchase/art holds remain breeding holds: `amphiprion-leucokranos`, `amphiprion-mccullochi`, `amphiprion-latezonatus`, `amphiprion-thiellei`, `amphiprion-maohiensis`. All other unverified profiles are held, including previously generic Royal Gramma, Firefish, Watchman, Chromis, Yellow Tang, Six-line, Tailspot Blenny, Marine Betta, both assessors and Greenbanded Goby. This does **not** claim these species cannot reproduce in captivity; the game lacks a fully reviewed role/habitat/rearing profile for them. Purchased and legacy broods keep their saved incubation model and genetics. No coral or invertebrate reproduction is added; coral fragmentation remains separate.

`AL.Breeding` supplies current runtime `breedingSupported`, `breedingStatus` and `autonomousBreeding` metadata. Original v2.7/v2.9 batch registries remain historical records, including their earlier simplified breeding flags. Current runtime status supersedes those flags. The research report and expansion details show the current status.

## Eligibility, chance and population limits

An individual must be mature, alive, at least 85 HP, nutrition at least 75%, hunger at most 40, stress below 25 and energy at least 20. Active disease above severity 0.15, infection, treatment, reproductive transition, an active pair, a dependent brood or recovery blocks another courtship. Same biological species and same aquarium are required; no cross-species hybrids or unsupported designer pairings are created.

Water must be prepared and cycled (bacteria ≥0.65 and secondary bacteria ≥0.5), within that species’ temperature, pH and salinity ranges, ammonia/nitrite ≤0.05 mg/L, nitrate ≤30 mg/L and dissolved oxygen ≥6 mg/L. Minimum tank volume still applies. Adult food **and** the correct larval ration must actually be stocked; a full adult-food inventory alone cannot support pelagic rearing.

Spawning habitat must exist. Clownfish need real hardscape; coral alone or empty glass cannot substitute. Demersal gobies use rock or an installed cave; mouthbrooding pairs need protected cover. A nest cannot share an occupied rock/nearby territory. Aggressive neighbors close to a proposed nest block courtship. Moving a support moves attached eggs through saved local coordinates. Existing attached-clutch rock-removal protection remains.

Before courtship, reserve the entire cohort’s **adult** load, plus existing fish, invertebrates, nurseries, other eggs and other active pairs. Total adult reservations must fit within **80%** of tank load capacity, keeping 20% breeding headroom for oxygen/chemistry stability. Fish/egg/pair entity reservations must fit the 250-fish limit; at most 20 incubation/pair spaces per tank. Purchases honor active courtship and egg reservations. A pair transfers its reservation to its clutch once, rather than counting twice. Space is rechecked at spawning and hatching.

Each tank checks once per saved game hour, using its own saved next-check timestamp and an independent persistent breeding RNG stream. No load-time roll occurs. Daily spawn windows and hourly chance factors are:

| Profile | Game-hour window | Base hourly chance × minimum parental fertility |
|---|---|---|
| Clownfish | 07:00–18:00 | 0.085 |
| Banggai | 06:00–18:00 | 0.070 |
| Chalk bass | 17:00–20:00 | 0.140 |
| Sharknose | 08:00–12:00 | 0.110 |

Readiness is not a promise to spawn that day. Both parents receive the profile recovery time at spawning. Disturbed/abandoned courtship has a 24-game-hour recovery delay. Clownfish born in game are immature nonbreeders, then start in the male role at maturity. If a mature group lacks an established female, the largest mature male undergoes a saved 14-game-day transition; established females never revert. A second established female is not forcibly converted to make a pair.

## Incubation, losses and feeding

At spawning, assign the existing bounded parental-average genes and the existing independent embryo pattern identities. Fertilization probability per modeled embryo is `clamp(0.72 + 0.25 × min(parent fertility), 0.72, 0.96)`. Known nonviability in the documented Snowflake reference model remains nonviable; it is recorded separately from failed fertilization. Neither fertility nor population limits guarantee one survivor.

Suitable incubation hours advance by `dtHours × clamp(1.06 ** (temperature - 25), 0.75, 1.2)`. Unsuitable water pauses development and adds loss risk. Every surviving embryo receives independent per-step hazards `1 - exp(-rate × dtHours)`:

| Category | Hourly calibrated rate |
|---|---|
| Water | 0 when suitable; otherwise 0.08 + 0.30 if oxygen <4 + 0.15 × ammonia + 0.15 × nitrite |
| Lost/poor parental care | 0.025 for a dependent clutch without a living, healthy, sufficiently fed, low-stress male |
| Parental disease | 0.012 when a parent has active illness |
| Predation | External eggs only: summed hungry-neighbor predator pressure × 0.0004 when tended, otherwise × 0.003 |
| Pelagic dispersal | 0.004, pelagic eggs only |

A dead or transferred mouthbrooding male loses his internal brood. Missing external support loses an attached brood. An external failed clutch remains selectable for one game day, or until the player removes it; pollution is added once and it never hatches. Failure records describe the modeled loss categories; no unobserved microbial diagnosis is invented.

Hatching creates persistent unique fish IDs in the parents’ aquarium. Existing baby/juvenile assets and inherited seeds are reused. Newly hatched clownfish/gobies/chalk bass start at age 1 game day and baby-stage growth; Banggai start at 30% of species maturity for the existing juvenile stage, a disclosed developmental-age calibration. No instant adults are created.

Pelagic larvae accept `plankton`, a marine-only ration representing size-appropriate cultured rotifers/copepod nauplii; standard fry food does not meet this profile. Other modeled larvae accept `fry`; the existing automatic feeder adapts to the saved larval food requirement and consumes stocked rations. The current adult diet resumes after juvenile growth and the initial establishment period; newly released Banggai juveniles keep fine fry food for their first seven game days. All ordinary nutrition, disease, predation, oxygen and mortality calculations continue. Naturally bred fish cannot be sold before juvenile growth **and** at least seven game days after hatching. Existing dealer health/value/budget limits still apply; breeding adds no AC directly.

## Genes, artwork and observations

`js/patterns.js` is unchanged. Normal, non-designer Ocellaris pairings retain 85% standard / 10% minor / 4% misbar / 1% exceptional pattern rolls. Snowflake reference-line segregation and inferred early double-mutant nonviability remain separately documented in [RARITY_GENETICS_RESEARCH.md](RARITY_GENETICS_RESEARCH.md). Other species receive ordinary saved catalog appearance identities, not Ocellaris bar categories or Snowflake alleles. The normal-pattern renderer, left/right anatomy, eyes and approved sprite assets are unchanged.

Courtship sets movement targets for the existing velocity-based swimming; it never teleports partners, freezes unrelated fish or changes sprite anatomy. Two small cyan observation marks identify courting fish; a small gold mark identifies a mouthbrooding male. Parental care returns the male toward his nest. Attached scene clutches stay 8 logical pixels, pelagic eggs 5; a fixed magnified cluster/embryo preview replaces the earlier size-growing preview. Real eggs are not represented as growing fivefold.

Field Journal → Breeding & Eggs observes current pairs/readiness, actual spawning, active clutches with parents/tank/date/count/progress, offspring growth/survival/lineage and completed/failed histories. There is no manual marine courtship button or action. The separate player-fragged clone lineage and original archived losses remain. Fish inspectors show role, maturity, partner, reproductive condition, brood, last spawn and recovery; these fields refresh without resetting the three-second selection outline or closing the inspector.

The latest 600 detailed reproductive records persist; the dashboard shows the latest 100. Older completed cohorts contribute to saved archive totals. Living fish and existing loss archives keep their own parentage/patterns; original legacy keeper events remain unchanged. This is a bounded journal, not a new permanent full-fidelity event archive.

## Evidence and scientific scope

Biological structure is based on primary or institution-maintained references; all numerical game parameters above remain calibrations:

- [Florida Museum — Ocellaris clownfish](https://www.floridamuseum.ufl.edu/discover-fish/species-profiles/clown-anemonefish/): protandry, attached spawning, male tending and pelagic larvae. The family profile shares these broad traits; it does not assert identical real incubation/culture rates for all 26 clownfish.
- [NOAA Fisheries — Banggai cardinalfish](https://www.fisheries.noaa.gov/species/banggai-cardinalfish): paternal mouthbrooding and release of developed juveniles.
- [Fischer 1984, simultaneous hermaphroditism](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1439-0310.1984.tb01361.x) and [Smithsonian archived reef-spawning study](https://repository.si.edu/server/api/core/bitstreams/6b5e5b5c-b2d3-4fbf-b879-a0a3ec507769/content): chalk-bass reciprocal egg trading/free spawning and pelagic eggs.
- [Gobioids of the Americas — Elacatinus evelynae](https://gobynet.org/species/elacatinus-evelynae): taxonomist-maintained species account with original breeding references, male nest care and larval development; [primary field study](https://link.springer.com/article/10.1007/s00338-021-02105-x): species pairing/spawning context.
- [ORA — Blue Assessor](https://www.orafarm.com/product/blue-assessor/): confirms captive mouthbrooding, but does not by itself verify the complete role/larval protocol; the new autonomous profile remains held. [ORA — Greenbanded Goby](https://www.orafarm.com/product/greenbanded-goby/): identity/habitat; the game does not guess its sex-change implementation.

Accessed 2026-10-15. This simulator is not a real-life breeding or treatment manual. Exact reproductive physiology, nest microstructure, live-culture density/enrichment and species-specific larval settlement are simplified. No biological species, approved sprite replacement, freshwater development or network service is introduced.

## Compatible Store pairs — October20

The5%listing-bound offer uses only existing supported profiles and roles, does not assert established bonding, and does not generate courtship/spawn history or guarantee a brood. Two mature individuals carry separate identities/genes/health, while actual reproductive readiness, autonomy, cooldowns, spawning windows and offspring care remain unchanged. Current coverage and inheritance holds are in BREEDING_PAIR_OFFERS.md. Completed breeding records referring to a sold tank require its real whole-sale receipt; current courtship closes factually as transferred and is not recorded as mortality.
