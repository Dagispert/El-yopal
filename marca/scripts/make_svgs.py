"""Genera los SVG de marca de El Yopal.

- Logotipo: el logotipo ORIGINAL vectorizado (logo-original/path.txt), solo cambia la tinta.
- Solete: mascota de trazo, con la misma lógica que el sol del logotipo
  (trazo uniforme de puntas redondas, rayos separados del círculo).
"""
import math, os, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FONTS, LOGO, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
C = dict(granate="#8C1D2F", deep="#4A0E18", crema="#FFF4E2", sol="#FFC83D", blanco="#FFFFFF")

head, LOGO_D = open(LOGO).read().split("\n", 1)
LW, LH = map(float, head.split())

def write(group, name, content):
    p = os.path.join(OUT, group); os.makedirs(p, exist_ok=True)
    open(os.path.join(p, name), "w").write(content)

def svg(w, h, body, title, vb=None):
    vb = vb or f"0 0 {w:.0f} {h:.0f}"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{w:.0f}" height="{h:.0f}" role="img" aria-label="{title}">\n'
            f'  <title>{title}</title>\n  {body}\n</svg>\n')

def logo(ink, x=0, y=0, s=1.0):
    return f'<path transform="translate({x:.1f} {y:.1f}) scale({s:.4f})" fill-rule="evenodd" fill="{ink}" d="{LOGO_D}"/>'

# 1. Logotipo original en tres tintas (mismo dibujo, solo cambia el color)
for name, ink in [("logotipo-granate.svg", C["granate"]), ("logotipo-crema.svg", C["crema"]), ("logotipo-tinta.svg", C["deep"])]:
    write("Logos", name, svg(LW / 3, LH / 3, logo(ink), "El Yopal", vb=f"0 0 {LW:.0f} {LH:.0f}"))

# 2. Bloque: logotipo + rótulo del toldo debajo
f = TTFont(os.path.join(FONTS, "BarlowCondensed-Bold.ttf")); gs = f.getGlyphSet(); cmap = f.getBestCmap()
def text_d(text, size, tracking):
    s = size / f["head"].unitsPerEm; pen = SVGPathPen(gs); cx = 0
    for ch in text:
        g = cmap[ord(ch)]
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, cx, 0)))
        cx += f["hmtx"][g][0] * s + tracking
    return pen.getCommands(), cx - tracking
for name, ink, sub in [("bloque-granate.svg", C["granate"], C["deep"]), ("bloque-crema.svg", C["crema"], C["sol"])]:
    td, tw = text_d("URBAN EXPRESS · CAFÉ & GALLETAS", 100, 10)
    tw_target = LW * 0.62
    sc = tw_target / tw
    ty = LH + 150 * sc + 40
    body = logo(ink) + f'\n  <g transform="translate({(LW - tw_target) / 2:.1f} {ty:.1f}) scale({sc:.4f})"><path d="{td}" fill="{sub}"/></g>'
    H = ty + 40
    write("Logos", name, svg(LW / 3, H / 3, body, "El Yopal · Urban Express", vb=f"0 0 {LW:.0f} {H:.0f}"))

# 3. Avatar: logotipo crema sobre granate
S = 1080; s = (S * 0.84) / LW
write("Logos", "avatar-perfil.svg", svg(S, S, f'<rect width="{S}" height="{S}" fill="{C["granate"]}"/>\n  ' +
      logo(C["crema"], (S - LW * s) / 2, (S - LH * s) / 2 + 10, s), "El Yopal · avatar"))

# 4. El Solete
# Proporciones medidas en el sol del logotipo: trazo ≈ 0,26 del radio del arco,
# hueco entre arco y rayos ≈ 0,22 del radio, rayos de longitud ligeramente desigual.
R, T = 100, 26
RAYS = [(-92, 60), (-122, 50), (-155, 56), (172, 46), (140, 54), (106, 48), (72, 54), (38, 46), (4, 56), (-30, 50)]
def ray(cx, cy, ang, ln, start=R + T / 2 + 24):
    a = math.radians(ang)
    x1, y1 = cx + start * math.cos(a), cy + start * math.sin(a)
    x2, y2 = cx + (start + ln) * math.cos(a), cy + (start + ln) * math.sin(a)
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>'

