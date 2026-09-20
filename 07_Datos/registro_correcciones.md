# Registro de correcciones

Cada entrada corresponde a una de las 39 tareas oficiales del Plan de
mejora de datos (19/09/2026). El campo **Estado de rúbrica** se deja en
*pendiente de mapeo* hasta que el docente aclare la diferencia práctica
entre *Por modificar* y *Por culminar*.

---

## G1 — Datos personales

**Estado operativo:** VERFICADA
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

**Estado operativo:** EN PROCESO
**Estado de rúbrica:** pendiente de mapeo
**Responsable:** Macías Herrera Josthyn Esteban
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
| RF-42 no deja el nombre recuperable | Cero apariciones tras la supresión |

### Commits

- `035470c` (repositorio del prototipo) — implementar RF-40, RF-41 y RF-42
- `147d9d1` — actualizar el puntero del submódulo
- `fb82f18` — README final del MVP

### Limitaciones

La verificación de los criterios se realizó ejecutando la lógica de la
aplicación fuera del navegador, lo que valida el comportamiento pero no la
interfaz. La prueba de extremo a extremo por rol, con evidencia gráfica en
`05_MVP/evidencia_e2e/`, está pendiente.

El despliegue de Netlify se publica manualmente y no está enlazado al
repositorio, por lo que ambos pueden volver a divergir.
---

## A1 — Repetir la evaluación con evaluadores externos

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,80 pts
**Responsable(s):** Sin asignar (fuera del núcleo de la rev. 8)
**Dependencias:** A2, A3

### Problema detectado
Las tres hojas de puntuación se subieron el 12/09 con 25 y 27 segundos de diferencia. En 131 de 150 filas las puntuaciones siguen un ciclo por posición de fila; en 139 de 150 las cinco dimensiones valen lo mismo; los comentarios de dos evaluadores citan términos que no aparecen en los requisitos; el registro de evaluadores fecha la evaluación antes de que existieran el archivo cegado y las instrucciones.

### Acción aplicada
Ninguna todavía.

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
No iniciada. No forma parte del núcleo del plan de ejecución rev. 8: la demanda del núcleo (28 h por persona) supera la capacidad disponible (~17 h por persona). Si no se ejecuta antes del cierre, se declara como no ejecutada por esta causa.

Qué haría falta: Evaluadores reales de otro paralelo, sin participación en el proyecto, con consentimiento firmado y declaración de conflicto de interés; cada evaluador sube su propia hoja o la sube un custodio ajeno al equipo. Depende de A2 y A3. La explicación escrita se entrega por correo aunque no se repita la evaluación.

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## A2 — Normalizar el estilo de los dos conjuntos antes de cegar

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,40 pts
**Responsable(s):** Sin asignar (fuera del núcleo de la rev. 8)
**Dependencias:** A3

### Problema detectado
Si el criterio de verificación empieza por El, Cada, Todo, La, Ningún o Se, el requisito es del LLM en 48 de 50 casos, y la longitud media es de 619 caracteres en los del equipo frente a 464 en los del LLM.

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] Un clasificador simple (primera palabra y longitud, validación dejando uno fuera) no supera el 65 % de acierto sobre el origen

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
No iniciada. No forma parte del núcleo del plan de ejecución rev. 8: la demanda del núcleo (28 h por persona) supera la capacidad disponible (~17 h por persona). Si no se ejecuta antes del cierre, se declara como no ejecutada por esta causa.

Qué haría falta: Normalizar el estilo de ambos conjuntos, volver a cegar y medir el clasificador con un script versionado.

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## A3 — Rehacer el conjunto del equipo desde la transcripción congelada ENTR-04

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,30 pts
**Responsable(s):** Sin asignar (fuera del núcleo de la rev. 8)
**Dependencias:** Ninguna

