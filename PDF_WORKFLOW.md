# Aquarium Life — PDF workflow and continuity rules

## Current v3.8 delivery — 2026-10-15

PROJECT_CONTINUITY_SOURCE.md contains the full MDP v4.1 and both original 38/35-entry ledgers, including the current autonomous breeding rule. Binary PDF generation/render verification remains pending: Node, ReportLab, pypdf/PyMuPDF and Poppler are unavailable. No current binary PDF is claimed.

## Equipment filters, inspector research and The Dock Casino - v3.7 current

Implemented the equipment-category dropdown and original fragging-tool previews, moved paid species research to living owned-fish inspectors, and added the authorized seventh sidebar entry The Dock Casino with playable Gold Fish and Predator & Prey. All wagers and returns use the existing account wallet/ledger and saved round authority; all research remains 5 AC once per canonical species. The aquarium header controls share the information-column grid and align to its actual panel edge. See STORE_CASINO_UPDATE_REPORT.md and CASINO_RULES.md for the release, verified probabilities, local persistence and limitations. Existing biological simulation, 20-minute day, rewards, freshwater lock, livestock/art approvals and local saves remain. Earlier release sections are historical where superseded.

## Heater levels and permanent mortality journal v3.6 - current, 2026-10-15

Marine equipment now offers seven fixed heater levels: 5-20, 20-75, 75-250, 250-1,000, 1,000-3,000, 3,000-7,500 and 7,500-15,000 US gallons. Store recommendations use the selected aquarium; undersized new purchases are blocked. The main tank view shows heater state, rated capacity and condition. Legacy heaters retain their actual saved ratings; transfers never resize a heater.

Marine heat uses capacity/condition-limited thermostat output and exact exponential heat exchange on the same live/offline timeline. No setpoint overrides failed or missing equipment. Status distinguishes suitable resident conditions, general chemistry, unsafe resident temperatures and empty/deceased aquariums. The 20-minute day, existing nutrition, maintenance, local saves, +50/+100 rewards and freshwater lock remain.

The existing single mortality authority now maintains a dedicated permanent account journal, detailed fatal-step evidence, hourly recent history and offline-run audits. Field Journal > Tank History > Livestock Deaths has filters, complete reports, Export Mortality Log and selected-report JSON export. Welcome Back links to the latest offline period. Original recorded evidence migrates unchanged; unknown older facts remain unknown. Storage failures retain pending records and warn rather than silently dropping them. See [HEATER_MORTALITY_REPORT.md](HEATER_MORTALITY_REPORT.md) and [MORTALITY_LOG_SCHEMA.md](MORTALITY_LOG_SCHEMA.md). Current playable version v3.6 / MDP v3.9. Earlier release statements are historical where superseded.

## Overnight mortality repair v3.5 - current rule, 2026-10-15

Repaired marine starvation, diet selection and coral-only automatic feeding on the existing 20-real-minute game day. Eight real hours still advances 24 game days. Provisioned adult, mixed, juvenile, coral and grazing/scavenging test aquariums survive 8, 12 and 24 real hours; this does not guarantee every stocking or unsupported tank. Actual food exhaustion, untreated disease and failed environmental support can still kill residents.

Automatic feeders check six times per game day, consume actual compatible inventory and adapt to maturation. Natural grazing/scavenging uses finite available resources. Hunger must coincide with depleted nutrition before calorie-deprivation damage; the separate malnutrition condition does not apply the same damage twice. No existing dead livestock is restored, no credits are compensated, and freshwater biology remains protected.

Equipment > Tank Care and Field Journal > Tank History show **Overnight Readiness**. Welcome Back and Tank History retain actual death-step causes, identities, food, equipment and chemistry separately from current recovered water. Local loads retain an untouched pre-repair snapshot when storage permits, exportable in Settings. Saves and downloads remain on each player's PC/browser. Review [OVERNIGHT_REPAIR_REPORT.md](OVERNIGHT_REPAIR_REPORT.md) for formulas, the complete absence matrix, reproducible evidence and limitations. Current playable release is v3.5 / consolidated MDP v3.8. Earlier release sections below are historical where superseded.

