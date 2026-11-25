"""Aplica la revisión hecha con la skill brand-identity al sistema de El Yopal."""
import json, re, sys
S = sys.argv[1]; P = S + "/ds/project"

def sub(path, pairs, must=True):
    s = open(path).read()
    for a, b in pairs:
        if must: assert a in s, (path, a[:60])
        s = s.replace(a, b)
    open(path, "w").write(s)

# 1. Tokens: Sansita para titulares y precios, Figtree para rótulos, sin el color galleta
t = json.load(open(P + "/tokens.json"))
t["color"]["tokens"] = [x for x in t["color"]["tokens"] if x["name"] != "galleta"]
for x in t["color"]["tokens"]:
    if x["name"] == "crema":
        x["usage"] = ("Color de marca fijo: logotipo y titulares sobre `granate`, fondo de posts claros. No cambia con el tema. "
                      "Es el crema de los referentes de la marca y de la celosía del kiosco; se usa con granate, nunca con acentos dorados o terracota.")
    if x["name"] == "sol":
        x["usage"] = ("El Solete, precios y ofertas. Fondo de acento; texto encima siempre en `granate-hondo` (9,9:1). "
                      "Nunca sobre `crema` (1,4:1) ni sobre kraft (1,6:1): ahí, `granate`.")
fam = t["type"]["families"]
fam["display"] = "Sansita, \"Arial Black\", system-ui, sans-serif"
fam["rotulo"] = "Figtree, system-ui, -apple-system, \"Segoe UI\", sans-serif"
for g in t["type"]["groups"]:
    if g["family"] == "display":
        for st in g["styles"]: st["fontWeight"] = 900
    if g["family"] == "rotulo":
        for st in g["styles"]:
            st["fontWeight"] = 700; st["letterSpacing"] = "0.1em"
            st["fontSize"] = {"rotulo-l": "24px", "rotulo": "13px"}.get(st["name"], st["fontSize"])
json.dump(t, open(P + "/tokens.json", "w"), ensure_ascii=False, indent=2)

# 2. Hoja de estilos compartida
sub(P + "/components/bundle.css", [
    ('@import url("https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT@9..144,600..900,0..100&family=Barlow+Condensed:wght@600;700&family=Caveat+Brush&family=Figtree:wght@400;500;700;800&display=swap");',
     '@import url("https://fonts.googleapis.com/css2?family=Sansita:wght@800;900&family=Figtree:wght@400;500;700;800&family=Caveat+Brush&display=swap");'),
    ('\n/* Fraunces con las puntas suavizadas en toda la marca (las demás fuentes ignoran este eje) */\nhtml, body, * { font-variation-settings: "SOFT" 100, "WONK" 0; font-optical-sizing: auto; }\n', '\n'),
    ("font-family: var(--font-rotulo); font-weight: 700; font-size: 17px; letter-spacing: .08em;", "font-family: var(--font-rotulo); font-weight: 700; font-size: 15px; letter-spacing: .1em;"),
])

# 3. Portada del sistema: sin el color galleta
sub(P + "/components/Cover/preview.html", [(".galleta { fill: var(--galleta); }", ".galleta { fill: var(--azul); }")])

# 4. Plantillas: ilustraciones a mano en lugar de los iconos de trazo genérico
p = S + "/scripts/make_components.py"
s = open(p).read()
nuevos = {"il_lata": "33e2af8433fe8637ff440a5a0310f621", "il_bolsa": "1bd876c1954dd27c9b8bb2e762fc7b96", "il_galleta": "952e2974f0b367a4a3b6d472a702736c",
          "il_revistas": "70566e9f9b54df9f604d2c8802e05c71", "il_vaso": "7ee960d9064343daff9dba977d9cb542", "icono": "8f9d418b4718c59eec589a254b3cd9ed"}
for k, v in nuevos.items():
    if f'"{k}":' not in s: s = s.replace("B = {\n", f'B = {{\n "{k}": "{v}",\n', 1)
for a, b in [("combo('i_bebida','Bebida')", "combo('il_lata','Bebida')"), ("combo('i_snack','Snack')", "combo('il_bolsa','Snack')"),
             ("combo('i_galleta','Dulce')", "combo('il_galleta','Dulce')"),
             ("""<img src="{u(icon)}" alt="" style="width:110px">""", """<img src="{u(icon)}" alt="" style="width:170px">"""),
             ("""<img src="{u('i_revista')}" alt="" style="position:absolute;left:96px;top:620px;width:120px">""",
              """<img src="{u('il_revistas')}" alt="" style="position:absolute;left:80px;top:600px;width:220px">"""),
             ("""<img src="{u('i_llevar')}" alt="" style="width:230px">""", """<img src="{u('il_vaso')}" alt="" style="width:300px">"""),
             ("""<span class="yp-tag yp-tag--sol" style="font-size:32px;padding:12px 28px"><img src="{u('i_ubicacion')}" alt="" style="width:34px">Te esperamos</span>""",
              """<span class="yp-tag yp-tag--sol" style="font-size:32px;padding:12px 28px">Te esperamos</span>""")]:
    assert a in s, a[:60]; s = s.replace(a, b)
open(p, "w").write(s)
print("ok")
