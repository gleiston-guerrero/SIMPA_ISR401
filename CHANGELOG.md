# Registro de cambios

Todas las modificaciones relevantes de este proyecto se documentan en este archivo.
El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).

---

## [4.4.0] - 2026-09-21 - Plan de mejora de los datos del proyecto

Ronda de correcciones sobre el Plan de mejora de datos del 19/09/2026. Todas
las tareas quedan registradas una a una, con su criterio de aceptación y su
comando de verificación, en `07_Datos/registro_correcciones.md`.

### Anadido

- Tabla de procedencia de los 79 requisitos (42 RF, 6 RF-IA, 19 RNF y 12
  RNF-IA) con clasificación verificada persona a persona, en
  `07_Datos/datos_procesados/tabla_procedencia_requisitos.csv` (D1).
- Columnas de cita literal y línea de transcripción en los dos archivos de
  codificación, con verificador propio `verificar_citas_C1.py` (C1).
- Matriz de cobertura pregunta x entrevista, 13 preguntas x 16 entrevistas,
  con cita literal en cada celda cubierta (B4).
- Tabla maestra de participantes y adenda de perfiles, con verificador de
  coincidencia entre todas las fuentes (B3).
- Análisis de saturación con sensibilidad al orden sobre 10 000 órdenes
  aleatorios (C4).
- Matriz de uso por consentimiento de cada participante (G3).
- Declaración explícita de ausencia de dictamen de comité de ética y de aval
  firmado de una de las organizaciones (G2, G4).
- Registro de la prueba de extremo a extremo por rol, con fecha, ejecutor y
  resultado observado (E1).
- Muestra congelada y hoja de doble codificación independiente (C3).

- Casos de prueba de los 24 RF "Must" definidos y ejecutados sobre el
  prototipo desplegado; hoja `04_Trazabilidad/D4_casos_prueba_RF_Must.md`
  (D4).
- Cobertura de los RF Must recalculada por script, con el reparto entre
  ejercitado en pantalla, declarado en pantalla y solo indicio (E2).
- Hoja `Ejecucion_D4` en `04_Trazabilidad/matriz_e2e.xlsx`, que cruza los
  24 RF Must con el resultado real de su ejecución (D5).
- Análisis de sensibilidad n = 62 frente a n = 58 sobre las respuestas del
  cuestionario, con diferencia máxima de 0,04 puntos / 2,0 puntos
  porcentuales (H1).
- Complemento de modalidad, hora y firma de las actas de member checking, y
  tabla de trazabilidad de los 12 enunciados con sus códigos y citas (F2).
- Declaración sobre las fechas de firma y la coherencia de perfiles del
  walkthrough (F3).

### Cambiado

- Las ocho entrevistas de las rondas 1 y 2 se retranscribieron desde el audio
  con marcas de tiempo; la cobertura de cada una frente a la duración real del
  audio queda declarada en `02_Evidencias/Transcripciones/readme.md` (B1).
- Los umbrales duplicados RNF-01 y RNF-02 se declaran precisados y sustituidos
  por RNF-IA-08 y RNF-IA-01 (D3).
- El anexo A.12 pasa de "Vigente" a "En curso" (G2).
- La documentación del cuestionario declara el modo real de aplicación,
  presencial y secuencial, y la distinción entre n = 62 y n = 58 (H1).
- Una sola URL vigente del prototipo; los despliegues anteriores quedan
  rotulados como históricos (E3).
- La doble codificación independiente (C3) se completó: kappa de Cohen
  0,655 entre los dos codificadores, cada uno desde su propia cuenta de
  git; 55 desacuerdos documentados en `desacuerdos_C3.csv`.
- La cobertura de ENTR-03 frente al audio pasa de 82 % a 100 %, tras
  verificar por escucha directa que el tramo final es ruido ambiental sin
  habla (B1).
