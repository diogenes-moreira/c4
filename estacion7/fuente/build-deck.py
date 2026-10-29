"""Genera ../estacion7.html: la estación 7 como laboratorio del primer merge.

Reutiliza los estilos y el mapa "estás aquí" de la estación 6.
Uso: python3 build-deck.py
"""

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("e6deck", HERE.parents[1] / "estacion6" / "fuente" / "build-deck.py")
e6 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(e6)

MAP, CSS, mapbar = e6.MAP, e6.CSS, e6.mapbar
CSS += """
.slice{display:grid;grid-template-columns:repeat(5,1fr);gap:0;margin-top:18px;border:1px solid #2A2A2A}
.slice div{padding:14px 14px 16px;border-left:1px solid #2A2A2A;font-size:19px;line-height:1.3;color:#B3B3B3;min-height:150px}
.slice div:first-child{border-left:0}
.slice b{display:block;color:white;font-size:21px;margin-bottom:8px}
.slice .band{grid-column:1/-1;background:#1F2A05;color:#C8E600;font-size:20px;font-weight:700;padding:12px 14px;border-left:0;border-top:1px solid #C8E600;min-height:0}
.cal td,.cal th{padding:7px 14px;font-size:18px}
pre.prompt{background:#141414;border:1px solid #2A2A2A;padding:16px 20px;font-size:19px;line-height:1.35;color:#E6E6E6;white-space:pre-wrap;margin:14px 0 0;font-family:Menlo,Consolas,monospace}
"""

SLIDES = []


def slide(title, active, module, body):
    SLIDES.append((title, active, module, body))


# ---------------------------------------------------------------- Apertura
slide("Del backlog al merge", [], "APERTURA", """
<div class="cover">
<p class="eyebrow">DEL BACKLOG AL MERGE · ESTACIÓN 7</p>
<h1>Hoy todos salen con un PR mergeado</h1>
<p class="lead">Sobre tu repo y tu producto. Teoría corta, laboratorio largo y review en parejas.</p>
<p class="take">Outcome de hoy: la primera tarea de tu rebanada, implementada con un agente, revisada y mergeada.</p>
</div>""")

slide("Una rebanada, de punta a punta", [], "APERTURA", """
<p class="eyebrow">EL CAMBIO DE PLAN</p>
<h1>Una rebanada, de punta a punta</h1>
<div class="slice">
<div><b>Spec</b>Un flujo, tres criterios de aceptación</div>
<div><b>Código</b>Tareas implementadas con agentes</div>
<div><b>Tests</b>Un E2E y uno de API</div>
<div><b>Deploy</b>Corriendo fuera de tu máquina</div>
<div><b>Observable</b>Un dashboard que muestra que funciona</div>
<div class="band">Tu rebanada: un solo flujo que un usuario completa de principio a fin</div>
</div>
<p class="take">En el Demo Day se muestra una rebanada que funciona, no un producto a medias.</p>""")

slide("Tres semanas hasta el Demo Day", [], "APERTURA", """
<p class="eyebrow">EL PLAN HASTA EL 18 DE NOVIEMBRE</p>
<h1>Cada sesión termina con algo que funciona</h1>
<table class="cal tight">
<tr><th style="width:18%">Fecha</th><th style="width:30%">Sesión</th><th>Outcome sobre tu rebanada</th></tr>
<tr><td>Lun 2 nov</td><td>E7 · Laboratorio</td><td>Plan de tareas y la primera mergeada</td></tr>
<tr><td>Mié 4 nov</td><td>E8 · Calidad</td><td>Un flujo E2E y un test de API</td></tr>
<tr><td>Jue 5 nov</td><td>Tutoría</td><td>Segunda tarea mergeada</td></tr>
<tr><td>Lun 9 nov</td><td>E9 · Despliegue</td><td>Tu rebanada corriendo fuera de tu máquina</td></tr>
<tr><td>Mié 11 nov</td><td>E10 · Seguridad</td><td>Secretos y dependencias revisados; flujo completo</td></tr>
<tr><td>Lun 16 nov</td><td>E11 · Observabilidad</td><td>Un dashboard y el video de 3 minutos</td></tr>
<tr><td>Mié 18 nov</td><td>Demo Day</td><td>Tu rebanada funcionando en vivo</td></tr>
</table>
<p class="take">Cada enlace va al roadmap del grupo. Si quedas dos estaciones atrás, te buscamos antes de la siguiente.</p>""")

