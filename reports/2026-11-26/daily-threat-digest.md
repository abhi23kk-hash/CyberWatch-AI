# Cybersecurity Daily Intelligence Digest

Generated: 2026-11-26 23:08 UTC
Records included: 35

## Data Sources

- National Vulnerability Database (NVD)
- CISA Known Exploited Vulnerabilities (KEV)

## AI Analyst Summary

Gemini AI analysis was unavailable. The collected vulnerability records are retained below for manual review.

## Vulnerability Findings

### CVE-2026-122676 — HIGH (CVSS: 8.5)

- Published: 2026-11-19T23:19:24.940
- Description: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in PublishPress PublishPress Authors publishpress-authors allows Blind SQL Injection.This issue affects PublishPress Authors: from n/a through 4.18.0.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-122676

### CVE-2026-133327 — LOW (CVSS: 2.1)

- Published: 2026-11-19T23:19:29.040
- Description: A vulnerability was identified in Dolibarr ERP CRM up to 23.0.4. This affects the function dol_convert_file in the library htdocs/core/lib/files.lib.php of the component Document Upload. Such manipulation leads to code injection. The attack can be launched remotely. The exploit is publicly available and might be used. Upgrading to version 24.0.0 is able to mitigate this issue. The name of the patch is 9b6368b2a9eae3eec690b2ce22c4f291f0051540. Upgrading the affected component is advised.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133327

### CVE-2026-133435 — LOW (CVSS: 3.7)

- Published: 2026-11-19T23:19:29.293
- Description: A flaw was found in Keycloak. When configured with a database that uses case-insensitive collation, Keycloak resolves realm URLs regardless of letter casing. A remote attacker can exploit this behavior by sending requests with alternate letter casing to bypass upstream reverse proxy access controls that rely on case-sensitive path matching. This issue can expose restricted authentication endpoints intended only for internal access, though Keycloak's internal authentication mechanisms remain intact.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133435

### CVE-2026-22062 — LOW (CVSS: 2.3)

- Published: 2026-11-20T00:17:26.170
- Description: StorageGRID (formerly StorageGRID Webscale) versions 12.1.0 and higher are susceptible to an information exposure vulnerability which allows a remote unauthenticated attacker to acquire low-sensitivity credentials via a Man-in-the-middle attack when certain non-default features are enabled.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-22062

### CVE-2025-71473 — MEDIUM (CVSS: 6.9)

- Published: 2026-11-20T01:17:07.597
- Description: lwext4 through 1.0.0 contains a heap buffer overflow in ext4_fs_init_inode_bitmap() in src/ext4_fs.c because it does not validate s_inodes_per_group against the inode bitmap size. Attackers can supply a crafted ext4 image with an oversized s_inodes_per_group so memset writes past the heap buffer, corrupting memory and crashing the mounting application.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2025-71473

### CVE-2025-71474 — MEDIUM (CVSS: 6.9)

- Published: 2026-11-20T01:17:08.690
- Description: lwext4 through 1.0.0 contains an out-of-bounds write vulnerability in ext4_fs_init_block_bitmap() that allows attackers to corrupt heap memory via crafted superblock geometry fields. Attackers can supply an ext4 image with oversized s_reserved_gdt_blocks and BLOCK_UNINIT groups to write past the bitmap buffer, crashing applications that mount it.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2025-71474

### CVE-2026-126540 — HIGH (CVSS: 7.5)

- Published: 2026-11-20T01:17:08.843
- Description: Convert::ASN1 versions before 0.37 for Perl allow CPU exhaustion via quadratic bigint loop in os2ip.

Every INTEGER or ENUMERATED longer than four content octets reaches os2ip, which iterates over each content octet with $result = ($result * 256) + $octet. Each multiplication operates on a bigint that grows by one octet per step, so decoding an n-octet value takes O(n^2) bigint work. Nothing limits content length before this loop runs.

An attacker who controls the decoded data can exhaust CPU with a single oversized INTEGER or ENUMERATED value.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126540

### CVE-2026-126568 — HIGH (CVSS: 7.5)

- Published: 2026-11-20T01:17:08.970
- Description: Convert::ASN1 versions before 0.37 for Perl allow memory exhaustion via unbounded MSG_PEEK buffer doubling in asn_recv.

asn_recv peeks the socket in a loop, doubling the buffer size on each pass until a tag and length can be decoded. An inverted boolean guard ($tb || rather than $tb &&) prevents the need-more-data exit from firing once a tag byte has been decoded. When asn_decode_length returns no value because the length is absent or incomplete, no exit fires for that case either. MSG_PEEK leaves socket data unconsumed, so each re-peek returns at once while the buffer size doubles.

