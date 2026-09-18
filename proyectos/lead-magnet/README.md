# Lead magnet

**Estado: brief recibido, contenido pendiente.** La pieza es «3 pasos para hackear tu Gemini Notebook sanitario».

## Archivos

- `brief.md`: qué se construye, las reglas que no se negocian y los quince elementos interactivos en orden. Es la referencia de esta pieza.
- `CLAUDE.md`: reglas técnicas del proyecto. Las lee Claude Code al trabajar en esta carpeta.
- `plantilla.html`: esqueleto de marca con los tokens ya incrustados. Sirve como referencia de estilos y como origen del bloque de tokens, no como base de esta pieza: el brief pide una idea por pantalla sin desplazamiento vertical, y la plantilla es una página de secciones apiladas.

## Qué falta para poder empezar

- `contenido.md`, con el texto final y las marcas `[ELEMENTO · …]` en su sitio. Sin él no hay pieza: el brief dice que ese texto no se reescribe ni se resume.
- Las dos capturas del elemento 9 (antes y después). El brief las sitúa en `assets/`, carpeta que todavía no existe.
- Quién firma la pieza (ver «Quién firma qué» en `marca/voz.md`).
- Servicio y campos del formulario de lista de espera del elemento 15 (D-015).
- Dónde se aloja el archivo, con qué nombre, y la fecha de publicación visible en el pie.

## Cómo sincronizar los tokens de un archivo

```
python3 proyectos/sincroniza-tokens.py proyectos/lead-magnet/<archivo>.html
```

El archivo se abre directamente en el navegador. No hay servidor ni instalación.
