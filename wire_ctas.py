#!/usr/bin/env python3
"""Wire soap_site product CTAs to the real app URL — idempotent, with a --check gate.

Why: every buy-intent button on the marketing site was `href="#"` (nav "Try Free",
hero "Start Your Free Note", pricing "Start Free" / "Go Professional" / "Contact Us").
A visitor could not reach /signup at all, so no live Stripe key could ever earn a dollar.

The app has no `?tier` / `?next` handling on /signup and checkout is a POST behind login,
so every plan CTA lands on `<base>/signup` — the account page is where the plan is picked.

The logo anchor (`href="#"` scroll-to-top on a one-pager) is NOT a CTA and is left alone.

Usage:
    python wire_ctas.py --check                 # exit 1 while any buy-intent CTA is dead
    python wire_ctas.py --base https://host     # rewrite (trailing slash tolerated)
    python wire_ctas.py --base http://127.0.0.1:5570
"""
import argparse
import re
import sys
from pathlib import Path

SITE = Path(r"D:\Hermes_Core\Workspace\soap_site\index.html")
MARK = "data-app-cta"

# button label (as it appears in the HTML) -> app path
CTAS = {
    "Start Your Free Note": "/signup",
    "Try Free": "/signup",
    "Start Free": "/signup",
    "Go Professional": "/signup",
    "Contact Us": "/signup",
}

# only anchors that actually contain a buy-intent label count as CTAs
LABEL_ALT = "|".join(re.escape(k) for k in CTAS)


def anchors(html: str):
    """Return [(full_match, href, label)] for every <a …>…</a> containing a CTA label."""
    out = []
    for m in re.finditer(r"<a\s[^>]*>.*?</a>", html, re.S):
        text = re.sub(r"<[^>]+>", "", m.group(0)).strip()
        text = re.sub(r"\s+", " ", text)
        if text in CTAS:
            href = re.search(r'href="([^"]*)"', m.group(0))
            out.append((m.group(0), href.group(1) if href else None, text))
    return out


def base_of(html: str):
    m = re.search(rf'{MARK}="([^"]+)"', html)
    return m.group(1) if m else None


def check(html: str) -> int:
    found = anchors(html)
    dead = [t for _, h, t in found if h in ("#", "", None)]
    wired = [t for _, h, t in found if h and h.startswith("http")]
    malformed = html.count('""')
    print(f"{SITE}")
    print(f"  buy-intent anchors     : {len(found)}")
    print(f"  dead href=\"#\" CTAs     : {len(dead)}")
    print(f"  CTAs on a real app URL : {len(wired)}")
    print(f"  malformed \"\" sequences : {malformed}")
    if malformed:
        print("  FAIL: doubled quotes in the markup — an earlier rewrite damaged the anchors.")
        return 1
    if dead:
        print(f"  FAIL: CTAs point nowhere ({', '.join(dead)}) — a visitor cannot reach /signup.")
        return 1
    if len(found) < len(CTAS):
        print(f"  FAIL: expected >= {len(CTAS)} buy-intent anchors, found {len(found)}.")
        return 1
    if len(re.findall(rf'{MARK}=', html)) < len(found):
        print("  WARN: some CTAs are wired but untagged (no data-app-cta); re-run with --base.")
    print("  PASS: every buy-intent CTA carries a real app URL.")
    return 0


def wire(html: str, base: str) -> str:
    base = base.rstrip("/")
    if not re.match(r"^https?://", base):
        sys.exit(f"--base must be an absolute http(s) URL, got: {base}")

    # idempotency + healing: drop any marker we added previously, and collapse the doubled
    # quotes an earlier version of this script left behind (`href="url""` -> `href="url"`).
    html = re.sub(rf'\s*{MARK}="[^"]*"', "", html)
    html = html.replace('""', '"')

    n = 0
    for m in list(re.finditer(r"<a\s[^>]*>.*?</a>", html, re.S)):
        block = m.group(0)
        text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", block)).strip()
        if text not in CTAS:
            continue
        url = base + CTAS[text]
        new_block = re.sub(r'href="[^"]*"', f'href="{url}"', block, count=1)
        new_block = new_block.replace(f'href="{url}"', f'href="{url}" {MARK}="{url}"', 1)
        if new_block != block:
            html = html.replace(block, new_block, 1)
            n += 1
    print(f"  rewrote {n} anchor(s) -> {base}")
    return html


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", help="absolute app URL, e.g. https://soap.example.com")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    if not SITE.exists():
        sys.exit(f"FAIL: {SITE} not found")
    html = SITE.read_text(encoding="utf-8")

    if a.check or not a.base:
        prev = base_of(html)
        if prev:
            print(f"  current app base: {prev}")
        return check(html)

    out = wire(html, a.base)
    SITE.write_text(out, encoding="utf-8")
    return check(out)


if __name__ == "__main__":
    sys.exit(main())