## Daily livestock survival reward v3.4 - current rule, 2026-10-15

Players earn **100 AC** for every completed qualifying in-game day without a livestock death. The player must own eligible living marine livestock throughout the full simulated day. This is one account-wide payment, not one per aquarium. The separate healthy-aquarium award remains **50 AC**; both independently qualified awards total **150 AC**.

A confirmed fish, coral or bottom-invertebrate death cancels the current qualifying day and starts 1,440 game minutes of recovery. Another confirmed death restarts recovery. Recovery time cannot count toward a qualifying reward day. Illness or living coral bleaching is not a death. The authoritative game calendar remains 20 real minutes per day; legitimate offline catch-up processes the same conditions. Game windows do not stop simulation. Casino requirements apply only if that game is implemented.

Existing balances and actual historical ledger receipts remain unchanged. Every future survival payment is 100 AC through the existing financial service, with canonical account/transaction IDs, actual payment time and completed qualifying day/status. Local save, financial sequence and offline timeline guards prevent re-awarding a settled day. See [V34_UPDATE_REPORT.md](V34_UPDATE_REPORT.md) and [FINANCIAL_TRANSACTIONS.md](FINANCIAL_TRANSACTIONS.md).

## Earlier milestone material - superseded where inconsistent

## v3.3 current release - 2026-10-14

Implemented the authorized v3.1 coral fragging/trading, v3.2 financial dashboard and v3.3 Marine Research Center. Equipment has three reusable coral tools and two mounting consumables; eligible parents produce independently simulated, mounted clones with tissue loss, recovery and lineage. Diving livestock can use regular or Deep Market dealers; regular pays floor(0.60 x the same Deep reference), and Deep requires Reputation 5 plus an active wanted request. Wanted Livestock remains separate from exactly four rotating dealer stock slots.

The AC button opens a reconciled, persisted financial history. Existing wallets migrate unchanged; new profiles start at the requested 5,000 AC. Saltwater Research and the existing Encyclopedia share permanent 5-AC canonical-species unlocks. All 94 marine fish are indexed; 93 real species are researchable, one fictional entry is preview-only. Fully verified dossiers: 0; incomplete: 93; five have reviewed biological annotations. Partial content is disclosed before purchase. See [V33_UPDATE_REPORT.md](V33_UPDATE_REPORT.md), [FINANCIAL_TRANSACTIONS.md](FINANCIAL_TRANSACTIONS.md) and [RESEARCH_SOURCES.md](RESEARCH_SOURCES.md).

Saltwater-only scope, safe persistent store destinations, local PC/browser saves, existing rewards/odds, all old livestock and artwork approvals/holds remain. No new biological species or art assets were added. Full printable continuity source is updated; binary PDF regeneration remains pending. Current playable version v3.3 / consolidated MDP v3.6.

The full current 31-section MDP v3.6 and both existing 38/35-entry ledgers are retained in PROJECT_CONTINUITY_SOURCE.md. No PDF was generated or render-verified; the previously documented authoring/rendering toolchain remains unavailable. Historical workflow/version statements below are superseded by this source status.

## Earlier milestone record - historical where superseded

**Authorized 2026-10-14:** The user approved the complete 25/5/5 roster and rarities, confirmed saltwater-only, and explicitly requested "Implement v2.9". Roster approval and artwork approval are separate; new artwork remains unapproved. [Authorization](planning/v2.9/approval.json).

## v2.9 — current implementation

Implemented the twelve-step saved/skippable saltwater tutorial with medical guidance, three-second selection outlines, disabled freshwater UI, separate +50 healthy / +100 survival rewards with persistent death/recovery tracking, Deep Market display rename, local asset-value leaderboard preview, exact 15,000-US-gallon / 5,000-AC aquarium, proportional water-change salt consumption, independent mystery products and the approved 35-species marine batch. Saves remain local to each player's browser on their PC. The bottom mystery product is content-held because its Legendary host specialist is not eligible. See [V29_UPDATE_REPORT.md](V29_UPDATE_REPORT.md) for actual checks, care/art limits and release details. Earlier milestone sections below are historical wherever superseded.

