# Experiencia del estudiante: revisión del recorrido

Revisión del material de la cohorte 4, estación por estación, hecha el 28 de octubre de 2026. Objetivo: que el estudiante sepa siempre qué leer primero, qué tiene que entregar y cómo eso alimenta la siguiente estación.

## Qué funciona

- **El hilo existe.** Cada estación pide como entrada lo que produjo la anterior: Vision Board → PRD → Inception → Construction → tareas → código → tests → infraestructura → observabilidad.
- **Las guías de E1, E2, E8, E9 y E11** tienen tarea concreta, checklist y fechas.
- **EntreVista AI** acompaña desde E4 hasta E11 y permite mostrar continuidad con un mismo producto.

## Fricciones

| # | Fricción | Dónde | Efecto en el estudiante |
|---|---|---|---|
| 1 | La estación 3 no tiene carpeta | E3 | No hay material para repasar «Ingeniería agéntica», que es la base de E6 y E7. |
| 2 | Cinco formatos distintos para el punto de entrada | README (E1, E2, E6, E7, E10), runbook (E4, E5), `clase-N-estudiante.md` (E8, E9, E11), solo archivos sueltos (nivelación 2) | Cada semana hay que descubrir dónde empezar. |
| 3 | E8, E9 y E11 dicen «Clase» en lugar de «Estación» | Guías de esas estaciones | El mapa usa estaciones; las guías, clases. Parece otro programa. |
| 4 | La tarea no siempre está escrita | E7 (solo «Después de clase»), E10 (solo recursos), E12 | No queda claro qué traer a la siguiente estación. |
| 5 | El ejemplo cambia de producto | SkillWall (E1), AgentVault (E2), EntreVista AI (E4–E6, E11), producto propio de los repos (E8, E9) | El estudiante no ve un mismo caso atravesar todo el recorrido. |
| 6 | El home listaba las carpetas fuera de orden | README raíz | Corregido en esta revisión: ahora la tabla sigue el orden del programa. |
| 7 | El refuerzo solo se explica en E1 y E2 | Guías | Quien entra a mitad de semana no sabe que existe. Corregido en el home. |
| 8 | Nivelación 2 no tiene README y la 1 no está | `nivelacion2/` | No queda claro cuándo conviene hacerla. |

## Formato propuesto para cada estación

Un `README.md` en la carpeta de cada estación, siempre con estas secciones y en este orden:

1. **De qué se trata** — dos o tres frases y dónde queda en el mapa.
2. **Llegas con** — los artefactos de la estación anterior.
3. **Antes de la clase** — instalaciones, accesos y lectura, con tiempo estimado.
4. **En clase** — ruta por módulos con minutos.
5. **Tu tarea** — lista numerada y verificable.
6. **Te vas con** — el entregable, en una línea. Es lo que la siguiente estación pide en «Llegas con».
7. **Material** — slides, guías, repos y skills, con enlaces.
8. **Refuerzo y dudas** — día del refuerzo y canal.

Los runbooks y guías largas se mantienen, pero se enlazan desde el README.

## Próximos pasos sugeridos

| Prioridad | Acción |
|---|---|
| Alta | Publicar el material de E3. |
| Alta | Escribir la tarea de E7 y E10 con su entregable. |
| Media | Normalizar E4, E5, E8, E9 y E11 al formato de README, renombrando «Clase» por «Estación». |
| Media | Agregar un README a la nivelación 2 con cuándo hacerla. |
| Baja | Usar EntreVista AI como ejemplo también en E1, E2, E8 y E9, o explicar en cada estación por qué cambia. |