- La matriz de uso por consentimiento (G3) queda cerrada: decisión
  aplicada en los 5 usos no cubiertos, declarando como desviación
  irreversible los casos en que retirar el uso habría invalidado evidencia
  ya verificada (audio y vídeo de ENTR-01 a 03; sesión con el prototipo de
  ENTR-11 y 12; depósito abierto de ENTR-01 a 08).
- La rectificación de notas de campo (F1b) queda firmada por 5 de los 6
  integrantes, cada uno desde su cuenta.
- La bitácora de sesiones incorpora la visita del 21/08/2026, declarada
  como evidencia parcial sin acta que la autorice (F4).
- Las fórmulas de `matriz_e2e.xlsx` (hojas Diagnóstico y Sincronización)
  se recalculan: la hoja ya no abre con casillas vacías (D5).
- `CITATION.cff` corrige "ocho entrevistas" por dieciséis y la cabecera del
  ERS corrige "v3.0" por "v2.0" (I1).

### Retirado

- Los 16 PDF presentados como notas de campo manuscritas, cuyo cuerpo era
  idéntico entre sí; la carpeta declara la ausencia real (F1).
- 14 fragmentos de la codificación sin respaldo literal en ninguna
  transcripción, con el motivo de cada uno en
  `07_Datos/datos_procesados/fragmentos_retirados_C2.csv` (C1, C2).

## [4.3.1] - 2026-09-18 - Segunda ronda de correcciones post-evaluacion

### Cambiado

- La tercera captura de autoría de Alcívar pasa a
  `10_Autoria/capturas/2026-09-17_AdonisAlcivar_gitlog_verificar_fichas.png`.
  El nombre anterior reutilizaba la ruta histórica de la captura cuestionada
  por autoría; el nombre definitivo evita esa colisión y describe el contenido
  real mostrado (`git log` sobre `verificar_fichas.py`).
- `10_Autoria/verificacion_seccion15.md` documenta que la primera verificación
  visual no detectó que una de las capturas se había tomado en el equipo de
  Macías Herrera y registra la secuencia posterior de sustitución, retirada y
  renombrado de esa evidencia.
- `10_Autoria/retrospectiva_equipo.md` incorpora una segunda ronda de cierre
  fechada el 18/09/2026, corrige la atribución de las cinco fotografías de la
  sesión complementaria y documenta la autoría real de las etiquetas anotadas.
  Las fotografías fueron incorporadas por Macías Herrera (`e4bab0c`,
  `71e67c0`, `1a20cbe`, `57a3086`, `24a81c2`) y renombradas posteriormente
  por Huilcapi León (`ac5820c`).
- `10_Autoria/aporte_individual.md` corrige la fecha de `7301a59`, describe
  según el historial los tres archivos incorporados en `219fb9a`, registra su
  retirada en `a2480c6` e incorpora los commits posteriores `32a8e7f` y
  `d0b32f2`.
- `README.md` registra el identificador completo del commit congelado por
  `baseline-v6.3` y documenta por separado las dos evaluaciones oficiales
  conservadas en el historial.
- El cierre incorpora la regeneración final de `checksums.sha256` después de
  completar todas las ediciones documentales y antes del commit de cierre.
- `10_Autoria/verificacion_seccion15.md` y `10_Autoria/README.md` acotan a la
  verificación interna del 16/09 dos afirmaciones que declaraban §15 cerrado
  por cuenta del equipo, y remiten al docente la determinación del estado
  oficial del ítem.
- `checksums.sha256` se regeneró nuevamente tras esa edición; verifica 570
  entradas sobre el árbol versionado.
- Esta entrada se consolida en el commit de congelación documental de la ronda
  del 18/09, que no introduce cambios de contenido distintos de los descritos
  aquí. Su identificador se publica en el mensaje de `baseline-v6.4`.

### Corregido

- La evaluación oficial del 17/09/2026 a las 17:50 determinó que §15 y §16
  permanecían en `Por modificar`. Esta entrada registra las correcciones
  posteriores sin reescribir la entrada histórica `[4.3.0]`.
