#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Curvas de saturación temática estratificadas — Proyecto SIMPA
Equipo AHMRV · ISR-401 · UTEQ

Integra dos fuentes de codificación sin modificar los archivos históricos:
  - 07_Datos/datos_crudos/codificacion.csv
      Codificación histórica de las primeras ocho entrevistas (EV-01..EV-08).
  - 07_Datos/datos_procesados/codificacion_tercera_ronda.csv
      Codificación de la tercera ronda (ENTR-09..ENTR-16).

Produce en 07_Datos/resultados/:
  - tabla_saturacion.csv
  - curva_saturacion_dominio.png / .pdf
  - curva_saturacion_contraste.png / .pdf
  - curva_saturacion_agregada.png / .pdf

La separación por estratos responde a la adenda A.14/R-14.7: la curva agregada
se conserva como descripción global, pero no debe interpretarse como evidencia
de saturación homogénea entre poblaciones distintas.

Uso:
    python 07_Datos/scripts/curva_saturacion.py

Opcionalmente:
    python 07_Datos/scripts/curva_saturacion.py <legacy.csv> <tercera_ronda.csv>

Requiere: matplotlib
"""

from __future__ import annotations

import csv
import sys
from collections import OrderedDict
from pathlib import Path

try:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except ImportError:
    sys.exit("Falta matplotlib. Instalar con: pip install matplotlib")

ROOT = Path(__file__).resolve().parents[2]
DATOS = ROOT / "07_Datos"

LEGACY = (
    Path(sys.argv[1])
    if len(sys.argv) > 1
    else DATOS / "datos_crudos" / "codificacion.csv"
)
TERCERA = (
    Path(sys.argv[2])
    if len(sys.argv) > 2
    else DATOS / "datos_procesados" / "codificacion_tercera_ronda.csv"
)
SALIDA_DIR = DATOS / "resultados"
SALIDA_DIR.mkdir(parents=True, exist_ok=True)

DOMINIO_FUENTE = [f"EV-{i:02d}" for i in range(1, 9)]
DOMINIO_ENTREVISTA = [f"ENTR-{i:02d}" for i in range(1, 9)]
CONTRASTE = [f"ENTR-{i:02d}" for i in range(9, 17)]

MAPEO_DOMINIO = dict(zip(DOMINIO_FUENTE, DOMINIO_ENTREVISTA))

PERFILES = {   # categorías públicas de tabla_maestra_participantes.csv (B3); no editar aquí sin cambiar la tabla
    "ENTR-01": "Administrador General",
    "ENTR-02": "Asesor técnico",
    "ENTR-03": "Jefe de polinización",
    "ENTR-04": "Supervisor de técnicos agrícolas (planta extractora)",
    "ENTR-05": "Trabajador agrícola",
    "ENTR-06": "Trabajador agrícola",
    "ENTR-07": "Asistente de administración",
    "ENTR-08": "Técnico de extractora",
    "ENTR-09": "Profesional del área agrícola",
    "ENTR-10": "Estudiante de carrera afín",
    "ENTR-11": "Estudiante de carrera afín",
    "ENTR-12": "Profesional del área agrícola",
    "ENTR-13": "Profesional del área agrícola",
    "ENTR-14": "Profesional del área agrícola",
    "ENTR-15": "Estudiante de carrera afín",
    "ENTR-16": "Profesional del área tecnológica",
}

# Solo se usan estas dos columnas; los CSV actuales (tras C1/C2) ya no traen
# "Fragmento" ni "Categoria" (ahora Fragmento_parafraseado y sin categoría).
CABECERA_REQUERIDA = {
    "Codigo",
    "ID_evidencia",
}


def leer_codificacion(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise FileNotFoundError(f"No existe el archivo requerido: {path}")

    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter=";")
        campos = set(reader.fieldnames or [])
        faltan = CABECERA_REQUERIDA - campos
        if faltan:
            raise ValueError(
                f"{path.name} no contiene las columnas requeridas: "
                + ", ".join(sorted(faltan))
            )
        return list(reader)


def agrupar(rows: list[dict[str, str]], orden: list[str]) -> OrderedDict[str, list[str]]:
    grupos = OrderedDict((identificador, []) for identificador in orden)
    observados = set()

    for fila in rows:
        ident = fila["ID_evidencia"].strip()
        codigo = fila["Codigo"].strip()
        if not codigo:
            raise ValueError(f"Código vacío encontrado en {ident or '[sin ID]'}")
        observados.add(ident)
        if ident in grupos:
            grupos[ident].append(codigo)

    esperados = set(orden)
    faltantes = [x for x in orden if not grupos[x]]
    extras = sorted(observados - esperados)

    if faltantes:
        raise ValueError(
            "Faltan entrevistas codificadas: " + ", ".join(faltantes)
        )
    if extras:
        raise ValueError(
            "Se encontraron identificadores fuera del alcance esperado: "
            + ", ".join(extras)
        )

    return grupos


def calcular_estrato(grupos: OrderedDict[str, list[str]]) -> list[dict[str, object]]:
    vistos: set[str] = set()
    salida: list[dict[str, object]] = []

    for ident_fuente, codigos in grupos.items():
        unicos = set(codigos)
        nuevos = unicos - vistos
        vistos.update(unicos)
        salida.append(
            {
                "id_fuente": ident_fuente,
                "fragmentos": len(codigos),
                "codigos_unicos": len(unicos),
                "nuevos": len(nuevos),
                "acumulado": len(vistos),
            }
        )

    return salida


def construir_tabla(
    dominio: OrderedDict[str, list[str]],
    contraste: OrderedDict[str, list[str]],
) -> list[dict[str, object]]:
    dominio_stats = calcular_estrato(dominio)
    contraste_stats = calcular_estrato(contraste)

    vistos_agregado: set[str] = set()
    filas: list[dict[str, object]] = []

    for orden_global, stat in enumerate(dominio_stats, start=1):
        id_fuente = str(stat["id_fuente"])
        id_entrevista = MAPEO_DOMINIO[id_fuente]
        codigos = set(dominio[id_fuente])
        nuevos_agregado = codigos - vistos_agregado
        vistos_agregado.update(codigos)
        filas.append(
            {
                "Orden_global": orden_global,
                "ID_entrevista": id_entrevista,
                "ID_fuente": id_fuente,
                "Estrato": "dominio",
                "Perfil": PERFILES[id_entrevista],
                "Fragmentos_codificados": stat["fragmentos"],
                "Codigos_unicos_entrevista": stat["codigos_unicos"],
                "Codigos_nuevos_estrato": stat["nuevos"],
                "Codigos_acumulados_estrato": stat["acumulado"],
                "Codigos_nuevos_agregado": len(nuevos_agregado),
                "Codigos_acumulados_agregado": len(vistos_agregado),
            }
        )

    for offset, stat in enumerate(contraste_stats, start=9):
        id_fuente = str(stat["id_fuente"])
        id_entrevista = id_fuente
        codigos = set(contraste[id_fuente])
        nuevos_agregado = codigos - vistos_agregado
        vistos_agregado.update(codigos)
        filas.append(
            {
                "Orden_global": offset,
                "ID_entrevista": id_entrevista,
                "ID_fuente": id_fuente,
                "Estrato": "contraste",
                "Perfil": PERFILES[id_entrevista],
                "Fragmentos_codificados": stat["fragmentos"],
                "Codigos_unicos_entrevista": stat["codigos_unicos"],
                "Codigos_nuevos_estrato": stat["nuevos"],
                "Codigos_acumulados_estrato": stat["acumulado"],
                "Codigos_nuevos_agregado": len(nuevos_agregado),
                "Codigos_acumulados_agregado": len(vistos_agregado),
            }
        )

    return filas


def escribir_tabla(filas: list[dict[str, object]]) -> Path:
    path = SALIDA_DIR / "tabla_saturacion.csv"
    campos = [
        "Orden_global",
        "ID_entrevista",
        "ID_fuente",
        "Estrato",
        "Perfil",
        "Fragmentos_codificados",
        "Codigos_unicos_entrevista",
        "Codigos_nuevos_estrato",
        "Codigos_acumulados_estrato",
        "Codigos_nuevos_agregado",
        "Codigos_acumulados_agregado",
    ]

    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=campos, delimiter=";", lineterminator="\n")
        writer.writeheader()
        writer.writerows(filas)

    return path


def guardar_curva(
    ids: list[str],
    acumulados: list[int],
    nuevos: list[int],
    titulo: str,
    nombre: str,
    nota: str,
) -> None:
    fig, ax = plt.subplots(figsize=(10.5, 5.8))
    x = list(range(1, len(ids) + 1))

    ax.plot(x, acumulados, marker="o", linewidth=2)
    for i, (acum, nuevo) in enumerate(zip(acumulados, nuevos), start=1):
        ax.annotate(
            f"{acum} (+{nuevo})",
            (i, acum),
            textcoords="offset points",
            xytext=(0, 8),
            ha="center",
            fontsize=8,
        )

    ax.set_title(titulo)
    ax.set_xlabel("Entrevista en orden de análisis")
    ax.set_ylabel("Códigos únicos acumulados")
    ax.set_xticks(x)
    ax.set_xticklabels(ids, rotation=45, ha="right")
    ax.grid(axis="y", alpha=0.25, linestyle=":")
    ax.text(
        0.01,
        -0.23,
        nota,
        transform=ax.transAxes,
        fontsize=8.5,
        va="top",
        wrap=True,
    )
    fig.subplots_adjust(bottom=0.30)

    fig.savefig(SALIDA_DIR / f"{nombre}.png", dpi=300, bbox_inches="tight")
    fig.savefig(
        SALIDA_DIR / f"{nombre}.pdf",
        bbox_inches="tight",
        metadata={"CreationDate": None, "ModDate": None},
    )
    plt.close(fig)


def main() -> None:
    legacy_rows = leer_codificacion(LEGACY)
    tercera_rows = leer_codificacion(TERCERA)

    dominio = agrupar(legacy_rows, DOMINIO_FUENTE)
    contraste = agrupar(tercera_rows, CONTRASTE)

    filas = construir_tabla(dominio, contraste)
    tabla_path = escribir_tabla(filas)

    dominio_filas = [f for f in filas if f["Estrato"] == "dominio"]
    contraste_filas = [f for f in filas if f["Estrato"] == "contraste"]

    guardar_curva(
        [str(f["ID_entrevista"]) for f in dominio_filas],
        [int(f["Codigos_acumulados_estrato"]) for f in dominio_filas],
        [int(f["Codigos_nuevos_estrato"]) for f in dominio_filas],
        "Saturación temática — estrato de dominio",
        "curva_saturacion_dominio",
        "ENTR-01..ENTR-08. La fuente histórica conserva IDs EV-01..EV-08; "
        "la normalización ENTR se usa únicamente para el orden analítico.",
    )

    guardar_curva(
        [str(f["ID_entrevista"]) for f in contraste_filas],
        [int(f["Codigos_acumulados_estrato"]) for f in contraste_filas],
        [int(f["Codigos_nuevos_estrato"]) for f in contraste_filas],
        "Saturación temática — estrato de contraste",
        "curva_saturacion_contraste",
        "ENTR-09..ENTR-16. El acumulado se reinicia al comenzar el estrato "
        "para evitar confundir mezcla de poblaciones con saturación.",
    )

    guardar_curva(
        [str(f["ID_entrevista"]) for f in filas],
        [int(f["Codigos_acumulados_agregado"]) for f in filas],
        [int(f["Codigos_nuevos_agregado"]) for f in filas],
        "Saturación temática — vista agregada de 16 entrevistas",
        "curva_saturacion_agregada",
        "Vista descriptiva. La inflexión entre estratos puede reflejar la mezcla de "
        "poblaciones y no debe interpretarse por sí sola como saturación homogénea.",
    )

    codigos_dominio = {c for codigos in dominio.values() for c in codigos}
    codigos_contraste = {c for codigos in contraste.values() for c in codigos}
    codigos_agregados = codigos_dominio | codigos_contraste

    print(f"Fuente dominio: {LEGACY}")
    print(f"Fuente contraste: {TERCERA}")
    print(f"Fragmentos dominio: {sum(len(v) for v in dominio.values())}")
    print(f"Fragmentos contraste: {sum(len(v) for v in contraste.values())}")
    print(f"Fragmentos totales: {sum(len(v) for v in dominio.values()) + sum(len(v) for v in contraste.values())}")
    print()
    print(f"Códigos únicos — dominio: {len(codigos_dominio)}")
    print(f"Códigos únicos — contraste: {len(codigos_contraste)}")
    print(f"Códigos compartidos entre estratos: {len(codigos_dominio & codigos_contraste)}")
    print(f"Códigos nuevos exclusivos del contraste: {len(codigos_contraste - codigos_dominio)}")
    print(f"Códigos únicos — agregado: {len(codigos_agregados)}")
    print()
    print("Aportación de códigos nuevos dentro del estrato de contraste:")
    print(
        ", ".join(
            f"{f['ID_entrevista']}={f['Codigos_nuevos_estrato']}"
            for f in contraste_filas
        )
    )
    print("Aportación de códigos nuevos a la vista agregada (ENTR-09..ENTR-16):")
    print(
        ", ".join(
            f"{f['ID_entrevista']}={f['Codigos_nuevos_agregado']}"
            for f in contraste_filas
        )
    )
    print()
    print(f"Tabla: {tabla_path}")
    print("Figuras generadas:")
    print("  - curva_saturacion_dominio.png / .pdf")
    print("  - curva_saturacion_contraste.png / .pdf")
    print("  - curva_saturacion_agregada.png / .pdf")
    print()
    print("Lectura metodológica:")
    print("  * dominio y contraste se interpretan por separado;")
    print("  * la vista agregada es descriptiva;")
    print("  * no se infiere estrato técnico/no técnico a partir del cargo del participante.")


if __name__ == "__main__":
    main()
