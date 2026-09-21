# SIMPA — Sistema Inteligente de Mantenimiento de Palma Africana

Especificación de Requisitos de Software (ERS/SRS) conforme a **ISO/IEC/IEEE 29148:2018**, con prototipo funcional y paquete de replicación.

> **Proyecto Fin de Curso · Ingeniería de Requerimientos (ISR-401) · 4to Nivel**
> Universidad Técnica Estatal de Quevedo · Facultad de Ciencias de la Computación
> Período 2026–2027 PPA

---

## El sistema

SIMPA da soporte a la gestión, el monitoreo y el diagnóstico asistido del cultivo de palma africana (*Elaeis guineensis* e híbridos interespecíficos) en una explotación de aproximadamente cien hectáreas.

Sustituye un proceso que hoy se registra en libretas de papel y se comunica por mensajería instantánea: registro de labores, control de lotes, detección de plagas y enfermedades, alertas tempranas, seguimiento de recorridos de polinización y reportes. Incorpora un **componente inteligente** especificado conforme al Reglamento (UE) 2024/1689, con requisitos de predicción, explicabilidad, equidad, supervisión humana, monitoreo posterior al despliegue y clasificación de nivel de riesgo.

**Organización cliente:** Palmicultora M (seudónimo) · Cantón El Empalme, Guayas, Ecuador
**Segunda organización fuente:** Extractora R (seudónimo)

> **Estado del prototipo:** aplicación frontend académica con persistencia en el navegador. No existe backend productivo, base de datos remota, inferencia de IA validada ni geolocalización real. Los flujos afectados están declarados uno a uno en [`05_MVP/readme.md`](05_MVP/readme.md).

---

## Los tres repositorios del proyecto

| Repositorio | Qué contiene | Enlace |
|---|---|---|
| **Principal** | Documentación, ERS, modelado, trazabilidad, datos, publicación, ética y defensa. Es este repositorio | <https://github.com/gleiston-guerrero/SIMPA_ISR401> |
| **Prototipo** | Código fuente del MVP (V1 y V2) | <https://github.com/jmaciasherr4/Prottotipo_Simpa> |
| **Evidencias** | Audio, video y consentimientos originales, en contenedores cifrados publicados como assets de release | <https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias> |

La separación no es arbitraria. El material audiovisual supera la cuota de almacenamiento de Git LFS, y el contenido identificable no puede residir en un repositorio público sin cifrar. Ambas decisiones están documentadas.

---

## Estructura del repositorio

```
SIMPA_ISR401/
├── 01_ERS/            Documento ERS/SRS v2.0, fuente LaTeX modular, anexos CCB y RFC
├── 02_Evidencias/     Transcripciones, consentimientos, cuestionario, codificación, walkthrough
├── 03_Modelado/       13 diagramas UML e i* en PlantUML (PNG y SVG) + mockups
├── 04_Trazabilidad/   Matriz extremo a extremo, matriz CSV, backlog de Jira, priorización
├── 05_MVP/            Documentación del prototipo y puntero al repositorio de código
├── 06_Experimento/    Protocolo, registro OSF con alcance temporal aclarado, consignas de LLM
├── 07_Datos/          Paquete de datos: crudos, procesados, scripts, resultados, diccionario
├── 08_Publicacion/    Manuscrito LNCS, evaluación FAIR, instantánea del depósito Zenodo
├── 09_Etica/          Anexos A01–A14, adendas, documentación de Categoría C
├── 10_Autoria/        Evidencia de autoría y declaración de identidades de Git
├── 11_Defensa/        Guion de exposición, guion de demostración, preguntas previsibles
├── CHANGELOG.md · CITATION.cff · LICENSE · README.md
├── checksums.sha256 · checksums_evidencias.sha256
└── .gitattributes · .gitignore · .mailmap
```

---

## Obtener el repositorio

```bash
git clone https://github.com/gleiston-guerrero/SIMPA_ISR401.git
cd SIMPA_ISR401
```

> **Líneas base de cierre:** `baseline-v5.0` corresponde a una evaluación
> oficial anterior del docente del 17/09/2026. `baseline-v6.0`,
> `baseline-v6.1` y `baseline-v6.2` se conservan como instantáneas históricas
> de las correcciones posteriores.
>
> `baseline-v6.3` congela el commit
> `1424f05038cbb6718c9dee3d360f7d9ff6307299`, evaluado oficialmente por el
> docente el 17/09/2026 a las 17:50. Se conserva intacta como registro de esa
> evaluación y no se mueve.
>
> El cierre posterior a esa evaluación se identifica como `baseline-v6.4`.
> Su etiqueta anotada se publica únicamente después de que el commit final
> supere la verificación desde un clon limpio. Ninguna etiqueta histórica se
> mueve, elimina ni reutiliza.

