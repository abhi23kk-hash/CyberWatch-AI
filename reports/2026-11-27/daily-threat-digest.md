# Cybersecurity Daily Intelligence Digest

Generated: 2026-11-27 22:49 UTC
Records included: 35

## Data Sources

- National Vulnerability Database (NVD)
- CISA Known Exploited Vulnerabilities (KEV)

## AI Analyst Summary

Gemini AI analysis was unavailable. The collected vulnerability records are retained below for manual review.

## Vulnerability Findings

### CVE-2026-107942 — LOW (CVSS: 3.1)

- Published: 2026-11-20T23:16:57.537
- Description: Improper Content Security Policy (CSP) nonce implementation in HCL BigFix MCM allows a remote attacker to reduce the effectiveness of the Content Security Policy protection mechanism via an orphaned nonce value in the style-src directive of the CSP header without a corresponding nonce attribute on any <style> or <script> element.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-107942

### CVE-2026-124213 — Unknown (CVSS: N/A)

- Published: 2026-11-20T23:16:57.877
- Description: Rejected reason: ** REJECT ** DO NOT USE THIS CANDIDATE NUMBER. ConsultIDs: CVE-2026-125822. Reason: This candidate is a reservation duplicate of CVE-2026-125822. Notes: All CVE users should reference CVE-2026-125822 instead of this candidate. All references and descriptions in this candidate have been removed to prevent accidental usage.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-124213

### CVE-2026-134163 — MEDIUM (CVSS: 6.9)

- Published: 2026-11-20T23:16:57.960
- Description: probe-image-size 7.4.0 contains a regular expression denial of service vulnerability in lib/common/svg_header.js that allows remote unauthenticated attackers to block the event loop via crafted SVG doctypes. Attackers can supply SVGs with an unclosed internal subset followed by many ']' characters to trigger quadratic backtracking in probe.sync, probe(stream) or probe(url), causing repeated event loop stalls.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134163

### CVE-2026-134164 — HIGH (CVSS: 8.7)

- Published: 2026-11-20T23:16:58.120
- Description: probe-image-size before 7.5.0 contains an algorithmic-complexity denial of service vulnerability in lib/exif_utils.js that allows remote unauthenticated attackers to exhaust CPU by supplying self-referencing EXIF IFDs. Attackers can submit a crafted 9.6 KB JPEG with repeated ExifIFD and InteropIFD pointers to block the Node.js event loop for about 23 seconds.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134164

### CVE-2026-134165 — MEDIUM (CVSS: 6.9)

- Published: 2026-11-20T23:16:58.263
- Description: probe-image-size before 7.5.0 contains an unbounded memory allocation vulnerability in lib/parse_stream/avif.js that allows remote attackers to exhaust memory via attacker-declared ftyp or meta box sizes. Attackers can supply an AVIF stream or URL to probe(url) or probe(stream) declaring a huge box length, forcing the parser to buffer all received bytes and causing denial of service.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134165

### CVE-2026-134166 — MEDIUM (CVSS: 6.9)

- Published: 2026-11-20T23:16:58.413
- Description: probe-image-size before 7.5.0 contains an unbounded memory buffering vulnerability in parseExif in lib/parse_stream/webp.js that allows remote attackers to exhaust memory via an attacker-declared EXIF chunk length. Attackers can supply a WebP stream or URL to probe(url) or probe(stream) declaring a huge EXIF length after VP8X, causing unbounded buffering and process memory exhaustion.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134166

### CVE-2026-134167 — HIGH (CVSS: 8.7)

- Published: 2026-11-20T23:16:58.563
- Description: devpi-web before 5.2.0 contains an unauthenticated path traversal vulnerability in the +doc documentation route because docs_file_exists and docs_file_path in doczip.py never confine relpath to the documentation directory. Attackers can request a relpath with a leading // or percent-encoded .. segments to read server files, including the keyfs sqlite database holding password hashes.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134167

### CVE-2026-134168 — MEDIUM (CVSS: 5.3)