def cara(cx, cy, mood, k=1.0):
    ex, ey, el = 36 * k, 18 * k, 13 * k
    eyes = []
    for sx in (-1, 1):
        if mood == "guino" and sx == 1:
            eyes.append(f'<path d="M{cx+ex-14*k:.1f} {cy-ey+4*k:.1f} q14 -16 28 0" transform="scale(1)"/>')
        else:
            eyes.append(f'<line x1="{cx+sx*ex:.1f}" y1="{cy-ey-el/2:.1f}" x2="{cx+sx*ex:.1f}" y2="{cy-ey+el/2:.1f}"/>')
    if mood == "sorpresa":
        boca = f'<circle cx="{cx:.1f}" cy="{cy+30*k:.1f}" r="{11*k:.1f}"/>'
    else:
        boca = f'<path d="M{cx-30*k:.1f} {cy+20*k:.1f} q{30*k:.1f} {30*k:.1f} {60*k:.1f} 0"/>'
    return "".join(eyes) + boca

def arco(cx, cy, a0=-48, a1=262):
    # círculo abierto, como el trazo de pincel del sol del logotipo
    p = lambda a: (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
    (x0, y0), (x1, y1) = p(a0), p(a1)
    return f'<path d="M{x0:.1f} {y0:.1f} A{R} {R} 0 1 1 {x1:.1f} {y1:.1f}"/>'

def solete(mood, fill, ink, size, face=None):
    c = size / 2
    rays = "".join(ray(c, c, a, l) for a, l in RAYS)
    disco = f'<circle cx="{c}" cy="{c}" r="{R}" fill="{fill}"/>' if fill else ""
    return (f'{disco}<g fill="none" stroke="{ink}" stroke-width="{T}" stroke-linecap="round" stroke-linejoin="round">'
            f'{arco(c, c)}{rays}</g>'
            f'<g fill="none" stroke="{face or ink}" stroke-width="{T*0.62:.1f}" stroke-linecap="round" stroke-linejoin="round">{cara(c, c, mood)}</g>')

SIZE = 2 * (R + T / 2 + 24 + 58 + T / 2) + 8
for mood in ["feliz", "guino", "sorpresa"]:
    write("Mascota", f"solete-{mood}.svg", svg(SIZE, SIZE, solete(mood, C["sol"], C["deep"], SIZE), f"El Solete ({mood})"))
write("Mascota", "solete-linea.svg", svg(SIZE, SIZE, solete("feliz", None, C["granate"], SIZE), "El Solete (una tinta)"))
write("Mascota", "solete-crema.svg", svg(SIZE, SIZE, solete("feliz", C["sol"], C["crema"], SIZE, C["deep"]), "El Solete (sobre granate)"))

# Solete asomando: medio sol saliendo, como en el logotipo, para pegar en el borde inferior
W2 = SIZE; H2 = SIZE / 2 + 6; c = W2 / 2; cy = H2 + 4
rays = "".join(ray(c, cy, a, l) for a, l in [(-162, 48), (-126, 56), (-90, 60), (-54, 56), (-18, 48)])
body = (f'<path d="M{c-R} {cy} A{R} {R} 0 0 1 {c+R} {cy} Z" fill="{C["sol"]}"/>'
        f'<g fill="none" stroke="{C["deep"]}" stroke-width="{T}" stroke-linecap="round">'
        f'<path d="M{c-R} {cy+T} L{c-R} {cy} A{R} {R} 0 0 1 {c+R} {cy} L{c+R} {cy+T}"/>{rays}</g>'
        f'<g fill="none" stroke="{C["deep"]}" stroke-width="{T*0.62:.1f}" stroke-linecap="round">{cara(c, cy - 40, "feliz", 0.85)}</g>')
write("Mascota", "solete-asomando.svg", svg(W2, H2, body, "El Solete asomando"))

# 5. Iconos (sin cambios)
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