- `checksums.sha256` verificaba correctamente en `baseline-v6.3`
  (`1424f05038cbb6718c9dee3d360f7d9ff6307299`). La regresión apareció después,
  al sustituir y renombrar la captura de autoría: primero como archivo ausente
  y posteriormente como hash no coincidente. No se atribuye esa regresión a
  `baseline-v6.3`.

### Estado de cierre

- `baseline-v5.0` y `baseline-v6.3` se conservan intactas como registros de
  evaluaciones oficiales distintas.
- El mensaje histórico de `baseline-v6.3` afirma que §15, §16 y §3 quedaron
  corregidas; la evaluación posterior no confirmó §15 ni §16. La etiqueta no
  se modifica ni se reutiliza; la discrepancia queda documentada.
- Estas modificaciones se incorporan para atender las observaciones de §15 y
  §16. La determinación de su estado final y cualquier calificación
  corresponden al docente.
- La nueva línea base de cierre se creará únicamente después de verificar el
  commit final desde un clon limpio.

---

## [4.3.0] - 2026-09-17 - Correcciones post-evaluacion oficial

### Añadido

- Documentación de las actas individuales de `Member_Checking/Actas/`, sustituyendo el marcador vacío por un índice verificable de ENTR-01, ENTR-02 y ENTR-13.
- Documentación de las seis actas y los seis consentimientos de `Validacion_Walkthrough/`, sustituyendo los dos marcadores vacíos señalados durante la revisión.
- Cinco fotografías JPG de una sesión complementaria real del cuestionario realizada el 15/09/2026, con metadatos EXIF verificables.
- `02_Evidencias/Cuestionario/Fotos_Aplicacion/readme.md`, que diferencia las cinco fotografías reales de las 15 capturas PNG del instrumento y evita presentarlas como evidencia de la aplicación original de 62 respuestas.
- Consentimiento informado complementario para cinco trabajadores localizables, mantenido separado de las 62 respuestas originales y sin relación uno-a-uno con estas.
- Verificaciones de cierre para evidencia de autoría, metadatos EXIF y resultados estadísticos canónicos.

### Cambiado

- `10_Autoria/correspondencia/readme.md` delimita ahora la captura de WhatsApp como evidencia de coordinación logística de entrevistas y no como evidencia de aplicación del cuestionario original.
- `10_Autoria/README.md` fue actualizado para reflejar la bitácora de 30 sesiones, capturas, notas de campo y documentos de verificación actualmente existentes.
- La documentación de las 62 respuestas originales declara su procedencia vía Google Forms, la presencia de columnas identificativas en la exportación cruda y el uso exclusivo del conjunto anonimizado para análisis.
- El manuscrito final incorpora resultados de saturación temática, alpha de Krippendorff, kappa ponderado y el modelo ordinal, además de la amenaza derivada del consentimiento retrospectivo.
- El repositorio principal fue transferido a `https://github.com/gleiston-guerrero/SIMPA_ISR401`; se actualizaron las referencias canónicas vigentes y se recompilaron la ERS y el manuscrito final con la nueva URL.
- Se documentó en `09_Etica/solicitud_cambio_composicion.md` una solicitud de cambio de composición del equipo. La evaluación oficial posterior mantiene la trazabilidad de los seis integrantes y no considera esa solicitud, por sí sola, como exclusión formal de los miembros afectados.

### Estado de cierre

