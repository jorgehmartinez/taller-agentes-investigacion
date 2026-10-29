# Herramientas del taller: orientación sin instalación obligatoria

## Cuatro niveles

1. **Modelo:** GPT, Claude, Gemini u otros LLM.
2. **Agente:** Codex, Claude Code, Gemini CLI, OpenCode o Posit Assistant según entorno.
3. **Editor/interfaz:** Positron o RStudio, donde se gestiona el proyecto.
4. **Motor analítico:** R y sus paquetes.

MCP es un protocolo de conexión con herramientas: no es un modelo ni reemplaza a R.

## Opción principal de la demostración: Positron + MCP + R

La versión Positron 2026.10 incorporó un **servidor MCP experimental** para conectar agentes externos con sesiones activas de R y Python. Según sus notas oficiales, se activa con `ai.mcp.enabled`; ofrece una configuración para Claude Code y comando de asociación para Codex/Gemini CLI. Confirmar la versión local y probar el recorrido completo antes del evento.

Fuente: https://positron.posit.co/release-notes

## Alternativa: Posit Assistant

Posit Assistant está disponible en Positron y RStudio, se conecta al contexto vivo de R/Python y permite configurar proveedores de modelos. Un proveedor puede requerir API key u otro mecanismo de acceso; una suscripción de chat no implica automáticamente acceso API.

Fuentes:
- https://assistant.posit.co/docs/getting-started/
- https://assistant.posit.co/docs/getting-started/providers/
- https://positron.posit.co/assistant

## Preparación docente

- Preparar el proyecto antes del taller.
- Mantener una sesión de R conocida, con datos **sintéticos**.
- Verificar si el agente puede ejecutar R, inspeccionar resultados y guardar archivos.
- Probar el mismo recorrido desde una sesión R limpia.
- Disponer de capturas o salidas de respaldo verificadas.
- No pedir a los asistentes que conecten credenciales en directo.

## Portabilidad realista

No todos los agentes admiten idéntica sintaxis de instrucciones, selección de skills, permisos ni MCP. El método de investigación es el componente transferible; el montaje concreto debe comprobarse por producto y versión.

Actualizado contra la documentación oficial consultada el 29-10-2026.
