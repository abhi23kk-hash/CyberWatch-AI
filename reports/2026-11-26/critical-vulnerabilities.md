# Critical Vulnerability Watch

Generated: 2026-11-26 14:09 UTC
Records included: 38

## Data Sources

- National Vulnerability Database (NVD)
- CISA Known Exploited Vulnerabilities (KEV)

## AI Analyst Summary

Gemini AI analysis was unavailable. The collected vulnerability records are retained below for manual review.

## Vulnerability Findings

### CVE-2026-111506 — HIGH (CVSS: 8.8)

- Published: 2026-11-19T14:17:23.843
- Description: Dell PowerStore contains a Missing Authentication vulnerability that a network-adjacent attacker could exploit to bypass authentication and authorization, leading to information disclosure and denial of service.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-111506

### CVE-2026-126826 — HIGH (CVSS: 7.8)

- Published: 2026-11-19T14:17:27.037
- Description: A maliciously crafted SBSAR file, when imported or loaded through the Substance in 3ds Max plugin in Autodesk 3ds Max, can trigger an Out-of-Bounds Write vulnerability. A malicious actor may leverage this vulnerability to cause an application crash, data corruption, or potentially execute arbitrary code in the context of the current process.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126826

### CVE-2026-132858 — HIGH (CVSS: 7.8)

- Published: 2026-11-19T14:17:28.057
- Description: A flaw was found in gdm. The CreateRemoteDisplay D-Bus method fails to perform proper authorization checks when initiating a remote display session. A local attacker with access to the login screen environment can invoke this method with an arbitrary username to bypass standard automatic login verification checks. This vulnerability allows the attacker to achieve privilege escalation and start an unauthorized session as any user on the system, including root.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132858

### CVE-2026-133113 — HIGH (CVSS: 7.1)

- Published: 2026-11-19T14:17:28.367
- Description: Gogs through 0.14.4 contains an authorization bypass vulnerability that allows collaborators with write access to push to protected branches by merging pull requests. Because MergePullRequest skips branch protection checks and PullRequest.Merge omits hook environment variables, attackers can merge commits into branches restricted to allowlisted users.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133113

### CVE-2026-115560 — CRITICAL (CVSS: 9.2)

- Published: 2026-11-19T15:17:24.610
- Description: Session serializer mismatch can lead to remote code execution.

Session upload progress, when enabled, can store attacker-controlled data in a session key using the php_binary or php_serialize session serializer. If the same session is later read with the php serializer, because session.serialize_handler is changed at runtime or differs between applications sharing a session store, bytes inside the key can be passed to the unserializer. A remote attacker able to submit a multipart upload can inject objects, which may lead to code execution when the reading application contains a suitable gadget chain, or to session corruption or denial of service.

This issue affects PHP versions before 8.2.36, 8.3.* before 8.3.37, 8.4.* before 8.4.28 and 8.5.* before 8.5.13.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-115560

### CVE-2026-120753 — CRITICAL (CVSS: 9.1)

- Published: 2026-11-19T15:17:25.013
- Description: In Eclipse Ditto versions 1.1.0 to 3.9.8, when pre-authentication is enabled, the gateway service accepts the pre-authenticated subject not only from the `x-ditto-pre-authenticated` HTTP header set by a trusted reverse proxy, but also from an undocumented `x-ditto-pre-authenticated` URL query parameter that a client can set. A reverse proxy that only overwrites the header therefore does not stop clients from supplying their own subject. With the default configuration of the Ditto Helm chart (`global.jwtOnly: false`, which implicitly enables pre-authentication), the bundled nginx skips HTTP Basic authentication for any request with an `Authorization: Bearer` header and forwards it without the pre-authentication header. An unauthenticated remote attacker can send an invalid Bearer token together with the query parameter to authenticate as any chosen policy subject. Pre-authentication succeeds before the JWT is validated, so the attacker can read and modify Things and Policies with that subject's permissions. As a mitigation, disable pre-authentication in the gateway (`ENABLE_PRE_AUTHENTICATION=false`) or, when using the Helm chart, configure `global.jwtOnly: true`.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-120753

