#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
E2 - Cobertura real de los RF Must en el prototipo entregado.

El repositorio declaraba 20 de 24 RF Must cubiertos, sin que esa cifra
saliera de ningun calculo reproducible. Este script la deriva del codigo.

QUE SIGNIFICA CADA CATEGORIA, Y POR QUE IMPORTA
-----------------------------------------------
El prototipo rotula cada pantalla con los requisitos que dice cubrir:

    shell('Plantaciones y lotes', 'RF-02 · RF-06 · RF-10 · estructura productiva', ...)

Ese rotulo es una DECLARACION del equipo dentro del codigo, no una prueba de
que el requisito funcione. Por eso el script no dice "cubierto":

  DECLARADO_EN_PANTALLA  el identificador aparece en el rotulo de una pantalla.
                         Es lo que el prototipo dice cubrir.
  EJERCITADO_EN_E1       ademas, la prueba de extremo a extremo de la tarea E1
                         lo ejecuto y registro su resultado observado.
  SOLO_INDICIO           no se cita el identificador, pero hay una pantalla o
                         funcion cuyo nombre coincide con el del requisito.
  SIN_MENCION            no aparece ni el identificador ni el nombre.

Solo EJERCITADO_EN_E1 sostiene una afirmacion de cobertura funcional.

La columna COBERTURA_VERIFICADA la rellena una persona abriendo la pantalla
citada. Nada se marca como verificado por el script.

Uso:
    python3 cobertura_rf_must_E2.py [ruta_del_prototipo]

Por defecto 05_MVP/prototipo. Si el submodulo no esta descargado:
    git submodule update --init 05_MVP/prototipo
