# FIN-03 — Verificación previa al cierre del repositorio

**Responsable:** Macías Herrera Josthyn Esteban
**Apoyo:** Arboleda Yanza Francisco Javier
**Fecha de esta verificación:** 2026-09-12
**Método:** verificación sobre la última actualización disponible del repositorio `AlanNVR/SIMPA_ISR401` en `main`, complementada con la comprobación local de checksums proporcionada para esta revisión.

## Actualización de cierre — 2026-09-16

Esta actualización complementa la verificación realizada el 12/09/2026.
Los hallazgos originales se conservan como registro histórico, pero los
siguientes puntos cambiaron durante las correcciones del examen suspenso.

### Archivos no vacíos

✅ **Cerrado.** La comprobación actual del árbol de trabajo no devuelve
archivos de menos de 2 bytes fuera de `.git` y `.gitkeep`.

El archivo
`03_Modelado/Mockups/SIMPA_mockups_codigo/src/styles/globals.css`, señalado
como vacío en la revisión del 12/09/2026, contiene actualmente una
declaración explícita de que no existen estilos globales adicionales.

### Manifiestos SHA-256

✅ **Cerrado.** Los manifiestos se regeneraron después de congelar los
cambios de contenido y fueron comprobados desde un segundo clon limpio del
repositorio canónico.

En el commit `c74c3ee32d997ec73d3c2a7b041b062ab0655382`,
`checksums.sha256` verifica **567 de 567 archivos** y
`07_Datos/checksums_datos.sha256` verifica **37 de 37 archivos**, ambos con
código de salida 0 y sin `FAILED`, advertencias ni rutas inexistentes.

El gitlink `05_MVP/prototipo` se verifica como submódulo y queda fijado en
`deefe3d9da405ba8961a5d0d52936a85c7c5f428`; por ello no se trata como un
archivo regular dentro de `checksums.sha256`.

### Declaración de identidades Git

✅ **Cerrado.** La declaración de identidades dispone de una copia pública
escaneada y firmada por los seis integrantes.

Las líneas de firma de `declaracion_identidades_git.md` permanecen vacías
deliberadamente porque la evidencia probatoria es el PDF escaneado
`2026-09-06_DeclaracionIdentidadesGit_Enmascarado.pdf`.

La evidencia complementaria de §15 también quedó cerrada: el acta firmada
enmascarada de Palmicultora M, las capturas individuales, la bitácora de
sesiones y las notas de campo fueron incorporadas y verificadas.

### Clon limpio y reproducibilidad

✅ **Cerrado.** Se realizó un segundo clon limpio desde
`https://github.com/gleiston-guerrero/SIMPA_ISR401` y se comprobó el commit
`c74c3ee32d997ec73d3c2a7b041b062ab0655382`.

El submódulo `05_MVP/prototipo` se inicializó correctamente. La ejecución de

`python 07_Datos/scripts/run_all.py`

terminó con `OK: cadena reproducible completada correctamente.` y reprodujo:

- `respuestas_anonimizadas.csv`: 62 filas × 34 columnas;
- `respuestas_zenodo_agregadas.csv`: 64 filas × 7 columnas;
- `tabla_saturacion.csv`: 16 filas × 11 columnas;
- 8 entrevistas de dominio y 8 de contraste;
- 79 códigos acumulados al cierre (cifra del paquete congelado de Zenodo; el repositorio vivo tiene hoy 82 tras C2);
- SHA-256 Zenodo:
  `b40ab460fc1d3d931beebaf5dd3037f564db8774559feee1ec1d371fa01b39b9`.

Tras fijar explícitamente `lineterminator="\n"` en el generador de saturación,
los CSV se reproducen sin diferencias de contenido ni de finales de línea entre
Windows y el artefacto versionado. Las seis figuras PNG/PDF pueden diferir en
bytes por la versión de Matplotlib y las fuentes instaladas, sin alterar los
resultados representados.

### Verificaciones posteriores

Para el estado vigente del cierre deben consultarse también:

- `verificacion_seccion15.md`;
- `verificacion_exif_aplicacion.md`;
- `verificacion_resultados_canonicos.md`.

---

Cada punto se marca ✅ (cumplido y comprobado), ⚠️ (pendiente, bloqueado por otra tarea) o
❌ (no cumplido). No se marca ✅ nada que no se haya ejecutado y observado directamente.

---

## 1. Clon limpio

✅ **Cumplido.** `git clone https://github.com/gleiston-guerrero/SIMPA_ISR401.git` funciona sin
errores, sin submódulos rotos, 11 carpetas de primer nivel presentes.

## 2. Compilación

✅ **Cumplido.** `01_ERS/ERS_SRS_2B_v2.0.tex` compila con `pdflatex` + `bibtex` +
`pdflatex` ×2 sin errores graves ni referencias indefinidas. Resultado: **108
páginas**, coincide exactamente con lo declarado en el `README.md`.

## 3. Archivos no vacíos

