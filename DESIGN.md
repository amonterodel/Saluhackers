---
version: alpha
name: Saluhackers
description: "Sistema de diseño de Saluhackers, escuela de IA para profesionales sanitarios. Los valores canónicos viven en marca/tokens.css; este bloque los refleja y no se edita por su cuenta."
colors:
  # Papel: fondos, blanco puro
  paper-100: "#FFFFFF"
  paper-200: "#FFFFFF"
  paper-300: "#F2F1EC"
  paper-400: "#DFDDD4"
  # Tinta: carbón con matiz verde-negro
  ink-900: "#14201A"
  ink-700: "#283330"
  ink-500: "#4A554F"
  ink-300: "#7C857D"
  # Teal: color primario de marca
  teal-900: "#16383A"
  teal-700: "#234E50"
  teal-500: "#357072"
  teal-300: "#6FA0A0"
  teal-100: "#C6DAD8"
  # Verde terminal / salvia: la señal «hacker»
  green-900: "#1C4A2E"
  green-700: "#2E7D4F"
  green-500: "#3FAE6A"
  green-term: "#34D17E"
  green-glow: "#5BF6A6"
  green-100: "#CDE8D6"
  # Terracota / rust: acento cálido
  rust-900: "#7A3A1E"
  rust-700: "#A8552E"
  rust-500: "#C2683E"
  rust-300: "#DC9A72"
  rust-100: "#F0D7C4"
  # Oliva / arena: neutro cálido terciario
  olive-700: "#6E6838"
  olive-500: "#8A8350"
  olive-300: "#BAB385"
  # Violeta: nivel «pros»
  purple-900: "#3D2A66"
  purple-700: "#573D90"
  purple-500: "#7558B4"
  purple-300: "#A793D6"
  purple-100: "#E6DEF4"
  # Roles y semántica (equivalen a --brand, --accent, --bg, --fg… de tokens.css)
  primary: "{colors.teal-700}"
  brand: "{colors.teal-700}"
  brand-strong: "{colors.teal-900}"
  accent: "{colors.rust-500}"
  accent-strong: "{colors.rust-700}"
  signal: "{colors.green-700}"
  signal-bright: "{colors.green-term}"
  bg: "{colors.paper-200}"
  bg-raised: "{colors.paper-100}"
  bg-sunken: "{colors.paper-300}"
  bg-inverse: "{colors.ink-900}"
  fg: "{colors.ink-900}"
  fg-soft: "{colors.ink-700}"
  fg-muted: "{colors.ink-500}"
  fg-faint: "{colors.ink-300}"
  fg-on-dark: "{colors.paper-100}"
  fg-on-accent: "{colors.paper-100}"
  border: "{colors.paper-400}"
  border-strong: "{colors.ink-300}"
  border-ink: "{colors.ink-900}"
  success: "{colors.green-700}"
  warning: "{colors.rust-500}"
  danger: "#B23A33"
  info: "{colors.teal-500}"
  level-init: "{colors.green-500}"
  level-amateur: "{colors.teal-500}"
  level-pro: "{colors.purple-500}"
