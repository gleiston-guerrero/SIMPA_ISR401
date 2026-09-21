#!/usr/bin/env python3
"""
cegar_aleatorizar.py — cegado posterior a A2

Toma los artefactos normalizados y etiquetados internamente de A2:

  - 06_Experimento/normalizado_A2/requisitos_humano_A2.csv
    22 requisitos humanos reconstruidos en A3 y normalizados en A2.

  - 06_Experimento/normalizado_A2/requisitos_LLM_A2.csv
    25 requisitos LLM normalizados en A2.

Produce:

  1) 06_Experimento/cegado/requisitos_cegados_A2.csv
     — 47 requisitos con el mismo esquema visible, sin id_origen ni otra
       etiqueta explícita de procedencia, renumerados R-001..R-047 y
       aleatorizados de forma reproducible.

  2) ../mapa_confidencial_NO_SUBIR/mapa_origen_A2.csv
     — correspondencia R-ID ↔ origen ↔ id_origen ↔ semilla.
       Se escribe FUERA del repositorio y no debe entregarse a evaluadores.

Este script no vuelve a redactar ni normalizar contenido: el estilo ya fue
normalizado en A2. Su función es exclusivamente retirar la etiqueta de origen,
aleatorizar y producir el artefacto para evaluación cegada.

Uso:
    python 06_Experimento/scripts_analisis/cegar_aleatorizar.py
    python 06_Experimento/scripts_analisis/cegar_aleatorizar.py --seed 20260912

Debe ejecutarse desde la raíz del repositorio.
"""

import argparse
import csv
import random
import re
import sys
from pathlib import Path


RUTA_HUMANO = Path(
    "06_Experimento/normalizado_A2/requisitos_humano_A2.csv"
)
RUTA_LLM = Path(
    "06_Experimento/normalizado_A2/requisitos_LLM_A2.csv"
)

DIR_SALIDA = Path("06_Experimento/cegado")
RUTA_CEGADOS = DIR_SALIDA / "requisitos_cegados_A2.csv"

# Deliberadamente fuera del repositorio.
DIR_CONFIDENCIAL = Path("../mapa_confidencial_NO_SUBIR")
RUTA_MAPA = DIR_CONFIDENCIAL / "mapa_origen_A2.csv"

CAMPOS_VISIBLES = [
    "nombre",
    "descripcion",
    "actor",
    "entradas_salidas",
    "precondicion_postcondicion",
    "prioridad_moscow",
    "criterio_verificacion",
]

CAMPOS_ENTRADA = ["id_origen", *CAMPOS_VISIBLES]
CAMPOS_SALIDA = ["id_cegado", *CAMPOS_VISIBLES]

IDS_HUMANOS_ESPERADOS = {
    f"H-{i:03d}"
    for i in range(1, 26)
    if i not in {1, 4, 6}
}
IDS_LLM_ESPERADOS = {
    f"LLM-{i:03d}"
    for i in range(1, 26)
}

PATRON_ID_ORIGEN = re.compile(r"\b(?:H|LLM)-\d{3}\b")


def leer_normalizados(
    ruta: Path,
    origen: str,
    ids_esperados: set[str],
) -> list[dict[str, str]]:
    if not ruta.exists():
        raise SystemExit(f"ERROR: no existe la entrada requerida: {ruta}")

    with ruta.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter=";")

        if reader.fieldnames != CAMPOS_ENTRADA:
            raise SystemExit(
                "ERROR: esquema inesperado en "
                f"{ruta}\n"
                f"Esperado: {CAMPOS_ENTRADA}\n"
                f"Encontrado: {reader.fieldnames}"
            )

        filas = list(reader)

    ids = [fila["id_origen"].strip() for fila in filas]

    if len(ids) != len(set(ids)):
        raise SystemExit(f"ERROR: IDs duplicados en {ruta}")

    if set(ids) != ids_esperados:
        faltan = sorted(ids_esperados - set(ids))
        sobran = sorted(set(ids) - ids_esperados)
        raise SystemExit(
            f"ERROR: IDs inesperados en {ruta}. "
            f"Faltan={faltan}; sobran={sobran}"
        )

    salida = []

    for numero, fila in enumerate(filas, start=1):
        id_origen = fila["id_origen"].strip()

        visibles = {
            campo: fila[campo].strip()
            for campo in CAMPOS_VISIBLES
        }

        vacios = [
            campo
            for campo, valor in visibles.items()
            if not valor
        ]
        if vacios:
            raise SystemExit(
                f"ERROR: {ruta}, fila {numero}: "
                f"campos visibles vacíos: {vacios}"
            )

        texto_visible = " ".join(visibles.values())
        if PATRON_ID_ORIGEN.search(texto_visible):
            raise SystemExit(
                f"ERROR: {id_origen} contiene un identificador "
                "H-/LLM- dentro de un campo visible."
            )

        salida.append(
            {
                "origen": origen,
                "id_original": id_origen,
                **visibles,
            }
        )

    return salida


