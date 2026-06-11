#!/usr/bin/env python3
"""Report content-freshness signals for the repository.

Two checks:

1. Review age. Markdown files carry a ``<!-- last-reviewed: YYYY-MM -->``
   marker. Files whose marker is older than ``REVIEW_MAX_MONTHS`` are flagged
   as due for review. Content files (under ``Docs/`` and ``Tutorials/``) that
   have no marker at all are also reported.

2. Linked repositories. GitHub repositories linked from the Markdown files are
   checked via the API: any that are archived, or have not been pushed to in
   ``REPO_STALE_MONTHS``, are flagged. (Dead URLs are left to the link checker;
   this catches abandonment that still returns HTTP 200.)

A Markdown report is written to the path given as the first argument *only when
there is something to report*, so the workflow can gate issue creation on the
file's existence. The script always exits 0.
"""

from __future__ import annotations

import glob
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

REVIEW_MAX_MONTHS = int(os.environ.get("REVIEW_MAX_MONTHS", "6"))
REPO_STALE_MONTHS = int(os.environ.get("REPO_STALE_MONTHS", "12"))
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = sys.argv[1] if len(sys.argv) > 1 else "freshness-report.md"

NOW = datetime.now(timezone.utc)

# Owners that are not real repositories when they appear as the first path
# segment of a github.com URL.
NON_REPO_OWNERS = {
    "features", "about", "pricing", "marketplace", "sponsors", "orgs", "apps",
    "users", "user-attachments", "topics", "collections", "settings",
    "notifications", "login", "join", "contact", "site", "readme", "explore",
}

MARKER_RE = re.compile(r"<!--\s*last-reviewed:\s*(\d{4})-(\d{2})\s*-->", re.I)
REPO_RE = re.compile(r"https?://github\.com/([A-Za-z0-9._-]+)/([A-Za-z0-9._-]+)")


def months_since(year: int, month: int) -> int:
    return (NOW.year - year) * 12 + (NOW.month - month)


def md_files() -> list[str]:
    return [
        f.replace("\\", "/")
        for f in glob.glob("**/*.md", recursive=True)
        if not f.replace("\\", "/").startswith(".github/")
    ]


def read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def check_review_age(files: list[str]):
    overdue, unmarked = [], []
    for path in sorted(files):
        text = read(path)
        m = MARKER_RE.search(text)
        if not m:
            if path.startswith(("Docs/", "Tutorials/")):
                unmarked.append(path)
            continue
        year, month = int(m.group(1)), int(m.group(2))
        age = months_since(year, month)
        if age >= REVIEW_MAX_MONTHS:
            overdue.append((path, f"{year:04d}-{month:02d}", age))
    overdue.sort(key=lambda r: r[2], reverse=True)
    return overdue, unmarked


def gh_repo(owner: str, repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "content-freshness-check",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp), None
    except urllib.error.HTTPError as exc:
        return None, exc.code
    except Exception:  # network/transient: skip silently
        return None, "error"


def check_repos(files: list[str]):
    repos: dict[tuple[str, str], set[str]] = {}
    for path in files:
        for owner, repo in REPO_RE.findall(read(path)):
            if owner.lower() in NON_REPO_OWNERS:
                continue
            repo = repo[:-4] if repo.endswith(".git") else repo
            repos.setdefault((owner, repo), set()).add(path)

    archived, stale = [], []
    for (owner, repo) in sorted(repos):
        data, err = gh_repo(owner, repo)
        if err is not None or not data:
            # 404 (renamed/removed) is the link checker's job; transient errors
            # and rate limits are skipped to avoid false alarms.
            continue
        if data.get("archived"):
            archived.append((owner, repo))
            continue
        pushed = data.get("pushed_at")
        if not pushed:
            continue
        then = datetime.strptime(pushed, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        age = (NOW.year - then.year) * 12 + (NOW.month - then.month)
        if age >= REPO_STALE_MONTHS:
            stale.append((owner, repo, pushed[:7], age))
    stale.sort(key=lambda r: r[3], reverse=True)
    return archived, stale


def main() -> int:
    files = md_files()
    overdue, unmarked = check_review_age(files)
    archived, stale = check_repos(files)

    lines: list[str] = []

    if overdue:
        lines.append(f"### Files due for review (older than {REVIEW_MAX_MONTHS} months)\n")
        lines.append("| File | Last reviewed | Age (months) |")
        lines.append("| --- | --- | --- |")
        for path, when, age in overdue:
            lines.append(f"| `{path}` | {when} | {age} |")
        lines.append("")

    if unmarked:
        lines.append("### Content files missing a `last-reviewed` marker\n")
        for path in unmarked:
            lines.append(f"- `{path}`")
        lines.append("")

    if archived:
        lines.append("### Linked repositories that are archived\n")
        for owner, repo in archived:
            lines.append(f"- [{owner}/{repo}](https://github.com/{owner}/{repo}) (archived by its maintainers)")
        lines.append("")

    if stale:
        lines.append(f"### Linked repositories with no activity in {REPO_STALE_MONTHS}+ months\n")
        lines.append("| Repository | Last push | Months idle |")
        lines.append("| --- | --- | --- |")
        for owner, repo, when, age in stale:
            lines.append(f"| [{owner}/{repo}](https://github.com/{owner}/{repo}) | {when} | {age} |")
        lines.append("")

    if not lines:
        print("Content freshness: nothing to report.")
        return 0

    header = (
        "Automated content-freshness report. These items are *signals to review*, "
        "not necessarily problems: a stale or archived project may still be the "
        "right recommendation. Bump a file's `last-reviewed` marker after you "
        "review it.\n"
    )
    report = header + "\n" + "\n".join(lines)
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(report)
    print(f"Content freshness: wrote report to {OUT}")
    print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