typography:
  # Familia, peso, tracking e interlineado salen de los originales.
  # Todo valor marcado [PENDIENTE] es una propuesta de mapeo sobre la escala existente (--text-*, --leading-*), no un dato del original. Ver DECISIONES.md.
  display:
    fontFamily: Anton
    fontSize: 5.5rem # [PENDIENTE] --text-5xl
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -0.01em
  h1:
    fontFamily: Anton
    fontSize: 4rem # [PENDIENTE] --text-4xl
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -0.01em
  h2:
    fontFamily: Oswald
    fontSize: 3rem # [PENDIENTE] --text-3xl
    fontWeight: 600 # [PENDIENTE]
    lineHeight: 1.25 # [PENDIENTE] --leading-snug
  h3:
    fontFamily: Oswald
    fontSize: 2.25rem # [PENDIENTE] --text-2xl
    fontWeight: 600 # [PENDIENTE]
    lineHeight: 1.25 # [PENDIENTE] --leading-snug
  lead:
    fontFamily: Barlow
    fontSize: 1.375rem # [PENDIENTE] --text-lg
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: Barlow
    fontSize: 1rem # [PENDIENTE] --text-base
    fontWeight: 400
    lineHeight: 1.55
  small:
    fontFamily: Barlow
    fontSize: 0.875rem # [PENDIENTE] --text-sm
    fontWeight: 400
    lineHeight: 1.55
  kicker:
    fontFamily: Space Mono
    fontSize: 0.75rem # [PENDIENTE] --text-xs
    fontWeight: 400
    letterSpacing: 0.22em
  label:
    fontFamily: Oswald
    fontSize: 0.75rem # [PENDIENTE] --text-xs
    fontWeight: 600 # [PENDIENTE]
    letterSpacing: 0.06em
  mono:
    fontFamily: Space Mono
    fontSize: 0.875rem # [PENDIENTE] --text-sm
    fontWeight: 400
    lineHeight: 1.55
  # Niveles con valores explícitos en los originales (componentes y presentaciones)
  button:
    fontFamily: Oswald
    fontWeight: 600
    letterSpacing: 0.06em
  badge:
    fontFamily: Space Mono
    fontSize: 11px
    fontWeight: 700
    letterSpacing: 0.1em
  input:
    fontFamily: Barlow
    fontSize: 15px
  input-label:
    fontFamily: Oswald
    fontSize: 12px
  tag:
    fontFamily: Space Mono
    fontSize: 11px
  deck-kicker:
    fontFamily: Space Mono
    fontSize: 26px
    letterSpacing: 0.22em
  deck-footer:
    fontFamily: Space Mono
    fontSize: 20px
  deck-data:
    fontSize: 200px
rounded:
  xs: 2px
  sm: 4px
  md: 6px
  lg: 10px
  pill: 999px
spacing:
  base: 4px
  sp-1: 4px
  sp-2: 8px
  sp-3: 12px
  sp-4: 16px
  sp-5: 24px
  sp-6: 32px
  sp-7: 48px
  sp-8: 64px
  sp-9: 96px
  sp-10: 128px
components:
  button-primary:
    backgroundColor: "{colors.rust-500}"
    textColor: "{colors.fg-on-accent}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
  button-primary-hover:
    backgroundColor: "{colors.rust-700}"
  button-brand:
    backgroundColor: "{colors.teal-700}"
    textColor: "{colors.fg-on-accent}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
  button-brand-hover:
    backgroundColor: "{colors.teal-900}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink-900}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
  button-ghost-hover:
    backgroundColor: "rgba(20,32,26,0.06)"
  button-term:
    backgroundColor: "{colors.ink-900}"
    textColor: "{colors.green-term}"
    typography: "{typography.mono}"
    rounded: "{rounded.sm}"
  button-disabled:
    textColor: "{colors.ink-300}"
  badge-level-init:
    backgroundColor: "{colors.green-100}"
    textColor: "{colors.green-900}"
    typography: "{typography.badge}"
    rounded: "{rounded.pill}"
  badge-level-amateur:
    backgroundColor: "{colors.teal-100}"
    textColor: "{colors.teal-900}"
    typography: "{typography.badge}"
    rounded: "{rounded.pill}"
  badge-level-pro:
    backgroundColor: "{colors.purple-100}"
    textColor: "{colors.purple-900}"
    typography: "{typography.badge}"
    rounded: "{rounded.pill}"
  badge-on-dark:
    backgroundColor: "rgba(0,0,0,0.28)"
    textColor: "{colors.paper-100}"
    typography: "{typography.badge}"
    rounded: "{rounded.pill}"
  course-card:
    backgroundColor: "{colors.paper-100}"
    textColor: "{colors.ink-900}"
    rounded: "{rounded.md}"
  course-card-header:
    backgroundColor: "{colors.teal-700}"
  input:
    backgroundColor: "{colors.paper-100}"
    typography: "{typography.input}"
    rounded: "{rounded.sm}"
  input-label:
    typography: "{typography.input-label}"
  terminal-panel:
    backgroundColor: "{colors.ink-900}"
    textColor: "{colors.green-term}"
    typography: "{typography.mono}"
  tag:
    typography: "{typography.tag}"
    rounded: "{rounded.sm}"
# Grupos propios de Saluhackers (el estándar los acepta como extensión; su CLI no los exporta)
borders:
  hairline: 1.5px
  thick: 2.5px
