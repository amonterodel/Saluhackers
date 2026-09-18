#!/usr/bin/env python3
"""Copia marca/tokens.css dentro del bloque de tokens de un HTML autocontenido.

Uso:
    python3 proyectos/sincroniza-tokens.py proyectos/lead-magnet/plantilla.html

El archivo de destino debe llevar estas dos marcas dentro de un <style>:

    /* tokens:inicio ... */
    /* tokens:fin */

Todo lo que haya entre ellas se sustituye por el contenido literal de
marca/tokens.css, que es la fuente de verdad (D-004). El script solo copia en
esa dirección: nunca escribe en marca/tokens.css.
"""

import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "marca" / "tokens.css"
MARCAS = re.compile(r"(/\* tokens:inicio[^\n]*\*/)(.*?)([ \t]*/\* tokens:fin \*/)", re.S)


def sincroniza(destino: pathlib.Path, tokens: str) -> bool:
    texto = destino.read_text(encoding="utf-8")
    if not MARCAS.search(texto):
        sys.exit(f"{destino}: faltan las marcas /* tokens:inicio */ y /* tokens:fin */")
    def reemplaza(coincidencia: "re.Match[str]") -> str:
        apertura = coincidencia.group(1)
        cierre = coincidencia.group(3).lstrip(" \t")
        return apertura + "\n" + tokens + "\n" + cierre

    nuevo = MARCAS.sub(reemplaza, texto)
    if nuevo == texto:
        return False
    destino.write_text(nuevo, encoding="utf-8")
    return True


def main() -> None:
    destinos = sys.argv[1:]
    if not destinos:
        sys.exit(__doc__)
    tokens = FUENTE.read_text(encoding="utf-8").strip()
    for ruta in destinos:
        destino = pathlib.Path(ruta)
        if not destino.is_file():
            sys.exit(f"{destino}: no existe")
        cambiado = sincroniza(destino, tokens)
        print(f"{destino}: {'actualizado' if cambiado else 'ya estaba al día'}")


if __name__ == "__main__":
    main()
