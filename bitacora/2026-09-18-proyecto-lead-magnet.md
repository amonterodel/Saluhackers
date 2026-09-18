# Sesión 2026-09-18 · Dónde vive el proyecto del lead magnet

- **Quién**: Alfredo, con Claude Code.
- **Objetivo**: decidir dónde crear la carpeta del proyecto para construir un lead magnet y dejarla montada.
- **Hecho**: nueva carpeta `proyectos/` con `sincroniza-tokens.py` y `proyectos/lead-magnet/` (su `CLAUDE.md`, un `README.md` con el brief por cerrar y `plantilla.html`). `CLAUDE.md` y `README.md` de la raíz actualizados para acotar qué cabe en `proyectos/`. PR #5.
- **Decisiones**: D-013 (los artefactos autocontenidos viven en `proyectos/` dentro de este repositorio) y D-014 (se mantiene el `@import` a Google Fonts como única petición externa). Las dos cerradas por Alfredo.
- **Probado y descartado**:
  - Repositorio aparte para el proyecto, que era mi recomendación inicial. Descartado por Alfredo. Dos de mis cuatro objeciones se caían solas al saber que el artefacto es un único archivo sin dependencias ni compilación: no hay árbol de dependencias ni artefactos de compilación que ensucien el contexto del agente. Las otras dos (ciclos de vida distintos y copy de negocio) se resuelven con el `CLAUDE.md` del proyecto y con la regla de que el copy de negocio sigue en Notion.
  - Incrustar las cuatro tipografías en base64 para que el archivo fuese autónomo de verdad. Descartado: del orden de un megabyte por archivo a cambio de funcionar sin conexión, que no es el caso de uso.
  - Escribir ya un `index.html` con estructura de landing de captación. Descartado: no está decidido si la pieza capta el correo o se entrega después de captarlo, y eso cambia la estructura. Queda como `plantilla.html` neutra.
  - Duplicar los tokens a mano dentro del HTML. Descartado: se generan con `sincroniza-tokens.py` desde `marca/tokens.css`, que sigue mandando (D-004).
- **Pendiente y preguntas abiertas**:
  - El brief del lead magnet está sin cerrar: tema y caso clínico, quién firma, si capta o entrega, dónde se aloja y fecha. Está en `proyectos/lead-magnet/README.md`.
  - D-002, D-006 y D-007 siguen esperando a los cuatro fundadores.
  - Sigue pendiente purgar del historial de git los commits con los documentos de origen.
- **Archivos de gobierno tocados**: `CLAUDE.md` (mapa con `proyectos/`, qué cabe y qué no, y la frase de que en la raíz no hay nada que compilar) y `README.md` (la línea que decía «no contiene código de producto» era falsa desde D-013, y la lista de dónde va cada cosa nueva).
