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
| 0–8 | 1–4 | Apertura | Mostrar la salida de hoy. Presentarse en 2 minutos (slide 2). Recorrer el mapa completo (slide 3) y la ruta por módulos (slide 4). |
| 8–25 | 5–7 | 1 · Del LLM al orquestador | Dos piezas por slide, 3 min cada una. Cerrar con el ejercicio de 5 min: cada uno ubica su herramienta en el mapa y dice qué pieza le falta. |
| 25–50 | 8–11 | 2 · Evaluar la spec | 2 min contraste ambigua/preparada. 3 min las tres lentes. 3 min la nota ABCD. 17 min de práctica con `evaluate-spec`. |
| 50–55 | 12 | Pausa | Al volver, preguntar qué nota sacaron dos o tres personas. |
| 55–72 | 13–15 | 3 · design.md + Linear | 5 min fuentes de verdad. 5 min design.md con la plantilla abierta. 5 min Linear vía MCP. 2 min de preguntas. |
| 72–105 | 16–20 | 4 · Del plan al grafo | 2 min de AIDLC a tareas. 2 min la skill. 2 min el grafo: qué tareas están listas. 2 min publicación con dry-run. 25 min de práctica en parejas. |
| 105–112 | 21 | 5 · Loop y orquestador | Recorrer el ciclo de una tarea. Aclarar qué se hace a mano en E7 y qué automatiza el orquestador. |
| 112–120 | 22–23 | Cierre | Responder el estacionamiento, checklist de preparación de E7 y dónde están las skills. |

En caso de retraso, proteger los dos bloques de práctica (módulos 2 y 4). El módulo 1 se puede dar en 10 minutos y el 5 en 3.

## Reglas para el instructor

Salen de la clase de C4 ([análisis](analisis-clase-c4.md)), donde no hubo práctica y el objetivo llegó después de 1 h 20 min.

- **Estacionamiento:** una pregunta que no está en la pieza resaltada del mapa se anota en el chat o en una pizarra y se responde en el cierre. Responderla en el momento solo si cabe en un minuto.
- **Reloj visible:** los bloques de práctica empiezan a la hora del guion aunque la explicación anterior no haya terminado.
- **Sin recorridos de herramientas:** mostrar solo lo que el participante usa hoy. Modelos, benchmarks, suscripciones y observabilidad quedan en `recursos.md`.
- **Presentación personal:** dos minutos como máximo.

## Módulo 2: cómo conducir la evaluación

1. Cada participante abre su repo y le pide al arnés que lea y siga `skills/evaluate-spec/SKILL.md` (prompt en `../ejemplo-y-prompts.md`).
2. La skill escribe `docs/spec-review.md` con la nota y los vacíos citados.
3. Corrigen el vacío más grave y vuelven a evaluar. Interesa el cambio de nota, no llegar a A.
4. Si la spec queda en C o D, el participante sigue con EntreVista AI en el módulo 4 y registra su propio pendiente.
5. Para mostrar cómo se ve una salida real, abrir `../ejemplos/spec-review-entrevista-ai.md`: auth-lambda saca B y el resto del MVP C, porque solo esa unidad tiene diseño funcional. Sirve para explicar por qué la nota va por ola.

Sobre ABCD: la rúbrica no estaba definida en el post-mortem. Esta versión la concreta: A lista, B lista con supuestos aceptados, C faltan criterios críticos, D todavía no es spec. TDD se exige solo si el equipo lo declaró.

## Módulo 3: design.md y fuentes de verdad

- La spec dice qué; `design.md` dice cómo se ve y cómo se construye; los archivos de tarea son el contrato; Linear lleva el estado; el PR y los tests son la evidencia.
- No hay sincronización automática entre archivos de tarea e issues. Si cambia un contrato, se actualizan los dos.
- Publicar en un proyecto observado por un orquestador puede disparar trabajo. Usar un proyecto de preparación.

## Módulo 4: práctica en parejas

12 min para generar el paquete con `create-implementation-plan`; 7 min de revisión cruzada (cobertura, ciclos, tareas listas); 6 min de dry-run con `convert-tasks-to-linear` o carga manual de las primeras tareas. El paquete completo se termina como preparación de E7.

Si falta acceso a Linear, se entrega el paquete validado y se registra «publicación pendiente».

## Preguntas frecuentes

Son preguntas que hicieron participantes de C4.

- **¿Esto reemplaza AIDLC?** No. AIDLC deja la spec y el diseño de cada unidad; aquí cada unidad se convierte en una ola de tareas (slide 16).
- **¿Es obligatorio usar Linear?** No. Es lo recomendado por su API y su capa gratuita. Con Jira o ClickUp, se pide al agente una skill equivalente a `convert-tasks-to-linear` para ese tracker.
- **¿Puedo usar cualquier modelo con cualquier arnés?** Casi siempre sí, pero los planes de suscripción limitan con qué arnés se pueden usar. Revisar los términos de cada proveedor.
- **En un proyecto grande, ¿qué hago con los archivos de tareas viejas?** Antes de borrarlos o archivarlos, extraer lo que sirve para la documentación o la memoria del proyecto. Conviene conservar la ola anterior como referencia.
- **¿Cómo reviso tantos PRs?** Es tema de E7: review automatizado con límites y contexto del grafo para que el agente pueda rechazar pedidos que pertenecen a otra tarea.

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
