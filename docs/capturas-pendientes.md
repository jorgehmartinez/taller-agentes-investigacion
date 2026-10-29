# Capturas auténticas del agente del taller

Las escenas ChatGPT → RStudio son esquemas ficticios intencionados: no necesitan capturas reales. Ya existen capturas propias del editor, consola, archivo de skill, ajuste MCP y comando de configuración. Falta mostrar el **cliente definitivo conectado** y la skill realmente utilizada.

Guardar los originales PNG en:

`presentacion/assets/screenshots/por-incorporar/`

## 01_mcp_agente_r.png

Abrir el proyecto sintético del taller en Positron, iniciar R y conectar el agente definitivo por MCP. Pedir: «Identifica la sesión R del taller y ejecuta sum(1:4) en ella». Distribuir los paneles para ver la petición, la llamada a la herramienta y la consola de Positron con el código y su salida 10. Capturar después de completar la ejecución real. Una respuesta textual del chat no prueba conexión.

No mostrar URL de conexión, tokens, archivos de credenciales, cuentas personales ni claves. Cerrar esas vistas antes de capturar. No reconstruir una ejecución ficticia ni modificar los resultados de la imagen.

## 02_skill_codigo_revisable.png

En el mismo proyecto, cargar o invocar `r-analytic-coding-principles` mediante el mecanismo del agente elegido. Usar una tarea pequeña con datos sintéticos para revisar o reorganizar un análisis manteniendo sus decisiones y resultados. Mostrar la llamada o indicador que permita comprobar la lectura de la skill y un fragmento de script con especificación, estimación e inspección visibles. Escribir el nombre en un prompt no demuestra por sí solo que la skill se haya cargado.

Cuando esté validada la skill psicométrica, podrá añadirse una captura de una decisión metodológica que realmente se deje a revisión humana. No fingir ese comportamiento mientras la implementación esté pendiente.

## Formato y contexto

Capturar la ventana de aplicación, no todo el escritorio. Preferir 1920×1080 o superior, PNG original y fuente del editor aproximadamente de 20–24 px; evitar líneas cortadas, notificaciones y compresión de mensajería. No añadir anotaciones al original: se prepararán recortes y llamadas después.

Guardar también `contexto.md` con fecha, versión de Positron, agente, skill o commit, prompt exacto y operación realizada. No incluir secretos. Mientras falten estas imágenes, la presentación mantiene una captura oficial de Posit, identificada como ejemplo de otro proyecto, y no la atribuye al taller.
