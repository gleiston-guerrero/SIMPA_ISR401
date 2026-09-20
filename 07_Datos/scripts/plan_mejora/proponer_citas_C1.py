#!/usr/bin/env python3
"""
proponer_citas_C1.py  ·  C1 · SIMPA_ISR401

PROPÓSITO
    Preparar la hoja de revisión de citas literales. Para cada uno de los 227
    fragmentos codificados, busca en SU transcripción (solo intervenciones del
    entrevistado) las frases más parecidas al fragmento parafraseado y las
    ofrece como CANDIDATAS con su número de línea.

    Este script NO decide nada ni escribe en los CSV de codificación.
    La decisión la toma una persona: copia la frase exacta que respalda el
    fragmento o marca NO_LOCALIZADA. Después, aplicar_revision_C1.py comprueba
    que lo copiado es literal antes de aceptarlo.

USO (desde la raíz del repositorio)
    python3 07_Datos/scripts/plan_mejora/proponer_citas_C1.py

SALIDA
    07_Datos/resultados/revision_citas_C1.csv
"""
import csv
import difflib
import re
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
TRANSCRIPCIONES = RAIZ / "02_Evidencias" / "Transcripciones"
ARCHIVOS_CSV = [
    RAIZ / "07_Datos" / "datos_crudos" / "codificacion.csv",
    RAIZ / "07_Datos" / "datos_procesados" / "codificacion_tercera_ronda.csv",
]
SALIDA = RAIZ / "07_Datos" / "resultados" / "revision_citas_C1.csv"
REVISORES = ["Arboleda", "Macías", "Villafuerte", "Huilcapi"]
ETIQUETA = "**Entrevistado:**"

VACIAS = set("""de la el los las un una unos unas y o u e en a al del que se su sus
lo le les por para con sin sobre es son ser esta este esto estos estas como mas muy
ya no si ha han hay tiene tienen tambien pero cuando donde segun entre hasta desde
cada todo toda todos todas otro otra otros otras mismo misma""".split())


def sin_tildes(s):
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def normalizar(s):
    return re.sub(r"\s+", " ", sin_tildes(s).lower()).strip()


def raices(s):
    """Conjunto de raíces (5 primeras letras) de las palabras con contenido."""
    palabras = re.findall(r"[a-z0-9]+", normalizar(s))
    return {p[:5] for p in palabras if p not in VACIAS and len(p) > 2}


def puntuar(parafrasis, candidato, raices_p):
    if not raices_p:
        return 0.0
    r_c = raices(candidato)
    cobertura = len(raices_p & r_c) / len(raices_p)
    parecido = difflib.SequenceMatcher(None, normalizar(parafrasis), normalizar(candidato)).ratio()
    return round(0.6 * cobertura + 0.4 * parecido, 3)


def turnos_entrevistado(ruta):
    """[(numero_de_linea, texto_completo_de_la_linea, offset_del_texto)]"""
    salida = []
    texto = ruta.read_text(encoding="utf-8", errors="ignore")
    for n, linea in enumerate(texto.splitlines(), start=1):
        if linea.startswith(ETIQUETA):
            salida.append((n, linea, len(ETIQUETA)))
    return salida


def oraciones(linea, desde):
    """Tramos (inicio, fin) de cada oración dentro de la línea, como subcadenas exactas."""
    tramos, ini = [], desde
    for m in re.finditer(r"(?<=[.!?…])\s+", linea[desde:]):
        fin = desde + m.start()
        if linea[ini:fin].strip():
            tramos.append((ini, fin))
        ini = desde + m.end()
    if linea[ini:].strip():
        tramos.append((ini, len(linea)))
    return [(a, b) for a, b in tramos]


def candidatas(ruta, parafrasis, k=3):
    raices_p = raices(parafrasis)
    encontradas = []
    for n, linea, off in turnos_entrevistado(ruta):
        tramos = oraciones(linea, off)
        ventanas = [(a, b) for a, b in tramos] + [
            (tramos[i][0], tramos[i + 1][1]) for i in range(len(tramos) - 1)
        ]
        for a, b in ventanas:
            frase = linea[a:b].strip()
            if 12 <= len(frase) <= 450:
                encontradas.append((puntuar(parafrasis, frase, raices_p), n, frase))
    encontradas.sort(key=lambda x: -x[0])
    elegidas, usadas = [], []
    for punt, n, frase in encontradas:
        if any(n == n2 and (frase in f2 or f2 in frase) for n2, f2 in usadas):
            continue
        elegidas.append((punt, n, frase))
        usadas.append((n, frase))
        if len(elegidas) == k:
            break
    return elegidas


def main():
    filas = []
    for csv_path in ARCHIVOS_CSV:
        with open(csv_path, newline="", encoding="utf-8-sig") as f:
            for fila in csv.DictReader(f, delimiter=";"):
                fila["_csv"] = csv_path.name
                filas.append(fila)

    salida = []
    for i, fila in enumerate(filas, start=1):
        ruta = TRANSCRIPCIONES / fila["transcripcion"]
        cands = candidatas(ruta, fila["Fragmento_parafraseado"])
        while len(cands) < 3:
            cands.append((0, "", ""))
        bloque = (len(filas) + len(REVISORES) - 1) // len(REVISORES)
        registro = {
            "N": i,
            "Revisor": REVISORES[(i - 1) // bloque],
            "Archivo_CSV": fila["_csv"],
            "Fila_CSV": fila["linea_csv"],
            "ID_evidencia": fila["ID_evidencia"],
            "Transcripcion": fila["transcripcion"],
            "Codigo": fila["Codigo"],
            "Fragmento_parafraseado": fila["Fragmento_parafraseado"],
        }
        for j, (punt, n, frase) in enumerate(cands, start=1):
            registro[f"Cand{j}_linea"] = n
            registro[f"Cand{j}_parecido"] = punt
            registro[f"Cand{j}_texto"] = frase
        registro.update({"CITA_ELEGIDA": "", "LINEA_ELEGIDA": "", "DECISION": "", "OBSERVACION": ""})
        salida.append(registro)

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    with open(SALIDA, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(salida[0].keys()), delimiter=";")
        w.writeheader()
        w.writerows(salida)
    print(f"{len(salida)} fragmentos preparados -> {SALIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
