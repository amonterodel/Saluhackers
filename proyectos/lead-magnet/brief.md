# Brief · Lead magnet «3 pasos para hackear tu Gemini Notebook sanitario»

## Qué es

Un único archivo HTML autocontenido (CSS y JS incrustados, sin dependencias
externas salvo las permitidas en DESIGN.md). Se lee como una historia: una
idea por pantalla, sin desplazamiento vertical, navegación con flechas,
teclado y gesto táctil. Indicador de progreso discreto. Debe funcionar en
móvil.

## Reglas que no se negocian

- mobile-first (responsive 100%)
- El texto de contenido.md es final. No se reescribe, no se resume, no se
  añade ni una frase. Si algo no cabe, me avisas.
- Nada de emoticonos. Iconografía propia según DESIGN.md.
- Ningún signo de exclamación.
- Ninguna tabla o dato clínico inventado con fármacos o dosis reales: los
  ejemplos ilustrativos usan «Fármaco A» y llevan etiqueta «ejemplo».
- Tono y paleta: DESIGN.md. Si DESIGN.md y este brief se contradicen, gana
  DESIGN.md y me lo dices.

## Elementos

Cada `[ELEMENTO · …]` de contenido.md describe un componente en el punto
exacto donde va. Son estos, en orden de aparición:

1. Simulación de cita: botón «ver cita» que abre un panel con un fragmento
   resaltado que no coincide con la afirmación.
2. Diagrama animado de tres estados: documento → troceado → recuperación por
   parecido.
3. Tabla de dos columnas: lo que no cambia / lo que sí cambia.
4. Tabla de tres filas: fallo / qué hace el cuaderno / qué pregunta lo detecta.
5. Pantalla propia para la cita «No hay prompt que arregle un corpus mal
   montado».
6. Comparador con conmutador: usuario / hacker. Mismo componente que el 10.
7. Cuaderno rellenable: tres campos (localización, cruce, ausencia) con botón
   de copiar. Es el elemento interactivo principal.
8. Mini-ejercicio de tres tarjetas: ninguna / toda / una parte.
9. Antes/después con las dos capturas de assets/.
10. Comparador de tres estados sobre una tabla ilustrativa: lo que ves tú /
    lo que ve el cuaderno / traducida. Reutiliza el componente 6.
11. Lista de verificación interactiva de tres filas; al completarla,
    transición de vuelta a la escena de la primera pantalla con la cita
    abierta y coincidiendo.
12. Tabla de decisión: no compensa / compensa.
13. Tres tarjetas de límites con iconografía propia.
14. Diagrama de tres capas: fuentes (hecha), comportamiento (bloqueada),
    conexión (insinuada).
15. CTA final: formulario de lista de espera. [PENDIENTE: servicio y campos]

## Fuera de alcance

Vídeo incrustado, muro de correo antes del contenido, cualquier
promesa de ahorro de tiempo.
