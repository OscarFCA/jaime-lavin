# Jaime Lavín — Arquitectura para la vida

Sitio de la marca personal de Jaime Lavín, en GitHub Pages.

- **En vivo:** https://oscarfca.github.io/jaime-lavin/
- **Estado:** borrador de trabajo, no aprobado por Jaime. Lleva `noindex` y `robots.txt` con `Disallow: /`.
- **Fuentes:** `Hel3na/documentos/JaimeLavinPagina personal/` — `uploads/DesignJaimeLavin.md`
  (marca), `uploads/content (1).md` (sitemap y copy) y `Home Jaime Lavin.dc.html` (canvas de la home).

## Cómo se construye

HTML estático, sin framework ni runtime. El header, el nav, el footer y el `<head>` viven
una sola vez en `src/shell.html`; cada página es un fragmento en `src/pages/*.html` con un
bloque `<!--meta -->` que define su URL, título, descripción y el enlace activo del menú.

```
python3 build.py     # regenera las 16 páginas a partir de src/
```

Las rutas dentro de los fragmentos usan `{{B}}` como prefijo a la raíz del sitio; el
generador lo sustituye por el `../` que corresponda a la profundidad de cada URL, para que
el sitio funcione bajo el subdirectorio `/jaime-lavin/` de Pages.

Diseño en `assets/styles.css`: tokens de `DesignJaimeLavin.md` §5 (carbón, piedra, tierra,
marfil — **sin dorado**, ese acento es de Lazza), Instrument Sans + Fraunces, y la capa
responsiva en 1024 / 860 / 600 / 480 / 345 px.

## Páginas

| URL | Qué es |
|---|---|
| `/` | Home: hero, audiencias, territorio, terrenos, manifiestos, conversaciones y contacto |
| `/sobre-mi/` | Trayectoria desde 1997, historias, cómo trabaja |
| `/para-ti/` | Hub de los cuatro momentos de decisión |
| `/para-ti/familia/` `/descanso/` `/nueva-etapa/` `/extranjero/` | Landing por momento, con formulario y mapa |
| `/manifiestos/` | Las cuatro tesis |
| `/terrenos/` | Mapa, fichas y las decisiones pendientes de la página |
| `/conversaciones/` + `/gracias/` | Registro al encuentro mensual |
| `/guia/` + `/gracias/` | Lead magnet (propuesta sin confirmar) |
| `/contacto/` + `/gracias/` | Única página de contacto, con triage |
| `/contacto/enlaces/` | Página de enlaces tipo Linktree, para la bio de redes (`/links/` redirige aquí) |
| `/404.html` | Error |

## Pendientes de contenido

- **Fotografía real** (Jaime, vida, espacio, materia): hoy son placeholders de marca.
- **Banco real de terrenos** con fotos, superficie y estatus; y si se muestra precio y con
  qué precisión la ubicación.
- **Formularios sin conectar**: falta decidir a dónde llegan los mensajes y quién responde.
- **Selector de mapa con pin** en los formularios: sigue siendo maqueta estática. El mapa
  general (home y `/terrenos/`) ya es un prototipo real con Leaflet + OpenStreetMap
  (`assets/mapa.js`, se carga solo en las páginas con `mapa: si` en su meta); sus pines
  son de ejemplo hasta tener el banco real de terrenos.
- **Entrevista de tesis, voz e historias** con Jaime: las historias de `/sobre-mi/` y el
  texto largo de `/manifiestos/` están reservados, no redactados a su nombre.
- Nav del canvas vs. nav de `content.md`, y cuál es el hero definitivo (§9 y §12 de
  `DesignJaimeLavin.md`).
