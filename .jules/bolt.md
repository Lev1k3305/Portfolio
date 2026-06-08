## 2025-06-08 - Identifying Unused External Dependencies
**Learning:** In static sites, it's common to find legacy external resource links (CDNs) that are no longer utilized by any elements in the DOM. Removing these reduces the number of HTTP requests and initial CSS/JS parsing time.
**Action:** Always grep for specific classes or identifiers associated with external libraries (like `devicon-` for Devicon) before assuming they are needed.

## 2025-06-08 - Performance Boost via Resource Hints
**Learning:** For static sites with heavy hero assets (like large GIFs) and external fonts, `preconnect` and `preload` are critical for reducing Time to Interactive (TTI) and Largest Contentful Paint (LCP).
**Action:** Implement `preconnect` for font/CDN domains and `preload` for critical above-the-fold assets in future static site optimizations.

## 2025-06-08 - Favoring Preconnect over Brittle Preloads
**Learning:** Preloading specific font assets from external CDNs (like Google Fonts) can be brittle as the hashed filenames may change without notice. `preconnect` provides most of the benefit with none of the maintenance risk.
**Action:** Use `preconnect` for third-party dynamic assets and `preload` only for internal, stable assets.
