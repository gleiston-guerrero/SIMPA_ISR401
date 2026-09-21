#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
saturacion_orden_C4.py  ·  C4 · SIMPA_ISR401

Criterio de C4: "Media y probabilidad de cero códigos nuevos en la última posición,
por script" (saturación con sensibilidad al orden).

Qué hace
    Los códigos que aporta cada entrevista salen de los dos CSV de codificación.
    Se reordenan las 16 entrevistas al azar N veces (semilla declarada) y, en cada
    orden, se cuenta cuántos códigos NUEVOS aparece en cada posición. Así se ve si la
    "saturación" (que la última entrevista no aporte nada nuevo) depende del orden
    real en que se hicieron las entrevistas o se mantiene con cualquier orden.

Salidas
    07_Datos/resultados/c4_saturacion_orden.txt
    07_Datos/resultados/c4_saturacion_orden.csv

USO (desde la raíz del repositorio)
    python3 07_Datos/scripts/plan_mejora/saturacion_orden_C4.py            # 10 000 órdenes
    python3 07_Datos/scripts/plan_mejora/saturacion_orden_C4.py --n 50000 --semilla 7
"""
import argparse
import csv
import random
import re
import statistics as st
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
ARCHIVOS = [RAIZ / "07_Datos" / "datos_crudos" / "codificacion.csv",
            RAIZ / "07_Datos" / "datos_procesados" / "codificacion_tercera_ronda.csv"]
SALIDA_TXT = RAIZ / "07_Datos" / "resultados" / "c4_saturacion_orden.txt"
SALIDA_CSV = RAIZ / "07_Datos" / "resultados" / "c4_saturacion_orden.csv"


def codigos_por_entrevista():
    por = defaultdict(set)
    for ruta in ARCHIVOS:
        with open(ruta, newline="", encoding="utf-8-sig") as f:
            for fila in csv.DictReader(f, delimiter=";"):
                por[re.search(r"ENTR-\d+", fila["transcripcion"]).group(0)].add(fila["Codigo"].strip())
    return dict(sorted(por.items()))


def nuevos_por_posicion(orden, por):
    vistos, salida = set(), []
    for e in orden:
        nuevos = por[e] - vistos
        salida.append(len(nuevos))
        vistos |= nuevos
    return salida


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=10000)
    ap.add_argument("--semilla", type=int, default=20260921)
    a = ap.parse_args()

    por = codigos_por_entrevista()
    entrevistas = list(por)
    total = len(set().union(*por.values()))
    k = len(entrevistas)

    real = nuevos_por_posicion(entrevistas, por)
    rng = random.Random(a.semilla)
    acum = [[] for _ in range(k)]
    ult_cero = ult2_cero = 0
    for _ in range(a.n):
        orden = entrevistas[:]
        rng.shuffle(orden)
        n = nuevos_por_posicion(orden, por)
        for i, v in enumerate(n):
            acum[i].append(v)
        ult_cero += n[-1] == 0
        ult2_cero += n[-1] == 0 and n[-2] == 0

    filas = [["posicion", "nuevos_orden_real", "media_nuevos_aleatorio", "p5", "p95",
              "prob_cero_nuevos"]]
    for i in range(k):
        v = sorted(acum[i])
        filas.append([i + 1, real[i], round(st.mean(v), 2), v[int(0.05 * len(v))], v[int(0.95 * len(v)) - 1],
                      round(sum(x == 0 for x in v) / len(v), 3)])
    SALIDA_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(SALIDA_CSV, "w", newline="", encoding="utf-8") as f:
        csv.writer(f, delimiter=";").writerows(filas)

    p_ult, p_ult2 = ult_cero / a.n, ult2_cero / a.n
    txt = [
        "C4 · Saturación de códigos con sensibilidad al orden",
        f"Entrevistas: {k} · códigos distintos: {total} · órdenes aleatorios: {a.n} · semilla: {a.semilla}",
        "",
        f"Orden real: códigos nuevos por entrevista = {real}",
        f"Orden real: la última entrevista ({entrevistas[-1]}) aporta {real[-1]} códigos nuevos.",
        "",
        f"Media de códigos nuevos en la ÚLTIMA posición (órdenes al azar): {st.mean(acum[-1]):.2f}",
        f"Probabilidad de CERO códigos nuevos en la última posición: {p_ult:.1%}",
        f"Probabilidad de cero códigos nuevos en las DOS últimas posiciones: {p_ult2:.1%}",
        "",
        "Lectura: si esa probabilidad es baja, decir que hubo 'saturación' depende del orden en que se",
        "hicieron las entrevistas y no debe presentarse como un hallazgo firme.",
    ]
    SALIDA_TXT.write_text("\n".join(txt) + "\n", encoding="utf-8")
    print("\n".join(txt))


if __name__ == "__main__":
    main()
