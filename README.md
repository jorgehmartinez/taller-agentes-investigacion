# Taller: Uso de Agentes IA para análisis de datos e investigación

## Abrir la versión actual

La presentación rediseñada está en **`presentacion/deck.qmd`** y su salida es **`presentacion/deck.bento.html`**. El `deck.qmd` de la raíz se conserva como **borrador anterior de 40 diapositivas**, no como versión vigente.

```sh
cd /home/brian/Documents/Github/taller-agentes-investigacion
qbento edit presentacion/deck.qmd
```

Para regenerar el HTML: `qbento render presentacion/deck.qmd`.

## Segunda versión: explicación visual y práctica

59 diapositivas: 56 del recorrido principal, incluida la pausa, y 3 de apoyo/referencias. La duración continúa siendo 180 minutos. El número aumenta por secuencias progresivas y ampliaciones de capturas, no por incorporar nuevas unidades de contenido.

La presentación utiliza 31 esquemas SVG originales y 8 recortes/capturas diferentes efectivamente insertados en el deck. Hay 9 derivados preparados en el directorio de capturas. Se distingue entre esquemas didácticos, datos ficticios, capturas oficiales de Posit y capturas propias de Positron.

El microejemplo de cinco respuestas está **ejecutado y reproducido en R**: tratar 99 como respuesta produce 21.8; recodificarlo como perdido según el diccionario produce 2.5, con cuatro respuestas válidas. Las capturas propias muestran ese script, su consola y una skill real abierta en Positron. No se presentan como ejecuciones realizadas por un agente.

## Materiales

- `docs/programa.md`: secuencia de 180 minutos y tramos de diapositivas.
- `docs/guion-docente-v2.md`: instrucciones de presentación, preguntas y transiciones.
- `docs/rediseno-pedagogico.md`: decisiones de comunicación y papel de cada contraste.
- `docs/fuentes.md`: fuentes oficiales y límites de lo que respaldan.
- `materiales/microcaso/`: script R, diccionario y salida de referencia.
- `materiales/descripciones-visuales.md`: guía textual de las diapositivas, código y notas.
- `materiales/plantilla-proyecto/`: ejemplo de protocolo, diccionario y AGENTS.md.
- `materiales/actividades.md` y `prompts-demostracion.md`: práctica complementaria.
- `docs/integracion-skills.md`: integración pendiente con el EPIC paralelo.

## Fuente y diseño

`presentacion/deck.qmd` es la autoridad semántica; `presentacion/.qbento/` conserva diseño y estado nativo. El paquete reutilizable es `design/spp-workshop-v2.design.json`. No editar manualmente el HTML generado ni el estado interno.

Los scripts `build_visuals.py` y `build_design.py` generan recursos y el paquete, pero no aplican cambios de estado. `author_deck_v2.py --write` fue el autor inicial: **no volver a ejecutarlo sobre cambios manuales de QMD sin revisar**, porque regenera el contenido. `capture_deck.mjs` comprueba la presentación real en Chromium sin reescribir su contenido.

Se conservó el primer proyecto ligado a su identidad Bento y se creó una identidad independiente para el rediseño. No se sobrescribió su estado interno. El respaldo previo está en `backups/` y la evidencia técnica en `output/qa/`.

## Límites actuales

El caso factorial completo de 500 casos y 12 ítems sigue siendo una especificación, no un análisis ejecutado. La integración final de skills de datos y psicometría espera versiones comprobadas del EPIC. No se modificó `r-workflow-plugins` ni se configuraron credenciales o un proveedor IA en el perfil usado para capturas.

La revisión visual y las comprobaciones de render no sustituyen un ensayo cronometrado en videoconferencia ni una validación psicométrica. La accesibilidad del adaptador Bento tiene límites; se proporcionan descripciones textuales, sin afirmar una auditoría completa de lectores de pantalla.
