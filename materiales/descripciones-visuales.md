# Descripciones y guía textual de los apoyos visuales

Las imágenes de esta versión usan el adaptador de Quarto-Bento 0.2.0. El atributo Quarto fig-alt no está admitido en este adaptador; se conservan descripciones aquí, en los SVG originales y en las notas docentes. Esto no constituye una auditoría de accesibilidad completa.

## 1. Uso de Agentes IA para análisis de datos e investigación

Pregunta, código, R y evidencia alrededor del criterio científico.

Una introducción al trabajo con agentes, con aplicaciones al análisis psicométrico.

**Orientación docente:** Conservar el título anunciado. Presentar carácter introductorio, independencia del agente y foco psicométrico. No prometer investigación autónoma ni una validación completa de instrumentos.

## 2. Cinco respuestas, una decisión

Pedir al grupo que anticipe qué información revisaría antes de aceptar la media

¿Qué falta saber antes de aceptar el resultado?

**Orientación docente:** Pedir al grupo que anticipe qué información revisaría antes de aceptar la media. No revelar todavía que 99 representa un perdido. Mantener fijo el vector durante los estados siguientes.

## 3. Una ejecución sin errores

Mostrar que R efectivamente ejecutó el código y devolvió 21

El código funciona; el análisis puede seguir estando mal.

**Orientación docente:** Mostrar que R efectivamente ejecutó el código y devolvió 21.8. Es una interpretación errónea preparada, no un fallo atribuido a un agente. Si las respuestas válidas van de 1 a 4, el resultado exige revisar el diccionario.

## 4. La ruta del taller

Enlazar el error con tres preguntas: comprender, dirigir y verificar

Un método transferible; un caso psicométrico para aprenderlo.

**Orientación docente:** Enlazar el error con tres preguntas: comprender, dirigir y verificar. Presentar el mismo microejemplo como hilo que regresará en contexto, auditoría y reproducción. El caso factorial amplía esas decisiones sin inventar resultados.

## 5. Punto de partida

¿Hasta dónde has trabajado con IA?

En el chat: 1 = conversación; 2 = código sugerido; 3 = herramientas; 4 = análisis ejecutado.

**Orientación docente:** Sondeo de 90 segundos. No confundir experiencia con IA con formación estadística. Usar las respuestas para graduar la explicación, no como evaluación.

## 6. Generación condicionada por el contexto

Explicar primero con un encargo familiar: describir respuestas

El modelo es probabilístico; una respuesta plausible no prueba que sea correcta.

**Orientación docente:** Explicar primero con un encargo familiar: describir respuestas. Las continuaciones son ilustrativas y no probabilidades medidas. Un LLM modela distribuciones; la decodificación puede reducir variabilidad. Probabilístico no significa que todo resultado cambie siempre. Una propuesta plausible no es una decisión estadística validada.

## 7. Proponer, ejecutar y verificar

Separar tres operaciones que suelen mezclarse

No pedir números al modelo cuando podemos obtenerlos de una ejecución.

**Orientación docente:** Separar tres operaciones que suelen mezclarse. El modelo propone código, R produce salidas y la persona revisa pertinencia y conclusiones. El retorno representa la corrección iterativa, no autonomía irrestricta.

## 8. Dos recorridos para una misma tarea

Contraste controlado: misma pregunta y mismo R

Automatizar intercambios no transfiere la responsabilidad.

**Orientación docente:** Contraste controlado: misma pregunta y mismo R. A la izquierda la persona hace el intercambio manual; a la derecha el agente opera herramientas. Preguntar qué cambia y qué permanece. La responsabilidad científica permanece.

## 9. La anatomía de un agente

Definir herramienta por su función: leer archivos, ejecutar R o inspeccionar una figura

Modelo + herramientas + contexto + controles.

**Orientación docente:** Definir herramienta por su función: leer archivos, ejecutar R o inspeccionar una figura. Contexto, permisos y objetivo limitan el proceso. No presentar un agente como un modelo más inteligente por definición.

