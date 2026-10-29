# Guion docente de la presentación vigente

Fuente: `presentacion/deck.qmd`. 58 diapositivas: 56 del recorrido, incluida la pausa, y dos de referencias. La práctica empieza con insumos sin configurar; consultar `practica-guiada.md` para tiempos y permisos.

## 1. Uso de Agentes IA para análisis de datos e investigación

Presentar el título difundido y la promesa introductoria. Abrir con qué aprenderemos y qué no. No mostrar código ni el ejemplo de 99 en la apertura. La meta es incorporar agentes sin perder la posibilidad de continuar el análisis por nuestra cuenta.

## 2. Qué aprenderemos y qué no

Explicar el alcance antes de entrar en herramientas. Aprenderemos a comprender, encuadrar y supervisar un agente; usaremos R y un ejemplo psicométrico. No sustituye formación en programación o metodología, ni promete investigación autónoma. La sesión no intenta enseñar todos los modelos estadísticos ni todos los agentes.

## 3. Punto de partida

Sondeo breve y opcional sobre experiencia con chat, código sugerido y herramientas locales. No presentar un ejercicio estadístico todavía. Graduar el detalle de las analogías según las respuestas.

## 4. El recorrido de hoy

Anticipar el recorrido: fundamentos; trabajo analítico; fricciones del chat; agentes y código revisable; contexto e instrucciones; Positron y práctica. No es un temario de tecnologías desconectadas.

## 5. Un redactor que trabaja con contexto

Usar la analogía de un redactor que completa un encargo atendiendo al contexto. El modelo representa distribuciones de continuaciones; las alternativas dibujadas no son probabilidades medidas. No reducir todas sus capacidades a completar una palabra: la analogía solo introduce generación condicionada. La decodificación puede hacer más consistentes las respuestas; probabilístico no exige que cada ejecución sea distinta.

## 6. Algunos nombres conocidos

Mostrar tres marcas reconocibles, sin ranking ni versiones efímeras. GPT es una familia de modelos y ChatGPT es un producto que los utiliza. Claude y Gemini nombran familias y productos. Los iconos identifican marcas; no representan una comparación de rendimiento ni patrocinio.

## 7. Conversar o actuar sobre el proyecto

Dar la distinción operativa en una sola lámina: un chat sin herramientas locales propone texto y código; un agente de codificación puede leer y modificar archivos, usar la terminal y encadenar acciones observando resultados. Siempre según permisos y límites. Algunas interfaces de chat también incorporan herramientas: la frontera está en las capacidades disponibles, no en el aspecto de la ventana.

## 8. Lenguaje, cálculo y criterio

Contrastar generación probabilística y ejecución de instrucciones. R no verifica por sí mismo la pertinencia del análisis y puede incluir aleatoriedad: reproducibilidad exige datos, código, versiones y semillas cuando corresponda. No introducir sintaxis aún. Este reparto de funciones permite hablar del uso de LLM en análisis de datos.

## 9. Más capacidad, el mismo criterio

Presentar el potencial: acelerar tareas mecánicas, bosquejar código, explorar documentación y revisar errores. Puede aumentar la productividad al aprender a dirigirlo, pero el beneficio depende de tarea, experiencia y supervisión; no afirmar una ganancia garantizada. No reemplaza aprender a programar ni a juzgar el método. No generalizar que el desarrollo de software prescinde de revisión; la investigación exige una revisión metodológica explícita.

## 10. Un código del que podamos hacernos cargo

Fijar el contrato de aprendizaje: leer, revisar, ejecutar, modificar y depurar, incluso sin el agente. Poder continuar no significa memorizar toda la sintaxis; implica localizar decisiones, entender objetos y seguir diagnósticos. Este objetivo distingue nuestro estilo de análisis. La revisión humana no puede ser nominal si el código es opaco.

## 11. Una petición de análisis en el chat

Mostrar una recreación explícitamente ficticia de ChatGPT web. El usuario pide contrastar dos factores en doce ítems ordinales. La respuesta propone revisar el diccionario y aporta un fragmento de código. No es una captura real ni una respuesta evaluada de un modelo; sirve para seguir el recorrido de trabajo.

## 12. Del bloque de código a RStudio

