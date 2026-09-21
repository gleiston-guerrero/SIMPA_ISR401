#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
resolver_C2.py  ·  C2 (y cierre de C1) · SIMPA_ISR401

QUÉ RESUELVE
    Tras reanclar las citas (C1) quedaron 21 fragmentos sin cita. Al buscarles
    respaldo en las 16 transcripciones resultó que:

      · 7 pertenecen a OTRA entrevista (fragmentos cruzados, p. ej. ENTR-06 <-> ENTR-05,
        ENTR-04 -> ENTR-08): se REASIGNAN a su entrevista con cita literal.
      · 5 repiten algo que ya está codificado en la entrevista correcta:
        se RETIRAN como duplicados.
      · 9 no tienen respaldo en la transcripción literal (varios solo existían en la
        versión anterior, no literal, de ENTR-02): se RETIRAN por falta de respaldo.

    Nada se borra sin dejar rastro: los retirados van a
    07_Datos/datos_procesados/fragmentos_retirados_C2.csv (con motivo) y las
    reasignaciones a 07_Datos/resultados/c2_reasignaciones.csv (antes -> después).

    Cada cita nueva se comprueba como subcadena EXACTA de un turno del entrevistado.

USO (desde la raíz del repositorio)
    python3 07_Datos/scripts/plan_mejora/resolver_C2.py --simular
    python3 07_Datos/scripts/plan_mejora/resolver_C2.py
    python3 07_Datos/scripts/plan_mejora/verificar_citas_C1.py
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import citas_lib as L  # noqa: E402

RAIZ = L.RAIZ
CSV_PRINCIPAL = RAIZ / "07_Datos" / "datos_crudos" / "codificacion.csv"
RETIRADOS = RAIZ / "07_Datos" / "datos_procesados" / "fragmentos_retirados_C2.csv"
REASIGNADOS = RAIZ / "07_Datos" / "resultados" / "c2_reasignaciones.csv"

# (fila del CSV, ID_evidencia actual) -> decisión
# REASIGNAR: (entrevista destino, inicio de la cita, fin de la cita)
REASIGNAR = {
    (78, "EV-04"): ("ENTR-08", "En sí, en sí, primero eh revisamos todo", "se elige cierta cantidad."),
    (80, "EV-04"): ("ENTR-08", "Entonces vemos si tiene mayor este sobremaduración", "eso también causa acidez."),
    (82, "EV-04"): ("ENTR-08", "Lo más básico siempre va a ser la mala selección de frutos", "Ese es el único error que cometen."),
    (96, "EV-06"): ("ENTR-05", "eso se lleva un conteo de las flores", "se cuenta por mata"),
    (97, "EV-06"): ("ENTR-05", "Claro, porque ya sé lo que estoy ganándome", "cuánto me sacaría en la quincena."),
    (104, "EV-06"): ("ENTR-05", "Porque eso, o sea, anota el encargado", "cuántos sacamos en la quincena."),
    (105, "EV-06"): ("ENTR-05", "O sea, tenemos días bajos y altos", "según como esté el clima."),
}
# RETIRAR: (fila, ID_evidencia) -> (motivo, detalle)
DUP = "DUPLICADO"
SIN = "SIN_RESPALDO_EN_TRANSCRIPCION_LITERAL"
RETIRAR = {
    (79, "EV-04"): (DUP, "Ya codificado en ENTR-08 como 'El grupo de seleccionadores revisa el fruto despues del pesaje'."),
    (81, "EV-04"): (DUP, "Ya codificado en ENTR-08 como 'Se hace visita tecnica para ver si el problema es de cosecha o de cultivo'."),
    (94, "EV-05"): (DUP, "Ya codificado en ENTR-06 como 'La senal de internet solo llega a la casa, no a todo el cultivo'."),
    (101, "EV-06"): (DUP, "Ya codificado en ENTR-05 como 'El conteo se entrega verbalmente al encargado al final de la jornada'."),
    (106, "EV-06"): (DUP, "Ya codificado en ENTR-05 como 'Al ver una planta enferma se avisa al encargado'."),
    (25, "EV-01"): (SIN, "ENTR-01 no habla de historial de actividades o diagnosticos por lote."),
    (34, "EV-02"): (SIN, "Solo existia en la version del 03/09 de ENTR-02 (no literal); no aparece en la retranscripcion."),
    (41, "EV-02"): (SIN, "Solo existia en la version del 03/09 de ENTR-02 (no literal); no aparece en la retranscripcion."),
    (42, "EV-02"): (SIN, "Solo existia en la version del 03/09 de ENTR-02 (no literal); no aparece en la retranscripcion."),
    (44, "EV-02"): (SIN, "No aparece en la retranscripcion de ENTR-02; su parecido con ENTR-01 es solo general."),
    (45, "EV-02"): (SIN, "No aparece en la retranscripcion de ENTR-02 sobre la forma de pago."),
    (46, "EV-02"): (SIN, "Solo existia en la version del 03/09 de ENTR-02 (no literal); no aparece en la retranscripcion."),
    (60, "EV-03"): (SIN, "ENTR-03 solo pide marcaciones del GPS para el numero de flores; no habla de evitar el registro planta por planta."),
    (118, "EV-07"): (SIN, "ENTR-07 no habla de ver cuanto se trabajo ni cuanto se lleva ganado; ese tema es de ENTR-05."),
}


