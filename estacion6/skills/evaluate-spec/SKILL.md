---
name: evaluate-spec
description: |
  Evalúa si una especificación está lista para convertirse en un plan de
  implementación. Revisa tres lentes (producto, TDD y diseño), asigna una
  nota de A a D y devuelve los vacíos con evidencia y la corrección mínima.
  Úsala antes de create-implementation-plan.
---

# Evaluate Spec

## Propósito

Decidir con evidencia si una especificación permite planificar e implementar
sin que el agente tenga que adivinar. La skill no reescribe la spec: la
evalúa, señala vacíos y propone la corrección mínima para cada uno.

Una spec puede leerse bien y aun así no estar lista. La pregunta que responde
esta skill es: **¿un agente podría convertir esto en tareas verificables sin
este chat?**

## Cuándo usarla

- Antes de ejecutar `create-implementation-plan`.
- Después de cambiar el alcance o recibir una spec de otra persona.
- Para revisar en pareja la spec de otro participante.

## Entradas

Pide o localiza, sin inventar rutas:

- La spec o PRD (por ejemplo, artefactos de Inception y Construction).
- `design.md` del repositorio, si existe.
- `AGENTS.md`, `README.md` y el estado actual del repo.
- Si el equipo trabaja con TDD: la declaración de cómo se escriben y ejecutan
  las pruebas (runner, comando, ubicación).

Si falta un artefacto, regístralo como vacío. No lo reconstruyas de memoria.

## Las tres lentes

Evalúa cada criterio como **Cumple**, **Parcial** o **Falta**, citando la
ruta y la sección o línea que lo respalda. Los criterios marcados con (*) son
críticos.

### 1. Producto: información mínima

| Criterio | Qué buscar |
|---|---|
| P1 (*) Problema y usuario | Para quién es y qué problema resuelve. |
| P2 (*) Alcance | Qué entra en esta ronda, expresado como capacidades concretas. |
| P3 (*) Fuera de alcance | Qué queda afuera de forma explícita. |
| P4 (*) Reglas de negocio | Reglas identificables (por ejemplo, BR-XXX-01) y sin contradicciones. |
| P5 Criterio de éxito | Cómo se sabe que el producto cumple su objetivo. |
| P6 Decisiones pendientes | Preguntas abiertas listadas, no escondidas en el texto. |

### 2. TDD: lo verificable

| Criterio | Qué buscar |
|---|---|
| T1 (*) Aceptación observable | Cada requisito tiene un resultado que se puede observar. |
| T2 (*) Casos de prueba | Entradas y resultados esperados, incluidos errores y bordes. |
| T3 Runner y comando | Cómo se ejecutan las pruebas en este repo. Si no existe, es un vacío. |
| T4 Declaración TDD | Si el equipo decidió trabajar con TDD, está escrito: pruebas antes del código y dónde viven. Si no lo decidió, márcalo N/A; no lo impongas. |

### 3. Diseño: cómo se construye y cómo se ve

| Criterio | Qué buscar |
|---|---|
| D1 (*) Arquitectura | Componentes, datos e integraciones, aunque sea mínimo. |
| D2 Contratos | APIs, eventos o esquemas que otras tareas van a consumir. |
| D3 design.md | Sistema visual, componentes y patrones para las tareas de interfaz. Si el producto no tiene interfaz, N/A. |
| D4 Restricciones | Requisitos no funcionales: seguridad, datos personales, rendimiento, despliegue. |

## Nota global

| Nota | Significado | Siguiente paso |
|---|---|---|
| **A** | Lista para implementar. Todos los críticos cumplen. | Pasar a `create-implementation-plan`. |
| **B** | Lista con supuestos. Ningún crítico falta; los parciales tienen un supuesto escrito y aceptado. | Planificar y registrar los supuestos en las tareas. |
| **C** | Necesita decisiones. Falta al menos un crítico, pero el alcance existe. | Resolver los vacíos críticos antes de planificar. |
| **D** | Todavía no es una spec. Falta el alcance o no hay requisitos verificables. | Volver a la definición (estaciones 2, 4 y 5). |

Solo una spec con nota **A** o **B** pasa a planificación.

## Salida

Escribe `docs/spec-review.md` con:

1. Nota global y una frase que la justifique.
2. Tabla por lente: criterio, estado, evidencia (ruta y sección), corrección mínima.
3. Los tres vacíos más graves, ordenados por impacto en la implementación.
4. Supuestos propuestos para los parciales, marcados como **pendientes de
   aprobación**.

## Reglas

- No modifiques la spec salvo que te lo pidan explícitamente.
- No apruebes un criterio sin evidencia citada.
- No inventes requisitos, comandos ni decisiones. Si algo no está, es un vacío.
- No conviertas TDD en obligación si el equipo no lo declaró.
- Si la spec es grande, evalúa primero el alcance de esta ronda.
