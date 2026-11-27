# Critical Vulnerability Watch

Generated: 2026-11-27 14:07 UTC
Records included: 48

## Data Sources

- National Vulnerability Database (NVD)
- CISA Known Exploited Vulnerabilities (KEV)

## AI Analyst Summary

Gemini AI analysis was unavailable. The collected vulnerability records are retained below for manual review.

## Vulnerability Findings

### CVE-2026-128996 — HIGH (CVSS: 7.1)

- Published: 2026-11-20T14:17:44.730
- Description: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Tomdever wpForo Forum wpforo allows Stored XSS.This issue affects wpForo Forum: from n/a through 3.2.4.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-128996

### CVE-2026-129017 — HIGH (CVSS: 7.1)

- Published: 2026-11-20T14:17:44.883
- Description: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Gemini Labs Site Reviews site-reviews allows Stored XSS.This issue affects Site Reviews: from n/a through 8.3.7.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129017

### CVE-2026-129039 — CRITICAL (CVSS: 9.8)

- Published: 2026-11-20T14:17:45.273
- Description: Deserialization of Untrusted Data vulnerability in Tribulant Software Newsletters newsletters-lite allows Object Injection.This issue affects Newsletters: from n/a through 4.18.2.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129039

### CVE-2026-129043 — CRITICAL (CVSS: 9.3)

- Published: 2026-11-20T14:17:45.410
- Description: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Tribulant Software Newsletters newsletters-lite allows SQL Injection.This issue affects Newsletters: from n/a through 4.18.2.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129043

### CVE-2026-129074 — HIGH (CVSS: 7.1)

- Published: 2026-11-20T14:17:45.657
- Description: Missing Authorization vulnerability in miniOrange miniOrange's Google Authenticator miniorange-2-factor-authentication allows Exploiting Incorrectly Configured Access Control Security Levels.This issue affects miniOrange's Google Authenticator: from n/a through 6.6.0.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129074

### CVE-2026-14914 — CRITICAL (CVSS: 10.0)

- Published: 2026-11-20T14:17:53.043
- Description: Unrestricted upload of file with dangerous type vulnerability in Tegsoft Yönetim ve Bilişim Hizmetleri Tic. Ltd. Şti. Tegsoft Contact Center allows Upload a Web Shell to a Web Server.

This issue affects Tegsoft Contact Center: before latest-202611161510.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-14914

### CVE-2026-80188 — CRITICAL (CVSS: 9.8)

- Published: 2026-11-20T14:17:54.003
- Description: The BuddyBoss Addons plugin for WordPress is vulnerable to Authentication Bypass leading to Account Takeover in versions up to, and including, 1.2.1. This is due to the Social Login REST endpoint trusting unverified Apple and Facebook identity-token claims and linking an attacker-controlled provider identifier to an existing WordPress user selected by the token’s email claim. This makes it possible for unauthenticated attackers who know a user’s email address to associate their provider identity with that account, including administrator accounts, and subsequently authenticate as the victim. Successful exploitation requires the BuddyBoss Platform plugin to be installed and active, with the Social Login module and selected provider enabled and configured. On sites with the separate BuddyBoss App JWT component, the vulnerable REST request can return an application token immediately.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-80188

### CVE-2026-126054 — CRITICAL (CVSS: 9.3)

- Published: 2026-11-20T15:17:39.943
- Description: A Path Traversal vulnerability in workspace directory handling and Git integration in Google Cloud Dataform, BigQuery Studio and Colab Enterprise on Google Cloud Platform allows an authenticated remote attacker to read private files and create arbitrary files across tenant repositories using crafted workspace operations and Git integration requests.


This vulnerability was patched on 10 October 2026, and no customer action is needed.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126054

### CVE-2026-127027 — CRITICAL (CVSS: 9.2)

- Published: 2026-11-20T15:17:40.763
- Description: Poste.io is vulnerable to remote code execution in DMARC report processing. Email sent to dmarc-reports@<domain> is saved without sender verification. Script that runs as root unpacks the attachments using unsafe shell commands, allowing command injection through crafted attachments (e.g. file names or archive contents). A remote unauthenticated attacker who can send an email to the server's port 25 can execute arbitrary commands as root within the Poste.io container.


This issue was fixed in version 2.5.22.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-127027

### CVE-2026-132658 — CRITICAL (CVSS: 9.4)