- Published: 2026-11-20T23:16:58.720
- Description: devpi-server before 6.21.0 contains a path traversal vulnerability that allows authenticated users to write files outside the +files storage root by naming a user and index '..'. Attackers can self-register a '..' user, create a '..' index, and upload release files with attacker-chosen filenames and contents into a parent of the server directory.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134168

### CVE-2026-134169 — HIGH (CVSS: 8.7)

- Published: 2026-11-20T23:16:58.873
- Description: Qwik City before 1.20.3 (@builder.io/qwik-city) and @qwik.dev/router before 2.0.0-rc.4 contain an improperly controlled object modification vulnerability in formToObj that allows unauthenticated attackers to overwrite built-in function properties. Attackers can send a form POST with nested field names traversing inherited members of string values, breaking Object.prototype.hasOwnProperty.call process-wide until server restart.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134169

### CVE-2026-134170 — HIGH (CVSS: 8.2)

- Published: 2026-11-20T23:16:59.037
- Description: Cesanta Mongoose 7.22 before 7.24 with the built-in TLS stack contains an out-of-bounds read in mg_timegm() that allows remote attackers to crash the process via crafted X.509 certificate validity months. Attackers can present a certificate with month '00' or out-of-range values during the handshake, before signature verification, causing an unchecked dm array index and denial of service.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134170

### CVE-2026-134171 — MEDIUM (CVSS: 6.9)

- Published: 2026-11-20T23:16:59.247
- Description: Cesanta Mongoose 7.21 before 7.24 contains an out-of-bounds read vulnerability in rx_ip6() checksum validation that allows remote unauthenticated attackers to read past received packets by sending IPv6 extension headers. Attackers can send a single IPv6 TCP or ICMPv6 packet with extension headers, causing tcp6csum_ok() and icmp6csum_ok() to use the full payload length and read adjacent receive-buffer memory.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134171

### CVE-2026-134172 — HIGH (CVSS: 8.5)

- Published: 2026-11-20T23:16:59.420
- Description: audio-separator before 0.47.2 contains an insecure deserialization vulnerability that allows attackers to execute code by supplying malicious Demucs .th model files loaded via torch.load with weights_only=False. Local users writing to the shared /tmp/audio-separator-models/ default directory, or attackers controlling unverified model download sources, can execute code when victims run Demucs separation.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134172

### CVE-2026-16132 — MEDIUM (CVSS: 5.1)

- Published: 2026-11-20T23:16:59.577
- Description: A stored cross-site scripting (XSS) vulnerability exists in the Icon API: Menu submodule of the Drupal 7 Icon API module. When a menu item is configured with the Title Wrapper option enabled, the value of the Title Wrapper Class field is output directly into an HTML attribute without sanitization or escaping. A user with the "administer menu icons" permission can inject a payload such as `title" onmouseover="alert(document.cookie)` that is rendered verbatim on every page displaying the affected menu item, executing arbitrary JavaScript in the browser of any user who interacts with the menu link. This can lead to session theft, account hijacking, and further attacks against site users.

This issue affects Icon API 7.1.0.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-16132

### CVE-2026-19030 — MEDIUM (CVSS: 6.9)

- Published: 2026-11-20T23:16:59.727
- Description: Observable Discrepancy vulnerability in Drupal CAPTCHA for Drupal 7 allows unauthenticated attackers to test login credentials despite CAPTCHA protection.

When CAPTCHA is enabled on Drupal login forms, normal form validation can still run after a missing or incorrect CAPTCHA response. This may expose credential validation feedback and allow an attacker to distinguish invalid credentials from valid credentials paired with a failed CAPTCHA.



This issue affects CAPTCHA for Drupal 7: from 7.x-1.0 through 7.x-1.7.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-19030

### CVE-2026-79790 — Unknown (CVSS: N/A)

- Published: 2026-11-20T23:16:59.900
- Description: Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-79790

### CVE-2026-112465 — HIGH (CVSS: 7.5)

- Published: 2026-11-21T00:17:43.960
- Description: An out-of-bounds read was addressed with improved bounds checking. This issue is fixed in iOS 27.2 and iPadOS 27.2, macOS Golden Gate 27.2, tvOS 27.2, visionOS 27.2. An app may be able to cause unexpected system termination or read kernel memory.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-112465

