# Acompañamiento textual de la presentación

Las interfaces esquemáticas son recreaciones ficticias. Las capturas reales indican su origen. Estas descripciones complementan el visor, sin declarar conformidad completa de accesibilidad.

## 1. Uso de Agentes IA para análisis de datos e investigación

Pregunta, código, R y evidencia alrededor del criterio científico.

Una introducción al trabajo con agentes, con aplicaciones al análisis psicométrico.

**Orientación docente:** Presentar el título difundido y la promesa introductoria. Abrir con qué aprenderemos y qué no. No mostrar código ni el ejemplo de 99 en la apertura. La meta es incorporar agentes sin perder la posibilidad de continuar el análisis por nuestra cuenta.

## 2. Qué aprenderemos y qué no

Explicar el alcance antes de entrar en herramientas

Aprender a dirigir y revisar un análisis, no a dejar de comprenderlo.

**Orientación docente:** Explicar el alcance antes de entrar en herramientas. Aprenderemos a comprender, encuadrar y supervisar un agente; usaremos R y un ejemplo psicométrico. No sustituye formación en programación o metodología, ni promete investigación autónoma. La sesión no intenta enseñar todos los modelos estadísticos ni todos los agentes.

## 3. Punto de partida

¿Hasta dónde has trabajado con IA?

En el chat: 1 = conversación; 2 = código sugerido; 3 = herramientas; 4 = análisis ejecutado.

**Orientación docente:** Sondeo breve y opcional sobre experiencia con chat, código sugerido y herramientas locales. No presentar un ejercicio estadístico todavía. Graduar el detalle de las analogías según las respuestas.

## 4. El recorrido de hoy

Fundamentos, forma de trabajo, instrucciones y práctica en R.

Primero entender la necesidad; después elegir y configurar la herramienta.

**Orientación docente:** Anticipar el recorrido: fundamentos; trabajo analítico; fricciones del chat; agentes y código revisable; contexto e instrucciones; Positron y práctica. No es un temario de tecnologías desconectadas.

## 5. Un redactor que trabaja con contexto

Analogía de un modelo de lenguaje que propone continuaciones condicionadas por el contexto.

LLM: modelo de lenguaje. Genera propuestas; no certifica su verdad.

**Orientación docente:** Usar la analogía de un redactor que completa un encargo atendiendo al contexto. El modelo representa distribuciones de continuaciones; las alternativas dibujadas no son probabilidades medidas. No reducir todas sus capacidades a completar una palabra: la analogía solo introduce generación condicionada. La decodificación puede hacer más consistentes las respuestas; probabilístico no exige que cada ejecución sea distinta.

## 6. Algunos nombres conocidos

Mostrar tres marcas reconocibles, sin ranking ni versiones efímeras

Reconocer una marca no basta para saber qué herramientas tiene disponibles.

**Orientación docente:** Mostrar tres marcas reconocibles, sin ranking ni versiones efímeras. GPT es una familia de modelos y ChatGPT es un producto que los utiliza. Claude y Gemini nombran familias y productos. Los iconos identifican marcas; no representan una comparación de rendimiento ni patrocinio.

## 7. Conversar o actuar sobre el proyecto

Dar la distinción operativa en una sola lámina: un chat sin herramientas locales propone texto y código; un agente de codificación puede leer y modificar archivos, usar la terminal y encadenar acciones observando resultados

Archivos + terminal + ejecución e iteración, dentro de un alcance autorizado.

**Orientación docente:** Dar la distinción operativa en una sola lámina: un chat sin herramientas locales propone texto y código; un agente de codificación puede leer y modificar archivos, usar la terminal y encadenar acciones observando resultados. Siempre según permisos y límites. Algunas interfaces de chat también incorporan herramientas: la frontera está en las capacidades disponibles, no en el aspecto de la ventana.

## 8. Lenguaje, cálculo y criterio

Separar tres operaciones que suelen mezclarse

El modelo propone; R ejecuta; el investigador evalúa el significado.

