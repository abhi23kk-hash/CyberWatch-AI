# CyberWatch

Defensive cybersecurity intelligence automation using the NVD CVE API and CISA Known Exploited Vulnerabilities (KEV) catalog.

## Five tasks
- `cve`: recent CVE discovery
- `critical`: high/critical CVEs
- `kev`: CISA known exploited vulnerabilities
- `ransomware`: KEVs marked as used in ransomware campaigns
- `digest`: daily vulnerability digest

Add `GEMINI_API_KEY` as a GitHub Actions secret for optional AI analysis. Add `NVD_API_KEY` optionally to increase NVD request limits.

Sources:
- https://nvd.nist.gov/developers/vulnerabilities
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
