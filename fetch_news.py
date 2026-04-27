import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
import json
import os
import re

FEEDS = [
    # Major AI Labs
    ("Anthropic",              "https://www.anthropic.com/rss.xml"),
    ("OpenAI News",            "https://openai.com/news/rss.xml"),
    ("Google DeepMind",        "https://deepmind.google/blog/rss.xml"),
    ("Google AI Blog",         "https://blog.google/technology/ai/rss/"),
    ("Meta AI",                "https://ai.meta.com/blog/rss/"),
    ("Microsoft AI",           "https://blogs.microsoft.com/ai/feed/"),
    ("NVIDIA AI",              "https://blogs.nvidia.com/feed/"),
    ("Hugging Face",           "https://huggingface.co/blog/feed.xml"),
    ("AWS Machine Learning",   "https://aws.amazon.com/blogs/machine-learning/feed/"),
    ("Apple ML Research",      "https://machinelearning.apple.com/rss.xml"),
    # News & Analysis
    ("MIT Technology Review",  "https://www.technologyreview.com/feed/"),
    ("VentureBeat AI",         "https://venturebeat.com/category/ai/feed/"),
    ("AI News",                "https://www.artificialintelligence-news.com/feed/"),
    ("The Verge AI",           "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml"),
    ("TechCrunch AI",          "https://techcrunch.com/category/artificial-intelligence/feed/"),
    ("Wired",                  "https://www.wired.com/feed/rss"),
    ("Ars Technica",           "https://feeds.arstechnica.com/arstechnica/index"),
    ("The Information AI",     "https://www.theinformation.com/feed"),
    ("IEEE Spectrum AI",       "https://spectrum.ieee.org/feeds/topic/artificial-intelligence.rss"),
]

AI_KEYWORDS = [
    "ai", "llm", "gpt", "openai", "anthropic", "machine learning",
    "neural", "model", "deepmind", "gemini", "claude", "artificial intelligence",
    "chatgpt", "mistral", "deepseek", "robot", "automation", "agent",
]

def fetch_feed(name, url, limit=5):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=12) as response:
            content = response.read()
        root = ET.fromstring(content)
        ns = {"atom": "http://www.w3.org/2005/Atom"}

        items = []
        for item in root.findall(".//item")[:limit * 3]:
            title    = (item.findtext("title")       or "").strip()
            link     = (item.findtext("link")        or "").strip()
            pub_date = (item.findtext("pubDate")     or "").strip()
            desc_raw = (item.findtext("description") or "").strip()
            # strip HTML tags
            desc_clean = re.sub(r"<[^>]+>", "", desc_raw).strip()
            desc = desc_clean[:200].rsplit(" ", 1)[0] + "…" if len(desc_clean) > 200 else desc_clean
            if title and link:
                items.append((title, link, pub_date, desc))
            if len(items) >= limit:
                break

        if not items:
            for entry in root.findall(".//atom:entry", ns)[:limit]:
                title    = (entry.findtext("atom:title",   "", ns) or "").strip()
                link_el  = entry.find("atom:link", ns)
                link     = link_el.get("href", "") if link_el is not None else ""
                pub_date = (entry.findtext("atom:updated", "", ns) or "").strip()
                summary  = re.sub(r"<[^>]+>", "", entry.findtext("atom:summary", "", ns) or "").strip()
                desc = summary[:200].rsplit(" ", 1)[0] + "…" if len(summary) > 200 else summary
                if title and link:
                    items.append((title, link, pub_date, desc))

        return items
    except Exception as e:
        print(f"  ✗ {name}: {e}")
        return []

def fetch_hn_ai(limit=5):
    try:
        req = urllib.request.Request(
            "https://hacker-news.firebaseio.com/v0/topstories.json",
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=10) as r:
            ids = json.load(r)[:40]
        results = []
        for sid in ids:
            with urllib.request.urlopen(
                f"https://hacker-news.firebaseio.com/v0/item/{sid}.json", timeout=8
            ) as r:
                s = json.load(r)
            title = s.get("title", "")
            if any(k in title.lower() for k in AI_KEYWORDS):
                results.append((title, s.get("url", f"https://news.ycombinator.com/item?id={sid}"), s.get("score", 0)))
            if len(results) >= limit:
                break
        return results
    except:
        return []

