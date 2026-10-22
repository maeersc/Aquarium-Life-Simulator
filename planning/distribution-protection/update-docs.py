from pathlib import Path
import re
R=Path(__file__).resolve().parents[2]
p=R/'MASTER_DEVELOPMENT_PROMPT.md';old=p.read_text(encoding='utf8');new=old.replace('VERSION 4.16','VERSION 4.17',1)
new=new.replace('# 30. CONTINUITY, DOCUMENTATION & LOCKED RULES','''## 29.1 Protected Production Distribution

Development source, original assets, review pages, full debugging and test tooling remain human-readable and unchanged by production builds. `python tools/production/bootstrap.py` prepares pinned build-only Terser5.44.0/clean-css5.3.3 and a checksum-verified portable Node22.23.0 on Windows; `python build.py` then reproducibly regenerates DIST and the root-level Pages ZIP offline using the installed local tools. No global installation, runtime server, licensing service or player dependency is added.

Production includes only index.html, required local runtime assets/scripts/styles, a checksum manifest, .nojekyll and a short ownership/protection notice. Exclude review pages, development documentation, original named code copies, source maps, tests, build tools, archives and player data. Minify JS/CSS; use scoped local-identifier mangling and content-derived runtime filenames. Preserve public AL interfaces, registry/species/save keys, script dependency order, relative URLs, dynamic file-origin sprite transports and all16 native frames. Disable gameplay expression rewrites when they threaten performance or fidelity. Do not mangle properties or global interfaces, add runtime string decryption, control-flow flattening, anti-debugging loops, debugger traps or artificial slowdowns.

Minification reduces syntax; identifier mangling is limited obfuscation; ZIP compression reduces storage/transfer; SHA-256/CRC checks detect accidental corruption. None is encryption or tamper-proofing. PNG assets retain their exact approved pixels; HTTP native files and on-demand classic-script transports preserve existing file:// compatibility. Offline delivery cannot conceal a distributed asset-decryption key from its recipient. Do not add ineffective encryption claims, passwords or online key services. No save encryption, authentication change or save rewrite is authorized. Browser code/assets remain inspectable, copyable and locally modifiable.

Keep the source-to-protected mapping, transformation/cache records and all development evidence outside DIST. Public checksums contain output paths/hashes, not source maps. Validate all original source/art hashes, native transports and every published checksum, and reproduce manifest/ZIP bytes with a second build under the same pinned toolchain. Complete section25.5 with matched development/protected benchmarks, local-video multitasking where possible, memory/listener soak, file and HTTP repository-subpath launches, purchases/Inventory, saves, tutorial, diving, casino and biological/breeding regressions. Report physical GPU/Netflix/audio-sync measurements as unavailable when not measured. See DISTRIBUTION_PROTECTION_REPORT.md for actual commands, evidence and limitations.

# 30. CONTINUITY, DOCUMENTATION & LOCKED RULES''',1)
new=new.replace('## 24.17 Store Quantity Persistence','''## 24.18 Production Protection and Existing Saves

Production transformation never encrypts or rewrites player profiles, local authentication, account IDs, financial replay keys or saved species/property names. Keep original local storage keys and schema2/tutorial2 migration/validation. Preserve the same DIST/index.html launch location and existing export/import behavior; moving between browser/site origins still uses explicit JSON backups. Source maps and private build records must not contain player data or ship in production. See section29.1.

## 24.17 Store Quantity Persistence''',1)
new=new.replace('# 28. DEVELOPMENT ROADMAP & EXECUTION ORDER','''## 27.23 Protected Production Acceptance

Verify original development/art hashes, production-only allowlist, minified code/styles, stable public keys, no maps/review documents/tooling/player data, exact manifest and ZIP bytes and deterministic rebuild. Run tests/browser_qa.py --protected-build in Chrome/Edge for actual offline file-origin gameplay and all382 existing native sheets; --pages covers HTTP repository-subpath loads and existing diving/receiving/art/save systems. Run affected tutorial, economy, equipment/offline and breeding suites against --dist. Benchmark development and protected builds in fresh browser processes, record actual startup, capped60/30FPS, one-core main-thread CPU, GC heap, hidden/covered work and local-video playback. Compare exact matched biological state and run a five-minute navigation/listener/memory soak. Do not claim physical GPU, Netflix/DRM/audio-sync results or missing artwork completion without actual evidence. Section25.5 gates completion; record final outcomes in DISTRIBUTION_PROTECTION_REPORT.md.

# 28. DEVELOPMENT ROADMAP & EXECUTION ORDER''',1)
# Keep new persistence subsections numerically ordered.
a=new.index('## 24.18 Production Protection');b=new.index('## 24.17 Store Quantity Persistence',a);block=new[a:b];new=new[:a]+new[b:];new=new.replace('# 25. GRAPHICS ENGINE, ANIMATION & PERFORMANCE',block+'# 25. GRAPHICS ENGINE, ANIMATION & PERFORMANCE',1)
assert len(re.findall(r'^# \d+\.',new,re.M))==31
p.write_text(new,encoding='utf8')
lead='''## Protected production distribution - 2026-10-22

Current master v4.17; gameplay remains v4.3.1 with a new protected distribution pipeline. Production now minifies JS/CSS, shortens internal identifiers, uses content-derived code filenames and excludes review pages, source maps, project documentation and tooling. Human-readable game code and original assets remain untouched. Assets retain their original pixels and offline file transports; no encryption, passwords, licensing dependency, profile rewrite or save-key change is introduced. Runtime safety and the mandatory performance pass take priority over obfuscation. DISTRIBUTION_PROTECTION_REPORT.md records exact mechanisms, commands, executed tests, benchmarks and limits. Earlier build descriptions are historical where superseded.

'''
p=R/'PROJECT_CONTINUITY_SOURCE.md';s=p.read_text(encoding='utf8');assert s.count(old)==1;s=s.replace(old,new,1);i=s.index('\n')+1;p.write_text(s[:i]+'\n'+lead.replace('Earlier build descriptions are historical where superseded.','The exact complete31-section master is embedded below. Earlier build descriptions are historical where superseded.')+s[i:].lstrip('\n'),encoding='utf8')
for f in ['README.md','GITHUB_PAGES.md','DEVELOPMENT_STATUS.md','GITHUB_PAGES_BUILD_REPORT.md','TEST_REPORT.md']:
 p=R/f;s=p.read_text(encoding='utf8');i=s.index('\n')+1;p.write_text(s[:i]+'\n'+lead+s[i:].lstrip('\n'),encoding='utf8')
