# Evidencia del facilitador: no incluir en el ZIP inicial

## Propósito

Estos archivos comprueban que la carpeta recibida puede analizarse y conservan una referencia para un ensayo o fallo de conexión. No son el punto de partida de participantes ni una demostración de comportamiento de un agente.

## Preparación y ejecución

Desde la raíz del taller:

```sh
Rscript --vanilla docente/caso_autorregulacion/01_generar_datos.R
Rscript --vanilla docente/caso_autorregulacion/02_comprobar_caso.R
python3 scripts/empaquetar_practica.py
```

La generación recrea los CSV de la copia distribuible; no ejecutarla sobre una carpeta de práctica en curso. Los PDF finales están en `practica/carpeta_recibida/`. Su fuente, `generar_documentos.py`, requiere ReportLab y pypdf, no instalados automáticamente. Esa fuente genera los PDF junto al script; revisar antes de reemplazar los finales.

## Incidencias conocidas

La exportación principal tiene 501 filas y 500 identificadores únicos. La fila de E0173 está duplicada de forma exacta. El piloto es independiente (60 casos) y no se concatena. Hay 90 códigos 99 y 30 celdas vacías entre los 6000 valores de ítems de los 500 casos únicos. i03 e i09 se entregan en dirección inversa. Todas estas situaciones son sintéticas; su significado debe extraerse del cuestionario, diccionario y notas.

## Decisiones de la referencia

Eliminar exclusivamente la fila exactamente repetida, después de comprobarla; convertir 99 y vacíos en ausencias; invertir solo las respuestas válidas de i03 e i09; ajustar un modelo de dos factores correlacionados y uno unidimensional mediante llamadas explícitas en R. La referencia usa WLSMV y pares disponibles, no FIML. Guarda N por ítem/par, diagnósticos y fiabilidad de los compuestos de seis ítems en la escala ordinal observada, sin asumir una puntuación total.

La elección de pares disponibles es una decisión del ensayo, no una recomendación universal ni una prueba de que las ausencias sean ignorables. MCAR es parte de la generación; el analista no puede deducirlo como certeza de los archivos recibidos. Se dispone de 389 casos completos en esta realización. Un análisis de casos completos, si se justifica, cambia el conjunto analítico y los valores de referencia.

No hacer una selección automática por índices de ajuste, ni un test de diferencia ingenuo entre uno y dos factores. El contraste también requiere interpretación sustantiva y consideración de las restricciones del modelo. Los coeficientes de fiabilidad no son evidencia suficiente de validez.

## Fuentes de las funciones

- lavaan: https://lavaan.ugent.be/tutorial/cat.html
- semTools, compRelSEM: https://simsem.r-universe.dev/semTools/doc/manual.html

La instalación comprobada es R 4.6.1, lavaan 0.7.3 y semTools 0.5.10. Las versiones exactas restantes están en los archivos de sessionInfo. Las estimaciones concretas se guardan en CSV; no son datos de una investigación real.