- §15 fue corregida después de la evaluación oficial: las tres capturas de Alcívar fueron sustituidas por evidencia de artefactos propios y verificadas visualmente por Josthyn Macías. La aceptación definitiva corresponde al docente.
- §16 fue verificada reproduciblemente: los intervalos de confianza al 95 % se regeneran sin producir diferencias en los CSV versionados, las curvas de saturación están incorporadas al manuscrito y la compilación completa finaliza sin errores graves, citas ni referencias indefinidas.
- `07_Datos/checksums_datos.sha256` fue regenerado después de §16 y verifica 38/38 archivos con código de salida 0.
- La composición formal se mantiene trazable con seis integrantes; la solicitud de cambio de composición no sustituye las firmas o aceptaciones requeridas para excluir integrantes.
- `baseline-v5.0` se conserva como línea base oficialmente evaluada. `baseline-v6.0`, `baseline-v6.1` y `baseline-v6.2` se mantienen como líneas base históricas del proceso de cierre. `baseline-v6.3` identifica la línea base final vigente, creada como etiqueta anotada sobre el commit final validado después de regenerar los manifiestos y superar la validación desde un clon limpio; ninguna etiqueta histórica se mueve ni reutiliza.

---

## [4.2.0] - 2026-09-11 - Cierre de saneamiento, experimento y autoría

### Añadido

- Repositorio complementario de evidencias (`SIMPA_ISR401_Evidencias`) con
  los contenedores `.7z` publicados como assets de release, eliminando la
  dependencia de Git LFS del repositorio principal.
- `10_Autoria/`: bitácora de sesiones reconstruida desde el historial real
  de Git, declaración de identidades, aporte individual, exif_inventario.csv,
  inventario de fuentes editables, fotografías reales del equipo,
  declaración de uso de IA.
- `06_Experimento/`: desviación metodológica registrada (EXP-01), material
  fuente y conjunto humano de referencia congelados (EXP-02, EXP-03),
  ejecución del LLM registrada (EXP-04), conjunto cegado (EXP-05),
  reclutamiento y puntuación de tres evaluadores independientes (EXP-06),
  consolidado de puntuaciones reales en formato largo (EXP-07).
- Publicación del dataset en Zenodo con DOI y evaluación FAIR.

### Corregido

- README.md raíz: instrucciones de clonado actualizadas (ya no depende de
  Git LFS).
- Referencias cruzadas de sección en la adenda A.14 tras insertar una
  sección nueva.

### Nota

- El repositorio original (`Villafuerte_Grupo_AHMRV`) quedó archivado en
  privado por una limitación de GitHub (`refs/pull/2/head`) que impedía
  retirar del todo datos identificables del historial pese a la
  reescritura con `git filter-repo`.

---

---
## [4.1.4] - 2026-08-31 - P9: reubicar Palma_Africana.pdf; reconciliar checksums de diagramas traducidos

### Corregido

- `AHMRV/Palma_Africana.pdf` (propuesta inicial del 5 de mayo de 2026) estaba
  suelto en la raíz de `AHMRV/`, sin pertenecer a ninguna de las nueve
  carpetas del árbol obligatorio. Se movió a
  `AHMRV/01_ERS/antecedentes/2026-05-05_Propuesta_Inicial_1A.pdf`.
- `checksums.sha256` no reflejaba la traducción al inglés de los 13 diagramas
  de `AHMRV/03_Modelado/Diagramas_UML/` (fuentes `.puml`, `.png` y `.svg`,
  39 archivos): los nombres cambiaron de español a inglés y varias rutas
  quedaron registradas contra archivos que ya no existían. Se regeneraron
  las 39 entradas de esa carpeta desde el estado actual.
- `checksums.sha256` verificado íntegro: 192/192.

### Nota

- `AHMRV/01_ERS/img/` (usada para compilar `ERS_SRS_2B_v2.0.tex`) conserva
  los diagramas en español; `03_Modelado/Diagramas_UML/` ya está en inglés.
  No es una referencia rota — son dos copias independientes — pero queda
  como inconsistencia de idioma pendiente de resolver por el equipo.

---

## [4.1.3] - 2026-08-31 - P6: declarar el alcance de la trazabilidad de RNF y RD

### Corregido