shadows:
  sm: "0 1px 2px rgba(20,32,26,.10)"
  md: "0 2px 6px rgba(20,32,26,.12), 0 1px 2px rgba(20,32,26,.10)"
  lg: "0 8px 24px rgba(20,32,26,.16)"
  stamp: "3px 3px 0 #14201A"
  glow-term: "0 0 0 1px rgba(52,209,126,.5), 0 0 14px rgba(52,209,126,.45)"
gradients:
  headline: "linear-gradient(45deg, #357072 0%, #234E50 38%, #2E7D4F 100%)"
  headline-bright: "linear-gradient(45deg, #6FA0A0 0%, #357072 45%, #3FAE6A 100%)"
motion:
  duration-min: 120ms
  duration-max: 200ms
  easing: ease-out
---

# Saluhackers · DESIGN.md

Sistema de diseño de Saluhackers en el formato DESIGN.md. Los valores del bloque YAML se copian de `marca/tokens.css`, que es la fuente de verdad; la prosa explica cómo aplicarlos. La voz y el tono no viven aquí: ver `marca/voz.md`.

## Overview

Escuela online de IA exclusivamente para profesionales sanitarios. La marca habla como un colega sanitario, no como un proveedor tecnológico, y su promesa es recuperar tiempo para lo humano: «Automatizar para humanizar».

La estética es **póster pulp de ciencia ficción vintage × terminal de hacker, anclado en la clínica**. Cálido, táctil, un poco rebelde. Explícitamente NO es el degradado azul-morado del cliché de startup de IA, ni la estética fría y pulida de la sanidad corporativa. La referencia visual primaria es un póster impreso: tinta casi negra sobre papel blanco, grano de impresión, tipografía condensada en mayúsculas, y una segunda cara de «terminal» oscura con texto verde monoespaciado para los momentos de código, IA o «hacker».

Dos superficies, un solo estilo:

- **Blanco** (por defecto): papel puro, tinta, acentos y grano. Mucho aire. Es la cara clínica, calmada, con criterio.
- **Terminal oscuro**: paneles de tinta o teal profundo, líneas de escaneo tenues, verde brillante. Es la cara «hacker». Se reserva para portadas, separadores, citas, cierres y demostraciones técnicas.

El público son sanitarios quemados por la burocracia y con miedo a quedarse atrás. La interfaz debe transmitir lo contrario a lo que sufren: calma, espacio, criterio, y una energía cálida (terracota) que contrapese lo clínico (teal). **El espacio en blanco generoso es principio de marca**: «dejar respirar el diseño como se deja respirar al profesional». Se evita explícitamente el aspecto de PowerPoint de congreso médico o de catálogo de funcionalidades.

## Colors

Paleta con siete familias y una regla: **los fondos son blanco puro**. El calor viene de la tinta, de los acentos y del grano, nunca de un lienzo tintado. El neutro {colors.paper-300} se usa solo para zonas hundidas.

- **Tinta {colors.ink-900}**: casi negro con matiz verde carbón (el rotulado del póster). Todo el texto de lectura, bordes asertivos y superficies inversas.
- **Teal {colors.teal-700}**: color primario de marca (`primary`, `brand`). Clínico, frío, calmado. Titulares en degradado, botón de marca, cabeceras de tarjeta, información.
- **Verde terminal**: {colors.green-700} es la señal «hacker» y el color de éxito; {colors.green-term} y {colors.green-glow} son los brillantes y se reservan para CTAs, destacados, texto sobre terminal y foco. **Nunca en titulares.**
- **Terracota {colors.rust-500}**: acento de energía cálida (`accent`). CTAs principales, avisos y el contrapeso humano al teal. Se oscurece un paso a {colors.rust-700} en hover.
- **Oliva {colors.olive-500}**: neutro cálido terciario. Uso puntual (por ejemplo, uno de los tres puntos del panel terminal).
- **Violeta {colors.purple-500}**: exclusivo del nivel de curso «pros».
- **Peligro {colors.danger}**: error, deprecado, incorrecto. **El rojo nunca identifica un nivel de curso.**

Semántica: éxito = verde · aviso = terracota · peligro = {colors.danger} · información = teal.

Niveles de curso: iniciados = {colors.level-init} · amateurs = {colors.level-amateur} · pros = {colors.level-pro}.

**Degradado de firma.** Todos los titulares grandes van con un degradado a 45°, de izquierda a derecha, de teal pastel a verde: {gradients.headline} sobre blanco (clase `.sh-grad`) y {gradients.headline-bright} sobre oscuro (`.sh-grad-bright`). Sin degradados satinados, sin glassmorphism, sin degradados azul→morado.

