"""Escribe las vistas previas y guías de cada componente de El Yopal."""
import os, sys
OUT = sys.argv[1]
B = {
 "icono": "8f9d418b4718c59eec589a254b3cd9ed",
 "il_vaso": "7ee960d9064343daff9dba977d9cb542",
 "il_revistas": "70566e9f9b54df9f604d2c8802e05c71",
 "il_galleta": "952e2974f0b367a4a3b6d472a702736c",
 "il_bolsa": "1bd876c1954dd27c9b8bb2e762fc7b96",
 "il_lata": "33e2af8433fe8637ff440a5a0310f621",
 "sol_tinta": "887e1aa1a7c46675f44622526c79a1ed",
 "sol_asomando": "427ad19ae5098cc91368c6fb2d4a6726",
 "logo_granate": "14e119fe25db84bd279e3d1483998cdb", "logo_crema": "e6bd11abc0ef6264dc6e882ce14cad11",
 "logo_tinta": "821369b3fbc76aa387486f26bc18b3dc", "bloque_granate": "ad06c551c11b64a079e945c1fa9f281d",
 "bloque_crema": "6c9291e9a1d67a9167adf8be432503e5", "avatar": "7d21f01b159d698cac9b1642b2665c5e",
 "sol_feliz": "6ed061dfa0f9ef08f29f71b433321930", "sol_guino": "afcb9592b8df9e56acb7c77c98772cc5",
 "sol_sorpresa": "197caebd84a252d8d9feaf351c3895d2", "i_cafe": "6bfe039ccebe4d45a9b91d036bcc9acc",
 "i_galleta": "73b2a50af1261ef026472e11600e35e2", "i_llevar": "138dad471ca184bbde802fb4220c3867",
 "i_bebida": "0078b103f58371008256e74c2b8a5e67", "i_snack": "18d2f75d08e105f8c102f5f7f90063e0",
 "i_revista": "7e5e442eb1c383ff4fb30de2de18cb77", "i_sol": "dfb618a492c26db8d6fc79f6d350fe50",
 "i_ubicacion": "489d4e391e4e865e7a066a90c4afd3c0", "f_fachada": "ae22d6c2f49cda4472a73a1336a876ab",
 "f_mostrador": "9fc953f2f8cc23dcf35532c2226e537e", "f_revistas": "59e3ba07b8e7fe687162cbaa84f282fb",
}
def u(k): return f"/_blob/{B[k]}"

import re as _re
_GALLETA = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ilustra", "galleta-pegatina.svg")).read()
def galleta(size, extra=""):
    """Galleta dibujada a mano (pegatina granate sobre crema)."""
    svg = _re.sub(r'<title>.*?</title>', '', _GALLETA.strip())
    svg = _re.sub(r'width="[^"]*" height="[^"]*"', f'width="{size}" height="{size}"', svg, count=1)
    return svg.replace('<svg ', f'<svg aria-hidden="true" {extra} ', 1)

def doc(marker, title, style, body):
    return f"""{marker}
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
  html, body {{ margin: 0; }}
  body {{ background: var(--superficie); color: var(--tinta); font-family: var(--font-texto); padding: 16px; }}
{style}
</style>
</head>
<body>
{body}
<script>
  /* Reduce cada lienzo de 1080 px al ancho de su marco */
  document.querySelectorAll('.yp-lienzo-marco').forEach(function (m) {{
    var l = m.querySelector('.yp-lienzo'); var s = m.clientWidth / 1080;
    l.style.transform = 'scale(' + s + ')'; m.style.height = (l.offsetHeight * s) + 'px';
  }});
</script>
</body>
</html>
"""

def marco(w, inner, cls="yp-lienzo--post", bg="granate"):
    return f'<div class="yp-lienzo-marco" style="width:{w}px" data-theme="claro"><div class="yp-lienzo {cls}" style="background:var(--{bg})">{inner}</div></div>'

C = {}  # nombre -> (marker, style, body, readme)