### CVE-2026-112603 — HIGH (CVSS: 7.8)

- Published: 2026-11-21T00:17:44.323
- Description: A logic issue was addressed with improved checks. This issue is fixed in Xcode 27.2. An app may be able to gain root privileges.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-112603

### CVE-2026-112662 — MEDIUM (CVSS: 4.7)

- Published: 2026-11-21T00:17:44.447
- Description: A race condition was addressed with additional validation. This issue is fixed in iOS 27.2 and iPadOS 27.2. An app may be able to access sensitive user data.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-112662

### CVE-2026-113953 — HIGH (CVSS: 7.8)

- Published: 2026-11-21T00:17:44.570
- Description: An integer overflow was addressed with improved input validation. This issue is fixed in iOS 27.2 and iPadOS 27.2, macOS Golden Gate 27.2, macOS Sequoia 15.8.2, macOS Tahoe 26.7.2, tvOS 27.2, visionOS 27.2. Processing a maliciously crafted USD file may lead to unexpected app termination.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-113953

### CVE-2026-113954 — HIGH (CVSS: 7.8)

- Published: 2026-11-21T00:17:44.697
- Description: A use-after-free issue was addressed with improved memory management. This issue is fixed in iOS 27.2 and iPadOS 27.2. Processing a maliciously crafted file may lead to unexpected app termination.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-113954

### CVE-2026-113955 — MEDIUM (CVSS: 6.5)

- Published: 2026-11-21T00:17:44.820
- Description: A cross-origin issue was addressed with improved tracking of security origins. This issue is fixed in iOS 26.7.2 and iPadOS 26.7.2. Processing maliciously crafted web content may disclose sensitive user information.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-113955

### CVE-2026-114021 — CRITICAL (CVSS: 9.8)

- Published: 2026-11-21T00:17:44.940
- Description: An out-of-bounds write issue was addressed with improved bounds checking. This issue is fixed in macOS Golden Gate 27.2, macOS Sequoia 15.8.2, macOS Tahoe 26.7.2. Connecting to a malicious NFS server may lead to kernel memory corruption.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-114021

### CVE-2026-114022 — CRITICAL (CVSS: 9.8)

- Published: 2026-11-21T00:17:45.057
- Description: An out-of-bounds write issue was addressed with improved bounds checking. This issue is fixed in macOS Sequoia 15.8.2, macOS Tahoe 26.7.2. An app may be able to cause unexpected system termination.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-114022

### CVE-2026-114023 — HIGH (CVSS: 8.8)

- Published: 2026-11-21T00:17:45.177
- Description: A path handling issue was addressed with improved validation. This issue is fixed in macOS Golden Gate 27.2, macOS Sequoia 15.8.2, macOS Tahoe 26.7.2. Processing web content may lead to arbitrary code execution.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-114023

### CVE-2026-114024 — MEDIUM (CVSS: 5.5)

- Published: 2026-11-21T00:17:45.300
- Description: This issue was addressed with improved checks. This issue is fixed in iOS 27.2 and iPadOS 27.2, macOS Golden Gate 27.2, visionOS 27.2, watchOS 27.2. An app may be able to access sensitive user data.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-114024

### CVE-2026-114025 — HIGH (CVSS: 7.8)

- Published: 2026-11-21T00:17:45.423
- Description: An out-of-bounds write was addressed with improved input validation. This issue is fixed in iOS 26.7.2 and iPadOS 26.7.2, iOS 27.2 and iPadOS 27.2, macOS Golden Gate 27.2, macOS Sequoia 15.8.2, macOS Tahoe 26.7.2, tvOS 27.2. A user may be able to cause unexpected app termination or arbitrary code execution.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-114025

### CVE-2026-114026 — MEDIUM (CVSS: 5.5)

- Published: 2026-11-21T00:17:45.550
- Description: An out-of-bounds read was addressed with improved bounds checking. This issue is fixed in iOS 27.2 and iPadOS 27.2, macOS Golden Gate 27.2, tvOS 27.2, visionOS 27.2, watchOS 27.2. Processing a maliciously crafted font may result in the disclosure of process memory.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-114026