### Problema detectado
9 de 25 requisitos del equipo vienen del ERS anterior, al menos 5 tratan temas que no aparecen en ENTR-04 y 16 se redactaron el 11/09 para llegar al mínimo de 25. Las columnas procedencia y nota_metodologica están intercambiadas en 6 filas (H-002, H-003, H-013 a H-015, H-020) y hay pares casi idénticos (H-013/LLM-005, H-014/LLM-006, H-015/LLM-007, H-020/LLM-015).

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] Cada RF del equipo cita un fragmento literal de ENTR-04
- [ ] Columnas alineadas
- [ ] Pares casi idénticos excluidos o analizados aparte

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
No iniciada. No forma parte del núcleo del plan de ejecución rev. 8: la demanda del núcleo (28 h por persona) supera la capacidad disponible (~17 h por persona). Si no se ejecuta antes del cierre, se declara como no ejecutada por esta causa.

Qué haría falta: Rehacer el conjunto solo desde ENTR-04 con cita literal, o declarar la desviación; corregir las columnas intercambiadas y tratar los pares casi idénticos.

### Evidencia entregada fuera del repositorio
No aplica todavía.

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
- `06_Experimento/prompts_llm/2026-09-11_1300_claude-sonnet-5.md` (commit `dbc5d1e`)

### Criterio de aceptación
- [x] Conversación archivada — prompt literal y respuesta íntegra conservados en el archivo de registro
- [x] Prompt recalculable desde la fuente congelada — hash verificado contra EXP-02
- [x] La nota borrada se restituye — commit nuevo, sin reescribir `037f995`

### Verificación
Comando:

    git show 037f995 -- 06_Experimento/prompts_llm/2026-09-11_1300_claude-sonnet-5.md

Resultado: confirma que la línea eliminada contenía la nota del desfase horario, restituida en el commit `dbc5d1e`.

### Commits
- `dbc5d1e` — `docs(A4): restituir nota de desfase horario borrada en 037f995`

### Limitaciones
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

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Macías Herrera Josthyn Esteban
**Dependencias:** Ninguna

### Problema detectado
Los resultados actuales (modelo_ordinal_mixto.csv y archivos de acuerdo en 07_Datos/resultados/; 06_Experimento/readme.md líneas 26 y 125) se presentan como hallazgo, y desviaciones.md (línea 76) afirma que no se incorporaron observaciones fabricadas. La fiabilidad real es alfa entre -0,015 y 0,027 e ICC(2,1) entre 0,09 y 0,12; con 25 por grupo el efecto mínimo detectable es d aprox. 0,81.

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] Ningún documento presenta esos resultados como hallazgo
- [ ] Fiabilidad y potencia declaradas, con cifras que salen de un script

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
En ejecución según el plan de ejecución rev. 8. Esta sección se completa con lo que realmente ocurra al cerrar la tarea; no se marca Hecho sin criterio cumplido.

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## B1 — Retranscribir literalmente las entrevistas de las rondas 1 y 2

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,50 pts
**Responsable(s):** Sin asignar (fuera del núcleo de la rev. 8)
**Dependencias:** Acceso a los audios originales

### Problema detectado
Las entrevistas ENTR-01 a 08 tienen 0 % de turnos con muletillas frente a 6-69 % en la ronda 3, contienen glosas editoriales y el consolidado dice que se presentan en el orden solicitado.

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] Marcas [mm:ss]
- [ ] La última marca coincide ±10 % con la duración del audio
- [ ] En muestras de 3 minutos, menos de un 5 % de discrepancia

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
No iniciada. No forma parte del núcleo del plan de ejecución rev. 8: la demanda del núcleo (28 h por persona) supera la capacidad disponible (~17 h por persona). Si no se ejecuta antes del cierre, se declara como no ejecutada por esta causa.

Qué haría falta: Retranscribir literalmente desde el audio ENTR-01 a 08 con marcas de tiempo; requiere acceso a los audios originales.

### Evidencia entregada fuera del repositorio
No aplica todavía.

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

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Sin asignar (fuera del núcleo de la rev. 8)
**Dependencias:** Ninguna

