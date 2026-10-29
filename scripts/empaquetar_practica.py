#!/usr/bin/env python3
"""Empaqueta únicamente los insumos iniciales, sin soluciones ni instrucciones de agentes."""
from pathlib import Path
import csv
import hashlib
import io
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'practica/carpeta_recibida'
EXPECTED = {
    'Encargo de investigacion.pdf',
    'Cuestionario y clave.pdf',
    'respuestas_octubre.csv',
    'piloto_agosto.csv',
    'diccionario_variables.csv',
    'Notas del equipo.txt',
}
actual = {p.name for p in SOURCE.iterdir()}
if actual != EXPECTED or any(not p.is_file() or p.is_symlink() for p in SOURCE.iterdir()):
    raise SystemExit(f'La carpeta inicial no coincide con los seis insumos aprobados: {sorted(actual)}')

archive = ROOT / 'practica/caso_autorregulacion_inicio.zip'
manifest = {}
with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as out:
    for name in sorted(EXPECTED):
        data = (SOURCE / name).read_bytes()
        entry = zipfile.ZipInfo('caso_autorregulacion/' + name, (2026, 10, 29, 12, 0, 0))
        entry.compress_type = zipfile.ZIP_DEFLATED
        entry.external_attr = 0o100644 << 16
        out.writestr(entry, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
        manifest[name] = {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
with zipfile.ZipFile(archive) as z:
    if z.testzip() is not None:
        raise SystemExit('El archivo ZIP no superó la verificación CRC.')
    for name in EXPECTED:
        if z.read('caso_autorregulacion/' + name) != (SOURCE / name).read_bytes():
            raise SystemExit('Contenido de ZIP diferente del original: ' + name)

report = {
    'archive': str(archive.relative_to(ROOT)),
    'sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
    'files': manifest,
    'has_agent_instructions': False,
    'has_scripts_or_solutions': False,
    'distribution_note': 'Extraer fuera del repositorio; revisar instrucciones globales o heredadas del cliente.'
}
(ROOT / 'docente/caso_autorregulacion/manifest_inicial.json').write_text(
    json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8'
)
print(json.dumps({'zip': str(archive), 'bytes': archive.stat().st_size, 'files': len(EXPECTED)}))
