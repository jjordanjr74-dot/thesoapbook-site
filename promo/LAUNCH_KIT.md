# SOAP Autopilot — Promo Launch Kit (thesoapbook.com/promo/)

Staged on disk only. Nothing here has been committed, pushed or posted. Every price traces to
`D:/Hermes_Core/workspace/soap_autopilot/billing.py` (PLANS price_cents 0 / 1400 / 3900) and
`D:/Hermes_Core/Teams/Marketing/ops/offer_truth.json` (`advertised_prices_usd` "14", "39").

## 1. Package index
| File | What it is |
|---|---|
| `promo/index.html` | Self-contained landing page: hero, 3 value props, demo (video + app link), pricing, FAQ, CTA band, footer. CSP self + inline; zero external requests. |
| `promo/fonts/fraunces-600-latin.woff2`, `promo/fonts/inter-var-latin.woff2` | Self-hosted fonts (SIL OFL 1.1). |
| `promo/fonts/LICENSE`, `promo/fonts/OFL-Fraunces.txt`, `promo/fonts/OFL-Inter.txt` | Font licences. |
| `promo/assets/og.png` | 1200x630 link-preview card. |
| `promo/assets/social_1080.png` | 1080x1080 feed card with exact prices. |
| `promo/assets/scenes/scene1..6_*.png` | 1920x1080 storyboard cards for the video. |
| `promo/video/soap_16x9.jpg` | Video poster (1920x1080). |
| `promo/video/BRIEF.md` | 6-scene storyboard, VO lines, voice, durations. |
| `promo/video/storyboard.json` | Renderer input for `Teams/Marketing/video/make_promo_video.py` (dry-run VALIDATION OK, exit 0). |
| `promo/assets/scenes/video_bg1..5_*.png` + `_make_video_bg.py` | Text-free 1920x1080 backgrounds the renderer captions over. |
| `promo/video/soap_16x9.mp4` | **Not yet rendered** — lands at exactly this path; the page already embeds it. |
| `promo/_manifest.json` | Byte-verified file list + verified_against map. |

## 2. Deploy (owner runs — NOT executed by the builder)
Repo: `D:/Hermes_Core/workspace/soap_site`, branch `gh-pages`, remote
`origin https://github.com/jjordanjr74-dot/thesoapbook-site.git`, `CNAME` = thesoapbook.com (GitHub Pages).
```bash
cd D:/Hermes_Core/workspace/soap_site
git status --short                      # expect: ?? promo/
python -m http.server 8765              # optional local look: http://127.0.0.1:8765/promo/
git add promo/
git commit -m "promo: type-led SOAP Autopilot landing + og/social cards + video storyboard"
git push origin gh-pages
curl -s -o /dev/null -w "%{http_code}\n" https://thesoapbook.com/promo/   # expect 200 after Pages builds
```
Render: `python D:/Hermes_Core/Teams/Marketing/video/make_promo_video.py --storyboard D:/Hermes_Core/workspace/soap_site/promo/video/storyboard.json --out D:/Hermes_Core/workspace/soap_site/promo/video` (writes `soap_16x9.mp4` in place; also overwrites `soap_16x9.jpg`). Then re-run the manifest byte check, commit, push.
Note: the zone's Cloudflare CSP is self + inline — this page needs nothing more (fonts, poster and video are same-origin).

## 3. Video placement (practitioner audience)
| Channel | Cut | Where it goes | Notes |
|---|---|---|---|
| YouTube Shorts | 9:16, <=30 s (re-render the cards at 1080x1920) | Brand channel; link in description to thesoapbook.com/promo/ | Captions burned in; title "Dictate the session, get the SOAP draft" |
| Instagram / Facebook Reels | 9:16, same cut | Brand account; pin to profile | Cover = scene 2 card; no paid boost without owner approval (spend gate) |
| LinkedIn | 16:9 `soap_16x9.mp4` native upload | Owner's profile + any massage-therapy / bodywork groups that allow tools posts | Link to thesoapbook.com/promo/ in the post or first comment |
| Landing page | 16:9 embed | `promo/index.html` demo section | Already wired |

## 4. Two-week posting cadence (drafted and staged — a human presses publish)
| Day | Channel | Asset | Copy angle |
|---|---|---|---|
| D1 Mon | LinkedIn | `soap_16x9.mp4` (or `social_1080.png` until the mp4 exists) | Dictate the session, get the SOAP draft |
| D2 Tue | Instagram feed | `social_1080.png` | Prices up front: Seedling $0 / Professional $14 / Premier $39 |
| D3 Wed | Shorts + Reels | 9:16 cut | Scene 3: dictation audio stays on your device |
| D5 Fri | Facebook practitioner groups (where rules allow) | `og.png` link preview | Value-first: self-serve cancel + waitlist on Professional |
| D7 Sun | — | — | Rest; reply to comments only |
| D8 Mon | LinkedIn | scene4 card | Signed notes lock; corrections become amendments |
| D9 Tue | Instagram story | scene5 card | Clients cancel within your policy |
| D10 Wed | Shorts + Reels | 9:16 cut, re-captioned | Premier: multiple therapists, one flat $39/mo |
| D12 Fri | LinkedIn + FB | end-card scene6 | Start free at thesoapbook.com |
| D14 Sun | — | — | Review: link clicks and Seedling signups from the app's own records (never quote numbers you have not measured) |

## 5. Staged-vs-live truth table (measured 2026-10-17)
| Item | State | Evidence |
|---|---|---|
| https://app.thesoapbook.com | **LIVE** (named Cloudflare tunnel `soap-app` -> 127.0.0.1:5570) | `curl` -> HTTP 200; `/signup` -> HTTP 200 |
| https://thesoapbook.com (main site) | **LIVE** (GitHub Pages behind Cloudflare) | `curl` -> HTTP 200 |
| Main site CTAs | **LIVE**, 5/5 wired to app signup | `python wire_ctas.py --check` -> PASS |
| Main site tier names | Correct: Seedling / Professional / Premier | grep of index.html: 0 hits for the stale names |
| thesoapbook.com/promo/ | **STAGED** (files on disk, untracked in git) | `git status --short` -> `?? promo/` |
| Promo video mp4 | **NOT RENDERED** | storyboard + poster + scene cards exist; mp4 path empty |
| Public cs_live checkout link for SOAP | **NONE** — checkout is a POST behind login inside the app | LIVE_LINKS.md: "SOAP is sold by demo, not by link"; every CTA = app signup |
| Paying customers | Not claimed anywhere in this kit | — |
| Social posts / outreach | **STAGED** (human gate) | offer_truth.json `human_gates` |
