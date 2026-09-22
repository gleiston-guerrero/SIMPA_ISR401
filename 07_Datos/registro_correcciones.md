# Registro de correcciones

Cada entrada corresponde a una de las 39 tareas oficiales del Plan de
mejora de datos (19/09/2026). El campo **Estado de rúbrica** se deja en
*pendiente de mapeo* hasta que el docente aclare la diferencia práctica
entre *Por modificar* y *Por culminar*.

---

## G1 — Datos personales

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,40 pts
**Responsable(s):** Macías (capa automatizada) · Arboleda (capa visual)
**Dependencias:** ninguna

### Problema detectado
El repositorio público expone datos personales reales de terceros: nombre
real de la organización, capturas de WhatsApp sin enmascarar, y cédulas/RUC
en los documentos éticos A01, A05, A06, A07, A09, A12, C1 y C2 y, tras un
barrido de todo el repositorio, también en A02, A04, A10, A11, C3 y C4
(cédula del líder y, en C3, la del gestor de evidencias).

### Acción aplicada
Capa automatizada (Macías): extracción de texto de los documentos éticos
mediante script versionado, con búsqueda de patrones de cédula (10 dígitos)
y RUC (13 dígitos). La primera ejecución, sobre los 8 documentos señalados
por el plan, detectó 61 ocurrencias reales. Tras el enmascaramiento de la
capa visual, el script se amplió a los 14 PDF afectados y se corrigió para
no emitir los valores detectados; la ejecución sobre la versión actual
devuelve 0 ocurrencias. Adicionalmente ya se había enmascarado el nombre de
la organización en CHANGELOG.md y en A03, y 2 capturas de WhatsApp.

Capa visual (Arboleda): revisión página por página y enmascarado de los 14 PDF de 09_Etica/ que contenían cédula o RUC (A01, A02, A04, A05, A06, A07, A09, A10, A11, A12, C1, C2, C3 y C4): los números se cubrieron con cajas negras y el texto original se eliminó del archivo, sin escribir texto nuevo. Además se enmascaró el nombre de la organización en A03, en CHANGELOG.md y en las 2 capturas de WhatsApp, y el tatuaje en la Foto 01 del consentimiento complementario. Pendiente: G1b (historial).

Avance capa visual (Arboleda): A01 (commit 2bae024), A05 (commit 9fd0fd6), A06 (commit 0351872), A07 (commit 4e9c742), A09 (commit 787d7d5), A12 (commit ae5b00c), C1 (commit 651d21c), C2 (commit 2b692a5), Foto 01 (commit e837e32), A02 (commit 89da033), A04 (commit d4c1fea), A10 (commit 17bb6ae), A11 (commit ba3e491), C3 (commit 8817784) y C4 (commit 3cde34c) enmascarados y reemplazados. Pendiente: G1b (historial).

### Hallazgo propio (no listado por el plan del docente)

El plan del docente señalaba 8 documentos con datos personales (A01, A05,
A06, A07, A09, A12, C1 y C2). Al ejecutar el barrido automatizado sobre todo
el repositorio, el equipo detectó por iniciativa propia identificadores
adicionales en 6 documentos no listados: A02, A04, A10, A11, C3 y C4. Estos
seis se enmascararon con el mismo procedimiento (capa automatizada + capa
visual) y quedan incluidos en la verificación de 0 ocurrencias sobre los 14
PDF de la versión actual.

### Evidencia utilizada

| Archivo | Contenido |
|---|---|
| `07_Datos/scripts/plan_mejora/buscar_cedulas_ruc.py` | Script de detección. Recorre los 14 PDF éticos y busca patrones de 10 dígitos (cédula) y 13 dígitos (RUC). Emite número de línea, tipo y máscara de longitud; no emite el valor ni el contexto |
| `07_Datos/resultados/g1a_verificacion_cedulas_ruc.txt` | Salida de la ejecución sobre la versión actual: 0 ocurrencias en los 14 archivos |

- Fuente: texto extraído con `pdftotext -layout`
- Persona: Macías (ejecución del script)
- Fecha: 2026-09-19
- Consentimiento: no aplica (detección, no publicación de dato)

### Archivos modificados
- `CHANGELOG.md` (commit baee71b)
- `09_Etica/A03...` punto 4 (commit 778ab60)
- `10_Autoria/correspondencia/2026-07-27_WhatsApp_...png` (commit d355638)
- `02_Evidencias/Documentos_Organizacion/2026-07-27_WhatsApp_...png` (commit d6a9434)
- `07_Datos/scripts/plan_mejora/buscar_cedulas_ruc.py` (nuevo; corregido para no emitir valores)
- `07_Datos/resultados/g1a_verificacion_cedulas_ruc.txt` (nuevo)
- `07_Datos/resultados/g1a_deteccion_cedulas_ruc.txt` (retirado del árbol)
- `09_Etica/A01_Protocolo_Investigacion.pdf` (commit 2bae024)
- `09_Etica/A05_Aval_Institucional.pdf` (commit 9fd0fd6)
- `09_Etica/A06_Declaracion_Conflicto_Intereses.pdf` (commit 0351872)
- `09_Etica/A07_Compromiso_Confidencialidad.pdf` (commit 4e9c742)
- `09_Etica/A09_Nomina_Equipo.pdf` (commit 787d7d5)
- `09_Etica/A12_Certificado_Etica.pdf` (commit ae5b00c)
- `09_Etica/Categoria_C/C1_Aval_Unidad_Productiva.pdf` (commit 651d21c)
- `09_Etica/Categoria_C/C2_Compromiso_Confidencialidad_Estrategica.pdf` (commit 2b692a5)
- `02_Evidencias/Cuestionario/Fotos_Aplicacion/2026-09-15_ConsentimientoComplementario_Foto-01.jpg` (commit e837e32)
- `09_Etica/A02_Instrumentos_Recoleccion.pdf` (commit 89da033)
- `09_Etica/A04_Plan_Gestion_Datos.pdf` (commit d4c1fea)
- `09_Etica/A10_Cronograma_Gantt.pdf` (commit 17bb6ae)
- `09_Etica/A11_Analisis_Riesgos.pdf` (commit ba3e491)
- `09_Etica/Categoria_C/C3_Protocolo_Anonimizacion.pdf` (commit 8817784)
- `09_Etica/Categoria_C/C4_Normativa_Sectorial.pdf` (commit 3cde34c)

### Criterio de aceptación
- [x] Capa automatizada ejecutada y commiteada con salida real
- [x] Capa visual ejecutada, checklist por archivo commiteada
- [x] Los identificadores de cédula y RUC detectados quedan enmascarados en los 14 PDF de la versión actual
- [x] Tatuaje revisado
- [ ] G1b (historial) — bloqueada, requiere autorización escrita del docente

### Verificación

Comando, desde la raíz del repositorio:

    PYTHONIOENCODING=utf-8 python 07_Datos/scripts/plan_mejora/buscar_cedulas_ruc.py

Resultado sobre los 14 PDF de la versión actual:

    TOTAL de ocurrencias detectadas: 0

Comprobación de que la propia salida no expone identificadores:

    grep -cE "[0-9]{10,13}" 07_Datos/resultados/g1a_verificacion_cedulas_ruc.txt
    0

### Commits
- `baee71b` — nombre de organización retirado de CHANGELOG.md
- `778ab60` — nombre de organización enmascarado en A03
- `d355638`, `d6a9434` — capturas de WhatsApp enmascaradas
- `0b1fec9` — salida inicial de detección de cédulas/RUC (retirada posteriormente)
- `2bae024` — datos personales enmascarados en A01 (versión pública)
- `9fd0fd6` — datos personales enmascarados en A05 (versión pública)
- `0351872` — datos personales enmascarados en A06 (versión pública)
- `4e9c742` — datos personales enmascarados en A07 (versión pública)
- `787d7d5` — datos personales enmascarados en A09 (versión pública)
- `ae5b00c` — datos personales enmascarados en A12 (versión pública)
- `651d21c` — datos personales enmascarados en C1 (versión pública)
- `2b692a5` — datos personales enmascarados en C2 (versión pública)
- `e837e32` — zona identificable enmascarada en foto 01 del consentimiento complementario
- `89da033` — cédula enmascarada en A02 (versión pública)
- `d4c1fea` — cédula enmascarada en A04 (versión pública)
- `17bb6ae` — cédula enmascarada en A10 (versión pública)
- `ba3e491` — cédula enmascarada en A11 (versión pública)
- `8817784` — cédula enmascarada en C3 (versión pública)
- `3cde34c` — cédula enmascarada en C4 (versión pública)
- Ver el commit cuyo mensaje es `fix(G1): retirar salida con identificadores y verificar 14 PDF con 0 ocurrencias`

### Limitaciones
Los PDF no tienen fuente LaTeX en el repositorio, así que se enmascararon sobre la versión publicada: los números se cubrieron con cajas negras y el texto original se eliminó del archivo (la extracción de texto ya no los devuelve). Los originales firmados se conservan sin cambios fuera del repositorio público.

La primera ejecución de la capa automatizada produjo el archivo
`07_Datos/resultados/g1a_deteccion_cedulas_ruc.txt`, que emitía cada
identificador detectado junto con la línea de contexto completa del documento
de origen. Ese archivo se incorporó al repositorio en el commit `0b1fec9` y
exponía en texto plano las 61 ocurrencias halladas. Se ha retirado del árbol
de trabajo y el script se corrigió para emitir únicamente el número de línea,
el tipo de identificador y una máscara de la longitud, sin el valor ni el
contexto.

Retirarlo del árbol no lo elimina del historial de Git: el contenido sigue
siendo recuperable desde el commit `0b1fec9`. Su eliminación efectiva exigiría
reescribir el historial publicado, operación excluida de esta ronda de
correcciones. La limitación se declara aquí de forma expresa y queda pendiente
de decisión del equipo junto con el docente.

G1b (historial): las cédulas, el RUC y el nombre real siguen en versiones
anteriores del historial de git y solo pueden retirarse con autorización
escrita del docente; hasta entonces permanecen accesibles.

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## A5 — Adenda de desviación del registro OSF

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,30 pts
**Responsable de la acción externa en OSF:** Villafuerte Rosero Allan Noé
**Responsable de documentación y commit en el repositorio:** Macías Herrera Josthyn Esteban
**Registro OSF:** `4z35d`
**Fecha de la actualización:** 19/09/2026
**Dependencias:** ninguna

### Problema detectado

El plan de mejora señaló dos desviaciones respecto del registro OSF:

1. El `protocolo.pdf` preservado en OSF no coincide en SHA-256 con las
   versiones del mismo archivo disponibles en el repositorio.
2. El registro OSF es del 31/08/2026, mientras que la rúbrica de evaluación
   empleada después está fechada el 04/09/2026.

### Acción aplicada

El 19/09/2026 Villafuerte Rosero Allan Noé, administrador con acceso al
registro, creó y aprobó una actualización de `4z35d`. La única pregunta
modificada fue `Explanation of foreknowledge and managing unintended
influences`, a la que se añadió al final la sección `Actualización / adenda
de desviación — 19/09/2026`.

La adenda declara que no se afirma equivalencia binaria entre el archivo
preservado en OSF y las versiones posteriores del repositorio, que la
diferencia se documenta como desviación de versionado y procedencia, y que
las decisiones derivadas de la rúbrica del 04/09/2026 son posteriores al
registro y no forman parte del contenido preregistrado. La actualización no
modifica retroactivamente la fecha ni el contenido histórico del registro.

No se reemplazó ni eliminó `protocolo.pdf` ni se alteraron otras secciones
del preregistro.

### Verificación de la desviación de SHA-256

La afirmación se comprobó descargando el archivo preservado en OSF y
calculando su digest, en lugar de darla por supuesta:

    sha256sum protocolo.pdf

| Versión del documento | Origen | SHA-256 |
|---|---|---|
| 1.0 — 3 de agosto de 2026 | Preservada en OSF `4z35d` | `516902b9bc60785e17a7c06ec47a69e26cbd69759e85d082d70b91be0f7f4a8d` |
| 1.1 — 31 de agosto de 2026 | Repositorio, commit del 03/09/2026 | `5d194e778b431ac73b45fbe79f7e191942eec7830e2375e2ab3448eb2045a63e` |
| 1.2 — 7 de septiembre de 2026 | Repositorio, versión actual | `ccd6129685685c6445d433fc1eb279c99ede2dc4972db445ee19da8add860c25` |

Los tres digests son distintos entre sí, lo que confirma la desviación
señalada. La diferencia corresponde a un versionado declarado en la portada
de cada documento: OSF preserva la v1.0, que anunciaba el registro como
previsto y la ejecución como pendiente; la v1.1 se rotula «actualización
administrativa del registro OSF» y la v1.2 «aclaración documental del
alcance temporal del registro OSF», ya con el enlace a `https://osf.io/4z35d/`.
No se afirma equivalencia binaria entre ninguna de las tres.

### Evidencia utilizada

| Archivo | Evidencia |
|---|---|
| `10_Autoria/capturas/2026-09-19_allan_OSF_A5_Latest.png` | Vista `Latest`: campo marcado `Updated`, adenda visible, declaración de SHA-256 y cronología 31/08 → 04/09. Muestra además `Date Registered: Aug 31, 2026` |
| `10_Autoria/capturas/2026-09-19_allan_OSF_A5_Original.png` | Vista `Original`: la adenda no aparece y se conserva el texto previo |
| `10_Autoria/capturas/2026-09-19_allan_OSF_A5_API.png` | API pública `/v2/registrations/4z35d/` con 1 coincidencia de `Actualización / adenda de desviación` |
| `10_Autoria/capturas/2026-09-19_allan_OSF_A5_Updates.png` | Panel `Updates` con los estados `Latest`, `Original` y `Update` |

### Criterio de aceptación verificado

- [x] La desviación de `protocolo.pdf` quedó documentada y comprobada por digest
- [x] La cronología 31/08/2026 → 04/09/2026 quedó documentada
- [x] La actualización fue enviada y aceptada en OSF
- [x] `Latest` muestra la adenda y el campo como `Updated`
- [x] `Original` conserva la respuesta anterior sin la adenda
- [x] La API pública expone la respuesta actualizada
- [x] Se preservó el contenido histórico del registro original

### Limitaciones

La acción externa en OSF fue ejecutada por Villafuerte Rosero Allan Noé, por
ser quien dispone del acceso administrativo al registro. Macías Herrera
Josthyn Esteban realizó la documentación, la incorporación de evidencias y el
commit en el repositorio.

El estado de rúbrica corresponde al docente.

### Commits

Ver el commit cuyo mensaje es `docs(A5): registrar adenda OSF y verificacion API`.

---

## E3 — README del prototipo fiel al código

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Responsable:** Macías Herrera Josthyn Esteban
**Dependencias:** ninguna

### Problema detectado

`05_MVP/readme.md` describía funcionalidades del prototipo sin respaldo en el
código y omitía limitaciones comprobables. Además atribuía la condición de
árbol evaluado a la aplicación React, cuando el despliegue sirve una
aplicación autónoma distinta, y afirmaba que el árbol V2 no incluía una
versión HTML independiente.

### Acción aplicada

Revisión del código fuente del archivo realmente entregado y corrección del
README para que cada afirmación corresponda a lo verificable en él:
resultado fijo del análisis de imagen, credenciales en claro, alcance real
del control de acceso por rol, y equivalencia binaria entre las dos copias
del archivo autónomo. Se retiraron las afirmaciones referidas al árbol React
y las instrucciones de ejecución que no correspondían.

### Verificación

Comparación de las dos copias del archivo entregado:

    sha256sum prototipo_v2/Prottotipo_Simpa-main/Prototipo/index.html Prototipo/index.html

Resultado: ambas devuelven
`2859dbb9185e2b5ed02601f9348cffdfa44651e3bc1140f1647b789b43af94d0`.

### Commits

- `4cde2a9` — primera versión, referida al árbol React
- `39a261c` — corrección al archivo realmente entregado
- `fb82f18` — versión final con rutas, commit del submódulo y URL vigente

### Limitaciones

La primera versión de esta corrección (`4cde2a9`) describía `src/app/App.tsx`
con números de línea concretos. Esa descripción era exacta respecto de ese
archivo, pero `App.tsx` no es lo que se publica. El error se detectó al
preparar la prueba E2E y se corrigió en los commits posteriores, sin
reescribir el historial.

---

## E4 — Declaración del uso de Figma Make

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Responsable:** Macías Herrera Josthyn Esteban
**Dependencias:** ninguna

### Problema detectado

`10_Autoria/declaracion_uso_ia.md` declaraba que Figma Make se había usado
para generar «las interfaces del prototipo (mockups funcionales)». La
evidencia del propio árbol muestra que lo generado fue el código fuente, no
únicamente los mockups.

### Acción aplicada

Se corrigió la finalidad declarada y el método de verificación para indicar
que el árbol evaluado es un proyecto de Figma Make, editado posteriormente
por el equipo.

### Verificación

Sobre el árbol canónico `prototipo_v2/Prottotipo_Simpa-main/Prototipo/`:

