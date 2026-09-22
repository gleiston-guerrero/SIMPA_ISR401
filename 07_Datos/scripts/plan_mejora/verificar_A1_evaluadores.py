#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verificar_A1_evaluadores.py  ·  A1 · SIMPA_ISR401

Verificación automática de las 3 hojas de la repetición correctiva A1, tal
como la pide el "CONTEXTO DE CONTINUIDAD - A1 SIMPA" (sección 13). Este
script NO decide si una hoja "pasa" o "no pasa": calcula cada indicador y lo
reporta. La decisión metodológica (aceptar, declarar limitación, etc.) la
toma el equipo, nunca el script, y el script nunca modifica una hoja para
que cumpla un criterio.

Comprueba, por cada hoja de 06_Experimento/A1_repeticion_correctiva/evaluadores/:
  1. 47/47 requisitos, con IDs R-001 a R-047 (ni de más ni de menos, sin repetir)
  2. Valores de COM, AMB, VER, COR, CON dentro de 1 a 5
  3. Campos obligatorios completos (las 5 dimensiones, sin celdas vacías)
  4. Periodicidad por posición: para cada período de 2 a 10, el % de filas donde
     valor[i] == valor[i-periodo]; se reporta el máximo, con el propio periodo
  5. % de filas donde COM != CON
  6. Términos de cada observación no vacía que SÍ aparecen en el texto del
     requisito correspondiente (nombre + descripcion + criterio_verificacion
     de requisitos_cegados_A2.csv), y cuáles no
  7. Fecha y hora de inicio/fin presentes en el registro de evaluadores
  8. Fecha de evaluación posterior a la fecha de creación del archivo cegado
     (git log de requisitos_cegados_A2.csv)

USO (desde la raíz del repositorio)
    python3 07_Datos/scripts/plan_mejora/verificar_A1_evaluadores.py

Requiere que ya existan:
    06_Experimento/A1_repeticion_correctiva/evaluadores/registro_evaluadores_A1.csv
    06_Experimento/A1_repeticion_correctiva/evaluadores/<codigo>_hoja_puntuacion.csv
      (un archivo por cada fila de codigo en el registro)

Salida:
    07_Datos/resultados/a1_verificacion_evaluadores.md
    07_Datos/resultados/a1_verificacion_evaluadores.csv  (una fila por hoja)
