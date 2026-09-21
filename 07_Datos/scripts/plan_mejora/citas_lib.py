#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
citas_lib.py  ·  C1 / C2 / B4 · SIMPA_ISR401

Biblioteca compartida (solo biblioteca estándar) para localizar citas literales
en las transcripciones. Existe porque, tras la retranscripción de B1, las
transcripciones tienen TRES formatos de hablante y los scripts de C1 solo
entendían uno:

    ENTR-01, 02, 08 :  [00:17] **Entrevistado:** texto
    ENTR-03 a 07    :  **[00:11] Entrevistado:** texto
    ENTR-09 a 16    :  **Entrevistado:** texto

Con el analizador antiguo (`linea.startswith("**Entrevistado:**")`) las ocho
entrevistas retranscritas quedaban con CERO turnos del entrevistado, de modo
que ninguna cita, ni siquiera una literal perfecta, podía verificarse.

Contrato de `turnos_de_entrevistado` (igual que en los scripts antiguos):
    devuelve [(numero_de_linea, linea, offset)]; la cita debe estar en
    linea[offset:], es decir, NUNCA en la etiqueta ni en la marca de tiempo.
"""
import difflib
import re
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
TRANSCRIPCIONES = RAIZ / "02_Evidencias" / "Transcripciones"

_TS = r"\[\d{1,2}:\d{2}(?::\d{2})?\]"
RE_TURNO = re.compile(
    rf"^(?:{_TS}\s*)?\*\*(?:{_TS}\s*)?(Entrevistado|Entrevistador):\*\*"
)
RE_ACOTACION = re.compile(r"^\s*\*?\(.*\)\*?\s*$")  # *(Sonidos de ...)*: no es habla


def turnos_de_entrevistado(texto):
    """[(n_linea, linea, offset)] de todo lo que dice el ENTREVISTADO."""
    salida, hablante = [], None
    for n, linea in enumerate(texto.splitlines(), start=1):
        m = RE_TURNO.match(linea)
        if m:
            hablante = "E" if m.group(1) == "Entrevistado" else "R"
            if hablante == "E":
                salida.append((n, linea, m.end()))
        elif linea.startswith("#") or linea.startswith("**Rol:**"):
            hablante = None
        elif linea.strip() and hablante == "E" and not RE_ACOTACION.match(linea):
            salida.append((n, linea, 0))
    return salida


def turnos_de_archivo(ruta):
    return turnos_de_entrevistado(Path(ruta).read_text(encoding="utf-8", errors="ignore"))


# ----------------------------------------------------------- similitud
VACIAS = set("""de la el los las un una unos unas y o u e en a al del que se su sus
lo le les por para con sin sobre es son ser esta este esto estos estas como mas muy
ya no si ha han hay tiene tienen tambien pero cuando donde segun entre hasta desde
cada todo toda todos todas otro otra otros otras mismo misma bueno entonces ahi asi
eso esa ese ahora aqui""".split())


def sin_tildes(s):
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def normalizar(s):
    return re.sub(r"\s+", " ", sin_tildes(s).lower()).strip()


def raices(s):
    """Raíces (5 primeras letras) de las palabras con contenido."""
    palabras = re.findall(r"[a-z0-9]+", normalizar(s))
    return {p[:5] for p in palabras if p not in VACIAS and len(p) > 2}


def puntuar(consulta, candidato, raices_c=None):
    raices_c = raices(consulta) if raices_c is None else raices_c
    if not raices_c:
        return 0.0
    cobertura = len(raices_c & raices(candidato)) / len(raices_c)
    parecido = difflib.SequenceMatcher(None, normalizar(consulta), normalizar(candidato)).ratio()
    return round(0.6 * cobertura + 0.4 * parecido, 3)


# ------------------------------------------------------------ ventanas
def _tramos_oracion(linea, desde):
    tramos, ini = [], desde
    for m in re.finditer(r"(?<=[.!?…])\s+", linea[desde:]):
        fin = desde + m.start()
        if linea[ini:fin].strip():
            tramos.append((ini, fin))
        ini = desde + m.end()
    if linea[ini:].strip():
        tramos.append((ini, len(linea)))
    return tramos


def _trocear(linea, a, b, maximo=300):
    """Si una 'oración' es un párrafo sin puntos, ofrece ventanas por comas."""
    if b - a <= maximo:
        return [(a, b)]
    cortes = [a] + [a + m.end() for m in re.finditer(r",\s+", linea[a:b])] + [b]
    ventanas = []
    for i in range(len(cortes) - 1):
        j = i + 1
        while j < len(cortes) and cortes[j] - cortes[i] <= maximo:
            j += 1
        j = max(j - 1, i + 1)
        ventanas.append((cortes[i], cortes[j]))
    return ventanas


def ventanas_de_linea(linea, off):
    tramos = _tramos_oracion(linea, off)
    v = []
    for a, b in tramos:
        v += _trocear(linea, a, b)
    v += [(tramos[i][0], tramos[i + 1][1]) for i in range(len(tramos) - 1)
          if tramos[i + 1][1] - tramos[i][0] <= 420]
    return v


def candidatas(turnos, consulta, extra="", k=3):
    """
    Top-k ventanas (subcadenas EXACTAS de un turno del entrevistado) más
    parecidas a `consulta`. `extra` (p. ej. la cita antigua, que era una versión
    depurada de lo dicho) refuerza la búsqueda: la puntuación es el promedio.
    Devuelve [(puntuacion, n_linea, texto)].
    """
    rc = raices(consulta)
    re_ = raices(extra) if extra else None
    hallazgos = []
    for n, linea, off in turnos:
        for a, b in ventanas_de_linea(linea, off):
            frase = linea[a:b].strip()
            if not 12 <= len(frase) <= 450:
                continue
            p = puntuar(consulta, frase, rc)
            if extra:
                p = round((p + puntuar(extra, frase, re_)) / 2, 3)
            hallazgos.append((p, n, frase))
    hallazgos.sort(key=lambda x: (-x[0], len(x[2])))
    elegidas, usadas = [], []
    for p, n, frase in hallazgos:
        if any(n == n2 and (frase in f2 or f2 in frase) for n2, f2 in usadas):
            continue
        elegidas.append((p, n, frase))
        usadas.append((n, frase))
        if len(elegidas) == k:
            break
    return elegidas