A single truncated BER header sent to a process calling asn_recv doubles the peek buffer until memory is exhausted. Perl's realloc failure is fatal and not catchable with eval.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126568

### CVE-2026-126576 — HIGH (CVSS: 7.5)

- Published: 2026-11-20T01:17:09.083
- Description: Convert::ASN1 versions before 0.37 for Perl allow CPU exhaustion via unchecked exponent length in binary REAL decoding.

Binary REAL decoding never bounds-checks the exponent length against the available content. For a minimal one-byte binary REAL, the exponent byte is read from outside the element, making the mantissa length -1. Perl reads a negative length as an offset from the end of the string, so the mantissa is nearly all of the input that follows the element. The long-form exponent path also omits the extra length octet when sizing the mantissa.

An attacker who controls the decoded data can exhaust CPU with a list of such values, as each mantissa loop iterates over the remaining input. The decoded values are also computed from bytes outside each element.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126576

### CVE-2026-126682 — HIGH (CVSS: 7.5)

- Published: 2026-11-20T01:17:09.197
- Description: Convert::ASN1 versions before 0.37 for Perl allow CPU exhaustion via exponent-notation string in INTEGER encoding.

The encoder routes any value with abs >= 2**31 to i2osp without validating that it is an integer. A string in exponent notation such as "1e8000" passes that threshold. Math::BigInt expands it to an 8001-digit integer, and i2osp's per-octet conversion loop is quadratic in that size.

An attacker who controls encoded INTEGER values can exhaust CPU with a short exponent-notation string.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126682

### CVE-2026-126819 — HIGH (CVSS: 7.5)

- Published: 2026-11-20T01:17:09.313
- Description: Convert::ASN1 versions before 0.37 for Perl allow memory exhaustion via zero-length BIT STRING content.

A BIT STRING with zero content octets passes -1 to substr as the length. Perl reads a negative length as an offset from the end of the string, so the decoded value is nearly all of the input that follows the element. In the constructed form each zero-length segment copies the rest of the input again, so memory grows with the square of the input size.

An attacker who controls the decoded data can exhaust memory with a short constructed BIT STRING. The resulting value also contains bytes from adjacent input.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126819

### CVE-2026-126956 — HIGH (CVSS: 7.5)

- Published: 2026-11-20T01:17:09.427
- Description: Convert::ASN1 versions before 0.37 for Perl allow memory exhaustion via unlimited recursion depth in constructed-form string decoding.

Any constructed-form string element causes the decoder to recurse on the element's contents. The BER encoding controls nesting depth at four bytes per level, with no bound checked. Perl recursion is heap-allocated, so the process grows without a stack crash.

An attacker who controls the decoded data can exhaust memory with a small deeply nested constructed string.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126956

### CVE-2026-131868 — HIGH (CVSS: 7.5)

- Published: 2026-11-20T01:17:09.543
- Description: Convert::ASN1 versions before 0.37 for Perl allow memory exhaustion via a declared element length passed unchecked to sysread in asn_read and asn_get.

The length an element declares in its BER header is passed to sysread as the read size. Perl grows the target buffer to that size before reading, so memory is allocated from the declared length, not from the data received. A 6-byte header can declare a length of up to 4GB.

A single header makes the reading process allocate the declared size. Where the allocation fails, perl exits with "Out of memory", which eval cannot catch.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-131868

### CVE-2026-131877 — HIGH (CVSS: 7.5)

- Published: 2026-11-20T01:17:09.660
- Description: Convert::ASN1 versions before 0.37 for Perl allow CPU exhaustion via unbounded arc length in OBJECT IDENTIFIER decoding and encoding.

The content of an OBJECT IDENTIFIER or RELATIVE-OID element is passed to unpack "w*" on decode, and the arcs of an OID string to pack "w*" on encode. Perl converts each arc to or from its decimal string in time quadratic in the arc's length, and nothing limits that length.

An attacker who controls the decoded data, or an OID string passed to encode, can exhaust CPU with a single oversized arc.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-131877

### CVE-2026-133406 — MEDIUM (CVSS: 4.8)

- Published: 2026-11-20T01:17:09.923
- Description: A vulnerability was determined in aoiflux mutant 2.3.0/2.4.0/2.5.0. This vulnerability affects unknown code of the file builtin/hive_builtins.go of the component Forensic Parser. This manipulation of the argument Count causes uncontrolled memory allocation. It is possible to launch the attack on the local host. Upgrading to version 2.6.0 is able to resolve this issue. Patch name: c4b1a7dec6c603115e2a05d1e8970a142f0b9774. Upgrading the affected component is recommended.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133406

### CVE-2026-133519 — MEDIUM (CVSS: 6.8)

