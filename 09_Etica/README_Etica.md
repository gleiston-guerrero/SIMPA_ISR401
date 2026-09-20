# Ética — Proyecto SIMPA · Equipo AHMRV

Este documento reúne, en un solo lugar y en orden cronológico, la traza completa
de los anexos éticos (A.01–A.14), las desviaciones de procedimiento detectadas en
rondas anteriores, cómo fueron subsanadas, y la explicación de la migración de
repositorio realizada por motivos de privacidad. Su propósito es que cualquier
persona evaluadora pueda reconstruir, sin preguntar al equipo, qué pasó y en qué
estado quedó cada punto.

---

## 1. Traza de anexos A.01–A.14

| Anexo | Contenido | Estado |
|---|---|---|
| A.01 | Protocolo de investigación | Vigente desde Entrega 1 |
| A.02 | Instrumentos de recolección | Vigente, ampliado en Entrega 3 con los instrumentos de la segunda ronda de campo |
| A.03 | Consentimiento informado (formato base) | Vigente. Las copias públicas firmadas se anonimizaron — ver sección 2 |
| A.04 | Plan de gestión de datos | Vigente |
| A.05 | Aval institucional | Vigente |
| A.06 | Declaración de conflicto de intereses | Vigente |
| A.07 | Compromiso de confidencialidad | Vigente |
| A.08 | CV del docente responsable | Vigente |
| A.09 | Nómina del equipo | Vigente, seis integrantes |
| A.10 | Cronograma Gantt | Vigente |
| A.11 | Análisis de riesgos | Vigente |
| A.12 | Acreditación de formación ética | **En curso** — sin certificados adjuntos; su propia sección 5 indica que debe presentarse con ese estado mientras no haya certificado emitido. Ver sección de estado de la acreditación y la aprobación ética |
| A.13 | Participantes externos | Vigente, incorporado en Entrega 3 junto con la organización externa |
| — | Adenda ética, segunda ronda (`Adenda_Segunda_Ronda.pdf`) | Declara la desviación de procedimiento de la segunda ronda de campo — ver sección 2 |
| A.14 | Adenda tercera ronda (`A14_Adenda_Tercera_Ronda.pdf` y `.tex`) | Documento de trazabilidad y subsanación de la desviación anterior; no constituye una nueva solicitud de permiso. **Es el único anexo con fuente LaTeX versionada** |

Categoría C (participación de la organización externa), en `Categoria_C/`:
`C1` Aval de la unidad productiva, `C2` Compromiso de confidencialidad
estratégica, `C3` Protocolo de anonimización, `C4` Normativa sectorial aplicable.

### 1.1 Compromisos sustantivos adquiridos en la A.14

Además de documentar la subsanación, la A.14 adquiere dos compromisos que
condicionan el análisis y que se registran aquí para su seguimiento:

- **Reporte de saturación por estratos.** La curva se reporta en tres curvas
  separadas —estrato de dominio (`ENTR-01` a `ENTR-08`), estrato de contraste
  (`ENTR-09` a `ENTR-16`) y agregada— y no sobre la mezcla indiferenciada. El
  razonamiento es que los participantes del segundo estrato generan pocos
  códigos nuevos de dominio **por construcción, no por saturación alcanzada**,
  de modo que mezclarlos produciría una inflexión artificial.
- **Mitigación R-14.4.** Ningún integrante entrevista a estudiantes sobre los
  que tenga función de evaluación.

### Estado de la acreditación de formación ética y de la aprobación del proyecto

Conforme a la tarea G2 del Plan de mejora de datos, se precisa el estado real
de dos cuestiones que hasta ahora se presentaban de forma conjunta y que son
distintas entre sí.

**1. Acreditación de formación ética (anexo A.12).**

A.12 es la *Acreditación de Formación Ética en Investigación*: documenta que
el docente responsable y al menos un integrante del equipo han completado un
curso de formación en ética de la investigación. Es una credencial de
formación de personas, no un pronunciamiento sobre el proyecto.