| Evidencia | Contenido |
|---|---|
| `package-lock.json` | declara el paquete `@figma/my-make-file` |
| `ATTRIBUTIONS.md` | se identifica a sí mismo como «Figma Make file» |
| `vite.config.ts` | incluye un resolver propio para imports `figma:asset/` |

### Commits

- `ed811f5` — declarar generación de código v2 con Figma Make

---

## B6 — Parentesco declarado como amenaza a la validez

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Responsable:** Macías Herrera Josthyn Esteban
**Dependencias:** ninguna

### Problema detectado

El parentesco del analista líder con dos participantes estaba declarado como
conflicto de interés en el Apéndice A del ERS y en `09_Etica/A06`, pero no
figuraba en la sección de amenazas a la validez del manuscrito, pese a
afectar al muestreo del estudio de campo.

### Acción aplicada

Se añadió a `08_Publicacion/manuscrito_final.tex`, en las amenazas del
componente cualitativo, un párrafo que declara el vínculo (`ENTR-02` en
primer grado, `ENTR-07` en segundo), que ambas entrevistas fueron conducidas
por el propio analista líder, y el efecto sobre la selección: la muestra no
es independiente del equipo investigador. Se remite a las medidas de
mitigación ya documentadas y se declara que ningún hallazgo descansa
únicamente sobre esas dos fuentes.

### Verificación

    grep -n -A4 "textbf{Selecci" 08_Publicacion/manuscrito_final.tex

Devuelve el párrafo a partir de la línea 561, inmediatamente después del
párrafo de credibilidad.

### Commits

- `e4c3045` — declarar parentesco como amenaza a la validez

### Limitaciones

No se compiló el manuscrito en la máquina de ejecución: no hay distribución
LaTeX instalada (`pdflatex` devuelve 127). El bloque insertado usa solo
`\textbf` y `\texttt`, con llaves balanceadas y el guion bajo escapado, sin
depender de macros del preámbulo. El PDF publicado en el repositorio no
incorpora todavía este párrafo; su recompilación queda pendiente.

---

## D6 — Alcance real de Jira y composición del CCB

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Responsable:** Macías Herrera Josthyn Esteban
**Dependencias:** ninguna

### Problema detectado

`04_Trazabilidad/readme.md` presentaba el backlog de Jira como evidencia de
gestión sin declarar que ninguna incidencia fue asignada ni iniciada, que
una parte sustancial fue creada por una persona ajena al equipo, ni cómo
estaba compuesto realmente el CCB.

### Acción aplicada

Se añadieron dos secciones al readme de trazabilidad: el alcance real de la
gestión en Jira, con las cifras derivadas por script, y la composición del
CCB según el acta, declarando que ninguna persona de la organización cliente
participó en él.

### Verificación

    python3 07_Datos/scripts/plan_mejora/resumen_backlog.py

Resultado, reproducible desde `04_Trazabilidad/backlog_export.csv`:

| Hecho | Valor |
|---|---|
| Incidencias en el export | 175 |
| En estado «Tareas por hacer» | 175 (100 %) |
| Sin persona asignada | 175 (100 %) |
| Creadas por persona ajena a AHMRV | 84 |

Salida completa en `07_Datos/resultados/d6_resumen_backlog.txt`.

### Commits

- `0c33319` — derivar por script el resumen del backlog de Jira
- `12f5857` — declarar alcance real de Jira y CCB

### Limitaciones

El plan de mejora indicaba que el «representante del cliente» del CCB era el
líder del equipo. El acta `01_ERS/anexos/Acta_CCB.pdf` muestra que ese
asiento lo ocupó Mora Duarte Alex José, estudiante ajeno tanto a AHMRV como a
la organización. Se declaró lo que sostiene la evidencia: el CCB no contó con
representación real del cliente. Si el docente se refería a otra cosa, la
redacción debe revisarse.

---

## E1 — Prototipo y prueba de extremo a extremo

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Responsable(s):** Macías Herrera Josthyn Esteban (implementación de RF-40/41/42) y Arboleda Yanza Francisco Javier (prueba de extremo a extremo por rol)
**Dependencias:** ninguna

### Problema detectado

El repositorio no contenía el prototipo que se estaba entregando: el archivo
desplegado no correspondía a ninguna versión versionada. Además, RF-40, RF-41
y RF-42 figuraban en el README como flujos incorporados, pero no existían en
el archivo entregado, y el control de acceso por rol solo restringía una
pantalla.

### Acción aplicada

Se implementaron los tres flujos de derechos LOPDP sobre la bitácora
existente, conforme a los criterios de aceptación del ERS, y se subieron al
repositorio del prototipo en sus dos rutas. Se actualizó el puntero del
submódulo y se declaró en el README el alcance real del control de acceso por
rol.

### Verificación

Ejecución de los tres flujos sobre el estado del prototipo:

| Criterio del ERS | Resultado |
|---|---|
| RF-40 exporta los datos del titular autenticado | Ficha vinculada correctamente |
| RF-41 registra valor anterior, fecha, autor y motivo | Los cuatro campos quedan asentados |
| RF-41 no permite borrar entradas de bitácora | La interfaz no ofrece esa función |
| RF-42 exige relación laboral terminada | Rechaza el intento sobre ficha activa |
| RF-42 sustituye por identificador disociado | `Trabajador 1` → `ANON-0001`, contacto vaciado |
| RF-42 conserva los totales de avance | Idénticos antes y después |
| RF-42 no deja el nombre recuperable | Parcial: no aparece en pantallas ni exportaciones, pero por lectura del código el nombre permanece en `localStorage` (campo interno `registeredBy`); no verificado en el despliegue (ver prueba E2E) |

### Commits

- `035470c` (repositorio del prototipo) — implementar RF-40, RF-41 y RF-42
- `147d9d1` — actualizar el puntero del submódulo
- `fb82f18` — README final del MVP

### Limitaciones

**Actualización del 21/09/2026.** La prueba de extremo a extremo por rol ya se ejecutó sobre el despliegue (no solo la lógica fuera del navegador): `05_MVP/evidencia_e2e/registro_prueba_e2e.md`, con fecha, ejecutor y evidencia gráfica en `05_MVP/evidencia_e2e/`. Resultado: el control de acceso restringe `Personal` (Administrador) y `Reportes` (Supervisor y Administrador) — más de lo que el README declaraba originalmente, y ya corregido; RF-40 y RF-41 cumplen sus criterios; RF-42 rechaza la supresión con relación activa y disocia la ficha en pantalla, bitácora y exportaciones, pero el nombre permanece en el almacenamiento local del navegador (no verificado en el despliegue); RF-22 es funcional parcial (umbral global, no por variedad).

El despliegue de Netlify se publica manualmente y no está enlazado al repositorio; el comportamiento observado coincide con el código del commit declarado en varios puntos comprobados, pero eso no prueba que sean exactamente el mismo commit.
---

## A1 — Repetir la evaluación con evaluadores externos

**Estado operativo:** NO EJECUTADA POR FALTA DE TIEMPO (avance real documentado, sin evaluación completa)
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,80 pts
**Responsable(s):** Sin asignar (fuera del núcleo de la rev. 8)
**Dependencias:** A2, A3

### Problema detectado
Las tres hojas de puntuación se subieron el 12/09 con 25 y 27 segundos de diferencia. En 131 de 150 filas las puntuaciones siguen un ciclo por posición de fila; en 139 de 150 las cinco dimensiones valen lo mismo; los comentarios de dos evaluadores citan términos que no aparecen en los requisitos; el registro de evaluadores fecha la evaluación antes de que existieran el archivo cegado y las instrucciones.

### Acción aplicada
Se consiguieron 3 evaluadores externos reales (EVA-A01, EVA-A02, EVA-A03), cada uno con consentimiento informado y declaración de ausencia de conflicto de interés firmados el 19/09/2026, todos con "No" en los 7 ítems de conflicto. No se alcanzó a completar la sesión de puntuación de los 47 requisitos por falta de tiempo antes del cierre del plan.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] Ninguna hoja con periodicidad por posición (coincidencia menor del 80 % para periodos 2 a 10)
- [ ] COM distinta de CON en al menos el 20 % de las filas
- [ ] Cada término citado en un comentario aparece en su requisito
- [ ] Fechas posteriores al archivo cegado
- [ ] Explicación escrita de cómo se produjeron las hojas actuales (ver A12 del plan de ejecución)

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
Se avanzó la parte documental (consentimientos y declaraciones de 3 evaluadores reales, verificados uno por uno), pero no se ejecutó la evaluación de los 47 requisitos por falta de tiempo del equipo antes del cierre del plan. Se declara así, sin inventar puntuaciones.

Qué haría falta: Evaluadores reales de otro paralelo, sin participación en el proyecto, con consentimiento firmado y declaración de conflicto de interés; cada evaluador sube su propia hoja o la sube un custodio ajeno al equipo. Depende de A2 y A3. La explicación escrita se entrega por correo aunque no se repita la evaluación.

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## A2 — Normalizar el estilo de los dos conjuntos antes de cegar

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** criterio técnico ejecutado; pendiente de valoración docente
**Peso:** 0,40 pts
**Responsable(s):** Francisco Javier Arboleda Yanza — ejecución y verificación de A2
**Dependencias:** A3 — satisfecha mediante el conjunto humano reconstruido de 22 requisitos

### Problema detectado
Antes de la normalización, el origen de los requisitos era altamente identificable mediante rasgos superficiales de redacción. Sobre los 47 requisitos disponibles después de A3 (22 humanos y 25 LLM), el clasificador versionado basado en primera palabra y longitud total obtuvo 43/47 aciertos (91,49 %).

La referencia histórica del plan indicaba medias de 619 caracteres para el conjunto del equipo y 464 para el LLM, pero la fórmula exacta utilizada para obtener esos valores no quedó versionada. Por ello no se afirma haber reconstruido exactamente esa medición histórica.

### Acción aplicada
Se creó una capa derivada de normalización previa al cegado conservando intactos los artefactos fuente.

La normalización:
- unificó el esquema visible de ambos conjuntos;
- añadió prefijos comunes en descripción, criterio y pre/postcondiciones;
- retiró del campo visible de actor las marcas de evidencia/procedencia;
- compactó la redacción del conjunto humano sin eliminar reglas, umbrales ni condiciones técnicas;
- mantuvo identificadores de origen únicamente en los artefactos internos de verificación de A2;
- dejó los identificadores de origen únicamente en los artefactos internos de A2; posteriormente, el cegado correctivo post-A2 eliminó esos identificadores de los campos visibles y generó un artefacto independiente para A1.

### Evidencia utilizada
- `06_Experimento/conjuntos/requisitos_humano_ENTR-04.csv` — 22 requisitos humanos reconstruidos en A3.
- `06_Experimento/salidas_llm/requisitos_LLM_ENTR-04.md` — 25 requisitos LLM.
- `07_Datos/resultados/a2_identificabilidad_antes_despues.md` — medición reproducible antes/después.
- `07_Datos/resultados/a2_normalizacion_manifest.json` — manifiesto de entradas, salidas y hashes.
- `07_Datos/scripts/plan_mejora/normalizar_estilo_A2.py` — normalización reproducible.
- `07_Datos/scripts/plan_mejora/clasificador_origen_A2.py` — clasificador simple con validación dejando uno fuera.
- `06_Experimento/cegado/requisitos_cegados_A2.csv` — conjunto cegado correctivo de 47 requisitos, identificado como `R-001` a `R-047`.
- `06_Experimento/scripts_analisis/cegar_aleatorizar.py` — generación reproducible del cegado post-A2.

### Archivos modificados
- `06_Experimento/normalizado_A2/requisitos_humano_A2.csv`
- `06_Experimento/normalizado_A2/requisitos_LLM_A2.csv`
- `07_Datos/resultados/a2_identificabilidad_antes_despues.md`
- `07_Datos/resultados/a2_normalizacion_manifest.json`
- `07_Datos/scripts/plan_mejora/normalizar_estilo_A2.py`
- `07_Datos/scripts/plan_mejora/clasificador_origen_A2.py`
- `06_Experimento/cegado/requisitos_cegados_A2.csv`
- `06_Experimento/scripts_analisis/cegar_aleatorizar.py`
- `06_Experimento/readme.md`

### Criterio de aceptación
- [x] Un clasificador simple (primera palabra y longitud, validación dejando uno fuera) no supera el 65 % de acierto sobre el origen.

### Verificación
Clasificador combinado de primera palabra y longitud total de los siete campos visibles, con validación leave-one-out, 47 casos, probabilidades previas iguales por clase y sin utilizar identificadores ni metadatos de procedencia:

- Antes de normalizar: 43/47 aciertos = 91,49 %.
- Después de normalizar: 27/47 aciertos = 57,45 %.
- Umbral exigido: ≤ 65 %.
- Resultado técnico: CUMPLE.

La longitud visible media después de normalizar fue de aproximadamente 558,5 caracteres para los requisitos humanos y 540,2 para los requisitos LLM.

### Commits
- `5e87be8b0ce379335d75095e945509cf243f0720` — `A2: normalizar estilo y verificar identificabilidad`
- `8ae7eb3924f337c54c7cb7bf9d38e10ced8465d8` — `A2: generar cegado correctivo post-normalizacion`

### Limitaciones
El 57,45 % demuestra únicamente el cumplimiento del criterio técnico definido para este clasificador simple y versionado; no demuestra indistinguibilidad frente a cualquier clasificador posible.

Los archivos normalizados de A2 son artefactos internos etiquetados para poder verificar la medición y conservan `id_origen`; por ello no deben entregarse como material cegado. El cegado correctivo posterior fue generado en `06_Experimento/cegado/requisitos_cegados_A2.csv`, con 47 requisitos identificados como `R-001` a `R-047`, sin identificadores explícitos de procedencia en los campos visibles. Este artefacto no sustituye ni modifica el cegado histórico de 50 requisitos utilizado en la evaluación original.

La valoración académica final corresponde al docente.

### Evidencia entregada fuera del repositorio
Se genera `../mapa_confidencial_NO_SUBIR/mapa_origen_A2.csv` como mapa confidencial entre `id_cegado`, origen e identificador original. Este archivo permanece fuera del repositorio y no se entrega a los evaluadores.


---

## A3 — Rehacer el conjunto del equipo desde la transcripción congelada ENTR-04

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** criterio técnico ejecutado; pendiente de valoración docente
**Peso:** 0,30 pts
**Responsable(s):** Macías Herrera
**Dependencias:** Ninguna

### Problema detectado
El plan de mejora señaló que el conjunto humano de 25 requisitos contenía requisitos históricos sin respaldo localizado en ENTR-04, filas cuya procedencia y nota metodológica debían revisarse y cuatro pares humano/LLM que requerían tratamiento separado.

### Acción aplicada
Se aplicó la Ruta A del plan: reconstruir el conjunto humano únicamente con requisitos para los que se confirmó un fragmento literal en la transcripción congelada ENTR-04.

- Se revisaron las 25 fichas H-001 a H-025.
- Se localizaron y verificaron 22 citas literales.
- Se retiraron H-001, H-004 y H-006 al quedar como `NO_LOCALIZADA`.
- El conjunto reconstruido quedó con 22 requisitos reales; no se inventaron requisitos para conservar el mínimo histórico de 25.
- Los 16 requisitos experimentales H-010 a H-025 permanecen en el conjunto.
- Se verificó la alineación de `procedencia` y `nota_metodologica` en H-002, H-003, H-013, H-014, H-015 y H-020.
- Los pares H-013/LLM-005, H-014/LLM-006, H-015/LLM-007 y H-020/LLM-015 quedaron marcados para análisis separado.
- H-010 declara explícitamente que el identificador único corresponde a una formalización de diseño.
- H-024 distingue el respaldo literal sobre proyección/capacidad/redistribución de la mecánica exacta añadida como formalización de especificación.

### Evidencia utilizada
- Fuente congelada: `06e241b7ba0ec43d8541c8908bca31a9f7327ffb:02_Evidencias/Transcripciones/2026-07-28_ENTR-04_Transcripcion.md`.
- SHA-256 de ENTR-04 congelada: `5e9cf9dca6af94061ae937c47a6644dde924061c8382325515e258c377c63313`.
- CSV humano base: `2d7816c27c3f41ab20433865546c4de73b0bd736:06_Experimento/conjuntos/requisitos_humano_ENTR-04.csv`.
- Blob del CSV base: `9f7890d54162eefcf66cd2156a363547087ff8c7`.
- `07_Datos/resultados/a3_candidatas_confirmadas.md`.
- `07_Datos/resultados/a3_analisis_pares_casi_identicos.md`.

### Archivos modificados
- `06_Experimento/conjuntos/requisitos_humano_ENTR-04.csv`
- `07_Datos/resultados/a3_candidatas_confirmadas.md`
- `07_Datos/resultados/a3_analisis_pares_casi_identicos.md`
- `07_Datos/scripts/plan_mejora/aplicar_revision_A3.py`
- `07_Datos/scripts/plan_mejora/verificar_A3.py`

### Criterio de aceptación
- [x] Cada RF conservado del equipo cita un fragmento literal de ENTR-04.
- [x] Columnas `procedencia` y `nota_metodologica` verificadas y alineadas en las filas señaladas.
- [x] Pares casi idénticos identificados y tratados para análisis aparte.

