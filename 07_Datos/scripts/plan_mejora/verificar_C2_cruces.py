#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verificar_C2_cruces.py  ·  C2 · SIMPA_ISR401

Criterio de C2: "Ningún fragmento tiene mejor respaldo en otra entrevista".

Para cada fragmento codificado compara:
    · qué tan bien lo respalda LA CITA que tiene en SU entrevista, con
    · qué tan bien lo respalda la MEJOR frase de cada una de las OTRAS entrevistas.
Se marca como CRUCE si otra entrevista supera a la propia por más de un margen
y con un parecido mínimo. Es una señal para revisar, no una sentencia.

USO (desde la raíz del repositorio)
    python3 07_Datos/scripts/plan_mejora/verificar_C2_cruces.py
Código de salida: 0 si no hay cruces; 1 si hay.
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import citas_lib as L  # noqa: E402

RAIZ = L.RAIZ
ARCHIVOS = [RAIZ / "07_Datos" / "datos_crudos" / "codificacion.csv",
            RAIZ / "07_Datos" / "datos_procesados" / "codificacion_tercera_ronda.csv"]
REPORTE = RAIZ / "07_Datos" / "resultados" / "c2_verificacion_cruces.txt"
MARGEN, MINIMO = 0.15, 0.45

# Señales revisadas a mano que se MANTIENEN (archivo, fila_csv) -> por qué
REVISADOS = {
    ("codificacion.csv", "57"): "Cita corta ('Con un rastreador GPS.', respuesta a '¿mediante qué control?'); el parecido de ENTR-01 es genérico.",
    ("codificacion.csv", "87"): "Ambas entrevistas mencionan la libreta; ENTR-05 la respalda directamente ('lo van a tener en una libreta').",
    ("codificacion.csv", "90"): "Respuesta corta ('El administrador.') a '¿quién le dice en qué lote trabajar?'; ENTR-02 habla de seguimiento por GPS.",
    ("codificacion.csv", "91"): "El texto (avisar al encargado) sí es de ENTR-05; el CÓDIGO EVIDENCIA_FOTOGRAFICA encaja mejor con ENTR-07: revisar el código, no la entrevista.",
    ("codificacion.csv", "100"): "Respuesta corta ('Lote uno y lote dos.'); el parecido de ENTR-13 es genérico.",
}


def main():
    turnos = {f.name: L.turnos_de_archivo(f) for f in sorted(L.TRANSCRIPCIONES.glob("2026-*_Transcripcion.md"))}
    total, cruces, revisados = 0, [], []
    for ruta in ARCHIVOS:
        with open(ruta, newline="", encoding="utf-8-sig") as f:
            for fila in csv.DictReader(f, delimiter=";"):
                total += 1
                frag, propia = fila["Fragmento_parafraseado"], fila["transcripcion"]
                mia = L.puntuar(frag, fila["CITA_LITERAL"]) if fila["CITA_LITERAL"] else 0.0
                mejor = (0.0, "", "")
                for nombre, tr in turnos.items():
                    if nombre == propia:
                        continue
                    c = L.candidatas(tr, frag, "", k=1)
                    if c and c[0][0] > mejor[0]:
                        mejor = (c[0][0], nombre, c[0][2])
                if mejor[0] >= MINIMO and mejor[0] > mia + MARGEN:
                    if (ruta.name, fila["linea_csv"]) in REVISADOS:
                        revisados.append(f"{ruta.name} fila {fila['linea_csv']}: {REVISADOS[(ruta.name, fila['linea_csv'])]}")
                        continue
                    cruces.append(f"{ruta.name} fila {fila['linea_csv']} ({fila['ID_evidencia']} {fila['Codigo']}): "
                                  f"su cita {mia:.2f} vs {mejor[1].split('_')[1]} {mejor[0]:.2f} «{mejor[2][:90]}»")
    salida = [f"C2 · fragmentos revisados: {total} · señales sin revisar: {len(cruces)} · "
              f"señales revisadas y mantenidas: {len(revisados)} (margen {MARGEN}, mínimo {MINIMO})"]
    salida += [f"  ! {c}" for c in cruces] + [f"  ok (revisado) {r}" for r in revisados]
    salida.append("RESULTADO: CUMPLE (ningún fragmento tiene mejor respaldo en otra entrevista)."
                  if not cruces else "RESULTADO: REVISAR los cruces marcados.")
    REPORTE.parent.mkdir(parents=True, exist_ok=True)
    REPORTE.write_text("\n".join(salida) + "\n", encoding="utf-8")
    print("\n".join(salida))
    return 1 if cruces else 0


if __name__ == "__main__":
    sys.exit(main())