Su estado real a la fecha es el siguiente:

- En el registro de acreditaciones (sección 3) las casillas de estado están
  sin marcar para ambas personas.
- Las fichas de detalle por certificado (sección 4) están vacías y no hay
  ningún certificado adjunto al anexo.
- La propia sección 5 del documento advierte que «la formación ética del
  integrante designado del equipo se encuentra en curso y no cuenta aún con
  certificado emitido», y que «mientras el certificado no esté emitido, este
  documento debe presentarse indicando el estado real "en curso" y no como
  acreditación cumplida».

Este documento corrige en consecuencia la fila A.12 de la tabla anterior, que
hasta la revisión del Plan de mejora de datos figuraba como «Vigente».

**2. Aprobación ética del proyecto.**

En el repositorio no consta ningún dictamen de comité de ética sobre el
proyecto, con número y fecha. Las únicas menciones a un «comité» en el
repositorio corresponden al Comité de Control de Cambios (CCB), que es un
órgano de gestión de requisitos y no de revisión ética.

El equipo ha solicitado al docente responsable la precisión de este punto,
dado que fue él quien gestionó el trámite de ética del proyecto: si existe un
dictamen de comité con número y fecha, se adjuntará a este anexo y esta
sección se actualizará en consecuencia; si lo que consta es su acreditación de
formación ética y la aprobación del proyecto en el marco de la asignatura, se
declarará en esos términos y no como dictamen de comité.

Hasta obtener esa precisión, **este documento no afirma que el proyecto cuente
con dictamen de comité de ética**, ni afirma lo contrario.

**3. Condiciones en que se realizó el trabajo de campo.**

En todos los casos, el trabajo de campo se realizó con consentimiento
informado de las personas participantes. Las limitaciones de los
consentimientos se detallan en la tarea G3 y el estado de los avales
institucionales en la G4.

---

## 2. Desviación de procedimiento (segunda ronda) y su subsanación

**Qué ocurrió.** Durante la segunda ronda de trabajo de campo (Entrega 3, agosto
2026) se detectaron deficiencias de anonimización en la evidencia fotográfica y en
los consentimientos informados publicados: nombres propios de los participantes
visibles en los nombres de archivo, cédula y firma sin enmascarar en las copias
públicas de consentimiento, y metadatos GPS presentes en fotografías publicadas.
Esta desviación quedó declarada en `Adenda_Segunda_Ronda.pdf`.

**Cómo se subsanó (Entrega 3, `CHANGELOG.md` [3.0.0]).**

- Cédula y firma enmascaradas en la copia pública de cada consentimiento; los
  originales sin enmascarar se trasladaron a la zona restringida cifrada — ver
  sección 5.
- Metadatos GPS eliminados de todas las fotografías publicadas.
- Nomenclatura de archivos multimedia migrada al patrón
  `AAAA-MM-DD_TipoParticipante_ENTR-XX_Tecnica.ext`, sustituyendo los nombres
  propios por el código de participante correspondiente.

**Criterio de convalidación.** Conforme a la decisión operativa del equipo (plan
de cierre 2B, sección 0.2), esta desviación se considera **aceptada y cerrada**:
la A.14 no vuelve a pedir una nueva aprobación sobre este punto, sino que
documenta históricamente qué se hizo mal, cómo se corrigió y qué medida evita que
se repita.

### 2.1 Efecto colateral sobre los metadatos EXIF

El proceso de retirada de coordenadas GPS eliminó **la totalidad** de los
metadatos EXIF de las fotografías, no solo las etiquetas de geolocalización.
Verificado sobre las 24 imágenes de `02_Evidencias/Fotos_Entorno/` y
`02_Evidencias/Documentos_Organizacion/`: ninguna conserva `DateTimeOriginal`,
`DateTime` ni `Model`.

