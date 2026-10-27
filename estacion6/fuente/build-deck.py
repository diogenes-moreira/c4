"""Genera ../estacion6.html: el deck de la estación 6 con el mapa "estás aquí".

Uso: python3 build-deck.py
Después exportar el PDF con Chromium (1280 × 720, fondos habilitados).
"""

from pathlib import Path

MAP = ["LLM", "Coding agent", "Arnés", "Loop", "Orquestador", "MCP"]

CSS = """
:root{--lime:#C8E600}*{box-sizing:border-box}
body{margin:0;background:#262626;color:#E6E6E6;font-family:Calibri,Aptos,Arial,sans-serif;letter-spacing:0}
.deck{display:grid;gap:24px;padding:24px;justify-items:center}
.slide{position:relative;width:1280px;height:720px;padding:84px 64px 40px;background:#0A0A0A;overflow:hidden}
.map{position:absolute;top:24px;left:64px;right:64px;display:flex;align-items:center;gap:8px;font-size:15px;color:#666}
.map span{padding:5px 12px;border:1px solid #333;border-radius:999px;white-space:nowrap}
.map span.on{color:#0A0A0A;background:var(--lime);border-color:var(--lime);font-weight:700}
.map em{font-style:normal;color:#4D4D4D}
.map .here{margin-left:auto;color:#808080;font-size:13px;letter-spacing:.08em}
.eyebrow{color:var(--lime);font-size:18px;font-weight:700;margin:0 0 14px;letter-spacing:.04em}
h1{color:white;font-size:42px;line-height:1.08;margin:0 0 24px}
h2{color:white;font-size:24px;margin:0 0 12px}
p{font-size:24px;line-height:1.32;margin:0 0 14px}
.small{font-size:21px}.label{color:var(--lime);font-size:18px;font-weight:bold}.bad{color:#FF4444}
.take{background:#1F2A05;padding:16px 22px;font-size:24px;margin-top:22px}
.source{font-size:18px;color:#808080}a{color:inherit}
.footer{position:absolute;bottom:20px;left:64px;right:64px;display:flex;justify-content:space-between;color:#808080;font-size:12px}
.three{display:grid;grid-template-columns:repeat(3,1fr);gap:34px;margin-top:20px}
.three>div,.two>div{border-top:1px solid #2A2A2A;padding-top:18px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:46px;margin-top:20px}
.comparison{display:grid;grid-template-columns:1fr 1fr;gap:46px;margin-top:20px}
.comparison>div+div{border-left:1px solid #2A2A2A;padding-left:45px}
.comparison blockquote{margin:24px 0;font-size:40px;line-height:1.15;color:white}
.num{font-size:54px;color:var(--lime);display:block;margin-bottom:10px}
.example{color:#B3B3B3;font-size:21px}
table{border-collapse:collapse;width:100%;font-size:21px;line-height:1.25;margin-top:16px}
th{background:var(--lime);color:#1A1A1A;text-align:left;padding:12px 16px}
td{padding:13px 16px;border-bottom:1px solid #4D4D4D;vertical-align:top}
td:first-child{color:white;font-weight:bold}
code{font-size:20px;color:white}
.steps>div{display:flex;gap:30px;border-bottom:1px solid #4D4D4D;padding:16px 0;font-size:24px}
.steps b{color:var(--lime);min-width:96px}
.checklist p{border-bottom:1px solid #4D4D4D;padding:14px 0;font-size:24px;margin:0}
.checklist b{color:var(--lime);margin-right:22px}
.chain{display:flex;align-items:stretch;gap:12px;margin:26px 0}
.chain div{flex:1;border:1px solid #4D4D4D;padding:16px 14px}
.chain div.on{border-color:var(--lime)}
.chain strong{display:block;color:white;font-size:22px;margin-bottom:8px}
.chain span{font-size:18px;color:#B3B3B3;line-height:1.3;display:block}
.chain i{align-self:center;font-style:normal;color:var(--lime);font-size:28px;flex:0}
.grades{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:20px}
.grades div{border-top:4px solid #4D4D4D;padding-top:14px}
.grades div.ok{border-color:var(--lime)}
.grades b{font-size:64px;color:white;display:block;line-height:1}
.grades div.ok b{color:var(--lime)}
.grades strong{display:block;font-size:22px;color:white;margin:10px 0 6px}
.grades span{font-size:19px;color:#B3B3B3;line-height:1.3;display:block}
.graph{display:grid;grid-template-columns:1fr 40px 1fr 40px 1fr;align-items:center;row-gap:22px;margin-top:22px}
.node{border:1px solid #4D4D4D;padding:12px 14px;font-size:19px;line-height:1.25}
.node b{display:block;color:white;font-size:18px;letter-spacing:.03em}
.node.ready{border:2px solid var(--lime)}
.arrow{text-align:center;color:var(--lime);font-size:26px}
.legend{display:flex;gap:28px;font-size:18px;color:#B3B3B3;margin-top:20px}
.legend span:before{content:"";display:inline-block;width:14px;height:14px;margin-right:8px;vertical-align:-2px;border:1px solid #4D4D4D}
.legend span.r:before{border:2px solid var(--lime)}
.modules td:first-child{white-space:nowrap}
.tight td{padding:9px 16px}.tight th{padding:10px 16px}
.cover h1{font-size:60px;max-width:1000px}
.cover .lead{font-size:28px;max-width:950px;color:#E6E6E6}
.big{font-size:30px;line-height:1.3;color:white}
.bio{display:grid;grid-template-columns:380px 1fr;gap:56px;align-items:start;margin-top:4px}
.bio img{width:380px;height:500px;object-fit:cover;object-position:50% 30%;border-radius:4px}
.bio .rows>div{border-top:1px solid #2A2A2A;padding:12px 0}
.bio .rows strong{display:block;color:white;font-size:22px}
.bio .rows span{display:block;color:#B3B3B3;font-size:18px;line-height:1.3;margin-top:4px}
.slide:focus{outline:2px solid var(--lime)}
@media print{@page{size:1280px 720px;margin:0}body{background:#0A0A0A}.deck{display:block;padding:0}
.slide{margin:0;break-after:page}.slide:last-child{break-after:auto}.slide:focus{outline:none}}
"""


