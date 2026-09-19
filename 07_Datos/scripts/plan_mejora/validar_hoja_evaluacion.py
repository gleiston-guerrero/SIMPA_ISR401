#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A1 — Validación de hojas de puntuación.

Comprueba una hoja de evaluación contra los cuatro criterios objetivos que el
docente exige en A1. Está pensado para ejecutarse EN EL MOMENTO en que el
evaluador entrega la hoja, mientras todavía está disponible para repetir o
aclarar lo que haga falta.

Criterios verificados:

  C1  Sin periodicidad por posición.
      Para cada periodo p de 2 a 10, la coincidencia entre filas separadas por
      p posiciones debe ser INFERIOR al 80 %. Una coincidencia alta delata un
      patrón mecánico en vez de un juicio requisito por requisito.

  C2  COM distinta de CON en al menos el 20 % de las filas.
      Si completitud y consistencia reciben siempre el mismo valor, no se
      están puntuando como dimensiones independientes.

  C3  Cada término citado en un comentario aparece en su requisito.
      Un comentario que menciona términos ausentes del requisito indica que no
      se leyó ese requisito.

  C4  Fecha de la hoja posterior al archivo cegado.

Uso, desde la raíz del repositorio:

    python3 07_Datos/scripts/plan_mejora/validar_hoja_evaluacion.py <hoja.csv>

Para revisar todas las hojas de una vez:

    python3 07_Datos/scripts/plan_mejora/validar_hoja_evaluacion.py \
        06_Experimento/evaluadores/EV-*.csv