Esto no afecta a la privacidad —el efecto va en la dirección protectora— pero sí
limita la evidencia de autoría: la fecha de captura ya no puede acreditarse desde
el archivo. **No se han reconstruido fechas** a partir del nombre de archivo ni
del historial de Git. Si los originales existen en los dispositivos de captura,
la reposición debe preservar `DateTimeOriginal` y `Model` y retirar únicamente
las etiquetas GPS. Si no existen, se declara como desviación.

---

## 3. Migración de repositorio por privacidad

**Motivo.** Con posterioridad a la corrección descrita en la sección 2, una
auditoría del repositorio confirmó que el historial de Git seguía conservando,
en la rama `reorganizar-estructura-ahmrv`, versiones anteriores y sin anonimizar
de los consentimientos firmados y de las fotografías de entorno — con nombres
reales de los participantes visibles tanto en el nombre de archivo como en el
contenido — recuperables aunque la zona pública actual ya mostrara las versiones
corregidas.

**Qué se hizo.** Se reescribió el historial de dicha rama con `git filter-repo`,
retirando por completo las rutas que contenían las versiones sin anonimizar
(`AHMRV/evidencias/`, `AHMRV/02_Evidencias/formularios/`,
`AHMRV/02_Evidencias/fotos/`, entre otras equivalentes), verificado mediante
auditoría directa de los objetos del historial (`git rev-list --objects --all`).

**Por qué se migró a un repositorio nuevo.** La reescritura de la rama, por sí
sola, resultó insuficiente: GitHub conserva de forma permanente e inmutable la
referencia de un Pull Request (`refs/pull/2/head`) abierto en algún momento desde
esa rama, la cual seguía sirviendo el contenido original sin anonimizar y no
puede eliminarse mediante `git push --force` ni ninguna operación estándar de
Git. Por esta limitación, ajena al equipo, el proyecto se migró a un repositorio
nuevo bajo la cuenta `AlanNVR`, denominado `SIMPA_ISR401`, que no heredó referencias de
Pull Requests ni historial previo. El repositorio original quedó archivado en
modo privado. Posteriormente, `SIMPA_ISR401` fue transferido al docente; su URL canónica vigente es `https://github.com/gleiston-guerrero/SIMPA_ISR401`. Se verificó de forma independiente que el repositorio nuevo no
contiene ninguna referencia adicional (`refs/pull/*` ni de otro tipo) ni ningún
dato identificable en su historial completo.

Esta operación queda registrada también en `CHANGELOG.md` y referenciada en la
A.14, conforme a lo exigido por el STOP A del plan de cierre: la corrección no
sustituye ni oculta la traza de lo ocurrido, se documenta hacia adelante.

> **Alcance de esta operación.** La reescritura afectó únicamente al repositorio
> anterior, hoy archivado, y fue la razón para migrar. **En el repositorio
> vigente `SIMPA_ISR401` no se ha reescrito el historial en ningún momento**: no
> se ha empleado `rebase`, `filter-branch`, `filter-repo` ni `push --force`, y
> ningún hash histórico ha sido alterado.

### 3.1 Correspondencia de repositorio y rutas históricas

Los anexos firmados de rondas anteriores se conservan sin alteración. Por ello,
algunas referencias internas reflejan la estructura y el repositorio vigentes
en el momento de su firma. Para su interpretación durante la evaluación se
aplica la siguiente correspondencia, coherente con la migración documentada en
la A.14 y con la reorganización posterior del repositorio:

| Referencia histórica | Referencia vigente | Tratamiento |
|---|---|---|
| `https://github.com/AlanNVR/Villafuerte_Grupo_AHMRV/tree/main/AHMRV` | `https://github.com/gleiston-guerrero/SIMPA_ISR401` | El repositorio anterior quedó archivado en privado; `SIMPA_ISR401` fue posteriormente transferido al docente y esta es su URL canónica vigente |
| `AHMRV/06_Etica/` · `AHMRV/08_Etica/` | `09_Etica/` | Doble cambio de ubicación: primero dentro de la estructura consolidada, después por la renumeración descrita abajo |
| `AHMRV/evidencias/` · `AHMRV/02_Evidencias/` | `02_Evidencias/` | Reorganización de las evidencias dentro del árbol vigente y saneado |
| `AHMRV/07_Publicacion/` | `08_Publicacion/` | Renumeración |
| `AHMRV/09_Defensa/` | `11_Defensa/` | Renumeración |
| Cualquier ruta con prefijo `AHMRV/` | La misma ruta **sin** el prefijo | Ver abajo |