def mapbar(active):
    parts = []
    for i, name in enumerate(MAP):
        cls = ' class="on"' if name in active else ""
        parts.append(f"<span{cls}>{name}</span>")
        if i < len(MAP) - 1:
            parts.append("<em>→</em>")
    here = '<span class="here" style="border:0;padding:0">ESTÁS AQUÍ</span>' if active else ""
    return f'<nav class="map" aria-label="Mapa conceptual">{"".join(parts)}{here}</nav>'


SLIDES = []


def slide(title, active, module, body):
    SLIDES.append((title, active, module, body))


# ---------------------------------------------------------------- Apertura
slide("Del spec al harness", [], "APERTURA", """
<div class="cover">
<p class="eyebrow">DEL SPEC AL HARNESS · ESTACIÓN 6</p>
<h1>¿Tu spec está lista para implementar?</h1>
<p class="lead">Hoy evaluamos la spec, la convertimos en un grafo de tareas y la dejamos en Linear, lista para que un agente la ejecute en la estación 7.</p>
<p class="take">Salida de hoy: spec con nota A o B · design.md · paquete de tareas · grafo publicado o listo para publicar.</p>
</div>""")

slide("Quién les habla", [], "APERTURA", """
<div class="bio">
<img src="assets/presentador.webp" alt="Foto de Diógenes Moreira">
<div>
<p class="eyebrow">QUIÉN LES HABLA</p>
<h1 style="margin-bottom:6px">Diógenes Moreira</h1>
<p class="example" style="margin-bottom:12px">CTO de 30X</p>
<div class="rows">
<div><strong>5 años en Frubana, de VP of Engineering a CTO</strong><span>El equipo de tecnología pasó de 10 a casi 100 personas, organizado por verticales.</span></div>
<div><strong>8 años de tecnología en el sector público</strong><span>Ministerio Público Fiscal y fundador de la Unidad de Ciberdelincuencia (UFECI).</span></div>
<div><strong>Fractional CTO y advisor</strong><span>rintin, Masu, ONA Report y Atina.app. Docente de posgrado en la UBA.</span></div>
<div><strong>Autor</strong><span>Arquitectura para Vibe-Coders, Vibe Coding para Desarrolladores y El martes que no estás.</span></div>
</div>
</div>
</div>""")

slide("El mapa de la estación", MAP, "APERTURA", """
<p class="eyebrow">EL MAPA</p>
<h1>Seis piezas, una cadena</h1>
<table class="tight">
<tr><th style="width:20%">Pieza</th><th style="width:44%">Qué hace</th><th>Dónde la usamos</th></tr>
<tr><td>LLM</td><td>Interpreta y propone. No tiene manos.</td><td>Detrás de todo</td></tr>
<tr><td>Coding agent</td><td>Un LLM con herramientas: lee, edita, ejecuta.</td><td>Claude Code, Codex, OpenHands</td></tr>
<tr><td>Arnés</td><td>Contexto, permisos, skills y hooks alrededor del agente.</td><td>Módulos 2, 3 y 4</td></tr>
<tr><td>Loop</td><td>Planear, editar, probar y corregir hasta un criterio.</td><td>Módulo 5 y E7</td></tr>
<tr><td>Orquestador</td><td>Toma tareas listas, respeta dependencias, junta evidencia.</td><td>Módulo 5 y E7</td></tr>
<tr><td>MCP</td><td>Conecta el agente con sistemas externos como Linear o GitHub.</td><td>Módulos 3 y 4</td></tr>
</table>
<p class="take">La barra de arriba te dice en qué pieza estamos en cada momento.</p>""")

slide("La ruta de hoy", [], "APERTURA", """
<p class="eyebrow">CINCO MÓDULOS · CADA UNO ENTRA CON UN ARTEFACTO Y SALE CON OTRO</p>
<h1>La ruta de hoy</h1>
<table class="modules">
<tr><th style="width:30%">Módulo</th><th style="width:10%">Min</th><th style="width:30%">Entra</th><th>Sale</th></tr>
<tr><td>1 · Del LLM al orquestador</td><td>17</td><td>Tu herramienta actual</td><td>Tu herramienta ubicada en el mapa</td></tr>
<tr><td>2 · Evaluar la spec</td><td>25</td><td>Tu spec de E4 y E5</td><td>spec-review.md con nota A–D</td></tr>
<tr><td>3 · design.md + Linear</td><td>17</td><td>Spec con nota A o B</td><td>design.md y fuentes de verdad claras</td></tr>
<tr><td>4 · Del plan al grafo</td><td>30</td><td>Spec + design.md</td><td>Paquete de tareas y grafo en Linear</td></tr>
<tr><td>5 · Loop y orquestador</td><td>12</td><td>Grafo publicado</td><td>Qué automatiza E7</td></tr>
</table>
<p class="take">Preguntas fuera del mapa van al estacionamiento: las respondemos al cierre.</p>""")

