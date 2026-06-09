## 2025-05-15 - [Initial UX Assessment]
**Learning:** The contact form currently causes a full page redirect upon submission, which breaks the immersive Cyberpunk single-page experience. Additionally, language selector buttons use a CSS class for active state but lack semantic ARIA attributes to signal this to screen readers.
**Action:** Implement AJAX form submission with inline success feedback and add `aria-pressed` to language buttons for better accessibility.
