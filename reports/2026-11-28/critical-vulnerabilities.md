# Critical Vulnerability Watch

Generated: 2026-11-28 13:24 UTC
Records included: 63

## Data Sources

- National Vulnerability Database (NVD)
- CISA Known Exploited Vulnerabilities (KEV)

## AI Analyst Summary

Gemini AI analysis was unavailable. The collected vulnerability records are retained below for manual review.

## Vulnerability Findings

### CVE-2025-61963 — HIGH (CVSS: 8.4)

- Published: 2026-11-21T15:17:06.070
- Description: Improper input validation within the AmdPlatformRasSmm driver could allow an attacker with privileged access to overwrite SMRAM, potentially resulting in arbitrary code execution.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2025-61963

### CVE-2026-74127 — CRITICAL (CVSS: 9.4)

- Published: 2026-11-21T15:17:10.487
- Description: Improper verification of a cryptographic signature in the PSP Boot ROM of AMD Zeppelin (Zen1/Zen+) processors could allow an attacker with local access to the SPI flash to bypass secure boot authentication, potentially resulting in arbitrary unsigned code execution at full Platform Security Processor privilege, loss of confidentiality, loss of integrity of the host boot chain, and persistent loss of availability.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-74127

### CVE-2026-133985 — HIGH (CVSS: 7.4)

- Published: 2026-11-21T16:16:38.730
- Description: A flaw has been found in TRENDnet TEW-657BRM 1.00.1. Affected by this issue is some unknown functionality of the file /usr/sbin/restore_config.cgi. Executing a manipulation can lead to out-of-bounds read. The attack may be launched remotely. The exploit has been published and may be used. The vendor explains: "I am not able to confirm if such vulnerability exists as the product has been EOL for more than 15 years. We will send out an announcement letting customers know." This vulnerability only affects products that are no longer supported by the maintainer.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133985

### CVE-2026-124626 — CRITICAL (CVSS: 9.1)

- Published: 2026-11-21T17:16:39.777
- Description: @fastify/express is a compatibility layer that lets Express middleware run inside the Fastify web framework. In versions 4.0.5 through 4.0.9, the plugin matches path-scoped Express middleware with a matcher that requires a non-empty value for a dynamic segment, while Fastify's router accepts an empty parameter or wildcard value. When a route and an Express middleware mount share a dynamic pattern, a request with an empty segment matches the Fastify route and runs the handler while the middleware mounted on that pattern is skipped, so on a scoped mount an unauthenticated request can reach a protected handler. No special configuration is required, and the practical impact depends on what the empty value selects in the application. The issue is fixed in @fastify/express 4.0.10, and users should upgrade to 4.0.10 or later.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-124626

### CVE-2026-129504 — CRITICAL (CVSS: 9.1)

- Published: 2026-11-21T17:16:39.920
- Description: @fastify/express is a compatibility layer that lets Express middleware run inside the Fastify web framework. In versions 4.0.0 through 4.0.9, the plugin joins a path-scoped middleware's mount path to the Fastify plugin prefix by string concatenation, so when the plugin prefix ends with a slash or the mount path omits its leading slash, the resulting Express mount path does not line up with the route the Fastify router serves. Express then fails to match and passes the request on while the Fastify router still dispatches the route, so the middleware is silently skipped. An application that uses path-scoped Express middleware for authentication or authorization inside a prefixed plugin can expose protected routes to unauthenticated clients, with no crafted request and no non-default option required, and string, array, and regular-expression mount paths are all affected. The issue is fixed in @fastify/express 4.0.10, and users should upgrade to 4.0.10 or later.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129504

### CVE-2026-129850 — HIGH (CVSS: 7.4)

- Published: 2026-11-21T17:16:40.043
- Description: @fastify/express is a compatibility layer that lets Express middleware run inside the Fastify web framework. In versions 4.0.0 through 4.0.9, when Fastify routing is configured to be case-insensitive, the router folds the request path to lower case in a way that maps certain non-ASCII Unicode characters to ASCII letters, but @fastify/express matches Express mount paths against the decoded path without applying the same folding. The two disagree, so a request that spells a letter of a mount path with an equivalent Unicode character is routed to the protected handler while the path-scoped middleware mounted on that path never matches and is skipped. An unauthenticated client can therefore reach a handler that an authentication, authorization, or rate-limiting middleware was meant to protect, though only when the application enables case-insensitive routing and the mount path contains an affected letter. The issue is fixed in @fastify/express 4.0.10, and users should upgrade to 4.0.10 or later.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129850

