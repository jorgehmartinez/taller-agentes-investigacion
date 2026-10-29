#!/usr/bin/env python3
"""Esquemas de la práctica inicial. Reflejan archivos reales, no una captura de software."""
from visual_primitives import Figure, NAVY, TEAL, MAG, MUTED, LINE, WHITE, PALE, PINK

f = Figure('carpeta-recibida', 'La carpeta recibida',
           'Seis archivos reales: encargo PDF, cuestionario y clave PDF, base principal CSV, piloto CSV, diccionario CSV y notas TXT. No contiene AGENTS.md, scripts ni resultados.')
f.rect(20, 24, 650, 376, WHITE, LINE, 12, 1)
f.rect(20, 24, 650, 58, NAVY, r=12)
f.text(42, 62, 'caso_autorregulacion/', 30, WHITE, 600)
files = [('PDF', 'Encargo de investigacion.pdf'),
         ('PDF', 'Cuestionario y clave.pdf'),
         ('CSV', 'respuestas_octubre.csv'),
         ('CSV', 'piloto_agosto.csv'),
         ('CSV', 'diccionario_variables.csv'),
         ('TXT', 'Notas del equipo.txt')]
for i, (kind, name) in enumerate(files):
    y = 112 + i * 47
    f.rect(43, y - 22, 54, 30, PALE if kind == 'CSV' else PINK, r=5)
    f.text(70, y, kind, 18, TEAL if kind == 'CSV' else MAG, 600, 'middle')
    f.text(115, y + 1, name, 26, NAVY)
f.text(727, 104, 'TODAVÍA NO HAY', 23, MAG, 700)
f.text(727, 157, 'AGENTS.md', 31, NAVY, 500)
f.text(727, 203, 'Scripts de análisis', 28, NAVY)
f.text(727, 249, 'Resultados', 28, NAVY)
f.line(727, 277, 1090, 277, LINE, 2)
f.text(727, 322, 'La organización se construye', 24, MUTED)
f.text(727, 355, 'durante la práctica.', 24, MUTED)
f.save()

f = Figure('preparar-proyecto', 'Antes del primer modelo',
           'Leer el encargo, acordar decisiones, proponer organización y crear instrucciones. La aprobación humana precede a la escritura y al análisis.')
steps = [('Entender', 'PDF, diccionario', 'y archivos'),
         ('Acordar', 'Objetivos, límites', 'y revisiones'),
         ('Organizar', 'Originales intactos;', 'derivados claros'),
         ('Configurar', 'AGENTS.md + skill', 'disponible')]
for i, (title, a, b) in enumerate(steps):
    x = 18 + i * 280
    color = TEAL if i % 2 == 0 else MAG
    f.circle(x + 32, 80, 26, color)
    f.text(x + 32, 89, str(i + 1), 26, WHITE, 700, 'middle')
    f.text(x, 149, title, 32, NAVY, 600)
    f.text(x, 203, a, 24, MUTED)
    f.text(x, 238, b, 24, MUTED)
    if i < 3:
        f.arrow(x + 204, 143, x + 261, 143, LINE, 2)
f.rect(18, 302, 1080, 91, NAVY, r=10)
f.text(558, 340, 'Propuesta → revisión humana → cambios autorizados', 29, WHITE, 600, 'middle')
f.text(558, 373, 'No empezamos copiando una plantilla ni ejecutando modelos.', 23, '#D4E6E8', 400, 'middle')
f.save()
print('Created carpeta-recibida.svg and preparar-proyecto.svg')
