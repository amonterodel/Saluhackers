# Saluhackers · repositorio de contexto de marca

Fuente de verdad de marca, voz y diseño de Saluhackers, escuela online de IA para profesionales sanitarios. Lo consumen personas y agentes (Claude Code, Claude Design) para producir carruseles de LinkedIn, herramientas web y otras piezas. Notion es la fuente de verdad de negocio: ningún dato de negocio entra aquí.

No hay código que compilar ni tests que ejecutar. El «producto» son documentos de marca y las piezas que se derivan de ellos. Este archivo es el mapa definitivo del repositorio: `README.md` orienta a las personas y remite aquí.

## Mapa del repositorio y qué manda sobre qué

```
CLAUDE.md              Este archivo. Mapa definitivo, reglas de trabajo y gobierno
README.md              Orientación para personas: qué es, primer día, cómo se trabaja. No duplica el mapa
DESIGN.md              Sistema de diseño en el formato DESIGN.md de Google: YAML de tokens más prosa
DECISIONES.md          Decisiones con ID D-NNN, en dos tablas: abiertas y cerradas
CHANGELOG.md           Historial de cambios en lista por fecha, lo más reciente arriba
marca/
  contexto.md          Qué es Saluhackers, público objetivo, territorio (misión, visión, valores, territorios)
  voz.md               Voz: reglas duras, tono, léxico prohibido, frases ancla, quién firma qué, ejemplos
  tokens.css           Todos los valores de diseño. Manda sobre el YAML de DESIGN.md
activos/               Activos visuales persistentes de la marca: logotipo, marca de agua, plantillas
inspiracion/           Referencias visuales externas en las que se basa el estilo (capturas, PDF, pósteres)
piezas/
  carruseles/          Carruseles de LinkedIn publicados (PDF). Otros tipos: piezas/<tipo>/ cuando existan
bitacora/
  PLANTILLA.md         Plantilla de entrada de sesión
  AAAA-MM-DD-tema.md   Una entrada por sesión de trabajo
_origen/               Documentos de origen. Ignorada por git, solo existe en local
PRIVADO_*              Cualquier archivo con ese prefijo queda fuera de git
```

- **Valores de diseño** (color, tipografía, espaciado, radios, bordes, sombras, degradados): `marca/tokens.css`. El YAML de `DESIGN.md` los refleja; un cambio se hace primero en el CSS y después se sincroniza el YAML (D-004).
- **Reglas visuales y cómo aplicar los valores**: `DESIGN.md`.
- **Voz y tono**: `marca/voz.md`. Único lugar donde vive la voz.
- **Posicionamiento, público y territorio**: `marca/contexto.md`.
- **Estado de lo no decidido**: `DECISIONES.md`. Este archivo no repite decisiones; las cita por ID.
- **Activos frente a inspiración frente a piezas**: `activos/` es lo nuestro y reutilizable; `inspiracion/` es ajeno y solo referencia; `piezas/` es lo nuestro ya publicado, que sirve de ejemplo. Nombres de archivo en minúsculas, con guiones, sin espacios ni acentos, y con el contenido reconocible en el nombre (`logo-saluhackers-horizontal.svg`, `visualize-value-carrusel-minimal.png`).

## Gobierno: qué hacer cuando algo cambia

- **Se decide algo** (un valor, un nombre, un criterio, una excepción): fila nueva en la tabla de abiertas de `DECISIONES.md` con el siguiente `D-NNN` libre. Por defecto decide «Los cuatro fundadores». Solo el usuario cierra una decisión: entonces se mueve a la tabla de cerradas con fecha y nombre. Nunca se borra una fila ni se reutiliza un ID.
- **Cambia algo importante** (estructura de carpetas, qué archivo manda sobre qué, un comando, una convención, una fuente de verdad): se actualiza este archivo en el mismo commit, y `README.md` solo si cambia lo que una persona necesita saber al aterrizar.
- **Cualquier cambio relevante**: viñeta en `CHANGELOG.md`, bajo la fecha de hoy (crear el encabezado `## AAAA-MM-DD` si no existe, arriba del todo), con qué cambió, por qué, y el PR y las `D-NNN` relacionadas.
- **Al cerrar la sesión**: crear `bitacora/AAAA-MM-DD-tema.md` copiando `bitacora/PLANTILLA.md` y rellenando todos sus apartados, y repetir en el mensaje final al usuario las decisiones añadidas o cerradas, las viñetas de `CHANGELOG.md` y si se tocó `CLAUDE.md` o `README.md` y por qué. Una sesión sin entrada de bitácora no está cerrada.
- Nada marcado `[PENDIENTE]` se convierte en decisión por cuenta del agente: se registra y se pregunta.
- No se crean archivos ni carpetas fuera del mapa de arriba sin que lo pida el usuario.

## Antes de producir una pieza