## Typography

Cuatro familias de Google Fonts, cada una con un papel fijo. En Canva se usó AGRANDIR como excepción histórica; la tipografía canónica es esta.

- **Anton** (`display`, `h1`): condensada ultra-negrita, siempre en MAYÚSCULAS. El logotipo y los titulares grandes. Tracking apretado ({typography.display.letterSpacing}) e interlineado nunca por debajo de 1.0: los glifos de Anton se desbordan.
- **Oswald** (`h2`, `h3`, `label`, `button`): encabezados condensados en mayúsculas, etiquetas y botones. Tracking de mayúsculas 0.06em.
- **Barlow** (`lead`, `body`, `small`, `input`): grotesca humanista utilitaria para todo el texto de lectura. Interlineado de cuerpo 1.55.
- **Space Mono** (`kicker`, `mono`, `badge`, `tag`): kickers, código, prompts con `>`, datos y el motivo CRT. Los kickers van en mayúsculas con tracking amplio de 0.22em.

Ritmo estándar de cualquier bloque: **kicker mono → titular condensado grande → cuerpo**. Las grandes afirmaciones y el logotipo van en MAYÚSCULAS; el cuerpo, en frase normal.

Escala de tamaños disponible en `tokens.css`: 0.75 · 0.875 · 1 · 1.125 · 1.375 · 1.75 · 2.25 · 3 · 4 · 5.5 rem. Interlineados: 1.05 (tight) · 1.25 (snug) · 1.55 (body).

**[PENDIENTE]** Los originales no asignan qué paso de la escala corresponde a cada nivel web. Los tamaños de `display`, `h1`, `h2`, `h3`, `lead`, `body`, `small`, `kicker`, `label` y `mono` del bloque YAML son una propuesta de mapeo, marcada como tal, registrada en `DECISIONES.md`. Los únicos tamaños afirmados por los originales son los de componentes (badge 11px, campo 15px, etiqueta de campo 12px, tag 11px) y los de presentaciones (kicker 26px, pie 20px, cifras 200px, cuerpo 32 a 44px, suelo 24px).

## Layout

Rejilla de 4px: toda medida de espaciado es múltiplo de {spacing.base}, con la escala {spacing.sp-1} a {spacing.sp-10}. Se maqueta con grid y flex usando `gap`, no con márgenes sueltos.

El espacio en blanco es un principio de marca, no un recurso decorativo. Cada sección respira; el contenido se agrupa en islas claras separadas por aire generoso ({spacing.sp-8} o más entre bloques). Los héroes y los encabezados de sección pueden ir a sangre completa con imagen o con un panel terminal oscuro.

La página alterna las dos superficies con intención: blanco por defecto, terminal oscuro solo cuando el contenido es código, IA o un momento «hacker». Nunca más de esos dos fondos en una misma pieza.

## Elevation & Depth

La profundidad se transmite con **textura y bordes**, no con sombras aparatosas.

- **Grano**: la capa de textura de firma (`.sh-grain` en `tokens.css`, un SVG en línea sin activo externo). Moteado impreso tenue sobre blanco (mezcla `multiply`, opacidad 0.06 a 0.10) y más fuerte sobre superficies oscuras y héroes (`overlay`, opacidad 0.13). Nunca un relleno plano muerto.
- **Sombras**: bajas, cálidas y teñidas de tinta: {shadows.sm}, {shadows.md} y {shadows.lg}. Los elementos con carácter de póster llevan la **sombra de sello dura** {shadows.stamp}: un desplazamiento sólido sin desenfoque, como un cuño.
- **Superficies terminal**: paneles de tinta o teal profundo con líneas de escaneo tenues y texto mono verde. Son el segundo modo de fondo.
- **Brillo (glow)**: {shadows.glow-term} se reserva para elementos de terminal o IA activos sobre superficies oscuras.

## Shapes

Radios pequeños y mecánicos: {rounded.xs}, {rounded.sm}, {rounded.md} y {rounded.lg}. Píldoras ({rounded.pill}) solo para etiquetas y niveles. Se evitan las esquinas mullidas de 16px o más.

Los bordes son líneas finas asertivas de {borders.hairline}, a menudo en tinta. Los elementos enmarcados o con sello llevan {borders.thick}. Las tarjetas: relleno blanco, borde de {borders.hairline}, radio pequeño y sombra cálida baja; las de tipo póster, sombra de sello.

