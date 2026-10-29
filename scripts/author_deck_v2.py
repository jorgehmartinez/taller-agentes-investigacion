#!/usr/bin/env python3
"""One-off authoring source for redesign v2. QMD remains authoritative afterwards.
Use --write only to deliberately regenerate this first version, not after manual edits.
"""
from pathlib import Path
import json,sys
PROJECT=Path(__file__).resolve().parents[1]
ROOT=PROJECT/'presentacion'
S=[]
V=lambda n: 'assets/visuals/'+n+'.svg'
P=lambda n: 'assets/screenshots/'+n+'.png'
def tx(slot,content):return (slot,'text',content)
def im(slot,path,alt):return (slot,'image',(path,alt))
def co(slot,content,lang='r'):return (slot,'code',(content,lang))
def add(id,title,section,blocks,notes,variant='visual',source='',takeaway=None,kind='concepto'):
    if takeaway:blocks=blocks+[tx('takeaway',takeaway)]
    if source:blocks=blocks+[tx('citation',source)]
    S.append(dict(id=id,title=title,section=section,blocks=[tx('kicker',section)]+blocks,notes=notes,variant=variant,kind=kind))
def vis(id,title,section,file,notes,takeaway=None,source='Esquema didáctico · no son resultados observados.'):
    add(id,title,section,[im('visual',V(file),notes.split('.')[0])],notes,source=source,takeaway=takeaway,kind='explicación visual')
def q(id,title,section,question,prompt,notes):
    add(id,title,section,[tx('question',question),tx('prompt',prompt)],notes,'question',kind='actividad')
def sec(id,title,num,section,subtitle,notes):
    add(id,title,section,[tx('number',num),tx('subtitle',subtitle)],notes,'section',kind='transición')
MICRO='Microejemplo ficticio · R 4.6.1 · materiales/microcaso/01_microcaso.R'
POSIT='Posit (13-10-2026) · captura oficial de producto · fuente y original en assets/screenshots/'
CORE='Captura propia · r-analytic-core / r-analytic-coding-principles · consulta local 29-10-2026'

add('inicio','Uso de Agentes IA para análisis de datos e investigación','SOCIEDAD PERUANA DE PSICOMETRÍA · TALLER VIRTUAL',[
 im('visual',V('hero'),'Pregunta, código, R y evidencia alrededor del criterio científico.'),
 tx('subtitle','Una introducción al trabajo con agentes, con aplicaciones al análisis psicométrico.'),
 tx('citation','Brian Norman Peña Calero · 3 horas · R como motor de ejecución')],
 'Conservar el título anunciado. Presentar carácter introductorio, independencia del agente y foco psicométrico. No prometer investigación autónoma ni una validación completa de instrumentos.','hero',kind='portada')
vis('promesa','Cinco respuestas, una decisión','APERTURA · ANTICIPAR','micro-pregunta',
 'Pedir al grupo que anticipe qué información revisaría antes de aceptar la media. No revelar todavía que 99 representa un perdido. Mantener fijo el vector durante los estados siguientes.',
 '¿Qué falta saber antes de aceptar el resultado?',MICRO)
vis('micro-ejecucion','Una ejecución sin errores','APERTURA · OBSERVAR','micro-ejecucion',
 'Mostrar que R efectivamente ejecutó el código y devolvió 21.8. Es una interpretación errónea preparada, no un fallo atribuido a un agente. Si las respuestas válidas van de 1 a 4, el resultado exige revisar el diccionario.',
 'El código funciona; el análisis puede seguir estando mal.',MICRO)
vis('tres-preguntas','La ruta del taller','APERTURA · ORIENTARSE','ruta',
 'Enlazar el error con tres preguntas: comprender, dirigir y verificar. Presentar el mismo microejemplo como hilo que regresará en contexto, auditoría y reproducción. El caso factorial amplía esas decisiones sin inventar resultados.',
 'Un método transferible; un caso psicométrico para aprenderlo.')
q('sondeo-inicial','Punto de partida','APERTURA · PARTICIPAR',
 '¿Hasta dónde has trabajado con IA?',
 'En el chat: 1 = conversación; 2 = código sugerido; 3 = herramientas; 4 = análisis ejecutado.',
 'Sondeo de 90 segundos. No confundir experiencia con IA con formación estadística. Usar las respuestas para graduar la explicación, no como evaluación.')

vis('modelo-probabilistico','Generación condicionada por el contexto','01 / COMPRENDER','generacion',
 'Explicar primero con un encargo familiar: describir respuestas. Las continuaciones son ilustrativas y no probabilidades medidas. Un LLM modela distribuciones; la decodificación puede reducir variabilidad. Probabilístico no significa que todo resultado cambie siempre. Una propuesta plausible no es una decisión estadística validada.',
 'El modelo es probabilístico; una respuesta plausible no prueba que sea correcta.')
