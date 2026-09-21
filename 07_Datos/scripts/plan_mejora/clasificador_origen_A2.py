#!/usr/bin/env python3
"""
A2 — Clasificador simple de origen antes/después de la normalización.

Criterio evaluado:
- variables: primera palabra del criterio de verificación + longitud total visible;
- validación: leave-one-out cross-validation (LOOCV);
- aceptación A2: acierto <= 65 % después de normalizar.

La longitud visible excluye IDs y cualquier campo explícito de procedencia.

El clasificador combina:
1. primera palabra: modelo categórico con suavizado de Laplace;
2. longitud: modelo gaussiano por clase;
3. prior igual 0.5 / 0.5 para no favorecer el grupo de 25 frente al de 22.

No usa bibliotecas externas de aprendizaje automático.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import csv
import math
import re


ROOT = Path(__file__).resolve().parents[3]

HUMANO_ORIGINAL = (
    ROOT / "06_Experimento/conjuntos/requisitos_humano_ENTR-04.csv"
)
LLM_ORIGINAL = (
    ROOT / "06_Experimento/salidas_llm/requisitos_LLM_ENTR-04.md"
)

HUMANO_NORMALIZADO = (
    ROOT / "06_Experimento/normalizado_A2/requisitos_humano_A2.csv"
)
LLM_NORMALIZADO = (
    ROOT / "06_Experimento/normalizado_A2/requisitos_LLM_A2.csv"
)

SALIDA = ROOT / "07_Datos/resultados/a2_identificabilidad_antes_despues.md"

UMBRAL = 65.0

CAMPOS_VISIBLES = [
    "nombre",
    "descripcion",
    "actor",
    "entradas_salidas",
    "precondicion_postcondicion",
    "prioridad_moscow",
    "criterio_verificacion",
]


LLM_RE = re.compile(
    r"###\s*(LLM-\d+)\s*\n"
    r"1\.\s*\*\*Identificador:\*\*\s*.*?\n"
    r"2\.\s*\*\*Nombre:\*\*\s*(.*?)\n"
    r"3\.\s*\*\*Descripción:\*\*\s*(.*?)\n"
    r"4\.\s*\*\*Actor/origen:\*\*\s*(.*?)\n"
    r"5\.\s*\*\*Entradas/salidas:\*\*\s*(.*?)\n"
    r"6\.\s*\*\*Precondiciones/postcondiciones:\*\*\s*(.*?)\n"
    r"7\.\s*\*\*Prioridad MoSCoW:\*\*\s*(.*?)\n"
    r"8\.\s*\*\*Criterio de verificación:\*\*\s*(.*?)(?:\n\n|\Z)",
    re.DOTALL,
)


def compactar(texto: str) -> str:
    return re.sub(r"\s+", " ", texto.strip())


def limpiar_actor(texto: str) -> str:
    return re.split(r"\s*·\s*", texto.strip())[0].strip()


def normalizar_prepost_base(texto: str) -> str:
    texto = compactar(texto)
    texto = re.sub(r"\bPre:\s*", "Precondición: ", texto)
    texto = re.sub(r"\bPost:\s*", "Postcondición: ", texto)
    texto = re.sub(
        r"\s*Postcondición:\s*",
        " | Postcondición: ",
        texto,
        count=1,
    )
    return texto.strip()


def primera_palabra(texto: str) -> str:
    m = re.search(
        r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+",
        texto.strip(),
    )
    return m.group(0).lower() if m else ""


def longitud_visible(fila: dict[str, str]) -> int:
    return len(
        " ".join(
            fila[campo].strip()
            for campo in CAMPOS_VISIBLES
        )
    )


def leer_humanos_originales() -> list[dict[str, str]]:
    filas = []

    with HUMANO_ORIGINAL.open(
        encoding="utf-8-sig",
        newline="",
    ) as f:
        for r in csv.DictReader(f, delimiter=";"):
            filas.append({
                "origen": "Humano",
                "nombre": compactar(r["nombre"]),
                "descripcion": compactar(r["descripcion"]),
                "actor": limpiar_actor(r["actor_origen"]),
                "entradas_salidas": compactar(r["entradas_salidas"]),
                "precondicion_postcondicion":
                    normalizar_prepost_base(r["pre_postcondiciones"]),
                "prioridad_moscow": compactar(r["prioridad"]),
                "criterio_verificacion":
                    compactar(r["criterio_verificacion"]),
            })

    return filas


def leer_llm_originales() -> list[dict[str, str]]:
    filas = []
    texto = LLM_ORIGINAL.read_text(encoding="utf-8")

    for m in LLM_RE.finditer(texto):
        (
            _lid,
            nombre,
            descripcion,
            actor,
            entradas_salidas,
            prepost,
            prioridad,
            criterio,
        ) = m.groups()

        filas.append({
            "origen": "LLM",
            "nombre": compactar(nombre),
            "descripcion": compactar(descripcion),
            "actor": limpiar_actor(actor),
            "entradas_salidas": compactar(entradas_salidas),
            "precondicion_postcondicion":
                normalizar_prepost_base(prepost),
            "prioridad_moscow": compactar(prioridad),
            "criterio_verificacion": compactar(criterio),
        })

    return filas


def leer_normalizado(
    path: Path,
    origen: str,
) -> list[dict[str, str]]:
    filas = []

    with path.open(
        encoding="utf-8-sig",
        newline="",
    ) as f:
        for r in csv.DictReader(f, delimiter=";"):
            fila = {"origen": origen}

            for campo in CAMPOS_VISIBLES:
                fila[campo] = compactar(r[campo])

            filas.append(fila)

    return filas


def validar_conjunto(
    filas: list[dict[str, str]],
    etiqueta: str,
) -> None:
    if len(filas) != 47:
        raise SystemExit(
            f"ERROR A2: {etiqueta} contiene {len(filas)} casos; "
            "se esperaban 47."
        )

    n_h = sum(x["origen"] == "Humano" for x in filas)
    n_l = sum(x["origen"] == "LLM" for x in filas)

    if (n_h, n_l) != (22, 25):
        raise SystemExit(
            f"ERROR A2: {etiqueta} tiene Humano={n_h}, LLM={n_l}; "
            "se esperaban 22 y 25."
        )

    for i, fila in enumerate(filas, start=1):
        faltantes = [
            campo
            for campo in CAMPOS_VISIBLES
            if not fila[campo].strip()
        ]
        if faltantes:
            raise SystemExit(
                f"ERROR A2: {etiqueta}, caso {i}, "
                f"campos vacíos: {faltantes}"
            )


def media_varianza(valores: list[int]) -> tuple[float, float]:
    media = sum(valores) / len(valores)
    varianza = (
        sum((x - media) ** 2 for x in valores)
        / len(valores)
    )

    # Evita división por cero sin alterar el método en estos datos.
    return media, max(varianza, 1.0)


def log_gauss(
    x: int,
    media: float,
    varianza: float,
) -> float:
    return (
        -0.5 * math.log(2 * math.pi * varianza)
        - ((x - media) ** 2) / (2 * varianza)
    )


def predecir(
    entrenamiento: list[dict[str, str]],
    prueba: dict[str, str],
) -> str:
    clases = ("Humano", "LLM")

    vocabulario = {
        primera_palabra(x["criterio_verificacion"])
        for x in entrenamiento
    }

    palabra = primera_palabra(
        prueba["criterio_verificacion"]
    )
    largo = longitud_visible(prueba)

    puntajes = {}

    for clase in clases:
        grupo = [
            x for x in entrenamiento
            if x["origen"] == clase
        ]

        cuentas = Counter(
            primera_palabra(x["criterio_verificacion"])
            for x in grupo
        )

        # Laplace + una categoría reservada para palabra no observada.
        p_palabra = (
            (cuentas[palabra] + 1)
            / (len(grupo) + len(vocabulario) + 1)
        )

        largos = [
            longitud_visible(x)
            for x in grupo
        ]
        media, varianza = media_varianza(largos)

        # Prior igual para las dos clases.
        puntajes[clase] = (
            math.log(0.5)
            + math.log(p_palabra)
            + log_gauss(largo, media, varianza)
        )

    return max(puntajes, key=puntajes.get)


def evaluar(
    filas: list[dict[str, str]],
) -> dict:
    correctos = 0
    matriz = Counter()

    for i, prueba in enumerate(filas):
        entrenamiento = filas[:i] + filas[i + 1:]
        predicho = predecir(entrenamiento, prueba)

        if predicho == prueba["origen"]:
            correctos += 1

        matriz[(prueba["origen"], predicho)] += 1

    largos_h = [
        longitud_visible(x)
        for x in filas
        if x["origen"] == "Humano"
    ]
    largos_l = [
        longitud_visible(x)
        for x in filas
        if x["origen"] == "LLM"
    ]

    palabras_h = Counter(
        primera_palabra(x["criterio_verificacion"])
        for x in filas
        if x["origen"] == "Humano"
    )
    palabras_l = Counter(
        primera_palabra(x["criterio_verificacion"])
        for x in filas
        if x["origen"] == "LLM"
    )

    total = len(filas)
    acierto = 100 * correctos / total

    return {
        "correctos": correctos,
        "total": total,
        "acierto": acierto,
        "longitud_h": {
            "media": sum(largos_h) / len(largos_h),
            "min": min(largos_h),
            "max": max(largos_h),
        },
        "longitud_l": {
            "media": sum(largos_l) / len(largos_l),
            "min": min(largos_l),
            "max": max(largos_l),
        },
        "palabras_h": dict(sorted(palabras_h.items())),
        "palabras_l": dict(sorted(palabras_l.items())),
        "matriz": {
            "HH": matriz[("Humano", "Humano")],
            "HL": matriz[("Humano", "LLM")],
            "LH": matriz[("LLM", "Humano")],
            "LL": matriz[("LLM", "LLM")],
        },
    }


def formatear_palabras(datos: dict[str, int]) -> str:
    return ", ".join(
        f"`{palabra}`={cantidad}"
        for palabra, cantidad in datos.items()
    )


def escribir_reporte(
    antes: dict,
    despues: dict,
) -> None:
    cumple = despues["acierto"] <= UMBRAL

    texto = f"""# A2 — Identificabilidad del origen antes y después de normalizar