### CVE-2026-133120 — CRITICAL (CVSS: 9.1)

- Published: 2026-11-21T17:16:40.170
- Description: @fastify/express is a compatibility layer that lets Express middleware run inside the Fastify web framework. In versions before 4.0.10, the plugin passes Express a request URL that does not always match the path Fastify's router dispatched, so path-scoped Express middleware can be skipped while the route handler still runs. Several request forms trigger the mismatch, including percent-decoding that rewrites a backslash to a slash or double-decodes an encoded percent sign, and a request target that begins with an asterisk, so the middleware and the handler disagree on the path or on parameter and query values. An unauthenticated client can therefore reach a handler that an authentication, authorization, or rate-limiting middleware was meant to protect, with no special configuration required. The issue is fixed in @fastify/express 4.0.10, and users should upgrade to 4.0.10 or later.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133120

### CVE-2026-133250 — CRITICAL (CVSS: 9.1)

- Published: 2026-11-21T17:16:40.293
- Description: @fastify/middie is the middleware engine for the Fastify web framework. In versions up to and including 9.3.7, middie matches path-scoped middleware against its own reading of the request path, which can differ from the path Fastify's router uses to dispatch the request. When the two disagree, the router can route a request to a handler covered by a middleware mount while middie skips that middleware, so an unauthenticated client reaches a handler that an authentication, authorization, or rate-limiting middleware was meant to protect, with no special configuration required. The mismatch is triggered by empty parameter or wildcard values, request targets that do not begin with a slash, and literal percent characters in a mount path. The issue is fixed in @fastify/middie 9.3.8, and users should upgrade to 9.3.8 or later.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133250

### CVE-2026-133867 — CRITICAL (CVSS: 9.1)

- Published: 2026-11-21T17:16:40.663
- Description: @fastify/express is a compatibility layer that lets Express middleware run inside the Fastify web framework. In versions 4.0.7 through 4.0.9, the plugin does not rewrite regular-expression mount paths to account for a parameterized plugin prefix, so when middleware is mounted with a regular expression inside a plugin registered under a parameterized prefix, the Express matcher treats the prefix parameter as literal text and never matches the real request path. As a result, Express silently skips that middleware while Fastify still runs the route handler, so an application that relies on regular-expression mounted middleware for authentication or authorization inside a parameterized-prefix plugin exposes protected routes to unauthenticated clients. No special configuration is required beyond a parameterized prefix and a regular-expression mount. The issue is fixed in @fastify/express 4.0.10, and users should upgrade to 4.0.10 or later.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133867

### CVE-2026-134242 — HIGH (CVSS: 8.2)

- Published: 2026-11-21T17:16:41.093
- Description: Parse Server 2.5.0 before 8.6.121 and 9.0.0 before 9.11.1-alpha.1 does not handle a failure to serialize an object after a beforeSave trigger, leaving the request unsettled and terminating the server process. A remote attacker able to update an object in a class with a beforeSave trigger can send a dot notation key below a non-object field, such as a timestamp, to crash the server for all clients.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134242

### CVE-2026-134245 — HIGH (CVSS: 8.7)

- Published: 2026-11-21T17:16:41.657
- Description: SiYuan 3.8.0 before 3.8.10 contains an incorrect authorization vulnerability in the serveAssets route that allows unauthenticated attackers to read password-protected document assets via name collisions. Attackers can request GET /assets/<name> when a visible document references the same relative asset name, retrieving the protected file's contents on public-publish instances with Basic Auth disabled.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134245

### CVE-2026-134246 — HIGH (CVSS: 8.7)

- Published: 2026-11-21T17:16:41.833
- Description: SiYuan 3.6.0 before 3.6.2 and 3.7.3 before 3.8.10 contains a missing authorization vulnerability in the /api/block/getDOMText endpoint, which renders caller-supplied DOM without checking publish access for referenced image paths. When publish authentication is disabled, anonymous visitors can submit DOM referencing a known unpublished, non-encrypted asset path to retrieve its already-cached OCR text.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134246