**Aplanado de la estructura.** El contenido residía bajo una carpeta
contenedora `AHMRV/`. Por indicación expresa del docente responsable, esa
carpeta se eliminó y su contenido pasó a la raíz del repositorio, quedando la
estructura numerada `01_ERS` a `11_Defensa`. El movimiento se realizó con
`git mv`, de modo que el historial de cada archivo permanece accesible mediante
`git log --follow`.

**Excepción deliberada.** Las rutas internas de
`08_Publicacion/dataset_zenodo/` conservan el prefijo `AHMRV/` y **no se
corrigen**: son la instantánea exacta de lo depositado bajo el DOI
`10.5281/zenodo.22236500` y alterarlas rompería la correspondencia con el
depósito.

Esta tabla es de correspondencia documental: **no modifica ni reemplaza los PDF
firmados**. Su función es permitir que una persona evaluadora resuelva las rutas
históricas contra el estado actual del repositorio sin alterar los anexos
originales.

---

## 4. Estado de privacidad al cierre

- La zona pública no contiene nombre, firma, cédula, rostro identificado por
  nombre, ni coordenadas GPS.
- Los **dieciséis** consentimientos públicos muestran el código de participante
  (`ENTR-01` a `ENTR-16`) en lugar de datos identificables, con el nombre, la
  firma y el documento de identidad enmascarados.
- Las transcripciones publicadas identifican a los participantes únicamente como
  `ENTREVISTADO-01` a `ENTREVISTADO-16`. Verificado que no contienen ninguna
  cadena que permita reidentificar.
- El cuestionario se configuró como **anónimo**: las 62 respuestas tienen la
  columna de correo con el valor literal `anonymous` y la columna de nombre
  vacía. No hay dato personal en el archivo crudo.
- Las versiones históricas sensibles fueron saneadas en la medida técnicamente
  posible; la limitación encontrada (refs de Pull Request) y la solución aplicada
  quedan documentadas en la sección 3.
- La contraseña de los contenedores cifrados no se publica en ningún
  repositorio; se entrega únicamente por el canal académico correspondiente.

### 4.1 Base legal del tratamiento

La base legal declarada es el artículo 7 de la Ley Orgánica de Protección de
Datos Personales del Ecuador. **Se rechaza razonadamente el consentimiento como
base legal en el marco de la relación laboral**, por no concurrir la libertad
exigible: un trabajador no puede negarse a participar en igualdad de condiciones
frente a quien le emplea. La tabla `tab:lopdp-ia` del ERS detalla, para cada
dato tratado, la base legal invocada y la medida aplicada.

### 4.2 Finalidad del tratamiento

Los datos personales recolectados (audio, video, transcripciones, respuestas
del cuestionario) se tratan exclusivamente con fines académicos: el desarrollo
del Proyecto Fin de Curso de la asignatura Ingeniería de Requisitos (ISR-401),
UTEQ. No se usan con fines comerciales, de vigilancia laboral, ni se comparten
con la organización empleadora más allá del reporte agregado y anonimizado.

### 4.3 Plazo de conservación

