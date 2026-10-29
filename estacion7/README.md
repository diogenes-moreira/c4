# Estación 7: Del backlog al merge

Un laboratorio: implementas con un agente la primera tarea de tu producto, la revisas con tu pareja y la mergeas. Todo sobre **tu repo** y **tu rebanada**.

**LLM → Coding agent → Arnés → Loop → Orquestador → MCP**

## Income

Lo que traes de la estación 6 (detalle en la [preparación](preparacion.md)):

- `docs/spec-rebanada.md`: la spec mínima de un solo flujo de tu producto.
- `docs/spec-review.md` con nota A o B.
- Un plan de 3 a 6 tareas en `docs/tasks/`.
- Claude Code funcionando dentro de tu repo.

Si llegas sin algo de esto, la clase tiene una vía rápida en los primeros 30 minutos.

## Outcome

**La primera tarea de tu rebanada implementada, revisada en pareja y mergeada**, con el enlace del PR en el roadmap del grupo.

## En clase (120 minutos)

| Min | Bloque | Sales con |
|---|---|---|
| 0–10 | Dónde estamos | El plan hasta el Demo Day |
| 10–40 | Spec mínima y plan (vía rápida) | Spec A o B y de 3 a 6 tareas |
| 40–50 | Demo en vivo | Una tarea que pasa por agente, PR, review y merge |
| 50–95 | Laboratorio | Tu primer PR abierto |
| 95–110 | Review cruzado en parejas | PR revisado y mergeado |
| 110–120 | Cierre | Enlace en el roadmap y tarea para E8 |

## Tu tarea para E8 (miércoles 4 de noviembre)

1. TASK-001 mergeada y su enlace en el roadmap.
2. TASK-002 en un PR abierto o mergeado.
3. Tu rebanada corriendo en local, con el comando documentado en el README de tu repo.
4. El flujo de la rebanada escrito paso a paso, para convertirlo en test E2E en E8.

## Material

- [Preparación](preparacion.md): qué traer el lunes.
- [Guía del laboratorio](laboratorio.md): los pasos y prompts de la clase.
- [Plantilla de spec mínima](plantillas/spec-minima.md).
- [Presentación HTML](estacion7.html), [PDF](estacion7.pdf) y [PowerPoint](estacion7.pptx). Se generan con [`fuente/build-deck.py`](fuente/build-deck.py) y [`fuente/build-pptx.py`](fuente/build-pptx.py).
- Skills: [`evaluate-spec`](../estacion6/skills/evaluate-spec/SKILL.md) y [`create-implementation-plan`](../estacion6/skills/create-implementation-plan/SKILL.md).

## Por qué cambió esta estación

A mitad de la cohorte 5 los estudiantes no habían avanzado en su propio producto: las sesiones fueron clases magistrales sobre ejemplos. Desde E7 cada sesión trabaja sobre el repo de cada estudiante y termina con algo que funciona. La meta del Demo Day es **una rebanada funcionando de punta a punta**. La orquestación con OpenSymphony queda como paso opcional, una vez que el ciclo manual funciona.

## Refuerzo y dudas

Tutoría del jueves 5 de noviembre y el grupo de la cohorte. Un bloqueo de más de 10 minutos se reporta con el paso, el comando y el error exacto.
