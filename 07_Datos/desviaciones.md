# Registro de desviaciones y limitaciones

Proyecto SIMPA — Sistema Inteligente de Mantenimiento de Palma Africana
Equipo AHMRV
Fecha de actualización: 2026-09-12

Este documento registra únicamente desviaciones, limitaciones y estados
verificados del trabajo realizado. No contiene resultados simulados ni
evidencia fabricada.

---

## D-01 — Potencia experimental inferior al objetivo convencional

**Estado:** limitación documentada y reportada en el análisis final.

El diseño originalmente registrado contemplaba una comparación apareada. Antes
de recolectar las puntuaciones experimentales se documentó la imposibilidad de
sostener un emparejamiento uno a uno válido entre requisitos humanos y
requisitos generados por el modelo, por lo que el análisis ejecutado trató los
dos orígenes como grupos independientes.

El experimento utilizó:

- 25 requisitos de origen humano;
- 25 requisitos generados por el LLM;
- 3 evaluadores independientes;
- 750 puntuaciones ordinales en total.

Como análisis de sensibilidad, bajo una aproximación convencional para dos
grupos independientes con α = 0,05 bilateral y un tamaño de efecto medio
d = 0,5, la potencia aproximada con 25 observaciones por grupo es 0,41. Para
alcanzar una potencia cercana a 0,80 bajo esos mismos supuestos serían
necesarias aproximadamente 64 observaciones por grupo.

No se incrementó el tamaño muestral después de observar los resultados ni se
duplicaron requisitos u observaciones. La potencia limitada se conserva como
amenaza a la validez de conclusión y la ausencia de significación estadística
no se interpreta como demostración de equivalencia.

**Fuente documental:**
`06_Experimento/osf_deviations.md`, `06_Experimento/readme.md` y
`08_Publicacion/manuscrito_final.tex`.

---

## D-02 — Ejecución del experimento comparativo humano–LLM

**Estado:** cerrada el 2026-09-12.

El experimento comparativo fue ejecutado con 25 requisitos humanos y 25
requisitos generados por el modelo de lenguaje. Tres evaluadores independientes
puntuaron los 50 requisitos en cinco dimensiones de calidad, generando 750
puntuaciones ordinales.

El análisis principal de RQ1 se realizó mediante modelos ordinales mixtos con
origen como efecto fijo y evaluador y requisito como interceptos aleatorios.
Los cinco modelos convergieron sin advertencias. Después de la corrección de
Holm-Bonferroni no se encontró evidencia estadísticamente significativa de
diferencias entre los dos orígenes.

Para RQ2 se calculó como medida principal el alfa de Krippendorff ordinal y,
como análisis secundario, el kappa de Cohen ponderado cuadráticamente. El
acuerdo interevaluador observado fue muy bajo y se mantiene como una limitación
del estudio.

Los datos y resultados verificables se conservan en:

- `06_Experimento/evaluadores/puntuaciones_reales.csv`;
- `07_Datos/datos_procesados/puntuaciones_experimento_con_origen.csv`;
- `07_Datos/resultados/modelo_ordinal_mixto.csv`;
- `07_Datos/resultados/comparacion_descriptiva.csv`;
- `07_Datos/resultados/acuerdo_krippendorff.csv`;
- `07_Datos/resultados/acuerdo_kappa_ponderado.csv`.

No se incorporaron resultados hipotéticos ni observaciones fabricadas: cada
puntuación de esos archivos procede de una hoja de evaluación real.

Que los datos sean reales no significa que los resultados sean interpretables.
El acuerdo entre evaluadores es nulo —alfa de Krippendorff de -0,015 a 0,027,
ICC(2,1) de 0,09 a 0,12— y el diseño solo podía detectar efectos de d = 0,81 o
mayores. Por eso la comparación entre el conjunto humano y el del LLM **se
retira como hallazgo** y se conserva únicamente como registro de lo ejecutado
(tarea A6 del Plan de mejora de datos; cifras en
`07_Datos/resultados/fiabilidad_potencia_A6.txt`).

