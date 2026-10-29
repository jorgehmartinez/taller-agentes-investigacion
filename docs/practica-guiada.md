# Práctica guiada: de archivos recibidos a análisis supervisado

## Punto de partida real

Usar `practica/caso_autorregulacion_inicio.zip` en una carpeta vacía, fuera del repositorio. Abrir solo la carpeta extraída. Así no se precarga el AGENTS.md docente ni se hacen visibles las soluciones. Verificar también las instrucciones globales del agente; la ausencia de un archivo local no garantiza ausencia total de instrucciones.

El ZIP no contiene configuración de agentes, scripts ni resultados. El PDF del encargo contiene objetivos científicos, no la solución operativa de la actividad. La clave del instrumento y los códigos de ausencia sí están documentados: el ejercicio consiste en encontrarlos, entenderlos y aplicarlos correctamente.

## Recorrido sugerido: 55 minutos

| Tiempo | Acción | Resultado observable / revisión humana |
|---|---|---|
| 0–8 min | Inventariar y leer PDF, diccionario y notas | Distinguir principal/piloto; resumir objetivo, diseño y preguntas pendientes |
| 8–18 min | Acordar organización y forma de trabajo | Proponer estructura, redacción de AGENTS.md, rutas de contexto y skill a usar; aprobar antes de escribir |
| 18–28 min | Organizar y auditar con R | Mantener originales; inspeccionar IDs, categorías, ausencias y clave; revisar recodificaciones |
| 28–43 min | Especificar y ejecutar el análisis | Aprobar método; construir llamadas de AFC visibles; revisar convergencia y parámetros |
| 43–50 min | Examinar fiabilidad y límites | Identificar a qué puntuación corresponde el coeficiente; no inferir validez global |
| 50–55 min | Reiniciar y reproducir | Ejecutar desde archivos, comparar salidas y dejar un handoff comprensible |

El tiempo incluye decisiones del público. Si falta tiempo, conservar la organización del proyecto y un modelo verificable; la comparación y la fiabilidad pueden revisarse con la salida docente identificada como respaldo. No fingir que un análisis de respaldo se ejecutó en directo.

## Encargo inicial al agente

«Acabamos de recibir esta carpeta. Sin modificar archivos ni ajustar modelos, identifica qué contiene. Lee el PDF del encargo, el cuestionario, el diccionario y las notas del equipo. Resume objetivos, diseño, datos disponibles, qué archivo corresponde al estudio principal y qué decisiones necesitan revisión. Separa lo documentado de lo que estás suponiendo».

## Construir el contexto, no copiar una receta

«Propón una organización mínima que conserve los originales y permita reproducir el trabajo. Sugiere qué reglas estables y rutas deberían ir en AGENTS.md, qué debe permanecer en la documentación científica y qué procedimientos conviene obtener de la skill disponible. No crees archivos todavía; revisemos primero la propuesta».

Tras revisar, autorizar una lista concreta de operaciones: crear directorios, copiar originales a una ubicación protegida por convención, redactar AGENTS.md y un resumen del proyecto. No hay un árbol único correcto ni es obligatorio generar plan.md. Las instrucciones del archivo no reemplazan permisos efectivos de la herramienta.

## Puntos que deben quedar bajo revisión humana

Archivo principal y unidad de análisis; registros repetidos; dirección de los ítems; tratamiento de ausencias; especificación y estimador; cambios sustantivos para mejorar ajuste; interpretación y publicación. La herramienta puede ejecutar las operaciones rutinarias autorizadas sin pedir aprobación por cada comando.

## Material docente separado

La referencia de R y los parámetros de simulación están en `docente/caso_autorregulacion/`. Sirven para comprobar que el caso es utilizable, no para precargar el agente de los participantes. La referencia utiliza dos modelos explícitos y una estrategia de ausencias documentada; otras decisiones justificadas pueden producir salidas distintas. No presentar la coincidencia numérica con la referencia como único criterio de corrección.

## Capturas que faltan

Una ejecución auténtica por MCP en la sesión de R y evidencia de que el agente definitivo leyó la skill. Seguir `docs/capturas-pendientes.md`. Las capturas de la configuración no demuestran por sí solas conexión ni activación de skills.