### Problema detectado
ENTR-02, 04, 09, 12, 13 y 15 tienen perfiles distintos en el consentimiento, la transcripción, curva_saturacion.py (líneas 71-82) y las actas.

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] Los mismos perfiles en todas las fuentes, comprobado por script

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
No iniciada. No forma parte del núcleo del plan de ejecución rev. 8: la demanda del núcleo (28 h por persona) supera la capacidad disponible (~17 h por persona). Si no se ejecuta antes del cierre, se declara como no ejecutada por esta causa.

Qué haría falta: Tabla maestra con un solo perfil por persona y script que la compare con las cuatro fuentes.

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## B4 — Matriz de cobertura pregunta por entrevista

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,30 pts
**Responsable(s):** Sin asignar (fuera del núcleo de la rev. 8)
**Dependencias:** B1

### Problema detectado
La guía (A02_Instrumentos_Recoleccion.pdf, creada el 30/07) es posterior a las rondas 1 y 2; las preguntas 3 y 7 no se formularon; la IA solo se preguntó en 4 de 16 entrevistas; en ENTR-01 (línea 65) el entrevistador propone el análisis de imagen.

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] Matriz 13 x 16 con cita por celda
- [ ] Limitaciones declaradas

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
No iniciada. No forma parte del núcleo del plan de ejecución rev. 8: la demanda del núcleo (28 h por persona) supera la capacidad disponible (~17 h por persona). Si no se ejecuta antes del cierre, se declara como no ejecutada por esta causa.

Qué haría falta: Construir la matriz con cita literal por celda y declarar las limitaciones.

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## B5 — Tabla de hora de inicio, fin y duración real de cada entrevista

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Sin asignar (fuera del núcleo de la rev. 8)
**Dependencias:** Acceso a los archivos originales

### Problema detectado
La guía, el consentimiento y la adenda declaran duraciones distintas; ENTR-03 tiene 7 vídeos y 368 palabras; ENTR-05 tiene 60 palabras del participante.

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] Duraciones verificables contra los archivos
- [ ] Bitácora sin N/D

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
No iniciada. No forma parte del núcleo del plan de ejecución rev. 8: la demanda del núcleo (28 h por persona) supera la capacidad disponible (~17 h por persona). Si no se ejecuta antes del cierre, se declara como no ejecutada por esta causa.

Qué haría falta: Tabla con hora de inicio, fin y duración real verificada contra los archivos.

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## C1 — Cita literal por fragmento y libro de códigos versionado

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,50 pts
**Responsable(s):** Sin asignar (fuera del núcleo de la rev. 8)
**Dependencias:** B3

### Problema detectado
Solo 2 de 227 fragmentos de codificacion.csv y codificacion_tercera_ronda.csv son citas literales, y no hay libro de códigos versionado.

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] Un script comprueba que el 100 % de las citas aparece literal en su transcripción
- [ ] El 100 % de los 79 códigos tiene definición

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
No iniciada. No forma parte del núcleo del plan de ejecución rev. 8: la demanda del núcleo (28 h por persona) supera la capacidad disponible (~17 h por persona). Si no se ejecuta antes del cierre, se declara como no ejecutada por esta causa.

Qué haría falta: Añadir columna de cita literal con número de línea y versionar un libro de códigos con definición e inclusión/exclusión. Es el inicio de la cadena C1 a C3, que no cabe en el plazo.

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## C2 — Reasignar fragmentos cruzados entre ENTR-05 y ENTR-06

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Sin asignar (fuera del núcleo de la rev. 8)
**Dependencias:** C1

### Problema detectado
Hay fragmentos cruzados entre ENTR-05 y ENTR-06 (líneas 88-92, 95, 99 y 103) y etiquetas que no corresponden (ESTACIONALIDAD_PLAGA en 56 y 105, RASTREO_GPS en 60, EVIDENCIA_FOTOGRAFICA en 91 y 106).

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] Ningún fragmento tiene mejor respaldo en otra entrevista

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
No iniciada. No forma parte del núcleo del plan de ejecución rev. 8: la demanda del núcleo (28 h por persona) supera la capacidad disponible (~17 h por persona). Si no se ejecuta antes del cierre, se declara como no ejecutada por esta causa.

