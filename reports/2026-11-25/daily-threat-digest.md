# Cybersecurity Daily Intelligence Digest

Generated: 2026-11-25 23:12 UTC
Records included: 35

## Data Sources

- National Vulnerability Database (NVD)
- CISA Known Exploited Vulnerabilities (KEV)

## AI Analyst Summary

Gemini AI analysis was unavailable. The collected vulnerability records are retained below for manual review.

## Vulnerability Findings

### CVE-2026-125353 — MEDIUM (CVSS: 5.1)

- Published: 2026-11-18T23:17:17.430
- Description: An incorrect
permission assignment vulnerability in Omada SDN Controller prior to 6.2.20 may
cause a database backup generated during the uninstall workflow to remain
readable by other local users on the host. 





Successful
exploitation requires local, low-privileged access to the affected host and a
retained uninstall backup. An attacker meeting these conditions could access
the backup and disclose controller data without controller credentials.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-125353

### CVE-2026-129315 — HIGH (CVSS: 8.5)

- Published: 2026-11-18T23:17:18.000
- Description: Dokploy is a free, self-hostable Platform as a Service (PaaS). In 0.31.0 and earlier, the hosted installer and manual installation instructions set /etc/dokploy to mode 0777, allowing a local non-root user on a shared host to replace root-owned schedule or Traefik configuration directories. Dokploy subsequently consumes those paths as trusted configuration and can execute substituted scheduled-task scripts as root, resulting in local privilege escalation.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129315

### CVE-2026-129316 — CRITICAL (CVSS: 9.9)

- Published: 2026-11-18T23:17:18.187
- Description: Dokploy is a free, self-hostable Platform as a Service (PaaS). From 0.29.13 until 0.31.0, the Docker terminal, container-log, and monitoring WebSocket handlers accept a caller-controlled serviceId as authorization but do not consistently bind the requested containerId or appName to that service. A member with read access to any service can consequently target unrelated containers, obtain a root shell in the Dokploy panel container, read other tenants' logs and statistics, and use the mounted Docker socket to compromise the host. This issue is fixed in version 0.31.0.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129316

### CVE-2026-129985 — HIGH (CVSS: 8.7)

- Published: 2026-11-18T23:17:18.380
- Description: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.31.1, a user-controlled schedule appName is joined into the schedule directory path and interpolated without shell quoting into commands that create the directory and write the schedule script. An authenticated user who can create or update a dokploy-server schedule can inject operating-system commands that execute with the Dokploy process privileges when the schedule is saved, including root privileges on typical installations. This issue is fixed in version 0.31.1.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129985

### CVE-2026-129986 — CRITICAL (CVSS: 9.9)

- Published: 2026-11-18T23:17:18.550
- Description: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.31.1, mount.deleteFileMount passes a path containing the user-controlled filePath to the local removeFileOrDirectory helper, which interpolates it unquoted into rm -rf, while the remote branch is quoted. An authenticated member with file-mount create and delete permissions can execute arbitrary commands in the host context immediately when deleting a local file mount, without requiring a running container. This issue is fixed in version 0.31.1.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129986

### CVE-2026-129989 — CRITICAL (CVSS: 9.9)

- Published: 2026-11-18T23:17:18.737
- Description: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.31.1, the Nixpacks publishDirectory build setting accepts shell metacharacters and is interpolated into a docker cp command executed through child_process.exec. An authenticated user with access to an application can execute arbitrary commands on the Dokploy host when triggering a Nixpacks deployment, leading to host compromise through the privileged Docker environment. This issue is fixed in version 0.31.1.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129989

### CVE-2026-129990 — HIGH (CVSS: 8.3)

- Published: 2026-11-18T23:17:18.917
- Description: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.31.1, every network.* procedure is only authentication-protected and does not require the Docker permission, allowing a standard member to list, inspect, create, import, recreate, resynchronize, and delete Docker networks. A member can disrupt service connectivity or alter network configuration, and create/import operations can target an unchecked serverId. This issue is fixed in version 0.31.1.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129990

### CVE-2026-129991 — CRITICAL (CVSS: 9.9)

- Published: 2026-11-18T23:17:19.090
- Description: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.31.1, the backup prefix field is only checked for a nonempty value, and normalizeS3Path preserves shell metacharacters before the prefix is interpolated into rclone upload and retention-cleanup command strings. An authenticated organization member with backup permission for a service can execute arbitrary commands as root on the Dokploy host or configured remote server when a PostgreSQL, MySQL, MariaDB, MongoDB, libSQL, Compose, or web-server backup runs manually, on schedule, or performs retention cleanup. This issue is fixed in version 0.31.1.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129991

