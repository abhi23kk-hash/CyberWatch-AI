# Critical Vulnerability Watch

Generated: 2026-11-25 14:45 UTC
Records included: 66

## Data Sources

- National Vulnerability Database (NVD)
- CISA Known Exploited Vulnerabilities (KEV)

## AI Analyst Summary

Gemini AI analysis was unavailable. The collected vulnerability records are retained below for manual review.

## Vulnerability Findings

### CVE-2026-109908 — HIGH (CVSS: 7.8)

- Published: 2026-11-18T15:17:32.020
- Description: A heap buffer overflow in reading encoding files in X.Org libfontenc before 1.11.0 could be used by local attackers able to inject enc files to the X server could crash or escalate privileges.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-109908

### CVE-2026-111507 — HIGH (CVSS: 8.1)

- Published: 2026-11-18T15:17:32.167
- Description: Dell PowerStore contains an authorization bypass vulnerability. A remote attacker could exploit this vulnerability to act under another user's session, potentially leading to denial of service.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-111507

### CVE-2026-116446 — CRITICAL (CVSS: 9.8)

- Published: 2026-11-18T15:17:32.780
- Description: Dell PowerStore SDNAS contains an out-of-bounds memory vulnerability in the NAS NFS service that an unauthenticated remote attacker could exploit to cause a denial of service.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-116446

### CVE-2026-116447 — HIGH (CVSS: 8.8)

- Published: 2026-11-18T15:17:32.943
- Description: Dell PowerStore SDNAS contains a local privilege-escalation vulnerability that could allow a low-privileged attacker to execute code as root on the NAS node.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-116447

### CVE-2026-116448 — CRITICAL (CVSS: 9.8)

- Published: 2026-11-18T15:17:33.083
- Description: Dell PowerStore SDNAS contains an OS Command Injection vulnerability that could allow an attacker with internal network access to execute arbitrary commands as root on the NAS node.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-116448

### CVE-2026-131801 — HIGH (CVSS: 7.7)

- Published: 2026-11-18T15:17:41.607
- Description: Tanium addressed an improper input validation vulnerability in Threat Response.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-131801

### CVE-2026-132038 — HIGH (CVSS: 7.8)

- Published: 2026-11-18T15:17:41.740
- Description: Rapid7 Metasploit Framework versions prior to 6.5.10 suffer from an Improper Access Control issue in the msfdb database initialisation component whereby a PostgreSQL cluster initialised via msfdb init is configured with trust authentication and a world-accessible Unix domain socket in /tmp, allowing any local user on the same host to authenticate as the passwordless postgres superuser and execute arbitrary operating system commands as the msfdb owner. 


This issue is fixed in version 6.5.10.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132038

### CVE-2026-132150 — HIGH (CVSS: 7.8)

- Published: 2026-11-18T15:17:41.873
- Description: A flaw was found in the file-xmc plugin in GIMP. When processing a specially crafted XMC image file, the plugin does not properly validate the comment subtype before using it as an array index. This missing validation leads to out-of-bounds memory access, invalid free and use-after-free issues. This vulnerability can result in an application crash, leading to a denial of service, or potentially allow for arbitrary code execution.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132150

### CVE-2026-15263 — HIGH (CVSS: 7.1)

- Published: 2026-11-18T15:17:42.033
- Description: A server-side request forgery (SSRF) vulnerability in the Pure Storage FlashArray extension for Windows Admin Center versions could allow an authenticated Gateway User to direct the management gateway to an unintended host, potentially exposing stored FlashArray credentials and API tokens and allowing unauthorized access to the managed FlashArray.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-15263

### CVE-2026-3232 — HIGH (CVSS: 7.2)

- Published: 2026-11-18T15:17:42.550
- Description: The Easy Appointments plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'name' and 'phone' fields in all versions up to, and including, 3.12.23.1 due to insufficient input sanitization and output escaping. This makes it possible for unauthenticated attackers to inject arbitrary web scripts in pages that will execute whenever an administrator accesses the Customers page.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-3232

### CVE-2026-82171 — HIGH (CVSS: 8.0)

- Published: 2026-11-18T15:17:43.763
- Description: Dell PowerStore contains an XML External Entity (XXE) Injection vulnerability. A high-privileged attacker could exploit this vulnerability, potentially leading to disclosure of sensitive files and root-level compromise of the appliance.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-82171

### CVE-2026-95823 — HIGH (CVSS: 7.5)