# ---------- MARCA ----------
C["Logotipo"] = ('<!-- @dsCard group="Marca" height=340 subtitle="Logotipo y bloque de marca sobre sus tres fondos" -->', """
  .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 12px; }
  .t { border-radius: var(--radio-m); padding: 22px 24px; display: grid; place-items: center; min-height: 112px; }
  .t img { max-width: 100%; height: 96px; }
  .t.b img { height: 118px; }
  .lab { font: 700 12px/1 var(--font-rotulo); letter-spacing: .08em; text-transform: uppercase; color: var(--tinta-suave); margin: 6px 2px 0; }
""", f"""<div class="grid" data-theme="claro">
  <div><div class="t" style="background:var(--crema);border:1px solid var(--linea)"><img src="{u('logo_granate')}" alt="El Yopal"></div><p class="lab">Granate sobre crema · principal</p></div>
  <div><div class="t" style="background:var(--granate)"><img src="{u('logo_crema')}" alt="El Yopal"></div><p class="lab">Crema sobre granate · toldo y redes</p></div>
  <div><div class="t" style="background:var(--sol)"><img src="{u('logo_tinta')}" alt="El Yopal"></div><p class="lab">Granate hondo sobre sol · una tinta</p></div>
  <div><div class="t b" style="background:var(--granate)"><img src="{u('bloque_crema')}" alt="El Yopal · Urban Express"></div><p class="lab">Bloque con rótulo · cabeceras</p></div>
</div>""", """# Logotipo

El logotipo de El Yopal es el rotulado a mano original: «El Yopal» en letra de pincel inclinada, subrayado, con el sol saliendo por encima de la «l». **No se modifica**: ni el dibujo, ni la inclinación, ni las proporciones. Solo cambia el color de la tinta, y siempre es una sola tinta.

## Qué archivo usar
- `logotipo-granate.svg` sobre `crema` o `superficie`: la versión principal.
- `logotipo-crema.svg` sobre `granate` o fotos oscuras.
- `logotipo-tinta.svg` (`granate-hondo`) sobre `sol` o `azul`, y para impresión a una tinta.
- `bloque-*.svg`: el logotipo con el rótulo URBAN EXPRESS · CAFÉ & GALLETAS debajo, para cabeceras, la carta y pies de post.
- `avatar-perfil.svg`: logotipo `crema` sobre `granate`, para la foto de perfil (a partir de unos 100 px).
- `icono-pequeno.svg`: el Solete sobre un círculo `granate`, para todo lo que mida menos de 48 px (favicon, icono de app, mapas).

## Reglas
- Área de respeto: la altura de la «o» alrededor de todo el logotipo, rayos incluidos.
- Tamaño mínimo: 90 px de ancho en pantalla, 25 mm impreso.
- No lo enderezes, no lo estires, no separes el sol del texto, no pintes el sol de otro color, no le pongas sombra ni contorno y no lo reescribas con ninguna fuente.
- Sobre foto, solo `logotipo-crema` y solo encima de una zona oscura y tranquila de la imagen.
""")

C["Solete"] = ('<!-- @dsCard group="Marca" height=300 subtitle="La mascota: un sol plano y luminoso" -->', """
  .row { display: flex; flex-wrap: wrap; gap: 20px; align-items: flex-end; }
  figure { margin: 0; display: grid; gap: 8px; justify-items: center; }
  .f { width: 150px; height: 150px; border-radius: var(--radio-m); display: grid; place-items: center; }
  .f img { width: 130px; height: 130px; }
  .as { width: 316px; height: 150px; border-radius: var(--radio-m); background: var(--azul); display: flex; align-items: flex-end; justify-content: center; overflow: hidden; }
  .as img { width: 230px; display: block; }
  figcaption { font: 700 12px/1.2 var(--font-rotulo); letter-spacing: .08em; text-transform: uppercase; color: var(--tinta-suave); text-align: center; }
""", f"""<div class="row" data-theme="claro">
  <figure><div class="f" style="background:var(--granate)"><img src="{u('sol_feliz')}" alt="Solete sonriendo"></div><figcaption>Feliz · por defecto</figcaption></figure>
  <figure><div class="f" style="background:var(--azul)"><img src="{u('sol_guino')}" alt="Solete guiñando"></div><figcaption>Guiño · ofertas</figcaption></figure>
  <figure><div class="f" style="background:var(--granate)"><img src="{u('sol_sorpresa')}" alt="Solete sorprendido"></div><figcaption>Sorpresa · novedades</figcaption></figure>
  <figure><div class="f" style="background:var(--sol)"><img src="{u('sol_tinta')}" alt="Solete a una tinta"></div><figcaption>Una tinta · sobre sol</figcaption></figure>
  <figure><div class="as"><img src="{u('sol_asomando')}" alt="Solete asomando"></div><figcaption>Asomando · bordes</figcaption></figure>
</div>""", """# Solete

El Solete es la mascota de El Yopal: un sol plano y luminoso, macizo y sin contorno, con doce rayos de puntas redondas que alternan largo y corto, y una cara sencilla de trazo en `granate-hondo`.

## Versiones
- **Feliz** (`solete-feliz.svg`): la cara por defecto. Saludos, horarios, «ya estamos abiertos».
- **Guiño** (`solete-guino.svg`): ofertas y combos.
- **Sorpresa** (`solete-sorpresa.svg`): novedades y sabores nuevos.
- **Una tinta** (`solete-tinta.svg`): sol en `granate-hondo` con cara `sol`. Para fondos `sol`, donde el amarillo desaparecería, y para impresión a una tinta (vasos, bolsas, sellos).
- **Asomando** (`solete-asomando.svg`): medio sol saliendo, para pegar en el borde inferior de un post o una historia.

## Dónde se lee bien
- Muy bien sobre `granate`, `azul`, `granate-hondo` y fotos.
- Sobre `crema` o `superficie` el amarillo tiene poco contraste: ponlo dentro de un bloque de color o usa `solete-tinta`.
- Sobre `sol`, siempre `solete-tinta`.

## Reglas
- Uno por pieza, como mucho.
- Se puede girar un poco (entre -12° y 12°). Sin contorno, sin sombra, sin borde de pegatina y sin cambiarle el color.
- Tamaño mínimo: 40 px.
""")

