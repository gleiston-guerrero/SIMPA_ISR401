#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
F2 - Trazabilidad del member checking: enunciado -> codigos -> citas literales.

Para cada uno de los doce enunciados sometidos a verificacion el 04/09/2026,
el script PROPONE los codigos del libro que le corresponden y recupera las
citas literales verificadas en C1 que sostienen cada uno.

La correspondencia enunciado-codigo es una PROPUESTA calculada por solape de
terminos contra el nombre, la definicion y el criterio de aplicacion de cada
codigo. Las columnas CODIGOS_VERIFICADOS y VERIFICADO_POR las rellena una
persona. Nada se marca como verificado por el script.

Declara ademas que enunciados se apoyan UNICAMENTE en ENTR-13, cuya
codificacion es posterior a la fecha del acta.
"""
import csv, re, unicodedata, collections, os, sys

LIBRO   = "07_Datos/libro_codigos.md"
CODIF   = ["07_Datos/datos_crudos/codificacion.csv",
           "07_Datos/datos_procesados/codificacion_tercera_ronda.csv"]
SAL_CSV = "07_Datos/datos_procesados/trazabilidad_member_checking_F2.csv"
SAL_MD  = "07_Datos/resultados/trazabilidad_member_checking_F2.md"

FECHA_ACTA       = "2026-09-04"
COMMIT_ENTR13    = "2026-09-07"   # fecha de codificacion de ENTR-13
PARTICIPANTES    = ["ENTR-01", "ENTR-02", "ENTR-13"]

# Los doce enunciados y la posicion de cada participante, transcritos del
# acta consolidada (seccion 4, Matriz de resultados).
#   C = confirma · P = parcial/matiz · R = rechaza · NA = no abordado
#   SP = sin posicion registrada
ENUNCIADOS = [
 (1,  "Registro en libreta y reporte por WhatsApp sin formato fijo",        "R","P","C"),
 (2,  "Reporte con detalle insuficiente",                                   "R","P","C"),
 (3,  "Brecha entre aviso y verificación en sitio",                         "C","P","C"),
 (4,  "Conectividad estable solo en el campamento",                         "P","P","C"),
 (5,  "Pago mixto y necesidad de conteo confiable",                         "P","P","C"),
 (6,  "Riego y control diario como factores determinantes",                 "P","P","C"),
 (7,  "Dificultad de adopción concentrada en el personal manual",           "R","P","P"),
 (8,  "Formalización del registro asociada al tamaño de la finca",          "R","P","C"),
 (9,  "Cosecha programada por desgrane del fruto",                          "C","P","P"),
 (10, "Decisión por observación del cielo y desconfianza en reportes climáticos","R","NA","P"),
 (11, "Abandono de herramientas por resistencia al cambio",                 "SP","NA","C"),
 (12, "La mayor dificultad reside en lograr el uso efectivo",               "P","NA","C"),
]

STOP = set("""de la el en y a los las del que se un una por con para es su al lo como mas o
sin sobre entre solo segun cada su sus este esta estos estas ser son haber hay muy mas menos
necesidad dificultad reside mayor asociada concentrada""".split())

def norm(s):
    s = unicodedata.normalize('NFD', str(s or ''))
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'\s+', ' ', s.lower()).strip()

def terminos(s):
    return {w for w in re.split(r'[^a-z]+', norm(s)) if len(w) > 4 and w not in STOP}

# ---------- libro de codigos ----------
CODIGOS = {}
for linea in open(LIBRO, encoding='utf-8'):
    m = re.match(r'\|\s*\d+\s*\|\s*([A-Z0-9_]+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|', linea)
    if m:
        CODIGOS[m.group(1)] = (m.group(2), m.group(3))

# ---------- fragmentos codificados vigentes ----------
FRAG = []
for f in CODIF:
    for r in csv.DictReader(open(f, encoding='utf-8-sig'), delimiter=';'):
        cita = (r.get('CITA_LITERAL') or '').strip()
        if len(cita) < 15:
            continue
        FRAG.append({
            'codigo': (r.get('Codigo') or '').strip(),
            'ev':     (r.get('ID_evidencia') or '').strip(),
            'trans':  (r.get('transcripcion') or '').strip(),
            'linea':  (r.get('LINEA_TRANSCRIPCION') or '').strip(),
            'cita':   cita,
            'rf':     (r.get('Requisito_derivado') or '').strip(),
        })

por_codigo = collections.defaultdict(list)
for x in FRAG:
    por_codigo[x['codigo']].append(x)

# ---------- peso de cada termino (IDF) ----------
# Sin esto, una palabra como "registro", que aparece en muchos codigos, pesa
# igual que una rara como "conectividad", y enunciados distintos reciben el
# mismo conjunto de codigos.
import math
CAMPO = {cod: terminos(cod.replace('_', ' ') + ' ' + d + ' ' + c)
         for cod, (d, c) in CODIGOS.items()}
df = collections.Counter()
for s_ in CAMPO.values():
    df.update(s_)
N = len(CAMPO)
def idf(w):
    return math.log((N + 1) / (df.get(w, 0) + 1))

UMBRAL_REL = 0.55   # se conservan los codigos que alcanzan el 55 % del mejor
UMBRAL_MIN = 1.20   # y un peso absoluto minimo

# ---------- propuesta enunciado -> codigos ----------
filas, bloques = [], []
for num, texto, p1, p2, p13 in ENUNCIADOS:
    t = terminos(texto)
    puntuados = []
    for cod, campo in CAMPO.items():
        comun = t & campo
        if not comun:
            continue
        peso = sum(idf(w) for w in comun)
        puntuados.append((peso, cod, sorted(comun, key=lambda w: -idf(w))))
    puntuados.sort(reverse=True)
    if puntuados:
        mejor = puntuados[0][0]
        top = [p for p in puntuados
               if p[0] >= max(UMBRAL_MIN, mejor * UMBRAL_REL)][:5]
    else:
        top = []

    citas, evs = [], set()
    for _, cod, _ in top:
        for x in por_codigo.get(cod, []):
            citas.append((cod, x))
            evs.add(x['ev'])

    solo13 = bool(evs) and evs <= {'ENTR-13'}
    alerta = []
    if not citas:
        alerta.append("SIN CITA LITERAL QUE LO SOSTENGA")
    if solo13:
        alerta.append(f"SE APOYA SOLO EN ENTR-13, codificada el {COMMIT_ENTR13}, "
                      f"posterior al acta del {FECHA_ACTA}")
    if p1 == 'R' or p2 == 'R' or p13 == 'R':
        alerta.append("RECHAZADO por al menos un participante")

    filas.append({
        'enunciado_n': num,
        'enunciado': texto,
        'ENTR-01': p1, 'ENTR-02': p2, 'ENTR-13': p13,
        'CODIGOS_PROPUESTOS': "; ".join(c for _, c, _ in top),
        'MOTIVO_PROPUESTA': "; ".join(f"{c} ({p:.1f}): {'+'.join(w[:3])}" for p, c, w in top[:3]),
        'n_citas': len(citas),
        'entrevistas_que_lo_sostienen': "; ".join(sorted(evs)),
        'CODIGOS_VERIFICADOS': '',
        'VERIFICADO_POR': '',
        'ALERTA': " | ".join(alerta),
    })
    bloques.append((num, texto, p1, p2, p13, top, citas, alerta))

os.makedirs(os.path.dirname(SAL_CSV), exist_ok=True)
with open(SAL_CSV, 'w', newline='', encoding='utf-8-sig') as g:
    w = csv.DictWriter(g, fieldnames=list(filas[0].keys()), delimiter=';')
    w.writeheader(); w.writerows(filas)

# ---------- informe legible ----------
os.makedirs(os.path.dirname(SAL_MD), exist_ok=True)
with open(SAL_MD, 'w', encoding='utf-8') as g:
    g.write("# F2 — Trazabilidad del member checking\n\n")
    g.write(f"Ronda del {FECHA_ACTA}, doce enunciados, tres participantes "
            f"({', '.join(PARTICIPANTES)}).\n\n")
    g.write("Generado por `07_Datos/scripts/plan_mejora/trazabilidad_F2.py` sobre el "
            "libro de códigos v1.0 y los 213 fragmentos con cita literal verificada en C1. "
            "La correspondencia enunciado→código es una **propuesta**; la columna "
            "`CODIGOS_VERIFICADOS` la firma una persona.\n\n")
    g.write("| N.º | Enunciado | ENTR-01 | ENTR-02 | ENTR-13 | Códigos propuestos | Citas | Alerta |\n")
    g.write("|---:|---|:-:|:-:|:-:|---|---:|---|\n")
    for num, texto, p1, p2, p13, top, citas, alerta in bloques:
        g.write(f"| {num} | {texto} | {p1} | {p2} | {p13} | "
                f"{', '.join(c for _,c,_ in top) or '—'} | {len(citas)} | "
                f"{' · '.join(alerta) or ''} |\n")
    g.write("\n---\n\n## Citas literales que sostienen cada enunciado\n")
    for num, texto, p1, p2, p13, top, citas, alerta in bloques:
        g.write(f"\n### Enunciado {num} — {texto}\n\n")
        g.write(f"Posiciones: ENTR-01 `{p1}` · ENTR-02 `{p2}` · ENTR-13 `{p13}`\n\n")
        if alerta:
            g.write("> **" + " · ".join(alerta) + "**\n\n")
        if not citas:
            g.write("_Ninguna cita literal verificada corresponde a los códigos propuestos._\n")
            continue
        for cod, x in citas[:8]:
            g.write(f"- **{cod}** · {x['ev']} · `{x['trans']}` línea {x['linea']}"
                    f"{' · ' + x['rf'] if x['rf'] else ''}\n")
            g.write(f"  > {x['cita'][:300]}\n")
        if len(citas) > 8:
            g.write(f"\n_(y {len(citas)-8} citas más en el CSV)_\n")

print(f"Enunciados: {len(filas)}")
print(f"Codigos del libro: {len(CODIGOS)} | fragmentos con cita: {len(FRAG)}")
print(f"Sin cita que lo sostenga: {sum(1 for x in filas if 'SIN CITA' in x['ALERTA'])}")
print(f"Solo ENTR-13: {sum(1 for x in filas if 'SOLO EN ENTR-13' in x['ALERTA'])}")
print(f"Rechazados por alguien: {sum(1 for x in filas if 'RECHAZADO' in x['ALERTA'])}")
print(f"\nEscrito: {SAL_CSV}\n         {SAL_MD}")
