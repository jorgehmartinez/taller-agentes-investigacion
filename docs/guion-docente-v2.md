# Guion docente del rediseño visual

Las notas de cada diapositiva contienen la explicación local. Este documento organiza las transiciones y el uso de pantalla compartida.

## 1. Abrir con una decisión, no con un glosario

En las slides 2 y 3, mantener el vector 1, 2, 3, 4, 99. Primero pedir qué habría que saber; después mostrar 21.8, obtenido realmente en R. Todavía no desarrollar toda la recodificación: el mismo ejemplo volverá cuando tenga sentido consultar el diccionario. Aclarar que es un error preparado de interpretación de códigos, no un resultado atribuido a la incompetencia de un agente.

## 2. Introducir el mecanismo

En la slide 6, las opciones de continuación son esquemáticas, no frecuencias estimadas. Decir explícitamente que el modelo es probabilístico y que la decodificación puede reducir la variabilidad. Pasar al reparto modelo/R/investigador y al contraste controlado chatbot/agente: la tarea y el motor R se mantienen; cambia quién opera el intercambio con las herramientas.

La semilla de R no es una receta universal de reproducibilidad. En la slide 10, repetir el pequeño muestreo opcionalmente en R, manteniendo el entorno y la semilla. Después separar cómputo, método e inferencia.

## 3. Orientar, ampliar, interpretar

La captura general de Positron sirve para localizar editor, consola y salidas. No pedir que se lea todo a tamaño reducido. La captura oficial de MCP muestra dónde se ve una llamada, el nombre del agente en la consola y el gráfico. La slide siguiente amplía exclusivamente las regiones decisivas.

Identificar las capturas oficiales como ejemplos publicados por Posit con otros datos. Las capturas propias muestran únicamente R y el archivo de una skill. No se han simulado conversaciones ni ejecutado un proveedor IA para obtenerlas.

## 4. Onboarding y organización de la información

Preguntar qué necesitaría un investigador nuevo en el equipo. Luego ordenar el contexto en ciencia, datos y reglas del equipo. Presentar el mapa documental antes de mostrar el fragmento de AGENTS.md.

Dar dos minutos a la clasificación de «99 = perdido» y «no sobrescribir originales». En la resolución, añadir hipótesis y procedimiento de auditoría. Estas ubicaciones constituyen una organización útil del taller, no un mandato universal de nombres de archivos.

No pedir un plan.md por defecto. Distinguir inspección acotada de decisiones encadenadas, costosas o difíciles de revertir.

## 5. Skills reales, no un catálogo de promesas

Mostrar la captura del archivo `r-analytic-coding-principles/SKILL.md` y leer solo nombre, propósito y prioridad. Contrastar código compacto con código que explicita la transformación; ambos calculan lo mismo. Esto es una comparación docente de legibilidad, no un experimento que pruebe que activar una skill mejora a cualquier agente.

Separar procedimiento de herramienta. Después revisar procedencia, contenido, permisos y prueba. El EPIC de datos/psicometría continúa fuera del taller y deberá incorporarse con identificadores y versiones reales.

## 6. Práctica psicométrica

La matriz es ficticia. El diagrama de dos factores es una hipótesis y omite residuos para facilitar su lectura. No se han estimado sus coeficientes. Al hablar de AFC ordinal, contextualizar WLSMV como candidato justificado, no como regla automática.

El microejemplo ya permite demostrar la auditoría de 99, su recodificación y el denominador. Se puede abrir `materiales/microcaso/01_microcaso.R` en R sin depender de IA. Comprobar que 21.8, 2.5 y 4 coinciden con la salida de referencia.

Para el caso factorial definitivo, mantener las fases previstas de inspección, propuesta, revisión, ejecución y diagnóstico. Sustituir las estaciones explicativas por la evidencia del modelo cuando exista. No alargar la demostración improvisando dependencias o configurando cuentas.

## 7. Cerrar con transferencia

Preguntar qué parte de la afirmación de validez está respaldada. Vincular cada control final a algo observado en el taller. El ticket de salida pide un documento, una restricción y una comprobación concreta: eso muestra aprendizaje mejor que recordar marcas de modelos.

## Si falla la conexión

Usar las capturas y la salida canónica, identificándolas como respaldo. No fingir una ejecución en directo. El microejemplo se puede ejecutar sin conexión de IA; el caso completo necesita su script y dependencias antes del evento.
