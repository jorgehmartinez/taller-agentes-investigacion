# Preparar Positron y un agente para el taller

Guía para la integración experimental documentada en Positron 2026.10. Probar la versión, cliente y equipo concretos antes del evento. No se presupone compatibilidad idéntica entre todos los agentes.

## Preparar el entorno

Abrir la carpeta del caso e iniciar una sesión R. Comprobar directorio, datos sintéticos y permisos. Configurar previamente el acceso al modelo del agente elegido. Preparar paquetes antes del taller; no introducir instalación automática en scripts de análisis.

## Agente externo mediante MCP

1. Abrir Settings en Positron, buscar `ai.mcp.enabled` y activar el servidor para la ventana de trabajo.
2. Para Codex o Gemini CLI, abrir la paleta y usar **Positron MCP: Add to Coding Agent**. Seguir la configuración que genere la versión instalada.
3. Las notas oficiales describen configuración automática para Claude Code. Verificarla en la instalación real, sin asumirla por el nombre del agente.
4. Otros clientes pueden utilizar **Positron MCP: Copy Connection Details**. Estos detalles pueden incluir tokens: tratarlos como secretos y no proyectarlos, publicarlos ni guardarlos en el repositorio.
5. Revisar herramientas y permisos. Conectar MCP no concede aprobación metodológica ni permiso ilimitado para modificar archivos.

Fuente: https://opensource.posit.co/blog/2026-10-13_positron-2026-10-release/

## Comprobar la conexión

Pedido: «Lista las sesiones disponibles. Identifica la sesión R del taller. Ejecuta sum(1:4) en esa sesión. Muestra la salida y no modifiques archivos ni configuraciones».

El cálculo debe producir 10, pero **que el chat responda 10 no prueba acceso a R**. Deben observarse la sesión correcta, la llamada a herramienta y la ejecución en Positron. Las capturas del ajuste y del comando preparadas para las diapositivas no constituyen esa prueba. La conexión debe verificarse con el agente definitivo.

## Vía integrada

Posit Assistant en Positron o RStudio es otra opción. No hace falta usar simultáneamente las dos rutas durante el taller. Configurar un proveedor compatible fuera de la proyección y revisar sus condiciones de acceso. Tener una cuenta de chat no establece por sí solo acceso API.

Documentación: https://assistant.posit.co/docs/getting-started/ y https://assistant.posit.co/docs/getting-started/providers/ .

## Compartir pantalla y entregar resultados

Usar datos sintéticos, cerrar proyectos y notificaciones ajenos, y no mostrar claves, tokens o archivos de credenciales. Guardar código y resultados en el proyecto, no solo en una conversación. Una sesión persistente facilita explorar; los scripts deben poder ejecutarse también desde una sesión limpia.