- `AHMRV/04_Trazabilidad/matriz_e2e.xlsx`: se agregó una nota de alcance
  (fila 4 de `Matriz_E2E`) que declara que las 73 filas trazan extremo a
  extremo los 42 RF y los 18 requisitos de IA (60 de 60), mientras que los
  19 RNF y 10 RD del catálogo se verifican por otra vía. Antes la cabecera
  no acotaba a qué tipo de requisito aplicaba la cadena, lo que podía leerse
  como una omisión de 21 filas que en realidad no faltan bajo el alcance
  decidido en la auditoría de PE5.
- `AHMRV/04_Trazabilidad/readme.md`: se añadió la sección "Alcance de las 73
  filas", con la misma tabla y justificación, para que quien audite el
  repositorio no tenga que inferirlo del cruce manual.
- `AnexoA_auditoria_calidad.xlsx`, hoja `Valoracion`, celda `E8` (criterio de
  M4): decía "Cumple en ambos sentidos, sin requisitos huérfanos", una
  afirmación que abarcaba más que lo medido (M4 se calculó solo sobre los 42
  RF). Se acotó el texto al alcance real. Esta corrección quedó pendiente
  del cierre de P5 y se resuelve en este mismo commit por tratarse de la
  misma declaración de alcance.
- `checksums.sha256` se regeneró para los 3 archivos modificados.

---

## [4.1.2] - 2026-08-31 - Cierre de P5: métrica M2 sin artefacto de respaldo

### Corregido

- `AnexoA_auditoria_calidad.xlsx`, hoja `Valoracion`: el nivel de la métrica
  M2 (Consistencia) se ajustó de 4 a 2. Se confirmó que no existe en este
  repositorio ni en ningún otro lugar accesible al equipo un artefacto que
  respalde los "210 pares / 2 conflictos" reportados en PE5 (la hoja
  `Conflictos_M2` referida por el informe original nunca formó parte del
  Anexo A migrado). El criterio de M2 se actualizó para declarar esta
  limitación explícitamente, siguiendo el mismo estándar de honestidad ya
  aplicado a M6.
- `Portada!B10` del mismo libro apuntaba al aporte individual de M6
  (`Valoracion!D10`, 0.30) en vez de al total ponderado (`Valoracion!D11`).
  Se corrigió la referencia.
- El texto introductorio de la hoja `Valoracion` describía la fórmula como
  "peso × nivel / 4"; la fórmula real (columna `Aporte`) siempre fue
  "peso × nivel", sin dividir. Se corrigió el texto para que coincida con
  la fórmula viva.
- Como consecuencia de los tres puntos anteriores, la valoración ponderada
  total pasó de 3,70 a 3,40 sobre 4,00. El cambio en el número es el efecto
  esperado de declarar una limitación real, no un error a ocultar.
- `checksums.sha256` se regeneró para reflejar el nuevo hash de
  `AnexoA_auditoria_calidad.xlsx` (191/191 verificados).

---

## [4.1.1] - 2026-08-31 - Correcciones post-auditoría de cierre

### Corregido

- Se armonizó la identificación del ERS como Entrega 4 (2B), versión 2.0,
  con fecha 31/08/2026.
- Se añadió la revisión interna 3.2 correspondiente a ERS v2.0 y se aclaró
  la relación histórica con la línea base ERS v1.1 de PE5.
- `CITATION.cff` se actualizó al catálogo vigente de 42 RF y 19 RNF.
- Se sustituyeron las referencias editables al repositorio anterior por
  `https://github.com/AlanNVR/SIMPA_ISR401`, preservando sin modificación
  los documentos firmados.
- `README_Etica.md` incorpora una tabla de correspondencia entre rutas
  históricas y rutas vigentes.
- El criterio muestral se actualizó al umbral vigente de n >= 60,
  distinguiendo el perfil ocupacional agregado (n=60) de los subperfiles
  por labor (18, 18, 13 y 11), sin declarar cumplimiento por subperfil.
- Las referencias a gatekeepers de la Entrega 3 se identificaron
  explícitamente como criterios históricos de la 2A.

### Bibliografía y reproducibilidad