vis('generar-ejecutar','Proponer, ejecutar y verificar','01 / COMPRENDER','modelo-r-investigador',
 'Separar tres operaciones que suelen mezclarse. El modelo propone código, R produce salidas y la persona revisa pertinencia y conclusiones. El retorno representa la corrección iterativa, no autonomía irrestricta.',
 'No pedir números al modelo cuando podemos obtenerlos de una ejecución.')
vis('chatbot-agente','Dos recorridos para una misma tarea','01 / COMPRENDER','chatbot-vs-agente',
 'Contraste controlado: misma pregunta y mismo R. A la izquierda la persona hace el intercambio manual; a la derecha el agente opera herramientas. Preguntar qué cambia y qué permanece. La responsabilidad científica permanece.',
 'Automatizar intercambios no transfiere la responsabilidad.')
vis('anatomia-agente','La anatomía de un agente','01 / COMPRENDER','anatomia',
 'Definir herramienta por su función: leer archivos, ejecutar R o inspeccionar una figura. Contexto, permisos y objetivo limitan el proceso. No presentar un agente como un modelo más inteligente por definición.',
 'Modelo + herramientas + contexto + controles.')
add('r-reproducible','Aleatoriedad bajo control','01 / COMPRENDER',[
 tx('left-label','Mismo punto de partida'),co('left','set.seed(2026)\nsample(1:100, size = 5)'),
 tx('right-label','Qué debemos conservar'),tx('right','La semilla, el generador, la versión de R, los datos y las decisiones de cálculo.\n\nUna semilla no resuelve todos los problemas de reproducibilidad.')],
 'Ejecutar opcionalmente dos veces la misma llamada tras reiniciar la semilla. No mostrar una lista de números que no haya sido calculada. La lección es que R puede contener aleatoriedad controlada y que reproducibilidad no equivale a determinismo absoluto.',
 'comparison','R Core: documentación de set.seed y RNGversion.',
 'Ejecución controlada y reproducible, no determinismo absoluto.',kind='ejemplo de código')
vis('niveles-de-verificacion','Tres preguntas de verificación','01 / COMPRENDER','verificaciones',
 'Volver al 21.8: pasó la ejecución, no la lectura metodológica de los datos. Que un script reproduzca un error no lo hace correcto. Hacer explícito qué evidencia responde cada pregunta.',
 'Superar una comprobación no implica superar las otras.')

vis('ecosistema-capas','Cuatro capas diferentes','02 / HERRAMIENTAS','capas',
 'Nombrar modelo, agente, entorno y motor. La selección no es una competición de marcas. Aclarar que las herramientas evolucionan y que no todos los agentes cargan las mismas instrucciones o conectores.',
 'No confundir el modelo con el programa que opera las herramientas.',
 'Documentación oficial: Codex, Claude Code, Gemini CLI y Posit. Referencias al final.')
add('opciones-agentes','Agentes: elegir una vía de trabajo','02 / HERRAMIENTAS',[
 tx('first','Codex · Claude Code · Gemini CLI'),
 tx('second','Agentes externos que trabajan sobre archivos y herramientas.'),
 tx('third','Posit Assistant: una vía integrada en Positron o RStudio.'),
 tx('fourth','Para la sesión: un agente preparado, no cuatro instalaciones.')],
 'Explicar las tres familias externas y la opción integrada. Mencionar otras alternativas solo si surge en preguntas. No prometer equivalencia de permisos, skills, plataformas o MCP. No convertir esta diapositiva en tabla de precios.',
 'summary','Fuentes oficiales de OpenAI, Anthropic, Google y Posit; consultadas el 29-10-2026.',kind='mapa de opciones')
add('positron-entorno','Positron por dentro','02 / HERRAMIENTAS · CAPTURA PROPIA',[
 im('visual',P('r-entorno'),'Captura propia de Positron con el script del microejemplo y resultados reales en la consola.'),
 tx('side1','**1 · Script.** Instrucciones que podemos leer y modificar.'),
 tx('side2','**2 · Consola R.** Lugar donde se ejecutan los cálculos.'),
 tx('side3','**3 · Salida.** Evidencia que debe coincidir con lo reportado.')],
 'Mostrar la ventana real en perfil aislado, sin cuentas ni credenciales. No se utilizó un agente para producir esta captura: se ejecutó el script docente en R. El fin es localizar las superficies, no leer todo el código a esta escala.',
 'screenshot','Captura propia · Positron 2026.10.2 · R 4.6.1 · microejemplo sintético.',
 'No basta con la respuesta del chat: observa dónde se ejecuta.')
