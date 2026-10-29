# Cómo revisar una skill para análisis de datos e investigación

La skill no sustituye conocimientos disciplinares: proporciona instrucciones y recursos reutilizables que ayudan al agente a actuar de manera más consistente. Un modelo generalista puede conocer una técnica sin conocer las convenciones, decisiones y límites de un equipo.

## Checklist de adopción

- [ ] **Problema de uso:** ¿la skill tiene una finalidad precisa, activable y diferenciada de instrucciones generales?
- [ ] **Descripción:** ¿el nombre y la descripción indican cuándo usarla y, cuando importa, cuándo *no* usarla?
- [ ] **Densidad:** ¿el contenido principal es conciso, accionable y sin repeticiones, con detalles en referencias?
- [ ] **Alcance:** ¿separa convenciones de codificación de decisiones metodológicas que dependen del estudio?
- [ ] **Compatibilidad:** ¿identifica versiones, herramientas y limitaciones verificadas sin prometer portabilidad perfecta?
- [ ] **Evidencia:** ¿sus afirmaciones específicas, criterios estadísticos y recomendaciones tienen base y condiciones de aplicación?
- [ ] **Seguridad:** ¿el origen es fiable? ¿Revisaste scripts, comandos, dependencias, datos enviados fuera y permisos?
- [ ] **Prueba positiva:** ¿la utilizaste con un ejemplo compatible y verificaste resultados y legibilidad?
- [ ] **Prueba negativa:** ¿la utilizaste ante un error o una ambigüedad y comprobaste que no toma decisiones peligrosas?
- [ ] **Mantenibilidad:** ¿cuenta con responsable, versión, referencias, changelog o estrategia de actualización apropiada?

## Ejemplo para el taller

Una skill puede pedir que, antes de ajustar un AFC ordinal, se inspeccionen categorías, códigos perdidos y diccionario. **No** debería dar por válida una recodificación sin respaldo documental ni imponer un estimador sin evaluar el diseño.

## Para una skill propia

1. Identifica un procedimiento repetitivo cuyo valor supere el coste de mantenerlo.
2. Define el criterio de activación y lo que queda fuera.
3. Establece pasos observables y entregables, manteniendo decisiones científicas como puntos de revisión.
4. Incluye recursos mínimos de apoyo, sin duplicar el protocolo del proyecto.
5. Prueba casos correctos y adversariales, registra fallos y revisa antes de publicar.

La versión ilustrativa presentada en las diapositivas **no es una skill psicométrica publicada**. El material definitivo se integrará desde `r-workflow-plugins` cuando haya una versión comprobada.
