#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
D6 — Alcance real de la gestion del backlog en Jira.

Deriva por computo, desde `04_Trazabilidad/backlog_export.csv`, las cifras que
se declaran en `04_Trazabilidad/readme.md`: total de incidencias, estado,
asignacion y autoria. Ninguna cifra del readme se escribe a mano.

Uso, desde la raiz del repositorio:

    python3 07_Datos/scripts/plan_mejora/resumen_backlog.py
"""

import csv
import os
import sys
from collections import Counter

CSV = os.path.join("04_Trazabilidad", "backlog_export.csv")

INTEGRANTES = {
    "ALLAN NOE VILLAFUERTE ROSERO",
    "erizzov",
}


def main():
    if not os.path.exists(CSV):
        sys.exit(
            f"ERROR: no se encontro '{CSV}'.\n"
            "Ejecute el script desde la raiz del repositorio."
        )

    with open(CSV, encoding="utf-8-sig", newline="") as f:
        filas = list(csv.DictReader(f))

    if not filas:
        sys.exit("ERROR: el export no contiene ninguna incidencia.")

    total = len(filas)
    estados = Counter(r["Estado"] for r in filas)
    sin_asignar = sum(1 for r in filas if not (r["Persona asignada"] or "").strip())
    creadores = Counter(r["Creador"] for r in filas)
    informadores = Counter(r["Informador"] for r in filas)

    print("D6 - RESUMEN DEL BACKLOG DE JIRA")
    print("Fuente:", CSV)
    print("=" * 60)
    print()
    print(f"Total de incidencias en el export: {total}")
    print()

    print("Estado:")
    for estado, n in estados.most_common():
        print(f"  {n:4d}  ({n / total:6.1%})  {estado}")
    print()

    print("Asignacion:")
    print(f"  {sin_asignar:4d}  ({sin_asignar / total:6.1%})  sin persona asignada")
    print(f"  {total - sin_asignar:4d}  ({(total - sin_asignar) / total:6.1%})  con persona asignada")
    print()

    print("Creador:")
    externas = 0
    for quien, n in creadores.most_common():
        marca = "" if quien in INTEGRANTES else "   <- AJENO A AHMRV"
        if quien not in INTEGRANTES:
            externas += n
        print(f"  {n:4d}  ({n / total:6.1%})  {quien}{marca}")
    print()

    print("Informador:")
    for quien, n in informadores.most_common():
        print(f"  {n:4d}  ({n / total:6.1%})  {quien}")
    print()

    print("=" * 60)
    print("LECTURA")
    print(f"  Incidencias sin asignar ni iniciar: {sin_asignar} de {total}")
    print(f"  Incidencias creadas por persona ajena a AHMRV: {externas} de {total}")
    print()
    print("  El backlog documenta la DEFINICION de los elementos de trabajo,")
    print("  no su ejecucion: ninguna incidencia fue asignada ni iniciada.")


if __name__ == "__main__":
    main()