vis('positron-mcp','MCP: el puente hacia R','02 / HERRAMIENTAS','mcp',
 'Definir Model Context Protocol una sola vez. Es un mecanismo para conectar herramientas. Positron 2026.10 incorporó un servidor MCP experimental; verificar agente y versión. El puente puede acceder a la sesión persistente, no sustituye los scripts.',
 'Sesión compartida para explorar; archivos para reproducir.',
 'Posit: October Release Highlights, 13-10-2026. Funcionalidad experimental.')
add('mcp-captura','Una llamada visible a una herramienta','02 / HERRAMIENTAS · CAPTURA OFICIAL',[
 im('visual',P('mcp-vista'),'Captura oficial de Claude Code conectado a Positron: llamadas a herramientas, ejecución en consola y gráfico.'),
 tx('side1','**1 · Solicitud.** El agente llama a una herramienta de Positron.'),
 tx('side2','**2 · Ejecución.** La consola identifica el código del agente.'),
 tx('side3','**3 · Resultado.** Un gráfico observable, no solo una descripción.')],
 'Se trata de una captura publicada por Posit, con otro conjunto de datos. No presentarla como una ejecución del taller. Señalar las tres regiones; la siguiente lámina amplía dos detalles para que se puedan leer.',
 'screenshot',POSIT,'La llamada y la salida dejan rastros que podemos inspeccionar.')
add('mcp-detalle','Del pedido a la consola','02 / HERRAMIENTAS · AMPLIACIÓN',[
 tx('left-label','Detalle 1 · llamada de herramienta'),
 im('left',P('mcp-ejecutar'),'Recorte real de la llamada Positron execute_code en la captura oficial.'),
 tx('right-label','Detalle 2 · código en la sesión R'),
 im('right',P('mcp-consola'),'Recorte real de la consola R: nombre del agente Claude Code y primera instrucción de código.')],
 'Mantener los píxeles de la captura original y ampliar dos regiones. Preguntar dónde buscaríamos un error de ejecución. No leer nombres de modelos de la interfaz como requisito para el curso.',
 'comparison','Posit (2026) · recortes de claude-code-in-positron.png; original conservado.',
 'La conexión debe probarse con el agente y la versión elegidos.')
add('posit-assistant','Posit Assistant: otra forma de entrar','02 / HERRAMIENTAS · CAPTURA OFICIAL',[
 im('visual',P('assistant-flujo'),'Recorte oficial de Posit Assistant: lectura de una skill, comando y apertura de datos.'),
 tx('side1','**Pedir.** Formular una tarea dentro del entorno.'),
 tx('side2','**Inspeccionar.** Observar las instrucciones y herramientas utilizadas.'),
 tx('side3','**Comprobar.** Revisar el objeto abierto y el resultado.')],
 'Captura oficial con un archivo de ejemplo ajeno al taller. Mostrar la secuencia skill, referencia, comando y resultado. Indicar disponibilidad en Positron y RStudio; el acceso requiere un proveedor configurado. No suponer que una suscripción de chat equivale a cualquier acceso API.',
 'screenshot',POSIT,'Un proveedor configurado; ningún secreto en las diapositivas.')

sec('analista-equipo','Un nuevo analista en el equipo','03','03 / CONTEXTUALIZAR',
 'Antes de pedir código: explicar el estudio, los datos y la forma de trabajar.',
 'Usar la analogía propuesta por Brian. Preguntar qué información necesitaría una persona competente recién incorporada. No empezar por ingeniería de prompts.')
vis('onboarding','El contexto que falta','03 / CONTEXTUALIZAR','onboarding',
 'Diferenciar conocimiento general de investigación de contexto específico del estudio. Un analista experimentado tampoco sabe por defecto qué significa 99 o cuál es la hipótesis factorial.',
 'Saber estadística no equivale a conocer este proyecto.')
vis('documentos','Un mapa, no un documento gigante','03 / CONTEXTUALIZAR','documentos',
 'Recorrer las tres fuentes: protocolo, diccionario y README. AGENTS.md contiene reglas persistentes y rutas; no absorbe todos los documentos. La metodología pertenece al estudio y debe ser legible también sin un agente.',
 'Una fuente por decisión; referencias claras entre documentos.',
 'Convención AGENTS.md + plantilla docente en materiales/plantilla-proyecto/.')
q('clasificar-actividad','¿Dónde guardarías cada información?','03 / CONTEXTUALIZAR · ANTICIPAR',
 '«99 = perdido»\n«No sobrescribir originales»',
 '¿Van en el mismo archivo? Responde y justifica antes de avanzar.',
 'Pausa de dos minutos. Buscar la diferencia entre significado de los datos y regla de trabajo. No convertir la organización documental en ritual.')
