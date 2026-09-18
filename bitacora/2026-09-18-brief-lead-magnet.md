# Sesión 2026-09-18 · Brief del lead magnet

- **Quién**: Alfredo, con Claude Code.
- **Objetivo**: dejar por escrito en el repositorio el brief de «3 pasos para hackear tu Gemini Notebook sanitario».
- **Hecho**: `proyectos/lead-magnet/brief.md` con el texto de Alfredo. `README.md` del proyecto reescrito: remite al brief y enumera lo que falta. Traído a la rama `contenido.md`, que Alfredo subió a `main` mientras tanto (PR #6). PR #7.
- **Decisiones**: D-015 (servicio y campos del formulario de lista de espera), D-016 (contradicción entre el brief y `marca/voz.md` sobre las promesas de ahorro de tiempo) y D-017 (cuatro desajustes entre `brief.md` y `contenido.md`). Las tres abiertas.
- **Probado y descartado**:
  - Transcribir el brief con `design.md` en minúsculas. Descartado: ese archivo no existe, el del repositorio es `DESIGN.md`, y en un sistema de archivos que distingue mayúsculas la referencia se rompe. Corregida solo la caja del nombre.
  - Dejar la lista de «Reglas que no se negocian» con la mezcla de viñetas y la frase partida del original. Descartado: era daño de formato al pegar. Se unificaron las viñetas y se unió la frase sin tocar una palabra.
  - Empezar la pieza sobre `plantilla.html`. Descartado: la plantilla es una página de secciones apiladas y el brief pide una idea por pantalla sin desplazamiento vertical. Queda como referencia de estilos y origen del bloque de tokens.
  - Renombrar `assets/` a `activos/` por coherencia con D-009. No hecho: la carpeta aún no existe y `contenido.md` ya enlaza esa ruta en tres sitios, así que cambiarla obligaría a tocar el texto, que es final.
  - Dar por incumplida la regla de «ningún signo de exclamación». Falsa alarma mía: los tres resultados eran la sintaxis markdown de imagen `![alt](ruta)`. En la prosa no hay ninguno.
  - Dar por ausente el componente 15. Falsa alarma mía: existe, pero marcado `[CTA · lista de espera]` en vez de `[ELEMENTO · …]`, así que el recuento de marcas daba catorce.
- **Pendiente y preguntas abiertas**:
  - Faltan las tres imágenes de `assets/`, carpeta que no existe.
  - D-015, D-016 y D-017 esperan respuesta. D-002, D-006 y D-007 siguen abiertas.
  - Falta decidir dónde va la bibliografía de cinco referencias con la que cierra `contenido.md`. El brief no la contempla.
  - Faltan quién firma, dónde se aloja el archivo y la fecha de publicación.
- **Archivos de gobierno tocados**: ninguno. `CLAUDE.md` y `README.md` de la raíz no cambian: el brief no altera la estructura del repositorio ni ninguna convención.
