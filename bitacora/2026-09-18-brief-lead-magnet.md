# Sesión 2026-09-18 · Brief del lead magnet

- **Quién**: Alfredo, con Claude Code.
- **Objetivo**: dejar por escrito en el repositorio el brief de «3 pasos para hackear tu Gemini Notebook sanitario».
- **Hecho**: `proyectos/lead-magnet/brief.md` con el texto de Alfredo. `README.md` del proyecto reescrito: deja de listar preguntas de brief y remite al archivo, y enumera lo que falta para poder empezar. PR #6.
- **Decisiones**: D-015 (servicio y campos del formulario de lista de espera) y D-016 (contradicción entre el brief y `marca/voz.md` sobre las promesas de ahorro de tiempo), las dos abiertas.
- **Probado y descartado**:
  - Transcribir el brief tal cual, con `design.md` en minúsculas. Descartado: ese archivo no existe, el del repositorio es `DESIGN.md`, y en un sistema de archivos que distingue mayúsculas la referencia se rompe. Corregida solo la caja del nombre.
  - Dejar la lista de «Reglas que no se negocian» con la mezcla de viñetas y la frase partida que traía el original. Descartado: era daño de formato al pegar, no intención. Se unificaron las viñetas y se unió la frase sin tocar una sola palabra.
  - Empezar la pieza sobre `plantilla.html`. Descartado: la plantilla es una página de secciones apiladas y el brief pide una idea por pantalla sin desplazamiento vertical. La plantilla queda como referencia de estilos y origen del bloque de tokens.
  - Renombrar `assets/` a `activos/` por coherencia con D-009. No hecho: la carpeta todavía no existe y el nombre lo decide Alfredo.
- **Pendiente y preguntas abiertas**:
  - Falta `contenido.md` con el texto final y las marcas `[ELEMENTO · …]`. Sin él no se puede construir nada: el brief prohíbe reescribir o resumir ese texto.
  - Faltan las dos capturas del elemento 9.
  - Falta quién firma, dónde se aloja el archivo y la fecha de publicación.
  - D-015 y D-016 esperan respuesta. D-002, D-006 y D-007 siguen abiertas.
- **Archivos de gobierno tocados**: ninguno. `CLAUDE.md` y `README.md` de la raíz no cambian: el brief no altera la estructura del repositorio ni ninguna convención.
