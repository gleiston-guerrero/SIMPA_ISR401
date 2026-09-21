#!/usr/bin/env python3
"""
A2 — Normalización de estilo de los dos conjuntos antes del cegado.

Entradas:
- 06_Experimento/conjuntos/requisitos_humano_ENTR-04.csv
- 06_Experimento/salidas_llm/requisitos_LLM_ENTR-04.md

Salidas derivadas:
- 06_Experimento/normalizado_A2/requisitos_humano_A2.csv
- 06_Experimento/normalizado_A2/requisitos_LLM_A2.csv
- 07_Datos/resultados/a2_normalizacion_manifest.json

Principios:
- conservar los artefactos originales sin modificarlos;
- normalizar estructura y estilo superficial;
- no inventar requisitos ni datos;
- mantener 22 requisitos humanos confirmados por A3 y 25 requisitos LLM;
- conservar `id_origen` únicamente en estos artefactos internos etiquetados,
  necesarios para verificar A2; el archivo cegado posterior debe eliminarlo.
"""

from __future__ import annotations

from pathlib import Path
import csv
import hashlib
import json
import re


ROOT = Path(__file__).resolve().parents[3]

HUMANO = ROOT / "06_Experimento/conjuntos/requisitos_humano_ENTR-04.csv"
LLM = ROOT / "06_Experimento/salidas_llm/requisitos_LLM_ENTR-04.md"

OUT_DIR = ROOT / "06_Experimento/normalizado_A2"
OUT_H = OUT_DIR / "requisitos_humano_A2.csv"
OUT_L = OUT_DIR / "requisitos_LLM_A2.csv"

MANIFEST = ROOT / "07_Datos/resultados/a2_normalizacion_manifest.json"

CAMPOS = [
    "id_origen",
    "nombre",
    "descripcion",
    "actor",
    "entradas_salidas",
    "precondicion_postcondicion",
    "prioridad_moscow",
    "criterio_verificacion",
]