- Published: 2026-11-20T15:17:47.477
- Description: In Postgres Enterprise Manager (PEM), the pem_agent role, which every PEM agent login inherits, is a member of the PostgreSQL pg_read_server_files and pg_write_server_files roles on the PEM backend database. An attacker who controls any monitored host, and so its PEM agent certificate, can read and write files on the PEM server host as the postgres operating system user. This includes the PEM certificate authority key, which lets the attacker issue certificates for other agents and act as them.
From PEM 10.6.1, PEM agents no longer hold these roles.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132658

### CVE-2026-132659 — CRITICAL (CVSS: 9.4)

- Published: 2026-11-20T15:17:47.637
- Description: In Postgres Enterprise Manager (PEM), the row-level security policies on pem.job and pem.jobstep that apply to PEM agents do not limit an agent to its own jobs. An attacker who controls one monitored host, and so its PEM agent certificate, can create, change or delete jobs for every other agent, including the agent on the PEM server. Agents run SQL job steps with the database credentials of the server they monitor, and shell job steps where batch jobs are enabled, so compromising one monitored host can give superuser SQL access to every monitored database and to the PEM backend.
From PEM 10.6.1, PEM agents can no longer create jobs or change job definitions or job steps.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132659

### CVE-2026-132660 — CRITICAL (CVSS: 9.4)

- Published: 2026-11-20T15:17:47.800
- Description: In Postgres Enterprise Manager (PEM), several SECURITY DEFINER functions in the pem schema of the PEM backend database are owned by a superuser but do not set a safe search_path. Any PEM user who can connect to the PEM backend database can create objects that these functions use in place of the intended ones, and so run arbitrary SQL with superuser privileges. Temporary objects can be used for this on every supported PostgreSQL version, and objects in the public schema on PostgreSQL 14 backends and backends upgraded from PostgreSQL 14.
From PEM 10.6.1, these functions run with a fixed search_path.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132660

### CVE-2026-132661 — HIGH (CVSS: 7.6)

- Published: 2026-11-20T15:17:47.937
- Description: In Postgres Enterprise Manager (PEM), multi-factor authentication (MFA) is not enforced on the PEM web application's own routes. An attacker who knows the password of a user who has enrolled a second factor can skip the second factor and call PEM's pages and APIs directly, with that user's permissions. A similar issue in pgAdmin 4 was assigned CVE-2024-4215.
From PEM 10.6.1, every authenticated PEM route requires a completed MFA check.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132661

### CVE-2026-132662 — HIGH (CVSS: 7.2)

- Published: 2026-11-20T15:17:48.070
- Description: In Postgres Enterprise Manager (PEM), the SQL Profiler save and load functions in the PEM web application do not keep the client-supplied file name inside the user's storage directory. A user with the SQL Profiler role (pem_comp_sqlprofiler) can read JSON files, and overwrite files that the PEM web server account can write, outside their own storage directory. Overwriting the PEM web application's configuration database stops the web console for all users.
From PEM 10.6.1, the SQL Profiler only reads and writes files inside the user's storage directory.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132662

### CVE-2026-132663 — HIGH (CVSS: 7.1)

- Published: 2026-11-20T15:17:48.200
- Description: In Postgres Enterprise Manager (PEM), webhook URLs are not validated, and the PEM agent does not restrict the URL schemes it uses to deliver webhooks. A user with the alert configuration role (pem_config_alert) can set up a webhook with a file:// URL. When the webhook is sent, the agent on the PEM server, which runs as root by default, reads the local file and stores its contents in the webhook error record in the PEM database, where any PEM user can read it.
From PEM 10.6.1, PEM accepts and sends only http and https webhook URLs.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132663

### CVE-2026-132664 — HIGH (CVSS: 7.0)

- Published: 2026-11-20T15:17:48.333
- Description: In Postgres Enterprise Manager (PEM), any PEM user can read the encrypted passwords that PEM agents use to connect to monitored servers, including the PEM backend superuser password stored when the PEM server is configured. Unless a custom encryption key is configured, these passwords are encrypted with a key that is the same in every PEM installation, so they can be decrypted.
From PEM 10.6.1, PEM users can no longer read these passwords.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132664

### CVE-2026-133837 — HIGH (CVSS: 7.1)

- Published: 2026-11-20T15:17:51.130
- Description: flowintel contains an authorization bypass in its task completion workflow for privileged cases. Users with lower-privilege roles (editor, queuer) were able to mark tasks as completed without the required approver review (Admin, Case Admin, or Queue Admin), undermining the approval workflow.