- Published: 2026-11-18T15:17:44.383
- Description: tcp_pkt_linearize() in subsys/net/ip/tcp.c is used by th_get() whenever a received TCP header is not contiguous in a single net_buf. While pulling the header bytes out of the following fragments, the loop called net_buf_unref() on an emptied fragment without first detaching its frags pointer. net_buf_unref() walks the whole fragment list, so the payload buffers still linked behind that fragment were freed as well, and the stale pointer was then reinstalled into the packet as buf->frags, producing a use-after-free and a later double free during packet teardown. The same loop also advanced to second->frags unconditionally: when the fragment still held payload after the header remainder was pulled, it was spliced out of the packet without ever being unreferenced, permanently leaking that buffer and silently dropping the data it carried.

The defect is reached from tcp_recv() via th_get() on every received TCP segment, before connection lookup or any header validation, so a single unauthenticated segment that matches a listening socket is sufficient. An attacker only needs the TCP header to straddle a net_buf boundary, which they can arrange from off-link: IPv6 extension headers are accepted on receive and their length is added to the header offset by th_get(), so a Destination Options header of a suitable length places the TCP header across the boundary of the fixed-size receive buffers (CONFIG_NET_BUF_DATA_SIZE). Packet chains assembled from several sources - IPv4/IPv6 reassembly, 6LoWPAN/802.15.4 reassembly, tunnel or virtual interfaces that strip an outer header, or drivers producing scatter-gather chains - can additionally present a short interior fragment that the loop empties exactly, which is the case that frees the remainder of the packet while it is still in use.

The reliably reachable consequence is exhaustion of the receive buffer pool: each crafted segment leaks one net_buf from the fixed CONFIG_NET_BUF_RX_COUNT pool, the buffers are never reclaimed, and once the pool is empty the device can no longer receive network traffic until it is rebooted. Where a fragment is emptied exactly, the impact rises to memory corruption: freed pool buffers are written through by the remainder of the loop, their contents may be delivered to the application, and the packet is double-freed on teardown.

The fix saves and clears second->frags before the net_buf_unref() so only the emptied header fragment is released, and advances to the next fragment only when second->len == 0, keeping any fragment that still holds payload in the packet. This restores the detach-before-unref ownership pattern used elsewhere in the stack, for example in net_pkt_trim_buffer().
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-95823

### CVE-2012-20007 — CRITICAL (CVSS: 9.3)

- Published: 2026-11-18T16:17:47.560
- Description: ThinkPHP 2.0 through 2.2 and 3.0 Lite mode contains an eval injection vulnerability in the Dispatcher PATH_INFO parsing, which uses preg_replace with the /e modifier and a double-quoted replacement. Unauthenticated attackers can send crafted requests to index.php with a malicious 's' parameter containing PHP expressions to execute arbitrary code on the server. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-14.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2012-20007

### CVE-2012-20008 — HIGH (CVSS: 8.7)

- Published: 2026-11-18T16:17:47.733
- Description: openSIS 5.1 before 9.0 contains a local file inclusion vulnerability that allows authenticated users to include arbitrary files through the modname parameter of ajax.php. Attackers can prefix a payload with misc/ and use ../ directory traversal to read sensitive files like /etc/passwd or execute local scripts in the web server context. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-19.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2012-20008

### CVE-2016-20105 — CRITICAL (CVSS: 9.2)

- Published: 2026-11-18T16:17:47.940
- Description: Lucee Server versions 5.0.0.0 before 5.3.4.46 contain an insecure default configuration that allows unauthenticated attackers to set the initial admin password via the first-run form on /lucee/admin/web.cfm and /lucee/admin/server.cfm. Attackers can access the 'New Password' set-password form before any password is configured to seize administrative control of the server. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-24.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2016-20105

### CVE-2016-20106 — HIGH (CVSS: 8.7)

- Published: 2026-11-18T16:17:48.120
- Description: NUUO NVRmini 2 through 3.0.8 contains a file disclosure vulnerability that allows unauthenticated attackers to read web-root files by passing a filename to the 'css' parameter of css_parser.php. Attackers can retrieve PHP source files confined to the document root, exposing hardcoded credentials and sensitive application logic. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-17.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2016-20106

### CVE-2018-25443 — CRITICAL (CVSS: 9.3)

- Published: 2026-11-18T16:17:48.500
- Description: Baidu UEditor 1.4.0 through 1.4.3.3 contains an unrestricted file upload vulnerability in the catchimage action of /ueditor/net/controller.ashx that only validates the Content-Type header. Unauthenticated attackers can supply a source[] URL like x.jpg?.aspx to retain a malicious extension and write an executable .aspx file for remote code execution. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-17.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2018-25443