Mantener fija la petición y el mismo fragmento de código. La persona copia el bloque del chat y lo pega en un script de RStudio. Mostrar que entre ambas ventanas hay un paso manual. El fragmento está abreviado y no se distribuye como receta de AFC; el método requiere especificación previa. No afirmar que todo copiado produce errores.

## 13. Del error de vuelta al chat

En el mismo escenario ficticio, falta cargar una función y aparece un error ilustrativo de R. La persona debe copiar el mensaje, explicar el estado de la sesión y probar otra propuesta. No se atribuye este fallo a un producto concreto ni se representa como ejecución observada. Identificar fricciones posibles: omisiones, bloques desactualizados, objetos de sesión y diagnóstico de rutas o paquetes.

## 14. Una posibilidad distinta

Usar esta pregunta como transición, no como actividad larga. La definición breve de agente ya se vio; ahora aparece la razón práctica para usarlo. Mantener visible que poder ejecutar no implica elegir correctamente el método.

## 15. El agente dentro del proyecto

Mostrar el ciclo archivos, ejecución, observación y corrección. El agente puede inspeccionar el directorio, ejecutar R, leer el mensaje, modificar el script y volver a probar, según permisos. Puede mantener una tarea durante varias iteraciones, no de forma ilimitada ni infalible. La persona decide alcance, metodología y qué cambios requieren aprobación.

## 16. Human Gates: puntos de revisión

Definir Human Gates como puntos de decisión y revisión humana. Antes: confirmar pregunta, datos, hipótesis y procedimiento. Durante: detenerse ante recodificación ambigua, cambio de modelo o supuesto. Después: revisar código, diagnósticos e interpretación. No pedir autorización para cada comando inocuo; definir autonomía proporcional. Una línea ejecutada correctamente no resuelve una decisión científica.

## 17. El problema que sigue abierto

La ganancia operativa no garantiza legibilidad. Dar paso al problema de código orientado a un entorno distinto del nuestro. Evitar afirmar que todos los LLM están entrenados para priorizar pipelines; lo que se discute es un patrón de salida posible que queremos encauzar.

## 18. Un cambio pequeño, demasiados lugares

Proyecto ficticio con modelos definidos en configuración, función safe_cfa en helpers, un bucle en otro script y clasificación de resultados aparte. Pregunta: dónde cambiar un único AFC y revisar lo que ocurrió. La división en scripts no es por sí misma un defecto; el problema es dispersar decisiones que se modifican juntas y dificultar la inspección del investigador.

## 19. Qué puede esconder una función auxiliar

safe_cfa es un nombre ficticio, no una función de lavaan. En este antiejemplo, warnings y fallos dejan de ser visibles. La envoltura también puede ocultar argumentos y decisiones. Ni for ni las funciones auxiliares son incorrectos en general: se cuestiona que escondan las decisiones del estudio. No recomendar este código ni atribuirlo al entrenamiento universal de los LLM.

## 20. Un AFC que podamos revisar y modificar

El objeto es la organización del código, no enseñar AFC desde cero. Mostrar especificación, estimación y diagnóstico cerca. datos e items son entradas del estudio aún por definir: este fragmento es ilustrativo y no se ha ejecutado. WLSMV está escrito como decisión visible del ejemplo, no impuesto como regla general. Alterar una estructura factorial necesita justificación sustantiva, no solo editar una línea.

## 21. La preparación de datos también debe verse

Ejemplo ficticio: el diccionario define NS como perdido y la clave define i03 como inverso en respuestas de 1 a 4. No inferir estas reglas de las correlaciones. clean_data es una función inventada de contenido no mostrado, no se afirma equivalencia entre fragmentos. La derecha muestra dónde revisar la decisión. Las validaciones sustantivas y el registro de exclusiones se conservan.

## 22. Un error visible también informa

No enseñar a retirar todos los controles: distinguir un fallo de lectura real de una rutina genérica que lo silencia. El agente puede inspeccionar archivos y mensajes en vez de añadir manejadores para cada escenario imaginable. Los riesgos silenciosos concretos, por ejemplo una unión muchos-a-muchos inesperada, sí pueden requerir controles persistentes.

## 23. El estilo depende del trabajo

