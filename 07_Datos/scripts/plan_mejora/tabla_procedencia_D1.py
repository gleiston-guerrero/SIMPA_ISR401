#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
D1 — Tabla de procedencia de TODOS los requisitos (RF, RNF y RNF-IA).

Deriva del propio repositorio, sin inventar nada:
  - el catalogo completo de requisitos y la evidencia que cada uno cita;
  - la fecha de cada evidencia, tomada del apendice del ERS;
  - el commit en que cada requisito aparece por primera vez (git log -S);
  - una CLASIFICACION PROPUESTA con el motivo que la sustenta.

La clasificacion es una PROPUESTA derivada de reglas explicitas. La columna
CLASIFICACION_VERIFICADA la rellena una persona. Nada se marca como
verificado por el script.
"""
import csv, re, subprocess, os, sys
from datetime import datetime

ERS   = "01_ERS/ERS_SRS_2B_v2.0.tex"
IA    = "01_ERS/seccion9_ia.tex"
APEND = "01_ERS/apendices.tex"
PROPUESTA = "01_ERS/antecedentes/2026-05-05_Propuesta_Inicial_1A.pdf"
FECHA_PROPUESTA = "2026-05-05"

# Requisitos que el Plan de mejora de datos (19/09/2026) senala expresamente
# como ya presentes en la propuesta del 05/05, antes de la primera entrevista.
# Se incorporan aqui para que la deteccion automatica no los pierda.
SENALADOS_DOCENTE = {"RF-03","RF-07","RF-08","RF-18"}
SALIDA= "07_Datos/datos_procesados/tabla_procedencia_requisitos.csv"

def leer(p): return open(p, encoding="utf-8").read()

# ---------- fechas de evidencia ----------
FECHA_EV = {}
for m in re.finditer(r"\\id\{(EV-\d+)\}\s*&\s*([^&]+?)\s*&\s*([^&]+?)\s*&", leer(APEND)):
    ev, tipo, fecha = m.group(1), m.group(2).strip(), m.group(3).strip()
    if ev not in FECHA_EV:
        FECHA_EV[ev] = (tipo, fecha)

def fecha_iso(txt):
    m = re.search(r"(\d{2})/(\d{2})/(\d{4})", txt or "")
    return f"{m.group(3)}-{m.group(2)}-{m.group(1)}" if m else ""

# ---------- modulos de la propuesta inicial (05/05/2026) ----------
# Se comparan las palabras significativas del nombre del requisito con el texto
# de cada modulo. El resultado es una PROPUESTA de correspondencia, no un juicio.
MODULOS = []
try:
    _t = subprocess.run(["pdftotext","-layout",PROPUESTA,"-"],
                        capture_output=True, text=True, timeout=60).stdout
    for _s in re.split(r"\n(?=\d+\.\d+\s)", _t):
        _m = re.match(r"(\d+\.\d+)\s+(.+)", _s)
        if _m:
            MODULOS.append((_m.group(1), _m.group(2).strip(),
                            re.sub(r"\s+"," ",_s).lower()))
except Exception:
    pass

_STOP = set("de la el en y a los las del que se un una por con para es su al lo como mas o "
            "sistema debe permitir gestion registro control".split())

def en_propuesta(nombre):
    pal = {w for w in re.sub(r"[^a-zA-ZáéíóúñÁÉÍÓÚÑ ]"," ",nombre.lower()).split()
           if len(w) > 4 and w not in _STOP}
    if not pal: return ""
    mejor = (0, "")
    for num, tit, cuerpo in MODULOS:
        n = sum(1 for w in pal if w[:6] in cuerpo)
        if n > mejor[0]: mejor = (n, f"{num} {tit}")
    return mejor[1] if mejor[0] >= 2 else ""

# ---------- commit de alta ----------
CACHE = {}
def commit_alta(rid, ficheros):
    if rid in CACHE: return CACHE[rid]
    try:
        out = subprocess.run(
            ["git","log","--reverse","--format=%h|%ad","--date=short","-S",rid,"--"]+ficheros,
            capture_output=True, text=True, timeout=90).stdout.strip().splitlines()
        CACHE[rid] = out[0] if out else "|"
    except Exception:
        CACHE[rid] = "|"
    return CACHE[rid]

# ---------- catalogo ----------
reqs = []
t_ers = leer(ERS)

for m in re.finditer(r"\\RF\{(RF-\d+)\}\{([^}]*)\}\s*\{(.*?)\}\s*\{(.*?)\}", t_ers, re.S):
    reqs.append({"id":m.group(1),"tipo":"RF","nombre":m.group(2).strip(),
                 "origen_ers":re.sub(r"\s+"," ",m.group(4)).strip(),"fuente":ERS})

for m in re.finditer(r"\\id\{(RNF-\d+)\}\s*&\s*([^&]+?)\s*&(.*?)\\\\ *\\hline", t_ers, re.S):
    cuerpo = m.group(3)
    reqs.append({"id":m.group(1),"tipo":"RNF","nombre":m.group(2).strip(),
                 "origen_ers":re.sub(r"\s+"," ",cuerpo.split("&")[-1]).strip(),"fuente":ERS})

t_ia = leer(IA)
for m in re.finditer(r"\\id\{(RNF-IA-\d+)\}\s*&\s*([^&]+?)\s*&(.*?)\\\\ *\\hline", t_ia, re.S):
    reqs.append({"id":m.group(1),"tipo":"RNF-IA","nombre":m.group(2).strip(),
                 "origen_ers":re.sub(r"\s+"," ",m.group(3)).strip(),"fuente":IA})

vistos=set(); uniq=[]
for r in reqs:
    if r["id"] not in vistos: vistos.add(r["id"]); uniq.append(r)
reqs = uniq

# ---------- clasificacion propuesta ----------
NORMA = re.compile(r"LOPDP|ISO|IEC|25010|29148|legal|normativ", re.I)
filas=[]
for r in reqs:
    evs = sorted(set(re.findall(r"EV-\d+", r["origen_ers"])), key=lambda x:int(x.split("-")[1]))
    refs = sorted(set(re.findall(r"(?:RF|RNF|RD|L)-(?:IA-)?\d+", r["origen_ers"])) - {r["id"]})
    sha, falta = (commit_alta(r["id"], [r["fuente"]]).split("|")+[""])[:2]

    fechas=[fecha_iso(FECHA_EV.get(e,("",""))[1]) for e in evs]
    fechas=[f for f in fechas if f]
    f_ev = min(fechas) if fechas else ""

    if evs:
        clas, motivo = "elicitado", f"cita evidencia: {', '.join(evs)}"
    elif NORMA.search(r["origen_ers"]+" "+r["nombre"]):
        clas, motivo = "normativo", "el origen declarado invoca norma o marco legal"
    elif refs:
        clas, motivo = "derivado", f"se apoya en: {', '.join(refs)}"
    else:
        clas, motivo = "propuesta_equipo", "no declara evidencia ni norma ni requisito previo"

    modulo = en_propuesta(r["nombre"])
    if r["id"] in SENALADOS_DOCENTE and not modulo:
        modulo = "senalado en el plan de mejora (correspondencia a verificar)"

    alerta=""
    if modulo and f_ev and FECHA_PROPUESTA < f_ev:
        alerta = (f"FUNCIONALIDAD YA EN LA PROPUESTA DEL {FECHA_PROPUESTA} "
                  f"({modulo}), anterior a su evidencia {f_ev}")
    if f_ev and falta and falta < f_ev:
        alerta = f"REQUISITO ANTERIOR A SU EVIDENCIA (alta {falta} < evidencia {f_ev})"
    if not evs and r["tipo"]=="RF":
        alerta = (alerta+" | " if alerta else "")+"RF sin evidencia citada"

    filas.append({"id_requisito":r["id"],"tipo":r["tipo"],"nombre":r["nombre"][:120],
        "evidencias_citadas":"; ".join(evs),
        "fecha_evidencia_mas_antigua":f_ev,
        "tipo_evidencia":"; ".join(FECHA_EV.get(e,("",""))[0] for e in evs),
        "commit_alta":sha,"fecha_commit_alta":falta,
        "CLASIFICACION_PROPUESTA":clas,"MOTIVO_PROPUESTA":motivo,
        "en_propuesta_inicial":modulo,
        "CLASIFICACION_VERIFICADA":"","VERIFICADO_POR":"",
        "ALERTA":alerta,"origen_completo_ers":r["origen_ers"][:300]})

filas.sort(key=lambda x:(x["tipo"],int(re.search(r"(\d+)$",x["id_requisito"]).group(1))))
os.makedirs(os.path.dirname(SALIDA), exist_ok=True)
with open(SALIDA,"w",newline="",encoding="utf-8-sig") as f:
    w=csv.DictWriter(f,fieldnames=list(filas[0].keys()),delimiter=";")
    w.writeheader(); w.writerows(filas)

import collections
print(f"Requisitos: {len(filas)}  ->  {dict(collections.Counter(x['tipo'] for x in filas))}")
print(f"Clasificacion propuesta: {dict(collections.Counter(x['CLASIFICACION_PROPUESTA'] for x in filas))}")
al=[x for x in filas if x["ALERTA"]]
print(f"En la propuesta del 05/05: {sum(1 for x in filas if x['en_propuesta_inicial'])}")
print(f"Con alerta: {len(al)}")
for x in al: print(f"   {x['id_requisito']:11s} {x['ALERTA'][:96]}")
print(f"\nEscrito: {SALIDA}")
