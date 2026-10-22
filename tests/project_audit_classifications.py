"""Explicit review decisions, in the user's original checklist order."""
import collections,json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
LABELS={'P':'PASS','Q':'PARTIAL','F':'FAIL','M':'MISSING','T':'NOT TESTED','N':'NOT APPLICABLE'}
GROUPS={}

def add(section,codes,evidence,notes=None):
    GROUPS[section]=(codes.split(),evidence,notes or {})

add(1,'P P P P P P P P P P P Q P P Q F P','E01 E02 E03 E18',{
 12:'Startup is clean; changing a store quantity throws an uncaught exception (R32).',
 14:'Representative schema-1/schema-2 saves and corruption paths were exercised; no private player save was opened.',
 15:'Namespaced modules exist, but core/UI/simulation are heavily compressed and duplicate shop code remains (I20).',
 16:'Legacy full-page shop and its delegated quantity handler coexist with the modal shop; the handler causes R32 (I01).',
 17:'Runtime species identifiers, base links, unique entity IDs and asset bank records validated.'})
add(2,'P Q Q Q Q Q P M P P Q Q Q P P P P','E04 E05 E06 E07 E16',{
 2:'Older fish have finer, noisier shading than the newer clownfish. All new sheets are provisional, not approved (I18).',
 3:'Detailed coral art exists, but style acceptance and species-level anatomy remain provisional.',
 4:'Four benthic stage sets exist; their fine shading differs from the newer clownfish collection.',
 5:'All three rock collections have detailed art; visual acceptance is still pending.',
 6:'Substrate uses procedural colored grains rather than three polished bundled substrate texture sets (I10).',
 8:'VIP cards contain future-concept text; tier-specific illustrated previews are missing (I17).',
 11:'Recognizable adult silhouettes were inspected; complete species/stage anatomical certification is not established.',
 12:'Vivid art is present; commercial varieties and species-specific biological accuracy are still provisional.',
 13:'Different generations use different effective texture density despite common frame dimensions.',
 15:'Assigned adult Ocellaris source and earlier reference remain in place; audit source hashes are unchanged.',
 17:'Actual animal art is shown; VIP concepts are explicitly labeled unfinished, not sold as completed artwork.'})
add(3,'P P Q P Q P P P P P P P P P','E02 E04 E05 E07 E18',{
 3:'Nineteen real older fish lack scientificName; all five coral entries are broad groups (R31/I14).',
 5:'Identifiers and numeric game definitions work, but care profiles are game calibrations and five specialist profiles are held.',
 10:'Five purchase-held catalog species stay visible as unavailable; art-only/planned entries are not store livestock.',
 11:'The global gallery explicitly labels planned subjects; no runtime species is inferred from a proposal.',
 13:'DATA ONLY count is zero; metadata states this explicitly.',
 14:'52 fish entities/definitions plus five coral groups; benthic fish are counted once.'})
add(4,'P P P P P P P P Q P P Q P P P P','E04 E05 E06 E07',{
 9:'All eight mappings exist; stage biology and all newly generated anatomy have not received scientific/user approval (I18).',
 12:'Shared base eggs/larvae and separate juvenile/adult phenotypes exist; exact pattern-development timing is provisional.',
 13:'Current renderer covers 311 stage selections and 156 authored dead selections without double inversion (R03).',
 14:'Designer eggs/larvae reuse their base species. Historical sheets are retained deliberately for continuity.',
 15:'Manual contact review preserves recognizable silhouettes/colors in authored dead forms; this is visual inspection only.'})
add(5,'P P P P P P P P P P P Q P P','E04 E05 E06 E07',{
 12:'Raster eye components survive cropping/scaling tests, but the complete fish can clip against tank edges (R14/I06).',
 14:'All 52 gameplay fish inspected in eight current contact pages, plus all 56 clownfish sheets and earlier stage contacts; approval remains separate.'})