# ---------- WEB ----------
C["Boton"] = ('<!-- @dsCard group="Web" height=96 subtitle="Principal, sol y contorno" -->', "", """<div class="yp-row" style="padding:8px 0">
  <button class="yp-btn" type="button">Ver la carta</button>
  <button class="yp-btn yp-btn--sol" type="button">Cómo llegar</button>
  <button class="yp-btn yp-btn--contorno" type="button">Síguenos</button>
</div>""", """# Boton

Píldora en Barlow Condensed mayúscula con borde `granate-hondo` y `sombra-pegatina`; al pulsar se «despega» hacia la sombra.

## Variantes
- `yp-btn`: acción principal, una por pantalla. Fondo `granate`, texto `sobre-granate`.
- `yp-btn yp-btn--sol`: acción secundaria con ganas («Cómo llegar», «Pedir»). Texto `sobre-sol`.
- `yp-btn yp-btn--contorno`: acciones discretas sobre `superficie`.

## Qué pones tú
Un `<button>` o `<a>` con el texto en infinitivo o imperativo corto: «Ver la carta», «Llámanos», «Cómo llegar». Máximo tres palabras. El foco de teclado usa `foco` (3 px, separado 2 px).
""")

C["Etiqueta"] = ('<!-- @dsCard group="Web" height=90 subtitle="Pegatinas alargadas para destacar" -->', "", """<div class="yp-row" style="padding:8px 0">
  <span class="yp-tag yp-tag--sol">Recién horneadas</span>
  <span class="yp-tag">Para llevar</span>
  <span class="yp-tag yp-tag--azul">Bien fría</span>
  <span class="yp-tag yp-tag--granate">Nuevo</span>
</div>""", """# Etiqueta

Pegatina alargada en mayúsculas para marcar un producto o un post: «Recién horneadas», «Para llevar», «Nuevo».

## Variantes
- `yp-tag` (crema): información neutra.
- `yp-tag--sol`: lo que queremos vender hoy.
- `yp-tag--azul`: bebidas frías y cosas frescas.
- `yp-tag--granate`: «Nuevo» y avisos.

## Reglas
Dos palabras como mucho. Máximo dos etiquetas juntas. En posts se pueden girar unos grados, en la web van rectas.
""")

C["Precio"] = ('<!-- @dsCard group="Web" height=200 subtitle="Pegatina de precio" -->', """
  .row { display: flex; gap: 32px; align-items: center; padding: 16px 8px; flex-wrap: wrap; }
""", """<div class="row">
  <span class="yp-precio"><span><b>2,80 €</b><small>la galleta</small></span></span>
  <span class="yp-precio" style="transform:rotate(6deg)"><span><small>2 productos</small><b>3,45 €</b></span></span>
</div>""", """# Precio

Círculo `sol` con borde blanco, `sombra-pegatina` y el precio en el estilo `precio`, girado como si se hubiera pegado a mano.

## Qué pones tú
El importe con coma decimal y el símbolo detrás, separado por un espacio: `2,80 €`. Una línea pequeña opcional en `rotulo` («la galleta», «2 productos»).

## Reglas
Un precio por pieza. Gíralo entre -10° y 10°. Siempre encima del fondo, nunca sobre texto.
""")

