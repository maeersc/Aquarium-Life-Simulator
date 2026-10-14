# Aquarium Life — GitHub Pages deployment

Build the latest game from the development folder:

```powershell
python build.py
```

The build refreshes `DIST/index.html`, scripts, styles, referenced local art and
review pages. It removes stale generated files, checks exact filename case and
source/output hashes, writes `DIST/build-manifest.json`, adds `.nojekyll`, and
rebuilds `AquariumLife-GitHub-Pages.zip`. Python's standard library is enough;
no Node install, package downloads or server is required to build or play locally.
This classic-script game has no transpilation stage. Current source scripts and
prebuilt art banks are copied exactly; rebuilding does not regenerate artwork.

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

- The active game (`aquarium-life-v2`), recovery backup and offline timeline are
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
