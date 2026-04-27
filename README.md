<div align="center">

# 🤖 AI News Tracker

### The internet's AI news — automatically curated, committed & archived. Every. Single. Day.

[![GitHub stars](https://img.shields.io/github/stars/aredwan-xyz/ai-news-tracker?style=social)](https://github.com/aredwan-xyz/ai-news-tracker/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/aredwan-xyz/ai-news-tracker?style=social)](https://github.com/aredwan-xyz/ai-news-tracker/network/members)
[![GitHub last commit](https://img.shields.io/github/last-commit/aredwan-xyz/ai-news-tracker?style=flat-square&color=green&label=last%20update)](https://github.com/aredwan-xyz/ai-news-tracker/commits/main)
[![Automated](https://img.shields.io/badge/🤖%20automated-daily%208am%20UTC-blue?style=flat-square)](https://github.com/aredwan-xyz/ai-news-tracker/actions)
[![Sources](https://img.shields.io/badge/sources-19%20feeds-orange?style=flat-square)](#sources)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

**[📰 Today's Digest](#latest-digest) · [📚 Full Archive](ARCHIVE.md) · [⭐ Star this repo](https://github.com/aredwan-xyz/ai-news-tracker)**

</div>

---

## 💡 What is this?

**AI News Tracker** automatically scrapes **19 of the best AI news sources** every morning and commits a clean, readable markdown digest to this repo — no ads, no paywalls, no noise.

- ✅ **Zero manual effort** — GitHub Actions does everything
- ✅ **19 sources** in one place — labs, blogs & news
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
| 1 | [Our principles](https://openai.com/index/our-principles) | OpenAI News |
| 2 | [GPT-5.5 System Card](https://openai.com/index/gpt-5-5-system-card) | OpenAI News |
| 3 | [Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5) | OpenAI News |
| 4 | [Top 10 uses for Codex at work](https://openai.com/academy/top-10-use-cases-codex-for-work) | OpenAI News |
| 5 | [How to get started with Codex](https://openai.com/academy/codex-how-to-start) | OpenAI News |
| 6 | [Decoupled DiLoCo: A new frontier for resilient, distributed AI training](https://deepmind.google/blog/decoupled-diloco/) | Google DeepMind |
| 7 | [Partnering with industry leaders to accelerate AI transformation](https://deepmind.google/blog/partnering-with-industry-leaders-to-accelerate-ai-transformation/) | Google DeepMind |
| 8 | [Gemini 3.1 Flash TTS: the next generation of expressive AI speech](https://deepmind.google/blog/gemini-3-1-flash-tts-the-next-generation-of-expressive-ai-speech/) | Google DeepMind |

_🔄 Auto-updated daily · [View full digest →](news/2026-04-27.md)_
<!-- LATEST-END -->

---

## 📡 Sources

### 🏢 Major AI Labs
| Source | Coverage |
|--------|----------|
| 🟣 **Anthropic** | Claude, safety research & releases |
| 🤖 **OpenAI** | GPT, Sora, Codex & product updates |
| 🧠 **Google DeepMind** | Gemini, AlphaFold & frontier research |
| 🔵 **Google AI Blog** | Google's broader AI initiatives |
| 👥 **Meta AI** | LLaMA, open-source AI & research |
| 🪟 **Microsoft AI** | Copilot, Azure AI & partnerships |
| 💚 **NVIDIA AI** | GPU tech, CUDA & AI infrastructure |
| 🤗 **Hugging Face** | Open models, datasets & ML tooling |
| ☁️ **AWS Machine Learning** | Cloud AI services & launches |
| 🍎 **Apple ML Research** | On-device AI & Core ML |

### 📰 News & Analysis
| Source | Coverage |
|--------|----------|
| 🧪 **MIT Technology Review** | AI research & breakthroughs |
| ⚡ **VentureBeat AI** | AI industry, startups & funding |
| 🌐 **AI News** | General AI coverage |
| 🔺 **The Verge AI** | AI in tech & culture |
| 🚀 **TechCrunch AI** | AI startups & product launches |
| 📡 **Wired** | AI trends & longform analysis |
| 🖥 **Ars Technica** | Technical AI deep-dives |
| 📊 **IEEE Spectrum** | Engineering & AI research |
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
         ├── 📡 scrapes 19 RSS feeds
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