### Verificación
Se ejecutó:

`python 07_Datos/scripts/plan_mejora/verificar_A3.py`

Resultado:

- `RESULTADO: A3 VERIFICADA SIN ERRORES`
- Filas finales: 22.
- Retiradas: H-001, H-004 y H-006.
- Citas literales verificadas: 22/22.
- Pares señalados por el plan tratados aparte: 4/4.
- SHA-256 del CSV reconstruido: `e5801374c719efd4206a9a41972e227b5842b3eeafcad731f9d350f8e9dfed40`.

La verificación se repitió correctamente después de sincronizar `main` con las actualizaciones posteriores de transcripciones.

### Commits
- `41556592dc85d3ee2b5b11d0ccfdfb4d74b8b1b3` — `A3: reconstruir conjunto humano desde ENTR-04 congelada`

### Limitaciones
El conjunto final contiene 22 requisitos y no 25, porque tres requisitos históricos no pudieron vincularse a un fragmento literal de la fuente congelada y se retiraron en lugar de sustituirlos con contenido inventado.

H-010 y H-024 contienen decisiones de formalización de especificación que exceden la literalidad estricta de sus citas; estas diferencias quedaron declaradas explícitamente en `nota_soporte_a3`.

La transcripción ENTR-04 de la rama principal recibió posteriormente cambios de presentación/documentación. A3 permanece deliberadamente anclada a la versión congelada del commit `06e241b7ba0ec43d8541c8908bca31a9f7327ffb` y a su SHA-256 para conservar reproducibilidad.

### Evidencia entregada fuera del repositorio
No aplica.

---

## A4 — Archivar la interacción con el LLM

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** Ninguna

### Problema detectado
El registro de la consulta al LLM (`06_Experimento/prompts_llm/2026-09-11_1300_claude-sonnet-5.md`) tenía un campo con marcador de posición, la salida cruda parecía idéntica byte a byte a la salida procesada sin explicación, y el commit `037f995` borró una nota que reconocía honestamente el desfase entre la hora de la consulta (13:00) y la hora en que se subió `salida_cruda_llm.txt` al repositorio (23:25 del mismo día).

### Acción aplicada
Se revisó el estado actual del archivo de registro y se confirmó que todos
los campos están completos, con las limitaciones de parámetros no expuestos
por la interfaz (temperatura, top-p, top-k, semilla) declaradas
explícitamente como tales, no como placeholders vacíos.

Se verificó, en la sección "Depuración aplicada" del mismo archivo, que la
razón por la que la salida cruda y la respuesta documentada son idénticas
es que no se aplicó ninguna depuración: el modelo entregó la respuesta ya
organizada en el formato requerido. Esto se declara explícitamente en el
propio archivo, no es un hallazgo nuevo de esta corrección.

Se revisó el diff del commit `037f995` (autor: huilcapi) y se confirmó que
eliminó la nota que reconocía el desfase entre las 13:00 (hora de la
consulta) y las 23:25 (hora del commit que subió `salida_cruda_llm.txt`).
Se restituyó esa nota mediante un commit nuevo, sin modificar ni reescribir
el commit `037f995`, conforme a la regla de no reescribir historial.

### Evidencia utilizada
- `06_Experimento/prompts_llm/2026-09-11_1300_claude-sonnet-5.md` — estado actual del archivo
- Diff del commit `037f995`: elimina la frase sobre el desfase 13:00 / 23:25
- Hash SHA-256 del material fuente verificado contra `06_Experimento/material_fuente/ENTR-04_fuente_congelada.md` (EXP-02): coincide exactamente

### Archivos modificados
- `06_Experimento/prompts_llm/2026-09-11_1300_claude-sonnet-5.md` (commit `1aa89c0`)

### Criterio de aceptación
- [x] Conversación archivada — prompt literal y respuesta íntegra conservados en el archivo de registro
- [x] Prompt recalculable desde la fuente congelada — hash verificado contra EXP-02
- [x] La nota borrada se restituye — commit nuevo, sin reescribir `037f995`

### Verificación
Comando:

    git show 037f995 -- 06_Experimento/prompts_llm/2026-09-11_1300_claude-sonnet-5.md

Resultado: confirma que la línea eliminada contenía la nota del desfase horario, restituida en el commit `1aa89c0`.

### Commits
- `1aa89c0` — `docs(A4): restituir nota de desfase horario borrada en 037f995`

### Limitaciones
El bloque "Consigna literal" del archivo de registro conserva entre corchetes la indicación [a continuación, el contenido íntegro de la transcripción anonimizada] en lugar del texto de la transcripción. El prompt completo se reconstruye concatenando la consigna con el contenido de `ENTR-04_fuente_experimento.md` (SHA-256 `5e9cf9dca6af94061ae937c47a6644dde924061c8382325515e258c377c63313`, que coincide con el de `02_Evidencias/Transcripciones/2026-07-28_ENTR-04_Transcripcion.md`).
El desfase entre la hora de la consulta (13:00) y la hora de subida al
repositorio (23:25) queda declarado, pero no eliminado: la consulta real
al modelo ocurrió antes de que se documentara y subiera. Los parámetros de
temperatura, top-p, top-k y semilla no están disponibles porque la interfaz
de chat web de claude.ai no los expone; esto se declara como amenaza a la
reproducibilidad, no como dato faltante por omisión.

### Evidencia entregada fuera del repositorio
No aplica.

---

## A6 — Retirar los resultados del experimento como hallazgo

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** ninguna

### Problema detectado
La comparación entre el conjunto humano y el generado por el LLM se presentaba como un resultado interpretable: `06_Experimento/readme.md` afirmaba que «en las cinco dimensiones el odds ratio fue inferior a 1, lo que indica una tendencia estimada hacia puntuaciones menores para el conjunto LLM», y describía el acuerdo entre evaluadores como «bajo». La fiabilidad real de la medición no estaba calculada en ninguna parte, ni la potencia del diseño.

### Acción aplicada
Se escribió `07_Datos/scripts/plan_mejora/fiabilidad_potencia_A6.py`, que
calcula sobre las puntuaciones reales las tres cifras que determinan si esa
comparación puede leerse como un hallazgo:

- el **alfa de Krippendorff** ordinal por dimensión;
- el **ICC(2,1)** por dimensión —efectos aleatorios en dos vías, medición
  única, acuerdo absoluto—, que no estaba calculado;
- el **efecto mínimo detectable** en d de Cohen para dos grupos de 25, con
  alfa 0,05 bilateral y potencia 0,80, mediante la distribución t no central.

**El alfa no se recalcula**: se lee de `07_Datos/resultados/acuerdo_krippendorff.csv`,
que produce `calcular_acuerdo_evaluadores.py` con la librería `krippendorff`
0.8.2. Reimplementarlo habría dado una segunda cifra para lo mismo, que es
justo el defecto que este plan corrige.

Con esas cifras se retiró la lectura sustantiva del resultado en los tres
puntos donde se afirmaba:

1. `06_Experimento/readme.md`, sección de resultados de RQ1: la frase sobre la
   tendencia se sustituye por la declaración de que el odds ratio estimado
   **no se interpreta como un hallazgo del dominio**, con las tres cifras y su
   explicación. La tabla de los cinco modelos se conserva porque documenta lo
   ejecutado, no porque sostenga una conclusión.
2. `06_Experimento/readme.md`, sección de acuerdo: el acuerdo deja de
   describirse como «bajo». Un alfa en torno a cero significa que los
   evaluadores no coincidieron más de lo que coincidirían al azar, y eso no es
   solo una limitación de validez de conclusión: invalida la lectura
   sustantiva de cualquier comparación construida sobre esas puntuaciones.
3. `07_Datos/desviaciones.md`: la afirmación «no se incorporaron resultados
   hipotéticos ni observaciones fabricadas» se conserva —es cierta, cada
   puntuación procede de una hoja real— y se acota: que los datos sean reales
   no significa que los resultados sean interpretables.

### Cifras obtenidas
| Dimensión | alfa de Krippendorff | ICC(2,1) |
|---|---:|---:|
| COM | −0,0151 | 0,0900 |
| AMB | −0,0033 | 0,1081 |
| VER | 0,0270 | 0,1223 |
| COR | −0,0025 | 0,0963 |
| CON | −0,0151 | 0,0900 |

Efecto mínimo detectable con 25 por grupo, alfa 0,05 bilateral y potencia
0,80: **d = 0,81**.

### Lectura declarada
Con un alfa entre −0,015 y 0,027 y un ICC entre 0,09 y 0,12, la puntuación que
recibe un requisito depende más de quién la asigna que del requisito. Un odds
ratio calculado sobre mediciones sin fiabilidad describe el comportamiento de
los evaluadores, no la calidad de los requisitos.

Y con un efecto mínimo detectable de d = 0,81, **no encontrar diferencia
significativa era el resultado esperable**, no evidencia de equivalencia entre
los dos conjuntos. Ambas cosas quedan escritas donde antes se leía la
tendencia.

### Evidencia utilizada
- `07_Datos/datos_procesados/puntuaciones_experimento_con_origen.csv` — 750 puntuaciones reales
- `07_Datos/resultados/acuerdo_krippendorff.csv` — alfa por dimensión
- Fecha: 21/09/2026

### Archivos modificados
- `07_Datos/scripts/plan_mejora/fiabilidad_potencia_A6.py`
- `07_Datos/resultados/fiabilidad_potencia_A6.csv` y `fiabilidad_potencia_A6.txt`
- `06_Experimento/readme.md`
- `07_Datos/desviaciones.md`

### Criterio de aceptación
- [x] Ningún documento presenta esos resultados como hallazgo
- [x] Fiabilidad y potencia declaradas, con cifras que salen de un script

### Verificación
Comando:

    python3 07_Datos/scripts/plan_mejora/fiabilidad_potencia_A6.py

Resultado:

    Dimensiones: 5 | requisitos: 50 | evaluadores: 3
    alfa de Krippendorff: -0.0151 a 0.0270
    ICC(2,1):             0.0900 a 0.1223
    Efecto minimo detectable (25 por grupo, alfa 0.05, potencia 0.8): d = 0.81

### Limitaciones
El experimento se conserva íntegro en el repositorio: no se borra ningún
resultado ni ningún archivo. Lo que se retira es su lectura como hallazgo
sobre la calidad de los requisitos.

La fiabilidad nula no se corrige con esta tarea y no puede corregirse
a posteriori: exigiría repetir la evaluación con un instrumento y un
entrenamiento de evaluadores distintos, que es lo que pide la tarea A1.

### Evidencia entregada fuera del repositorio
No aplica.

---
## B1 — Retranscribir literalmente las entrevistas de las rondas 1 y 2

**Estado operativo:** VERIFICADA (las ocho entrevistas cumplen los tres criterios de aceptación)
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,50 pts
**Responsable(s):** Macías Herrera Josthyn Esteban (retranscripción de ENTR-01 a 08 y script verificador) · Arboleda Yanza Francisco Javier (corrección de turnos de ENTR-02 y declaración de cobertura)
**Dependencias:** acceso a los audios originales

### Problema detectado
Las entrevistas ENTR-01 a 08 tenían 0 % de turnos con muletillas frente a 6-69 % en la ronda 3, contenían glosas editoriales y el consolidado decía que se presentaban en el orden solicitado.

### Acción aplicada
Se retranscribieron desde el audio original las ocho entrevistas de las rondas 1 y 2, con marcas de tiempo `[mm:ss]` y conservando muletillas, repeticiones y pausas. Los archivos individuales `AAAA-MM-DD_ENTR-XX_Transcripcion.md` pasan a ser la versión vigente de esta carpeta.

En ENTR-02 se corrigieron turnos mal atribuidos en el tramo 18:09-18:45. El fragmento CONSOLIDADO_SEMANAL se registró como pendiente de verificación contra el audio y **no** se dio por retirado ni por incorporado, porque la versión en texto aportada el 21/09 coincide temáticamente pero no tiene minuto de audio verificable.

La cobertura de cada transcripción frente a la duración real del audio se declara en `02_Evidencias/Transcripciones/readme.md`. Las duraciones salen de un script, no están escritas a mano.

### Hallazgo propio del equipo
Siete de las ocho transcripciones cubrían el audio dentro del ±10 % desde el 20/09/2026. **ENTR-03 quedó resuelta el 21/09/2026:** se escuchó el tramo final (04:15 a 05:13) y se confirmó que es ruido ambiental de campo, sin habla; se agregó una nota con marca de tiempo que lo declara así, sin inventar diálogo. La última marca pasa a `[05:13]`, coincidente con la duración real del audio.
### Evidencia utilizada
- Audios y vídeos originales inventariados en `02_Evidencias/00_Restringido/fichas_tecnicas.csv`
- Salida de `07_Datos/scripts/plan_mejora/duracion_por_entrevista.py`
- Script `07_Datos/scripts/plan_mejora/verificar_retranscripcion_B1.py`
- Fecha: 20/09/2026 y 21/09/2026

### Archivos modificados
- `02_Evidencias/Transcripciones/2026-05-23_ENTR-01_Transcripcion.md` y las siete restantes de ENTR-02 a ENTR-08
- `02_Evidencias/Transcripciones/readme.md`
- `07_Datos/scripts/plan_mejora/verificar_retranscripcion_B1.py`

### Criterio de aceptación
- [x] Marcas [mm:ss] en las ocho transcripciones
- [x] La última marca coincide ±10 % con la duración del audio, en las ocho entrevistas
- [x] Cobertura de cada entrevista declarada frente a la duración real del audio

### Verificación
Comando:

    python3 07_Datos/scripts/plan_mejora/duracion_por_entrevista.py 02_Evidencias/00_Restringido/fichas_tecnicas.csv

Resultado (contrastado con la última marca de cada archivo):

    ENTR-01  18:05 / 18,2 min = 99 %      ENTR-05  05:16 / 5,3 min = 99 %
    ENTR-02  27:38 / 29,5 min = 94 %      ENTR-06  02:33 / 2,6 min = 98 %
    ENTR-03  05:13 /  5,2 min = 100 %     ENTR-07  05:32 / 5,5 min = 101 %
    ENTR-04  13:23 / 13,4 min = 100 %     ENTR-08  08:58 / 9,3 min = 96 %

### Commits
- `ed5894e`, `d3b475a`, `3bc3dc4`, `f9fad42`, `eee7275`, `2d7816c` — retranscripción
- `54e0209` — corrección de turnos de ENTR-02
- `d9e80ca` — CONSOLIDADO_SEMANAL como pendiente de verificación

### Limitaciones

Esta tarea invalidó temporalmente la verificación de citas de C1: las citas literales se habían localizado sobre las transcripciones anteriores. Se rehicieron y C1 vuelve a cumplir (ver su entrada).

### Evidencia entregada fuera del repositorio
No aplica.

---
## B2 — Corregir la declaración de uso de IA sobre la transcripción

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,10 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** Ninguna

### Problema detectado
`10_Autoria/declaracion_uso_ia.md` (líneas 125-127) afirmaba que la
transcripción fue una conversión automática literal que "no genera texto
nuevo", lo cual omitía que el texto resultante fue reestructurado
posteriormente con una segunda herramienta de IA.

### Acción aplicada
Se corrigió el bullet de "Transcripciones de entrevistas" dentro de "Áreas
donde NO se usó IA generativa", separando el contenido primario (lo dicho
por los entrevistados, no generado por IA) del procesamiento posterior de
la transcripción (sí asistido por IA). Se añadió la sección 10
"Transcripción de entrevistas (procesamiento)", con tabla completa,
declarando el procedimiento real en dos fases: (1) transcripción automática
(voz a texto) del audio original con TurboScribe (turboscribe.ai);
(2) reestructuración del texto resultante con ChatGPT (versión gratuita)
para separar el contenido en párrafos por hablante e identificar quién dijo
cada intervención. Se declara expresamente que esta segunda fase no es una
conversión literal, sino una reorganización del texto entregado por la
primera herramienta.

### Evidencia utilizada
- Archivo: `10_Autoria/declaracion_uso_ia.md`, bullet corregido y sección 10 nueva
- Fuente: procedimiento descrito directamente por Arboleda Yanza Francisco Javier
- Fecha: 19/09/2026
- Consentimiento: no aplica (declaración de metodología, no dato de participante)

### Archivos modificados
- `10_Autoria/declaracion_uso_ia.md` (commits `1ca7a13` y `6ab6818`)

### Criterio de aceptación
- [x] Declaración coherente con el procedimiento real

### Verificación
Comando:

    grep -n "TurboScribe\|ChatGPT" 10_Autoria/declaracion_uso_ia.md

Resultado: 3 coincidencias: la línea 93 (otra sección del documento) y las líneas 127 y 128 (sección 10, con TurboScribe y ChatGPT).

### Commits
- `1ca7a13` — `docs(B2): corregir declaracion de uso de ia sobre transcripcion`
- `6ab6818` — `docs(B2): declarar responsable y verificador de la transcripción según el responsable`
### Limitaciones
La responsabilidad de Arboleda Yanza Francisco Javier sobre la transcripción y la verificación por Rizzo Vélez Edson Nagib se declaran según el propio responsable; no existe registro escrito del cotejo ni de qué entrevistas abarcó. La transcripción final reorganiza el texto, por lo que no es literal: la retranscripción literal de ENTR-01 a 08 con marcas de tiempo corresponde a la tarea B1, pendiente.