Qué haría falta: Reasignar los fragmentos y recodificar las etiquetas indicadas.

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## C3 — Doble codificación real

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,50 pts
**Responsable(s):** Sin asignar (fuera del núcleo de la rev. 8)
**Dependencias:** C1, C2

### Problema detectado
El archivo del segundo codificador (2001ace) es idéntico byte a byte al del primero (011283c) salvo el BOM, y después una sola cuenta reescribió ambos (e91287a, a0dbabb).

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] Commit del libro de códigos anterior a los dos archivos
- [ ] Autores de git distintos
- [ ] Ningún archivo modificado por una cuenta ajena
- [ ] Kappa por script y tabla de desacuerdos

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
No iniciada. No forma parte del núcleo del plan de ejecución rev. 8: la demanda del núcleo (28 h por persona) supera la capacidad disponible (~17 h por persona). Si no se ejecuta antes del cierre, se declara como no ejecutada por esta causa.

Qué haría falta: Con el libro versionado, al menos el 20 % de los fragmentos elegidos al azar con semilla declarada, cada codificador subiendo su archivo desde su propia cuenta sin ver el del otro.

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## C4 — Saturación con sensibilidad al orden

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Sin asignar (fuera del núcleo de la rev. 8)
**Dependencias:** C1

### Problema detectado
Con orden aleatorio la última entrevista aporta de media 4,7 códigos nuevos en la ronda de dominio. Codificacion_Tematica/readme.md (línea 3) dice 8 entrevistas.

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] Media y probabilidad de cero códigos nuevos en la última posición, por script

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
No iniciada. No forma parte del núcleo del plan de ejecución rev. 8: la demanda del núcleo (28 h por persona) supera la capacidad disponible (~17 h por persona). Si no se ejecuta antes del cierre, se declara como no ejecutada por esta causa.

Qué haría falta: Permutaciones en cada ronda con criterio declarado, y corregir la línea 3 del readme.

### Evidencia entregada fuera del repositorio
No aplica todavía.

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

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,40 pts
**Responsable(s):** Sin asignar (fuera del núcleo de la rev. 8)
**Dependencias:** Ninguna

### Problema detectado
RF-03, 07, 08 y 18 ya estaban en la propuesta del 05/05, antes de la primera entrevista (23/05); RF-36 y EV-13 aparecen el 02/08 con una evidencia fechada del 03 al 07/08; RF-40 a 42 y los requisitos de IA aparecen el 31/08 sin entrevista.

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] 100 % de RF, RNF y requisitos de IA clasificados
- [ ] Ningún requisito anterior a su evidencia sin declararlo

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
No iniciada. No forma parte del núcleo del plan de ejecución rev. 8: la demanda del núcleo (28 h por persona) supera la capacidad disponible (~17 h por persona). Si no se ejecuta antes del cierre, se declara como no ejecutada por esta causa.

Qué haría falta: Tabla con clasificación (elicitado, propuesta del equipo, normativo o derivado), fecha de la fuente y commit de alta de cada requisito.

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## D2 — Corregir la cita atribuida a EV-01 y verificar las citas del ERS

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Sin asignar (fuera del núcleo de la rev. 8)
**Dependencias:** Ninguna

### Problema detectado
La cita atribuida a EV-01 en ERS_SRS_2B_v2.0.tex (línea 1132) son palabras del entrevistador en ENTR-02 (línea 77).

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] 100 % de las citas literales, con la entrevista correcta y en boca del entrevistado

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
No iniciada. No forma parte del núcleo del plan de ejecución rev. 8: la demanda del núcleo (28 h por persona) supera la capacidad disponible (~17 h por persona). Si no se ejecuta antes del cierre, se declara como no ejecutada por esta causa.

Qué haría falta: Corregir la cita y añadir un script que busque cada cita del ERS en las transcripciones.

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## D3 — Umbrales y duplicados en los requisitos de IA

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Sin asignar (fuera del núcleo de la rev. 8)
**Dependencias:** D1