add(6,'P P P Q P P Q Q P Q Q M F P P F Q','E04 E05 E06 E07 E08',{
 4:'Stable mirrored switching exists; intermediate perspective/turn poses are absent.',
 7:'Seek-food movement accelerates 1.7x; dedicated fast animation poses are absent.',
 8:'Fish pursue food and enter Eat behavior; there is no authored bite/feeding cycle (I19).',
 10:'Activity, zone, schooling and night behavior vary, but movement uses one common steering model.',
 11:'Clownfish adults have four-frame cycles; most non-clownfish select one static stage image (R15/I15).',
 12:'Motion never consults Habitat.solid; a fish placed in rock remains inside it (R13/I05).',
 13:'Centers clamp to fixed normalized bounds, independent of full sprite dimensions (R14).',
 16:'Full adult silhouette can extend beyond the glass at legal center positions (R14/I06).',
 17:'Interpolation and facing hysteresis are present; exhaustive visual testing across varied hardware/frame pacing is incomplete.'})
codes=['P']*64
for i in [40,41,55,59,60]:codes[i-1]='Q'
add(7,' '.join(codes),'E04 E05 E07 E18',{
 23:'Whitebonnet is catalogued with hybrid uncertainty and a purchase hold; presence is verified, care completeness is not.',
 24:'McCulloch is present with a specialist care hold.',25:'Wide-band is present with a specialist care hold.',
 30:'Thielle is catalogued with hybrid uncertainty and a purchase hold.',31:'Polynesian is present with a specialist care hold.',
 40:'Mocha Storm exists and is base-linked; commercial-label/source confidence remains provisional.',
 41:'Mocha Ocellaris exists and is base-linked; commercial-label/source confidence remains provisional.',
 55:'Onyx Percula exists and is base-linked; commercial-label/source confidence remains provisional.',
 59:'All intended pattern sheets exist, but exact breeder phenotype correspondence is not fully certified (I18).',
 60:'Basic clownfish family silhouettes are recognizable; species-specific spine/fin/anatomy review remains provisional.',
 61:'All 31 species and 25 varieties have eight stage/state presentations; designer early stages share the base.',
 62:'Technical eye/direction tests pass at tested sizes. Tank-edge clipping is recorded separately in section 6.',
 63:'Variety purchases reuse biological species care and compatibility. This does not certify the underlying care science.',
 64:'31 named catalog entries and 25 phenotypes; phenotypes do not increase biological species counts.'})
add(8,'P P P P P P P P P P','E02 E03 E18',{
 5:'144 protected freshwater art/source files are byte-identical to the earlier baseline.',
 6:'js/data.js is byte-identical to the protected baseline.',
 7:'Replacing only the previously delivered marine clownfish block reproduces the protected simulation file exactly.',
 8:'Shared UI freshwater destination/navigation/purchase tests pass; no new freshwater biology was introduced.',
 10:'Navigation exposes protected existing stock and honest empty categories; the current MDP explicitly protects freshwater.'})
add(9,'Q Q P P P P P P P P Q Q Q','E06 E07 E09',{
 1:'Five category-level care groups exist, without verified coral species identities (I14).',
 2:'Distinct group silhouettes exist; precise taxon anatomy remains unverified.',
 5:'Bleached art exists in the review bank, but gameplay never selects it (R16/I11). This row checks artwork existence.',
 10:'Two-frame soft coral motion and rigid-skeleton polyp pulses exist; frames stop on death.',
 11:'Eight static colony/early-stage views exist; live colony growth mainly scales adult health-state art.',
 12:'Distinct detailed colonies replace generic templates; exact group anatomy is still provisional.',
 13:'Reviewable local art exists; user acceptance of full reference fidelity is pending.'})
