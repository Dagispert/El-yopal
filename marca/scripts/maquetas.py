"""Maquetas vectoriales de El Yopal (vaso, bolsa, camiseta, pegatinas, patrón, tarjeta)."""
import os, re, sys
S = sys.argv[1]
A = S + "/ds/project/assets"; I = S + "/ilustra"; O = S + "/maquetas"
os.makedirs(O, exist_ok=True)
G, H, C, SOL, ALT, AZUL = "#8C1D2F", "#4A0E18", "#FFF4E2", "#FFC83D", "#FBE6C6", "#6F8FCF"
FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Sansita:wght@900&family=Figtree:wght@500;700;800&display=swap">'

def f(p): return "file://" + p
def ilu(n, modo): return f(f"{I}/{n}-{modo}.svg")
LOGO = {k: f(f"{A}/Logos/logotipo-{k}.svg") for k in ("granate", "crema", "tinta")}

def page(name, w, h, bg, body, extra_css=""):
    html = f'''<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>
    *{{box-sizing:border-box}} body{{margin:0}} .c{{position:relative;width:{w}px;height:{h}px;background:{bg};overflow:hidden}}
    .r{{font-family:Figtree,sans-serif;font-weight:800;letter-spacing:.12em;text-transform:uppercase}}
    .fr{{font-family:Sansita,sans-serif;font-weight:900}}
    {extra_css}</style></head><body><div class="c">{body}</div></body></html>'''
    open(f"{O}/{name}.html", "w").write(html)

# 1. Vasos para llevar
def vaso(x, y, cuerpo, tapa, logo, sombra=0.0):
    return f'''<svg style="position:absolute;left:{x}px;top:{y}px" width="440" height="760" viewBox="0 0 440 760">
<defs><linearGradient id="g{x}" x1="0" x2="1"><stop offset="0" stop-color="#000" stop-opacity=".22"/><stop offset=".22" stop-color="#000" stop-opacity="0"/>
<stop offset=".62" stop-color="#fff" stop-opacity=".10"/><stop offset=".85" stop-color="#000" stop-opacity=".05"/><stop offset="1" stop-color="#000" stop-opacity=".28"/></linearGradient>
<filter id="b{x}"><feGaussianBlur stdDeviation="14"/></filter></defs>
<ellipse cx="220" cy="735" rx="170" ry="18" fill="#000" opacity=".28" filter="url(#b{x})"/>
<path d="M40 150 L400 150 L360 728 Q220 742 80 728 Z" fill="{cuerpo}"/>
<path d="M40 150 L400 150 L360 728 Q220 742 80 728 Z" fill="url(#g{x})"/>
<path d="M22 112 Q220 98 418 112 L410 152 Q220 164 30 152 Z" fill="{tapa}"/>
<path d="M60 112 Q90 40 220 36 Q350 40 380 112 Z" fill="{tapa}"/>
<path d="M22 112 Q220 98 418 112 L410 152 Q220 164 30 152 Z" fill="url(#g{x})"/>
<path d="M60 112 Q90 40 220 36 Q350 40 380 112 Z" fill="url(#g{x})"/>
<image href="{logo}" x="85" y="330" width="270" height="138"/>
</svg>'''
page("vaso", 1200, 1500, G, vaso(150, 420, C, G, LOGO["granate"]) + vaso(610, 380, G, C, LOGO["crema"]) +
     f'<p class="r" style="position:absolute;left:0;right:0;top:150px;text-align:center;color:{C};font-size:34px;margin:0">Café para llevar</p>'
     f'<p class="fr" style="position:absolute;left:0;right:0;top:200px;text-align:center;color:{SOL};font-size:96px;margin:0">recién hecho</p>')

