# Datos y cadena de análisis — SIMPA

Proyecto SIMPA — Sistema Inteligente de Mantenimiento de Palma Africana
Equipo AHMRV — Universidad Técnica Estatal de Quevedo

## 1. Propósito

La carpeta `07_Datos/` concentra los datos utilizados por el proyecto, sus
transformaciones reproducibles, los scripts de análisis y los resultados
derivados.

La separación estructural del repositorio es:

- `06_Experimento/`: diseño del estudio, protocolo, registro OSF, instrumentos
  y procedimiento experimental.
- `07_Datos/`: datos crudos, datos procesados, scripts, resultados y
  documentación de reproducibilidad.
- `08_Publicacion/`: manuscrito y artefactos relacionados con publicación.

Los datos y la cadena de análisis se centralizan aquí para evitar múltiples
copias canónicas del mismo insumo.

## 2. Estructura

El primer nivel de esta carpeta está definido como:

- `datos_crudos/`
- `datos_procesados/`
- `scripts/`
- `resultados/`
- `diccionario_datos.csv`
- `README_datos.md`
- `LICENSE-DATA.txt`
- `checksums_datos.sha256`
- `desviaciones.md`
- `registro_deposito.md`

## 3. Fuentes de datos

### 3.1 Cuestionario

Archivo:

`datos_crudos/Sistema Inteligente de Mantenimiento de Palma Africana(1-62).xlsx`

Corresponde a la exportación primaria del cuestionario aplicado a 62
participantes.

Se conserva para trazabilidad y reproducibilidad, pero está excluido del
depósito abierto. Consulte `LICENSE-DATA.txt`.

### 3.2 Codificación temática histórica — estrato de dominio

Archivo:

`datos_crudos/codificacion.csv`

Contiene la codificación histórica de las primeras ocho entrevistas. Su
ubicación se conserva por trazabilidad histórica; aunque se encuentra bajo
`datos_crudos/`, se reconoce que es un artefacto analítico derivado y no una
captura primaria sin transformación.

Esta fuente contiene:

- 8 entrevistas de dominio;
- 124 fragmentos codificados (138 hasta el 21/09/2026; ver tarea C2);
- 67 códigos únicos (68 hasta esa fecha).

Para el análisis actual, los identificadores históricos `EV-01` a `EV-08` se
mapean únicamente en la salida analítica a `ENTR-01` a `ENTR-08`. El archivo
histórico no se reescribe.

### 3.3 Codificación temática de tercera ronda — estrato de contraste

Archivo:

`datos_procesados/codificacion_tercera_ronda.csv`

Contiene la codificación de `ENTR-09` a `ENTR-16`, revisada de forma cruzada
antes de integrarla al análisis de saturación.

Esta fuente contiene:

- 8 entrevistas de contraste;
- 89 fragmentos codificados;
- 36 códigos temáticos distintos (31 en la versión del 07/09/2026; el 20/09/2026 la codificación se normalizó al libro de códigos v1.0);
- 21 códigos compartidos con el estrato de dominio;
- 15 códigos que aparecen por primera vez en el estrato de contraste.

El identificador del analista de este bloque es `AVR`.

## 4. Datos procesados

### 4.1 Respuestas anonimizadas

Archivo:

`datos_procesados/respuestas_anonimizadas.csv`

Se genera desde el XLSX crudo mediante:

`07_Datos/scripts/anonimizar_encuesta.py`

La ejecución vigente produce:

- 62 filas;
- 34 columnas.

El procesamiento elimina columnas identificativas y artefactos del formulario
sin imputar ni modificar las respuestas sustantivas.

### 4.2 Dataset agregado para Zenodo

Archivo:

`datos_procesados/respuestas_zenodo_agregadas.csv`

Se genera mediante:

`07_Datos/scripts/preparar_dataset_zenodo_agregado.py`

El conjunto contiene:

- 62 participantes de origen;
- 15 preguntas sustantivas;
- 64 filas agregadas;
- 7 columnas.

Ninguna fila del conjunto agregado representa a una persona individual.

El depósito se documenta en `registro_deposito.md`.

## 5. Scripts

Los scripts reproducibles se encuentran en:

`07_Datos/scripts/`

Actualmente incluyen:

- `anonimizar_encuesta.py`
- `preparar_dataset_zenodo_agregado.py`
- `curva_saturacion.py`
- `run_all.py`
- `generar_fichas.py`

`run_all.py` es el punto de entrada de la cadena reproducible.

## 6. Resultados del análisis de saturación

Los resultados reproducibles se encuentran en:

`07_Datos/resultados/`

La ejecución actual genera:

- `tabla_saturacion.csv`
- `curva_saturacion_dominio.png`
- `curva_saturacion_dominio.pdf`
- `curva_saturacion_contraste.png`
- `curva_saturacion_contraste.pdf`
- `curva_saturacion_agregada.png`
- `curva_saturacion_agregada.pdf`

Se regeneran mediante:

`07_Datos/scripts/curva_saturacion.py`

### 6.1 Resultado global verificado

La ejecución del 2026-09-21 (tras las tareas C1 y C2) produjo:

- 124 fragmentos en el estrato de dominio;
- 89 fragmentos en el estrato de contraste;
- 213 fragmentos en total;
- 67 códigos únicos en dominio;
- 36 códigos únicos en contraste;
- 21 códigos compartidos entre ambos estratos;
- 15 códigos nuevos exclusivos del contraste frente al dominio;
- 82 códigos únicos en la vista agregada.