- Se eliminó el fallback silencioso de IEEEtran a `unsrt`.
- Se incorporó `IEEEtran.bst` al directorio del ERS para hacer determinista
  el estilo bibliográfico.
- Se eliminaron los marcadores de trabajo `[RECIENTE]` de la bibliografía.
- Se completaron DOI, ISBN o URL verificables en las referencias citadas
  cuando correspondía.
- La referencia `arora2024` se corrigió a su publicación bibliográfica
  verificable.
- La compilación completa `pdflatex -> bibtex -> pdflatex -> pdflatex`
  finalizó sin errores LaTeX graves, sin errores de BibTeX y sin citas o
  referencias indefinidas.
- El PDF resultante contiene 108 páginas.

## [4.1.0] - 2026-08-31 - Migración y consolidación de la Entrega PE5

### Cambiado

## 31/08/2026 — Migración y consolidación de la Entrega PE5

Se integró al repositorio principal el trabajo consolidado durante la Entrega PE5,
preservando los cambios posteriores que ya existían en `SIMPA_ISR401`.

### ERS

- Se retiró la versión anterior:
  - `ERS_SRS_2A_v1.0.tex`
  - `ERS_SRS_2A_v1.0.pdf`
- Se incorporó y compiló la línea base:
  - `ERS_SRS_2B_v2.0.tex`
  - `ERS_SRS_2B_v2.0.pdf`
- Se migraron las secciones de DFD, inteligencia artificial, casos de uso
  CU-11 a CU-18 y el apéndice BDD.
- Se conservó `declaracion_uso_ia.tex`, creado después de PE5, y se integró
  en la nueva compilación.
- La compilación final se verificó sin errores LaTeX graves ni referencias
  o citas indefinidas.

### Auditoría y control de cambios

Se incorporaron como anexos de soporte:

- `AnexoA_auditoria_calidad.xlsx`
- `AnexoB_registro_defectos.xlsx`
- `Acta_CCB.pdf`
- `RFC-01.pdf`
- `RFC-02.pdf`
- `RFC-03.pdf`

Estos documentos sustentan la evolución de la línea base y las modificaciones
aprobadas mediante el Change Control Board.

### Trazabilidad

- Se incorporó `matriz_e2e.xlsx` como matriz vigente de PE5.
- La matriz contiene 73 filas de trazabilidad.
- Se incorporaron `backlog_export.csv` y las capturas de sincronización con Jira.
- Se corrigió la traza de `RNF-11`, sustituyendo `EV-12` por `EV-10`:
  `EV-07, EV-10`.
- La matriz anterior de 52 filas se conserva como artefacto histórico.

### Priorización

El catálogo funcional quedó reconciliado en:

- 42 RF;
- 24 Must;
- 16 Should;
- 2 Could;
- 0 Won't.

Se incorporaron RF-40, RF-41 y RF-42 como Must conforme a RFC-03.
No se asignaron retrospectivamente valores Kano o WSJF que no estuvieran
documentados en PE5.

### MVP

Se corrigió la cobertura publicada anteriormente como `9/19 = 47,4 %`.

Los valores auditados son:

- 8/21 = 38,1 % respecto al catálogo utilizado durante la construcción del MVP;
- 8/24 = 33,3 % respecto al catálogo vigente post-CCB.

La cifra antigua se conserva únicamente en las notas históricas que documentan
la corrección.

## [4.0.1] — 2026-08-31 · Higiene del historial y portabilidad de checksums

### Corregido