def escribir_cegado(
    filas: list[dict[str, str]],
    seed: int,
) -> None:
    rng = random.Random(seed)
    aleatorias = list(filas)
    rng.shuffle(aleatorias)

    DIR_SALIDA.mkdir(parents=True, exist_ok=True)
    DIR_CONFIDENCIAL.mkdir(parents=True, exist_ok=True)

    with (
        RUTA_CEGADOS.open(
            "w",
            encoding="utf-8",
            newline="",
        ) as f_cegado,
        RUTA_MAPA.open(
            "w",
            encoding="utf-8",
            newline="",
        ) as f_mapa,
    ):
        w_cegado = csv.DictWriter(
            f_cegado,
            fieldnames=CAMPOS_SALIDA,
            delimiter=";",
            lineterminator="\n",
        )
        w_cegado.writeheader()

        w_mapa = csv.writer(
            f_mapa,
            delimiter=";",
            lineterminator="\n",
        )
        w_mapa.writerow(
            [
                "id_cegado",
                "origen",
                "id_original",
                "semilla_usada",
            ]
        )

        for i, item in enumerate(aleatorias, start=1):
            id_cegado = f"R-{i:03d}"

            w_cegado.writerow(
                {
                    "id_cegado": id_cegado,
                    **{
                        campo: item[campo]
                        for campo in CAMPOS_VISIBLES
                    },
                }
            )

            w_mapa.writerow(
                [
                    id_cegado,
                    item["origen"],
                    item["id_original"],
                    seed,
                ]
            )


def validar_salida() -> None:
    with RUTA_CEGADOS.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as f:
        reader = csv.DictReader(f, delimiter=";")

        if reader.fieldnames != CAMPOS_SALIDA:
            raise SystemExit(
                "ERROR: el archivo cegado no tiene el esquema esperado."
            )

        filas = list(reader)

    if len(filas) != 47:
        raise SystemExit(
            f"ERROR: se esperaban 47 filas cegadas; hay {len(filas)}."
        )

    ids = [fila["id_cegado"] for fila in filas]
    esperados = [
        f"R-{i:03d}"
        for i in range(1, 48)
    ]

    if ids != esperados:
        raise SystemExit(
            "ERROR: los IDs cegados no son exactamente R-001..R-047."
        )

    for numero, fila in enumerate(filas, start=1):
        texto_visible = " ".join(
            fila[campo]
            for campo in CAMPOS_VISIBLES
        )

        if PATRON_ID_ORIGEN.search(texto_visible):
            raise SystemExit(
                f"ERROR: la fila cegada {numero} conserva "
                "un identificador explícito de origen."
            )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--seed",
        type=int,
        default=20260912,
        help="Semilla reproducible usada únicamente para aleatorizar.",
    )
    args = ap.parse_args()

    humanos = leer_normalizados(
        RUTA_HUMANO,
        "Humano",
        IDS_HUMANOS_ESPERADOS,
    )
    llm = leer_normalizados(
        RUTA_LLM,
        "LLM",
        IDS_LLM_ESPERADOS,
    )

    if len(humanos) != 22:
        raise SystemExit(
            f"ERROR: se esperaban 22 requisitos humanos; hay {len(humanos)}."
        )

    if len(llm) != 25:
        raise SystemExit(
            f"ERROR: se esperaban 25 requisitos LLM; hay {len(llm)}."
        )

    todos = humanos + llm

    if len(todos) != 47:
        raise SystemExit(
            f"ERROR: se esperaban 47 requisitos en total; hay {len(todos)}."
        )

    escribir_cegado(todos, args.seed)
    validar_salida()

    print("CEGADO GENERADO CORRECTAMENTE")
    print(f"Humanos : {len(humanos)}")
    print(f"LLM     : {len(llm)}")
    print(f"Total   : {len(todos)}")
    print(f"Semilla : {args.seed}")
    print(f"Cegado  : {RUTA_CEGADOS}")
    print(f"Mapa    : {RUTA_MAPA} (FUERA DEL REPOSITORIO)")


if __name__ == "__main__":
    main()
