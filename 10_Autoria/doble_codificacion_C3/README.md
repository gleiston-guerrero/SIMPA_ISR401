# C3 — Doble codificación real (rehecha)

**Por qué existe esta carpeta.** Los archivos de `10_Autoria/doble_codificacion/` (`codificacion_allan.csv` y
`codificacion_josthyn.csv`) eran idénticos byte a byte, por lo que no constituyen doble codificación
independiente. Esa carpeta se conserva como historial; **el acuerdo vigente es el de esta carpeta.**

## Muestra congelada
- **45 fragmentos de 213 (21,1 %)**, elegidos **al azar sin reemplazo** con la **semilla 20260921**
  (`preparar_muestra_C3.py`, determinista y auditable).
- Los fragmentos están en `muestra_C3_fragmentos.csv` (ID, fragmento, cita literal, entrevista). **No incluye ningún código.**
- Libro de códigos usado: `07_Datos/libro_codigos.md` v1.0 (2026-09-20), publicado **antes** de las hojas de codificación.

## Reglas
1. Cada codificador trabaja solo con `hoja_codificacion_C3.xlsx` (lista desplegable de los 95 códigos).
2. No abre `codificacion.csv` ni el archivo de otra persona antes de subir el suyo.
3. Cada archivo `codificacion_C3_APELLIDO.xlsx` lo sube **su autor desde su propia cuenta de GitHub**; nadie más lo modifica.
4. No se vuelve a ejecutar `preparar_muestra_C3.py` una vez que alguien empezó a codificar.

## Cálculo
`python3 10_Autoria/doble_codificacion_C3/calcular_acuerdo_C3.py` compara cada par de codificadores y cada uno contra la
codificación original (`codificacion.csv`), con acuerdo observado, kappa de Cohen, IC 95 % por bootstrap (2000
remuestreos, semilla fija) y `desacuerdos_C3.csv`. Comprueba además que cada archivo tiene una sola cuenta de git y que
no coincide con la de otro archivo.

## Limitaciones
- 95 códigos y 45 fragmentos: el kappa es inestable; se reporta con su intervalo de confianza.
- El código original fue asignado por el equipo (`Analista_codificador` = VER/AVR) y luego se ajustaron citas con
  asistencia de Claude (declarado en `10_Autoria/declaracion_uso_ia.md`, sección 12); no se modificó ningún código.
- Los scripts y la hoja fueron preparados con asistencia de Claude; **los códigos de esta doble codificación los asigna
  cada codificador humano**, no una IA.