## Components

### Buttons

Oswald 600, mayúsculas, tracking 0.06em, radio {rounded.sm}, borde de {borders.hairline}. Al pulsar, el botón se desplaza 1px hacia abajo (`translateY(1px)`) y reduce la sombra de sello: queda «estampado».

- **primary**: relleno {colors.rust-500}, borde {colors.rust-700}; hover {colors.rust-700}. La acción principal.
- **brand**: relleno {colors.teal-700}, borde {colors.teal-900}; hover {colors.teal-900}.
- **ghost**: transparente con borde de tinta; hover con tinte `rgba(20,32,26,.06)`.
- **term**: relleno de tinta con etiqueta mono verde brillante, sin mayúsculas; hover añade {shadows.glow-term}.
- **disabled**: tinta tenue, sin sombra, cursor `not-allowed`.

### Level badges

Space Mono 700, 11px, tracking 0.1em, píldora, punto de 7px más etiqueta. iniciados {colors.green-100} sobre {colors.green-900} · amateurs {colors.teal-100} sobre {colors.teal-900} · pros {colors.purple-100} sobre {colors.purple-900}. Sobre fondo oscuro: fondo `rgba(0,0,0,.28)` y texto blanco.

### Course card

Relleno blanco, borde de tinta de {borders.hairline}, radio {rounded.md}, sombra de sello {shadows.stamp} que crece a `5px 5px 0` con `translate(-2px,-2px)` en hover. Cabecera en teal con un kicker mono (`> CURSO 03`) y el badge de nivel. Cuerpo: título en Oswald (interlineado ≥ 1.2), descripción en Barlow, etiqueta meta y CTA en terracota «Empezar →».

### Form fields

Barlow 15px, relleno blanco, borde de {borders.hairline} en {colors.border-strong}, radio {rounded.sm}. Etiqueta en Oswald mayúsculas 12px. Foco: borde de tinta más contorno de 2px en {colors.green-term} con 2px de separación.

### Terminal panel

Fondo {colors.ink-900}, borde {colors.teal-900}, barra superior con tres puntos (terracota, oliva, verde), cuerpo en Space Mono con el prompt `academia@saluhackers:~$`, salida en verde brillante y cursor `_` parpadeante.

### Tags

Space Mono 11px, borde tenue, radio {rounded.sm}, icono Lucide opcional de 13px.

## Do's and Don'ts

- **Do** dejar respirar el diseño: aire generoso entre bloques, como se deja respirar al profesional.
- **Do** seguir el ritmo kicker mono → titular condensado → cuerpo en cada bloque.
- **Do** poner en degradado 45° teal→verde todos los titulares grandes (`.sh-grad` sobre blanco, `.sh-grad-bright` sobre oscuro).
- **Do** usar terracota para la acción principal y verde brillante solo para CTAs, destacados y foco.
- **Do** usar imágenes realistas y épicas de entornos sanitarios reales: una guardia, una pantalla con resultados, unas manos sobre un teclado.
- **Do** tratar el fondo como papel: blanco puro con grano, nunca un lienzo tintado.
- **Don't** usar el degradado azul→morado de startup de IA, degradados satinados ni glassmorphism.
- **Don't** poner verdes brillantes ({colors.green-term}, {colors.green-glow}) en titulares.
- **Don't** usar el rojo para un nivel de curso: se reserva para peligro, error o deprecado.
- **Don't** usar bancos de imágenes con médicos sonrientes.
- **Don't** dibujar iconos ni escenas SVG a mano; los iconos son Lucide y las imágenes, artwork real de la marca.
- **Don't** mezclar iconos rellenos y de contorno en una misma vista.
- **Don't** usar esquinas de 16px o más, ni píldoras fuera de etiquetas y niveles.
- **Don't** animar con parallax, spring ni bucles decorativos: nada rebota ni flota.
- **Don't** usar más de dos fondos (blanco y terminal oscuro) en una misma pieza.
- **Don't** montar el aspecto de PowerPoint de congreso médico o de catálogo de funcionalidades.
- **Don't** usar emojis en interfaz; se prefieren los glifos monoespaciados.

## Iconography

