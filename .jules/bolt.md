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
