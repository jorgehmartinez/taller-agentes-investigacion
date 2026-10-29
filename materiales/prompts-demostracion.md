# Prompts de demostración comentados

Los textos de ejemplo son punto de partida; no garantizan buenos resultados sin documentación, herramientas y supervisión. Utilizar datos ficticios o aprobados.

## 1. Inspección antes de modificar

> Lee el README, el protocolo resumido y el diccionario de variables del proyecto. Explica qué pregunta busca responder el análisis, qué datos existen y qué información falta. No modifiques archivos ni ejecutes modelos todavía.

**Objetivo:** comprobar comprensión del contexto, sin imponer un plan.md.

## 2. Auditoría de datos

> Con la documentación disponible, inspecciona la base usando R. Resume tipos de variables, categorías, datos perdidos, valores fuera de rango y posibles ítems inversos. No recodifiques valores ambiguos. Registra los hallazgos y las preguntas que requieren mi decisión.

**Objetivo:** diferenciar inspección automática de decisión sustantiva.

## 3. Propuesta metodológica proporcional

> La pregunta es evaluar evidencia de estructura interna y fiabilidad de una escala ordinal de dos dimensiones hipotéticas. Propón un análisis explícito con supuestos, decisiones pendientes, diagnósticos y entregables. Distingue lo establecido en el protocolo de tus alternativas. Espera mi aprobación para ajustar los modelos.

**Objetivo:** aprobación cuando hay decisiones importantes; no confundir «plan» con un archivo obligatorio.

## 4. Ejecución supervisada

> Aplica únicamente las decisiones que ya aprobamos. Escribe scripts R legibles y editables, conserva los datos originales, ejecuta desde el proyecto, guarda resultados y revisa diagnósticos. Informa qué procedimientos corriste y cuáles no, sin inventar estadísticas ni reinterpretar resultados faltantes.

**Objetivo:** producir evidencias reproducibles, no solo una respuesta narrativa.

## 5. Auditoría crítica

> Comprueba los resultados desde una sesión limpia de R. Contrasta las salidas con las afirmaciones del informe, identifica problemas de estimación o especificación y distingue evidencia sobre estructura interna de una conclusión global de validez. Explica incertidumbres y decisiones metodológicas que requieren revisión.

**Objetivo:** auditar incluso un script que se ejecuta correctamente.

## 6. Revisión de skills externas

> Inspecciona la procedencia, contenido, referencias, scripts y permisos de esta skill antes de utilizarla. Resume qué instrucciones son generales, cuáles son decisiones metodológicas discutibles y qué riesgos de seguridad o mantenimiento observas. No ejecutes recursos no revisados.

**Objetivo:** uso crítico y seguro de conocimientos reutilizables.

## 7. Cómo invocar las skills del EPIC

Cuando las skills del monorepo estén **versionadas y probadas**, reemplazar el nombre genérico por el identificador exacto disponible en el agente elegido. En una demostración agnóstica, explicar que algunos agentes aceptan invocación explícita y otros descubren skills a partir del contexto. No prometer activación automática.

**Evitar:** «usa siempre WLSMV», «elige el modelo de mejor ajuste sin consultarme», «corrige automáticamente los ítems inversos», «borra todo lo innecesario», «haz un plan.md para cualquier tarea».
