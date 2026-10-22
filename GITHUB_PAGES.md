# Aquarium Life — GitHub Pages deployment

## Protected production distribution - 2026-10-22

Current master v4.17; gameplay remains v4.3.1 with a new protected distribution pipeline. Production now minifies JS/CSS, shortens internal identifiers, uses content-derived code filenames and excludes review pages, source maps, project documentation and tooling. Human-readable game code and original assets remain untouched. Assets retain their original pixels and offline file transports; no encryption, passwords, licensing dependency, profile rewrite or save-key change is introduced. Runtime safety and the mandatory performance pass take priority over obfuscation. DISTRIBUTION_PROTECTION_REPORT.md records exact mechanisms, commands, executed tests, benchmarks and limits. Earlier build descriptions are historical where superseded.

## Current delivery — playable v4.3.1, 2026-10-22

The current UI polish and store quantity release is rebuilt with `python build.py`. Deploy all contents of DIST, including `.nojekyll`, or extract AquariumLife-GitHub-Pages.zip at the Pages site root. Original local art and on-demand native source transports remain included. All player saves, inventories, receipts and profiles remain device-local; JSON export/import moves a collection between browser/site origins. See UI_POLISH_QUANTITY_REPORT.md and STORE_QUANTITY_RULES.md. Earlier release sections are historical where superseded.

## Current v3.8 delivery — 2026-10-15

DIST is rebuilt from current local source with python build.py; deploy its contents (including .nojekyll) at the Pages site root. The Pages ZIP contains those same contents. Breeding, all account saves and JSON backups remain local to the player's browser/PC. Export/import JSON when changing file/site/browser origin. See BREEDING_UPDATE_REPORT.md for actual release verification.

## v3.7 equipment, inspector research and Dock Casino - 2026-10-15

Current playable release is v3.7 / consolidated MDP v4.0. DIST includes equipment-category search filters, original fragging-tool previews, owned-fish inspector research at 5 AC once per species, playable Gold Fish and Predator & Prey, and aligned aquarium header controls. All player data, including casino rounds and research, remains device-local. Use the rebuilt DIST contents or AquariumLife-GitHub-Pages.zip at the site root. See STORE_CASINO_UPDATE_REPORT.md and CASINO_RULES.md for changes, odds, persistence and limitations. Earlier build/release sections below are historical.

## Heater levels and permanent mortality journal v3.6 - current, 2026-10-15

Marine equipment now offers seven fixed heater levels: 5-20, 20-75, 75-250, 250-1,000, 1,000-3,000, 3,000-7,500 and 7,500-15,000 US gallons. Store recommendations use the selected aquarium; undersized new purchases are blocked. The main tank view shows heater state, rated capacity and condition. Legacy heaters retain their actual saved ratings; transfers never resize a heater.

Marine heat uses capacity/condition-limited thermostat output and exact exponential heat exchange on the same live/offline timeline. No setpoint overrides failed or missing equipment. Status distinguishes suitable resident conditions, general chemistry, unsafe resident temperatures and empty/deceased aquariums. The 20-minute day, existing nutrition, maintenance, local saves, +50/+100 rewards and freshwater lock remain.

The existing single mortality authority now maintains a dedicated permanent account journal, detailed fatal-step evidence, hourly recent history and offline-run audits. Field Journal > Tank History > Livestock Deaths has filters, complete reports, Export Mortality Log and selected-report JSON export. Welcome Back links to the latest offline period. Original recorded evidence migrates unchanged; unknown older facts remain unknown. Storage failures retain pending records and warn rather than silently dropping them. See [HEATER_MORTALITY_REPORT.md](HEATER_MORTALITY_REPORT.md) and [MORTALITY_LOG_SCHEMA.md](MORTALITY_LOG_SCHEMA.md). Current playable version v3.6 / MDP v3.9. Earlier release statements are historical where superseded.

## Overnight mortality repair v3.5 - current rule, 2026-10-15

Repaired marine starvation, diet selection and coral-only automatic feeding on the existing 20-real-minute game day. Eight real hours still advances 24 game days. Provisioned adult, mixed, juvenile, coral and grazing/scavenging test aquariums survive 8, 12 and 24 real hours; this does not guarantee every stocking or unsupported tank. Actual food exhaustion, untreated disease and failed environmental support can still kill residents.