### Evidencia entregada fuera del repositorio
No aplica.
---

## B3 — Tabla maestra de participantes

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** ninguna

### Problema detectado
ENTR-02, 04, 09, 12, 13 y 15 tenían perfiles distintos según la fuente: consentimiento, transcripción, `curva_saturacion.py` (líneas 71-82) y actas de member checking no coincidían entre sí.

### Acción aplicada
Se construyó `07_Datos/datos_procesados/tabla_maestra_participantes.csv`, con un solo perfil por persona, y se alinearon con ella `curva_saturacion.py` y `tabla_saturacion.csv`.

Se escribió `07_Datos/scripts/plan_mejora/verificar_B3_perfiles.py`, que contrasta el perfil de cada participante contra **todas** las fuentes del repositorio: el script de saturación, la tabla de saturación, el apéndice del ERS, la adenda de segunda ronda, las actas de member checking y el consentimiento manuscrito.

Las discrepancias con anexos ya firmados no se corrigen sobre el anexo: se declaran en `09_Etica/Adenda_Perfiles_Participantes.md`, conforme a la regla de `09_Etica/README_Etica.md`. La A.14 no se altera.

### Hallazgos propios del equipo
- Los perfiles **previstos** en A.14 difieren de los reales en ENTR-09, 10, 11, 13, 14 y 16. Se declara en la adenda; el anexo firmado queda intacto.
- La etiqueta del archivo de consentimiento de ENTR-02 dice "Administrador" y no coincide con el perfil real. Es una etiqueta informal de nombre de archivo, y así consta.

### Evidencia utilizada
- `02_Evidencias/Consentimientos/`, `02_Evidencias/Transcripciones/`, `01_ERS/apendices.tex`
- Actas de member checking y adenda de segunda ronda
- Fecha: 21/09/2026

### Archivos modificados
- `07_Datos/datos_procesados/tabla_maestra_participantes.csv`
- `07_Datos/scripts/plan_mejora/verificar_B3_perfiles.py`
- `07_Datos/scripts/curva_saturacion.py` · `07_Datos/resultados/tabla_saturacion.csv`
- `09_Etica/Adenda_Perfiles_Participantes.md`

### Criterio de aceptación
- [x] Un solo perfil por persona, coincidente en todas las fuentes

### Verificación
Comando:

    python3 07_Datos/scripts/plan_mejora/verificar_B3_perfiles.py

Resultado (salida guardada en `07_Datos/resultados/b3_verificacion_perfiles.txt`):

    RESULTADO: CUMPLE, el perfil coincide en todas las fuentes.

### Commits
- `acc24df`, `2a05e54`, `619dec8`, `f156e84`

### Limitaciones
La adenda declara la discrepancia con los perfiles previstos de A.14 pero no la resuelve: A.14 es un anexo firmado y no se modifica. La firma de la adenda consta en su sección 6.

Asistencia de IA declarada en `10_Autoria/declaracion_uso_ia.md`, sección 12.

### Evidencia entregada fuera del repositorio
No aplica.

---
## B4 — Matriz de cobertura pregunta por entrevista

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,30 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** B1

### Problema detectado
La guía `A02_Instrumentos_Recoleccion.pdf` se creó el 30/07, después de las rondas 1 y 2; las preguntas 3 y 7 no se formularon; la IA solo se preguntó en 4 de 16 entrevistas; en ENTR-01 (línea 65) el entrevistador propone el análisis de imagen.

### Acción aplicada
Se construyó la matriz de 13 preguntas por 16 entrevistas, 208 celdas, con **cita literal en cada celda cubierta**, mediante `07_Datos/scripts/plan_mejora/matriz_cobertura_B4.py`. Cada celda recibe uno de cuatro estados: PREGUNTADA, ESPONTANEA, PARCIAL o NO_ABORDADA.

Reparto obtenido: 66 PREGUNTADA, 9 ESPONTANEA, 15 PARCIAL y 118 NO_ABORDADA.

### Hallazgos propios del equipo
- Las preguntas **3** (planificación de fitosanitarios, reingreso y carencia) y **7** (reporte a organismos de control) **no se formularon en ninguna de las 16 entrevistas**; solo hay menciones incidentales.
- La pregunta 12 (utilidad de un apoyo automático por fotografía) se formula de forma directa solo en algunas entrevistas, y en ENTR-01 la introduce el entrevistador: queda marcada como pregunta inducida.
- Las ocho entrevistas de las rondas 1 y 2 no siguieron el banco de 13 preguntas, porque la guía es posterior; usaron preguntas por rol. Las de la ronda 3 usaron una guía corta distinta.

### Evidencia utilizada
- `02_Evidencias/Transcripciones/` (las 16 transcripciones vigentes)
- `02_Evidencias/Instrumentos/A02_Instrumentos_Recoleccion.pdf` — banco de preguntas
- Fecha: 21/09/2026

### Archivos modificados
- `07_Datos/scripts/plan_mejora/matriz_cobertura_B4.py`
- `07_Datos/datos_procesados/matriz_cobertura_B4.csv`
- `07_Datos/resultados/matriz_cobertura_B4.md` y `matriz_cobertura_B4.xlsx`

### Criterio de aceptación
- [x] Matriz 13 x 16 con cita literal por celda cubierta
- [x] Limitaciones declaradas

### Verificación
Comando:

    python3 07_Datos/scripts/plan_mejora/matriz_cobertura_B4.py

Resultado:

    Celdas: 208 · PREGUNTADA 66 · ESPONTANEA 9 · PARCIAL 15 · NO_ABORDADA 118

### Commits
- `f5bc188`, `09a9769`, `a1fbf8f`, `33ebbe8`

### Limitaciones
Las ocho limitaciones de la matriz se declaran íntegras en `07_Datos/resultados/matriz_cobertura_B4.md`. Las principales:

"Cobertura" significa que la persona habló del tema con una cita literal; no mide la calidad ni la profundidad de la respuesta. La asignación de cada celda la hizo un solo analista y **no fue doblemente codificada**: es una decisión revisable, fila a fila, en el CSV. En ENTR-02 se excluyó el tramo posterior a `[16:04]`, que no es fiable hasta compararlo con el audio (hallazgo de B1), de modo que las preguntas que solo se responden ahí no cuentan como cubiertas.

Asistencia de IA declarada en `10_Autoria/declaracion_uso_ia.md`, sección 12.

### Evidencia entregada fuera del repositorio
No aplica.

---
## B5 — Tabla de hora de inicio, fin y duración real de cada entrevista

**Estado operativo:** VERIFICADA (duración real calculada; hora de inicio y fin declarada como no recuperable)
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Macías Herrera Josthyn Esteban (script de duración) · Arboleda Yanza Francisco Javier (corrección de la bitácora)
**Dependencias:** ninguna

### Problema detectado
La bitácora de sesiones declaraba `N/D` en hora de inicio y hora de fin de las cuatro sesiones de campo (SES-27 a SES-30), y no recogía ninguna duración. La guía, el consentimiento y la adenda declaraban duraciones distintas entre sí.

### Acción aplicada
Se calculó la duración real de cada entrevista con `07_Datos/scripts/plan_mejora/duracion_por_entrevista.py`, que lee `duracion_segundos` de cada archivo multimedia en `02_Evidencias/00_Restringido/fichas_tecnicas.csv`. Ninguna cifra se escribe a mano.

Se añadió a `10_Autoria/bitacora_sesiones.csv` la columna `duracion_grabada_min`, con el total de cada sesión de campo y el desglose por entrevista, y se eliminaron los cuatro `N/D`.

### Hallazgo propio del equipo
**La hora de inicio y de fin no es recuperable.** Los contenedores `.7z` publicados en el repositorio de evidencias no conservan la marca de hora de los archivos: las fichas técnicas registran fecha y duración, pero no la hora del día. Los cuatro `N/D` se sustituyen por esa declaración explícita, no por una hora estimada.

El total grabado es de **157,8 minutos sobre 16 entrevistas**, frente a los 240 minutos que exigía originalmente la guía. La salida del script lo declara como NO CUMPLE y así queda.

### Evidencia utilizada
- `02_Evidencias/00_Restringido/fichas_tecnicas.csv` — duración, tamaño y SHA-256 de cada archivo
- Fecha: 21/09/2026

### Archivos modificados
- `10_Autoria/bitacora_sesiones.csv`
- `07_Datos/resultados/b5_duraciones_salida.txt`

### Criterio de aceptación
- [x] Duraciones verificables contra los archivos multimedia
- [x] Bitácora sin `N/D` — sustituidos por la duración real y por la declaración de que la hora no es recuperable

### Verificación
Comando:

    python3 07_Datos/scripts/plan_mejora/duracion_por_entrevista.py 02_Evidencias/00_Restringido/fichas_tecnicas.csv

Resultado:

    2026-05-23  3 entrevistas   52,9 min    2026-08-31  4 entrevistas   32,7 min
    2026-07-28  5 entrevistas   36,2 min    2026-09-01  4 entrevistas   34,6 min
    Total de video: 157.8 minutos (9466 segundos), sobre 16 entrevistas.
    Minimo exigido originalmente por la guia: 240 minutos. NO CUMPLE.

### Limitaciones
La hora de inicio y de fin de cada sesión de campo **no se ha podido reconstruir** y se declara como no recuperable, en lugar de estimarse. La duración sí es verificable, archivo por archivo, contra su SHA-256.

El total grabado queda por debajo del mínimo que pedía la guía. No se corrige ni se justifica aquí: se declara.

### Evidencia entregada fuera del repositorio
Los archivos multimedia están en el repositorio de evidencias audiovisuales, en contenedores cifrados; el manifiesto `checksums_evidencias.sha256` permite comprobar su contenido.

---
## C1 — Cita literal por fragmento y libro de códigos versionado

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,50 pts
**Responsables:** Arboleda (pipeline y libro de códigos) · revisión repartida
entre Arboleda, Macías, Villafuerte y Huilcapi · Macías (aplicación final y
dos correcciones de contenido)
**Dependencias:** ninguna

### Problema detectado

De 227 fragmentos codificados (138 en `codificacion.csv` + 89 en
`codificacion_tercera_ronda.csv`), solo 2 tenían cita literal verificable
con número de línea; el resto contenía paráfrasis del analista, no el texto
real de la transcripción. No había libro de códigos versionado con
definición y criterio de cada código.

### Acción aplicada

Se creó `07_Datos/libro_codigos.md` con definición y criterio de los 82
códigos usados. Arboleda construyó el pipeline de verificación:
`proponer_citas_C1.py` (candidatas por similitud contra las intervenciones
del entrevistado), `aplicar_revision_C1.py` (verifica que la cita elegida
sea subcadena exacta antes de aceptarla; nunca confía en un número de línea
escrito a mano) y `verificar_citas_C1.py` (control final independiente).

Las 227 filas se revisaron a mano entre cuatro personas. Al aplicar la
revisión se corrigieron dos errores de contenido que el verificador
automático no detecta por sí solo (solo comprueba que el texto exista, no
que respalde el código):

- **Fila 2 de `codificacion.csv` (EQUIPOS_TRABAJO):** la cita elegida era
  literal pero hablaba de otro tema. Se corrigió a la candidata que sí
  respalda el código (línea 11 de
  `2026-05-23_ENTR-01_Transcripcion.md`).
- **Fila 128 de `codificacion.csv` (EV-08, CRITERIO_RECEPCION):** la cita
  elegida unía dos turnos separados por una pregunta del entrevistador en
  medio, sin espacio, produciendo una oración que nadie dijo así. Se
  corrigió usando solo el primer turno.

### Verificación

    python3 07_Datos/scripts/plan_mejora/verificar_citas_C1.py

Resultado (`07_Datos/resultados/c1_verificacion_citas.txt`):

    Total de fragmentos: 227
    Citas literales verificadas: 180 (79.3 % del total)
    NO_LOCALIZADA (declaradas, no cuentan como verificadas): 47
    Pendientes de revisión: 0
    Citas rechazadas (no literales): 0
    Códigos distintos en los CSV: 82
    Códigos con definición y criterio en el libro: 82
    RESULTADO: CUMPLE el criterio de C1.

### Evidencia utilizada

| Archivo | Contenido |
|---|---|
| `07_Datos/libro_codigos.md` | 82 códigos con definición y criterio |
| `07_Datos/datos_crudos/codificacion.csv` | 138 fragmentos, ronda 1-2 |
| `07_Datos/datos_procesados/codificacion_tercera_ronda.csv` | 89 fragmentos, ronda 3 |
| `07_Datos/resultados/c1_verificacion_citas.txt` | Salida oficial del verificador |

### Limitaciones

47 de 227 fragmentos (20,7 %) quedan como `NO_LOCALIZADA`: el parafraseo
original no tiene respaldo textual exacto en la transcripción indicada. El
libro de códigos y el script de verificación reconocen ese estado como
cierre válido — no se inventa texto para forzar un 100 % de citas
literales.

### Commits

- `12577f3`, `f91846f` — libro de códigos y CSV base
- `c374015`, `ce678f1` — pipeline de propuesta y verificación (Arboleda)
- `380b2da` — aplicación de la revisión y correcciones de contenido

---

## C2 — Reasignar fragmentos cruzados entre ENTR-05 y ENTR-06

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** C1

### Problema detectado
Fragmentos codificados como procedentes de ENTR-05 aparecían respaldados por el texto de ENTR-06 y viceversa: las dos transcripciones estaban intercambiadas en su origen.

### Acción aplicada
Se escribió `07_Datos/scripts/plan_mejora/resolver_C2.py`, que para cada uno de los 213 fragmentos vigentes compara el respaldo literal de su entrevista declarada con el de todas las demás, y señala aquellos en los que otra entrevista respalda mejor el texto (margen 0,15, mínimo 0,45).

Las señales no se aplicaron de forma automática: **las cinco que el script levantó se revisaron una a una** y se anotó el motivo de mantenerlas o cambiarlas en `07_Datos/resultados/c2_reasignaciones.csv`.

Los 14 fragmentos que no tienen respaldo literal en ninguna transcripción se retiraron de la codificación y quedan registrados con su motivo en `07_Datos/datos_procesados/fragmentos_retirados_C2.csv`. No se completó ninguno con una cita aproximada.

### Evidencia utilizada
- `02_Evidencias/Transcripciones/` (versiones vigentes tras B1)
- `07_Datos/datos_crudos/codificacion.csv` y `07_Datos/datos_procesados/codificacion_tercera_ronda.csv`
- Fecha: 21/09/2026

### Archivos modificados
- `07_Datos/scripts/plan_mejora/resolver_C2.py` y `verificar_C2_cruces.py`
- `07_Datos/resultados/c2_reasignaciones.csv` y `c2_verificacion_cruces.txt`
- `07_Datos/datos_procesados/fragmentos_retirados_C2.csv`

### Criterio de aceptación
- [x] Ningún fragmento tiene mejor respaldo literal en una entrevista distinta de la declarada

### Verificación
Comando:

    python3 07_Datos/scripts/plan_mejora/verificar_C2_cruces.py

Resultado:

    C2 · fragmentos revisados: 213 · señales sin revisar: 0 · señales revisadas y mantenidas: 5
    RESULTADO: CUMPLE (ningún fragmento tiene mejor respaldo en otra entrevista).

### Commits
- `dce160e`, `3130062`

### Limitaciones
Una de las cinco señales revisadas (fila 91 de `codificacion.csv`) indica que el **código** `EVIDENCIA_FOTOGRAFICA` encaja mejor con ENTR-07 aunque el texto sí es de ENTR-05. Se deja constancia de que lo revisable ahí es el código, no la entrevista, y no se modifica.

El umbral de similitud (0,45 con margen 0,15) es una decisión del equipo; con otro umbral el número de señales cambiaría. El criterio no es el umbral sino que ninguna señal quede sin revisar por una persona.

Asistencia de IA declarada en `10_Autoria/declaracion_uso_ia.md`, sección 12.

### Evidencia entregada fuera del repositorio
No aplica.

---
## C3 — Doble codificación real

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,50 pts
**Responsable(s):** Macías Herrera Josthyn Esteban y Arboleda Yanza Francisco Javier — cada uno desde su propia cuenta
**Dependencias:** C1 commiteada (cumplida)

### Problema detectado
Los archivos `10_Autoria/doble_codificacion/codificacion_allan.csv` y `codificacion_josthyn.csv` eran **idénticos byte a byte**. Dos archivos iguales no son una doble codificación independiente, y el acuerdo calculado sobre ellos no significa nada.

### Acción aplicada
Se preparó una doble codificación nueva en `10_Autoria/doble_codificacion_C3/`, sobre una muestra congelada y con reglas escritas antes de empezar:

- **Muestra:** 45 fragmentos de los 213 vigentes (21,1 %), elegidos al azar sin reemplazo con semilla `20260921` mediante `preparar_muestra_C3.py`, que es determinista y auditable. El archivo `muestra_C3_fragmentos.csv` contiene el fragmento y su cita literal, **sin ningún código**.
- **Instrumento:** `hoja_codificacion_C3.xlsx`, con lista desplegable de los códigos del libro.
- **Libro de códigos:** `07_Datos/libro_codigos.md` v1.0 (20/09/2026), publicado **antes** que las hojas.
- **Reglas:** cada persona codifica sola, no abre `codificacion.csv` ni el archivo de otra persona antes de subir el suyo, sube su archivo desde su propia cuenta de GitHub, y nadie vuelve a ejecutar `preparar_muestra_C3.py` una vez empezada la codificación.
- **Cálculo:** `calcular_acuerdo_C3.py` compara cada par de codificadores y cada uno contra la codificación original, con acuerdo observado, kappa de Cohen e IC 95 % por bootstrap (2000 remuestreos, semilla fija). Comprueba además que cada archivo procede de una cuenta de git distinta.

La carpeta anterior se conserva como historial; el acuerdo vigente será el de esta.

### Evidencia utilizada
- `07_Datos/datos_crudos/codificacion.csv` y `codificacion_tercera_ronda.csv` — universo de 213 fragmentos
- `07_Datos/libro_codigos.md` v1.0
- Fecha: 21/09/2026

### Archivos modificados
- `10_Autoria/doble_codificacion_C3/` — README, muestra, hoja, y los dos scripts

### Criterio de aceptación
- [x] Muestra congelada, aleatoria y reproducible, sin códigos a la vista
- [x] Libro de códigos publicado antes que las hojas de codificación
- [x] Un archivo de codificación por persona, publicado desde su propia cuenta
- [x] Acuerdo observado y kappa con intervalo de confianza calculados por script

### Verificación
Comando (una vez subidos los dos archivos):

    python3 10_Autoria/doble_codificacion_C3/calcular_acuerdo_C3.py

Resultado (`10_Autoria/doble_codificacion_C3/desacuerdos_C3.csv` para el detalle):

    Arboleda vs Macías   : acuerdo observado 66.7 %  ·  kappa 0.655 (IC 95 % 0.506–0.789)
    Arboleda vs ORIGINAL : acuerdo observado 57.8 %  ·  kappa 0.566 (IC 95 % 0.409–0.698)
    Macías vs ORIGINAL   : acuerdo observado 53.3 %  ·  kappa 0.521 (IC 95 % 0.375–0.653)
    Desacuerdos registrados: 55
    Reglas de C3 (identidad de archivo/autor git): sin problemas detectados.

El kappa entre codificadores (0,655) corresponde a acuerdo sustancial según
los umbrales convencionales del área, con un intervalo de confianza amplio
por el tamaño de la muestra frente al número de códigos posibles.

### Commits
- `b35091d` — preparación de muestra e instrumento
- `8ca5ed7` — codificación de Macías (autor `jmaciasherr4`)
- `f7f6a8e` — codificación de Arboleda (autor `farboleday-wq`)
- `39fb436` — resultado del cálculo de acuerdo y desacuerdos

### Limitaciones
Con 95 códigos posibles y 45 fragmentos el kappa es inestable; por eso se reporta con su intervalo de confianza y no como cifra aislada.

El código original de cada fragmento lo asignó el equipo (`Analista_codificador` = VER/AVR) y después se ajustaron las citas con asistencia de IA, sin modificar ningún código. Los scripts y la hoja se prepararon con asistencia de IA; **los códigos de esta doble codificación los asigna cada persona**, no una IA. Declarado en `10_Autoria/declaracion_uso_ia.md`.

Si al cierre del plazo no están los dos archivos, la tarea queda como está: con la muestra y el instrumento congelados y sin acuerdo calculado. No se sustituye por una codificación hecha por una sola persona.

### Evidencia entregada fuera del repositorio
No aplica.

---
## C4 — Saturación con sensibilidad al orden

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** C1, C2

### Problema detectado
La saturación se presentaba como un hallazgo firme por el hecho de que la última entrevista no aportara códigos nuevos, sin comprobar si eso dependía del orden en que se hicieron las entrevistas.

### Acción aplicada
Se escribió `07_Datos/scripts/plan_mejora/saturacion_orden_C4.py`, que calcula los códigos nuevos por entrevista en el orden real y después repite el cálculo sobre **10 000 órdenes aleatorios** (semilla `20260921`), para estimar con qué frecuencia la última posición no aporta códigos nuevos por puro azar.

### Hallazgo propio del equipo
En el orden real, ENTR-16 aporta 0 códigos nuevos. Pero en órdenes al azar eso ocurre el **43,9 %** de las veces, y que las **dos** últimas no aporten nada ocurre el 16,7 %. Es decir: **el dato no distingue la saturación del azar**, y presentarlo como evidencia de saturación no se sostiene. Queda escrito así en la salida del script.

### Evidencia utilizada
- `07_Datos/datos_crudos/codificacion.csv` y `07_Datos/datos_procesados/codificacion_tercera_ronda.csv`
- Fecha: 21/09/2026

### Archivos modificados
- `07_Datos/scripts/plan_mejora/saturacion_orden_C4.py`
- `07_Datos/resultados/c4_saturacion_orden.csv` y `c4_saturacion_orden.txt`

### Criterio de aceptación
- [x] Saturación recalculada con sensibilidad al orden y resultado declarado

### Verificación
Comando:

    python3 07_Datos/scripts/plan_mejora/saturacion_orden_C4.py

Resultado:

    Entrevistas: 16 · códigos distintos: 82 · órdenes aleatorios: 10000 · semilla: 20260921
    Orden real: códigos nuevos por entrevista = [23, 8, 6, 18, 5, 1, 4, 2, 5, 5, 1, 1, 0, 1, 2, 0]
    Media de códigos nuevos en la ÚLTIMA posición (órdenes al azar): 2.20
    Probabilidad de CERO códigos nuevos en la última posición: 43.9%
    Probabilidad de cero códigos nuevos en las DOS últimas posiciones: 16.7%

### Commits
- `3130062`

### Limitaciones
El cálculo se hace sobre los 213 fragmentos vigentes tras C1 y C2; con el conjunto anterior, que contenía citas no verificadas, el resultado sería distinto y no comparable.

La conclusión es negativa y así se deja: **no se afirma saturación**. Cualquier texto del proyecto que la afirme debe corregirse o declararse como no sustentado.

Asistencia de IA declarada en `10_Autoria/declaracion_uso_ia.md`, sección 12.

### Evidencia entregada fuera del repositorio
No aplica.

---
## C5 — Identificar al analista VER y documentar la revisión cruzada

**Estado operativo:** VERIFICADA (limitación declarada: identidad de VER no determinable; revisión cruzada no realizada)
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,10 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** Ninguna

### Problema detectado
El plan del docente señala que la ronda 3 fue codificada por un solo analista (commit `cbcdab5`) y pide identificar al analista "VER".

### Acción aplicada
Se revisó el commit `cbcdab5` (autor `AlanNVR`) y el README que introduce, `07_Datos/datos_procesados/README_codificacion_tercera_ronda.md`. Ese README declara como responsable principal a Villafuerte Rosero Allan Noé, con identificador `AVR` en las 89 filas de `codificacion_tercera_ronda.csv` (ENTR-09 a ENTR-16), y estado "codificación realizada; pendiente revisión cruzada del integrante de apoyo".

"VER" es el identificador del analista del archivo histórico `07_Datos/datos_crudos/codificacion.csv` (138 fragmentos, EV-01 a EV-08, rondas 1 y 2): figura en la columna `Analista_codificador` de las 138 filas y en `07_Datos/datos_crudos/readme.md` (línea 38). Ningún documento del repositorio indica a qué integrante corresponde. El archivo se subió por primera vez en el commit `df619cb` (cuenta `AlanNVR`, 02/08/2026 22:18, "Add files via upload"), ya con `VER` en las 138 filas; el commit `1236a21` (03/09) solo lo movió a `07_Datos/datos_crudos/`. El 20/09/2026 se consultó por mensaje al líder del equipo (Villafuerte Rosero Allan Noé), quien no supo indicar a quién corresponde. Quién subió un archivo no equivale a quién lo codificó, por lo que la identidad de VER se declara no determinable con la evidencia disponible y no se asigna por suposición.

Nota: en `07_Datos/libro_codigos.md` (commit `12577f3`) `VER` también es un código de estado de la cita (cita literal verificada en intervención del entrevistado); es un uso distinto del identificador de analista.

La revisión cruzada de la ronda 3 no se realizó. El README de `cbcdab5` ya la declaraba pendiente.

### Evidencia utilizada
- `07_Datos/datos_crudos/codificacion.csv`, columna `Analista_codificador`: `VER` en 138 filas
- `07_Datos/datos_crudos/readme.md`, línea 38
- Commit `df619cb`: primera subida del archivo
- `07_Datos/datos_procesados/codificacion_tercera_ronda.csv`: `AVR` en 89 filas
- `07_Datos/datos_procesados/README_codificacion_tercera_ronda.md`
- `07_Datos/libro_codigos.md`, línea 25 (uso de `VER` como código de estado)

### Archivos modificados
- `07_Datos/registro_correcciones.md` (esta entrada)

### Criterio de aceptación
- [x] Analista VER: identificador localizado (138 filas de `codificacion.csv`); persona no determinable con la evidencia disponible, declarado
- [x] Revisión cruzada de la ronda 3: no realizada; limitación declarada

### Verificación
Comandos:

    python3 -c "import csv; r=list(csv.DictReader(open('07_Datos/datos_crudos/codificacion.csv',encoding='utf-8-sig'),delimiter=';')); print(sum(x['Analista_codificador']=='VER' for x in r))"
    python3 -c "import csv; r=list(csv.DictReader(open('07_Datos/datos_procesados/codificacion_tercera_ronda.csv',encoding='utf-8-sig'),delimiter=';')); print(sum(x['Analista_codificador']=='AVR' for x in r))"

Resultado:

    138
    89

### Commits
- `0836c50` y `3af8698` — versión inicial de esta entrada, que afirmaba por error que no existía un analista VER
- `c31bc1d` — corrección: VER existe en codificacion.csv y la ronda 3 tiene 89 filas

### Limitaciones
No existe artefacto de revisión cruzada de la ronda 3, y la identidad de VER no se pudo determinar. Qué haría falta: que el "integrante de apoyo" que menciona el README revise una muestra de la codificación de `AVR` y registre acuerdo o desacuerdo, y que alguien del equipo aporte evidencia de quién codificó las rondas 1 y 2. Mientras tanto, se mantiene la limitación declarada.

### Evidencia entregada fuera del repositorio
Consulta por mensaje al líder del equipo (20/09/2026): no supo indicar a quién corresponde VER.
---

## D1 — Tabla de procedencia por requisito

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,40 pts
**Responsable(s):** Macías Herrera Josthyn Esteban (primera versión del script) · NOMBRE (paquete con el catálogo de 79 requisitos) · Arboleda Yanza Francisco Javier (versión final, revisión y firma)
**Dependencias:** ninguna

### Problema detectado
El ERS no declaraba la procedencia de cada requisito. RF-03, 07, 08 y 18 ya figuraban en la propuesta del 05/05/2026, antes de la primera entrevista (23/05); RF-36 y EV-13 aparecen el 02/08 con evidencia del 03 al 07/08; RF-40 a 42 y los requisitos de IA aparecen el 31/08 sin entrevista.

### Acción aplicada
La primera versión del script cubría solo los 42 RF y daba las citas por verificadas. Se rehízo para los 79 requisitos (42 RF, 6 RF-IA, 19 RNF y 12 RNF-IA) con seis correcciones documentadas en la cabecera del script: origen sin truncar, RL-XX como normativo, los 6 RF-IA que faltaban, origen de los de IA desde la tabla de trazabilidad, commit de alta desde el historial completo del ERS (53 requisitos el 02/08 en `35fff3c`, RF-36 a RF-39 el 02/08 en `54bd614` y 22 el 31/08 en `14b9e6b`) y una tabla verificada de correspondencia con la propuesta del 05/05.

Clasificación firmada: 45 elicitado, 7 propuesta_equipo, 4 normativo y 23 derivado.

Anteriores a su evidencia, declarados: RF-03, 07, 08 y 18 (ya en la propuesta del 05/05) y RF-36, 38 y 39 (alta el 02/08, EV-13 del 03 al 07/08). RF-37 es parcial: EV-11 es anterior y EV-13 posterior.

### Hallazgos propios
- 24 requisitos citan una evidencia que la tabla del apéndice del ERS no les asigna, y en 7 casos el apéndice lista un requisito que no cita esa evidencia: incoherencia interna del ERS, declarada y no corregida.
- RNF-07, 10, 13, 15 y 17 declaran "Derivado" sin decir de qué; su origen no está identificado.
- RF-32 y RF-40 fueron falsos positivos del emparejamiento automático con la propuesta.

### Evidencia utilizada
- `01_ERS/` (versiones .tex, `apendices.tex`) y su historial de git
- `01_ERS/antecedentes/2026-05-05_Propuesta_Inicial_1A.pdf`

### Archivos modificados
- `07_Datos/scripts/plan_mejora/tabla_procedencia_D1.py`
- `07_Datos/datos_procesados/tabla_procedencia_requisitos.csv`

### Criterio de aceptación
- [x] 100 % de RF, RNF y requisitos de IA clasificados (79 de 79)
- [x] Fecha de la fuente y commit de alta por requisito
- [x] Ningún requisito anterior a su evidencia sin declararlo (7)

### Verificación
Comando:

    python3 07_Datos/scripts/plan_mejora/tabla_procedencia_D1.py

Resultado:

    Requisitos: 79 -> {'RF': 42, 'RF-IA': 6, 'RNF': 19, 'RNF-IA': 12}
    En la propuesta del 05/05: 4
    Verificadas por persona: 79 de 79
    Con alerta: 33

### Commits
- `f918b01`, `ce988a5`, `eeeec71`, `a34288d`

### Limitaciones
La clasificación se propuso con reglas del script y un análisis asistido por IA que comprobó las evidencias citadas, sus fechas, el historial de git y el apéndice. Arboleda revisó las notas de cada fila y firmó su conformidad en las 79; no leyó a mano cada requisito en el ERS.

### Evidencia entregada fuera del repositorio
No aplica.

---

## D2 — Corregir la cita atribuida a EV-01 y verificar las citas del ERS

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** C1

### Problema detectado
El ERS atribuía a EV-01 una cita que en la transcripción corresponde a palabras del **entrevistador**, no del entrevistado. No existía ninguna comprobación de las citas textuales del ERS contra sus transcripciones.

### Acción aplicada
Se corrigieron las citas textuales del ERS y del manuscrito para que cada una sea literal, de la entrevista que se le atribuye y dicha por la persona entrevistada. Se alineó además la procedencia declarada de RNF-16.

Se escribió `07_Datos/scripts/plan_mejora/verificar_D2_citas_ers.py`, que localiza las citas con atribución en el ERS y el manuscrito y comprueba las tres condiciones en la transcripción correspondiente. La comprobación queda incorporada al repositorio y puede repetirse.

### Evidencia utilizada
- `01_ERS/ERS_SRS_2B_v2.0.tex` y `08_Publicacion/manuscrito_final.tex`
- `02_Evidencias/Transcripciones/` (versiones vigentes tras B1)
- Fecha: 21/09/2026

### Archivos modificados
- `01_ERS/ERS_SRS_2B_v2.0.tex` y `01_ERS/apendices.tex`
- `07_Datos/scripts/plan_mejora/verificar_D2_citas_ers.py`
- `07_Datos/resultados/d2_verificacion_citas_ers.txt`

### Criterio de aceptación
- [x] El 100 % de las citas textuales con atribución es literal, de la entrevista correcta y del entrevistado

### Verificación
Comando:

    python3 07_Datos/scripts/plan_mejora/verificar_D2_citas_ers.py

Resultado:

    D2 · citas textuales del ERS y del manuscrito con atribución: 5 · correctas: 5 · a corregir: 0
    RESULTADO: CUMPLE, el 100 % de las citas es literal, de la entrevista correcta y del entrevistado.

### Commits
- `024253e`, `a466481`, `eed6281`, `6e0388f`

### Limitaciones
El verificador localiza las citas que llevan atribución explícita a una entrevista. Una cita sin atribución no se detecta; el ERS no contiene ninguna de ese tipo a la fecha, pero la comprobación no lo garantiza para versiones futuras.

Asistencia de IA declarada en `10_Autoria/declaracion_uso_ia.md`.

### Evidencia entregada fuera del repositorio
No aplica.

---
## D3 — Umbrales y duplicados en los requisitos de IA

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** ninguna

### Problema detectado
Dos pares de requisitos vigentes fijaban la misma métrica con umbral o método distinto: RNF-01 con RNF-IA-08 (exactitud de clasificación de madurez) y RNF-02 con RNF-IA-01 (detección de plagas). Un catálogo con dos umbrales vigentes para la misma métrica no es verificable: no se sabe cuál rige.

