#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
G1a — Capa automatizada: búsqueda de cédulas y RUC en documentos éticos
Proyecto SIMPA — Equipo AHMRV — ISR-401 — UTEQ

Extrae el texto de cada PDF listado en el plan de mejora de datos
(sección 9.1, "Cédulas y RUC") y busca patrones de 10 dígitos (cédula
ecuatoriana) y 13 dígitos (RUC ecuatoriano), reportando archivo, línea
y contexto exacto. No modifica ningún PDF — solo detecta y reporta.

Requiere: pdftotext (poppler-utils)

Uso:
    python3 buscar_cedulas_ruc.py > g1a_salida.txt
"""

import re
import subprocess
from pathlib import Path

ARCHIVOS = [
    "09_Etica/A01_Protocolo_Investigacion.pdf",
    "09_Etica/A05_Aval_Institucional.pdf",
    "09_Etica/A06_Declaracion_Conflicto_Intereses.pdf",
    "09_Etica/A07_Compromiso_Confidencialidad.pdf",
    "09_Etica/A09_Nomina_Equipo.pdf",
    "09_Etica/A12_Certificado_Etica.pdf",
    "09_Etica/Categoria_C/C1_Aval_Unidad_Productiva.pdf",
    "09_Etica/Categoria_C/C2_Compromiso_Confidencialidad_Estrategica.pdf",
    "09_Etica/A02_Instrumentos_Recoleccion.pdf",
    "09_Etica/A04_Plan_Gestion_Datos.pdf",
    "09_Etica/A10_Cronograma_Gantt.pdf",
    "09_Etica/A11_Analisis_Riesgos.pdf",
    "09_Etica/Categoria_C/C3_Protocolo_Anonimizacion.pdf",
    "09_Etica/Categoria_C/C4_Normativa_Sectorial.pdf",
]

PATRON = re.compile(r"\b[0-9]{10}\b|\b[0-9]{13}\b")


def extraer_texto(ruta_pdf: Path) -> list[str]:
    resultado = subprocess.run(
        ["pdftotext", "-layout", str(ruta_pdf), "-"],
        capture_output=True, text=True, check=True,
    )
    return resultado.stdout.splitlines()


def main():
    total_ocurrencias = 0
    for ruta_str in ARCHIVOS:
        ruta = Path(ruta_str)
        if not ruta.is_file():
            print(f"AVISO: no se encontró {ruta_str}")
            continue
        lineas = extraer_texto(ruta)
        encontrados = []
        for num_linea, texto in enumerate(lineas, start=1):
            for m in PATRON.finditer(texto):
                encontrados.append((num_linea, m.group(), texto.strip()))

        print(f"=== {ruta_str} ===")
        if not encontrados:
            print("  Sin coincidencias de 10 o 13 dígitos.")
        for num_linea, valor, contexto in encontrados:
            tipo = "RUC" if len(valor) == 13 else "cédula"
            print(f"  línea {num_linea} [{tipo}] {'#' * len(valor)}")
            total_ocurrencias += 1
        print()

    print(f"TOTAL de ocurrencias detectadas: {total_ocurrencias}")
    print("Este script solo detecta. La redacción real del PDF es un paso aparte,")
    print("y su verificación visual (Capa 2) es responsabilidad de Arboleda.")


if __name__ == "__main__":
    main()
