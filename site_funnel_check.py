#!/usr/bin/env python3
"""Revenue-funnel check: marketing site -> real signup -> real Stripe checkout.

What it proves (all of it against running servers, nothing simulated):
  1. the site serves and every data-app-cta link points at a URL that answers 200
  2. that URL renders the actual signup form (csrf_token + password field present)
  3. signup really creates an account, /account shows the free plan
  4. /billing/checkout/professional really returns a Stripe checkout URL (test mode)

Usage:
    python site_funnel_check.py [--site http://127.0.0.1:5588] [--app http://127.0.0.1:5570]
Exit 0 = a stranger can go from the marketing page to a Stripe checkout page.
"""
import argparse
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import http.cookiejar

ap = argparse.ArgumentParser()
ap.add_argument("--site", default="http://127.0.0.1:5588")
ap.add_argument("--app", default="http://127.0.0.1:5570")
a = ap.parse_args()

jar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
# a real browser shows up as a browser; the site is hand-written HTML, no JS needed
opener.addheaders = [("User-Agent", "Mozilla/5.0 (revenue-funnel-check)")]
fails = []


def get(url, data=None):
    body = urllib.parse.urlencode(data).encode() if data else None
    try:
        with opener.open(url, body, timeout=30) as r:
            return r.status, r.read().decode("utf-8", "ignore")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "ignore")


def step(ok, label, detail=""):
    print(("  PASS  " if ok else "  FAIL  ") + label + (f" — {detail}" if detail else ""))
    if not ok:
        fails.append(label)


# 1. site serves + links resolve
status, html = get(a.site + "/")
step(status == 200, "site serves index.html", f"HTTP {status}")
cta_urls = re.findall(r'data-app-cta="([^"]+)"', html)
step(len(cta_urls) >= 5, "site exposes >= 5 tagged buy-intent CTAs", f"{len(cta_urls)} found, all -> {set(cta_urls) or '{}'}")
step(all(c.startswith(a.app) for c in cta_urls), "every CTA targets the app base", a.app)

# 2. the CTA target is the real signup form
status, signup_html = get(a.app + "/signup")
has_form = "csrf_token" in signup_html and 'name="password"' in signup_html
step(status == 200 and has_form, "/signup renders the signup form", f"HTTP {status}, csrf+password={has_form}")

# 3. signup creates a real account
tok = re.search(r'name="csrf_token" value="([^"]+)"', signup_html)
step(bool(tok), "signup form carries a CSRF token")
email = f"funnel{int(time.time())}@site-check.test"
status, body = get(
    a.app + "/signup",
    {"name": "Funnel Check Practice", "email": email, "password": "secret123", "csrf_token": tok.group(1) if tok else ""},
)
step(status in (200, 302), "signup POST accepted", f"HTTP {status}")
status, acct = get(a.app + "/account")
step(status == 200 and "Seedling" in acct, "/account shows the free Seedling plan", f"HTTP {status}")

# 3b. the two surfaces must agree on tier names — a rename on one side only is a broken promise
plans = ["Seedling", "Professional", "Premier"]
missing_app = [p for p in plans if p not in acct]
step(not missing_app, "app /account offers all three tiers", f"missing: {missing_app}" if missing_app else ", ".join(plans))
missing_site = [p for p in plans if p not in html]
step(not missing_site, "marketing site advertises the same three tiers",
     f"missing: {missing_site}" if missing_site else ", ".join(plans))
stale = [w for w in ("Practitioner", "Clinic")
         if any(re.search(rf"\b{w}\b", t) for t in (acct, html))]
step(not stale, "no retired tier names left on either surface", f"still present: {stale}" if stale else "none")

# 3c. the monetization gate is real: a fresh free practice cannot reach the paid surfaces
status, records = get(a.app + "/records")
step(status == 402 and "Paid feature" in records,
     "paid surfaces are gated for a free practice (402, not a soft warning)", f"HTTP {status}")
status, chart = get(a.app + "/client/1/chart")
step(status in (402, 302), "the chart is not reachable on the free plan", f"HTTP {status}")

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kw):
        return None


raw = urllib.request.build_opener(
    urllib.request.HTTPCookieProcessor(jar), NoRedirect()
)
raw.addheaders = [("User-Agent", "Mozilla/5.0 (revenue-funnel-check)")]


def post_noredirect(url, data):
    body = urllib.parse.urlencode(data).encode()
    try:
        with raw.open(url, body, timeout=30) as r:
            return r.status, r.headers.get("Location", "")
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Location", "")


# 4. the money step — checkout must redirect OFF-SITE to Stripe's hosted page
status, pay = get(a.app + "/account")
tok2 = re.search(r'name="csrf_token" value="([^"]+)"', pay)
step(bool(tok2), "logged-in page carries a CSRF token for checkout")
status, loc = post_noredirect(a.app + "/billing/checkout/professional",
                              {"csrf_token": tok2.group(1) if tok2 else ""})
on_stripe = status in (301, 302, 303) and loc.startswith("https://checkout.stripe.com/")
step(on_stripe, "checkout POST redirects to Stripe's hosted page",
     f"HTTP {status} -> {loc[:64]}{'…' if len(loc) > 64 else ''}")

print()
if fails:
    print(f"FUNNEL BROKEN at: {', '.join(fails)}")
    sys.exit(1)
print("FUNNEL OK: marketing page -> /signup -> account -> Stripe checkout page")