**Orientación docente:** Contrastar generación probabilística y ejecución de instrucciones. R no verifica por sí mismo la pertinencia del análisis y puede incluir aleatoriedad: reproducibilidad exige datos, código, versiones y semillas cuando corresponda. No introducir sintaxis aún. Este reparto de funciones permite hablar del uso de LLM en análisis de datos.

## 9. Más capacidad, el mismo criterio

Presentar el potencial: acelerar tareas mecánicas, bosquejar código, explorar documentación y revisar errores

Aprovechar la ejecución asistida sin renunciar a comprender el análisis.

**Orientación docente:** Presentar el potencial: acelerar tareas mecánicas, bosquejar código, explorar documentación y revisar errores. Puede aumentar la productividad al aprender a dirigirlo, pero el beneficio depende de tarea, experiencia y supervisión; no afirmar una ganancia garantizada. No reemplaza aprender a programar ni a juzgar el método. No generalizar que el desarrollo de software prescinde de revisión; la investigación exige una revisión metodológica explícita.

## 10. Un código del que podamos hacernos cargo

Fijar el contrato de aprendizaje: leer, revisar, ejecutar, modificar y depurar, incluso sin el agente

No queremos un análisis que solo el LLM pueda mantener.

**Orientación docente:** Fijar el contrato de aprendizaje: leer, revisar, ejecutar, modificar y depurar, incluso sin el agente. Poder continuar no significa memorizar toda la sintaxis; implica localizar decisiones, entender objetos y seguir diagnósticos. Este objetivo distingue nuestro estilo de análisis. La revisión humana no puede ser nominal si el código es opaco.

## 11. Una petición de análisis en el chat

Mostrar una recreación explícitamente ficticia de ChatGPT web

**Orientación docente:** Mostrar una recreación explícitamente ficticia de ChatGPT web. El usuario pide contrastar dos factores en doce ítems ordinales. La respuesta propone revisar el diccionario y aporta un fragmento de código. No es una captura real ni una respuesta evaluada de un modelo; sirve para seguir el recorrido de trabajo.

## 12. Del bloque de código a RStudio

Mantener fija la petición y el mismo fragmento de código

**Orientación docente:** Mantener fija la petición y el mismo fragmento de código. La persona copia el bloque del chat y lo pega en un script de RStudio. Mostrar que entre ambas ventanas hay un paso manual. El fragmento está abreviado y no se distribuye como receta de AFC; el método requiere especificación previa. No afirmar que todo copiado produce errores.

## 13. Del error de vuelta al chat

En el mismo escenario ficticio, falta cargar una función y aparece un error ilustrativo de R

El usuario transporta código, resultados y contexto de una ventana a otra.

**Orientación docente:** En el mismo escenario ficticio, falta cargar una función y aparece un error ilustrativo de R. La persona debe copiar el mensaje, explicar el estado de la sesión y probar otra propuesta. No se atribuye este fallo a un producto concreto ni se representa como ejecución observada. Identificar fricciones posibles: omisiones, bloques desactualizados, objetos de sesión y diagnóstico de rutas o paquetes.

## 14. Una posibilidad distinta

¿Y si el LLM pudiera ejecutar el código y observar qué ocurrió?

Sin que tú tengas que copiar cada resultado de vuelta.

**Orientación docente:** Usar esta pregunta como transición, no como actividad larga. La definición breve de agente ya se vio; ahora aparece la razón práctica para usarlo. Mantener visible que poder ejecutar no implica elegir correctamente el método.

## 15. El agente dentro del proyecto

Mostrar el ciclo archivos, ejecución, observación y corrección

Se reduce el intercambio manual; no desaparece la supervisión.

**Orientación docente:** Mostrar el ciclo archivos, ejecución, observación y corrección. El agente puede inspeccionar el directorio, ejecutar R, leer el mensaje, modificar el script y volver a probar, según permisos. Puede mantener una tarea durante varias iteraciones, no de forma ilimitada ni infalible. La persona decide alcance, metodología y qué cambios requieren aprobación.

