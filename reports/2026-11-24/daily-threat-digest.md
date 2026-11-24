# Cybersecurity Daily Intelligence Digest

Generated: 2026-11-24 23:34 UTC
Records included: 35

## Data Sources

- National Vulnerability Database (NVD)
- CISA Known Exploited Vulnerabilities (KEV)

## AI Analyst Summary

Gemini AI analysis was unavailable. The collected vulnerability records are retained below for manual review.

## Vulnerability Findings

### CVE-2026-118630 — HIGH (CVSS: 8.8)

- Published: 2026-11-18T00:18:36.207
- Description: Winmate HotTab Exposed Dangerous Function Local Privilege Escalation Vulnerability. This vulnerability allows local attackers to escalate privileges on affected installations of Winmate devices. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability.

The specific flaw exists within the HotTab driver. The issue results from an exposed dangerous function. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel. Was ZDI-CAN-29948.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-118630

### CVE-2026-126962 — HIGH (CVSS: 8.8)

- Published: 2026-11-18T00:18:36.357
- Description: open62541 Subscription Use-After-Free Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of open62541. Authentication is required to exploit this vulnerability.

The specific flaw exists within the handling of subscriptions. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the service account. Was ZDI-CAN-30231.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126962

### CVE-2026-126963 — HIGH (CVSS: 7.5)

- Published: 2026-11-18T00:18:36.483
- Description: Hinemos Agent Improper Certificate Validation Remote Code Execution Vulnerability. This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Hinemos Agent. Authentication is not required to exploit this vulnerability.

The specific flaw exists within the Hinemos Agent service. The issue results from the lack of proper validation of the certificate presented by a server. An attacker can leverage this vulnerability to execute code in the context of the service account. Was ZDI-CAN-28837.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126963

### CVE-2026-126964 — MEDIUM (CVSS: 5.5)

- Published: 2026-11-18T00:18:36.617
- Description: ATEN eco DC fwDeletes.json Directory Traversal Arbitrary File Deletion Vulnerability. This vulnerability allows remote attackers to delete arbitrary files on affected installations of ATEN eco DC. Authentication is required to exploit this vulnerability.

The specific flaw exists within the handling of JSON request data supplied to the fwDeletes.json endpoint. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete files in the context of SYSTEM. Was ZDI-CAN-28621.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126964

### CVE-2026-126965 — LOW (CVSS: 2.7)

- Published: 2026-11-18T00:18:36.743
- Description: ATEN eco DC chartDefine SQL Injection Information Disclosure Vulnerability. This vulnerability allows remote attackers to disclose sensitive information on affected installations of ATEN eco DC. Authentication is required to exploit this vulnerability.

The specific flaw exists within the handling of color references when creating charts. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise. Was ZDI-CAN-29124.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126965

### CVE-2026-126966 — HIGH (CVSS: 8.8)

- Published: 2026-11-18T00:18:36.867
- Description: SmarterTools SmarterMail Missing Authorization Privilege Escalation Vulnerability. This vulnerability allows remote attackers to escalate privileges on affected installations of SmarterTools SmarterMail. Authentication is required to exploit this vulnerability.

The specific flaw exists within the svcDomainAdmin.asmx endpoint. The issue results from the lack of authorization prior to allowing access to functionality. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user. Was ZDI-CAN-33566.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126966

### CVE-2026-126967 — HIGH (CVSS: 8.8)

- Published: 2026-11-18T00:18:36.993
- Description: SmarterTools SmarterMail File Edit API Directory Traversal Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of SmarterTools SmarterMail. Authentication is required to exploit this vulnerability.

The specific flaw exists within the FileStorageController class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM. Was ZDI-CAN-30742.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126967

### CVE-2026-126968 — MEDIUM (CVSS: 6.5)

- Published: 2026-11-18T00:18:37.130
- Description: SmarterTools SmarterMail Missing Authorization Information Disclosure Vulnerability. This vulnerability allows remote attackers to disclose sensitive information on affected installations of SmarterTools SmarterMail. Authentication is required to exploit this vulnerability.

The specific flaw exists within the handling of email attachments. The issue results from the lack of authorization prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose sensitive information in the context of a target user. Was ZDI-CAN-33567.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126968

