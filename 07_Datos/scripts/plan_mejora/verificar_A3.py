#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verificar_A3.py · Verificador independiente de la tarea A3 · SIMPA_ISR401

Comprueba, sin modificar archivos:
- fuente congelada ENTR-04 y su SHA-256;
- archivo de decisiones humanas (25 fichas, 22 LITERAL + 3 NO_LOCALIZADA);
- conjunto humano reconstruido con 22 filas;
- retiro exacto de H-001, H-004 y H-006;
- cita literal exacta en la línea declarada del ENTREVISTADO;
- cobertura completa de EXP-01..EXP-16;
- alineación de procedencia/nota_metodologica en las seis filas señaladas;
- señalamiento de los cuatro pares humano/LLM para análisis aparte;
- notas explícitas de H-010 y H-024;
- artefacto de análisis de pares y sus referencias base.

Uso desde la raíz del repositorio:
    python 07_Datos/scripts/plan_mejora/verificar_A3.py
"""

import csv
import hashlib
import io
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]

REVISION = RAIZ / "07_Datos" / "resultados" / "a3_candidatas_confirmadas.md"
CSV_ACTUAL = RAIZ / "06_Experimento" / "conjuntos" / "requisitos_humano_ENTR-04.csv"
ANALISIS = RAIZ / "07_Datos" / "resultados" / "a3_analisis_pares_casi_identicos.md"

COMMIT_BASE = "2d7816c27c3f41ab20433865546c4de73b0bd736"
RUTA_CSV_GIT = "06_Experimento/conjuntos/requisitos_humano_ENTR-04.csv"
BLOB_CSV_ESPERADO = "9f7890d54162eefcf66cd2156a363547087ff8c7"

COMMIT_FUENTE = "06e241b7ba0ec43d8541c8908bca31a9f7327ffb"
RUTA_FUENTE_GIT = "02_Evidencias/Transcripciones/2026-07-28_ENTR-04_Transcripcion.md"
SHA256_FUENTE_ESPERADO = "5e9cf9dca6af94061ae937c47a6644dde924061c8382325515e258c377c63313"

SHA256_CSV_ESPERADO = "e5801374c719efd4206a9a41972e227b5842b3eeafcad731f9d350f8e9dfed40"

IDS_RETIRADOS = ["H-001", "H-004", "H-006"]
IDS_FINALES = [
    "H-002", "H-003", "H-005", "H-007", "H-008", "H-009",
    "H-010", "H-011", "H-012", "H-013", "H-014", "H-015",
    "H-016", "H-017", "H-018", "H-019", "H-020", "H-021",
    "H-022", "H-023", "H-024", "H-025",
]
IDS_EXP = [f"H-{i:03d}" for i in range(10, 26)]

PARES = {
    "H-013": "LLM-005",
    "H-014": "LLM-006",
    "H-015": "LLM-007",
    "H-020": "LLM-015",
}

ERRORES = []


def ok(msg):
    print(f"[OK] {msg}")


def fallo(msg):
    ERRORES.append(msg)
    print(f"[ERROR] {msg}")


def git_bytes(commit, ruta):
    p = subprocess.run(
        ["git", "show", f"{commit}:{ruta}"],
        cwd=RAIZ,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if p.returncode != 0:
        fallo(
            f"no se pudo leer {commit}:{ruta}: "
            + p.stderr.decode("utf-8", errors="replace").strip()
        )
        return b""
    return p.stdout


def git_blob(commit, ruta):
    p = subprocess.run(
        ["git", "rev-parse", f"{commit}:{ruta}"],
        cwd=RAIZ,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    )
    if p.returncode != 0:
        fallo(f"no se pudo resolver blob de {commit}:{ruta}")
        return ""
    return p.stdout.strip()


def lineas_entrevistado(texto):
    resultado = {}
    hablante = None
    for n, linea in enumerate(texto.splitlines(), start=1):
        if linea.startswith("**Entrevistado:**"):
            hablante = "E"
            resultado[n] = linea[len("**Entrevistado:**"):].lstrip()
        elif linea.startswith("**Entrevistador:**"):
            hablante = "R"
        elif linea.startswith("#") or linea.startswith("**Rol:**"):
            hablante = None
        elif linea.strip() and hablante == "E":
            resultado[n] = linea
    return resultado


def verificar_fuente():
    bruto = git_bytes(COMMIT_FUENTE, RUTA_FUENTE_GIT)
    if not bruto:
        return {}
    sha = hashlib.sha256(bruto).hexdigest()
    if sha == SHA256_FUENTE_ESPERADO:
        ok(f"SHA-256 de ENTR-04 congelada coincide: {sha}")
    else:
        fallo(
            "SHA-256 de ENTR-04 congelada no coincide: "
            f"esperado {SHA256_FUENTE_ESPERADO}, obtenido {sha}"
        )
    try:
        return lineas_entrevistado(bruto.decode("utf-8"))
    except UnicodeDecodeError as e:
        fallo(f"no se pudo decodificar ENTR-04 como UTF-8: {e}")
        return {}


def verificar_base():
    blob = git_blob(COMMIT_BASE, RUTA_CSV_GIT)
    if blob == BLOB_CSV_ESPERADO:
        ok(f"blob del CSV base coincide: {blob}")
    else:
        fallo(
            f"blob del CSV base distinto: esperado {BLOB_CSV_ESPERADO}, obtenido {blob}"
        )


def verificar_revision():
    if not REVISION.exists():
        fallo(f"falta {REVISION.relative_to(RAIZ)}")
        return {}

    texto = REVISION.read_text(encoding="utf-8")
    patron = re.compile(r"(?ms)^##\s+(H-\d{3})\s+—.*?(?=^---\s*$|\Z)")
    bloques = {}
    for m in patron.finditer(texto):
        hid = m.group(1)
        if hid in bloques:
            fallo(f"{hid} aparece duplicado en el archivo de revisión.")
        bloques[hid] = m.group(0)

    esperados = [f"H-{i:03d}" for i in range(1, 26)]
    if sorted(bloques) == esperados:
        ok("archivo de revisión contiene exactamente H-001..H-025")
    else:
        fallo(
            "IDs de revisión distintos de H-001..H-025; "
            f"encontrados: {sorted(bloques)}"
        )

    decisiones = {}
    literal = 0
    no_loc = 0

    patron_x = re.compile(
        r'^-\s*\[[xX]\]\s*línea\s+(\d+)\s+\(similitud\s+[^)]*\):\s+"(.*)"\s*$'
    )

    for hid in esperados:
        bloque = bloques.get(hid, "")
        if not bloque:
            continue

        linea_decision = next(
            (x.strip() for x in bloque.splitlines() if x.startswith("**Decisión:")),
            ""
        )
        marcadas = []
        for linea in bloque.splitlines():
            m = patron_x.match(linea.strip())
            if m:
                marcadas.append((int(m.group(1)), m.group(2)))

        tiene_no_loc = "NO_LOCALIZADA" in linea_decision.upper()
        if tiene_no_loc:
            if marcadas:
                fallo(f"{hid}: NO_LOCALIZADA y [X] simultáneamente.")
            decisiones[hid] = {"tipo": "NO_LOCALIZADA"}
            no_loc += 1
        else:
            if len(marcadas) != 1:
                fallo(f"{hid}: se esperaba una sola [X], hay {len(marcadas)}.")
                continue
            n, cita = marcadas[0]
            decisiones[hid] = {"tipo": "LITERAL", "linea": n, "cita": cita}
            literal += 1

    if literal == 22 and no_loc == 3:
        ok("decisiones humanas: 22 LITERAL + 3 NO_LOCALIZADA")
    else:
        fallo(f"conteo de decisiones inesperado: LITERAL={literal}, NO_LOCALIZADA={no_loc}")

    no_localizados = sorted(
        hid for hid, d in decisiones.items() if d.get("tipo") == "NO_LOCALIZADA"
    )
    if no_localizados == IDS_RETIRADOS:
        ok("NO_LOCALIZADA exactas: H-001, H-004, H-006")
    else:
        fallo(f"NO_LOCALIZADA inesperadas: {no_localizados}")

    return decisiones


def leer_csv_actual():
    if not CSV_ACTUAL.exists():
        fallo(f"falta {CSV_ACTUAL.relative_to(RAIZ)}")
        return [], []

    bruto = CSV_ACTUAL.read_bytes()
    sha = hashlib.sha256(bruto).hexdigest()
    if sha == SHA256_CSV_ESPERADO:
        ok(f"SHA-256 del CSV reconstruido coincide: {sha}")
    else:
        fallo(
            "SHA-256 del CSV reconstruido difiere: "
            f"esperado {SHA256_CSV_ESPERADO}, obtenido {sha}"
        )

    texto = bruto.decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(texto), delimiter=";")
    filas = list(reader)
    campos = list(reader.fieldnames or [])

    obligatorios = {
        "id_conjunto",
        "procedencia",
        "nota_metodologica",
        "cita_literal_entr04",
        "linea_entr04",
        "estado_revision_a3",
        "tratamiento_a3",
        "nota_soporte_a3",
    }
    faltantes = sorted(obligatorios - set(campos))
    if not faltantes:
        ok("columnas A3 requeridas presentes")
    else:
        fallo(f"faltan columnas requeridas: {faltantes}")

    ids = [f.get("id_conjunto", "").strip() for f in filas]
    if ids == IDS_FINALES and len(filas) == 22:
        ok("conjunto reconstruido contiene exactamente 22 filas esperadas")
    else:
        fallo(f"IDs/orden del conjunto reconstruido inesperados: {ids}")

    for hid in IDS_RETIRADOS:
        if hid in ids:
            fallo(f"{hid} debía estar retirado y sigue presente.")
    if not any(hid in ids for hid in IDS_RETIRADOS):
        ok("H-001, H-004 y H-006 no están en el conjunto reconstruido")

    if all(hid in ids for hid in IDS_EXP):
        ok("EXP-01..EXP-16 permanecen completos")
    else:
        faltan = [hid for hid in IDS_EXP if hid not in ids]
        fallo(f"faltan filas experimentales: {faltan}")

    return filas, campos


def verificar_citas(filas, decisiones, lineas):
    por_id = {f["id_conjunto"].strip(): f for f in filas}
    errores_locales = 0

    for hid in IDS_FINALES:
        f = por_id.get(hid)
        d = decisiones.get(hid)
        if not f or not d or d.get("tipo") != "LITERAL":
            fallo(f"{hid}: no hay fila o decisión LITERAL válida.")
            errores_locales += 1
            continue

        try:
            n = int(f.get("linea_entr04", ""))
        except ValueError:
            fallo(f"{hid}: linea_entr04 inválida: {f.get('linea_entr04')!r}")
            errores_locales += 1
            continue

        cita_csv = f.get("cita_literal_entr04", "")
        if n != d["linea"] or cita_csv != d["cita"]:
            fallo(f"{hid}: CSV no coincide con la decisión humana confirmada.")
            errores_locales += 1
            continue

        if n not in lineas:
            fallo(f"{hid}: línea {n} no pertenece al ENTREVISTADO.")
            errores_locales += 1
            continue

        if cita_csv not in lineas[n]:
            fallo(f"{hid}: cita no es literal en la línea {n}.")
            errores_locales += 1
            continue

        if f.get("estado_revision_a3", "").strip() != "LITERAL_VERIFICADA":
            fallo(f"{hid}: estado_revision_a3 no es LITERAL_VERIFICADA.")
            errores_locales += 1

    if errores_locales == 0:
        ok("22/22 citas coinciden con decisión humana y línea literal del ENTREVISTADO")


def verificar_alineacion_y_notas(filas):
    por_id = {f["id_conjunto"].strip(): f for f in filas}

    for hid in ["H-002", "H-003"]:
        f = por_id[hid]
        if f.get("procedencia", "").strip() != "Histórico del ERS":
            fallo(f"{hid}: procedencia histórica no alineada.")
        elif not f.get("nota_metodologica", "").strip():
            fallo(f"{hid}: nota_metodologica vacía.")
        else:
            ok(f"{hid}: procedencia/nota alineadas")

    for hid in ["H-013", "H-014", "H-015", "H-020"]:
        f = por_id[hid]
        proc = f.get("procedencia", "").strip()
        nota = f.get("nota_metodologica", "").strip()
        if not proc.startswith("Elicitado durante la fase de experimentación"):
            fallo(f"{hid}: procedencia experimental inesperada.")
        elif not nota.startswith("Derivado únicamente de ENTR-04"):
            fallo(f"{hid}: nota_metodologica experimental inesperada.")
        else:
            ok(f"{hid}: procedencia/nota alineadas")

    nota10 = por_id["H-010"].get("nota_soporte_a3", "").lower()
    if "identificador único" in nota10 and "formalización" in nota10:
        ok("H-010 declara explícitamente la formalización del identificador único")
    else:
        fallo("H-010 no declara claramente la formalización del identificador único.")

    nota24 = por_id["H-024"].get("nota_soporte_a3", "").lower()
    if (
        "línea 95" in nota24
        and "distribuir" in nota24
        and "formalizaciones" in nota24
    ):
        ok("H-024 distingue respaldo literal de la mecánica formalizada")
    else:
        fallo("H-024 no distingue de forma suficiente respaldo literal y formalización.")


def verificar_pares(filas):
    por_id = {f["id_conjunto"].strip(): f for f in filas}

    for hid, lid in PARES.items():
        esperado = f"ANALIZAR_APARTE_CON_{lid}"
        real = por_id[hid].get("tratamiento_a3", "").strip()
        if real == esperado:
            ok(f"{hid}/{lid}: marcado ANALIZAR_APARTE")
        else:
            fallo(f"{hid}/{lid}: tratamiento inesperado {real!r}")

    if not ANALISIS.exists():
        fallo(f"falta {ANALISIS.relative_to(RAIZ)}")
        return

    texto = ANALISIS.read_text(encoding="utf-8")
    requisitos = [
        COMMIT_BASE,
        BLOB_CSV_ESPERADO,
        COMMIT_FUENTE,
        "No se infiere a partir de la similitud si hubo o no dependencia",
        "medida descriptiva",
    ]
    for item in requisitos:
        if item not in texto:
            fallo(f"análisis de pares no contiene referencia requerida: {item!r}")

    for hid, lid in PARES.items():
        if hid not in texto or lid not in texto:
            fallo(f"análisis de pares no documenta {hid}/{lid}.")

    if not any(msg.startswith("análisis de pares") for msg in ERRORES):
        ok("artefacto de análisis separado documenta los cuatro pares y sus bases")


def main():
    print("=" * 78)
    print("A3 — VERIFICACIÓN INDEPENDIENTE")
    print("=" * 78)

    verificar_base()
    lineas = verificar_fuente()
    decisiones = verificar_revision()
    filas, _ = leer_csv_actual()

    if filas and decisiones and lineas:
        verificar_citas(filas, decisiones, lineas)
        verificar_alineacion_y_notas(filas)
        verificar_pares(filas)

    print()
    print("=" * 78)
    if ERRORES:
        print(f"RESULTADO: FALLA ({len(ERRORES)} error(es))")
        for i, e in enumerate(ERRORES, 1):
            print(f"{i}. {e}")
        return 1

    print("RESULTADO: A3 VERIFICADA SIN ERRORES")
    print("Filas finales: 22")
    print("Retiradas: H-001, H-004, H-006")
    print("Citas literales verificadas: 22/22")
    print("Pares casi idénticos: 4/4 tratados aparte")
    return 0


if __name__ == "__main__":
    sys.exit(main())