---

## D-03 — Codificación temática limitada inicialmente a las primeras ocho entrevistas

**Estado:** cerrada el 2026-09-07.

La versión histórica de:

`07_Datos/datos_crudos/codificacion.csv`

continúa conservando la codificación de las primeras ocho entrevistas (cifras al 07/09/2026; tras la tarea C2 del 21/09/2026 el archivo tiene 124 fragmentos y 67 códigos únicos):

- 138 fragmentos;
- 68 códigos únicos;
- identificadores históricos `EV-01` a `EV-08`.

La tercera ronda se codificó de forma separada en:

`07_Datos/datos_procesados/codificacion_tercera_ronda.csv`

con:

- `ENTR-09` a `ENTR-16`;
- 89 fragmentos;
- 31 códigos distintos;
- 20 códigos ya presentes en el estrato de dominio;
- 11 códigos nuevos frente al estrato de dominio.

El script:

`07_Datos/scripts/curva_saturacion.py`

integra ambas fuentes sin reescribir la codificación histórica.

La ejecución verificada (07/09/2026; hoy hay 213 fragmentos y 82 códigos únicos, tras la tarea C2 y la normalización de contraste del 20/09) produce:

- 227 fragmentos totales;
- 79 códigos únicos en la vista agregada;
- 8 entrevistas en el estrato de dominio;
- 8 entrevistas en el estrato de contraste;
- tres curvas separadas: dominio, contraste y agregada;
- `tabla_saturacion.csv` con 16 filas × 11 columnas.

La separación por estratos responde a la medida metodológica declarada en la
adenda A.14 frente al riesgo de contaminar la interpretación de saturación al
mezclar poblaciones diferentes.

La vista agregada se conserva como descripción global y no como prueba de
saturación homogénea.

---

## D-04 — Cobertura del cuestionario por perfil ocupacional

**Estado:** limitación documentada.

El conjunto procesado contiene 62 respuestas totales.

Los perfiles con mayor representación observada son:

- Polinización: 18
- Control fitosanitario: 18

Por tanto, no existe un perfil ocupacional individual con 60 respuestas.

El proyecto no debe afirmar que alcanzó un mínimo de 60 respuestas por perfil
dominante cuando los datos disponibles no sostienen esa afirmación.

Esta limitación debe mantenerse visible al interpretar la generalización de los
resultados del cuestionario.

---

## D-05 — Archivo XLSX crudo excluido de publicación abierta

**Estado:** control deliberado de privacidad.

El archivo:

`07_Datos/datos_crudos/Sistema Inteligente de Mantenimiento de Palma Africana(1-62).xlsx`

se conserva como exportación primaria para trazabilidad y reproducibilidad.

Sin embargo, no forma parte del depósito abierto ni queda cubierto por la
licencia CC BY 4.0 de los datos abiertos.

Para análisis y publicación se utilizan:

- `07_Datos/datos_procesados/respuestas_anonimizadas.csv`
- `07_Datos/datos_procesados/respuestas_zenodo_agregadas.csv`

La restricción está documentada también en `07_Datos/LICENSE-DATA.txt`.

---

## D-06 — Orquestador único de análisis

**Estado:** cerrada; verificación ampliada el 2026-09-07.

Se implementó:

`07_Datos/scripts/run_all.py`

La cadena reproducible puede ejecutarse desde la raíz mediante:

```bash
python 07_Datos/scripts/run_all.py
```

La ejecución verificada sobre datos reales reproduce y comprueba:

- 62 filas × 34 columnas en `respuestas_anonimizadas.csv`;
- 64 filas × 7 columnas en `respuestas_zenodo_agregadas.csv`;
- 16 filas × 11 columnas en `tabla_saturacion.csv`;
- 8 entrevistas de dominio;
- 8 entrevistas de contraste;
- 79 códigos agregados al cierre;
- el SHA-256 publicado del dataset agregado de Zenodo:
  `b40ab460fc1d3d931beebaf5dd3037f564db8774559feee1ec1d371fa01b39b9`.

