# Lead magnet

**Estado: brief recibido, contenido pendiente.** La pieza es «3 pasos para hackear tu Gemini Notebook sanitario».

## Archivos

- `brief.md`: qué se construye, las reglas que no se negocian y los quince componentes en orden. Es la referencia de esta pieza.
- `contenido.md`: el texto final, con las marcas `[ELEMENTO · …]` y `[CTA · …]` en el punto exacto donde va cada componente. No se reescribe, no se resume, no se añade ni una frase (primera regla del brief).
- `assets/`: los originales de las imágenes. El inventario, con qué es cada una y dónde va, está en `CLAUDE.md`.
- `CLAUDE.md`: reglas técnicas del proyecto. Las lee Claude Code al trabajar en esta carpeta.
- `plantilla.html`: esqueleto de marca con los tokens ya incrustados. Sirve como referencia de estilos y como origen del bloque de tokens, no como base de esta pieza: el brief pide una idea por pantalla sin desplazamiento vertical, y la plantilla es una página de secciones apiladas.

## Qué falta para poder empezar

- **La infografía `assets/infografia-usuario-vs-hacker.png`**, que `contenido.md` enlaza y todavía no existe. Es la única imagen que falta: las otras dos que enlaza el texto ya están, y en `assets/` hay además la escena del archivo y las dos capturas de respuesta para los elementos interactivos.
- **Resolver los cuatro desajustes entre `brief.md` y `contenido.md`** (D-017): número de tarjetas del elemento 8, orden del antes/después frente al comparador, nombre de la primera capa del elemento 14 y cuántas imágenes hay.
- **Servicio y campos del formulario de lista de espera** de la marca `[CTA · lista de espera]` (D-015).
- **Quién firma la pieza** (ver «Quién firma qué» en `marca/voz.md`).
- **Dónde se aloja el archivo**, con qué nombre, y la fecha de publicación visible en el pie.
- **Dónde va la bibliografía** de cinco referencias con la que cierra `contenido.md`: pantalla propia, panel desplegable o pie. El brief no la contempla.

## Cómo sincronizar los tokens de un archivo

```
python3 proyectos/sincroniza-tokens.py proyectos/lead-magnet/<archivo>.html
```

El archivo se abre directamente en el navegador. No hay servidor ni instalación.