vis('clasificar-respuesta','Información y lugar apropiado','03 / CONTEXTUALIZAR · RESOLVER','clasificar',
 'Resolver la actividad y añadir hipótesis del estudio y procedimiento reutilizable. No presentar estas ubicaciones como un estándar único; son una organización proporcionada para el proyecto del taller.',
 'La semántica de los datos no debería esconderse en un prompt.')
add('agents-md','AGENTS.md en una tarea real','03 / CONTEXTUALIZAR',[
 tx('left-label','Instrucciones persistentes'),co('left','# Reglas de trabajo\n- Lee docs/protocolo.md.\n- Consulta el diccionario.\n- No cambies datos originales.\n- Conserva scripts legibles.\n- Consulta cambios del método.','markdown'),
 tx('right-label','Lo que esta guía NO decide'),tx('right','No elige el constructo, la dimensionalidad ni el estimador.\n\nTe ayuda a encontrar y respetar las decisiones del equipo.')],
 'Mostrar el ejemplo mínimo y después abrir la plantilla entregada si el tiempo lo permite. La carga de AGENTS.md depende del producto; explicar que la convención no equivale a un permiso efectivo de seguridad.',
 'comparison','Ejemplo docente · AGENTS.md no es un protocolo científico ni un mecanismo de seguridad.',
 'Instrucciones estables; metodología documentada en su fuente.')
vis('no-agents','Qué dejar fuera de AGENTS.md','03 / CONTEXTUALIZAR','agents-limites',
 'Contrastar pares con el mismo propósito: ayudar a trabajar. Mostrar por qué secretos, protocolos duplicados y recetas universales empeoran el diseño. No incluir un token real ni siquiera como captura.',
 'Menos duplicación; más contexto pertinente y verificable.')
vis('plan-proporcional','La planificación proporcional','03 / CONTEXTUALIZAR','plan',
 'No exigir un plan.md para cada operación. La explicación de objetivos, método y entregables sí es necesaria. Un plan escrito adquiere valor con dependencias, riesgo, coste o decisiones que requieren revisión.',
 'Planificar es explicitar decisiones; no producir archivos por reflejo.')
vis('actividad-pedido','De un pedido vago a un encargo','03 / CONTEXTUALIZAR · PRACTICAR','pedido',
 'Dar tres minutos para reformular el pedido. Valorar información relevante y control de decisiones, no longitud del prompt. Usar el caso del instrumento, no introducir otro estudio.',
 'Pregunta + contexto + límites + evidencia de entrega.')

sec('skills-intro','De conocimiento general a procedimiento','04','04 / SKILLS',
 'Un modelo puede conocer una técnica sin conocer cómo queremos trabajar.',
 'Introducir el papel de instrucciones reutilizables. Las skills no reentrenan el modelo ni eliminan la evaluación metodológica. El taller consumirá el monorepo en desarrollo.')
vis('skills-carga','Cómo se utiliza una skill','04 / SKILLS','skill-carga',
 'Explicar la selección por nombre/descripción y la carga del procedimiento, con referencias cuando corresponde. La activación exacta depende del agente. No afirmar que un modelo sigue perfectamente las instrucciones.',
 'Procedimiento reutilizable, no garantía de especialización.',
 'Agent Skills: especificación oficial, agentskills.io/specification, consultada 29-10-2026.')
add('skill-real','Una skill real de nuestro repositorio','04 / SKILLS · CAPTURA PROPIA',[
 im('visual',P('skill-real'),'Captura propia del archivo real SKILL.md de r-analytic-coding-principles abierto en Positron.')],
 'Mostrar el archivo existente sin modificar el monorepo. El encabezado identifica cuándo se usa; la introducción explica la prioridad de editabilidad y transparencia. La captura es del archivo real, no de una skill psicométrica imaginada. No se afirma que un agente la haya cargado.',
 'wide',CORE,'Lee la finalidad, el alcance y los límites antes de utilizarla.')
add('skill-anatomia','Qué mirar dentro de SKILL.md','04 / SKILLS',[
 tx('left-label','Tres preguntas sobre la cabecera'),tx('left','**name:** ¿cómo se identifica?\n\n**description:** ¿cuándo se activa?\n\n**Cuerpo:** ¿qué procedimiento propone?'),
 tx('right-label','Más allá del archivo principal'),tx('right','Referencias para profundizar.\n\nScripts que debemos inspeccionar.\n\nAlcance, límites y ejemplos comprobables.')],
 'Usar la captura anterior como objeto de referencia. Descripción no es publicidad: debe orientar la selección de tareas. Una buena skill distingue reglas de código de decisiones científicas del proyecto.',
 'comparison','Agent Skills: formato SKILL.md; ejemplo real en r-workflow-plugins.',
 'Una skill breve puede enlazar detalles sin cargarlos todos al principio.')
