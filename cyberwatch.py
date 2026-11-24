import argparse, json, os
from datetime import datetime, timedelta, timezone
from pathlib import Path
import requests

NVD = "https://services.nvd.nist.gov/rest/json/cves/2.0"
KEV = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"

TASKS = {
    "cve": ("Daily CVE Discovery", "cve-discovery.md"),
    "critical": ("Critical Vulnerability Watch", "critical-vulnerabilities.md"),
    "kev": ("Known Exploited Vulnerabilities", "known-exploited-vulnerabilities.md"),
    "ransomware": ("Ransomware-Relevant Vulnerability Watch", "ransomware-watch.md"),
    "digest": ("Cybersecurity Daily Intelligence Digest", "daily-threat-digest.md"),
}

def get_json(url, params=None, headers=None):
    r = requests.get(url, params=params, headers=headers, timeout=(15, 60))
    r.raise_for_status()
    return r.json()

def fetch_nvd():
    end = datetime.now(timezone.utc)
    start = end - timedelta(days=7)
    params = {
        "pubStartDate": start.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "pubEndDate": end.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "resultsPerPage": 100,
    }
    headers = {}
    if os.getenv("NVD_API_KEY"):
        headers["apiKey"] = os.environ["NVD_API_KEY"]
    data = get_json(NVD, params, headers)
    out = []
    for item in data.get("vulnerabilities", []):
        c = item.get("cve", {})
        desc = next((d.get("value", "") for d in c.get("descriptions", []) if d.get("lang") == "en"), "")
        score, severity = "N/A", "Unknown"
        metrics = c.get("metrics", {})
        for key in ("cvssMetricV40", "cvssMetricV31", "cvssMetricV30"):
            if metrics.get(key):
                cv = metrics[key][0].get("cvssData", {})
                score, severity = cv.get("baseScore", "N/A"), cv.get("baseSeverity", "Unknown")
                break
        out.append({"id": c.get("id", "Unknown"), "published": c.get("published", ""),
                    "description": desc, "score": score, "severity": severity,
                    "url": "https://nvd.nist.gov/vuln/detail/" + c.get("id", "")})
    return out

def fetch_kev():
    return get_json(KEV).get("vulnerabilities", [])

def analyze(task, records):
    key = os.getenv("GEMINI_API_KEY")
    if not key or not records:
        return "AI analysis skipped: API key unavailable or no matching records."
    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    prompt = f"""You are CyberWatch, a defensive cybersecurity analyst.
Task: {TASKS[task][0]}
Analyze only these source records. Do not invent exploit status, affected products,
patches, or mitigations. Separate source facts from interpretation. Give concise
defensive priorities.\n\n{json.dumps(records[:60], ensure_ascii=False)}"""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    r = requests.post(url, params={"key": key},
        json={"contents": [{"parts": [{"text": prompt}]}],
              "generationConfig": {"temperature": 0.2, "maxOutputTokens": 1600}},
        timeout=(15, 120))
    r.raise_for_status()
    return r.json()["candidates"][0]["content"]["parts"][0]["text"]

def run(task):
    nvd, kev = fetch_nvd(), fetch_kev()
    if task == "critical":
        records = [x for x in nvd if str(x["severity"]).upper() in ("HIGH", "CRITICAL")]
    elif task == "kev":
        records = kev[:100]
    elif task == "ransomware":
        records = [x for x in kev if x.get("knownRansomwareCampaignUse", "").lower() == "known"]
    elif task == "digest":
        records = nvd[:35]
    else:
        records = nvd

    if not records:
        print(f"No matching records for {task}; skipping report.")
        return

    summary = analyze(task, records)
    now = datetime.now(timezone.utc)
    lines = [f"# {TASKS[task][0]}", "", f"Generated: {now:%Y-%m-%d %H:%M UTC}",
             f"Records included: {len(records)}",
             "Sources: NVD CVE API 2.0 and CISA KEV catalog", "",
             "## Analyst summary", "", summary, "", "## Findings", ""]
    for item in records:
        if "cveID" in item:
            cve = item.get("cveID", "Unknown")
            lines += [f"### {cve} — {item.get('vulnerabilityName', 'Name unavailable')}",
                      f"- Vendor/product: {item.get('vendorProject', 'Unknown')} / {item.get('product', 'Unknown')}",
                      f"- Date added: {item.get('dateAdded', 'Unknown')}",
                      f"- Required action: {item.get('requiredAction', 'See CISA advisory')}",
                      f"- Ransomware use: {item.get('knownRansomwareCampaignUse', 'Not specified')}",
                      f"- NVD: https://nvd.nist.gov/vuln/detail/{cve}", ""]
        else:
            lines += [f"### {item['id']} — {item['severity']} (CVSS: {item['score']})",
                      f"- Published: {item['published']}",
                      f"- Description: {item['description'] or 'No English description supplied.'}",
                      f"- Source: {item['url']}", ""]
    out = Path("reports") / now.strftime("%Y-%m-%d") / TASKS[task][1]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report saved: {out}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--task", choices=TASKS, required=True)
    run(p.parse_args().task)
