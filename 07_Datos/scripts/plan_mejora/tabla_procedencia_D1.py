#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
D1 — Tabla de procedencia por requisito.

Extrae, del propio ERS (`\\RF{}`, argumento 4 = «Actor / Origen (evidencia)»),
la procedencia declarada de cada uno de los 42 RF, y la vuelca en una tabla
verificable y reproducible por script. Cada código EV-XX citado se contrasta
contra la lista real de entrevistas presentes en el repositorio: si el ERS
cita una evidencia que no existe, el script lo señala en vez de aceptarla.

No inventa ni corrige nada por sí mismo: si algo no cuadra, lo reporta en la
columna OBSERVACION para que una persona decida.

Uso, desde la raíz del repositorio:

    python3 07_Datos/scripts/plan_mejora/tabla_procedencia_D1.py
"""

import csv
import os
import re

ERS = "01_ERS/ERS_SRS_2B_v2.0.tex"
TRANSCRIPCIONES = "02_Evidencias/Transcripciones"
SALIDA = "07_Datos/datos_procesados/tabla_procedencia_requisitos.csv"

PATRON_EV = re.compile(r"EV-(\d+)")


def extraer_argumentos(texto, inicio, n):
    """Extrae los primeros n argumentos {..} de una macro, balanceando llaves
    anidadas (necesario porque la descripción contiene \\emph{}, \\id{}, etc.)."""
    args = []
    i = inicio
    for _ in range(n):
        while i < len(texto) and texto[i] != "{":
            i += 1
        if i >= len(texto):
            return None
        prof = 1
        j = i + 1
        while j < len(texto) and prof > 0:
            if texto[j] == "{":
                prof += 1
            elif texto[j] == "}":
                prof -= 1
            j += 1
        args.append(texto[i + 1:j - 1])
        i = j
    return args


def encontrar_RF(texto):
    for m in re.finditer(r"\\RF(?=\{)", texto):
        args = extraer_argumentos(texto, m.end(), 4)
        if args:
            yield args


def evidencias_reales():
    """EV-XX que realmente tienen transcripción en el repositorio."""
    reales = set()
    if not os.path.isdir(TRANSCRIPCIONES):
        return reales
    for nombre in os.listdir(TRANSCRIPCIONES):
        m = re.search(r"ENTR-(\d+)", nombre)
        if m:
            reales.add(int(m.group(1)))
    return reales


def main():
    with open(ERS, encoding="utf-8") as f:
        lineas = f.readlines()
    # Descartar comentarios de LaTeX (líneas que empiezan con %, permitiendo
    # espacios previos) para no confundir el comentario de uso de la macro
    # (línea 85: "% Uso: \RF{ID}{Nombre}...") con una invocación real.
    texto = "".join(l for l in lineas if not l.lstrip().startswith("%"))

    reales = evidencias_reales()
    if not reales:
        raise SystemExit(f"ERROR: no se encontraron transcripciones en {TRANSCRIPCIONES}")

    filas = []
    for rf_id, nombre, _desc, origen in encontrar_RF(texto):
        rf_id = rf_id.strip()
        origen = re.sub(r"\s+", " ", origen).strip()

        actor = origen.split("·")[0].strip() if "·" in origen else ""
        codigos = sorted(set(int(x) for x in PATRON_EV.findall(origen)))
        faltantes = [c for c in codigos if c not in reales]

        cita_legal = bool(re.search(r"\\id\{RL-\d+\}", origen))

        observacion = ""
        if not codigos and not cita_legal:
            observacion = "SIN EVIDENCIA NI BASE LEGAL CITADA"
        elif faltantes:
            observacion = "CITA EV-XX SIN TRANSCRIPCIÓN: " + ", ".join(f"EV-{c:02d}" for c in faltantes)

        filas.append({
            "id_requisito": rf_id,
            "nombre": nombre.strip(),
            "actor_declarado": actor,
            "evidencias_citadas": "; ".join(f"EV-{c:02d}" for c in codigos),
            "origen_completo_ers": origen,
            "observacion": observacion,
        })

    if len(filas) != 42:
        print(f"AVISO: se esperaban 42 \\RF{{}} y se extrajeron {len(filas)}. Revisar antes de continuar.")

    os.makedirs(os.path.dirname(SALIDA), exist_ok=True)
    with open(SALIDA, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "id_requisito", "nombre", "actor_declarado",
            "evidencias_citadas", "origen_completo_ers", "observacion",
        ], delimiter=";")
        w.writeheader()
        w.writerows(filas)

    con_obs = [x for x in filas if x["observacion"]]
    print(f"Requisitos extraídos: {len(filas)}")
    print(f"Entrevistas reales detectadas: {sorted(reales)}")
    print(f"Filas con observación: {len(con_obs)}")
    for x in con_obs:
        print(f"  {x['id_requisito']}: {x['observacion']}")
    print(f"\nSalida: {SALIDA}")


if __name__ == "__main__":
    main()