"""
import csv
import re
import subprocess
import sys
import unicodedata
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
DIR_A1 = RAIZ / "06_Experimento" / "A1_repeticion_correctiva" / "evaluadores"
REGISTRO = DIR_A1 / "registro_evaluadores_A1.csv"
CEGADO = RAIZ / "06_Experimento" / "cegado" / "requisitos_cegados_A2.csv"
SAL_MD = RAIZ / "07_Datos" / "resultados" / "a1_verificacion_evaluadores.md"
SAL_CSV = RAIZ / "07_Datos" / "resultados" / "a1_verificacion_evaluadores.csv"

DIMENSIONES = ["COM", "AMB", "VER", "COR", "CON"]
N_REQUISITOS = 47


def norm(s):
    s = unicodedata.normalize("NFD", str(s))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn").lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def stopwords():
    return set(norm(w) for w in (
        "el la los las un una unos unas de del al y o u que se su sus para "
        "con sin por en no es debe deben ser tiene tienen cada este esta "
        "estos estas cual cuales cuando donde como asi mas menos si ya solo "
        "entre desde hasta sobre tambien pero porque"
    ).split())


def fecha_creacion_cegado():
    try:
        out = subprocess.run(
            ["git", "log", "--follow", "--format=%aI", "--", str(CEGADO.relative_to(RAIZ))],
            cwd=RAIZ, capture_output=True, text=True, check=True,
        ).stdout.strip().splitlines()
        if out:
            return datetime.fromisoformat(out[-1])
    except Exception:
        pass
    return None


def parse_fecha_hora(fecha, hora):
    for fmt_f in ("%Y-%m-%d", "%d/%m/%Y"):
        for fmt_h in ("%H:%M:%S", "%H:%M", ""):
            try:
                if fmt_h:
                    return datetime.strptime(f"{fecha} {hora}", f"{fmt_f} {fmt_h}")
                return datetime.strptime(fecha, fmt_f)
            except Exception:
                continue
    return None


def cargar_cegado():
    if not CEGADO.exists():
        sys.exit(f"Falta {CEGADO.relative_to(RAIZ)}")
    filas = list(csv.DictReader(open(CEGADO, newline="", encoding="utf-8-sig"), delimiter=";"))
    texto = {}
    for r in filas:
        rid = r.get("id_cegado", "").strip()
        junto = " ".join(r.get(c, "") for c in ("nombre", "descripcion", "criterio_verificacion", "entradas_salidas"))
        texto[rid] = norm(junto)
    return texto


def revisar_hoja(path, texto_req, sw):
    filas = list(csv.DictReader(open(path, newline="", encoding="utf-8-sig"), delimiter=";"))
    ids = [r.get("id_requisito", "").strip() for r in filas]
    esperados = [f"R-{i:03d}" for i in range(1, N_REQUISITOS + 1)]
    faltan = sorted(set(esperados) - set(ids))
    sobran = sorted(set(ids) - set(esperados))
    repetidos = sorted({i for i in ids if ids.count(i) > 1})

    fuera_de_rango, vacios = [], []
    valores_por_pos = []
    for r in filas:
        rid = r.get("id_requisito", "").strip()
        vals = {}
        for d in DIMENSIONES:
            v = (r.get(d) or "").strip()
            if v == "":
                vacios.append((rid, d))
                vals[d] = None
                continue
            try:
                n = int(v)
                if not (1 <= n <= 5):
                    fuera_de_rango.append((rid, d, v))
                vals[d] = n
            except ValueError:
                fuera_de_rango.append((rid, d, v))
                vals[d] = None
        valores_por_pos.append(vals)

    # Periodicidad por posición: para cada dimensión y periodo 2..10, % de i donde vals[i]==vals[i-periodo]
    peor_periodo, peor_pct, peor_dim = None, 0.0, None
    for d in DIMENSIONES:
        serie = [v[d] for v in valores_por_pos if v[d] is not None]
        n = len(serie)
        for periodo in range(2, 11):
            if n <= periodo:
                continue
            coincide = sum(1 for i in range(periodo, n) if serie[i] == serie[i - periodo])
            total = n - periodo
            pct = 100 * coincide / total if total else 0
            if pct > peor_pct:
                peor_pct, peor_periodo, peor_dim = pct, periodo, d

    com_con_dif = sum(
        1 for v in valores_por_pos if v["COM"] is not None and v["CON"] is not None and v["COM"] != v["CON"]
    )
    total_filas = len(valores_por_pos)
    pct_com_con_dif = 100 * com_con_dif / total_filas if total_filas else 0

    # Terminos de las observaciones
    obs_con_termino_ajeno = []
    for r in filas:
        obs = (r.get("observaciones") or "").strip().strip('"')
        if not obs:
            continue
        rid = r.get("id_requisito", "").strip()
        req_txt = texto_req.get(rid, "")
        palabras = [w for w in norm(obs).split() if len(w) >= 5 and w not in sw]
        ajenas = [w for w in palabras if w not in req_txt]
        if ajenas:
            obs_con_termino_ajeno.append((rid, ajenas))

    return {
        "archivo": path.name,
        "total_filas": total_filas,
        "faltan": faltan,
        "sobran": sobran,
        "repetidos": repetidos,
        "fuera_de_rango": fuera_de_rango,
        "vacios": vacios,
        "peor_periodicidad_pct": round(peor_pct, 1),
        "peor_periodicidad_periodo": peor_periodo,
        "peor_periodicidad_dim": peor_dim,
        "pct_com_con_distinto": round(pct_com_con_dif, 1),
        "obs_con_termino_ajeno": obs_con_termino_ajeno,
    }


def main():
    if not REGISTRO.exists():
        sys.exit(
            f"Falta {REGISTRO.relative_to(RAIZ)}.\n"
            "Este script se corre DESPUÉS de recibir las 3 hojas reales; "
            "todavía no hay nada que verificar."
        )
    texto_req = cargar_cegado()
    sw = stopwords()
    fecha_cegado = fecha_creacion_cegado()

    registro = list(csv.DictReader(open(REGISTRO, newline="", encoding="utf-8-sig"), delimiter=";"))
    filas_out, md = [], []
    md.append("# A1 — Verificación automática de las hojas de la repetición correctiva")
    md.append("")
    md.append(
        "Este informe solo calcula indicadores; no decide si una hoja se acepta. "
        "Ninguna hoja se modifica para que cumpla un criterio."
    )
    if fecha_cegado:
        md.append(f"\nEl archivo cegado (`requisitos_cegados_A2.csv`) se creó el **{fecha_cegado:%Y-%m-%d %H:%M}**.")
    md.append("")

    for r in registro:
        codigo = r.get("codigo", "").strip()
        archivo_hoja = (r.get("archivo_hoja") or f"{codigo}_hoja_puntuacion.csv").strip()
        path = DIR_A1 / archivo_hoja
        md.append(f"## {codigo}")
        if not path.exists():
            md.append(f"- **Archivo no encontrado:** `{archivo_hoja}`. Sin verificar.")
            md.append("")
            continue

        res = revisar_hoja(path, texto_req, sw)

        # cronología
        fi = parse_fecha_hora(r.get("fecha_evaluacion", ""), r.get("hora_inicio", ""))
        ff = parse_fecha_hora(r.get("fecha_evaluacion", ""), r.get("hora_fin", ""))
        cronologia_ok = None
        if fecha_cegado and fi:
            fi_cmp = fi if fi.tzinfo else fi.replace(tzinfo=fecha_cegado.tzinfo)
            cronologia_ok = fi_cmp > fecha_cegado

        md.append(f"- Archivo: `{archivo_hoja}` · {res['total_filas']} filas")
        md.append(f"- Requisitos: faltan {res['faltan'] or 'ninguno'}; sobran {res['sobran'] or 'ninguno'}; repetidos {res['repetidos'] or 'ninguno'}")
        md.append(f"- Fuera de rango (1–5): {len(res['fuera_de_rango'])}" + (f" → {res['fuera_de_rango'][:5]}" if res["fuera_de_rango"] else ""))
        md.append(f"- Campos vacíos: {len(res['vacios'])}" + (f" → {res['vacios'][:5]}" if res["vacios"] else ""))
        md.append(
            f"- Periodicidad por posición, peor caso: **{res['peor_periodicidad_pct']} %** "
            f"en {res['peor_periodicidad_dim']}, período {res['peor_periodicidad_periodo']} "
            f"(criterio: menor a 80 % para ser aceptable)"
        )
        md.append(f"- COM distinta de CON: **{res['pct_com_con_distinto']} %** de las filas (criterio: al menos 20 %)")
        md.append(f"- Observaciones con algún término que no aparece en el requisito citado: {len(res['obs_con_termino_ajeno'])}"
                   + (f" → {res['obs_con_termino_ajeno'][:3]}" if res["obs_con_termino_ajeno"] else ""))
        md.append(f"- Fecha/hora de inicio registrada: {'sí' if fi else 'NO'} · de fin: {'sí' if ff else 'NO'}")
        if cronologia_ok is not None:
            md.append(f"- Evaluación posterior al archivo cegado: {'sí' if cronologia_ok else 'NO — revisar'}")
        else:
            md.append("- Cronología: no se pudo comparar (falta fecha u hora)")
        md.append("")

        filas_out.append({
            "codigo": codigo,
            "archivo": archivo_hoja,
            "requisitos_ok": res["total_filas"] == N_REQUISITOS and not res["faltan"] and not res["sobran"] and not res["repetidos"],
            "rango_ok": len(res["fuera_de_rango"]) == 0,
            "completo_ok": len(res["vacios"]) == 0,
            "peor_periodicidad_pct": res["peor_periodicidad_pct"],
            "pct_com_con_distinto": res["pct_com_con_distinto"],
            "observaciones_con_termino_ajeno": len(res["obs_con_termino_ajeno"]),
            "fecha_hora_completa": bool(fi and ff),
            "posterior_al_cegado": cronologia_ok,
        })

    SAL_MD.write_text("\n".join(md) + "\n", encoding="utf-8")
    with open(SAL_CSV, "w", newline="", encoding="utf-8-sig") as f:
        if filas_out:
            w = csv.DictWriter(f, fieldnames=list(filas_out[0].keys()), delimiter=";")
            w.writeheader()
            w.writerows(filas_out)
    print("\n".join(md))
    print(f"\nEscrito: {SAL_MD.relative_to(RAIZ)} y {SAL_CSV.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
