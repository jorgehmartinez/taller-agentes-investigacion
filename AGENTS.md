# Instrucciones de trabajo del proyecto

## Propósito y alcance

Este repositorio contiene **material docente en desarrollo** para un taller introductorio virtual de tres horas. Conserva el título publicitado y utiliza la psicometría como ejemplo, sin afirmar que los agentes reemplazan el criterio científico.

## Fuentes de autoridad

- `presentacion/deck.qmd`: autoridad textual y notas del ponente de la versión actual. El deck.qmd de la raíz es el borrador anterior, preservado.
- `presentacion/.qbento/`: autoridad visual retenida del rediseño; consultar `quarto-bento-workflow` antes de modificar estado.
- `docs/programa.md`: secuencia y tiempos acordados.
- `caso/especificacion.md`: contrato provisional del caso, no resultados estimados.
- El repositorio vecino `../r-workflow-plugins` es **externo y está en desarrollo paralelo**. Leerlo cuando corresponda; no escribir en él desde este proyecto ni congelar una interfaz no publicada.

## Reglas estables

- Escribir en español claro, sin exceso de tecnicismos; definir términos al introducirlos.
- Mantener **introducción general + aplicación psicométrica**, no un curso exclusivo de CFA.
- Diferenciar modelo generativo, agente de codificación, editor y motor de análisis.
- Explicar que el LLM es un componente probabilístico; R ofrece ejecución controlable, no determinismo universal.
- Mantener explícitos los puntos de intervención humana y los límites de inferencia.
- No afirmar que un análisis es válido porque el código corre ni que una skill garantiza corrección.
- Los materiales proyectados deben ser sintéticos, anonimizados o expresamente públicos; no incluir claves, tokens ni datos sensibles.
- Presentar `AGENTS.md` como reglas/ubicaciones persistentes; no exigir `plan.md` para toda tarea.
- La intención de usar skills del EPIC no autoriza copiar ejemplos provisionalmente ni declarar publicados módulos todavía incompletos.
- No atribuir a una implementación propiedades experimentales como garantía de estabilidad.
- Evitar inventar índices de ajuste, coeficientes, tamaños muestrales observados o pantallazos de ejecución.
- En código R, seguir el estilo research-first de `r-analytic-core`: código editable, sin megachunks ni automatización prematura; los análisis de aula han de ser reproducibles sin depender de un agente.

## Cambios y comprobación

- Antes de modificar QMD o diseño, revisar los IDs y el estado de Bento.
- No modificar manualmente `.qbento/state.json`, no sincronizar QMD sin revisar plan de cambios y no publicar contenidos pendientes excluidos.
- Después de cambios importantes, volver a renderizar, inspeccionar estructura y revisar visualmente las diapositivas afectadas.
- Un render correcto no equivale a auditoría visual, ni a análisis psicométrico validado.
- Mantener las notas docentes y las actividades alineadas con el código canónico cuando este exista.

## Documentos de referencia

Usar la skill local `plugins/quarto-bento/skills/quarto-bento-workflow/SKILL.md` del repositorio de plugins, y Quarto Publishing para redacción pedagógica, formato y comprobación de slides. Si cambia la versión del CLI, comprobar compatibilidad antes de utilizar componentes exclusivos de 0.2.0.

## Segunda versión visual

La presentación actual está en `presentacion/`. Los recursos visuales tienen fuente y descripción; no convertir capturas oficiales en evidencia de ejecuciones propias. El microejemplo ya está ejecutado, pero el caso factorial continúa pendiente. Conservar originales de capturas y resultados de referencia. No reejecutar `scripts/author_deck_v2.py --write` sobre cambios manuales sin comparar antes.
