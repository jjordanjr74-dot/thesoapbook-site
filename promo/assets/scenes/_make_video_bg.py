"""Text-free 1920x1080 typographic background cards for make_promo_video.py.

The renderer burns headline/sub over the bottom ~45% of each frame, so these cards carry
NO headline: only the wordmark + a centred motif in the upper half (centre 600px column is
also the 9:16 centre-crop safe zone). Palette = site: ink #111827, honey #f2603a, paper #f8f5ef.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent
W, H = 1920, 1080
INK, HONEY, PAPER, RULE, SOFT = (17, 24, 39), (242, 96, 58), (248, 245, 239), (226, 219, 204), (55, 65, 81)
F_BOLD = "C:/Windows/Fonts/segoeuib.ttf"
F_REG = "C:/Windows/Fonts/segoeui.ttf"
CX = W // 2


def base():
    im = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 10], fill=HONEY)
    # faint ruled-paper texture across the frame
    for y in range(90, H, 54):
        d.line([(0, y), (W, y)], fill=(24, 32, 49), width=2)
    d.text((CX, 64), "SOAP AUTOPILOT", font=ImageFont.truetype(F_BOLD, 30), fill=HONEY, anchor="mm")
    return im, d


def note_card(d, x0, y0, w, h, letters=True, lines=3):
    d.rounded_rectangle([x0, y0, x0 + w, y0 + h], radius=22, fill=PAPER)
    d.line([(x0 + 70, y0 + 14), (x0 + 70, y0 + h - 14)], fill=HONEY, width=5)
    f = ImageFont.truetype(F_BOLD, 30)
    band = (h - 40) / 4
    for i, ch in enumerate("SOAP"):
        y = y0 + 20 + band * i + band / 2
        if letters:
            d.text((x0 + 36, y), ch, font=f, fill=INK, anchor="mm")
        for j in range(lines):
            yy = y - 22 + j * 22
            d.line([(x0 + 100, yy), (x0 + w - (110 if j == lines - 1 else 30), yy)], fill=RULE, width=4)


def s1():  # notes waiting: stack of blank cards
    im, d = base()
    for off, shade in ((40, (205, 199, 186)), (20, (228, 223, 212))):
        d.rounded_rectangle([CX - 230 + off, 130 + off, CX + 230 + off, 530 + off], radius=22, fill=shade)
    note_card(d, CX - 230, 130, 460, 400, letters=True, lines=1)
    im.save(OUT / "video_bg1_notes_waiting.png")


def s2():  # dictate: waveform feeding a filled card
    im, d = base()
    note_card(d, CX - 40, 130, 380, 410)
    import math
    for i in range(16):
        hgt = 30 + 130 * abs(math.sin(i * 0.8))
        x = CX - 330 + i * 18
        d.rounded_rectangle([x, 335 - hgt / 2, x + 9, 335 + hgt / 2], radius=4, fill=HONEY)
    im.save(OUT / "video_bg2_dictate.png")


def s3():  # local audio: laptop outline with mic, no cloud
    im, d = base()
    d.rounded_rectangle([CX - 290, 150, CX + 290, 500], radius=20, outline=PAPER, width=8)
    d.rounded_rectangle([CX - 340, 500, CX + 340, 530], radius=12, fill=PAPER)
    d.rounded_rectangle([CX - 40, 230, CX + 40, 360], radius=40, fill=HONEY)
    d.arc([CX - 80, 280, CX + 80, 420], 0, 180, fill=HONEY, width=10)
    d.line([(CX, 420), (CX, 455)], fill=HONEY, width=10)
    d.line([(CX - 45, 455), (CX + 45, 455)], fill=HONEY, width=10)
    im.save(OUT / "video_bg3_local_audio.png")


def s4():  # sign + lock: card with padlock seal
    im, d = base()
    note_card(d, CX - 240, 130, 400, 410)
    lx, ly = CX + 170, 360
    d.ellipse([lx - 110, ly - 110, lx + 110, ly + 110], fill=HONEY)
    d.arc([lx - 42, ly - 82, lx + 42, ly + 2], 180, 360, fill=INK, width=16)
    d.line([(lx - 42, ly - 40), (lx - 42, ly - 10)], fill=INK, width=16)
    d.line([(lx + 42, ly - 40), (lx + 42, ly - 10)], fill=INK, width=16)
    d.rounded_rectangle([lx - 62, ly - 14, lx + 62, ly + 72], radius=12, fill=INK)
    d.ellipse([lx - 12, ly + 12, lx + 12, ly + 36], fill=HONEY)
    im.save(OUT / "video_bg4_sign_lock.png")


def s5():  # self-serve cancel + waitlist: calendar grid
    im, d = base()
    x0, y0, w, h = CX - 300, 140, 600, 400
    d.rounded_rectangle([x0, y0, x0 + w, y0 + h], radius=22, fill=PAPER)
    d.rounded_rectangle([x0, y0, x0 + w, y0 + 70], radius=22, fill=HONEY)
    d.rectangle([x0, y0 + 48, x0 + w, y0 + 70], fill=HONEY)
    cw, ch = (w - 40) / 7, (h - 110) / 4
    for r in range(4):
        for c in range(7):
            cx0, cy0 = x0 + 20 + c * cw, y0 + 90 + r * ch
            box = [cx0 + 6, cy0 + 6, cx0 + cw - 6, cy0 + ch - 6]
            if (r, c) == (1, 3):
                d.rounded_rectangle(box, radius=8, fill=INK)
                d.line([(box[0] + 18, box[1] + 18), (box[2] - 18, box[3] - 18)], fill=HONEY, width=6)
                d.line([(box[0] + 18, box[3] - 18), (box[2] - 18, box[1] + 18)], fill=HONEY, width=6)
            elif (r, c) in ((2, 1), (2, 4), (3, 5)):
                d.rounded_rectangle(box, radius=8, fill=RULE)
            else:
                d.rounded_rectangle(box, radius=8, outline=RULE, width=3)
    im.save(OUT / "video_bg5_cancel_waitlist.png")


if __name__ == "__main__":
    for fn in (s1, s2, s3, s4, s5):
        fn()
    for p in sorted(OUT.glob("video_bg*.png")):
        with Image.open(p) as im:
            assert im.size == (W, H), (p, im.size)
        print(p.as_posix(), p.stat().st_size)