# 2. Bolsa kraft con pegatina
bolsa = f'''<svg style="position:absolute;left:250px;top:220px" width="700" height="1120" viewBox="0 0 700 1120">
<defs><filter id="bb"><feGaussianBlur stdDeviation="18"/></filter><linearGradient id="kg" x1="0" x2="1"><stop offset="0" stop-color="#000" stop-opacity=".12"/><stop offset=".5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".08"/></linearGradient></defs>
<ellipse cx="350" cy="1088" rx="320" ry="24" fill="#000" opacity=".25" filter="url(#bb)"/>
<path d="M60 160 L640 160 L660 1080 L40 1080 Z" fill="#C79A6B"/>
<path d="M60 160 L640 160 L660 1080 L40 1080 Z" fill="url(#kg)"/>
<path d="M60 160 L640 160 L640 60 L60 60 Z" fill="#B88A5C"/>
<path d="M60 60 L90 80 L120 60 L150 80 L180 60 L210 80 L240 60 L270 80 L300 60 L330 80 L360 60 L390 80 L420 60 L450 80 L480 60 L510 80 L540 60 L570 80 L600 60 L630 80 L640 60 L640 40 L60 40 Z" fill="{ALT}"/>
<path d="M60 160 L640 160" stroke="#A97C50" stroke-width="4"/>
<path d="M350 160 L350 1080" stroke="#000" stroke-opacity=".05" stroke-width="3"/>
<g transform="rotate(-4 350 520)">
<rect x="150" y="300" width="400" height="460" rx="30" fill="{C}"/>
<image href="{LOGO['granate']}" x="190" y="340" width="320" height="163"/>
<image href="{ilu('kiosco', 'linea')}" x="255" y="520" width="190" height="190"/>
<text x="350" y="738" text-anchor="middle" font-family="Figtree" font-weight="800" font-size="26" letter-spacing="3" fill="{G}">CAFÉ · GALLETAS · KIOSCO</text>
</g></svg>'''
page("bolsa", 1200, 1500, ALT, bolsa)

# 3. Camiseta (espalda)
cami = f'''<svg style="position:absolute;left:100px;top:180px" width="1000" height="1180" viewBox="0 0 1000 1180">
<defs><filter id="cb"><feGaussianBlur stdDeviation="20"/></filter>
<linearGradient id="cg" x1="0" x2="1"><stop offset="0" stop-color="#000" stop-opacity=".18"/><stop offset=".3" stop-color="#000" stop-opacity="0"/><stop offset=".7" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".18"/></linearGradient></defs>
<path d="M330 40 Q500 90 670 40 L960 190 L880 420 L780 380 L790 1140 L210 1140 L220 380 L120 420 L40 190 Z" fill="#000" opacity=".25" filter="url(#cb)" transform="translate(0 18)"/>
<path d="M330 40 Q500 90 670 40 L960 190 L880 420 L780 380 L790 1140 L210 1140 L220 380 L120 420 L40 190 Z" fill="{G}"/>
<path d="M330 40 Q500 90 670 40 L960 190 L880 420 L780 380 L790 1140 L210 1140 L220 380 L120 420 L40 190 Z" fill="url(#cg)"/>
<path d="M330 40 Q500 72 670 40" stroke="{H}" stroke-width="10" fill="none"/>
<text x="500" y="250" text-anchor="middle" font-family="Figtree" font-weight="800" font-size="30" letter-spacing="4" fill="{C}">URBAN EXPRESS · DESDE EL KIOSCO</text>
<image href="{LOGO['crema']}" x="290" y="280" width="420" height="214"/>
<image href="{ilu('kiosco', 'linea-crema')}" x="380" y="540" width="240" height="240"/>
<text x="500" y="850" text-anchor="middle" font-family="Sansita" font-weight="900" font-size="54" fill="{SOL}">tu parada de cada día</text>
<text x="500" y="910" text-anchor="middle" font-family="Figtree" font-weight="800" font-size="26" letter-spacing="4" fill="{C}">CAFÉ · GALLETAS ARTESANAS · REVISTAS</text>
</svg>'''
page("camiseta", 1200, 1500, AZUL, cami)

# 4. Hoja de pegatinas
peg = ""
pos = [("kiosco", 120, 140, -6, 330), ("vaso", 520, 110, 7, 300), ("galleta", 860, 260, -10, 260), ("solete-linea", 90, 560, 8, 300),
       ("revistas", 470, 520, -4, 280), ("lata", 820, 640, 9, 250), ("bolsa-snacks", 130, 980, 5, 290), ("pizarra", 800, 1010, -8, 250)]
for n, x, y, r, w in pos:
    peg += f'<img src="{ilu(n, "pegatina")}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;transform:rotate({r}deg)">'
peg += (f'<div style="position:absolute;left:390px;top:930px;width:420px;padding:36px 30px;background:{C};border-radius:40px;transform:rotate(-3deg);text-align:center">'
        f'<img src="{LOGO["granate"]}" style="width:340px;display:block;margin:0 auto"></div>')
page("pegatinas", 1200, 1500, G, peg)

# 5. Patrón
pat = ""
names = ["galleta", "vaso", "solete-linea", "kiosco", "lata", "revistas", "bolsa-snacks", "pizarra"]
k = 0
for row in range(8):
    for col in range(7):
        n = names[(row * 3 + col) % len(names)]
        x = col * 180 - 40 + (90 if row % 2 else 0); y = row * 200 - 40
        r = [-12, 8, -4, 10, -8, 5][(row + col) % 6]
        pat += f'<img src="{ilu(n, "linea")}" style="position:absolute;left:{x}px;top:{y}px;width:140px;transform:rotate({r}deg)">'
