> **Documento de la primera versión.** El guion vigente está en `guion-docente-v2.md`.

# Guion de conducción y puntos de control

Este documento complementa, sin duplicarlas, las notas de orador incorporadas a cada slide de `deck.qmd`.

## Inicio: la pregunta del taller

Abrir con una formulación clara: «Vamos a aprender a incorporar agentes al trabajo de análisis de datos como se incorpora un analista a un equipo. Puede ejecutar tareas, pero necesita conocer el proyecto y ser supervisado». Precisar que la psicometría será el caso central porque el evento es psicométrico; los principios son transferibles.

## Demostración breve A: generación versus ejecución

Proponer un cálculo simple con datos preparados. Contrastar una propuesta textual del LLM con la salida real de R. Mostrar `set.seed()` en un ejemplo de muestreo, aclarando que la semilla no asegura por sí sola reproducibilidad completa. Conectar con tres niveles: computacional, metodológico y científico.

**Punto didáctico:** no confundir salida plausible con resultado ejecutado ni reproducibilidad computacional con adecuación científica.

## Demostración breve B: Positron/MCP

Preparar de antemano Positron, R activo y el agente externo compatible con MCP. Ejecutar una consulta pequeña y mostrar el resultado en la consola o el entorno. Explicar qué componente pone a disposición las herramientas y cuáles son las limitaciones experimentales del servidor MCP. Si la conexión falla, mostrar un registro previo comprobado, no recrear la configuración en directo.

Posit Assistant se enseña como alternativa integrada; no iniciar una instalación de API keys con los participantes.

## Demostración breve C: contextualización

Presentar dos escenarios con el **mismo proyecto**:

A. Solicitud vaga sin objetivos ni diccionario.
B. Solicitud con documentación enlazada, instrucciones de AGENTS.md y restricciones.

No comparar respuestas como si se tratara de un ensayo aleatorizado ni garantizar superioridad. Analizar qué información faltaba y qué decisiones siguen abiertas.

## AGENTS.md frente a otros documentos

Explicar por analogía con onboarding de un analista:
- El protocolo contiene el método y las hipótesis.
- El diccionario explica los datos.
- AGENTS.md explica cómo trabajar y dónde encontrar documentación.
- Una skill contiene un procedimiento reutilizable.
- La solicitud concreta define la tarea del momento.
- Un plan escrito es proporcional a la complejidad y el riesgo.

Recalcar que un plan no es obligatorio para cada análisis y que los datos de acceso o claves no pertenecen a AGENTS.md.

## Demostración breve D: skills

Mostrar el formato y una lectura rápida de una skill **validada y disponible** desde el repositorio de r-workflow-plugins. Conectar la skill de estilo R con la psicométrica: la primera mejora legibilidad y edición; la segunda especifica comprobaciones metodológicas. La procedencia y las condiciones de uso deben ser evaluadas antes de ejecutar código de terceros.

**No emplear públicamente ejemplos de branches del EPIC aún no verificados.**

## Caso integrado (60 minutos)

| Fase | Minutos | Acción en directo | Intervención humana |
| --- | ---: | --- | --- |
| Reconocer proyecto | 10 | Lectura de archivos y objetivos | Confirmar finalidad del estudio |
| Auditar datos | 10 | Examinar categorías, missing, ítems invertidos | Resolver ambigüedades del diccionario |
| Aprobar modelo | 10 | Proponer AFC ordinal y justificación | Evaluar hipótesis y estimador |
| Ejecutar R | 15 | Preparar, ajustar, extraer diagnósticos | Revisar mensajes, resultados y código |
| Error preparado | 8 | Comparar versión incorrecta y corregida | Identificar por qué importa el 99 |
| Reproducción y cierre | 7 | Ejecutar script canónico desde R limpio | Delimitar conclusiones y pendientes |

El calendario anterior sustituye la repartición por diapositiva. Mantener un camino canónico verificado y un respaldo estático de cada paso; no depender de un fallo espontáneo del agente para producir aprendizaje.

## Preguntas que deben quedar abiertas a discusión

- ¿Un análisis factorial que converge puede estar mal especificado?
- ¿Un valor alto de fiabilidad prueba validez?
- ¿Qué significa que los ítems sean ordinales y por qué importa para la estimación?
- ¿Qué verificación exige el tratamiento de valores perdidos y recodificaciones?
- ¿Qué responsabilidad corresponde al investigador aunque delegue ejecución?

## Cierre

Volver a los cuatro contrastes: generar/calcular, contextualizar/acumular, especializar/garantizar, ejecutar/responsabilizarse. Dejar claro que los recursos y scripts se proporcionarán en su versión reproducida, no como capturas aisladas. Invitar a aplicar el mismo método en otra familia de modelos.
