# Historical initial review

The current submission is [Art Development Update 1.1](ART_UPDATE_REPORT.md), including all priority fish, coral/rock art and eye/direction fixes. The first-review record below is preserved as history.

# Livestock art review — first submission

Date: 2026-10-09. **Update: user requested this artwork for Ocellaris clownfish; assignment is complete.**

## Open the review

Open [art-review.html](art-review.html) directly, or choose **Livestock art review** in the game's footer. Everything runs offline. The gallery has the approved reference, all 22 current fish sprites, and one proposed clownfish replacement. Other proposals are explicitly Not Started.

Use Normal swim / Idle for the short animation preview, Pause and Next frame for inspection, and Dark / Bright / Transparency checker for edge review. Native candidates are 96, 128, 192 and 256 pixels; 128 is the assigned atlas resolution for Ocellaris. The upper pair and aquarium pair use equal visible fish widths without stretching proportions. No creature is added to the player's collection.

## Delivered

- [CURRENT_FISH_CATALOG.md](CURRENT_FISH_CATALOG.md): all 22 actual IDs, current source/size/animation, purchase availability, quality gaps and planned priority subjects. Ocellaris is now identified as Amphiprion ocellaris; the other real species still lack scientific-name fields.
- [ART_DIRECTION.md](ART_DIRECTION.md): reference analysis, proposed pixel/animation standard, coral-state art requirements and approval gate.
- [Clownfish 128-pixel atlas](assets/livestock/fish/clownfish/clownfish-benchmark-v1-128.png), three alternative native resolutions, preserved generated source, and JSON/classic-script metadata.
- [Exact generation prompt](assets/livestock/fish/clownfish/GENERATION_PROMPT.md): built-in imagegen, transparent output, approved concept as a style reference.
- [Comparison preview](assets/previews/chrome-art-review.png) and [game-scale preview](assets/previews/chrome-art-scale.png).
- Local review status/notes, saved separately from gameplay. Only an explicit user action records Approved; no action installs the candidate.

## Differences requiring review

The candidate captures orange-gold color, cool white-band shadows, dark edging and detailed fin/scale clusters from the reference. It is an AI-generated, technically packed prototype rather than finished hand-crafted production art.

The body is still rounded and fins are emphasized. Black band margins and pale rims are stronger than the desired natural ocellaris profile. Some detailed pixels are lost at the current small game footprint. The four generated poses have slight body/band variation. Turning is demonstrated only by mirrored endpoints, and death only by a frozen inverted pose; authored transition and decomposition frames remain open.

The reference's decorative environment has not been copied into the sprite. Alpha is transparent, candidate edges use binary alpha, and all candidate frames retain the same native dimensions. Original generated artwork remains preserved before packing.

## Verification

| Browser | Art-gallery checks | Exceptions | HTTP(S) requests |
|---|---:|---:|---:|
| Chrome 154 | 53 passed, 0 failed | 0 | 0 |
| Edge 154 | 53 passed, 0 failed | 0 | 0 |

Evidence: [Chrome](tests/chrome-art-results.json), [Edge](tests/edge-art-results.json). Checks ran through actual `file://` URLs with network emulation offline. They cover all 22 current sprite selections, four atlas loads, native dimensions and binary transparency, animation progress/pause/step, labeled turn/death limitations, three backgrounds, camera scale, user review persistence, preservation of draft feedback, unchanged gameplay-save bytes, and overflow at 1440/1024/760/390 pixels. Desktop comparison and aquarium-scale screenshots were inspected.

Reproduce with `python tests/browser_qa.py chrome --art-review` or `python tests/browser_qa.py edge --art-review`. Art packing and PNG validation require developer-side Pillow; playing the game and viewing the gallery require only a browser. `python tests/prepare_art.py` regenerates packed candidates from the preserved source, not new artwork.

Firefox, comprehensive screen-reader/touch behavior and long-session performance remain unverified. Automated rendering checks do not establish artistic approval or biological accuracy. The renderer now maps the assigned atlas to the existing clown ID, including genetic brightness, store thumbnails and individual inspectors. The old procedural sprite is preserved for comparison. Save schema 2 remains compatible; no care, economy or progression systems changed.

## Assignment and remaining work

The user requested the generated artwork for Ocellaris clownfish. It is assigned in gameplay and labeled accordingly in the gallery. The main game passed 68 system checks and 69 browser/UI checks in each of Chrome and Edge, including four distinct PNG frames, file-URL thumbnails, store/inspection artwork and saved identity after reload. Further species art and gameplay development await separate direction.