### Problema detectado
RF-07 y RF-08 (líneas 973-988) no fijan umbrales; hay duplicados con umbral distinto (RNF-01 frente a RNF-IA-08; RNF-02 frente a RNF-IA-01); algunos requisitos dependen de datos que no existen (L-05).

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] Ningún par vigente con la misma métrica y distinto umbral

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
No iniciada. No forma parte del núcleo del plan de ejecución rev. 8: la demanda del núcleo (28 h por persona) supera la capacidad disponible (~17 h por persona). Si no se ejecuta antes del cierre, se declara como no ejecutada por esta causa.

Qué haría falta: Fijar umbrales, eliminar duplicados y marcar como no verificable hasta disponer de conjunto de evaluación lo que dependa de datos inexistentes.

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## D4 — Casos de prueba definidos y ejecutados

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,30 pts
**Responsable(s):** Sin asignar (fuera del núcleo de la rev. 8)
**Dependencias:** E1

### Problema detectado
Los 68 CP de la matriz son solo identificadores (en 40 filas copian el número del RF y en 25 el de la fila).

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] Cada CP Must especificado (pasos, dato, resultado esperado) y con resultado Pasa/Falla y evidencia

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
No iniciada. No forma parte del núcleo del plan de ejecución rev. 8: la demanda del núcleo (28 h por persona) supera la capacidad disponible (~17 h por persona). Si no se ejecuta antes del cierre, se declara como no ejecutada por esta causa.

Qué haría falta: Definir cada CP de los RF Must y registrar ejecuciones reales con evidencia.

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## D5 — Corregir matriz_e2e.xlsx

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Sin asignar (fuera del núcleo de la rev. 8)
**Dependencias:** D4

### Problema detectado
matriz_e2e.xlsx cubre 68 de 89 identificadores (76 %), tiene duplicados (RF-04, 07, 08, 12, 21), 36 filas sin historia, hojas Diagnostico y Sincronizacion sin calcular, restos de LaTeX (filas 56 a 61) y el título v1.1.

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] La hoja abre sin fórmulas vacías y coincide con la matriz

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
No iniciada. No forma parte del núcleo del plan de ejecución rev. 8: la demanda del núcleo (28 h por persona) supera la capacidad disponible (~17 h por persona). Si no se ejecuta antes del cierre, se declara como no ejecutada por esta causa.

Qué haría falta: Declarar la cobertura real, quitar duplicados, versionar el script que la generó, calcular las hojas y limpiar los restos.

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## E2 — Recalcular la cobertura de RF Must

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Sin asignar (puede resolverse junto con E1)
**Dependencias:** E1

### Problema detectado
Se declara cobertura de 20/24 RF Must y el código sostiene como mucho 17/24.

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] Cifra reproducible con la lista de RF y la línea de código

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
No iniciada. No forma parte del núcleo del plan de ejecución rev. 8: la demanda del núcleo (28 h por persona) supera la capacidad disponible (~17 h por persona). Si no se ejecuta antes del cierre, se declara como no ejecutada por esta causa.

Qué haría falta: Recalcular la cifra con un script sobre la lista de RF y el código del prototipo.

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## F1 — Notas de campo: retirar o rotular los 16 PDF y rectificar

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,40 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** Firma de la rectificación

### Problema detectado
El 11/09 se declaró por escrito que no existían notas físicas (b59d4ef) y el 12/09 se subieron 16 PDF (1135321) que comparten el mismo bloque de imagen. verificacion_seccion15.md (línea 18) también requiere corrección.

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] Ningún PDF presentado como escaneo contemporáneo
- [ ] Rectificación firmada por el equipo

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
En ejecución según el plan de ejecución rev. 8. Esta sección se completa con lo que realmente ocurra al cerrar la tarea; no se marca Hecho sin criterio cumplido.

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## F2 — Member checking: trazabilidad, evidencia y actas

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,30 pts
**Responsable(s):** Macías Herrera Josthyn Esteban (tabla) · Arboleda Yanza Francisco Javier (evidencia y actas)
**Dependencias:** A7 (inventario) antes de la tabla

