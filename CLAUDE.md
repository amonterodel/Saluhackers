# Saluhackers · repositorio de contexto de marca

Fuente de verdad de marca, voz y diseño de Saluhackers, escuela online de IA para profesionales sanitarios. Lo consumen personas y agentes (Claude Code, Claude Design) para producir carruseles de LinkedIn, herramientas web y otras piezas. Notion es la fuente de verdad de negocio: ningún dato de negocio entra aquí.

No hay código que compilar ni tests que ejecutar. El «producto» son documentos de marca y las piezas que se derivan de ellos.

## Qué hay y qué manda sobre qué

- `DESIGN.md` — sistema de diseño en el formato DESIGN.md de Google (bloque YAML de tokens más prosa). Reglas visuales y cómo aplicar los valores.
- `marca/tokens.css` — todos los valores: color, tipografía, espaciado, radios, bordes, sombras, degradados. Manda sobre el YAML de `DESIGN.md`.
- `marca/voz.md` — reglas duras, tono, léxico prohibido, frases ancla, quién firma qué y ejemplos. Único lugar donde vive la voz.
- `marca/contexto.md` — qué es Saluhackers, público objetivo y territorio de marca (misión, visión, valores, territorios temáticos).
- `DECISIONES.md` — tabla de decisiones abiertas y cerradas.
- `CHANGELOG.md` — fecha, qué cambió, por qué.
- `piezas/carruseles/` — carruseles de LinkedIn publicados (PDF).
- `_origen/` y cualquier `PRIVADO_*` — ignorados por git. No los subas ni los cites.

## Antes de producir una pieza

1. Lee `marca/voz.md` entero y las secciones Overview, Colors, Typography y Do's and Don'ts de `DESIGN.md`.
2. Toma los valores de `marca/tokens.css` (variables `--*` y clases `.sh-grad`, `.sh-grad-bright`, `.sh-grain`), no de memoria.
3. Para un carrusel de LinkedIn: 1080×1350 px, una página por diapositiva, sección «LinkedIn Carousels» de `DESIGN.md`. Guárdalo en `piezas/carruseles/`.
4. Si necesitas un dato que no está en el repositorio (una cifra, un nombre, un precio, una fecha), no lo inventes: pregunta o deja `[PENDIENTE]`.
5. Repasa la pieza contra el léxico prohibido de `marca/voz.md` antes de darla por terminada.

## Comandos

- Validar `DESIGN.md`: `npx @google/design.md lint DESIGN.md`. Debe dar 0 errores. Avisos esperados y aceptados: `orphaned-tokens` (la paleta se declara completa), `token-like-ignored` en `borders` y `motion` (grupos propios), `contrast-ratio` en `button-primary` (decisión abierta en `DECISIONES.md`) y en `button-ghost` (falso positivo: el fondo es transparente).
- Comprobar `marca/tokens.css` tras editarlo (requiere `pip install tinycss2`):
  `python3 -c "import tinycss2;r=tinycss2.parse_stylesheet(open('marca/tokens.css').read());print([x.message for x in r if x.type=='error'])"` debe imprimir `[]`.
- Recuento de variables: `grep -oE -- '--[a-z0-9-]+:' marca/tokens.css | sort -u | wc -l` debe dar 102 mientras no se añadan tokens.

## Convenciones de edición

- Castellano de España, norma RAE, sin anglicismos que tengan equivalente castellano. Excepción: los encabezados `##` de `DESIGN.md` quedan en inglés (Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts, en ese orden) porque el validador los reconoce por nombre.
- Sin guiones largos en ningún texto de marca (regla dura 7 de `marca/voz.md`). Guion corto o paréntesis.
- Traslado literal: al mover texto de marca entre archivos no se reformula, no se resume, no se «mejora».
- Un cambio de valor de diseño se hace primero en `marca/tokens.css`, después en el YAML de `DESIGN.md`, y se pasa el lint. Los dos archivos deben coincidir hexadecimal a hexadecimal y nombre a nombre.
- Nada marcado `[PENDIENTE]` se convierte en decisión por tu cuenta: se registra en `DECISIONES.md` y se pregunta.
- Toda decisión nueva es una fila en `DECISIONES.md` (Decisión · Estado · Fecha · Quién decide). Por defecto: estado «Abierta», decide «Los cuatro fundadores».
- Todo cambio relevante es una fila en `CHANGELOG.md` (Fecha · Qué cambió · Por qué), en el mismo commit que el cambio.
- No crees archivos ni carpetas fuera de la estructura descrita en `README.md` sin que lo pida el usuario.

## Marcas dentro de los documentos

- `[PENDIENTE]` decisión no cerrada por el equipo. Si la necesitas, pregunta antes de asumir.
- `[SIN VERIFICAR]` cifra o afirmación que nadie ha confirmado. No la uses en copy público.
- `[VERIFICADO]` cifra o afirmación validada. Se puede usar citando la fuente original.
- Si detectas una contradicción entre documentos, señálala en vez de resolverla por tu cuenta.

## Flujo de trabajo

- Rama por tarea desde `main`. Mensaje de commit en castellano, imperativo, una línea de asunto (ejemplo: «Consolida la voz de marca en marca/voz.md»).
- PR en borrador con qué cambió y por qué.
- Si trasladaste texto, verifica con `diff` contra el origen antes de commitear. Si tocaste `DESIGN.md` o `tokens.css`, ejecuta los comandos de arriba.

## Advertencias

- Los documentos de origen (Brand Reference en inglés y Contexto Maestro) no están en el árbol. Contienen comisiones, cifras y nombres de embajadores: no los traigas de vuelta ni cites esos datos. Existen en `_origen/` solo en local (no aparecen al clonar) y en el historial de git (`git show fa6cef9:docs/contexto-maestro.md`).
- Hay tres nombres de marca en circulación (Saluhackers, Ágora Saluhackers, AgorIA/Academia) y la decisión está abierta. Usa «Saluhackers» y no cierres el naming por tu cuenta.
- La palabra «hacker» no se sustituye por sinónimos (arquitecto, experto, pionero, ninja). Es identidad, no estilo.
- Los verdes brillantes (`green-term`, `green-glow`) nunca van en titulares. El rojo nunca identifica un nivel de curso.
- Los tamaños tipográficos web de `DESIGN.md` marcados `[PENDIENTE]` son una propuesta, no un dato. Los únicos tamaños afirmados por los originales son los de componentes (badge 11px, campo 15px, etiqueta 12px, tag 11px) y los de presentaciones.
- El botón primario (blanco sobre `#C2683E`) da 3.93:1 de contraste, por debajo de WCAG AA. Es una decisión abierta: no cambies el valor por tu cuenta.
- Anton solo se carga en peso 400 y sus glifos desbordan con interlineado inferior a 1.0.
- El equipo son cuatro fundadores (Alfredo, Yared, Gonzalo, Vicente). El Brand Reference original listaba tres; la referencia válida es «Quién firma qué» en `marca/voz.md`.
- La frase ancla canónica es «reilusionarse con la profesión». Las variantes «reenamorarse» y «re-enamorarse» de los originales están retiradas.