### Acción aplicada
Se resolvió la duplicidad **sin borrar los requisitos de origen**. RNF-01 y RNF-02 declaran ahora de forma expresa, en su propio texto del ERS, que su umbral genérico **queda precisado y sustituido** por RNF-IA-08 y RNF-IA-01 respectivamente, que fijan la métrica y el procedimiento de medición definitivos, y que se conservan como requisito de origen.

En el caso de RNF-02 se deja constancia del motivo del cambio de métrica: RNF-IA-01 emplea macro-F1 en lugar de exactitud porque las clases están desbalanceadas y la exactitud premiaría a un modelo que acertara siempre la clase mayoritaria.

El ERS se recompiló para que el PDF y la fuente coincidan.

### Evidencia utilizada
- `01_ERS/ERS_SRS_2B_v2.0.tex`, tabla de RNF y sección 9 (requisitos de IA)
- Fecha: 21/09/2026

### Archivos modificados
- `01_ERS/ERS_SRS_2B_v2.0.tex` y `01_ERS/ERS_SRS_2B_v2.0.pdf`

### Criterio de aceptación
- [x] Ningún par de requisitos vigentes fija la misma métrica con distinto umbral

### Verificación
Comando:

    grep -n "queda precisado y sustituido" 01_ERS/ERS_SRS_2B_v2.0.tex

Resultado: dos coincidencias, en las filas de RNF-01 y RNF-02 de la tabla de requisitos no funcionales.

### Commits
- `611f33a`, `dc2ca0f`

### Limitaciones
El umbral vigente de ambos pares sigue siendo **no verificable** hasta que exista el conjunto de evaluación etiquetado, cuya ausencia está declarada como limitación `L-05` en el propio ERS. Esta tarea resuelve cuál es el umbral que rige, no la posibilidad de comprobarlo.

### Evidencia entregada fuera del repositorio
No aplica.

---
## D4 — Casos de prueba definidos y ejecutados

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,30 pts
**Responsable(s):** Arboleda Yanza Francisco Javier (ejecución sobre el prototipo desplegado)
**Dependencias:** E1 (cumplida)

### Problema detectado
Los 68 casos de prueba de la matriz eran solo identificadores: en 40 filas repetían el número del RF y en 25 el de la fila. No había pasos, ni dato de entrada, ni resultado esperado, ni ejecución registrada.

### Acción aplicada
Se definieron y **se ejecutaron** los casos de prueba de los RF con prioridad
Must sobre el prototipo desplegado en `https://simpa-v3-prototipo.netlify.app/`,
entrando como Administrador en una sola ventana de incógnito. El resultado de
cada uno queda en `04_Trazabilidad/D4_casos_prueba_RF_Must.md`, con el
resultado **observado**, no el esperado.

Cinco RF Must no se repiten aquí porque ya se ejecutaron y registraron en E1:
RF-01, RF-22, RF-40, RF-41 y RF-42. Quedaban **19 por probar**, y se probaron
los 19.

### Resultado
| | RF | Cuáles |
|---|---:|---|
| Cumplen | 16 | RF-02, 03, 04, 07, 08, 12, 13, 14, 18, 19, 21, 26, 28, 35, 36, 37 |
| Parcial | 1 | RF-10 — permite elegir entre variedades predefinidas pero no escribir texto libre |
| **No cumplen** | **2** | **RF-05** y **RF-30** |

### Hallazgos propios del equipo
- **RF-05** (registro de monitoreo fitosanitario) **no está implementado**: no
  existe pantalla ni botón separado; lo que hay es el mismo análisis de imagen
  de RF-07 y RF-08. Coincide con lo que ya señalaba E2, donde RF-05 era el
  único RF Must sin rótulo propio en ninguna pantalla.
- **RF-30** (reporte de incidencia desde campo con evidencia fotográfica)
  **tampoco**: no existe la opción en el módulo de mapa.

Los dos se declaran como incumplimientos. No se reformula el requisito ni se
ajusta el criterio para que dé por bueno lo que hay.

### Evidencia utilizada
- `07_Datos/datos_procesados/cobertura_rf_must_E2.csv` — lista de RF Must y su cobertura declarada
- `05_MVP/evidencia_e2e/registro_prueba_e2e.md` — los cinco ya ejecutados en E1
- Prototipo desplegado, ejecución del 21/09/2026
- Fecha: 21/09/2026

### Archivos modificados
- `04_Trazabilidad/D4_casos_prueba_RF_Must.md`
- `04_Trazabilidad/matriz_e2e.xlsx` — hoja `Ejecucion_D4`

### Criterio de aceptación
- [x] Cada CP Must especificado y con resultado Pasa/Falla y evidencia observada

### Verificación
Comando:

    grep -c "^### RF-" 04_Trazabilidad/D4_casos_prueba_RF_Must.md
    grep -o "¿Cumple?\*\* [A-Za-zí]*" 04_Trazabilidad/D4_casos_prueba_RF_Must.md | sort | uniq -c

Resultado: 19 RF evaluados · 16 Sí · 1 Parcial · 2 No.

### Limitaciones
Los pasos y el «resultado esperado» de cada caso se redactaron leyendo el
código del prototipo, no probándolo: **lo único que cuenta es el resultado
observado al ejecutarlo**, y así está declarado en el propio documento. RF-05
se corrigió el mismo 21/09/2026 al volver a mirar la aplicación y confirmar
que no existe una pantalla separada de monitoreo fitosanitario.

La ejecución la hizo una sola persona, en una sola sesión y con un solo rol
(Administrador). No se probó el comportamiento de cada RF bajo los demás
roles, salvo lo ya cubierto por E1.

La preparación del documento contó con asistencia de IA, declarada en su
encabezado y en `10_Autoria/declaracion_uso_ia.md`; la ejecución y el
resultado observado son de la persona que firma.

### Evidencia entregada fuera del repositorio
No aplica.

---
## D5 — Corregir matriz_e2e.xlsx

**Estado operativo:** VERIFICADA (granularidad declarada en el propio Alcance; el título ya decía v2.0 en el momento de esta nota, verificado de nuevo el 21/09/2026 a las 23:46)
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** D4 (cumplida)

### Problema detectado
`matriz_e2e.xlsx` cubría 68 de 89 identificadores (76 %), tenía duplicados de RF-04, RF-07, RF-08, RF-12 y RF-21, 36 filas sin historia, las hojas `Diagnostico` y `Sincronizacion` sin calcular, restos de LaTeX en las filas 56 a 61 y el título «v1.1».

### Acción aplicada
Se reconstruyó la matriz: **73 filas de trazabilidad**, sin restos de LaTeX,
con las hojas `Diagnostico` y `Sincronizacion` calculadas y con sus valores
guardados, y con una hoja nueva `Ejecucion_D4` que recoge la ejecución de los
casos de prueba.

El diagnóstico que arroja la propia hoja: 73 filas, 73 trazas completas, 0
parciales, 0 huérfanas.

### Lo que sigue sin estar resuelto, y se declara
**1. Los cinco «duplicados» no son duplicados, pero tampoco están explicados.**
RF-04, RF-07, RF-08, RF-12 y RF-21 aparecen en dos filas cada uno. Al
compararlas, las dos filas de cada par son idénticas **salvo en la columna
Evidencia** (y en RF-12, también en Interesado): son el mismo requisito
trazado desde dos fuentes de evidencia distintas.

Es decir, la matriz tiene una fila por par requisito-evidencia, no una por
requisito. Eso es legítimo, pero **no está declarado en ninguna parte**, y por
eso 73 filas se leen como 73 requisitos cuando en realidad son 68.
Esto ya se corrigió: la celda A4 de `Matriz_E2E` ahora dice, además del alcance original, "GRANULARIDAD: la matriz tiene 73 filas para 68 requisitos únicos, porque 5 requisitos (RF-04, RF-07, RF-08, RF-12 y RF-21) se trazan dos veces, una por cada evidencia de origen distinta que los sustenta; no son filas duplicadas por error, son el mismo requisito visto desde dos fuentes."

Esto ya se corrigió: la celda A4 de `Matriz_E2E` ahora dice, además del alcance original, "GRANULARIDAD: la matriz tiene 73 filas para 68 requisitos únicos, porque 5 requisitos (RF-04, RF-07, RF-08, RF-12 y RF-21) se trazan dos veces, una por cada evidencia de origen distinta que los sustenta; no son filas duplicadas por error, son el mismo requisito visto desde dos fuentes."


**2. La cobertura real es de 66 de los 79 requisitos del ERS (83,5 %).**
Faltan trece, todos RNF: RNF-02, 03, 04, 06, 07, 09, 10, 12, 13, 15, 17, 18 y
19. **No se añaden filas para ellos**: completar su cadena de trazabilidad
—caso de uso, historia, clase, proceso, prototipo y criterio BDD— exigiría
decidir esos valores, y decidirlos a esta altura sería escribirlos, no
trazarlos.

**3. Corregido.** 
El título ya dice «ERS SIMPA v2.0» (commit `cb5f137`, 21/09/2026 23:45). Esta nota se escribió sobre una copia local un minuto antes de que ese commit se reflejara.

**4. Aparecen RD-07 y RD-10**, que son restricciones de diseño y no requisitos
del ERS. No es un error, pero conviene distinguirlo de los 79.

### Evidencia utilizada
- `04_Trazabilidad/matriz_e2e.xlsx`, hojas `Matriz_E2E`, `Diagnostico`, `Sincronizacion` y `Ejecucion_D4`
- `01_ERS/ERS_SRS_2B_v2.0.tex` — catálogo de los 79 requisitos
- Fecha: 21/09/2026

### Archivos modificados
- `04_Trazabilidad/matriz_e2e.xlsx`

### Criterio de aceptación
- [x] La hoja abre sin fórmulas vacías y coincide con la matriz. La cobertura de 60 de 60 (RF + requisitos de IA) es una decisión de alcance ya declarada desde PE5, no un vacío nuevo; los 13 RNF fuera de esta matriz se verifican por otra vía, como el propio Alcance explica. La granularidad (73 filas / 68 requisitos únicos) ya está declarada en la celda A4.

### Verificación
Comando:

    python3 -c "import openpyxl,collections;wb=openpyxl.load_workbook('04_Trazabilidad/matriz_e2e.xlsx',data_only=True);ws=wb['Matriz_E2E'];ids=[str(r[3]).strip() for r in ws.iter_rows(min_row=9,max_row=81,values_only=True) if r[3]];print(len(ids),'filas',len(set(ids)),'requisitos');print({k:v for k,v in collections.Counter(ids).items() if v>1})"

Resultado:

    73 filas 68 requisitos
    {'RF-04': 2, 'RF-07': 2, 'RF-08': 2, 'RF-12': 2, 'RF-21': 2}

### Limitaciones
Trece RNF del ERS no están trazados en la matriz y **no se completan de
memoria**: se declaran por su identificador para que la ausencia sea
verificable.



### Evidencia entregada fuera del repositorio
No aplica.

---
## E2 — Recalcular la cobertura de RF Must

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** E1 (cumplida)

### Problema detectado
El repositorio declaraba una cobertura de **20 de 24 RF Must** sin que esa
cifra saliera de ningún cálculo reproducible, y el código no la sostenía.

### Acción aplicada
Se escribió `07_Datos/scripts/plan_mejora/cobertura_rf_must_E2.py`, que
deriva la cifra de dos fuentes del propio repositorio: la lista de RF con
prioridad Must del ERS —leída de la macro `\RF`, no escrita a mano— y el
código del prototipo declarado en el submódulo.

El punto de fondo es qué cuenta como cobertura. El prototipo rotula cada
pantalla con los requisitos que dice cubrir:

    shell('Plantaciones y lotes', 'RF-02 · RF-06 · RF-10 · estructura productiva', ...)

Ese rótulo es una declaración del equipo escrita dentro del código, **no una
prueba de que el requisito funcione**. Por eso el script no emite un
«cubierto» único, sino cuatro categorías:

| Categoría | Qué sostiene |
|---|---|
| `EJERCITADO_EN_E1` | se ejecutó y su resultado observado quedó registrado |
| `DECLARADO_EN_PANTALLA` | el código lo rotula; nadie comprobó que funcione |
| `SOLO_INDICIO` | coincide el nombre del requisito, nada más |
| `SIN_MENCION` | no aparece en el código |

### Cifra corregida
**23 de los 24 RF Must aparecen declarados** en el rótulo de alguna pantalla.
De ellos, **solo 5 han sido ejercitados** con resultado registrado en la
prueba de extremo a extremo de E1: RF-01, RF-22, RF-40, RF-41 y RF-42.

La cifra anterior, 20 de 24, mezclaba las dos cosas. Ninguna de las dos
cifras nuevas la reproduce, y ambas son verificables ejecutando el script.

### Hallazgo propio del equipo
**RF-05** (registro de monitoreo fitosanitario) es el único RF Must que no
aparece rotulado en ninguna pantalla: solo hay coincidencia de nombre en la
pantalla de análisis. Queda como `SOLO_INDICIO` y pendiente de comprobación.

El submódulo contiene **dos versiones del prototipo** en paralelo
(`Prototipo/` y `prototipo_v2/`), con los mismos rótulos de pantalla. El
script analiza ambas; conviene declarar cuál es la entregada.

### Evidencia utilizada
- `01_ERS/ERS_SRS_2B_v2.0.tex` — prioridad MoSCoW de cada RF
- Submódulo del prototipo, commit `035470cb1dfd7be9557f1c5e2db24473cbcb8c02`
- `05_MVP/evidencia_e2e/registro_prueba_e2e.md` — requisitos ejercitados en E1
- Fecha: 21/09/2026

### Archivos modificados
- `07_Datos/scripts/plan_mejora/cobertura_rf_must_E2.py`
- `07_Datos/datos_procesados/cobertura_rf_must_E2.csv`
- `07_Datos/resultados/cobertura_rf_must_E2.md`

### Criterio de aceptación
- [x] Cifra reproducible a partir de la lista de RF y de la línea de código

### Verificación
Comando:

    git submodule update --init 05_MVP/prototipo
    python3 07_Datos/scripts/plan_mejora/cobertura_rf_must_E2.py

Resultado:

    RF Must en el ERS: 24
    Codigo analizado: 14095 lineas
    Reparto: {'EJERCITADO_EN_E1': 5, 'DECLARADO_EN_PANTALLA': 18, 'SOLO_INDICIO': 1}
    Declarados en pantalla: 23 de 24
    Ejercitados en E1:      5 de 24

### Limitaciones
Que un requisito esté rotulado en una pantalla no significa que esté
implementado: significa que el equipo escribió ese rótulo. La única categoría
que sostiene una afirmación de cobertura funcional es `EJERCITADO_EN_E1`, y
son cinco. Elevar esa cifra exige ejecutar los casos de prueba y registrar el
resultado, que es la tarea D4.

La columna `COBERTURA_VERIFICADA` está pendiente en las 24 filas: se rellena
abriendo la pantalla citada y comprobando el comportamiento.

### Evidencia entregada fuera del repositorio
No aplica.

---
## F1 — Notas de campo: retirar o rotular los 16 PDF y rectificar

**Estado operativo:** VERIFICADA (F1a y F1b hechas; firmada por 5 de 6 integrantes)
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,40 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** Firma de la rectificación por el equipo

### Problema detectado
El 11/09 se declaró por escrito que no existían notas físicas (`b59d4ef`) y el 12/09 se subieron 16 PDF (`1135321`) que comparten el mismo bloque de imagen. `verificacion_seccion15.md` (línea 18) decía "sin fabricación detectada".

### Acción aplicada
F1a: se reescribió `10_Autoria/notas_campo/readme.md`: se rotulan los 16 PDF como material no contemporáneo, de origen por documentar; se restituye la declaración de ausencia del 11/09 y se declara que los PDF se incorporaron el 12/09 (`1135321`). Se corrigió la fila de notas de campo de `verificacion_seccion15.md`, que pasa a "NO VERIFICADO". No se retiran los PDF: se rotulan, y su origen se documenta en F1b.

### Evidencia utilizada
- Commits `b59d4ef` (declaración de ausencia, 11/09), `1135321` (subida de los 16 PDF, 12/09) y `d26f879` (renombrado, 14/09)
- Informe del docente (los 16 PDF comparten el mismo bloque de imagen)

### Archivos modificados
- `10_Autoria/notas_campo/readme.md` (commit `d96fc5c`)
- `10_Autoria/verificacion_seccion15.md` (commit `61ec1f3`)

### Criterio de aceptación
- [x] Ningún PDF presentado como escaneo contemporáneo (en el readme de la carpeta)
- [x] Rectificación firmada por el equipo (F1b: 5 de 6 firmas, cada una desde su propia cuenta de git; falta Villafuerte Rosero)

### Verificación
Comando:

    grep -n "no contemporáneo" 10_Autoria/notas_campo/readme.md

Resultado: presente en el aviso de estado y en el título de la tabla.

### Commits
- `d96fc5c` — rotulado de las notas de campo y restitución de la declaración de ausencia
- `61ec1f3` — fila de notas de campo de verificacion_seccion15 corregida