# Reescrituras conservadoras del conjunto humano.
# Reducen redundancia verbal manteniendo reglas, umbrales y comportamiento.
DC = {
    "H-002": (
        "Registrar por lote la variedad sembrada y usarla para parametrizar "
        "umbrales de diagnóstico y madurez y las advertencias sobre "
        "polinizadores naturales.",
        "Para guineensis aplicar un umbral de madurez de 3 frutos desprendidos "
        "y para híbrido, de 5.",
    ),
    "H-003": (
        "Estimar la madurez de un racimo desde una fotografía de su parte basal "
        "usando el conteo de frutos desprendidos y el umbral de la variedad; "
        "no usar el color del fruto.",
        "Para híbrido, menos de 5 frutos desprendidos indica verde y 5 o más "
        "maduro; para guineensis, aplicar el umbral de 3 frutos.",
    ),
    "H-005": (
        "Registrar del ticket de la extractora peso bruto, tara, peso neto y "
        "calificación de calidad: tamaño, fruta verde, sobremadura, malformada "
        "y pedúnculo largo.",
        "Registrado un ticket, asociar sus valores al lote de origen y permitir "
        "consultarlos en el histórico de entregas.",
    ),
    "H-007": (
        "Registrar fecha y hora de corte por lote, calcular el tiempo hasta la "
        "entrega en la extractora y advertir cuando supere el valor recomendado "
        "para la variedad.",
        "Con un umbral de 24 horas, una entrega realizada 30 horas después del "
        "corte genera una advertencia.",
    ),
    "H-008": (
        "Exportar a la extractora la estimación de cosecha del período limitada "
        "al conteo de racimos y peso promedio estimado, sin datos personales ni "
        "económicos.",
        "El archivo exportado contiene conteo de racimos y peso promedio por "
        "período y excluye datos personales y económicos.",
    ),
    "H-009": (
        "Registrar número y fecha de la guía de remisión de cada despacho y "
        "advertir cuando un despacho se registre sin guía.",
        "Un despacho sin número de guía genera una advertencia visible para la "
        "administración antes del cierre.",
    ),
    "H-010": (
        "Registrar cada llegada de vehículo con centro de acopio, fecha y hora, "
        "finca, productor y conductor, y generar un identificador único de "
        "recepción.",
        "Registrada una llegada con los cinco datos requeridos, generar un "
        "identificador único que permita recuperar centro de acopio, finca, "
        "productor, conductor, fecha y hora.",
    ),
    "H-011": (
        "Registrar el peso bruto del vehículo cargado obtenido en la báscula de "
        "ingreso y asociarlo a la recepción abierta.",
        "Registrado el peso bruto en una recepción abierta, asociarlo a ella; "
        "un segundo registro se conserva como corrección junto con el valor "
        "anterior.",
    ),
    "H-012": (
        "Registrar el peso de salida como tara y calcular el peso neto como "
        "diferencia entre peso bruto y tara.",
        "Con 20 000 kg de peso bruto y 7 500 kg de tara, calcular y conservar "
        "12 500 kg de peso neto.",
    ),
    "H-013": (
        "Calificar la madurez por frutos desprendidos usando un umbral de 3 para "
        "guineensis y de 5 para híbridos.",
        "Guineensis cumple con 3 frutos desprendidos y no con 2; híbrido cumple "
        "con 5 y no con 4.",
    ),
    "H-014": (
        "Generar una observación de calidad al productor cuando el pedúnculo "
        "medido en la base del racimo supere 5 cm.",
        "Con 5,5 cm generar la observación; con 5,0 cm o menos no generarla.",
    ),
    "H-015": (
        "Marcar la fruta como no recibida cuando la malformación evaluada "
        "supere el 30 %.",
        "Con 30,5 % marcar la fruta como no recibida; con 30 % o menos permitir "
        "continuar la recepción.",
    ),
    "H-016": (
        "Registrar la devolución de fruta rechazada en el mismo vehículo, "
        "exigiendo peso de salida y emisión del tiquete antes de cerrar la "
        "recepción.",
        "Una recepción rechazada no puede cerrarse sin registrar el peso de "
        "salida y emitir el tiquete de devolución.",
    ),
    "H-017": (
        "Registrar en cada entrega una única categoría de tamaño: grande, "
        "mediana o pequeña.",
        "La entrega conserva exactamente una de las tres categorías y no admite "
        "dos simultáneas.",
    ),
    "H-018": (
        "Registrar por entrega los indicadores de fruta verde, sobremadura, "
        "malformada y pedúnculos largos.",
        "La calificación conserva los cuatro indicadores y permite recuperarlos "
        "asociados a la recepción y su fecha.",
    ),
    "H-019": (
        "Emitir un ticket con peso bruto, tara, peso neto, productor, finca, "
        "transportista, placa, fecha y hora de ingreso y calificación de la "
        "fruta.",
        "El ticket presenta los nueve campos declarados y no puede emitirse sin "
        "peso neto o calificación.",
    ),
    "H-020": (
        "Permitir la entrega del ticket al conductor o productor presente y su "
        "envío automático por correo cuando exista una dirección registrada, "
        "dejando constancia del resultado.",
        "Con correo registrado, enviar el ticket y almacenar el estado; sin "
        "correo, conservar solo la entrega física sin generar error.",
    ),
    "H-021": (
        "Identificar mediante el histórico a los productores con mayor "
        "recurrencia de fruta verde y generar el listado al menos un mes antes "
        "del período de baja productividad de julio a octubre.",
        "Con julio como inicio del período de baja productividad, generar en "
        "junio el listado ordenado por recurrencia de fruta verde.",
    ),
    "H-022": (
        "Programar visitas de campo y capacitaciones para productores "
        "identificados, registrando finca, fecha, motivo y participantes, y "
        "permitir cerrarlas como realizadas.",
        "Una visita conserva finca, fecha, motivo y participantes y permite "
        "separar actividades pendientes de realizadas.",
    ),
    "H-023": (
        "Registrar una excepción para recibir fruta que incumple indicadores "
        "solo en la fecha de capacitación y para el productor participante, "
        "impidiendo usarla después.",
        "Una excepción del 10 de julio no aplica a una entrega del mismo "
        "productor el 11 de julio; esa entrega se procesa como devolución.",
    ),
    "H-024": (
        "Consolidar estimaciones de cosecha por período, compararlas con la "
        "capacidad de cada extractora, señalar excedentes y permitir "
        "redistribuirlos a plantas con capacidad disponible.",
        "Si una proyección supera la capacidad configurada, mostrar el excedente "
        "en toneladas y permitir reasignarlo a otra planta con capacidad "
        "disponible.",
    ),
    "H-025": (
        "Mantener un histórico por finca con conteo de racimos, peso promedio "
        "informado y peso neto recibido, permitiendo comparar períodos sin datos "
        "personales del productor.",
        "Con dos períodos registrados, mostrar por finca conteo de racimos, peso "
        "promedio, peso neto y variación entre períodos, sin datos personales.",
    ),
}