## Método

Se aplicó un clasificador simple con dos señales visibles:

1. primera palabra del criterio de verificación;
2. longitud total de los siete campos visibles.

La evaluación usa **leave-one-out cross-validation (LOOCV)** sobre 47 requisitos:
22 del conjunto humano confirmado después de A3 y 25 del conjunto LLM.

La primera palabra se modela de forma categórica con suavizado de Laplace.
La longitud se modela con una distribución gaussiana por clase.
Se usan probabilidades previas iguales (0,5 / 0,5) para evitar que la
diferencia 22/25 favorezca automáticamente al conjunto mayoritario.

No se usan IDs ni campos explícitos de procedencia como variables.

## Antes de la normalización

- Casos: {antes["total"]}
- Correctos: {antes["correctos"]}/{antes["total"]}
- Acierto LOOCV: **{antes["acierto"]:.2f} %**
- Longitud media humana: {antes["longitud_h"]["media"]:.1f} caracteres
- Longitud media LLM: {antes["longitud_l"]["media"]:.1f} caracteres
- Rango humano: {antes["longitud_h"]["min"]}–{antes["longitud_h"]["max"]}
- Rango LLM: {antes["longitud_l"]["min"]}–{antes["longitud_l"]["max"]}
- Primeras palabras humanas: {formatear_palabras(antes["palabras_h"])}
- Primeras palabras LLM: {formatear_palabras(antes["palabras_l"])}