"""
import re, os, sys, csv, unicodedata, collections

ERS    = "01_ERS/ERS_SRS_2B_v2.0.tex"
PROTO  = sys.argv[1] if len(sys.argv) > 1 else "05_MVP/prototipo"
SALIDA = "07_Datos/datos_procesados/cobertura_rf_must_E2.csv"
INFORME= "07_Datos/resultados/cobertura_rf_must_E2.md"
EXT    = ('.tsx', '.ts', '.jsx', '.js', '.html')

# Requisitos ejercitados y con resultado registrado en la prueba E2E de E1
# (05_MVP/evidencia_e2e/registro_prueba_e2e.md).
EJERCITADOS_E1 = {"RF-01", "RF-22", "RF-40", "RF-41", "RF-42"}

def norm(s):
    s = unicodedata.normalize('NFD', str(s or ''))
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn').lower()

STOP = set("""de la el en y a los las del que se un una por con para es su al lo como mas o
sistema debe permitir sobre cada desde entre segun entrada salida persona usuaria""".split())

def terminos(s):
    return [w for w in re.split(r'[^a-z]+', norm(s)) if len(w) > 4 and w not in STOP]

# ---------- RF Must del ERS ----------
def arg_bal(t, i):
    if i >= len(t) or t[i] != '{': return None, i
    p, j = 0, i
    while j < len(t):
        c = t[j]
        if c == '\\': j += 2; continue
        if c == '{': p += 1
        elif c == '}':
            p -= 1
            if p == 0: return t[i+1:j], j+1
        j += 1
    return None, i

t_ers = open(ERS, encoding='utf-8').read()
MUST = []
for m in re.finditer(r'\\RF\s*(?=\{)', t_ers):
    i, a = m.end(), []
    for _ in range(8):
        while i < len(t_ers) and t_ers[i] in ' \t\r\n': i += 1
        v, i = arg_bal(t_ers, i)
        if v is None: break
        a.append(v)
    if len(a) == 8 and re.fullmatch(r'RF-\d+', a[0].strip()) and 'must' in a[6].lower():
        MUST.append((a[0].strip(), re.sub(r'\s+', ' ', a[1]).strip()))

# ---------- codigo del prototipo ----------
if not os.path.isdir(PROTO):
    sys.exit(f"ERROR: no encuentro el prototipo en {PROTO}\n"
             f"       git submodule update --init 05_MVP/prototipo")

LINEAS = []
for raiz, dirs, fich in os.walk(PROTO):
    dirs[:] = [d for d in dirs if d not in ('.git', 'node_modules', 'dist', 'build')]
    for f in fich:
        if f.endswith(EXT):
            ruta = os.path.join(raiz, f)
            try:
                for n, l in enumerate(open(ruta, encoding='utf-8', errors='ignore'), 1):
                    LINEAS.append((os.path.relpath(ruta, PROTO), n, l.rstrip()))
            except Exception:
                pass
if not LINEAS:
    sys.exit(f"ERROR: no hay codigo legible en {PROTO}")

# ---------- pantallas y los RF que cada una rotula ----------
PANTALLA = {}    # RF -> [nombres de pantalla]
DONDE    = {}    # RF -> [archivo:linea]
for r, n, l in LINEAS:
    for m in re.finditer(r"shell\(\s*'([^']*)'\s*,\s*'([^']*)'", l):
        titulo, rotulo = m.group(1), m.group(2)
        for rid in re.findall(r'(?<![A-Za-z])RF-\d+(?![\w-])', rotulo):
            PANTALLA.setdefault(rid, [])
            if titulo not in PANTALLA[rid]:
                PANTALLA[rid].append(titulo)
            DONDE.setdefault(rid, []).append(f"{r}:{n}")

NORM = [(r, n, norm(l)) for r, n, l in LINEAS]

filas = []
for rid, nombre in MUST:
    pantallas = PANTALLA.get(rid, [])
    if pantallas and rid in EJERCITADOS_E1:
        cob = "EJERCITADO_EN_E1"
        motivo = ("rotulado en la pantalla «" + " / ".join(pantallas) +
                  "» y ejecutado con resultado registrado en la prueba E2E de E1")
        ev = "; ".join(sorted(set(DONDE.get(rid, [])))[:2])
    elif rid in EJERCITADOS_E1:
        cob = "EJERCITADO_EN_E1"
        motivo = "ejecutado con resultado registrado en la prueba E2E de E1, sin rotulo en pantalla"
        ev = "05_MVP/evidencia_e2e/registro_prueba_e2e.md"
    elif pantallas:
        cob = "DECLARADO_EN_PANTALLA"
        motivo = "el codigo lo rotula en la pantalla «" + " / ".join(pantallas) + "»"
        ev = "; ".join(sorted(set(DONDE.get(rid, [])))[:2])
    else:
        tn = terminos(nombre)
        marcas = collections.Counter()
        for r, n, l in NORM:
            k = sum(1 for w in tn if w[:7] in l)
            if k >= 2:
                marcas[(r, n)] = k
        mej = marcas.most_common(2)
        if mej:
            cob = "SOLO_INDICIO"
            motivo = "no se cita el identificador; coincide el nombre del requisito"
            ev = "; ".join(f"{r}:{n}" for (r, n), _ in mej)
        else:
            cob = "SIN_MENCION"
            motivo = "ni el identificador ni el nombre del requisito aparecen en el codigo"
            ev = ""

    filas.append({'id_requisito': rid, 'nombre': nombre[:110],
                  'COBERTURA_PROPUESTA': cob, 'MOTIVO_PROPUESTA': motivo,
                  'pantalla': " / ".join(pantallas), 'evidencia_archivo_linea': ev,
                  'COBERTURA_VERIFICADA': '', 'VERIFICADO_POR': ''})

filas.sort(key=lambda x: int(x['id_requisito'].split('-')[1]))
os.makedirs(os.path.dirname(SALIDA), exist_ok=True)
with open(SALIDA, 'w', newline='', encoding='utf-8-sig') as g:
    w = csv.DictWriter(g, fieldnames=list(filas[0].keys()), delimiter=';')
    w.writeheader(); w.writerows(filas)

c = collections.Counter(x['COBERTURA_PROPUESTA'] for x in filas)
decl = c.get('DECLARADO_EN_PANTALLA', 0) + c.get('EJERCITADO_EN_E1', 0)

os.makedirs(os.path.dirname(INFORME), exist_ok=True)
with open(INFORME, 'w', encoding='utf-8') as g:
    g.write("# E2 — Cobertura de los RF Must en el prototipo\n\n")
    g.write(f"Prototipo analizado: `{PROTO}` · {len(LINEAS)} líneas en "
            f"{len(set(r for r, _, _ in LINEAS))} archivos.\n\n")
    g.write(f"**RF con prioridad Must en el ERS: {len(MUST)}.**\n\n")
    g.write("| Categoría | RF | Qué sostiene |\n|---|---:|---|\n")
    g.write(f"| EJERCITADO_EN_E1 | {c.get('EJERCITADO_EN_E1',0)} | "
            "ejecutado con resultado observado y registrado |\n")
    g.write(f"| DECLARADO_EN_PANTALLA | {c.get('DECLARADO_EN_PANTALLA',0)} | "
            "el código lo rotula, pero nadie ha comprobado que funcione |\n")
    g.write(f"| SOLO_INDICIO | {c.get('SOLO_INDICIO',0)} | coincidencia de nombre, nada más |\n")
    g.write(f"| SIN_MENCION | {c.get('SIN_MENCION',0)} | no aparece en el código |\n")
    g.write(f"\n**Cifra reproducible:** {decl} de {len(MUST)} RF Must aparecen declarados en "
            f"el rótulo de alguna pantalla del prototipo; de ellos, "
            f"**{c.get('EJERCITADO_EN_E1',0)} han sido ejercitados** con resultado "
            f"registrado en la prueba de extremo a extremo de E1. "
            f"El resto no tiene comprobación de funcionamiento.\n\n")
    g.write("| RF | Nombre | Categoría | Pantalla | Evidencia |\n|---|---|---|---|---|\n")
    for x in filas:
        g.write(f"| {x['id_requisito']} | {x['nombre'][:46]} | {x['COBERTURA_PROPUESTA']} "
                f"| {x['pantalla'][:32]} | `{x['evidencia_archivo_linea'][:46]}` |\n")

print(f"RF Must en el ERS: {len(MUST)}")
print(f"Codigo analizado: {len(LINEAS)} lineas")
print(f"Reparto: {dict(c)}")
print(f"Declarados en pantalla: {decl} de {len(MUST)}")
print(f"Ejercitados en E1:      {c.get('EJERCITADO_EN_E1',0)} de {len(MUST)}")
print(f"\nEscrito: {SALIDA}\n         {INFORME}")
