#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B1 — Verificación de marcas de tiempo contra el audio real.

Comprueba, para una transcripción retranscrita desde audio:

  1. Que tenga marcas [mm:ss] con el formato correcto, al inicio de turno.
  2. Que las marcas sean crecientes (ninguna retrocede en el tiempo).
  3. Que la última marca coincida con la duración real del audio (±10 %,
     criterio de aceptación de B1).
  4. Densidad de muletillas detectadas, como indicio de literalidad (no es
     prueba definitiva: la lectura humana sigue siendo necesaria).
  5. Extrae el texto de cualquier ventana de 3 minutos que pidas, para que
     la compares de oído contra el audio (el 5 % de discrepancia de B1 no
     se puede automatizar: es una comprobación humana, esto solo te
     entrega el tramo exacto a revisar).

Requiere ffprobe (parte de ffmpeg) para leer la duración del audio.

Uso:

    python3 07_Datos/scripts/plan_mejora/verificar_retranscripcion_B1.py \
        <transcripcion.md> <audio.mp3> [--muestra 03:00]

El parámetro --muestra (opcional) marca el minuto:segundo donde empieza la
ventana de 3 minutos a extraer para la comprobación manual.
"""

import argparse
import re
import subprocess
import sys

PATRON_MARCA = re.compile(r"^\[(\d{2}):(\d{2})\]\s*(\*\*(Entrevistador|Entrevistado):\*\*)", re.M)
PATRON_MARCA_MAL = re.compile(r"\[(\d{1,2}):(\d{1,2})\]")

MULETILLAS = ["este", "o sea", "como que", "eh", "ehh", "mmm", "pues", "bueno", "digamos"]


def duracion_audio(ruta):
    try:
        salida = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", ruta],
            capture_output=True, text=True, check=True,
        )
    except FileNotFoundError:
        sys.exit("ERROR: ffprobe no está instalado. Instala ffmpeg antes de continuar.")
    except subprocess.CalledProcessError as e:
        sys.exit(f"ERROR: ffprobe no pudo leer '{ruta}': {e.stderr.strip()}")
    return float(salida.stdout.strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transcripcion")
    ap.add_argument("audio")
    ap.add_argument("--muestra", help="mm:ss donde empieza la ventana de 3 min a extraer")
    args = ap.parse_args()

    with open(args.transcripcion, encoding="utf-8") as f:
        texto = f.read()
    lineas = texto.splitlines()

    print("=" * 60)
    print("1. FORMATO DE LAS MARCAS")
    print("=" * 60)

    marcas_bien = list(PATRON_MARCA.finditer(texto))
    todas_las_marcas = list(PATRON_MARCA_MAL.finditer(texto))

    print(f"Marcas con formato correcto (al inicio del turno): {len(marcas_bien)}")
    print(f"Total de patrones [mm:ss] encontrados en el texto: {len(todas_las_marcas)}")
    if len(marcas_bien) < len(todas_las_marcas):
        print(f"  AVISO: {len(todas_las_marcas) - len(marcas_bien)} marca(s) no están "
              f"exactamente al inicio del turno (revisar formato).")

    if not marcas_bien:
        sys.exit("\nERROR: no se encontró ninguna marca [mm:ss] al inicio de turno. "
                  "Nada más que verificar hasta que existan marcas.")

    print()
    print("=" * 60)
    print("2. MARCAS CRECIENTES")
    print("=" * 60)
    segundos = [(int(m.group(1)) * 60 + int(m.group(2))) for m in marcas_bien]
    retrocesos = [(i, segundos[i - 1], segundos[i]) for i in range(1, len(segundos)) if segundos[i] < segundos[i - 1]]
    if retrocesos:
        print(f"ERROR: {len(retrocesos)} marca(s) retroceden en el tiempo:")
        for i, antes, despues in retrocesos[:5]:
            print(f"   marca #{i}: {antes}s -> {despues}s")
    else:
        print("OK: todas las marcas son crecientes.")

    print()
    print("=" * 60)
    print("3. ÚLTIMA MARCA vs DURACIÓN DEL AUDIO (criterio: ±10 %)")
    print("=" * 60)
    dur_audio = duracion_audio(args.audio)
    ultima_marca = segundos[-1]
    diferencia = abs(dur_audio - ultima_marca)
    margen = dur_audio * 0.10
    print(f"Duración real del audio : {dur_audio:.1f} s  ({dur_audio/60:.1f} min)")
    print(f"Última marca de tiempo  : {ultima_marca} s  ({ultima_marca/60:.1f} min)")
    print(f"Diferencia              : {diferencia:.1f} s")
    print(f"Margen permitido (10 %) : {margen:.1f} s")
    if diferencia <= margen:
        print("RESULTADO: OK, dentro del margen del 10 %.")
    else:
        print("RESULTADO: FUERA de margen. Revisar si faltó transcribir el final "
              "del audio, o si alguna marca está mal escrita.")

    print()
    print("=" * 60)
    print("4. DENSIDAD DE MULETILLAS (indicio, no prueba)")
    print("=" * 60)
    texto_min = texto.lower()
    total_turnos_entrevistado = len(re.findall(r"\*\*Entrevistado:\*\*", texto))
    turnos_con_muletilla = 0
    for bloque in re.split(r"\*\*Entrevistado:\*\*", texto)[1:]:
        siguiente = bloque.split("**Entrevistador:**")[0]
        if any(m in siguiente.lower() for m in MULETILLAS):
            turnos_con_muletilla += 1
    if total_turnos_entrevistado:
        pct = 100 * turnos_con_muletilla / total_turnos_entrevistado
        print(f"Turnos del entrevistado con al menos una muletilla: "
              f"{turnos_con_muletilla}/{total_turnos_entrevistado} ({pct:.0f} %)")
        print("Referencia del defecto original: 0 % en las 8 de ronda 1-2 "
              "frente a 6-69 % en ronda 3. Un valor en 0 % aquí es señal de alerta.")
    else:
        print("No se encontraron turnos de Entrevistado para medir.")

    if args.muestra:
        print()
        print("=" * 60)
        print(f"5. VENTANA DE 3 MINUTOS DESDE {args.muestra}")
        print("=" * 60)
        mm, ss = args.muestra.split(":")
        inicio = int(mm) * 60 + int(ss)
        fin = inicio + 180
        print(f"Reproduce el audio de {args.muestra} a "
              f"{fin//60:02d}:{fin%60:02d} y compara de oído contra este tramo:")
        print()
        dentro = False
        for m in PATRON_MARCA.finditer(texto):
            s = int(m.group(1)) * 60 + int(m.group(2))
            if inicio <= s <= fin:
                dentro = True
                idx = m.start()
                fin_linea = texto.find("\n\n", idx)
                print(texto[idx:fin_linea if fin_linea > 0 else idx + 300].strip())
                print()
        if not dentro:
            print("(no hay marcas de turno dentro de esa ventana — revisa el minuto indicado)")


if __name__ == "__main__":
    main()
