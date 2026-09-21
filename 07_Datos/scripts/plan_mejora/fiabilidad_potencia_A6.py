#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A6 - Fiabilidad y potencia del experimento humano frente a LLM.

El repositorio presentaba la comparacion entre el conjunto humano y el del
LLM como un resultado interpretable. Este script calcula las tres cifras que
determinan si esa interpretacion se sostiene, todas a partir de las
puntuaciones reales:

  1. alfa de Krippendorff ordinal, por dimension  -> acuerdo entre evaluadores
  2. ICC(2,1), por dimension                      -> fiabilidad de una medicion
  3. efecto minimo detectable (d de Cohen)        -> que podia detectar el diseno

El alfa NO se recalcula aqui: se lee de acuerdo_krippendorff.csv, que produce
06_Experimento/scripts_analisis/calcular_acuerdo_evaluadores.py con la libreria
krippendorff 0.8.2. Reimplementarlo daria una segunda cifra para lo mismo, que
es justo lo que este plan corrige. Lo que este script anade es el ICC(2,1) y el
efecto minimo detectable, que no estaban calculados en ninguna parte.

Ninguna cifra se escribe a mano. Si el acuerdo entre evaluadores es nulo, la
diferencia estimada entre los dos conjuntos no puede leerse como un hallazgo
del dominio, y asi se declara.

Uso:
    python3 fiabilidad_potencia_A6.py