add(10,'P P F F P P P P P P P F Q P P P P','E02 E04 E09',{
 3:'Shallow permitted sand depth gives a suitable preview at y=.936458, but Save.validate rejects y>.92 (R05/I02).',
 4:'Upper mounted rack y=.25 passes geometry but is rejected by the save y>=.3 constraint (R06/I02). Side rack movement also loses glass anchoring (R10/I04).',
 7:'New placement checks full sprite/footprint bounds. Subsequent growth is a separate gap (I07).',
 12:'Removing a sand support is blocked, but full grown-silhouette/neighbor validation is skipped during other depth edits (R09/R30/I07).',
 13:'Suitable/Conditional/Invalid text and color previews exist, but some Suitable previews cannot commit (R05/R06).',
 16:'Initial footprint overlap and LPS warnings work; ongoing growth does not continuously revalidate geometry.'})
add(11,'P P P P P P P P P P P P P Q M Q N Q','E02 E06 E07 E09',{
 14:'Detailed alpha-column geometry supports coral mounting; AI and physical swim-space integration are incomplete (I05).',
 15:'Fish motion has no rock collision integration (R13).',
 16:'Support IDs and move/remove validation work, but growth/depth edits can leave invalid full silhouettes (I07).',
 17:'No dry/live rock-state feature is implemented; this conditional check is inapplicable, not a success. Full dry setup remains required in section 14.',
 18:'Twelve detailed collection/size/arch variants exist; art approval is pending.'})
add(12,'P Q P M P P F M M P M P Q M P','E02 E09 E10',{
 2:'Three grain colors alter procedural sand; standalone polished category texture art is incomplete.',
 4:'Every installation costs 40 AC regardless of mass, floor area or depth (R29/I10).',
 5:'A tank with no livestock accepts substrate installation; this does not imply a dry tank exists.',
 7:'Store/inspector fields use step=0.1 rather than 0.25; Core accepts arbitrary finite depths.',
 8:'Inches are displayed; centimetre conversion is absent.',
 9:'No physical floor dimensions or required sand mass exists.',
 11:'Water chemistry and capacity use nominal volume; no displacement model (R29).',
 13:'Depth moves bed/support anchors and disallows removing an occupied sand base; burrowing/maturation suitability is absent.',
 15:'Geographical sand names change visual grains without chemistry/stat bonuses.'})
add(13,'M M M M M M M M M M Q Q M P M','E08 E10',{
 11:'No algae growth exists at all; absence of a fixed timer is not a working environmental algae model.',
 12:'Sand stays visually static, including under unsuitable conditions; cleanliness is not condition-dependent.',
 14:'Whole-tank organic waste is modeled from food/fish/corpses; spatial substrate accumulation is absent.',
 15:'No anaerobic strata, conditional disturbance risk or substrate-cleaning action (I10).'},)
add(14,'P P F F F M P P Q M P Q P Q P Q P Q','E01 E02 E08 E09 E10',{
 3:'New marine tank includes five owned starter rocks (R12/I09).',
 4:'Marine sand defaults to 2.4 inches (R12); freshwater scenery is also pre-drawn.',
 5:'New tanks have full water parameters and full water visuals; prepared=false is not a dry/fill state.',
 6:'Dry bare-glass rendering and water level/filling state are missing.',
 9:'Prepare toggles readiness; separate water mixing/quantity/filling steps are absent.',
 12:'Marine rock editing works, but no staged dry/live-rock setup progression exists.',
 14:'Cycling/toxins/oxygen admission checks work; physical dimensions and substrate maturity do not.',
 16:'Cycle/reef/chemistry/light/flow checks exist; coral-specific long-term habitat age is absent.',
 18:'Prepare/cycle/stock hints exist; complete build/fill/substrate guidance does not.'})
add(15,'P P P P P P P P P P P P P P P P P P P Q M P','E02 E08 E09',{
 20:'Fish corpses and failed broods pollute; dead coral tissue is ignored (R17/I12).',
 21:'No substrate nutrient/maturation engine exists (R28/I10).',
 22:'Admission tests current temperature, salinity, pH, oxygen and toxins; this is a simplified game model.'})