C["TarjetaProducto"] = ('<!-- @dsCard group="Web" height=380 subtitle="Producto para la web y la carta digital" -->', """
  .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 24px; }
  .card { background: var(--superficie-alt); border-radius: var(--radio-m); box-shadow: var(--sombra-suave); overflow: hidden; }
  .foto { height: 170px; display: grid; place-items: center; position: relative; }
  .foto .yp-tag { position: absolute; top: 12px; left: 12px; transform: rotate(-4deg); }
  .info { padding: 16px; display: flex; justify-content: space-between; align-items: end; gap: 8px; }
  .info h3 { margin: 0; font: 900 26px/1 var(--font-display); color: var(--tinta); }
  .info p { margin: 4px 0 0; font: 500 13px/1.4 var(--font-texto); color: var(--tinta-suave); }
  .pr { font: 900 24px/1 var(--font-display); color: var(--tinta); white-space: nowrap; }
""", f"""<div class="grid">
  <article class="card"><div class="foto" style="background:var(--azul)"><span class="yp-tag yp-tag--sol">Favorita</span>{galleta(130)}</div>
    <div class="info"><div><h3>Choco chips</h3><p>Pepitas de chocolate, centro blandito.</p></div><span class="pr">2,80 €</span></div></article>
  <article class="card"><div class="foto" style="background:var(--sol)">{galleta(130)}</div>
    <div class="info"><div><h3>Oreo</h3><p>Masa de cacao y trozos de galleta.</p></div><span class="pr">2,80 €</span></div></article>
  <article class="card"><div class="foto" style="background:var(--granate)"><span class="yp-tag">Nuevo</span>{galleta(130)}</div>
    <div class="info"><div><h3>Lotus</h3><p>Galleta especiada y crema Lotus.</p></div><span class="pr">2,80 €</span></div></article>
</div>""", """# TarjetaProducto

Tarjeta para la web y la carta digital: foto del producto sobre un fondo de color plano, nombre en `display` y precio a la derecha.

## Qué pones tú
- Foto del producto recortada (PNG sin fondo) sobre `azul`, `sol` o `granate`, alternando colores en una fila.
- Nombre corto (una o dos palabras) y una frase de descripción de menos de 50 caracteres.
- Precio con el formato `2,80 €`.
- Opcional: una `Etiqueta` arriba a la izquierda.

## Reglas
Fondo `superficie-alt`, `radio-m`, `sombra-suave`. La galleta dibujada es un marcador: sustitúyela por la foto real en cuanto la tengas.
""")

# ---------- REDES ----------
post_style = """
  .row { display: flex; gap: 16px; flex-wrap: wrap; align-items: flex-start; }
  .yp-lienzo-marco { box-shadow: 0 0 0 1px var(--linea); }
"""

