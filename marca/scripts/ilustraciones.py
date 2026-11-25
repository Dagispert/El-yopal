"""Ilustraciones de trazo a mano de El Yopal (estilo pegatina, una tinta).

Cada dibujo se define con primitivas sencillas; luego cada trazo se muestrea,
se le añade un temblor suave (como un rotulador) y se suaviza con Catmull-Rom.
"""
import math, os, random, sys

OUT = sys.argv[1]
GRANATE, CREMA, HONDO = "#8C1D2F", "#FFF4E2", "#4A0E18"
W = 300  # lienzo de cada ilustración

# ---------- primitivas ----------
def seg(p0, p1, n=None):
    d = math.dist(p0, p1); n = n or max(3, int(d / 8))
    return [(p0[0] + (p1[0] - p0[0]) * i / n, p0[1] + (p1[1] - p0[1]) * i / n) for i in range(n + 1)]

def poly(pts, closed=False):
    out = []
    pts = pts + [pts[0]] if closed else pts
    for a, b in zip(pts, pts[1:]):
        s = seg(a, b); out += s if not out else s[1:]
    return out

def arc(c, r, a0, a1, ry=None, n=None):
    ry = ry or r; n = n or max(6, int(abs(a1 - a0) / 6))
    return [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + ry * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

def bez(p0, p1, p2, p3, n=16):
    out = []
    for i in range(n + 1):
        t = i / n; u = 1 - t
        out.append((u**3*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t**3*p3[0], u**3*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t**3*p3[1]))
    return out

# ---------- temblor de mano y suavizado ----------
def wobble(pts, amp, rng, closed=False):
    if amp == 0 or len(pts) < 3: return pts
    k1, k2 = rng.uniform(0, 6.28), rng.uniform(0, 6.28)
    f1, f2 = rng.uniform(0.15, 0.3), rng.uniform(0.5, 0.9)
    out = []
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        a, b = pts[max(0, i - 1)], pts[min(n - 1, i + 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]; L = math.hypot(dx, dy) or 1
        nx, ny = -dy / L, dx / L
        o = amp * (0.7 * math.sin(i * f1 + k1) + 0.3 * math.sin(i * f2 + k2))
        if not closed and (i == 0 or i == n - 1): o *= 0.4
        out.append((x + nx * o, y + ny * o))
    return out

def to_path(pts, closed=False):
    if closed: pts = pts[:-1] if pts[0] == pts[-1] else pts
    P = (pts[-1:] + pts + pts[:2]) if closed else ([pts[0]] + pts + [pts[-1]])
    d = f"M{P[1][0]:.1f} {P[1][1]:.1f}"
    rng_ = range(1, len(P) - 2)
    for i in rng_:
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f"C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}"
    return d + ("Z" if closed else "")

class Dibujo:
    def __init__(self, nombre, seed):
        self.nombre, self.rng = nombre, random.Random(seed)
        self.trazos = []   # (d, cerrado, relleno_silueta, relleno_tinta)
    def t(self, pts, closed=False, silueta=False, tinta=False, amp=1.6):
        self.trazos.append((to_path(wobble(pts, amp, self.rng, closed), closed), closed, silueta, tinta))

    def svg(self, modo):
        """modo: 'pegatina' (granate sobre crema con borde), 'linea' (granate), 'linea-crema'."""
        tinta = CREMA if modo == "linea-crema" else GRANATE
        g = []
        if modo == "pegatina":
            for d, c, sil, _ in self.trazos:
                g.append(f'<path d="{d}" fill="{CREMA if sil else "none"}" stroke="{CREMA}" stroke-width="40" stroke-linecap="round" stroke-linejoin="round"/>')
            for d, c, sil, _ in self.trazos:
                if sil: g.append(f'<path d="{d}" fill="{CREMA}"/>')
        for d, c, sil, tin in self.trazos:
            fill = tinta if tin else "none"
            g.append(f'<path d="{d}" fill="{fill}" stroke="{tinta}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>')
        pad = 26 if modo == "pegatina" else 6
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad} {-pad} {W + 2*pad} {W + 2*pad}" width="{W + 2*pad}" height="{W + 2*pad}" role="img" aria-label="{self.nombre}">'
                f'<title>{self.nombre}</title>{"".join(g)}</svg>\n')

D = []