### CVE-2026-123890 — CRITICAL (CVSS: 9.8)

- Published: 2026-11-19T15:17:25.407
- Description: VMware vCenter contains an authentication bypass vulnerability in the VMware Directory Service.
Affected versions: 9.1.x (fixed in 9.1.1.0200); 9.0.x (fixed in 9.0.2.0200); 8.0 (fixed in 8.0 U3m); 5.x (fixed in 5.2.5).
Telco Cloud Platform 3.0, 4.x, 5.0.x, 5.1.x, 5.2 and Telco Cloud Infrastructure 3.0 are also affected (see KB463116).
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-123890

### CVE-2026-123891 — HIGH (CVSS: 8.1)

- Published: 2026-11-19T15:17:25.543
- Description: SDDC Manager contains an SQL-injection vulnerability due to improper sanitization of user-supplied input.
Affected versions: 9.1.x.x (fixed in 9.1.1.0200); 9.0.x.x (fixed in 9.0.2.0100); 5.x (fixed in 5.2.5).
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-123891

### CVE-2026-123892 — HIGH (CVSS: 7.2)

- Published: 2026-11-19T15:17:25.663
- Description: SDDC Manager contains an authenticated command-injection vulnerability due to improper sanitization of user-supplied input.
Affected versions: 9.1.x.x (fixed in 9.1.1.0200); 9.0.x.x (fixed in 9.0.2.0100); 5.x (fixed in 5.2.5).
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-123892

### CVE-2026-126086 — HIGH (CVSS: 8.8)

- Published: 2026-11-19T15:17:26.027
- Description: In Eclipse Dataspace Components (EDC) – Connector (`org.eclipse.edc:decentralized-claims-*`, `org.eclipse.edc:jwt-verifiable-credentials`, `org.eclipse.edc:ldp-verifiable-credentials`) there's a credential verification bypass in Decentralized Claims Protocol (DCP) presentation handling: a participant can present credentials appearing to be issued by any trusted issuer without holding them.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126086

### CVE-2026-126714 — CRITICAL (CVSS: 9.2)

- Published: 2026-11-19T15:17:26.167
- Description: Partially overwritten session files can lead to remote code execution.

The files session save handler, which is the default, writes updated session data into the existing session file without first clearing it. If a write is interrupted, the file can contain the beginning of the new session followed by the end of the old one, and bytes of an ordinary string can later be unserialized as objects. An attacker who can influence the session data, for example through session upload progress, and interrupt a write at a suitable point may inject objects, which can lead to code execution when the application contains a suitable gadget chain. Session data can also be corrupted.

This issue affects PHP versions before 8.2.36, 8.3.* before 8.3.37, 8.4.* before 8.4.28 and 8.5.* before 8.5.13.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126714

### CVE-2026-127960 — HIGH (CVSS: 8.7)

- Published: 2026-11-19T15:17:26.990
- Description: Denial of service through folded HTTP response headers.

The HTTP stream wrapper joins each continuation line of a folded response header to the accumulated value by allocating a new string and copying the whole value, so a response with many short continuation lines takes disproportionate CPU time to parse. An attacker who controls an HTTP or HTTPS response fetched through file_get_contents(), fopen() or other stream functions, by making the application request a chosen URL or by influencing a server it already contacts, can keep PHP workers busy. Repeated or concurrent requests can cause a denial of service.

This issue affects PHP versions from 8.1.32 through 8.1.34, from 8.2.28 before 8.2.36, from 8.3.18 before 8.3.37, from 8.4.5 before 8.4.28 and 8.5.* before 8.5.13.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-127960

### CVE-2026-128064 — HIGH (CVSS: 8.2)

- Published: 2026-11-19T15:17:27.120
- Description: Mixed-case HTTPS and FTPS URLs can expose data in plaintext.