# ---------------------------------------------------------------- Módulo 1
slide("El modelo propone. El agente actúa.", ["LLM", "Coding agent"], "MÓDULO 1", """
<p class="eyebrow">MÓDULO 1 · DEL LLM AL ORQUESTADOR</p>
<h1>El modelo propone. El agente actúa.</h1>
<div class="two">
<div><span class="num">LLM</span><h2>Predice la siguiente respuesta</h2><p>Recibe texto y devuelve texto. No ve tu repo ni puede ejecutar nada por su cuenta.</p><p class="example">Sirve para razonar, redactar y decidir el próximo paso.</p></div>
<div><span class="num">Agente</span><h2>Un LLM con herramientas</h2><p>Puede leer archivos, editar, correr comandos y ver el resultado.</p><p class="example">Claude Code, Codex u OpenHands son coding agents. Casi cualquier modelo entra en casi cualquier arnés: revisa qué permite tu suscripción.</p></div>
</div>
<p class="take">El mismo modelo rinde distinto según lo que le damos alrededor.</p>""")

slide("Lo que rodea al agente", ["Arnés", "Loop"], "MÓDULO 1", """
<p class="eyebrow">MÓDULO 1 · DEL LLM AL ORQUESTADOR</p>
<h1>Lo que rodea al agente</h1>
<div class="two">
<div><span class="num">Arnés</span><h2>Contexto, permisos y hábitos</h2><p class="small">AGENTS.md y design.md dan contexto. Las skills enseñan procedimientos. Los hooks reaccionan a eventos. Los permisos limitan qué puede tocar.</p><p class="example">Ingeniería de contexto: todo lo necesario y solo lo necesario.</p></div>
<div><span class="num">Loop</span><h2>Intentar hasta un criterio</h2><p class="small">Planear → editar → probar → corregir. Termina cuando se cumple la aceptación, no cuando el agente deja de escribir.</p></div>
</div>
<p class="take">Sin criterio de aceptación, el loop no sabe cuándo parar. Por eso hoy trabajamos la spec.</p>""")

slide("Anatomía de un arnés", ["Arnés"], "MÓDULO 1", """
<p class="eyebrow">MÓDULO 1 · DEL LLM AL ORQUESTADOR</p>
<h1 style="margin-bottom:10px">Anatomía de un arnés</h1>
<svg viewBox="0 0 1152 500" width="1152" height="500" role="img" aria-label="Anatomía de un arnés: el LLM dentro del coding agent, rodeado por contexto, skills, permisos, hooks, memoria y loop; el orquestador despacha tareas y MCP conecta con Linear, GitHub y documentación" style="display:block;margin-top:6px;font-family:Calibri,Aptos,Arial,sans-serif">
<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#C8E600"/></marker></defs>
<rect x="210" y="8" width="620" height="484" fill="#111" stroke="#C8E600" stroke-width="2" stroke-dasharray="8 6"/>
<text x="230" y="40" fill="#C8E600" font-size="20" font-weight="700" letter-spacing="2">ARNÉS</text>
<g font-size="18" fill="#B3B3B3">
<rect x="230" y="62" width="160" height="104" fill="#0A0A0A" stroke="#4D4D4D"/><text x="246" y="90" fill="white" font-size="21" font-weight="700">Contexto</text><text x="246" y="116">AGENTS.md</text><text x="246" y="138">design.md · spec</text>
<rect x="230" y="186" width="160" height="104" fill="#0A0A0A" stroke="#4D4D4D"/><text x="246" y="214" fill="white" font-size="21" font-weight="700">Skills</text><text x="246" y="240">evaluate-spec</text><text x="246" y="262">create-impl-plan</text>
<rect x="230" y="310" width="160" height="80" fill="#0A0A0A" stroke="#4D4D4D"/><text x="246" y="338" fill="white" font-size="21" font-weight="700">Permisos</text><text x="246" y="364">qué puede tocar</text>
<rect x="650" y="62" width="160" height="104" fill="#0A0A0A" stroke="#4D4D4D"/><text x="666" y="90" fill="white" font-size="21" font-weight="700">Hooks</text><text x="666" y="116">evento → acción</text><text x="666" y="138">bloquea · registra</text>
<rect x="650" y="186" width="160" height="104" fill="#0A0A0A" stroke="#4D4D4D"/><text x="666" y="214" fill="white" font-size="21" font-weight="700">Memoria</text><text x="666" y="240">notas de la tarea</text><text x="666" y="262">compactación</text>
<rect x="650" y="310" width="160" height="80" fill="#0A0A0A" stroke="#4D4D4D"/><text x="666" y="338" fill="white" font-size="21" font-weight="700">Evidencia</text><text x="666" y="364">tests · diff · logs</text>
</g>
<rect x="410" y="62" width="220" height="250" fill="#0A0A0A" stroke="#808080"/>
<text x="520" y="92" fill="white" font-size="21" font-weight="700" text-anchor="middle">Coding agent</text>
<rect x="450" y="130" width="140" height="84" fill="#C8E600"/>
<text x="520" y="180" fill="#0A0A0A" font-size="30" font-weight="700" text-anchor="middle">LLM</text>
<text x="520" y="248" fill="#B3B3B3" font-size="18" text-anchor="middle">lee · edita</text>
<text x="520" y="272" fill="#B3B3B3" font-size="18" text-anchor="middle">ejecuta · observa</text>
<rect x="410" y="332" width="220" height="140" fill="#0A0A0A" stroke="#C8E600"/>
<text x="520" y="362" fill="#C8E600" font-size="21" font-weight="700" text-anchor="middle">Loop</text>
<text x="520" y="392" fill="white" font-size="18" text-anchor="middle">planear → editar</text>
<text x="520" y="418" fill="white" font-size="18" text-anchor="middle">→ probar → corregir</text>
<text x="520" y="452" fill="#808080" font-size="16" text-anchor="middle">hasta cumplir la aceptación</text>
<rect x="0" y="186" width="170" height="104" fill="#0A0A0A" stroke="#4D4D4D"/>
<text x="16" y="214" fill="white" font-size="21" font-weight="700">Orquestador</text>
<text x="16" y="240" fill="#B3B3B3" font-size="18">despacha tareas</text>
<text x="16" y="262" fill="#B3B3B3" font-size="18">sin bloqueos</text>
<line x1="170" y1="238" x2="206" y2="238" stroke="#C8E600" stroke-width="2" marker-end="url(#ah)"/>
<rect x="870" y="62" width="120" height="70" fill="#C8E600"/>
<text x="930" y="105" fill="#0A0A0A" font-size="24" font-weight="700" text-anchor="middle">MCP</text>
<line x1="830" y1="97" x2="866" y2="97" stroke="#C8E600" stroke-width="2" marker-end="url(#ah)"/>
<g font-size="20" fill="white">
<rect x="1010" y="62" width="142" height="56" fill="#0A0A0A" stroke="#4D4D4D"/><text x="1026" y="97">Linear</text>
<rect x="1010" y="136" width="142" height="56" fill="#0A0A0A" stroke="#4D4D4D"/><text x="1026" y="171">GitHub</text>
<rect x="1010" y="210" width="142" height="56" fill="#0A0A0A" stroke="#4D4D4D"/><text x="1026" y="245">Docs y APIs</text>
</g>
<g stroke="#4D4D4D" stroke-width="2" fill="none"><path d="M990 90 H1010"/><path d="M990 110 C1000 110 1000 164 1010 164"/><path d="M990 120 C1004 120 1000 238 1010 238"/></g>
</svg>""")