# 1. Vaso para llevar
v = Dibujo("Vaso de café", 3)
v.t(poly([(84, 98), (216, 98), (198, 268), (102, 268)], closed=True), closed=True, silueta=True)
v.t(poly([(72, 98), (228, 98), (224, 76), (76, 76)], closed=True), closed=True, silueta=True)
v.t(bez((88, 76), (100, 50), (200, 50), (212, 76)), silueta=False)
v.t(poly([(92, 152), (208, 152)])); v.t(poly([(97, 214), (203, 214)]))
for i, a in enumerate(range(200, 341, 35)):
    r0, r1 = 15, 24
    v.t(seg((150 + r0 * math.cos(math.radians(a)), 196 + r0 * math.sin(math.radians(a))), (150 + r1 * math.cos(math.radians(a)), 196 + r1 * math.sin(math.radians(a))), 3), amp=0.4)
v.t(arc((150, 196), 11, 180, 360), amp=0.4)
v.t(bez((128, 40), (118, 26), (140, 16), (130, 2)), amp=1); v.t(bez((160, 40), (150, 26), (172, 16), (162, 2)), amp=1)
D.append(("vaso", v))

# 2. Galleta con mordisco
g = Dibujo("Galleta", 11)
R = 112
cont = arc((150, 150), R, 335, 655, n=64)
A = cont[0]; B = cont[-1]
def pc(ang, r): return (150 + r * math.cos(math.radians(ang)), 150 + r * math.sin(math.radians(ang)))
M = pc(315, R - 34)
bite = bez(B, pc(300, R - 26), pc(306, R - 40), M, n=8)[1:] + bez(M, pc(322, R - 40), pc(330, R - 26), A, n=8)[1:]
g.t(cont + bite, closed=True, silueta=True, amp=2.2)
rng = random.Random(4)
for (x, y, r) in [(110, 105, 16), (165, 120, 13), (95, 170, 14), (150, 185, 17), (205, 175, 12), (130, 230, 11), (190, 225, 14), (70, 130, 9)]:
    pts = arc((x, y), r, 0, 360, ry=r * 0.8, n=10)
    pts = [(px + rng.uniform(-3, 3), py + rng.uniform(-3, 3)) for px, py in pts]
    g.t(pts, closed=True, tinta=(r > 12), amp=0.8)
D.append(("galleta", g))

# 3. Revistas
m = Dibujo("Revistas", 5)
def rot(pts, c, ang):
    a = math.radians(ang); return [(c[0] + (x - c[0]) * math.cos(a) - (y - c[1]) * math.sin(a), c[1] + (x - c[0]) * math.sin(a) + (y - c[1]) * math.cos(a)) for x, y in pts]
m.t(rot(poly([(70, 50), (210, 50), (210, 250), (70, 250)], closed=True), (140, 150), -8), closed=True, silueta=True)
m.t(poly([(100, 66), (236, 66), (236, 268), (100, 268)], closed=True), closed=True, silueta=True)
m.t(poly([(118, 86), (218, 86), (218, 116), (118, 116)], closed=True), closed=True, tinta=True, amp=0.8)
m.t(arc((168, 206), 40, 180, 360, n=16), amp=1)
for ang in (200, 235, 270, 305, 340):
    m.t(seg((168 + 52 * math.cos(math.radians(ang)), 206 + 52 * math.sin(math.radians(ang))), (168 + 66 * math.cos(math.radians(ang)), 206 + 66 * math.sin(math.radians(ang))), 3), amp=0.4)
m.t(poly([(116, 206), (220, 206)]), amp=0.8)
m.t(poly([(118, 236), (200, 236)])); m.t(poly([(118, 250), (170, 250)]))
D.append(("revistas", m))

# 4. Lata de refresco
l = Dibujo("Lata", 8)
l.t(arc((150, 66), 58, 180, 360, ry=16) + poly([(208, 66), (208, 250)])[1:] + arc((150, 250), 58, 0, 180, ry=16)[1:] + poly([(92, 250), (92, 66)])[1:], closed=True, silueta=True)
l.t(arc((150, 66), 58, 0, 180, ry=16))
l.t(arc((150, 62), 40, 0, 360, ry=10, n=20), closed=True, amp=0.6)
l.t(arc((162, 60), 9, 0, 360, ry=5, n=10), closed=True, amp=0.3)
l.t(bez((92, 160), (130, 130), (170, 190), (208, 150)))
l.t(bez((92, 190), (130, 160), (170, 220), (208, 180)))
D.append(("lata", l))