The HTTP and FTP stream wrappers recognise URL schemes case-insensitively, but enable TLS only when the scheme contains a lowercase "s" at a fixed position. A URL such as HTTPS:// or FTPS:// passed to file_get_contents(), fopen() or other stream functions, or received as an HTTP redirect target, is therefore handled over unencrypted HTTP or FTP. An attacker able to observe the network traffic can read data the application expected TLS to protect, including credentials, request bodies and transferred files.

This issue affects PHP versions before 8.2.36, 8.3.* before 8.3.37, 8.4.* before 8.4.28 and 8.5.* before 8.5.13.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-128064

### CVE-2026-128090 — HIGH (CVSS: 7.7)

- Published: 2026-11-19T15:17:27.257
- Description: PHAR OpenSSL signature bypass via algorithm downgrade.

The Phar extension selects the signature verification method from the signature type stored in the archive, and only the OpenSSL types consult the separate .pubkey file holding the trusted public key. An attacker who can modify an OpenSSL-signed Phar archive, but not its public key file, can switch the signature type to a keyless hash such as SHA-256 with a recomputed digest, so the altered archive passes verification even with phar.require_hash enabled. An application that loads the archive may then execute attacker-controlled PHP code. Native, tar-based and zip-based phars are affected.

This issue affects PHP versions before 8.2.36, 8.3.* before 8.3.37, 8.4.* before 8.4.28 and 8.5.* before 8.5.13.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-128090

### CVE-2026-129182 — CRITICAL (CVSS: 9.2)

- Published: 2026-11-19T15:17:27.390
- Description: Use-after-free via repopulation of last_fatal_error_backtrace global after shutdown.

A fatal error raised while modified INI settings are restored during request shutdown can repopulate the stored fatal error backtrace after the executor has been cleaned up. The request memory is then freed, and a diagnostic emitted before executor initialization in a later request handled by the same PHP-FPM or mod_php worker can access the stale backtrace. The shutdown error requires per-path configuration of max_memory_limit, or of zlib.output_compression together with output_handler (which .user.ini can also set). The early diagnostic requires Apache per-directory configuration or, for PHP-FPM, a PHP_VALUE or PHP_ADMIN_VALUE parameter sent by the front end. This can cause memory corruption and worker crashes, and may allow remote code execution.

This issue affects PHP versions 8.5.* before 8.5.13.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129182

### CVE-2026-129289 — CRITICAL (CVSS: 9.2)

- Published: 2026-11-19T15:17:27.523
- Description: PHP-FPM request smuggling through an unread HTTP request body.

PHP does not discard the unread part of an HTTP request body at request shutdown when the application has opened php://input without reading it to the end. When the front end reuses backend connections, which is not the default in nginx or Apache (for example nginx with fastcgi_keep_conn on, or Apache mod_proxy_fcgi with enablereuse=on), PHP-FPM can parse the leftover bytes as a new FastCGI request. An unauthenticated remote attacker can use a single crafted multipart/form-data request to forge a backend request with chosen parameters such as SCRIPT_FILENAME, REMOTE_ADDR and PHP_ADMIN_VALUE, which can lead to execution of attacker-controlled PHP code. With LSAPI, subsequent requests on the connection can be disrupted.

This issue affects PHP versions before 8.2.36, 8.3.* before 8.3.37, 8.4.* before 8.4.28 and 8.5.* before 8.5.13.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129289

### CVE-2026-129291 — HIGH (CVSS: 8.8)

- Published: 2026-11-19T15:17:27.663
- Description: PHP-FPM epoll use-after-free can lead to local privilege escalation.

When catch_workers_output is enabled and the epoll event backend is used, the PHP-FPM master can close a worker's output pipe in fpm_child_close() without removing the associated event, and the delayed cleanup can free the worker record while its epoll registration is still active. A later event is then dispatched through a pointer into freed memory. A local attacker who can execute PHP code in an FPM worker can crash the master or execute code with its privileges, commonly root. catch_workers_output is disabled by default but enabled in the official PHP-FPM Docker images.