### 6.2 Interpretación por estratos

La adenda A.14 establece que la mezcla indiferenciada de poblaciones puede
introducir una inflexión artificial en la curva de saturación.

Por esa razón se reportan tres vistas:

1. **Estrato de dominio:** `ENTR-01` a `ENTR-08`.
2. **Estrato de contraste:** `ENTR-09` a `ENTR-16`.
3. **Vista agregada:** las 16 entrevistas en orden, utilizada únicamente como
   descripción global.

La vista agregada no se interpreta como evidencia de una saturación homogénea
entre poblaciones distintas.

La clasificación adicional como técnico/no técnico no se infiere a partir del
cargo o condición de docente/estudiante.

## 7. Experimento humano–LLM

El diseño y protocolo del experimento comparativo se encuentran en:

`06_Experimento/`

El experimento principal todavía no ha sido ejecutado completamente.

Por esta razón, no se presentan como resultados reales:

- evaluación a ciegas completa;
- comprobación de ceguera;
- kappa con intervalo de confianza;
- tamaño del efecto con IC del 95 %;
- análisis estadístico final del experimento.

Los resultados de `07_Datos/resultados/` corresponden al análisis cualitativo
de entrevistas y no al experimento comparativo humano–LLM.

No se generan cifras hipotéticas o simuladas para completar esos entregables.

## 8. Diccionario de datos

El archivo:

`diccionario_datos.csv`

documenta los conjuntos de datos y resultados utilizados por la cadena
reproducible.

Tras integrar la tercera ronda y la tabla de saturación estratificada, el
diccionario cubre 64 columnas pertenecientes a cinco conjuntos:

- `respuestas_anonimizadas.csv`: 34 columnas;
- `respuestas_zenodo_agregadas.csv`: 7 columnas;
- `codificacion.csv`: 6 columnas;
- `codificacion_tercera_ronda.csv`: 6 columnas;
- `tabla_saturacion.csv`: 11 columnas.

Para cada columna se documenta:

- dataset;
- nombre de la columna;
- tipo;
- unidad;
- rango admisible;
- codificación de valores perdidos;
- procedencia;
- descripción.

## 9. Reproducibilidad

La cadena de datos y análisis se ejecuta mediante:

`07_Datos/scripts/run_all.py`

Desde la raíz del repositorio:

```bash
python 07_Datos/scripts/run_all.py
```

**Estado: implementado y verificado el 2026-09-07.**

El orquestador ejecuta, en orden:

1. anonimización reproducible del XLSX crudo;
2. generación del dataset agregado para Zenodo;
3. análisis de saturación temática estratificado.

La verificación automática confirma:

- `respuestas_anonimizadas.csv`: 62 filas × 34 columnas;
- `respuestas_zenodo_agregadas.csv`: 64 filas × 7 columnas;
- `tabla_saturacion.csv`: 16 filas × 11 columnas;
- 8 entrevistas en el estrato de dominio;
- 8 entrevistas en el estrato de contraste;
- 79 códigos agregados al cierre;
- SHA-256 del dataset Zenodo:
  `b40ab460fc1d3d931beebaf5dd3037f564db8774559feee1ec1d371fa01b39b9`.

El orquestador `run_all.py` ejecuta únicamente la cadena reproducible general
del paquete `07_Datos`: anonimización del cuestionario, reconstrucción del
dataset agregado de Zenodo y análisis de saturación estratificado.

El experimento comparativo humano–LLM ya fue ejecutado. Su preparación y sus
análisis estadísticos se reproducen mediante los scripts específicos ubicados
en `06_Experimento/scripts_analisis/`, mientras que los datasets derivados y
los resultados se conservan en `07_Datos/datos_procesados/` y
`07_Datos/resultados/`. Actualmente `run_all.py` no invoca esa cadena
experimental.

## 10. Integridad

El manifiesto específico del paquete es:

`checksums_datos.sha256`

Debe regenerarse después de estabilizar los cambios de esta carpeta para que
incluya la codificación de tercera ronda, la documentación actualizada y las
tres curvas de saturación vigentes.

Una vez regenerado, debe verificarse mediante SHA-256.

## 11. Licencia y privacidad

La política específica para los datos se encuentra en:

`LICENSE-DATA.txt`

En términos generales:

- los datos anonimizados y agregados destinados a reutilización abierta se
  distribuyen bajo CC BY 4.0;
- el XLSX crudo queda expresamente fuera de la publicación abierta;
- los scripts se rigen por la licencia de código declarada en el repositorio.

Las restricciones de privacidad y protección de datos prevalecen sobre una
autorización general de reutilización cuando correspondan.

## 12. Depósito

El estado vigente del depósito se documenta en:

`registro_deposito.md`

DOI de versión:

`10.5281/zenodo.22236500`

Concept DOI:

`10.5281/zenodo.22236499`

La carpeta:

`08_Publicacion/dataset_zenodo/`

se conserva como snapshot histórico congelado y no debe modificarse para
adaptar su contenido a reorganizaciones posteriores del repositorio.

## 13. Desviaciones y limitaciones

Las desviaciones, limitaciones metodológicas y pendientes conocidos se
registran en:

`desviaciones.md`

No se eliminan ni ocultan limitaciones para aparentar cumplimiento.

Una desviación solo se considera cerrada cuando existe evidencia versionada que
demuestre su resolución.
