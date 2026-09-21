# Resultados

Esta carpeta contiene resultados generados reproduciblemente por los scripts
versionados en `../scripts/`.

## Análisis de saturación temática

La ejecución vigente utiliza dos fuentes reales de codificación:

- `../datos_crudos/codificacion.csv`: primeras ocho entrevistas, estrato de dominio;
- `../datos_procesados/codificacion_tercera_ronda.csv`: `ENTR-09` a `ENTR-16`, estrato de contraste.

Los resultados vigentes son:

- `tabla_saturacion.csv`
- `curva_saturacion_dominio.png`
- `curva_saturacion_dominio.pdf`
- `curva_saturacion_contraste.png`
- `curva_saturacion_contraste.pdf`
- `curva_saturacion_agregada.png`
- `curva_saturacion_agregada.pdf`

Estos archivos se generan mediante:

`../scripts/curva_saturacion.py`

La ejecución verificada el 2026-09-21 (tras las tareas C1 y C2) produce:

- 124 fragmentos en dominio;
- 89 fragmentos en contraste;
- 213 fragmentos totales;
- 67 códigos únicos en dominio;
- 36 códigos únicos en contraste;
- 21 códigos compartidos entre los dos estratos;
- 15 códigos nuevos del contraste frente al dominio;
- 82 códigos únicos en la vista agregada.

`tabla_saturacion.csv` contiene 16 filas × 11 columnas.

## Interpretación

Las curvas de dominio y contraste deben interpretarse por separado.

La curva agregada se conserva únicamente como vista descriptiva de las 16
entrevistas. No debe utilizarse como prueba de saturación homogénea entre
poblaciones distintas.

Esta separación responde a la adenda A.14 y a la medida asociada al riesgo de
mezclar poblaciones con distinta relación con el dominio.

## Resultados anteriores

Los antiguos archivos genéricos:

- `curva_saturacion.png`
- `curva_saturacion.pdf`

correspondían exclusivamente al análisis de las primeras ocho entrevistas.

Se retiran de la carpeta de resultados al incorporar las tres curvas
estratificadas, para evitar mantener dos resultados vigentes con alcances
diferentes.

## Experimento humano–LLM

Esta carpeta reúne también los resultados reales del experimento comparativo
humano–LLM ejecutado con 25 requisitos humanos, 25 requisitos generados por el
modelo y tres evaluadores independientes.

Los principales artefactos experimentales son:

- `comparacion_descriptiva.csv`: estadísticos descriptivos por origen y dimensión;
- `modelo_ordinal_mixto.csv`: resultados de los cinco modelos ordinales mixtos;
- `metadatos_modelo_ordinal.txt`: información de ejecución y convergencia;
- `acuerdo_krippendorff.csv`: alfa de Krippendorff ordinal por dimensión;
- `acuerdo_kappa_ponderado.csv`: kappa de Cohen ponderado por pares de evaluadores;
- `metadatos_acuerdo.txt`: información del análisis de acuerdo.

Los scripts que generan estos resultados se encuentran en
`06_Experimento/scripts_analisis/`. Los archivos de curvas y saturación que
también residen en esta carpeta pertenecen al componente cualitativo de
entrevistas y se mantienen diferenciados de los resultados experimentales.

No se incorporan resultados hipotéticos ni cifras simuladas.