### CVE-2026-126969 — CRITICAL (CVSS: 9.1)

- Published: 2026-11-18T00:18:37.280
- Description: SmarterTools SmarterMail Insufficient Entropy Authentication Bypass Vulnerability. This vulnerability allows remote attackers to bypass authentication on affected installations of SmarterTools SmarterMail. Authentication is not required to exploit this vulnerability.

The specific flaw exists within the generation of Application Passwords. The issue results from using insufficient entropy in the generation of credentials. An attacker can leverage this vulnerability to bypass authentication on the system. Was ZDI-CAN-33568.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126969

### CVE-2026-126970 — HIGH (CVSS: 7.8)

- Published: 2026-11-18T00:18:37.417
- Description: KiCad Altium SCHLIB File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of KiCad. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file.

The specific flaw exists within the parsing of SCHLIB files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current process. Was ZDI-CAN-33213.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126970

### CVE-2026-126971 — HIGH (CVSS: 7.8)

- Published: 2026-11-18T00:18:37.570
- Description: KiCad Project Archive File Handling Directory Traversal Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of KiCad. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file.

The specific flaw exists within the handling of project archive files. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current user. Was ZDI-CAN-33212.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126971

### CVE-2026-126972 — HIGH (CVSS: 7.8)

- Published: 2026-11-18T00:18:37.690
- Description: KiCad Plugin Directory Traversal Remote Code Execution   Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of KiCad. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file.

The specific flaw exists within the handling of plugin packages. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current user. Was ZDI-CAN-33085.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126972

### CVE-2026-126973 — HIGH (CVSS: 7.8)

- Published: 2026-11-18T00:18:37.807
- Description: KDE Gwenview PNG File Parsing Integer Overflow Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of KDE Gwenview. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file.

The specific flaw exists within the parsing of PNG files. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of the current process. Was ZDI-CAN-29373.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126973

### CVE-2026-126974 — HIGH (CVSS: 7.8)

- Published: 2026-11-18T00:18:37.943
- Description: llama.cpp GGUF File Parsing Integer Overflow Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of llama.cpp. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file.

The specific flaw exists within the parsing of GGUF files. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before writing to memory. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current process. Was ZDI-CAN-34553.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126974

### CVE-2026-126975 — HIGH (CVSS: 7.8)

- Published: 2026-11-18T00:18:38.080
- Description: llama.cpp GGUF File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of llama.cpp. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file.

The specific flaw exists within the parsing of GGUF files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current process. Was ZDI-CAN-34558.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126975

### CVE-2026-126976 — HIGH (CVSS: 7.0)

- Published: 2026-11-18T00:18:38.210
- Description: llama.cpp MTMD Multimodal GGUF File Parsing Integer Overflow Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of llama.cpp. User interaction is required to exploit this vulnerability in that the target must open a malicious file.

The specific flaw exists within the parsing of audio multimodal projector GGUF files. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current process. Was ZDI-CAN-30980.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126976

### CVE-2026-126977 — HIGH (CVSS: 8.1)

- Published: 2026-11-18T00:18:38.347
- Description: Philips Hue Bridge HomeKit Pair-Setup Default Password Authentication Bypass Vulnerability. This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Philips Hue Bridge. Authentication is not required to exploit this vulnerability.

The specific flaw exists within the HomeKit Authentication service, which listens on TCP port 8080 by default. Crafted data in a pairing request can cause the device to allow authentication using a blank password. An attacker can leverage this vulnerability to bypass authentication on the system. Was ZDI-CAN-28323.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126977

### CVE-2026-126978 — HIGH (CVSS: 8.8)

- Published: 2026-11-18T00:18:38.467
- Description: Philips Hue Bridge hap_pair_setup_handler Heap-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Philips Hue Bridge. Authentication is not required to exploit this vulnerability.

The specific flaw exists within the HomeKit Accessory Protocol service, which listens on TCP port 8080 by default. When parsing pairing requests, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length, heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the device. Was ZDI-CAN-28434.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126978

### CVE-2026-126979 — HIGH (CVSS: 8.8)

- Published: 2026-11-18T00:18:38.590
- Description: Philips Hue Bridge HomeKit Accessory Protocol chacha20_decrypt Integer Underflow Remote Code Execution Vulnerability. This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Philips Hue Bridge. Authentication is not required to exploit this vulnerability.

