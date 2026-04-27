import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
import os

FEEDS = [
    ("MIT Technology Review - AI", "https://www.technologyreview.com/feed/"),
    ("VentureBeat AI", "https://venturebeat.com/category/ai/feed/"),
    ("AI News", "https://www.artificialintelligence-news.com/feed/"),
    ("The Verge AI", "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml"),
]

def fetch_feed(name, url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read()
        root = ET.fromstring(content)
        ns = {"atom": "http://www.w3.org/2005/Atom"}

        items = []
        # RSS format
        for item in root.findall(".//item")[:5]:
            title = item.findtext("title", "").strip()
            link = item.findtext("link", "").strip()
            pub_date = item.findtext("pubDate", "").strip()
            if title and link:
                items.append((title, link, pub_date))

        # Atom format
        if not items:
            for entry in root.findall(".//atom:entry", ns)[:5]:
                title = entry.findtext("atom:title", "", ns).strip()
                link_el = entry.find("atom:link", ns)
                link = link_el.get("href", "") if link_el is not None else ""
                pub_date = entry.findtext("atom:updated", "", ns).strip()
                if title and link:
                    items.append((title, link, pub_date))

        return items
    except Exception as e:
        print(f"  Failed to fetch {name}: {e}")
        return []

def main():
    today = datetime.utcnow().strftime("%Y-%m-%d")
    output_path = f"news/{today}.md"

    lines = [f"# AI News — {today}\n"]

    for name, url in FEEDS:
        print(f"Fetching: {name}")
        items = fetch_feed(name, url)
        if items:
            lines.append(f"\n## {name}\n")
            for title, link, pub_date in items:
                lines.append(f"- [{title}]({link})")
                if pub_date:
                    lines.append(f"  *{pub_date}*")

    os.makedirs("news", exist_ok=True)
    with open(output_path, "w") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Saved to {output_path}")

if __name__ == "__main__":
    main()
