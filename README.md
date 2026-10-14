# backdropped

A vibrant event backdrop and signage website with a centred, full-screen process video hero.

## GitHub Pages deployment

The complete static website is in `docs/`. The GitHub Actions workflow deploys that directory when website changes are pushed to `main`, or when manually run from the Actions tab.

Enable GitHub Pages under **Settings → Pages → Source → GitHub Actions**. GitHub Free requires a public repository; private repositories require an eligible paid plan.

The root entry point and relative asset paths support this project site at `https://chyvors8.github.io/chyvors.github.io/` once Pages is enabled.

## Pages

- Home: `docs/index.html`
- What we do: `docs/what-we-do.html`
- Your Occasion: `docs/your-occasion.html`
- About Us: `docs/about-us.html`
- Enquire Now: `docs/lets-talk.html`
- FAQ: `docs/faq.html`
- Theme inspiration: `docs/themes.html`

Shared styles and navigation work at the project URL. The homepage service strip loops left to right, includes a pause control, and becomes static when reduced motion is requested.

## Content notes

The background film is an illustrative 20-second animated montage of AI-generated design, fabrication, installation and finished-backdrop scenes. It is not footage of an actual team or client project. The remaining event image is also an AI-generated concept.

The project enquiry form downloads a brief to the visitor's device. It does not send enquiries. Add real contact details before accepting customer enquiries.

## Occasion and About backgrounds

Built-in image generation created three illustrative scenes: a bright creative studio with sketches and lime/pink/orange/blue backdrop materials; a pastel celebration with arches, balloons, flowers and table styling; and a corporate activation with blue/lime panels, acrylic displays and illuminated signboard shapes. Prompts requested wide editorial photographs without people, logos or readable lettering.

Saved assets: `docs/assets/creative-studio.jpg`, `personal-event-poster.jpg`, `corporate-event-poster.jpg`, `personal-event-loop.mp4` and `corporate-event-loop.mp4` (all in `docs/assets/`). The two 12-second silent H.264 videos animate the generated event scenes with a seamless camera pan; they are illustrative loops, not live event footage. Category switching selects the relevant film. Pause preferences persist when switching; reduced motion uses the poster image.

## Service mockups

Each occasion service card includes its own AI-generated concept photograph. The 12 final optimised images and exact generation prompts are in `docs/assets/mockups/`; see `PROMPTS.md`. These illustrate possible designs rather than completed customer projects.

### Main brand logo
The approved spaced ocean-blue logo is used in the header and footer on all five pages. `docs/brand.css` only handles responsive logo sizing. The original site colours and styling are preserved. The refined logo and its edit prompt are retained in `output/logo/`.

### Enquiry services and FAQ
The enquiry navigation label is Enquire Now. Existing FAQ questions now live on `docs/faq.html`, linked from every page. The form uses singular Personal Event / Corporate Event labels and grouped service checkboxes populated from the same categories as the occasion page. Changing event type replaces the choices and clears selections; selected service details are included in the downloaded project brief. The form still saves locally rather than submitting an enquiry.

### Smooth background films
The website now uses `backdrop-process-smooth.mp4`, `personal-event-loop-smooth.mp4` and `corporate-event-loop-smooth.mp4`. All are silent 20-second 1280×720 H.264 loops at 60 fps with fast-start metadata. Fractional-pixel bicubic sampling avoids stepped crop motion; occasion scenes use a gentle horizontal cycle without vertical drift. The homepage preserves its four process scenes with eased movement and soft crossfades, including the loop boundary. Active videos use automatic preloading, while pause controls and reduced-motion behaviour are retained. Original film assets are kept as source material.

### Singapore theme collection
The personal occasion cards now link to 42 realistic illustrative concepts: 8 baby showers, 10 birthdays (ages 7–80), and 6 each for anniversaries, engagements, weddings and table decorations. The revised image direction uses printed 2D backdrops, flat cutouts and practical creative props across varied Singapore settings and cultural inspirations. The original colour palette is preserved.

`docs/assets/themes/` contains the optimised JPEGs and exact prompts in `PROMPTS.md`; `docs/themes-data.json` is the readable catalogue. Built-in image generation produced the final assets. The galleries support category filters, click-to-enlarge, left-to-right preview reels on hover/focus, explicit mobile motion controls and reduced motion. Each individual theme reel shows the full image and two detail crops of that same concept. Enquiry links carry the chosen theme into the brief.

### Corporate inspiration and project portfolio
Corporate inspiration now uses the same carousel, mobile movement controls, enlarged views and enquiry links as Personal Events. Each of the six categories has five generated concepts plus three authentic examples from the supplied Drive folder. Concept previews and real project photographs are labelled separately. The mixed galleries link to full portfolio collections.

The portfolio reviews all 264 supplied photos, removes 11 exact duplicates, and groups 253 unique project images into 38 collections. It includes service filters, search, individual project galleries, photo navigation, original/enhanced comparison and enquiry links. Source attribution is recorded in `docs/assets/portfolio/SOURCE.md`; corporate prompts are in `docs/assets/corporate-themes/PROMPTS.md`. Installation photos are preserved as originals. Additional service choices derive from photographed exhibition booths, custom retail fixtures, hoarding graphics, wayfinding, standees and print collateral.

Portfolio photo cleanup is documented in `docs/assets/portfolio-enhanced/PROMPTS.md`. The portfolio uses native-resolution AI-retouched previews with original-image comparison; smaller responsive derivatives keep browsing light. Corporate galleries continue to identify generated concepts and authentic photographs separately.

Photo-editing status: 182 of 253 unique images have retouched previews. The remaining 71 retain originals and are listed in `docs/assets/portfolio-enhanced/PENDING.json` for continuation after the image-editing service limit resets.
