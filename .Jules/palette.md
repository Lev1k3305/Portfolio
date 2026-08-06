## 2026-06-11 - AJAX Form Feedback and Multi-lingual State
**Learning:** Implementing AJAX submission for forms in multi-lingual static sites requires maintaining a global language state to provide localized feedback (e.g., "Sending...", "Success") without a page reload. This prevents jarring redirects to external service pages (like Formspree) and keeps the user within the immersive "DEDSEC" terminal experience.
**Action:** Always track the active locale in a global variable and include success/error/loading keys in the translation manifest for all form interactions.

## 2026-06-11 - Visual Cues for "System Status"
**Learning:** In a terminal/cyberpunk themed UI, text-based status indicators (e.g., "[ STATUS: ONLINE ]") are more effective and "delightful" when accompanied by a pulsing visual element (like a green neon dot). This provides immediate pre-attentive confirmation of status.
**Action:** Pair critical status text with a simple CSS-animated pulsing dot to enhance the "living system" aesthetic.

## 2026-08-06 - Localized Cyber-Themed Input Character Limits
**Learning:** Adding input character counters in multi-lingual cyberpunk portfolios enhances UX by preventing input truncation during form submission while preserving the digital terminal immersion (e.g. labeling length as "BYTES" or "БАЙТ" instead of "characters"). Real-time JS updates must sync with the language switching dictionary to avoid jarring mixed-language UI states.
**Action:** Always include localization keys for dynamic feedback placeholders (like counters or labels) and register inputs to trigger updates when the active locale changes.