## 16. Human Gates: puntos de revisión

Recorrer los carriles

Antes del método, ante cambios sustantivos y antes de interpretar.

**Orientación docente:** Definir Human Gates como puntos de decisión y revisión humana. Antes: confirmar pregunta, datos, hipótesis y procedimiento. Durante: detenerse ante recodificación ambigua, cambio de modelo o supuesto. Después: revisar código, diagnósticos e interpretación. No pedir autorización para cada comando inocuo; definir autonomía proporcional. Una línea ejecutada correctamente no resuelve una decisión científica.

## 17. El problema que sigue abierto

El agente ya lo ejecutó. ¿Puedes modificar el análisis tú?

Piensa en cambiar un solo modelo, una recodificación o un gráfico.

**Orientación docente:** La ganancia operativa no garantiza legibilidad. Dar paso al problema de código orientado a un entorno distinto del nuestro. Evitar afirmar que todos los LLM están entrenados para priorizar pipelines; lo que se discute es un patrón de salida posible que queremos encauzar.

## 18. Un cambio pequeño, demasiados lugares

Proyecto ficticio con modelos definidos en configuración, función safe_cfa en helpers, un bucle en otro script y clasificación de resultados aparte

La organización debe facilitar la siguiente decisión del investigador.

**Orientación docente:** Proyecto ficticio con modelos definidos en configuración, función safe_cfa en helpers, un bucle en otro script y clasificación de resultados aparte. Pregunta: dónde cambiar un único AFC y revisar lo que ocurrió. La división en scripts no es por sí misma un defecto; el problema es dispersar decisiones que se modifican juntas y dificultar la inspección del investigador.

## 19. Qué puede esconder una función auxiliar

Una envoltura demasiado silenciosa

```r
safe_cfa <- function(modelo, datos) {
  tryCatch(
    suppressWarnings(
      lavaan::cfa(modelo, data = datos)
    ),
    error = function(e) NULL
  )
}
```

Comparación mecánica de modelos

```r
for (nombre in names(modelos)) {
  ajustes[[nombre]] <- safe_cfa(
    modelos[[nombre]], datos
  )
}

# ¿Dónde revisas estimador y fallos?
```

Ejecutar muchos modelos no equivale a contrastar hipótesis justificadas.

**Orientación docente:** safe_cfa es un nombre ficticio, no una función de lavaan. En este antiejemplo, warnings y fallos dejan de ser visibles. La envoltura también puede ocultar argumentos y decisiones. Ni for ni las funciones auxiliares son incorrectos en general: se cuestiona que escondan las decisiones del estudio. No recomendar este código ni atribuirlo al entrenamiento universal de los LLM.

## 20. Un AFC que podamos revisar y modificar

```r
modelo <- '
  planificacion =~ i01 + i02 + i03 + i04 + i05 + i06
  persistencia  =~ i07 + i08 + i09 + i10 + i11 + i12
'

ajuste <- lavaan::cfa(
  modelo, data = datos, ordered = items, estimator = "WLSMV"
)
summary(ajuste, fit.measures = TRUE, standardized = TRUE)
```

Especificación, estimación e inspección juntas; las decisiones siguen siendo tuyas.

**Orientación docente:** El objeto es la organización del código, no enseñar AFC desde cero. Mostrar especificación, estimación y diagnóstico cerca. datos e items son entradas del estudio aún por definir: este fragmento es ilustrativo y no se ha ejecutado. WLSMV está escrito como decisión visible del ejemplo, no impuesto como regla general. Alterar una estructura factorial necesita justificación sustantiva, no solo editar una línea.

## 21. La preparación de datos también debe verse

Transformaciones escondidas

```r
source("R/preparacion.R")
datos <- clean_data(ruta)

# ¿Qué códigos cambió?
# ¿Qué ítems invirtió?
# ¿Qué casos excluyó?
```

Reglas explícitas en el análisis

