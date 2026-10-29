# Integración con el EPIC paralelo de r-workflow-plugins

## Decisión de arquitectura

Este proyecto es consumidor de las skills de **`/home/brian/Documents/Github/r-workflow-plugins`**, no un fork ni una copia estática del monorepo. Su desarrollo continúa en paralelo, especialmente en análisis de datos y psicometría.

El taller puede explicar el formato de una skill y sus características antes de que termine el EPIC. **No** debe presentar como estable una skill que esté únicamente propuesta, en construcción o no haya sido probada.

## Responsabilidades separadas

| Repositorio | Autoridad |
| --- | --- |
| r-workflow-plugins | Diseño, versiones, pruebas, referencias y publicación de skills de R |
| taller-agentes-investigacion | Estrategia docente, diapositivas, ejercicios, caso sintético y validación del taller |
| quarto-bento | Motor de visualización, diseño y sincronización QMD / estado nativo |

## Contrato mínimo para incorporar una skill

1. Nombre exacto y ubicación confirmados en el monorepo.
2. Alcance declarado: estilo R, datos, psicometría u otra especialidad.
3. Versión o commit fijado para las demostraciones públicas.
4. Compatibilidad comprobada con el agente seleccionado; selección automática no presupuesta.
5. Recursos y dependencias inspeccionados; sin scripts externos inesperados.
6. Un caso positivo y un caso de fallo/ambigüedad ensayados.
7. Efectos sobre código y resultados registrados; ningún cambio estadístico oculto.
8. Demostración que pueda reproducirse sin dependencia de un estado conversacional.

## Interfaz docente prevista

La skill de estilo analítico en R debe encauzar legibilidad, organización research-first, tidyverse cuando corresponda y diagnósticos proporcionados. La skill psicométrica debe orientar auditoría de ítems y justificación metodológica. No sustituir la especificación científica del proyecto por una instrucción de aplicación ciega.

No copiar ni adaptar el `SKILL.md` completo a los slides: enseñar **qué hace y cómo se inspecciona**, con una muestra mínima cuya procedencia se declara. El kit final puede incluir instrucciones de instalación o selección según agente y la versión fijada, pero no asumir APIs idénticas.

## Puntos de integración pendientes

- Actualizar la diapositiva `dos-skills` con nombres **reales** de las skills verificadas.
- Revisar `skill-anatomia` con un fragmento fiel a la skill usada.
- Completar `caso/especificacion.md` con código, datos y salidas reales.
- Ensayar prompts de `materiales/prompts-demostracion.md` con el agente y la versión elegidos.
- Registrar la compatibilidad de Positron/MCP del entorno usado.
- Añadir licencia y atribuciones correctas a materiales distribuidos.

**No modificar el monorepo desde este repo sin una instrucción independiente y explícita.**

## Correspondencia de la presentación visual v2

La fuente actual es `presentacion/deck.qmd`. Las slides 28–35 muestran selección, estructura, legibilidad, seguridad y fuente de skills. `skill-real` utiliza una captura propia del archivo de r-analytic-core; no prueba activación de un agente. `skills-proyecto` identifica el EPIC pendiente. La incorporación psicométrica definitiva debe actualizar 37–50 y no introducir cifras sin ejecución.
