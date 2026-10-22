# Cutout revision

Built-in imagegen edit, preserved original and revised outputs.

Use case: background-extraction. Remove ALL background gradients, atmosphere, glow, shadows and colored rectangles from this 2-by-2 sprite atlas. Make every pixel outside the four animal/rock silhouettes fully alpha-transparent, including gaps between fins/spines and the rock arch opening. Preserve the four subjects exactly: same positions, pixel colors, eyes, body details, fin/tail shapes, frame grid and canvas size. No new backdrop, no checkerboard painted into the image, no shadows. Output an actual RGBA transparent PNG with opaque subject interiors and clean crisp pixel-art edges. This must be a sprite cutout usable over any aquarium background.
