# SOAP Autopilot — Outreach Templates

**File:** `D:\Hermes_Core\workspace\soap_site\marketing\OUTREACH.md`
**Use:** cold email (solo practitioners), DM/IG, call script, and a 3-touch follow-up sequence.
**Compliance — read before sending anything (mandatory):**
1. **No medical claims.** Never say we treat, cure, prevent, or diagnose; never imply SOAP improves patient outcomes. We are documentation + practice-management software.
2. **No HIPAA-certification claim.** We may say "privacy-aligned recordkeeping with encrypted, locked notes." We do **not** claim to be a HIPAA-certified product, a business associate, or an official HIPAA partner.
3. **No fake testimonials / no unverifiable stats.** Only real, named, consent-granted customers and file-backed numbers ($14/$39, 8/8 test suites, Stripe checkout verified).
4. Respect opt-outs and CAN-SPAM basics (real sender identity, working opt-out, physical business address in bulk email).
5. Don't imply we're affiliated with ClinicSense, Jane, or MassageBook.

Prices cited below are **verified** (`soap_autopilot/billing.py`, `soap_site/index.html`).

---

## 1. Cold email — solo practitioner

**Subject:** Notes, booking & no-show protection for ~1/5 the price

> Hi [First],
>
> I build practice software for solo therapists. Most all-in-one tools bill $35–70+/mo and still paywall the useful parts — ClinicSense, for example, gates your email/SMS reminders behind its top tier (roughly $69).
>
> SOAP Autopilot puts the whole system on one local-first stack: encrypted, locked SOAP notes + recordkeeping, a client booking portal with self-serve cancel/waitlist, refundable deposits to cut no-shows, and unlimited email reminders from your own mailbox — on a $14/mo Professional plan. You scale to Premier ($39) only if you add multiple therapists.
>
> No per-seat cloud AI fees, no per-therapist licenses. Happy to walk you through a 15-minute no-commitment screen share of the actual product.
>
> Worth 2 minutes? Reply and I'll send a link to the live storefront.
>
> [Your name]
> SOAP Autopilot

---

## 2. DM (Instagram / Facebook / LinkedIn)

> Hi [First] — saw you're [practicing/solo]. I built SOAP Autopilot for therapists who are tired of $35–70/mo software that still paywalls reminders + records.
> Everything-in-one (encrypted notes, booking portal, no-show deposits, reminders) is $14/mo. No per-therapist fees, no per-user AI charges. And I'm happy to do a quick screen share — zero obligation. Open to it?

---

## 3. Call script (~90 sec, leave voicemail or talk)

```
Intro (10s):   "Hi [First], this is [Name] from SOAP Autopilot. I build practice software
               specifically for solo therapists."
Hook (20s):    "I won't keep you — most all-in-one tools run $35–70/mo and still lock
               reminders and recordkeeping behind their top tier. Ours is $14/mo all-in:
               encrypted SOAP notes, booking portal, no-show deposit protection, and
               unlimited email reminders included."
Objection A — "we already use X":   "Totally fair. Do you see no-shows or pay for reminders
               as add-ons where you are? That's the gap we close at $14. Happy to compare."
Objection B — "is it HIPAA safe?":  "We build privacy-aligned recordkeeping with encrypted,
               locked notes and run the notes engine locally. I won't overclaim a
               certification we don't hold — happy to send our security overview."
CTA (15s):     "Can I send you a 2-minute link to the live storefront, and we find 15 min
               this week to peek at it together?"
```

---

## 4. 3-touch follow-up sequence (after first contact)

**Touch 1 — Day 1:** Send the initial email/DM (template #1 or #2).

**Touch 2 — Day 4 (value add, no pitch):**
> Subject: A 5-min fix for a 30-min problem
>
> Hi [First] — quick one, no pitch. The single most common gap I see in solo practices is
> reminder/no-show control: no reflection on you, it's just where the paywalled tools hurt.
> SOAP Autopilot books deposits at booking and queues your own-mailbox reminders automatically.
> If you want, I'll send you the 2-min video of exactly how that works. Otherwise no worries.

**Touch 3 — Day 10 (soft close / drop):**
> Happy to leave this with you [First]. When you're ready, here's the live storefront link —
> $0 Seedling plan has no card, and Professional is $14/mo. I'll close this out unless you'd
> like me to keep you on the list. Good luck with the practice either way.

*(Respect a "not interested" and stop after Touch 3 unless the prospect re-engages.)*

---

## Appendices
- **Storefront:** `soap_site/index.html` — all buy-intent CTAs wired to the app `/signup` (see `wire_ctas.py`).
- **Verified prices:** Seedling $0, Professional $14, Premier $39 (`billing.py`).
- **Proof points to cite:** 8/8 test suites, funnel verified to Stripe checkout, ClinicSense/Jane parity (own-mailbox reminders, deposits, packages/gift certs, locked notes).