- Published: 2026-11-20T01:17:10.133
- Description: FFmpeg 7.0 through 9.0.2 contains an out-of-bounds read vulnerability in dvdvideo_menu_next_ps_block() in libavformat/dvdvideodec.c when demuxing DVD menu domains. Attackers can craft a DVD image whose last cell sector and NAV next-VOBU pointer bypass the end-of-cell check, overreading pgc->cell_playback and crashing the process.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133519

### CVE-2026-133520 — MEDIUM (CVSS: 5.3)

- Published: 2026-11-20T01:17:10.303
- Description: Dokploy 0.28.0 before 0.31.1 contains a path traversal vulnerability in the patch.readRepoDirectories tRPC procedure that allows authenticated organization members to list tracked files of arbitrary git repositories. Attackers with service read permission can supply a crafted repoPath, which is passed to git ls-tree unconfined, to enumerate other organizations' application and compose source trees.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133520

### CVE-2026-133521 — MEDIUM (CVSS: 5.3)

- Published: 2026-11-20T01:17:10.480
- Description: Bar Assistant 3.0.0 before 6.11.0 contains an authorization bypass vulnerability in BarController::join that allows authenticated users to join bars without a valid invite code. Attackers can send POST requests to /api/bars/join omitting invite_code, matching invite-disabled bars with NULL codes, to read cocktails, ingredients, members, settings and search tokens.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133521

### CVE-2026-133528 — CRITICAL (CVSS: 9.3)

- Published: 2026-11-20T01:17:10.633
- Description: BeamNG.drive before 0.40.6 contains an out-of-bounds write vulnerability because JIT-compiled LuaJIT traces omit FFI array bounds checks, letting untrusted Lua escape the sandbox. Attackers supplying a malicious mod can JIT-compile an FFI store loop, write out of range using a tostring() address leak, re-enable ffi.load, and run commands as the game user.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133528

### CVE-2026-82091 — LOW (CVSS: 3.2)

- Published: 2026-11-20T01:17:10.807
- Description: The Canva Desktop App before 1.128.0 stores encrypted application state on disk. The encryption key is hardcoded as a plaintext string in the main.js file and is identical across all Canva installations on Windows and macOS.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-82091

### CVE-2026-102430 — MEDIUM (CVSS: 6.9)

- Published: 2026-11-20T02:17:16.100
- Description: An uncontrolled recursion vulnerability exists in the LINE iOS app prior to version 26.19.0.

The Flex Message processing component does not adequately validate the structure of externally supplied message content.

As a result, an attacker who is able to send a crafted message to a victim could cause the application to crash when the message is received or displayed.

A server-side mitigation has been deployed that also protects existing iOS clients that have not been updated to version 26.19.0.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-102430

### CVE-2026-133224 — MEDIUM (CVSS: 5.4)

- Published: 2026-11-20T02:17:16.640
- Description: A flaw was found in Keycloak. When an administrator revokes tokens by setting a not-before revocation cutoff, Keycloak fails to enforce this boundary when processing User-Managed Access (UMA) grant requests using ID token claims. An authenticated remote user with an active session can submit a previously revoked ID token to receive a fresh Requesting Party Token (RPT). This flaw allows an attacker to bypass token revocation and retain unauthorized access to protected resources.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133224

### CVE-2026-133225 — MEDIUM (CVSS: 5.4)

- Published: 2026-11-20T02:17:16.820
- Description: A flaw was found in Keycloak. When processing token requests using the User-Managed Access (UMA) grant, Keycloak fails to verify whether a target client or resource server is enabled before issuing an authorization token. An authenticated remote user can exploit this flaw to obtain valid Requesting Party Tokens (RPTs) for disabled clients, bypassing administrative access controls and permissions restrictions.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133225

### CVE-2026-133226 — MEDIUM (CVSS: 4.3)

- Published: 2026-11-20T02:17:16.973
- Description: A flaw was found in Keycloak. The Account API endpoint for sharing resources fails to verify whether owner-managed access is enabled and accepts permission scopes not assigned to the resource. An authenticated user can exploit this vulnerability to generate pre-granted permission tickets, causing Keycloak to bypass policy evaluation and issue access tokens with unauthorized scopes.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133226

### CVE-2026-133228 — MEDIUM (CVSS: 6.8)

- Published: 2026-11-20T02:17:17.127
- Description: A flaw was found in Keycloak. When a client application enforces step-up authentication or multi-factor authentication (MFA) via a minimum authentication level, Keycloak fails to apply this requirement to login sessions initiated through the credential reset endpoint. An attacker who possesses a user's initial credentials (such as a password) can navigate from the reset interface back to the standard login form and authenticate without completing the required second factor. This flaw allows an attacker to obtain valid access tokens and gain unauthorized access to protected services without satisfying mandatory security controls.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133228

### CVE-2026-133413 — MEDIUM (CVSS: 4.6)