ps1 = f"""
<div style="position:absolute;left:96px;right:96px;top:72px;display:flex;justify-content:space-between;align-items:center">
  <span class="yp-rotulo" style="font-size:34px;color:var(--sol)">Galletas artesanas</span>
  <img src="{u('logo_crema')}" alt="" style="height:110px">
</div>
<h2 class="yp-display" style="position:absolute;left:96px;top:190px;margin:0;font-size:190px;line-height:.88;color:var(--crema)">Choco<br>chips</h2>
<div style="position:absolute;left:250px;top:560px">{galleta(640)}</div>
<span class="yp-precio" style="position:absolute;right:96px;top:520px;width:230px;height:230px;border-width:7px"><span><b style="font-size:60px">2,80 €</b><small style="font-size:22px">la galleta</small></span></span>
<p class="yp-mano" style="position:absolute;left:96px;bottom:150px;margin:0;font-size:64px;color:var(--sol);transform:rotate(-6deg)">¡recién horneada!</p>
<p class="yp-rotulo" style="position:absolute;left:96px;right:96px;bottom:72px;margin:0;font-size:26px;color:var(--crema);opacity:.85">Urban Express · Café &amp; galletas</p>
"""
ps2 = f"""
<div style="position:absolute;inset:0 0 auto 0;height:760px;background:var(--azul);border-radius:0 0 var(--radio-l) var(--radio-l)"></div>
<div style="position:absolute;left:220px;top:120px">{galleta(640)}</div>
<img src="{u('sol_sorpresa')}" alt="" style="position:absolute;right:70px;top:70px;width:220px;transform:rotate(10deg)">
<span class="yp-tag yp-tag--granate" style="position:absolute;left:96px;top:96px;font-size:30px;padding:12px 28px;transform:rotate(-5deg)">Nuevo sabor</span>
<h2 class="yp-display" style="position:absolute;left:96px;top:820px;margin:0;font-size:200px;line-height:.9;color:var(--granate)">Lotus</h2>
<p style="position:absolute;left:96px;top:1020px;margin:0;width:620px;font:500 36px/1.35 var(--font-texto);color:var(--tinta)">Galleta especiada con crema Lotus por dentro. Hasta que se acaben.</p>
<span class="yp-precio" style="position:absolute;right:96px;top:880px;width:220px;height:220px;border-width:7px;transform:rotate(8deg)"><span><b style="font-size:56px">2,80 €</b></span></span>
<img src="{u('logo_granate')}" alt="" style="position:absolute;left:96px;bottom:70px;height:100px">
"""
C["PostProducto"] = ('<!-- @dsCard group="Redes" height=600 subtitle="Post 4:5 (1080 × 1350) de producto" -->', post_style,
  f'<div class="row">{marco(420, ps1)}{marco(420, ps2, bg="crema")}</div>', """# PostProducto

Post de Instagram de 1080 × 1350 px para presentar un producto: nombre enorme en `titular-xl`, el producto grande y una pegatina de `Precio`.

## Dos versiones
- **Granate**: para los clásicos. Fondo `granate`, titular `crema`, antetítulo `sol` en `rotulo-l`, nota a mano en `sol`.
- **Crema con bloque azul**: para novedades. Bloque `azul` con `radio-l` abajo, titular `granate` y el Solete de sorpresa.

## Qué pones tú
Foto del producto recortada sin fondo (o sostenida por una mano, mirando a cámara), nombre de 1-2 palabras, precio y una frase corta. Márgenes de 96 px en los cuatro lados.

## Reglas
Una sola nota a mano por post. El logotipo siempre en una esquina, nunca centrado. Alterna granate y crema en el feed para que la rejilla respire.
""")

combo = lambda icon, txt: f'<div style="display:grid;justify-items:center;gap:18px"><span style="width:230px;height:230px;border-radius:50%;background:var(--crema);border:6px solid var(--granate-hondo);display:grid;place-items:center"><img src="{u(icon)}" alt="" style="width:170px"></span><span class="yp-rotulo" style="font-size:44px;color:var(--granate-hondo)">{txt}</span></div>'
plus = '<span class="yp-display" style="font-size:110px;color:var(--granate);align-self:start;margin-top:30px">+</span>'
po1 = f"""
<p class="yp-rotulo" style="position:absolute;left:96px;top:96px;margin:0;font-size:38px;color:var(--granate-hondo)">Combínalos como quieras</p>
<h2 class="yp-display" style="position:absolute;left:96px;top:160px;margin:0;font-size:230px;line-height:.86;color:var(--granate)">2 por<br>3,45 €</h2>
<img src="{u('sol_tinta')}" alt="" style="position:absolute;right:60px;top:120px;width:300px;transform:rotate(12deg)">
<div style="position:absolute;left:96px;right:96px;top:720px;display:flex;justify-content:space-between">{combo('il_lata','Bebida')}{plus}{combo('il_bolsa','Snack')}{plus}{combo('il_galleta','Dulce')}</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:190px;background:var(--granate);display:flex;align-items:center;justify-content:space-between;padding:0 96px">
  <img src="{u('logo_crema')}" alt="" style="height:110px"><span class="yp-mano" style="font-size:54px;color:var(--sol)">elige 2 y listo</span>
</div>
"""
C["PostOferta"] = ('<!-- @dsCard group="Redes" height=600 subtitle="Post 4:5 de promoción (el combo del kiosco)" -->', post_style,
  f'<div class="row">{marco(420, po1, bg="sol")}</div>', """# PostOferta

Post de promoción sobre `sol`: el precio es el titular y los productos se explican con ilustraciones a mano en círculos `crema`. Es la versión de marca del cartel «2 productos por 3,45 €» del kiosco.

## Qué pones tú
- La oferta en dos líneas como mucho, con el precio dentro del titular.
- De 2 a 3 ilustraciones `-linea` del grupo **Ilustraciones** con una palabra cada una.
- Una nota a mano en la banda inferior.

## Reglas
Solete de guiño siempre en las ofertas. Texto sobre `sol` en `granate` o `granate-hondo`, nunca en blanco ni en `crema`. Si la oferta tiene condiciones, van en `texto-s` dentro de la banda, no encima del amarillo.
""")