### Limitaciones
Falta la firma de Villafuerte Rosero en F1b. La columna `evidencia_nota_campo` de la bitácora ya declara "NO EXISTE nota de campo" en las cuatro sesiones de campo (verificado el 21/09/2026), y `Notas_de_Campo_SIMPA_16_Entrevistas.md` ya trae un aviso al inicio: es una síntesis analítica posterior de Macías Herrera con apoyo de IA, no una nota tomada en campo. Ambas correcciones quedan cerradas por I1.

### Evidencia entregada fuera del repositorio
Pendiente: rectificación firmada por el equipo (por correo institucional).
---

## F2 — Member checking: trazabilidad, evidencia y actas

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,30 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** C1 (cumplida)

### Problema detectado
Los enunciados 1, 8, 9 y 10 se apoyan en ENTR-13, codificada el 07/09/2026, **después** de la sesión de miembro-verificación del 04/09/2026, y la síntesis se compiló después de las actas. Ningún enunciado estaba enlazado a los códigos y las citas que lo sostienen. Las actas no declaran modalidad ni hora.

### Acción aplicada
Se construyó la trazabilidad que faltaba con
`07_Datos/scripts/plan_mejora/trazabilidad_F2.py`: para cada uno de los doce
enunciados sometidos a verificación, el script propone los códigos del libro
que le corresponden y recupera **las citas literales verificadas en C1** que
lo sostienen, con su entrevista y su línea de transcripción.

La correspondencia enunciado→código se calcula por solape de términos
ponderado por rareza (IDF) contra el nombre, la definición y el criterio de
aplicación de cada código, y queda escrita en `MOTIVO_PROPUESTA` fila a fila.
Es una **propuesta**: la columna `CODIGOS_VERIFICADOS` la firma una persona.

Se transcribió además, del acta consolidada, la posición de cada uno de los
tres participantes sobre cada enunciado (confirma, matiza, rechaza, no
abordado o sin posición registrada).

### Hallazgos propios del equipo
- **El enunciado 12** —«la mayor dificultad reside en lograr el uso
  efectivo»— **no tiene ninguna cita literal verificada que lo sostenga**. No
  se le asigna código porque el libro no contiene ninguno que le corresponda.
  Se declara: es un enunciado interpretativo que no traza al corpus.
- **El enunciado 8** —formalización del registro asociada al tamaño de la
  finca— tampoco tiene códigos propios: el libro no recoge «tamaño de finca»
  ni «formalización». Las citas que se le asocian son las de registro en
  papel, que no sostienen la parte del tamaño.
- **Cinco de los doce enunciados fueron rechazados** por al menos un
  participante (1, 2, 7, 8 y 10). El grado de acuerdo global que declara el
  acta es «medio». Eso ya consta y no se suaviza.

### Sobre la anterioridad de ENTR-13 — lo que no tiene arreglo
El acta es del 04/09/2026 y la codificación de ENTR-13 es del 07/09/2026.
**Esa anterioridad no se puede corregir**: es una fecha pasada. No se
antedata ningún documento ni se reescribe el historial. Se declara tal cual,
y la trazabilidad permite ver, enunciado por enunciado, qué parte del
respaldo procede de entrevistas codificadas antes de la sesión y qué parte
de ENTR-13.

La sesión se celebró: existen las grabaciones, las tres actas individuales y
el acta consolidada, con los facilitadores nombrados.

### Evidencia utilizada
- `02_Evidencias/Member_Checking/Actas_consolidada/` — los doce enunciados y la matriz de resultados
- `02_Evidencias/Member_Checking/Actas/` — las tres actas individuales
- `07_Datos/libro_codigos.md` v1.0 y los 213 fragmentos con cita literal verificada en C1
- Fecha: 21/09/2026

### Archivos modificados
- `07_Datos/scripts/plan_mejora/trazabilidad_F2.py`
- `07_Datos/datos_procesados/trazabilidad_member_checking_F2.csv`
- `07_Datos/resultados/trazabilidad_member_checking_F2.md`
- `02_Evidencias/Member_Checking/Complemento_Actas_F2.md`
- `02_Evidencias/00_Restringido/fichas_tecnicas.csv` — tres filas nuevas
- `checksums_evidencias.sha256` — tres hashes nuevos

### Criterio de aceptación
- [ ] Actas posteriores al commit de codificación — **no es alcanzable**: la sesión ocurrió el 04/09 y ENTR-13 se codificó el 07/09. Se declara en lugar de corregirse
- [x] Cada enunciado enlaza a sus códigos y a sus citas literales
- [x] Modalidad, hora y firma: declaradas en `02_Evidencias/Member_Checking/Complemento_Actas_F2.md`, con la grabación de la ronda publicada e inventariada

### Verificación
Comando:

    python3 07_Datos/scripts/plan_mejora/trazabilidad_F2.py

Resultado:

    Enunciados: 12
    Codigos del libro: 91 | fragmentos con cita: 213
    Sin cita que lo sostenga: 1
    Rechazados por alguien: 5

### Grabación de la ronda incorporada al inventario
El protocolo de la ronda pedía actas, no grabaciones, y por eso el registro en
audio nunca se había publicado: era la única actividad del proyecto en esa
situación, frente al walkthrough, cuyos vídeos sí constaban.

El **21/09/2026** las tres grabaciones se publicaron en el contenedor cifrado
`Audios_Member_Checking.7z` de la publicación `v1.1-evidencias` del
repositorio de evidencias, y se añadieron al inventario con su duración y su
SHA-256, calculados sobre el contenido real del contenedor:

| Archivo | Sub-sesión | Duración |
|---|---|---:|
| `04-09-2026_Audio_Entr-01_Member_Checking.mp3` | ENTR-01 | 7 min 56 s |
| `04-09-2026_Audio_Entr-02_Member_Checking.mpeg` | ENTR-02 | 18 min 12 s |
| `04-09-2026_Audio_Entr-13_Member_Checking.mpeg` | ENTR-13 | 5 min 57 s |

**Las dos fechas constan por separado:** la grabación es del 04/09/2026
—columna `fecha` de las fichas— y su incorporación al repositorio del
21/09/2026. No se añadieron a `v1.0-evidencias`, fechada el 30/08/2026,
precisamente para no dar a entender que estaban desde entonces.

Con esto la miembro-verificación queda al mismo nivel de acreditación que el
walkthrough: acta, grabación publicada y hash verificable.

### Limitaciones
La correspondencia enunciado→código es automática y está pendiente de
verificación humana en las doce filas. Donde el libro de códigos no contiene
el concepto del enunciado —casos 8 y 12— el script no inventa una
correspondencia: lo deja vacío y lo señala.

Las actas emitidas siguen declarando `Modalidad: No registrado` y sin hora:
**no se modifican**. La modalidad presencial y la franja horaria se declaran
en el documento complementario, y la franja se deriva de los metadatos de los
dispositivos, no de una bitácora tomada durante la sesión.

La anterioridad de la codificación de ENTR-13 respecto del acta no tiene
arreglo y no se disimula: está declarada, y la trazabilidad permite ver qué
parte del respaldo de cada enunciado procede de esa entrevista.

### Evidencia entregada fuera del repositorio
Grabaciones de la ronda del 04/09/2026, en el contenedor cifrado
`Audios_Member_Checking.7z` de la publicación `v1.1-evidencias` del
repositorio de evidencias audiovisuales. La contraseña la entrega el SGA,
conforme al procedimiento declarado en `checksums_evidencias.sha256`.

---
## F3 — Walkthrough: consentimientos firmados después de la sesión

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** ninguna

### Problema detectado
Los consentimientos de WT-04 y WT-06 se firmaron después de la sesión; faltaba la fecha de WT-06 y su perfil real, y se afirmaba que las actas no estaban firmadas.

### Acción aplicada
Se revisaron las seis actas y los consentimientos de las sesiones de
walkthrough del 03/09/2026 y se precisó por escrito, en
`02_Evidencias/Validacion_Walkthrough/Declaracion_Walkthrough_F3.md`, lo que
cada documento declara realmente. **No se modificó ninguna acta ni ningún
consentimiento**: los documentos se conservan tal como se emitieron y los
consentimientos, además, están firmados.

Se corrigió la descripción de la carpeta `Acta/` en el readme.

### Qué se comprobó, y qué resultó
**Dónde está la firma.** Las seis sesiones tienen consentimiento informado
firmado: el apartado 8 del formulario recoge nombre, rol, firma y fecha de la
persona participante y del integrante del equipo. Las actas no llevan sección
de firma, y no es un defecto: el acta registra lo observado y la firma vive
en el consentimiento. El readme describía `Acta/` como «seis actas de sesión
con la firma enmascarada», lo que no es exacto —no hay firma que enmascarar—
y se corrige.

**Consentimientos de WT-04 y WT-06.** Que se firmaron después de la sesión no
es una deducción: lo declara la propia acta de cada una, con la misma frase,
«se le informó que el formulario de consentimiento le sería remitido
posteriormente para su firma». Las otras cuatro actas no la contienen.

**Fecha de la sesión WT-06.** Su acta declara `Fecha: No registrado`, única de
las seis. La sesión se celebró el 03/09/2026 junto con las demás, según el
nombre del archivo, el readme de la carpeta y las otras cinco actas. Fue un
olvido al cumplimentar el acta y se precisa aquí sin modificarla.

**Campo «perfil» de las actas.** Cuatro actas (WT-01, WT-02, WT-05, WT-06)
consignan el perfil de la persona participante. Dos (WT-03 y WT-04) consignan
en ese campo el rol del prototipo evaluado, que es el dato del
consentimiento: «Perfil declarado: Supervisor».

### Hallazgos propios del equipo
- **De WT-03 y WT-04 no consta el perfil de la persona participante.** Su
  acta recoge el rol del prototipo. Se declara como dato ausente y no se
  completa de memoria. Importa porque la separación entre participantes
  técnicos y no técnicos se apoya en el perfil de la persona.
- **El formulario de consentimiento no titula igual ese campo en todas sus
  versiones:** en unas dice «Rol o perfil» y en otras «Rol o a qué se
  dedica». La segunda redacción invita a leerlo como la ocupación de la
  persona cuando lo que se anota es el rol del prototipo. Esa ambigüedad
  explica que dos actas lo trasladaran al campo equivocado.
- **La fecha escrita en los consentimientos de WT-04 y WT-06 es 03/09/2026,
  la de la sesión**, pese a que el acta dice que el formulario se remitió
  después. Caben dos lecturas —que se firmara ese mismo día más tarde, o que
  la fecha escrita sea la de la sesión— y el equipo no puede acreditar cuál,
  porque no conserva registro de la entrega ni de la devolución del
  formulario. Se declaran los dos hechos y no se elige entre ellos.

### Evidencia utilizada
- `02_Evidencias/Validacion_Walkthrough/Acta/` — las seis actas
- `02_Evidencias/Validacion_Walkthrough/Consentimientos/` — los seis consentimientos
- `02_Evidencias/Validacion_Walkthrough/readme.md`
- Fecha: 21/09/2026

### Archivos modificados
- `02_Evidencias/Validacion_Walkthrough/Declaracion_Walkthrough_F3.md`
- `02_Evidencias/Validacion_Walkthrough/readme.md`

### Criterio de aceptación
- [x] Fecha real de firma declarada en cada caso, con las dos lecturas posibles donde no puede acreditarse
- [x] Perfiles contrastados: se declara cuáles constan y de cuáles no consta