slide("Coordinar y conectar", ["Orquestador", "MCP"], "MÓDULO 1", """
<p class="eyebrow">MÓDULO 1 · DEL LLM AL ORQUESTADOR</p>
<h1>Coordinar y conectar</h1>
<div class="two">
<div><span class="num">Orquestador</span><h2>Muchas tareas, en orden</h2><p class="small">Lee una cola de tareas, despacha las que no tienen bloqueos y junta la evidencia de cada una. Lo vemos con OpenSymphony en E7.</p></div>
<div><span class="num">MCP</span><h2>Un enchufe estándar</h2><p class="small">Model Context Protocol: la forma en que el agente habla con Linear, GitHub o tu documentación sin integraciones a medida.</p></div>
</div>
<p class="take">Tu turno · 5 min: ubica tu herramienta en el mapa. ¿Qué piezas ya usas y cuál te falta?</p>""")

# ---------------------------------------------------------------- Módulo 2
slide("¿Le darías esta tarea a un agente?", ["Coding agent"], "MÓDULO 2", """
<p class="eyebrow">MÓDULO 2 · EVALUAR LA SPEC</p>
<h1>¿Le darías esta tarea a un agente?</h1>
<div class="comparison">
<div><p class="label bad">INTENCIÓN AMBIGUA</p><blockquote>“Implementa autenticación.”</blockquote><p>¿Qué parte?<br>¿Con qué reglas?<br>¿Cómo sabemos que terminó?</p></div>
<div><p class="label">TRABAJO PREPARADO</p><blockquote>“Valida la política de contraseña.”</blockquote><p>Reglas BR-PASS-01 a 04.<br>Función y pruebas; sin base de datos.<br>Casos normales y de error explícitos.</p></div>
</div>
<p class="take">La diferencia no está en el código. Está en la spec.</p>""")

slide("Tres lentes para revisar una spec", ["Arnés"], "MÓDULO 2", """
<p class="eyebrow">MÓDULO 2 · SKILL EVALUATE-SPEC</p>
<h1>Tres lentes para revisar una spec</h1>
<div class="three">
<div><span class="num">1</span><h2>Producto</h2><p class="small">Problema, usuario, alcance, fuera de alcance y reglas de negocio sin contradicciones.</p></div>
<div><span class="num">2</span><h2>TDD</h2><p class="small">Cada requisito tiene un resultado observable y casos de prueba, incluidos errores y bordes.</p></div>
<div><span class="num">3</span><h2>Diseño</h2><p class="small">Arquitectura mínima, contratos entre componentes y design.md para la interfaz.</p></div>
</div>
<p class="take">La skill no reescribe tu spec: cita la evidencia y propone la corrección mínima.</p>""")

slide("La nota define el siguiente paso", ["Arnés"], "MÓDULO 2", """
<p class="eyebrow">MÓDULO 2 · NOTA ABCD</p>
<h1>La nota define el siguiente paso</h1>
<div class="grades">
<div class="ok"><b>A</b><strong>Lista</strong><span>Todos los criterios críticos cumplen. Pasa al plan.</span></div>
<div class="ok"><b>B</b><strong>Lista con supuestos</strong><span>Ningún crítico falta. Los supuestos quedan escritos y aceptados.</span></div>
<div><b>C</b><strong>Necesita decisiones</strong><span>Falta al menos un crítico. Resolver antes de planificar.</span></div>
<div><b>D</b><strong>Todavía no es spec</strong><span>Sin alcance o sin requisitos verificables. Volver a E4 y E5.</span></div>
</div>
<p class="take">Una nota por ola, no por proyecto. Solo A o B pasan al módulo 4.</p>""")

