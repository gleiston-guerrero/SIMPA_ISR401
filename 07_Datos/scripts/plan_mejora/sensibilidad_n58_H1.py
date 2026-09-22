#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H1 — Análisis de sensibilidad n=62 vs n=58 del cuestionario al personal operativo.

Calcula las estadísticas descriptivas de las 15 preguntas del cuestionario
dos veces: sobre las 62 respuestas totales y sobre las 58 de la ronda
ampliada (excluyendo las 4 del piloto del 30/06/2026), y las compara.

Parte SIEMPRE de `respuestas_anonimizadas.csv` (nunca del .xlsx crudo, que
contiene correo y nombre — ver 02_Evidencias/Cuestionario/Respuestas/readme.md).

Preguntas categóricas: se reporta la distribución en % sobre el total de esa
base (no sobre 100, por si hay respuestas en blanco).
Preguntas de escala 1-5: se reporta media, desviación estándar y n de
respuestas válidas (excluye vacíos, sin inventar un valor).

Uso, desde la raíz del repositorio:

    python3 07_Datos/scripts/plan_mejora/sensibilidad_n58_H1.py
"""

import csv
import statistics

CSV = "07_Datos/datos_procesados/respuestas_anonimizadas.csv"
SALIDA = "07_Datos/resultados/sensibilidad_n58_H1.md"
FECHA_PILOTO = "2026-06-30"

# Preguntas de escala 1-5 (por posición de columna, 0-indexado, según el CSV)
COLS_ESCALA = [16, 20, 22, 24, 26, 28]
# Preguntas categóricas
COLS_CATEGORICA = [4, 6, 8, 10, 12, 14, 18, 30, 32]


def cargar():
    with open(CSV, encoding="utf-8-sig", newline="") as f:
        lector = csv.reader(f)
        cabecera = next(lector)
        filas = list(lector)
    return cabecera, filas


def es_piloto(fila):
    return fila[1][:10] == FECHA_PILOTO


def limpio(v):
    v = (v or "").strip()
    return v if v else None


def stats_categorica(filas, col):
    valores = [limpio(f[col]) for f in filas]
    validos = [v for v in valores if v is not None]
    from collections import Counter
    c = Counter(validos)
    n = len(validos)
    return n, c


def stats_escala(filas, col):
    valores = []
    for f in filas:
        v = limpio(f[col])
        if v is None:
            continue
        try:
            valores.append(float(v))
        except ValueError:
            continue
    if not valores:
        return 0, None, None
    media = statistics.mean(valores)
    de = statistics.stdev(valores) if len(valores) > 1 else 0.0
    return len(valores), media, de


def main():
    cabecera, filas = cargar()
    n_pilotos = sum(1 for f in filas if es_piloto(f))
    todas = filas
    ampliada = [f for f in filas if not es_piloto(f)]

    assert len(todas) == 62, f"se esperaban 62 filas totales, hay {len(todas)}"
    assert n_pilotos == 4, f"se esperaban 4 respuestas piloto, hay {n_pilotos}"
    assert len(ampliada) == 58, f"se esperaban 58 en la ronda ampliada, hay {len(ampliada)}"

    out = []
    out.append("# H1 — Análisis de sensibilidad n=62 vs n=58\n")
    out.append(
        f"Calculado desde `{CSV}` (62 filas), separando por fecha de "
        f"`Hora de inicio`: **n=62** son todas las respuestas; **n=58** "
        f"excluye las 4 del piloto del {FECHA_PILOTO}. Regenerar con:\n"
    )
    out.append("    python3 07_Datos/scripts/plan_mejora/sensibilidad_n58_H1.py\n")
    out.append("---\n")

    out.append("## Preguntas de escala 1 a 5 (media · desviación estándar · n válido)\n")
    out.append("| Pregunta | Media (n=62) | DE (n=62) | Media (n=58) | DE (n=58) | Diferencia de medias |")
    out.append("|---|---:|---:|---:|---:|---:|")
    max_dif_escala = 0.0
    for col in COLS_ESCALA:
        pregunta = cabecera[col].replace("\xa0", " ").strip()
        n62, m62, de62 = stats_escala(todas, col)
        n58, m58, de58 = stats_escala(ampliada, col)
        dif = abs(m62 - m58) if (m62 is not None and m58 is not None) else None
        if dif is not None:
            max_dif_escala = max(max_dif_escala, dif)
        pregunta_corta = pregunta[:70] + ("…" if len(pregunta) > 70 else "")
        out.append(
            f"| {pregunta_corta} | {m62:.2f} | {de62:.2f} | {m58:.2f} | {de58:.2f} | {dif:.2f} |"
        )
    out.append("")

    out.append("## Preguntas categóricas (% sobre las respuestas válidas de cada base)\n")
    max_dif_pct = 0.0
    for col in COLS_CATEGORICA:
        pregunta = cabecera[col].replace("\xa0", " ").strip()
        n62, c62 = stats_categorica(todas, col)
        n58, c58 = stats_categorica(ampliada, col)
        opciones = sorted(set(c62) | set(c58))
        out.append(f"### {pregunta}\n")
        out.append(f"n=62: {n62} respuestas válidas · n=58: {n58} respuestas válidas\n")
        out.append("| Opción | % (n=62) | % (n=58) | Diferencia (pp) |")
        out.append("|---|---:|---:|---:|")
        for op in opciones:
            p62 = 100 * c62.get(op, 0) / n62 if n62 else 0
            p58 = 100 * c58.get(op, 0) / n58 if n58 else 0
            dif = abs(p62 - p58)
            max_dif_pct = max(max_dif_pct, dif)
            out.append(f"| {op} | {p62:.1f} % | {p58:.1f} % | {dif:.1f} |")
        out.append("")

    out.append("## Conclusión del análisis de sensibilidad\n")
    out.append(
        f"Mayor diferencia de medias observada en las preguntas de escala: "
        f"**{max_dif_escala:.2f} puntos** (escala 1-5).\n"
    )
    out.append(
        f"Mayor diferencia porcentual observada en las preguntas categóricas: "
        f"**{max_dif_pct:.1f} puntos porcentuales**.\n"
    )
    out.append(
        "Ninguna cifra de este documento se escribió a mano: todas salen de "
        "la ejecución del script arriba indicado sobre "
        "`respuestas_anonimizadas.csv`.\n"
    )

    with open(SALIDA, "w", encoding="utf-8") as f:
        f.write("\n".join(out))

    print(f"n=62 (todas): {len(todas)} filas")
    print(f"n=58 (ampliada, sin piloto): {len(ampliada)} filas")
    print(f"Mayor diferencia de medias (escala 1-5): {max_dif_escala:.2f}")
    print(f"Mayor diferencia porcentual (categóricas): {max_dif_pct:.1f} pp")
    print(f"Salida: {SALIDA}")


if __name__ == "__main__":
    main()