The vulnerability was exploitable through multiple paths:
- Direct task completion via browser UI or REST API
- Changing a task's status to "Finished", which implicitly completed the task
- Creating a new task in a privileged case with the completed flag already set
- Using UUID aliases or Matrix delegation to reach the same endpoints

Preconditions:
- An authenticated user with at least editor or queuer role
- A privileged case with tasks in a non-completed state

Security impact:
- Bypass of the mandatory approver review process for privileged cases
- Unauthorized modification of task completion state
- Potential to mark sensitive work as finished without proper oversight

Affected versions: flowintel prior to 4.1.0
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133837

### CVE-2026-133839 — HIGH (CVSS: 7.1)

- Published: 2026-11-20T15:17:51.530
- Description: FlowIntel contains a missing authorization vulnerability in its task file deletion functionality. When a privileged task is in a restricted state (Requested, Rejected, or Request Review), any authenticated user with basic case membership (e.g., editor or queuer) was able to delete evidence files associated with that task via both the browser interface and the REST API. The deletion operation should have been restricted to users holding Admin, Case Admin, or Queue Admin roles.

The vulnerability affects the core file deletion logic, the browser-facing task endpoint, and the API task endpoint. No role-based restriction was enforced prior to performing disk removal, database record deletion, timeline event removal, or history log updates.

An attacker with a low-privilege case membership could destroy evidence files, corrupt investigation timelines, and alter case history, compromising the integrity of ongoing investigations.

Affected versions: FlowIntel prior to 4.1.0.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133839

### CVE-2026-133847 — HIGH (CVSS: 8.4)

- Published: 2026-11-20T15:17:52.740
- Description: flowintel contains an authorization bypass in the browser-based admin user editing interface. The edit_user view in the admin panel verified that a non-platform-admin user could only edit accounts belonging to their own organization, but it did not verify that the target account was not a platform-admin account. As a result, an authenticated user holding an organization-admin role could open the edit form for any platform-admin account and submit modifications, including changes to credentials, roles, or other account attributes.

The API layer already enforced a restriction preventing non-admin users from targeting admin accounts, but the browser-based admin view lacked the equivalent check, creating an inconsistent authorization boundary.

Impact:
- Unauthorized modification of platform-admin account data (integrity)
- Potential lockout or privilege manipulation of platform administrators (availability)
- Escalation of an organization-admin role to effectively control platform-level administration

Affected versions: flowintel prior to 4.1.0.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133847

### CVE-2026-133848 — HIGH (CVSS: 8.3)

- Published: 2026-11-20T15:17:52.937
- Description: flowintel contains an authorization flaw in its user deletion functionality. Organization-scoped administrators (org admins) are able to delete platform-level administrator accounts through both the browser-based admin interface and the REST API.

The existing authorization logic verified that an org admin could only target users within their own organization, but it did not enforce the privilege hierarchy between organization admins and platform admins. As a result, an authenticated org admin could issue a deletion request against any platform-admin account belonging to the same organization, causing the target account, its sessions, and related records to be permanently removed.

Impact:
- Loss of platform-level administrative oversight
- Potential disruption of platform-wide management functions
- Removal of higher-privilege accounts that should be protected from lower-privilege roles

Affected versions: flowintel prior to 4.1.0
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133848

### CVE-2026-133849 — HIGH (CVSS: 7.1)

- Published: 2026-11-20T15:17:53.137
- Description: A vulnerability exists in the flowintel application's calendar functionality that allows unauthorized access to private case data. The task calendar queries failed to enforce visibility checks on the parent case associated with tasks. Specifically, tasks assigned to a user or belonging to the user's organization were returned in calendar views (including browser and API ICS feeds) without verifying whether the user had permission to view the parent case. This allowed users to potentially discover and access details of private cases they were not authorized to view, leading to information disclosure.

The issue affected the default task visibility logic and the assigned-only task queries. The fix ensures that case visibility is rechecked in addition to task assignment or organization membership, preventing the exposure of private case data in calendar outputs.

Affected versions: flowintel < 4.1.0
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133849

### CVE-2026-133854 — HIGH (CVSS: 7.1)

- Published: 2026-11-20T15:17:54.090
- Description: flowintel contains a vulnerability in the case and task classification usage endpoints that allows authenticated users to view classification data associated with cases they do not have permission to access.

The affected endpoints, which provide lists of used taxonomies, tags, galaxies, clusters, and custom tags, did not properly enforce object-level access controls. While the endpoints required authentication, they failed to filter the returned data based on the requesting user's visibility permissions for the underlying cases. This allowed any authenticated user to enumerate classification usage across all cases, including private or restricted cases belonging to other organizations or users.

