# Análisis de la clase E6 de la cohorte 4

Fuente: grabación de Zoom del 10 de septiembre de 2026 (2 h 12 min) y su transcripción automática. La transcripción no se incluye en el repo porque contiene datos de participantes. Los minutos son aproximados.

## Qué pasó

| Reloj | Qué se hizo | Comentario |
|---|---|---|
| 0:00–0:07 | Charla informal y encuadre de Danny | Anticipa que serán sesiones «muy densas» y que habrá que volver a ver la grabación. |
| 0:07–0:16 | Presentación del instructor y de su plataforma | 9 minutos antes del primer contenido. |
| 0:16–0:26 | Alcance, contexto y ejecución; grafo de tareas | El núcleo conceptual, bien explicado. |
| 0:26–0:40 | Respuesta larga sobre revisión de PRs | Tema de E7. |
| 0:40–1:10 | Modelos abiertos, benchmarks, arneses, suscripciones y ventanas de contexto | Desvío de unos 30 minutos fuera del plan. El instructor lo reconoce: «perdón por ser tan disperso». |
| 1:10–1:22 | Skills de diseño, DESIGN.md, AGENTS.md, MCP y hooks | Recorrido rápido por muchas piezas sin anclarlas a un mapa. |
| 1:22–1:43 | Spec → tarea, Linear, `create-implementation-plan` y `convert-tasks-to-linear` | El objetivo de la estación llega en el último tercio y solo como demo. |
| 1:43–1:50 | Preguntas sobre proyectos grandes y Linear | |
| 1:50–2:05 | ARC-AGI-3, observatorio de comportamiento y plataforma de cursos | Contenido extracurricular. |
| 2:05–2:12 | Cierre y encuesta | |

## Hallazgos

1. **No hubo práctica.** El guion preveía 30 minutos de generación del plan en parejas y 18 de revisión cruzada. Ningún participante trabajó sobre su spec durante la clase.
2. **No se evaluó la spec.** El paso que el post-mortem de C3 puso primero no apareció.
3. **El objetivo llegó tarde.** Las skills que preparan las tareas aparecen después de 1 h 20 min.
4. **Sin marco, las demos abruman.** Modelos, arneses, MCP, ACP, hooks y benchmarks se mostraron como un recorrido de herramientas. Es exactamente la fricción que pedía resolver el mapa persistente.
5. **La conexión con AIDLC quedó como duda.** Un participante preguntó si esto era «otro camino al framework AIDLC». Hace falta mostrar cómo una unidad de AIDLC se convierte en una ola de tareas.
6. **Lo valorado:** la definición de ingeniería de contexto («todo lo necesario y solo lo necesario»), el grafo de tareas, la demo de Linear con tareas reales y la observabilidad de agentes, que generó ideas en varios participantes.

## Preguntas reales de los participantes

| Pregunta | Dónde se responde ahora |
|---|---|
| ¿Cómo manejo el cuello de botella de revisar muchos PRs? | E7. En E6, una línea en el módulo 5. |
| ¿Puedo usar Claude con el arnés de OpenHands? | Módulo 1, slide de modelo y agente. |
| ¿Esto es otro camino distinto de AIDLC? | Módulo 4, nueva slide «De AIDLC a tareas». |
| En proyectos grandes, ¿qué hago con los archivos de tareas viejas? | Preguntas frecuentes del guion. |
| ¿Es obligatorio usar Linear? | Preguntas frecuentes del guion y slide de Linear. |

## Cambios que aplica el rediseño

- Práctica protegida en los módulos 2 y 4 (42 minutos en total), con reloj visible.
- Evaluación de la spec como primer paso de trabajo.
- Mapa persistente en cada slide para anclar cada concepto.
- Regla de «estacionamiento»: las preguntas fuera del mapa se anotan y se responden al cierre o por escrito.
- Sin presentación de herramientas ajenas al recorrido. Benchmarks, observabilidad y auto-mejora pasan a lecturas opcionales.
- Slide nueva que conecta AIDLC con el plan de tareas.
