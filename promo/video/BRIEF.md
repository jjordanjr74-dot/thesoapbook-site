# SOAP Autopilot — promo video storyboard (16:9, ~28 s)

**Output path (exact):** `D:/Hermes_Core/workspace/soap_site/promo/video/soap_16x9.mp4` — the landing page
(`promo/index.html`) already embeds `<video poster="video/soap_16x9.jpg" src="video/soap_16x9.mp4">`.
**Poster (exists):** `D:/Hermes_Core/workspace/soap_site/promo/video/soap_16x9.jpg` (1920x1080).
**Audience:** licensed massage therapists (solo and small practices).
**Look:** type-led cards, ink #111827, honey #f2603a, Fraunces SemiBold + Inter. No photography; no stock faces.
**Voice (verified on this host, `edge-tts --list-voices | grep en-US`):** `en-US-AvaNeural`
(Female — "Expressive, Caring, Pleasant, Friendly"). Alternate: `en-US-AndrewNeural` (Male — "Warm, Confident,
Authentic, Honest"). Render example:
`edge-tts --voice en-US-AvaNeural --rate -5% --text "<VO line>" --write-media scene1.mp3`

Every VO line was checked against the repo (source per scene). No banned superlatives, no certification
claim, no time-saving numbers, no outcome claims.

| # | Visual asset (absolute path, exists) | Headline (<=6 words) | Sub (<=10 words) | VO line (<=14 words) | Duration | Source |
|---|---|---|---|---|---|---|
| 1 | `D:/Hermes_Core/workspace/soap_site/promo/assets/scenes/scene1_notes_waiting.png` | Session done. Notes still waiting. | The charting that follows every session. | You finished the last session. Now the notes are waiting. | 4 s | framing only, no claim |
| 2 | `D:/Hermes_Core/workspace/soap_site/promo/assets/scenes/scene2_dictate.png` | Dictate it. Get a SOAP draft. | Speak or paste the session; review a structured draft. | Dictate or paste your session, and SOAP Autopilot drafts a complete SOAP note. | 5 s | soap_autopilot/README.md; soap_engine.py docstring |
| 3 | `D:/Hermes_Core/workspace/soap_site/promo/assets/scenes/scene3_local_audio.png` | Audio stays on your device. | Voice dictation runs locally on your own machine. | Voice dictation runs locally, so the audio never leaves your device. | 4 s | README.md "audio never leaves the device" |
| 4 | `D:/Hermes_Core/workspace/soap_site/promo/assets/scenes/scene4_sign_lock.png` | Sign it. Lock it. | Corrections become amendments, never silent edits. | Signed notes lock with a tamper-evident hash. Corrections become amendments. | 5 s | recordkeeping.py docstring |
| 5 | `D:/Hermes_Core/workspace/soap_site/promo/assets/scenes/scene5_cancel_waitlist.png` | Self-serve cancel and waitlist. | Clients manage visits within your policy. | On Professional, clients cancel within your policy and join a waitlist themselves. | 5 s | README.md client + bookings portal (Professional+) |
| 6 (end-card) | `D:/Hermes_Core/workspace/soap_site/promo/assets/scenes/scene6_endcard.png` | Start free at thesoapbook.com | Seedling $0 · Professional $14/mo · Premier $39/mo | Start free on Seedling at thesoapbook dot com. Upgrade when you're ready. | 5 s | billing.py PLANS; offer_truth.json |

End-card on screen: **thesoapbook.com** + **Start free** (both drawn on scene6_endcard.png).

## Assembly notes
- Hold each card for its duration; 300 ms cross-fade between cards; no zoom on the end-card.
- Burn the headline as on-card text (already drawn); add the sub as a lower caption only for vertical cuts.
- Vertical (9:16) cuts for Shorts/Reels: centre-crop is NOT safe (text is left-aligned) — re-render the same
  copy at 1080x1920 with `poster()` from the generator pattern rather than cropping.
- Music: none, or a royalty-free bed at -24 LUFS under the VO. Captions on (most practitioners watch muted).

## Machine storyboard (renderer input)
`D:/Hermes_Core/workspace/soap_site/promo/video/storyboard.json` — schema of
`Teams/Marketing/video/test_storyboards/wwe_test.json` (slug `soap`, 5 scenes + cta `thesoapbook.com`), same copy as
scenes 1-5 above. Because `make_promo_video.py` burns headline/sub onto the lower frame, the storyboard points at
**text-free** background cards `assets/scenes/video_bg{1..5}_*.png` (1920x1080, motif centred in the 9:16-safe column),
drawn by `assets/scenes/_make_video_bg.py`; the renderer draws its own end-card. The `scene*_*.png` cards above
(headline already drawn) stay as stills for social posts.
Dry-run (2026-10-17): `python D:/Hermes_Core/Teams/Marketing/video/make_promo_video.py --storyboard
D:/Hermes_Core/workspace/soap_site/promo/video/storyboard.json --out D:/Hermes_Core/workspace/soap_site/promo/video --dry-run`
-> `VALIDATION OK ... slug=soap scenes=5 voice=en-US-AvaNeural aspects=['9x16', '16x9']` / `DRY RUN: nothing rendered.` exit 0.
Not rendered yet — run the same command without `--dry-run` to produce the mp4s — the renderer writes `{slug}_{aspect}.mp4` straight into `--out`, i.e. `video/soap_16x9.mp4` (the path the page embeds) plus `soap_9x16.mp4`; note it ALSO writes `soap_16x9.jpg`, replacing the typographic poster with a frame grab (back up the poster first if you prefer it).