add('codigo-legible','Mismo cálculo, distinta legibilidad','04 / SKILLS · CONTRASTE CONTROLADO',[
 tx('left-label','Compacto, difícil de revisar'),co('left','x <- c(1, 2, 3, 4, 99)\nmean(replace(x, x == 99, NA),\n     na.rm = TRUE)'),
 tx('right-label','Decisiones a la vista'),co('right','respuestas_limpias <- replace(\n  respuestas,\n  respuestas == 99,\n  NA\n)\nmean(respuestas_limpias,\n     na.rm = TRUE)')],
 'Comparación elaborada por el docente, no un ensayo de rendimiento de agentes ni una prueba causal del efecto de la skill. Ambas expresiones calculan 2.5 con la misma entrada. Señalar los nombres, la transformación y la decisión sobre perdidos. La versión derecha presupone respuestas definido en el script canónico.',
 'comparison',MICRO,'La brevedad del código no es el objetivo principal del análisis.')
vis('dos-skills','Una instrucción no es una herramienta','04 / SKILLS','skill-herramienta',
 'Distinguir qué procedimiento utilizar de qué operación está disponible. Una skill puede orientar auditoría y legibilidad; MCP puede facilitar acceso a R. El criterio metodológico sigue fuera de esa automatización.',
 'La skill encamina el trabajo; el investigador juzga su pertinencia.')
vis('skills-confianza','Antes de adoptar una skill','04 / SKILLS','skill-confianza',
 'Dar un ejemplo de recomendación metodológica rígida y otro de script externo no revisado. Inspeccionar procedencia, contenido, permisos y pruebas. No ejecutar recursos de terceros durante la explicación.',
 'Revisar también lo que la skill puede ejecutar.')
vis('skills-proyecto','Nuestro repositorio como fuente','04 / SKILLS','repo',
 'Distinguir la skill ya presente r-analytic-coding-principles del EPIC de datos y psicometría. El taller no crea otra implementación paralela. Fijar versión y probarla antes de la demostración final.',
 'Una versión comprobada para la sesión, no una promesa de disponibilidad.',
 'Instantánea local de r-workflow-plugins consultada 29-10-2026; sin modificar el monorepo.')
sec('descanso','Pausa','10','DESCANSO · MINUTOS',
 'Al volver: aplicar el método a un caso psicométrico y revisar sus decisiones.',
 'Descanso de diez minutos incluido en las tres horas. Mantener la sesión y los materiales de demostración preparados; no usar este tiempo para instalaciones improvisadas.')

sec('caso-portada','Del diccionario al modelo','05','05 / CASO PSICOMÉTRICO',
 'Una escala sintética: documentar, inspeccionar, decidir y comprobar.',
 'Iniciar la demostración integrada. La preparación de 500 casos, 12 ítems y dos dimensiones continúa pendiente; no mostrar índices inventados. El microejemplo de cinco respuestas ya tiene código y salidas de referencia.')
vis('caso-diseno','Respuestas ordinales','05 / CASO PSICOMÉTRICO','datos-ordinales',
 'Matriz ilustrativa ficticia, no resultados de la escala final. Pedir que identifiquen qué cosas inspeccionarían antes de un análisis. El código 99 obliga a consultar el diccionario; ninguna recodificación se decide solo por su magnitud.',
 'Primero, entender la estructura y los códigos.',
 'Ilustración ficticia · el caso completo previsto es de 500 casos, 12 ítems y 2 dimensiones.')
q('caso-pregunta','La pregunta de investigación','05 / CASO PSICOMÉTRICO',
 '¿Qué evidencia respalda la estructura interna propuesta?',
 'Después: ¿qué fiabilidad tienen las puntuaciones de cada dimensión?',
 'Separar objetivos. Las preguntas proceden del diseño del caso ya acordado. Ni el agente ni el ajuste de un modelo deben redefinirlas silenciosamente.')
add('caso-auditoria','El diccionario antes de recodificar','05 / CASO PSICOMÉTRICO',[
 tx('left-label','Dato observado en el microejemplo'),co('left','respuestas <- c(1, 2, 3, 4, 99)\nmean(respuestas)\n# [1] 21.8'),
 tx('right-label','Documentación que decide el sentido'),tx('right','**Categorías válidas:** 1, 2, 3 y 4.\n\n**Código 99:** respuesta perdida.\n\nNo es una quinta categoría ni un valor extremo interpretable.')],
 'Usar diccionario.csv del microejemplo. Los resultados del código están verificados. El texto de la derecha es la fuente que autoriza recodificar, no una conjetura de la IA.',
 'comparison',MICRO,'El agente puede detectar una anomalía; el diccionario explica su significado.')
