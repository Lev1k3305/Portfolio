## 2026-08-08 - Reverse Tabnabbing and Missing Content Security Policy
**Vulnerability:** External links with `target="_blank"` without `rel="noopener noreferrer"` (Reverse Tabnabbing), and the complete absence of a Content Security Policy (CSP) leaving the site open to potential script/style injection or data exfiltration.
**Learning:** Even simple static portfolios must follow defense-in-depth principles. Vulnerable external links can allow a newly opened tab to redirect the original portfolio tab to a malicious site. Lack of CSP makes it easier to execute unauthorized scripts if any HTML injection occurs.
**Prevention:** Always use `rel="noopener" rel="noreferrer"` for external `target="_blank"` links and configure a strict, tailored Content Security Policy (CSP) meta tag.
