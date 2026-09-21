# Datos procesados

Esta carpeta contiene conjuntos derivados y documentados utilizados por la
cadena reproducible de `07_Datos/`.

## Contenido actual

| Dato | Naturaleza | Generación / procedencia |
|---|---|---|
| `respuestas_anonimizadas.csv` | Cuestionario anonimizado, 62 filas × 34 columnas | Generado por `../scripts/anonimizar_encuesta.py` desde el XLSX crudo |
| `respuestas_zenodo_agregadas.csv` | Distribuciones agregadas para publicación, 64 filas × 7 columnas | Generado por `../scripts/preparar_dataset_zenodo_agregado.py` |
| `codificacion_tercera_ronda.csv` | Codificación temática de `ENTR-09` a `ENTR-16`, 89 fragmentos | Elaborada a partir de transcripciones anonimizadas y revisada de forma cruzada |

También se conserva:

`diccionario_codificacion_tercera_ronda.csv`

como diccionario específico del bloque de codificación de tercera ronda.

## Codificación de tercera ronda

`codificacion_tercera_ronda.csv` contiene:

- 8 entrevistas;
- 89 fragmentos;
- 36 códigos distintos (31 en la versión del 07/09/2026; se normalizaron al libro de códigos v1.0 el 20/09/2026);
- 21 códigos compartidos con la codificación histórica;
- 15 códigos nuevos frente al estrato de dominio;
- analista `AVR`.

Su fuente documental son las transcripciones anonimizadas versionadas en
`02_Evidencias/Transcripciones/`.

Se integra a la cadena mediante `../scripts/curva_saturacion.py`.

## Regla de reproducibilidad

Las transformaciones automáticas deben poder regenerarse desde su fuente y el
script correspondiente.

La codificación temática es un producto analítico humano: no se presenta como
salida automática. Su trazabilidad se mantiene mediante los fragmentos
codificados, el identificador de entrevista y el analista registrado.

## Experimento humano–LLM

Los conjuntos analíticos específicos del experimento comparativo permanecen
pendientes porque dicho experimento todavía no ha sido ejecutado completamente.

No se crean datasets sintéticos para sustituir esa evidencia.
