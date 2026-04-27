import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
import json
import os

FEEDS = [
    ("MIT Technology Review",       "https://www.technologyreview.com/feed/"),
    ("VentureBeat AI",              "https://venturebeat.com/category/ai/feed/"),
    ("AI News",                     "https://www.artificialintelligence-news.com/feed/"),
    ("The Verge AI",                "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml"),
    ("Wired AI",                    "https://www.wired.com/feed/tag/artificial-intelligence/latest/rss"),
    ("TechCrunch AI",               "https://techcrunch.com/category/artificial-intelligence/feed/"),
    ("DeepMind Blog",               "https://deepmind.google/blog/rss.xml"),
    ("OpenAI News",                 "https://openai.com/news/rss.xml"),
]

def fetch_feed(name, url, limit=5):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=12) as response:
            content = response.read()
        root = ET.fromstring(content)
        ns = {"atom": "http://www.w3.org/2005/Atom"}

        items = []
        for item in root.findall(".//item")[:limit]:
            title    = (item.findtext("title")   or "").strip()
            link     = (item.findtext("link")    or "").strip()
            pub_date = (item.findtext("pubDate") or "").strip()
            desc_raw = (item.findtext("description") or "").strip()
            desc = desc_raw[:180].rsplit(" ", 1)[0] + "…" if len(desc_raw) > 180 else desc_raw
            if title and link:
                items.append((title, link, pub_date, desc))

        if not items:
            for entry in root.findall(".//atom:entry", ns)[:limit]:
                title    = (entry.findtext("atom:title",   "", ns) or "").strip()
                link_el  = entry.find("atom:link", ns)
                link     = link_el.get("href", "") if link_el is not None else ""
                pub_date = (entry.findtext("atom:updated", "", ns) or "").strip()
                summary  = (entry.findtext("atom:summary", "", ns) or "").strip()
                desc = summary[:180].rsplit(" ", 1)[0] + "…" if len(summary) > 180 else summary
                if title and link:
                    items.append((title, link, pub_date, desc))

        return items
    except Exception as e:
        print(f"  Failed to fetch {name}: {e}")
        return []

def fetch_top_hn_ai(limit=3):
    try:
        req = urllib.request.Request(
            "https://hacker-news.firebaseio.com/v0/topstories.json",
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=10) as r:
            ids = json.load(r)[:30]

        results = []
        for story_id in ids:
            with urllib.request.urlopen(
                f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json", timeout=8
            ) as r:
                story = json.load(r)
            title = story.get("title", "")
            if any(kw in title.lower() for kw in ["ai", "llm", "gpt", "openai", "anthropic",
                                                    "machine learning", "neural", "model",
                                                    "deepmind", "gemini", "claude"]):
                url   = story.get("url", f"https://news.ycombinator.com/item?id={story_id}")
                score = story.get("score", 0)
                results.append((title, url, score))
            if len(results) >= limit:
                break
        return results
    except:
        return []

def main():
    now   = datetime.utcnow()
    today = now.strftime("%Y-%m-%d")
    day   = now.strftime("%A")
    time  = now.strftime("%H:%M UTC")
    output_path = f"news/{today}.md"

    lines = []
    lines.append(f"# 🤖 AI News Digest — {day}, {today}")
    lines.append(f"_Curated daily by **[Abid Redwan](https://aredwan.com)** · **[CodeBeez](https://codebeez.xyz)** · Auto-fetched at {time}_")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ── News feeds ────────────────────────────────────────────
    lines.append("## 📰 Latest AI Headlines")
    lines.append("")

    total = 0
    for name, url in FEEDS:
        print(f"Fetching: {name}")
        items = fetch_feed(name, url)
        if items:
            lines.append(f"### {name}")
            for title, link, pub_date, desc in items:
                lines.append(f"- **[{title}]({link})**")
                if desc:
                    lines.append(f"  {desc}")
                if pub_date:
                    lines.append(f"  <sub>{pub_date}</sub>")
            lines.append("")
            total += len(items)

    # ── HackerNews AI picks ───────────────────────────────────
    print("Fetching: HackerNews AI picks")
    hn_items = fetch_top_hn_ai()
    if hn_items:
        lines.append("### 🔥 Trending on HackerNews")
        for title, url, score in hn_items:
            lines.append(f"- **[{title}]({url})** — {score} points")
        lines.append("")

    # ── Footer ────────────────────────────────────────────────
    lines.append("---")
    lines.append(f"_{total} stories fetched across {len(FEEDS)} sources · Next update tomorrow at 8:00 AM UTC_")
    lines.append("")
    lines.append("_Made with ☕ by **[Abid Redwan](https://aredwan.com)** · A **[CodeBeez](https://codebeez.xyz)** Project_")

    os.makedirs("news", exist_ok=True)
    with open(output_path, "w") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Done — {total} stories saved to {output_path}")

if __name__ == "__main__":
    main()
