## 2025-06-08 - Identifying Unused External Dependencies
**Learning:** In static sites, it's common to find legacy external resource links (CDNs) that are no longer utilized by any elements in the DOM. Removing these reduces the number of HTTP requests and initial CSS/JS parsing time.
**Action:** Always grep for specific classes or identifiers associated with external libraries (like `devicon-` for Devicon) before assuming they are needed.

## 2025-06-08 - Performance Boost via Resource Hints
**Learning:** For static sites with heavy hero assets (like large GIFs) and external fonts, `preconnect` and `preload` are critical for reducing Time to Interactive (TTI) and Largest Contentful Paint (LCP).
**Action:** Implement `preconnect` for font/CDN domains and `preload` for critical above-the-fold assets in future static site optimizations.

## 2025-06-08 - Favoring Preconnect over Brittle Preloads
**Learning:** Preloading specific font assets from external CDNs (like Google Fonts) can be brittle as the hashed filenames may change without notice. `preconnect` provides most of the benefit with none of the maintenance risk.
**Action:** Use `preconnect` for third-party dynamic assets and `preload` only for internal, stable assets.

## 2026-06-09 - Critical Path Optimization: Lazy Fonts and Non-blocking CSS
**Learning:** For multi-lingual static sites, bundling all language-specific fonts into the initial payload significantly degrades FCP and LCP. Dynamically injecting stylesheets for non-primary languages (e.g., JP/CN) reduces the initial critical path. Combining this with the "media=print" trick for non-critical CSS (Font Awesome) further unblocks rendering.
**Action:** Always audit Google Fonts payloads and defer non-primary language families to user interaction or late-load.

## 2026-06-10 - O(1) DOM Updates and Layout Stability
**Learning:** Repetitive DOM lookups and `innerText` updates in hot paths (like language switching) cause significant layout thrashing. Caching elements and using `textContent` can yield a ~30x performance boost in script execution. Additionally, optimizing `IntersectionObserver` callbacks to avoid full nav-link iterations by tracking the active ID ensures smooth scrolling even on low-end devices.
**Action:** Use `Map` for O(1) DOM element lookups in event-driven logic and prefer `textContent` for non-HTML updates.

## 2026-06-11 - Eliminating Massive Library Dependencies for Small Wins
**Learning:** External icon libraries like Font Awesome are convenient but often excessive for small projects. Loading a ~70KB CSS file and multiple font assets just for 4 icons is a major performance bottleneck in terms of both payload size and HTTP requests.
**Action:** Replace external icon libraries with optimized inline SVGs. Use `fill: currentColor` on SVGs to maintain styling flexibility through CSS `color` properties.

## 2026-08-06 - Eliminating Render-Blocking Google Fonts stylesheets
**Learning:** Standard `<link rel="stylesheet">` tags for web fonts block page rendering while fetching the CSS from the server, causing higher First Contentful Paint times. Loading the primary font asynchronously with `media="print" onload="this.media='all'"` completely unblocks the critical rendering path, using standard browser fallback fonts during the brief fetching phase (with `display=swap`).
**Action:** Always load critical but non-layout-critical third-party stylesheets using the non-blocking media toggle method with a `<noscript>` fallback.

## 2026-08-11 - High-Value LCP Optimization via Hero Asset Compression
**Learning:** Rendering full-resolution (750x343), 70-frame animated GIFs for a hero display box that is explicitly constrained to 160px width in CSS is a major layout-rendering and bandwidth bottleneck. Halving the image dimensions, skipping alternate frames, converting to an adaptive color palette, and doubling frame duration reduces size from 4.01MB to 643KB (~84% savings) while keeping the visual speed and rendering quality indistinguishable.
**Action:** Always audit above-the-fold media/GIF sizes against their actual CSS viewport dimensions, optimize palette color depth, and drop redundant animation frames to maximize LCP.
