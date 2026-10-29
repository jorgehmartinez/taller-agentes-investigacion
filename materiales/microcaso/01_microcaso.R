# Microejemplo didáctico: cinco respuestas ficticias ----
# El diccionario define 1:4 como respuestas y 99 como perdido.
# No es el caso factorial completo del taller.

respuestas <- c(1, 2, 3, 4, 99)

# Ejecuta sin error, pero ignora el significado de 99 ----
mean(respuestas)

# Corregir exige consultar el diccionario ----
respuestas_limpias <- replace(respuestas, respuestas == 99, NA)
mean(respuestas_limpias, na.rm = TRUE)

# El denominador también cambia ----
sum(!is.na(respuestas_limpias))
