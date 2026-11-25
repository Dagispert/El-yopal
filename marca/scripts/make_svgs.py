"""Genera los SVG de marca de El Yopal (texto convertido a trazos)."""
import math, os, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

FONTS, OUT = sys.argv[1], sys.argv[2]
C = dict(granate="#8C1D2F", deep="#4A0E18", crema="#FFF4E2", sol="#FFC83D",
         cielo="#BCD4F6", galleta="#D99148", blanco="#FFFFFF", rosa="#F28B82")

def load(name):
    f = TTFont(os.path.join(FONTS, name))
    return f, f.getGlyphSet(), f.getBestCmap()

BAGEL = load("BagelFatOne-Regular.ttf")
BARLOW = load("BarlowCondensed-Bold.ttf")

def text_path(font, text, size, x=0, y=0, tracking=0):
    """Devuelve (d, ancho, glyph_boxes) para texto en baseline y."""
    f, gs, cmap = font
    upm = f["head"].unitsPerEm
    s = size / upm
    pen = SVGPathPen(gs)
    cx = 0
    boxes = []
    hmtx = f["hmtx"]
    kern = {}
    for i, ch in enumerate(text):
        g = cmap.get(ord(ch))
        if g is None:
            cx += size * 0.3
            continue
        tp = TransformPen(pen, (s, 0, 0, -s, x + cx, y))
        gs[g].draw(tp)
        bp = BoundsPen(gs)
        gs[g].draw(bp)
        b = bp.bounds
        if b:
            boxes.append((ch, x + cx + b[0] * s, y - b[3] * s, x + cx + b[2] * s, y - b[1] * s))
        cx += hmtx[g][0] * s + tracking
    return pen.getCommands(), cx - tracking, boxes

def rays(cx, cy, r_in, r_out, a0, a1, n, width, color):
    out = []
    for i in range(n):
        a = math.radians(a0 + (a1 - a0) * i / (n - 1))
        x1, y1 = cx + r_in * math.cos(a), cy - r_in * math.sin(a)
        x2, y2 = cx + r_out * math.cos(a), cy - r_out * math.sin(a)
        out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"/>')
    return "\n  ".join(out)

def wordmark(color, ray_color):
    """Logotipo: 'El Yopal' con el sol saliendo sobre la última l."""
    d, w, boxes = text_path(BAGEL, "El Yopal", 200, 0, 0, tracking=-4)
    l = boxes[-1]  # la última 'l'
    cx = (l[1] + l[3]) / 2
    top = l[2]
    r = rays(cx, top - 6, 26, 64, 20, 160, 5, 15, ray_color)
    minx = min(b[1] for b in boxes); maxx = max(max(b[3] for b in boxes), cx + 64 * math.cos(math.radians(20)) + 8)
    miny = top - 6 - 64 - 10; maxy = max(b[4] for b in boxes)
    pad = 12
    vb = (minx - pad, miny - pad, maxx - minx + 2 * pad, maxy - miny + 2 * pad)
    return d, r, vb, (minx, miny, maxx, maxy)

def svg(vb, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb[0]:.1f} {vb[1]:.1f} {vb[2]:.1f} {vb[3]:.1f}" '
            f'width="{vb[2]:.0f}" height="{vb[3]:.0f}" role="img" aria-label="{title}">\n  <title>{title}</title>\n  {body}\n</svg>\n')

def write(group, name, content):
    p = os.path.join(OUT, group)
    os.makedirs(p, exist_ok=True)
    with open(os.path.join(p, name), "w") as fh:
        fh.write(content)

# 1. Logotipo en sus tres tintas
for name, ink, ray in [("logotipo-granate.svg", C["granate"], C["sol"]),
                       ("logotipo-crema.svg", C["crema"], C["sol"]),
                       ("logotipo-tinta.svg", C["deep"], C["deep"])]:
    d, r, vb, _ = wordmark(ink, ray)
    write("Logos", name, svg(vb, f'{r}\n  <path d="{d}" fill="{ink}"/>', "El Yopal"))

# 2. Bloque de marca: logotipo + URBAN EXPRESS (lo que se lee en el toldo)
for name, ink, ray, sub in [("bloque-granate.svg", C["granate"], C["sol"], C["deep"]),
                            ("bloque-crema.svg", C["crema"], C["sol"], C["sol"])]:
    d, r, vb, (minx, miny, maxx, maxy) = wordmark(ink, ray)
    sd, sw, sb = text_path(BARLOW, "URBAN EXPRESS · CAFÉ & GALLETAS", 44, 0, 0, tracking=4)
    scale = (maxx - minx) / sw
    sy = maxy + 70
    body = (f'{r}\n  <path d="{d}" fill="{ink}"/>\n'
            f'  <g transform="translate({minx:.1f} {sy:.1f}) scale({scale:.4f})"><path d="{sd}" fill="{sub}"/></g>')
    vb2 = (vb[0], vb[1], vb[2], (sy + 12) - vb[1])
    write("Logos", name, svg(vb2, body, "El Yopal · Urban Express"))