### CVE-2026-134247 — HIGH (CVSS: 8.7)

- Published: 2026-11-21T17:16:42.027
- Description: SiYuan 3.8.0 before 3.8.10 contains an incorrect authorization vulnerability that allows anonymous attackers to read indexed asset text referenced only by publish-disabled attribute-view rows. Attackers can request /api/asset/getDocAssets on a public host document to obtain the leaked asset path, then query /api/search/getAssetContentByPath to retrieve the confidential file's full indexed text.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134247

### CVE-2026-134248 — HIGH (CVSS: 8.3)

- Published: 2026-11-21T17:16:42.197
- Description: SiYuan 3.6.0 before 3.8.10 contains an information disclosure vulnerability that allows authenticated Readers to read protected documents through block-reference footnote resolution in Markdown export. Attackers can request copyStdMarkdown for a public document referencing a hidden, disabled, or password-protected document to disclose its body text without the publish password.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134248

### CVE-2026-134249 — HIGH (CVSS: 8.7)

- Published: 2026-11-21T17:16:42.373
- Description: SiYuan before 3.8.10 contains an authentication bypass vulnerability that allows unauthenticated attackers to gain Administrator role by spoofing X-Forwarded-For through a loopback-trusted reverse proxy. Attackers can send requests with Host set to localhost and X-Forwarded-For set to 127.0.0.1 to read private note-history contents via the /history/*path route when no lock-screen password is set.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134249

### CVE-2026-134250 — HIGH (CVSS: 8.8)

- Published: 2026-11-21T17:16:42.550
- Description: Grav Form plugin 1.1.0 before 9.1.40 contains a stored cross-site scripting vulnerability in Form::uploadFiles(), which sanitizes SVG only when a file's last extension is .svg and accepts markup under unrecognized extensions. Anonymous attackers can upload files like drawing.svg.foo through public any-type upload forms, running script in an administrator's session when opened, enabling super-admin creation on Grav 2.x with Admin2.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134250

### CVE-2026-134253 — HIGH (CVSS: 8.7)

- Published: 2026-11-21T17:16:42.870
- Description: Grav API plugin from 1.0.0 before 1.1.4 contains a remote code execution vulnerability that allows publishers with media and page write rights to write theme template files through the blueprint-upload endpoint. Attackers can upload a file into a theme's Twig templates folder and include it from sandboxed page Twig to execute commands as the web-server user.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134253

### CVE-2026-134254 — HIGH (CVSS: 7.1)

- Published: 2026-11-21T17:16:43.050
- Description: Admidio from 5.0.0 before 5.0.18 contains a path traversal vulnerability in DocumentsService::renameFile() that allows authenticated users to move files outside adm_my_files by supplying an unvalidated adm_new_name value. Attackers with folder upload permission can submit ../ sequences to file_rename_save to write files and create directories in arbitrary writable locations, including the web root.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134254

### CVE-2026-134258 — CRITICAL (CVSS: 9.3)

- Published: 2026-11-21T17:16:43.747
- Description: Admidio 5.0.0 before 5.0.18 contains a path traversal vulnerability in the Documents & Files renameFile() action that allows authenticated users with folder upload rights to move files outside adm_my_files by supplying ../ sequences in adm_new_name. Attackers can relocate an uploaded SVG containing script to the web root, where it is served inline and executes stored cross-site scripting against administrators for account takeover.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134258

### CVE-2026-134261 — HIGH (CVSS: 7.1)

- Published: 2026-11-21T17:16:44.253
- Description: Admidio before 5.0.18 contains an insecure direct object reference vulnerability in mylist.php that loads list configurations by the list_uuid parameter while checking only the organization, not the owner or private flag. Authenticated users with Lists module access who know a victim's list UUID can read its name, selected profile fields, sort order and filter conditions.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134261

### CVE-2026-134262 — CRITICAL (CVSS: 9.2)

- Published: 2026-11-21T17:16:44.420
- Description: Admidio 5.0.0 before 5.0.18 contains a stored cross-site scripting vulnerability that allows role administrators to inject JavaScript by placing quote-breaking payloads in role names rendered unencoded in the data-message attribute in modules/profile/roles_functions.php. Attackers can execute scripts when a full administrator views an affected profile page, stealing the CSRF token to assign themselves the Administrator role.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134262

### CVE-2026-134264 — HIGH (CVSS: 7.1)

- Published: 2026-11-21T17:16:44.600
- Description: Admidio from 5.0.2 before 5.0.17 contains an arbitrary file read vulnerability that allows any logged-in member to read server files by placing local paths in img src attributes of eCard messages. Attackers can send an eCard to their own account so sendEcard() embeds files like adm_my_files/config.php via addEmbeddedImage(), disclosing database credentials and /etc/passwd.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134264

### CVE-2026-134265 — HIGH (CVSS: 7.1)

- Published: 2026-11-21T17:16:44.767
- Description: Vikunja from 2.4.0 before 2.8.0 contains a denial of service vulnerability in the richtext converter that allows authenticated project writers to exhaust server memory and CPU by storing tables with unbounded rowspan and colspan values. Any project reader or CalDAV client can trigger the expansion through markdown task reads, CalDAV GETs, or the frontend editor, producing 100 MB responses from a 64-byte description.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134265

### CVE-2026-134266 — HIGH (CVSS: 7.1)

- Published: 2026-11-21T17:16:44.947
- Description: Vikunja from 0.19.0 before 2.8.0 contains a denial of service vulnerability that allows authenticated users to exhaust CPU by supplying unbounded business-day operands in datemath filters. Attackers can send task or time-tracking filters like due_date > now+999999999999b, triggering a per-day loop in go-datemath that pins CPU cores and exhausts the server.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134266

### CVE-2026-134268 — HIGH (CVSS: 7.1)

- Published: 2026-11-21T17:16:45.290
- Description: Vikunja from 0.21.0 before 2.8.0 contains a resource exhaustion vulnerability that allows authenticated users to trigger instance-wide database writes by setting a project position below 0.1. Attackers can repeatedly send PUT requests to /api/v2/projects/{id} so recalculateProjectPositions updates every user's root projects, holding SQLite's write lock and degrading availability.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134268

### CVE-2026-134269 — HIGH (CVSS: 7.1)

- Published: 2026-11-21T17:16:45.463
- Description: Vikunja from 0.18.0 before 2.8.0 contains a resource amplification vulnerability in pkg/models/export.go that allows authenticated users to exhaust server memory by exporting heavily related tasks. Attackers can relate many tasks to one task with a large description and request a user export, causing an out-of-memory crash for all users.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134269

### CVE-2026-134270 — HIGH (CVSS: 7.1)

- Published: 2026-11-21T17:16:45.643
- Description: Vikunja from 0.19.0 before 2.8.0 contains a denial of service vulnerability that allows authenticated CalDAV users to exhaust server CPU by uploading VTODO properties with many parameters. Attackers can PUT an iCalendar body with thousands of parameters on one line to any valid project ID, triggering superlinear parsing before permission checks.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134270

### CVE-2026-134271 — HIGH (CVSS: 7.1)

- Published: 2026-11-21T17:16:45.810
- Description: Vikunja from 1.0.0 before 2.8.0 contains a memory exhaustion vulnerability that allows authenticated users to crash the server by uploading extreme-width images as task attachments. Attackers can request the attachment preview endpoint so Lanczos resampling allocates width-proportional weight tables, OOM-killing the process repeatedly with sub-megabyte PNGs.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134271

### CVE-2026-134273 — HIGH (CVSS: 7.1)

- Published: 2026-11-21T17:16:46.150
- Description: Vikunja from 2.6.0 before 2.8.0 contains a resource exhaustion vulnerability in the Planka migration converter that multiplies task allocations for duplicate list IDs. Attackers controlling a Planka server can return boards with duplicate list IDs and many cards to exhaust memory and OOM-kill the Vikunja process.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134273

### CVE-2026-134275 — HIGH (CVSS: 7.1)

- Published: 2026-11-21T17:16:46.320
- Description: Vikunja from 0.8.0 before 2.8.0 contains a denial of service vulnerability that allows authenticated project readers to amplify response size by repeating requested properties in CalDAV PROPFIND requests. Attackers can send PROPFIND requests to the dav projects endpoint with hundreds of duplicate calendar-data properties to exhaust server memory, CPU, and bandwidth.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134275

### CVE-2026-134278 — HIGH (CVSS: 7.1)

- Published: 2026-11-21T17:16:46.833
- Description: Vikunja 2.3.0 before 2.8.0 contains an uncontrolled memory allocation in the CSV migration module because it does not de-duplicate label column mappings or cap labels per row, and enforces the item limit only after the full import is built. Authenticated users can send one request to /api/v2/migration/csv/migrate with repeated label mappings or many labels per row, exhausting memory until the server is OOM-killed.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134278

### CVE-2026-134282 — HIGH (CVSS: 8.6)

- Published: 2026-11-21T17:16:47.537
- Description: Vikunja from 0.14.0 before 2.8.0 contains a mass assignment vulnerability that allows authenticated users to set json-hidden fields by sending XML request bodies to the v1 API. Attackers can set BackgroundFileID on project creation to download any stored file via the background endpoint, or create bots with IsAdmin set to gain instance-admin access.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134282

### CVE-2026-134284 — HIGH (CVSS: 7.7)

- Published: 2026-11-21T17:16:47.710
- Description: Vikunja from 1.0.0 before 2.8.0 contains an account takeover vulnerability that allows attackers to hijack SSO identities by planting local accounts with unverified victim emails. When emailfallback is enabled, attackers register or edit a local account using the victim's email, causing the victim's first OIDC login to link into the attacker-controlled account and expose their data.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134284

### CVE-2026-134287 — CRITICAL (CVSS: 9.2)

- Published: 2026-11-21T17:16:48.030
- Description: OpenRemote core before 1.34.0 contains an authentication bypass vulnerability in UserAssetProvisioningMQTTHandler that allows unauthenticated attackers to impersonate provisioned devices without proof of private key possession. Attackers can publish a known device's public certificate to the provisioning request topic, authenticating their anonymous MQTT connection as the device's service account to read and modify assets.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134287

### CVE-2026-134288 — HIGH (CVSS: 7.1)

- Published: 2026-11-21T17:16:48.207
- Description: SurrealDB 3.0.0 before 4.0.0 contains an authorization bypass vulnerability that allows clients with table write access to persist writes refused by THROWing table events within interactive transactions. Attackers can run a guarded statement via RPC begin and query, ignore the returned error, and commit to persist the record and event side effects.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134288

### CVE-2026-134290 — HIGH (CVSS: 7.1)

- Published: 2026-11-21T17:16:48.553
- Description: SurrealDB 2.2.0 before 4.0.0 includes the record id of a referencing row in the error returned when a delete is blocked by an ON DELETE REJECT reference, without checking the caller's SELECT permission on that row. An authenticated principal with DELETE permission can attempt to delete a referenced record and read the rejection error to learn the existence and exact ids of referencing records hidden by row-level SELECT permissions.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134290

### CVE-2026-134291 — HIGH (CVSS: 8.7)

- Published: 2026-11-21T17:16:48.727
- Description: SurrealDB 3.0.0 before 4.0.0 contains a path traversal vulnerability in its filesystem storage bucket that only canonicalizes the bucket root, not descendant symlinks. Attackers can reference paths through a pre-existing symlink inside the bucket that pass the lexical prefix check, reading and writing files across the host filesystem.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134291

### CVE-2026-134292 — CRITICAL (CVSS: 9.3)

- Published: 2026-11-21T17:16:48.897
- Description: SurrealDB 1.0.0 before 4.0.0 contains a capability check bypass in its embedded JavaScript scripting engine, where the surrealdb.functions bridge calls the internal fnc::synchronous() and fnc::asynchronous() dispatchers without enforcing function capability checks. Authenticated users denied access to built-in functions in SurrealQL can execute them by calling them through surrealdb.functions from embedded JavaScript.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134292

### CVE-2026-134293 — HIGH (CVSS: 8.8)

- Published: 2026-11-21T17:16:49.057
- Description: SurrealDB 3.1.0 before 4.0.0 contains an SQL injection vulnerability in its Model Context Protocol (MCP) server because the identifier validator (consume_backtick_ident and validate_identifier) treats the first backtick as the closing delimiter, ignoring escape characters that the SurrealQL parser honors. Attackers can supply MCP tool arguments containing an escaped backtick to break out of the quoted identifier and execute arbitrary SurrealQL statements.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134293

### CVE-2026-134294 — HIGH (CVSS: 8.7)

- Published: 2026-11-21T17:16:49.223
- Description: SurrealDB 3.0.0 before 4.0.0 contains a path traversal vulnerability in its bucket storage layer on Windows, where ObjectKey::check_no_traversal splits object keys only on forward slashes while FileStore::to_os_path treats backslashes as directory separators. Attackers can supply object keys such as /..\bucket2\secret to bypass the traversal check and read or modify files in other buckets.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134294

### CVE-2026-134295 — HIGH (CVSS: 8.7)

- Published: 2026-11-21T17:16:49.393
- Description: SurrealDB 3.0.0 before 4.0.0 contains a path traversal vulnerability in direct filesystem buckets because BucketController::check_permission evaluates key-based ACLs against the un-normalized object key, while FileStore::to_os_path collapses '..' sequences without a traversal check. An authenticated tenant permitted only for certain keys can supply a key such as /public/../private/confidential.txt to read, write, or delete arbitrary files within the storage root.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134295

### CVE-2026-134299 — HIGH (CVSS: 8.7)

- Published: 2026-11-21T17:16:49.743
- Description: SurrealDB 3.0.4 before 4.0.0 does not apply operator-configured WebSocket frame, message, and buffer size limits to the GraphQL WebSocket upgrade handler at GET /graphql, falling back to permissive library defaults. Unauthenticated remote attackers who supply the target namespace and database in request headers can hold up to 64 MiB of in-flight data per concurrent connection, exhausting server memory and degrading availability.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134299

### CVE-2026-134300 — HIGH (CVSS: 7.2)

- Published: 2026-11-21T17:16:49.917
- Description: SurrealDB from 2.2.0 before 4.0.0 contains an authorization bypass vulnerability in Document::purge_references that lets authenticated users bypass target table PERMISSIONS by triggering REFERENCE ON DELETE cascades. Attackers can delete a referenced record to delete, unset, or run CUSTOM expressions on referencing records despite PERMISSIONS FOR delete or update NONE.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134300

### CVE-2026-134302 — HIGH (CVSS: 7.1)

- Published: 2026-11-21T17:16:50.267
- Description: SurrealDB 1.0.0 before 4.0.0 contains a denial of service vulnerability that allows any user able to run queries to crash the server by triggering unchecked decimal overflow in math::sum or math::product. Attackers can submit a query summing or multiplying large decimal literals or aggregate stored decimals with GROUP ALL, causing a rust_decimal panic that terminates the entire server process.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134302

### CVE-2026-134303 — HIGH (CVSS: 8.3)

- Published: 2026-11-21T17:16:50.480
- Description: SurrealKV before 1.1.0 contains an out-of-bounds read vulnerability in the safe InternalKeyRef::from_encoded constructor, which only checks key length with a debug-only assertion. Callers passing keys shorter than 16 bytes, or crafted or corrupted SSTable blocks, trigger unchecked length underflow in timestamp(), seq_num() and trailer(), reading heap bytes before the allocation or panicking.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134303

### CVE-2026-134307 — HIGH (CVSS: 7.1)

- Published: 2026-11-21T17:16:50.820
- Description: SurrealDB 3.0.0 before 4.0.0 contains a permission bypass vulnerability that allows authenticated low-privilege database users to read restricted records by calling the GET /export endpoint. Attackers can export raw records that skip table SELECT predicates and field-level SELECT permissions, exposing other users' rows and hidden fields.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134307

### CVE-2026-134309 — HIGH (CVSS: 8.7)

- Published: 2026-11-21T17:16:50.990
- Description: SurrealDB 1.0.0 before 4.0.0 contains an authorization bypass vulnerability that allows authenticated users to shadow protected $access, $auth, and $token variables by binding them as FOR loop variables. Attackers can wrap queries in nested FOR loops with forged values to satisfy table permission predicates, enabling unauthorized reads, modifications, or deletions as a VIEWER.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134309

### CVE-2026-134310 — HIGH (CVSS: 7.1)

- Published: 2026-11-21T17:16:51.180
- Description: SurrealDB from 3.2.0 before 3.3.4 contains an authorization bypass vulnerability that allows record users to update protected rows by exploiting table-level PERMISSIONS FOR update predicates referencing COMPUTED fields. Because check_update_permissions evaluates the predicate before computed fields are populated, the field reads as NONE and deny-intended predicates like blocked != true pass, letting attackers modify records.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134310

### CVE-2026-134311 — HIGH (CVSS: 7.6)

- Published: 2026-11-21T17:16:51.387
- Description: better-auth 1.3.0 before 1.7.16 and 1.8.0-beta.0 before 1.8.0-beta.5 contains an incorrect authorization vulnerability in the admin plugin's /admin/update-user endpoint that lets roles holding user:update change another user's phoneNumber and phoneNumberVerified fields. Attackers can set their own verified phone number on a higher-privileged account and sign in via phone OTP to take it over.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134311

### CVE-2026-134312 — HIGH (CVSS: 7.4)

- Published: 2026-11-21T17:16:51.567
- Description: Better Auth 0.4.9 before 1.7.16 and 1.8.0-beta.0 before 1.8.0-beta.5 contains an OAuth sign-in authentication flaw that treats unverified provider emails as verified, including string "false" email_verified claims, unchecked generic OAuth profile/ID-token subject mismatches, and ignored Zoom provider options. Attackers holding a victim's address unverified at an affected provider can sign in, link to the victim's local account, and obtain its session.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134312

### CVE-2026-134313 — HIGH (CVSS: 7.6)

- Published: 2026-11-21T17:16:52.017
- Description: Better Auth (better-auth, @better-auth/kysely-adapter, and @better-auth/drizzle-adapter) before 1.7.16 and 1.8.0-beta.0 before 1.8.0-beta.5 contains a race condition with MySQL or MariaDB serial IDs because the inserted row's ID is read via a separate LAST_INSERT_ID() query that may run on a different pooled connection. Under concurrent load, a user signing in can receive another user's session and act as that user.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134313

### CVE-2026-134315 — HIGH (CVSS: 7.4)

- Published: 2026-11-21T17:16:52.377
- Description: better-auth 1.4.0 before 1.7.16 and 1.8.0-beta.0 before 1.8.0-beta.5 contains an improper authentication vulnerability because email-change links record the old and new addresses but not the requesting user. Attackers can open a still-valid link issued for their own account after a victim registers the attacker's released old address, gaining a session and changing the victim's email to one they control.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134315

### CVE-2026-134316 — HIGH (CVSS: 8.6)

- Published: 2026-11-21T17:16:52.550
- Description: @better-auth/electron 1.5.0-beta.12 before 1.7.16 and 1.8.0-beta.0 before 1.8.0-beta.5 accepts any validly signed value as its transfer cookie and returns the full endpoint context, including the auth secret and social provider client secrets, in sign-in responses. Authenticated users can obtain these secrets to forge sessions as other users. Attackers knowing a password can exchange desktop authorization codes issued before two-factor verification to bypass the second factor.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134316

### CVE-2026-134322 — HIGH (CVSS: 8.6)

- Published: 2026-11-21T17:16:53.363
- Description: better-auth 0.4.12-beta.7 before 1.7.16 and 1.8.0-beta.0 before 1.8.0-beta.5 contains an improper authentication vulnerability in the phone number plugin that lets sign-up and other flows save unverified phone numbers, which phone OTP sign-in then uses to select the account. Attackers can attach a victim's number to an attacker-controlled account so the victim's valid OTP sign-in yields a session for that account, exposing data the victim then enters.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134322

### CVE-2026-134325 — HIGH (CVSS: 8.7)

- Published: 2026-11-21T17:16:53.720
- Description: ArcadeDB before 26.11.1 contains a denial of service vulnerability in the Redis protocol handler, which neither replies to nor closes a pre-authentication connection when it receives an array whose first element is not a string. Unauthenticated attackers can resend such an array just within the 30-second socket idle timeout to hold connections open indefinitely and exhaust RedisNetworkExecutor threads.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134325

### CVE-2026-134327 — HIGH (CVSS: 7.1)

- Published: 2026-11-21T17:16:53.890
- Description: ArcadeDB before 26.11.1 contains an authorization bypass vulnerability that allows authenticated users to read schema definitions of denied types through listings ignoring per-type ACLs. Attackers can query the PostgreSQL wire catalog, GraphQL introspection, or MCP get_schema to reveal property names, indexes, inheritance, and materialized view SQL.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134327

### CVE-2026-134329 — HIGH (CVSS: 7.1)

- Published: 2026-11-21T17:16:54.060
- Description: ArcadeDB 26.2.1 before 26.11.1 contains an observable response discrepancy in MCPToolUtils.resolveDatabase, which checks database existence before authorization and returns distinct 'not authorized' and 'does not exist' errors; separately, a failed Bolt LOGON from READY leaves the previous principal bound after RESET. Authenticated MCP callers can enumerate names of databases they are not granted by probing tools such as query or get_schema.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134329

### CVE-2026-134334 — HIGH (CVSS: 7.1)

- Published: 2026-11-21T17:16:54.220
- Description: ArcadeDB from 26.7.1 before 26.11.1 contains an information disclosure vulnerability because LSMTreeFullTextIndex computes BM25 corpus statistics over all buckets of the indexed type, ignoring bucket access control on subtypes. Authenticated users with read access to a supertype but not its subtype can run EXPLAIN or PROFILE on full-text queries and read totalDocs and per-term df values to count hidden subtype documents containing chosen terms.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134334

### CVE-2026-134337 — HIGH (CVSS: 8.7)

- Published: 2026-11-21T17:16:54.557
- Description: ArcadeDB native-image server builds 26.8.1 before 26.11.1 contain an authorization bypass vulnerability that allows authenticated clients to perform writes through read-only query paths by nesting statements in SELECT. Missing reflection metadata leaves SqlAstInspector with an empty AST, letting INSERT in projections or LET clauses persist via the query endpoint, MCP read-only mode, and HA follower routing.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134337

### CVE-2026-134338 — HIGH (CVSS: 8.7)

- Published: 2026-11-21T17:16:54.730
- Description: ArcadeDB 25.8.1 before 26.11.1 contains an incorrect authorization vulnerability because per-type ACLs are keyed by type name, renames are not propagated to the permission configuration, and requestAccessOnType allows unknown type names by default. Authenticated users holding only updateSchema can run ALTER TYPE NAME on a denied type to gain read, DELETE and TRUNCATE access, immediately for TIMESERIES types and after the next security rebuild for record-backed types.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134338

### CVE-2026-134339 — HIGH (CVSS: 8.7)

- Published: 2026-11-21T17:16:54.900
- Description: ArcadeDB from 26.11.1-SNAPSHOT before 26.11.1 contains an authorization bypass vulnerability that allows authenticated users to skip per-type ACL checks when a database is opened on demand. Attackers can send the first POST /api/v1/batch/{database} request to a closed database to read and write types they are not entitled to access.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134339

### CVE-2026-134341 — HIGH (CVSS: 8.7)

- Published: 2026-11-21T17:16:55.073
- Description: actix-http 3.0.0 before 3.20.3 contains a denial of service vulnerability that allows unauthenticated remote attackers to exhaust memory by sending large-window brotli request bodies. Attackers can send an 850-byte body with Content-Encoding: br declaring a 2^30 window, forcing about 1 GiB of decoder allocation per request and OOM-killing servers.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134341

### CVE-2026-134347 — HIGH (CVSS: 8.7)

- Published: 2026-11-21T17:16:55.373
- Description: actix-files before 0.7.4 contains an information disclosure vulnerability that allows remote unauthenticated attackers to read hidden files by requesting Windows 8.3 short-name aliases. Attackers can request short names like ENV~1 or GIT~1/config to bypass the leading-dot check in actix_files::Files and retrieve .env secrets and .git contents.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-134347
