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
en los documentos éticos A01, A05, A06, A07, A09, A12, C1 y C2.

### Acción aplicada
Capa automatizada (Macías): extracción de texto de los 8 documentos
éticos señalados por el plan, búsqueda de patrones de cédula (10 dígitos)
y RUC (13 dígitos) mediante script versionado. Se detectaron 61
ocurrencias reales. Adicionalmente ya se había enmascarado el nombre de
la organización en CHANGELOG.md y en A03, y 2 capturas de WhatsApp.

Capa visual (Arboleda): pendiente — revisión página por página de cada
PDF afectado y de las capturas/fotos, incluyendo verificación del
tatuaje identificable en la Foto 01 del consentimiento complementario y
en Fotos_Aplicacion/.

Avance capa visual (Arboleda): A01 (commit 2bae024), A05 (commit 9fd0fd6), A06 (commit 0351872), A07 (commit 4e9c742), A09 (commit 787d7d5), A12 (commit ae5b00c) y C1 (commit 651d21c) enmascarados y reemplazados.
Pendiente revisar C2 y la Foto 01; solo se modifican los que contengan cédula, RUC, teléfono o el nombre real de la organización.

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


### Criterio de aceptación
- [x] Capa automatizada ejecutada y commiteada con salida real
- [ ] Capa visual ejecutada, checklist por archivo commiteada
- [ ] Los 61 identificadores detectados quedan enmascarados en los 8 PDF
- [ ] Tatuaje revisado
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

### Limitaciones
Los 8 PDF no tienen fuente LaTeX en el repositorio, así que la redacción
real (retirar el texto, no solo cubrirlo visualmente) requiere el
documento fuente original o una herramienta de redacción de PDF —
pendiente de confirmar con Allan/Denisses si existe el .docx/.tex
original. La capa visual (tatuaje, capturas) sigue pendiente de
Arboleda. G1b (historial) permanece bloqueada sin autorización escrita
del docente.

### Evidencia entregada fuera del repositorio
No aplica todavía.