# 3. El Solete (mascota)
def solete_group(cx, cy, R, mood="feliz", sticker=True):
    n = 12
    parts = []
    def sun(fill, stroke=None, sw=0):
        s = f' stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"' if stroke else ""
        rr = []
        for i in range(n):
            a = 2 * math.pi * i / n
            x1, y1 = cx + R * 0.95 * math.cos(a), cy + R * 0.95 * math.sin(a)
            x2, y2 = cx + R * 1.42 * math.cos(a), cy + R * 1.42 * math.sin(a)
            rr.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke or fill}" stroke-width="{R*0.26 + sw:.1f}" stroke-linecap="round"/>')
        return "\n  ".join(rr) + f'\n  <circle cx="{cx}" cy="{cy}" r="{R + sw/2:.1f}" fill="{stroke or fill}"/>'
    if sticker:
        parts.append(f'<g transform="translate({R*0.06:.1f} {R*0.08:.1f})">' + sun(C["deep"], C["deep"], R * 0.16) + '</g>')
        parts.append(sun(C["blanco"], C["blanco"], R * 0.16))
    parts.append(sun(C["sol"]))
    ex, ey, er = R * 0.32, R * 0.12, R * 0.11
    ink = C["deep"]
    if mood == "guino":
        parts.append(f'<ellipse cx="{cx-ex:.1f}" cy="{cy-ey:.1f}" rx="{er*0.85:.1f}" ry="{er*1.25:.1f}" fill="{ink}"/>')
        parts.append(f'<path d="M{cx+ex-er*1.2:.1f} {cy-ey:.1f} q{er*1.2:.1f} {-er*1.3:.1f} {er*2.4:.1f} 0" fill="none" stroke="{ink}" stroke-width="{R*0.08:.1f}" stroke-linecap="round"/>')
    else:
        for sx in (-1, 1):
            parts.append(f'<ellipse cx="{cx+sx*ex:.1f}" cy="{cy-ey:.1f}" rx="{er*0.85:.1f}" ry="{er*1.25:.1f}" fill="{ink}"/>')
    # mejillas
    for sx in (-1, 1):
        parts.append(f'<ellipse cx="{cx+sx*R*0.55:.1f}" cy="{cy+R*0.18:.1f}" rx="{R*0.13:.1f}" ry="{R*0.08:.1f}" fill="{C["rosa"]}" opacity=".9"/>')
    # boca
    if mood == "sorpresa":
        parts.append(f'<ellipse cx="{cx}" cy="{cy+R*0.3:.1f}" rx="{R*0.12:.1f}" ry="{R*0.15:.1f}" fill="{ink}"/>')
    else:
        mw = R * 0.42
        parts.append(f'<path d="M{cx-mw/2:.1f} {cy+R*0.2:.1f} q{mw/2:.1f} {R*0.32:.1f} {mw:.1f} 0" fill="none" stroke="{ink}" stroke-width="{R*0.08:.1f}" stroke-linecap="round"/>')
    return "\n  ".join(parts)

for mood in ["feliz", "guino", "sorpresa"]:
    R = 100
    size = R * 1.42 * 2 + R * 0.5
    c = size / 2
    write("Mascota", f"solete-{mood}.svg", svg((0, 0, size, size), solete_group(c, c - 4, R, mood), f"El Solete ({mood})"))

# 4. Avatar de perfil (círculo granate + Solete)
S = 1080
body = f'<rect width="{S}" height="{S}" fill="{C["granate"]}"/>\n  ' + solete_group(S/2, S/2 - 10, 250, "feliz")
write("Logos", "avatar-perfil.svg", svg((0, 0, S, S), body, "El Yopal · avatar"))

# 5. Iconos de producto: trazo granate 2px a 24px, puntas redondas
ICONS = {
 "cafe": '<path d="M5 9h11v5a5 5 0 0 1-5 5h-1a5 5 0 0 1-5-5z"/><path d="M16 10h1.5a2.5 2.5 0 0 1 0 5H16"/><path d="M8 3c-.8 1 .8 2 0 3M11.5 3c-.8 1 .8 2 0 3"/>',
 "galleta": '<circle cx="12" cy="12" r="8.5"/><circle cx="9" cy="9.5" r="1" fill="currentColor"/><circle cx="14.5" cy="8.5" r="1" fill="currentColor"/><circle cx="15" cy="14" r="1" fill="currentColor"/><circle cx="9.5" cy="15" r="1" fill="currentColor"/>',
 "para-llevar": '<path d="M6 7h12l-1.3 13H7.3z"/><path d="M5 7h14V5.5A1.5 1.5 0 0 0 17.5 4h-11A1.5 1.5 0 0 0 5 5.5z"/><path d="M8 12h8"/>',
 "bebida": '<rect x="7" y="5" width="10" height="15" rx="2.5"/><path d="M9 3h6"/><path d="M7 10h10"/>',
 "snack": '<path d="M6 4c2 1 10 1 12 0l-1 16c-2-1-8-1-10 0z"/><path d="M9.5 10.5l1.5 1.5 3-3"/>',
 "revista": '<rect x="5" y="3.5" width="14" height="17" rx="1.5"/><path d="M8 7.5h8M8 11h5"/><circle cx="14" cy="15.5" r="2"/>',
 "sol": '<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/>',
 "ubicacion": '<path d="M12 21s-6.5-6-6.5-11a6.5 6.5 0 0 1 13 0c0 5-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.3"/>',
}
for name, d in ICONS.items():
    body = f'<g fill="none" stroke="{C["granate"]}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" color="{C["granate"]}">{d}</g>'
    write("Iconos", f"{name}.svg", f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" role="img" aria-label="{name}"><title>{name}</title>{body}</svg>\n')
print("ok")
