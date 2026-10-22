# Rarity and genetic pattern research — 2026-10-13

## Autonomous breeding integration — v3.8

The new marine breeding authority reuses the existing embryo/pattern functions unchanged. Normal non-designer Ocellaris retain 85/10/4/1; Snowflake reference-line segregation and explicitly inferred nonviability remain separate. No unrelated species gains those traits. Species biology, primary/institutional sources and calibration boundaries for autonomous courtship/eggs/larvae are recorded in [BREEDING_RULES.md](BREEDING_RULES.md). Existing evidence and uncertainty below are retained.

These are game design classifications and a deliberately limited inheritance model. They do not change species biology, husbandry requirements, retail prices, conservation classifications or the approved clownfish rarity table.

## Trade availability and proposed non-clownfish classifications

Common watchman goby, tailspot blenny and chromis represent accessible collection staples. Primary seller catalogs list [Yellow Watchman Goby](https://manhattanaquariums.com/products/yellow-watchman-goby), [Tail Spot Blenny among blennies](https://www.liveaquaria.com/collections/blennies), and [Blue/Green Reef Chromis](https://www.liveaquaria.com/products/blue-green-reef-chromis-1). Listings establish aquarium-trade presence, not global abundance or conservation status.

Royal gramma, firefish, Banggai and six-line wrasse are assigned Uncommon as a moderate gameplay availability band, not a claim that they are biologically rare. The trade documents [Royal Grammas](https://www.liveaquaria.com/blogs/stocking-your-aquarium/reef-basslets-grammas), [Firefish stock](https://www.liveaquaria.com/?general_pagesid=540), [Banggai cardinal production](https://www.orafarm.com/products/fish/cardinals/) and [Six Line Wrasse](https://www.liveaquaria.com/products/six-line-wrasse).

Yellow tang and marine betta receive Rare game availability for desirable collector products already in the game. Both have commercial captive-bred supply: [Biota Yellow Tang](https://shop.thebiotagroup.com/products/hawaiian-yellow) and [ORA Marine Betta catalog](https://www.orafarm.com/products/fish/other/). “Rare” here deliberately controls the seventh store slot, not a conservation assertion. Coral entries are broad existing groups, so Common zoa/mushroom/soft, Uncommon LPS and Rare SPS are game classifications, not species-level biological research claims. Fictional contraband gets separate Rare metadata; it remains fictional and excluded from normal daily fish and Mystery Egg species pools.

All 31 clownfish species and 25 variety rarity labels are unchanged. No eligible Very Rare, Ultra Rare or Legendary marine species exists in the approved roster. The safe policy is a visible Mystery Egg sales hold; probability redistribution and unauthorized rarity promotions are prohibited.

## Genetic evidence and limits

[Klann et al., Nature Communications (2026)](https://doi.org/10.1038/s41467-026-69524-8) identifies gja5b E42K in Snowflake Ocellaris. The study reports 48 Snowflake and 28 wild-type offspring from a Snowflake pair and interprets segregation as consistent with dominant inheritance and early homozygous lethality. That last point is an inference, not a directly demonstrated fate for every commercial strain. Larval patterns are indistinguishable before metamorphosis, and mature patterns develop later.

Implementation: newly purchased standard Ocellaris, Snowflake Ocellaris and Premium Snowflake can carry an explicitly labeled reference-line game model. Independent parental allele selection gives 1:1 normal/Snowflake in Normal × Snowflake and 1:2:1 alleles at fertilization for Snowflake × Snowflake. Double-mutant embryos are modeled as early nonviable, with that inference visible in the inspector. Premium is a grade, not a gene. Individually measured genotype remains null; old designer fish retain unknown genotype and their existing art. This model does not assert all commercial Snowflake combinations, pigmentation or longfin genetics are identical.

[Anikuttan et al. (2022)](https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2022.907362/full) documents heterogeneous designer offspring and trade-name ambiguity without supplying the complete cross-specific probabilities needed here. [ORA's Snowflake account](https://www.orafarm.com/product/snowflake-clownfish/) also describes individual pattern grading and breeding history, rather than a complete genotype table. Picasso, Platinum, Black Ocellaris, Longfin, Lightning Maroon and compound designer lines therefore retain unknown genotypes and visible unsupported-cross holds. No invented universal dominant/recessive rule and no cross-species hybrid production is added.

The 85/10/4/1 normal Ocellaris distribution is the user's explicit **game-balance** rule, not a scientific mutation rate. Its exceptional outcome is natural variation, never an automatic designer or rarity promotion. Other marine species retain stable catalog appearance and unknown detailed pattern genotype.

## Local randomness and persistence

Separate saved Weyl-counter/mixed 32-bit streams serve daily rotation, Mystery rarity and patterns. Bounded draws reject the incomplete upper interval before modulo. A 10,000-bucket tier roll gives the exact fractional Mystery odds, independently on each purchase; no inventory of outcomes, pity counter or guarantee is used. This is reproducible local game randomness, not a cryptographic or server-authoritative anti-cheat claim.

Mystery identity is intentionally revealed only after a successful purchase. Current content holds mean no production purchase can reach a roll. Conditional future purchase code validates all tiers against the selected home before charging/rolling, creates the existing species brood, and saves identity and genetics. Full production purchase/hatch testing for six populated tiers is deferred until authorized eligible content exists.
