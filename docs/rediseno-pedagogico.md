# Secuencia pedagógica vigente

## Organización por necesidades

Primero establecer qué aprenderemos y qué queda fuera. Después comprender el componente generativo. A continuación reconocer el intercambio manual con un chat, motivar herramientas, comprobar qué no resuelven y solo entonces introducir instrucciones y entorno. No abrir con un fallo estadístico que presupone familiaridad con R.

## Transiciones

**Fundamentos → análisis.** La analogía del redactor introduce generación condicionada por contexto, no describe toda la arquitectura de un LLM. Las marcas permiten reconocer productos sin ranking ni versiones efímeras. Se distingue modelo, interfaz y herramientas disponibles.

**Chat → agente.** La misma petición y código pasan por tres escenas: recibir, trasladar a RStudio y devolver un error. Se etiquetan como recreaciones ficticias, no screenshots ni evaluaciones de productos. El problema es el transporte manual de contexto. Un producto de chat también puede incorporar herramientas: la distinción está en el acceso operativo, no en el aspecto de la ventana.

**Agente → código revisable.** Ejecutar y observar puede reducir intercambios, pero no garantiza adecuación o legibilidad. Preguntar si podemos cambiar un solo AFC prepara los antiejemplos de safe_cfa, limpieza escondida y fallos silenciados. No se desacreditan todas las funciones o bucles; se analiza qué decisiones quedan ocultas.

**Legibilidad → instrucciones.** Un mapa único presenta harness, reglas, AGENTS.md, skills/plugins y MCP. La siguiente lámina mantiene la composición y resalta la guía del proyecto y los procedimientos reutilizables. El onboarding del analista explica por qué necesitamos contexto. El mapa documental distingue ciencia, reglas locales y procedimientos reutilizables.

**Instrucciones → Positron.** La configuración llega cuando ya sabemos qué queremos del entorno. Se muestran ajuste, comando y una prueba que debe dejar rastros en la sesión correcta. Las capturas oficiales permanecen atribuidas a otro proyecto, no a la ejecución del taller.

## Matices que deben mantenerse

La productividad es un beneficio potencial dependiente de tarea, experiencia y supervisión, no una promesa cuantificada. No afirmar que todo software se desarrolla sin revisión ni que todos los LLM se entrenaron para priorizar pipelines. El patrón de código sobreestructurado es un riesgo posible, no una característica universal demostrada.

Las funciones, bucles, controles y pipelines también son útiles en investigación, especialmente en simulaciones y tareas estables. Legibilidad y reproducibilidad no se contraponen. El objetivo es mantener visibles las decisiones que queremos revisar y modificar, conservando diagnósticos y controles sustantivos.

AGENTS.md puede incluir normas cortas cuando basta. Una skill es útil para un procedimiento reutilizable o especializado. No exigir documentación fragmentada artificialmente, ni plan.md para cada tarea. AGENTS.md no equivale al system prompt ni impone permisos de ejecución por sí mismo.

## Edición y continuidad

Se mantiene presentacion/deck.qmd y su identidad Bento. Las láminas retiradas se borraron mediante revisión de fuente; las retenidas conservan sus identificadores. Git guarda el estado previo y la reorganización. No se creó otra presentación numerada para esta revisión.