The specific flaw exists within the HomeKit Accessory Protocol service, which listens on TCP port 8080 by default. When parsing pairing requests, the process does not properly validate user-supplied data, which can result in an integer underflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the device. Was ZDI-CAN-28332.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126979

### CVE-2026-126980 — MEDIUM (CVSS: 6.5)

- Published: 2026-11-18T00:18:38.713
- Description: Philips Hue Bridge HomeKit Observable Discrepancy Information Disclosure Vulnerability. This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of Philips Hue Bridge. Authentication is not required to exploit this vulnerability.

The specific flaw exists within the HomeKit Authentication service, which listens on TCP port 8080 by default. When processing crafted pairing requests, the service discloses internal information via an observable discrepancy between possible responses. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the device. Was ZDI-CAN-28470.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126980

### CVE-2026-129040 — MEDIUM (CVSS: 5.3)

- Published: 2026-11-18T00:18:39.850
- Description: Missing Authorization vulnerability in WP User Manager WP User Manager wp-user-manager allows Exploiting Incorrectly Configured Access Control Security Levels.This issue affects WP User Manager: from n/a through 2.10.4.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129040

### CVE-2026-129049 — MEDIUM (CVSS: 6.5)

- Published: 2026-11-18T00:18:39.997
- Description: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WP Go Maps WP Go Maps wp-google-maps allows Stored XSS.This issue affects WP Go Maps: from n/a through 10.1.12.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129049

### CVE-2026-129069 — MEDIUM (CVSS: 5.3)

- Published: 2026-11-18T00:18:40.143
- Description: Missing Authorization vulnerability in John-Michael L'Allier Create mediavine-create allows Exploiting Incorrectly Configured Access Control Security Levels.This issue affects Create: from n/a through 3.1.3.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129069

### CVE-2026-129891 — HIGH (CVSS: 7.5)

- Published: 2026-11-18T00:18:40.290
- Description: IO::Socket::SSL::PublicSuffix versions through 2.099 for Perl let an on-path attacker choose the installed public suffix list because update_self_from_url fetches it over cleartext HTTP with no integrity check.

Called with no argument, as the module's documentation shows, the updater fetches the list from the `http://` address in the URL constant and checks only that the request succeeded, with no signature or digest over the response. The lines that come back are written into the module's own source file as the built-in list.

An attacker on the network path when the updater runs chooses the suffix boundary the module reports to every caller on the host, and that answer persists in the installed module until it is reinstalled. Dropping one rule makes the hostname check in IO::Socket::SSL accept a wildcard certificate that spans the whole public suffix that rule named.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129891

### CVE-2026-129892 — CRITICAL (CVSS: 9.8)

- Published: 2026-11-18T00:18:40.417
- Description: IO::Socket::SSL::PublicSuffix versions through 2.099 for Perl allow code injection via a fetched list line that closes the built-in data heredoc when update_self_from_url rewrites the module's source.

The rewrite copies the module's source down to the built-in list's heredoc and appends each fetched line below it. Nothing checks that a line looks like a domain. A line that is not a comment loses only what follows a `//` and its trailing whitespace, so a line reading END_BUILTIN_DATA is appended as it stands and ends the data block in the rewritten file. Every fetched line after it is Perl.

Arbitrary Perl runs in every process that loads IO::Socket::SSL, which loads this module unconditionally, until the file is reinstalled. The attacker must control the fetched list, through the cleartext default URL or a caller-supplied one, and the updater must run with write access to the installed module.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129892

### CVE-2026-130600 — MEDIUM (CVSS: 4.3)

- Published: 2026-11-18T00:18:40.533
- Description: Insertion of Sensitive Information Into Sent Data vulnerability in BdThemes Element Pack Elementor Addons bdthemes-element-pack-lite allows Retrieve Embedded Sensitive Data.This issue affects Element Pack Elementor Addons: from n/a through 10.0.9.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-130600

### CVE-2026-131842 — MEDIUM (CVSS: 5.7)

- Published: 2026-11-18T00:18:41.440
- Description: Poppler pdfdetach 24.03.0 through 26.11.0 contains a path traversal vulnerability in utils/pdfdetach.cc that allows attackers to write files outside the output directory by bypassing a string-prefix containment check. Attackers can craft PDFs with embedded file names containing '..' sequences or absolute paths, so -saveall or -savefile extraction creates or overwrites files with the invoking user's privileges.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-131842

