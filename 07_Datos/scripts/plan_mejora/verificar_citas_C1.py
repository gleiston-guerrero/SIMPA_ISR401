#!/usr/bin/env python3
"""
verificar_citas_C1.py  ·  C1 · SIMPA_ISR401

Criterios del docente para C1, comprobados sin atajos:

  1. El 100 % de las citas aparece LITERAL en su transcripción: la subcadena
     exacta (sin ignorar tildes, mayúsculas ni espacios) está en la línea
     indicada y esa línea es una intervención del entrevistado.
  2. El 100 % de los códigos usados tiene definición y criterio en
     07_Datos/libro_codigos.md.

Las filas NO_LOCALIZADA se cuentan aparte (no cuentan como citas verificadas)
y las filas sin revisar hacen fallar la verificación.

USO (desde la raíz del repositorio)
    python3 07_Datos/scripts/plan_mejora/verificar_citas_C1.py
"""
import csv
import re
import sys
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
TRANSCRIPCIONES = RAIZ / "02_Evidencias" / "Transcripciones"
ARCHIVOS = [
    RAIZ / "07_Datos" / "datos_crudos" / "codificacion.csv",
    RAIZ / "07_Datos" / "datos_procesados" / "codificacion_tercera_ronda.csv",
]
LIBRO = RAIZ / "07_Datos" / "libro_codigos.md"
REPORTE = RAIZ / "07_Datos" / "resultados" / "c1_verificacion_citas.txt"
ETIQUETA = "**Entrevistado:**"


def definiciones_del_libro():
    """{codigo: (definicion, criterio)} leído de las filas '| n | CODIGO | definición | criterio |'."""
    defs = {}
    if not LIBRO.exists():
        return defs
    for linea in LIBRO.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*\d+\s*\|\s*([A-Z0-9_]+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$", linea)
        if m:
            defs[m.group(1)] = (m.group(2).strip(), m.group(3).strip())
    return defs


def main():
    lineas, salida = {}, []
    estados, errores, codigos, total = Counter(), [], set(), 0
    for ruta in ARCHIVOS:
        salida.append(f"Archivo: {ruta.relative_to(RAIZ)}")
        with open(ruta, newline="", encoding="utf-8-sig") as f:
            for fila in csv.DictReader(f, delimiter=";"):
                total += 1
                codigos.add(fila["Codigo"].strip())
                estado = fila.get("ESTADO", "").strip()
                estados[estado or "(vacío)"] += 1
                if estado != "VER":
                    continue
                nombre, cita = fila["transcripcion"], fila["CITA_LITERAL"]
                n = fila["LINEA_TRANSCRIPCION"].strip()
                if nombre not in lineas:
                    texto = (TRANSCRIPCIONES / nombre).read_text(encoding="utf-8", errors="ignore")
                    lineas[nombre] = texto.splitlines()
                if not cita or not n.isdigit() or not (1 <= int(n) <= len(lineas[nombre])):
                    errores.append(f"{ruta.name} fila {fila['linea_csv']}: falta la cita o el número de línea es inválido")
                    continue
                linea = lineas[nombre][int(n) - 1]
                if not linea.startswith(ETIQUETA):
                    errores.append(f"{ruta.name} fila {fila['linea_csv']}: la línea {n} no es del entrevistado")
                elif cita not in linea[len(ETIQUETA):]:
                    errores.append(f"{ruta.name} fila {fila['linea_csv']}: la cita NO aparece literal en la línea {n} de {nombre}")

    defs = definiciones_del_libro()
    sin_definir = sorted(c for c in codigos if not defs.get(c, ("", ""))[0] or not defs.get(c, ("", ""))[1])
    verificadas = estados["VER"] - len(errores)
    pendientes = total - estados["VER"] - estados["NO_LOCALIZADA"]

    salida += ["", "=" * 60,
               f"Total de fragmentos: {total}",
               f"Citas literales verificadas: {verificadas} ({100 * verificadas / total:.1f} % del total)" if total else "Sin datos",
               f"NO_LOCALIZADA (declaradas, no cuentan como verificadas): {estados['NO_LOCALIZADA']}",
               f"Pendientes de revisión: {pendientes}",
               f"Citas rechazadas (no literales): {len(errores)}",
               f"Códigos distintos en los CSV: {len(codigos)}",
               f"Códigos con definición y criterio en el libro: {len(codigos) - len(sin_definir)}",
               "=" * 60]
    for e in errores[:60]:
        salida.append("  ✗ " + e)
    if sin_definir:
        salida.append("Códigos sin definición o criterio: " + ", ".join(sin_definir))
    ok = not errores and pendientes == 0 and not sin_definir
    salida.append("RESULTADO: CUMPLE el criterio de C1." if ok else "RESULTADO: NO CUMPLE todavía (ver arriba).")
    REPORTE.parent.mkdir(parents=True, exist_ok=True)
    REPORTE.write_text("\n".join(salida) + "\n", encoding="utf-8")
    print("\n".join(salida))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