### CVE-2019-25782 — CRITICAL (CVSS: 9.3)

- Published: 2026-11-18T16:17:48.667
- Description: ThinkPHP 5.0.0 before 5.0.24 contains a code injection vulnerability that allows unauthenticated attackers to execute commands by setting _method=__construct in POST data to overwrite the Request filter property. Attackers can send POST requests to endpoints reached via ?s=captcha or ?s=index/index/index with filter[]=system and server[REQUEST_METHOD] values to execute arbitrary system commands. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-14.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2019-25782

### CVE-2019-25784 — HIGH (CVSS: 8.8)

- Published: 2026-11-18T16:17:49.010
- Description: FineCMS versions 5.0.4 before 5.0.11 contain an unauthenticated SQL injection vulnerability in the data2 API action handled by list_tag in libraries/Template.php. Attackers can send GET requests to index.php?c=api&m=data2 with a valid auth hash and the param action=sql sql='...' to execute arbitrary SELECT queries and extract database information. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-14.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2019-25784

### CVE-2019-25785 — HIGH (CVSS: 8.7)

- Published: 2026-11-18T16:17:49.170
- Description: FineReport 8.0 contains a path traversal vulnerability that allows unauthenticated attackers to read arbitrary files through the resourcepath parameter of the /WebReport/ReportServer endpoint. Attackers can send GET requests with op=chart and cmd=get_geo_json to read sensitive files like privilege.xml and extract admin credentials. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-19.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2019-25785

### CVE-2021-48021 — HIGH (CVSS: 8.8)

- Published: 2026-11-18T16:17:50.097
- Description: Chamilo LMS 1.11.10 before 1.11.16 contains an unauthenticated SQL injection vulnerability in the searchOptionsFromTags function through the options parameter of extra_field.ajax.php. Attackers can send POST requests with a malicious JSON options array to inject SQL into the IN clause and extract database information. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-14.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2021-48021

### CVE-2021-48022 — HIGH (CVSS: 8.7)

- Published: 2026-11-18T16:17:50.593
- Description: Rocket.Chat versions 0.61.0 before 3.11.4, 3.12.x before 3.12.4 and 3.13.x before 3.13.2 contain a missing authorization vulnerability allowing unauthenticated attackers to read any room's messages via the livechat:loadHistory Meteor method. Attackers can mint a guest token through livechat:registerGuest and send POST requests to /api/v1/method.callAnon with a target rid parameter to retrieve message history without membership checks. Exploitation evidence was first observed by the Shadowserver Foundation on 2025-02-13.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2021-48022

### CVE-2021-48023 — CRITICAL (CVSS: 9.3)

- Published: 2026-11-18T16:17:50.763
- Description: Weaver E-cology 9.0 contains an unrestricted file upload vulnerability in /page/exportImport/uploadOperation.jsp that allows unauthenticated attackers to upload arbitrary JSP files. Attackers can send a crafted multipart POST request with a JSP webshell written to /page/exportImport/fileTransfer/ to achieve remote code execution. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-20.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2021-48023

### CVE-2021-48025 — CRITICAL (CVSS: 9.3)

- Published: 2026-11-18T16:17:50.927
- Description: OpenSNS 3.2.1 contains an unauthenticated code injection vulnerability in the shareBox method of ShareController that allows attackers to invoke arbitrary model methods via the query parameter. Attackers can send crafted GET requests to /index.php?s=weibo/Share/shareBox abusing parse_str and ShareModel::getInfo to reach Schedule::runSchedule and execute code through assert. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-14.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2021-48025

### CVE-2022-51027 — CRITICAL (CVSS: 9.3)

