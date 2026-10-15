# SOAP Autopilot — Positioning

**File:** `D:\Hermes_Core\workspace\soap_site\marketing\POSITIONING.md`
**Owner:** SOAP marketing / outreach
**Status:** Internal working doc — claims below are verified against code + site on disk (cited inline). Do not publish any claim marked `verify-before-publish`.

---

## 1. Who we are for (primary ICP)

- **Solo practitioners** (1 therapist, self-employed massage therapists, acupuncturists, PT's, counselors) who currently run their practice on paper, spreadsheets, or a generic calendar.
- **Small clinics** (2–8 therapists) that want an all-in-one bookkeeping + client portal + revenue tool without paying per-therapist license fees.

We win margins on the low end. We are intentionally **not** chasing enterprise multi-location franchises — Jane and ClinicSense own that and it's not our cost structure.

## 2. Verified product facts (cite the file, do not drift)

| Feature | Fact | Source on disk |
|---|---|---|
| Seedling plan | **$0/mo** — up to 15 clients, 1 therapist, voice dictation, SOAP notes + body chart | `soap_site/index.html` (Seedling card) |
| Professional plan | **$14/mo** — unlimited clients, 1 therapist, online booking, client bookings portal (self-serve cancel + waitlist), intake forms, **refundable deposits at booking**, **unlimited email reminders from your own mailbox**, mobile app | `soap_autopilot/billing.py` (price_cents 1400), `soap_site/index.html` (Professional card) |
| Premier plan | **$39/mo** — everything in Professional + signed & locked recordkeeping notes, chart timeline, record export, packages & gift certificates, multiple therapist seats, business analytics, patient portal, marketing tools | `soap_autopilot/billing.py` (price_cents 3900), `soap_site/index.html` (Premier card) |
| Reminders not paywalled | Email/SMS reminder queueing is included at the **$14 Professional** tier, not gated to a top tier | `soap_autopilot/notify.py` (docstring: "we queue reminders on the $14 plan") |
| Stripe checkout | Pre-provisioned live price IDs wired (`professional` / `premier`) | `soap_autopilot/stripe_prices_test.json`, `billing.py` |
| Storefront CTA | Buy-intent CTAs wired to the app `/signup` (not dead `#` anchors) | `soap_site/wire_ctas.py`, `soap_site/index.html` (`data-app-cta`) |
| Test suite | 8/8 suites passing | `soap_autopilot/test_*.py`, `conftest.py` |

Plan names & prices are **verified** against `billing.py` and the live site HTML. Use only `$0 / $14 / $39`. Legacy alias `practitioner→professional`, `clinic→premier` (`billing.py`).

## 3. Competitive frame (internal, used to sell — phrase carefully in public copy)

- **ClinicSense** — public pricing is roughly **$35–70/mo** for the tiers we emulate; notably it **gates email/SMS reminders behind its top ~$69 tier** (per `soap_autopilot/notify.py`). Our equivalent reminder queueing is on the $14 plan.
- **MassageBook** — gates reminders behind ~$59; we include them at $14.
- **Jane** — excellent EMR but priced for multi-practitioner clinics; overkill and pricey for a solo practitioner.
- **Our edges (defensible):**
  1. **Local-first, $0 per-user inference** — the notes engine can run on the practice's own hardware with no per-seat cloud LLM/token costs and no per-therapist license fee. Cost scales with your practice, not your headcount.
  2. **Reminders included, not paywalled** — deposit/no-show protection (refundable deposits at booking) plus unlimited own-mailbox email reminders, on the Professional tier.
  3. **All-in-one at a small-clinic price** — recordkeeping, client portal, and revenue/booking tools in one $14/$39 package instead of $35–70+ for a feature set we match.
  4. **Verifiable quality** — 8/8 test suites, funnel verified to Stripe checkout.

## 4. Honesty guardrails (mandatory)

- **No medical claims.** SOAP is documentation/practice-management software. We never claim to treat, cure, prevent, or diagnose any condition, and we never imply it improves patient outcomes.
- **No HIPAA "certification" claim.** We provide HIPAA-aligned / HIPAA-grade **features** (encrypted recordkeeping, HMAC-locked notes) — we do **not** claim to be a HIPAA-certified/BA-partner product unless we hold that designation. Say "privacy-aligned recordkeeping with encrypted, locked notes," not "HIPAA certified."
- **No fake testimonials.** Use only named, real, consent-granted customer quotes.
- **No fabricated stats.** Every number (prices, tests, feature tiers) traces to a file cited above.
- **Competitor pricing** in public ads must be worded as "public pricing I've seen runs approximately…" and re-checked before launch (`verify-before-publish`).