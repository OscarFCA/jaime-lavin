# Jaime Lavín — Arquitectura para la vida

Home de la marca personal de Jaime Lavín, desplegada en GitHub Pages.

- **En vivo:** https://oscarfca.github.io/jaime-lavin/
- **Fuente:** `Hel3na/documentos/JaimeLavinPagina personal/Home Jaime Lavin.dc.html` (design canvas)
- **Estado:** borrador de trabajo, no aprobado por Jaime. Lleva `noindex` y `robots.txt` con `Disallow: /`.

## Qué es este repo
Copia desplegable del canvas: `index.html` + `support.js` (runtime del formato `.dc.html`) + `assets/`.
`uploads/` y `_ds/` del origen no se despliegan.

Cambios respecto al canvas original:
- `<title>`, meta description, favicon, `noindex`.
- Los `<image-slot>` (sin fotografía aún) se sustituyeron por placeholders de marca.
- Capa responsiva móvil/tablet: media queries con `!important` en el `<helmet>`, apuntadas con
  atributos `data-m="..."` porque `support.js` re-serializa los estilos inline.

## Pendientes de contenido
- Fotografía real (Jaime, vida, espacio, materia) para los cuatro placeholders.
- Banco real de terrenos; hoy las fichas son maqueta.
- Formulario de contacto funcional y datos de contacto/handles confirmados.
- Decisiones abiertas en `DesignJaimeLavin.md` §12 y `content.md` §12.