### Problema detectado
Los enunciados 1, 8, 9 y 10 salen de ENTR-13, codificada el 07/09, después de la sesión del 04/09, y la síntesis se compiló después de las actas. Existen videos de la sesión según el docente.

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] Actas posteriores al commit de codificación
- [ ] Cada enunciado enlaza a sus códigos y citas
- [ ] Modalidad, hora y firma en cada acta

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
En ejecución según el plan de ejecución rev. 8. Esta sección se completa con lo que realmente ocurra al cerrar la tarea; no se marca Hecho sin criterio cumplido.

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## F3 — Walkthrough: consentimientos firmados después de la sesión

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Sin asignar (fuera del núcleo de la rev. 8)
**Dependencias:** Ninguna

### Problema detectado
Los consentimientos de WT-04 y WT-06 se firmaron después de la sesión; falta la fecha de WT-06 y su perfil real, y las actas no están firmadas.

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] Fecha real de firma en cada acta
- [ ] Perfiles coherentes

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
No iniciada. No forma parte del núcleo del plan de ejecución rev. 8: la demanda del núcleo (28 h por persona) supera la capacidad disponible (~17 h por persona). Si no se ejecuta antes del cierre, se declara como no ejecutada por esta causa.

Qué haría falta: Declarar que los consentimientos se firmaron después de la sesión, registrar la fecha real de firma y el perfil de WT-06 y firmar las actas. No se pone en ningún documento una fecha distinta de la real.

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## F4 — Registrar las visitas del 27/06, 02/08 y 21/08

**Estado operativo:** VERIFICADA (discrepancia de fechas documentada) · limitación declarada (pie de foto)
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,10 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** Ninguna

### Problema detectado
Las visitas del 27/06, 02/08 y 21/08 aparecen en fotos y en la constancia,
pero no en la bitácora; el pie de la foto usada como "visita del equipo" e
"Ingenieros de calidad" es incorrecto.

### Acción aplicada
Se contrastaron tres fuentes: `02_Evidencias/Fotos_Entorno/` (fotos de
campo por fecha), `10_Autoria/correspondencia/2026-09-16_Acta_Constancia_
Actividades_Campo_Enmascarada.png` (fechas autorizadas para entrevistas) y
`bitacora_sesiones.csv` (sesiones de trabajo y de entrevista registradas).
El cruce muestra:

| Fecha | Fotos de campo | Constancia (fechas autorizadas) | Bitácora de sesiones |
|---|---|---|---|
| 27/06/2026 | Sí (detección de plagas, evidencia de trabajo, prueba de humedad, vista general) | No aparece | No aparece como sesión presencial (SES-04 de esa fecha es virtual, trabajo de repositorio) |
| 28/07/2026 | Sí (entrevistas, `Ingenieros_De_Calidad_Fruta_Foto.jpeg`, pesaje de fruta) | Sí — "Entrevistas y elicitación de requisitos..." | Sí (SES-28, elicitación ENTR-04 a 08) |
| 02/08/2026 | No se encontró ninguna foto ni archivo con esta fecha | Sí — "Entrevista y levantamiento complementario..." | Sí (SES-10), pero es una sesión virtual de carga al repositorio, no de campo |
| 21/08/2026 | Sí (pre-vivero, vivero de palmas) | No aparece | No aparece ninguna fila con esta fecha |

Solo el 28/07 tiene respaldo consistente en las tres fuentes. Las otras dos
fechas de foto (27/06, 21/08) no están autorizadas en la constancia ni
registradas como sesión presencial, y la fecha autorizada del 02/08 no
tiene ningún respaldo fotográfico ni documental de que la actividad haya
ocurrido.

Sobre el pie de foto: se buscó en todo el repositorio la frase "visita del
equipo" y no se encontró en ningún archivo. La foto
`2026-07-28_Ingenieros_De_Calidad_Fruta_Foto.jpeg` sí existe y su fecha de
archivo es coherente con la constancia; no se localizó ningún documento
que la use con un pie de foto distinto o incorrecto.