"""
import csv, os, sys, collections, math
import numpy as np
from scipy import stats

DATOS  = "07_Datos/datos_procesados/puntuaciones_experimento_con_origen.csv"
ALFAS  = "07_Datos/resultados/acuerdo_krippendorff.csv"
SALIDA = "07_Datos/resultados/fiabilidad_potencia_A6.csv"
INFORME= "07_Datos/resultados/fiabilidad_potencia_A6.txt"

N_POR_GRUPO = 25      # requisitos por conjunto (humano / LLM)
ALFA        = 0.05    # bilateral
POTENCIA    = 0.80

# ---------------------------------------------------------------- datos
filas = list(csv.DictReader(open(DATOS, encoding='utf-8-sig')))
if not filas:
    sys.exit(f"ERROR: {DATOS} vacio")

dims = sorted(set(f['dimension'] for f in filas))
evals = sorted(set(f['evaluador'] for f in filas))
reqs = sorted(set(f['requisito'] for f in filas))

def matriz(dim):
    """requisitos x evaluadores, con NaN donde falte."""
    m = np.full((len(reqs), len(evals)), np.nan)
    ir = {r: i for i, r in enumerate(reqs)}
    ie = {e: i for i, e in enumerate(evals)}
    for f in filas:
        if f['dimension'] == dim:
            m[ir[f['requisito']], ie[f['evaluador']]] = float(f['puntuacion'])
    return m

# --------------------------------- alfa de Krippendorff (leido, no recalculado)
if not os.path.exists(ALFAS):
    sys.exit(f"ERROR: falta {ALFAS}. Ejecuta antes\n"
             f"       python3 06_Experimento/scripts_analisis/calcular_acuerdo_evaluadores.py")
ALFA_DIM = {}
for r in csv.DictReader(open(ALFAS, encoding='utf-8-sig')):
    ALFA_DIM[r['dimension']] = float(r['alpha_krippendorff_ordinal'])

# ------------------------------------------------------------- ICC(2,1)
def icc21(m):
    """ICC(2,1): efectos aleatorios en dos vias, medicion unica, acuerdo absoluto."""
    m = m[~np.isnan(m).any(axis=1)]
    n, k = m.shape
    if n < 2 or k < 2:
        return float('nan')
    gran = m.mean()
    msr = k * ((m.mean(axis=1) - gran) ** 2).sum() / (n - 1)          # entre sujetos
    msc = n * ((m.mean(axis=0) - gran) ** 2).sum() / (k - 1)          # entre evaluadores
    ss_t = ((m - gran) ** 2).sum()
    ss_e = ss_t - (msr * (n - 1)) - (msc * (k - 1))
    mse = ss_e / ((n - 1) * (k - 1))
    den = msr + (k - 1) * mse + k * (msc - mse) / n
    return (msr - mse) / den if den else float('nan')

# ------------------------------------- efecto minimo detectable (2 grupos)
def d_minimo(n_grupo, alfa=ALFA, potencia=POTENCIA):
    """d de Cohen minimo detectable en una prueba t de dos muestras
    independientes, usando la distribucion t no central."""
    gl = 2 * n_grupo - 2
    t_crit = stats.t.ppf(1 - alfa / 2, gl)
    lo, hi = 0.0, 5.0
    for _ in range(200):
        d = (lo + hi) / 2
        nc = d * math.sqrt(n_grupo / 2.0)
        pot = 1 - stats.nct.cdf(t_crit, gl, nc) + stats.nct.cdf(-t_crit, gl, nc)
        if pot < potencia: lo = d
        else: hi = d
    return (lo + hi) / 2

# --------------------------------------------------------------- calculo
res = []
for d in dims:
    m = matriz(d)
    res.append({'dimension': d,
                'alfa_krippendorff_ordinal': round(ALFA_DIM.get(d, float('nan')), 4),
                'icc_2_1': round(icc21(m), 4),
                'n_requisitos': int((~np.isnan(m).any(axis=1)).sum()),
                'n_evaluadores': len(evals)})

dmin = d_minimo(N_POR_GRUPO)

os.makedirs(os.path.dirname(SALIDA), exist_ok=True)
with open(SALIDA, 'w', newline='', encoding='utf-8') as g:
    w = csv.DictWriter(g, fieldnames=list(res[0].keys()))
    w.writeheader(); w.writerows(res)

alfas = [r['alfa_krippendorff_ordinal'] for r in res]
iccs  = [r['icc_2_1'] for r in res]

with open(INFORME, 'w', encoding='utf-8') as g:
    g.write("A6 - Fiabilidad y potencia del experimento humano frente a LLM\n")
    g.write("=" * 62 + "\n\n")
    g.write(f"Fuente de las puntuaciones: {DATOS}\n")
    g.write(f"Fuente del alfa: {ALFAS} (calculado por calcular_acuerdo_evaluadores.py)\n")
    g.write(f"Requisitos: {len(reqs)} ({N_POR_GRUPO} por conjunto) · "
            f"Evaluadores: {len(evals)} · Dimensiones: {len(dims)}\n\n")
    g.write(f"{'Dimension':<12}{'alfa Krippendorff':>20}{'ICC(2,1)':>12}\n")
    g.write("-" * 44 + "\n")
    for r in res:
        g.write(f"{r['dimension']:<12}{r['alfa_krippendorff_ordinal']:>20.4f}"
                f"{r['icc_2_1']:>12.4f}\n")
    g.write("-" * 44 + "\n")
    g.write(f"{'rango':<12}{min(alfas):>9.4f} a {max(alfas):<8.4f}"
            f"{min(iccs):>6.4f} a {max(iccs):.4f}\n\n")
    g.write(f"Efecto minimo detectable con {N_POR_GRUPO} por grupo,\n")
    g.write(f"alfa = {ALFA} bilateral y potencia = {POTENCIA}:  d = {dmin:.2f}\n\n")
    g.write("Lectura\n-------\n")
    g.write("El alfa de Krippendorff mide cuanto coinciden los evaluadores mas alla\n")
    g.write("del azar: 0 significa que no coinciden mas que al azar. El ICC(2,1) mide\n")
    g.write("que parte de la variacion observada corresponde al requisito evaluado y\n")
    g.write("no a quien lo evalua.\n\n")
    g.write(f"Con un alfa entre {min(alfas):.3f} y {max(alfas):.3f} y un ICC entre\n")
    g.write(f"{min(iccs):.2f} y {max(iccs):.2f}, la puntuacion de un requisito depende\n")
    g.write("mas de quien la asigna que del requisito. La medicion no es fiable, y una\n")
    g.write("diferencia estimada sobre ella no puede leerse como una propiedad de los\n")
    g.write("requisitos.\n\n")
    g.write(f"El diseno solo podia detectar diferencias de d = {dmin:.2f} o mayores, que\n")
    g.write("es un efecto grande. No encontrar diferencia significativa era el\n")
    g.write("resultado esperable con esta muestra, y no es evidencia de equivalencia.\n")

print(f"Dimensiones: {len(dims)} | requisitos: {len(reqs)} | evaluadores: {len(evals)}")
print(f"alfa de Krippendorff: {min(alfas):.4f} a {max(alfas):.4f}")
print(f"ICC(2,1):             {min(iccs):.4f} a {max(iccs):.4f}")
print(f"Efecto minimo detectable ({N_POR_GRUPO} por grupo, alfa {ALFA}, potencia {POTENCIA}): d = {dmin:.2f}")
print(f"\nEscrito: {SALIDA}\n         {INFORME}")