## 10. Aleatoriedad bajo control

Mismo punto de partida

```r
set.seed(2026)
sample(1:100, size = 5)
```

Qué debemos conservar

La semilla, el generador, la versión de R, los datos y las decisiones de cálculo.

Una semilla no resuelve todos los problemas de reproducibilidad.

Ejecución controlada y reproducible, no determinismo absoluto.

**Orientación docente:** Ejecutar opcionalmente dos veces la misma llamada tras reiniciar la semilla. No mostrar una lista de números que no haya sido calculada. La lección es que R puede contener aleatoriedad controlada y que reproducibilidad no equivale a determinismo absoluto.

## 11. Tres preguntas de verificación

Volver al 21

Superar una comprobación no implica superar las otras.

**Orientación docente:** Volver al 21.8: pasó la ejecución, no la lectura metodológica de los datos. Que un script reproduzca un error no lo hace correcto. Hacer explícito qué evidencia responde cada pregunta.

## 12. Cuatro capas diferentes

Nombrar modelo, agente, entorno y motor

No confundir el modelo con el programa que opera las herramientas.

**Orientación docente:** Nombrar modelo, agente, entorno y motor. La selección no es una competición de marcas. Aclarar que las herramientas evolucionan y que no todos los agentes cargan las mismas instrucciones o conectores.

## 13. Agentes: elegir una vía de trabajo

Codex · Claude Code · Gemini CLI

Agentes externos que trabajan sobre archivos y herramientas.

Posit Assistant: una vía integrada en Positron o RStudio.

Para la sesión: un agente preparado, no cuatro instalaciones.

**Orientación docente:** Explicar las tres familias externas y la opción integrada. Mencionar otras alternativas solo si surge en preguntas. No prometer equivalencia de permisos, skills, plataformas o MCP. No convertir esta diapositiva en tabla de precios.

## 14. Positron por dentro

Captura propia de Positron con el script del microejemplo y resultados reales en la consola.

**1 · Script.** Instrucciones que podemos leer y modificar.

**2 · Consola R.** Lugar donde se ejecutan los cálculos.

**3 · Salida.** Evidencia que debe coincidir con lo reportado.

No basta con la respuesta del chat: observa dónde se ejecuta.

**Orientación docente:** Mostrar la ventana real en perfil aislado, sin cuentas ni credenciales. No se utilizó un agente para producir esta captura: se ejecutó el script docente en R. El fin es localizar las superficies, no leer todo el código a esta escala.

## 15. MCP: el puente hacia R

Definir Model Context Protocol una sola vez

Sesión compartida para explorar; archivos para reproducir.

**Orientación docente:** Definir Model Context Protocol una sola vez. Es un mecanismo para conectar herramientas. Positron 2026.10 incorporó un servidor MCP experimental; verificar agente y versión. El puente puede acceder a la sesión persistente, no sustituye los scripts.

## 16. Una llamada visible a una herramienta

Captura oficial de Claude Code conectado a Positron: llamadas a herramientas, ejecución en consola y gráfico.

**1 · Solicitud.** El agente llama a una herramienta de Positron.

**2 · Ejecución.** La consola identifica el código del agente.

**3 · Resultado.** Un gráfico observable, no solo una descripción.

La llamada y la salida dejan rastros que podemos inspeccionar.

**Orientación docente:** Se trata de una captura publicada por Posit, con otro conjunto de datos. No presentarla como una ejecución del taller. Señalar las tres regiones; la siguiente lámina amplía dos detalles para que se puedan leer.

## 17. Del pedido a la consola

Detalle 1 · llamada de herramienta

Recorte real de la llamada Positron execute_code en la captura oficial.

Detalle 2 · código en la sesión R

Recorte real de la consola R: nombre del agente Claude Code y primera instrucción de código.

La conexión debe probarse con el agente y la versión elegidos.