```r
datos <- readr::read_csv(
  "data/escala.csv", na = "NS"
)
datos <- datos |>
  dplyr::mutate(i03 = 5 - i03)
```

Lo que cambia el significado de los datos debe poder localizarse.

**Orientación docente:** Ejemplo ficticio: el diccionario define NS como perdido y la clave define i03 como inverso en respuestas de 1 a 4. No inferir estas reglas de las correlaciones. clean_data es una función inventada de contenido no mostrado, no se afirma equivalencia entre fragmentos. La derecha muestra dónde revisar la decisión. Las validaciones sustantivas y el registro de exclusiones se conservan.

## 22. Un error visible también informa

Continuar como si nada hubiera pasado

```r
datos <- tryCatch(
  readr::read_csv(ruta),
  error = function(e) tibble::tibble()
)
# Falla la lectura, pero devuelve
# una tabla vacía.
```

Diagnosticar el problema concreto

Leer con una llamada ordinaria.
Inspeccionar el error de ruta o paquete.
Corregir su causa en el entorno.
Conservar las comprobaciones del estudio.

Controles proporcionados; diagnósticos visibles; sin errores maquillados.

**Orientación docente:** No enseñar a retirar todos los controles: distinguir un fallo de lectura real de una rutina genérica que lo silencia. El agente puede inspeccionar archivos y mensajes en vez de añadir manejadores para cada escenario imaginable. Los riesgos silenciosos concretos, por ejemplo una unión muchos-a-muchos inesperada, sí pueden requerir controles persistentes.

## 23. El estilo depende del trabajo

Contrastar una tarea estable y repetitiva con una investigación iterativa en la que se revisa cada modelo

Automatizar mecánica estable; mantener editables las decisiones que evolucionan.

**Orientación docente:** Contrastar una tarea estable y repetitiva con una investigación iterativa en la que se revisa cada modelo. Funciones, bucles y pipelines pueden ser apropiados en simulaciones o procesos acordados; el taller no contrapone reproducibilidad y legibilidad. Un modelo generalista puede proponer un estilo que no coincide con nuestras prioridades. Presentarlo como riesgo observable, no como afirmación no comprobada sobre todo su entrenamiento.

## 24. Lo que rodea al agente

Dar un solo mapa

**Orientación docente:** Dar un solo mapa. Harness: programa que organiza el ciclo, el contexto, herramientas y permisos. System prompt: reglas iniciales del producto o implementación. AGENTS.md: guía persistente del proyecto en agentes compatibles. Skills: procedimientos y recursos reutilizables. Plugins: una vía de empaquetarlos junto con herramientas. MCP: conexión con herramientas. No son sinónimos ni todos se configuran del mismo modo.

## 25. Nuestro foco: contexto y forma de trabajar

Repetir el mismo mapa, destacando únicamente AGENTS

El proyecto explica qué investigamos; las instrucciones orientan cómo trabajamos.

**Orientación docente:** Repetir el mismo mapa, destacando únicamente AGENTS.md y skills. No redibujar todo ni sumar definiciones. Ambas responden a lo que acabamos de observar: el agente necesita contexto del estudio y un procedimiento de trabajo orientado a investigación. MCP y el harness se utilizarán después al montar Positron.

## 26. Como un analista que llega al equipo

Diferenciar conocimiento general de investigación de contexto específico del estudio

Conocer estadística no equivale a conocer tu estudio.

**Orientación docente:** Conectar la analogía con el mapa anterior, sin iniciar otro bloque de definiciones. El analista necesita objetivos, diseño, datos y normas. El LLM puede tener conocimiento general, pero no sabe qué se acordó en este estudio ni cómo queremos revisar los modelos.

## 27. Proyecto, guía y procedimientos

Ubicación de documentos científicos, reglas del proyecto y procedimientos reutilizables.

Una fuente para cada decisión; las demás instrucciones la enlazan.