This issue could lead to the disclosure of sensitive information, such as the existence of specific cases, the types of threats or indicators associated with them, and the relationships between different classification elements, potentially aiding an attacker in reconnaissance or targeting.

Affected versions: < 4.1.0
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133854

### CVE-2026-115407 — CRITICAL (CVSS: 9.1)

- Published: 2026-11-20T17:18:07.373
- Description: In `github.com/eclipse-keypont/crypto11/v2` versions `<= 2.0.0-rc8` (and the deprecated v1 module paths `github.com/eclipse-keypont/crypto11 <= 1.6.8`, `github.com/ThalesGroup/crypto11 <= 1.7.0-rc1` and `github.com/ThalesIgnite/crypto11 <= 1.2.5`), the `cipher.AEAD` returned by `SecretKey.NewGCM()` passes whatever nonce it is given straight to `CK_GCM_PARAMS` without checking its length against `NonceSize()`, and accepts an empty nonce. On a token that accepts a zero-length GCM IV — SoftHSM2 does — every `Seal` with an empty nonce encrypts under the same IV, reusing the keystream and exposing the GHASH authentication key, which allows forgeries. Separately, `Config.UseGCMIVFromHSM` sends a NULL IV with length zero to the token unless `GCMIVFromHSMControl.SupplyIvForHSMGCMEncrypt` is also set, so the token has nowhere to write the IV it generates: a `Seal` with a non-empty nonce panics after the plaintext has already been encrypted, and a `Seal` with an empty nonce returns ciphertext under an empty IV without error. On the v1 line HSM-IV mode additionally never copies the token-generated IV back to the caller, so the caller keeps its own nonce while the data was encrypted under another one.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-115407

### CVE-2026-122244 — HIGH (CVSS: 7.7)

- Published: 2026-11-20T17:18:07.970
- Description: Budibase is an open-source low-code platform. Prior to 3.50.0, a BASIC application user, or an unauthenticated visitor to a public write form, can store markup in a shared external datasource that a builder or administrator later evaluates in any Handlebars binding Preview that surfaces the value, including the Data-section Formula column editor or any binding drawer. jsonFormatter.format() in packages/frontend-core/src/utils/jsonFormatter.ts leaves raw strings and object keys unescaped, while packages/builder/src/components/common/bindings/EvaluationSidePanel.svelte inserts the formatted result as raw HTML. The Handlebars SafeString path preserves the attacker-controlled value, and the Builder origin lacks a Content-Security-Policy that would block the resulting script. This permits stored script execution in the higher-privileged builder or administrator session rather than the writer's own role, allowing privileged Builder API actions and workspace data access. This issue is fixed in versions 3.50.0 and 4.0.0.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-122244

### CVE-2026-122247 — HIGH (CVSS: 8.2)

- Published: 2026-11-20T17:18:08.170
- Description: Budibase is an open-source low-code platform. Prior to 3.50.0, the public POST /api/global/users/init endpoint on a self-hosted single-tenant deployment accepts an attacker-controlled tenantId and evaluates checkAnyUserExists() in the selected tenant database instead of the legitimate default tenant. An unauthenticated attacker can select an unused tenant namespace to bypass the one-time initialization guard, causing packages/worker/src/api/controllers/global/users.ts to create a tenant-specific CouchDB database and a global-administrator document without a session or CSRF token. Repeating this operation with unique tenant identifiers can exhaust datastore resources and leave latent privileged records. The created administrator cannot log into the default tenant while multi-tenancy remains disabled, which limits the immediate impact to persistent writes, denial of service, and records that may become usable during later multi-tenant operation or migration. This issue is fixed in versions 3.50.0 and 4.0.0.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-122247

### CVE-2026-132275 — HIGH (CVSS: 7.5)

- Published: 2026-11-20T17:18:12.567
- Description: svglib reads SVG files and converts them to other formats. Prior to 2.3.1, the svg2rlg() renderer recursively expands nested SVG <use> references by deep-copying each referenced subtree; SvgRenderer.renderUse() in src/svglib/svglib.py calls xlink_href_target(), which rejects direct cycles but permits acyclic reference graphs with repeated fan-out. A small attacker-controlled SVG can therefore trigger exponentially increasing node expansion, consuming excessive CPU and memory in any application that renders it without a non-default option; HTML-to-PDF workflows using xhtml2pdf can reach the same renderer when an embedded data:image/svg+xml image in an HTML img element is passed to pisa.CreatePDF(). This issue is fixed in 2.3.1.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132275

