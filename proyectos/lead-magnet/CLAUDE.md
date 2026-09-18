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

## Imágenes

En `assets/` viven los originales. Los nombres de las dos primeras los fija `contenido.md`, que las enlaza por ruta: no se renombran, porque ese texto es final.

| Archivo | Qué es | Dónde va |
|---|---|---|
| `fuentes-antes.png` | Lista de fuentes con nombres de descarga, el cuaderno sin arquitecturar | Elemento antes/después, enlazada desde `contenido.md` |
| `fuentes-despues.png` | La misma lista con nomenclatura, el cuaderno arquitecturado | Elemento antes/después, enlazada desde `contenido.md` |
| `escena-archivo.webp` | Archivo en penumbra: estanterías desordenadas a un lado, archivadores rotulados al otro | Escena de la primera pantalla, a la que vuelve la lista de verificación |
| `respuesta-no-hacker.png` | Respuesta del cuaderno citando la recomendación de 2019 | Simulación de cita y comparador usuario / hacker |
| `respuesta-hacker.png` | Respuesta del cuaderno citando la guía de 2025 | Simulación de cita y comparador usuario / hacker |

Reglas:

- **Todas se incrustan como `data:` URI.** La pieza es un archivo único y no puede pedir imágenes al servidor.
- **Optimiza antes de incrustar.** En crudo pesan 715 KB, que en base64 son 950 KB, y las dos capturas de respuesta son 775 KB de ese total. Son capturas de texto de unos 1400 px de ancho: convertidas a WebP y ajustadas al ancho al que se ven, el archivo final baja de forma drástica. Los originales se quedan aquí sin tocar.
- **Cada imagen necesita su texto alternativo**, y el de las dos enlazadas ya lo escribe `contenido.md`.

## Antes de escribir copy

Lee `marca/voz.md` entero. El titular, la entradilla y la llamada a la acción se repasan contra su léxico prohibido antes de dar la pieza por terminada. Ninguna cifra entra sin fuente: se marca `[SIN VERIFICAR]` o se pregunta. Los datos de negocio (precios, conversión, embajadores) no entran aquí: viven en Notion.

## Estructura de una pieza

El ritmo de marca es kicker mono, titular condensado en mayúsculas y cuerpo. Se alternan las dos únicas superficies: blanca por defecto y terminal oscura para los momentos de código o impacto. `plantilla.html` ya lo trae montado; las reglas completas están en `DESIGN.md`.