### CVE-2026-129992 — MEDIUM (CVSS: 6.3)

- Published: 2026-11-18T23:17:19.260
- Description: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.31.0, failed Railpack builds and database backups propagate an execution error containing the full command, exposing application environment variables, database passwords, and S3 access keys embedded in those commands. When the corresponding App Build Error or Database Backup notification setting is enabled, the disclosure can send secrets to email, Slack, Discord, Telegram, or webhooks; the same secrets are written separately to persistent Dokploy container logs, which may be accessible to more principals than the affected service. This issue is fixed in version 0.31.0.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-129992

### CVE-2026-132279 — LOW (CVSS: 2.1)

- Published: 2026-11-18T23:17:20.560
- Description: A flaw has been found in elunez eladmin up to 2.7. Affected by this vulnerability is the function SqlUtils.sanitizeJdcUrl of the component JDBC URL Sanitization. Executing a manipulation can lead to improper input validation. The attack may be performed from remote. The exploit has been published and may be used. The project was informed of the problem early through an issue report but has not responded yet.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132279

### CVE-2026-132280 — LOW (CVSS: 2.1)

- Published: 2026-11-18T23:17:20.773
- Description: A vulnerability has been found in elunez eladmin up to 2.7. Affected by this issue is the function CheckBean of the file /api/jobs/exec of the component Quartz Handler. The manipulation of the argument methodName leads to improper input validation. It is possible to initiate the attack remotely. The exploit has been disclosed to the public and may be used. The project was informed of the problem early through an issue report but has not responded yet.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132280

### CVE-2026-71500 — MEDIUM (CVSS: 6.8)

- Published: 2026-11-18T23:17:21.173
- Description: Mareforma is a local verification layer for AI-assisted research. From 0.3.0 until 0.3.8, _maybe_update_replicated_unlocked in mareforma/db/core.py does not check t_invalid in its new-claim gate, peer-selection query, or final update, so a claim marked invalid by a signed contradiction verdict can still be promoted to REPLICATED through convergence. The invalidated claim can also act as the corroborating peer that promotes an honest claim, bypassing the trust ladder's terminal refutation state. This issue is fixed in version 0.3.8.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-71500

### CVE-2026-71533 — MEDIUM (CVSS: 6.8)

- Published: 2026-11-18T23:17:21.337
- Description: Mareforma is a local verification layer for AI-assisted research. From 0.3.7 until 0.3.8, search_claims in mareforma/db/core.py does not call _row_verified_on_read and therefore does not provide the same high-trust verification projection as query_claims. A forged or tampered REPLICATED or ESTABLISHED row that query_claims excludes can be returned by search_claims at its persisted trust level, and the missing verified marker prevents consumers from detecting that signature verification was skipped. The include_unverified option does not authorize this high-trust bypass. This issue is fixed in version 0.3.8.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-71533

### CVE-2026-71534 — MEDIUM (CVSS: 6.9)

- Published: 2026-11-18T23:17:21.480
- Description: Mareforma is a local verification layer for AI-assisted research. From 0.3.0 until 0.3.8, restore logic in mareforma/db/restore.py derives transparency_logged from the unsigned rekor.uuid field inside signature_bundle without requiring a verified claim-bound rekor_inclusions entry, so an attacker who modifies claims.toml can falsely make a claim eligible for REPLICATED convergence. The same logic resets signed claims in non-Rekor graphs from transparency_logged 1 to 0 after restore, permanently preventing convergence because no Rekor refresh is configured. This issue is fixed in version 0.3.8.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-71534

### CVE-2026-71535 — HIGH (CVSS: 7.1)

- Published: 2026-11-18T23:17:21.620
- Description: Mareforma is a local verification layer for AI-assisted research. From 0.3.0 until 0.3.7, the _maybe_update_replicated_unlocked convergence path in mareforma/db/core.py uses generated_by labels without requiring a valid signature_bundle from a distinct enrolled signer, so an unsigned claim written to a shared graph can converge with a signed peer and be promoted to REPLICATED. The forged trust state is returned by queries requiring REPLICATED support, allowing false multi-party endorsement signals to reach downstream consumers. This issue is fixed in version 0.3.7.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-71535

### CVE-2026-71536 — HIGH (CVSS: 7.0)

- Published: 2026-11-18T23:17:21.770
- Description: Mareforma is a local verification layer for AI-assisted research. From 0.3.0 until 0.3.8, verify_bundle in mareforma/export_bundle.py validates the outer DSSE envelope and exporter-signed subject digests, but JSONLDExporter._claim_node in mareforma/exporters/jsonld.py supplies no signatureBundle for individual claims. Because the exporter signs both the predicate nodes and their digest list, the check proves only internal bundle consistency and allows claims with missing, invalid, or forged asserter signatures to be accepted as authentic. This issue is fixed in version 0.3.8.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-71536