vis('caso-correccion','La corrección documentada','05 / CASO PSICOMÉTRICO · RESOLVER','micro-correccion',
 'Regresar al mismo vector del inicio y cambiar solo el tratamiento documentado de 99. R devuelve 2.5 y cuatro respuestas válidas. Esta media ilustra una decisión de limpieza; no es un análisis de fiabilidad ni una validación de la escala.',
 'La corrección debe quedar en código y conservar el original.',MICRO)
add('r-salida-real','La salida real de R','05 / CASO PSICOMÉTRICO · CAPTURA PROPIA',[
 im('visual',P('r-consola'),'Recorte de consola Positron que muestra las medias 21.8 y 2.5 y el recuento válido de 4.')],
 'Mostrar la ampliación para poder leer el resultado. Esta consola procede de una sesión R real en un perfil aislado de Positron; no es una captura simulada ni una conversación inventada con un agente. Contrastar con el archivo salida_referencia.txt.',
 'wide','Captura propia de consola · salida comprobada también con Rscript --vanilla.',
 'Los números del relato deben coincidir con la evidencia de ejecución.')
vis('item-inverso','Ítems invertidos: la clave importa','05 / CASO PSICOMÉTRICO','invertir',
 'Esquema de recodificación de una escala de 1 a 4. La fórmula 5 menos respuesta es correcta solo si las categorías y la clave lo justifican. No invertir un ítem por una correlación negativa sin revisar contenido y documentación.',
 'No automatizar una decisión sustantiva a partir de un signo.')
vis('modelo-propuesto','La estructura que vamos a contrastar','05 / CASO PSICOMÉTRICO','modelo-factorial',
 'Dos factores correlacionados y doce indicadores; los nombres de dimensiones son didácticos y corresponden a autorregulación académica. No hay cargas ni índices ajustados en el dibujo. Antes de ejecutar, revisar teoría, identificación y tratamiento de respuestas ordinales.',
 'El modelo expresa una hipótesis; no es un dibujo que el agente deba adivinar.',
 'Esquema del modelo propuesto · sin parámetros estimados ni evidencia empírica.')
add('caso-decision','Decisiones antes del AFC','05 / CASO PSICOMÉTRICO',[
 tx('left-label','Sintaxis ilustrativa, no ejecutada'),co('left','ajuste <- lavaan::cfa(\n  modelo,\n  data = datos,\n  ordered = items,\n  estimator = "WLSMV"\n)'),
 tx('right-label','Preguntas que no resuelve la sintaxis'),tx('right','¿Qué categorías y patrones hay?\n\n¿Cómo se tratan los perdidos?\n\n¿El modelo y el estimador son pertinentes?')],
 'Esta es una ilustración docente, no código para ejecutar con el microejemplo de un ítem. WLSMV es candidato para el caso ordinal, no regla universal. Un argumento bien escrito no demuestra la pertinencia estadística.',
 'comparison','lavaan: tutorial de datos categóricos. Caso completo pendiente de ejecución.',
 'Los argumentos de una función también contienen decisiones metodológicas.')
vis('caso-ejecucion','Autonomía con puntos de revisión','05 / CASO PSICOMÉTRICO','controles-humanos',
 'Recorrer los carriles. Aprobar decisiones sustantivas no significa autorizar cada comando. Las operaciones rutinarias de lectura pueden estar preautorizadas, mientras que cambiar el modelo o la codificación requiere revisión.',
 'Permisos proporcionales; decisiones científicas explícitas.')
add('caso-prompt','El encargo para la demostración','05 / CASO PSICOMÉTRICO',[
 tx('left-label','Primero: comprender e inspeccionar'),co('left','Lee protocolo y diccionario.\nIdentifica la pregunta del estudio.\nAudita ítems y códigos con R.\nNo recodifiques ambigüedades.','text'),
 tx('right-label','Después: actuar y justificar'),co('right','Explica decisiones pendientes.\nEspera aprobación del método.\nEjecuta código legible.\nGuarda salidas y diagnósticos.','text')],
 'No es un prompt mágico. Acompañarlo del contexto real y las skills probadas. Durante el bloque principal se trabaja en el IDE, no se leen todas las instrucciones desde la diapositiva.',
 'comparison','Texto docente · versión extendida en materiales/prompts-demostracion.md.',
 'La tarea y los controles importan más que una formulación sofisticada.')
