#!/usr/bin/env python3
"""Render entry.png: a one-page newspaper front page summing up world news
of Friday 20 November 2026. Pure Pillow, deterministic output.

Stories verified 21 Nov 2026 from Reuters, BBC, AP, NYT, WSJ, Axios and the
Just Security / OneTurn day briefs for 20 Nov 2026:
 1. Shenzhen: Trump, Xi and Putin hold first three-way summit, sign a joint
    declaration ("a nuclear war cannot be won and must never be fought").
 2. Kyiv: Russian overnight strikes kill 8, hit bridges; 28 hurt in nine
    regions; 2 more killed in Lviv.
 3. The Hague: a day after the ICJ found Myanmar guilty of genocide against
    the Rohingya (9-6), Myanmar calls the ruling "unfair"; UK expels
    Myanmar's defence attache.
 4. Riyadh: Houthi missile damages the 80-storey PIF Tower (several floors,
    no injuries).
 5. Markets: S&P 500 -2% (fifth straight loss); Nikkei -4.8% after
    Anthropic's Nasdaq debut.
 6. COP31 (Antalya): draft deal drops any call to phase out fossil fuels.
Ticker: Estonia to shut its Russia border from 1 Dec; Russian missiles land
in Poland; Kenya discharges its last Ebola patient; UK-EU youth travel deal;
US Senate blocks Iran war-powers measure 51-48.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

PAPER = (253, 252, 248)
INK = (20, 20, 20)
GREY = (92, 92, 92)
NAVY = (16, 36, 62)
NAVY2 = (27, 58, 92)
RED = (179, 39, 30)
GOLD = (201, 162, 39)
TEAL = (15, 118, 110)
AMBER = (180, 83, 9)
BORDER = (216, 210, 196)
CARD = (255, 255, 255)
GREEN_BG = (238, 245, 238)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def kicker(draw, x, y, text, color):
    f = font(SANS_B, 20)
    draw.text((x, y), text, font=f, fill=color)
    return draw.textlength(text, font=f)


# ---------------------------------------------------------------- canvas
img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
MX = 28  # side margin

# ---------------------------------------------------------------- masthead
d.rectangle([0, 0, W, 150], fill=NAVY)
d.rectangle([0, 150, W, 156], fill=RED)
d.text((MX, 22), "WORLD NEWS", font=font(SERIF_B, 88), fill=(255, 255, 255))
d.text((MX, 118), "THE DAY IN BRIEF", font=font(SANS_B, 20), fill=GOLD)
for _txt, _y, _f, _c in [
    ("FRIDAY", 30, font(SANS_B, 34), GOLD),
    ("20 NOVEMBER 2026", 72, font(SANS_B, 34), (255, 255, 255)),
    ("SIX STORIES  •  FIVE REGIONS", 116, font(SANS, 19), (190, 200, 215)),
]:
    _w = d.textlength(_txt, font=_f)
    d.text((W - MX - _w, _y), _txt, font=_f, fill=_c)

# ---------------------------------------------------------------- hero: Shenzhen
HY = 176
kicker(d, MX, HY, "SHENZHEN, CHINA  —  DIPLOMACY", RED)
hero_head = ["Trump, Xi and Putin", "sign joint peace", "declaration"]
y = HY + 30
y = draw_lines(d, hero_head, MX, y, font(SERIF_B, 48), INK, 50)
hero_body = (
    "At their first three-way summit, the leaders of the U.S., China and "
    "Russia declared that \u201ca nuclear war cannot be won and must "
    "never be fought.\u201d"
)
y += 6
y = draw_lines(
    d, wrap(d, hero_body, font(SANS, 25), 600), MX, y, font(SANS, 25), (40, 40, 40), 30
)
d.text((MX, y + 4), "Sources: New York Times  •  Reuters", font=font(SANS, 18), fill=GREY)

# hero globe panel (schematic, decorative)
GX, GY, GW, GH = 668, 176, 328, 292
d.rounded_rectangle([GX, GY, GX + GW, GY + GH], radius=10, fill=NAVY2)
d.text((GX + 18, GY + 14), "THE DAY, AROUND", font=font(SANS_B, 19), fill=(255, 255, 255))
d.text((GX + 18, GY + 38), "THE WORLD", font=font(SANS_B, 19), fill=(255, 255, 255))
cx, cy, r = GX + 164, GY + 178, 82
d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(150, 180, 210), width=3)
for rx in (30, 58):
    d.ellipse([cx - rx, cy - r, cx + rx, cy + r], outline=(110, 145, 180), width=2)
d.line([cx - r, cy, cx + r, cy], fill=(110, 145, 180), width=2)
d.ellipse([cx - r, cy - 30, cx + r, cy + 30], outline=(110, 145, 180), width=2)
dots = [
    (cx + 52, cy - 8, "SHENZHEN"),
    (cx - 18, cy - 38, "KYIV"),
    (cx - 34, cy + 18, "RIYADH"),
    (cx - 52, cy - 52, "THE HAGUE"),
]
for x, y, label in dots:
    d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=RED, outline=(255, 255, 255), width=2)
d.text((GX + 18, GY + GH - 26), "DOTS MARK THE STORIES BELOW",
       font=font(SANS, 15), fill=(170, 185, 205))

d.line([MX, 484, W - MX, 484], fill=BORDER, width=2)

# ---------------------------------------------------------------- story cards
def burst(draw, cx, cy, r, color):
    for ang in range(0, 360, 30):
        import math
        x2 = cx + r * math.cos(math.radians(ang))
        y2 = cy + r * math.sin(math.radians(ang))
        draw.line([cx, cy, x2, y2], fill=color, width=4)
    draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=color)


def scales(draw, cx, cy, r, color):
    draw.line([cx, cy - 18, cx, cy + 18], fill=color, width=4)
    draw.line([cx - 20, cy - 14, cx + 20, cy - 14], fill=color, width=4)
    draw.line([cx - 20, cy - 14, cx - 26, cy + 2], fill=color, width=3)
    draw.line([cx - 20, cy - 14, cx - 14, cy + 2], fill=color, width=3)
    draw.line([cx + 20, cy - 14, cx + 26, cy + 2], fill=color, width=3)
    draw.line([cx + 20, cy - 14, cx + 14, cy + 2], fill=color, width=3)
    draw.arc([cx - 32, cy - 4, cx - 8, cy + 14], 0, 180, fill=color, width=3)
    draw.arc([cx + 8, cy - 4, cx + 32, cy + 14], 0, 180, fill=color, width=3)
    draw.line([cx - 12, cy + 20, cx + 12, cy + 20], fill=color, width=4)


def tower(draw, cx, cy, r, color):
    draw.rectangle([cx - 13, cy - 20, cx + 13, cy + 20], outline=color, width=4)
    for wy in (-12, -2, 8):
        draw.line([cx - 8, cy + wy, cx + 8, cy + wy], fill=color, width=3)
    draw.line([cx - 13, cy - 20, cx - 22, cy - 30], fill=color, width=3)
    draw.line([cx + 2, cy - 30, cx + 13, cy - 20], fill=color, width=3)


def chart_down(draw, cx, cy, r, color):
    pts = [(cx - 24, cy - 14), (cx - 8, cy - 2), (cx + 4, cy - 8), (cx + 22, cy + 14)]
    draw.line(pts, fill=color, width=4, joint="curve")
    draw.line([cx + 22, cy + 14, cx + 22, cy + 2], fill=color, width=4)
    draw.line([cx + 22, cy + 14, cx + 10, cy + 14], fill=color, width=4)


CARDS = [
    dict(kick="KYIV, UKRAINE  —  WAR", color=RED, icon=burst,
         head="Russian strikes kill 8 in Kyiv",
         body="Overnight missiles hit bridges; 28 hurt across nine regions. "
              "Two killed in Lviv.",
         src="Source: BBC"),
    dict(kick="THE HAGUE  —  JUSTICE", color=NAVY2, icon=scales,
         head="Myanmar rejects genocide ruling",
         body="Found guilty of genocide against the Rohingya; Myanmar calls "
              "the verdict \u201cunfair.\u201d",
         src="Sources: BBC  •  AP"),
    dict(kick="RIYADH  —  MIDDLE EAST", color=AMBER, icon=tower,
         head="Houthi missile hits Saudi wealth-fund tower",
         body="The 80-storey PIF Tower is damaged on several floors. "
              "No injuries reported.",
         src="Sources: Wall Street Journal  •  Reuters"),
    dict(kick="MARKETS  —  ECONOMY", color=TEAL, icon=chart_down,
         head="Stocks slide as AI doubts grow",
         body="S&P 500 falls 2%, a fifth straight loss; Nikkei drops 4.8% "
              "after Anthropic\u2019s debut.",
         src="Market reports, 20 Nov"),
]

CW, CH, GAP = 478, 180, 12
GY0 = 500
for i, c in enumerate(CARDS):
    x = MX + (i % 2) * (CW + GAP)
    y = GY0 + (i // 2) * (CH + GAP)
    d.rounded_rectangle([x, y, x + CW, y + CH], radius=8, fill=CARD,
                        outline=BORDER, width=1)
    d.rectangle([x, y + 8, x + 6, y + CH - 8], fill=c["color"])
    tx = x + 20
    kicker(d, tx, y + 12, c["kick"], c["color"])
    # icon disc, top right
    icx, icy = x + CW - 34, y + 34
    d.ellipse([icx - 26, icy - 26, icx + 26, icy + 26],
              outline=c["color"], width=3)
    c["icon"](d, icx, icy, 16, c["color"])
    hy = y + 40
    hy = draw_lines(d, wrap(d, c["head"], font(SERIF_B, 29), CW - 100),
                    tx, hy, font(SERIF_B, 29), INK, 32)
    by = draw_lines(d, wrap(d, c["body"], font(SANS, 20), CW - 40),
                    tx, hy + 6, font(SANS, 20), (40, 40, 40), 25)
    d.text((tx, y + CH - 24), c["src"], font=font(SANS, 16), fill=GREY)

# ---------------------------------------------------------------- climate band
CY = 884
d.rounded_rectangle([MX, CY, W - MX, CY + 62], radius=8, fill=GREEN_BG,
                    outline=BORDER, width=1)
d.text((MX + 18, CY + 8), "CLIMATE  —  COP31, ANTALYA",
       font=font(SANS_B, 19), fill=TEAL)
d.text((MX + 18, CY + 33),
       "Draft deal drops any call to phase out fossil fuels.",
       font=font(SERIF_B, 24), fill=INK)

# ---------------------------------------------------------------- ticker
TY = 954
d.text((MX, TY), "ALSO TODAY", font=font(SANS_B, 20), fill=RED)
tick = ("Estonia to shut Russia border from 1 Dec  •  Russian missiles land "
        "in Poland  •  Kenya Ebola-free  •  UK\u2013EU youth travel deal  •  "
        "Senate blocks Iran war powers 51\u201348")
_ty = TY
for _line in wrap(d, tick, font(SANS, 19), W - MX - 152):
    _line = _line.rstrip()
    if _line.endswith("\u2022"):
        _line = _line[:-1].rstrip()
    d.text((MX + 152, _ty), _line, font=font(SANS, 19), fill=(40, 40, 40))
    _ty += 24

# ---------------------------------------------------------------- footer
d.line([MX, 1000, W - MX, 1000], fill=BORDER, width=1)
d.text((MX, 1006),
       "Sources: Reuters  •  BBC  •  AP  •  New York Times  •  Wall Street Journal  •  Axios",
       font=font(SANS, 16), fill=GREY)

img.save(OUT, optimize=True)
print("wrote", OUT, os.path.getsize(OUT), "bytes,", img.size)