**Orientación docente:** Mantener los píxeles de la captura original y ampliar dos regiones. Preguntar dónde buscaríamos un error de ejecución. No leer nombres de modelos de la interfaz como requisito para el curso.

## 18. Posit Assistant: otra forma de entrar

Recorte oficial de Posit Assistant: lectura de una skill, comando y apertura de datos.

**Pedir.** Formular una tarea dentro del entorno.

**Inspeccionar.** Observar las instrucciones y herramientas utilizadas.

**Comprobar.** Revisar el objeto abierto y el resultado.

Un proveedor configurado; ningún secreto en las diapositivas.

**Orientación docente:** Captura oficial con un archivo de ejemplo ajeno al taller. Mostrar la secuencia skill, referencia, comando y resultado. Indicar disponibilidad en Positron y RStudio; el acceso requiere un proveedor configurado. No suponer que una suscripción de chat equivale a cualquier acceso API.

## 19. Un nuevo analista en el equipo

03

Antes de pedir código: explicar el estudio, los datos y la forma de trabajar.

**Orientación docente:** Usar la analogía propuesta por Brian. Preguntar qué información necesitaría una persona competente recién incorporada. No empezar por ingeniería de prompts.

## 20. El contexto que falta

Diferenciar conocimiento general de investigación de contexto específico del estudio

Saber estadística no equivale a conocer este proyecto.

**Orientación docente:** Diferenciar conocimiento general de investigación de contexto específico del estudio. Un analista experimentado tampoco sabe por defecto qué significa 99 o cuál es la hipótesis factorial.

## 21. Un mapa, no un documento gigante

Recorrer las tres fuentes: protocolo, diccionario y README

Una fuente por decisión; referencias claras entre documentos.

**Orientación docente:** Recorrer las tres fuentes: protocolo, diccionario y README. AGENTS.md contiene reglas persistentes y rutas; no absorbe todos los documentos. La metodología pertenece al estudio y debe ser legible también sin un agente.

## 22. ¿Dónde guardarías cada información?

«99 = perdido»
«No sobrescribir originales»

¿Van en el mismo archivo? Responde y justifica antes de avanzar.

**Orientación docente:** Pausa de dos minutos. Buscar la diferencia entre significado de los datos y regla de trabajo. No convertir la organización documental en ritual.

## 23. Información y lugar apropiado

Resolver la actividad y añadir hipótesis del estudio y procedimiento reutilizable

La semántica de los datos no debería esconderse en un prompt.

**Orientación docente:** Resolver la actividad y añadir hipótesis del estudio y procedimiento reutilizable. No presentar estas ubicaciones como un estándar único; son una organización proporcionada para el proyecto del taller.

## 24. AGENTS.md en una tarea real

Instrucciones persistentes

```markdown
# Reglas de trabajo
- Lee docs/protocolo.md.
- Consulta el diccionario.
- No cambies datos originales.
- Conserva scripts legibles.
- Consulta cambios del método.
```

Lo que esta guía NO decide

No elige el constructo, la dimensionalidad ni el estimador.

Te ayuda a encontrar y respetar las decisiones del equipo.

Instrucciones estables; metodología documentada en su fuente.

**Orientación docente:** Mostrar el ejemplo mínimo y después abrir la plantilla entregada si el tiempo lo permite. La carga de AGENTS.md depende del producto; explicar que la convención no equivale a un permiso efectivo de seguridad.

## 25. Qué dejar fuera de AGENTS.md

Contrastar pares con el mismo propósito: ayudar a trabajar

Menos duplicación; más contexto pertinente y verificable.

**Orientación docente:** Contrastar pares con el mismo propósito: ayudar a trabajar. Mostrar por qué secretos, protocolos duplicados y recetas universales empeoran el diseño. No incluir un token real ni siquiera como captura.

## 26. La planificación proporcional

No exigir un plan

