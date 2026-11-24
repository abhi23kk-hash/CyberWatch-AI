
import argparse
import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

NVD_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

KEV_URL = (
    "https://www.cisa.gov/sites/default/files/feeds/"
    "known_exploited_vulnerabilities.json"
)

GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

TASKS = {
    "cve": (
        "Daily CVE Discovery",
        "cve-discovery.md"
    ),
    "critical": (
        "Critical Vulnerability Watch",
        "critical-vulnerabilities.md"
    ),
    "kev": (
        "Known Exploited Vulnerabilities",
        "known-exploited-vulnerabilities.md"
    ),
    "ransomware": (
        "Ransomware-Relevant Vulnerability Watch",
        "ransomware-watch.md"
    ),
    "digest": (
        "Cybersecurity Daily Intelligence Digest",
        "daily-threat-digest.md"
    ),
}


# --------------------------------------------------
# HTTP HELPER
# --------------------------------------------------

def get_json(url, params=None, headers=None):

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=(15, 60)
    )

    response.raise_for_status()

    return response.json()


# --------------------------------------------------
# FETCH NVD VULNERABILITIES
# --------------------------------------------------

def fetch_nvd():

    print("Fetching vulnerabilities from NVD...")

    end = datetime.now(timezone.utc)

    start = end - timedelta(days=7)

    params = {
        "pubStartDate": start.strftime(
            "%Y-%m-%dT%H:%M:%S.000Z"
        ),
        "pubEndDate": end.strftime(
            "%Y-%m-%dT%H:%M:%S.000Z"
        ),
        "resultsPerPage": 100,
    }

    headers = {}

    nvd_api_key = os.getenv("NVD_API_KEY")

    if nvd_api_key:
        headers["apiKey"] = nvd_api_key

    data = get_json(
        NVD_URL,
        params=params,
        headers=headers
    )

    results = []

    for item in data.get("vulnerabilities", []):

        cve = item.get("cve", {})

        descriptions = cve.get("descriptions", [])

        description = next(
            (
                d.get("value", "")
                for d in descriptions
                if d.get("lang") == "en"
            ),
            ""
        )

        score = "N/A"
        severity = "Unknown"

        metrics = cve.get("metrics", {})

        for metric_name in (
            "cvssMetricV40",
            "cvssMetricV31",
            "cvssMetricV30"
        ):

            metric_list = metrics.get(metric_name, [])

            if metric_list:

                cvss = metric_list[0].get(
                    "cvssData", {}
                )

                score = cvss.get(
                    "baseScore", "N/A"
                )

                severity = cvss.get(
                    "baseSeverity", "Unknown"
                )

                break

        cve_id = cve.get("id", "Unknown")

        results.append({
            "id": cve_id,
            "published": cve.get("published", ""),
            "modified": cve.get("lastModified", ""),
            "description": description,
            "score": score,
            "severity": severity,
            "url": (
                "https://nvd.nist.gov/vuln/detail/"
                + cve_id
            )
        })

    print(f"NVD records collected: {len(results)}")

    return results


# --------------------------------------------------
# FETCH CISA KEV CATALOG
# --------------------------------------------------

def fetch_kev():

    print("Fetching CISA KEV catalog...")

    data = get_json(KEV_URL)

    vulnerabilities = data.get(
        "vulnerabilities", []
    )

    print(
        f"CISA KEV records collected: "
        f"{len(vulnerabilities)}"
    )

    return vulnerabilities


# --------------------------------------------------
# GEMINI AI ANALYSIS
# --------------------------------------------------

def analyze(task, records):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:

        return (
            "Gemini analysis skipped because "
            "GEMINI_API_KEY is not configured."
        )

    if not records:

        return "No records available for AI analysis."

    model = os.getenv(
        "GEMINI_MODEL",
        "gemini-2.5-flash"
    )

    task_title = TASKS[task][0]

    prompt = f"""
You are CyberWatch, a defensive cybersecurity
vulnerability intelligence analyst.

TASK:
{task_title}

Analyze the supplied cybersecurity records.

REQUIREMENTS:

1. Explain the most important findings.
2. Identify significant vulnerabilities.
3. Explain their potential security impact.
4. Highlight known exploitation information only
   when supported by the supplied records.
5. Provide high-level defensive priorities.
6. Distinguish source facts from interpretation.
7. Do not invent CVEs, affected products, patches,
   exploit activity, or statistics.
8. Use clear Markdown formatting.

SOURCE RECORDS:

{json.dumps(records[:60], ensure_ascii=False)}
"""

    url = (
        "https://generativelanguage.googleapis.com/"
        f"v1beta/models/{model}:generateContent"
    )

    try:

        response = requests.post(
            url,
            params={"key": api_key},
            json={
                "contents": [
                    {
                        "parts": [
                            {"text": prompt}
                        ]
                    }
                ],
                "generationConfig": {
                    "temperature": 0.2,
                    "maxOutputTokens": 1600
                }
            },
            timeout=(15, 120)
        )

        response.raise_for_status()

        result = response.json()

        return (
            result["candidates"][0]
            ["content"]["parts"][0]["text"]
        )

    except (
        requests.RequestException,
        KeyError,
        IndexError,
        TypeError
    ) as error:

        print(
            f"Gemini analysis unavailable: {error}"
        )

        return (
            "Gemini AI analysis was unavailable. "
            "The collected vulnerability records "
            "are retained below for manual review."
        )