### Historial de líneas base

| Etiqueta | Commit congelado | Estado |
|---|---|---|
| `baseline-v2.0` | `3486021da5469a92833bbbffb37455933acd1d2f` | Histórica |
| `baseline-v3.0` | `734a42f0dd6228b8229745752d96bc6f234766d9` | Histórica |
| `baseline-v3.1` | `7c537240c32984c17a689dcb1e775968c90d3cd4` | Histórica |
| `baseline-v4.0` | `d79a39b75617dc4f4743770319866415afdca5a2` | Histórica |
| `baseline-v4.1` | `8b609aef8e40b4e43349df70018fac99c5a1ac83` | Histórica |
| `baseline-v4.2` | `831b83341ee39732d2a5722e53e26e44dc8c9cfd` | Histórica |
| `baseline-v5.0` | `e63c9b3343ef9c56df8fa07ada1868bd4c171caf` | Evaluada oficialmente |
| `baseline-v6.0` | `32c248351b2d3cefbebc0086c16c5d1cdd261b55` | Histórica — cierre post-evaluación |
| `baseline-v6.1` | `26c3561f10679dbdf61c60fcfcd806506b8a1dbd` | Histórica — ajuste documental |
| `baseline-v6.2` | `dafaf0c86563ce63fc95d90432f67b8dafb165ec` | Histórica — ajuste de vigencia y manifiesto |
| `baseline-v6.3` | `1424f05038cbb6718c9dee3d360f7d9ff6307299` | Evaluada oficialmente — revisión del 17/09/2026, 17:50 |
| `baseline-v6.4` | Ver objeto de etiqueta anotada | Cierre posterior a esa evaluación; publicación condicionada a verificación desde clon limpio |

`baseline-v6.4` no incluye su propio hash en esta tabla porque un commit no
puede contener su propio identificador. El commit congelado se consulta en
el objeto de la etiqueta anotada (`git show baseline-v6.4`) una vez publicada.

Una nueva línea base solo se crea después de completar las correcciones,
regenerar los manifiestos de integridad y verificar el repositorio desde un
clon limpio.

Eso es todo. **No se requiere Git LFS**: se evaluó su uso para la evidencia audiovisual y se descartó al agotarse la cuota de almacenamiento. No queda ninguna regla `filter=lfs` ni ningún puntero en el árbol. La evidencia pesada se obtiene desde el repositorio complementario, como se explica más abajo.

---

## Dónde está el prototipo

El código vive en un repositorio propio; aquí reside su documentación.

| Recurso | Ubicación |
|---|---|
| Documentación del prototipo | [`05_MVP/readme.md`](05_MVP/readme.md) |
| Código fuente | <https://github.com/jmaciasherr4/Prottotipo_Simpa> |
| Commit evaluado | `ba33002dcf680f8b39d42df04553733bd5389f6d` (2026-08-31) |
| Árbol canónico de la V2 | `prototipo_v2/Prottotipo_Simpa-main/Prototipo/` |
| **Demostración en vivo** | <https://simpa-v3-prototipo.netlify.app/> |

### Cuentas de demostración

| Usuario | Contraseña | Rol |
|---|---|---|
| `admin` | `admin123` | Administrador |
| `supervisor` | `super123` | Supervisor |
| `operario` | `oper123` | Operario |

> Cuentas de demostración únicamente. No deben utilizarse con información real.

`05_MVP/readme.md` declara, requisito por requisito, qué flujos son funcionales y cuáles son interfaz simulada. Los flujos de análisis por imagen (`RF-07`, `RF-08` y la clasificación visual de `RF-21`) y el conteo georreferenciado (`RF-14`) **no realizan inferencia ni geolocalización reales**.

---

## Dónde está la evidencia

La evidencia se organiza en dos zonas, conforme a la Ley Orgánica de Protección de Datos Personales del Ecuador.

### Zona pública — en este repositorio

`02_Evidencias/` contiene transcripciones anonimizadas bajo `ENTREVISTADO-NN`, consentimientos con nombre y firma enmascarados, fotografías sin rostros identificables ni coordenadas, respuestas del cuestionario sin columnas identificativas, y el inventario técnico de cada archivo multimedia.

