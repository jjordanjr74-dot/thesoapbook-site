# SOAP Autopilot — OFFER

**File:** `D:/Hermes_Core/workspace/soap_site/marketing/OFFER.md`
**Sources:** prices = `D:/Hermes_Core/workspace/soap_autopilot/billing.py` PLANS (price_cents 0 / 1400 / 3900)
and `D:/Hermes_Core/Teams/Marketing/ops/offer_truth.json` (`advertised_prices_usd` "14", "39"). Features =
billing.py docstring + `soap_autopilot/README.md`. Live app: https://app.thesoapbook.com (GET 200, 2026-10-17).

## The offer, in one line
Start on Seedling at $0. Move to Professional at $14/mo when you want online booking and the client portal;
Premier at $39/mo when more than one therapist works in the practice.

## Tiers (exact)
| Tier | Price | Includes (from billing.py / README.md) |
|---|---|---|
| Seedling | $0 | 15 clients, 1 therapist, no online booking; SOAP drafts from dictation or pasted notes |
| Professional | $14/mo | Unlimited clients, 1 therapist, online booking; bookings portal (notice window, cancellation window, policy acceptance, waitlist); client portal (self-serve cancel, intake); recordkeeping (intake forms, signed + locked notes, export bundle) |
| Premier | $39/mo | Everything in Professional, multiple therapists, one flat monthly price |

## How a practice buys
1. Sign up at https://app.thesoapbook.com/signup (Seedling, $0).
2. Upgrade from the account page; checkout is a Stripe session created inside the app for the chosen tier.
   There is no public pay link to send — send the signup link. (LIVE_LINKS.md: "SOAP is sold by demo, not by link".)
3. "Upgrade or downgrade any time. Cancel whenever." Cancelling stops auto-renewal at the end of the current
   period (`web_ui.py` account page copy).

## Objection handling
| They say | Honest answer |
|---|---|
| "I don't trust AI with my notes." | The draft comes from a deterministic engine that maps what you said to named muscles and regions (README). You review and sign every note. |
| "Is it HIPAA certified?" | We make no certification claim. It offers privacy-aligned recordkeeping with encrypted, locked notes (AES-256-GCM field-level encryption, `crypto.py`; signed notes lock with a tamper-evident hash, `recordkeeping.py`). |
| "Where does my dictation audio go?" | Nowhere — dictation runs locally; audio never leaves the device (README). |
| "I already use another booking tool." | Keep it while you try Seedling for notes at $0. Compare when online booking matters. |
| "We have three therapists." | Premier is $39/mo flat for multiple therapists — no per-therapist charge (billing.py). |
| "How many practices use it?" | Say the true number from the app's own records. Never round up or imply traction. |

## Not offered / never say
- No discounts, trials, coupons or annual pricing exist in billing.py — do not invent them.
- No time-saved numbers, outcome claims, customer counts or testimonials.
- No competitor prices unless quoted from a repo file with the file named.
