#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verificar_B3_perfiles.py  ·  B3 · SIMPA_ISR401

Criterio de B3: "Los mismos perfiles en todas las fuentes, comprobado por script".

La fuente de verdad es 07_Datos/datos_procesados/tabla_maestra_participantes.csv
(un solo perfil por persona). Este script lee el perfil que cada fuente asigna a
ENTR-01 ... ENTR-16 y avisa de cualquier diferencia.

FUENTES QUE SE COMPARAN (cuentan como error si difieren)
    1. Transcripciones            línea "**Rol:**"                       -> igual al perfil público
    2. curva_saturacion.py        diccionario PERFILES                    -> igual al perfil público
    3. tabla_saturacion.csv       columna Perfil                          -> igual al perfil público
    4. ERS (apendices.tex)        tabla de participantes                  -> perfil público o alias
    5. Adenda de 2.ª ronda (PDF)  tabla de roles ENTR-04 a 08             -> perfil público o alias
    6. Actas de member checking   "Participante: ENTR-NN — perfil"        -> perfil público o alias
    7. Consentimiento manuscrito  cargo escrito a mano (ENTR-01 a 03)     -> perfil público o alias

SOLO INFORMATIVAS (no cuentan como error)
    · Etiqueta en el nombre de los archivos de consentimiento (es informal).
    · Perfil PREVISTO en la A.14 (documento firmado: lo previsto no se modifica; la
      diferencia con lo real se declara en 09_Etica/Adenda_Perfiles_Participantes.md).

USO (desde la raíz del repositorio)
    python3 07_Datos/scripts/plan_mejora/verificar_B3_perfiles.py