### CVE-2026-133872 — CRITICAL (CVSS: 9.1)

- Published: 2026-11-20T17:18:24.293
- Description: LessPass self-hosted sync server backend before commit 9469b0c lacks rate limiting on the JWT login endpoints /tokens/auth/ and /auth/jwt/create/, allowing unlimited authentication attempts. Unauthenticated remote attackers can brute force passwords or perform credential stuffing against known account emails to obtain tokens granting read and write access to stored profiles.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133872

### CVE-2026-133874 — HIGH (CVSS: 8.6)

- Published: 2026-11-20T17:18:24.647
- Description: Iceburg CRM through 5.0.0 contains an incorrect authorization vulnerability in Module::saveRecord() that allows authenticated users to write to unauthorized modules by prefixing request body keys with another module id. Attackers with write access to one module can submit crafted requests to POST /data/save or PUT /api/crm/{id} to set their role_id to Admin and access administrative data.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133874

### CVE-2026-133879 — HIGH (CVSS: 7.7)

- Published: 2026-11-20T17:18:25.317
- Description: A flaw was found in KubeVirt/containerized-data-importer. When a VirtualMachine with an embedded DataVolumeTemplate carrying the cdi.kubevirt.io/storage.checkStaticVolume annotation and a cross-namespace clone source is created by a tenant, the service-account clone authorization check can be bypassed, allowing a PVC from another namespace to be cloned into the tenant's namespace without the required permissions. This can result in cross-tenant data disclosure.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133879

### CVE-2026-77329 — HIGH (CVSS: 8.8)

- Published: 2026-11-20T17:18:26.917
- Description: Tapo provides Rust and Python APIs and an MCP server for TP-Link Tapo smart devices. From 0.3.1 until 0.5.0, the Streamable HTTP implementation in tapo-mcp/src/server.rs calls disable_allowed_hosts() without replacement Host or Origin validation, while TAPO_MCP_API_KEY remains optional for a listener that can bind to all interfaces. A malicious website can use DNS rebinding to send same-origin browser requests to the victim's local or LAN Tapo MCP listener when it runs without an API key. The attacker can invoke exposed tools including control_device for smart-device actuation and take_snapshot for configured cameras. Deployments with TAPO_MCP_API_KEY set are not affected by the unauthenticated path, and exploitation requires a running listener configured with real Tapo credentials and devices, plus victim interaction with the malicious site. This issue is fixed in version 0.5.0.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-77329

### CVE-2026-79751 — HIGH (CVSS: 7.6)

- Published: 2026-11-20T17:18:27.397
- Description: SportEase is a web application for managing school sports events, class rosters, and competition teams. Prior to 1.3, an authenticated account with is_profile_complete=false can submit an attacker-selected class_id for any class in the currently active event to PUT /api/user/profile during first profile completion. AuthHandler.UpdateProfile accepts the class without validating the user's legitimate membership and automatically derives and assigns the corresponding {class_name}_rep role while isFirstCompletion is true. The attacker can become representative of one selected class, view roster information including email addresses, and add or remove competition-team assignments. Downstream handlers correctly reject access to other classes, so the impact is bounded to the selected class, but the representative privilege cannot be revoked through the exposed API and requires direct database intervention or another out-of-band remediation method. This issue is fixed in version 1.3.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-79751

### CVE-2026-82675 — HIGH (CVSS: 8.1)

- Published: 2026-11-20T17:18:27.703
- Description: The GiveWP – Donation Plugin and Fundraising Platform plugin for WordPress is vulnerable to donor account account takeover in all versions up to, and including, 4.17.0. This is due to the plugin not properly validating a donor's identity prior to updating the password of a linked WordPress account. The donation receipt processes an attacker-controlled first name through the V3 template engine and then reprocesses the result through the legacy `{meta_donor_*}` engine, which can disclose the donor's email-access bearer token. The donor-dashboard password endpoint accepts that token by itself and calls `wp_set_password()` for the WordPress user linked to the donor. This makes it possible for unauthenticated attackers to reset the password of any WordPress account linked to a GiveWP donor record and gain access to that account. If the linked account is an administrator, the attacker can achieve full site compromise and remote code execution through standard administrator functionality. A published GiveWP form with a usable gateway, enabled donor email access (enabled by default), knowledge of the donor email address, and an account already linked to the targeted donor record are required. NOTE: This vulnerability can be chained with CVE-2026-82676 to satisfy the administrator donor pre-requisite for a targeted administrator user attack.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-82675