Matriz real → predicho:

| Real | Humano | LLM |
|---|---:|---:|
| Humano | {antes["matriz"]["HH"]} | {antes["matriz"]["HL"]} |
| LLM | {antes["matriz"]["LH"]} | {antes["matriz"]["LL"]} |

## Después de la normalización

- Casos: {despues["total"]}
- Correctos: {despues["correctos"]}/{despues["total"]}
- Acierto LOOCV: **{despues["acierto"]:.2f} %**
- Longitud media humana: {despues["longitud_h"]["media"]:.1f} caracteres
- Longitud media LLM: {despues["longitud_l"]["media"]:.1f} caracteres
- Rango humano: {despues["longitud_h"]["min"]}–{despues["longitud_h"]["max"]}
- Rango LLM: {despues["longitud_l"]["min"]}–{despues["longitud_l"]["max"]}
- Primeras palabras humanas: {formatear_palabras(despues["palabras_h"])}
- Primeras palabras LLM: {formatear_palabras(despues["palabras_l"])}

Matriz real → predicho:

| Real | Humano | LLM |
|---|---:|---:|
| Humano | {despues["matriz"]["HH"]} | {despues["matriz"]["HL"]} |
| LLM | {despues["matriz"]["LH"]} | {despues["matriz"]["LL"]} |