def stack(word, n, color, outline):
    out = []
    for i in range(n):
        st = f"color:transparent;-webkit-text-stroke:4px {outline}" if i % 2 else f"color:{color}"
        out.append(f'<div class="yp-display" style="font-size:236px;line-height:.86;white-space:nowrap;{st}">{word}</div>')
    return "".join(out)
pt1 = f"""
<div style="position:absolute;left:-30px;top:90px">{stack('GALLETAS', 5, 'var(--crema)', 'var(--sol)')}</div>
<div style="position:absolute;left:300px;top:390px;transform:rotate(-10deg)">{galleta(480)}</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:200px;background:var(--granate-hondo);display:flex;align-items:center;justify-content:space-between;padding:0 96px"><span class="yp-rotulo" style="font-size:34px;color:var(--crema)">Artesanas · todos los días</span><img src="{u('logo_crema')}" alt="" style="height:110px"></div>
"""
pt2 = f"""
<div style="position:absolute;left:-20px;top:90px">{stack('CAFÉ CAFÉ', 5, 'var(--granate)', 'var(--granate)')}</div>
<span style="position:absolute;left:330px;top:420px;width:420px;height:420px;border-radius:50%;background:var(--sol);border:8px solid var(--granate-hondo);display:grid;place-items:center;transform:rotate(-6deg)"><img src="{u('il_vaso')}" alt="" style="width:300px"></span>
<div style="position:absolute;left:0;right:0;bottom:0;height:200px;background:var(--crema);display:flex;align-items:center;justify-content:space-between;padding:0 96px"><span class="yp-mano" style="font-size:62px;color:var(--granate)">para llevar, claro</span><img src="{u('logo_granate')}" alt="" style="height:110px"></div>
"""
C["PostTipografico"] = ('<!-- @dsCard group="Redes" height=600 subtitle="Post 4:5 de palabra repetida" -->', post_style,
  f'<div class="row">{marco(420, pt1)}{marco(420, pt2, bg="azul")}</div>', """# PostTipografico

Una palabra repetida en `titular-xl` que llena el post, alternando líneas rellenas y en contorno, con el producto o un icono encima como pegatina. Sirve para romper el feed entre fotos.

## Qué pones tú
Una palabra (o dos muy cortas) en mayúsculas: GALLETAS, CAFÉ CAFÉ, SNACKS. Un producto recortado o un icono en círculo `sol` encima.

## Reglas
Las líneas se salen por los lados a propósito. Rellenas en `crema` sobre `granate`, o en `granate` sobre `azul`; el contorno en `sol` o el mismo `granate`. Nunca más de un post de este tipo seguido en la rejilla.
""")

pf1 = f"""
<img src="{u('f_fachada')}" alt="" style="position:absolute;left:48px;top:48px;width:984px;height:980px;object-fit:cover;object-position:50% 45%;border-radius:var(--radio-l)">
<img src="{u('sol_feliz')}" alt="" style="position:absolute;right:30px;top:850px;width:250px;transform:rotate(-8deg)">
<h2 class="yp-display" style="position:absolute;left:96px;top:1060px;margin:0;font-size:96px;line-height:.95;color:var(--crema)">Tu parada<br>de cada día</h2>
<span class="yp-tag yp-tag--sol" style="position:absolute;left:96px;top:930px;font-size:28px;padding:10px 24px;transform:rotate(-3deg)">Ya estamos abiertos</span>
"""
pf2 = f"""
<img src="{u('f_revistas')}" alt="" style="position:absolute;right:48px;top:48px;width:470px;height:1254px;object-fit:cover;border-radius:var(--radio-l)">
<p class="yp-rotulo" style="position:absolute;left:96px;top:110px;margin:0;font-size:34px;color:var(--granate)">Y además</p>
<h2 class="yp-display" style="position:absolute;left:96px;top:170px;margin:0;font-size:92px;line-height:.95;color:var(--granate)">Tus<br>revistas</h2>
<p style="position:absolute;left:96px;top:390px;width:400px;margin:0;font:500 34px/1.4 var(--font-texto);color:var(--tinta)">Las de siempre, cada semana, junto al café.</p>
<img src="{u('il_revistas')}" alt="" style="position:absolute;left:80px;top:600px;width:220px">
<img src="{u('bloque_granate')}" alt="" style="position:absolute;left:96px;bottom:90px;width:360px">
"""
C["PostFoto"] = ('<!-- @dsCard group="Redes" height=600 subtitle="Post 4:5 con foto real del kiosco" -->', post_style,
  f'<div class="row">{marco(420, pf1)}{marco(420, pf2, bg="crema")}</div>', """# PostFoto

Post con foto real del kiosco o de un producto, enmarcada con `radio-l` sobre `granate` o `crema` y con el texto fuera de la foto.

## Qué pones tú
Foto vertical u horizontal con luz cálida (por la mañana o con el kiosco iluminado), un titular de 2-4 palabras y, si hace falta, una frase.

## Reglas
- El texto va en el color de fondo, nunca encima de la foto. La única excepción es una `Etiqueta` o el Solete pegados en el borde.
- Margen de 48 px entre la foto y el borde del post.
- Fotos de producto: una mano sosteniendo el producto, fondo liso (`azul`, `sol` o la pared crema) y nada de filtros fríos.
""")

