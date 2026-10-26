# design.md

Plantilla para el repositorio de tu proyecto. Cópiala como `design.md` en la
raíz y complétala. El agente la lee antes de cualquier tarea que toque la
interfaz o los contratos entre componentes.

La spec dice **qué** debe hacer el producto. Este archivo dice **cómo se ve y
cómo se construye**. Si una decisión ya está aquí, ninguna tarea la repite: la
enlaza.

## 1. Principios

- Tres o cuatro frases sobre la experiencia que buscamos.
- Ejemplo: «Primero el dato que el reclutador necesita para decidir».

## 2. Sistema visual

| Token | Valor | Uso |
|---|---|---|
| Color primario | `#______` | Acciones principales |
| Color de texto | `#______` | Texto general |
| Tipografía | ______ | Títulos y texto |
| Espaciado base | __ px | Márgenes y separaciones |

Si usas una librería de componentes, nómbrala con su versión.

## 3. Componentes y patrones

| Componente | Cuándo se usa | Cuándo no |
|---|---|---|
| ______ | ______ | ______ |

Estados obligatorios para cada pantalla: carga, vacío, error y éxito.

## 4. Arquitectura y contratos

- Componentes principales y cómo se comunican.
- Contratos que otras tareas consumen (endpoints, eventos, esquemas). Enlaza
  el archivo donde vive cada uno.

## 5. Decisiones

| Fecha | Decisión | Por qué | Enlace |
|---|---|---|---|
| ______ | ______ | ______ | ADR o issue |

## 6. Qué no hacer

- Lista corta de patrones prohibidos en este proyecto.

## 7. Cómo se verifica

- Cómo comprobar que una tarea respeta este diseño (capturas, tests visuales,
  revisión humana).