def leer(ruta):
    b = ruta.read_bytes()
    bom, crlf = b.startswith(b"\xef\xbb\xbf"), b"\r\n" in b[:3000]
    with open(ruta, newline="", encoding="utf-8-sig") as f:
        lector = csv.DictReader(f, delimiter=";")
        return list(lector), list(lector.fieldnames), bom, crlf


def escribir(ruta, filas, campos, bom=True, crlf=False, delim=";"):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with open(ruta, "w", newline="", encoding="utf-8-sig" if bom else "utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos, delimiter=delim, lineterminator="\r\n" if crlf else "\n")
        w.writeheader()
        w.writerows(filas)


def cita_exacta(turnos, ini, fin):
    """Subcadena EXACTA de un turno del entrevistado, de `ini` a `fin`. Devuelve (linea, cita)."""
    for n, linea, off in turnos:
        txt = linea[off:]
        a = txt.find(ini)
        if a < 0:
            continue
        b = txt.find(fin, a)
        if b >= 0:
            return n, txt[a:b + len(fin)].strip()
    raise SystemExit(f"NO se encontró la cita en la transcripción: {ini[:50]}...")


def main(simular):
    filas, campos, bom, crlf = leer(CSV_PRINCIPAL)
    turnos = {f.name.split("_")[1]: (f.name, L.turnos_de_archivo(f))
              for f in L.TRANSCRIPCIONES.glob("2026-*_Transcripcion.md")}
    conservadas, retiradas, reasignadas = [], [], []
    vistos = set()
    for fila in filas:
        clave = (int(fila["linea_csv"]), fila["ID_evidencia"])
        if clave in REASIGNAR:
            vistos.add(clave)
            destino, ini, fin = REASIGNAR[clave]
            nombre, tr = turnos[destino]
            n, cita = cita_exacta(tr, ini, fin)
            reasignadas.append({
                "linea_csv": fila["linea_csv"], "Codigo": fila["Codigo"],
                "Fragmento_parafraseado": fila["Fragmento_parafraseado"],
                "antes_ID_evidencia": fila["ID_evidencia"], "antes_transcripcion": fila["transcripcion"],
                "despues_ID_evidencia": "EV-" + destino[-2:], "despues_transcripcion": nombre,
                "CITA_LITERAL": cita, "LINEA_TRANSCRIPCION": n})
            fila.update({"ID_evidencia": "EV-" + destino[-2:], "transcripcion": nombre,
                         "CITA_LITERAL": cita, "LINEA_TRANSCRIPCION": str(n),
                         "ESTADO": "VER", "REVISOR_CITA": "Claude"})
            conservadas.append(fila)
        elif clave in RETIRAR:
            vistos.add(clave)
            motivo, detalle = RETIRAR[clave]
            retiradas.append({**{k: fila[k] for k in campos}, "motivo_retiro": motivo, "detalle_retiro": detalle})
        else:
            conservadas.append(fila)
    faltan = (set(REASIGNAR) | set(RETIRAR)) - vistos
    if faltan:
        raise SystemExit(f"Filas no encontradas en el CSV: {sorted(faltan)}. ¿Ya se aplicó este script?")

    print(f"Reasignadas: {len(reasignadas)} | Retiradas: {len(retiradas)} "
          f"({sum(r['motivo_retiro'] == DUP for r in retiradas)} duplicados, "
          f"{sum(r['motivo_retiro'] == SIN for r in retiradas)} sin respaldo) | "
          f"Quedan {len(conservadas)} de {len(filas)} en codificacion.csv")
    if simular:
        print("(SIMULACIÓN: no se escribió nada)")
        return
    escribir(CSV_PRINCIPAL, conservadas, campos, bom, crlf)
    escribir(RETIRADOS, retiradas, campos + ["motivo_retiro", "detalle_retiro"])
    escribir(REASIGNADOS, reasignadas, list(reasignadas[0].keys()))
    print("Siguiente paso: python3 07_Datos/scripts/plan_mejora/verificar_citas_C1.py")


if __name__ == "__main__":
    main("--simular" in sys.argv)
