# Guion de clase

Presentación: `../estacion6.html`, generada con `build-deck.py`; exportación para enseñar: `../estacion6.pdf`. Duración: 120 minutos.

## Decisión pedagógica

La estación responde a una sola pregunta: **¿tu spec está lista para implementar?** Todo lo demás sirve para contestarla y para dejar el trabajo en Linear.

- Un mapa fijo (LLM → Coding agent → Arnés → Loop → Orquestador → MCP) aparece arriba en cada slide. Antes de cada bloque, señalar qué pieza está resaltada y por qué.
- Cinco módulos con entrada y salida propias. Si un módulo se atrasa, se cierra con su salida y se pasa al siguiente.
- Un solo ejemplo, EntreVista AI, desde la evaluación de la spec hasta el grafo.
- La ejecución y la orquestación quedan para E7. Aquí solo se muestra qué van a automatizar.
- No se usa la skill Dispatch de OpenSymphony (fue objetada en el post-mortem).

## Guion de 120 minutos

| Reloj | Slides | Módulo | Qué hacer |
|---|---|---|---|
| 0–8 | 1–3 | Apertura | Mostrar la salida de hoy. Recorrer el mapa completo (slide 2) y la ruta por módulos (slide 3). |
| 8–25 | 4–6 | 1 · Del LLM al orquestador | Dos piezas por slide, 3 min cada una. Cerrar con el ejercicio de 5 min: cada uno ubica su herramienta en el mapa y dice qué pieza le falta. |
| 25–50 | 7–10 | 2 · Evaluar la spec | 2 min contraste ambigua/preparada. 3 min las tres lentes. 3 min la nota ABCD. 17 min de práctica con `evaluate-spec`. |
| 50–55 | 11 | Pausa | Al volver, preguntar qué nota sacaron dos o tres personas. |
| 55–72 | 12–14 | 3 · design.md + Linear | 5 min fuentes de verdad. 5 min design.md con la plantilla abierta. 5 min Linear vía MCP. 2 min de preguntas. |
| 72–105 | 15–18 | 4 · Del plan al grafo | 3 min la skill. 3 min el grafo: qué tareas están listas. 2 min publicación con dry-run. 25 min de práctica en parejas. |
| 105–112 | 19 | 5 · Loop y orquestador | Recorrer el ciclo de una tarea. Aclarar qué se hace a mano en E7 y qué automatiza el orquestador. |
| 112–120 | 20–21 | Cierre | Checklist de preparación de E7, dónde están las skills y preguntas. |

En caso de retraso, proteger los dos bloques de práctica (módulos 2 y 4). El módulo 1 se puede dar en 10 minutos y el 5 en 3.

## Módulo 2: cómo conducir la evaluación

1. Cada participante abre su repo y le pide al arnés que lea y siga `skills/evaluate-spec/SKILL.md` (prompt en `../ejemplo-y-prompts.md`).
2. La skill escribe `docs/spec-review.md` con la nota y los vacíos citados.
3. Corrigen el vacío más grave y vuelven a evaluar. Interesa el cambio de nota, no llegar a A.
4. Si la spec queda en C o D, el participante sigue con EntreVista AI en el módulo 4 y registra su propio pendiente.

Sobre ABCD: la rúbrica no estaba definida en el post-mortem. Esta versión la concreta: A lista, B lista con supuestos aceptados, C faltan criterios críticos, D todavía no es spec. TDD se exige solo si el equipo lo declaró.

## Módulo 3: design.md y fuentes de verdad

- La spec dice qué; `design.md` dice cómo se ve y cómo se construye; los archivos de tarea son el contrato; Linear lleva el estado; el PR y los tests son la evidencia.
- No hay sincronización automática entre archivos de tarea e issues. Si cambia un contrato, se actualizan los dos.
- Publicar en un proyecto observado por un orquestador puede disparar trabajo. Usar un proyecto de preparación.

## Módulo 4: práctica en parejas

12 min para generar el paquete con `create-implementation-plan`; 7 min de revisión cruzada (cobertura, ciclos, tareas listas); 6 min de dry-run con `convert-tasks-to-linear` o carga manual de las primeras tareas. El paquete completo se termina como preparación de E7.

Si falta acceso a Linear, se entrega el paquete validado y se registra «publicación pendiente».

## Fuentes

| Tema | Fuente | Uso |
|---|---|---|
| Rediseño | `post-mortem.md` | Requisitos de la cohorte 3 |
| Plan de tareas | `../skills/create-implementation-plan/SKILL.md` | Contrato del paquete |
| Publicación | [convert-tasks-to-linear](https://github.com/kumanday/OpenSymphony/tree/main/.agents/skills/convert-tasks-to-linear) | Validación, dry-run y publicación |
| MCP | [Model Context Protocol](https://modelcontextprotocol.io) | Definición del protocolo |
| Orquestación | [OpenSymphony](https://github.com/kumanday/OpenSymphony) | Demo de E7 |

## Regeneración

Editar `build-deck.py`, ejecutar `python3 build-deck.py` y exportar el PDF con impresión Chromium a 1280 × 720, fondos habilitados y sin encabezados. Las capturas de `verificacion/` corresponden a esta versión.
