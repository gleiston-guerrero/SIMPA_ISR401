# D4 — Casos de prueba de los RF "Must"

**Prepara:** Claude (a partir de `07_Datos/datos_procesados/cobertura_rf_must_E2.csv` y el código del prototipo) · **Ejecuta:** Arboleda Yanza Francisco Javier
**Entorno:** https://simpa-v3-prototipo.netlify.app/ · **Fecha de ejecución:** 21/09/2026

> Esta tarea no depende de nadie más: se prueba sobre el prototipo ya desplegado, sin tocar código ni el submódulo. No interfiere con A1 (evaluadores) ni con nada que estén subiendo otros compañeros.

Cinco RF Must ya se probaron en la tarea E1 y no se repiten aquí: **RF-01, RF-22, RF-40, RF-41, RF-42** (ver `05_MVP/evidencia_e2e/registro_prueba_e2e.md`).

Quedan **19 por probar**: 18 declarados en pantalla y 1 con solo indicio (RF-05). Se entró como **Administrador** (`admin` / `admin123`), en una sola ventana de incógnito.

---

## 1. Plantaciones y lotes

### RF-02 · Gestión de plantaciones y lotes
**Resultado observado:** Se creó el lote correctamente y la información en el detalle se visualiza correctamente sin errores.
**¿Cumple?** Sí

### RF-10 · Gestión de variedades de palma
**Resultado observado:** Permite seleccionar entre dos tipos de variedades de palma predefinidas en la lista, pero no permite la escritura directa de un nuevo texto.
**¿Cumple?** Parcial

---

## 2. Personal, equipos y cuentas

### RF-03 · Gestión de personal y equipos de trabajo
**Resultado observado:** El nuevo personal registrado aparece correctamente en la tabla con su equipo asignado.
**¿Cumple?** Sí

### RF-35 · Registro delegado para personal sin dispositivo propio
**Resultado observado:** Permite registrar un avance de labor seleccionando y asignándolo a otro trabajador.
**¿Cumple?** Sí

---

## 3. Labores y avance

### RF-04, RF-26, RF-28, RF-36, RF-37
**Resultado observado:** El catálogo incluye código y tarifa. El avance de labor se registra correctamente por unidad y la sección de Reportes procesa y calcula adecuadamente la liquidación semanal del presupuesto contra lo ejecutado.
**¿Cumple?** RF-04 Sí · RF-26 Sí · RF-28 Sí · RF-36 Sí · RF-37 Sí

---

## 4. Mapa GPS y polinización

### RF-13, RF-14, RF-30
**Resultado observado:** Permite el registro de marcación de polinización registrando cantidad de flores y ubicación (RF-13 y RF-14). No existe un botón ni opción disponible para reportar incidencias desde campo con fotografía (RF-30).
**¿Cumple?** RF-13 Sí · RF-14 Sí · RF-30 No

---

## 5. Análisis asistido por IA

### RF-05 · Registro de monitoreo fitosanitario
**Resultado observado:** No se encontró una pantalla, pestaña ni botón separado para "monitoreo fitosanitario". Es el mismo análisis de imagen que ya cubre RF-07 y RF-08.
**¿Cumple?** No diferenciado del análisis de imagen

### RF-07, RF-08, RF-21
**Resultado observado:** Los análisis IA para plagas, deficiencias nutricionales y madurez generan los resultados esperados.
**¿Cumple?** RF-07 Sí · RF-08 Sí · RF-21 Sí

---

## 6. Alertas tempranas

### RF-12 · Generación de alertas tempranas
**Resultado observado:** Las alertas se muestran correctamente filtradas y al hacer clic en "Marcar atendida", su estado cambia adecuadamente en el sistema.
**¿Cumple?** Sí

---

## 7. Reportes, estimación e histórico

### RF-18, RF-19
**Resultado observado:** Muestra la estimación de producción esperada y genera/descarga correctamente los archivos PDF y reportes solicitados.
**¿Cumple?** RF-18 Sí · RF-19 Sí

---

## 8. Resumen final

| RF | Pantalla | ¿Cumple? | Nota |
|---|---|---|---|
| RF-02 | Plantaciones y lotes | Sí | Registro de lote y detalle funcionando correctamente |
| RF-03 | Personal | Sí | Creación y asignación de personal a equipos operativa |
| RF-04 | Labores | Sí | Registro de avances de labores activo |
| RF-05 | Análisis IA | No | No hay pantalla ni botón separado; es el mismo análisis de imagen de RF-07/RF-08 |
| RF-07 | Análisis IA | Sí | Detección de plagas y enfermedades devuelve resultados |
| RF-08 | Análisis IA | Sí | Diagnóstico de deficiencias nutricionales devuelve resultados |
| RF-10 | Plantaciones y lotes | Parcial | Permite seleccionar entre opciones predefinidas pero no escribir texto libre |
| RF-12 | Alertas | Sí | Cambio de estado de alerta a "atendida" y visualización correctas |
| RF-13 | Mapa GPS | Sí | Registro de polinización operativo |
| RF-14 | Mapa GPS | Sí | Conteo de flores polinizadas georreferenciado disponible |
| RF-18 | Reportes | Sí | Visualización de estimación de producción habilitada |
| RF-19 | Reportes | Sí | Descarga de reportes (PDF/CSV) funcionando |
| RF-21 | Análisis IA | Sí | Clasificación de madurez del racimo devolviendo resultado |
| RF-26 | Labores | Sí | Planificación semanal y presupuestos mostrados en reportes |
| RF-28 | Labores | Sí | Registro de avance por unidad de labor operativo |
| RF-30 | Mapa GPS | No | No existe el botón/opción para reportar incidencias con evidencia fotográfica |
| RF-35 | Personal / Labores | Sí | Permite el registro delegado asignando la labor a otro trabajador |
| RF-36 | Labores | Sí | Catálogo codificado con tarifas por unidad presente |
| RF-37 | Labores | Sí | Liquidación semanal calculada y visible en Reportes |

**Conclusión:** De los 19 RF evaluados: 16 cumplen completamente, 1 cumple parcialmente (RF-10) y 2 no cumplen (RF-05 y RF-30).

**Nota:** los pasos y el "resultado esperado" salieron de leer el código del prototipo, no de haberlo probado antes. Lo único que vale es lo que se vea al ejecutarlo. RF-05 se corrigió el 21/09/2026 tras confirmar, al volver a mirar la aplicación, que no existe una pantalla separada de monitoreo fitosanitario.