### CVE-2026-131843 — MEDIUM (CVSS: 5.3)

- Published: 2026-11-18T00:18:41.607
- Description: Poppler pdftohtml through 26.11.0 contains a cross-site scripting vulnerability in HtmlLink::getLinkStart() in utils/HtmlLinks.cc that writes PDF link annotation URIs into href attributes without escaping in HTML output modes. Attackers can craft a PDF whose /URI entry contains a double quote followed by HTML markup or event handlers to execute script in browsers viewing the generated HTML.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-131843

### CVE-2026-131844 — HIGH (CVSS: 7.1)

- Published: 2026-11-18T00:18:41.757
- Description: Poppler through 26.11.0 contains an uncontrolled memory allocation vulnerability in the libcurl-based remote file loader that trusts unvalidated HEAD Content-Length values in CurlCachedFileLoader::init(). Malicious HTTP servers can return an enormous Content-Length so CachedFile resizes its chunk cache accordingly, aborting pdfinfo or PDFDocFactory-based applications with std::bad_alloc for denial of service.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-131844

### CVE-2026-131845 — MEDIUM (CVSS: 4.1)

- Published: 2026-11-18T00:18:41.903
- Description: Poppler 21.01.0 through 26.11.0 contains a time-of-check time-of-use race condition in FormWidgetSignature::signDocument() that allows local attackers to obtain valid signatures over altered content. Attackers with write access to the output file or directory can overwrite or swap the PDF between writing and hashing, causing the signer's key to sign attacker-controlled content.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-131845

### CVE-2026-131846 — MEDIUM (CVSS: 5.8)

- Published: 2026-11-18T00:18:42.047
- Description: Poppler 0.76.1 through 26.11.0 contains a heap-based buffer overflow in SplashOutputDev::iccTransform() that allows attackers to write out of bounds when rendering in splashModeDeviceN8. Attackers can supply a PDF with an ICCBased image whose alternate is DeviceN, causing getDeviceNLine() to overflow the per-row buffer, crashing the renderer and corrupting heap memory.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-131846

### CVE-2026-131847 — MEDIUM (CVSS: 4.8)

- Published: 2026-11-18T00:18:42.220
- Description: Poppler through 26.11.0 contains a use-after-free vulnerability in NSSCryptoSignBackend.cc that allows attackers to trigger reads of freed CMS arena memory during repeated signature verification. Attackers can supply a signed PDF embedding the signer certificate to crash applications or pdfsig runs validating multiple signatures, or cause incorrect certificate validation results.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-131847

### CVE-2026-131848 — HIGH (CVSS: 8.3)

- Published: 2026-11-18T00:18:42.417
- Description: Snap7 through 1.4.3 contains an out-of-bounds write vulnerability in TSnap7MicroClient::opReadMultiVars() that allows malicious PLCs to overflow client buffers via unchecked DataLength fields. Attackers controlling or impersonating a PLC can return crafted ReadVar responses to Cli_ReadMultiVars() callers, writing up to 65535 bytes per item to corrupt memory and crash clients.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-131848

### CVE-2026-131849 — HIGH (CVSS: 8.3)

- Published: 2026-11-18T00:18:42.583
- Description: Snap7 through 1.4.3 contains a heap-based buffer overflow in TSnap7MicroClient::opReadSZL() that allows malicious PLCs to overwrite client memory by sending oversized multi-slice SZL responses. A rogue or impersonated PLC can keep flagging more data with attacker-controlled DLen slices, overflowing the 65536-byte opData buffer via Cli_ReadSZL() and Cli_ReadSZLList(), crashing the client and corrupting heap memory.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-131849

### CVE-2026-131850 — HIGH (CVSS: 8.6)

- Published: 2026-11-18T00:18:42.747
- Description: ILIAS 11.0 before 11.6 contains an sql injection vulnerability in RegistrationCodeRepository::getCodesData() that concatenates unvalidated sort fields into an ORDER BY clause. Authenticated users with read access to the Authentication and Registration administration node can supply SQL expressions as the sort parameter to extract database contents via boolean-based inference.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-131850
