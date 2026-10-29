# Caso psicométrico sintético: especificación provisional

**Estado: diseño del caso, no análisis ejecutado.** Ningún valor numérico inferencial debe aparecer en los materiales hasta generar y ejecutar los scripts de referencia.

## Objetivo didáctico

Comparar el valor de un agente con herramientas R, documentación y controles humanos frente a una solicitud descontextualizada de análisis psicométrico.

## Datos que se generarán

- Muestra sintética prevista: 500 casos.
- Instrumento ficticio: 12 ítems de autorregulación académica, dos dimensiones teóricas de seis ítems cada una.
- Respuestas ordinales: cuatro categorías.
- Diccionario: nombre del ítem, contenido sintético breve, dimensión teórica, dirección de puntuación, códigos perdidos y procedencia.
- Problemas preparados: valores 99 como missing, al menos un ítem inverso identificado en documentación y algún patrón de distribución a inspeccionar.
- Los parámetros de simulación deberán permanecer en un script docente separado de los scripts entregados para análisis, evitando filtrar artificialmente la solución.

## Pregunta de investigación

¿Qué evidencia proporciona la muestra sintética sobre la estructura interna propuesta y la fiabilidad de las puntuaciones de ambas dimensiones?

## Decisiones metodológicas por fijar en el script canónico

1. Tratamiento de códigos faltantes y evaluación descriptiva de patrones.
2. Dirección de los ítems según contenido y clave, nunca por inversión automática de signos.
3. Modelo de dos factores correlacionados especificado explícitamente.
4. Pertinencia de tratar los ítems como ordinales y elección justificada de estimador (WLSMV es un candidato, no una regla universal).
5. Inspección de estimación, parámetros, residuos y ajuste global/local; evitar heurísticas sin contexto.
6. Estimación de fiabilidad compatible con el modelo y las puntuaciones, con límites interpretativos.
7. Reproducción en sesión limpia de R y comparación con salidas guardadas.

## Artefactos futuros y responsables

- `caso/data/escala_sintetica.csv` y `caso/data/diccionario_items.csv`: pendientes.
- `caso/scripts/01_generar_datos.R`: generación sintética solo docente, pendiente.
- `caso/scripts/02_auditoria.R`: entrada para participantes, pendiente.
- `caso/scripts/03_estructura_interna.R`: análisis canónico, pendiente.
- `caso/scripts/04_fiabilidad.R`: análisis canónico, pendiente.
- `caso/resultados_referencia/`: salidas comprobadas, pendiente.
- `caso/errores_preparados/`: contraste pedagógico deliberadamente defectuoso, pendiente.

Evitar incorporar rutas inventadas a diapositivas como si los archivos existieran. Cuando se produzcan, enlazar explícitamente el script canónico y las diapositivas afectadas.

## Condiciones de publicación del caso

- Datos completamente sintéticos y documentados.
- Código R research-first y legible, siguiendo la skill del monorepo cuando su alcance esté fijado.
- Una ejecución canónica desde sesión limpia con resultados archivados.
- Una segunda comprobación independiente de los números que se mostrarán.
- Cualquier error intencional claramente marcado como ejemplo defectuoso.
- Material del estudiante separado de parámetros y soluciones docentes, sin perder trazabilidad.