### Evidencia utilizada
- `02_Evidencias/Fotos_Entorno/` — nombres de archivo con fecha (2026-06-27_*, 2026-07-28_*, 2026-08-21_*)
- `10_Autoria/correspondencia/2026-09-16_Acta_Constancia_Actividades_Campo_Enmascarada.png`, tabla "Fechas autorizadas para entrevistas y actividades de elicitación"
- `bitacora_sesiones.csv`, filas SES-04, SES-10, SES-28
- Búsqueda de texto completo del repositorio por "visita del equipo": sin resultados
- Búsqueda de texto completo del repositorio por "Ingenieros_De_Calidad" / "Ingenieros de calidad": solo el nombre del archivo de la foto, sin otro documento que la referencie

### Archivos modificados
- `07_Datos/registro_correcciones.md` (esta entrada)

### Criterio de aceptación
- [x] Bitácora y fotos contrastadas — discrepancia real documentada, no forzada a cuadrar
- [ ] Pie de foto incorrecto — no localizado en el estado actual del repositorio; se declara como no encontrado

### Verificación
Comparación manual de fechas entre las tres fuentes listadas arriba,
reproducible abriendo cada archivo referenciado.

### Commits
- `8cd23f0` — `docs(F4): documentar discrepancia de fechas entre fotos, constancia y bitacora`

### Limitaciones
No existe una bitácora de visitas de campo separada de `bitacora_sesiones.csv`
(que registra sesiones de Git y de entrevista, no visitas generales). Las
fechas 27/06 y 21/08 tienen evidencia fotográfica de actividad de campo
pero ningún documento formal que las autorice o las declare como visita
oficial; la fecha 02/08, autorizada en la constancia, no tiene evidencia
fotográfica ni documental de que haya ocurrido. El pie de foto incorrecto
que señala el plan del docente no se pudo localizar en el repositorio
actual; puede haberse corregido en una ronda anterior o encontrarse en un
documento externo (por ejemplo, el guion de exposición oral) no incluido
en el repositorio.

### Evidencia entregada fuera del repositorio
No aplica.

---

## G2 — Estado real de la acreditación y la aprobación ética

**Estado operativo:** EN PROCESO
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** respuesta del docente sobre la existencia de dictamen

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
- [ ] Dictamen con número y fecha, o declaración explícita de ausencia
      — pendiente de la respuesta del docente

### Verificación
Comando:

    grep -n "A.12" 09_Etica/README_Etica.md

Resultado:

    [pegar la salida real]

### Commits
- `<SHA>` — `docs(G2): precisar estado real de la acreditacion etica A12`

### Limitaciones
El criterio pide dictamen con número y fecha o declaración explícita. A la
fecha de este registro la declaración es parcial: se precisa el estado de la
acreditación de formación, pero la existencia o no de dictamen de comité queda
sujeta a la respuesta del docente, solicitada el 19/09/2026.

Las líneas 49 y 96 de `A14_Adenda_Tercera_Ronda.tex`, que se refieren al
«protocolo aprobado», no se han modificado a la espera de esa misma respuesta.

### Evidencia entregada fuera del repositorio
Consulta al docente por correo institucional — 19/09/2026.

---

## G3 — Matriz uso por consentimiento de cada participante

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,30 pts
**Responsable(s):** Sin asignar (entra si aparece tiempo extra)
**Dependencias:** B3

### Problema detectado
El formulario de ENTR-01 a 03 no cubre grabación ni los usos posteriores; en el cuestionario, 57 de 62 respuestas no tienen consentimiento. Los videos del member checking introducen además el uso vídeo.

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] Cada uso de cada participante (audio, vídeo, foto, repositorio abierto, envío a un LLM externo) con autorización o retirado

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
No iniciada. No forma parte del núcleo del plan de ejecución rev. 8: la demanda del núcleo (28 h por persona) supera la capacidad disponible (~17 h por persona). Si no se ejecuta antes del cierre, se declara como no ejecutada por esta causa.

