# Saluhackers · repositorio de contexto de marca

Fuente de verdad de marca, voz y diseño de Saluhackers, escuela online de IA para profesionales sanitarios. Lo consumen personas y agentes (Claude Code, Claude Design) para producir carruseles de LinkedIn, herramientas web y otras piezas. Notion es la fuente de verdad de negocio: ningún dato de negocio entra aquí.

No hay código que compilar ni tests que ejecutar. El «producto» son documentos de marca y las piezas que se derivan de ellos. Este archivo es el mapa definitivo del repositorio: `README.md` no lo repite, remite aquí.

## Mapa del repositorio y qué manda sobre qué

```
CLAUDE.md              Este archivo. Mapa definitivo, reglas de trabajo y gobierno
README.md              Presentación para personas. Remite aquí; no duplica el mapa
DESIGN.md              Sistema de diseño en el formato DESIGN.md de Google: YAML de tokens más prosa
DECISIONES.md          Decisiones abiertas y cerradas (Decisión · Estado · Fecha · Quién decide)
CHANGELOG.md           Historial de cambios (Fecha · Qué cambió · Por qué)
marca/
  contexto.md          Qué es Saluhackers, público objetivo, territorio (misión, visión, valores, territorios)
  voz.md               Voz: reglas duras, tono, léxico prohibido, frases ancla, quién firma qué, ejemplos
  tokens.css           Todos los valores de diseño. Manda sobre el YAML de DESIGN.md
piezas/
  carruseles/          Carruseles de LinkedIn publicados (PDF)
_origen/               Documentos de origen. Ignorada por git, solo existe en local
PRIVADO_*              Cualquier archivo con ese prefijo queda fuera de git
```

- **Valores de diseño** (color, tipografía, espaciado, radios, bordes, sombras, degradados): `marca/tokens.css`. El YAML de `DESIGN.md` los refleja; un cambio se hace primero en el CSS y después se sincroniza el YAML.
- **Reglas visuales y cómo aplicar los valores**: `DESIGN.md`.
- **Voz y tono**: `marca/voz.md`. Único lugar donde vive la voz.
- **Posicionamiento, público y territorio**: `marca/contexto.md`.
- **Estado de lo no decidido**: `DECISIONES.md`. Este archivo no repite decisiones; las enlaza.

## Gobierno: qué hacer cuando algo cambia

- **Se decide algo** (un valor, un nombre, un criterio, una excepción): fila nueva en `DECISIONES.md`. Por defecto estado «Abierta» y decide «Los cuatro fundadores». Solo el usuario cierra una decisión.
- **Cambia algo importante** (estructura de carpetas, qué archivo manda sobre qué, un comando, una convención, una fuente de verdad): se actualiza este archivo en el mismo commit, y `README.md` solo si cambia la presentación del repositorio.
- **Cualquier cambio relevante**: fila en `CHANGELOG.md` en el mismo commit.
- **Siempre se avisa al usuario.** El informe final de cada sesión lista, explícitamente: decisiones añadidas o cerradas, filas de `CHANGELOG.md`, y si se tocó `CLAUDE.md` o `README.md` y por qué. No se cierra una sesión con cambios de gobierno sin decirlo.
- Nada marcado `[PENDIENTE]` se convierte en decisión por cuenta del agente: se registra y se pregunta.
- No se crean archivos ni carpetas fuera del mapa de arriba sin que lo pida el usuario.

## Antes de producir una pieza

1. Lee `marca/voz.md` entero y las secciones Overview, Colors, Typography y Do's and Don'ts de `DESIGN.md`.
2. Toma los valores de `marca/tokens.css` (variables `--*` y clases `.sh-grad`, `.sh-grad-bright`, `.sh-grain`), no de memoria.
3. Para un carrusel de LinkedIn: 1080×1350 px, una página por diapositiva, sección «LinkedIn Carousels» de `DESIGN.md`. Guárdalo en `piezas/carruseles/`.
4. Si necesitas un dato que no está en el repositorio (una cifra, un nombre, un precio, una fecha), no lo inventes: pregunta o deja `[PENDIENTE]`.
5. Repasa la pieza contra el léxico prohibido de `marca/voz.md` antes de darla por terminada.

## Comandos

- Validar `DESIGN.md`: `npx @google/design.md lint DESIGN.md`. Debe dar 0 errores. Avisos aceptados: `orphaned-tokens` (la paleta se declara completa), `token-like-ignored` en `borders` y `motion` (grupos propios), `contrast-ratio` en `button-primary` (decisión abierta) y en `button-ghost` (falso positivo: fondo transparente).
- Comprobar `marca/tokens.css` tras editarlo (requiere `pip install tinycss2`):
  `python3 -c "import tinycss2;r=tinycss2.parse_stylesheet(open('marca/tokens.css').read());print([x.message for x in r if x.type=='error'])"` debe imprimir `[]`.
- Recuento de variables: `grep -oE -- '--[a-z0-9-]+:' marca/tokens.css | sort -u | wc -l` debe dar 102 mientras no se añadan tokens.

## Convenciones de edición

- Castellano de España, norma RAE, sin anglicismos que tengan equivalente castellano. Excepción: los encabezados `##` de `DESIGN.md` quedan en inglés (Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts, en ese orden) porque el validador los reconoce por nombre.
- Sin guiones largos en ningún texto de marca (regla dura 7 de `marca/voz.md`). Guion corto o paréntesis.
- Traslado literal: al mover texto de marca entre archivos no se reformula, no se resume, no se «mejora».
- Un mismo contenido vive en un solo archivo. Si dos archivos necesitan lo mismo, uno lo contiene y el otro remite («ver marca/voz.md»).
- Un cambio de valor de diseño: primero `marca/tokens.css`, después el YAML de `DESIGN.md`, después el lint. Los dos deben coincidir hexadecimal a hexadecimal y nombre a nombre.

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
- El nombre público de la marca es una decisión abierta. Usa «Saluhackers» y no cierres el naming por tu cuenta.
- La palabra «hacker» no se sustituye por sinónimos (arquitecto, experto, pionero, ninja). Es identidad, no estilo.
- Los verdes brillantes (`green-term`, `green-glow`) nunca van en titulares. El rojo nunca identifica un nivel de curso.
- Los tamaños tipográficos web de `DESIGN.md` marcados `[PENDIENTE]` son una propuesta, no un dato (decisión abierta). Los únicos tamaños afirmados por los originales son los de componentes y presentaciones.
- El contraste del botón primario es una decisión abierta: no cambies el valor por tu cuenta.
- Anton solo se carga en peso 400 y sus glifos desbordan con interlineado inferior a 1.0.
- El equipo son cuatro fundadores (Alfredo, Yared, Gonzalo, Vicente). El Brand Reference original listaba tres; la referencia válida es «Quién firma qué» en `marca/voz.md`.
- La frase ancla canónica es «reilusionarse con la profesión». Las variantes «reenamorarse» y «re-enamorarse» de los originales están retiradas.
