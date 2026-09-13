# Saluhackers · Contexto de marca

Este repositorio es la fuente de verdad de marca, voz y diseño. Notion es la fuente de verdad de negocio. Ningún dato de negocio entra aquí.

## Qué es

Contexto de referencia de Saluhackers, escuela de formación en IA para profesionales sanitarios. Lo consumen personas y agentes (Claude Code, Claude Design) para producir piezas coherentes con la marca: carruseles de LinkedIn, herramientas web y otros materiales.

## Estructura

```
README.md              Este archivo
DECISIONES.md          Decisiones abiertas y cerradas sobre marca, voz y diseño
CHANGELOG.md           Historial de cambios del repositorio
marca/
  contexto.md          Qué es Saluhackers, público objetivo y territorio, voz y tono
  design-system.md     Sistema de diseño: fundamentos visuales, iconografía, componentes y reglas de presentaciones
  tokens.css           Hoja de tokens CSS: colores, tipografía, espaciado, radios, sombras y degradados
piezas/
  carruseles/          Carruseles de LinkedIn (vacío por ahora)
```

## Convenciones

- Los archivos de `marca/` son la referencia. Cualquier pieza nueva se comprueba contra ellos.
- Las decisiones pendientes se registran en `DECISIONES.md`, no dentro de los documentos de marca.
- Cada cambio relevante se anota en `CHANGELOG.md`.
- Los archivos cuyo nombre empiece por `PRIVADO_` y la carpeta `_origen/` no entran en git.
