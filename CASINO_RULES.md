# The Dock Casino - rules and persistence

Playable v3.7, rules version 1. `js/casino-rules.js` is the sole runtime definition of symbols, weights, payouts, card statistics and comparisons. UI probabilities are enumerated directly from those rules before wagers are offered. Changes to the rules require a new version and migration for pending rounds; never silently reinterpret a saved wager.

## Gold Fish

Each of three independent draws uses ten equally likely buckets: Blue Reef Fish 4, Clownfish 3, Reef Angelfish 2, Gold Fish 1. There are 1,000 equally likely ordered bucket triples.

| Exclusive outcome | Bucket triples | Probability | Total returned, including stake |
| --- | ---: | ---: | ---: |
| Three Gold Fish | 1 | 0.10% | 25 x wager |
| Any other three identical symbols | 99 | 9.90% | 3 x wager |
| Exactly one matching pair | 600 | 60.00% | 1 x wager |
| All different | 300 | 30.00% | 0 |

Expected total return per AC = (1 x 25 + 99 x 3 + 600 x 1) / 1,000 = 0.922, or 92.2%. Net expected change is -7.8% of wagers. This describes the probability model, not a guaranteed session result or an external fairness certification.

## Predator & Prey

Both sides independently draw one card, with replacement, from the same six marine species: Ocellaris clownfish, Royal gramma, Yellow watchman goby, Tailspot blenny, Marine betta and Yellow tang. Identity, scientific names, art and game foods come from the existing livestock catalog; no livestock is acquired, consumed or harmed by a card round.

The central card table defines attack, defense, fictional role and trait. Score = attack + defense + applicable trait bonus. Shelter gains +2 against Hunter; Forage gains +1 against Reef shelter; Surge gains +2 against Grazer. Larger score wins; equal scores draw, including equal cards. Rarity never affects scores. Local research supports ecological feeding annotations where available; missing facts are labeled. **These roles, statistics and pair bonuses are fictional card mechanics. No undocumented biological species-pair predation claim is made.**

All 36 ordered pairs are enumerated: player wins 11, dealer wins 11, draws 14. Wins return 2 x wager, draws return 1 x, losses zero. Expected return = (11 x 2 + 14) / 36 = 100%. There is no house edge in this symmetric card game. Independent random outcomes still vary.

## Wallet, safeguards and storage

Whole wagers from 1 to 1,000 AC use the actual wallet, never aquarium asset value. Review and confirmation precede deduction. A single `AL.Casino` service runs through atomic `AL.Core.act` drafts and `AL.Finance`, category Casino. Wager and payout receipts use canonical `<account>:casino:<sequence>:wager/payout` keys. Casino payouts are total returns, not extra amounts on top of a refunded wager.

The draft is saved successfully before the live UI commits a new wager or settlement. Storage failure leaves the live wallet unchanged. At confirmation, rejection-sampled browser cryptographic randomness fixes the game draws, round ID, stake, account, time and wager receipt in a saved pending round. Animation only reveals that saved outcome. Loading and continuing resumes the same round. X/Escape/backdrop dismissal waits during an active reveal. If settlement fails, the player can safely close the window with the fixed outcome still saved and settle after resolving storage or wallet capacity; there is no voluntary discard/reroll. A completed sequence is never charged or paid again even after recent action tokens or the 100-round display history expire.

`casino` is an additive version-1 save extension. It retains account, next sequence, pending round, latest 100 completed rounds, cumulative wager/payout totals and optional spending preferences. Save validation recomputes outcomes/payouts and cross-checks available ledger receipts and durable keys. Local `aquarium-life-casino-heads-v1` checkpoints reject older backups that predate this account's saved rounds, including losing settlements with no payout receipt. The raw older save is protected, not silently overwritten. Heads are auxiliary safeguards, not a server authority. Clearing local browser data removes local safeguards and saves; an offline client cannot prevent deliberate client/source/storage tampering.

The optional account-wide daily limit counts wagers across both games per **in-game day** (20 real minutes); zero disables it. It does not refund wagers or change the odds. Balance space for maximum payout is required under the existing 1-billion-AC wallet cap. If an unrelated credit gain fills that cap before settlement, the pending round remains saved until wallet space is available; it is never erased or downgraded.

Casino wager/payout spending and earnings use the normal totals and receipts. Existing +50 healthy-care and +100 survival rewards, death/recovery rules, simulation time, maintenance, Deep Market reputation and freshwater biology are unchanged. Casino is an account activity and can be opened while a retained legacy freshwater tank is selected, without enabling freshwater actions. All data is local. No deposits, payments, withdrawals or real-money prizes exist.