- Published: 2026-11-20T02:17:17.290
- Description: A vulnerability was detected in smartalock wireguard-lwip up to cfba91666590e86bd67842c71cedf9a423be823a. This affects the function wireguard_generate_unique_index of the file src/wireguard.c of the component Session Index Allocator. The manipulation of the argument receiver_index results in allocation of resources. The attack is only possible with local access. The project was informed of the problem early through an issue report but has not responded yet.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133413

### CVE-2026-133414 — MEDIUM (CVSS: 6.9)

- Published: 2026-11-20T02:17:17.533
- Description: A security flaw has been discovered in sofastack sofa-bolt up to 1.6.12. Affected by this issue is the function HessianSerializer.deserialize of the file src/main/java/com/alipay/remoting/serialization/HessianSerializer.java of the component Hessian2 Deserialization. Performing a manipulation results in allocation of resources. The attack can be initiated remotely. The vendor was contacted early about this disclosure but did not respond in any way.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133414

### CVE-2026-133415 — MEDIUM (CVSS: 5.5)

- Published: 2026-11-20T02:17:17.740
- Description: A vulnerability has been found in sumiie24 School-Management-System up to d946d649c7c95e101fc5679ecd91999533bb10d7. The affected element is an unknown function of the file parent_Registration.php. Such manipulation of the argument student_reg leads to sql injection. The attack can be executed remotely. The exploit has been disclosed to the public and may be used. This product implements a rolling release for ongoing delivery, which means version information for affected or updated releases is unavailable.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133415

### CVE-2026-133477 — MEDIUM (CVSS: 6.3)

- Published: 2026-11-20T03:17:34.393
- Description: A weakness has been identified in sofastack sofa-bolt up to 1.6.12. This impacts the function initSSLContext of the file src/main/java/com/alipay/remoting/connection/AbstractConnectionFactory.java of the component TLS Stack. Executing a manipulation can lead to certificate with host mismatch. The attack may be performed from remote. This attack is characterized by high complexity. The exploitability is said to be difficult. The vendor was contacted early about this disclosure but did not respond in any way.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133477

### CVE-2026-133478 — MEDIUM (CVSS: 5.5)

- Published: 2026-11-20T03:17:34.977
- Description: A security vulnerability has been detected in rajesh2211 Doctor-Appointment-System up to ee974dcf4c50da85e6ea026e27f4370e9468b3cc. Affected is an unknown function of the file AppointmentSystem/AppointmentSystem/Connectivity.php of the component Login. The manipulation of the argument User leads to sql injection. It is possible to initiate the attack remotely. The exploit has been disclosed publicly and may be used. This product is using a rolling release to provide continious delivery. Therefore, no version details for affected nor updated releases are available.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133478

### CVE-2026-133479 — LOW (CVSS: 2.0)

- Published: 2026-11-20T03:17:35.177
- Description: A vulnerability was detected in WebKul QloApps up to 1.8.0. Affected by this vulnerability is the function postProcessDownload/installTheme of the file controllers/admin/AdminModulesController.php of the component Archive Import. The manipulation results in path traversal. It is possible to launch the attack remotely. The exploit is now public and may be used. The vendor was contacted early about this disclosure but did not respond in any way.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133479

### CVE-2026-133534 — HIGH (CVSS: 8.7)

- Published: 2026-11-20T03:17:35.377
- Description: PowerLink developed by Neotroni Lighting has a SQL Injection vulnerability, allowing unauthenticated remote attackers to inject arbitrary SQL commands to read database contents.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133534

### CVE-2026-133535 — MEDIUM (CVSS: 4.3)

- Published: 2026-11-20T03:17:35.533
- Description: A flaw was found in Hawtio. An authenticated remote attacker can cause a Denial of Service (DoS) by sending a specially crafted request URI to monitored endpoints. The FlightRecordingDownloadFacade servlet filter uses an inefficient regular expression pattern that causes catastrophic backtracking when processing certain long requests. This issue leads to excessive CPU utilization, causing handling threads to hang and degrading service availability.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133535

### CVE-2026-24205 — MEDIUM (CVSS: 6.4)

- Published: 2026-11-20T03:17:35.923
- Description: NVIDIA TensorRT-LLM for any platform contains a vulnerability where a user may cause a race condition by running concurrent requests. A successful exploit of this vulnerability may lead to data tampering.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-24205

### CVE-2026-65094 — CRITICAL (CVSS: 9.0)

- Published: 2026-11-20T03:17:36.693
- Description: NVIDIA VIRTIO-Net for Bluefield contains a vulnerability in Virtio-Net where a VM user may cause a Write-What-Where condition by crafted message. A successful exploit of this vulnerability may lead to Code Execution in Virtio-Net scope.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-65094
