# Registro de correcciones

Cada entrada corresponde a una de las 39 tareas oficiales del Plan de
mejora de datos (19/09/2026). El campo **Estado de rúbrica** se deja en
*pendiente de mapeo* hasta que el docente aclare la diferencia práctica
entre *Por modificar* y *Por culminar*.

---

## G1 — Datos personales

**Estado operativo:** EN PROCESO
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
Capa automatizada (Macías): extracción de texto de los 8 documentos
éticos señalados por el plan, búsqueda de patrones de cédula (10 dígitos)
y RUC (13 dígitos) mediante script versionado. Se detectaron 61
ocurrencias reales. Adicionalmente ya se había enmascarado el nombre de
la organización en CHANGELOG.md y en A03, y 2 capturas de WhatsApp.

Capa visual (Arboleda): revisión página por página y enmascarado de los 14 PDF de 09_Etica/ que contenían cédula o RUC (A01, A02, A04, A05, A06, A07, A09, A10, A11, A12, C1, C2, C3 y C4): los números se cubrieron con cajas negras y el texto original se eliminó del archivo, sin escribir texto nuevo. Además se enmascaró el nombre de la organización en A03, en CHANGELOG.md y en las 2 capturas de WhatsApp, y el tatuaje en la Foto 01 del consentimiento complementario. Pendiente: G1b (historial).

Avance capa visual (Arboleda): A01 (commit 2bae024), A05 (commit 9fd0fd6), A06 (commit 0351872), A07 (commit 4e9c742), A09 (commit 787d7d5), A12 (commit ae5b00c), C1 (commit 651d21c), C2 (commit 2b692a5), Foto 01 (commit e837e32), A02 (commit 89da033), A04 (commit d4c1fea), A10 (commit 17bb6ae), A11 (commit ba3e491), C3 (commit 8817784) y C4 (commit 3cde34c) enmascarados y reemplazados. Pendiente: G1b (historial).

### Evidencia utilizada
- Archivo: los 8 PDF de 09_Etica/ listados arriba
- Fuente: texto extraído con pdftotext -layout
- Persona: Macías (ejecución del script)
- Fecha: 2026-09-19
- Consentimiento: no aplica (detección, no publicación de dato)

### Archivos modificados
- `CHANGELOG.md` (commit baee71b)
- `09_Etica/A03...` punto 4 (commit 778ab60)
- `10_Autoria/correspondencia/2026-07-27_WhatsApp_...png` (commit d355638)
- `02_Evidencias/Documentos_Organizacion/2026-07-27_WhatsApp_...png` (commit d6a9434)
- `07_Datos/scripts/plan_mejora/buscar_cedulas_ruc.py` (nuevo)
- `07_Datos/resultados/g1a_deteccion_cedulas_ruc.txt` (nuevo)
- `09_Etica/A01_Protocolo_Investigacion.pdf` (commit 2bae024)
- `09_Etica/A05_Aval_Institucional.pdf` (commit 9fd0fd6)
- `09_Etica/A06_Declaracion_Conflicto_Intereses.pdf` (commit 0351872)
- `09_Etica/A07_Compromiso_Confidencialidad.pdf` (commit 4e9c742)
- `09_Etica/A09_Nomina_Equipo.pdf` (commit 787d7d5)
- `09_Etica/A12_Certificado_Etica.pdf` (commit ae5b00c)
- `09_Etica/Categoria_C/C1_Aval_Unidad_Productiva.pdf` (commit 651d21c)
- `09_Etica/Categoria_C/C2_Compromiso_Confidencialidad_Estrategica.pdf` (commit 2b692a5)
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
- [ ] Los 61 identificadores detectados quedan enmascarados en los 8 PDF
- [x] Tatuaje revisado
- [ ] G1b (historial) — bloqueada, requiere autorización escrita del docente

### Verificación
Comando:

    python3 07_Datos/scripts/plan_mejora/buscar_cedulas_ruc.py

Resultado:

    TOTAL de ocurrencias detectadas: 61
    (ver 07_Datos/resultados/g1a_deteccion_cedulas_ruc.txt para el detalle completo)

### Commits
- `baee71b` — nombre de organización retirado de CHANGELOG.md
- `778ab60` — nombre de organización enmascarado en A03
- `d355638`, `d6a9434` — capturas de WhatsApp enmascaradas
- `<pendiente>` — docs(G1): agregar script y salida de deteccion de cedulas/RUC
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

### Limitaciones
Los PDF no tienen fuente LaTeX en el repositorio, así que se enmascararon sobre la versión publicada: los números se cubrieron con cajas negras y el texto original se eliminó del archivo (la extracción de texto ya no los devuelve). Los originales firmados se conservan sin cambios fuera del repositorio público. G1b (historial): las cédulas, el RUC y el nombre real siguen en versiones anteriores del historial de git y solo pueden retirarse con autorización escrita del docente; hasta entonces permanecen accesibles.

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
- [ ] `Original` conserva la respuesta anterior sin la adenda
- [x] La API pública expone la respuesta actualizada
- [x] Se preservó el contenido histórico del registro original

### Limitaciones

La acción externa en OSF fue ejecutada por Villafuerte Rosero Allan Noé, por
ser quien dispone del acceso administrativo al registro. Macías Herrera
Josthyn Esteban realizó la documentación, la incorporación de evidencias y el
commit en el repositorio.

Al cierre de esta entrada no se dispone de la captura de la vista `Original`,
por lo que ese criterio queda sin acreditar. El estado de rúbrica corresponde
al docente.

### Commits

Ver el commit cuyo mensaje es `docs(A5): registrar adenda OSF y verificacion API`.