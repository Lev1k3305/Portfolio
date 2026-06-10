## 2025-05-15 - Responsive Typing Animations
**Learning:** In Cyberpunk-themed designs, typing animations often rely on `white-space: nowrap` to maintain the effect. This causes horizontal overflow on mobile devices.
**Action:** Use a media query for small screens (< 768px) to set `white-space: normal` and disable the animation to prioritize readability and layout stability over the visual effect.

## 2025-05-15 - Localized AJAX Feedback
**Learning:** For multi-lingual sites, AJAX feedback (like form submission states) must be localized. Hardcoding feedback strings in JS breaks the localized experience.
**Action:** Store feedback strings in the central `translations` object and use a global `currentLang` tracker (updated by the language switcher) to retrieve the correct localized string during async operations.
