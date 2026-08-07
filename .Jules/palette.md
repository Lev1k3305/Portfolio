## 2026-06-11 - AJAX Form Feedback and Multi-lingual State
**Learning:** Implementing AJAX submission for forms in multi-lingual static sites requires maintaining a global language state to provide localized feedback (e.g., "Sending...", "Success") without a page reload. This prevents jarring redirects to external service pages (like Formspree) and keeps the user within the immersive "DEDSEC" terminal experience.
**Action:** Always track the active locale in a global variable and include success/error/loading keys in the translation manifest for all form interactions.

## 2026-06-11 - Visual Cues for "System Status"
**Learning:** In a terminal/cyberpunk themed UI, text-based status indicators (e.g., "[ STATUS: ONLINE ]") are more effective and "delightful" when accompanied by a pulsing visual element (like a green neon dot). This provides immediate pre-attentive confirmation of status.
**Action:** Pair critical status text with a simple CSS-animated pulsing dot to enhance the "living system" aesthetic.

## 2026-06-12 - Dynamic Multi-Lingual Character and Byte Limits
**Learning:** Providing real-time, localized character or byte counters for form inputs improves UX and accessibility (with aria-live) by preventing frustration from hitting invisible form limit thresholds. To avoid layout shifts and mixed-language rendering, the counter should be initialized immediately on DOM content load according to the active locale, rather than waiting for first user input.
**Action:** Bind real-time input counters to both textarea listeners and language-switching events, initializing the localized counter state immediately on page load.