- Se realizó una segunda reescritura del historial, independiente del saneamiento de privacidad anterior, para retirar material ajeno al PFC que permanecía únicamente en commits históricos.
- Se eliminaron del historial las rutas `Tareas_Villafuerte/`, `Grupo_C/`, `MRV_Equipo_B/` y `cambios_fase0_v2.patch`.
- El historial pasó de 281 a 241 commits tras retirar 40 commits asociados exclusivamente a dicho material.
Se verificó nuevamente que el nombre real de la organización no aparece en los commits alcanzables y que el seudónimo `Palmicultora M` permanece correctamente aplicado.
- El tag `v1.0-mvp-demo` fue reescrito durante el saneamiento y quedó asociado al commit limpio equivalente.
- Se añadió `.gitattributes` en la raíz con la regla `* -text` para impedir conversiones automáticas LF/CRLF entre plataformas.
- `checksums.sha256` fue regenerado para incorporar `.gitattributes` y permitir su verificación directa mediante `sha256sum -c checksums.sha256` también en Windows.
- La verificación final se realizó desde un clon fresco del repositorio, sin presentar archivos `FAILED`.

---

## [3.0.0] — 2026-08-03 · Entrega 3 (2A)

Especificación completa con componente empírico. Segunda ronda de trabajo de campo
e incorporación de una organización externa como fuente de requisitos.

### Añadido

**Requisitos**
- 19 requisitos funcionales nuevos (`RF-21` a `RF-39`), derivados en su totalidad
  de la segunda ronda de campo.
- 9 requisitos no funcionales nuevos, completando la cobertura de las nueve
  características de calidad de ISO/IEC 25010:2023.
- `RNF-16`: requisito de explicabilidad obligatorio para los tres componentes
  basados en inteligencia artificial (`RF-07`, `RF-08`, `RF-21`).
- 8 requisitos legales (`RL-01` a `RL-08`) con trazabilidad artículo de la
  LOPDP → requisito del sistema.
- 3 restricciones de diseño nuevas (`RD-08`, `RD-09`, `RD-10`).
- 19 historias de usuario en formato Connextra con criterios INVEST verificados
  y escenarios de aceptación en Gherkin.

**Modelado**
- Modelado organizacional i\*: diagramas de Dependencia Estratégica (SD) y de
  Razón Estratégica (SR).
- Cinco tipos de diagrama nuevos: secuencia (3), actividad, estados (2),
  componentes y despliegue.
- 5 casos de uso detallados adicionales (`CU-06` a `CU-10`), completando 10.
- Diagrama de clases refinado con operaciones además de atributos.

**Evidencia**
- Cinco entrevistas nuevas (`EV-04` a `EV-08`), dos de ellas con personal de una
  organización externa.
- Cuestionario ampliado de 4 a 62 respondientes (`EV-12`).
- Dos tipos documentales de la organización: plan semanal de labores (`EV-11`) y
  hoja de liquidación de presupuesto contra ejecución (`EV-13`).
- Adenda ética de la segunda ronda con declaración de desviación de procedimiento.

**Otros**
- Prototipo funcional (MVP) con nueve pantallas y control de acceso por rol.
- Protocolo experimental registrado en OSF (Enfoque 1: comparación de calidad de
  requisitos humanos frente a los generados por un modelo grande de lenguaje).
- Los cinco archivos raíz obligatorios.

### Modificado
- Documento migrado de Word a LaTeX, reproducible desde el fuente.
- Matriz de trazabilidad ampliada de 24 a 52 filas, con nueve niveles de enlace.
- Bibliografía ampliada de 7 a 31 fuentes primarias, 12 de ellas del período
  2023–2026.
- Priorización: se añaden el modelo de Kano y el cálculo WSJF a la clasificación
  MoSCoW existente.
- Rol de `ENTR-02` corregido a Administrador / Asesor Técnico.

### Corregido
- `RF-17` y `RF-20` carecían de caso de uso asociado en la Entrega 2. La cobertura
  requisito-caso de uso es ahora del 100 %.
- Consentimientos informados: cédula y firma enmascaradas en la copia pública; los
  originales se trasladan a la zona restringida cifrada.
- Metadatos GPS eliminados de todas las fotografías publicadas.
- Nomenclatura de archivos multimedia migrada a
  `YYYY-MM-DD_TipoParticipante_CodigoParticipante_Tecnica.ext`, sustituyendo los
  nombres propios por códigos de participante.
