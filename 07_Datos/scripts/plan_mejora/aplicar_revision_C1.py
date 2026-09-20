#!/usr/bin/env python3
"""
aplicar_revision_C1.py  ·  C1 · SIMPA_ISR401

PROPÓSITO
    Pasar a los CSV de codificación el resultado de la revisión humana de citas
    (hoja exportada como CSV desde revision_citas_C1.xlsx), aceptando SOLO lo
    que se puede comprobar:

      · DECISION = LITERAL        -> CITA_ELEGIDA debe ser una subcadena EXACTA
                                     de una intervención del entrevistado en la
                                     transcripción de esa fila. El número de
                                     línea lo calcula este script.
      · DECISION = NO_LOCALIZADA  -> no se inventa texto: se deja constancia.
      · cualquier otra cosa       -> la fila queda PENDIENTE_REVISION.

    Nunca se escribe una cita que no se haya encontrado literalmente.

USO (desde la raíz del repositorio)
    python3 07_Datos/scripts/plan_mejora/aplicar_revision_C1.py ruta/revision_citas_C1.csv

    Añadir --simular para ver el resultado sin modificar ningún archivo.
"""
import csv
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
TRANSCRIPCIONES = RAIZ / "02_Evidencias" / "Transcripciones"
ARCHIVOS_CSV = {
    "codificacion.csv": RAIZ / "07_Datos" / "datos_crudos" / "codificacion.csv",
    "codificacion_tercera_ronda.csv": RAIZ / "07_Datos" / "datos_procesados" / "codificacion_tercera_ronda.csv",
}
ETIQUETA = "**Entrevistado:**"
NUEVAS = ["REVISOR_CITA"]


def leer_revision(ruta):
    crudo = ruta.read_bytes().decode("utf-8-sig", errors="replace")
    delim = max([";", ",", "\t"], key=lambda d: crudo.split("\n", 1)[0].count(d))
    return list(csv.DictReader(crudo.splitlines(), delimiter=delim))


def turnos_de_entrevistado(texto):
    """
    Devuelve [(numero_de_linea, linea, offset)] de todo lo que dice el ENTREVISTADO.
    Un turno puede tener varios párrafos: una línea sin etiqueta continúa al último
    hablante. `offset` es el largo de la etiqueta (0 en los párrafos de continuación).
    """
    salida, hablante = [], None
    for n, linea in enumerate(texto.splitlines(), start=1):
        if linea.startswith("**Entrevistado:**"):
            hablante = "E"
            salida.append((n, linea, len("**Entrevistado:**")))
        elif linea.startswith("**Entrevistador:**"):
            hablante = "R"
        elif linea.startswith("#") or linea.startswith("**Rol:**"):
            hablante = None
        elif linea.strip() and hablante == "E":
            salida.append((n, linea, 0))
    return salida


def lineas_entrevistado(nombre, cache):
    if nombre not in cache:
        texto = (TRANSCRIPCIONES / nombre).read_text(encoding="utf-8", errors="ignore")
        cache[nombre] = turnos_de_entrevistado(texto)
    return cache[nombre]


def localizar(cita, nombre, linea_indicada, cache):
    """Devuelve el número de línea donde la cita aparece EXACTA en boca del entrevistado, o None."""
    if not cita:
        return None
    turnos = lineas_entrevistado(nombre, cache)
    if str(linea_indicada).strip().isdigit():
        for n, l, off in turnos:
            if n == int(linea_indicada) and cita in l[off:]:
                return n
    for n, l, off in turnos:
        if cita in l[off:]:
            return n
    return None


def leer_csv_codificacion(ruta):
    b = ruta.read_bytes()
    bom = b.startswith(b"\xef\xbb\xbf")
    crlf = b"\r\n" in b[:3000]
    with open(ruta, newline="", encoding="utf-8-sig") as f:
        lector = csv.DictReader(f, delimiter=";")
        return list(lector), list(lector.fieldnames), bom, crlf


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    simular = "--simular" in sys.argv
    if not args:
        sys.exit(__doc__)
    revision = leer_revision(Path(args[0]))
    por_clave = {(r["Archivo_CSV"].strip(), str(r["Fila_CSV"]).strip()): r for r in revision}

    cache, resumen, errores = {}, {"LITERAL": 0, "NO_LOCALIZADA": 0, "PENDIENTE_REVISION": 0}, []
    for nombre, ruta in ARCHIVOS_CSV.items():
        filas, campos, bom, crlf = leer_csv_codificacion(ruta)
        for c in NUEVAS:
            if c not in campos:
                campos.append(c)
        for fila in filas:
            rev = por_clave.get((nombre, str(fila["linea_csv"]).strip()))
            decision = (rev.get("DECISION", "") if rev else "").strip().upper()
            fila["CITA_LITERAL"], fila["LINEA_TRANSCRIPCION"], fila["ESTADO"] = "", "", "PENDIENTE_REVISION"
            fila["REVISOR_CITA"] = (rev.get("Revisor", "") if rev else "").strip()
            if decision == "LITERAL":
                cita = rev.get("CITA_ELEGIDA", "").strip()
                n = localizar(cita, fila["transcripcion"], rev.get("LINEA_ELEGIDA", ""), cache)
                if n is None:
                    errores.append(f"{nombre} fila {fila['linea_csv']} ({fila['ID_evidencia']}): "
                                   f"la cita NO aparece literal en boca del entrevistado -> queda PENDIENTE_REVISION")
                else:
                    fila["CITA_LITERAL"], fila["LINEA_TRANSCRIPCION"], fila["ESTADO"] = cita, str(n), "VER"
                    resumen["LITERAL"] += 1
                    continue
            elif decision == "NO_LOCALIZADA":
                fila["ESTADO"] = "NO_LOCALIZADA"
                resumen["NO_LOCALIZADA"] += 1
                continue
            resumen["PENDIENTE_REVISION"] += 1
        if not simular:
            with open(ruta, "w", newline="", encoding="utf-8-sig" if bom else "utf-8") as f:
                w = csv.DictWriter(f, fieldnames=campos, delimiter=";", lineterminator="\r\n" if crlf else "\n")
                w.writeheader()
                w.writerows(filas)

    print("Resultado de aplicar la revisión" + (" (SIMULACIÓN, no se escribió nada)" if simular else ""))
    for k, v in resumen.items():
        print(f"  {k}: {v}")
    if errores:
        print(f"\n{len(errores)} citas rechazadas por no ser literales:")
        for e in errores[:50]:
            print("  -", e)
    print("\nSiguiente paso: python3 07_Datos/scripts/plan_mejora/verificar_citas_C1.py")


if __name__ == "__main__":
    main()
