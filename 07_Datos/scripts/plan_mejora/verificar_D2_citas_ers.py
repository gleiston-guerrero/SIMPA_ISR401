#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verificar_D2_citas_ers.py  ·  D2 · SIMPA_ISR401

Criterio de D2: "100 % de las citas literales, con la entrevista correcta y en boca del
entrevistado".

Qué hace
    Recorre los .tex del ERS (01_ERS) y del manuscrito (08_Publicacion) y toma cada cita
    entre comillas de LaTeX (``...'') que lleve una atribución a una evidencia
    (\\id{EV-01} ... \\id{EV-16}) o a una entrevista (ENTR-01 ... ENTR-16). Para cada una:

      OK                     la cita es subcadena EXACTA de lo que dijo el entrevistado
                             de la entrevista atribuida;
      EN_BOCA_ENTREVISTADOR  el texto existe, pero lo dijo quien entrevista;
      EN_OTRA_ENTREVISTA     el texto existe, pero en otra entrevista (se indica cuál);
      NO_LITERAL             el texto no aparece tal cual en ninguna transcripción.

    Las comillas sin atribución a una evidencia (p. ej. términos, encuestas) se ignoran.
    EV-nn corresponde a ENTR-nn.

USO (desde la raíz del repositorio)
    python3 07_Datos/scripts/plan_mejora/verificar_D2_citas_ers.py
Salida: 07_Datos/resultados/d2_verificacion_citas_ers.txt · código 0 si todo OK, 1 si no.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import citas_lib as L  # noqa: E402

RAIZ = L.RAIZ
REPORTE = RAIZ / "07_Datos" / "resultados" / "d2_verificacion_citas_ers.txt"
CITA = re.compile(r"``(.+?)''", re.S)
ATRIB = re.compile(r"\\id\{(?:EV|ENTR)-(\d{2})\}|(?:EV|ENTR)-(\d{2})")


def limpia(t):
    t = t.replace("{,}", ",").replace("\\%", "%").replace("~", " ").replace("\\ ", " ")
    return re.sub(r"\s+", " ", t).strip()


def hablantes():
    """{ENTR-nn: (lineas_del_entrevistado, lineas_del_entrevistador)}"""
    out = {}
    for f in sorted(L.TRANSCRIPCIONES.glob("2026-*_Transcripcion.md")):
        cod = re.search(r"ENTR-\d+", f.name).group(0)
        ent, rev, sp = [], [], None
        for linea in f.read_text(encoding="utf-8", errors="ignore").splitlines():
            m = L.RE_TURNO.match(linea)
            if m:
                sp = "E" if m.group(1) in ("Entrevistado", "Entrevistada") else "R"
                (ent if sp == "E" else rev).append(linea[m.end():])
            elif linea.startswith("#") or linea.startswith("**Rol:**"):
                sp = None
            elif linea.strip() and sp and not L.RE_ACOTACION.match(linea):
                (ent if sp == "E" else rev).append(linea)
        out[cod] = (ent, rev)
    return out


def main():
    turnos = hablantes()
    archivos = sorted((RAIZ / "01_ERS").rglob("*.tex")) + sorted((RAIZ / "08_Publicacion").glob("*.tex"))
    resultados = []
    for f in archivos:
        texto = f.read_text(encoding="utf-8", errors="ignore")
        for m in CITA.finditer(texto):
            resto = re.sub(r"\s+", " ", texto[m.end():m.end() + 140])
            a = ATRIB.search(resto[:100])
            if not a:
                continue
            cod = f"ENTR-{a.group(1) or a.group(2)}"
            cita = limpia(m.group(1))
            linea = texto.count("\n", 0, m.start()) + 1
            ent, rev = turnos.get(cod, ([], []))
            if any(cita in t for t in ent):
                estado, nota = "OK", ""
            elif any(cita in t for t in rev):
                estado, nota = "EN_BOCA_ENTREVISTADOR", "lo dijo quien entrevista"
            else:
                otras = [c for c, (e, _) in turnos.items() if c != cod and any(cita in t for t in e)]
                if otras:
                    estado, nota = "EN_OTRA_ENTREVISTA", "aparece en " + ", ".join(otras)
                else:
                    estado, nota = "NO_LITERAL", "no aparece tal cual en ninguna transcripción"
            resultados.append((f.relative_to(RAIZ), linea, cod, estado, cita, nota))

    malos = [r for r in resultados if r[3] != "OK"]
    salida = [f"D2 · citas textuales del ERS y del manuscrito con atribución: {len(resultados)} · "
              f"correctas: {len(resultados) - len(malos)} · a corregir: {len(malos)}", ""]
    for ruta, linea, cod, estado, cita, nota in resultados:
        salida.append(f"[{estado}] {ruta}:{linea} ({cod}) «{cita[:110]}»" + (f" · {nota}" if nota else ""))
    salida += ["", "RESULTADO: CUMPLE, el 100 % de las citas es literal, de la entrevista correcta y del entrevistado."
               if not malos else "RESULTADO: NO CUMPLE, corregir las citas marcadas."]
    REPORTE.parent.mkdir(parents=True, exist_ok=True)
    REPORTE.write_text("\n".join(salida) + "\n", encoding="utf-8")
    print("\n".join(salida))
    return 1 if malos else 0


if __name__ == "__main__":
    sys.exit(main())
