<div align="center">

# 🤖 AI News Tracker

### The internet's AI news — automatically curated, committed & archived. Every. Single. Day.

[![GitHub stars](https://img.shields.io/github/stars/aredwan-xyz/ai-news-tracker?style=social)](https://github.com/aredwan-xyz/ai-news-tracker/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/aredwan-xyz/ai-news-tracker?style=social)](https://github.com/aredwan-xyz/ai-news-tracker/network/members)
[![GitHub last commit](https://img.shields.io/github/last-commit/aredwan-xyz/ai-news-tracker?style=flat-square&color=green&label=last%20update)](https://github.com/aredwan-xyz/ai-news-tracker/commits/main)
[![Automated](https://img.shields.io/badge/🤖%20automated-daily%208am%20UTC-blue?style=flat-square)](https://github.com/aredwan-xyz/ai-news-tracker/actions)
[![Sources](https://img.shields.io/badge/sources-9%20feeds-orange?style=flat-square)](#sources)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

**[📰 Today's Digest](#latest-digest) · [📚 Full Archive](ARCHIVE.md) · [⭐ Star this repo](https://github.com/aredwan-xyz/ai-news-tracker)**

</div>

---

## 💡 What is this?

**AI News Tracker** automatically scrapes **9 of the best AI news sources** every morning and commits a clean, readable markdown digest to this repo — no ads, no paywalls, no noise.

- ✅ **Zero manual effort** — GitHub Actions does everything
- ✅ **9 top sources** in one place
- ✅ **Full archive** going back to day one
- ✅ **Free forever** — no API keys, no subscriptions
- ✅ **Forkable** — set it up for yourself in 2 minutes

---

## 🔴 Latest Digest

<!-- LATEST-START -->
<!-- auto-updated: 2026-04-27 -->
**Latest digest: [Monday, 2026-04-27](news/2026-04-27.md)**

| # | Headline | Source |
|---|----------|--------|
| 1 | [Three reasons why DeepSeek’s new model matters](https://www.technologyreview.com/2026/04/24/1136422/why-deepseeks-v4-matters/) | MIT Technology Review |
| 2 | [The Download: supercharged scams and studying AI healthcare](https://www.technologyreview.com/2026/04/24/1136400/the-download-supercharged-scams-questionable-ai-healthcare/) | MIT Technology Review |
| 3 | [Health-care AI is here. We don’t know if it actually helps patients.](https://www.technologyreview.com/2026/04/24/1136352/health-care-ai-dont-know-actually-helps-patients/) | MIT Technology Review |
| 4 | [The Download: introducing the Nature issue](https://www.technologyreview.com/2026/04/23/1136346/the-download-introducing-nature-issue/) | MIT Technology Review |
| 5 | [Will fusion power get cheap? Don’t count on it.](https://www.technologyreview.com/2026/04/23/1136329/fusion-power-cost/) | MIT Technology Review |
| 6 | [Why AI agents need interaction infrastructure](https://www.artificialintelligence-news.com/news/why-ai-agents-need-interaction-infrastructure/) | AI News |
| 7 | [How AI models use real-time cryptocurrency data to interpret market beha…](https://www.artificialintelligence-news.com/news/how-ai-models-use-real-time-cryptocurrency-data-to-interpret-market-behaviour/) | AI News |
| 8 | [The billion-dollar startup with a different idea for AI](https://www.artificialintelligence-news.com/news/the-billion-dollar-startup-with-a-different-idea-for-ai-ami-labs-yann-lecun/) | AI News |

_🔄 Auto-updated daily · [View full digest →](news/2026-04-27.md)_
<!-- LATEST-END -->

---

## 📡 Sources

| Source | Coverage |
|--------|----------|
| 🧪 **MIT Technology Review** | AI research & breakthroughs |
| ⚡ **VentureBeat AI** | AI industry, startups & funding |
| 🌐 **AI News** | General AI coverage |
| 🔺 **The Verge AI** | AI in tech & culture |
| 🚀 **TechCrunch AI** | AI startups & product launches |
| 🧠 **DeepMind Blog** | Research direct from DeepMind |
| 🤖 **OpenAI News** | Releases & updates from OpenAI |
| 📡 **Wired** | AI trends & longform analysis |
| 🔥 **HackerNews** | Top AI stories voted by developers |

---

## ⚙️ How It Works

```
Every day at 8:00 AM UTC
         │
         ▼
  GitHub Actions triggers
         │
         ▼
  fetch_news.py runs
         │
         ├── 📡 scrapes 9 RSS feeds
         ├── 🔥 filters HackerNews for AI stories
         ├── 📝 writes news/YYYY-MM-DD.md
         ├── 🔄 updates README with latest headlines
         ├── 📚 updates ARCHIVE.md index
         └── ✅ git commit + push
```

---

## 🍴 Fork & Run Your Own

Want your own daily AI digest? Fork this in 2 minutes:

```bash
# 1. Fork this repo on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/ai-news-tracker.git

# 3. That's it — GitHub Actions runs automatically!
# Trigger manually: Actions → Daily AI News → Run workflow
```

> **Customize it:** Edit `FEEDS` in `fetch_news.py` to add/remove sources. Change the cron schedule in `.github/workflows/daily-ai-news.yml`.

---

## 📚 Archive

All past digests are indexed in **[ARCHIVE.md](ARCHIVE.md)** and stored in the [`news/`](./news/) folder.

---

## 🤝 Contributing

Contributions are welcome! Know a great AI news source that's missing?

1. Fork the repo
2. Add your feed to `FEEDS` in `fetch_news.py`
3. Open a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📄 License

MIT © [Abid Redwan](https://aredwan.com) · [CodeBeez](https://codebeez.xyz)

---

<div align="center">

**If this repo saves you time, give it a ⭐ — it helps others find it!**

Made with ☕ by **[Abid Redwan](https://aredwan.com)** · A **[CodeBeez](https://codebeez.xyz)** Project

</div>