Contrastar una tarea estable y repetitiva con una investigación iterativa en la que se revisa cada modelo. Funciones, bucles y pipelines pueden ser apropiados en simulaciones o procesos acordados; el taller no contrapone reproducibilidad y legibilidad. Un modelo generalista puede proponer un estilo que no coincide con nuestras prioridades. Presentarlo como riesgo observable, no como afirmación no comprobada sobre todo su entrenamiento.

## 24. Lo que rodea al agente

Dar un solo mapa. Harness: programa que organiza el ciclo, el contexto, herramientas y permisos. System prompt: reglas iniciales del producto o implementación. AGENTS.md: guía persistente del proyecto en agentes compatibles. Skills: procedimientos y recursos reutilizables. Plugins: una vía de empaquetarlos junto con herramientas. MCP: conexión con herramientas. No son sinónimos ni todos se configuran del mismo modo.

## 25. Nuestro foco: contexto y forma de trabajar

Repetir el mismo mapa, destacando únicamente AGENTS.md y skills. No redibujar todo ni sumar definiciones. Ambas responden a lo que acabamos de observar: el agente necesita contexto del estudio y un procedimiento de trabajo orientado a investigación. MCP y el harness se utilizarán después al montar Positron.

## 26. Como un analista que llega al equipo

Conectar la analogía con el mapa anterior, sin iniciar otro bloque de definiciones. El analista necesita objetivos, diseño, datos y normas. El LLM puede tener conocimiento general, pero no sabe qué se acordó en este estudio ni cómo queremos revisar los modelos.

## 27. Proyecto, guía y procedimientos

Explicar en conjunto: protocolo y especificación para objetivos, diseño e hipótesis; diccionario para variables; AGENTS.md para rutas, restricciones y expectativas persistentes; skills para estilo y procedimientos reutilizables. AGENTS.md puede contener normas cortas de estilo si basta; una skill resulta útil si el contenido es largo, especializado o se reutiliza. No exigir fragmentación artificial ni duplicar todo en ambos.

## 28. AGENTS.md y la skill trabajando juntos

Este archivo es un ejemplo de coordinación, no una invocación garantizada. r-analytic-coding-principles debe estar instalado y visible; su carga depende del agente. Otros productos pueden utilizar CLAUDE.md o GEMINI.md: el concepto es transferible, el nombre y prioridad se verifican. AGENTS.md no es sinónimo de system prompt ni un control de seguridad de ejecución.

## 29. La skill de codificación que utilizaremos

Captura propia del archivo r-analytic-core/r-analytic-coding-principles. Leer solo la finalidad: código que el investigador pueda inspeccionar, editar y retomar. Vincularlo con safe_cfa, lectura de datos y diagnósticos, no con una lista abstracta de buenas prácticas. No afirmar que ver el archivo prueba que un agente lo haya cargado.

## 30. Qué contiene y cuándo ayuda una skill

Mantener la explicación junto con AGENTS.md. La estructura puede incluir SKILL.md, referencias, scripts y assets. No toda skill trae código ejecutable. Las descripciones pueden facilitar descubrimiento; no garantizar activación automática ni portabilidad idéntica.

## 31. Las skills del taller

Mostrar r-analytic-core como base actualmente inspeccionable. Reservar dos espacios de alcance para datos y análisis psicométrico que se integrarán desde el EPIC; no inventar nombres definitivos ni versión publicada. No se crea una copia paralela de las skills en el taller. Al cerrar el EPIC, fijar versión, alcance y prueba con el caso.

## 32. ¿Dónde guardarías cada información?

Actividad breve: hipótesis de estructura al protocolo o especificación; estilo R a una skill o guía reutilizable. La regla local puede enlazarla desde AGENTS.md. Aceptar soluciones de organización equivalentes siempre que no mezclen autoridad científica y procedimiento genérico.

## 33. La planificación proporcional

Recordar la proporcionalidad: un encargo pequeño no necesita plan.md; sí objetivos, datos y criterios suficientes. Un estudio con varias fases puede necesitar planificación escrita. El nombre del archivo no sustituye pensar el diseño. Esta regla evita que la solución a la opacidad sea más burocracia.

## 34. Antes de adoptar una skill

