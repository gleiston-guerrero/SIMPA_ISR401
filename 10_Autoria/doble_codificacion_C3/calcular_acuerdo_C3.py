#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
calcular_acuerdo_C3.py  ·  C3 · SIMPA_ISR401

Calcula el acuerdo entre codificadores de la doble codificación REAL (C3).

Lee, de esta misma carpeta, todos los archivos  codificacion_C3_*.xlsx  (o .csv) y compara:
    · cada par de personas que codificaron (acuerdo observado, kappa de Cohen, IC 95 %
      por bootstrap con semilla fija);
    · cada persona contra la codificación ORIGINAL del equipo (la de codificacion.csv).
Además escribe la tabla de desacuerdos y comprueba las reglas de C3:
    · cada archivo lo subió una sola cuenta de git, y no la misma que otro archivo;
    · las respuestas están dentro del libro de códigos (95 códigos) y completas.

USO (desde la raíz del repositorio; requiere numpy y openpyxl)
    python3 10_Autoria/doble_codificacion_C3/calcular_acuerdo_C3.py
Salidas: resultado_acuerdo_C3.txt · resultado_acuerdo_C3.csv · desacuerdos_C3.csv
"""
import csv
import itertools
import random
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

CARPETA = Path(__file__).resolve().parent
RAIZ = CARPETA.parents[1]
sys.path.insert(0, str(CARPETA))
import preparar_muestra_C3 as M  # noqa: E402  (misma muestra, misma semilla)

BOOT, SEMILLA_BOOT = 2000, 20260921


def kappa(a, b):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[k] * cb.get(k, 0) for k in ca) / (n * n)
    return po, (1.0 if pe == 1 else (po - pe) / (1 - pe))


def kappa_ic(a, b):
    rng = random.Random(SEMILLA_BOOT)
    n, ks = len(a), []
    for _ in range(BOOT):
        idx = [rng.randrange(n) for _ in range(n)]
        ks.append(kappa([a[i] for i in idx], [b[i] for i in idx])[1])
    ks.sort()
    return ks[int(0.025 * BOOT)], ks[int(0.975 * BOOT) - 1]


def leer(ruta):
    """{ID_fragmento: (codigo, codificador)}"""
    if ruta.suffix.lower() == ".xlsx":
        from openpyxl import load_workbook
        ws = load_workbook(ruta, data_only=True)["Codificar"]
        cab = [c.value for c in ws[1]]
        filas = [dict(zip(cab, r)) for r in ws.iter_rows(min_row=2, values_only=True)]
    else:
        with open(ruta, newline="", encoding="utf-8-sig") as f:
            filas = list(csv.DictReader(f, delimiter=";"))
    return {r["ID_fragmento"]: ((r.get("CODIGO") or "").strip(), (r.get("CODIFICADOR") or "").strip()) for r in filas}


def autores_git(ruta):
    try:
        out = subprocess.run(["git", "log", "--format=%an", "--", str(ruta.relative_to(RAIZ))],
                             capture_output=True, text=True, cwd=RAIZ).stdout.split()
        return sorted(set(out))
    except Exception:
        return []


def main():
    sel = M.muestra_congelada()   # la muestra CONGELADA en muestra_C3_fragmentos.csv
    ids = [i for i, _ in sel]
    original = {i: r["Codigo"].strip() for i, r in sel}
    validos = {c[1] for c in M.cargar_libro()}
    archivos = sorted(list(CARPETA.glob("codificacion_C3_*.xlsx")) + list(CARPETA.glob("codificacion_C3_*.csv")))
    if not archivos:
        sys.exit("No hay archivos codificacion_C3_*.xlsx en la carpeta.")
    coders, lineas, problemas = {}, [], []
    lineas.append(f"C3 · muestra de {len(ids)} fragmentos (semilla {M.SEMILLA}); archivos: {', '.join(a.name for a in archivos)}")
    for a in archivos:
        d = leer(a)
        nombre = a.stem.replace("codificacion_C3_", "")
        if set(d) != set(ids):
            problemas.append(f"{a.name}: los IDs no coinciden con la muestra congelada")
            continue
        vacios = [i for i in ids if not d[i][0]]
        fuera = [i for i in ids if d[i][0] and d[i][0] not in validos]
        if vacios:
            problemas.append(f"{a.name}: {len(vacios)} fragmentos sin código")
        if fuera:
            problemas.append(f"{a.name}: {len(fuera)} códigos fuera del libro ({', '.join(fuera[:3])}...)")
        aut = autores_git(a)
        lineas.append(f"  {a.name}: codificador declarado = {sorted({v[1] for v in d.values() if v[1]})}; autores git = {aut}")
        if aut and len(aut) != 1:
            problemas.append(f"{a.name}: lo tocaron varias cuentas de git {aut}")
        coders[nombre] = ({i: d[i][0] for i in ids}, aut)
    autores = [tuple(c[1]) for c in coders.values() if c[1]]
    if len(set(autores)) != len(autores):
        problemas.append("Dos archivos comparten la misma cuenta de git: no es doble codificación independiente.")

    filas_res, desac = [], []
    pares = [(a, b) for a, b in itertools.combinations(coders, 2)] + [(a, "ORIGINAL") for a in coders]
    for a, b in pares:
        va = [coders[a][0][i] for i in ids]
        vb = [original[i] for i in ids] if b == "ORIGINAL" else [coders[b][0][i] for i in ids]
        po, k = kappa(va, vb)
        lo, hi = kappa_ic(va, vb)
        filas_res.append([a, b, len(ids), round(po, 3), round(k, 3), round(lo, 3), round(hi, 3)])
        lineas.append(f"  {a} vs {b}: acuerdo observado {po:.1%} · kappa {k:.3f} (IC 95 % {lo:.3f} a {hi:.3f})")
        for i, x, y in zip(ids, va, vb):
            if x != y:
                desac.append([a, b, i, x, y])
    with open(CARPETA / "resultado_acuerdo_C3.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["codificador_A", "codificador_B", "n", "acuerdo_observado", "kappa", "ic95_bajo", "ic95_alto"])
        w.writerows(filas_res)
    with open(CARPETA / "desacuerdos_C3.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["codificador_A", "codificador_B", "ID_fragmento", "codigo_A", "codigo_B"])
        w.writerows(desac)
    lineas.append(f"  desacuerdos registrados: {len(desac)} (ver desacuerdos_C3.csv)")
    lineas.append("Limitación: 95 códigos y solo 45 fragmentos: el kappa es inestable; interpretar con el IC 95 %.")
    lineas += [f"PROBLEMA: {p}" for p in problemas] or ["Reglas de C3: sin problemas detectados."]
    (CARPETA / "resultado_acuerdo_C3.txt").write_text("\n".join(lineas) + "\n", encoding="utf-8")
    print("\n".join(lineas))


if __name__ == "__main__":
    main()