Los materiales identificables (audio, video, consentimientos sin enmascarar)
se conservan cifrados en el repositorio complementario de evidencias mientras
dure el proceso de evaluación académica del curso. Conforme a la política de
retención declarada en `09_Etica/A04_Plan_Gestion_Datos.pdf` (punto 9): los
datos crudos con personas identificables se conservan **24 meses contados
desde la finalización del proyecto**, tras lo cual se realiza eliminación
segura (`shred` en Linux / `sdelete` en Windows, tanto en la copia local como
en la copia de nube) y se levanta un acta de destrucción firmada por el líder
del equipo y el docente responsable, archivada en `09_Etica/`. Los datos
agregados, disociados y los artefactos publicables (transcripciones
seudonimizadas, estadística descriptiva, fotografías sin personas
identificables, artefactos UML y matriz de trazabilidad) no tienen límite de
retención, por no ser datos personales.

### 4.4 Responsable del tratamiento

El responsable del tratamiento de los datos personales es el equipo AHMRV,
bajo la supervisión académica de PhD. Gleiston Cicerón Guerrero Ulloa, docente
de la asignatura ISR-401.

---

## 5. Zonas de evidencia y dónde reside cada una

| Zona | Contenido | Ubicación |
|---|---|---|
| **Pública** | Consentimientos enmascarados, transcripciones anonimizadas, fotografías sin datos identificables, respuestas del cuestionario | `02_Evidencias/`, en este repositorio |
| **Restringida — inventario** | Ficha técnica de cada archivo y su reporte de verificación | `02_Evidencias/00_Restringido/` |
| **Restringida — material** | Audio, video y consentimientos originales sin enmascarar | Contenedores cifrados publicados como assets de release en `erizzov-boop/SIMPA_ISR401_Evidencias` |

El material identificable **no reside en este repositorio en ninguna forma**. La
carpeta `00_Restringido/` contiene únicamente el inventario que describe dónde
está cada archivo, con su suma SHA-256 calculada antes de cifrar.

Los contenedores `.7z` llevan **la cabecera cifrada**, de modo que sin la
contraseña no puede listarse siquiera el nombre de los archivos. Es una medida
relevante porque esos nombres incluyen el rol del participante.

---

## 6. Validación por walkthrough y consentimientos de usabilidad

Las sesiones de validación por walkthrough emplean una serie de códigos propia,
`WT-01` a `WT-06`, **independiente de la serie `ENTR-XX`** de las entrevistas
semiestructuradas. Son dos estudios distintos y reutilizar los mismos códigos
haría que un identificador designara a dos personas diferentes según el archivo
en que apareciera.

Cuando un participante de walkthrough fue también entrevistado, recibe
igualmente un código `WT-XX` propio, y la correspondencia entre ambos códigos se
registra únicamente en la zona restringida. Publicar esa correspondencia
aumentaría el riesgo de reidentificación, porque una persona identificada por su
rol en un estudio y por su perfil técnico en el otro es más fácil de reconocer
que en cualquiera de los dos por separado.

La autorización de grabación de pantalla es una **casilla opcional e
independiente** de la de participación. Un participante puede aceptar la sesión y
rechazar la grabación; en ese caso no existe archivo de video para ese código y
el acta lo hace constar. La ausencia de grabación es una decisión registrada, no
un dato faltante.

---

## 7. Asuntos abiertos

Se declaran aquí en lugar de omitirse, conforme al criterio que ha guiado el
proyecto:

| Asunto | Estado |
|---|---|
| Metadatos EXIF de las 24 fotografías | Perdidos en el proceso de anonimización. Ver sección 2.1. Pendiente de determinar si existen los originales |
| Perfiles de `ENTR-13`, `ENTR-14` y `ENTR-16` | La A.14 los clasifica como estudiantado de carrera afín; los nombres de archivo de consentimiento indican otros perfiles. Requiere reconciliación mediante adenda nueva, no mediante modificación de la A.14, que ya está firmada |
| Doble codificación | La codificación temática cuenta hoy con un solo codificador. El cálculo de concordancia entre codificadores está pendiente |

Ninguno de estos asuntos se corrige alterando un documento ya firmado. Las
discrepancias con anexos firmados se resuelven mediante documentación nueva que
declare la discrepancia y su tratamiento.