EP = {
    "H-002": (
        "Entrada: variedad y parámetros del lote. Salida: umbrales para "
        "diagnóstico y clasificación.",
        "Pre: lote existente. Post: módulos de IA usan los umbrales de su "
        "variedad.",
    ),
    "H-003": (
        "Entrada: fotografía basal del racimo y variedad. Salida: madurez "
        "estimada (verde, maduro o sobremaduro), nivel de confianza y explicación.",
        "Pre: lote con variedad asignada. Post: estimación asociada a racimo, "
        "lote y fecha.",
    ),
    "H-005": (
        "Entrada: datos del ticket de pesaje. Salida: entrega asociada a lote, "
        "fecha y calificación.",
        "Pre: despacho registrado. Post: calificación asociada al lote y "
        "disponible en el histórico.",
    ),
    "H-007": (
        "Entrada: fecha y hora de corte y entrega. Salida: intervalo y "
        "advertencia si supera el umbral.",
        "Pre: cosecha con fecha y hora. Post: intervalo registrado con el despacho.",
    ),
    "H-008": (
        "Entrada: período y lotes. Salida: archivo con conteo de racimos y peso "
        "promedio estimado.",
        "Pre: estimación calculada. Post: archivo disponible sin datos personales.",
    ),
    "H-009": (
        "Entrada: número y fecha de guía. Salida: guía asociada al despacho o "
        "advertencia.",
        "Pre: despacho registrado. Post: guía vinculada al despacho.",
    ),
    "H-010": (
        "Entrada: centro de acopio, fecha y hora, finca, productor y conductor. "
        "Salida: recepción con identificador único.",
        "Pre: vehículo en centro habilitado. Post: recepción abierta para pesaje.",
    ),
    "H-011": (
        "Entrada: recepción y peso bruto. Salida: recepción con peso bruto "
        "registrado.",
        "Pre: recepción abierta sin peso bruto. Post: peso bruto asociado antes "
        "de la descarga.",
    ),
    "H-012": (
        "Entrada: peso bruto y peso de salida. Salida: tara y peso neto.",
        "Pre: peso bruto registrado y vehículo en báscula. Post: peso neto "
        "disponible para emitir el ticket.",
    ),
    "H-013": (
        "Entrada: variedad y frutos desprendidos. Salida: indicador de madurez "
        "cumplido o no.",
        "Pre: fruta en descarga y variedad declarada. Post: madurez asociada a "
        "la recepción.",
    ),
    "H-014": (
        "Entrada: longitud del pedúnculo. Salida: observación asociada a la "
        "recepción y comunicada al productor.",
        "Pre: evaluación de calidad en curso. Post: observación incorporada a "
        "la calificación.",
    ),
    "H-015": (
        "Entrada: porcentaje de malformación. Salida: recepción o rechazo con "
        "motivo.",
        "Pre: malformación evaluada. Post: regla aplicada y motivo registrado.",
    ),
    "H-016": (
        "Entrada: recepción rechazada y peso de salida. Salida: recepción "
        "devuelta y tiquete emitido.",
        "Pre: carga rechazada. Post: devolución cerrada con su tiquete.",
    ),
    "H-017": (
        "Entrada: categoría de tamaño. Salida: entrega con tamaño registrado.",
        "Pre: recepción evaluada. Post: categoría almacenada en la calificación.",
    ),
    "H-018": (
        "Entrada: cuatro indicadores de defecto. Salida: calificación asociada "
        "a la recepción.",
        "Pre: carga evaluada. Post: indicadores disponibles para ticket e histórico.",
    ),
    "H-019": (
        "Entrada: recepción con pesos y calificación. Salida: ticket con nueve "
        "campos.",
        "Pre: peso neto y calificación registrados. Post: ticket emitido y "
        "vinculado a la recepción.",
    ),
    "H-020": (
        "Entrada: ticket emitido y correo del productor. Salida: constancia de "
        "entrega y estado enviado o fallido.",
        "Pre: ticket emitido. Post: entrega registrada y, si aplica, estado del "
        "correo.",
    ),
    "H-021": (
        "Entrada: histórico de calificaciones y período de baja productividad. "
        "Salida: listado priorizado de productores para intervención anticipada.",
        "Pre: existen entregas calificadas previas. Post: listado disponible un "
        "mes antes del período configurado.",
    ),
    "H-022": (
        "Entrada: productor, finca, fecha, motivo y participantes. Salida: "
        "actividad programada con estado.",
        "Pre: productor identificado. Post: actividad en agenda y disponible "
        "para cierre.",
    ),
    "H-023": (
        "Entrada: capacitación, productor participante y fecha. Salida: "
        "excepción solo para esa fecha y productor.",
        "Pre: capacitación programada con productor. Post: excepción vinculada "
        "solo a la fecha declarada.",
    ),
    "H-024": (
        "Entrada: estimaciones del período y capacidad por planta. Salida: "
        "proyección, excedente y propuesta de distribución.",
        "Pre: existen estimaciones y capacidades por planta. Post: asignación "
        "de fruta registrada por planta.",
    ),
    "H-025": (
        "Entrada: estimaciones de la finca y pesos netos del período. Salida: "
        "serie histórica por finca y variación entre períodos.",
        "Pre: al menos dos períodos con datos. Post: serie consultable sin datos "
        "personales.",
    ),
}


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