## Criterio A2

Criterio definido en el registro de correcciones:
el clasificador no debe superar **{UMBRAL:.0f} %** de acierto sobre el origen.

Resultado reproducido: **{despues["acierto"]:.2f} %**.

**Estado técnico del criterio: {"CUMPLE" if cumple else "NO CUMPLE"}.**

## Nota sobre la cifra histórica 619 / 464

El registro previo documentaba medias históricas de 619 caracteres para el
conjunto humano y 464 para el LLM, pero la fórmula exacta usada para obtener
esas dos cifras no quedó versionada. Por ello, este análisis no presenta esa
fórmula como reconstruida. La medición actual fija explícitamente los siete
campos visibles y deja el procedimiento completo en este script.

## Alcance

La normalización busca reducir señales de estilo que revelaban el origen.
No demuestra que ambos conjuntos sean indistinguibles bajo cualquier
clasificador ni sustituye la evaluación humana cegada de A1.
"""

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    with SALIDA.open("w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def main() -> None:
    antes = (
        leer_humanos_originales()
        + leer_llm_originales()
    )

    despues = (
        leer_normalizado(
            HUMANO_NORMALIZADO,
            "Humano",
        )
        + leer_normalizado(
            LLM_NORMALIZADO,
            "LLM",
        )
    )

    validar_conjunto(antes, "ANTES")
    validar_conjunto(despues, "DESPUÉS")

    resultado_antes = evaluar(antes)
    resultado_despues = evaluar(despues)

    escribir_reporte(
        resultado_antes,
        resultado_despues,
    )

    print("=" * 72)
    print("A2 — CLASIFICADOR DE ORIGEN")
    print("=" * 72)
    print(
        f"ANTES   : "
        f"{resultado_antes['correctos']}/{resultado_antes['total']} "
        f"= {resultado_antes['acierto']:.2f}%"
    )
    print(
        f"DESPUÉS : "
        f"{resultado_despues['correctos']}/{resultado_despues['total']} "
        f"= {resultado_despues['acierto']:.2f}%"
    )
    print(f"UMBRAL  : <= {UMBRAL:.2f}%")
    print(
        "RESULTADO: "
        + (
            "CUMPLE"
            if resultado_despues["acierto"] <= UMBRAL
            else "NO CUMPLE"
        )
    )
    print(
        "Reporte : "
        + SALIDA.relative_to(ROOT).as_posix()
    )


if __name__ == "__main__":
    main()