La ampliación de la cadena incorpora la codificación real de la tercera ronda y
las tres vistas de saturación. El experimento humano–LLM, que todavía se
encontraba pendiente durante esta verificación del 7 de septiembre de 2026,
fue ejecutado posteriormente y su estado final se documenta en D-02 y en
`06_Experimento/`.

---

## D-07 — Rutas históricas del snapshot Zenodo no corregidas

**Estado:** control deliberado de integridad, documentado el 2026-09-06.

Los seis archivos de `08_Publicacion/dataset_zenodo/` citan rutas con el prefijo
`AHMRV/` y la numeración histórica `07_Publicacion`, eliminadas en la
reestructuración del repositorio.

Su `readme.md` declara además el DOI como reservado y la publicación como
pendiente, estado que era correcto al momento de la carga.

Estas referencias no se corrigen. El manifiesto:

`08_Publicacion/dataset_zenodo/checksums_zenodo.sha256`

incluye el hash del propio `readme.md` de la carpeta, por lo que editar el
snapshot rompería la correspondencia con el material efectivamente depositado
bajo el DOI `10.5281/zenodo.22236500`.

La equivalencia entre rutas históricas y rutas vigentes, junto con el estado
real de publicación del depósito, se documenta fuera del snapshot.

---

## D-08 — Cambio de diseño analítico: de contraste apareado a modelo mixto independiente

**Estado:** abierta / declarada antes de la ejecución.

El protocolo prerregistrado (https://osf.io/4z35d/) prevé un contraste
apareado sobre 25 pares de requisitos. Al revisar el diseño antes de
recoger puntuación alguna, se detectó que no existe correspondencia uno a
uno defendible entre cada requisito elicitado por el equipo humano y uno
generado por el LLM sobre el mismo material fuente (`ENTR-04`): ambos
conjuntos no describen necesariamente las mismas funciones, por lo que el
emparejamiento carece de fundamento y el contraste apareado sería inválido.

En consecuencia:

- Los dos conjuntos se tratan como grupos independientes, no apareados.
- El análisis principal pasa a un modelo mixto de vínculo acumulativo para
  respuesta ordinal (`origen` como efecto fijo; `evaluador` y `requisito`
  como interceptos aleatorios cruzados), con la prueba U de Mann-Whitney +
  δ de Cliff como análisis de reserva si el modelo no converge.
- El coeficiente de acuerdo entre evaluadoras cambia de κ nominal
  (Cohen/Fleiss) a α de Krippendorff ordinal como medida principal, con κ
  ponderado cuadrático como medida secundaria.

Esta desviación agrava la limitación de potencia ya declarada en D-01: con
25 requisitos por grupo, la potencia de sensibilidad estimada es de
aproximadamente 0,41 (frente al objetivo de 0,80), y alcanzar 0,80
requeriría unos 64 requisitos por grupo. No se ampliará la muestra a
posteriori para corregir esta limitación; se priorizará el tamaño del
efecto con su intervalo de confianza al 95 % sobre la significación
estadística.

Detalle completo, especificación exacta del modelo y justificación en:
`06_Experimento/osf_deviations.md`.

**Fuente documental:** `manuscrito_final.tex`, sección 6.1–6.3; commit
`2a5412b` (2026-09-01), primer registro verificable de este razonamiento.

**Responsable de reflejar esta desviación en la plataforma OSF:** Allan
Villafuerte.

---

## Cierre de desviaciones

Una desviación solo puede marcarse como cerrada cuando exista evidencia
versionada que demuestre su resolución.

La eliminación de una entrada de este registro no sustituye su cierre: las
desviaciones resueltas deben conservarse con su estado actualizado para mantener
trazabilidad histórica.