slide("La ruta de hoy", [], "APERTURA", """
<p class="eyebrow">120 MINUTOS · 85 DE PRÁCTICA</p>
<h1>La ruta de hoy</h1>
<table class="modules">
<tr><th style="width:12%">Min</th><th style="width:34%">Bloque</th><th>Sales con</th></tr>
<tr><td>0–10</td><td>Dónde estamos</td><td>El plan hasta el Demo Day</td></tr>
<tr><td>10–40</td><td>Spec mínima y plan</td><td>Spec con nota A o B y de 3 a 6 tareas</td></tr>
<tr><td>40–50</td><td>Demo en vivo</td><td>Una tarea que pasa por agente, PR, review y merge</td></tr>
<tr><td>50–95</td><td>Laboratorio</td><td>Tu primer PR abierto</td></tr>
<tr><td>95–110</td><td>Review cruzado</td><td>PR revisado y mergeado</td></tr>
<tr><td>110–120</td><td>Cierre</td><td>Enlace en el roadmap y tarea para E8</td></tr>
</table>
<p class="take">Si trajiste spec y plan, el bloque de 10 a 40 es tuyo para empezar a implementar.</p>""")

# ---------------------------------------------------------------- Módulo 1
slide("La spec mínima", ["Arnés"], "SPEC MÍNIMA", """
<p class="eyebrow">VÍA RÁPIDA · UNA PÁGINA</p>
<h1>La spec mínima de una rebanada</h1>
<div class="three">
<div><span class="num">1</span><h2>Problema y usuario</h2><p class="small">Qué le duele a quién. Un solo usuario.</p></div>
<div><span class="num">2</span><h2>El flujo</h2><p class="small">De 3 a 7 pasos, desde que empieza hasta que obtiene el resultado.</p></div>
<div><span class="num">3</span><h2>Tres criterios</h2><p class="small">Cada uno se comprueba con un test. Más lo que queda fuera.</p></div>
</div>
<p class="take">Plantilla: estacion7/plantillas/spec-minima.md · Evalúala con evaluate-spec hasta A o B.</p>""")

slide("Ejemplo de spec mínima", ["Arnés"], "SPEC MÍNIMA", """
<p class="eyebrow">EJEMPLO · ENTREVISTA AI</p>
<h1>«El reclutador crea una campaña y recibe el link»</h1>
<div class="two">
<div><h2>Flujo</h2><p class="small">1. Entra al dashboard.<br>2. Crea una campaña con el cargo y tres preguntas.<br>3. La guarda.<br>4. Ve el link para compartir.</p><p class="example">Fuera: login, edición, Telegram, evaluación.</p></div>
<div><h2>Criterios de aceptación</h2><p class="small">Una campaña válida aparece como «Activa».<br>Sin nombre del cargo, muestra error y no guarda.<br>El link abre una página con el nombre del cargo.</p></div>
</div>
<p class="take">Chica, completa y comprobable. Todo lo demás espera a la siguiente rebanada.</p>""")

slide("De la spec al plan", ["Arnés", "Orquestador"], "SPEC MÍNIMA", """
<p class="eyebrow">CREATE-IMPLEMENTATION-PLAN</p>
<h1>De 3 a 6 tareas, la primera en una hora</h1>
<div class="graph">
<div class="node ready"><b>TASK-001</b>Proyecto creado y un test que corre</div><div class="arrow">→</div>
<div class="node"><b>TASK-002</b>Modelo y guardado de la campaña</div><div class="arrow">→</div>
<div class="node"><b>TASK-003</b>Formulario con validación</div>
<div class="node"><b>TASK-004</b>Link para compartir</div><div class="arrow">→</div>
<div class="node"><b>TASK-005</b>Página pública del link</div><div class="arrow">→</div>
<div class="node"><b>…</b>Nada más hasta el Demo Day</div>
</div>
<p class="take">La primera tarea siempre deja el proyecto andando con un test. Sin eso, no hay dónde verificar nada.</p>""")

slide("Spec y plan", ["Arnés"], "SPEC MÍNIMA", """
<p class="eyebrow">TU TURNO · 30 MIN</p>
<h1>Spec mínima y plan</h1>
<div class="steps">
<div><b>10 min</b><span>Completa docs/spec-rebanada.md con la plantilla.</span></div>
<div><b>08 min</b><span>Evalúala con evaluate-spec y corrige el vacío más grave.</span></div>
<div><b>12 min</b><span>Genera de 3 a 6 tareas con create-implementation-plan.</span></div>
</div>
<p class="take">¿Ya lo traías? Empieza ya el laboratorio con tu primera tarea.</p>""")

# ---------------------------------------------------------------- Demo
slide("Una tarea atraviesa el loop", ["Coding agent", "Loop"], "DEMO EN VIVO", """
<p class="eyebrow">DEMO EN VIVO · 10 MIN</p>
<h1>Una tarea, de punta a punta</h1>
<div class="chain">
<div class="on"><strong>Tarea</strong><span>Alcance y criterio claros.</span></div><i>→</i>
<div><strong>Agente</strong><span>Resume el plan y lo implementa.</span></div><i>→</i>
<div><strong>Tests</strong><span>Corren y pasan. Los corres tú.</span></div><i>→</i>
<div><strong>PR</strong><span>Diff, criterio y resultado.</span></div><i>→</i>
<div><strong>Review y merge</strong><span>Una persona aprueba.</span></div>
</div>
<p class="take">El agente propone y ejecuta. Tú lees el resumen, corres el test y decides el merge.</p>""")