Automatic feeders check six times per game day, consume actual compatible inventory and adapt to maturation. Natural grazing/scavenging uses finite available resources. Hunger must coincide with depleted nutrition before calorie-deprivation damage; the separate malnutrition condition does not apply the same damage twice. No existing dead livestock is restored, no credits are compensated, and freshwater biology remains protected.

Equipment > Tank Care and Field Journal > Tank History show **Overnight Readiness**. Welcome Back and Tank History retain actual death-step causes, identities, food, equipment and chemistry separately from current recovered water. Local loads retain an untouched pre-repair snapshot when storage permits, exportable in Settings. Saves and downloads remain on each player's PC/browser. Review [OVERNIGHT_REPAIR_REPORT.md](OVERNIGHT_REPAIR_REPORT.md) for formulas, the complete absence matrix, reproducible evidence and limitations. Current playable release is v3.5 / consolidated MDP v3.8. Earlier release sections below are historical where superseded.

Build the latest game from the development folder:

```powershell
python build.py
```

First prepare the private build tools once with `python tools/production/bootstrap.py`. They use pinned package-lock versions and an isolated portable Node runtime; they are never player dependencies. Subsequent `python build.py` runs use the local installed toolchain without downloading packages.

The protected build transforms into DIST only, preserves original development files, emits hashed/minified scripts and styles, retains required original images/file transports, removes stale development files, writes output checksums and produces a deterministic root-level Pages ZIP. No source maps, development review pages, source mapping records, tests, tools or player saves ship. The game remains classic-script and opens directly at DIST/index.html with no server. No assets or profiles are encrypted. Keep AquariumLife-v0.1.zip private: it is the separate human-readable development archive, not a deployment artifact. See DISTRIBUTION_PROTECTION_REPORT.md for exact protections and limitations.

## Upload the finished contents

1. Run the build after editing the source game.
2. Copy **the contents inside `DIST`** into the root of your GitHub Pages repository
   or publishing branch. `index.html`, `.nojekyll`, `js`, `css` and `assets` must be
   at that root. Alternatively extract `AquariumLife-GitHub-Pages.zip` there; its
   contents have no outer `DIST` directory. Keep `.nojekyll` even if hidden.
3. In GitHub, choose **Settings → Pages → Deploy from a branch**, then choose that
   branch and **/(root)**. Save the settings and wait for GitHub's deployment.
4. Open the published Pages URL. Relative paths support a repository address such
   as `https://username.github.io/aquarium-life/` as well as a domain root.

Do not upload the development directory wholesale: it contains test browser
profiles and a large archival development ZIP that are not part of this release.
There are no player saves or browser profiles inside DIST. Individual build files
are checked below 100 MB and the published folder below 1 GB. For larger files,
use Git rather than GitHub's web file uploader, which has its own smaller limit.

GitHub's branch publishing UI accepts root or `/docs`, not `/DIST`. To keep DIST
inside a full source repository instead, configure your own GitHub Actions
workflow to run `python build.py` and upload `./DIST` using the official Pages
artifact/deployment actions. No deployment or account change is performed by
this local build.

Official instructions: [publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site),
[custom Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Saves stay on each player's computer

- The active game (`aquarium-life-v2`), recovery backup, offline timeline and diving completion receipts are
  stored in that player's browser localStorage. GitHub serves static game files;
  the game does not upload saves or send them to GitHub or another player.
- Autosave, Save now, settings and transaction saves use the same local save
  system. No account, database, shared server save or cloud synchronization exists.
- **Settings → Export JSON backup** downloads a save file to the player's PC.
  **Import JSON backup** reads a file selected by the player locally in the browser.
- Progress belongs to the browser profile and website origin. Another browser,
  computer, private window, local `file://` copy or different domain will not
  automatically see it. Export/import JSON to move it. Clearing site data can
  erase browser saves; private browsing generally removes them on exit.
- Updating the static game at the same address does not intentionally reset
  local saves. Existing additive migrations remain. Keep a JSON backup before
  changing hosting addresses. GitHub Pages repositories on the same hostname
  share an origin; this game's existing keys are retained for compatibility.

Browser storage behavior: [MDN localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage).

The hosted site needs a connection to download its files. The original extracted
build can still run directly from `index.html` offline. This deployment does not
add a service worker or promise the hosted URL will reload without a connection.
