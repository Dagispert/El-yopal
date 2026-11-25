"""Vectoriza el logotipo original de El Yopal (una tinta) a un path SVG."""
import sys
import numpy as np
from PIL import Image, ImageFilter
import potrace

src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("L")
# subir resolución para un trazado suave
im = im.resize((im.width * 3, im.height * 3), Image.LANCZOS).filter(ImageFilter.GaussianBlur(1.2))
a = np.array(im)
mask = a < 110  # tinta oscura sobre fondo crema
ys, xs = np.where(mask)
pad = 6
x0, x1, y0, y1 = xs.min() - pad, xs.max() + pad, ys.min() - pad, ys.max() + pad
mask = mask[y0:y1, x0:x1]
bm = potrace.Bitmap(~mask)
plist = bm.trace(turdsize=40, alphamax=1.0, opticurve=True, opttolerance=0.3)
d = []
for curve in plist:
    s = curve.start_point
    d.append(f"M{s.x:.1f} {s.y:.1f}")
    for seg in curve.segments:
        if seg.is_corner:
            d.append(f"L{seg.c.x:.1f} {seg.c.y:.1f}L{seg.end_point.x:.1f} {seg.end_point.y:.1f}")
        else:
            d.append(f"C{seg.c1.x:.1f} {seg.c1.y:.1f} {seg.c2.x:.1f} {seg.c2.y:.1f} {seg.end_point.x:.1f} {seg.end_point.y:.1f}")
    d.append("Z")
W, H = mask.shape[1], mask.shape[0]
open(out, "w").write(f"{W} {H}\n" + "".join(d))
print("trazado", W, H, len(plist), "curvas")