### CVE-2026-103933 — HIGH (CVSS: 7.7)

- Published: 2026-11-20T18:18:34.790
- Description: Netatalk is a Free and Open Source file server suite for Unix-like operating systems. From 2.1.0 until 4.5.2, get_eacontent in libatalk/vfs/ea_ad.c subtracts MAX_REPLY_EXTRA_BYTES from a client-controlled FPGetExtAttr MaxReplySize without rejecting values from 1 through 5, and a signed-to-unsigned comparison can then select an untrusted AppleDouble ea_size. An authenticated client on a volume configured with ea = ad can use a pre-existing malformed AppleDouble sidecar to make read copy attacker-controlled bytes beyond dsi->data + 6 into the surrounding struct DSI, including protocol callback pointers. The malformed sidecar must already exist or be created through a separate local, co-export, management, restore, or vulnerability-assisted write path, and practical code execution depends on the target architecture, structure layout, and address uncertainty; runtime command execution was demonstrated on one x86-64 build. Volumes using ea = sys, ea = none, or ea = auto when it resolves to native system xattrs do not reach this path. This issue is fixed in version 4.5.2.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-103933

### CVE-2026-104184 — HIGH (CVSS: 7.1)

- Published: 2026-11-20T18:18:34.980
- Description: LinkAce is a self-hosted archive to collect website links. Prior to 2.6.0, LinkController::update() in app/Http/Controllers/API/LinkController.php passes $request->all() to the repository update method even though user_id is fillable and is not an allowed field in the validated update request. An authenticated API user who is authorized to update a link can therefore assign an arbitrary or nonexistent user_id, transferring the link into another user's bookmark collection or orphaning it from any real account. The web update controller is unaffected because it passes only validated fields. This issue is fixed in version 2.6.0.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-104184

### CVE-2026-133212 — CRITICAL (CVSS: 9.0)

- Published: 2026-11-20T18:18:47.127
- Description: @fastify/reply-from is a Fastify plugin that forwards an incoming HTTP request to an upstream server. In versions before 12.9.1, when the plugin forwards a request whose body is not written to the upstream connection, such as a GET, HEAD, or TRACE request that carried a body, or a request with a falsy JSON body, it still forwards the client's Content-Length header while sending no body. The upstream server then treats the bytes of the following request as the unfinished body, which an attacker can use to desynchronize the connection and smuggle a request. The issue is fixed in @fastify/reply-from 12.9.1, and users should upgrade to 12.9.1 or later.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133212

### CVE-2026-133730 — HIGH (CVSS: 7.5)

- Published: 2026-11-20T18:18:52.030
- Description: A flaw was found in dnsmasq, where a memory handling issue exists in its Dynamic Host Configuration Protocol for IPv6 (DHCPv6) relay processing. A remote attacker can exploit this vulnerability by sending a sequence of network packets to a system configured as a DHCPv6 relay. This causes the service to write data to previously freed memory and crash, resulting in a Denial of Service (DoS).
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133730

### CVE-2026-45354 — HIGH (CVSS: 7.5)

- Published: 2026-11-20T18:18:52.790
- Description: Netatalk is a Free and Open Source file server suite for Unix-like operating systems. Prior to 4.4.3, libatalk/dsi/dsi_stream.c interprets the dsi_code and dsi_doff union field as a data offset for all DSI command types instead of limiting that interpretation to DSIWrite. An unauthenticated client can send a non-WRITE DSIFUNC_CMD packet with a nonzero dsi_code smaller than dsi_len, causing dsi_stream_receive to consume only the dsi_code number of payload bytes and leave attacker-controlled bytes in the readahead buffer. The residual bytes become the next DSI header, allowing protocol desynchronization that can close sessions, corrupt protocol state, or trigger an infinite-read denial of service. This issue is fixed in version 4.4.3.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-45354

### CVE-2026-45355 — HIGH (CVSS: 7.1)

- Published: 2026-11-20T18:18:52.967
- Description: Netatalk is a Free and Open Source file server suite for Unix-like operating systems. Prior to 4.4.3, the afpd Spotlight RPC string unmarshalling path in etc/afpd/spotlight_marshalling.c uses sl_unpack_cpx to calculate slen from qlen and the attacker-controlled used_in_last_block value without preventing a negative result. An authenticated AFP client can send a complex string or UTF-16 string element that makes slen negative, and the implicit conversion to size_t causes dalloc_strndup or convert_string_allocate to read beyond the heap buffer. The out-of-bounds read can expose heap data through the RPC response or crash the worker process. This issue is fixed in version 4.4.3.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-45355