### CVE-2026-132475 — CRITICAL (CVSS: 9.8)

- Published: 2026-11-21T00:17:45.870
- Description: An out-of-bounds write issue was addressed with improved bounds checking. This issue is fixed in macOS Golden Gate 27.2. An app may be able to cause unexpected system termination or corrupt kernel memory.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132475

### CVE-2026-131651 — MEDIUM (CVSS: 6.4)

- Published: 2026-11-21T04:17:20.330
- Description: The rtMedia for WordPress, BuddyPress and bbPress plugin for WordPress is vulnerable to Stored DOM-Based Cross-Site Scripting via the 'media_title' parameter in all versions up to, and including, 4.7.18 due to insufficient input sanitization and output escaping. This makes it possible for authenticated attackers, with subscriber-level access and above, to inject arbitrary web scripts in pages that will execute whenever a user accesses an injected page. The vulnerability is only triggerable via the Backbone.js-rendered "Load More" pagination path; the server-side PHP gallery rendering correctly escapes media_title with esc_attr() and is not affected.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-131651

### CVE-2026-19793 — HIGH (CVSS: 8.8)

- Published: 2026-11-21T04:17:20.800
- Description: The WP Import Export Lite plugin for WordPress is vulnerable to Limited Code Injection in all versions up to, and including, 3.9.32 via the 'comment' parameter. This is due to a two-stage shortcode check that evaluates the raw mapping placeholder before data substitution, causing the neutralizer to be skipped when attacker-controlled comment content containing a malicious [wpie_function] shortcode is substituted at runtime. This makes it possible for unauthenticated attackers to inject arbitrary PHP callables on the server. Exploitation requires an Administrator to perform the standard Export With Settings For Import followed by a New Import migration workflow, which is a routine operational task; the attacker themselves requires no account or authentication, needing only the ability to submit a pending comment on any comments-open post.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-19793

### CVE-2026-133958 — MEDIUM (CVSS: 5.5)

- Published: 2026-11-21T05:18:22.503
- Description: A flaw was found in Quay. Insufficient validation of repository notification webhook URLs allows an authenticated administrator to trigger Server-Side Request Forgery (SSRF). By specifying an internal URL or a redirect to an internal destination, an attacker can force the Quay worker to issue unauthorized HTTP requests to internal network locations and cloud metadata services.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133958

### CVE-2026-111067 — HIGH (CVSS: 7.1)

- Published: 2026-11-21T06:16:31.253
- Description: The UpdraftPlus: WP Backup & Migration Plugin WordPress plugin before 1.26.10, UpdraftPlus: WP Backup & Migration Plugin WordPress plugin before 2.26.10.26 does not guard all execution paths of its database restore process against second-order SQL injection, allowing a Subscriber-level user who has stored crafted content in their own account to escalate to administrator when an administrator later restores a backup.
This is due to an incomplete fix of CVE-2026-108761 in 1.26.9: the fix guards only one of the restore routine's execution paths, and a second path remains exploitable.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-111067

### CVE-2026-111975 — MEDIUM (CVSS: 5.3)

- Published: 2026-11-21T06:16:32.293
- Description: The GiveWP  WordPress plugin before 4.19.2.1 does not exclude donors who chose to give anonymously from one of its public REST API listings, allowing unauthenticated users to retrieve those donors' names.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-111975

### CVE-2026-114434 — HIGH (CVSS: 7.5)

- Published: 2026-11-21T06:16:32.417
- Description: The Video Conferencing with Zoom WordPress plugin before 4.7.0 does not check that the requester is authorized to join a meeting before issuing a Zoom Meeting SDK signature for it, allowing unauthenticated users to obtain a valid signed join credential for an arbitrary meeting.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-114434

### CVE-2026-114435 — MEDIUM (CVSS: 5.3)

- Published: 2026-11-21T06:16:32.520
- Description: The Video Conferencing with Zoom WordPress plugin before 4.7.0 does not check authorization, or whether a meeting is restricted to logged-in users, password-protected or unpublished, before returning a meeting's join links, allowing unauthenticated users to obtain the passcode-embedded join links of any meeting, including meetings the site restricts.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-114435
