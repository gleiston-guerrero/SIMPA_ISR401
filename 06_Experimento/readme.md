# Componente experimental

Comparación de la calidad de requisitos funcionales elicitados por el equipo humano frente a los generados por un modelo grande de lenguaje a partir del mismo material fuente.

## Estado

**Experimento ejecutado y análisis principal completado.**

**Registro público OSF:** https://osf.io/4z35d/

El registro OSF es retrospectivo respecto a la recolección del material fuente de entrevistas y anterior a la ejecución del experimento comparativo humano–LLM.

La desviación metodológica respecto del diseño originalmente apareado se encuentra documentada en:

`06_Experimento/osf_deviations.md`

El protocolo registrado en OSF se conserva sin modificación retroactiva.

## Diseño ejecutado

El experimento utilizó:

- 25 requisitos funcionales del conjunto humano.
- 25 requisitos funcionales generados por el LLM.
- 50 requisitos cegados identificados como `R-001` a `R-050`.
- 3 evaluadores independientes: `EV-01`, `EV-02` y `EV-03`.
- 5 dimensiones de calidad:
  - COM: completitud.
  - AMB: ausencia de ambigüedad.
  - VER: verificabilidad.
  - COR: corrección respecto de la fuente.
  - CON: consistencia interna.
- Escala ordinal de 1 a 5.

Cada evaluador puntuó los 50 requisitos en las cinco dimensiones.

Total de observaciones:

`3 evaluadores × 50 requisitos × 5 dimensiones = 750 puntuaciones`

## Cegado y aleatorización

### Cegado histórico utilizado en la evaluación ejecutada

La evaluación original utilizó 50 requisitos cegados (`25 humanos + 25 LLM`),
identificados como `R-001` a `R-050`.

Semilla utilizada:

`20260912`

Archivo entregado a los evaluadores:

`06_Experimento/cegado/requisitos_cegados.csv`

Este archivo histórico fue incorporado en el commit `41618dd`
(`EXP-05: requisitos cegados listos para evaluación`) y se conserva sin
modificaciones para mantener la trazabilidad de la evaluación ya ejecutada.

La correspondencia entre el identificador cegado, su origen y el identificador
original se mantuvo fuera del repositorio público.

### Cegado correctivo posterior a A2

Después de A3 y A2, el conjunto disponible quedó formado por 22 requisitos
humanos reconstruidos desde ENTR-04 y 25 requisitos LLM, para un total de 47.

El script versionado:

`06_Experimento/scripts_analisis/cegar_aleatorizar.py`

toma ahora los dos artefactos normalizados de A2 y genera, con la misma semilla
`20260912`, un artefacto nuevo e independiente:

`06_Experimento/cegado/requisitos_cegados_A2.csv`

con identificadores `R-001` a `R-047`.

El mapa correspondiente se genera fuera del repositorio como
`mapa_origen_A2.csv`. Este cegado post-A2 no sustituye ni altera el archivo
histórico de 50 requisitos y queda preparado para una eventual repetición de
la evaluación conforme a A1.

## Evaluaciones

Las hojas individuales se encuentran en:

- `06_Experimento/evaluadores/EV-01_hoja_puntuacion.csv`
- `06_Experimento/evaluadores/EV-02_hoja_puntuacion.csv`
- `06_Experimento/evaluadores/EV-03_hoja_puntuacion.csv`

El consolidado de las 750 puntuaciones está en:

`06_Experimento/evaluadores/puntuaciones_reales.csv`

El dataset analítico después del descegado se encuentra en:

`07_Datos/datos_procesados/puntuaciones_experimento_con_origen.csv`

El script que genera y valida dicho dataset es:

`06_Experimento/scripts_analisis/preparar_datos_experimento.py`

## RQ2 — Acuerdo entre evaluadores

La medida principal fue el alfa de Krippendorff con métrica ordinal.

| Dimensión | Alfa de Krippendorff |
|---|---:|
| COM | -0.015110 |
| AMB | -0.003284 |
| VER | 0.027043 |
| COR | -0.002534 |
| CON | -0.015110 |

Los valores obtenidos muestran un acuerdo interevaluador muy bajo.

Como análisis secundario se calculó el kappa de Cohen ponderado cuadráticamente para cada par de evaluadores y para cada dimensión.

Archivos de resultados:

- `07_Datos/resultados/acuerdo_krippendorff.csv`
- `07_Datos/resultados/acuerdo_kappa_ponderado.csv`
- `07_Datos/resultados/metadatos_acuerdo.txt`

Script:

`06_Experimento/scripts_analisis/calcular_acuerdo_evaluadores.py`

El acuerdo bajo se conserva como resultado del experimento y debe discutirse como una limitación de medición y de validez de conclusión.

## RQ1 — Comparación Humano frente a LLM

El análisis principal siguió la desviación metodológica declarada antes de la recolección de puntuaciones.

Se ajustó un modelo ordinal mixto independiente para cada una de las cinco dimensiones:

`puntuacion ~ origen + (1 | evaluador) + (1 | requisito)`

Características del análisis:

- respuesta ordinal;
- enlace logit acumulativo;
- `Humano` como categoría de referencia;
- `origen` como efecto fijo;
- `evaluador` y `requisito` como interceptos aleatorios cruzados;
- implementación mediante `ordinal::clmm` en R;
- corrección Holm-Bonferroni sobre los cinco contrastes de origen.

Los cinco modelos finalizaron sin advertencias.

### Resultados

| Dimensión | OR LLM vs Humano | p crudo | p Holm |
|---|---:|---:|---:|
| COM | 0.765750 | 0.392092 | 1.000 |
| AMB | 0.753772 | 0.392934 | 1.000 |
| VER | 0.755302 | 0.413985 | 1.000 |
| COR | 0.738786 | 0.347637 | 1.000 |
| CON | 0.765750 | 0.392092 | 1.000 |

En las cinco dimensiones el odds ratio fue inferior a 1, lo que indica una tendencia estimada hacia puntuaciones menores para el conjunto LLM respecto del conjunto humano.

Sin embargo, ninguna diferencia fue estadísticamente significativa y todos los intervalos de confianza del odds ratio incluyeron 1.

Después de aplicar Holm-Bonferroni, los cinco valores p ajustados fueron 1.000.

Por tanto, con la muestra disponible no se encontró evidencia estadísticamente significativa de diferencias de calidad entre los requisitos humanos y los generados por el LLM.

Archivos:

- `07_Datos/resultados/comparacion_descriptiva.csv`
- `07_Datos/resultados/modelo_ordinal_mixto.csv`
- `07_Datos/resultados/resumen_modelos_ordinales.txt`
- `07_Datos/resultados/metadatos_modelo_ordinal.txt`

Script:

`06_Experimento/scripts_analisis/analizar_comparacion.R`

## Limitaciones

El estudio se limita a:

- un único material fuente;
- un dominio agroindustrial;
- un único modelo de lenguaje;
- 25 requisitos por grupo;
- tres evaluadores.

La aproximación de sensibilidad previamente documentada estimó una potencia aproximada de 0.41 con 25 requisitos por grupo para un efecto medio bajo un contraste convencional de grupos independientes.

El acuerdo interevaluador observado fue muy bajo.

Estas limitaciones deben conservarse en la interpretación de los resultados y no se ampliará la muestra ni se modificará el análisis después de observar los datos.

## Reproducibilidad

Los principales scripts del experimento son:

06_Experimento/scripts_analisis/
├── cegar_aleatorizar.py
├── preparar_datos_experimento.py
├── calcular_acuerdo_evaluadores.py
└── analizar_comparacion.R