### CVE-2026-45356 — HIGH (CVSS: 7.1)

- Published: 2026-11-20T18:18:53.130
- Description: Netatalk is a Free and Open Source file server suite for Unix-like operating systems. Prior to 4.4.3, the afpd Spotlight RPC unmarshalling loop in etc/afpd/spotlight_marshalling.c subtracts an attacker-controlled subcount from the unsigned count variable in sl_unpack_loop without verifying that subcount is not larger. An authenticated AFP client can place an excessive element count in the sl_unpack_ints, sl_unpack_uuid, sl_unpack_floats, or sl_unpack_date handler, or in a null element, so the subtraction wraps near UINT_MAX and the loop continues reading heap memory at increasing offsets up to toc_offset, which is capped at 65000. The out-of-bounds values can be stored in dalloc structures and returned in the Spotlight RPC response, disclosing heap contents. This issue is fixed in version 4.4.3.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-45356

### CVE-2026-49387 — HIGH (CVSS: 7.1)

- Published: 2026-11-20T18:18:53.307
- Description: Netatalk is a Free and Open Source file server suite for Unix-like operating systems. From 3.1.0 until 4.5.0, the afpd FPSpotlightRPC unmarshalling handlers in etc/afpd/spotlight_marshalling.c trust the element count encoded in the upper 32 bits of an RPC tag without comparing it with the remaining input length. An authenticated client with access to a Spotlight-enabled volume can make sl_unpack_ints, sl_unpack_date, sl_unpack_uuid, or sl_unpack_floats iterate beyond dsi->commands and read heap memory. The read values remain in internal dalloc storage and no information-disclosure channel was demonstrated, but the worker serving the attacker's session can be crashed. This issue is fixed in version 4.5.0.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-49387

### CVE-2026-49388 — HIGH (CVSS: 7.1)

- Published: 2026-11-20T18:18:53.480
- Description: Netatalk is a Free and Open Source file server suite for Unix-like operating systems. From 3.1.0 until 4.5.0, sl_unpack_loop in etc/afpd/spotlight_marshalling.c uses an attacker-controlled Spotlight table-of-contents index during FPSpotlightRPC without checking it against the number of entries or the remaining dsi->commands buffer. An authenticated AFP client with access to a Spotlight-enabled volume can choose a large toc_index whose multiplication and addition produce an out-of-range address, causing an attacker-influenced heap read and reliably crashing the worker serving that session. The earlier CVE-2026-44066 remediation bounded recursion depth and toc_offset but did not bound toc_index. This issue is fixed in version 4.5.0.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-49388

### CVE-2026-55216 — HIGH (CVSS: 8.1)

- Published: 2026-11-20T18:18:54.100
- Description: Logto is the modern, open-source auth infrastructure for SaaS and AI apps. Prior to 1.46.0, social account linking can use an unverified email returned by the standard OAuth 2.0 or Azure AD connector to select an existing local account. When findSocialRelatedUser matches a victim's email and a request to POST /api/experience/identification enables linkSocialIdentity, an attacker who controls that unverified provider email can link an attacker-controlled social identity to the victim account and sign in as the victim. The issue applies when the provider does not verify email ownership or allows the value to be set freely; Google, GitHub, and default OIDC connector behavior is not affected because those paths expose only verified email. Version 1.46.0 adds an opt-in email synchronization control to the standard OAuth 2.0 connector, while the Azure AD connector has offered an equivalent opt-in control since version 1.43.0. These controls preserve existing behavior by default, so administrators must enable them on affected connectors. A configurable mitigation is available in version 1.46.0.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-55216

### CVE-2026-62318 — CRITICAL (CVSS: 9.3)

- Published: 2026-11-20T18:18:54.807
- Description: Netatalk is a Free and Open Source file server suite for Unix-like operating systems. From 2.0.0 until 4.5.1, the DHX2 and DHX2-PAM authentication state machine in etc/uams/uams_dhx2_pam.c permits logincont1 to be invoked again with the same FPLoginCont retID after it has released the global gcry_mpi_t Ra object. When DHX2 or DHX2PAM is enabled in the UAM list, a remote attacker without valid AFP credentials can repeat the first continuation step, causing gcry_mpi_powm to dereference the freed Ra value and gcry_mpi_release to free it again in a privileged afpd worker. The demonstrated result is a repeatable pre-authentication worker crash, and the use-after-free and double-free provide a plausible allocator exploitation primitive although code execution was not demonstrated. This issue is fixed in version 4.5.1.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-62318

