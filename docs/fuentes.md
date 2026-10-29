# Fuentes, capturas y alcance de la evidencia

Consulta documental: **29 de octubre de 2026**. Las referencias de producto pueden cambiar antes del evento.

## Herramientas y convenciones

- Posit / Julia Silge. **Positron October Release Highlights**, 13-10-2026. Servidor MCP experimental, conexión de agentes externos, ejecución visible en consola y nuevas capacidades de Posit Assistant. https://opensource.posit.co/blog/2026-10-13_positron-2026-10-release/
- Posit. **Posit Assistant: Getting Started**. Disponibilidad en Positron, RStudio y terminal; distinción respecto a Positron Assistant. https://assistant.posit.co/docs/getting-started/
- Posit. **Available providers**. Consultar condiciones de acceso, sin asumir equivalencia entre suscripciones y API. https://assistant.posit.co/docs/getting-started/providers/
- Posit. **Posit AI: Getting Started**. Fuente de la captura de configuración de proveedor del apéndice. https://docs.posit.co/posit-ai/user/getting-started/
- Agent Skills. **Specification**. SKILL.md, metadatos, instrucciones y recursos opcionales; carga progresiva. https://agentskills.io/specification
- **AGENTS.md**. Convención de instrucciones para agentes. https://agents.md/
- OpenAI. **Codex CLI**, documentación oficial. https://developers.openai.com/codex/cli/
- Anthropic. **Claude Code overview**, documentación oficial. https://code.claude.com/docs/en/overview
- Google. **Gemini CLI documentation**. https://geminicli.com/docs/

## R y ejemplo estadístico

- R Core. **Random Number Generation**: set.seed, RNGkind y RNGversion. https://stat.ethz.ch/R-manual/R-devel/library/base/html/Random.html
- lavaan project. **Categorical data**. El argumento ordered y el uso de WLSMV en modelos con respuestas ordinales. La documentación describe la implementación; no establece que ese estimador sea adecuado en todo estudio. https://lavaan.ugent.be/tutorial/cat.html
- Microejemplo del taller: `materiales/microcaso/01_microcaso.R`, diccionario y salida de referencia. Es una ilustración de lectura de códigos, no evidencia de validez ni un resultado del caso factorial completo.

## Repositorios locales del autor

- `r-workflow-plugins/plugins/r-analytic-core/skills/r-analytic-coding-principles/SKILL.md`: fuente de la captura de skill real. El monorepo se leyó, no se modificó.
- Skills de Quarto Publishing: pedagogical-communication y slide-deck-design para explicación, títulos, secuencia y comprobación visual.
- `quarto-bento` y su skill local: componentes, diseño nativo, preservación de estado y revisión de salida. La presentación se generó con qbento 0.2.0.

## Registro de capturas

`presentacion/assets/screenshots/provenance.json` documenta fuente, origen y hash de originales. `presentacion/assets/visuals/manifest.json` documenta figuras y transformaciones de capturas. Las imágenes oficiales siguen perteneciendo a sus titulares; su inclusión con atribución no implica cesión de licencia sobre ellas.

Las capturas propias se obtuvieron en un perfil aislado de Positron, con datos sintéticos y sin proveedor de IA configurado. Las de MCP/Posit Assistant proceden de documentación oficial y muestran otros proyectos, no el caso del taller.

## Límites metodológicos

La bibliografía específica para fiabilidad y evaluación del caso factorial debe completarse cuando se fijen y ejecuten los procedimientos. No se han incorporado índices de ajuste, cargas ni coeficientes inventados. Las frases que se auditan en actividades se identifican como afirmaciones para discutir, no como resultados.

## Fuentes adicionales de esta reorganización

- Anthropic. Effective harnesses for long-running agents: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents . Papel del entorno de coordinación, no garantía de autonomía ilimitada.
- OpenAI. Iterating development workflows with Codex: https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex . Ejemplo de instrucciones y revisión humana; no evidencia de productividad universal.
- Iconos oficiales: registro en presentacion/assets/brands/provenance.json. Las marcas pertenecen a sus titulares y no implican patrocinio.
- Capturas propias de configuración: presentacion/assets/screenshots/setup-provenance.json. Muestran interfaz, no conexión autenticada.

Los antiejemplos safe_cfa, clean_data y las escenas ChatGPT/RStudio son construcciones docentes. Las convenciones de legibilidad se apoyan en la skill r-analytic-coding-principles y en el encuadre del autor, no en una investigación del entrenamiento de todos los LLM.

## Referencia docente del caso completo

semTools, compRelSEM: https://simsem.r-universe.dev/semTools/doc/manual.html . Se usó la escala ordinal observada para los compuestos de seis ítems; decisiones y versiones están en `docente/caso_autorregulacion/`. Las salidas verificadas no se incluyen en la carpeta recibida.