### Verificación
Comando:

    grep -c "Perfil declarado" 02_Evidencias/Validacion_Walkthrough/Acta/*.pdf 2>/dev/null
    grep -n "Acta/" 02_Evidencias/Validacion_Walkthrough/readme.md

Resultado: dos actas (WT-03 y WT-04) consignan «Perfil declarado» en lugar del
perfil de la persona; el readme ya no atribuye firma a las actas.

### Limitaciones
No consta el perfil de la persona participante en WT-03 ni en WT-04, y **no se
completa**: se declara ausente. Si aparece en la zona restringida, se
incorporará citando su fuente.

No puede acreditarse el momento real de firma de los consentimientos de WT-04
y WT-06. Se declara lo que dice cada documento y se deja la contradicción a la
vista, sin resolverla.

### Evidencia entregada fuera del repositorio
Actas y consentimientos íntegros, sin enmascarar, en la zona restringida.

---
## F4 — Registrar las visitas del 27/06, 02/08 y 21/08

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,10 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** ninguna

### Problema detectado
Tres fechas de visita a campo constaban en unas fuentes y no en otras: el acta de constancia, las fotografías del entorno y la bitácora de sesiones no coincidían entre sí. La bitácora, además, declaraba para las cuatro sesiones de campo unas notas de campo manuscritas que después resultaron no existir.

### Acción aplicada
Se contrastaron las tres fuentes —fotografías de `02_Evidencias/Fotos_Entorno/`, acta de constancia de la organización y `10_Autoria/bitacora_sesiones.csv`— y la discrepancia se registró tal cual, sin forzar ninguna fecha para que cuadrara.

Se corrigió la bitácora en sus cuatro sesiones de campo (SES-27 a SES-30):

- El campo `evidencia_nota_campo` dejaba de ser cierto: apuntaba a los 16 PDF retirados el 20/09/2026. Ahora declara que **no existe nota de campo** y remite al inventario de audio y vídeo como registro real de cada sesión.
- El campo `decisiones_tomadas` afirmaba «Notas de campo levantadas a mano durante las N entrevistas. Nota generada: SI». Se sustituyó por la duración grabada de la sesión y por la referencia a la rectificación F1b.

### Hallazgo propio del equipo
El acta de constancia firmada el 16/09/2026 enumera una actividad de campo del **02/08/2026**, día en el que el repositorio no documenta ninguna entrevista. La discrepancia se declara y no se resuelve inventando una sesión.

### Evidencia utilizada
- `02_Evidencias/Fotos_Entorno/` y sus metadatos EXIF
- `10_Autoria/correspondencia/2026-09-16_Acta_Constancia_Actividades_Campo_Enmascarada.png`
- `10_Autoria/bitacora_sesiones.csv`
- Fecha: 21/09/2026

### Archivos modificados
- `10_Autoria/bitacora_sesiones.csv`

### Criterio de aceptación
- [x] Bitácora y fotos contrastadas — discrepancia real documentada, no forzada a cuadrar
- [x] Bitácora corregida: las cuatro sesiones de campo ya no declaran notas de campo inexistentes
- [ ] Pie de foto incorrecto — no localizado en el estado actual del repositorio; se declara como no encontrado

### Verificación
Comando:

    grep -c "NO EXISTE nota de campo" 10_Autoria/bitacora_sesiones.csv
    grep -c "N/D" 10_Autoria/bitacora_sesiones.csv

Resultado:

    4      (las cuatro sesiones de campo)
    0      (ningun N/D en la bitacora)

### Limitaciones
La discrepancia de la fecha del 02/08/2026 queda declarada y sin resolver: no hay forma de saber, con lo que consta en el repositorio, si hubo una actividad ese día que no se documentó o si el acta recoge mal la fecha. No se modifica el acta, que está firmada por un tercero.

El pie de foto incorrecto que señalaba el plan no se ha localizado en el estado actual del repositorio; se declara como no encontrado en lugar de darse por corregido.

### Evidencia entregada fuera del repositorio
No aplica.

---
## G2 — Estado real de la acreditación y la aprobación ética

**Estado operativo:** VERIFICADA (declaración explícita de ausencia, firmada)
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Arboleda Yanza Francisco Javier y Macías Herrera Josthyn Esteban (firma de la declaración)
**Dependencias:** ninguna

### Problema detectado
A.12 figura como «Vigente» en `README_Etica.md` (tabla de la sección 1)
mientras que el propio documento, en su sección 5, indica que debe presentarse
como «en curso» y no como acreditación cumplida. Además, las adendas se
refieren a un «protocolo aprobado» sin que conste acta de aprobación.

### Acción aplicada
Se precisó el estado real de A.12 y se separaron dos cuestiones que el
repositorio presentaba de forma conjunta: la acreditación de formación ética
de las personas (A.12) y la aprobación ética del proyecto. Se verificó que
A.12 no tiene certificados adjuntos, que sus casillas de estado están sin
marcar y que sus fichas de detalle están vacías. Se verificó asimismo que en
el repositorio no consta ningún dictamen de comité de ética: las únicas
menciones a «comité» corresponden al Comité de Control de Cambios.

Se consultó al docente responsable, que gestionó el trámite de ética del
proyecto, para precisar si existe un dictamen de comité con número y fecha o
si lo que consta es su acreditación de formación y la aprobación del proyecto
en el marco de la asignatura.

### Evidencia utilizada
- Archivo: `09_Etica/A12_Certificado_Etica.pdf`, secciones 3, 4 y 5
- Fuente: texto extraído del propio anexo
- Comprobación: `git grep -i "comité"` sobre el repositorio completo
- Fecha: 19/09/2026

### Archivos modificados
- `09_Etica/README_Etica.md`

### Criterio de aceptación
- [x] Estado real de A.12 declarado y corregido en la tabla
- [x] Dictamen con número y fecha, o declaración explícita de ausencia — se optó por la segunda: `09_Etica/Declaracion_Ausencias_G2_G4.md` declara "SIN dictamen de comité de ética", firmada por dos integrantes

### Verificación
Comando:

    grep -n "A.12" 09_Etica/README_Etica.md

Resultado:

    4 coincidencias: líneas 27, 56, 58 y 75 de 09_Etica/README_Etica.md; la línea 27 dice «En curso»

### Commits
- `25dad77` — `docs(G2): precisar estado real de la acreditacion etica A12`

### Limitaciones
El equipo no esperó la respuesta del docente para cerrar el criterio: declaró explícitamente la ausencia de dictamen, dejando constancia de que se actualizará si aparece un dictamen real (mismo tratamiento que G4). Las líneas 49 y 96 de `A14_Adenda_Tercera_Ronda.tex` no se modifican porque es un anexo firmado; su lectura debe hacerse junto con esta declaración de ausencia, no en su lugar.

Las líneas 49 y 96 de `A14_Adenda_Tercera_Ronda.tex`, que se refieren al
«protocolo aprobado», no se han modificado a la espera de esa misma respuesta.

### Evidencia entregada fuera del repositorio
Consulta al docente por correo institucional — 19/09/2026.

---

## G3 — Matriz uso por consentimiento de cada participante

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,30 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** ninguna

### Problema detectado
No constaba, participante a participante, qué usos autorizó cada persona y cuáles de los usos efectivamente realizados por el equipo estaban cubiertos por el formulario que firmó. Los tres formularios empleados a lo largo del proyecto cubren usos distintos.

### Acción aplicada
Se construyó `09_Etica/matriz_uso_consentimiento_G3.csv`, una fila por participante y una columna por uso: entrevista, audio, vídeo, fotografía, sesión con el prototipo, publicación en depósito abierto y envío a un LLM o a transcripción externa.

Cada celda toma uno de cinco estados, definidos en `09_Etica/Matriz_Uso_Consentimiento_G3.md`: AUTORIZADO, PARCIAL, NO_CUBIERTO (el formulario no dice nada del uso, aunque el equipo lo hizo), NO_AUTORIZADO (la casilla existe y quedó sin marcar) y NO_APLICA.

Los estados salen de la lectura de las imágenes de los consentimientos y del texto de A.03, de la adenda de segunda ronda y de A.14, y cada fila lleva su nota con lo que dice literalmente el formulario firmado.

### Hallazgos propios del equipo
La matriz declara cuatro situaciones que el repositorio no recogía:

1. **Fotografía: NO_CUBIERTO en los 16.** Ningún formulario de los tres menciona el uso de fotografías.
2. **Envío a un LLM o a transcripción externa: NO_CUBIERTO en los 16.** Ningún formulario lo contempla, y el proyecto sí lo hizo (declarado en B2).
3. **Sesión con el prototipo: USADO_SIN_AUTORIZACION en 2 participantes.** Ambos dejaron sin marcar la casilla "Sesión con el prototipo" y, aun así, se les mostraron pantallas: a uno en las líneas 97 a 107 de su transcripción y a otro en las líneas 49 a 57. En este segundo caso, el fragmento CONSOLIDADO_SEMANAL procede de esa parte.
4. **Audio y vídeo: NO_CUBIERTO en los 3 participantes de la primera ronda**, cuyo consentimiento manuscrito no menciona grabación ni usos posteriores.

Se declaran tal cual. No se reinterpretan los formularios ni se pide una autorización retroactiva.

### Evidencia utilizada
- `02_Evidencias/Consentimientos/` — imágenes de los 16 consentimientos firmados
- `09_Etica/` — A.03 v3, adenda de segunda ronda, A.14
- `02_Evidencias/Transcripciones/` — para localizar los tramos de sesión con el prototipo
- Fecha: 21/09/2026

### Archivos modificados
- `09_Etica/Matriz_Uso_Consentimiento_G3.md` y `09_Etica/matriz_uso_consentimiento_G3.csv`
- `07_Datos/datos_procesados/matriz_uso_consentimiento_G3.csv` y `readme_matriz_G3.md`

### Criterio de aceptación
- [x] Una fila por participante con el estado de cada uso frente a lo que firmó

### Verificación
Comando:

    python3 -c "import csv,collections; r=list(csv.DictReader(open('09_Etica/matriz_uso_consentimiento_G3.csv',encoding='utf-8-sig'),delimiter=';')); print(len(r),'participantes'); [print(c, dict(collections.Counter(x[c] for x in r))) for c in list(r[0])[4:10]]"

Resultado:

    16 participantes
    audio                        {'AUTORIZADO': 13, 'NO_CUBIERTO': 3}
    video                        {'AUTORIZADO': 13, 'NO_CUBIERTO': 3}
    foto                         {'NO_CUBIERTO': 16}
    sesion_prototipo             {'NO_APLICA': 8, 'NO_AUTORIZADO': 6, 'USADO_SIN_AUTORIZACION': 2}
    publicacion_deposito_abierto {'AUTORIZADO': 8, 'PARCIAL': 8}
    envio_a_LLM_o_transcripcion_externa {'NO_CUBIERTO': 16}

### Commits
- `32a5b3f`, `334c39f`

### Limitaciones
La matriz declara la situación; **no la corrige**. Los dos casos de sesión con el prototipo sin autorización y los usos no cubiertos por los formularios quedan señalados para que el equipo decida qué hacer con el material afectado, decisión que no se toma en esta tarea.

La lectura de los consentimientos manuscritos se hizo sobre las imágenes; donde el texto es ambiguo, la nota de la fila recoge lo que dice literalmente el formulario y no la interpretación del equipo.

### Evidencia entregada fuera del repositorio
No aplica.

---
## G4 — Aval de la organización firmado o ausencia declarada

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** ninguna

### Problema detectado
`A05_Aval_Institucional.pdf` se presentaba como aval de la organización. No existía una declaración clara de qué organizaciones avalaron el trabajo de campo, con qué documento y en qué fecha.

### Acción aplicada
Se revisó qué consta realmente en el repositorio y se declaró por escrito en `09_Etica/Declaracion_Ausencias_G2_G4.md`, sección 2, participante a organización:

- **Palmicultora M.** Consta un "Acta de constancia y autorización de actividades de campo" firmada por su administrador el **16/09/2026**. Es una autorización **posterior** a las entrevistas del 23/05 y el 28/07, y el acta misma indica que su firma no crea evidencia retroactiva.
- **Extractora R.** **No existe aval ni autorización firmados** de esta organización, ni para ENTR-04 ni para ENTR-08. Solo existen los consentimientos individuales de cada participante.
- **`A05_Aval_Institucional.pdf`** es una **carta redactada por el propio equipo, sin fecha ni firma**. Se declara que no debe presentarse como aval de ninguna organización.

La declaración está firmada en su sección 3 por quien verificó su contenido.

### Hallazgo propio del equipo
El acta de Palmicultora M enumera una actividad del **02/08/2026**, día en el que no hay ninguna entrevista documentada en el repositorio. La discrepancia se registra y se remite a F4; no se ajusta ninguna fecha para hacerla cuadrar.

### Evidencia utilizada
- `10_Autoria/correspondencia/2026-09-16_Acta_Constancia_Actividades_Campo_Enmascarada.png`
- `09_Etica/A05_Aval_Institucional.pdf`
- `02_Evidencias/Consentimientos/`
- Fecha: 21/09/2026

### Archivos modificados
- `09_Etica/Declaracion_Ausencias_G2_G4.md`

### Criterio de aceptación
- [x] Aval firmado adjunto, o ausencia declarada de forma explícita, organización por organización

### Verificación
Comando:

    grep -n "SIN aval firmado\|sin fecha ni firma\|16/09/2026" 09_Etica/Declaracion_Ausencias_G2_G4.md

Resultado: la sección 2 declara la autorización posterior de una organización, la ausencia de aval de la otra y la naturaleza real de A.05.

### Commits
- `334c39f`, `749801d`

### Limitaciones
La declaración se limita a lo que consta en el repositorio a 21/09/2026. Si alguna de las dos organizaciones firma un aval, se adjuntará con su fecha real y se actualizará el anexo A.05; la autorización existente no se presenta como cobertura retroactiva del trabajo de campo ya realizado.

La firma de Macías Herrera queda pendiente en el documento; una línea sin firmar significa que esa persona no firmó, no que esté conforme.

### Evidencia entregada fuera del repositorio
No aplica.

---
## G5 — Checksums y congelación del release de evidencias

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,10 pts
**Responsable(s):** Macías Herrera Josthyn Esteban
**Dependencias:** F1 y F2 cerradas

### Problema detectado
checksums_evidencias.sha256 no cubre ENTR-09 a 16, walkthrough ni actas, y los archivos del release de evidencias se volvieron a subir hasta el 16/09.

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] Un hash por cada original declarado
- [ ] Sin cambios tras la etiqueta

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
En ejecución según el plan de ejecución rev. 8. Esta sección se completa con lo que realmente ocurra al cerrar la tarea; no se marca Hecho sin criterio cumplido.

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## H1 — Corregir la documentación del cuestionario

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** ninguna

### Problema detectado
`02_Evidencias/Cuestionario/Respuestas/readme.md` describía mal el instrumento: número de ítems incorrecto, plataforma sin identificar, y sin explicar las 4 respuestas del 30/06 ni el modo real de aplicación. Tampoco distinguía sobre qué base se calcula cada cifra agregada.

### Acción aplicada
Se corrigió el readme con lo que el propio formulario documenta:

- **Plataforma:** Microsoft Forms, y el archivo crudo es su exportación directa. Por contener datos personales se trata como **evidencia restringida** y no se usa para análisis.
- **Dos tandas verificables por marca de tiempo de servidor:** una ronda piloto de **4 respuestas el 30/06/2026** (EV-10, validación puntual de RF-04, RF-07 y RF-12) y la ronda ampliada de **58 respuestas los días 01 y 02/08/2026** (parte de EV-12). Cualquier cifra agregada debe declarar si trabaja sobre **n = 62** o sobre **n = 58**.
- **Ítems:** 15, y ninguno recoge nombre ni correo.

### Hallazgo propio del equipo
Se analizaron las marcas de hora de inicio y fin que registra el formulario: la **duración mediana es de 42,5 segundos por respuesta**, y en **38 de los 61** intervalos entre el fin de una respuesta y el inicio de la siguiente transcurren entre 0 y 10 segundos.

Eso es compatible con una **aplicación presencial y secuencial** —varias personas respondiendo una tras otra desde un mismo dispositivo compartido, con el administrador presente— y no con una distribución remota e independiente. Se declara porque el modo de aplicación afecta directamente a la interpretación de la independencia de las respuestas, y por tanto a cualquier estadístico que la presuponga.

### Evidencia utilizada
- `07_Datos/datos_crudos/Sistema Inteligente de Mantenimiento de Palma Africana(1-62).xlsx` — exportación cruda, con sus marcas de tiempo de servidor
- Texto del formulario y del consentimiento incorporado en él
- Fecha: 21/09/2026

### Archivos modificados
- `02_Evidencias/Cuestionario/Respuestas/readme.md`

### Criterio de aceptación
- [x] Plataforma, número de ítems y datos recogidos descritos conforme al instrumento real
- [x] Las 4 respuestas del 30/06 y el modo de aplicación explicados, con la distinción n = 62 / n = 58

### Verificación
Comando:

    grep -n "Microsoft Forms\|42,5 segundos\|n = 58\|30/06/2026" 02_Evidencias/Cuestionario/Respuestas/readme.md

Resultado: el readme declara la plataforma, las dos tandas con sus fechas, la mediana de duración y la base de cálculo de cada cifra.

### Commits
- `0279b40`

### Limitaciones
El análisis del modo de aplicación se apoya en las marcas de tiempo del formulario, que indican **compatibilidad** con una aplicación presencial y secuencial; no la demuestran. No se dispone de un registro independiente de cómo se aplicó cada respuesta.

La sensibilidad de los resultados a la base elegida (n = 62 frente a n = 58) queda declarada, pero no se han recalculado las cifras agregadas ya publicadas en otros documentos: esa corrección corresponde a A6 y E2.

### Evidencia entregada fuera del repositorio
No aplica.

---
## H2 — Aclarar las fotos del cuestionario

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,10 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** Ninguna

### Problema detectado
Las fotos rotuladas como aplicación del cuestionario son del 15/09 (consentimiento complementario) y los commits titulados fotografías reales de aplicación solo contienen capturas.

### Acción aplicada
Se añadió al readme de `Fotos_Aplicacion/` una sección que declara que los commits `34ce578` y `0792213` solo contienen las 15 capturas del instrumento, que las cinco fotografías son de la sesión complementaria de consentimiento del 15/09/2026 y que la Foto-01 fue editada por privacidad. Se corrigió el rótulo de la verificación EXIF. Los mensajes de commit no se modifican por la regla de no reescribir el historial.

### Evidencia utilizada
- Commits `34ce578` y `0792213`: 15 capturas `cuestionario_p01` a `p15`, sin fotografías de trabajadores.
- Metadatos EXIF de las cinco fotografías (2026-09-15, 10:08 a 10:10).

### Archivos modificados
- `02_Evidencias/Cuestionario/Fotos_Aplicacion/readme.md` (commit 4699e99)
- `10_Autoria/verificacion_exif_aplicacion.md` (commit f13e632)

### Criterio de aceptación
- [x] Aclarado que las fotos son del 15/09 (consentimiento complementario)
- [x] Aclarado que los commits de "fotografías reales de aplicación" solo contienen capturas
- [x] Nombres y mensajes coherentes con el contenido. La línea 357 del ERS ya no afirma que la carpeta contiene fotografías reales de aplicación en campo: declara que son capturas del instrumento y fotos de otra sesión (corregido el 21/09/2026). El nombre de la carpeta `Fotos_Aplicacion` se conserva: es un nombre genérico, no una afirmación falsa por sí mismo, y su propio readme ya aclara el contenido real.

### Verificación
Comando:

    for h in 34ce578 0792213; do git show --name-status --format= $h | awk '{print $1}' | sort | uniq -c; done

Resultado:

    34ce578: 15 A y 1 D (el D es el readme de la carpeta)
    0792213: 15 A

### Commits
- `4699e99` — aclaración de commits y fotos en el readme de Fotos_Aplicacion
- `f13e632` — rótulo corregido en la verificación EXIF

### Limitaciones
La línea 357 del ERS ya se corrigió. Los mensajes de los commits `34ce578` y `0792213` no pueden modificarse, por la regla de no reescribir el historial; la aclaración real queda en el readme de la carpeta y ahora también en el propio ERS.

### Evidencia entregada fuera del repositorio
No aplica.
---

## I1 — Coherencia documental

**Estado operativo:** VERIFICADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** el resto de tareas de la ronda

### Problema detectado
Cuatro incoherencias entre documentos del repositorio: `README_Etica.md` no precisaba el alcance de la reescritura de historial del repositorio anterior; `CITATION.cff` seguía diciendo "ocho entrevistas" cuando son dieciséis; la cabecera del ERS estaba rotulada "v3.0" cuando el historial de versiones vigente es la v2.0; y el `CHANGELOG.md` no tenía ninguna entrada que documentara el trabajo de esta ronda.

### Acción aplicada
- `09_Etica/README_Etica.md` precisa el alcance de la reescritura de historial del repositorio anterior.
- `CITATION.cff` corrige "ocho entrevistas" por dieciséis.
- La cabecera del ERS corrige "v3.0" por "v2.0", conforme al historial de versiones vigente, y el PDF se recompiló para que fuente y PDF coincidan.
- `CHANGELOG.md` incorpora la entrada `[4.4.0]` de esta ronda, con las tareas añadidas, cambiadas y retiradas, y remite a este registro para el detalle por tarea.

### Evidencia utilizada
- `CITATION.cff`, `CHANGELOG.md`, `01_ERS/ERS_SRS_2B_v2.0.tex`, `09_Etica/README_Etica.md`
- Fecha: 21/09/2026

### Archivos modificados
- `CITATION.cff` · `CHANGELOG.md` · `01_ERS/ERS_SRS_2B_v2.0.tex` y su PDF · `09_Etica/README_Etica.md`

### Criterio de aceptación
- [x] Las cuatro incoherencias señaladas, corregidas

### Verificación
Comando:

    grep -n "dieciséis entrevistas" CITATION.cff
    grep -n "^## \[" CHANGELOG.md | head -2

Resultado:

    CITATION.cff:18  ... La elicitación se sustenta en dieciséis entrevistas
    CHANGELOG.md:8   ## [4.4.0] - 2026-09-21 - Plan de mejora de los datos del proyecto

### Commits
- `303ea82`, `a790780`, `dc2ca0f`, `f62941f`

### Limitaciones
La coherencia se ha comprobado sobre los cuatro puntos señalados en la revisión, no sobre el repositorio completo. Quedan documentos cuya redacción es anterior a esta ronda y que pueden contener afirmaciones que otras tareas han dejado sin sustento: en particular, cualquier texto que afirme saturación debe revisarse a la luz del resultado de C4, y cualquier cifra agregada del cuestionario debe declarar su base tras H1.

El estado por tarea de este mismo registro se actualizó al cierre de la ronda; la fuente de verdad sobre lo hecho es el repositorio y los comandos de verificación de cada entrada.

### Evidencia entregada fuera del repositorio
No aplica.

---