Current printable source contains the old 38-row ledger, new 35-row implemented/held ledger and the complete MDP v3.5 with all 31 sections and permanent handoff rules. **Binary PDF export/render verification remains pending.** No new PDF is claimed. Future export must retain these statuses, all 73 batch IDs, back-of-source rules and art limits. Do not run historical generators that overwrite this source.

## Earlier milestone record




## Current export status

**PDF regeneration is pending.** The environment does not provide Node CLI, ReportLab, pypdf/PyMuPDF or Poppler, so no PDF has been generated or render-verified for this batch. The user explicitly permits an updated source when direct PDF generation is unsupported.

`PROJECT_CONTINUITY_SOURCE.md` is the full maintained printable source: current 38-row implemented registry, the separately marked 35-row roster-approved, unimplemented v2.9 proposal, known limits and the complete 31-section MDP v3.4 planning revision. `MASTER_DEVELOPMENT_PROMPT.md` remains the authoritative editable master; `assets/expansion-v27/registry.json` remains the authoritative implemented expansion ledger. Proposed records live only in `planning/v2.9/candidate-registry.json`. Historical report generators can overwrite newer documentation; do not run them without adapting them to the current planning revision. Do not treat an older binary PDF as current.

## Regeneration in a capable environment

1. Install/enable a permitted Node runtime, a PDF authoring tool and a PDF renderer; use the applicable PDF skill. Read its current SKILL.md rather than assuming an old script path still applies.
2. Verify the current continuity source retains the implemented registry, separately marked roster-approved, unimplemented proposal, complete MDP v3.4 and authorization gate. Use the current canonical sources; do not overwrite them with an older milestone report generator.
3. Immediately before the first PDF-authoring operation, invoke the PDF skill's `container_tools/mark_artifact_operation_started.mjs` using Node with `--operation-kind create --expected-output-count 1 --output-format pdf`, as required by that skill. Resolve the script relative to the active PDF skill installation.
4. Typeset `PROJECT_CONTINUITY_SOURCE.md` as a readable document. Repeat long-table headings and wrap species names, notes and asset links. Preserve all 38 rows and 31 major master sections; do not shrink the complete catalog to illegible text.
5. Render every page with the permitted PDF renderer. Inspect for clipping, missing glyphs, broken table rows, orphan headings and adequate margins. Correct and rerender until clean. Verify text extraction retains all 38 stable IDs and the final continuity rule.
6. Save the verified PDF as `AquariumLife-Project-Continuity-v2.8.pdf`, record page count/export date and validation in DIVING_UPDATE_REPORT.md, then update tests/package.py to include the verified PDF. Remove the pending status only after actual export and inspection.

## Back-of-workflow permanent rules

Every newly added livestock species MUST be logged in the permanent registry, CURRENT_LIVESTOCK_CATALOG.md, consolidated MDP and PDF/continuity source in the same update. Required fields: common name, scientific name, stable ID, category, rarity, care difficulty, planned/approved/implemented/art-only/partial status, update batch, implementation date, art status, living/dead support and honest notes. Synonyms must be checked before registration. Designer patterns do not add species counts.

Never automatically approve new artwork or conceal unsupported stages/reproduction. Preserve protected freshwater content, existing approved assets, saves and the selected store destination. Unsafe homes cannot receive automatic livestock placement. Keep eight daily Fish slots and independent Mystery odds unchanged unless separately authorized.

Record tests actually run, failures and not-run coverage. If PDF generation is unavailable, maintain this source and explicitly report regeneration pending. When authorized edits are complete, provide a concise report listing files, species, duplicates, tests, documentation and limits; end with the exact standalone line **Done With Edits**. Never use that completion line while authorized implementation work remains unfinished.


## Diving v2.8 source update

The current printable source is now v2.8 / MDP v3.3, with the complete 31-section master, regional ledger, expedition/provenance/reputation rules and existing 38-entry roster baseline. No biological species were added. Preserve these rules near the back of the eventual PDF. Binary regeneration remains pending the same unavailable toolchain; do not claim a new verified PDF.
