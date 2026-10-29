# Comprobación docente: NO forma parte de la carpeta inicial ----
# Ejecutar desde la raíz del repositorio del taller.
# Es un análisis de referencia, no la única estrategia metodológica admisible.
# La simulación es para formación y no valida un instrumento real.

library(dplyr)
library(readr)
library(tidyr)
library(tibble)
library(lavaan)

carpeta <- "practica/carpeta_recibida"
salida <- "docente/caso_autorregulacion/resultados"
items <- sprintf("i%02d", 1:12)

# Leer la exportación preservando sus códigos originales ----
original <- read_csv(
  file.path(carpeta, "respuestas_octubre.csv"),
  col_types = cols(id = col_character(), modalidad = col_character(),
                   .default = col_double()),
  na = ""
)
repetidos <- original |> count(id) |> filter(n > 1)
print(repetidos)
write_csv(repetidos, file.path(salida, "identificadores_repetidos.csv"))

# Decisión docente de referencia: la fila repetida es idéntica en TODAS las variables.
# En directo, debe mostrarse y aprobarse la decisión; no deduplicar por id a ciegas.
filas_duplicadas <- sum(duplicated(original))
datos_unicos <- distinct(original)

# Dos convenciones de ausencia y dos ítems de dirección inversa ----
resumen_entrada <- tibble(
  concepto = c("filas_exportadas", "identificadores_unicos", "duplicados_exactos",
               "codigos_99", "celdas_vacias", "personas_tras_deduplicacion"),
  valor = c(nrow(original), n_distinct(original$id), filas_duplicadas,
            sum(as.matrix(datos_unicos[items]) == 99, na.rm = TRUE),
            sum(is.na(datos_unicos[items])), nrow(datos_unicos))
)
print(resumen_entrada)
write_csv(resumen_entrada, file.path(salida, "auditoria_entrada.csv"))

datos <- datos_unicos |>
  mutate(across(all_of(items), ~ na_if(.x, 99))) |>
  mutate(across(c(i03, i09), ~ 5 - .x))

frecuencias <- datos |>
  select(all_of(items)) |>
  pivot_longer(everything(), names_to = "item", values_to = "respuesta") |>
  count(item, respuesta, name = "n") |>
  group_by(item) |>
  mutate(porcentaje_sobre_500 = 100 * n / sum(n)) |>
  ungroup()
write_csv(frecuencias, file.path(salida, "frecuencias_items.csv"))

n_completos <- sum(complete.cases(datos[items]))
n_por_pares <- crossprod(!is.na(as.matrix(datos[items])))
print(c(n_completos = n_completos, n_minimo_por_par = min(n_por_pares)))
write_csv(as_tibble(n_por_pares, rownames = "item"),
          file.path(salida, "n_por_pares.csv"))

# Modelo teórico: dos factores correlacionados ----
# Referencia: respuestas ordinales, WLSMV, identificación std.lv.
# Se usan pares disponibles. No es FIML ni prueba de ignorabilidad de omisiones.
# La elección de missing/estimador debe discutirse; conservar N por ítem y par.
modelo_dos <- '
  Planificacion =~ i01 + i02 + i03 + i04 + i05 + i06
  Persistencia =~ i07 + i08 + i09 + i10 + i11 + i12
'
ajuste_dos <- cfa(
  modelo_dos,
  data = datos,
  ordered = items,
  estimator = "WLSMV",
  missing = "pairwise",
  std.lv = TRUE
)
summary(ajuste_dos, fit.measures = TRUE, standardized = TRUE)

# Referencia sustantiva alternativa: un factor general ----
modelo_uno <- '
  Autorregulacion =~ i01 + i02 + i03 + i04 + i05 + i06 +
                    i07 + i08 + i09 + i10 + i11 + i12
'
ajuste_uno <- cfa(
  modelo_uno,
  data = datos,
  ordered = items,
  estimator = "WLSMV",
  missing = "pairwise",
  std.lv = TRUE
)
summary(ajuste_uno, fit.measures = TRUE, standardized = TRUE)

# Comparación descriptiva: no convertir el ajuste en selección automática ----
indices <- c("chisq.scaled", "df.scaled", "cfi.scaled", "tli.scaled",
             "rmsea.scaled", "srmr")
comparacion <- bind_rows(
  as_tibble_row(fitMeasures(ajuste_uno, indices)) |> mutate(modelo = "un_factor", .before = 1),
  as_tibble_row(fitMeasures(ajuste_dos, indices)) |> mutate(modelo = "dos_factores", .before = 1)
)
print(comparacion)
write_csv(comparacion, file.path(salida, "comparacion_modelos.csv"))
parametros_dos <- parameterEstimates(ajuste_dos, standardized = TRUE)
write_csv(parametros_dos, file.path(salida, "parametros_dos_factores.csv"))
residuos_dos <- lavResiduals(ajuste_dos, type = "cor.bentler")
write_csv(as_tibble(residuos_dos$cov, rownames = "item"),
          file.path(salida, "residuos_correlaciones.csv"))

# Fiabilidad de compuestos de seis ítems en la escala observada ordinal ----
# No calcular automáticamente un total de doce ítems.
fiabilidad <- semTools::compRelSEM(
  ajuste_dos, tau.eq = FALSE, ord.scale = TRUE,
  return.total = FALSE, simplify = TRUE
)
print(fiabilidad)
write_csv(tibble(dimension = names(fiabilidad), coeficiente = as.numeric(fiabilidad)),
          file.path(salida, "fiabilidad_dimensiones.csv"))

# Inspecciones de la solución y trazabilidad del ensayo ----
varianzas <- parametros_dos |>
  filter(op == "~~", lhs == rhs) |>
  select(lhs, est)
diagnosticos <- tibble(
  concepto = c("n_analitico", "casos_completos", "n_minimo_por_par",
               "convergio_dos_factores", "convergio_un_factor", "varianzas_negativas",
               "min_autovalor_cov_factores"),
  valor = c(nrow(datos), n_completos, min(n_por_pares),
            lavInspect(ajuste_dos, "converged"), lavInspect(ajuste_uno, "converged"),
            sum(varianzas$est < 0),
            min(eigen(lavInspect(ajuste_dos, "cov.lv"), symmetric = TRUE)$values))
)
print(diagnosticos)
write_csv(diagnosticos, file.path(salida, "diagnosticos.csv"))
saveRDS(list(dos_factores = ajuste_dos, un_factor = ajuste_uno),
        file.path(salida, "ajustes_referencia.rds"))
write_lines(capture.output(sessionInfo()), file.path(salida, "sesion_analisis.txt"))