### CVE-2026-62319 — HIGH (CVSS: 7.2)

- Published: 2026-11-20T18:18:54.980
- Description: Netatalk is a Free and Open Source file server suite for Unix-like operating systems. From 1.5.0 until 4.5.1, dsi_stream_receive in libatalk/dsi/dsi_stream.c independently clamps dsi_doff and dsi_len for DSIWrite requests without enforcing that the data offset is no greater than the declared frame length. An authenticated AFP client can send dsi_doff greater than dsi_len, causing the receiver to consume bytes from a queued subsequent frame before libatalk/dsi/dsi_write.c detects the inconsistency. The irreversible stream desynchronization lets the attacker control the next parsed DSI header and payload and corrupts protocol framing for the connection. This issue is fixed in version 4.5.1.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-62319

### CVE-2026-62320 — HIGH (CVSS: 8.8)

- Published: 2026-11-20T18:18:55.157
- Description: Netatalk is a Free and Open Source file server suite for Unix-like operating systems. From 1.5.0 until 4.5.1, dsi_tcp_open in libatalk/dsi/dsi_tcp.c silently limits the bytes read from an unauthenticated DSI frame received on TCP/548 to server_quantum when the attacker-controlled dsi_len is larger, without rejecting the frame or draining the declared remainder. The same silent dsi_len truncation pattern exists in libatalk/dsi/dsi_stream.c. The leftover bytes remain queued on the TCP connection and the next dsi_stream_receive call interprets them as a new DSI header and payload, allowing a remote unauthenticated attacker to smuggle one or more additional attacker-controlled DSI frames into the same connection. This issue is fixed in version 4.5.1.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-62320

### CVE-2026-62321 — HIGH (CVSS: 8.7)

- Published: 2026-11-20T18:18:55.320
- Description: Netatalk is a Free and Open Source file server suite for Unix-like operating systems. From 3.1.0 until 4.5.1, the afpd Spotlight RPC fetchQueryResultsForContext: reply path in etc/afpd/spotlight_marshalling.c calls the top-level sl_pack function from sl_pack_filemeta on a shifted sub-buffer without passing the remaining capacity of the outer DSI reply buffer. An authenticated AFP client can request an amplified nested file-metadata tree so the nested packer applies MAX_SLQ_DAT relative to the shifted pointer and writes beyond struct DSI::data. The out-of-bounds write corrupts heap memory beyond the DSI reply buffer. This issue is fixed in version 4.5.1.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-62321

### CVE-2026-77309 — HIGH (CVSS: 8.8)

- Published: 2026-11-20T18:18:55.847
- Description: AIT GUI provides a framework for building custom websites for real-time telemetry monitoring, commanding, and other mission operations. From 1.0.0 until 2.5.1, POST /tlm/query in ait/gui/__init__.py writes attacker-controlled field data to fields_in.txt, and its no-PCAP error path can abort before deleting that file. The unauthenticated POST /script/run route accepts a scriptPath that resolves outside ScriptRoot, reads the selected file, and executes it as Python. A network-reachable attacker can obtain the ordinary session cookie without credentials, combine the two routes, and execute arbitrary Python code with the AIT-GUI server process privileges. This issue is fixed in version 2.5.1.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-77309

### CVE-2026-77350 — HIGH (CVSS: 7.3)

- Published: 2026-11-20T18:18:56.280
- Description: pmo-platform is a modular PMO and release-management platform for Claude Code. Prior to 3.69.1, core/hooks/block-credential-reads.sh, core/hooks/block-egress.sh, core/hooks/block-fs-boundary.sh, and core/hooks/block-mcp-writes.sh pin PATH to /usr/bin:/bin, hard-code jq as /usr/bin/jq, and return success when jq is unavailable there. On systems where jq exists only in a Homebrew path, including affected pre-Sequoia or Homebrew-only macOS installations, the hooks can skip credential-read, network-egress, filesystem-boundary, and MCP-write controls. Native deny rules independently protect some credential paths but do not backstop the egress or MCP controls. An attacker who can influence a prompt, repository, or evaluation flow can use the skipped checks to expose secrets or perform unauthorized tool actions. This issue is fixed in version 3.69.1.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-77350
