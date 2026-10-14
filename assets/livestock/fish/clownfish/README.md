# Dedicated clownfish collection

31 catalogued scientific names and 25 designer phenotypes linked to base species. Sources and uncertainty are recorded in collection.json. All generated source PNGs and prompts are preserved. Sources are not silently approved. See the offline clownfish-review.html gallery and CLOWNFISH_STORE_REPORT.md.

Species atlases have twelve 192×160 frames: eight Egg/Baby/Juvenile/Adult alive/dead poses and four adult swim frames. Designer atlases have eight frames: juvenile/adult alive/dead plus four swim frames; egg/baby alive/dead explicitly resolve to the base species. JSON metadata records frame mapping, native direction, eyes, anchor, bounds and approval status. Native source facing is normalized only during frame loading. Existing approved Ocellaris adult art remains assigned to its original runtime ID.

Engineering-only packer: tests/pack_clownfish_art.py. Catalog/brief builder: tests/prepare_clownfish_collection.py. Browser review checks: tests/clownfish_qa.py and clownfish_checks.js. Diagnostic contact composition: clownfish_contacts.py. Re-running catalog scaffolding must never remove preserved source files or regenerate art without authorization.