- Archivo de evidencia fotográfica que era un marcador de 2 bytes, reemplazado por
  la imagen real.
- `fichas_tecnicas.csv` presentaba un conflicto de fusión sin resolver y contenía
  únicamente la plantilla de ejemplo. Reconstruido con el inventario real de 30
  archivos multimedia.
- `checksums.sha256`: rutas sin el prefijo `videos/`, carpeta duplicada
  `videos 2/` y un nombre de archivo con acentos.
- Audio de entrevista incorporado como archivo dentro del repositorio, en lugar de
  enlace externo a plataforma de video.

### Renumerado

Para asignar identificadores contiguos a las entrevistas de la segunda ronda, las
evidencias que no eran entrevistas se desplazaron:

| Entrega 2 (1B) | Entrega 3 (2A) | Contenido |
|---|---|---|
| `EV-04` | `EV-09` | Observación de campo |
| `EV-05` | `EV-10` | Cuestionario, aplicación piloto (n=4) |

Toda referencia a `EV-04` o `EV-05` en documentos anteriores a esta versión debe
leerse conforme a esta equivalencia.

### Suposiciones invalidadas

La ampliación del cuestionario a 62 respondientes refutó tres supuestos que la
Entrega 2 daba por establecidos a partir de cuatro respuestas:

1. **No todo el personal dispone de teléfono inteligente.** El 11,3 % declara no
   usarlo. Motivó `RF-35` (registro delegado) y `RD-10`.
2. **Existe conectividad permanente en algunas zonas.** El 25,8 % dispone de señal
   siempre, frente a la afirmación previa de que ninguna persona la tenía.
3. **El rastreo por GPS no goza de aceptación unánime.** El 25,8 % expresa
   reservas. Motivó que `RL-03` exija consentimiento revocable sin consecuencia
   laboral.

### Nota sobre la estructura del repositorio

La Sección 8.1 de la guía establece que la raíz del repositorio debe reproducir el
árbol del proyecto. En este repositorio el proyecto reside en `AHMRV/`.

La ruta se conserva de forma deliberada: es la declarada en la portada del
documento entregado en el SGA, cuya actividad se encuentra cerrada y no admite
modificación. Trasladar el contenido a la raíz produciría un error 404 en el
enlace evaluado y activaría el gatekeeper G1. Se optó por preservar la
verificabilidad del enlace y declarar la desviación estructural.

Los cinco archivos raíz obligatorios sí residen en la raíz del repositorio.

---

## [2.0.0] — 2026-06-26 · Entrega 2 (1B)

### Añadido
- 20 requisitos funcionales con la plantilla de ocho atributos.
- 9 requisitos no funcionales cuantificados según ISO/IEC 25010.
- 7 restricciones de diseño.
- Modelado UML: diagrama de casos de uso con 15 casos y 4 actores, especificación
  textual de 5 casos de uso, diagrama de clases conceptual con 18 clases.
- 8 prototipos de interfaz vinculados a requisitos funcionales.
- Matriz de trazabilidad parcial de 24 filas.
- Priorización MoSCoW de todos los requisitos.
- Cuestionario piloto aplicado a 4 personas trabajadoras.

### Modificado
- Documento unificado que acumula y reemplaza la Entrega 1 (1A).

---

## [1.1.0] — 2026-06-23

### Corregido
Incorporación de la retroalimentación docente sobre la Entrega 1 (1A):
- Diagrama de contexto del sistema.
- Actas formales de entrevista.
- Reformulación de los requisitos brutos con trazabilidad a su fuente.
- Depuración de secciones que no correspondían a la Entrega 1A.

---

## [1.0.0] — 2026-06-01 · Entrega 1 (1A)

### Añadido
- Planificación del proyecto de ingeniería de requisitos.
- Identificación de partes interesadas.
- Tres entrevistas semiestructuradas con consentimiento informado firmado.
- Observación directa del cultivo.
- 29 requisitos brutos trazados a su fuente.
- Repositorio GitHub con estructura inicial.