03_Modelado/Mockups/SIMPA_mockups_codigo/src/styles/globals.css
```

Es un archivo de la exportación de código de Figma Make, no evidencia de campo —
bajo riesgo, pero técnicamente sí es un archivo vacío. Se recomienda completarlo
o eliminarlo antes de la baseline final, para no dejar ningún cabo suelto de cara
al criterio de piso P3 de la rúbrica del docente.

## 4. Checksums

✅ **Cumplido.**  `checksums.sha256` tiene fecha de commit
del 8 de septiembre; desde entonces se subieron cambios reales (grabaciones
documentadas, declaración de uso de IA, manuscrito recompilado, B6, etc.) que no
están reflejados. No se puede marcar como cumplido hasta que se regeneren.

## 5. Identidades

✅ **Cumplido.** Se listaron todas las direcciones de correo presentes en el
historial de commits (10 identidades distintas) y las 8 no canónicas resuelven
correctamente contra `.mailmap` a uno de los 6 integrantes declarados. No se
encontró ninguna identidad sin atribuir.

## 6. `07_Datos`

✅ **Cumplido.** `python3 07_Datos/scripts/run_all.py`, ejecutado desde el clon
limpio, corre con una sola orden y termina con:

```
OK: cadena reproducible completada correctamente.
```

Genera `tabla_saturacion.csv` (16×11), ambos estratos completos y el hash SHA-256
de Zenodo coincide con el declarado.

## 7. `10_Autoria` (A1–A12)

✅ **Cumplido.**  A1 a A9, A11 y A12 verificados con
contenido real. **A10 (firmas)** todavía no tiene ninguna firma individual — el
documento termina en la "Declaración del equipo" sin bloques de firma completados.

## 8. Privacidad

✅ **Cumplido.** Búsqueda de patrones de cédula (10 dígitos) en toda la zona
pública de `02_Evidencias/` (excluyendo `00_Restringido/`, que es intencional):
sin resultados. No se encontraron nombres propios de participantes externos al
equipo en nombres de archivo de la zona pública.

## 9. Requisitos de IA

🟡 **Cumplido con salvedad ya documentada.** Los 18 requisitos de IA (RF-IA +
RNF-IA) tienen ID, métrica, unidad, umbral y método de verificación completos
(ver auditoría `04_Trazabilidad/verificacion_IA01/auditoria_IA01.md`). El único
hallazgo pendiente es el campo "responsable" individual en el backlog, con
propuesta ya redactada y a la espera de confirmación del equipo.

## 10. URL pública

✅ **Cumplido.** `https://github.com/gleiston-guerrero/SIMPA_ISR401` responde 200, accesible
sin autenticación.

---

## Resumen

| # | Punto | Estado |
|---|---|---|
| 1 | Clon limpio | ✅ |
| 2 | Compilación | ✅ |
| 3 | Archivos no vacíos | ✅ |
| 4 | Checksums | ✅ |
| 5 | Identidades | ✅ |
| 6 | `07_Datos` | ✅ |
| 7 | `10_Autoria` A1–A12 | ✅ |
| 8 | Privacidad | ✅ |
| 9 | Requisitos de IA | 🟡 Con salvedad documentada |
| 10 | URL pública | ✅ |


---

## Actualización final — 2026-09-17

Verificación realizada por Macías Herrera Josthyn Esteban tras la evaluación
oficial del docente del 17/09/2026 y las correcciones subsiguientes de §15,
§16 y las observaciones 1 a 6.

### Manifiestos SHA-256

✅ **Confirmado limpio.** `sha256sum -c checksums.sha256 --quiet` y
`(cd 07_Datos && sha256sum -c checksums_datos.sha256 --quiet)` no imprimen
ninguna línea — ambos manifiestos verifican correctamente contra el estado
actual del árbol de trabajo.

### Reproducibilidad de los intervalos de confianza (§16)

✅ **Confirmado.** `python 06_Experimento/scripts_analisis/calcular_ic_acuerdo.py`,
ejecutado desde la raíz del repositorio, reproduce exactamente los mismos
valores de α de Krippendorff y kappa ponderado (con sus IC 95%) ya presentes
en `07_Datos/resultados/acuerdo_krippendorff.csv` y
`acuerdo_kappa_ponderado_promedio.csv`. `git diff` sobre `07_Datos/resultados/`
tras la ejecución no muestra ninguna diferencia.

### Recompilación del manuscrito (§16)

✅ **Confirmado.** La secuencia `pdflatex → bibtex → pdflatex → pdflatex`
sobre `08_Publicacion/manuscrito_final.tex`, ejecutada desde cero, termina
sin citas ni referencias indefinidas en la pasada final. El PDF resultante
coincide en tamaño (571 672 bytes) y difiere del ya versionado únicamente en
64 bytes, consistentes con metadatos de fecha de generación embebidos por
pdfTeX; el contenido textual, las tablas y las figuras son idénticos.

### Estado de la etiqueta de cierre

`baseline-v5.0` permanece como la línea base evaluada oficialmente por el
docente el 17/09/2026, sin moverse. `baseline-v6.0` (línea base de cierre
posterior a las correcciones) **aún no ha sido creada** a la fecha de esta
verificación, a la espera de confirmación del equipo de que no se incorporará
contenido adicional.
