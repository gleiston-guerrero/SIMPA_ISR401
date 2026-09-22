# Scripts de datos y análisis

Esta carpeta contiene las copias canónicas de los scripts reproducibles
utilizados por `07_Datos/`.

## Ejecución principal

Desde la raíz del repositorio:

```bash
python 07_Datos/scripts/run_all.py
```

El orquestador ejecuta:

1. `anonimizar_encuesta.py`
2. `preparar_dataset_zenodo_agregado.py`
3. `curva_saturacion.py`

La ejecución reproduce y verifica los datasets procesados y los resultados de
saturación disponibles.

## Scripts

- `run_all.py`: punto de entrada único de la cadena reproducible.
- `anonimizar_encuesta.py`: genera `respuestas_anonimizadas.csv`.
- `preparar_dataset_zenodo_agregado.py`: genera el dataset agregado de Zenodo.
- `curva_saturacion.py`: integra los dos bloques reales de codificación y genera
  la tabla de 16 entrevistas y tres curvas de saturación.
- `generar_fichas.py`: utilidad para fichas técnicas de archivos audiovisuales.

`generar_fichas.py` no forma parte de la ejecución automática de `run_all.py`
porque requiere como entrada material audiovisual y pertenece al flujo de
documentación de evidencias.

## Análisis de saturación

`curva_saturacion.py` utiliza:

- `../datos_crudos/codificacion.csv` para el estrato de dominio;
- `../datos_procesados/codificacion_tercera_ronda.csv` para el estrato de contraste.

Genera:

- `../resultados/tabla_saturacion.csv`
- `../resultados/curva_saturacion_dominio.png/.pdf`
- `../resultados/curva_saturacion_contraste.png/.pdf`
- `../resultados/curva_saturacion_agregada.png/.pdf`

La vista agregada es descriptiva; dominio y contraste se interpretan
separadamente.

## Estado

La cadena ampliada fue ejecutada y verificada localmente el 2026-09-07.

La verificación confirmó:

- 62 × 34 en respuestas anonimizadas;
- 64 × 7 en el dataset agregado de Zenodo;
- 16 × 11 en la tabla de saturación;
- 79 códigos únicos agregados (cifra del paquete congelado de Zenodo; el repositorio vivo tiene hoy 82 tras C2);
- conservación del SHA-256 publicado del dataset Zenodo.

El experimento comparativo humano–LLM fue ejecutado y analizado mediante los
scripts específicos de `06_Experimento/scripts_analisis/`. El orquestador
`run_all.py` mantiene un alcance separado y no ejecuta actualmente esa cadena
experimental. Los resultados experimentales reales se conservan en
`../resultados/` y el dataset analítico en `../datos_procesados/`.
