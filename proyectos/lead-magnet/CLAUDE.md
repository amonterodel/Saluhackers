# Proyecto: lead magnet

Artefacto autocontenido en HTML, CSS y JavaScript que se abre en el navegador sin instalar nada. Es la excepción al «no hay nada que compilar» del `CLAUDE.md` de la raíz: aquí sí se construye algo que se ejecuta. Todo lo demás de la raíz (voz, diseño, gobierno, castellano estricto) sigue vigente.

## Restricciones duras

- **Un solo archivo HTML por pieza.** Todo el CSS y el JavaScript van en línea. Sin frameworks, sin CDN, sin empaquetador, sin dependencias que instalar y sin paso de compilación.
- **La única petición externa permitida es el `@import` de Google Fonts** que ya trae `marca/tokens.css` (D-014). Cualquier otra queda fuera: CDN, analítica, tipografías de otro origen, imágenes remotas.
- **Las imágenes van incrustadas** como `data:` URI, o se resuelven con CSS y SVG en línea. El grano ya viene resuelto así en `.sh-grain`.
- **El bloque entre `/* tokens:inicio */` y `/* tokens:fin */` es una copia generada.** No se edita a mano. Si un valor está mal, se corrige en `marca/tokens.css` y se vuelve a sincronizar (D-004).
- **Aquí no se definen valores nuevos.** Si necesitas un color, un tamaño o un radio que no existe en los tokens, eso es una decisión para `DECISIONES.md`, no una línea de CSS local.

## Comandos

- Sincronizar los tokens con la fuente de verdad:
  `python3 proyectos/sincroniza-tokens.py proyectos/lead-magnet/<archivo>.html`
- Comprobar que no han entrado dependencias externas:
  `grep -nE 'https?://' proyectos/lead-magnet/*.html | grep -v 'w3.org/2000/svg'` debe devolver solo la línea del `@import` de Google Fonts, una por archivo. El filtro descarta el espacio de nombres del SVG que va dentro del `data:` URI del grano, que no es una petición de red.
- Ver el resultado: abrir el archivo en el navegador. No hay servidor ni arranque.

## Antes de escribir copy

Lee `marca/voz.md` entero. El titular, la entradilla y la llamada a la acción se repasan contra su léxico prohibido antes de dar la pieza por terminada. Ninguna cifra entra sin fuente: se marca `[SIN VERIFICAR]` o se pregunta. Los datos de negocio (precios, conversión, embajadores) no entran aquí: viven en Notion.

## Estructura de una pieza

El ritmo de marca es kicker mono, titular condensado en mayúsculas y cuerpo. Se alternan las dos únicas superficies: blanca por defecto y terminal oscura para los momentos de código o impacto. `plantilla.html` ya lo trae montado; las reglas completas están en `DESIGN.md`.