# 5. Bolsa de patatas
b = Dibujo("Bolsa de snacks", 21)
top = [(70 + i * 20, 52 + (8 if i % 2 else 0)) for i in range(9)]
bot = [(230 - i * 20, 252 + (-8 if i % 2 else 0)) for i in range(9)]
b.t(poly(top + [(236, 150)] + bot + [(64, 150)], closed=True), closed=True, silueta=True, amp=1)
b.t(poly([(80, 78), (220, 78)])); b.t(poly([(80, 226), (220, 226)]))
b.t(bez((112, 150), (120, 108), (182, 104), (192, 140)) + bez((192, 140), (200, 176), (128, 196), (112, 150))[1:], closed=True, amp=1.2)
b.t(poly([(128, 146), (176, 140)]), amp=0.6); b.t(poly([(136, 162), (170, 158)]), amp=0.6)
D.append(("bolsa-snacks", b))

# 6. El kiosco
k = Dibujo("El kiosco", 2)
k.t(poly([(58, 104), (150, 46), (242, 104)], closed=True), closed=True, silueta=True)
k.t(arc((150, 38), 7, 0, 360, n=8), closed=True, tinta=True, amp=0.2)
scal = [(44, 104), (256, 104), (256, 132)]
for i in range(8):
    x0 = 256 - i * 26.5
    scal += arc((x0 - 13.25, 132), 13.25, 0, 180, ry=9, n=6)[1:]
k.t(scal + [(44, 104)], closed=True, silueta=True)
k.t(poly([(70, 142), (230, 142), (230, 262), (70, 262)], closed=True), closed=True, silueta=True)
k.t(poly([(112, 158), (188, 158), (188, 262), (112, 262)], closed=True), closed=True, amp=1)
k.t(poly([(112, 214), (188, 214)]))
for x in (84, 98):
    k.t(poly([(x, 150), (x, 254)]), amp=0.8)
for x in (202, 216):
    k.t(poly([(x, 150), (x, 254)]), amp=0.8)
for y in (172, 202, 232):
    k.t(poly([(74, y), (108, y)]), amp=0.6); k.t(poly([(192, y), (226, y)]), amp=0.6)
k.t(poly([(30, 272), (270, 272)]), amp=1.2)
D.append(("kiosco", k))

# 7. Pizarra de caballete
p = Dibujo("Pizarra", 17)
p.t(poly([(100, 40), (200, 40), (220, 222), (80, 222)], closed=True), closed=True, silueta=True)
p.t(poly([(112, 56), (188, 56), (204, 208), (96, 208)], closed=True), closed=True, amp=1)
p.t(poly([(84, 222), (72, 276)]), amp=0.6); p.t(poly([(216, 222), (228, 276)]), amp=0.6)
p.t(bez((120, 84), (134, 72), (152, 94), (172, 78)), amp=0.8)
p.t(poly([(116, 116), (184, 116)]), amp=1.2); p.t(poly([(114, 142), (166, 142)]), amp=1.2)
p.t(arc((132, 178), 13, 0, 360, n=10), closed=True, amp=0.5); p.t(arc((166, 180), 10, 0, 360, n=10), closed=True, amp=0.5)
D.append(("pizarra", p))

# 8. El Solete en línea
s = Dibujo("Solete", 1)
s.t(arc((150, 150), 70, 0, 360, n=40), closed=True, silueta=True, amp=1.6)
for i, a in enumerate(range(-90, 270, 30)):
    ln = 34 if i % 2 == 0 else 22
    s.t(seg((150 + 92 * math.cos(math.radians(a)), 150 + 92 * math.sin(math.radians(a))), (150 + (92 + ln) * math.cos(math.radians(a)), 150 + (92 + ln) * math.sin(math.radians(a))), 4), amp=0.8)
s.t(seg((126, 130), (126, 146), 3), amp=0.3); s.t(seg((174, 130), (174, 146), 3), amp=0.3)
s.t(bez((122, 168), (136, 190), (164, 190), (178, 168)), amp=0.6)
D.append(("solete-linea", s))

os.makedirs(OUT, exist_ok=True)
for nombre, d in D:
    for modo in ("pegatina", "linea", "linea-crema"):
        open(os.path.join(OUT, f"{nombre}-{modo}.svg"), "w").write(d.svg(modo))
print("ok", len(D))