slide("Evalúa tu spec", ["Arnés"], "MÓDULO 2", """
<p class="eyebrow">TU TURNO · 17 MIN</p>
<h1>Evalúa tu spec</h1>
<div class="steps">
<div><b>03 min</b><span>Abre tu repo y reúne la spec de E4 y E5.</span></div>
<div><b>06 min</b><span>Pide al arnés que lea y siga <code>skills/evaluate-spec/SKILL.md</code>.</span></div>
<div><b>05 min</b><span>Corrige el vacío más grave de <code>docs/spec-review.md</code>.</span></div>
<div><b>03 min</b><span>Vuelve a evaluar. Anota la nota antes y después.</span></div>
</div>
<p class="take">Sin spec propia: usa EntreVista AI de la estación 5.</p>""")

slide("Pausa", [], "PAUSA", """
<p class="eyebrow">PAUSA · 5 MIN</p>
<h1 style="font-size:72px;margin-top:120px">Volvemos en cinco minutos</h1>
<p class="big">Al volver: ¿qué nota sacó tu spec?</p>""")

# ---------------------------------------------------------------- Módulo 3
slide("Una fuente de verdad para cada cosa", ["Arnés"], "MÓDULO 3", """
<p class="eyebrow">MÓDULO 3 · DESIGN.MD + LINEAR</p>
<h1>Una fuente de verdad para cada cosa</h1>
<table>
<tr><th style="width:24%">Artefacto</th><th style="width:38%">Qué gobierna</th><th>Si cambia</th></tr>
<tr><td>Spec en Git</td><td>Qué debe hacer el producto y sus reglas</td><td>Re-evaluar y ajustar las tareas afectadas</td></tr>
<tr><td>design.md</td><td>Cómo se ve y cómo se construye</td><td>Las tareas lo enlazan, no lo copian</td></tr>
<tr><td>Archivos de tarea</td><td>El contrato de cada tarea</td><td>Actualizar el archivo y su issue</td></tr>
<tr><td>Linear</td><td>Estado, dependencias y responsable</td><td>Se mueve con el trabajo</td></tr>
<tr><td>PR y tests</td><td>La evidencia de que se cumplió</td><td>Nueva revisión</td></tr>
</table>
<p class="take">No hay sincronización automática: si cambia el contrato, se actualizan archivo e issue.</p>""")

slide("design.md: lo que el agente no debe adivinar", ["Arnés"], "MÓDULO 3", """
<p class="eyebrow">MÓDULO 3 · DESIGN.MD</p>
<h1>design.md: lo que el agente no debe adivinar</h1>
<div class="two">
<div><h2>Qué contiene</h2><p class="small">Principios de experiencia<br>Sistema visual y componentes<br>Estados: carga, vacío, error, éxito<br>Arquitectura y contratos<br>Decisiones y qué no hacer</p></div>
<div><h2>Cómo se usa</h2><p class="small">Vive en la raíz del repo.<br>El agente lo lee antes de cada tarea de interfaz o de contratos.<br>La skill de evaluación lo revisa en la lente de diseño.</p><p class="source">Plantilla: estacion6/plantillas/design.md</p></div>
</div>
<p class="take">Si una decisión de diseño está en el chat y no en design.md, el próximo agente no la conoce.</p>""")

slide("Linear como cola de trabajo", ["MCP"], "MÓDULO 3", """
<p class="eyebrow">MÓDULO 3 · LINEAR VÍA MCP</p>
<h1>Linear como cola de trabajo</h1>
<div class="chain">
<div><strong>Milestone</strong><span>Agrupa tareas de un mismo objetivo.</span></div><i>→</i>
<div><strong>Issue</strong><span>Una tarea con su contrato y criterio de aceptación.</span></div><i>→</i>
<div class="on"><strong>blockedBy</strong><span>Las dependencias que forman el grafo.</span></div><i>→</i>
<div><strong>area:</strong><span>Etiquetas que agrupan por componente.</span></div>
</div>
<p>Con el MCP de Linear, el agente lee y actualiza issues desde el arnés. La interfaz web también sirve. ¿Usas Jira o ClickUp? Adapta la skill a tu tracker.</p>
<p class="take">Publica en un proyecto sin orquestador observando: publicar puede disparar trabajo.</p>""")

# ---------------------------------------------------------------- Módulo 4
slide("De AIDLC a tareas", ["Arnés"], "MÓDULO 4", """
<p class="eyebrow">MÓDULO 4 · DEL PLAN AL GRAFO</p>
<h1>No es otro camino: es el paso siguiente a AIDLC</h1>
<div class="chain">
<div><strong>Inception</strong><span>Requisitos, historias y unidades de trabajo.</span></div><i>→</i>
<div><strong>Construction</strong><span>Diseño funcional, NFR e infraestructura de cada unidad.</span></div><i>→</i>
<div class="on"><strong>Ola de planificación</strong><span>Una unidad, o parte de ella, se planifica junta.</span></div><i>→</i>
<div><strong>Tareas</strong><span>Con dependencias, aceptación y Definition of Ready.</span></div>
</div>
<p class="take">AIDLC define qué y cómo. El plan define en qué orden y cuándo está terminado.</p>""")