slide("El prompt de implementación", ["Coding agent"], "DEMO EN VIVO", """
<p class="eyebrow">COPIA ESTE PROMPT · ESTÁ EN LABORATORIO.MD</p>
<h1>El prompt de implementación</h1>
<pre class="prompt">Toma únicamente la tarea docs/tasks/001-*.md. Léela completa, junto con
docs/spec-rebanada.md. Antes de escribir código, resume en 5 líneas el
alcance y el plan. Después implementa el cambio mínimo, escribe el test
del criterio de aceptación y córrelo. Entrégame: archivos cambiados,
comando de test y resultado. No toques nada fuera del alcance de la tarea.</pre>
<p class="take">Lee el resumen antes de dejarlo avanzar. Si se sale del alcance, detenlo.</p>""")

# ---------------------------------------------------------------- Laboratorio
slide("Laboratorio", ["Coding agent", "Loop"], "LABORATORIO", """
<p class="eyebrow">TU TURNO · 45 MIN</p>
<h1>Tu primer PR</h1>
<div class="steps">
<div><b>01</b><span>Rama con el ID de la tarea: git checkout -b task-001.</span></div>
<div><b>02</b><span>Pide la implementación con el prompt.</span></div>
<div><b>03</b><span>Corre tú el test y revisa el diff.</span></div>
<div><b>04</b><span>Commit, push y gh pr create, con criterio y resultado en la descripción.</span></div>
</div>
<p class="take">¿Trabado más de 10 minutos? Levanta la mano con el paso, el comando y el error exacto.</p>""")

slide("Review cruzado", ["Loop"], "LABORATORIO", """
<p class="eyebrow">EN PAREJAS · 15 MIN</p>
<h1>Revisa el PR de tu pareja</h1>
<div class="checklist">
<p><b>01</b>Hace lo que dice la tarea y nada más.</p>
<p><b>02</b>Hay un test del criterio de aceptación y pasa.</p>
<p><b>03</b>No hay secretos, claves ni archivos generados de más.</p>
<p><b>04</b>Entiendes el código lo suficiente para explicarlo.</p>
</div>
<p class="take">Deja al menos un comentario. Si todo está bien, aprueba y haz merge.</p>""")

slide("Lo que viene: orquestar", ["Orquestador", "MCP"], "LABORATORIO", """
<p class="eyebrow">CUANDO EL CICLO MANUAL FUNCIONA</p>
<h1>Lo que hiciste a mano, un orquestador lo repite</h1>
<div class="chain">
<div><strong>Linear</strong><span>Tareas con dependencias.</span></div><i>→</i>
<div class="on"><strong>Orquestador</strong><span>Toma las tareas listas.</span></div><i>→</i>
<div><strong>Agentes</strong><span>Un workspace por tarea.</span></div><i>→</i>
<div><strong>PR y review</strong><span>Automático, con merge humano.</span></div>
</div>
<p class="take">Primero el ciclo manual, bien hecho. La orquestación con OpenSymphony es opcional hasta el Demo Day.</p>""")

# ---------------------------------------------------------------- Cierre
slide("Antes de la estación 8", [], "CIERRE", """
<p class="eyebrow">INCOME DE E8 · MIÉRCOLES 4 DE NOVIEMBRE</p>
<h1>Llega a E8 con esto</h1>
<div class="checklist">
<p><b>01</b>TASK-001 mergeada y su enlace en el roadmap.</p>
<p><b>02</b>TASK-002 en un PR abierto o mergeado.</p>
<p><b>03</b>Tu rebanada corriendo en local con un comando documentado en el README.</p>
<p><b>04</b>El flujo de la rebanada escrito para convertirlo en test E2E.</p>
</div>
<p class="source">E8 trabaja sobre tu repo: los tests serán de tu rebanada.</p>""")


def render():
    total = len(SLIDES)
    out = []
    for n, (title, active, module, body) in enumerate(SLIDES, 1):
        out.append(
            f'<section class="slide" contenteditable="true" spellcheck="true" aria-label="{n}. {title}">'
            f"{mapbar(active)}{body.strip()}"
            f'<footer class="footer"><span>Hardcore AI by 30X · Estación 7 · {module}</span>'
            f"<span>{n:02d} / {total:02d}</span></footer></section>"
        )
    html = (
        '<!doctype html><html lang="es"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        "<title>Estación 7 · Del backlog al merge</title>"
        f"<style>{CSS}</style></head><body><main class=\"deck\">"
        + "\n".join(out)
        + "</main></body></html>\n"
    )
    target = HERE.parent / "estacion7.html"
    target.write_text(html, encoding="utf-8")
    print(f"{total} slides → {target}")


if __name__ == "__main__":
    render()