h1 = f"""
<div style="position:absolute;left:96px;top:250px"><img src="{u('logo_tinta')}" alt="" style="height:150px"></div>
<div style="position:absolute;left:0;right:0;top:900px;bottom:0;background:var(--crema);border-radius:var(--radio-l) var(--radio-l) 0 0"></div>
<img src="{u('sol_asomando')}" alt="" style="position:absolute;left:190px;top:541px;width:700px">
<h2 class="yp-display" style="position:absolute;left:96px;right:96px;top:1000px;margin:0;text-align:center;font-size:170px;line-height:.9;color:var(--granate)">Buenos<br>días</h2>
<p class="yp-mano" style="position:absolute;left:0;right:0;top:1340px;margin:0;text-align:center;font-size:72px;color:var(--granate-hondo)">el café ya está listo</p>
<div style="position:absolute;left:96px;right:96px;bottom:250px;display:flex;justify-content:center;gap:20px">
  <span class="yp-tag yp-tag--sol" style="font-size:32px;padding:12px 28px">Te esperamos</span>
</div>
"""
h2 = f"""
<p class="yp-rotulo" style="position:absolute;left:0;right:0;top:260px;margin:0;text-align:center;font-size:44px;color:var(--sol)">Pregunta seria</p>
<h2 class="yp-display" style="position:absolute;left:96px;right:96px;top:340px;margin:0;text-align:center;font-size:150px;line-height:.92;color:var(--crema)">¿Equipo<br>choco o<br>equipo<br>Lotus?</h2>
<div style="position:absolute;left:96px;right:96px;top:1080px;display:flex;justify-content:center;gap:60px">
  <div style="transform:rotate(-8deg)">{galleta(340)}</div><div style="transform:rotate(10deg)">{galleta(340)}</div>
</div>
<div style="position:absolute;left:150px;right:150px;top:1500px;height:150px;border-radius:var(--radio-pill);background:var(--crema);display:grid;place-items:center">
  <span class="yp-rotulo" style="font-size:36px;color:var(--tinta-suave)">Aquí va la encuesta</span>
</div>
<img src="{u('logo_crema')}" alt="" style="position:absolute;left:50%;bottom:110px;height:110px;transform:translateX(-50%)">
"""
C["Historia"] = ('<!-- @dsCard group="Redes" height=640 subtitle="Historia 9:16 (1080 × 1920)" -->', post_style,
  f'<div class="row">{marco(330, h1, "yp-lienzo--historia", "azul")}{marco(330, h2, "yp-lienzo--historia", "granate")}</div>', """# Historia

Historias de 1080 × 1920 px. Todo lo importante va entre los 250 px de arriba y los 250 px de abajo, que es donde Instagram no pone su interfaz.

## Dos usos
- **Saludo diario** sobre `azul`: logotipo en `granate-hondo` (`logotipo-tinta.svg`), Solete asomando, «Buenos días» en `display` y una nota a mano. Se puede repetir cada mañana cambiando solo la nota.
- **Encuesta o pregunta** sobre `granate`: pregunta en `crema`, dos opciones dibujadas o fotografiadas y hueco para la pegatina de encuesta.

## Reglas
Texto centrado solo en historias (en posts, siempre alineado a la izquierda). Una idea por historia.
""")