slide("De la spec al paquete de tareas", ["Arnés"], "MÓDULO 4", """
<p class="eyebrow">MÓDULO 4 · SKILL CREATE-IMPLEMENTATION-PLAN</p>
<h1>De la spec al paquete de tareas</h1>
<div class="chain">
<div><strong>Entra</strong><span>Spec con nota A o B, design.md, AGENTS.md y el estado del repo.</span></div><i>→</i>
<div class="on"><strong>create-implementation-plan</strong><span>Descompone el alcance en tareas con milestones, dependencias y aceptación.</span></div><i>→</i>
<div><strong>Sale</strong><span>task-package.yaml, milestones.md, un .md por tarea y cobertura.md.</span></div>
</div>
<p>Cada tarea trae alcance, fuera de alcance, entregables, criterios, plan de pruebas y Definition of Ready.</p>
<p class="take">El manifest es la fuente de verdad del paquete. El nombre del archivo no.</p>""")

slide("El grafo de tareas", ["Orquestador"], "MÓDULO 4", """
<p class="eyebrow">MÓDULO 4 · DEPENDENCIAS</p>
<h1>El grafo decide qué se puede empezar</h1>
<div class="graph">
<div class="node ready"><b>TASK-001</b>Runner de pruebas</div><div class="arrow">→</div>
<div class="node"><b>TASK-002</b>Validador de contraseña</div><div class="arrow">→</div>
<div class="node"><b>TASK-004</b>Alta de usuario</div>
<div class="node ready"><b>TASK-003</b>Esquema de candidatos</div><div class="arrow">→</div>
<div class="node"><b>TASK-005</b>API de candidatos</div><div class="arrow">→</div>
<div class="node"><b>TASK-006</b>Pantalla de revisión · lee design.md</div>
</div>
<div class="legend"><span class="r">Lista: sin bloqueos pendientes</span><span>Bloqueada por otra tarea</span></div>
<p class="take">Un paquete completo puede tener tareas bloqueadas. Sin ciclos, siempre hay una por donde empezar.</p>""")

slide("Del paquete a Linear", ["MCP"], "MÓDULO 4", """
<p class="eyebrow">MÓDULO 4 · SKILL CONVERT-TASKS-TO-LINEAR</p>
<h1>Del paquete a Linear, con red</h1>
<div class="chain">
<div><strong>1 · Validar</strong><span>IDs únicos, archivos existentes, milestones y referencias válidas.</span></div><i>→</i>
<div><strong>2 · Dry-run</strong><span>Ver qué se va a crear antes de crearlo.</span></div><i>→</i>
<div class="on"><strong>3 · Publicar</strong><span>Issues, milestones, blockedBy y etiquetas area:.</span></div><i>→</i>
<div><strong>4 · Verificar</strong><span>Jerarquía, bloqueos y proyecto correcto en Linear.</span></div>
</div>
<p class="take">Sin acceso a Linear: entrega el paquete validado y registra «publicación pendiente».</p>""")

slide("Genera tu grafo", ["Arnés", "MCP"], "MÓDULO 4", """
<p class="eyebrow">TU TURNO · 22 MIN</p>
<h1>Genera tu grafo</h1>
<div class="steps">
<div><b>11 min</b><span>Ejecuta create-implementation-plan sobre tu spec y design.md.</span></div>
<div><b>06 min</b><span>En pareja: ¿cada requisito tiene tareas? ¿Hay ciclos? ¿Cuáles están listas?</span></div>
<div><b>05 min</b><span>Dry-run con convert-tasks-to-linear o carga manual de las primeras tareas.</span></div>
</div>
<p class="take">El paquete completo se termina como preparación de E7. Hoy alcanza con empezarlo bien.</p>""")

# ---------------------------------------------------------------- Módulo 5
slide("Una tarea atraviesa el loop", ["Loop", "Orquestador"], "MÓDULO 5", """
<p class="eyebrow">MÓDULO 5 · PUENTE A E7</p>
<h1>Una tarea atraviesa el loop</h1>
<div class="chain">
<div class="on"><strong>Issue listo</strong><span>Sin bloqueos, con aceptación.</span></div><i>→</i>
<div><strong>Agente</strong><span>Lee contexto, implementa, prueba.</span></div><i>→</i>
<div><strong>PR</strong><span>Diff, tests y evidencia.</span></div><i>→</i>
<div><strong>Review</strong><span>Humana y automática.</span></div><i>→</i>
<div><strong>Merge</strong><span>Lo autoriza una persona.</span></div>
</div>
<p>En E7 lo hacemos primero a mano con una tarea. Después el orquestador lo repite para todo el grafo.</p>
<p class="take">Automatiza un ciclo que ya entiendes, no uno que todavía no probaste.</p>""")

