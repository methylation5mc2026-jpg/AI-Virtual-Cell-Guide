"""Audit built MkDocs HTML for navigation, mobile and accessibility basics."""

from __future__ import annotations

import argparse
from pathlib import Path
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup

EXPECTED_TABS = {"开始", "知识体系", "学习路线", "实践", "资源目录", "社区"}


def _local_target(site: Path, page: Path, href: str) -> Path | None:
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc or href.startswith(("mailto:", "tel:")):
        return None
    path = unquote(parsed.path)
    if not path:
        return page
    prefix = "/AI-Virtual-Cell-Guide/"
    if path.startswith(prefix):
        target = site / path[len(prefix) :]
    elif path.startswith("/"):
        return None
    else:
        target = page.parent / path
    if target.suffix:
        return target.resolve()
    return (target / "index.html").resolve()


def audit(site: Path) -> list[str]:
    failures: list[str] = []
    pages = sorted(site.rglob("*.html"))
    if len(pages) < 40:
        failures.append(f"expected at least 40 HTML pages, found {len(pages)}")
        return failures

    for page in pages:
        soup = BeautifulSoup(page.read_text(encoding="utf-8"), "html.parser")
        relative = page.relative_to(site)
        html = soup.find("html")
        if not html or not str(html.get("lang", "")).startswith("zh"):
            failures.append(f"{relative}: html language is not Chinese")
        if not soup.find("meta", attrs={"name": "viewport"}):
            failures.append(f"{relative}: missing responsive viewport")
        if page.name != "404.html" and not soup.select_one("main h1"):
            failures.append(f"{relative}: missing main h1")
        for image in soup.select("main img"):
            if not str(image.get("alt", "")).strip():
                failures.append(f"{relative}: image missing alt text")
        for field in soup.select(".md-content input, .md-content select, .md-content textarea"):
            field_id = field.get("id")
            has_label = bool(
                field.get("aria-label")
                or field.get("title")
                or field.find_parent("label")
                or (field_id and soup.find("label", attrs={"for": field_id}))
            )
            if not has_label:
                failures.append(f"{relative}: form control lacks accessible label")
        for anchor in soup.select("main a[href]"):
            target = _local_target(site, page, str(anchor["href"]))
            if target is not None and not target.exists():
                failures.append(f"{relative}: broken internal target {anchor['href']}")

    home = BeautifulSoup((site / "index.html").read_text(encoding="utf-8"), "html.parser")
    tabs = {item.get_text(" ", strip=True) for item in home.select(".md-tabs__item")}
    if tabs != EXPECTED_TABS:
        failures.append(f"top navigation mismatch: {sorted(tabs)}")
    if not home.select_one(".hero"):
        failures.append("homepage hero is missing")
    if len(home.select(".path-card")) != 3:
        failures.append("homepage must expose exactly three learning-path cards")
    return failures


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("site", nargs="?", default="site")
    args = parser.parse_args()
    failures = audit(Path(args.site).resolve())
    if failures:
        raise SystemExit("\n".join(failures))
    print("Site audit passed: responsive metadata, accessibility basics and links")


if __name__ == "__main__":
    main()