**Orientación docente:** Explicar en conjunto: protocolo y especificación para objetivos, diseño e hipótesis; diccionario para variables; AGENTS.md para rutas, restricciones y expectativas persistentes; skills para estilo y procedimientos reutilizables. AGENTS.md puede contener normas cortas de estilo si basta; una skill resulta útil si el contenido es largo, especializado o se reutiliza. No exigir fragmentación artificial ni duplicar todo en ambos.

## 28. AGENTS.md y la skill trabajando juntos

Guía del proyecto

```markdown
# Antes de analizar
- Lee docs/protocolo.md.
- Consulta docs/diccionario.csv.
- Conserva los datos originales.
- Usa la skill de estilo R disponible.
- Consulta cambios metodológicos.
```

Procedimiento reutilizable

La skill desarrolla el estilo de código,
las comprobaciones y sus límites.
El protocolo decide el método del estudio.
AGENTS.md no sustituye ese protocolo.

No duplicar la guía entera de R en cada proyecto.

**Orientación docente:** Este archivo es un ejemplo de coordinación, no una invocación garantizada. r-analytic-coding-principles debe estar instalado y visible; su carga depende del agente. Otros productos pueden utilizar CLAUDE.md o GEMINI.md: el concepto es transferible, el nombre y prioridad se verifican. AGENTS.md no es sinónimo de system prompt ni un control de seguridad de ejecución.

## 29. La skill de codificación que utilizaremos

Captura propia del archivo real SKILL.md de r-analytic-coding-principles abierto en Positron.

Lee la finalidad, el alcance y los límites antes de utilizarla.

**Orientación docente:** Captura propia del archivo r-analytic-core/r-analytic-coding-principles. Leer solo la finalidad: código que el investigador pueda inspeccionar, editar y retomar. Vincularlo con safe_cfa, lectura de datos y diagnósticos, no con una lista abstracta de buenas prácticas. No afirmar que ver el archivo prueba que un agente lo haya cargado.

## 30. Qué contiene y cuándo ayuda una skill

Cuándo usarla

**Nombre y descripción:** activación y alcance.
**Instrucciones:** cómo desarrollar la tarea.
**Límites:** qué no debe decidir por nosotros.

Qué puede acompañarla

Referencias que se consultan al necesitarlas.
Ejemplos y recursos de apoyo.
Scripts opcionales que hay que revisar.
No reentrena el modelo ni valida el resultado.

Reutilizar un procedimiento sin convertirlo en una regla ciega.

**Orientación docente:** Mantener la explicación junto con AGENTS.md. La estructura puede incluir SKILL.md, referencias, scripts y assets. No toda skill trae código ejecutable. Las descripciones pueden facilitar descubrimiento; no garantizar activación automática ni portabilidad idéntica.

## 31. Las skills del taller

Mostrar r-analytic-core como base actualmente inspeccionable

La misma fuente de skills; una versión comprobada para la demostración.

**Orientación docente:** Mostrar r-analytic-core como base actualmente inspeccionable. Reservar dos espacios de alcance para datos y análisis psicométrico que se integrarán desde el EPIC; no inventar nombres definitivos ni versión publicada. No se crea una copia paralela de las skills en el taller. Al cerrar el EPIC, fijar versión, alcance y prueba con el caso.

## 32. ¿Dónde guardarías cada información?

«Dos factores propuestos»
«Código R editable modelo por modelo»

¿Qué pertenece al estudio y qué se puede reutilizar en otros proyectos?

**Orientación docente:** Actividad breve: hipótesis de estructura al protocolo o especificación; estilo R a una skill o guía reutilizable. La regla local puede enlazarla desde AGENTS.md. Aceptar soluciones de organización equivalentes siempre que no mezclen autoridad científica y procedimiento genérico.

## 33. La planificación proporcional

No exigir un plan

Planificar es explicitar decisiones; no producir archivos por reflejo.

**Orientación docente:** Recordar la proporcionalidad: un encargo pequeño no necesita plan.md; sí objetivos, datos y criterios suficientes. Un estudio con varias fases puede necesitar planificación escrita. El nombre del archivo no sustituye pensar el diseño. Esta regla evita que la solución a la opacidad sea más burocracia.