q('caso-error','Tu turno: localizar el fallo','05 / CASO PSICOMÉTRICO · AUDITAR',
 'El script corre. El 99 quedó como respuesta válida.',
 '¿Qué revisarías, qué corregirías y qué análisis volverías a ejecutar?',
 'Error deliberado. No atribuirlo a un agente concreto. Pedir que conecten decisiones de preparación con resultados posteriores y documenten la corrección antes de recalcular.')
vis('caso-diagnostico','Después de la convergencia','05 / CASO PSICOMÉTRICO','diagnostico',
 'Introducir el significado de converger: el procedimiento alcanzó un criterio de parada. Luego inspeccionar solución, ajuste y sentido sustantivo. El diagrama es guía de revisión, no el reporte de un modelo corrido ni un criterio universal de aprobación.',
 'Un algoritmo que termina todavía deja preguntas importantes.')
vis('caso-repro','Volver a empezar desde los archivos','05 / CASO PSICOMÉTRICO','sesion-limpia',
 'Mostrar sesión persistente frente a ejecución limpia. Usar el microejemplo para comprobarlo ahora y repetir en el caso completo cuando esté preparado. La reproducción exige código, entradas y condiciones; no la memoria del agente.',
 'Reproducir el cálculo también permite reproducir un error: todavía hay que interpretarlo.',MICRO)

vis('actividad-auditoria','Del resultado a la conclusión','06 / AUDITORÍA Y TRANSFERENCIA','validez',
 'Actividad final. La frase es deliberadamente excesiva, no resultado del caso. Pedir fuentes de evidencia y límites. Un ajuste favorable de estructura interna no establece por sí solo todos los usos de las puntuaciones.',
 '¿Qué parte de la afirmación está respaldada y cuál excede la evidencia?')
vis('riesgos','Cuatro controles del trabajo','06 / AUDITORÍA Y TRANSFERENCIA','seguridad',
 'Sintetizar datos, código, método y skills. Reforzar que ninguna regla textual reemplaza permisos reales o políticas de privacidad. Mantener la distinción entre control computacional y evaluación metodológica.',
 'Un análisis supervisado deja evidencia, no solo una respuesta convincente.')
vis('transferencia','El mismo método, otros análisis','06 / AUDITORÍA Y TRANSFERENCIA','transferencia',
 'Mostrar que se conserva el método, pero cambian el diseño, las variables, los supuestos, el modelo y las skills pertinentes. Ejemplificar regresión sin iniciar otro análisis completo.',
 'La competencia transferible es dirigir y auditar el proceso.')
add('cuatro-ideas','Cuatro distinciones esenciales','CIERRE',[
 tx('first','**Generar** no equivale a **calcular**.'),
 tx('second','**Contextualizar** no equivale a **acumular instrucciones**.'),
 tx('third','**Especializar** no equivale a **garantizar la corrección**.'),
 tx('fourth','**Delegar ejecución** no equivale a **delegar responsabilidad**.')],
 'Recuperar el 99 inicial y pedir que asocien cada contraste con una evidencia vista durante la sesión. Cierre sin nuevos conceptos técnicos.',
 'summary',kind='síntesis')
q('ticket-salida','Antes de tu próximo análisis','CIERRE · TRANSFERIR',
 '¿Qué le entregarías hoy a un agente que ayer no le habrías dado?',
 'Responde con un documento, una restricción y una comprobación concreta.',
 'Ticket de salida de dos minutos. Buscar respuestas sobre contexto, permisos y evidencia, no nombres de modelos.')
add('recursos','Un proyecto para seguir practicando','CIERRE · MATERIALES',[
 tx('left-label','Recursos de aprendizaje'),co('left','materiales/\n  microcaso/\n  plantilla-proyecto/\n  actividades.md\n  guia-para-evaluar-skills.md','text'),
 tx('right-label','Ejecutar el microejemplo'),co('right','Rscript --vanilla \\\n  materiales/microcaso/01_microcaso.R','bash')],
 'Separar material ya ejecutable de la integración futura del caso factorial y skills. No vender una validación completada. El microejemplo puede reproducirse sin cuenta de IA. Los handouts conservan detalle que no cabe en la proyección.',
 'comparison','Proyecto local del taller · fuentes, notas y scripts separados.',
 'Practica el método antes de aumentar la complejidad.')

# Backup slides: not extra mandatory lecture time.
add('apendice-proveedor','Configurar un proveedor','APOYO · FUERA DEL RECORRIDO PRINCIPAL',[
 im('visual',P('proveedor'),'Captura oficial del diálogo para configurar un proveedor en Positron.')],
 'Apoyo para preguntas, no instalación durante la sesión. La captura oficial muestra un proveedor específico; no obliga a elegirlo. Consultar documentación vigente, términos y acceso antes de usar credenciales. No mostrar claves reales.',
 'wide','Posit: guía de inicio de Posit AI. Captura oficial; proveedores sujetos a disponibilidad.',
 'La configuración concreta depende del producto y de su versión.')
