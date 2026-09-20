#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B5 — Duración real de cada entrevista
Proyecto SIMPA — Equipo AHMRV — ISR-401 — UTEQ

Agrega, por ENTR-XX, la duración de audio y video ya registrada en
fichas_tecnicas.csv (calculada con ffprobe en generar_fichas.py, nunca
inventada). No mide nada por sí mismo — solo agrupa lo ya medido.

Uso:
    python3 duracion_por_entrevista.py 02_Evidencias/00_Restringido/fichas_tecnicas.csv
"""

import csv
import re
import sys
from collections import defaultdict


def main():
    if len(sys.argv) != 2:
        sys.exit("Uso: python3 duracion_por_entrevista.py <fichas_tecnicas.csv>")

    ruta = sys.argv[1]
    with open(ruta, encoding="utf-8-sig") as f:
        filas = list(csv.DictReader(f, delimiter=";"))

    duraciones = defaultdict(lambda: {"audio": 0.0, "video": 0.0})

    for fila in filas:
        tipo = fila.get("tipo", "")
        codigo = fila.get("codigo_participante", "")
        dur_str = fila.get("duracion_segundos", "")
        if tipo not in ("audio", "video") or "ENTR" not in codigo:
            continue
        m = re.search(r"ENTR-\d+", codigo)
        if not m:
            continue
        try:
            dur = float(dur_str)
        except (ValueError, TypeError):
            continue
        duraciones[m.group()][tipo] += dur

    print("| Entrevista | Audio (min) | Video (min) |")
    print("|---|---:|---:|")
    total_video = 0.0
    for entr in sorted(duraciones.keys(), key=lambda x: int(x.split("-")[1])):
        a = duraciones[entr]["audio"]
        v = duraciones[entr]["video"]
        total_video += v
        print(f"| {entr} | {a/60:.1f} | {v/60:.1f} |")

    print()
    print(f"**Total de video: {total_video/60:.1f} minutos ({total_video:.0f} segundos), "
          f"sobre {len(duraciones)} entrevistas.**")
    print(f"Mínimo exigido originalmente por la guía: 240 minutos. "
          f"{'CUMPLE' if total_video/60 >= 240 else 'NO CUMPLE'}.")


if __name__ == "__main__":
    main()