### Zona restringida — en el repositorio complementario

El material identificable —audio, video y consentimientos originales— se publica cifrado como assets de release en <https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias>, release `v1.0-evidencias`.

Los contenedores `.7z` llevan **la cabecera cifrada**: sin la contraseña no puede listarse siquiera el nombre de los archivos, que incluyen el rol del participante.

> **La contraseña se entrega únicamente al docente responsable, por el espacio de la actividad en el SGA.** No consta en este repositorio ni en ningún archivo público.

### Inventario y verificación

| Archivo | Qué contiene |
|---|---|
| [`02_Evidencias/00_Restringido/fichas_tecnicas.csv`](02_Evidencias/00_Restringido/fichas_tecnicas.csv) | Una fila por archivo: tipo, fecha, código de participante, duración, códec, tamaño, SHA-256 precifrado, contenedor, ruta interna y URL del release |
| [`02_Evidencias/00_Restringido/verificacion_fichas.md`](02_Evidencias/00_Restringido/verificacion_fichas.md) | Reporte generado por script que comprueba **por petición HTTP** que cada contenedor declarado existe con ese nombre exacto |
| `checksums_evidencias.sha256` | Sumas del contenido interno de los contenedores, calculadas antes de cifrar |

El inventario usa delimitador `;` y cubre tres series de códigos: `ENTR-01`
a `ENTR-16` para las entrevistas semiestructuradas, `WT-01` a `WT-06` para
las sesiones de validación por walkthrough, y `CUEST-01` a `CUEST-05` para
los consentimientos complementarios del cuestionario. Las series son
independientes y no se cruzan.

---

## Reproducir el documento

Desde `01_ERS/`, con TeX Live completo:

```bash
pdflatex ERS_SRS_2B_v2.0.tex
bibtex   ERS_SRS_2B_v2.0
pdflatex ERS_SRS_2B_v2.0.tex
pdflatex ERS_SRS_2B_v2.0.tex
```

Alternativa sin instalación local: subir el contenido de `01_ERS/` a Overleaf, marcar `ERS_SRS_2B_v2.0.tex` como *Main File* y compilar con pdfLaTeX.

**Resultado esperado:** 108 páginas, sin errores graves ni referencias o citas indefinidas.

### Regenerar los diagramas

Desde `03_Modelado/Diagramas_UML/`:

```bash
plantuml -DPLANTUML_LIMIT_SIZE=32768 -tpng -Sdpi=300 -o png *.puml
plantuml -DPLANTUML_LIMIT_SIZE=32768 -tsvg -o svg *.puml
```

> El parámetro `PLANTUML_LIMIT_SIZE` es necesario: el valor por defecto de 4096 px **recorta** diez de los trece diagramas.

---

## Reproducir el análisis de datos

Punto de entrada único, desde la raíz del repositorio:

```bash
python 07_Datos/scripts/run_all.py
```

La cadena parte de los datos crudos y regenera todo lo derivado:

```
XLSX del cuestionario
  → anonimizar_encuesta.py
  → respuestas_anonimizadas.csv

XLSX del cuestionario
  → preparar_dataset_zenodo_agregado.py
  → respuestas_zenodo_agregadas.csv

codificacion.csv + codificacion_tercera_ronda.csv
  → curva_saturacion.py
  → tabla_saturacion.csv
  → curva_saturacion_dominio.png / .pdf
  → curva_saturacion_contraste.png / .pdf
  → curva_saturacion_agregada.png / .pdf
```

**Resultado esperado:** 62 × 34 en respuestas anonimizadas, 64 × 7 en el dataset agregado para Zenodo y 16 × 11 en la tabla de saturación. El análisis integra 16 entrevistas y cierra con 79 códigos únicos en la vista agregada.

Verificar la integridad del paquete publicado, antes de regenerar artefactos:

```bash
cd 07_Datos && sha256sum -c checksums_datos.sha256
```

> La cadena `run_all.py` verifica dimensiones, estructura y resultados analíticos. Los CSV deben ser reproducibles bit a bit entre entornos; las figuras pueden diferir en bytes según la versión de Matplotlib y de las fuentes del sistema, sin que cambien los resultados representados. El manifiesto SHA-256 corresponde a los archivos versionados publicados.

