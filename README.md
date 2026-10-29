# Uso de Agentes IA para análisis de datos e investigación

Taller introductorio virtual de tres horas para el Congreso de la Sociedad Peruana de Psicometría. Método transferible a investigación cuantitativa, con R y aplicaciones psicométricas.

## Abrir la presentación

La fuente vigente sigue siendo **`presentacion/deck.qmd`** y su salida es **`presentacion/deck.bento.html`**. Esta revisión modifica el mismo proyecto Bento: no introduce otra carpeta de versión. Se eliminaron los antiguos archivos de presentación y estado Bento de la raíz para evitar duplicidades.

```sh
cd taller-agentes-investigacion
qbento edit presentacion/deck.qmd
# Para regenerar la salida:
qbento render presentacion/deck.qmd
```

## Secuencia actual

**Encuadre → fundamentos → análisis con chat → agentes → código revisable → contexto e instrucciones → Positron → práctica.**

La presentación contiene 58 diapositivas: 56 de recorrido, incluida la pausa, y dos de referencias. El número incluye estados sucesivos del mismo ejemplo, no 56 exposiciones independientes. Se mantienen 180 minutos y queda pendiente el ensayo cronometrado.

El taller abre con objetivos y límites, no con código. Las escenas ficticias de ChatGPT y RStudio hacen visible el intercambio manual. Después se introducen la ejecución con herramientas y los Human Gates. Los antiejemplos safe_cfa, limpieza oculta y errores silenciados plantean la necesidad de código que podamos revisar y continuar. AGENTS.md y skills se presentan conjuntamente. Positron y su configuración aparecen cuando ya se conoce la forma de trabajo que queremos implementar.

## Materiales principales

- `docs/programa.md`: organización de los 180 minutos.
- `docs/guion-docente.md`: indicaciones por diapositiva.
- `materiales/descripciones-visuales.md`: acompañamiento textual y código mostrado.
- `materiales/ejemplos-codigo.md`: antiejemplos, límites y alternativas de organización.
- `materiales/herramientas.md`: configuración de MCP y prueba de conexión.
- `docs/capturas-pendientes.md`: documentación de la captura propia de Codex/Positron y límites de su evidencia.
- `practica/caso_autorregulacion_inicio.zip`: los seis insumos iniciales, sin configuración de agentes ni soluciones.
- `practica/carpeta_recibida/`: copia distribuible de esos insumos.
- `docs/practica-guiada.md`: construcción de AGENTS.md y organización durante la sesión.
- `docente/caso_autorregulacion/`: generación y comprobación del caso, fuera del ZIP.
- `materiales/microcaso/`: ejemplo breve adicional con salida de referencia.
- `materiales/plantilla-proyecto/`: contexto y reglas de trabajo.
- `docs/integracion-skills.md`: integración del EPIC desde el repositorio externo.
- `docs/fuentes.md`: fuentes oficiales y procedencia de recursos.

## Fuente y diseño

QMD es la autoridad textual y `presentacion/.qbento/` conserva diseño y estado. No editar manualmente state.json ni el HTML generado. Los SVG son autocontenidos; las capturas originales se mantienen separadas de sus recortes y anotaciones.

`scripts/build_workflow_visuals.py` genera los esquemas del recorrido. `scripts/capture_deck.mjs` abre y recorre la presentación real en Chromium. Los scripts de autoría inicial con sufijo v2 son históricos: no ejecutarlos sobre el QMD actual, porque restablecerían contenido anterior. Las revisiones se guardan en Git.

## Evidencia y pendientes

El microejemplo del código 99 sí está ejecutado y reproducido en R: 21.8 antes de la corrección documentada; 2.5 y cuatro respuestas válidas después. Los ejemplos de AFC y arquitectura de código son ilustrativos, no modelos ya ajustados. Las escenas de chat no son screenshots de conversaciones reales.

Las capturas de configuración del MCP muestran el ajuste y el comando en un perfil aislado, sin conexión en ese momento. Una captura posterior proporcionada por el autor muestra una interacción real de Codex con R en Positron y una figura generada; no es una auditoría completa del transporte MCP ni prueba que el agente haya leído una skill. El caso factorial completo ya está generado y su referencia de R se ejecutó desde una extracción limpia, con salidas coincidentes. Falta ensayar el flujo con el agente definitivo y las skills de datos/psicometría. Las salidas docentes no se entregan en la carpeta inicial. El monorepo r-workflow-plugins se leyó, no se modificó.

## Arranque de la práctica

Extraer el ZIP en una carpeta vacía fuera de este repositorio y abrir solo `caso_autorregulacion/` en Positron. La copia versionada no es una carpeta de trabajo en vivo. Así se evita heredar este AGENTS.md docente; comprobar también instrucciones globales del cliente. No copiar las plantillas ni las soluciones antes de la actividad.