def compactar_espacios(texto: str) -> str:
    return re.sub(r"\s+", " ", texto.strip())


def limpiar_actor(texto: str) -> str:
    # Retira únicamente marcas de evidencia/procedencia añadidas al actor.
    return re.split(r"\s*·\s*", texto.strip())[0].strip()


def normalizar_descripcion(texto: str) -> str:
    texto = compactar_espacios(texto)
    texto = re.sub(
        r"^(?:El sistema debe permitir|El sistema debe poder|El sistema debe)\s+",
        "",
        texto,
        flags=re.IGNORECASE,
    )
    return "Función: " + texto


def normalizar_prepost(texto: str) -> str:
    texto = compactar_espacios(texto)
    texto = re.sub(r"^Pre:\s*", "Precondición: ", texto)
    texto = re.sub(r"\bPost:\s*", "Postcondición: ", texto)
    texto = re.sub(
        r"\s*Postcondición:\s*",
        " | Postcondición: ",
        texto,
        count=1,
    )
    return texto.strip()


def normalizar_criterio(texto: str) -> str:
    return "Verificación: " + compactar_espacios(texto)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for bloque in iter(lambda: f.read(1024 * 1024), b""):
            h.update(bloque)
    return h.hexdigest()


def leer_humanos() -> list[dict[str, str]]:
    with HUMANO.open(encoding="utf-8-sig", newline="") as f:
        filas = list(csv.DictReader(f, delimiter=";"))

    ids = [r["id_conjunto"].strip() for r in filas]

    if len(filas) != 22:
        raise SystemExit(
            f"ERROR A2: se esperaban 22 requisitos humanos tras A3; hay {len(filas)}."
        )

    if len(ids) != len(set(ids)):
        raise SystemExit("ERROR A2: hay IDs humanos duplicados.")

    if set(ids) != set(DC) or set(ids) != set(EP):
        faltan_dc = sorted(set(ids) - set(DC))
        sobran_dc = sorted(set(DC) - set(ids))
        faltan_ep = sorted(set(ids) - set(EP))
        sobran_ep = sorted(set(EP) - set(ids))
        raise SystemExit(
            "ERROR A2: el mapa de normalización no coincide con el conjunto A3.\n"
            f"faltan DC={faltan_dc}, sobran DC={sobran_dc}, "
            f"faltan EP={faltan_ep}, sobran EP={sobran_ep}"
        )

    salida = []

    for r in filas:
        hid = r["id_conjunto"].strip()
        descripcion, criterio = DC[hid]
        entradas_salidas, prepost = EP[hid]

        salida.append({
            "id_origen": hid,
            "nombre": compactar_espacios(r["nombre"]),
            "descripcion": normalizar_descripcion(descripcion),
            "actor": limpiar_actor(r["actor_origen"]),
            "entradas_salidas": compactar_espacios(entradas_salidas),
            "precondicion_postcondicion": normalizar_prepost(prepost),
            "prioridad_moscow": compactar_espacios(r["prioridad"]),
            "criterio_verificacion": normalizar_criterio(criterio),
        })

    return salida


