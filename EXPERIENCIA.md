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

## Lo que dice la cohorte (encuesta NPS)

Comentarios abiertos de la encuesta NPS, recibidos el 28 de octubre de 2026. Se resumen sin datos personales; no incluyen los puntajes.

| Tema | Lo que dicen | Cuántos lo mencionan | Fricción relacionada |
|---|---|---|---|
| Falta de hilo conductor | Las sesiones no se conectan entre sí; recién ahora conocieron cómo estaba planeado el curso. | 5 de 10 | 2, 4, 5 |
| Sin empalme entre profesores | No hay contexto entre quien sale y quien entra; se notó improvisación. | 3 de 10 | Nueva (10) |
| Entregables poco claros | A mitad del curso no tienen claro qué entregar ni algo concreto. | 2 de 10 | 4 |
| Material desordenado | Piden organizar el material y seguir el playbook tal cual. | 3 de 10 | 1, 2 |
| Mucha teoría o demo, poca práctica | Las clases fueron teóricas o de ver al profesor; la última, que mezcló teoría y práctica real, les resultó más concreta. | 1 de 10 | Confirma el rediseño de E6 |
| Claridad al enseñar | Un profesor domina el tema pero no lo explica con claridad. | 1 de 10 | Nueva (11) |
| Lo positivo | Buenas sesiones puntuales; la conversación de hoy fue necesaria y valoran el compromiso del instructor. Se acordó una clase de reposición. | 3 de 10 | |

**Lo que piden, en sus palabras resumidas:** primero organizar el material; después una o dos sesiones para resolver dudas de las cinco estaciones que sintieron autodidactas; y recién entonces retomar con un roadmap único del grupo.

### Fricciones nuevas

| # | Fricción | Efecto |
|---|---|---|
| 10 | No hay traspaso entre profesores | Cada estación arranca sin saber qué se vio, qué quedó pendiente ni en qué estado está el grupo. |
| 11 | Estilos de clase muy distintos | Algunas sesiones son exposición larga; otras, práctica. El estudiante no sabe qué esperar. |

## Plan de recuperación

### 1. Material organizado (en curso)

- Home con el recorrido, las entradas y salidas de cada estación: hecho.
- Normalizar el README de cada estación al formato de abajo: pendiente.
- Publicar E3 y escribir las tareas de E7 y E10: pendiente.

### 2. Dos sesiones de puesta al día

Cubren E1 a E6. Cada participante trabaja sobre su propio producto; el instructor circula y resuelve. Al final de cada sesión, cada uno actualiza su fila del roadmap.

**Sesión A · Definir y diseñar el qué (120 min)**

| Min | Bloque | Salida |
|---|---|---|
| 0–15 | El mapa del programa y el hilo del producto (home del repo) | Todos saben dónde está cada estación y qué produce |
| 15–45 | E1 y E2: clínica de Vision Board y PRD | PRD v1 revisado o con sus vacíos anotados |
| 45–60 | E3: chequeo del entorno agéntico (arnés, MCP, una skill funcionando) | Entorno probado |
| 60–65 | Pausa | |
| 65–110 | E4: Inception con AI-DLC sobre el PRD propio | Artefactos de Inception iniciados o revisados |
| 110–120 | Estado personal en el roadmap | Fila actualizada |

**Sesión B · Diseñar el cómo y dejarlo listo (120 min)**

| Min | Bloque | Salida |
|---|---|---|
| 0–10 | Estado del grupo según el roadmap | Prioridades de la sesión |
| 10–50 | E5: Construction de una unidad | Diseño funcional y reglas de una unidad |
| 50–55 | Pausa | |
| 55–95 | E6: `evaluate-spec` y plan de tareas de esa unidad | Spec con nota y primeras tareas |
| 95–115 | Dudas abiertas | |
| 115–120 | Estado personal en el roadmap | Fila actualizada |

### 3. Roadmap único del grupo

Una tabla compartida, actualizada al cierre de cada sesión. Cada celda es **Listo**, **En curso** o **Pendiente**, con el enlace al artefacto.

| Participante | E1 Vision Board | E2 PRD | E3 Entorno | E4 Inception | E5 Construction | E6 Tareas | E7 PR | … |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

Sirve a la vez como seguimiento oportuno: si alguien queda dos estaciones atrás, se lo contacta antes de la clase siguiente.

### 4. Empalme entre profesores

Antes de cada estación, quien la dio completa esta nota y la comparte con quien sigue:

```markdown
## Empalme E<n> → E<n+1>
- Qué se vio (y qué se saltó del plan):
- Tarea que quedó y cómo se entrega:
- Estado del grupo (enlace al roadmap):
- Dudas frecuentes que quedaron abiertas:
- Qué necesita la siguiente estación que los estudiantes traigan:
```

Quien entra abre su clase con dos minutos de «dónde estamos», usando el mapa y esta nota.

### 5. Formato de clase

Teoría corta y práctica sobre el producto propio en cada sesión, con la práctica protegida por reloj. Es lo que la cohorte valoró de la última clase y lo que aplica el rediseño de E6 ([guion](estacion6/fuente/guion.md)).

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
| Alta | Dar las dos sesiones de puesta al día y abrir el roadmap del grupo. |
| Alta | Empezar el empalme entre profesores desde la próxima estación. |
| Alta | Publicar el material de E3. |
| Alta | Escribir la tarea de E7 y E10 con su entregable. |
| Media | Normalizar E4, E5, E8, E9 y E11 al formato de README, renombrando «Clase» por «Estación». |
| Media | Agregar un README a la nivelación 2 con cuándo hacerla. |
| Baja | Usar EntreVista AI como ejemplo también en E1, E2, E8 y E9, o explicar en cada estación por qué cambia. |