def update_readme_preview(top_stories, today, day):
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        return
    with open(readme_path) as f:
        content = f.read()

    lines = [f"<!-- auto-updated: {today} -->"]
    lines.append(f"**Latest digest: [{day}, {today}](news/{today}.md)**")
    lines.append("")
    lines.append("| # | Headline | Source |")
    lines.append("|---|----------|--------|")
    for i, (title, link, source) in enumerate(top_stories[:8], 1):
        short = title[:72] + "…" if len(title) > 72 else title
        lines.append(f"| {i} | [{short}]({link}) | {source} |")
    lines.append("")
    lines.append(f"_🔄 Auto-updated daily · [View full digest →](news/{today}.md)_")

    new_block = "\n".join(lines)
    updated = re.sub(
        r"<!-- LATEST-START -->.*?<!-- LATEST-END -->",
        f"<!-- LATEST-START -->\n{new_block}\n<!-- LATEST-END -->",
        content,
        flags=re.DOTALL,
    )
    with open(readme_path, "w") as f:
        f.write(updated)
    print("  ✓ README preview updated")

def build_archive_index():
    news_dir = "news"
    files = sorted(
        [f for f in os.listdir(news_dir) if f.endswith(".md")],
        reverse=True,
    )
    lines = ["# 📚 Archive\n", "| Date | Link |", "|------|------|"]
    for fname in files:
        date = fname.replace(".md", "")
        lines.append(f"| {date} | [Read digest](news/{fname}) |")
    with open("ARCHIVE.md", "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"  ✓ ARCHIVE.md updated ({len(files)} digests)")

def main():
    now   = datetime.utcnow()
    today = now.strftime("%Y-%m-%d")
    day   = now.strftime("%A")
    time  = now.strftime("%H:%M UTC")
    output_path = f"news/{today}.md"

    all_stories = []   # (title, link, source) for README preview
    lines = []

    lines.append(f"# 🤖 AI News Digest — {day}, {today}")
    lines.append(f"_Curated daily by **[Abid Redwan](https://aredwan.com)** · **[CodeBeez](https://codebeez.xyz)** · {time}_")
    lines.append("")
    lines.append("> Stay ahead of the AI curve — top headlines from 9 trusted sources, delivered automatically every morning.")
    lines.append("")
    lines.append("---")
    lines.append("")

    total = 0
    for name, url in FEEDS:
        print(f"  Fetching: {name}")
        items = fetch_feed(name, url)
        if items:
            lines.append(f"### {name}")
            for title, link, pub_date, desc in items:
                lines.append(f"- **[{title}]({link})**")
                if desc:
                    lines.append(f"  _{desc}_")
                if pub_date:
                    lines.append(f"  <sub>🕐 {pub_date}</sub>")
                all_stories.append((title, link, name))
            lines.append("")
            total += len(items)

    print("  Fetching: HackerNews AI picks")
    hn = fetch_hn_ai()
    if hn:
        lines.append("### 🔥 Trending on HackerNews")
        for title, url, score in hn:
            lines.append(f"- **[{title}]({url})** — ⭐ {score} pts")
            all_stories.append((title, url, "HackerNews"))
        lines.append("")
        total += len(hn)

    lines.append("---")
    lines.append("")
    lines.append("## 📬 Never Miss a Digest")
    lines.append("")
    lines.append("⭐ **Star this repo** to bookmark it · 👁 **Watch** to get notified · 🍴 **Fork** to customize your own")
    lines.append("")
    lines.append("---")
    lines.append(f"_{total} stories · {len(FEEDS)+1} sources · Next update tomorrow 8:00 AM UTC_")
    lines.append("")
    lines.append("_Made with ☕ by **[Abid Redwan](https://aredwan.com)** · A **[CodeBeez](https://codebeez.xyz)** Project_")

    os.makedirs("news", exist_ok=True)
    with open(output_path, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"  ✓ {total} stories → {output_path}")

    update_readme_preview(all_stories, today, day)
    build_archive_index()

if __name__ == "__main__":
    main()