# --------------------------------------------------
# SELECT TASK RECORDS
# --------------------------------------------------

def select_records(task, nvd, kev):

    if task == "critical":

        return [
            item for item in nvd
            if str(item["severity"]).upper()
            in ("HIGH", "CRITICAL")
        ]

    elif task == "kev":

        return kev[:100]

    elif task == "ransomware":

        return [
            item for item in kev
            if str(
                item.get(
                    "knownRansomwareCampaignUse", ""
                )
            ).lower() == "known"
        ]

    elif task == "digest":

        return nvd[:35]

    return nvd


# --------------------------------------------------
# BUILD REPORT
# --------------------------------------------------

def generate_report(task, records, summary):

    now = datetime.now(timezone.utc)

    title, filename = TASKS[task]

    lines = [
        f"# {title}",
        "",
        f"Generated: {now:%Y-%m-%d %H:%M UTC}",
        f"Records included: {len(records)}",
        "",
        "## Data Sources",
        "",
        "- National Vulnerability Database (NVD)",
        "- CISA Known Exploited Vulnerabilities (KEV)",
        "",
        "## AI Analyst Summary",
        "",
        summary,
        "",
        "## Vulnerability Findings",
        ""
    ]

    for item in records:

        if "cveID" in item:

            cve_id = item.get(
                "cveID", "Unknown"
            )

            lines.extend([
                f"### {cve_id} — "
                f"{item.get('vulnerabilityName', 'Name unavailable')}",
                "",
                f"- Vendor: {item.get('vendorProject', 'Unknown')}",
                f"- Product: {item.get('product', 'Unknown')}",
                f"- Date added: {item.get('dateAdded', 'Unknown')}",
                f"- Required action: {item.get('requiredAction', 'See CISA advisory')}",
                f"- Due date: {item.get('dueDate', 'Unknown')}",
                f"- Ransomware use: {item.get('knownRansomwareCampaignUse', 'Not specified')}",
                f"- Source: https://nvd.nist.gov/vuln/detail/{cve_id}",
                ""
            ])

        else:

            lines.extend([
                f"### {item['id']} — "
                f"{item['severity']} "
                f"(CVSS: {item['score']})",
                "",
                f"- Published: {item['published']}",
                f"- Description: {item['description'] or 'No English description supplied.'}",
                f"- Source: {item['url']}",
                ""
            ])

    output_dir = (
        Path("reports")
        / now.strftime("%Y-%m-%d")
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = output_dir / filename

    output_file.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    print(f"Report saved: {output_file}")

    return output_file


# --------------------------------------------------
# MAIN EXECUTION
# --------------------------------------------------

def run(task):

    print("=" * 55)
    print("CYBERWATCH SECURITY INTELLIGENCE")
    print("=" * 55)

    print(f"Selected task: {task}")

    nvd = fetch_nvd()

    kev = fetch_kev()

    records = select_records(
        task,
        nvd,
        kev
    )

    print(
        f"Records selected for {task}: "
        f"{len(records)}"
    )

    if not records:

        print(
            "No matching records found. "
            "Skipping report generation."
        )

        return

    summary = analyze(
        task,
        records
    )

    generate_report(
        task,
        records,
        summary
    )

    print("=" * 55)
    print("CYBERWATCH TASK COMPLETED")
    print("=" * 55)


# --------------------------------------------------
# ENTRY POINT
# --------------------------------------------------

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description=(
            "CyberWatch Defensive Security "
            "Intelligence Automation"
        )
    )

    parser.add_argument(
        "--task",
        choices=list(TASKS.keys()),
        required=True
    )

    args = parser.parse_args()

    run(args.task)
