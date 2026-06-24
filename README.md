# McGeer Kitchens — Self-Hosted Static Clone

A 100% self-hosted static clone of <https://mcgeerkitchens-alberton.co.za/>,
transcribed directly from the fully-rendered DOM of each page. The rendered
HTML is the source of truth — pages were not reconstructed from screenshots
or simplified. One output page per input render, with the original folder
structure preserved.

## What's here

| Path | Contents |
|------|----------|
| `*.html` (13 files) | One static page per captured route |
| `wp-content/` | Theme/plugin CSS, uploaded images, local fonts (mirrored at original paths) |
| `wp-includes/` | WordPress CSS assets |
| `fonts.googleapis.com/`, `fonts.gstatic.com/` | Self-hosted Google Fonts (Roboto) + font files |
| `build_clone.py` | Phase 1 — downloads & mirrors every asset (recurses into CSS `url()`/`@import`) |
| `rewrite_html.py` | Phase 2 — strips hydration/tracking, rewrites refs to local paths |

### Pages

`index.html`, `about-us.html`, `contact-us.html`, `our-work.html`,
`our-process.html`, `our-projects.html`, `products.html`, `kitchens.html`,
`built-in-cupboards.html`, `vanities.html`, `virtual-showroom.html`,
`privacy-policy.html`, `terms-and-conditions.html`.

## What was done per page

1. **Stripped the framework hydration** — removed every `<script>` (the
   WordPress/Elementor/jQuery runtime plus Google Tag Manager, gtag, Google
   Ads/DoubleClick, and reCAPTCHA). The captured DOM is already fully
   rendered, so desktop layout stays pixel-faithful without any JS. Also
   removed the `<base href>`, third-party `dns-prefetch`/`preconnect` hints,
   the invisible reCAPTCHA iframes/badge, and dead WordPress endpoint
   `<link>`s (RSS/oEmbed/REST/RSD/xmlrpc).
2. **Self-hosted every asset** — all CSS, images (incl. `srcset` and inline
   `background-image`), favicons, and fonts were downloaded and mirrored at
   their original paths. CSS files were parsed recursively so their
   `url()`/`@import` dependencies (fonts, sprites) are local too. Google
   Fonts CSS and the `fonts.gstatic.com` font files it references are
   self-hosted as well.
3. **Relinked navigation** — internal links between the 13 captured routes
   now point to the local `.html` files.

After the build, all **1,492 local references across HTML and CSS resolve**
(0 missing) and there are **0 externally auto-loaded assets**.

## Intentionally left as external links (not assets)

These are not loaded automatically; they are genuine outbound content:

- Social profile links (Facebook, Instagram, LinkedIn, YouTube)
- A single Google Maps embed on the contact page (a live map cannot be
  self-hosted; it remains an `<iframe>`)
- Microdata / namespace URLs (`schema.org`, `w3.org`, `gmpg.org`) — metadata,
  never fetched

## Viewing

Open any `.html` file directly in a browser, e.g.:

```
xdg-open index.html
```

No web server is required — all asset references are document-relative.

## Reproducing

```
# expects the rendered-DOM export in ./_source
python3 build_clone.py     # mirror assets
python3 rewrite_html.py    # transcribe + rewrite pages
```