Planificar es explicitar decisiones; no producir archivos por reflejo.

**Orientación docente:** No exigir un plan.md para cada operación. La explicación de objetivos, método y entregables sí es necesaria. Un plan escrito adquiere valor con dependencias, riesgo, coste o decisiones que requieren revisión.

## 27. De un pedido vago a un encargo

Dar tres minutos para reformular el pedido

Pregunta + contexto + límites + evidencia de entrega.

**Orientación docente:** Dar tres minutos para reformular el pedido. Valorar información relevante y control de decisiones, no longitud del prompt. Usar el caso del instrumento, no introducir otro estudio.

## 28. De conocimiento general a procedimiento

04

Un modelo puede conocer una técnica sin conocer cómo queremos trabajar.

**Orientación docente:** Introducir el papel de instrucciones reutilizables. Las skills no reentrenan el modelo ni eliminan la evaluación metodológica. El taller consumirá el monorepo en desarrollo.

## 29. Cómo se utiliza una skill

Explicar la selección por nombre/descripción y la carga del procedimiento, con referencias cuando corresponde

Procedimiento reutilizable, no garantía de especialización.

**Orientación docente:** Explicar la selección por nombre/descripción y la carga del procedimiento, con referencias cuando corresponde. La activación exacta depende del agente. No afirmar que un modelo sigue perfectamente las instrucciones.

## 30. Una skill real de nuestro repositorio

Captura propia del archivo real SKILL.md de r-analytic-coding-principles abierto en Positron.

Lee la finalidad, el alcance y los límites antes de utilizarla.

**Orientación docente:** Mostrar el archivo existente sin modificar el monorepo. El encabezado identifica cuándo se usa; la introducción explica la prioridad de editabilidad y transparencia. La captura es del archivo real, no de una skill psicométrica imaginada. No se afirma que un agente la haya cargado.

## 31. Qué mirar dentro de SKILL.md

Tres preguntas sobre la cabecera

**name:** ¿cómo se identifica?

**description:** ¿cuándo se activa?

**Cuerpo:** ¿qué procedimiento propone?

Más allá del archivo principal

Referencias para profundizar.

Scripts que debemos inspeccionar.

Alcance, límites y ejemplos comprobables.

Una skill breve puede enlazar detalles sin cargarlos todos al principio.

**Orientación docente:** Usar la captura anterior como objeto de referencia. Descripción no es publicidad: debe orientar la selección de tareas. Una buena skill distingue reglas de código de decisiones científicas del proyecto.

## 32. Mismo cálculo, distinta legibilidad

Compacto, difícil de revisar

```r
x <- c(1, 2, 3, 4, 99)
mean(replace(x, x == 99, NA),
     na.rm = TRUE)
```

Decisiones a la vista

```r
respuestas_limpias <- replace(
  respuestas,
  respuestas == 99,
  NA
)
mean(respuestas_limpias,
     na.rm = TRUE)
```

La brevedad del código no es el objetivo principal del análisis.

**Orientación docente:** Comparación elaborada por el docente, no un ensayo de rendimiento de agentes ni una prueba causal del efecto de la skill. Ambas expresiones calculan 2.5 con la misma entrada. Señalar los nombres, la transformación y la decisión sobre perdidos. La versión derecha presupone respuestas definido en el script canónico.

## 33. Una instrucción no es una herramienta

Distinguir qué procedimiento utilizar de qué operación está disponible

La skill encamina el trabajo; el investigador juzga su pertinencia.

**Orientación docente:** Distinguir qué procedimiento utilizar de qué operación está disponible. Una skill puede orientar auditoría y legibilidad; MCP puede facilitar acceso a R. El criterio metodológico sigue fuera de esa automatización.

## 34. Antes de adoptar una skill

Dar un ejemplo de recomendación metodológica rígida y otro de script externo no revisado

Revisar también lo que la skill puede ejecutar.