carta_items = [("Café solo", "1,30 €"), ("Cortado", "1,40 €"), ("Café con leche", "1,60 €"), ("Capuchino", "2,00 €"), ("Chocolate", "2,20 €")]
filas = "".join(f'<li><span>{n}</span><i></i><b>{p}</b></li>' for n, p in carta_items)
C["Carta"] = ('<!-- @dsCard group="Redes" height=470 subtitle="Carta de café y galletas (precios de café de ejemplo)" -->', """
  .carta { max-width: 560px; background: var(--granate); color: var(--crema); border-radius: var(--radio-l); padding: 32px; position: relative; overflow: hidden; }
  .carta h2 { margin: 0 0 4px; font: 900 52px/1 var(--font-display); color: var(--crema); }
  .carta .sub { margin: 0 0 24px; font: 700 15px/1 var(--font-rotulo); letter-spacing: .08em; text-transform: uppercase; color: var(--sol); }
  .carta ul { list-style: none; margin: 0 0 20px; padding: 0; display: grid; gap: 12px; }
  .carta li { display: flex; align-items: baseline; gap: 8px; font: 500 19px/1.2 var(--font-texto); }
  .carta li i { flex: 1; border-bottom: 2px dotted rgba(255, 244, 226, .45); transform: translateY(-4px); }
  .carta li b { font: 900 22px/1 var(--font-display); font-variant-numeric: tabular-nums; color: var(--sol); }
  .carta h3 { margin: 0 0 12px; font: 700 15px/1 var(--font-rotulo); letter-spacing: .08em; text-transform: uppercase; color: var(--sol); }
  .carta .sol { position: absolute; right: -22px; top: -22px; width: 140px; transform: rotate(12deg); }
  .carta .nota { font: 400 26px/1.1 var(--font-mano); color: var(--sol); margin: 8px 0 0; }
""", f"""<div class="carta" data-theme="claro">
  <img class="sol" src="{u('sol_feliz')}" alt="">
  <h2>Carta café</h2><p class="sub">Urban Express · El Yopal</p>
  <ul>{filas}</ul>
  <h3>Galletas artesanas</h3>
  <ul><li><span>Choco chips · Oreo · Lotus</span><i></i><b>2,80 €</b></li></ul>
  <p class="nota">¿café + galleta? pregúntanos por el combo</p>
</div>""", """# Carta

La carta del café en formato tarjeta: sirve para el marco del mostrador, para la web y como post o historia fija.

## Qué pones tú
Los productos con su precio real. Los precios de café de esta vista previa son de ejemplo; los de las galletas (2,80 €) son los del mostrador.

## Reglas
- Fondo `granate`, nombres en `texto` color `crema`, precios en `display` color `sol` con cifras tabulares, unidos por una línea de puntos.
- Agrupa por secciones con un antetítulo en `rotulo`.
- Precios siempre con coma y `€` detrás: `1,60 €`.
""")

C["Pizarra"] = ('<!-- @dsCard group="Redes" height=420 subtitle="La pizarra de la puerta, en digital" -->', """
  .piz { max-width: 380px; background: var(--pizarra); border: 14px solid #6B4A2E; border-radius: var(--radio-s); padding: 28px 24px; color: var(--crema); font-family: var(--font-mano); position: relative; }
  .piz h2 { margin: 0; font: 400 46px/1 var(--font-mano); color: var(--crema); }
  .piz .s { color: var(--sol); }
  .piz p { margin: 8px 0 0; font-size: 34px; line-height: 1.05; }
  .piz .row2 { display: flex; gap: 16px; align-items: center; margin-top: 16px; }
  .piz small { font-size: 22px; opacity: .85; }
""", f"""<div class="piz" data-theme="claro">
  <h2>El <span class="s">Yopal</span></h2>
  <p>Galletas artesanas<br><span class="s">&amp; coffee</span></p>
  <div class="row2">{galleta(90)}{galleta(70)}</div>
  <p>¡Para llevar! <small>→</small></p>
  <small>hoy: Lotus recién hecha</small>
</div>""", """# Pizarra

La pizarra de caballete que está en la puerta del kiosco, pasada a reglas para que siempre parezca de la misma marca.

## En la pizarra real
- Tiza blanca para el texto y tiza amarilla (`sol`) para una palabra clave por línea.
- El nombre arriba con un solecito dibujado; dibujos de galletas sencillos, redondos y con pepitas.
- Cuatro líneas como mucho. Una novedad del día abajo en letra pequeña.

## En digital
Fondo `pizarra`, marco de madera, texto en el estilo `mano` color `crema`, palabras clave en `sol`. Úsala para historias de «hoy tenemos…» y para avisos rápidos.
""")

for name, (marker, style, body, readme) in C.items():
    d = os.path.join(OUT, "components", name)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "preview.html"), "w").write(doc(marker, f"{name} — El Yopal", style, body))
    open(os.path.join(d, "README.md"), "w").write(readme)
print("componentes:", ", ".join(C))