def leer_llm() -> list[dict[str, str]]:
    texto = LLM.read_text(encoding="utf-8")
    salida = []

    for m in LLM_RE.finditer(texto):
        (
            lid,
            nombre,
            descripcion,
            actor,
            entradas_salidas,
            prepost,
            prioridad,
            criterio,
        ) = m.groups()

        salida.append({
            "id_origen": lid.strip(),
            "nombre": compactar_espacios(nombre),
            "descripcion": normalizar_descripcion(descripcion),
            "actor": limpiar_actor(actor),
            "entradas_salidas": compactar_espacios(entradas_salidas),
            "precondicion_postcondicion": normalizar_prepost(prepost),
            "prioridad_moscow": compactar_espacios(prioridad),
            "criterio_verificacion": normalizar_criterio(criterio),
        })

    ids = [r["id_origen"] for r in salida]

    if len(salida) != 25:
        raise SystemExit(
            f"ERROR A2: se esperaban 25 requisitos LLM; hay {len(salida)}."
        )

    if len(ids) != len(set(ids)):
        raise SystemExit("ERROR A2: hay IDs LLM duplicados.")

    esperados = {f"LLM-{i:03d}" for i in range(1, 26)}
    if set(ids) != esperados:
        raise SystemExit(
            "ERROR A2: los IDs LLM no corresponden exactamente a LLM-001..LLM-025."
        )

    return salida


def validar(filas: list[dict[str, str]], etiqueta: str) -> None:
    for i, fila in enumerate(filas, start=1):
        faltantes = [campo for campo in CAMPOS if not fila.get(campo, "").strip()]
        if faltantes:
            raise SystemExit(
                f"ERROR A2: {etiqueta} fila {i} tiene campos vacíos: {faltantes}"
            )


def escribir_csv(path: Path, filas: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=CAMPOS,
            delimiter=";",
            quoting=csv.QUOTE_MINIMAL,
            lineterminator="\n",
        )
        w.writeheader()
        w.writerows(filas)


def main() -> None:
    humanos = leer_humanos()
    llm = leer_llm()

    validar(humanos, "Humano")
    validar(llm, "LLM")

    escribir_csv(OUT_H, humanos)
    escribir_csv(OUT_L, llm)

    manifest = {
        "tarea": "A2",
        "descripcion": "Normalización de estilo previa al cegado",
        "entradas": {
            HUMANO.relative_to(ROOT).as_posix(): {
                "sha256": sha256(HUMANO),
                "filas": 22,
            },
            LLM.relative_to(ROOT).as_posix(): {
                "sha256": sha256(LLM),
                "filas": 25,
            },
        },
        "salidas": {
            OUT_H.relative_to(ROOT).as_posix(): {
                "sha256": sha256(OUT_H),
                "filas": len(humanos),
            },
            OUT_L.relative_to(ROOT).as_posix(): {
                "sha256": sha256(OUT_L),
                "filas": len(llm),
            },
        },
        "total_requisitos": len(humanos) + len(llm),
        "nota_metodologica": (
            "Los originales se conservan sin cambios. La normalización produce "
            "artefactos derivados con esquema común y redacción superficial "
            "homogeneizada para la evaluación cegada posterior."
        ),
    }

    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    with MANIFEST.open("w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    print("A2 — normalización generada")
    print(f"Humanos: {len(humanos)}")
    print(f"LLM    : {len(llm)}")
    print(f"Total  : {len(humanos) + len(llm)}")
    print(f"Salida humana: {OUT_H.relative_to(ROOT)}")
    print(f"Salida LLM   : {OUT_L.relative_to(ROOT)}")
    print(f"Manifest     : {MANIFEST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