**Orientación docente:** Dar un ejemplo de recomendación metodológica rígida y otro de script externo no revisado. Inspeccionar procedencia, contenido, permisos y pruebas. No ejecutar recursos de terceros durante la explicación.

## 35. Nuestro repositorio como fuente

Distinguir la skill ya presente r-analytic-coding-principles del EPIC de datos y psicometría

Una versión comprobada para la sesión, no una promesa de disponibilidad.

**Orientación docente:** Distinguir la skill ya presente r-analytic-coding-principles del EPIC de datos y psicometría. El taller no crea otra implementación paralela. Fijar versión y probarla antes de la demostración final.

## 36. Pausa

10

Al volver: aplicar el método a un caso psicométrico y revisar sus decisiones.

**Orientación docente:** Descanso de diez minutos incluido en las tres horas. Mantener la sesión y los materiales de demostración preparados; no usar este tiempo para instalaciones improvisadas.

## 37. Del diccionario al modelo

05

Una escala sintética: documentar, inspeccionar, decidir y comprobar.

**Orientación docente:** Iniciar la demostración integrada. La preparación de 500 casos, 12 ítems y dos dimensiones continúa pendiente; no mostrar índices inventados. El microejemplo de cinco respuestas ya tiene código y salidas de referencia.

## 38. Respuestas ordinales

Matriz ilustrativa ficticia, no resultados de la escala final

Primero, entender la estructura y los códigos.

**Orientación docente:** Matriz ilustrativa ficticia, no resultados de la escala final. Pedir que identifiquen qué cosas inspeccionarían antes de un análisis. El código 99 obliga a consultar el diccionario; ninguna recodificación se decide solo por su magnitud.

## 39. La pregunta de investigación

¿Qué evidencia respalda la estructura interna propuesta?

Después: ¿qué fiabilidad tienen las puntuaciones de cada dimensión?

**Orientación docente:** Separar objetivos. Las preguntas proceden del diseño del caso ya acordado. Ni el agente ni el ajuste de un modelo deben redefinirlas silenciosamente.

## 40. El diccionario antes de recodificar

Dato observado en el microejemplo

```r
respuestas <- c(1, 2, 3, 4, 99)
mean(respuestas)
# [1] 21.8
```

Documentación que decide el sentido

**Categorías válidas:** 1, 2, 3 y 4.

**Código 99:** respuesta perdida.

No es una quinta categoría ni un valor extremo interpretable.

El agente puede detectar una anomalía; el diccionario explica su significado.

**Orientación docente:** Usar diccionario.csv del microejemplo. Los resultados del código están verificados. El texto de la derecha es la fuente que autoriza recodificar, no una conjetura de la IA.

## 41. La corrección documentada

Regresar al mismo vector del inicio y cambiar solo el tratamiento documentado de 99

La corrección debe quedar en código y conservar el original.

**Orientación docente:** Regresar al mismo vector del inicio y cambiar solo el tratamiento documentado de 99. R devuelve 2.5 y cuatro respuestas válidas. Esta media ilustra una decisión de limpieza; no es un análisis de fiabilidad ni una validación de la escala.

## 42. La salida real de R

Recorte de consola Positron que muestra las medias 21.8 y 2.5 y el recuento válido de 4.

Los números del relato deben coincidir con la evidencia de ejecución.

**Orientación docente:** Mostrar la ampliación para poder leer el resultado. Esta consola procede de una sesión R real en un perfil aislado de Positron; no es una captura simulada ni una conversación inventada con un agente. Contrastar con el archivo salida_referencia.txt.

## 43. Ítems invertidos: la clave importa

Esquema de recodificación de una escala de 1 a 4

No automatizar una decisión sustantiva a partir de un signo.

**Orientación docente:** Esquema de recodificación de una escala de 1 a 4. La fórmula 5 menos respuesta es correcta solo si las categorías y la clave lo justifican. No invertir un ítem por una correlación negativa sin revisar contenido y documentación.

