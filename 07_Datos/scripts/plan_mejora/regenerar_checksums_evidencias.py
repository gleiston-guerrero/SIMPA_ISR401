#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Regenera checksums_evidencias.sha256 a partir de fichas_tecnicas.csv.

Tarea G5 del Plan de mejora de los datos del proyecto (19/09/2026).

Por que existe este script
--------------------------
El manifiesto anterior cubria 27 de los 76 originales declarados en
02_Evidencias/00_Restringido/fichas_tecnicas.csv, y 6 de esas 27 lineas
tenian una ruta que no coincide con la que declara el inventario.

No se calcula ningun hash aqui: cada hash se copia de la columna sha256
del propio inventario, que es donde el equipo los registro al inventariar
los originales. Donde el manifiesto anterior ya traia un hash, se comprueba
que coincide con el del inventario; si alguno no coincidiera, el script se
detiene en vez de sobrescribirlo.

Uso, desde la raiz del repositorio:
    python 07_Datos/scripts/plan_mejora/regenerar_checksums_evidencias.py
"""
from __future__ import annotations

import csv
import os
import re
import sys
from collections import OrderedDict, defaultdict

CSV = "02_Evidencias/00_Restringido/fichas_tecnicas.csv"
MAN = "checksums_evidencias.sha256"
LINEA = re.compile(r"^([0-9a-f]{64})\s+\*?(.+)$")


def leer_manifiesto(ruta):
    """Devuelve {ruta_en_contenedor: hash} del manifiesto vigente."""
    previo = OrderedDict()
    if not os.path.exists(ruta):
        return previo
    with open(ruta, encoding="utf-8") as f:
        for linea in f:
            m = LINEA.match(linea.strip())
            if m:
                previo[m.group(2).strip()] = m.group(1)
    return previo


def main():
    if not os.path.exists(CSV):
        sys.exit("ERROR: ejecuta esto desde la raiz del repositorio.")

    with open(CSV, encoding="utf-8-sig", newline="") as f:
        filas = list(csv.DictReader(f, delimiter=";"))

    previo = leer_manifiesto(MAN)
    previo_por_nombre = {os.path.basename(r): h for r, h in previo.items()}

    declarados = OrderedDict()        # ruta -> (hash, contenedor)
    por_contenedor = defaultdict(list)
    conflictos = []

    for fila in filas:
        ruta = fila["ruta_en_contenedor"].strip()
        cont = fila["contenedor"].strip()
        sha = (fila.get("sha256") or "").strip().lower()

        if not re.fullmatch(r"[0-9a-f]{64}", sha):
            sys.exit(f"ERROR: {fila['id_archivo']} no tiene un sha256 valido "
                     f"en el inventario. No se inventa: corrige el CSV.")

        anterior = previo.get(ruta) or previo_por_nombre.get(os.path.basename(ruta))
        if anterior and anterior != sha:
            conflictos.append((ruta, anterior, sha))

        declarados[ruta] = (sha, cont)
        por_contenedor[cont].append(ruta)

    if conflictos:
        print("ERROR: el manifiesto anterior y el inventario discrepan.")
        print("No se sobrescribe nada. Hay que resolverlo a mano:")
        for ruta, viejo, nuevo in conflictos:
            print(f"  {ruta}\n    manifiesto: {viejo}\n    inventario: {nuevo}")
        sys.exit(1)

    # Hashes que ya estaban y que el inventario no declara: no se pierden.
    nombres_csv = {os.path.basename(r) for r in declarados}
    huerfanos = [(r, h) for r, h in previo.items()
                 if os.path.basename(r) not in nombres_csv]

    with open(MAN, "w", encoding="utf-8", newline="\n") as f:
        f.write(CABECERA.format(n_dec=len(declarados),
                                n_cont=len(por_contenedor),
                                n_huer=len(huerfanos)))
        for cont in sorted(por_contenedor):
            f.write(f"\n# --- {cont}\n")
            for ruta in sorted(por_contenedor[cont]):
                f.write(f"{declarados[ruta][0]}  {ruta}\n")

        if huerfanos:
            f.write(HUERFANOS)
            for ruta, h in sorted(huerfanos):
                f.write(f"{h}  {ruta}\n")

    print(f"Originales declarados en el inventario : {len(declarados)}")
    print(f"Contenedores                           : {len(por_contenedor)}")
    print(f"Hashes previos conservados             : "
          f"{sum(1 for r in declarados if os.path.basename(r) in previo_por_nombre)}")
    print(f"Hashes sin declarar en el inventario   : {len(huerfanos)}")
    print(f"Lineas de hash escritas                : {len(declarados) + len(huerfanos)}")
    print(f"Discrepancias manifiesto/inventario    : 0")


CABECERA = """\
# =====================================================================
# checksums_evidencias.sha256
# Proyecto SIMPA - Equipo AHMRV - ISR-401 - UTEQ
# ---------------------------------------------------------------------
# Estos hashes NO corresponden a archivos de este repositorio.
# Corresponden al CONTENIDO INTERNO de los contenedores cifrados .7z
# alojados en el repositorio de evidencias audiovisuales:
#   https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias
#
# Cobertura: {n_dec} originales declarados, repartidos en {n_cont}
# contenedores. Es el total de filas de
# 02_Evidencias/00_Restringido/fichas_tecnicas.csv.
#
# PROCEDENCIA DE LOS HASHES
#   Este archivo se genera con
#     07_Datos/scripts/plan_mejora/regenerar_checksums_evidencias.py
#   que copia la columna sha256 de fichas_tecnicas.csv y la ruta de la
#   columna ruta_en_contenedor. Ningun hash se escribe a mano.
#
#   Los hashes proceden del inventario que el equipo levanto al cifrar
#   los originales; no se han vuelto a calcular sobre los contenedores en
#   esta ronda. El script se detiene si alguno contradice al manifiesto
#   anterior. Al generarse esta version no hubo ninguna contradiccion.
#
# RUTAS
#   Cada ruta es relativa a la raiz de SU contenedor, no a una raiz comun.
#   Dos contenedores distintos pueden empezar por carpetas distintas
#   (`videos/`, `videos 2/`, `Entrevista_09/`): es como estan dentro.
#   Las {n_dec} rutas son distintas entre si, de modo que extraer todos
#   los contenedores en un mismo directorio no solapa ningun archivo.
#
# PROCEDIMIENTO DE VERIFICACION
#   1. Descargar los contenedores indicados en la columna url_release
#      de fichas_tecnicas.csv.
#   2. Descomprimirlos con la contrasena entregada por el SGA, todos
#      sobre el mismo directorio:
#        7z x <contenedor>.7z -o./verificacion
#   3. Situarse en ./verificacion y verificar:
#        sha256sum -c /ruta/al/SIMPA_ISR401/checksums_evidencias.sha256
#      Si solo se descargaron algunos contenedores:
#        sha256sum -c --ignore-missing /ruta/al/SIMPA_ISR401/checksums_evidencias.sha256
#
# DISCREPANCIA DECLARADA (ENTR-03)
#   El inventario declara el video de ENTR-03 como un unico archivo,
#   `videos/Entrevista_03/P03_video_01.mp4`. El manifiesto anterior no lo
#   contenia: contenia en su lugar siete archivos `Parte1..Parte6` y
#   `Proceso_de_polinizacion_antes_de_entrevista.mp4` bajo esa misma
#   carpeta. Ambos juegos de hashes se conservan aqui -los siete, al
#   final, bajo su propio epigrafe- porque resolver cual refleja el
#   contenido real exige abrir el contenedor, y no se ha abierto en esta
#   ronda. Hasta entonces, la verificacion de ENTR-03 se hace con
#   --ignore-missing y la discrepancia queda declarada, no encubierta.
#
# Para verificar los archivos de ESTE repositorio, use checksums.sha256
# desde la raiz del repositorio.
# =====================================================================
"""

HUERFANOS = """
# ---------------------------------------------------------------------
# Hashes presentes en el manifiesto anterior que fichas_tecnicas.csv no
# declara como originales. Se conservan porque son datos reales que el
# equipo ya habia registrado; su incorporacion al inventario queda
# pendiente (ver DISCREPANCIA DECLARADA, arriba).
# ---------------------------------------------------------------------
"""

if __name__ == "__main__":
    main()
