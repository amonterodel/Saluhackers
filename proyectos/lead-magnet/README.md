# Lead magnet

**Estado: sin empezar.** El esqueleto de marca está listo; el contenido, por definir.

## Archivos

- `plantilla.html`: esqueleto con los tokens de marca ya incrustados, las dos superficies, el panel de terminal y la llamada a la acción. Sin contenido: todo son marcas `[PENDIENTE]`.
- `CLAUDE.md`: reglas de este proyecto. Las lee Claude Code al trabajar en esta carpeta.

## Cómo empezar una pieza

```
cp proyectos/lead-magnet/plantilla.html proyectos/lead-magnet/<tema>.html
python3 proyectos/sincroniza-tokens.py proyectos/lead-magnet/<tema>.html
```

Y abrir el archivo en el navegador. No hay servidor ni instalación.

## Brief por cerrar

Ninguna de estas respuestas está en el repositorio, así que hay que traerlas antes de escribir:

- Tema y caso clínico concreto que resuelve, con el resultado medible que se lleva el lector.
- Quién firma la pieza (ver «Quién firma qué» en `marca/voz.md`).
- Si esta pieza **capta** el correo (lleva formulario, y hay que decidir a dónde envía) o se **entrega** después de haberlo captado (sin formulario). De eso depende el destino del botón de cierre.
- Dónde se aloja el archivo y con qué nombre.
- Fecha de publicación y de última actualización visible en el pie.