## 34. Antes de adoptar una skill

Dar un ejemplo de recomendación metodológica rígida y otro de script externo no revisado

Revisar también lo que la skill puede ejecutar.

**Orientación docente:** Revisar procedencia, contenido, permisos y un caso de prueba. Una skill externa puede contener instrucciones equivocadas o scripts peligrosos. Mostrar que la guía de estilo no elimina diagnóstico ni aprobación humana. No instalar recursos desconocidos durante el taller.

## 35. Pausa

10

Al volver: preparar el entorno y recorrer el caso en R.

**Orientación docente:** Pausa prevista de diez minutos tras los fundamentos y las instrucciones. Es un punto de ajuste del ritmo, no un nuevo módulo.

## 36. Positron por dentro

Captura propia de Positron con el script del microejemplo y resultados reales en la consola.

**1 · Script.** Instrucciones que podemos leer y modificar.

**2 · Consola R.** Lugar donde se ejecutan los cálculos.

**3 · Salida.** Evidencia que debe coincidir con lo reportado.

No basta con la respuesta del chat: observa dónde se ejecuta.

**Orientación docente:** Ahora que sabemos qué exigimos al código y al contexto, presentar Positron como entorno de trabajo. Localizar script, consola y salida en una captura propia. La captura usa un ejemplo sintético, no un agente: no fingir conexión. El archivo sigue siendo el entregable, aunque exploremos en una sesión persistente.

## 37. Una herramienta para practicar

Agente externo: Codex, Claude Code o Gemini CLI.

Positron + MCP conecta al agente con la sesión de R.

Alternativa integrada: Posit Assistant en Positron o RStudio.

Elegimos una vía y verificamos permisos, contexto y resultados.

**Orientación docente:** Mostrar las opciones después del método. No exigir cuatro instalaciones ni comparar precios. Una misma familia de modelos puede participar en varias interfaces. Verificar compatibilidad real de skills, instrucciones y MCP en el agente elegido.

## 38. MCP: el puente hacia R

Definir Model Context Protocol una sola vez

Sesión compartida para explorar; archivos para reproducir.

**Orientación docente:** Definir MCP como protocolo de conexión, no como un modelo ni una skill. La integración experimental de Positron 2026.10 permite listar sesiones, ejecutar código e inspeccionar resultados. El proceso de configuración se muestra inmediatamente después. No prometer compatibilidad universal.

## 39. Conectar el agente a Positron

1 · Activar el servidor

Captura propia de la opción experimental ai.mcp.enabled en un perfil aislado.

2 · Añadir el cliente

Captura propia de la búsqueda del comando Positron MCP: Add to Coding Agent, sin ejecutarlo.

Configuración local y permisos acotados; nunca proyectar credenciales.

**Orientación docente:** Abrir proyecto e iniciar una sesión R. En Settings buscar ai.mcp.enabled y activarlo. Después usar Positron MCP: Add to Coding Agent para Codex o Gemini CLI; la nota oficial describe configuración automática para Claude Code. Otros clientes requieren Copy Connection Details. No proyectar URL con token, claves API ni archivos de credenciales. Las capturas muestran el ajuste y el comando, no una conexión completada. Consultar la guía de herramientas para pasos y alcance.

## 40. Comprobar la conexión, no solo activarla

Pedido de comprobación

```text
Lista las sesiones disponibles.
Identifica la sesión R del taller.
Ejecuta sum(1:4) en esa sesión.
Muestra la salida y no modifiques
archivos ni configuraciones.
```

Qué debemos observar

La sesión correcta.
La llamada a la herramienta.
El código y el nombre del agente.
La salida 10 en la consola R.

Una respuesta correcta no basta: importa dónde y cómo se obtuvo.

