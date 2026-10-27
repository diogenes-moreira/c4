# Estación 6: Del spec al harness

Lleva tu especificación a un estado **listo para implementar**: primero la evalúas, después la conviertes en un grafo de tareas y lo dejas en Linear. En la estación 7 un agente lo ejecuta.

Todo el recorrido usa un mapa fijo que aparece arriba en cada slide, con la pieza actual resaltada:

**LLM → Coding agent → Arnés → Loop → Orquestador → MCP**

## Material de clase

- [Presentación PDF](estacion6.pdf).
- [Presentación HTML editable](estacion6.html). Se genera con [`fuente/build-deck.py`](fuente/build-deck.py).
- [Skill evaluate-spec](skills/evaluate-spec/SKILL.md): evalúa la spec con tres lentes (producto, TDD y diseño) y le pone una nota de A a D.
- [Skill create-implementation-plan](skills/create-implementation-plan/SKILL.md): copia de la skill de OpenSymphony que genera el paquete de tareas.
- [Ejemplo de spec review](ejemplos/spec-review-entrevista-ai.md): la skill aplicada a EntreVista AI. Una ola con nota B y el resto con C.
- [Plantilla design.md](plantillas/design.md): lo que el agente debe saber sobre cómo se ve y cómo se construye tu producto.
- [Ejemplo trabajado y prompts](ejemplo-y-prompts.md).
- [Recursos y lecturas](recursos.md).
- [Preparación para estación 7](../estacion7/preparacion.md).

## Cinco módulos

La clase está dividida en módulos que se sostienen solos: cada uno entra con un artefacto y sale con otro. Si uno se acorta, su salida sigue sirviendo.

| Módulo | Min | Entra | Sale | Pieza del mapa |
|---|---|---|---|---|
| Apertura | 8 | | El mapa y la ruta | Todo el mapa |
| 1 · Del LLM al orquestador | 17 | Tu herramienta actual | Tu herramienta ubicada en el mapa | Todo el mapa |
| 2 · Evaluar la spec | 25 | Tu spec de E4 y E5 | `docs/spec-review.md` con nota A–D | Arnés (skill) |
| Pausa | 5 | | | |
| 3 · design.md + Linear | 17 | Spec con nota A o B | `design.md` y fuentes de verdad claras | Arnés, MCP |
| 4 · Del plan al grafo | 30 | Spec + `design.md` | Paquete de tareas y grafo en Linear | Arnés, Orquestador, MCP |
| 5 · Loop y orquestador | 12 | Grafo publicado | Qué automatiza E7: meta-arnés y OpenSymphony | Loop, Orquestador |
| Cierre | 6 | | Preparación de E7 clara | |

## Qué cambió respecto de la versión anterior

El rediseño responde al [post-mortem de la cohorte 3](fuente/post-mortem.md), donde esta estación tuvo la nota más baja:

- **Reencuadre:** la estación conecta la spec con el estado listo para implementar.
- **Nuevo:** skill `evaluate-spec` con nota ABCD y lentes de producto, TDD y diseño.
- **Nuevo:** mapa conceptual persistente «estás aquí» en todas las slides.
- **Nuevo:** `design.md` y Linear como fuentes de verdad explícitas.
- **Nuevo:** recorrido completo de `create-implementation-plan` → grafo de tareas → `convert-tasks-to-linear`.
- **Modular:** cinco módulos con entrada y salida propias.
- **Fuera del deck:** persistencia, benchmarks, EBO y auto-mejora pasan a lecturas opcionales en `recursos.md`.
- **Conexión con AIDLC:** una slide muestra cómo una unidad de AIDLC se convierte en una ola de tareas.

También se incorporan los hallazgos de la [clase de C4](fuente/analisis-clase-c4.md): no hubo práctica en clase y el objetivo llegó tarde. El guion agrega reglas para proteger la práctica y preguntas frecuentes reales.

Para el instructor: [guion y tiempos](fuente/guion.md).