### CVE-2026-77283 — HIGH (CVSS: 8.8)

- Published: 2026-11-18T23:17:21.930
- Description: obsidian-sync-mcp is an MCP server that gives AI agents access to Obsidian vaults. Prior to 0.5.7, deployments running without MCP_AUTH_TOKEN install no serverOptions.authenticate check for the HTTP /mcp endpoint, so requests are dispatched without validating the Host or Origin headers. A malicious website visited by the operator can use DNS rebinding to reach loopback, LAN, VPN, or container-published addresses, or directly issue a cross-origin request to loopback, and invoke the MCP tool surface to read, create, overwrite, delete, or move vault notes. Deployments using MCP_AUTH_TOKEN are not affected because browsers do not attach the bearer token. This issue is fixed in version 0.5.7.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-77283

### CVE-2026-127039 — MEDIUM (CVSS: 5.9)

- Published: 2026-11-19T00:17:41.443
- Description: The certificate authentication info handling in gnutls from 2.5.9 up to 3.8.13 does not reset the certificate count and list pointer when re-allocation of raw_certificate_list fails, which allows remote attackers to cause a denial of service for a peer under heap pressure.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-127039

### CVE-2026-127040 — MEDIUM (CVSS: 5.9)

- Published: 2026-11-19T00:17:41.597
- Description: The RSA-PSK ClientKeyExchange handler in gnutls before 3.8.14 does not return after detecting a memory allocation failure when copying the PSK username, which allows remote attackers to cause a denial of service for a peer under heap pressure.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-127040

### CVE-2026-127231 — MEDIUM (CVSS: 5.9)

- Published: 2026-11-19T00:17:41.717
- Description: A double free in the X.509 name constraints enforcement of GnuTLS 3.8.13 on all platforms allows a remote attacker to cause a denial of service (application crash) via a certificate chain containing a NameConstraints extension processed while the application is under memory pressure. When an already populated name constraints object is reinitialized, previously freed list pointers are not cleared, so a memory allocation failure precisely at reinitialization leaves a dangling pointer that is freed again during a later cleanup.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-127231

### CVE-2026-132281 — LOW (CVSS: 2.1)

- Published: 2026-11-19T00:17:41.850
- Description: A vulnerability was found in elunez eladmin up to 2.7. This affects the function SqlUtils.batchExecute of the file /api/database/upload of the component Database Maintenance Module. The manipulation results in sql injection. It is possible to launch the attack remotely. The exploit has been made public and could be used. The project was informed of the problem early through an issue report but has not responded yet.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132281

### CVE-2026-132282 — LOW (CVSS: 2.1)

- Published: 2026-11-19T00:17:42.050
- Description: A vulnerability was determined in elunez eladmin up to 2.7. This vulnerability affects the function FileUtil.upload of the file /api/localStorage of the component File Upload Handler. This manipulation causes path traversal. The attack can be initiated remotely. The exploit has been publicly disclosed and may be utilized. The project was informed of the problem early through an issue report but has not responded yet.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132282

### CVE-2026-132283 — MEDIUM (CVSS: 6.9)

- Published: 2026-11-19T00:17:42.247
- Description: A vulnerability was identified in Directus up to 12.7.0. This issue affects the function AuthenticationService.refresh of the file api/src/services/authentication.ts of the component Authentication Service. Such manipulation leads to session expiration. The attack can be launched remotely. The vendor was contacted early about this disclosure.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132283

### CVE-2026-132745 — HIGH (CVSS: 7.1)

- Published: 2026-11-19T00:17:42.447
- Description: Vtiger CRM through 8.4.0 contains a blind SQL injection vulnerability that allows authenticated non-administrative users to inject SQL through the k (does not contain) comparator in list view search_params. Attackers can send crafted search_params to the ListAjax getRecordsCount mode, breaking out of the unescaped NOT LIKE clause to extract database contents via boolean or time-based techniques.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132745

### CVE-2026-132746 — HIGH (CVSS: 7.1)

- Published: 2026-11-19T00:17:42.600
- Description: Vtiger CRM through 8.4.0 contains a blind SQL injection vulnerability that allows authenticated low-privileged users to inject SQL via unescaped clientid values in the wsapp_map webservice operation. Attackers can register a sync application with wsapp_register, then send delete-mode entries with quoted clientid values processed by SyncServer.php to extract database contents including administrator access keys.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132746

