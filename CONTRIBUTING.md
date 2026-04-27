# Contributing to AI News Tracker

Thanks for your interest in contributing! Here's how to help.

## Adding a News Source

1. Fork the repo and clone it locally
2. Open `fetch_news.py`
3. Add your feed to the `FEEDS` list:
   ```python
   ("Source Name", "https://example.com/feed/rss"),
   ```
4. Test it locally: `python3 fetch_news.py`
5. Open a pull request with a short description of the source

**Good sources to add:** peer-reviewed AI research blogs, official lab blogs, AI policy news, regional AI coverage.

## Reporting Issues

Open an issue if:
- A feed is broken or returning errors
- The digest format looks wrong
- You have a feature suggestion

## Code Style

- Keep it simple — this is a single-file script by design
- Handle errors gracefully (feeds go down, APIs change)
- Test before submitting a PR

---

_Made with ☕ by [Abid Redwan](https://aredwan.com) · [CodeBeez](https://codebeez.xyz)_