p=R/'GITHUB_PAGES.md';s=p.read_text(encoding='utf8');a=s.index('The build refreshes `DIST/index.html`');b=s.index('\n',s.index('prebuilt art banks are copied exactly; rebuilding does not regenerate artwork.',a))+1
s=s[:a]+'''First prepare the private build tools once with `python tools/production/bootstrap.py`. They use pinned package-lock versions and an isolated portable Node runtime; they are never player dependencies. Subsequent `python build.py` runs use the local installed toolchain without downloading packages.

The protected build transforms into DIST only, preserves original development files, emits hashed/minified scripts and styles, retains required original images/file transports, removes stale development files, writes output checksums and produces a deterministic root-level Pages ZIP. No source maps, development review pages, source mapping records, tests, tools or player saves ship. The game remains classic-script and opens directly at DIST/index.html with no server. No assets or profiles are encrypted. Keep AquariumLife-v0.1.zip private: it is the separate human-readable development archive, not a deployment artifact. See DISTRIBUTION_PROTECTION_REPORT.md for exact protections and limitations.
''' +s[b:];p.write_text(s,encoding='utf8')
p=R/'README.md';s=p.read_text(encoding='utf8');needle='Run **`python build.py`** to refresh **`DIST`**';s=s.replace(needle,'Prepare the private build-only tools once with `python tools/production/bootstrap.py`.\nThe protected production build preserves readable development source, excludes maps/review tools and retains original pixel assets/local saves. See [distribution protection](DISTRIBUTION_PROTECTION_REPORT.md).\n\nRun **`python build.py`** to refresh **`DIST`**',1);p.write_text(s,encoding='utf8')