**Orientación docente:** Prueba a realizar con el cliente definitivo; no afirmar que ya se ejecutó vía MCP. sum(1:4) vale 10, pero obtener 10 en un chat no prueba acceso a esa sesión: debe observarse la llamada y su procedencia en Positron. Inspeccionar alcance de archivos y directorio de trabajo antes del caso. El kit incluye una lista de comprobación.

## 41. Una llamada visible a una herramienta

Captura oficial de Claude Code conectado a Positron: llamadas a herramientas, ejecución en consola y gráfico.

**1 · Solicitud.** El agente llama a una herramienta de Positron.

**2 · Ejecución.** La consola identifica el código del agente.

**3 · Resultado.** Un gráfico observable, no solo una descripción.

La llamada y la salida dejan rastros que podemos inspeccionar.

**Orientación docente:** Mostrar la captura oficial como referencia de lo que se busca comprobar: llamada a herramienta, consola identificada y salida. Proviene de otro proyecto publicado por Posit. No es ejecución de este taller. Si el equipo dispone de una captura propia del agente definitivo, sustituirla manteniendo las tres regiones anotadas.

## 42. Posit Assistant: otra forma de entrar

Recorte oficial de Posit Assistant: lectura de una skill, comando y apertura de datos.

**Pedir.** Formular una tarea dentro del entorno.

**Inspeccionar.** Observar las instrucciones y herramientas utilizadas.

**Comprobar.** Revisar el objeto abierto y el resultado.

Un proveedor configurado; ningún secreto en las diapositivas.

**Orientación docente:** Alternativa integrada a un agente externo. Mostrar petición, acceso a herramientas y revisión en la captura oficial. Requiere un proveedor compatible configurado; el acceso y las credenciales se resuelven fuera de la proyección. Evitar duplicar una instalación si ya se eligió la vía externa.

## 43. Del diccionario al modelo

07

Dirigir un análisis, revisar sus decisiones y poder continuarlo sin IA.

**Orientación docente:** Inicio de la práctica. Abrir el proyecto, leer contexto y mostrar el script que se construye. El caso factorial completo sigue pendiente de datos y validación; las láminas diferencian hipótesis, microejemplo comprobado y futuros resultados. No presentar números ajustados inexistentes.

## 44. Respuestas ordinales

Matriz ilustrativa ficticia, no resultados de la escala final

Primero, entender la estructura y los códigos.

**Orientación docente:** Presentar la matriz didáctica, el diseño previsto de 500 casos y 12 ítems, y las dos dimensiones. La matriz dibujada es ficticia y no es un extracto de un archivo analizado. Se revisará el diccionario antes de modelar. Mostrar después la hipótesis factorial.

## 45. El encargo para la demostración

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

**Orientación docente:** Aplicar las instrucciones del proyecto y la skill disponible antes de ejecutar. El encargo pide inspección, preguntas pendientes, código legible y evidencias. No exigir un plan.md. El investigador revisa los cambios de método; el agente puede realizar operaciones rutinarias autorizadas.

## 46. Antes de aceptar un cálculo

Pedir al grupo que anticipe qué información revisaría antes de aceptar la media

¿Qué falta saber antes de aceptar el resultado?

**Orientación docente:** Ahora, dentro de la práctica, mostrar las cinco respuestas ficticias. Pedir qué significa 99 y qué documento lo decide. No se usa esta pregunta para abrir el taller, sino para ejercitar la revisión ya aprendida.

## 47. Una ejecución sin errores

Mostrar que R efectivamente ejecutó el código y devolvió 21

El código funciona; el análisis puede seguir estando mal.

**Orientación docente:** Salida real de R para el microejemplo: mean de 1,2,3,4,99 es 21.8. El error didáctico es semántico, no computacional. No atribuirlo a un agente concreto. Buscar el diccionario antes de corregir.

## 48. La corrección documentada

Regresar al mismo vector del inicio y cambiar solo el tratamiento documentado de 99

La corrección debe quedar en código y conservar el original.