## 44. La estructura que vamos a contrastar

Dos factores correlacionados y doce indicadores; los nombres de dimensiones son didácticos y corresponden a autorregulación académica

El modelo expresa una hipótesis; no es un dibujo que el agente deba adivinar.

**Orientación docente:** Dos factores correlacionados y doce indicadores; los nombres de dimensiones son didácticos y corresponden a autorregulación académica. No hay cargas ni índices ajustados en el dibujo. Antes de ejecutar, revisar teoría, identificación y tratamiento de respuestas ordinales.

## 45. Decisiones antes del AFC

Sintaxis ilustrativa, no ejecutada

```r
ajuste <- lavaan::cfa(
  modelo,
  data = datos,
  ordered = items,
  estimator = "WLSMV"
)
```

Preguntas que no resuelve la sintaxis

¿Qué categorías y patrones hay?

¿Cómo se tratan los perdidos?

¿El modelo y el estimador son pertinentes?

Los argumentos de una función también contienen decisiones metodológicas.

**Orientación docente:** Esta es una ilustración docente, no código para ejecutar con el microejemplo de un ítem. WLSMV es candidato para el caso ordinal, no regla universal. Un argumento bien escrito no demuestra la pertinencia estadística.

## 46. Autonomía con puntos de revisión

Recorrer los carriles

Permisos proporcionales; decisiones científicas explícitas.

**Orientación docente:** Recorrer los carriles. Aprobar decisiones sustantivas no significa autorizar cada comando. Las operaciones rutinarias de lectura pueden estar preautorizadas, mientras que cambiar el modelo o la codificación requiere revisión.

## 47. El encargo para la demostración

Primero: comprender e inspeccionar

```text
Lee protocolo y diccionario.
Identifica la pregunta del estudio.
Audita ítems y códigos con R.
No recodifiques ambigüedades.
```

Después: actuar y justificar

```text
Explica decisiones pendientes.
Espera aprobación del método.
Ejecuta código legible.
Guarda salidas y diagnósticos.
```

La tarea y los controles importan más que una formulación sofisticada.

**Orientación docente:** No es un prompt mágico. Acompañarlo del contexto real y las skills probadas. Durante el bloque principal se trabaja en el IDE, no se leen todas las instrucciones desde la diapositiva.

## 48. Tu turno: localizar el fallo

El script corre. El 99 quedó como respuesta válida.

¿Qué revisarías, qué corregirías y qué análisis volverías a ejecutar?

**Orientación docente:** Error deliberado. No atribuirlo a un agente concreto. Pedir que conecten decisiones de preparación con resultados posteriores y documenten la corrección antes de recalcular.

## 49. Después de la convergencia

Introducir el significado de converger: el procedimiento alcanzó un criterio de parada

Un algoritmo que termina todavía deja preguntas importantes.

**Orientación docente:** Introducir el significado de converger: el procedimiento alcanzó un criterio de parada. Luego inspeccionar solución, ajuste y sentido sustantivo. El diagrama es guía de revisión, no el reporte de un modelo corrido ni un criterio universal de aprobación.

## 50. Volver a empezar desde los archivos

Mostrar sesión persistente frente a ejecución limpia

Reproducir el cálculo también permite reproducir un error: todavía hay que interpretarlo.

**Orientación docente:** Mostrar sesión persistente frente a ejecución limpia. Usar el microejemplo para comprobarlo ahora y repetir en el caso completo cuando esté preparado. La reproducción exige código, entradas y condiciones; no la memoria del agente.

## 51. Del resultado a la conclusión

Actividad final

¿Qué parte de la afirmación está respaldada y cuál excede la evidencia?

**Orientación docente:** Actividad final. La frase es deliberadamente excesiva, no resultado del caso. Pedir fuentes de evidencia y límites. Un ajuste favorable de estructura interna no establece por sí solo todos los usos de las puntuaciones.

## 52. Cuatro controles del trabajo