add(16,'P P P Q Q P P Q P P P P P P P P P Q Q P Q P P P Q','E02 E08 E11 E18',{
 4:'Expected lifespan is stored per species, but real-world lifespan verification is explicitly null for new clownfish.',
 5:'Maximum lifespan is bounded genetically; species-specific biological calibration remains provisional.',
 8:'Food quality affects particle nutrition/hunger, without a persistent individual nutrition/diet-quality state (I19).',
 18:'Oxygen affects health, but one generic low-oxygen threshold replaces species-specific respiratory demand.',
 19:'Water/minimum litres/cover/social requirements exist; rock navigation, actual dimensions and hosting are absent.',
 21:'Age, growth and probabilistic old-age death work; age-specific activity/fertility curves are incomplete.',
 25:'Cause and death count persist, but the 70-entry event log is not a permanent death history after removal (I12).'})
add(17,'P P Q M M P M Q P P P M M M P M M M','E02 E06 E08 E09 E11',{
 3:'Authored collapsed/sideways poses appear; no time-varying roll animation.',
 4:'Every dead fish is forced upward by the same constant motion rule (R18/I12).',
 5:'No sinking/bottom settlement implementation.',
 7:'deadHours is tracked but does not select early/advanced/remains imagery (R18).',
 8:'Constant corpse-driven pollution exists, without finite mass or decay-stage scaling.',
 11:'Cause is stored on the dead entity and displayed in inspector/log; long-term history is incomplete.',
 12:'Bleached gallery art exists, but no independent living bleach state (R16/I11).',
 13:'Generic stress recovers; there is no separate bleaching recovery mechanic.',
 14:'No finite fish/coral tissue mass or degradation progression.',
 15:'Stony dead artwork remains visible until manual removal; no dissolution or skeleton-algae process.',
 18:'Dead coral does not add organic waste (R17); no dead-tissue mass model.'})
add(18,'Q P M Q P P P P P P P Q Q Q P','E02 E08 E11 E18',{
 1:'Purchase checks are stronger than transfer checks; transfers can admit unsafe water or mixed clownfish territories (R36-R38/I08).',
 3:'Admission uses nominal litres, not actual floor dimensions/swim corridors.',
 4:'Aggressive encounters and cover matter; persistent geometric territories do not exist.',
 12:'Store warnings and purchase commits work; legacy inspector/transfer rules disagree with StoreRules.',
 13:'Reef compatibility metadata is displayed but does not model coral-hosting/reef predation rules.',
 14:'School counts and clownfish pair rules exist; actual social territories are incomplete.',
 15:'Predation requires proximity, hunger, size ratio, probability and cooldown, rather than an unconditional timer.'})
add(19,'P P P P M P P P M Q P Q P P P P','E02 E08 E12',{
 5:'No live-food catalog or consumption simulation.',
 9:'No dedicated coral-food product/feeding system.',
 10:'Adult accepted-food lists and fry food work; persistent nutritional adequacy is absent.',
 12:'Particles and food seeking exist; explicit bite/mouth animation is absent.',
 16:'Automatic feeder consumes inventory once per day at 09:00, validated by the system suite.'})
add(20,'Q P P Q Q P P P P P P P Q Q P P P','E02 E04 E08 E11 E18',{
 1:'Livebearer, mouthbrood and pair strategies exist, but many marine species use simplified shared brood assumptions.',
 4:'F/M sex and carrier dependencies exist; a full species-specific reproductive anatomy/courtship model is incomplete.',
 5:'Established females are never demoted by pairing; transfers can still create mixed or inappropriate territories (R37).',
 12:'Five bounded continuous genes are inherited; verified categorical morph segregation is outside this implemented model.',
 13:'Color brightness gene exists; pattern and fin-shape alleles are not modeled (I13).',
 14:'Saved purchase phenotype exists, but Snowflake parents produce offspring with no variety model (R19/I13).',
 16:'Entity IDs and atomic actions prevent duplicate broods/purchases in tested paths.'})
