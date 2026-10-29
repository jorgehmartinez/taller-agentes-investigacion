# Ejemplos de organización del código

Los fragmentos de AFC y arquitectura son ilustrativos y no se ejecutaron sobre una base real. safe_cfa y clean_data son nombres ficticios de antiejemplos, no recomendaciones ni funciones de lavaan.

## Qué puede esconder una función auxiliar: left

```r
safe_cfa <- function(modelo, datos) {
  tryCatch(
    suppressWarnings(
      lavaan::cfa(modelo, data = datos)
    ),
    error = function(e) NULL
  )
}
```

safe_cfa es un nombre ficticio, no una función de lavaan. En este antiejemplo, warnings y fallos dejan de ser visibles. La envoltura también puede ocultar argumentos y decisiones. Ni for ni las funciones auxiliares son incorrectos en general: se cuestiona que escondan las decisiones del estudio. No recomendar este código ni atribuirlo al entrenamiento universal de los LLM.

## Qué puede esconder una función auxiliar: right

```r
for (nombre in names(modelos)) {
  ajustes[[nombre]] <- safe_cfa(
    modelos[[nombre]], datos
  )
}

# ¿Dónde revisas estimador y fallos?
```

safe_cfa es un nombre ficticio, no una función de lavaan. En este antiejemplo, warnings y fallos dejan de ser visibles. La envoltura también puede ocultar argumentos y decisiones. Ni for ni las funciones auxiliares son incorrectos en general: se cuestiona que escondan las decisiones del estudio. No recomendar este código ni atribuirlo al entrenamiento universal de los LLM.

## Un AFC que podamos revisar y modificar: visual

```r
modelo <- '
  planificacion =~ i01 + i02 + i03 + i04 + i05 + i06
  persistencia  =~ i07 + i08 + i09 + i10 + i11 + i12
'

ajuste <- lavaan::cfa(
  modelo, data = datos, ordered = items, estimator = "WLSMV"
)
summary(ajuste, fit.measures = TRUE, standardized = TRUE)
```

El objeto es la organización del código, no enseñar AFC desde cero. Mostrar especificación, estimación y diagnóstico cerca. datos e items son entradas del estudio aún por definir: este fragmento es ilustrativo y no se ha ejecutado. WLSMV está escrito como decisión visible del ejemplo, no impuesto como regla general. Alterar una estructura factorial necesita justificación sustantiva, no solo editar una línea.

## La preparación de datos también debe verse: left

```r
source("R/preparacion.R")
datos <- clean_data(ruta)

# ¿Qué códigos cambió?
# ¿Qué ítems invirtió?
# ¿Qué casos excluyó?
```

Ejemplo ficticio: el diccionario define NS como perdido y la clave define i03 como inverso en respuestas de 1 a 4. No inferir estas reglas de las correlaciones. clean_data es una función inventada de contenido no mostrado, no se afirma equivalencia entre fragmentos. La derecha muestra dónde revisar la decisión. Las validaciones sustantivas y el registro de exclusiones se conservan.

## La preparación de datos también debe verse: right

```r
datos <- readr::read_csv(
  "data/escala.csv", na = "NS"
)
datos <- datos |>
  dplyr::mutate(i03 = 5 - i03)
```

Ejemplo ficticio: el diccionario define NS como perdido y la clave define i03 como inverso en respuestas de 1 a 4. No inferir estas reglas de las correlaciones. clean_data es una función inventada de contenido no mostrado, no se afirma equivalencia entre fragmentos. La derecha muestra dónde revisar la decisión. Las validaciones sustantivas y el registro de exclusiones se conservan.

## Un error visible también informa: left

```r
datos <- tryCatch(
  readr::read_csv(ruta),
  error = function(e) tibble::tibble()
)
# Falla la lectura, pero devuelve
# una tabla vacía.
```

No enseñar a retirar todos los controles: distinguir un fallo de lectura real de una rutina genérica que lo silencia. El agente puede inspeccionar archivos y mensajes en vez de añadir manejadores para cada escenario imaginable. Los riesgos silenciosos concretos, por ejemplo una unión muchos-a-muchos inesperada, sí pueden requerir controles persistentes.
