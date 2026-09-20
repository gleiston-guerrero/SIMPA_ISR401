#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A3 — Buscador de candidatas de cita literal para el conjunto humano ENTR-04.

Para cada una de las 25 filas de requisitos_humano_ENTR-04.csv, busca en la
transcripción CONGELADA de ENTR-04 las intervenciones del entrevistado más
parecidas al nombre/descripción/criterio del requisito, y las presenta con
su número de línea para que una persona confirme cuál es la cita real.

NO decide la cita por sí mismo. Reduce una transcripción de 125 líneas a
2-3 frases candidatas por fila.

Uso, desde la raíz del repositorio:

    python3 07_Datos/scripts/plan_mejora/buscar_candidatas_A3.py
"""

import csv
import re
import unicodedata

CSV = "06_Experimento/conjuntos/requisitos_humano_ENTR-04.csv"
TRANSCRIPCION = "02_Evidencias/Transcripciones/2026-07-28_ENTR-04_Transcripcion.md"
SHA256_ESPERADO = "5e9cf9dca6af94061ae937c47a6644dde924061c8382325515e258c377c63313"
SALIDA = "07_Datos/resultados/a3_candidatas_para_confirmar.md"


def normaliza(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9áéíóúñ ]", " ", s)


STOPWORDS = {
    "que", "de", "la", "el", "en", "y", "a", "los", "las", "se", "un", "una",
    "por", "con", "para", "es", "del", "al", "lo", "como", "su", "sus",
    "cuando", "esta", "este", "estos", "estas", "ese", "esa", "eso", "muy",
    "mas", "pero", "si", "no", "ya", "entre", "sobre", "debe", "sistema",
    "requisito", "ser", "o", "u", "e",
}


def tokens(s):
    return set(w for w in normaliza(s).split() if w not in STOPWORDS and len(w) > 3)


def parsear_transcripcion(ruta):
    turnos = []
    with open(ruta, encoding="utf-8") as f:
        for i, linea in enumerate(f, 1):
            m = re.match(r"\*\*Entrevistado:\*\*\s*(.+)", linea.strip())
            if m:
                turnos.append((i, m.group(1).strip()))
    return turnos


def dividir(texto):
    partes = re.split(r"(?<=[.:])\s+", texto)
    return [p.strip() for p in partes if len(p.strip()) > 15]


def puntuar(consulta, frase):
    ft = tokens(frase)
    if not ft:
        return 0.0
    return len(consulta & ft) / len(consulta | ft)


def main():
    import hashlib
    with open(TRANSCRIPCION, "rb") as f:
        real = hashlib.sha256(f.read()).hexdigest()
    if real != SHA256_ESPERADO:
        raise SystemExit(
            f"ERROR: la transcripción NO coincide con el hash congelado.\n"
            f"  esperado: {SHA256_ESPERADO}\n  actual:   {real}\n"
            "No se genera nada sobre una fuente distinta a la congelada."
        )

    turnos = parsear_transcripcion(TRANSCRIPCION)
    banco = [(n, f) for n, t in turnos for f in dividir(t)]

    with open(CSV, encoding="utf-8-sig", newline="") as f:
        filas = list(csv.DictReader(f, delimiter=";"))

    out = [
        "# A3 — Candidatas de cita literal para el conjunto humano ENTR-04\n",
        f"Transcripción verificada contra el hash congelado en "
        f"`06_Experimento/material_fuente/ENTR-04_fuente_congelada.md`: `{real}`.\n",
        "Cada bloque muestra hasta 3 frases del ENTREVISTADO más parecidas al "
        "requisito. Marcar con [X] la correcta, o escribir NO_LOCALIZADA si "
        "ninguna corresponde. Las filas con procedencia «Histórico del ERS» "
        "no requieren cita de ENTR-04 (trazan a EV-04 en el ERS, verificado "
        "en `07_Datos/datos_procesados/tabla_procedencia_requisitos.csv`); "
        "se incluyen igual por si el equipo decide reforzarlas con cita "
        "directa.\n",
        "---\n",
    ]

    for r in filas:
        consulta = tokens(r["nombre"]) | tokens(r["descripcion"]) | tokens(r["criterio_verificacion"])
        candidatas = sorted(
            ((puntuar(consulta, f), n, f) for n, f in banco),
            key=lambda x: -x[0],
        )
        vistas, top = set(), []
        for score, n, f in candidatas:
            if f in vistas or score == 0:
                continue
            vistas.add(f)
            top.append((score, n, f))
            if len(top) >= 3:
                break

        out.append(f"## {r['id_conjunto']} — {r['nombre']}")
        out.append(f"- **Origen:** `{r['id_origen']}`  ·  **Procedencia declarada:** {r['procedencia']}")
        out.append(f"- **Descripción:** {r['descripcion']}")
        out.append(f"- **Criterio de verificación:** {r['criterio_verificacion']}")
        out.append("")
        out.append("**Candidatas:**")
        out.append("")
        if not top:
            out.append("*(sin candidatas con solapamiento de términos)*")
        for score, n, f in top:
            out.append(f"- [ ] línea {n} (similitud {score:.2f}): \"{f}\"")
        out.append("")
        out.append("**Decisión (completar):** ")
        out.append("")
        out.append("---\n")

    with open(SALIDA, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"Filas procesadas: {len(filas)}")
    print(f"Salida: {SALIDA}")


if __name__ == "__main__":
    main()