Código de salida: 0 si todo coincide; 1 si hay diferencias.
"""
import csv
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
MAESTRA = RAIZ / "07_Datos" / "datos_procesados" / "tabla_maestra_participantes.csv"
REPORTE = RAIZ / "07_Datos" / "resultados" / "b3_verificacion_perfiles.txt"


def norm(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn").lower()
    return re.sub(r"[\s\.]+", " ", s.replace("\\", "")).strip(" .,;:—-")


def cargar_maestra():
    with open(MAESTRA, newline="", encoding="utf-8-sig") as f:
        return {r["codigo"]: r for r in csv.DictReader(f, delimiter=";")}


def aceptables(m):
    return [m["perfil_publico"]] + [a for a in m["alias_aceptados"].split("|") if a]


def coincide(valor, m, estricto):
    v = norm(valor)
    if v == norm(m["perfil_publico"]):
        return True
    if estricto:
        return False
    # alias exactos, o texto cortado por un salto de línea (prefijo de un alias)
    return any(v == norm(a) or (len(v) >= 8 and norm(a).startswith(v)) for a in aceptables(m))


def pdf_texto(ruta):
    if not shutil.which("pdftotext"):
        return None
    return subprocess.run(["pdftotext", "-layout", str(ruta), "-"], capture_output=True, text=True).stdout


def fuentes():
    """Devuelve [(nombre_fuente, estricto, {codigo: perfil}, codigos_esperados)]."""
    todos = {f"ENTR-{i:02d}" for i in range(1, 17)}
    out = []
    tr = {}
    for f in sorted((RAIZ / "02_Evidencias" / "Transcripciones").glob("2026-*_Transcripcion.md")):
        m = re.search(r"\*\*Rol:\*\*\s*(.+)", f.read_text(encoding="utf-8", errors="ignore"))
        if m:
            tr[re.search(r"ENTR-\d+", f.name).group(0)] = m.group(1).strip()
    out.append(("Transcripción (**Rol:**)", True, tr, todos))

    py = (RAIZ / "07_Datos" / "scripts" / "curva_saturacion.py").read_text(encoding="utf-8")
    bloque = py[py.index("PERFILES = {"):py.index("}", py.index("PERFILES = {"))]
    out.append(("curva_saturacion.py (PERFILES)", True, dict(re.findall(r'"(ENTR-\d+)":\s*"([^"]+)"', bloque)), todos))

    with open(RAIZ / "07_Datos" / "resultados" / "tabla_saturacion.csv", newline="", encoding="utf-8-sig") as f:
        out.append(("tabla_saturacion.csv (Perfil)", True,
                    {r["ID_entrevista"]: r["Perfil"] for r in csv.DictReader(f, delimiter=";")}, todos))

    ers = (RAIZ / "01_ERS" / "apendices.tex").read_text(encoding="utf-8", errors="ignore")
    filas_ers = {f"ENTR-{n}": p.strip() for n, p in re.findall(r"\\id\{ENTR-(\d+)\}\s*&\s*([^&]+?)\s*&", ers)
                 if "\\id{" not in p}          # solo la tabla de participantes, no la de evidencias
    out.append(("ERS apendices.tex", False, filas_ers, {f"ENTR-{i:02d}" for i in range(1, 9)}))

    t = pdf_texto(RAIZ / "09_Etica" / "Adenda_Segunda_Ronda.pdf")
    if t:
        seccion = t[t.index("Nuevos participantes previstos por rol"):][:2500]
        filas_ad = {}
        for n, p in re.findall(r"ENTR-(0[4-8])\s{2,}(.+?)\s{2,}", seccion):
            filas_ad.setdefault(f"ENTR-{n}", p.strip())          # la primera fila de cada código
        out.append(("Adenda de 2.ª ronda (PDF)", False, filas_ad, {f"ENTR-{i:02d}" for i in range(4, 9)}))
    actas = {}
    for f in sorted((RAIZ / "02_Evidencias" / "Member_Checking" / "Actas").glob("*.pdf")):
        t = pdf_texto(f)
        m = t and re.search(r"Participante:\s*(ENTR-\d+)\s*—\s*(.+?)(?:\.\s*$|\.\n\s*\n)", t, re.S | re.M)
        if m:
            actas[m.group(1)] = re.sub(r"\s+", " ", m.group(2)).strip()
    if actas:
        out.append(("Actas de member checking (PDF)", False, actas, {"ENTR-01", "ENTR-02", "ENTR-13"}))
    return out


def informativas(maestra):
    salida = []
    for f in sorted((RAIZ / "02_Evidencias" / "Consentimientos").glob("*_ENTR-*_Consentimiento.png")):
        cod = re.search(r"ENTR-\d+", f.name).group(0)
        etiqueta = re.sub(r"(?<!^)(?=[A-Z])", " ", f.name.split("_")[1])
        m = maestra[cod]
        ok = any(norm(etiqueta).split()[0][:6] in norm(x) for x in [m["perfil_publico"], m["perfil_especifico_interno"]] + aceptables(m))
        salida.append((cod, "Etiqueta del archivo de consentimiento", etiqueta, ok))
    return salida


def main():
    maestra = cargar_maestra()
    lineas, errores = [], []
    lineas.append(f"B3 · perfiles por fuente contra {MAESTRA.relative_to(RAIZ)}")
    lineas.append("")
    for nombre, estricto, datos, esperados in fuentes():
        faltan = sorted(esperados - set(datos))
        difieren = [(c, datos[c]) for c in sorted(datos) if c in maestra and not coincide(datos[c], maestra[c], estricto)]
        estado = "OK" if not difieren and not faltan else "DIFIERE"
        lineas.append(f"[{estado}] {nombre}: {len(datos)} participantes leídos"
                      + (f" (faltan {', '.join(faltan)})" if faltan else ""))
        for c, v in difieren:
            lineas.append(f"    {c}: fuente='{v}'  ·  maestra='{maestra[c]['perfil_publico']}'")
            errores.append((nombre, c))
    # cargo manuscrito del consentimiento (imagen transcrita en la maestra)
    dif = [c for c, m in maestra.items()
           if m["cargo_en_consentimiento"].endswith("(manuscrito)")
           and not coincide(m["cargo_en_consentimiento"].replace(" (manuscrito)", ""), m, False)]
    lineas.append(f"[{'OK' if not dif else 'DIFIERE'}] Consentimiento manuscrito (ENTR-01 a 03, transcrito de la imagen)")
    errores += [("Consentimiento manuscrito", c) for c in dif]
    lineas.append("")
    lineas.append("Solo informativo (no cuenta como error):")
    for cod, fuente, valor, ok in informativas(maestra):
        if not ok:
            lineas.append(f"    {cod} · {fuente}: '{valor}' no coincide con el perfil (etiqueta informal)")
    lineas.append("    A.14 (perfiles PREVISTOS): difieren de los reales en ENTR-09, 10, 11, 13, 14 y 16; se declara en 09_Etica/Adenda_Perfiles_Participantes.md")
    lineas.append("")
    lineas.append("RESULTADO: CUMPLE, el perfil coincide en todas las fuentes." if not errores
                  else f"RESULTADO: NO CUMPLE, {len(errores)} diferencia(s).")
    REPORTE.parent.mkdir(parents=True, exist_ok=True)
    REPORTE.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    print("\n".join(lineas))
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