**Orientación docente:** El diccionario del microejemplo define 99 como perdido. La recodificación explícita produce media 2.5 con cuatro observaciones válidas. Mostrar código y denominador, conservar los originales y vincular la corrección con el criterio humano. No confundir este ejemplo con un análisis de fiabilidad.

## 49. La salida real de R

Recorte de consola Positron que muestra las medias 21.8 y 2.5 y el recuento válido de 4.

Los números del relato deben coincidir con la evidencia de ejecución.

**Orientación docente:** Captura propia de la consola del microejemplo, también reproducida desde una sesión limpia de R. Verificar que aparecen 21.8, 2.5 y 4. La captura no prueba ejecución por un agente ni un ajuste factorial completo.

## 50. La estructura que vamos a contrastar

Dos factores correlacionados y doce indicadores; los nombres de dimensiones son didácticos y corresponden a autorregulación académica

El modelo expresa una hipótesis; no es un dibujo que el agente deba adivinar.

**Orientación docente:** Hipótesis de dos factores y doce indicadores. Residuos omitidos solo en el esquema. Contrastar con el código explícito mostrado antes: cambiar un ítem afecta una decisión sustantiva. Los coeficientes y diagnósticos del caso completo se incorporarán cuando se hayan ejecutado y verificado.

## 51. Después de la convergencia

Introducir el significado de converger: el procedimiento alcanzó un criterio de parada

Un algoritmo que termina todavía deja preguntas importantes.

**Orientación docente:** Después de ejecutar un AFC no basta el mensaje de convergencia. Revisar admisibilidad, parámetros, ajuste local/global y coherencia sustantiva. No se muestran índices de ajuste fabricados. Identificar qué procedimiento realizará el agente y qué evaluación corresponde al investigador.

## 52. Volver a empezar desde los archivos

Mostrar sesión persistente frente a ejecución limpia

Reproducir el cálculo también permite reproducir un error: todavía hay que interpretarlo.

**Orientación docente:** Volver a ejecutar el script desde archivos en una sesión limpia. La sesión persistente ayuda a explorar, pero no debe crear dependencia de objetos invisibles. La reproducibilidad conserva también los errores, así que revisar significado y decisiones sigue siendo necesario.

## 53. Del resultado a la conclusión

Actividad final

¿Qué parte de la afirmación está respaldada y cuál excede la evidencia?

**Orientación docente:** Auditar la frase que infiere validez global solo del ajuste factorial. Es una afirmación ficticia para discutir, no un resultado del taller. Pedir datos, código, diagnósticos y delimitación de la inferencia. Recuperar los Human Gates antes de redactar conclusiones.

## 54. Lo que conservamos al delegar

**La pregunta** y las decisiones metodológicas.

**El código**, legible y modificable por nosotros.

**La revisión**, en los puntos donde importa decidir.

**La evidencia**, ejecutada y reproducible.

**Orientación docente:** Cerrar sin novedades. Contrastar el inicio con el recorrido: ya no solo se recibe código, se dirige un proceso que podemos revisar y continuar. No prometer productividad automática; la mejora depende del uso competente y del contexto.

## 55. Un proyecto para seguir practicando

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

**Orientación docente:** Materiales reales disponibles: microcaso, plantilla de contexto, ejemplos de estilo y guía de herramientas. Identificar claramente el caso factorial y skills en desarrollo. No abrir otra unidad al cierre. Recordar ruta del proyecto y fuente QMD única.

## 56. Fuentes de herramientas y formatos

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

**Orientación docente:** Fuentes oficiales y enlaces completos en docs/fuentes.md. Esta lámina es apoyo, no tiempo de exposición obligatorio. Se añadieron fuentes sobre harness y configuración de MCP; no usar citas de producto como prueba de productividad universal.

## 57. Fuentes y límites del material

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

**Orientación docente:** Distinguir ejemplos de código ficticio, esquemas, capturas reales propias/oficiales y microejemplo ejecutado. La skill del repositorio fundamenta nuestras convenciones, no demuestra que todos los agentes produzcan el mismo estilo de código.