This issue affects PHP versions from 8.1.20 through 8.1.34, from 8.2.7 before 8.2.36, 8.3.* before 8.3.37, 8.4.* before 8.4.28 and 8.5.* before 8.5.13.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129291

### CVE-2026-129474 — CRITICAL (CVSS: 9.2)

- Published: 2026-11-19T15:17:28.110
- Description: Use-after-free in magic method backtraces can lead to remote code execution.

When collecting the arguments of a method call handled by __call() or __callStatic() for a backtrace, PHP can read stale values that may refer to freed memory. If a fatal error such as exceeding memory_limit occurs while an application enters such a call, with fatal_error_backtraces enabled (the default) and zend.exception_ignore_args disabled, a remote attacker who controls enough request data to influence memory allocation may cause memory corruption, crash the PHP worker or, with knowledge of memory addresses, execute arbitrary code. php.ini-production enables zend.exception_ignore_args, which prevents this.

This issue affects PHP versions 8.5.* before 8.5.13.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129474

### CVE-2026-129481 — CRITICAL (CVSS: 9.2)

- Published: 2026-11-19T15:17:28.240
- Description: Use-after-free after interrupted session shutdown.

The session extension records the filename of the executing script when a session starts. If a fatal error occurs in an application callback while the session variables are destroyed at shutdown, such as stream_close() of a user-defined stream wrapper, the pointer is retained after the request memory is freed, and a later request handled by the same worker can free the stale string. An attacker who can trigger such a failing cleanup may crash the worker or corrupt memory; code execution has not been demonstrated. This requires the filename to be allocated in request memory, for example when the script is not cached by OPcache.

This issue affects PHP versions 8.3.* before 8.3.37, 8.4.* before 8.4.28 and 8.5.* before 8.5.13.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129481

### CVE-2026-129496 — CRITICAL (CVSS: 9.2)

- Published: 2026-11-19T15:17:28.373
- Description: Timezone cache use-after-free can lead to remote code execution.

In non-thread-safe builds, a diagnostic written to a file-based error_log during module startup, for example for an invalid date.timezone value or a session configuration warning, causes the timezone cache to be allocated in startup memory that is freed while a reference to it is kept. A diagnostic raised early in the first request of a worker, such as the max_input_vars warning, then accesses the freed cache. On such a deployment an unauthenticated remote attacker can crash PHP-FPM, Apache mod_php or CGI workers with a crafted request. Arbitrary code execution may be possible and has been demonstrated with known memory addresses.

This issue affects PHP versions before 8.2.36, 8.3.* before 8.3.37, 8.4.* before 8.4.28 and 8.5.* before 8.5.13.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129496

### CVE-2026-129699 — HIGH (CVSS: 7.1)