add(21,'P P P P P P P P P P P P M M P Q P P Q','E02 E08 E10 E13',{
 13:'Volume-only aquarium products; no physical length/width/height model.',
 14:'No sand/rock displacement-adjusted effective volume (R29).',
 16:'Minimum nominal volume and reserved adult load exist; dimension/corridor suitability does not.',
 19:'Core.assets includes tank, fish, corals and equipment, but omits rock, sand, racks and decorations (I16).'})
add(22,'P Q P Q P P P N Q P P M P P P Q P','E02 E08 E14',{
 2:'Time-dependent ambience is present; explicit dawn-phase behavior is incomplete.',
 4:'Time-dependent ambience is present; explicit dusk-phase behavior is incomplete.',
 8:'No independently configurable spectrum engine; conditional spectrum check is inapplicable.',
 9:'Daily light affects coral stress/growth; distinct bleaching and pigment recovery are absent.',
 12:'No algae engine (I10).',
 16:'Day-dependent ambient temperature exists; lamp-generated heat/spectrum interactions are not modeled.'})
add(23,'P P P P P P P Q P P P P P P P P P','E02 E08 E15',{
 8:'Water laboratory displays values; dedicated testing consumables/instruments/history are not implemented.',
 15:'Durability reaching zero disables effect and logs failure; a broader random fault model is not claimed.'})
codes=['P']*37;codes[13]='Q'
add(24,' '.join(codes),'E03 E16',{
 14:'Default purchase connections work; editing livestock quantity triggers the duplicate legacy handler (R32/I01).',
 28:'Existing cave/driftwood/seasonal decorations only; no new freshwater habitat biology.',
 29:'Freshwater substrate category is intentionally empty with honest text.',
 33:'Black Market bottom-feeder category is present but empty.',
 34:'Black Market coral category is present but empty.',
 35:'Black Market rocks/environment category is present but empty.'})
add(25,'P P P P P P P P P P P P P P P P P','E02 E03 E04 E09',{
 9:'Explicit destination selection saves the new selection; a purchase then preserves that explicit choice.',
 10:'StoreRules is enforced inside Core.act for purchases; oxygen/toxin/predator/held-profile bypass tests reject atomically. Transfer gaps are separate (I08).',
 14:'Coral purchase commits require an allowed support; false-positive previews and later support edits are reported in section 10.',
 15:'Selection, mounts, depth and purchased entities round-trip; shopping tab choice is session-local, not saved across app restarts.'})
add(26,'P P P P Q Q P P P P P P P Q P P P','E02 E03 E04 E16',{
 3:'Equipment confirmation recomputes cost for the explicit destination volume; retail and commit formulas match.',
 5:'Difficulty labels exist; most old species use level/aggression fallback and new care remains provisional.',
 6:'Details/compatibility dialogs work; quantity changes throw a legacy UI exception (I01).',
 14:'Bounded transaction tokens and a bounded event log exist; a complete player-visible financial ledger is absent.',
 16:'Animals enter a compatible tank rather than ordinary inventory. Relocation-required corals remain owned entities, with a separate biology bug (I03).',
 17:'Empty categories state that content is unavailable/coming soon rather than offering fake products.'})
add(27,'P P P P P P N Q P P P P','E02 E03 E08 E16',{
 7:'No dealer reputation feature; conditional reputation check is inapplicable.',
 8:'Containment, habitat and night access are displayed, but fictional care uses simplified game parameters.',
 12:'Contraband resale is prohibited, stock is bounded and ordinary purchase validation applies; this is evidence for current paths, not proof against all conceivable exploits.'})
add(28,'P P P P Q P P P P Q P P P P M P P Q','E02 E08 E13 E18',{
 5:'Rarity is stored/displayed and designer retail differs, but Core.value ignores rarity and variety-specific retail.',
 10:'Rock, sand, decorations and rack ownership is omitted from Core.assets (I16).',
 11:'Adult reserved load and current growth load are separate from wallet/asset value.',
 14:'Sales reduce bounded demand, which recovers at dawn.',
 15:'Daily budgets/limits exist; no per-transaction resale waiting period (I16).',
 17:'Repeated immediate resale loses money and daily limits stop sales in exercised system fixtures.',
 18:'30-day care, 60-day breeding, hoarding/resale and 120-day bounded simulations ran; no complete new-roster 30/90/365-day economy matrix (I16).'})