### CVE-2026-132747 — HIGH (CVSS: 7.1)

- Published: 2026-11-19T00:17:42.750
- Description: Vtiger CRM through 8.4.0 contains an SQL injection vulnerability that allows authenticated users with export access to inject SQL through unvalidated selected_ids values in ExportData.php. Attackers can send a UNION SELECT payload in selected_ids[] to the ExportSelectedRecords mode and read password hashes and access keys from the exported CSV.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132747

### CVE-2026-132748 — HIGH (CVSS: 8.6)

- Published: 2026-11-19T00:17:42.893
- Description: Vtiger CRM through 8.4.0 contains a PHP code injection vulnerability that allows authenticated administrators to inject code via the updatedFields parameter into config.inc.php. Attackers can supply a crafted HELPDESK_SUPPORT_EMAIL_ID value that passes email validation but closes the PHP string literal to execute arbitrary operating system commands.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132748

### CVE-2026-132749 — HIGH (CVSS: 7.1)

- Published: 2026-11-19T00:17:43.043
- Description: Vtiger CRM through 8.4.0 contains a blind SQL injection vulnerability in ReportRun::generateAdvFilterSql() that allows authenticated low-privileged users to inject SQL via the bw comparator. Attackers can send a crafted advanced_filter parameter containing a single quote to the Reports getRecordsCount action to break out of BETWEEN literals and extract database contents.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132749

### CVE-2026-132750 — HIGH (CVSS: 7.1)

- Published: 2026-11-19T00:17:43.197
- Description: Meilisearch before 1.55.1 and 1.56.x before 1.56.1 contains a quadratic memory consumption vulnerability in filter-parser that allows attackers with a search API key to exhaust server memory. Attackers can send a roughly 100 KB filter, such as a _geoPolygon with thousands of coordinates, to the search endpoint, crashing the server and taking all indexes offline.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132750

### CVE-2026-132751 — HIGH (CVSS: 8.5)

- Published: 2026-11-19T00:17:43.357
- Description: yt through 4.4.4 contains a code injection vulnerability that allows attackers to execute Python code by supplying a crafted con_args attribute in a ytdata HDF5 file. SavedDataset._parse_parameter_file() passes con_args to eval() unrestricted, so loading a malicious .h5 file with yt.load() runs attacker code as the user.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132751

### CVE-2026-132752 — MEDIUM (CVSS: 5.1)

- Published: 2026-11-19T00:17:43.510
- Description: ScreenTinker before 3.2.4 contains a stored cross-site scripting vulnerability in the GET /api/kiosk/:id/render endpoint that allows users with kiosk page edit rights to store javascript: URLs in page buttons. Attackers can trigger script execution in the dashboard origin when an administrator activates the button, hijacking the victim's session and taking full control of the instance.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132752

### CVE-2026-132753 — MEDIUM (CVSS: 6.8)

- Published: 2026-11-19T00:17:43.670
- Description: MP4v2 through 2.1.0 contains a NULL pointer dereference vulnerability in MP4RtpHintTrack::GetPayload() in src/rtphint.cpp that passes an unchecked rtpmap value to strchr(). Attackers can supply a crafted MP4 file whose RTP hint track has a corrupted hinf atom to crash mp4info or applications calling MP4GetHintTrackRtpPayload().
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132753

### CVE-2026-132754 — MEDIUM (CVSS: 6.9)

- Published: 2026-11-19T00:17:43.843
- Description: MediaInfoLib before 26.10 contains an out-of-bounds read vulnerability in File_Mpeg4::meta_iloc that allows attackers to trigger a global buffer over-read via oversized iloc field sizes. Attackers can supply a crafted MP4 file with invalid offset_size or length_size values to overrun the BitStream_Fast mask table and crash applications analysing the file.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132754

### CVE-2026-132755 — MEDIUM (CVSS: 6.9)

- Published: 2026-11-19T00:17:44.000
- Description: MediaInfoLib before 26.10 contains a heap-based buffer over-read vulnerability in tfsxml_leave() caused by an off-by-one error when handling generic <! markup in truncated XML. Attackers can supply a crafted media file with malformed ADM XML parsed by File_Adm.cpp to crash MediaInfo or applications using MediaInfoLib.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132755

### CVE-2026-132756 — HIGH (CVSS: 8.5)

- Published: 2026-11-19T00:17:44.180
- Description: Geany through 2.1.0 contains an OS command injection vulnerability that allows attackers to run shell commands by embedding metacharacters in filenames substituted into build and execute commands. Attackers can craft a file named with backticks or $(...) that executes via /bin/sh when a user runs Compile, Build or Execute, gaining code execution as the user.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132756