Qué haría falta: Matriz por participante y renovación del consentimiento o retiro de los usos no cubiertos. Su ausencia impide declarar congelación definitiva de la evidencia (G5).

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## G4 — Aval de la organización firmado o ausencia declarada

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Arboleda Yanza Francisco Javier
**Dependencias:** Ninguna

### Problema detectado
El aval actual es una carta compuesta por el equipo, sin fecha ni firma; la constancia se firmó el 16/09 y enumera el 02/08, día sin entrevistas; no hay autorización de Extractora R para ENTR-04 y 08.

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] Avales firmados de ambas organizaciones o ausencia declarada

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
En ejecución según el plan de ejecución rev. 8. Esta sección se completa con lo que realmente ocurra al cerrar la tarea; no se marca Hecho sin criterio cumplido.

### Evidencia entregada fuera del repositorio
No aplica todavía.

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

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Sin asignar (fuera del núcleo de la rev. 8)
**Dependencias:** Ninguna

### Problema detectado
Respuestas/readme.md (líneas 8, 14-15, 47 y 61) no coincide con el archivo: la exportación es de Microsoft Forms, tiene 15 ítems (no 16) y no guarda nombre ni correo; hay 4 respuestas del 30/06 sin explicar y el modo de aplicación (mediana de 42,5 s; 38 de 61 respuestas empiezan 0-10 s después de terminar la anterior) no está declarado.

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] Texto coherente con el archivo
- [ ] Análisis de sensibilidad con n = 58

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
No iniciada. No forma parte del núcleo del plan de ejecución rev. 8: la demanda del núcleo (28 h por persona) supera la capacidad disponible (~17 h por persona). Si no se ejecuta antes del cierre, se declara como no ejecutada por esta causa.

Qué haría falta: Corregir el readme, explicar las 4 respuestas del 30/06 y el modo de aplicación, y ejecutar el análisis de sensibilidad con n = 58.

### Evidencia entregada fuera del repositorio
No aplica todavía.

---

## H2 — Aclarar las fotos del cuestionario

**Estado operativo:** EN PROCESO
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
- [ ] Nombres y mensajes coherentes con el contenido (la carpeta conserva el nombre `Fotos_Aplicacion` y la línea 357 del ERS aún dice "aplicación real del cuestionario"; se corrige en I1)

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
El nombre de la carpeta `Fotos_Aplicacion` y la línea 357 de `ERS_SRS_2B_v2.0.tex` siguen hablando de aplicación; el ERS se corrige en I1. Los mensajes de los commits `34ce578` y `0792213` no pueden modificarse.

### Evidencia entregada fuera del repositorio
No aplica.
---

## I1 — Coherencia documental

**Estado operativo:** NO INICIADA
**Estado de rúbrica:** pendiente de mapeo
**Peso:** 0,20 pts
**Responsable(s):** Macías Herrera Josthyn Esteban (verificación) · Arboleda Yanza Francisco Javier (redacción)
**Dependencias:** Todas las correcciones sustantivas y G5

### Problema detectado
El relato sobre la reescritura del historial difiere entre CHANGELOG.md (320-330) y README_Etica.md (116-128); CITATION.cff dice 8 entrevistas; el ERS tiene la cabecera v3.0 (línea 74); apendices.tex (232 y 350-362) está obsoleto; la fecha de EV-07 (28/07) y el estado pendiente del depósito de datos no coinciden; las fechas y herramientas de la declaración de uso de IA (líneas 21 y 31) están desactualizadas.

### Acción aplicada
Ninguna todavía.

### Evidencia utilizada
- Ninguna todavía.

### Archivos modificados
- Ninguno todavía.

### Criterio de aceptación
- [ ] git grep sin contradicciones en esos puntos

### Verificación
Aún no ejecutada.

### Commits
- Ninguno todavía.

### Limitaciones
En ejecución según el plan de ejecución rev. 8. Esta sección se completa con lo que realmente ocurra al cerrar la tarea; no se marca Hecho sin criterio cumplido.

### Evidencia entregada fuera del repositorio
No aplica todavía.