add(29,'P P P P Q P P P Q P P F P P Q P P','E02 E08 E13',{
 5:'Objectives use saved actions/state, but relocation-required corals incorrectly count for reef objectives (R23/I03).',
 9:'Prepare/cycle/stock quests exist; full dry-construction/substrate/water-filling chain is absent.',
 12:'Invisible relocation-required colonies count as healthy reef progress (R23).',
 15:'Showcase and asset/discovery progression exist; a dedicated prestige score/system is incomplete.'})
add(30,'P P P P P M M M M M Q P P P P P P','E08 E16',{
 1:'Bronze concept card exists; illustrated-tier completeness is evaluated separately below.',
 2:'Silver concept card exists; illustrated-tier completeness is evaluated separately below.',
 3:'Gold concept card exists; illustrated-tier completeness is evaluated separately below.',
 4:'Platinum concept card exists; illustrated-tier completeness is evaluated separately below.',
 5:'Diamond concept card exists; illustrated-tier completeness is evaluated separately below.',
 6:'Text cards and free tint buttons do not satisfy locally bundled illustrated VIP tiers (I17).',
 11:'Free ambient tint choices exist; actual premium background image previews are absent.'})
add(31,'Q Q Q Q Q Q Q Q P P','E02 E08 E16',{
 1:'Offline selectable season value exists; no dedicated Halloween reward/content chain.',
 2:'Offline selectable season value exists; no dedicated winter reward/content chain.',
 3:'Offline selectable season value exists; no dedicated Valentine reward/content chain.',
 4:'Offline selectable season value exists; no dedicated spring reward/content chain.',
 5:'Offline selectable season value exists; no dedicated summer reward/content chain.',
 6:'Offline selectable season value exists; no dedicated anniversary reward/content chain.',
 7:'Generic procedural lantern exists; dedicated event art sets are absent.',
 8:'One seasonal decoration objective exists; event-specific quest chains are absent.',
 9:'Season selection is local, save-validated and available without internet; system fixture changes season offline.',
 10:'System fixture confirms acquired lantern ID survives a season change.'})
add(32,'P P P Q P P P P P Q Q P Q Q P P P Q P P Q Q','E02 E03 E09 E16',{
 4:'Distinct palette/layout is present; originality is subjective and has not received user review.',
 10:'Compatibility reasons are clear, but Suitable coral previews can disagree with commit (I02).',
 11:'Some hover titles and explanations exist; unfamiliar chemistry/placement concepts are not comprehensively covered.',
 13:'Overview/Care tabs and reposition work; SPS transfer UI lacks mounting coordinates (I21).',
 14:'Type/depth/support controls exist; cm/mass/maturation/maintenance sections are absent (I10).',
 18:'Food/supply inventory is visible; no comprehensive owned-item inventory inspector.',
 21:'SPS transfer can appear available yet fail on default destination coordinates; some old buy eligibility differs from commit rules.',
 22:'No hidden store duplicate was observed, but full interaction coverage outside the exercised screens is incomplete.'})
add(33,'P P P Q P P P P P P P Q P P P P P P P P P P P','E02 E03 E04 E09 E17',{
 4:'Schema/number/identity checks are strong, but coral legal-coordinate ranges disagree with placement and full growth geometry is not validated (I02/I07).',
 12:'Health/age/growth/color persist; separate living bleaching/decomposition fields do not exist.',
 22:'Representative 365-day absence fixture produces bounded eight-hour catch-up and a valid state (R27); this is not a real-year soak.',
 23:'Code catches unavailable/quota storage, protects unreadable saves and offers export/recovery; no durability guarantee is made for disabled storage.'})
