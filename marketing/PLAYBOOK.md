# SOAP Autopilot — First-10-Practices Playbook

**File:** `D:\Hermes_Core\workspace\soap_site\marketing\PLAYBOOK.md`
**Goal:** Land the first 10 paying practices (credible, verifiable outreach — no badge-padding, no fake reviews) in ~4–5 weeks.

**Who to target (in priority order):**
1. **Google Maps "massage near me" spots with NO online-booking link.** Open Maps, search `massage near me` / `license massage therapist` in your metro, and look for listings with phone-only booking. These are exactly the practices still paying for friction and a paper calendar.
2. **Psychology Today / Wellness / Practitioner directories** (therapist, acupuncturist, bodywork sections) — solo providers, prescreened, openly listed.
3. **Local practitioner Facebook groups** (`[Your City] massage therapists`, `[State] bodyworkers`, PT/counselor guilds) — introduce value-first, never pitch.
4. **Your own warm network** — 1–2 practitioners you already know, run them as references (public, named, consenting testimonials).

---

## 10-practice sprint — exact daily actions

**Week 1 — Build the list (Days 1–5)**
- **D1:** Google Maps sweep. Export 10 phone-only-booking massage/bodywork spots (name, phone, "has booking link? no"). → these are leads 1–5.
- **D2:** Directory sweep. Psychology Today + 1 wellness directory for your specialty. Save 10 solo practitioners. → leads 6–10.
- **D3:** Join 2 local practitioner FB groups; read the rules; post a **value** intro (free resource: "a 5-min checklist to kill no-shows"), no product link.
- **D4:** Draft/queue the cold email (**OUTREACH.md** #1) for the 10 leads.
- **D5:** Run the storefront check: open `soap_site/index.html`, confirm buy-intent CTAs are wired to `/signup` (`wire_ctas.py --check`), confirm 8/8 tests green. Send email batch #1.

**Week 2 — Follow-up (Days 6–10)**
- **D6–D7:** No prospecting. Reply to inbound; book 2 screen-share demos.
- **D8:** **Touch 2** (value email #2 in OUTREACH.md) to non-repliers.
- **D9:** Call leads that never reply (call script #3). Log outcome in a simple tracker.
- **D10:** Call the 2 warm-network leads personally; offer $0 Seedling → Professional trial.

**Week 3 — Convert (Days 11–15)**
- **D11:** **Touch 3 / soft close** to all remaining. Drop link, offer to close out their thread.
- **D12–14:** Facilitate signups; onboard on a short screen share; gather consent for named testimonial.
- **D15:** Ask 2 happy practices for a **named, real** review quote; start their GBP presence if not present.

**Week 4 — Compound (Days 16–20)**
- **D16:** Publish 2 verified practitioner testimonials (named + consent).
- **D17:** 1 GBP post / 1 social snippet per converting practice (**GBP_POSTS.md**, **SOCIAL.md**).
- **D18–19:** Repeat the Maps + directory sweep for leads 11–20 (rinse the loop).
- **D20:** Review win-rate; double down on the channel that converted best.

---

## Where to find them (cheat sheet)
- **Google Maps:** query `massage near me`, `licensed massage therapist`, `sports massage`, `deep tissue massage`; filter for no `Book` button.
- **Psychology Today** (`therapists.psychologytoday.com`) / professional directories: filter by your city + specialty.
- **FB groups:** search `<city> massage therapists`, `<state> bodyworkers`, acupuncture/PT guilds — post value, not product.
- **Nextdoor / local business groups:** solo practitioners already active locally.

## Playing field rules (do not violate)
- No scraping PII or contact harvesting at scale without consent; manual, human, one-by-one outreach is the standard.
- Every claim you send must survive the honesty tests: no medical claims, no HIPAA-certification claim, no fabricated stats (prices and test counts must match `billing.py` / the site).
- One human, consenting touch at a time — touch 3 can close the loop, but never harass a "not interested."