- Published: 2026-11-19T15:17:28.930
- Description: In Eclipse Ditto versions 2.0.0 to 3.8.14 and 3.9.0 to 3.9.8, the authorization check for JSON merge patch commands on Things (HTTP `PATCH` / Ditto Protocol `merge`) does not check permissions for fields

  deleted or set to an empty object by the patch: fields with a `null` value or an empty object value (`{}`) are skipped by the check, and Ditto's regex-based key deletion with the documented `{{
  ~<regex>~ }}` syntax is not recognized as a deletion. An authenticated user with WRITE permission on any part of a Thing can therefore delete other attributes, features and the definition of that Thing,
  or overwrite or create fields as empty objects, including parts the policy revokes or never grants WRITE on.
  
  -->
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129699

### CVE-2026-129700 — HIGH (CVSS: 7.1)

- Published: 2026-11-19T15:17:29.067
- Description: In Eclipse Ditto versions 2.4.0 to 3.9.8, Thing fields a requester is not allowed to read can be disclosed through the `condition` and `live-channel-condition` headers, which are evaluated against the

  full Thing: the READ check of `live-channel-condition` is skipped when a `condition` header is also present on Thing query commands (3.0.0 to 3.9.8); both headers are evaluated without any authorization
  on WoT Thing Description requests (`Accept: application/td+json`) when WoT TD permission filtering is not active (by default in 3.0.0 to 3.8.14, in 2.4.x with WoT integration enabled, and in 3.9.x with
  filtering disabled); the `condition` of live messages and live events is evaluated without a READ check, and of claim messages without any permission (3.1.0 to 3.9.8); and the twin response of a Thing
  query with a non-matching `live-channel-condition` is returned without filtering it by the policy (3.0.0 to 3.9.8). This allows an authenticated user to read Thing fields they are not allowed to read, in
  some cases without any permission on the Thing.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129700

### CVE-2026-132039 — HIGH (CVSS: 7.1)

- Published: 2026-11-19T15:17:32.450
- Description: In Eclipse Ditto versions before 3.9.9, Thing events delivered via WebSocket, Server-Sent Events and connections disclose field values which the policy does not allow the subscriber to read. A READ

  revoke for one subject of the subscriber's authorization context is not applied when another of its subjects is granted READ. For subscribers with partial READ access, subscription RQL filters, the SSE
  `_context`, `thing-json` placeholders and extra fields are evaluated on the unfiltered event. This allows an authenticated subscriber with at least partial READ access to a Thing to obtain the values of
  fields it may not read when events for that Thing are emitted.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132039

### CVE-2026-133161 — HIGH (CVSS: 7.5)

- Published: 2026-11-19T15:17:35.953
- Description: ### Summary ui

With `strip_ansi=True`, Pydantic AI Harness's `ToolOutputLimits` capability removes ANSI escape sequences from tool output with a pattern that takes time quadratic in the length of a line. A tool result of a few hundred kilobytes, crafted with many unterminated escape sequences, can occupy the event loop for tens of seconds to minutes, delaying every other request and agent run in the process.

### Details

This affects applications that set `strip_ansi=True` on `ToolOutputLimits` (named `OverflowingToolOutput` before 0.13.0) and run tools whose output an attacker can influence, such as shell commands, file reads, fetched pages or MCP servers. Stripping runs on the event loop before the capability reduces the output, so its own size limits do not bound it.

The assumed attacker can place text in content a tool returns.

### Mitigation

Upgrade `pydantic-ai-harness` to 0.70.0 or later. Until then, leave `strip_ansi` at its default, `False`.

On Pydantic AI v1, the harness cannot be upgraded past 0.4.0. Upgrade to Pydantic AI v2 and `pydantic-ai-harness` 0.70.0, or leave `strip_ansi` off.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133161

### CVE-2026-133168 — HIGH (CVSS: 8.5)

- Published: 2026-11-19T15:17:36.650
- Description: OFFIS DCMTK 3.7.1 contains a heap buffer overflow vulnerability in togglePlanarConfiguration8 and togglePlanarConfiguration16 in djcodece.cc, which compute row offsets using rows instead of columns. Attackers can supply a crafted color-by-plane DICOM image with more rows than columns that is compressed with the true-lossless JPEG codec to corrupt heap memory, causing crashes and potentially code execution.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133168

### CVE-2026-133172 — HIGH (CVSS: 8.7)

- Published: 2026-11-19T15:17:37.253
- Description: Cozy Cloud cozy-stack 1.6.62 before 1.6.69 contains an authorization bypass vulnerability in the shared-drive move handler that allows authenticated users to access other instances' files. Attackers owning a shared drive can name another instance's domain and any directory ID as the move source to copy and delete the victim's file tree.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133172

### CVE-2026-133173 — HIGH (CVSS: 7.1)

- Published: 2026-11-19T15:17:37.410
- Description: WatchAlert 2.0.0 through 3.9.20 contains an insecure direct object reference vulnerability in the /api/w8t/datasource/dataSourceGet endpoint that lets authenticated users read other tenants' datasources because lookups omit tenant_id filtering. Tenant members with datasource view permission can request another tenant's datasource ID to obtain basic auth passwords, AWS and Alibaba Cloud keys, and Kubernetes kubeconfigs.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133173

### CVE-2026-133185 — CRITICAL (CVSS: 9.1)

- Published: 2026-11-19T15:17:39.470
- Description: Goproxy before 1.9.4 contains a weak key generation vulnerability in NewCounterEncryptorRandFromKey that derives RSA and Ed25519 leaf certificate private keys from public data due to misuse of hash.Sum. Attackers with the CA certificate and one observed leaf certificate can regenerate that host's leaf private key and impersonate the host to clients trusting the proxy CA.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133185

### CVE-2026-133195 — HIGH (CVSS: 7.5)

- Published: 2026-11-19T15:17:40.590
- Description: In JetBrains Junie CLI before 26.6.29 files outside the project directory could be modified by agent file tools
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133195

### CVE-2026-133198 — HIGH (CVSS: 7.8)

- Published: 2026-11-19T15:17:40.953
- Description: In JetBrains Junie before 252.819.35, 253.819.35 code execution was possible via terminal environment settings in project files
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133198

### CVE-2026-87867 — HIGH (CVSS: 7.1)

- Published: 2026-11-19T15:17:42.420
- Description: MRemoteNG establishes encrypted but unauthenticated channel with Microsoft SQL Server backend. Client accepts any certificate the server
presents, including a self-signed certificate supplied by an attacker. An attacker positioned between the client and the SQL server (for example via ARP/DNS spoofing) can
transparently pintercept the connection (man-in-the-middle) and read all traffic, including the encrypted connection-password table read and the database login.




Vendor did not provide the range of vulnerable versions. Only version 1.76.20 was tested and confirmed vulnerable. Other versions may also be vulnerable.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-87867

### CVE-2026-87868 — HIGH (CVSS: 8.2)

- Published: 2026-11-19T15:17:42.557
- Description: MRemoteNG uses single MD5 hash with no salt and no iterations for key-derivation. An attacker who obtains the encrypted data can brute-force
a weak or moderate passphrase offline at extreme speed and then decrypt every stored connection
password. When the default passphrase is in use, no cracking is needed at all; the key is derived from a
publicly known value.


Vendor did not provide the range of vulnerable versions. Only version 1.76.20 was tested and confirmed vulnerable. Other versions may also be vulnerable.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-87868

### CVE-2026-99322 — HIGH (CVSS: 8.8)

- Published: 2026-11-19T15:17:42.937
- Description: In the Linux kernel, the following vulnerability has been resolved:

ksmbd: rebind completed CREATE replays without draining the old channel

A completed DurableHandleReqV2 CREATE can be replayed through another
channel while its original channel is exiting. The existing replay path
returns the open but leaves its connection and oplock references pointing
at the old channel. Its open count also stays on that channel, and a
later CLOSE through the surviving channel decrements the wrong counter.

After checking the owner, lease key and persistent flag, verify that an
active open is still published in the requesting session's file table.
Do this even when no oplock was granted, and before processing a consumed
replay. Do not read a borrowed opinfo session pointer for this check.

Keep a healthy original binding. If the original channel is exiting or
releasing, move the open and its own oplock references to the requesting
channel. Serialize this with CLOSE using the session file-table lock,
and with detach, reconnect and notification snapshots using m_lock.
The earlier lock index and lease-table changes make their lifetimes
independent of this connection change. No old-channel r_count wait is
needed, including when an unrelated request remains active there.

Account final close against fp->conn in one place, balance durable detach
and reconnect, and transfer the count with a replay binding change. A
final global lookup put may run after CLOSE has removed the volatile id;
unlink the open from the inode list on that final close as well.

A live completed CREATE replay may follow a break that lowered the
durable open's batch oplock. Apply the batch eligibility check only to
detached reconnects, while retaining the owner, lease key and persistent
flag checks for active replays.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-99322

### CVE-2026-99336 — HIGH (CVSS: 7.0)

- Published: 2026-11-19T15:17:44.610
- Description: In the Linux kernel, the following vulnerability has been resolved:

KVM: guest_memfd: take the invalidate lock when unbinding a dying file

kvm_gmem_unbind() takes mapping->invalidate_lock only if the
get_file_active() succeeds. When the guest_memfd file is dying, its
reference count is already zero so get_file_active fails and the binding
is removed without holding the invalidate lock.

kvm_gmem_invalidate_{start,end}() checks f->bindings independently to
decide whether to begin or end KVM MMU invalidation. So, the bindings
must therefore remain stable between the two calls. Otherwise, unbind
can remove a binding after start increments mmu_invalidate_in_progress,
but before end finds the binding and decrements it.
Example, unbind race with memory failure:

  CPU 0: memory failure               CPU 1: memslot delete
  ----------------------------------  ---------------------------
                                      (guest_memfd file is dying)
  kvm_gmem_error_folio()
    kvm_gmem_invalidate_start()
      finds binding
      mmu_invalidate_in_progress++
                                      kvm_gmem_unbind()
                                        get_file_active() fails
                                        removes binding
    kvm_gmem_invalidate_end()
      no binding found
      counter stays elevated

mmu_invalidate_retry() then returns 1 forever, so guest page faults
retry without ever installing a mapping and the guest hangs.

Remove the distinction between live and dying files in the unbind path.
Always use slot->gmem.file and take the invalidate lock when it's non-NULL.
Normal unbind callers hold slots_lock, which prevents release from clearing
the pointer or freeing the file state until unbind completes. Final VM
teardown can only see a NULL pointer because guest_memfd pins the KVM until
release has cleared all bindings.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-99336

### CVE-2026-99340 — HIGH (CVSS: 7.8)

- Published: 2026-11-19T15:17:45.113
- Description: In the Linux kernel, the following vulnerability has been resolved:

KVM: x86: Take SRCU in kvm_zap_gfn_range()

kvm_zap_gfn_range() walks memslots and rmaps and may drop mmu_lock to
reschedule. Callers that do not already hold kvm->srcu (or slots_lock)
can race with memslot deletion: synchronize_srcu_expedited() does not
wait, kvm_free_memslot() frees the old slot and its rmap, and the zap
resumes on freed memory.

The VFIO noncoherent-DMA path hits this by zapping the entire GPA
space without SRCU. KASAN reported:

  BUG: KASAN: vmalloc-out-of-bounds in slot_rmap_walk_next+0x82/0x1c0
  Read of size 8 at addr ffffc900005c1008
  Call Trace:
   slot_rmap_walk_next+0x82/0x1c0
   __kvm_rmap_zap_gfn_range+0x17a/0x280
   kvm_zap_gfn_range+0x2a6/0x6a0
   kvm_vfio_set_attr+0x576/0x770
   kvm_device_ioctl+0x1ff/0x3b0

Take SRCU inside kvm_zap_gfn_range() so every caller is covered.
Nesting with an existing kvm->srcu critical section is fine; the
helper uses a local index. Drop the now-redundant SRCU pair from
__kvm_set_or_clear_apicv_inhibit().
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-99340

### CVE-2026-99343 — HIGH (CVSS: 7.1)

- Published: 2026-11-19T15:17:45.473
- Description: In the Linux kernel, the following vulnerability has been resolved:

KVM: x86/mmu: Bug the VM if KVM attempts to walk more levels than the MMU has

Extend the "EFER.LMA && !CR4.PAE" check, which exists largely to guard
against KVM configuring a paging32 MMU with more than 2 levels of paging,
with a very explicit check for exactly that: that KVM isn't trying to walk
more levels of paging than the MMU template provides.  I.e. harden KVM
against all bugs that would cause KVM to generates accesses beyond the
bounds of guest_walker's arrays, regardless of how KVM ended up with the
misconfigured MMU.

Note, don't use w->cpu_role.base.level directly as the paging64 template
only provides two levels of page tables for PAE paging on 32-bit hosts, and
handles the third level by manually emulating the PDPTR access.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-99343

### CVE-2026-99345 — HIGH (CVSS: 7.8)

- Published: 2026-11-19T15:17:45.720
- Description: In the Linux kernel, the following vulnerability has been resolved:

KVM: nSVM: Reject KVM_SET_NESTED_STATE if L1 has EFER.LMA=1 && EFER.LME=0

Reject KVM_SET_NESTED_STATE if the incoming L1 host state has what is
effectively an impossible EFER combination of LMA=1 but LME=0, i.e. if the
state says long mode is active but not enabled.  Unlike VMX, SVM doesn't
have an explicit consistent check for the illegal combination; presumably
hardware simply ignores EFER.LMA if EFER.LME=0.

Unfortunately, KVM doesn't ignore EFER.LMA in this case and consumes the
illegal state when constructing the shadow MMU for L2.  E.g. if userspace
also clears CR4.PAE, then kvm_calc_cpu_role() will compute a role with 4 or
5 levels of paging, but shadow_mmu_init_context() will wire up the MMU to
use the paging32 template, which maxes out its levels at 2.

Note, the "real badness" is effectively the same as what happened with the
nVMX bug fixed by commit 112e66017bff ("KVM: nVMX: add missing consistency
checks for CR0 and CR4").  Unfortunately, the sanity check added by commit
72e2fb24a0b0 ("KVM: x86/mmu: Bug the VM if a vCPU ends up in long mode
without PAE enabled") doesn't work for this case, since L2 state is active
at the time of the page fault, but it's L1 that has the bad state.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-99345

### CVE-2026-99346 — HIGH (CVSS: 8.8)

- Published: 2026-11-19T15:17:45.830
- Description: In the Linux kernel, the following vulnerability has been resolved:

KVM: SVM: Trigger new ASID allocation in both VMCBs on pCPU switch

When the pCPU where the VMCB was most recently used is switched, reset
the ASID generation in both VMCBs, triggering new ASID allocation for
the immediate VMRUN as well as the next VMRUN on the other VMCB.

The ASID is shared between vmcb01 and vmcb02, and gets flushed on every
nested transition. However, since pCPU tracking is done per VMCB, it is
possible for one VMCB to allocate a new ASID when migrated to a new
pCPU, and then the other VMCB reuses that ASID on the old pCPU. This can
result in the same ASID being used by multiple vCPUs on the old pCPU.

Example scenario:
- vCPU runs on pCPU A, vmcb01 is active, asid=1.
- vCPU migrates to pCPU B, vmcb01 pCPU changes, new asid=2.
- Another vCPU runs on pCPU A and allocates asid=2 as well.
- vCPU migrates back to pCPU A, and then switches to vmcb02 before it
  runs again with vmcb01.
- No pCPU switch is detected for vmcb02, so VMRUN is done with asid=2.
- Two vCPUs end up using asid=2 on the same pCPU.

Keep the VMCB dirtying to the active VMCB only. Clean bits are tracked
by a pCPU for each VMCB, so do not unnecessarily dirty a VMCB if its
pCPU does not change.

Additionally, initialize the tracked pCPU for vmcb02 to -1 on nested
enablement as hardening, so that a new ASID allocation is always
triggered when nested is disabled and re-enabled.

No performance regression was noticed when overcommitting L1 vCPUs in L0
(to force rescheduling), pinning L1 <-> L2 vCPUs, and running CPUID in a
tight loop bouncing between 2 vCPUs in L2.

An alternative (and perhaps more proper) fix would be tracking the ASID
per-VMCB instead (e.g. [1]). However, that's a more involved change, and
it would result in having different ASIDs for L1 and L2 without actually
properly maintaining them. It would probably work because all TLB
flushes target the current VMCB, and the other VMCB is always flushed on
nested transitions, but the code ends up in an arguably more fragile
state. Punt a proper clean fix to an incoming (and overdue) overhaul of
SVM's ASID usage [2].

[1] https://lore.kernel.org/lkml/20250205182402.2147495-2-yosry.ahmed@linux.dev
[2] https://lore.kernel.org/kvm/20260728003557.1136583-1-yosry@kernel.org
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-99346