1. Lee `marca/voz.md` entero y las secciones Overview, Colors, Typography y Do's and Don'ts de `DESIGN.md`.
2. Toma los valores de `marca/tokens.css` (variables `--*` y clases `.sh-grad`, `.sh-grad-bright`, `.sh-grain`), no de memoria.
3. Usa los archivos de `activos/` para el logotipo y las plantillas; no lo redibujes.
4. Para un carrusel de LinkedIn: 1080×1350 px, una página por diapositiva, sección «LinkedIn Carousels» de `DESIGN.md`. Guárdalo en `piezas/carruseles/`.
5. Si necesitas un dato que no está en el repositorio (una cifra, un nombre, un precio, una fecha), no lo inventes: pregunta o deja `[PENDIENTE]`.
6. Repasa la pieza contra el léxico prohibido de `marca/voz.md` antes de darla por terminada.

## Comandos

- Validar `DESIGN.md`: `npx @google/design.md lint DESIGN.md`. Debe dar 0 errores. Avisos aceptados: `orphaned-tokens` (la paleta se declara completa), `token-like-ignored` en `borders` y `motion` (grupos propios), `contrast-ratio` en `button-primary` (D-007) y en `button-ghost` (falso positivo: fondo transparente).
- Comprobar `marca/tokens.css` tras editarlo (requiere `pip install tinycss2`):
  `python3 -c "import tinycss2;r=tinycss2.parse_stylesheet(open('marca/tokens.css').read());print([x.message for x in r if x.type=='error'])"` debe imprimir `[]`.
- Recuento de variables: `grep -oE -- '--[a-z0-9-]+:' marca/tokens.css | sort -u | wc -l` debe dar 102 mientras no se añadan tokens.

## Convenciones de edición

- Castellano de España, norma RAE, sin anglicismos que tengan equivalente castellano. Excepción: los encabezados `##` de `DESIGN.md` quedan en inglés (Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts, en ese orden) porque el validador los reconoce por nombre.
- Sin guiones largos en ningún texto de marca (regla dura 7 de `marca/voz.md`). Guion corto o paréntesis.
- Traslado literal: al mover texto de marca entre archivos no se reformula, no se resume, no se «mejora». Un traslado se verifica con `diff` contra el origen.
- Un mismo contenido vive en un solo archivo. Si dos archivos necesitan lo mismo, uno lo contiene y el otro remite («ver marca/voz.md»).
- Un cambio de valor de diseño: primero `marca/tokens.css`, después el YAML de `DESIGN.md`, después el lint. Los dos deben coincidir hexadecimal a hexadecimal y nombre a nombre.

## Marcas dentro de los documentos

- `[PENDIENTE]` decisión no cerrada por el equipo. Si la necesitas, pregunta antes de asumir.
- `[SIN VERIFICAR]` cifra o afirmación que nadie ha confirmado. No la uses en copy público.
- `[VERIFICADO]` cifra o afirmación validada. Se puede usar citando la fuente original.
- Si detectas una contradicción entre documentos, señálala en vez de resolverla por tu cuenta.

## Flujo de trabajo

- Rama por tarea desde `main`. Mensaje de commit en castellano, imperativo, una línea de asunto (ejemplo: «Consolida la voz de marca en marca/voz.md»).
- PR en borrador con qué cambió y por qué, citando las `D-NNN` que toca.
- Si tocaste `DESIGN.md` o `tokens.css`, ejecuta los comandos de arriba antes de commitear.

## Advertencias

- Los documentos de origen (Brand Reference en inglés y Contexto Maestro) no están en el árbol. Contienen comisiones, cifras y nombres de embajadores: no los traigas de vuelta ni cites esos datos. Existen en `_origen/` solo en local (no aparecen al clonar) y en el historial de git (`git show fa6cef9:docs/contexto-maestro.md`).
- El nombre público de la marca es D-002, abierta. Usa «Saluhackers» y no cierres el naming por tu cuenta.
- La palabra «hacker» no se sustituye por sinónimos (arquitecto, experto, pionero, ninja). Es identidad, no estilo.
- Los verdes brillantes (`green-term`, `green-glow`) nunca van en titulares. El rojo nunca identifica un nivel de curso.
- Los tamaños tipográficos web de `DESIGN.md` marcados `[PENDIENTE]` son una propuesta, no un dato (D-006). Los únicos tamaños afirmados por los originales son los de componentes y presentaciones.
- El contraste del botón primario es D-007, abierta: no cambies el valor por tu cuenta.
- Anton solo se carga en peso 400 y sus glifos desbordan con interlineado inferior a 1.0.
- El equipo son cuatro fundadores (Alfredo, Yared, Gonzalo, Vicente). El Brand Reference original listaba tres; la referencia válida es «Quién firma qué» en `marca/voz.md`.
- La frase ancla canónica es «reilusionarse con la profesión» (D-003). Las variantes «reenamorarse» y «re-enamorarse» de los originales están retiradas.
- Nada de `inspiracion/` se copia en una pieza: es referencia de estilo, no material reutilizable, y puede tener derechos de terceros.