Revisar procedencia, contenido, permisos y un caso de prueba. Una skill externa puede contener instrucciones equivocadas o scripts peligrosos. Mostrar que la guía de estilo no elimina diagnóstico ni aprobación humana. No instalar recursos desconocidos durante el taller.

## 35. Pausa

Pausa prevista de diez minutos tras los fundamentos y las instrucciones. Es un punto de ajuste del ritmo, no un nuevo módulo.

## 36. Positron por dentro

Ahora que sabemos qué exigimos al código y al contexto, presentar Positron como entorno de trabajo. Localizar script, consola y salida en una captura propia. La captura usa un ejemplo sintético, no un agente: no fingir conexión. El archivo sigue siendo el entregable, aunque exploremos en una sesión persistente.

## 37. Una herramienta para practicar

Mostrar las opciones después del método. No exigir cuatro instalaciones ni comparar precios. Una misma familia de modelos puede participar en varias interfaces. Verificar compatibilidad real de skills, instrucciones y MCP en el agente elegido.

## 38. MCP: el puente hacia R

Definir MCP como protocolo de conexión, no como un modelo ni una skill. La integración experimental de Positron 2026.10 permite listar sesiones, ejecutar código e inspeccionar resultados. El proceso de configuración se muestra inmediatamente después. No prometer compatibilidad universal.

## 39. Conectar el agente a Positron

Abrir proyecto e iniciar una sesión R. En Settings buscar ai.mcp.enabled y activarlo. Después usar Positron MCP: Add to Coding Agent para Codex o Gemini CLI; la nota oficial describe configuración automática para Claude Code. Otros clientes requieren Copy Connection Details. No proyectar URL con token, claves API ni archivos de credenciales. Las capturas muestran el ajuste y el comando, no una conexión completada. Consultar la guía de herramientas para pasos y alcance.

## 40. Comprobar la conexión, no solo activarla

Prueba a realizar con el cliente definitivo; no afirmar que ya se ejecutó vía MCP. sum(1:4) vale 10, pero obtener 10 en un chat no prueba acceso a esa sesión: debe observarse la llamada y su procedencia en Positron. Inspeccionar alcance de archivos y directorio de trabajo antes del caso. El kit incluye una lista de comprobación.

## 41. Una ejecución visible desde el agente

Captura propia proporcionada por el autor: se observa un encargo de Codex para calcular 3 + 4 y generar un gráfico; la respuesta declara ejecución mediante MCP, la consola R identifica Codex y aparece la figura de un girasol. Son tres recortes del mismo original, sin el avatar ni controles personales. No presenta un log de transporte MCP completo, por lo que no usarla como certificación independiente. La prueba anterior de sum(1:4) es otro encargo sugerido, no el cálculo mostrado aquí.

## 42. Posit Assistant: otra forma de entrar

Alternativa integrada a un agente externo. Mostrar petición, acceso a herramientas y revisión en la captura oficial. Requiere un proveedor compatible configurado; el acceso y las credenciales se resuelven fuera de la proyección. Evitar duplicar una instalación si ya se eligió la vía externa.

## 43. De una carpeta recibida al análisis

Abrir una copia extraída del ZIP fuera del repositorio docente. El punto de partida contiene seis archivos, sin AGENTS.md, scripts ni resultados. El grupo debe construir esa organización durante la práctica. Los datos completos ya están simulados y comprobados en una referencia docente separada; no precargarla en el agente. Mantener visible la aprobación humana antes de reorganizar o modelar.

## 44. La carpeta que recibimos

Mostrar la carpeta extraída con los dos PDF, las dos bases, el diccionario y las notas. Pedir que el agente identifique objetivos, archivo principal y dudas sin modificar nada. No usar la raíz del repositorio porque contiene instrucciones y soluciones docentes. Verificar además instrucciones heredadas del cliente. El escenario contempla 500 participantes, doce ítems ordinales y dos dimensiones; no confundir filas exportadas con personas.

## 45. Antes del primer modelo

Después del inventario, pedir una propuesta de organización y de instrucciones estables. Separar qué va en AGENTS.md, qué se mantiene en los PDF o en un resumen científico y qué aporta la skill. Revisar antes de autorizar escritura. El agente puede proponer carpetas pero no hay un árbol obligatorio ni se exige plan.md. Solo entonces organizar una copia del trabajo, crear AGENTS.md y proceder con la auditoría y el método aprobado.