No existe un set de iconos propio. Se usa **Lucide**: contorno, trazo de unos 2px, geometría cuadrada, que casa con los bordes finos y se lee sobre blanco y sobre oscuro. Es una sustitución declarada: se reemplaza si algún día hay un set de marca.

- Tamaño 20 a 24px, `stroke-width: 2`, `currentColor` para heredar tinta, teal o verde. Nunca mezclar relleno y contorno.
- El motivo terminal usa glifos tipográficos como iconos, en Space Mono: `>` `_` `//` `[ ]` `›` `▸` `■`, para kickers, viñetas y cromo de terminal.
- Los motivos sanitarios (línea de ECG, corazón, reloj, pijama) pertenecen a la imagen ilustrativa, no al sistema de iconos. En interfaz se usan `activity`, `heart-pulse`, `clock` y `stethoscope` de Lucide.

## Imagery

Artwork realista y épico, «estilo Star Wars», de entornos sanitarios reales: una guardia, una pantalla llena de resultados, unas manos sobre un teclado. Autenticidad sobre pulido: residentes quemados, enfermeras que no dan abasto. Se maqueta con huecos que se rellenan con el artwork real de la marca; no se dibujan escenas SVG a mano.

## Motion

Contenida y mecánica: entre {motion.duration-min} y {motion.duration-max}, con {motion.easing}. Las cosas se deslizan y encajan; no rebotan ni flotan. La única personalidad en movimiento es el parpadeo del cursor de terminal y un brillo ocasional de línea de escaneo CRT. Sin parallax, sin spring, sin bucles decorativos.

## Interaction States

- **Hover**: los rellenos se oscurecen un paso (rust-500 → rust-700); los elementos ghost reciben un tinte tenue; los enlaces pasan a verde terminal.
- **Press**: desplazamiento de 1px hacia abajo y a la derecha, con la sombra de sello reducida («estampado»); `scale(0.98)` aceptable en botones de icono.
- **Focus**: contorno de 2px en verde terminal con 2px de separación.
- **Disabled**: tinta tenue, sin sombra, cursor `not-allowed`.

## Presentations

1920×1080. Solo dos modos de diapositiva: **blanco** (por defecto, mucho aire) y **terminal oscuro** (impacto: portadas, separadores, citas y cierres). Máximo esos dos fondos por presentación.

- Titulares en degradado (`.sh-grad` sobre blanco, `.sh-grad-bright` sobre oscuro).
- Kicker mono de 26px con tracking 0.22em sobre cada titular.
- Suelo de texto 24px; cuerpo 32 a 44px; cifras grandes 200px.
- Pie: mono 20px, línea fina, marca a la izquierda y número de diapositiva a la derecha.
- Tipos construidos: portada · declaración · agenda · idea madre (dos enemigos) · dato grande · comparativa · separador temático con hueco de imagen · cita grande · cierre con CTA.
- Verde brillante solo en chips de CTA y destacados, nunca como relleno de titular.

## LinkedIn Carousels

Descrito a partir de la única pieza publicada en el repositorio (`piezas/carruseles/carrusel-linkedin-ejemplo.pdf`, 6 páginas). Se consolida como regla cuando haya más piezas.

- **Formato**: 1080×1350 px (proporción 4:5), una página por diapositiva, exportado a PDF.
- **Superficie**: modo terminal oscuro en todas las páginas, con grano e imagen de fondo (interior de hospital) y un marco perimetral de {borders.thick} en terracota.
- **Estructura de cada página**: kicker mono en verde brillante arriba a la izquierda (`> GEMINI_NOTEBOOK`, `> EL_EXPERIMENTO`) → titular en Anton, MAYÚSCULAS, blanco, con una o dos líneas destacadas en verde brillante o terracota → cuerpo en Barlow sobre fondo oscuro.
- **Capturas y evidencias**: enmarcadas con borde en terracota (caso «no hacker») o blanco/verde (caso «hacker»); etiquetas en chips mono mayúsculas con relleno terracota o verde e ink de texto.
- **Paneles de terminal** para prompts y salidas, con los tres puntos y el texto en verde.
- **CTA**: chip mono en verde brillante con borde, abajo a la derecha (`DESCUBRE EL PORQUÉ →`). La última página cierra con la conclusión, la firma del autor y su usuario de LinkedIn.
- Tipografías comprobadas en el archivo: Anton, Oswald Bold, Barlow (Regular, Bold, Italic) y Space Mono (Regular, Bold).