# ---------------------------------------------------------------- Cierre
slide("Meta-arnés", ["Arnés", "Orquestador"], "MÓDULO 5", """
<p class="eyebrow">MÓDULO 5 · ORQUESTAR ARNESES</p>
<h1 style="margin-bottom:10px">Meta-arnés: un arnés que dirige otros</h1>
<svg viewBox="0 0 1152 470" width="1152" height="470" role="img" aria-label="Meta-arnés: un arnés coordinador reparte tareas a arneses trabajadores como Codex, OpenHands o un agente ACP, cada uno con su modelo y su suscripción" style="display:block;margin-top:6px;font-family:Calibri,Aptos,Arial,sans-serif"><defs><marker id="am" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#C8E600"/></marker></defs><rect x="386" y="0" width="380" height="110" fill="#111" stroke="#C8E600" stroke-width="2"/><text x="402" y="32" fill="#C8E600" font-size="21" font-weight="700">Arnés coordinador</text><text x="402" y="60" fill="#B3B3B3" font-size="18">Claude Code, por ejemplo</text><text x="402" y="84" fill="#B3B3B3" font-size="18">planifica, reparte y revisa</text><rect x="0" y="190" width="360" height="110" fill="#0A0A0A" stroke="#4D4D4D" stroke-width="1"/><text x="16" y="222" fill="white" font-size="21" font-weight="700">Codex</text><text x="16" y="250" fill="#B3B3B3" font-size="18">headless</text><text x="16" y="274" fill="#B3B3B3" font-size="18">modelo y plan de OpenAI</text><path d="M576 110 C576 150 180 150 180 186" stroke="#C8E600" stroke-width="2" fill="none" marker-end="url(#am)"/><rect x="396" y="190" width="360" height="110" fill="#0A0A0A" stroke="#4D4D4D" stroke-width="1"/><text x="412" y="222" fill="white" font-size="21" font-weight="700">OpenHands</text><text x="412" y="250" fill="#B3B3B3" font-size="18">arnés abierto</text><text x="412" y="274" fill="#B3B3B3" font-size="18">cualquier modelo vía API</text><path d="M576 110 C576 150 576 150 576 186" stroke="#C8E600" stroke-width="2" fill="none" marker-end="url(#am)"/><rect x="792" y="190" width="360" height="110" fill="#0A0A0A" stroke="#4D4D4D" stroke-width="1"/><text x="808" y="222" fill="white" font-size="21" font-weight="700">Agente ACP</text><text x="808" y="250" fill="#B3B3B3" font-size="18">otro proveedor</text><text x="808" y="274" fill="#B3B3B3" font-size="18">su modelo y su suscripción</text><path d="M576 110 C576 150 972 150 972 186" stroke="#C8E600" stroke-width="2" fill="none" marker-end="url(#am)"/><text x="606" y="160" fill="#808080" font-size="16">CLI headless · ACP</text><rect x="0" y="360" width="1152" height="96" fill="#111" stroke="#4D4D4D"/><text x="20" y="396" fill="white" font-size="21" font-weight="700">Repo y tareas</text><text x="20" y="428" fill="#B3B3B3" font-size="18">Cada trabajador usa su rama y su workspace. La evidencia vuelve al coordinador.</text><text x="1132" y="428" fill="#808080" font-size="16" text-anchor="end">Ejemplos: Orca, Paseo</text><line x1="180" y1="300" x2="180" y2="356" stroke="#4D4D4D" stroke-width="2"/><line x1="576" y1="300" x2="576" y2="356" stroke="#4D4D4D" stroke-width="2"/><line x1="972" y1="300" x2="972" y2="356" stroke="#4D4D4D" stroke-width="2"/></svg>""")

