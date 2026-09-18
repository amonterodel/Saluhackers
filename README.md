# Saluhackers · Contexto de marca

Este repositorio es la fuente de verdad de marca, voz y diseño. Notion es la fuente de verdad de negocio. Ningún dato de negocio entra aquí.

## Qué es Saluhackers

Escuela online de IA exclusivamente para profesionales sanitarios. No enseña IA en abstracto: enseña a los sanitarios a quitarse las partes más aburridas de su trabajo para reilusionarse con la profesión. La frase ancla es «Automatizar para humanizar». La montan cuatro fundadores con empleo y familia, y el tiempo es el recurso escaso: todo lo que hay aquí está pensado para no tener que volver a explicarlo.

## Qué es este repositorio (y qué no es)

Aquí vive todo lo necesario para que una pieza (un carrusel de LinkedIn, una landing, una presentación, una herramienta web) sea reconociblemente Saluhackers: cómo hablamos, cómo nos vemos y los valores exactos que usamos. Lo consumen los fundadores y los agentes con los que trabajamos (Claude Code, Claude Design).

No es un repositorio de negocio (precios, comisiones, embajadores, métricas: eso vive en Notion) ni el archivo de todo lo que publicamos. Sí se construyen aquí las piezas que son un único archivo autocontenido, en `proyectos/`, pero no aloja servicios, aplicaciones con despliegue ni nada que haya que instalar.

## Tu primer día aquí

1. Lee [`marca/contexto.md`](marca/contexto.md): qué somos, para quién y desde qué territorio hablamos.
2. Lee [`marca/voz.md`](marca/voz.md) entero: cómo hablamos, las siete reglas duras y el léxico prohibido.
3. Hojea [`DESIGN.md`](DESIGN.md): cómo nos vemos y por qué. Ten a mano [`marca/tokens.css`](marca/tokens.css), donde están los valores exactos.
4. Abre [`piezas/`](piezas/): piezas reales ya publicadas, para ver el resultado y no solo la norma.
5. Antes de proponer un cambio, mira [`DECISIONES.md`](DECISIONES.md): puede que ya esté decidido, o abierto y esperando a los cuatro.

## Cómo se trabaja

- Con rama y PR, también los agentes. Cada cambio deja huella: qué y por qué en [`CHANGELOG.md`](CHANGELOG.md), una fila en `DECISIONES.md` si se decidió algo, y una entrada en [`bitacora/`](bitacora/) al cerrar la sesión.
- El mapa completo de archivos, qué archivo manda sobre qué, los comandos de validación y las convenciones están en [`CLAUDE.md`](CLAUDE.md). Lo leen los agentes al arrancar y es la referencia también para personas. Este README no lo repite para que no diverjan.
- Nunca entra en git: la carpeta `_origen/`, cualquier archivo `PRIVADO_*`, ni ningún dato de negocio.

## Dónde va cada cosa nueva

- Un logotipo, una plantilla, una marca de agua: `activos/`.
- Una referencia externa que inspira el estilo (una captura, un PDF, un póster): `inspiracion/`.
- Una pieza nuestra ya publicada: `piezas/<tipo>/` (hoy, `piezas/carruseles/`).
- Algo que hay que construir y se abre en el navegador (un lead magnet, una página autocontenida): `proyectos/<nombre>/`.
- Una decisión: `DECISIONES.md`. Un cambio: `CHANGELOG.md`. Una sesión de trabajo: `bitacora/`.