Cada columna de cada conjunto está documentada en [`07_Datos/diccionario_datos.csv`](07_Datos/diccionario_datos.csv). Las limitaciones conocidas están registradas en [`07_Datos/desviaciones.md`](07_Datos/desviaciones.md).

---

## Estudio empírico

El protocolo experimental está registrado públicamente en OSF y el material reside en `06_Experimento/`.

El alcance temporal del registro está aclarado de forma explícita: es retrospectivo respecto a la recolección del material fuente de entrevistas, pero anterior a la ejecución del experimento comparativo humano–LLM.

**Estado: experimento humano–LLM ejecutado y análisis principal completado.**

Se compararon 25 requisitos funcionales elicitados por el equipo humano con 25 requisitos generados por un modelo grande de lenguaje a partir del mismo material fuente. Tres evaluadores independientes puntuaron los 50 requisitos en cinco dimensiones de calidad, para un total de 750 puntuaciones ordinales.

El análisis principal utilizó modelos ordinales mixtos con origen como efecto fijo y evaluador y requisito como interceptos aleatorios. No se encontró evidencia estadísticamente significativa de diferencias entre ambos orígenes después de aplicar la corrección de Holm-Bonferroni. El acuerdo interevaluador fue muy bajo y se conserva como una limitación relevante del estudio.

El registro OSF es retrospectivo respecto a la recolección del material fuente de entrevistas, pero anterior a la ejecución del experimento comparativo humano–LLM. Las desviaciones respecto del plan original se documentan sin modificar retroactivamente el protocolo registrado.

Los resultados, scripts y archivos derivados del experimento se encuentran en `06_Experimento/` y `07_Datos/`; el manuscrito actualizado está disponible en `08_Publicacion/manuscrito_final.pdf`.

---

## Publicación y datos abiertos

| Recurso | Referencia |
|---|---|
| Depósito de datos | DOI de versión `10.5281/zenodo.22236500` · DOI conceptual `10.5281/zenodo.22236499` |
| Registro | <https://zenodo.org/records/22236500> |
| Instantánea depositada | [`08_Publicacion/dataset_zenodo/`](08_Publicacion/dataset_zenodo/) |
| Evaluación FAIR | [`08_Publicacion/fair_assessment.pdf`](08_Publicacion/) — F-UJI 4.0.0: **24/26 indicadores, 92,31 %, nivel avanzado** |
| Manuscrito | [`08_Publicacion/manuscrito_final.pdf`](08_Publicacion/) — plantilla oficial Springer LNCS |
| Archivado de código | Software Heritage, SWHID declarado en [`CITATION.cff`](CITATION.cff) |

`08_Publicacion/dataset_zenodo/` es una **instantánea congelada** atada al DOI. Sus rutas internas son deliberadamente históricas y no se corrigen: alterarlas rompería la correspondencia con lo depositado.

---

## Equipo AHMRV

| Integrante | Rol | Estado (examen suspenso) |
|---|---|---|
| Villafuerte Rosero Allan Noé | Analista líder | Activo — evaluado |
| Huilcapi León Denisses Fabiola | Documentadora | Activo — evaluado |
| Rizzo Vélez Edson Nagib | Verificador y gestor de evidencias | Aprobó la asignatura — apoyo voluntario, no evaluado |
| Macías Herrera Josthyn Esteban | Modelador | Activo — evaluado |
| Arboleda Yanza Francisco Javier | Apoyo modelado y repositorio | Activo — evaluado |
| Alcívar Vélez Anderson Adonis | Apoyo repositorio | Reprobó la asignatura — retirado del equipo evaluado |

Composición vigente para el examen suspenso de ISR-401 (corte 18 de
septiembre de 2026) — ver `09_Etica/solicitud_cambio_composicion.md`.

**Docente responsable:** Ing. Gleiston Cicerón Guerrero Ulloa, PhD

Las contribuciones se atribuyen mediante `.mailmap`, que normaliza el historial a seis autores con correo institucional. El detalle consta en [`10_Autoria/declaracion_identidades_git.md`](10_Autoria/declaracion_identidades_git.md).

---

## Licencia

Ver [`LICENSE`](LICENSE). En resumen:

- **CC BY 4.0** — documento ERS/SRS y conjunto de datos anonimizado
- **MIT** — código fuente del prototipo
- **Sin licencia y sin redistribución** — contenido identificable de la zona restringida

## Cómo citar

Ver [`CITATION.cff`](CITATION.cff) o usar el botón *Cite this repository* de GitHub.