add(34,'P P P P Q Q P P P M M M P T T P Q','E02 E04 E08 E14 E19',{
 5:'Sprite/plant/palette caches exist; background grains/hardscape are redrawn every visual frame.',
 6:'Short 250-fish render and 3,000-fish tick workloads are measured, but repeated linear school/encounter searches lack spatial grouping.',
 10:'No Performance preset selector/configuration (I22).',
 11:'No Balanced preset selector/configuration (I22).',
 12:'No Ultra preset selector/configuration (I22).',
 13:'Disabling ambient particles retains the same sprite rasterization; there are no actual graphics presets.',
 14:'Only short-run heap snapshots and bounded-cache inspection; no extended memory/GC soak.',
 15:'Long simulated time is validated, but multi-hour wall-clock slowdown/heap behavior was not tested.',
 17:'Render-call costs are measured; end-to-end displayed FPS/frame pacing was not measured (I22).'})
add(35,'P P P P N Q P P P','E04 E05 E18',{
 3:'All added clownfish sheets supply eight views and adult swim poses; art-only historical fish remain explicitly incomplete.',
 4:'All added clownfish technical eye/direction cases pass at tested sizes; species anatomy is still provisional.',
 5:'No coral species were added during the dedicated clownfish expansion. Existing coral defects are assessed elsewhere.',
 6:'Difficulty/care metadata exists, but five specialist profiles remain held and group calibrations need verification.',
 9:'The dedicated clownfish collection is explicitly exempted from the broader 25/5/5 batch target.'})
add(36,'P P Q P Q Q P P Q T Q P P P P P P P P P P','E18 E20',{
 3:'Current header is accurate, but an unqualified older paragraph still says sand/rock stores and substrate inspector are absent (I20).',
 4:'Catalog updated with audit quality distinctions without changing biological data.',
 5:'Current/historical milestones are separated at top; unqualified earlier wording and stale test assumptions still need cleanup.',
 6:'Original phase balance findings exist; expanded clownfish/habitat economics lack required current 30/90/365-day coverage.',
 8:'Actual consolidated file has all 31 numbered major sections.',
 9:'Critical locked rules are present, but the historical art-only gate and newer active store scope are ambiguously combined.',
 10:'Full word-by-word preservation against every historical pasted request/version was not verified; 31 sections and latest named rules were checked.',
 11:'Historical art/update instructions and duplicate active-scope language remain; no cleanup was authorized.',
 12:'Primary numbered sections exist, with cross-references for shared store/mounting/art rules.',
 13:'Actual cross-references 2.5, 3.10/3.11, 18.4, 23.1 and 24 are present.'})

def classify():
    raw=json.loads((ROOT/'tests/audit-checklist-source.json').read_text())
    groups=collections.defaultdict(list)
    for item in raw['items']:
        if item['section']:groups[int(item['section'].split('.')[0])].append(item)
    rows=[]
    for section,items in groups.items():
        codes,evidence,notes=GROUPS[section]
        assert len(codes)==len(items),(section,len(codes),len(items))
        for n,(item,code) in enumerate(zip(items,codes),1):
            note=notes.get(n,{'P':'Verified within the evidence scope cited; code inspection and browser execution are distinguished in section G.',
                'Q':'Implemented in part; the linked evidence and section F identify the remaining limits.',
                'F':'Implemented behavior conflicts with the requirement; see the cited reproduction and issue register.',
                'M':'No corresponding runtime implementation found in the cited modules.',
                'T':'No suitable executed verification for this claim.',
                'N':'Conditional check does not apply to the current implemented feature set; excluded from the denominator.'}[code])
            rows.append({**item,'check':f'{section:02}.{n:02}','status':LABELS[code],'evidence':evidence.split(),'finding':note})
    assert len(rows)==668,len(rows)
    return rows

if __name__=='__main__':
    rows=classify();counts=collections.Counter(r['status'] for r in rows)
    (ROOT/'tests/audit-evidence/checklist-classifications.json').write_text(json.dumps({'date':'2026-10-12','counts':dict(counts),'checks':rows},indent=2),encoding='utf-8')
    print(dict(counts))
