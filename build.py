#!/usr/bin/env python3
"""Genera el sitio de Jaime Lavín a partir de src/shell.html + src/pages/*.html.

Cada fragmento de src/pages/ empieza con un bloque de metadatos:

    <!--meta
    out: sobre-mi/index.html
    title: Sobre mí — Jaime Lavín
    desc: ...
    nav: sobre-mi
    -->

`out` define la URL; `nav` marca el enlace activo del menú (vacío = ninguno).
Las rutas dentro del fragmento usan {{B}} como prefijo a la raíz del sitio.
"""
import pathlib, re, shutil, sys

RAIZ = pathlib.Path(__file__).parent
SRC = RAIZ / "src"
NAV = ["inicio", "sobre-mi", "para-ti", "manifiestos", "terrenos", "conversaciones", "contacto"]

shell = (SRC / "shell.html").read_text()
generados = []

for frag in sorted((SRC / "pages").glob("*.html")):
    texto = frag.read_text()
    m = re.match(r"<!--meta\n(.*?)\n-->\n", texto, re.S)
    if not m:
        sys.exit("falta el bloque <!--meta --> en %s" % frag.name)
    meta = dict(
        (k.strip(), v.strip())
        for k, v in (l.split(":", 1) for l in m.group(1).strip().splitlines() if l.strip())
    )
    cuerpo = texto[m.end():]
    salida = RAIZ / meta["out"]
    base = "../" * (len(pathlib.PurePath(meta["out"]).parts) - 1)

    html = shell.replace("{{TITLE}}", meta["title"]).replace("{{DESC}}", meta["desc"])
    html = html.replace("{{BODY}}", cuerpo.strip())
    for clave in NAV:
        activo = ' class="is-active"' if meta.get("nav") == clave else ""
        if clave == "contacto":
            activo = ' class="nav-cta is-active"' if meta.get("nav") == clave else ""
        html = html.replace("{{A_%s}}" % clave, activo)
    html = html.replace('<a class="nav-cta" href="{{B}}contacto/" class="nav-cta is-active"',
                        '<a href="{{B}}contacto/" class="nav-cta is-active"')
    html = html.replace("{{B}}", base)

    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text(html)
    generados.append((meta["out"], len(html)))

for ruta, tam in generados:
    print("  %-34s %6d bytes" % (ruta, tam))
print("%d páginas generadas" % len(generados))