slide("OpenSymphony", ["Orquestador", "Loop"], "MÓDULO 5", """
<p class="eyebrow">MÓDULO 5 · ORQUESTACIÓN DE TRABAJO · LO VEMOS EN E7</p>
<h1 style="margin-bottom:10px">OpenSymphony: el grafo de Linear, ejecutado</h1>
<svg viewBox="0 0 1152 470" width="1152" height="470" role="img" aria-label="Ciclo de OpenSymphony: Linear con dependencias, OpenSymphony elige tareas listas, workspace aislado por issue, arnés, PR, code review automático, merge humano y desbloqueo de dependientes" style="display:block;margin-top:6px;font-family:Calibri,Aptos,Arial,sans-serif"><defs><marker id="ao" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#C8E600"/></marker></defs><rect x="0" y="0" width="196" height="96" fill="#0A0A0A" stroke="#4D4D4D" stroke-width="1"/><text x="16" y="32" fill="white" font-size="21" font-weight="700">Linear</text><text x="16" y="60" fill="#B3B3B3" font-size="18">issues · blockedBy</text><rect x="239" y="0" width="196" height="96" fill="#0A0A0A" stroke="#C8E600" stroke-width="2"/><text x="255" y="32" fill="#C8E600" font-size="21" font-weight="700">OpenSymphony</text><text x="255" y="60" fill="#B3B3B3" font-size="18">elige tareas listas</text><rect x="478" y="0" width="196" height="96" fill="#0A0A0A" stroke="#4D4D4D" stroke-width="1"/><text x="494" y="32" fill="white" font-size="21" font-weight="700">Workspace</text><text x="494" y="60" fill="#B3B3B3" font-size="18">uno por issue · hooks</text><rect x="717" y="0" width="196" height="96" fill="#0A0A0A" stroke="#4D4D4D" stroke-width="1"/><text x="733" y="32" fill="white" font-size="21" font-weight="700">Arnés</text><text x="733" y="60" fill="#B3B3B3" font-size="18">OpenHands o Codex</text><rect x="956" y="0" width="196" height="96" fill="#0A0A0A" stroke="#4D4D4D" stroke-width="1"/><text x="972" y="32" fill="white" font-size="21" font-weight="700">Pull request</text><text x="972" y="60" fill="#B3B3B3" font-size="18">diff · tests · notas</text><line x1="196" y1="48" x2="235" y2="48" stroke="#C8E600" stroke-width="2" marker-end="url(#ao)"/><line x1="435" y1="48" x2="474" y2="48" stroke="#C8E600" stroke-width="2" marker-end="url(#ao)"/><line x1="674" y1="48" x2="713" y2="48" stroke="#C8E600" stroke-width="2" marker-end="url(#ao)"/><line x1="913" y1="48" x2="952" y2="48" stroke="#C8E600" stroke-width="2" marker-end="url(#ao)"/><rect x="956" y="170" width="196" height="120" fill="#0A0A0A" stroke="#4D4D4D" stroke-width="1"/><text x="972" y="202" fill="white" font-size="21" font-weight="700">Code review</text><text x="972" y="230" fill="#B3B3B3" font-size="18">automático, con el</text><text x="972" y="254" fill="#B3B3B3" font-size="18">contexto del grafo</text><rect x="717" y="170" width="196" height="120" fill="#0A0A0A" stroke="#4D4D4D" stroke-width="1"/><text x="733" y="202" fill="white" font-size="21" font-weight="700">Merge</text><text x="733" y="230" fill="#B3B3B3" font-size="18">lo autoriza</text><text x="733" y="254" fill="#B3B3B3" font-size="18">una persona</text><rect x="478" y="170" width="196" height="120" fill="#0A0A0A" stroke="#4D4D4D" stroke-width="1"/><text x="494" y="202" fill="white" font-size="21" font-weight="700">Desbloqueo</text><text x="494" y="230" fill="#B3B3B3" font-size="18">las dependientes</text><text x="494" y="254" fill="#B3B3B3" font-size="18">quedan listas</text><line x1="1054" y1="96" x2="1054" y2="166" stroke="#C8E600" stroke-width="2" marker-end="url(#ao)"/><line x1="956" y1="230" x2="917" y2="230" stroke="#C8E600" stroke-width="2" marker-end="url(#ao)"/><line x1="717" y1="230" x2="678" y2="230" stroke="#C8E600" stroke-width="2" marker-end="url(#ao)"/><path d="M478 230 H98 V100" stroke="#C8E600" stroke-width="2" fill="none" marker-end="url(#ao)"/><text x="120" y="222" fill="#808080" font-size="16">Linear se actualiza y el ciclo sigue</text><rect x="0" y="340" width="1152" height="110" fill="#111" stroke="#4D4D4D"/><text x="20" y="376" fill="white" font-size="21" font-weight="700">Tablero del operador y memoria</text><text x="20" y="406" fill="#B3B3B3" font-size="18">Grafo de tareas con ruta crítica, detalle de cada ejecución y un grafo de conocimiento</text><text x="20" y="430" fill="#B3B3B3" font-size="18">construido con el trabajo terminado.</text></svg>""")

slide("Antes de la estación 7", [], "CIERRE", """
<p class="eyebrow">PREPARACIÓN E7</p>
<h1>Llega con esto listo</h1>
<div class="checklist">
<p><b>01</b>docs/spec-review.md con nota A o B.</p>
<p><b>02</b>design.md en la raíz del repo.</p>
<p><b>03</b>Paquete completo: task-package.yaml, milestones.md, tareas y cobertura.md.</p>
<p><b>04</b>Grafo publicado en Linear, o «publicación pendiente» registrada.</p>
<p><b>05</b>Accesos probados: arnés, Git, GitHub y Linear.</p>
</div>
<p class="source">Guía completa: estacion7/preparacion.md</p>""")

slide("Recursos", [], "CIERRE", """
<p class="eyebrow">RECURSOS · ESTACIÓN 6</p>
<h1>Skills, plantillas y lecturas</h1>
<div class="two">
<div><h2>En este repo</h2><p class="small">skills/evaluate-spec<br>skills/create-implementation-plan<br>plantillas/design.md<br>ejemplo-y-prompts.md</p></div>
<div><h2>Afuera</h2><p class="small"><a href="https://github.com/kumanday/OpenSymphony/tree/main/.agents/skills/convert-tasks-to-linear">convert-tasks-to-linear</a> · <a href="https://github.com/kumanday/OpenSymphony/tree/main/.agents/skills/linear">linear</a><br><a href="https://opensymphony.dev">OpenSymphony</a><br><a href="https://openai.com/index/harness-engineering/">Harness engineering</a> · OpenAI<br><a href="https://trilogyai.substack.com/p/from-spec-driven-work-to-work-orchestration">From Spec-Driven Work to Work Orchestration</a></p></div>
</div>
<p class="take">Lista completa y lecturas opcionales: estacion6/recursos.md</p>""")


def render():
    total = len(SLIDES)
    out = []
    for n, (title, active, module, body) in enumerate(SLIDES, 1):
        out.append(
            f'<section class="slide" contenteditable="true" spellcheck="true" aria-label="{n}. {title}">'
            f"{mapbar(active)}{body.strip()}"
            f'<footer class="footer"><span>Hardcore AI by 30X · Estación 6 · {module}</span>'
            f"<span>{n:02d} / {total:02d}</span></footer></section>"
        )
    html = (
        '<!doctype html><html lang="es"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        "<title>Estación 6 · Del spec al harness</title>"
        f"<style>{CSS}</style></head><body><main class=\"deck\">"
        + "\n".join(out)
        + "</main></body></html>\n"
    )
    target = Path(__file__).resolve().parent.parent / "estacion6.html"
    target.write_text(html, encoding="utf-8")
    print(f"{total} slides → {target}")


if __name__ == "__main__":
    render()
