# 🤖 AI News Tracker

<div align="center">

**Built & maintained by [Abid Redwan](https://aredwan.com) · [CodeBeez](https://codebeez.xyz)**

_A daily AI news digest — automatically fetched and committed every morning._

![GitHub last commit](https://img.shields.io/github/last-commit/aredwan-xyz/ai-news-tracker?style=flat-square&color=green)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/aredwan-xyz/ai-news-tracker?style=flat-square&color=blue)
![Automated](https://img.shields.io/badge/automated-daily-brightgreen?style=flat-square)

</div>

---

## What It Does

Every day at **8:00 AM UTC**, a GitHub Actions workflow runs `fetch_news.py`, scrapes the latest AI headlines from 8 top sources, and commits a clean markdown digest to the `news/` folder.

---

## News Sources

| Source | Focus |
|---|---|
| 🧪 MIT Technology Review | AI research & breakthroughs |
| ⚡ VentureBeat AI | AI industry & startups |
| 🌐 AI News | General AI coverage |
| 🔺 The Verge AI | AI in tech & culture |
| 📡 Wired AI | AI trends & analysis |
| 🚀 TechCrunch AI | AI startups & funding |
| 🧠 DeepMind Blog | Research from DeepMind |
| 🤖 OpenAI News | Releases from OpenAI |
| 🔥 HackerNews (AI picks) | Community trending AI stories |

---

## How It Works

```
GitHub Actions (every day 8:00 AM UTC)
        │
        ▼
  fetch_news.py runs
        │
        ├── scrapes 8 RSS feeds (5 stories each)
        ├── filters HackerNews top stories for AI keywords
        ├── writes news/YYYY-MM-DD.md
        ├── git commit
        └── git push → GitHub ✅
```

Can also be triggered manually from the **Actions** tab → **Daily AI News** → **Run workflow**.

---

## Browse the Digests

All daily digests are in the [`news/`](./news/) folder:

```
news/
├── 2026-04-27.md
├── 2026-04-28.md
└── ...
```

---

<div align="center">

Made with ☕ by **[Abid Redwan](https://aredwan.com)** · A **[CodeBeez](https://codebeez.xyz)** Project

</div>