add('referencias-herramientas','Fuentes de herramientas y formatos','APOYO · REFERENCIAS',[
 tx('left','**Positron / MCP**\nPosit, October Release Highlights (13-10-2026).\n\n**Posit Assistant**\nGetting Started y Providers.\n\n**R Core**\nRandom Number Generation: set.seed / RNGversion.'),
 tx('right','**AGENTS.md**\nConvención oficial: agents.md.\n\n**Agent Skills**\nSpecification: agentskills.io.\n\n**Agentes de codificación**\nDocumentación de Codex, Claude Code y Gemini CLI.')],
 'Referencias completas con enlaces y fechas en docs/fuentes.md. No mostrar enlaces extensos en la proyección. Las capturas originales y sus derivados tienen registro de procedencia.',
 'references','Documentación oficial consultada el 29-10-2026.',kind='referencias')
add('referencias-materiales','Fuentes y límites del material','APOYO · REFERENCIAS',[
 tx('left','**Skill de R**\nr-workflow-plugins: r-analytic-coding-principles.\n\n**AFC ordinal**\nlavaan: tutorial de datos categóricos.\n\n**Cálculos del ejemplo**\nScript y salida real de R en materiales/microcaso/.'),
 tx('right','**Diagramas**\nEsquemas didácticos; no resultados empíricos.\n\n**Capturas**\nPropias en perfil aislado u oficiales de Posit, identificadas.\n\n**Caso completo**\nNo se presentan índices de ajuste ni coeficientes no calculados.')],
 'Distinguir fuente, ejemplo conceptual y evidencia computacional. La referencia metodológica definitiva del caso se completará con la integración y evaluación de las skills. Esta distinción no resta valor al microejemplo ya comprobado.',
 'references','Consultar docs/fuentes.md y assets/screenshots/provenance.json.',kind='referencias')

header='---\ntitle: "Uso de Agentes IA para análisis de datos e investigación"\nlang: es\nqbento-annotations: none\n---\n\n'
parts=[header]
for slide in S:
    sid=slide['id'];parts.append(f'## {slide["title"]} {{#{sid} bento-variant="{slide["variant"]}"}}\n')
    used=set()
    for slot,kind,val in slide['blocks']:
        if slot in used:raise ValueError('Duplicate slot '+sid+' '+slot)
        used.add(slot);eid=sid+'-'+slot
        attrs=f'#{eid} bento-slot="{slot}"'+(' .bento-code' if kind=='code' else '')
        if kind=='image':
            path,alt=val
            if not (ROOT/path).is_file():raise FileNotFoundError(path)
            body=f'![]({path})'
        elif kind=='code':body=f'```{{#{eid}-source .{val[1]}}}\n{val[0]}\n```'
        else:body=val.replace('\n\n','\n').replace('\n','  \n')
        parts.append(f'::: {{{attrs}}}\n\n{body}\n\n:::\n')
    parts.append(f'::: {{#{sid}-notas .notes}}\n{slide["notes"]}\n:::\n')
text='\n'.join(parts)
if '--write' not in sys.argv:
    print('Pass --write to author deck.qmd; this overwrites current QMD intentionally.');sys.exit(0)
(ROOT/'deck.qmd').write_text(text)
visual_descriptions=['# Descripciones y guía textual de los apoyos visuales\n', 'Las imágenes de esta versión usan el adaptador de Quarto-Bento 0.2.0. El atributo Quarto fig-alt no está admitido en este adaptador; se conservan descripciones aquí, en los SVG originales y en las notas docentes. Esto no constituye una auditoría de accesibilidad completa.\n']
for i,sl in enumerate(S,1):
    visual_descriptions.append(f'## {i}. {sl["title"]}\n')
    for slot,kind,value in sl['blocks']:
        if kind=='image':visual_descriptions.append(value[1]+'\n')
        elif kind=='text' and slot not in ['kicker','citation']:visual_descriptions.append(value+'\n')
        elif kind=='code':visual_descriptions.append('```'+value[1]+'\n'+value[0]+'\n```\n')
    visual_descriptions.append('**Orientación docente:** '+sl['notes']+'\n')
(PROJECT/'materiales/descripciones-visuales.md').write_text('\n'.join(visual_descriptions))
(PROJECT/'docs/storyboard-v2.json').write_text(json.dumps([{k:v for k,v in s.items() if k!='blocks'} for s in S],ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'slides':len(S),'core':len(S)-3,'appendix':3,'chars':len(text),'ids':[s['id'] for s in S]},ensure_ascii=False))
