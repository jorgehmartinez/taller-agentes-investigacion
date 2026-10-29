# Preparación docente: datos sintéticos para una carpeta recibida ----
# Ejecutar desde la raíz del repositorio del taller.
# No entregar este script ni los parámetros en la carpeta inicial.
library(dplyr)
library(readr)
library(tibble)

set.seed(20261029)

# Escenario sintético: 500 casos y un piloto independiente de 60 ----
n_principal <- 500L
n_piloto <- 60L
n_total <- n_principal + n_piloto
items <- sprintf("i%02d", 1:12)
cargas <- c(.72, .68, .67, .76, .70, .74, .73, .69, .66, .77, .71, .75)
correlacion_factores <- .45
planificacion <- rnorm(n_total)
persistencia <- correlacion_factores * planificacion +
  sqrt(1 - correlacion_factores^2) * rnorm(n_total)

# El bucle genera ítems, no oculta decisiones de modelos alternativos.
respuestas <- matrix(NA_integer_, nrow = n_total, ncol = 12,
                     dimnames = list(NULL, items))
desplazamientos <- c(-.20, .10, -.10, .15, .05, -.05,
                    -.10, .15, .05, -.15, .20, -.05)
for (j in seq_along(items)) {
  factor_item <- if (j <= 6) planificacion else persistencia
  respuesta_latente <- cargas[j] * factor_item +
    sqrt(1 - cargas[j]^2) * rnorm(n_total)
  umbrales <- c(-.75, 0, .85) + desplazamientos[j]
  respuestas[, j] <- as.integer(cut(
    respuesta_latente, breaks = c(-Inf, umbrales, Inf), labels = FALSE
  ))
}

# Dirección de redacción original: todavía no son puntuaciones recodificadas.
respuestas[, c("i03", "i09")] <- 5L - respuestas[, c("i03", "i09")]
respuestas_completas <- respuestas
metadatos <- tibble(
  id = c(sprintf("E%04d", 1:n_principal), sprintf("P%04d", 1:n_piloto)),
  edad = sample(18:30, n_total, replace = TRUE,
                prob = c(9, 12, 14, 14, 12, 10, 8, 6, 5, 4, 3, 2, 1)),
  ciclo = sample(c(2L, 4L, 6L, 8L, 10L), n_total, replace = TRUE),
  modalidad = sample(c("Presencial", "Hibrida"), n_total,
                     replace = TRUE, prob = c(.65, .35))
)

# Incidencias didácticas, sin seleccionar muestras por su ajuste factorial ----
# 120 celdas: 90 códigos 99 y 30 vacíos. E0173 se conserva completo.
coordenadas <- expand.grid(fila = seq_len(n_principal), columna = seq_along(items))
coordenadas <- coordenadas[coordenadas$fila != 173L, ]
seleccion <- coordenadas[sample(nrow(coordenadas), 120L), ]
respuestas[as.matrix(seleccion[1:90, ])] <- 99L
respuestas[as.matrix(seleccion[91:120, ])] <- NA_integer_
base_completa <- bind_cols(metadatos, as_tibble(respuestas))
principal <- slice(base_completa, 1:n_principal)
piloto <- slice(base_completa, (n_principal + 1):n_total)
# Un reintento de exportación: la fila es idéntica, no una medición longitudinal.
principal_exportada <- bind_rows(principal, slice(principal, 173L))

carpeta <- "practica/carpeta_recibida"
dir.create(carpeta, recursive = TRUE, showWarnings = FALSE)
dir.create("docente/caso_autorregulacion/resultados", recursive = TRUE,
           showWarnings = FALSE)
write_csv(principal_exportada, file.path(carpeta, "respuestas_octubre.csv"), na = "")
write_csv(piloto, file.path(carpeta, "piloto_agosto.csv"), na = "")

# Documentación del instrumento ficticio ----
textos_items <- c(
  "Antes de estudiar, defino qué quiero completar.",
  "Distribuyo mi tiempo entre las tareas que tengo pendientes.",
  "Empiezo a estudiar sin decidir qué tareas haré.",
  "Organizo los materiales que necesito antes de comenzar.",
  "Divido los trabajos extensos en pasos más pequeños.",
  "Reviso mi planificación cuando cambian los plazos.",
  "Continúo trabajando aunque una tarea requiera más esfuerzo del previsto.",
  "Retomo el estudio después de una interrupción.",
  "Cuando una actividad se complica, suelo abandonarla.",
  "Busco otra manera de avanzar cuando no entiendo un ejercicio.",
  "Mantengo el esfuerzo hasta terminar las actividades que me propongo.",
  "Vuelvo a intentar una tarea después de equivocarme."
)
diccionario_contexto <- tibble(
  variable = c("id", "edad", "ciclo", "modalidad"),
  descripcion = c("Identificador sintético; E = principal, P = piloto",
                  "Edad ficticia en años cumplidos", "Ciclo universitario ficticio",
                  "Modalidad ficticia de estudios"),
  tipo = c("texto", "entero", "entero", "texto"),
  valores_validos = c("E0001 a E0500; P0001 a P0060", "18 a 30",
                     "2; 4; 6; 8; 10", "Presencial; Hibrida"),
  perdidos = "No previstos", dimension_propuesta = "No aplica",
  direccion = "No aplica"
)
diccionario_items <- tibble(
  variable = items, descripcion = textos_items, tipo = "ordinal",
  valores_validos = "1 = casi nunca; 2 = algunas veces; 3 = muchas veces; 4 = casi siempre",
  perdidos = "99 = sin respuesta; celda vacía = dato no registrado en exportación",
  dimension_propuesta = rep(c("Planificacion", "Persistencia"), each = 6),
  direccion = if_else(items %in% c("i03", "i09"),
                      "Inversa: 1 a 4; 2 a 3; 3 a 2; 4 a 1 (solo valores válidos)",
                      "Directa")
)
write_csv(bind_rows(diccionario_contexto, diccionario_items),
          file.path(carpeta, "diccionario_variables.csv"), na = "")

# Información docente, fuera de los materiales de participantes ----
saveRDS(list(
  seed = 20261029L, cargas = cargas,
  correlacion_factores = correlacion_factores,
  umbrales_base = c(-.75, 0, .85), desplazamientos = desplazamientos,
  factores = tibble(planificacion, persistencia),
  respuestas_completas = respuestas_completas,
  indices_missing = seleccion, duplicado = "E0173",
  nota = "MCAR por construcción; no es una conclusión inferible de la base recibida."
), "docente/caso_autorregulacion/resultados/generacion.rds")
write_lines(capture.output(sessionInfo()),
            "docente/caso_autorregulacion/resultados/sesion_generacion.txt")
cat("Principal:", nrow(principal_exportada), "filas;",
    n_distinct(principal_exportada$id), "IDs únicos.\n")
cat("Piloto:", nrow(piloto), "filas.\n")
cat("Códigos 99:", sum(as.matrix(principal[items]) == 99, na.rm = TRUE),
    "; vacíos:", sum(is.na(principal[items])), "\n")