page("patron", 1200, 1500, C, pat)
pat2 = pat.replace("-linea.svg", "-linea-crema.svg")
pat2 += (f'<div style="position:absolute;left:300px;top:610px;width:600px;padding:56px 40px;background:{C};border-radius:60px;text-align:center;box-shadow:0 0 0 18px {G}">'
         f'<img src="{LOGO["granate"]}" style="width:480px;display:block;margin:0 auto"></div>')
page("patron-logo", 1200, 1500, G, pat2)

# 6. Tarjeta de fidelidad
def sello(i, x, y, lleno):
    inner = f'<img src="{ilu("solete-linea", "linea")}" style="width:96px;position:absolute;left:4px;top:4px">' if lleno else ""
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:104px;height:104px;border-radius:52px;border:4px dashed {G}">{inner}</div>'
def tarjeta(x, y, r, frente):
    if frente:
        inner = (f'<img src="{LOGO["crema"]}" style="position:absolute;left:60px;top:70px;width:420px">'
                 f'<img src="{ilu("galleta", "pegatina")}" style="position:absolute;right:50px;top:150px;width:300px;transform:rotate(-10deg)">'
                 f'<p class="r" style="position:absolute;left:64px;bottom:60px;margin:0;color:{SOL};font-size:28px">Tarjeta de cafés</p>')
        bg = G
    else:
        sellos = "".join(sello(i, 60 + (i % 5) * 140, 150 + (i // 5) * 130, i < 6) for i in range(10))
        inner = (f'<p class="fr" style="position:absolute;left:60px;top:56px;margin:0;color:{G};font-size:56px">10 cafés, 1 galleta</p>' + sellos +
                 f'<p class="r" style="position:absolute;left:60px;bottom:40px;margin:0;color:{H};font-size:22px">Pide tu sello en cada café</p>')
        bg = C
    return (f'<div style="position:absolute;left:{x}px;top:{y}px;width:780px;height:480px;border-radius:28px;background:{bg};transform:rotate({r}deg);'
            f'box-shadow:0 30px 60px rgba(0,0,0,.25);overflow:hidden">{inner}</div>')
page("tarjeta", 1200, 1500, AZUL, tarjeta(150, 230, -6, True) + tarjeta(270, 790, 4, False))

# --- Versiones 16:9 para el manual ---
cov = ""
for row in range(6):
    for col in range(11):
        n = names[(row * 3 + col) % len(names)]
        x = col * 180 - 40 + (90 if row % 2 else 0); y = row * 190 - 30
        r = [-12, 8, -4, 10, -8, 5][(row + col) % 6]
        cov += f'<img src="{ilu(n, "linea-crema")}" style="position:absolute;left:{x}px;top:{y}px;width:130px;opacity:.9;transform:rotate({r}deg)">'
cov += (f'<div style="position:absolute;left:560px;top:290px;width:800px;padding:70px 60px 56px;background:{C};border-radius:70px;text-align:center;box-shadow:0 0 0 24px {G}">'
        f'<img src="{LOGO["granate"]}" style="width:620px;display:block;margin:0 auto">'
        f'<p class="r" style="margin:26px 0 0;color:{G};font-size:30px">Manual de marca · 2026</p></div>')
page("portada", 1920, 1080, G, cov)
band = ""
for i, (n, w, r) in enumerate([("kiosco", 400, -5), ("vaso", 350, 6), ("galleta", 340, -8), ("solete-linea", 360, 4), ("revistas", 340, -6), ("lata", 300, 8), ("bolsa-snacks", 320, -4), ("pizarra", 310, 6)]):
    x = 40 + (i % 4) * 470 + (0 if i < 4 else 120); y = 50 if i < 4 else 560
    band += f'<img src="{ilu(n, "pegatina")}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;transform:rotate({r}deg)">'
page("ilustraciones", 1920, 1080, G, band)
pat3 = ""
for row in range(6):
    for col in range(11):
        n = names[(row * 3 + col) % len(names)]
        x = col * 180 - 40 + (90 if row % 2 else 0); y = row * 190 - 30
        r = [-12, 8, -4, 10, -8, 5][(row + col) % 6]
        pat3 += f'<img src="{ilu(n, "linea")}" style="position:absolute;left:{x}px;top:{y}px;width:130px;transform:rotate({r}deg)">'
page("patron-ancho", 1920, 1080, C, pat3)
print("ok")
