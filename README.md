# Saluhackers · Contexto de marca

Este repositorio es la fuente de verdad de marca, voz y diseño. Notion es la fuente de verdad de negocio. Ningún dato de negocio entra aquí.

## Qué es

Contexto de referencia de Saluhackers, escuela de formación en IA para profesionales sanitarios. Lo consumen personas y agentes (Claude Code, Claude Design) para producir piezas coherentes con la marca: carruseles de LinkedIn, herramientas web y otros materiales.

## Estructura

```
README.md              Este archivo
CLAUDE.md              Instrucciones para agentes (Claude Code)
DESIGN.md              Sistema de diseño en el formato DESIGN.md de Google: tokens en YAML más prosa
DECISIONES.md          Decisiones abiertas y cerradas sobre marca, voz y diseño
CHANGELOG.md           Historial de cambios del repositorio
marca/
  contexto.md          Qué es Saluhackers, público objetivo y territorio de marca
  voz.md               Voz de la marca: reglas duras, tono, léxico prohibido, frases ancla, quién firma qué, ejemplos
  tokens.css           Hoja de tokens CSS. Fuente de verdad de todos los valores de diseño
piezas/
  carruseles/          Carruseles de LinkedIn publicados (PDF)
```

## Qué manda sobre qué

- **Valores de diseño** (colores, tipografía, espaciado, radios, sombras): `marca/tokens.css`. El bloque YAML de `DESIGN.md` los refleja; un cambio se hace primero en el CSS y después se sincroniza el YAML.
- **Reglas visuales y cómo aplicar los valores**: `DESIGN.md`.
- **Voz y tono**: `marca/voz.md`.
- **Posicionamiento, público y territorio**: `marca/contexto.md`.

## Validación

```bash
npx @google/design.md lint DESIGN.md
```

Debe dar 0 errores. Son esperados los avisos de `orphaned-tokens` (la paleta se declara completa aunque no todos los colores tengan componente) y de `token-like-ignored` (los grupos propios `borders` y `motion` no los exporta la CLI de Google).

## Convenciones

- Cualquier pieza nueva se comprueba contra `DESIGN.md` y `marca/voz.md`.
- Las decisiones pendientes se registran en `DECISIONES.md`, no dentro de los documentos de marca.
- Cada cambio relevante se anota en `CHANGELOG.md`.
- Los archivos cuyo nombre empiece por `PRIVADO_` y la carpeta `_origen/` no entran en git.
