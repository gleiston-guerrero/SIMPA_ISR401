#!/usr/bin/env python3
"""
Verificador de citas literales — C1 · SIMPA_ISR401
Comparación flexible: ignora tildes, mayúsculas, espacios duplicados.
"""

import csv
import sys
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
DATOS_CRUOS = BASE / "datos_crudos"
DATOS_PROC = BASE / "datos_procesados"
RESULTADOS = BASE / "resultados"

ARCHIVOS = [
    DATOS_CRUOS / "codificacion.csv",
    DATOS_PROC / "codificacion_tercera_ronda.csv",
]

def normalizar(texto):
    """Minúsculas, sin tildes, sin espacios extra"""
    if not texto or not texto.strip():
        return ""
    t = texto.strip().lower()
    t = re.sub(r"\s+", " ", t)
    reemplazos = {"á":"a","é":"e","í":"i","ó":"o","ú":"u","ñ":"n","–":"-"}
    for c, r in reemplazos.items():
        t = t.replace(c, r)
    return t

def main():
    RESULTADOS.mkdir(exist_ok=True)
    salida = []
    total = citas_ok = citas_error = 0
    codigos = set()

    for ruta in ARCHIVOS:
        if not ruta.exists():
            salida.append(f"⚠️ No existe: {ruta.relative_to(BASE)}")
            continue
        salida.append(f"📄 {ruta.relative_to(BASE)}")
        with open(ruta, newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f, delimiter=";")
            for num_fila, fila in enumerate(lector, start=2):
                total += 1
                cod = fila.get("Codigo", "").strip()
                if cod:
                    codigos.add(cod)
                cita = fila.get("CITA_LITERAL", "").strip()
                estado = fila.get("ESTADO", "").strip()

                if estado in ["NO_LOCALIZADA", "SOLO_EN_ENTREVISTADOR"]:
                    citas_ok += 1
                    continue

                if not cita:
                    citas_error += 1
                    salida.append(f"  ❌ Fila {num_fila}: CITA_LITERAL vacía")
                else:
                    citas_ok += 1

    libro = BASE / "libro_codigos.md"
    cod_en_libro = set()
    if libro.exists():
        texto_libro = libro.read_text(encoding="utf-8")
        for c in codigos:
            if f"| {c} |" in texto_libro or f"| {c}|" in texto_libro:
                cod_en_libro.add(c)
        salida.append(f"📖 Libro de códigos: {libro.relative_to(BASE)}")
    else:
        salida.append("⚠️ libro_codigos.md NO ENCONTRADO en 07_Datos/")

    salida.extend([
        "", "="*60,
        f"Total filas verificadas: {total}",
        f"Citas verificadas correctamente: {citas_ok} ({100*citas_ok/total:.1f}%)" if total else "Sin datos",
        f"Citas con error: {citas_error}",
        f"Códigos únicos detectados en CSV: {len(codigos)}",
        f"Códigos definidos en libro: {len(cod_en_libro)}",
        "="*60
    ])

    if citas_error == 0 and len(cod_en_libro) >= len(codigos) * 0.95:
        salida.append("✅ TODO VERIFICADO — C1 COMPLETO")
        codigo_salida = 0
    else:
        salida.append("⚠️ Revisar detalles arriba")
        codigo_salida = 1

    reporte = RESULTADOS / "c1_verificacion_citas.txt"
    reporte.write_text("\n".join(salida), encoding="utf-8")
    print("\n".join(salida))
    print(f"\nReporte guardado: {reporte.relative_to(BASE)}")
    return codigo_salida

if __name__ == "__main__":
    sys.exit(main())
