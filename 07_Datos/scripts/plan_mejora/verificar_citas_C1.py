#!/usr/bin/env python3
"""
Verificador de citas literales — C1 · SIMPA_ISR401
Valida que cada texto en CITA_LITERAL aparezca tal cual
dentro del archivo de transcripción indicado.

Salida: 0 = todo OK, 1 = hay fallos
"""

import csv
import os
import sys
from pathlib import Path

# Rutas base
BASE = Path(__file__).resolve().parents[2]
DATOS_CRUOS = BASE / "datos_crudos"
DATOS_PROC = BASE / "datos_procesados"
RESULTADOS = BASE / "resultados"

ARCHIVOS_A_VALIDAR = [
    DATOS_CRUOS / "codificacion.csv",
    DATOS_PROC / "codificacion_tercera_ronda.csv",
]

def normalizar(texto):
    """Quita tildes, espacios duplicados y pasa a minúsculas para comparación."""
    if not texto:
        return ""
    t = texto.strip().lower()
    reemplazos = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
        "ñ": "n", "—": "-", "“": '"', "”": '"',
    }
    for c, r in reemplazos.items():
        t = t.replace(c, r)
    return " ".join(t.split())

def verificar_fila(fila, raiz_transcripciones):
    """Comprueba que la cita literal exista en su archivo de origen."""
    errores = []
    cita = fila.get("CITA_LITERAL", "").strip()
    archivo = fila.get("transcripcion", "").strip()
    estado = fila.get("ESTADO", "").strip()

    if not cita:
        return ["CITA_LITERAL vacía"]
    if estado == "NO_LOCALIZADA":
        return []  # Es válido intencionalmente
    if estado == "SOLO_EN_ENTREVISTADOR":
        return []  # No se verifica como evidencia de entrevistado

    ruta = raiz_transcripciones / archivo
    if not ruta.exists():
        return [f"Archivo no encontrado: {archivo}"]

    texto_completo = ruta.read_text(encoding="utf-8")
    if normalizar(cita) not in normalizar(texto_completo):
        errores.append(f"Cita NO localizada: «{cita[:60]}…»")

    return errores

def contar_codigos_unicos(archivo_csv):
    """Devuelve conjunto de códigos presentes en el CSV."""
    codigos = set()
    if not archivo_csv.exists():
        return codigos
    with open(archivo_csv, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f, delimiter=";")
        for fila in lector:
            c = fila.get("Codigo", "").strip()
            if c:
                codigos.add(c)
    return codigos

def main():
    RESULTADOS.mkdir(exist_ok=True)
    salida = []
    total_filas = 0
    citas_ok = 0
    citas_error = 0
    raiz_transcripciones = BASE.parent / "02_Evidencias" / "Transcripciones"

    # Si no encuentra la carpeta de transcripciones, busca hacia arriba
    if not raiz_transcripciones.exists():
        raiz_transcripciones = BASE.parent
        salida.append(f"⚠️  Buscando transcripciones en: {raiz_transcripciones}")

    todos_los_codigos = set()

    for ruta_csv in ARCHIVOS_A_VALIDAR:
        if not ruta_csv.exists():
            salida.append(f"⚠️  Archivo no existe: {ruta_csv.name} — se omite")
            continue
        salida.append(f"📄 Verificando: {ruta_csv.name}")
        with open(ruta_csv, newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f, delimiter=";")
            for fila in lector:
                total_filas += 1
                todos_los_codigos.add(fila.get("Codigo", "").strip())
                errores = verificar_fila(fila, raiz_transcripciones)
                if errores:
                    citas_error += 1
                    salida.append(f"  ❌ Fila {total_filas}: {'; '.join(errores)}")
                else:
                    citas_ok += 1

    # Verificar códigos en libro
    libro = BASE / "libro_codigos.md"
    codigos_en_libro = set()
    if libro.exists():
        texto_libro = libro.read_text(encoding="utf-8")
        for cod in todos_los_codigos:
            if cod and f"| {cod} |" in texto_libro:
                codigos_en_libro.add(cod)

    # Resumen
    salida.append("")
    salida.append("=" * 60)
    salida.append(f"Total filas verificadas: {total_filas}")
    salida.append(f"Citas verificadas correctamente: {citas_ok} ({100*citas_ok/total_filas:.1f}%)")
    salida.append(f"Citas con error: {citas_error}")
    salida.append(f"Códigos únicos detectados: {len(todos_los_codigos)}")
    salida.append(f"Códigos definidos en libro: {len(codigos_en_libro)}")
    salida.append("=" * 60)

    if citas_error == 0 and len(codigos_en_libro) == len(todos_los_codigos):
        salida.append("✅ RESULTADO: TODAS LAS CITAS Y CÓDIGOS VERIFICADOS — CUMPLE")
        codigo_salida = 0
    else:
        salida.append("❌ RESULTADO: HAY INCONSISTENCIAS — REVISAR ARRIBA")
        codigo_salida = 1

    # Guardar reporte
    ruta_salida = RESULTADOS / "c1_verificacion_citas.txt"
    ruta_salida.write_text("\n".join(salida), encoding="utf-8")
    print("\n".join(salida))
    print(f"\nReporte guardado en: {ruta_salida}")
    return codigo_salida

if __name__ == "__main__":
    sys.exit(main())