Sintetizar datos, código, método y skills

Un análisis supervisado deja evidencia, no solo una respuesta convincente.

**Orientación docente:** Sintetizar datos, código, método y skills. Reforzar que ninguna regla textual reemplaza permisos reales o políticas de privacidad. Mantener la distinción entre control computacional y evaluación metodológica.

## 53. El mismo método, otros análisis

Mostrar que se conserva el método, pero cambian el diseño, las variables, los supuestos, el modelo y las skills pertinentes

La competencia transferible es dirigir y auditar el proceso.

**Orientación docente:** Mostrar que se conserva el método, pero cambian el diseño, las variables, los supuestos, el modelo y las skills pertinentes. Ejemplificar regresión sin iniciar otro análisis completo.

## 54. Cuatro distinciones esenciales

**Generar** no equivale a **calcular**.

**Contextualizar** no equivale a **acumular instrucciones**.

**Especializar** no equivale a **garantizar la corrección**.

**Delegar ejecución** no equivale a **delegar responsabilidad**.

**Orientación docente:** Recuperar el 99 inicial y pedir que asocien cada contraste con una evidencia vista durante la sesión. Cierre sin nuevos conceptos técnicos.

## 55. Antes de tu próximo análisis

¿Qué le entregarías hoy a un agente que ayer no le habrías dado?

Responde con un documento, una restricción y una comprobación concreta.

**Orientación docente:** Ticket de salida de dos minutos. Buscar respuestas sobre contexto, permisos y evidencia, no nombres de modelos.

## 56. Un proyecto para seguir practicando

Recursos de aprendizaje

```text
materiales/
  microcaso/
  plantilla-proyecto/
  actividades.md
  guia-para-evaluar-skills.md
```

Ejecutar el microejemplo

```bash
Rscript --vanilla \
  materiales/microcaso/01_microcaso.R
```

Practica el método antes de aumentar la complejidad.

**Orientación docente:** Separar material ya ejecutable de la integración futura del caso factorial y skills. No vender una validación completada. El microejemplo puede reproducirse sin cuenta de IA. Los handouts conservan detalle que no cabe en la proyección.

## 57. Configurar un proveedor

Captura oficial del diálogo para configurar un proveedor en Positron.

La configuración concreta depende del producto y de su versión.

**Orientación docente:** Apoyo para preguntas, no instalación durante la sesión. La captura oficial muestra un proveedor específico; no obliga a elegirlo. Consultar documentación vigente, términos y acceso antes de usar credenciales. No mostrar claves reales.

## 58. Fuentes de herramientas y formatos

**Positron / MCP**
Posit, October Release Highlights (13-10-2026).

**Posit Assistant**
Getting Started y Providers.

**R Core**
Random Number Generation: set.seed / RNGversion.

**AGENTS.md**
Convención oficial: agents.md.

**Agent Skills**
Specification: agentskills.io.

**Agentes de codificación**
Documentación de Codex, Claude Code y Gemini CLI.

**Orientación docente:** Referencias completas con enlaces y fechas en docs/fuentes.md. No mostrar enlaces extensos en la proyección. Las capturas originales y sus derivados tienen registro de procedencia.

## 59. Fuentes y límites del material

**Skill de R**
r-workflow-plugins: r-analytic-coding-principles.

**AFC ordinal**
lavaan: tutorial de datos categóricos.

**Cálculos del ejemplo**
Script y salida real de R en materiales/microcaso/.

**Diagramas**
Esquemas didácticos; no resultados empíricos.

**Capturas**
Propias en perfil aislado u oficiales de Posit, identificadas.

**Caso completo**
No se presentan índices de ajuste ni coeficientes no calculados.

**Orientación docente:** Distinguir fuente, ejemplo conceptual y evidencia computacional. La referencia metodológica definitiva del caso se completará con la integración y evaluación de las skills. Esta distinción no resta valor al microejemplo ya comprobado.