- Published: 2026-11-18T16:17:51.580
- Description: MeterSphere versions 1.13.0 before 1.14.7 and 1.15.0 before 1.16.4 contain a pre-authentication code injection vulnerability due to the /plugin/** endpoints being exposed with anonymous access. Attackers can upload a malicious jar via POST /plugin/add and invoke it through POST /plugin/customMethod using the 'entry' and 'request' parameters, which are passed to Class.forName and method invocation for remote code execution. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-14.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2022-51027

### CVE-2022-51028 — HIGH (CVSS: 8.8)

- Published: 2026-11-18T16:17:51.760
- Description: CmsEasy 7.7.5_20210919 contains an unauthenticated SQL injection vulnerability in the execsql_action function at /?case=crossall&act=execsql that executes attacker-supplied queries decrypted with the hardcoded key 'cmseasy_sql'. Attackers can send a crafted 'sql' parameter to run arbitrary SQL and dump the admin username and password hash. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-22.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2022-51028

### CVE-2022-51029 — HIGH (CVSS: 8.7)

- Published: 2026-11-18T16:17:51.910
- Description: Synway SMG Gateway Management Software builds through 2022-03-15 contain a path traversal vulnerability that allows unauthenticated attackers to read arbitrary files via the downfile parameter in /down.php. Attackers can send a multipart POST request to /down.php with a traversal path in downfile to retrieve sensitive files like /etc/passwd. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-20.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2022-51029

### CVE-2022-51030 — HIGH (CVSS: 8.7)

- Published: 2026-11-18T16:17:52.063
- Description: QiboCMS V7 contains an arbitrary file download vulnerability in inc/job/download.php that allows unauthenticated attackers to read files by supplying a base64-encoded url parameter to /do/job.php?job=download. Attackers can bypass the .php extension check using the Windows 'ph<' wildcard to download sensitive files such as configuration files containing database credentials. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-18.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2022-51030

### CVE-2022-51034 — HIGH (CVSS: 8.8)

- Published: 2026-11-18T16:17:52.700
- Description: Tangshan Pingsheng Reservoir Safety Supervision Platform builds through 2022-11-30 contain an unauthenticated SQL injection vulnerability in the simcardId parameter of /WebServices/SIMMaintainService.asmx/GetAllRechargeRecordsBySIMCardId. Attackers can send crafted POST requests with time-based MSSQL payloads to extract database information including user, version, and database name. Exploitation evidence was first observed by the Shadowserver Foundation on 2024-07-30.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2022-51034

### CVE-2023-54417 — HIGH (CVSS: 8.7)

- Published: 2026-11-18T16:17:53.193
- Description: Nuxt 3.0.0 before 3.4.2 contains a semi-arbitrary file read vulnerability in the vite-node dev server middleware that allows unauthenticated attackers to read files by supplying an absolute path as the moduleId. Attackers can send GET requests to /__nuxt_vite_node__/module/ with an absolute file path to read sensitive system files. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-19.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2023-54417

### CVE-2023-54418 — HIGH (CVSS: 8.7)

- Published: 2026-11-18T16:17:53.367
- Description: Nuxt 3.0.0-rc.1 before 3.0.0-rc.13 contains an arbitrary file read vulnerability caused by the Vite dev server default setting vite.server.fs.strict=false. Unauthenticated attackers can request /_nuxt/@fs/<absolute path> with a raw query to read arbitrary files like /etc/passwd from the system. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-18.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2023-54418

### CVE-2023-54419 — CRITICAL (CVSS: 9.3)

- Published: 2026-11-18T16:17:53.547
- Description: nginxWebUI 3.0.0 before 3.5.8 contains an authentication bypass vulnerability that allows unauthenticated attackers to reach the /AdminPage/conf/runCmd endpoint by using a case-variant path that evades the case-sensitive /adminPage/ login filter. Attackers can pass OS commands through the cmd parameter, which are executed via /bin/sh with insufficient filtering of & and $() characters, achieving remote code execution. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-14.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2023-54419

### CVE-2023-54420 — HIGH (CVSS: 8.7)

- Published: 2026-11-18T16:17:53.717
- Description: LiveBOS builds through 2023-08-16 contain a path traversal vulnerability that allows unauthenticated attackers to read arbitrary files via the imgName parameter in /feed/ShowImage.do using a ';.js.jsp' suffix bypass. Attackers can send crafted GET requests with directory traversal sequences in imgName to read system files such as /etc/passwd. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-10-30.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2023-54420

### CVE-2023-54422 — CRITICAL (CVSS: 9.3)

- Published: 2026-11-18T16:17:54.023
- Description: iDocView before 13.10.1_20231115 contains an unrestricted file upload vulnerability in the /html/2word endpoint that allows unauthenticated attackers to write arbitrary files by supplying a malicious url parameter. Attackers can send a crafted GET request with the url parameter to download linked resources with an unsanitized path and unblocked .jsp extension, achieving remote code execution. Exploitation evidence was first observed by the Shadowserver Foundation on 2023-11-22.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2023-54422

### CVE-2024-58402 — HIGH (CVSS: 8.8)

- Published: 2026-11-18T16:17:54.363
- Description: Azon Dominator releases through 2024-06-03 contain an SQL injection vulnerability that allows unauthenticated attackers to manipulate database queries through the cid parameter in /fetch_products.php. Attackers can send crafted POST requests with boolean-based or time-based blind payloads to extract sensitive database information. Exploitation evidence was first observed by the Shadowserver Foundation on 2024-07-30.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2024-58402

### CVE-2024-58403 — HIGH (CVSS: 8.7)

- Published: 2026-11-18T16:17:54.547
- Description: AnyShare builds through 2024-11 contain a missing authentication vulnerability in the /api/ShareMgnt/Usrm_GetAllUsers endpoint that exposes user records including password fields. Attackers can send unauthenticated POST requests with a [start,limit] body to retrieve usernames, passwords, and department information for all users. Exploitation evidence was first observed by the Shadowserver Foundation on 2024-12-25.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2024-58403

### CVE-2026-113425 — CRITICAL (CVSS: 9.2)

- Published: 2026-11-18T16:17:59.493
- Description: When NGINX Plus or NGINX Open Source is configured as a mail proxy, undisclosed traffic can cause a use-after-free in an nginx worker process. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR.

Impact:
A remote unauthenticated attacker may crash an nginx worker process or corrupt its memory, disrupting service. Remote code execution is a potential impact. There is no control plane exposure; this is a data plane issue only.



Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-113425

### CVE-2026-116443 — CRITICAL (CVSS: 9.8)

- Published: 2026-11-18T16:17:59.803
- Description: Dell PowerStore SDNAS contains a stack-based buffer overflow in the NAS TFTP service that could allow an unauthenticated remote attacker to cause a denial of service or potential code execution.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-116443

### CVE-2026-116449 — CRITICAL (CVSS: 9.8)

- Published: 2026-11-18T16:17:59.947
- Description: Dell PowerStore SDNAS contains an OS Command Injection vulnerability that could allow an attacker with internal network access to execute arbitrary commands as root on the NAS node.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-116449

### CVE-2026-116953 — CRITICAL (CVSS: 9.3)

- Published: 2026-11-18T16:18:00.197
- Description: Description:

When an iRule that processes client traffic using the GENERICMESSAGE::route command is configured on a virtual server, undisclosed requests can cause the Traffic Management Microkernel (TMM) to terminate and may lead to remote code execution (RCE). 





Impact:



Traffic is disrupted while the TMM process restarts. This vulnerability allows a remote, unauthenticated attacker to cause a denial-of-service (DoS) on the BIG-IP system and may allow the attacker to perform RCE. There is no control plane exposure; this is a data plane issue only.







Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-116953

### CVE-2026-118899 — HIGH (CVSS: 8.7)

- Published: 2026-11-18T16:18:00.357
- Description: When using the listen directive with the ssl parameter in the http block with TLSv1.3 enabled, an attacker can use a specially crafted TLS connection to cause an infinite loop in the NGINX worker process while reading the HTTP request body. As a result, the worker process stops accepting new connections and processing existing connections. Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

Impact: This vulnerability allows a remote, unauthenticated attacker to cause a denial-of-service (DoS) of NGINX. There is no control plane exposure; this is a data plane issue only.



Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-118899

### CVE-2026-120285 — CRITICAL (CVSS: 9.3)

- Published: 2026-11-18T16:18:01.957
- Description: Description
When an HTTP profile and an iRule containing the PSC::ip_address command are configured on a virtual server, undisclosed requests can cause the Traffic Management Microkernel (TMM) to terminate and may lead to remote code execution (RCE).

Impact
Traffic is disrupted while the TMM process restarts. This vulnerability allows a remote, unauthenticated attacker to cause a denial-of-service (DoS) on the BIG-IP system and may allow the attacker to perform RCE. There is no control plane exposure; this is a data plane issue only.



Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-120285

### CVE-2026-120292 — CRITICAL (CVSS: 9.3)

- Published: 2026-11-18T16:18:02.110
- Description: Description:


When an HTTP profile and an iRule using the 

MR::message 

route command are configured on a virtual server, undisclosed requests can cause the Traffic Management Microkernel (TMM) to terminate and may lead to remote code execution (RCE)


Impact:










Traffic is disrupted while the TMM process restarts. This vulnerability allows a remote, unauthenticated attacker to cause a denial-of-service (DoS) on the BIG-IP system and may allow the attacker to perform RCE. There is no control plane exposure; this is a data plane issue only.


Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-120292

### CVE-2026-120718 — CRITICAL (CVSS: 9.2)

- Published: 2026-11-18T16:18:03.013
- Description: Description: 
BIG-IP iControl REST tokens may not expire as expected in all scenarios.   

Impact: 
An attacker who has obtained a token may be able to extend its expiry lifetime unless the token owner deletes it. There is no data plane exposure; this is a control plane issue only.

Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-120718

### CVE-2026-120722 — CRITICAL (CVSS: 9.3)

- Published: 2026-11-18T16:18:03.150
- Description: Description:

When an iRule that processes client traffic using the DNS::scrape command is configured on a virtual server, undisclosed requests can cause the Traffic Management Microkernel (TMM) to terminate and may lead to remote code execution (RCE). 





Impact:



Traffic is disrupted while the TMM process restarts. This vulnerability allows a remote, unauthenticated attacker to cause a denial-of-service (DoS) on the BIG-IP system. In addition, the attacker may be able to perform RCE. There is no control plane exposure; this is a data plane issue only.







Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-120722

### CVE-2026-121805 — CRITICAL (CVSS: 9.3)

- Published: 2026-11-18T16:18:03.607
- Description: Description:

When an iRule that processes client traffic using the PEM::subscriber command is configured on a virtual server, undisclosed requests can cause the Traffic Management Microkernel (TMM) to terminate and may lead to remote code execution (RCE). 





Impact:



Traffic is disrupted while the TMM process restarts. This vulnerability allows a remote unauthenticated attacker to cause a denial-of-service (DoS) on the BIG-IP system and may perform RCE. There is no control plane exposure; this is a data plane issue only.







Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-121805

### CVE-2026-121810 — CRITICAL (CVSS: 9.2)

- Published: 2026-11-18T16:18:03.763
- Description: Description:
This issue affects NGINX Plus and NGINX Open Source configurations that use HTTP/3. A remote, unauthenticated attacker can cause a use-after-free condition in the NGINX worker process, leading to a restart. Exploitation also depends on conditions beyond the attacker’s control. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR.

Impact:
This vulnerability may allow remote attackers to cause a denial-of-service (DoS) on the NGINX system or to possibly trigger a code execution. There is no control plane exposure; this is a data plane issue only.



Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-121810

### CVE-2026-121812 — HIGH (CVSS: 8.7)

- Published: 2026-11-18T16:18:03.910
- Description: Description:


When BIG-IP APM is provisioned, and a virtual server is configured with an APM access profile and a per-request policy, and the tmm.access.policytrace database key is enabled, undisclosed requests can cause the Traffic Management Microkernel (TMM) to terminate. The key is disabled by default.












Impact:



Traffic is disrupted
while the TMM process restarts. This vulnerability allows a remote unauthenticated attacker to cause a denial-of-service (DoS) on the BIG-IP system . There
is no control plane exposure; this is a data plane issue only.





Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-121812

### CVE-2026-123007 — CRITICAL (CVSS: 9.2)

- Published: 2026-11-18T16:18:04.047
- Description: This issue affects NGINX Plus or NGINX Open Source configurations that use HTTP/2. When NGINX processes undisclosed traffic, the flow control window can exceed the allowed threshold, potentially resulting in a heap buffer overflow typically followed by an NGINX worker segmentation fault. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR.

Impact: An attacker could leverage this vulnerability to crash the NGINX worker process, corrupt its memory, or potentially execute code remotely. There is no control plane exposure; this is a data plane issue only.



Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-123007

### CVE-2026-123633 — CRITICAL (CVSS: 9.2)

- Published: 2026-11-18T16:18:04.207
- Description: When NGINX Plus or NGINX Open Source is configured to use HTTP/2 for client connections and proxy client requests to a backend, a specially crafted request can result in use-after-free in the worker process, if this process is running low on worker_connections. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR.




Impact:



This vulnerability may allow remote attackers to cause a denial-of-service (DoS) on the NGINX system or may allow a code execution. There is no control plane exposure; this is a data plane issue only.



Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-123633

### CVE-2026-123634 — CRITICAL (CVSS: 9.2)

- Published: 2026-11-18T16:18:04.353
- Description: This issue occurs when NGINX Plus or NGINX Open Source is configured as a proxy, the proxied server name includes variables, and a Server Side Includes (SSI) or mirror directive sends a subrequest to a location that resolves the same server name. Under these conditions, a specially crafted HTTP request may cause a use-after-free condition in a worker process. An attacker may also be able to execute code if Address Space Layout Randomization (ASLR) is disabled or the attacker can bypass ASLR.

Impact: 
An attacker could leverage this vulnerability to crash the NGINX worker process, corrupt its memory, or perform remote code execution (RCE)



Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-123634

### CVE-2026-123637 — CRITICAL (CVSS: 9.3)

- Published: 2026-11-18T16:18:04.500
- Description: When BIG-IP APM is provisioned and a per-request policy that includes the Client Information agent and Endpoint Security agents is applied to a virtual server, undisclosed requests can cause the Traffic Management Microkernel (TMM) to terminate and may lead to remote code execution (RCE).

Impact:

Traffic is disrupted while the TMM process restarts. This vulnerability allows a remote, unauthenticated attacker to cause a denial-of-service (DoS) on the BIG-IP system and may allow the attacker to perform RCE. There is no control plane exposure; this is a data plane issue only.

Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-123637

### CVE-2026-124990 — CRITICAL (CVSS: 9.8)

- Published: 2026-11-18T16:18:05.313
- Description: The Masteriyo LMS – LMS Course Builder, Quizzes & Certificates plugin for WordPress is vulnerable to PHP Object Injection in versions up to, and including, 3.5.1 via deserialization of untrusted input in the course importer. The set_post_metas() method  calls maybe_unserialize() on attacker-controlled postmeta string values parsed from the uploaded JSON import file. This makes it possible for unauthenticated attackers to inject arbitrary PHP Objects. Exploitation by unauthenticated attackers requires that the site has enable_instructor_registration=true AND enable_guest_checkout=true AND at least one purchasable course exists. Install.php sets enable_instructor_registration=false on fresh installs, so this is a non-default configuration. On a default installation, where that is not configured, the vulnerability requires attackers with author-level access and above.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-124990

### CVE-2026-125272 — HIGH (CVSS: 8.7)

- Published: 2026-11-18T16:18:05.610
- Description: Description:






When BIG-IP APM is licensed and provisioned, and a virtual server with the APM access profile is configured with a per-request policy containing a form-based Logon Page, undisclosed requests can cause the Traffic Management Microkernel (TMM) to terminate.









Impact:


Traffic is disrupted while the TMM process restarts. This vulnerability allows a remote, unauthenticated attacker to cause a denial-of-service (DoS) on the BIG-IP system. There is no control plane exposure; this is a data plane issue only.









Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-125272

### CVE-2026-125274 — HIGH (CVSS: 8.7)

- Published: 2026-11-18T16:18:05.750
- Description: An authenticated iControl SOAP user with at least Guest access can inject an unauthorized management request.





Impact:

This vulnerability may allow an authenticated attacker with network access and at least Guest role privileges to the iControl SOAP utility to execute arbitrary system commands, create or delete files, or disable services. There is no data plane exposure; this is a control plane issue only.





Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-125274

### CVE-2026-126336 — HIGH (CVSS: 8.7)

- Published: 2026-11-18T16:18:07.960
- Description: Description:


When BIG-IP APM is provisioned and a virtual server is configured with an APM Access profile and a SAML Service Provider (SP) agent with encrypted assertions enabled, undisclosed requests can cause the Traffic Management Microkernel (TMM) to terminate.






Impact:


Traffic is disrupted while the TMM process restarts. This vulnerability allows a remote, unauthenticated attacker to cause a denial-of-service (DoS) on the BIG-IP system. There is no control plane exposure; this is a data plane issue only.









Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126336

### CVE-2026-126721 — HIGH (CVSS: 7.5)

- Published: 2026-11-18T16:18:08.267
- Description: The Magic Login Mail or QR Code plugin for WordPress is vulnerable to Privilege Escalation via Administrator Account Takeover in versions up to, and including, 2.07. This is due to the `curpageurl()` function falling back to the raw `$_SERVER['HTTP_HOST']` value — with no validation against the site's configured origin via `home_url()` or `site_url()` — when `get_the_permalink()` returns empty or false, allowing an attacker-controlled Host header to become the URL origin of the magic-login link generated by `generate_url()` and delivered to the target via `wp_mail()`. This makes it possible for unauthenticated attackers to intercept the one-time uid and token pair sent to a targeted Administrator's email and replay them against the real site, causing `autologin_via_url()` to call `wp_set_auth_cookie()` and establish a full Administrator session on the targeted account. Exploitation requires the `[magic_login]` shortcode to render on a path where `get_the_permalink()` returns empty or false (such as a 404 page or a block-theme header template part), the web server to forward non-canonical Host headers, the attacker to know the target administrator's email address, and the administrator to click the attacker-originated magic-login link. Successful exploitation gives the attacker control of a distinct, already-privileged Administrator account; it does not promote the attacker's original account. Successful exploitation additionally requires an action by an administrator — the attacker cannot trigger the vulnerability on their own.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126721

### CVE-2026-126752 — CRITICAL (CVSS: 9.3)

- Published: 2026-11-18T16:18:08.590
- Description: Dagu 1.23.0 before 2.0.0 defaults auth.mode to none, allowing unauthenticated attackers to execute OS commands through the /api/v2/dag-runs endpoint. Attackers can send a POST request with an inline spec defining steps containing arbitrary shell commands to achieve remote code execution. Exploitation evidence was first observed by the Shadowserver Foundation on 2026-03-11.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126752

### CVE-2026-126755 — CRITICAL (CVSS: 9.3)

- Published: 2026-11-18T16:18:09.083
- Description: ArangoDB before 3.12.11 contains an authentication bypass vulnerability caused by a parser differential between the raw path authentication gate and the URL-decoded dispatch logic. Attackers can send requests with a %5f-encoded leading underscore to endpoints like /_db/_system/%5fapi/simple/first-example to reach /_api/* actions as superuser without authentication. Exploitation evidence was first observed by the Shadowserver Foundation on 2026-09-16.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126755

### CVE-2026-126822 — HIGH (CVSS: 8.7)

- Published: 2026-11-18T16:18:09.250
- Description: Description:





When BIG-IP APM is provisioned, an Access Profile is configured as a SAML SP (Service Provider) and is applied to a virtual server, undisclosed requests can cause the Traffic Management Microkernel (TMM) to terminate.

Impact:





Traffic
is disrupted while the TMM process restarts. This vulnerability allows a remote unauthenticated attacker to cause a denial-of-service (DoS) on the BIG-IP system.









There
is no control plane exposure; this is a data plane issue only.






Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-126822

### CVE-2026-127178 — HIGH (CVSS: 8.1)

- Published: 2026-11-18T16:18:09.410
- Description: A stored cross site scripting attack when viewing email aliases in postfixadmin 4.0 before 4.0.7, and postfixadmin 3.3 before 3.3.17 could be caused by signed in admins able to inject aliases.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-127178

### CVE-2026-132224 — HIGH (CVSS: 7.1)

- Published: 2026-11-18T16:18:15.627
- Description: Optimizely Web Experimentation before 2026-11-17 mishandles the account signup flow, leading to presence of attacker-controlled code in the projectJS (aka Project JavaScript) field of certain cdn.optimizely.com assets.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-132224

### CVE-2026-30502 — HIGH (CVSS: 8.2)

- Published: 2026-11-18T16:18:15.847
- Description: A Cross-Site Scripting (XSS) vulnerability in OpenKM v6.3.12 allows attackers to execute arbitrary Javascript in the context of the user's browser via a crafted input injected into the Content parameter.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-30502

### CVE-2026-63189 — CRITICAL (CVSS: 9.8)

- Published: 2026-11-18T16:18:16.520
- Description: Dialoqbase is an application for creating chatbots. Prior to 1.11.5, the unauthenticated GET /api/v1/view/* route in server/src/routes/api/v1/view/root.ts resolves its attacker-controlled wildcard path without normalization or containment, allowing traversal outside the intended uploads directory and arbitrary server file reads. Reading environment files can disclose DB_SECRET_KEY, the application’s JWT signing key, which permits forged administrator tokens and takeover of bots, conversations, integrations, and stored third-party credentials. This issue is fixed in version 1.11.5.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-63189

### CVE-2026-71861 — HIGH (CVSS: 7.4)

- Published: 2026-11-18T16:18:16.967
- Description: The Chainguard SDK is a public Go SDK for integrating with the Chainguard platform. Prior to 0.1.107, auth/aws.VerifyToken trusts the Chainguard-Audience and Chainguard-Identity headers without requiring those headers to be covered by AWS SigV4 SignedHeaders. An attacker with a fresh STS GetCallerIdentity request signed by a victim can rewrite the unsigned binding headers and replay the proof to another relying party, causing the relying party to authenticate the victim’s AWS identity for an attacker-chosen audience and identity. Code that only uses auth/aws.GenerateToken is unaffected because the generator signs the binding headers, and exploitation requires a signed request within its validity window. This issue is fixed in version 0.1.107.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2026-71861

### CVE-2025-64441 — HIGH (CVSS: 8.9)

- Published: 2026-11-18T17:17:26.880
- Description: The ownCloud Desktop Client synchronizes files between an ownCloud server and a desktop. Prior to 6.0.2, an authenticated attacker can share a specially crafted file with a victim. If the file is synced by the client and revealed in the macOS Finder, it can cause operating-system command injection on the victim’s computer. This issue is fixed in version 6.0.2.
- Source: https://nvd.nist.gov/vuln/detail/CVE-2025-64441