## 46. El encargo para la demostración

No entregar un AGENTS.md prefabricado. Hacer explícito el paso de leer los insumos a proponer una forma de trabajo y obtener aprobación. Después de configurar, inspeccionar los datos con R y presentar decisiones metodológicas. La comparación con la solución docente es apoyo del facilitador, no información que reciba el agente al inicio. El método debe poder continuarse manualmente.

## 47. Antes de aceptar un cálculo

Ahora, dentro de la práctica, mostrar las cinco respuestas ficticias. Pedir qué significa 99 y qué documento lo decide. No se usa esta pregunta para abrir el taller, sino para ejercitar la revisión ya aprendida.

## 48. Una ejecución sin errores

Salida real de R para el microejemplo: mean de 1,2,3,4,99 es 21.8. El error didáctico es semántico, no computacional. No atribuirlo a un agente concreto. Buscar el diccionario antes de corregir.

## 49. La corrección documentada

El diccionario del microejemplo define 99 como perdido. La recodificación explícita produce media 2.5 con cuatro observaciones válidas. Mostrar código y denominador, conservar los originales y vincular la corrección con el criterio humano. No confundir este ejemplo con un análisis de fiabilidad.

## 50. La salida real de R

Captura propia de la consola del microejemplo, también reproducida desde una sesión limpia de R. Verificar que aparecen 21.8, 2.5 y 4. La captura no prueba ejecución por un agente ni un ajuste factorial completo.

## 51. La estructura que vamos a contrastar

Hipótesis de dos factores y doce indicadores. Residuos omitidos solo en el esquema. Contrastar con el código explícito mostrado antes: cambiar un ítem afecta una decisión sustantiva. Los coeficientes y diagnósticos del caso completo se incorporarán cuando se hayan ejecutado y verificado.

## 52. Después de la convergencia

Después de ejecutar un AFC no basta el mensaje de convergencia. Revisar admisibilidad, parámetros, ajuste local/global y coherencia sustantiva. No se muestran índices de ajuste fabricados. Identificar qué procedimiento realizará el agente y qué evaluación corresponde al investigador.

## 53. Volver a empezar desde los archivos

Volver a ejecutar el script desde archivos en una sesión limpia. La sesión persistente ayuda a explorar, pero no debe crear dependencia de objetos invisibles. La reproducibilidad conserva también los errores, así que revisar significado y decisiones sigue siendo necesario.

## 54. Del resultado a la conclusión

Auditar la frase que infiere validez global solo del ajuste factorial. Es una afirmación ficticia para discutir, no un resultado del taller. Pedir datos, código, diagnósticos y delimitación de la inferencia. Recuperar los Human Gates antes de redactar conclusiones.

## 55. Lo que conservamos al delegar

Cerrar sin novedades. Contrastar el inicio con el recorrido: ya no solo se recibe código, se dirige un proceso que podemos revisar y continuar. No prometer productividad automática; la mejora depende del uso competente y del contexto.

## 56. Un proyecto para seguir practicando

El recurso principal es el ZIP con seis insumos, sin scripts ni instrucciones de agentes. La carpeta docente guarda parámetros y comprobaciones y no debe distribuirse como punto de partida. El microejemplo y las guías generales siguen disponibles como apoyos, pero no deben resolver por anticipado la configuración del caso. Las skills definitivas siguen requiriendo ensayo con el agente elegido.

## 57. Fuentes de herramientas y formatos

Fuentes oficiales y enlaces completos en docs/fuentes.md. Esta lámina es apoyo, no tiempo de exposición obligatorio. Se añadieron fuentes sobre harness y configuración de MCP; no usar citas de producto como prueba de productividad universal.

## 58. Fuentes y límites del material

Distinguir esquemas y ejemplos ficticios de capturas y resultados ejecutados. La carpeta inicial sí tiene datos completos, PDF y diccionario; las comprobaciones en R se guardan por separado para el docente. La presentación no atribuye esos resultados a un agente ni muestra una activación de skills no comprobada. La documentación de lavaan y semTools respalda el uso de funciones, no la validez de un instrumento real.
