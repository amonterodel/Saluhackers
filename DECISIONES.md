# Decisiones

Registro de decisiones de marca, voz, diseño y gobierno del repositorio. Cada decisión tiene un identificador `D-NNN` correlativo que se cita desde `CHANGELOG.md`, `bitacora/` y los PR. Una decisión nueva entra en la tabla de abiertas con estado por defecto: la deciden «Los cuatro fundadores». Solo el usuario cierra una decisión: al cerrarla se mueve a la segunda tabla con fecha y quién la cerró. Nunca se borra una fila ni se reutiliza un identificador.

## Abiertas

| ID | Decisión | Abierta desde | Quién decide |
|---|---|---|---|
| D-002 | Nombre público de la marca: hay tres en circulación (Saluhackers, Ágora Saluhackers, AgorIA/Academia). Uno ya publicado en la web. | 2026-09-13 | Los cuatro fundadores |
| D-006 | Mapeo de la escala tipográfica a niveles web (display, h1, h2, h3, lead, body, small, kicker, label, mono). `DESIGN.md` lleva una propuesta marcada [PENDIENTE]; los originales solo fijan familias, pesos, tracking e interlineados. | 2026-09-13 | Los cuatro fundadores |
| D-007 | Contraste del botón primario: texto blanco sobre terracota `#C2683E` da 3.93:1, por debajo del mínimo WCAG AA de 4.5:1 para texto normal. Opciones: relleno `rust-700`, texto en tinta, o aceptar la excepción. | 2026-09-13 | Los cuatro fundadores |

## Cerradas

| ID | Decisión | Cerrada el | Quién decidió |
|---|---|---|---|
| D-001 | Tipografía canónica: Google Fonts (Anton, Oswald, Barlow, Space Mono). AGRANDIR queda como excepción histórica de Canva. | 2026-09-13 | Alfredo |
| D-003 | Forma canónica de la frase ancla: «reilusionarse con la profesión». Los originales también usaban «reenamorarse» y «re-enamorarse de la profesión». | 2026-09-13 | Alfredo |
| D-004 | Fuente de verdad de los valores de diseño: `marca/tokens.css` manda; el bloque YAML de `DESIGN.md` lo refleja y se sincroniza después de cada cambio en el CSS. | 2026-09-13 | Alfredo |
| D-005 | Retirar `marca/design-system.md` una vez creado `DESIGN.md`. El Brand Reference original en inglés se conserva en `_origen/` y en el historial de git. | 2026-09-13 | Alfredo |
| D-008 | `CLAUDE.md` es el mapa definitivo del repositorio (archivos, qué manda sobre qué, comandos, convenciones, gobierno). `README.md` orienta a las personas y remite; no duplica el mapa. Toda decisión va a `DECISIONES.md`, todo cambio importante actualiza `CLAUDE.md`, y siempre se avisa al usuario en el informe de sesión. | 2026-09-13 | Alfredo |
| D-009 | Carpetas nuevas con nombre en castellano, coherentes con `marca/` y `piezas/`: `activos/` (activos visuales persistentes de la marca), `inspiracion/` (referencias visuales externas) y `bitacora/` (sesiones de trabajo). Las piezas propias ya publicadas siguen en `piezas/<tipo>/`. | 2026-09-13 | Alfredo |
| D-010 | Bitácora de sesiones: un archivo por sesión en `bitacora/AAAA-MM-DD-tema.md` siguiendo `bitacora/PLANTILLA.md`. El informe final de cada sesión se guarda ahí. | 2026-09-13 | Alfredo |
| D-011 | `CHANGELOG.md` en lista por fecha, lo más reciente arriba, una viñeta por cambio con qué, por qué y el PR o decisión relacionados (convención Keep a Changelog). Sustituye a la tabla de tres columnas. | 2026-09-13 | Alfredo |
| D-012 | `DECISIONES.md` con identificador `D-NNN` por decisión y dos tablas, abiertas arriba y cerradas debajo. Sustituye a la tabla única. | 2026-09-13 | Alfredo |
