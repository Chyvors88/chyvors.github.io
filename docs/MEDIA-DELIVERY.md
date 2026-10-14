# Mobile media delivery

Display previews use 480px and 960px WebP variants at quality 82. Original project photographs, retouched originals, and full-size theme images remain unchanged and are used in enlarged viewers. On browsers that cannot decode a preview, the gallery falls back to its source image.

The 523 source images have 958 mappings (including existing thumbnail aliases). The median 480px preview is 92% smaller than its source file. The main logo's delivery file is 15,984 bytes, compared with the 1,451,987-byte original.

Brand tiles use small native images with eager loading, including inside the expandable section. Photo lettering frames and supplied logo whitespace are exported to match their existing visible presentation. This avoids full project photo downloads and nested SVG image loading on the homepage. Original supplied logos are retained in `assets/client-logos`.

Mobile background loops are H.264 at 720px wide and 30fps, with fast-start metadata. They retain the existing 20-second edits, smooth movement and loop transitions. Desktop keeps the original 1280px/60fps loops. The browser selects one source before downloading; the occasion page does not preload the unused personal video when opened in Corporate mode. Posters display while videos load, and autoplay respects data-saving preferences.

Theme conveyors load images near the visible part of each reel, rather than every offscreen slide. Gallery thumbnails never select the full-resolution viewing file.

Validation: all 34 homepage logo images loaded in a 390px viewport; no horizontal overflow; mobile homepage and corporate page selected the mobile videos; corporate previews displayed on scroll; portfolio previews selected WebP assets while the enlarged viewer selected the unchanged full-quality JPEG. Local asset references and JavaScript syntax passed.

Asset export utility: `scripts/optimize-web-media.py` (requires Pillow). Video variants were encoded using the existing local FFmpeg runtime.
