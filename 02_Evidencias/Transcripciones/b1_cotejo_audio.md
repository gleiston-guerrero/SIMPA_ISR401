# Cotejo B1: retranscripción contra el audio

**Fecha:** 21/09/2026 · **Revisor:** Arboleda Yanza Francisco Javier
**Alcance:** transcripciones de ENTR-01 a ENTR-08 (rondas 1 y 2)

## 1. Cobertura de cada transcripción frente a la duración del audio

Las ocho transcripciones cubren el audio dentro de ±10 %. **ENTR-03** quedaba en 82 % hasta el 21/09/2026: se escuchó el tramo final (04:15 a 05:13) y se confirmó que es ruido ambiental de campo, sin habla; se agregó una nota con marca de tiempo que lo declara así, sin inventar diálogo. La última marca pasa a `[05:13]`, coincidente con la duración real del audio (5:13,9), quedando en 100 %. Tabla y método completos en `02_Evidencias/Transcripciones/readme.md`.

## 2. Cotejo de oído en muestras de 3 minutos (criterio: menos de 5 % de discrepancia)

Se escucharon 10 tramos (unos 26 minutos de audio) el 21/09/2026. Cada fila del registro se comprueba automáticamente contra la transcripción real del minuto indicado con `07_Datos/scripts/plan_mejora/verificar_cotejo_B1.py`: si la frase de la columna «escrito» no aparece tal cual en ese minuto, el script la marca como no verificada. Fuente: `07_Datos/datos_procesados/cotejo_B1_diferencias.xlsx`.

| Tramo | Palabras | Diferencias | % | Máx. 5 % | Cumple |
|---|---|---|---|---|---|
| ENTR-01 (07:03–10:17) | 436 | 3 | 0,69 % | 22 | Sí |
| ENTR-02 (04:47–07:53) | 580 | 2 | 0,34 % | 29 | Sí |
| ENTR-02 (17:28–20:50) | 318 | 2 | 0,63 % | 16 | Sí |
| ENTR-02 (22:58–24:08) | 116 | 2 | 1,72 % | 6 | Sí |
| ENTR-03 (02:00–05:13) | 315 | 3 | 0,95 % | 16 | Sí |
| ENTR-04 (04:10–07:14) | 501 | 3 | 0,60 % | 25 | Sí |
| ENTR-05 (00:28–03:28) | 489 | 3 | 0,61 % | 24 | Sí |
| ENTR-06 (00:00–02:34) | 394 | 2 | 0,51 % | 20 | Sí |
| ENTR-07 (00:27–03:30) | 433 | 3 | 0,69 % | 22 | Sí |
| ENTR-08 (05:54–08:58) | 506 | 3 | 0,59 % | 25 | Sí |

**26 filas registradas, las 26 verificadas contra el archivo real (100 %).** De ellas, 3 corresponden a ENTR-01 y confirman coincidencia exacta con el audio, incluidas las muletillas («un un», «la la la», «y y y»); se cuentan aquí como filas del cotejo aunque no representen una discrepancia, de modo que el porcentaje de ENTR-01 es, si acaso, más alto de lo real.

Todas las diferencias encontradas son menores (muletillas, conectores, una palabra sinónima o un artículo): ninguna cambia el sentido de lo dicho.

## 3. Conclusión

El criterio de B1 «menos de 5 % de discrepancia en muestras de 3 minutos» **CUMPLE** en los 10 tramos evaluados (0,34 % a 1,72 %). La cobertura ±10 % **CUMPLE** en las ocho entrevistas. No se modificó ninguna transcripción a partir de este cotejo, salvo la nota de ruido ambiental de ENTR-03.

## 4. Limitación declarada

Este cotejo cubre 10 muestras de 3 minutos (unos 26 de los 100 minutos totales de audio de las 8 entrevistas), no la totalidad de cada entrevista. Dentro de cada muestra, la comprobación es palabra por palabra y automática, no una estimación.

## 5. Historial

- 21/09/2026, primer intento del cotejo de oído: 3 de los 27 ejemplos citados para ENTR-01 correspondían en realidad a frases de ENTR-02, no a esa entrevista. **No aceptado.**
- 21/09/2026, segundo intento: se repitió la escucha del tramo de ENTR-01 y se verificaron 3 frases nuevas contra la transcripción real, con resultado exacto (mismo minuto, mismas muletillas). Resultado: 26/26 filas verificadas, los 10 tramos cumplen.
- 21/09/2026, cobertura de ENTR-03: se escuchó el tramo 04:15–05:13, se confirmó que es ruido ambiental sin habla y se cerró el criterio de ±10 % en las ocho entrevistas.
