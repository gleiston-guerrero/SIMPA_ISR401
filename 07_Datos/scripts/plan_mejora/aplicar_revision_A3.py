#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
aplicar_revision_A3.py · A3 · SIMPA_ISR401

Reconstruye de forma reproducible el conjunto humano de ENTR-04 a partir de:
  1) un CSV base congelado por commit Git;
  2) la transcripción congelada de ENTR-04;
  3) las decisiones humanas de a3_candidatas_confirmadas.md.

La ejecución es idempotente: puede repetirse después de haber aplicado A3,
porque NO toma como fuente el CSV ya modificado, sino el CSV base fijado en Git.

Uso desde la raíz del repositorio:
    python 07_Datos/scripts/plan_mejora/aplicar_revision_A3.py --simular
    python 07_Datos/scripts/plan_mejora/aplicar_revision_A3.py --aplicar
"""

import argparse
import csv
import hashlib
import io
import re
import subprocess
import sys
from difflib import SequenceMatcher
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]

REVISION = RAIZ / "07_Datos" / "resultados" / "a3_candidatas_confirmadas.md"
CSV_DESTINO = RAIZ / "06_Experimento" / "conjuntos" / "requisitos_humano_ENTR-04.csv"
ANALISIS_PARES = RAIZ / "07_Datos" / "resultados" / "a3_analisis_pares_casi_identicos.md"

# CSV humano base, anterior a la aplicación de A3.
COMMIT_BASE = "2d7816c27c3f41ab20433865546c4de73b0bd736"
RUTA_CSV_GIT = "06_Experimento/conjuntos/requisitos_humano_ENTR-04.csv"
BLOB_CSV_ESPERADO = "9f7890d54162eefcf66cd2156a363547087ff8c7"

# Conjunto LLM usado únicamente para documentar los pares casi idénticos.
RUTA_LLM_GIT = "06_Experimento/salidas_llm/requisitos_LLM_ENTR-04.md"
BLOB_LLM_ESPERADO = "b048da80164dae9963154efcc74160db0bdaf03d"

# Fuente congelada EXP-02.
COMMIT_FUENTE = "06e241b7ba0ec43d8541c8908bca31a9f7327ffb"
RUTA_FUENTE_GIT = "02_Evidencias/Transcripciones/2026-07-28_ENTR-04_Transcripcion.md"
SHA256_FUENTE_ESPERADO = "5e9cf9dca6af94061ae937c47a6644dde924061c8382325515e258c377c63313"

IDS_ESPERADOS = [f"H-{i:03d}" for i in range(1, 26)]
IDS_EXP = [f"H-{i:03d}" for i in range(10, 26)]

PARES_CASI_IDENTICOS = {
    "H-013": "LLM-005",
    "H-014": "LLM-006",
    "H-015": "LLM-007",
    "H-020": "LLM-015",
}

FILAS_ALINEACION_HISTORICA = {"H-002", "H-003"}
FILAS_ALINEACION_EXP = {"H-013", "H-014", "H-015", "H-020"}

CAMPOS_A3 = [
    "cita_literal_entr04",
    "linea_entr04",
    "estado_revision_a3",
    "tratamiento_a3",
    "nota_soporte_a3",
]

NOTAS_ESPECIALES = {
    "H-010": (
        "La cita seleccionada respalda productor, finca, vehículo, fecha y hora. "
        "La llegada al centro de acopio y los datos de procedencia/conductor aparecen "
        "también en la línea 15 de ENTR-04. El identificador único es una formalización "
        "de diseño y no una frase literal de la entrevista."
    ),
    "H-024": (
        "La cita seleccionada respalda la proyección y el límite de capacidad. "
        "La continuación de la línea 95 de ENTR-04 respalda distribuir la fruta entre "
        "diferentes extractoras según la capacidad. El cálculo explícito del excedente "
        "en toneladas y la regla de capacidad restante son formalizaciones de diseño, "
        "no frases literales de la entrevista."
    ),
}


def abortar(msg):
    raise SystemExit(f"ERROR A3: {msg}")


def git_bytes(commit, ruta):
    proc = subprocess.run(
        ["git", "show", f"{commit}:{ruta}"],
        cwd=RAIZ,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        abortar(
            f"no se pudo recuperar {ruta} desde {commit}.\n"
            + proc.stderr.decode("utf-8", errors="replace").strip()
        )
    return proc.stdout


def git_blob(commit, ruta):
    proc = subprocess.run(
        ["git", "rev-parse", f"{commit}:{ruta}"],
        cwd=RAIZ,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    )
    if proc.returncode != 0:
        abortar(f"no se pudo obtener el blob Git de {ruta} en {commit}.")
    return proc.stdout.strip()


def verificar_blob(commit, ruta, esperado):
    obtenido = git_blob(commit, ruta)
    if obtenido != esperado:
        abortar(
            f"blob inesperado para {ruta}.\n"
            f"  esperado: {esperado}\n"
            f"  obtenido: {obtenido}"
        )
    return obtenido


def fuente_congelada():
    contenido = git_bytes(COMMIT_FUENTE, RUTA_FUENTE_GIT)
    digest = hashlib.sha256(contenido).hexdigest()
    if digest != SHA256_FUENTE_ESPERADO:
        abortar(
            "la fuente recuperada NO coincide con el SHA-256 congelado.\n"
            f"  esperado: {SHA256_FUENTE_ESPERADO}\n"
            f"  obtenido: {digest}"
        )
    return contenido, digest


def lineas_del_entrevistado(texto):
    resultado = {}
    hablante = None
    for numero, linea in enumerate(texto.splitlines(), start=1):
        if linea.startswith("**Entrevistado:**"):
            hablante = "E"
            resultado[numero] = linea[len("**Entrevistado:**"):].lstrip()
        elif linea.startswith("**Entrevistador:**"):
            hablante = "R"
        elif linea.startswith("#") or linea.startswith("**Rol:**"):
            hablante = None
        elif linea.strip() and hablante == "E":
            resultado[numero] = linea
    return resultado


def bloques_revision(texto):
    patron = re.compile(r"(?ms)^##\s+(H-\d{3})\s+—.*?(?=^---\s*$|\Z)")
    salida = {}
    for m in patron.finditer(texto):
        hid = m.group(1)
        if hid in salida:
            abortar(f"{hid} aparece más de una vez en el archivo confirmado.")
        salida[hid] = m.group(0)
    return salida


def decision_de_bloque(hid, bloque):
    linea_decision = next(
        (x.strip() for x in bloque.splitlines() if x.startswith("**Decisión:")),
        ""
    )
    if not linea_decision:
        abortar(f"{hid}: falta la línea '**Decisión:**'.")

    no_localizada = "NO_LOCALIZADA" in linea_decision.upper()

    marcadas = []
    patron_x = re.compile(
        r'^-\s*\[[xX]\]\s*línea\s+(\d+)\s+\(similitud\s+[^)]*\):\s+"(.*)"\s*$'
    )
    for linea in bloque.splitlines():
        m = patron_x.match(linea.strip())
        if m:
            marcadas.append((int(m.group(1)), m.group(2)))

    if no_localizada:
        if marcadas:
            abortar(f"{hid}: tiene NO_LOCALIZADA y también una candidata [X].")
        return {"tipo": "NO_LOCALIZADA"}

    if len(marcadas) != 1:
        abortar(
            f"{hid}: se esperaba exactamente una candidata [X] y se encontraron {len(marcadas)}."
        )

    n, cita = marcadas[0]
    return {"tipo": "LITERAL", "linea": n, "cita": cita}


def leer_revision():
    if not REVISION.exists():
        abortar(f"no existe {REVISION.relative_to(RAIZ)}")

    texto = REVISION.read_text(encoding="utf-8")
    bloques = bloques_revision(texto)

    faltan = [x for x in IDS_ESPERADOS if x not in bloques]
    sobran = sorted(set(bloques) - set(IDS_ESPERADOS))
    if faltan or sobran or len(bloques) != 25:
        abortar(
            "el archivo confirmado no contiene exactamente H-001..H-025.\n"
            f"  faltan: {faltan or 'ninguna'}\n"
            f"  sobran: {sobran or 'ninguna'}\n"
            f"  total detectado: {len(bloques)}"
        )

    return {hid: decision_de_bloque(hid, bloques[hid]) for hid in IDS_ESPERADOS}


def leer_csv_base():
    blob = verificar_blob(COMMIT_BASE, RUTA_CSV_GIT, BLOB_CSV_ESPERADO)
    bruto = git_bytes(COMMIT_BASE, RUTA_CSV_GIT)

    bom = bruto.startswith(b"\xef\xbb\xbf")
    crlf = b"\r\n" in bruto[:4096]
    texto = bruto.decode("utf-8-sig")

    reader = csv.DictReader(io.StringIO(texto), delimiter=";")
    filas = list(reader)
    campos = list(reader.fieldnames or [])

    if "id_conjunto" not in campos:
        abortar("el CSV base no contiene la columna id_conjunto.")

    ids = [f.get("id_conjunto", "").strip() for f in filas]
    if ids != IDS_ESPERADOS:
        abortar(
            "el CSV base no contiene exactamente H-001..H-025 en ese orden.\n"
            f"  encontrados: {ids}"
        )

    return filas, campos, bom, crlf, blob


def verificar_alineacion(filas):
    por_id = {f["id_conjunto"].strip(): f for f in filas}
    errores = []

    for hid in sorted(FILAS_ALINEACION_HISTORICA):
        procedencia = por_id[hid].get("procedencia", "").strip()
        nota = por_id[hid].get("nota_metodologica", "").strip()
        if procedencia != "Histórico del ERS":
            errores.append(f"{hid}: procedencia inesperada -> {procedencia!r}")
        if not nota or nota == "Histórico del ERS":
            errores.append(f"{hid}: nota_metodologica vacía o desalineada -> {nota!r}")

    for hid in sorted(FILAS_ALINEACION_EXP):
        procedencia = por_id[hid].get("procedencia", "").strip()
        nota = por_id[hid].get("nota_metodologica", "").strip()
        if not procedencia.startswith("Elicitado durante la fase de experimentación"):
            errores.append(f"{hid}: procedencia inesperada -> {procedencia!r}")
        if not nota.startswith("Derivado únicamente de ENTR-04"):
            errores.append(f"{hid}: nota_metodologica inesperada -> {nota!r}")

    if errores:
        abortar(
            "las columnas procedencia/nota_metodologica no están alineadas:\n  - "
            + "\n  - ".join(errores)
        )


def reconstruir(decisiones, filas, lineas_entrevistado):
    nuevas = []
    excluidas = []
    errores = []
    por_id = {f["id_conjunto"].strip(): f for f in filas}

    for hid in IDS_ESPERADOS:
        fila = dict(por_id[hid])
        dec = decisiones[hid]

        if dec["tipo"] == "NO_LOCALIZADA":
            procedencia = fila.get("procedencia", "").strip()
            if procedencia != "Histórico del ERS":
                errores.append(
                    f"{hid}: NO_LOCALIZADA no es histórica; no se retira automáticamente "
                    f"(procedencia={procedencia!r})."
                )
                continue
            excluidas.append(hid)
            continue

        n = dec["linea"]
        cita = dec["cita"]

        if n not in lineas_entrevistado:
            errores.append(
                f"{hid}: línea {n} no es una intervención del entrevistado "
                "en la fuente congelada."
            )
            continue

        if cita not in lineas_entrevistado[n]:
            errores.append(
                f"{hid}: la cita marcada NO es subcadena exacta de la línea {n} "
                "del entrevistado."
            )
            continue

        fila["cita_literal_entr04"] = cita
        fila["linea_entr04"] = str(n)
        fila["estado_revision_a3"] = "LITERAL_VERIFICADA"
        fila["tratamiento_a3"] = (
            f"ANALIZAR_APARTE_CON_{PARES_CASI_IDENTICOS[hid]}"
            if hid in PARES_CASI_IDENTICOS else
            "INCLUIR"
        )
        fila["nota_soporte_a3"] = NOTAS_ESPECIALES.get(
            hid,
            "Cita literal verificada contra la transcripción congelada ENTR-04."
        )
        nuevas.append(fila)

    if errores:
        abortar(
            "se rechazaron decisiones; el CSV NO debe modificarse:\n  - "
            + "\n  - ".join(errores)
        )

    ids_nuevos = {f["id_conjunto"].strip() for f in nuevas}
    faltan_exp = [hid for hid in IDS_EXP if hid not in ids_nuevos]
    if faltan_exp:
        abortar(
            "una o más filas EXP-01..EXP-16 quedaron fuera: " + ", ".join(faltan_exp)
        )

    if len(nuevas) + len(excluidas) != 25:
        abortar("el balance final no suma 25 filas.")

    return nuevas, excluidas


def serializar_csv(filas, campos, bom, crlf):
    campos_salida = list(campos)
    for c in CAMPOS_A3:
        if c not in campos_salida:
            campos_salida.append(c)

    salida = io.StringIO(newline="")
    w = csv.DictWriter(
        salida,
        fieldnames=campos_salida,
        delimiter=";",
        lineterminator="\r\n" if crlf else "\n",
        extrasaction="ignore",
    )
    w.writeheader()
    w.writerows(filas)

    datos = salida.getvalue().encode("utf-8")
    if bom:
        datos = b"\xef\xbb\xbf" + datos
    return datos


def parsear_llm():
    blob = verificar_blob(COMMIT_BASE, RUTA_LLM_GIT, BLOB_LLM_ESPERADO)
    texto = git_bytes(COMMIT_BASE, RUTA_LLM_GIT).decode("utf-8")
    salida = {}
    patron = re.compile(
        r"(?ms)^###\s+(LLM-\d+)\s*$"
        r"(.*?)(?=^###\s+LLM-\d+\s*$|\Z)"
    )
    for m in patron.finditer(texto):
        lid = m.group(1)
        bloque = m.group(2)
        nombre = re.search(r"\*\*Nombre:\*\*\s*(.+)", bloque)
        descripcion = re.search(r"\*\*Descripción:\*\*\s*(.+)", bloque)
        salida[lid] = {
            "nombre": nombre.group(1).strip() if nombre else "",
            "descripcion": descripcion.group(1).strip() if descripcion else "",
        }
    return salida, blob


def tokens(texto):
    return set(re.findall(r"[a-záéíóúüñ0-9]+", texto.lower()))


def jaccard(a, b):
    ta, tb = tokens(a), tokens(b)
    if not ta and not tb:
        return 1.0
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


def generar_analisis_pares(filas):
    llm, blob_llm = parsear_llm()
    humanos = {f["id_conjunto"]: f for f in filas}

    lineas = [
        "# A3 — Análisis separado de pares humano/LLM casi idénticos",
        "",
        "Este artefacto documenta los cuatro pares señalados por el plan de mejora.",
        "La similitud señalada por el plan no se interpreta como prueba de copia,",
        "dependencia causal ni falta de independencia en su generación.",
        "Por cautela metodológica, los cuatro pares se marcan para análisis separado",
        "en cualquier comparación posterior entre orígenes.",
        "",
        f"- CSV humano base: `{COMMIT_BASE}:{RUTA_CSV_GIT}` · blob `{BLOB_CSV_ESPERADO}`",
        f"- Salida LLM base: `{COMMIT_BASE}:{RUTA_LLM_GIT}` · blob `{blob_llm}`",
        f"- Fuente ENTR-04 congelada: `{COMMIT_FUENTE}:{RUTA_FUENTE_GIT}`",
        "",
        "| Par | Nombre humano | Nombre LLM | Jaccard descripción | SequenceMatcher descripción | Tratamiento |",
        "|---|---|---|---:|---:|---|",
    ]

    for hid, lid in PARES_CASI_IDENTICOS.items():
        h = humanos[hid]
        l = llm.get(lid)
        if not l:
            abortar(f"no se pudo localizar {lid} en la salida LLM base.")

        desc_h = h["descripcion"].strip()
        desc_l = l["descripcion"].strip()
        jac = jaccard(desc_h, desc_l)
        seq = SequenceMatcher(None, desc_h.lower(), desc_l.lower()).ratio()

        lineas.append(
            f"| `{hid}` / `{lid}` | {h['nombre']} | {l['nombre']} | "
            f"{jac:.3f} | {seq:.3f} | ANALIZAR_APARTE |"
        )

    lineas += [
        "",
        "## Regla de tratamiento",
        "",
        "1. Los cuatro pares permanecen en sus archivos de origen para conservar trazabilidad.",
        "2. No se infiere a partir de la similitud si hubo o no dependencia en su generación.",
        "3. Cualquier análisis posterior que compare orígenes debe identificarlos explícitamente",
        "   y reportar su sensibilidad por separado o excluirlos del análisis primario, dejando",
        "   constancia del criterio utilizado.",
        "4. Este archivo no atribuye intención ni establece cómo se produjo la similitud;",
        "   únicamente documenta los pares señalados por el plan y una medida descriptiva",
        "   reproducible de similitud textual.",
        "",
    ]
    return "\n".join(lineas).encode("utf-8")


def estado_destino(esperado):
    if not CSV_DESTINO.exists():
        return "AUSENTE"
    actual = CSV_DESTINO.read_bytes()
    return "COINCIDE" if actual == esperado else "DIFIERE"


def escribir_atomico(ruta, datos):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    tmp = ruta.with_name(ruta.name + ".tmp")
    try:
        tmp.write_bytes(datos)
        tmp.replace(ruta)
    finally:
        if tmp.exists():
            tmp.unlink()


def main():
    ap = argparse.ArgumentParser(description="Aplicar A3 de forma reproducible e idempotente.")
    grupo = ap.add_mutually_exclusive_group(required=True)
    grupo.add_argument("--simular", action="store_true")
    grupo.add_argument("--aplicar", action="store_true")
    args = ap.parse_args()

    contenido_fuente, digest_fuente = fuente_congelada()
    lineas_entr = lineas_del_entrevistado(contenido_fuente.decode("utf-8"))

    decisiones = leer_revision()
    filas_base, campos, bom, crlf, blob_csv = leer_csv_base()
    verificar_alineacion(filas_base)

    reconstruidas, excluidas = reconstruir(decisiones, filas_base, lineas_entr)
    csv_esperado = serializar_csv(reconstruidas, campos, bom, crlf)
    analisis_esperado = generar_analisis_pares(reconstruidas)

    n_literal = sum(d["tipo"] == "LITERAL" for d in decisiones.values())
    n_no_loc = sum(d["tipo"] == "NO_LOCALIZADA" for d in decisiones.values())

    print("=" * 76)
    print("A3 — VALIDACIÓN REPRODUCIBLE")
    print("=" * 76)
    print(f"Commit base CSV           : {COMMIT_BASE}")
    print(f"Blob CSV base             : OK  {blob_csv}")
    print(f"SHA-256 ENTR-04 congelada : OK  {digest_fuente}")
    print(f"Fichas de revisión        : {len(decisiones)}")
    print(f"LITERAL verificadas       : {n_literal}")
    print(f"NO_LOCALIZADA             : {n_no_loc}")
    print(f"Filas reconstruidas       : {len(reconstruidas)}")
    print(f"Filas retiradas Ruta A    : {', '.join(excluidas) if excluidas else 'ninguna'}")
    print("Columnas procedencia/nota : OK")
    print(f"Estado CSV actual         : {estado_destino(csv_esperado)}")
    print(f"SHA-256 CSV esperado      : {hashlib.sha256(csv_esperado).hexdigest()}")
    print()

    print("Pares casi idénticos:")
    for h, llm in PARES_CASI_IDENTICOS.items():
        print(f"  {h} / {llm} -> ANALIZAR_APARTE")
    print()

    print("Notas de soporte explícitas:")
    print("  H-010 -> identificador único declarado como formalización de diseño")
    print("  H-024 -> redistribución respaldada en línea 95; mecánica exacta declarada como formalización")
    print()

    if args.simular:
        print("RESULTADO: SIMULACIÓN CORRECTA.")
        print("No se modificó ningún archivo.")
        return 0

    escribir_atomico(CSV_DESTINO, csv_esperado)
    escribir_atomico(ANALISIS_PARES, analisis_esperado)

    if CSV_DESTINO.read_bytes() != csv_esperado:
        abortar("la verificación posterior a escritura del CSV falló.")
    if ANALISIS_PARES.read_bytes() != analisis_esperado:
        abortar("la verificación posterior a escritura del análisis de pares falló.")

    print(f"RESULTADO: APLICADO.")
    print(f"CSV escrito              : {CSV_DESTINO.relative_to(RAIZ)}")
    print(f"Análisis de pares escrito: {ANALISIS_PARES.relative_to(RAIZ)}")
    print(f"Filas escritas           : {len(reconstruidas)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