Código de salida 0 si todas las hojas pasan; 1 si alguna falla.
"""

import csv
import glob
import os
import re
import sys
import unicodedata

CEGADO = os.path.join("06_Experimento", "cegado", "requisitos_cegados.csv")
DIMENSIONES = ["COM", "AMB", "VER", "COR", "CON"]

UMBRAL_PERIODICIDAD = 0.80   # coincidencia máxima tolerada, periodos 2..10
UMBRAL_COM_CON = 0.20        # proporción mínima de filas con COM != CON
MIN_LONG_TERMINO = 5         # longitud mínima para considerar un token


def normaliza(texto):
    """Minúsculas y sin tildes, para comparar términos de forma robusta."""
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def carga_cegado():
    if not os.path.exists(CEGADO):
        sys.exit(f"ERROR: no se encontró '{CEGADO}'. Ejecute desde la raíz del repositorio.")
    requisitos = {}
    with open(CEGADO, encoding="utf-8-sig", newline="") as f:
        for fila in csv.DictReader(f, delimiter=";"):
            texto = " ".join(v or "" for k, v in fila.items() if k != "id_cegado")
            requisitos[fila["id_cegado"]] = normaliza(texto)
    return requisitos


def carga_hoja(ruta):
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        filas = list(csv.DictReader(f, delimiter=";"))
    if not filas:
        sys.exit(f"ERROR: '{ruta}' no contiene filas.")
    faltan = [d for d in DIMENSIONES if d not in filas[0]]
    if faltan:
        sys.exit(f"ERROR: a '{ruta}' le faltan las columnas: {', '.join(faltan)}")
    return filas


def c1_periodicidad(filas):
    """Coincidencia entre filas separadas por p posiciones, para p de 2 a 10."""
    vectores = [tuple(f[d] for d in DIMENSIONES) for f in filas]
    n = len(vectores)
    resultados = []
    peor = 0.0
    for p in range(2, 11):
        pares = n - p
        if pares <= 0:
            continue
        iguales = sum(1 for i in range(pares) if vectores[i] == vectores[i + p])
        ratio = iguales / pares
        peor = max(peor, ratio)
        resultados.append((p, iguales, pares, ratio))
    return resultados, peor


def c2_com_distinta_con(filas):
    distintas = sum(1 for f in filas if (f["COM"] or "") != (f["CON"] or ""))
    return distintas, len(filas), distintas / len(filas)


def c3_terminos(filas, requisitos):
    """Términos de cada comentario que no aparecen en su propio requisito."""
    hallazgos = []
    for f in filas:
        comentario = (f.get("observaciones") or "").strip().strip('"')
        if not comentario:
            continue
        rid = f["id_requisito"]
        texto_req = requisitos.get(rid)
        if texto_req is None:
            hallazgos.append((rid, ["(id ausente del archivo cegado)"]))
            continue
        tokens = re.findall(r"[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+", comentario)
        ausentes = []
        for t in tokens:
            if len(t) < MIN_LONG_TERMINO:
                continue
            tn = normaliza(t)
            # se ignora el vocabulario genérico de la propia rúbrica
            if tn in {"requisito", "sistema", "falta", "faltan", "debe", "deberia",
                      "especificar", "formato", "exacto", "esperada", "esperado",
                      "salida", "entrada", "criterio", "verificacion", "ambiguo",
                      "ambigua", "claro", "clara", "completo", "completa"}:
                continue
            if tn not in texto_req:
                ausentes.append(t)
        if ausentes:
            hallazgos.append((rid, ausentes))
    return hallazgos


def c4_fecha(ruta):
    """Compara la fecha de modificación de la hoja con la del archivo cegado."""
    if not os.path.exists(CEGADO):
        return None
    return os.path.getmtime(ruta), os.path.getmtime(CEGADO)


def valida(ruta, requisitos):
    print("=" * 70)
    print("HOJA:", ruta)
    print("=" * 70)
    filas = carga_hoja(ruta)
    print(f"Filas: {len(filas)}")
    print()
    ok = True

    # C1
    resultados, peor = c1_periodicidad(filas)
    print(f"C1 · Periodicidad por posición (umbral < {UMBRAL_PERIODICIDAD:.0%})")
    for p, iguales, pares, ratio in resultados:
        marca = "  <-- FALLA" if ratio >= UMBRAL_PERIODICIDAD else ""
        print(f"     periodo {p:2d}:  {iguales:3d}/{pares:3d}  = {ratio:6.1%}{marca}")
    if peor >= UMBRAL_PERIODICIDAD:
        print(f"     RESULTADO: FALLA — coincidencia máxima {peor:.1%}")
        ok = False
    else:
        print(f"     RESULTADO: pasa — coincidencia máxima {peor:.1%}")
    print()

    # C2
    distintas, total, ratio = c2_com_distinta_con(filas)
    print(f"C2 · COM distinta de CON (umbral >= {UMBRAL_COM_CON:.0%})")
    print(f"     {distintas}/{total} filas = {ratio:.1%}")
    if ratio < UMBRAL_COM_CON:
        print("     RESULTADO: FALLA")
        ok = False
    else:
        print("     RESULTADO: pasa")
    print()

    # C3
    hallazgos = c3_terminos(filas, requisitos)
    print("C3 · Términos del comentario presentes en su requisito")
    if hallazgos:
        for rid, ausentes in hallazgos[:15]:
            print(f"     {rid}: términos ausentes -> {', '.join(ausentes)}")
        if len(hallazgos) > 15:
            print(f"     ... y {len(hallazgos) - 15} comentario(s) más")
        print(f"     RESULTADO: FALLA — {len(hallazgos)} comentario(s) con términos ajenos")
        ok = False
    else:
        print("     RESULTADO: pasa")
    print()

    # C4
    fechas = c4_fecha(ruta)
    print("C4 · Fecha de la hoja posterior al archivo cegado")
    if fechas is None:
        print("     RESULTADO: no verificable (falta el archivo cegado)")
        ok = False
    else:
        t_hoja, t_cegado = fechas
        import datetime as dt
        print(f"     cegado: {dt.datetime.fromtimestamp(t_cegado):%Y-%m-%d %H:%M}")
        print(f"     hoja  : {dt.datetime.fromtimestamp(t_hoja):%Y-%m-%d %H:%M}")
        print("     AVISO: la marca de tiempo del sistema de archivos no se")
        print("     conserva en git. El criterio se acredita con la fecha y hora")
        print("     de exportación declarada por el evaluador y con la fecha del")
        print("     commit en que se sube la hoja, no con este dato.")
    print()

    print("VEREDICTO:", "PASA" if ok else "NO PASA")
    print()
    return ok


def main():
    argumentos = sys.argv[1:]
    if not argumentos:
        sys.exit(__doc__)

    rutas = []
    for a in argumentos:
        expandido = glob.glob(a)
        rutas.extend(expandido if expandido else [a])

    requisitos = carga_cegado()
    todas_ok = True
    for ruta in sorted(rutas):
        if not os.path.exists(ruta):
            print(f"ERROR: no existe '{ruta}'")
            todas_ok = False
            continue
        if not valida(ruta, requisitos):
            todas_ok = False

    print("=" * 70)
    print("RESULTADO GLOBAL:", "todas las hojas pasan" if todas_ok else "hay hojas que NO pasan")
    sys.exit(0 if todas_ok else 1)


if __name__ == "__main__":
    main()
